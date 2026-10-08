#!/usr/bin/env python3
"""Create and manage quarantined Empire artifact handoffs for Codex."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any

REVIEW_SCRIPTS = Path(__file__).resolve().parents[2] / "empire-review" / "scripts"
PLUGIN_SCRIPTS = Path(__file__).resolve().parents[3] / "scripts"
if str(PLUGIN_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(PLUGIN_SCRIPTS))
if str(REVIEW_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(REVIEW_SCRIPTS))

import context_policy  # noqa: E402
import empire_present  # noqa: E402
import empire_router as router  # noqa: E402
from empire_budget import (  # noqa: E402
    BudgetError,
    BudgetStore,
    microusd_to_usd,
    pricing_snapshot_id,
    project_identity,
    usd_to_microusd,
)

SCHEMA_VERSION = "1.1"
DEFAULT_MAX_ARTIFACT_BYTES = 120_000
DEFAULT_MAX_OUTPUT_TOKENS = 8_000
MIN_FITTED_OUTPUT_TOKENS = 1_024
CONTINUATION_TAIL_CHARS = 4_000
MAX_CONTINUATION_IDS = 100
ROLES = {"partner", "worker"}
FORMATS = {"checklist", "single-file"}
ALLOWED_MEDIA_TYPES = {
    "application/javascript",
    "application/json",
    "application/typescript",
    "application/xml",
    "text/css",
    "text/csv",
    "text/html",
    "text/javascript",
    "text/markdown",
    "text/plain",
    "text/typescript",
    "text/xml",
}
REJECTED_ROOTS = {".agents", ".aws", ".codex", ".git", ".ssh"}


class HandoffError(Exception):
    pass


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def quarantine_root() -> Path:
    configured = os.environ.get("EMPIRE_HANDOFF_DIR")
    root = (
        Path(configured).expanduser()
        if configured
        else router.platform_data_dir() / "handoffs"
    ).resolve()
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    try:
        os.chmod(root, 0o700)
    except OSError:
        pass
    return root


def ensure_quarantine_outside(repo_root: Path) -> None:
    root = quarantine_root()
    try:
        root.relative_to(repo_root.resolve())
    except ValueError:
        return
    raise HandoffError("Empire quarantine must remain outside the active repository")


def handoff_dir(handoff_id: str) -> Path:
    if not re.fullmatch(r"[0-9a-f-]{36}", handoff_id):
        raise HandoffError("Invalid handoff ID")
    root = quarantine_root()
    path = (root / handoff_id).resolve()
    try:
        path.relative_to(root)
    except ValueError as exc:
        raise HandoffError("Handoff path escapes quarantine") from exc
    return path


def atomic_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(json.dumps(value, indent=2, sort_keys=True) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        os.chmod(path, 0o600)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def write_private(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
        handle.write(content)


def sha256_bytes(value: bytes) -> str:
    return "sha256:" + hashlib.sha256(value).hexdigest()


def evidence_hash(evidence: str) -> str:
    return sha256_bytes(evidence.encode("utf-8"))


def task_hash(task: str) -> str:
    return sha256_bytes(task.encode("utf-8"))


def openrouter_provider_slug(value: str) -> str:
    """Validate an exact OpenRouter provider slug without deriving one from a label."""
    slug = value.strip()
    segment = r"[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?"
    if len(slug) > 129 or not re.fullmatch(rf"{segment}(?:/{segment})?", slug):
        raise HandoffError("OpenRouter provider pin is not an exact provider slug")
    return slug


def validate_role_format(role: str, artifact_format: str) -> None:
    if role not in ROLES:
        raise HandoffError("Role must be partner or worker")
    if artifact_format not in FORMATS:
        raise HandoffError("Format must be checklist or single-file")
    if artifact_format == "checklist" and role != "partner":
        raise HandoffError("Checklist handoffs require the partner role")
    if artifact_format == "single-file" and role != "worker":
        raise HandoffError("Single-file handoffs require the worker role")


def normalize_suggested_path(value: str) -> str:
    raw = str(value or "").strip().replace("\\", "/")
    if not raw or raw.startswith("/") or re.match(r"^[A-Za-z]:/", raw):
        raise HandoffError("Suggested path must be repository-relative")
    pure = PurePosixPath(raw)
    if any(part in {"", ".", ".."} for part in pure.parts):
        raise HandoffError("Suggested path contains traversal or empty components")
    normalized = str(pure)
    if pure.parts[0].lower() in REJECTED_ROOTS:
        raise HandoffError("Suggested path targets a protected configuration directory")
    if router.is_sensitive_path(Path(normalized)):
        raise HandoffError("Suggested path targets a credential file")
    return normalized


def validate_destination_parent(repo_root: Path, suggested_path: str) -> None:
    parent = (repo_root / suggested_path).parent
    existing = parent
    while not existing.exists() and existing != repo_root:
        existing = existing.parent
    canonical = existing.resolve()
    try:
        canonical.relative_to(repo_root)
    except ValueError as exc:
        raise HandoffError(
            "Suggested destination parent resolves outside repository"
        ) from exc


def secret_findings(content: str) -> list[str]:
    labels = []
    for index, pattern in enumerate(router.SECRET_PATTERNS, start=1):
        if pattern.search(content):
            labels.append(f"generated_secret_pattern_{index}")
    return labels


def parse_structured_response(payload: dict[str, Any]) -> dict[str, Any]:
    try:
        choice = payload["choices"][0]
        message = choice["message"]
        content = message.get("parsed", message.get("content"))
    except (KeyError, IndexError, TypeError) as exc:
        raise HandoffError(
            "Provider response did not contain assistant content"
        ) from exc
    if isinstance(content, list):
        structured_blocks = [
            item.get("json")
            for item in content
            if isinstance(item, dict) and isinstance(item.get("json"), dict)
        ]
        content = (
            structured_blocks[0]
            if structured_blocks
            else "".join(
                str(item.get("text", "")) for item in content if isinstance(item, dict)
            )
        )
    if isinstance(content, dict):
        result = content
    else:
        text = str(content or "").strip()
        text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.I)
        text = re.sub(r"\s*```\s*$", "", text)
        try:
            result = json.loads(text)
        except json.JSONDecodeError as exc:
            decoder = json.JSONDecoder()
            result = None
            for match in re.finditer(r"\{", text):
                try:
                    candidate, _ = decoder.raw_decode(text, match.start())
                except json.JSONDecodeError:
                    continue
                if isinstance(candidate, dict) and isinstance(
                    candidate.get("artifact"), dict
                ):
                    result = candidate
                    break
            if result is None:
                raise HandoffError(
                    "Provider returned malformed structured artifact JSON"
                ) from exc
    if not isinstance(result, dict):
        raise HandoffError("Structured artifact response must be an object")
    artifact = result.get("artifact")
    if not isinstance(artifact, dict):
        raise HandoffError("Structured artifact response is missing artifact")
    if not isinstance(artifact.get("content"), str) or not artifact["content"]:
        raise HandoffError("Artifact content must be a non-empty string")
    if not isinstance(artifact.get("suggested_path"), str):
        raise HandoffError("Artifact suggested_path must be a string")
    if not isinstance(artifact.get("media_type"), str):
        raise HandoffError("Artifact media_type must be a string")
    for key in ("assumptions", "acceptance_checks"):
        if not isinstance(result.get(key, []), list) or not all(
            isinstance(item, str) for item in result.get(key, [])
        ):
            raise HandoffError(f"{key} must be a list of strings")
    return result


def recover_artifact_content(value: str) -> str:
    """Recover an artifact.content JSON string prefix without another model call."""
    match = re.search(r'"content"\s*:\s*"', value)
    if not match:
        return value.strip()
    start = match.end()
    escaped = False
    end = start
    closed = False
    while end < len(value):
        character = value[end]
        if escaped:
            escaped = False
        elif character == "\\":
            escaped = True
        elif character == '"':
            closed = True
            break
        end += 1
    raw = value[start:end]
    if escaped:
        raw = raw[:-1]
    try:
        return json.loads('"' + raw + '"')
    except json.JSONDecodeError:
        if closed:
            return raw
        return raw.replace(r"\n", "\n").replace(r"\"", '"').replace(r"\\", "\\")


def truncate_utf8(value: str, maximum_bytes: int) -> tuple[str, bool]:
    """Return a valid UTF-8 prefix and whether truncation was required."""
    if maximum_bytes <= 0:
        return "", bool(value)
    encoded = value.encode("utf-8")
    if len(encoded) <= maximum_bytes:
        return value, False
    return encoded[:maximum_bytes].decode("utf-8", errors="ignore"), True


def served_identity(completion: dict[str, Any]) -> dict[str, Any]:
    metadata = completion.get("openrouter_metadata")
    if not isinstance(metadata, dict):
        return {
            "served_model": "unavailable",
            "served_provider": "unavailable",
            "fallback_applied": False,
            "fallback_reason": None,
        }
    selected = None
    endpoints = metadata.get("endpoints")
    if isinstance(endpoints, dict):
        for candidate in endpoints.get("available", []):
            if isinstance(candidate, dict) and candidate.get("selected") is True:
                selected = candidate
                break
    served_model = (
        str(selected.get("model"))
        if isinstance(selected, dict) and selected.get("model")
        else "unavailable"
    )
    served_provider = (
        str(selected.get("provider"))
        if isinstance(selected, dict) and selected.get("provider")
        else "unavailable"
    )
    attempt = metadata.get("attempt")
    requested = metadata.get("requested")
    fallback = bool(
        (isinstance(attempt, int) and attempt > 1)
        or (served_model != "unavailable" and requested and served_model != requested)
        or metadata.get("strategy") == "fallback"
    )
    reason = metadata.get("summary") if fallback else None
    return {
        "served_model": served_model,
        "served_provider": served_provider,
        "fallback_applied": fallback,
        "fallback_reason": str(reason)[:500] if reason else None,
    }


def provider_pin(
    completion: dict[str, Any], route_provider: str, selected_provider: str
) -> dict[str, Any]:
    """Return only an exact provider pin proven by the configured route or metadata."""
    if route_provider == "direct":
        try:
            slug = router.provider_slug(selected_provider)
        except router.RouterError:
            return {"slug": None, "proven": False, "source": "unavailable"}
        return {"slug": slug, "proven": True, "source": "direct_provider_config"}
    metadata = completion.get("openrouter_metadata")
    endpoints = metadata.get("endpoints") if isinstance(metadata, dict) else None
    available = endpoints.get("available") if isinstance(endpoints, dict) else None
    if isinstance(available, list):
        for candidate in available:
            if not isinstance(candidate, dict) or candidate.get("selected") is not True:
                continue
            raw_slug = candidate.get("provider_slug") or candidate.get("slug")
            if not isinstance(raw_slug, str):
                break
            try:
                slug = openrouter_provider_slug(raw_slug)
            except HandoffError:
                break
            return {
                "slug": slug,
                "proven": True,
                "source": "openrouter_metadata",
            }
    return {"slug": None, "proven": False, "source": "unavailable"}


def task_score(
    candidates: list[dict[str, Any]], role: str, mode: str
) -> list[dict[str, Any]]:
    _, ranked = router.choose(candidates, mode)
    for candidate in ranked:
        dimensions = candidate["dimension_scores"]
        fit = (
            0.60 * dimensions["intelligence"] + 0.40 * dimensions["context"]
            if role == "partner"
            else 0.75 * dimensions["coding"] + 0.25 * dimensions["capability"]
        )
        candidate["handoff_fit_score"] = round(fit, 6)
        candidate["handoff_score"] = round(
            0.65 * candidate["route_score"] + 0.35 * fit, 6
        )
    return sorted(
        ranked,
        key=lambda item: (-item["handoff_score"], item["blended_price"], item["id"]),
    )


def artifact_prompt(
    task: str,
    role: str,
    artifact_format: str,
    suggested_path: str,
    media_type: str,
    evidence: str,
) -> dict[str, Any]:
    return {
        "task": task,
        "role": role,
        "authority": (
            "Propose one artifact only. You have no tools, filesystem access, approval "
            "authority, or implementation authority. Codex will independently verify the result."
        ),
        "artifact_request": {
            "format": artifact_format,
            "suggested_path": suggested_path,
            "media_type": media_type,
        },
        "requirements": {
            "return_json_only": True,
            "schema": {
                "artifact": {
                    "suggested_path": "repository-relative string",
                    "media_type": "text media type",
                    "content": "complete proposed file content",
                },
                "assumptions": ["string"],
                "acceptance_checks": ["string"],
            },
            "rules": [
                "Use only the supplied evidence",
                "Return exactly one textual artifact",
                "Do not include credentials or secret values",
                "Do not claim that any file was written or executed",
                "Keep the requested path and media type unchanged",
            ],
        },
        "repository_evidence": evidence or "[No diff or selected files supplied]",
    }


def handoff_response_format(suggested_path: str, media_type: str) -> dict[str, Any]:
    return {
        "type": "json_schema",
        "json_schema": {
            "name": "empire_handoff",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "artifact": {
                        "type": "object",
                        "properties": {
                            "suggested_path": {
                                "type": "string",
                                "const": suggested_path,
                            },
                            "media_type": {"type": "string", "const": media_type},
                            # Keep the provider schema inside the portable
                            # structured-output subset. Non-empty content is
                            # enforced locally after receipt.
                            "content": {"type": "string"},
                        },
                        "required": ["suggested_path", "media_type", "content"],
                        "additionalProperties": False,
                    },
                    "assumptions": {"type": "array", "items": {"type": "string"}},
                    "acceptance_checks": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                },
                "required": ["artifact", "assumptions", "acceptance_checks"],
                "additionalProperties": False,
            },
        },
    }


def add_supported_sampling_parameters(
    request_body: dict[str, Any], candidate: dict[str, Any]
) -> None:
    if "temperature" in candidate.get("supported_parameters", []):
        request_body["temperature"] = 0.1


def openrouter_handoff_request_body(
    candidate: dict[str, Any],
    prompt: dict[str, Any],
    max_output_tokens: int,
    requested_path: str,
    media_type: str,
) -> dict[str, Any]:
    """Build a strict handoff request from advertised route capabilities."""
    supported = set(candidate.get("supported_parameters") or [])
    body: dict[str, Any] = {
        "model": candidate.get("api_model_id", candidate["id"]),
        "messages": [{"role": "user", "content": json.dumps(prompt)}],
    }
    if "max_tokens" in supported:
        body["max_tokens"] = max_output_tokens
    elif "max_completion_tokens" in supported:
        body["max_completion_tokens"] = max_output_tokens
    else:
        raise HandoffError(
            "Selected model does not advertise an output-token limit parameter"
        )
    if not ({"response_format", "structured_outputs"} & supported):
        raise HandoffError(
            "Selected model does not advertise structured JSON output support"
        )
    body["response_format"] = handoff_response_format(requested_path, media_type)
    add_supported_sampling_parameters(body, candidate)
    # Response healing is an OpenRouter request plugin rather than a model
    # parameter. It is valid only alongside the structured response format.
    body["plugins"] = [{"id": "response-healing"}]
    return body


def fitted_output_tokens(
    candidate: dict[str, Any],
    evidence: str,
    requested_tokens: int,
    ceiling_microusd: int | None,
) -> int | None:
    """Fit output capacity under a hard ceiling without increasing that ceiling."""
    if requested_tokens <= 0:
        raise HandoffError("Maximum output tokens must be positive")
    if ceiling_microusd is None:
        return requested_tokens
    if (
        router.projected_cost_microusd(candidate, evidence, requested_tokens)
        <= ceiling_microusd
    ):
        return requested_tokens
    minimum = min(MIN_FITTED_OUTPUT_TOKENS, requested_tokens)
    if router.projected_cost_microusd(candidate, evidence, minimum) > ceiling_microusd:
        return None
    low, high = minimum, requested_tokens
    while low < high:
        middle = (low + high + 1) // 2
        if (
            router.projected_cost_microusd(candidate, evidence, middle)
            <= ceiling_microusd
        ):
            low = middle
        else:
            high = middle - 1
    return low


def normalize_artifact(
    response: dict[str, Any],
    artifact_format: str,
    requested_path: str,
    requested_media_type: str,
    max_artifact_bytes: int,
) -> tuple[str, str, str, list[str], list[str], list[str]]:
    artifact = response["artifact"]
    path = normalize_suggested_path(artifact["suggested_path"])
    media_type = artifact["media_type"].strip().lower().split(";", 1)[0]
    if path != requested_path:
        raise HandoffError("Provider changed the requested suggested path")
    if media_type != requested_media_type:
        raise HandoffError("Provider changed the requested media type")
    if media_type not in ALLOWED_MEDIA_TYPES:
        raise HandoffError("Artifact media type is not allowed")
    if artifact_format == "checklist" and media_type != "text/markdown":
        raise HandoffError("Checklist artifacts must use text/markdown")
    content = artifact["content"].replace("\r\n", "\n").replace("\r", "\n")
    if not content.strip():
        raise HandoffError("Artifact content must not be empty")
    if artifact_format == "checklist":
        content = router.normalize_markdown_tables(content)
    size = len(content.encode("utf-8"))
    if max_artifact_bytes <= 0 or size > max_artifact_bytes:
        raise HandoffError("Artifact exceeds the configured byte ceiling")
    findings = secret_findings(content)
    assumptions = [
        item.strip() for item in response.get("assumptions", []) if item.strip()
    ]
    checks = [
        item.strip() for item in response.get("acceptance_checks", []) if item.strip()
    ]
    return content, path, media_type, assumptions, checks, findings


def build_manifest(
    *,
    handoff_id: str,
    role: str,
    artifact_format: str,
    profile: str,
    requested_model: str | None,
    selected: dict[str, Any],
    selected_provider: str,
    identity: dict[str, Any],
    benchmark_source: str,
    evidence_manifest_hash: str,
    maximum_input_tokens: int,
    maximum_output_tokens: int,
    maximum_artifact_bytes: int,
    authorized_cost_usd: float | None,
    projected_cost_usd: float,
    observed_cost_usd: float,
    budget: dict[str, Any],
    assumptions: list[str],
    acceptance_checks: list[str],
    suggested_path: str,
    media_type: str,
    content: str,
    secret_labels: list[str],
) -> dict[str, Any]:
    encoded = content.encode("utf-8")
    warnings = ["Generated content matched a secret pattern"] if secret_labels else []
    validation = {
        "schema_valid": True,
        "paths_valid": True,
        "hashes_valid": True,
        "limits_valid": True,
        "secret_scan_valid": not secret_labels,
        "safe_to_preview": not secret_labels,
        "warnings": warnings,
    }
    return {
        "schema_version": SCHEMA_VERSION,
        "handoff_id": handoff_id,
        "created_at": utcnow(),
        "role": role,
        "format": artifact_format,
        "status": "quarantined" if not secret_labels else "blocked",
        "request": {
            "profile": profile,
            "requested_model": requested_model,
            "evidence_manifest_hash": evidence_manifest_hash,
            "input_evidence_persisted": False,
        },
        "route": {
            "selected_model": selected["id"],
            "selected_provider": selected_provider,
            **identity,
            "benchmark_source": benchmark_source,
            "selection_score": selected.get(
                "handoff_score", selected.get("route_score", 0.0)
            ),
            "selection_rationale": [
                f"Highest {profile} score for the {role} role among eligible models",
                "Structured text output required",
                "Explicit cost ceiling enforced before transport"
                if authorized_cost_usd is not None
                else "Calculated request reservation recorded before transport",
            ],
        },
        "limits": {
            "maximum_input_tokens": maximum_input_tokens,
            "maximum_output_tokens": maximum_output_tokens,
            "maximum_artifact_bytes": maximum_artifact_bytes,
            "maximum_file_count": 1,
            "authorized_cost_usd": authorized_cost_usd,
        },
        "cost": {
            "projected_cost_usd": projected_cost_usd,
            "observed_cost_usd": observed_cost_usd,
            "cost_basis": budget.get("cost_source", "provider_usage_calculation"),
            "budget_settled": budget.get("authorization") == "settled",
        },
        "assumptions": assumptions,
        "acceptance_checks": acceptance_checks,
        "files": [
            {
                "suggested_path": suggested_path,
                "media_type": media_type,
                "byte_length": len(encoded),
                "sha256": sha256_bytes(encoded),
            }
        ],
        "validation": validation,
    }


def store_handoff(manifest: dict[str, Any], content: str) -> Path:
    directory = handoff_dir(manifest["handoff_id"])
    if directory.exists():
        if (directory / "empire-handoff.json").exists() or (
            directory / "artifact.txt"
        ).exists():
            raise HandoffError("Handoff ID already exists")
    else:
        directory.mkdir(parents=True, mode=0o700)
    write_private(directory / "artifact.txt", content)
    atomic_json(directory / "empire-handoff.json", manifest)
    return directory


def load_manifest(handoff_id: str) -> tuple[Path, dict[str, Any]]:
    directory = handoff_dir(handoff_id)
    path = directory / "empire-handoff.json"
    if not path.is_file():
        raise HandoffError("Handoff was not found")
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise HandoffError("Handoff manifest is unreadable") from exc
    if manifest.get("handoff_id") != handoff_id:
        raise HandoffError("Handoff manifest identity mismatch")
    return directory, manifest


def revalidate(directory: Path, manifest: dict[str, Any]) -> str:
    artifact_path = directory / "artifact.txt"
    if not artifact_path.is_file():
        raise HandoffError("Quarantined artifact is missing")
    content = artifact_path.read_text(encoding="utf-8")
    file_info = manifest.get("files", [{}])[0]
    digest = sha256_bytes(content.encode("utf-8"))
    if digest != file_info.get("sha256"):
        raise HandoffError("Artifact hash mismatch")
    if len(content.encode("utf-8")) != file_info.get("byte_length"):
        raise HandoffError("Artifact byte length mismatch")
    if secret_findings(content):
        raise HandoffError("Generated secret prevents this action")
    if not manifest.get("validation", {}).get("safe_to_preview"):
        raise HandoffError("Handoff is not safe to preview")
    return content


def lifecycle_show(
    handoff_id: str, offset: int = 0, max_chars: int = router.RECOVERY_CHUNK_CHARS
) -> dict[str, Any]:
    if offset < 0 or max_chars <= 0 or max_chars > router.RECOVERY_CHUNK_CHARS:
        raise HandoffError(
            f"Preview chunks require offset >= 0 and max_chars <= {router.RECOVERY_CHUNK_CHARS}"
        )
    directory, manifest = load_manifest(handoff_id)
    content = revalidate(directory, manifest)
    chunk = content[offset : offset + max_chars]
    next_offset = offset + len(chunk)
    has_more = next_offset < len(content)
    return {
        "status": "preview",
        "manifest": manifest,
        "content": chunk,
        "chunk": {
            "offset": offset,
            "max_chars": max_chars,
            "returned_chars": len(chunk),
            "has_more": has_more,
            "next_offset": next_offset if has_more else None,
            "total_chars": len(content),
        },
    }


def lifecycle_approve(handoff_id: str) -> dict[str, Any]:
    directory, manifest = load_manifest(handoff_id)
    revalidate(directory, manifest)
    if manifest.get("status") not in {"quarantined", "approved_for_codex"}:
        raise HandoffError("Only a quarantined handoff can be approved")
    manifest["status"] = "approved_for_codex"
    manifest["approved_at"] = utcnow()
    manifest["approval_meaning"] = "Approved for Codex consideration; not applied"
    atomic_json(directory / "empire-handoff.json", manifest)
    return {
        "status": "approved_for_codex",
        "handoff_id": handoff_id,
        "repository_modified": False,
        "message": "Codex may independently implement, modify, partially use, or reject this proposal.",
    }


def lifecycle_reject(handoff_id: str) -> dict[str, Any]:
    directory, manifest = load_manifest(handoff_id)
    if manifest.get("status") == "approved_for_codex":
        raise HandoffError("An approved handoff cannot be silently changed to rejected")
    manifest["status"] = "rejected"
    manifest["rejected_at"] = utcnow()
    atomic_json(directory / "empire-handoff.json", manifest)
    return {
        "status": "rejected",
        "handoff_id": handoff_id,
        "repository_modified": False,
    }


def lifecycle_adversarial_review(handoff_id: str) -> dict[str, Any]:
    directory, manifest = load_manifest(handoff_id)
    revalidate(directory, manifest)
    review_id = str(uuid.uuid4())
    result = {
        "schema_version": "1.0",
        "review_id": review_id,
        "handoff_id": handoff_id,
        "artifact_sha256": manifest["files"][0]["sha256"],
        "created_at": utcnow(),
        "status": "ready_for_codex_adversarial_review",
        "original_artifact_mutated": False,
        "review_checks": [
            "Verify the proposal against the supplied project specification",
            "Check correctness, security, accessibility, and missing tests",
            "Identify assumptions that Codex should reject or revise",
        ],
    }
    path = directory / "adversarial-reviews" / f"{review_id}.json"
    atomic_json(path, result)
    return result


def lifecycle_download(
    handoff_id: str, destination_value: str, repo_value: str
) -> dict[str, Any]:
    directory, manifest = load_manifest(handoff_id)
    content = revalidate(directory, manifest)
    repo = Path(repo_value).expanduser().resolve()
    root = Path(router.git(repo, "rev-parse", "--show-toplevel").strip()).resolve()
    expected_project_id = manifest.get("request", {}).get("project_id")
    actual_project_id, _ = project_identity(root)
    if expected_project_id and expected_project_id != actual_project_id:
        raise HandoffError("Download repository does not match the handoff project")
    destination = Path(destination_value).expanduser().resolve()
    try:
        destination.relative_to(root)
    except ValueError:
        pass
    else:
        raise HandoffError(
            "Download destination must remain outside the active repository"
        )
    if destination.exists() and destination.is_dir():
        destination = destination / Path(manifest["files"][0]["suggested_path"]).name
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        raise HandoffError("Download destination already exists")
    write_private(destination, content)
    return {
        "status": "downloaded",
        "handoff_id": handoff_id,
        "path": str(destination),
        "sha256": manifest["files"][0]["sha256"],
        "repository_modified": False,
    }


def continuation_prompt(
    *,
    missing_task: str,
    parent_handoff_id: str,
    parent_task_hash: str,
    evidence_manifest_hash: str,
    partial_response_hash: str,
    partial_tail: str,
    completed_ids: list[str],
) -> dict[str, Any]:
    """Build a bounded same-artifact continuation prompt without dispatching it."""
    return {
        "task": "Continue only the missing work; do not repeat completed material.",
        "missing_deliverables": missing_task,
        "authority": (
            "You have no tools, filesystem access, approval authority, or "
            "implementation authority. Codex will independently verify the result."
        ),
        "continuation": {
            "parent_handoff_id": parent_handoff_id,
            "original_task_hash": parent_task_hash,
            "evidence_manifest_hash": evidence_manifest_hash,
            "partial_response_hash": partial_response_hash,
            "completed_ids": completed_ids,
            "partial_response_tail": partial_tail,
        },
        "rules": [
            "Return only missing sections or findings",
            "Do not repeat completed material",
            "Use only the recollected allowlisted repository evidence",
            "Do not include credentials or secret values",
            "Do not claim that any file was written or executed",
        ],
    }


def _continuation_ids(values: list[str]) -> list[str]:
    if len(values) > MAX_CONTINUATION_IDS:
        raise HandoffError(
            f"At most {MAX_CONTINUATION_IDS} completed section or finding IDs may be supplied"
        )
    normalized: list[str] = []
    seen: set[str] = set()
    for value in values:
        item = router.validate_external_text(
            "Completed section or finding ID", value, max_chars=200
        )
        if item in seen:
            continue
        seen.add(item)
        normalized.append(item)
    return normalized


def continuation_plan(args: argparse.Namespace) -> dict[str, Any]:
    """Create a no-dispatch authorization plan for one partial handoff."""
    directory, manifest = load_manifest(args.handoff_id)
    completion = manifest.get("completion")
    continuation = manifest.get("continuation")
    if not isinstance(completion, dict) or not isinstance(continuation, dict):
        raise HandoffError("Handoff predates the continuation receipt contract")
    if (
        completion.get("state") != "partial_recoverable"
        or continuation.get("eligible") is not True
    ):
        raise HandoffError(
            "Only a partial_recoverable handoff is continuation eligible"
        )
    billing = manifest.get("billing")
    if not isinstance(billing, dict):
        raise HandoffError("Handoff billing state is unavailable")
    if (
        billing.get("state") == "pending_reconciliation"
        or billing.get("gross_provider_cost_usd") is None
    ):
        raise HandoffError(
            "Continuation is blocked until the parent billing outcome is reconciled"
        )

    content = revalidate(directory, manifest)
    missing_task = router.validate_external_text(
        "Missing continuation work",
        args.task,
        max_chars=router.MAX_EXTERNAL_TASK_CHARS,
    )
    completed_ids = _continuation_ids(args.completed_id)
    evidence, repo_meta = router.collect_evidence(args.repo, args.file, args.max_bytes)
    repository_root = Path(repo_meta["repository_root"]).resolve()
    expected_project_id = manifest.get("request", {}).get("project_id")
    actual_project_id, _ = project_identity(repository_root)
    if not expected_project_id or expected_project_id != actual_project_id:
        raise HandoffError("Continuation repository does not match the parent project")
    current_evidence_hash = evidence_hash(evidence)
    expected_evidence_hash = manifest.get("request", {}).get("evidence_manifest_hash")
    if not expected_evidence_hash or current_evidence_hash != expected_evidence_hash:
        raise HandoffError(
            "Continuation evidence differs from the parent allowlisted evidence boundary"
        )

    parent_task_hash = manifest.get("request", {}).get("task_hash")
    partial_response_hash = completion.get("response_sha256")
    blockers: list[str] = []
    if not isinstance(parent_task_hash, str) or not parent_task_hash.startswith(
        "sha256:"
    ):
        parent_task_hash = "unavailable"
        blockers.append("parent_task_hash_unavailable")
    if not isinstance(
        partial_response_hash, str
    ) or not partial_response_hash.startswith("sha256:"):
        raise HandoffError("Parent partial response hash is unavailable")
    route = manifest.get("route")
    if not isinstance(route, dict):
        raise HandoffError("Parent route receipt is unavailable")
    pin = route.get("provider_pin")
    if (
        not isinstance(pin, dict)
        or pin.get("proven") is not True
        or not pin.get("slug")
    ):
        blockers.append("exact_provider_pin_unavailable")
    if route.get("served_model") in {None, "", "unavailable"}:
        blockers.append("served_model_identity_unavailable")

    partial_tail = content[-CONTINUATION_TAIL_CHARS:]
    prompt = continuation_prompt(
        missing_task=missing_task,
        parent_handoff_id=args.handoff_id,
        parent_task_hash=parent_task_hash,
        evidence_manifest_hash=current_evidence_hash,
        partial_response_hash=partial_response_hash,
        partial_tail=partial_tail,
        completed_ids=completed_ids,
    )
    prompt_digest = sha256_bytes(
        json.dumps(prompt, sort_keys=True, separators=(",", ":")).encode("utf-8")
    )
    plan_id = (
        "continuation-"
        + hashlib.sha256(
            (args.handoff_id + "\0" + prompt_digest).encode("utf-8")
        ).hexdigest()[:24]
    )

    cost = manifest.get("cost")
    if not isinstance(cost, dict):
        raise HandoffError("Parent cost receipt is unavailable")
    try:
        prior_observed_microusd = usd_to_microusd(cost.get("observed_cost_usd"))
        incremental_estimate_microusd = usd_to_microusd(cost.get("projected_cost_usd"))
    except BudgetError as exc:
        raise HandoffError("Parent cost receipt is invalid") from exc
    cumulative_estimate_microusd = (
        prior_observed_microusd + incremental_estimate_microusd
    )
    status = "continuation_plan_blocked" if blockers else "continuation_plan_ready"
    return {
        "status": status,
        "handoff_id": args.handoff_id,
        "continuation_plan": {
            "schema_version": "1.0",
            "plan_id": plan_id,
            "parent_handoff_id": args.handoff_id,
            "attempt": 1,
            "maximum_attempts": 1,
            "original_task_hash": parent_task_hash,
            "missing_task_hash": task_hash(missing_task),
            "evidence_manifest_hash": current_evidence_hash,
            "partial_response_hash": partial_response_hash,
            "prompt_hash": prompt_digest,
            "completed_ids": completed_ids,
            "partial_tail_chars": len(partial_tail),
            "same_model_required": True,
            "same_provider_required": True,
            "selected_model": route.get("selected_model"),
            "served_model": route.get("served_model"),
            "served_provider": route.get("served_provider"),
            "provider_pin": pin
            if isinstance(pin, dict)
            else {"slug": None, "proven": False, "source": "unavailable"},
            "dispatch_ready": not blockers,
            "dispatch_blockers": blockers,
        },
        "authorization": {
            "state": "required",
            "incremental_estimated_max_usd": microusd_to_usd(
                incremental_estimate_microusd
            ),
            "cumulative_observed_before_usd": microusd_to_usd(prior_observed_microusd),
            "minimum_disclosed_cumulative_ceiling_usd": microusd_to_usd(
                cumulative_estimate_microusd
            ),
            "estimate_basis": "parent_receipt_projected_maximum",
            "current_pricing_refresh_required_before_dispatch": True,
        },
        "provider_dispatch_performed": False,
        "budget_reserved": False,
        "repository_modified": False,
        "next_action": (
            "Resolve every dispatch blocker, refresh current pricing, and obtain "
            "explicit incremental and cumulative cost authorization before adding "
            "or invoking continuation transport."
        ),
    }


def generation_result(
    args: argparse.Namespace,
    completion: dict[str, Any],
    response_capture: dict[str, Any],
    selected: dict[str, Any],
    route_provider: str,
    evidence: str,
    repo_meta: dict[str, Any],
    endpoint_generated_at: str,
    aa_available: bool,
    observed_microusd: int,
    budget_after: dict[str, Any],
    cost_source: str,
    billing_pending: bool = False,
    billing_state: str = "confirmed",
) -> dict[str, Any]:
    validate_role_format(args.role, args.format)
    requested_path = normalize_suggested_path(args.suggested_path)
    repo_root = Path(repo_meta["repository_root"]).resolve()
    validate_destination_parent(repo_root, requested_path)
    media_type = args.media_type.strip().lower().split(";", 1)[0]
    validation_error: str | None = None
    schema_valid = False
    limits_valid = True
    raw_content = response_capture["content"]
    try:
        parsed = parse_structured_response(completion)
        content, path, media, assumptions, checks, secrets = normalize_artifact(
            parsed, args.format, requested_path, media_type, args.max_artifact_bytes
        )
        schema_valid = True
    except HandoffError as exc:
        validation_error = str(exc)
        content = recover_artifact_content(raw_content)
        content = content.replace("\r\n", "\n").replace("\r", "\n")
        if args.format == "checklist":
            content = router.normalize_markdown_tables(content)
        path = requested_path
        media = media_type
        assumptions = []
        checks = []
        secrets = secret_findings(content)
        content, truncated_for_limit = truncate_utf8(content, args.max_artifact_bytes)
        limits_valid = not truncated_for_limit
    identity = (
        served_identity(completion)
        if route_provider == "openrouter"
        else {
            "served_model": str(completion.get("model") or "unavailable"),
            "served_provider": str(completion.get("provider") or "unavailable"),
            "fallback_applied": False,
            "fallback_reason": None,
        }
    )
    project_id, _ = project_identity(repo_root)
    observed_cost = microusd_to_usd(observed_microusd) or 0.0
    budget_payload = {
        **budget_after,
        "authorization": billing_state
        if billing_pending or billing_state == "settled_overrun"
        else "settled",
        "cost_source": cost_source,
    }
    manifest = build_manifest(
        handoff_id=response_capture["response_id"],
        role=args.role,
        artifact_format=args.format,
        profile=args.mode,
        requested_model=args.model,
        selected=selected,
        selected_provider=route_provider
        if route_provider == "openrouter"
        else selected["provider"],
        identity=identity,
        benchmark_source="artificial-analysis" if aa_available else "unavailable",
        evidence_manifest_hash=evidence_hash(evidence),
        maximum_input_tokens=max(1, args.max_bytes // 4 + 750),
        maximum_output_tokens=selected.get(
            "authorized_max_output_tokens", args.max_output_tokens
        ),
        maximum_artifact_bytes=args.max_artifact_bytes,
        authorized_cost_usd=float(args.max_authorized_cost)
        if args.max_authorized_cost is not None
        else None,
        projected_cost_usd=selected["projected_max_cost_usd"],
        observed_cost_usd=observed_cost,
        budget=budget_payload,
        assumptions=assumptions,
        acceptance_checks=checks,
        suggested_path=path,
        media_type=media,
        content=content,
        secret_labels=secrets,
    )
    manifest["request"]["project_id"] = project_id
    manifest["request"]["task_hash"] = task_hash(args.task)
    manifest["route"]["price_snapshot_id"] = pricing_snapshot_id(
        selected, endpoint_generated_at
    )
    manifest["route"]["provider_pin"] = provider_pin(
        completion,
        route_provider,
        route_provider
        if route_provider == "openrouter"
        else str(selected.get("provider") or route_provider),
    )
    manifest["route"].update(
        {
            "projected_maximum_usd": selected["projected_max_cost_usd"],
            "local_authorization_usd": selected["projected_max_cost_usd"],
            "provider_enforced_total_ceiling_usd": None,
            "provider_generation_id": response_capture["receipt"].get(
                "provider_generation_id"
            ),
            "provider_request_id": response_capture["receipt"].get(
                "provider_request_id"
            ),
        }
    )
    finish_reason = response_capture["receipt"].get("finish_reason")
    generation_state = response_capture["receipt"].get("generation_state")
    if generation_state == "blocked":
        completion_state = "blocked_provider_safety"
    elif secrets:
        completion_state = "blocked_sensitive"
    elif not content:
        completion_state = "failed_empty"
    elif generation_state in {"partial", "ambiguous"}:
        completion_state = "partial_recoverable"
    elif not limits_valid:
        completion_state = "partial_recoverable"
    elif not schema_valid:
        completion_state = "completed_degraded"
    else:
        completion_state = "completed"
    if completion_state != "completed" and not secrets:
        manifest["status"] = completion_state
    manifest["validation"].update(
        {
            "schema_valid": schema_valid,
            "limits_valid": limits_valid,
            "safe_to_preview": bool(content)
            and not secrets
            and limits_valid
            and generation_state != "blocked",
            "error": validation_error,
            "durable_before_validation": True,
        }
    )
    manifest["completion"] = {
        "state": completion_state,
        "finish_reason": finish_reason,
        "terminal_reason": response_capture["receipt"].get("terminal_reason"),
        "provider_error_type": response_capture["receipt"].get("provider_error_type"),
        "generation_state": generation_state,
        "durable_response_bytes": response_capture["receipt"]["durable_response_bytes"],
        "response_sha256": response_capture["receipt"]["response_sha256"],
        "schema_valid": schema_valid,
        "content_complete": response_capture["receipt"].get("content_complete", False),
    }
    manifest["continuation"] = {
        "eligible": completion_state == "partial_recoverable",
        "authorization": "ask",
        "attempt": 0,
        "maximum_automatic_attempts": 0,
        "automatic_continuation_started": False,
    }
    manifest["billing"] = {
        "gross_provider_cost_usd": None if billing_pending else observed_cost,
        "user_billable_cost_usd": None if billing_pending else observed_cost,
        "state": billing_state,
        "delivery_receipted": bool(raw_content),
        "compensation_status": "pending_reconciliation"
        if billing_pending and not raw_content
        else "compensation_pending"
        if observed_cost > 0 and not raw_content
        else "compensation_not_required",
    }
    store_handoff(manifest, content)
    research_artifact = router.finalize_provider_response(
        response_capture,
        state=completion_state,
        schema_valid=schema_valid,
        observed_cost_usd=observed_cost,
        billing_state=billing_state,
    )
    contributors = router.contributor_badges(
        selected,
        synthesis_available=bool(content) and not secrets,
    )
    web_sources = router.completion_web_sources(completion)
    served_provider = identity.get("served_provider")
    if served_provider == "unavailable":
        served_provider = None
    response_footnote = router.response_provenance_footnote(
        contributors,
        selected=selected,
        route_provider=route_provider,
        served_provider=served_provider,
        artificial_analysis_used=bool(
            aa_available and selected.get("benchmark_matched")
        ),
        artificial_analysis={
            "status": "available" if aa_available else "unavailable",
            "source": "Artificial Analysis" if aa_available else None,
        },
        web_sources=web_sources,
    )
    return {
        "status": manifest["status"],
        "handoff_id": manifest["handoff_id"],
        "manifest": manifest,
        "contributors": contributors,
        "contributor_footnote": router.contributor_footnote(contributors),
        "synthesis_footnote": router.synthesis_model_footnote(contributors),
        "model_syntheses": router.model_syntheses(
            contributors,
            research_artifact
            if completion_state in {"partial_recoverable", "completed_degraded"}
            else None,
        ),
        "research_artifact": research_artifact,
        "continuation": manifest["continuation"],
        "response_footnote": response_footnote,
        "web_research": {
            "used": bool(web_sources),
            "sources": web_sources,
            "citation_renderer": "native_codex_preferred",
        },
        "quarantine_path": str(handoff_dir(manifest["handoff_id"])),
        "repository_modified": False,
    }


def generate(args: argparse.Namespace) -> dict[str, Any]:
    validate_role_format(args.role, args.format)
    args.task = router.validate_external_text(
        "Handoff task", args.task, max_chars=router.MAX_EXTERNAL_TASK_CHARS
    )
    requested_path = normalize_suggested_path(args.suggested_path)
    media_type = args.media_type.strip().lower().split(";", 1)[0]
    if media_type not in ALLOWED_MEDIA_TYPES:
        raise HandoffError("Artifact media type is not allowed")
    if args.format == "checklist" and media_type != "text/markdown":
        raise HandoffError("Checklist artifacts must use text/markdown")
    evidence, repo_meta = router.collect_evidence(args.repo, args.file, args.max_bytes)
    repository_root = Path(repo_meta["repository_root"])
    ensure_quarantine_outside(repository_root)
    validate_destination_parent(repository_root, requested_path)
    fixture_dir = Path(args.fixtures).resolve() if args.fixtures else None
    settings: dict[str, Any] = {}
    route_provider = "openrouter"
    direct_key = None
    direct_config: dict[str, Any] | None = None
    catalog_refreshed_live = False
    if fixture_dir:
        openrouter_key = None
        endpoint = router.build_model_endpoint(
            router.fixture(fixture_dir, "openrouter-models.json"),
            router.fixture(fixture_dir, "artificial-analysis-models.json"),
            "offline_fixture",
            True,
        )
        aa_available = True
        completion = router.fixture(
            fixture_dir, f"handoff-{args.format}-completion.json"
        )
    else:
        openrouter_key, openrouter_source = router.resolve_credential(
            ("OPENROUTER_API_KEY",), "openrouter"
        )
        settings = router.load_settings()
        route_provider = (
            settings.get("inference_provider", "openrouter")
            if args.provider == "auto"
            else args.provider
        )
        if route_provider == "openrouter" and not openrouter_key:
            raise HandoffError(
                router.credential_required_message(
                    "OpenRouter", openrouter_source, "use $empire-settings"
                )
            )
        require_live_catalog = bool(
            getattr(args, "require_live_catalog", False)
            or router.task_requests_live_catalog(args.task)
        )
        if route_provider == "openrouter" and require_live_catalog:
            endpoint = router.refresh_model_endpoint()
            catalog_refreshed_live = True
        else:
            endpoint, _ = router.resolve_model_endpoint(
                require_benchmarks=args.require_benchmarks
            )
        aa_available = (
            endpoint.get("sources", {}).get("artificial_analysis", {}).get("status")
            == "available"
        )
        if args.require_benchmarks and not aa_available:
            raise HandoffError("Artificial Analysis benchmark evidence is unavailable")
        if route_provider == "direct":
            _, direct_config = router.configured_direct_provider(settings)
            if not isinstance(direct_config, dict):
                raise HandoffError("No direct provider is configured")
            direct_key, direct_source = router.resolve_credential(
                ("EMPIRE_PROVIDER_API_KEY",),
                router.provider_account(
                    router.provider_slug(str(direct_config.get("name", "")))
                ),
            )
            if not direct_key:
                raise HandoffError(
                    router.credential_required_message(
                        "Direct-provider", direct_source, "use $empire-settings"
                    )
                )
    if route_provider == "direct" and not fixture_dir:
        if direct_config is None:
            raise HandoffError("No direct provider is configured")
        catalog = [router.direct_provider_candidate(direct_config, endpoint)]
    else:
        catalog = [dict(item) for item in endpoint["eligible_models"]]
    if route_provider == "openrouter" and not fixture_dir:
        catalog = [item for item in catalog if item.get("supports_strict_json")]
    ceiling = (
        usd_to_microusd(args.max_authorized_cost)
        if args.max_authorized_cost is not None
        else None
    )
    for candidate in catalog:
        fitted_tokens = (
            fitted_output_tokens(candidate, evidence, args.max_output_tokens, ceiling)
            if getattr(args, "fit_output_to_cost_ceiling", False)
            else args.max_output_tokens
        )
        candidate["authorized_max_output_tokens"] = fitted_tokens
        candidate["projected_max_cost_microusd"] = (
            router.projected_cost_microusd(candidate, evidence, fitted_tokens)
            if fitted_tokens is not None
            else None
        )
        candidate["projected_max_cost_usd"] = microusd_to_usd(
            candidate["projected_max_cost_microusd"]
        )
    candidates = (
        list(catalog)
        if ceiling is None
        else [
            item
            for item in catalog
            if item["projected_max_cost_microusd"] is not None
            and item["projected_max_cost_microusd"] <= ceiling
        ]
    )
    if args.model:
        candidates = [item for item in candidates if item["id"] == args.model]
        if (
            not candidates
            and route_provider == "openrouter"
            and not fixture_dir
            and not catalog_refreshed_live
        ):
            endpoint = router.refresh_model_endpoint()
            catalog_refreshed_live = True
            aa_available = (
                endpoint.get("sources", {}).get("artificial_analysis", {}).get("status")
                == "available"
            )
            catalog = [
                dict(item)
                for item in endpoint["eligible_models"]
                if item.get("supports_strict_json")
            ]
            for candidate in catalog:
                fitted_tokens = (
                    fitted_output_tokens(
                        candidate, evidence, args.max_output_tokens, ceiling
                    )
                    if getattr(args, "fit_output_to_cost_ceiling", False)
                    else args.max_output_tokens
                )
                candidate["authorized_max_output_tokens"] = fitted_tokens
                candidate["projected_max_cost_microusd"] = (
                    router.projected_cost_microusd(candidate, evidence, fitted_tokens)
                    if fitted_tokens is not None
                    else None
                )
                candidate["projected_max_cost_usd"] = microusd_to_usd(
                    candidate["projected_max_cost_microusd"]
                )
            candidates = [
                item
                for item in catalog
                if item["id"] == args.model
                and item["projected_max_cost_microusd"] is not None
                and (ceiling is None or item["projected_max_cost_microusd"] <= ceiling)
            ]
        if not candidates:
            raise HandoffError(
                "Requested model is unavailable or exceeds the cost ceiling"
            )
    if not candidates:
        raise HandoffError("No eligible handoff route fits the authorized cost ceiling")
    ranked = task_score(candidates, args.role, args.mode)
    selected = ranked[0]
    prompt = artifact_prompt(
        args.task, args.role, args.format, requested_path, media_type, evidence
    )
    try:
        context_preflight = context_policy.build_preflight_receipt(
            workflow="handoff",
            request_text=json.dumps(prompt, separators=(",", ":"), ensure_ascii=False),
            requested_output_tokens=selected.get(
                "authorized_max_output_tokens", args.max_output_tokens
            ),
            provider_output_limit=None,
            output_limit_supported=bool(
                route_provider == "direct" or selected.get("supports_output_limit")
            ),
            context_limit_tokens=getattr(args, "codex_context_limit_tokens", None),
            current_usage_tokens=getattr(args, "codex_context_used_tokens", None),
            requested_class=getattr(args, "response_class", "automatic"),
        )
    except context_policy.ContextPolicyError as exc:
        raise HandoffError(f"Invalid context preflight: {exc}") from exc
    project_id, project_name = project_identity(repo_meta["repository_root"])
    response_capture = router.prepare_provider_response(
        kind="handoff",
        root=quarantine_root(),
    )
    snapshot = pricing_snapshot_id(selected, endpoint.get("generated_at"))
    with BudgetStore() as store:
        reservation_id, budget_before = store.reserve(
            project_id,
            project_name,
            route_provider if route_provider == "openrouter" else selected["provider"],
            selected["id"],
            selected["projected_max_cost_microusd"],
            snapshot,
            ttl_seconds=max(300, args.timeout * 2),
        )
    if reservation_id is None:
        denied_receipt = dict(response_capture["receipt"])
        denied_receipt.update(
            {
                "state": "not_dispatched_budget_denied",
                "generation_state": "not_dispatched",
                "billing_state": "released",
                "finalized_at": utcnow(),
            }
        )
        router._atomic_private_json(response_capture["receipt_path"], denied_receipt)
        return {
            "status": "codex_only",
            "reason": "project_budget_exhausted",
            "budget": budget_before,
            "context_preflight": context_preflight,
            "repository_modified": False,
        }
    dispatch_started = False
    provider_outcome_proven_nonbillable = False
    provider_generation_id: str | None = None
    provider_request_id: str | None = None
    provider_error_status: int | None = None
    provider_error_category: str | None = None
    started = time.monotonic()
    try:
        if not fixture_dir:
            endpoint_url = (
                selected["endpoint"]
                if route_provider == "direct"
                else router.OPENROUTER_CHAT
            )
            authorized_output_tokens = selected.get(
                "authorized_max_output_tokens", args.max_output_tokens
            )
            if route_provider == "openrouter":
                request_body = openrouter_handoff_request_body(
                    selected,
                    prompt,
                    authorized_output_tokens,
                    requested_path,
                    media_type,
                )
                request_body["provider"] = router.openrouter_provider_policy(
                    "frontier_quality",
                    require_zdr=getattr(args, "require_zdr", False),
                )
            else:
                request_body = {
                    "model": selected.get("api_model_id", selected["id"]),
                    "messages": [{"role": "user", "content": json.dumps(prompt)}],
                    "max_tokens": authorized_output_tokens,
                    "response_format": {"type": "json_object"},
                    "temperature": 0.1,
                }
            with BudgetStore() as store:
                store.mark_dispatched(reservation_id)
            router.mark_response_dispatched(response_capture, reservation_id)
            dispatch_started = True
            try:
                completion = router.request_json(
                    endpoint_url,
                    api_key=direct_key
                    if route_provider == "direct"
                    else openrouter_key,
                    headers={"X-OpenRouter-Metadata": "enabled"}
                    if route_provider == "openrouter"
                    else None,
                    body=request_body,
                    timeout=args.timeout,
                )
            except router.ProviderRequestError as exc:
                provider_generation_id = exc.provider_generation_id
                provider_request_id = exc.provider_request_id
                provider_error_status = exc.status_code
                provider_error_category = router.provider_failure_category(
                    exc.status_code, exc.provider_message
                )
                provider_outcome_proven_nonbillable = router.outcome_proven_nonbillable(
                    route_provider, exc.status_code
                )
                raise
            # Capture returned content before any fallible billing metadata write.
        provider_references = router.provider_reference_data(
            completion, route_provider=route_provider
        )
        provider_generation_id = provider_references["provider_generation_id"]
        provider_request_id = provider_references["provider_request_id"]
        response_capture = router.capture_provider_response(
            completion,
            kind="handoff",
            prepared=response_capture,
            route_provider=route_provider,
        )
        observed_value, cost_source = router.observed_usage_cost(
            completion,
            selected,
            route_provider=route_provider,
        )
        billing_pending = observed_value is None
        observed_microusd = observed_value or 0
        billing_state = router.response_billing_state(
            observed_microusd,
            selected["projected_max_cost_microusd"],
            pending=billing_pending,
        )
        with BudgetStore() as store:
            store.record_provider_references(
                reservation_id,
                provider_generation_id=provider_generation_id,
                provider_request_id=provider_request_id,
            )
            if billing_pending:
                store.mark_pending(
                    reservation_id,
                    cost_source,
                    provider_request_id=provider_request_id,
                    provider_generation_id=provider_generation_id,
                )
                budget_after = store.status(project_id, project_name)
            else:
                budget_after = store.settle(
                    reservation_id,
                    observed_microusd,
                    model_id=selected["id"],
                    price_snapshot_id=snapshot,
                )
        result = generation_result(
            args,
            completion,
            response_capture,
            selected,
            route_provider,
            evidence,
            repo_meta,
            endpoint.get("generated_at", "unavailable"),
            aa_available,
            observed_microusd,
            budget_after,
            cost_source,
            billing_pending,
            billing_state,
        )
        result["latency_ms"] = round((time.monotonic() - started) * 1000)
        result["context_preflight"] = context_preflight
        return result
    except router.AmbiguousProviderOutcome as exc:
        provider_generation_id = exc.provider_generation_id or provider_generation_id
        provider_request_id = exc.provider_request_id or provider_request_id
        with BudgetStore() as store:
            store.mark_pending(
                reservation_id,
                "transport_ended_without_proven_provider_outcome",
                provider_request_id=provider_request_id,
                provider_generation_id=provider_generation_id,
            )
        failed_receipt = dict(response_capture["receipt"])
        failed_receipt.update(
            {
                "state": "failed_ambiguous_provider_outcome",
                "generation_state": "ambiguous",
                "billing_state": "pending_reconciliation",
                "provider_generation_id": provider_generation_id,
                "provider_request_id": provider_request_id,
                "finalized_at": datetime.now(timezone.utc).isoformat(),
            }
        )
        router._atomic_private_json(response_capture["receipt_path"], failed_receipt)
        raise
    except Exception:
        with BudgetStore() as store:
            if dispatch_started and not provider_outcome_proven_nonbillable:
                store.mark_pending(
                    reservation_id,
                    "post_dispatch_processing_or_provider_outcome_ambiguous",
                    provider_request_id=provider_request_id,
                    provider_generation_id=provider_generation_id,
                )
                billing_state = "pending_reconciliation"
            else:
                try:
                    store.record_provider_references(
                        reservation_id,
                        provider_generation_id=provider_generation_id,
                        provider_request_id=provider_request_id,
                    )
                except BudgetError:
                    store.mark_pending(
                        reservation_id,
                        "provider_reference_conflict_requires_reconciliation",
                        provider_request_id=provider_request_id,
                        provider_generation_id=provider_generation_id,
                    )
                    billing_state = "pending_reconciliation"
                else:
                    store.release(reservation_id)
                    billing_state = "released"
        failed_receipt = dict(response_capture["receipt"])
        failed_receipt.update(
            {
                "state": "failed_provider_request"
                if provider_error_status is not None
                else "failed_post_dispatch",
                "generation_state": response_capture["receipt"].get("generation_state", "failed")
                if response_capture.get("content") else "failed",
                "billing_state": billing_state,
                "provider_error_status": provider_error_status,
                "provider_error_category": provider_error_category,
                "provider_generation_id": provider_generation_id,
                "provider_request_id": provider_request_id,
                "finalized_at": datetime.now(timezone.utc).isoformat(),
            }
        )
        router._atomic_private_json(response_capture["receipt_path"], failed_receipt)
        raise


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    empire_present.add_view_argument(root)
    sub = root.add_subparsers(dest="command", required=True)
    generate_parser = sub.add_parser(
        "generate", help="Generate one quarantined handoff"
    )
    generate_parser.add_argument("--task", required=True)
    generate_parser.add_argument("--role", choices=sorted(ROLES), required=True)
    generate_parser.add_argument("--format", choices=sorted(FORMATS), required=True)
    generate_parser.add_argument("--suggested-path", required=True)
    generate_parser.add_argument("--media-type", required=True)
    generate_parser.add_argument("--repo", default=".")
    generate_parser.add_argument("--file", action="append", default=[])
    generate_parser.add_argument(
        "--mode", choices=sorted(router.WEIGHTS), default="balanced"
    )
    generate_parser.add_argument(
        "--provider", choices=("auto", "openrouter", "direct"), default="auto"
    )
    generate_parser.add_argument("--model")
    generate_parser.add_argument("--require-benchmarks", action="store_true")
    generate_parser.add_argument(
        "--require-live-catalog",
        action="store_true",
        help="Refresh the authenticated OpenRouter catalog before routing",
    )
    generate_parser.add_argument(
        "--max-bytes", type=int, default=router.DEFAULT_MAX_BYTES
    )
    generate_parser.add_argument(
        "--max-artifact-bytes", type=int, default=DEFAULT_MAX_ARTIFACT_BYTES
    )
    generate_parser.add_argument(
        "--max-output-tokens", type=int, default=DEFAULT_MAX_OUTPUT_TOKENS
    )
    generate_parser.add_argument(
        "--response-class",
        choices=("automatic", "micro", "compact", "standard", "artifact"),
        default="automatic",
        help="Measurement-only recommended external response class",
    )
    generate_parser.add_argument(
        "--codex-context-limit-tokens",
        type=int,
        help="Caller-reported active Codex context limit for preflight only",
    )
    generate_parser.add_argument(
        "--codex-context-used-tokens",
        type=int,
        help="Caller-reported active Codex context usage for preflight only",
    )
    generate_parser.add_argument(
        "--max-authorized-cost",
        default=None,
        help="Explicit maximum USD authorization for this handoff",
    )
    generate_parser.add_argument(
        "--fit-output-to-cost-ceiling",
        action="store_true",
        help=(
            "Reduce output tokens, down to 1024, when needed to fit the explicit "
            "cost ceiling; never raises the ceiling"
        ),
    )
    generate_parser.add_argument(
        "--require-zdr",
        action="store_true",
        help="Require a Zero Data Retention endpoint",
    )
    generate_parser.add_argument("--timeout", type=int, default=90)
    generate_parser.add_argument("--fixtures", help=argparse.SUPPRESS)
    show = sub.add_parser("show", help="Validate and preview source")
    show.add_argument("handoff_id")
    show.add_argument("--offset", type=int, default=0)
    show.add_argument("--max-chars", type=int, default=router.RECOVERY_CHUNK_CHARS)
    continuation = sub.add_parser(
        "continuation-plan",
        help="Plan a same-route continuation without dispatch or reservation",
    )
    continuation.add_argument("handoff_id")
    continuation.add_argument("--task", required=True)
    continuation.add_argument("--repo", default=".")
    continuation.add_argument("--file", action="append", default=[])
    continuation.add_argument(
        "--completed-id",
        action="append",
        default=[],
        help="Completed section or finding ID that the continuation must not repeat",
    )
    continuation.add_argument("--max-bytes", type=int, default=router.DEFAULT_MAX_BYTES)
    approve = sub.add_parser("approve", help="Approve for Codex consideration only")
    approve.add_argument("handoff_id")
    reject = sub.add_parser("reject", help="Reject a handoff")
    reject.add_argument("handoff_id")
    adversarial = sub.add_parser(
        "adversarial-review", help="Create a separate Codex review record"
    )
    adversarial.add_argument("handoff_id")
    download = sub.add_parser("download", help="Download outside the active repository")
    download.add_argument("handoff_id")
    download.add_argument("--destination", required=True)
    download.add_argument("--repo", default=".")
    return root


def main() -> int:
    args = empire_present.parse_args_with_view(parser())
    try:
        if args.command == "generate":
            result = generate(args)
        elif args.command == "show":
            result = lifecycle_show(args.handoff_id, args.offset, args.max_chars)
        elif args.command == "continuation-plan":
            result = continuation_plan(args)
        elif args.command == "approve":
            result = lifecycle_approve(args.handoff_id)
        elif args.command == "reject":
            result = lifecycle_reject(args.handoff_id)
        elif args.command == "adversarial-review":
            result = lifecycle_adversarial_review(args.handoff_id)
        elif args.command == "download":
            result = lifecycle_download(args.handoff_id, args.destination, args.repo)
        else:
            raise HandoffError("Unsupported handoff command")
        print(
            empire_present.format_output(
                result,
                view=args.view,
                title=empire_present.command_title(args),
            ),
            end="",
        )
        return 0
    except (BudgetError, HandoffError, router.RouterError, OSError) as exc:
        print(
            empire_present.format_output(
                {"status": "error", "error": str(exc)},
                view=args.view,
                title=empire_present.command_title(args),
            ),
            end="",
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
