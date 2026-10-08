#!/usr/bin/env python3
"""Durable, bounded response recovery for the Empire review router."""

from __future__ import annotations

import codecs
import hashlib
import json
import math
import os
import re
import stat
import subprocess
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
from typing import Any

from empire_budget import (
    BudgetStore,
    project_identity,
    usd_to_microusd,
)
from empire_secret_policy import secret_findings


class RouterError(Exception):
    """Base error shared by recovery and routing operations."""


def budget_project(repo_value: str) -> tuple[str, str, Path]:
    """Resolve the durable budget identity for a Git repository."""
    repo = Path(repo_value).expanduser().resolve()
    if not repo.is_dir():
        raise RouterError(f"Repository is not a directory: {repo}")
    proc = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "--show-toplevel"],
        text=True,
        capture_output=True,
        timeout=20,
    )
    if proc.returncode:
        raise RouterError(proc.stderr.strip() or "git rev-parse failed")
    root = Path(proc.stdout.strip()).resolve()
    project_id, project_name = project_identity(root)
    return project_id, project_name, root


def platform_data_dir() -> Path:
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "empire-codex-router"
    if sys.platform == "win32":
        root = os.environ.get("LOCALAPPDATA") or os.environ.get("APPDATA")
        return (
            Path(root) / "Empire Codex Router"
            if root
            else Path.home() / "AppData" / "Local" / "Empire Codex Router"
        )
    root = os.environ.get("XDG_DATA_HOME")
    return (
        Path(root) / "empire-codex-router"
        if root
        else Path.home() / ".local" / "share" / "empire-codex-router"
    )


def platform_cache_dir() -> Path:
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Caches" / "empire-codex-router"
    if sys.platform == "win32":
        root = os.environ.get("LOCALAPPDATA")
        return (
            Path(root) / "Empire Codex Router" / "Cache"
            if root
            else platform_data_dir() / "Cache"
        )
    root = os.environ.get("XDG_CACHE_HOME")
    return (
        Path(root) / "empire-codex-router"
        if root
        else Path.home() / ".cache" / "empire-codex-router"
    )


RECOVERY_CHUNK_CHARS = 12_000
DEFAULT_MAX_PROVIDER_RESPONSE_BYTES = 8_000_000
MAX_RECOVERY_RECEIPT_BYTES = 262_144
MAX_RECOVERY_CONTENT_BYTES = DEFAULT_MAX_PROVIDER_RESPONSE_BYTES
COMPLETE_FINISH_REASONS = {"stop", "tool_calls"}
PARTIAL_FINISH_REASONS = {"length", "max_tokens"}
BLOCKED_FINISH_REASONS = {"content_filter", "safety"}


def response_recovery_root() -> Path:
    configured = os.environ.get("EMPIRE_RESPONSE_DIR")
    return (
        Path(configured).expanduser()
        if configured
        else platform_data_dir() / "responses"
    ).resolve()


def _atomic_private_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    try:
        os.chmod(path.parent, 0o700)
    except OSError:
        pass
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        os.chmod(path, 0o600)
        _fsync_directory(path.parent)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def _atomic_private_json(path: Path, value: dict[str, Any]) -> None:
    _atomic_private_text(
        path, json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    )


def _fsync_directory(path: Path) -> None:
    """Synchronize directory metadata after an atomic create or replace."""
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    try:
        descriptor = os.open(path, flags)
    except OSError:
        return
    try:
        os.fsync(descriptor)
    except OSError:
        pass
    finally:
        os.close(descriptor)


def _visible_message_content(message: dict[str, Any]) -> str:
    parsed = message.get("parsed")
    content = parsed if parsed is not None else message.get("content")
    if isinstance(content, list):
        blocks: list[str] = []
        for item in content:
            if not isinstance(item, dict):
                continue
            if isinstance(item.get("text"), str):
                blocks.append(item["text"])
            elif isinstance(item.get("json"), dict):
                blocks.append(json.dumps(item["json"], ensure_ascii=False))
        return "".join(blocks)
    if isinstance(content, dict):
        return json.dumps(content, ensure_ascii=False)
    return str(content or "")


def normalize_provider_result(payload: dict[str, Any]) -> dict[str, Any]:
    """Normalize completion, in-band error, and visible-content state."""
    choice: dict[str, Any] = {}
    message: dict[str, Any] = {}
    choices = payload.get("choices")
    if isinstance(choices, list) and choices and isinstance(choices[0], dict):
        choice = choices[0]
        candidate = choice.get("message")
        if isinstance(candidate, dict):
            message = candidate
    content = _visible_message_content(message)
    finish_value = choice.get("finish_reason")
    finish_reason = str(finish_value) if finish_value is not None else None
    error = choice.get("error") if isinstance(choice.get("error"), dict) else None
    if error is None and isinstance(payload.get("error"), dict):
        error = payload["error"]
    metadata = error.get("metadata") if isinstance(error, dict) else None
    error_type = None
    if isinstance(metadata, dict) and metadata.get("error_type") is not None:
        error_type = str(metadata["error_type"])
    elif isinstance(error, dict) and error.get("error_type") is not None:
        error_type = str(error["error_type"])
    elif payload.get("error_type") is not None:
        error_type = str(payload["error_type"])
    transport = payload.get("_empire_transport")
    deadline_exceeded = bool(
        isinstance(transport, dict) and transport.get("deadline_exceeded") is True
    )

    if finish_reason in BLOCKED_FINISH_REASONS:
        generation_state = "blocked"
        terminal_reason = "content_filter"
    elif deadline_exceeded:
        generation_state = "partial" if content else "ambiguous"
        terminal_reason = "total_deadline_exceeded"
    elif error is not None or finish_reason == "error":
        generation_state = "partial" if content else "failed"
        terminal_reason = "provider_error"
    elif finish_reason in PARTIAL_FINISH_REASONS:
        generation_state = "partial" if content else "failed"
        terminal_reason = "length"
    elif finish_reason in COMPLETE_FINISH_REASONS:
        generation_state = "complete"
        terminal_reason = "stop"
    else:
        generation_state = "ambiguous"
        terminal_reason = "unknown"
    return {
        "content": content,
        "finish_reason": finish_reason,
        "generation_state": generation_state,
        "terminal_reason": terminal_reason,
        "provider_error_type": error_type,
        "provider_error_present": error is not None,
        "transport_deadline_exceeded": deadline_exceeded,
        "content_complete": generation_state == "complete",
    }


def assistant_response_content(payload: dict[str, Any]) -> tuple[str, str | None]:
    """Project only assistant-authored content from a provider envelope."""
    normalized = normalize_provider_result(payload)
    return normalized["content"], normalized["finish_reason"]


def provider_reference_data(
    payload: dict[str, Any], *, route_provider: str | None = None
) -> dict[str, str | None]:
    """Project only non-secret provider identifiers from a completion envelope."""
    transport = payload.get("_empire_transport")
    transport = transport if isinstance(transport, dict) else {}
    generation_id = transport.get("provider_generation_id")
    request_id = transport.get("provider_request_id")
    payload_id = payload.get("id")
    explicit_generation_id = payload.get("generation_id")
    explicit_request_id = payload.get("request_id")
    if isinstance(explicit_generation_id, str) and explicit_generation_id.strip():
        generation_id = explicit_generation_id
    if isinstance(explicit_request_id, str) and explicit_request_id.strip():
        request_id = explicit_request_id
    if isinstance(payload_id, str) and payload_id.strip():
        if route_provider == "openrouter" or payload_id.startswith("gen-"):
            generation_id = payload_id
        elif request_id is None:
            request_id = payload_id

    def bounded(value: Any) -> str | None:
        if not isinstance(value, str):
            return None
        normalized = value.strip()
        if (
            not normalized
            or len(normalized) > 200
            or any(ord(character) < 33 for character in normalized)
        ):
            return None
        return normalized

    return {
        "provider_generation_id": bounded(generation_id),
        "provider_request_id": bounded(request_id),
    }


def prepare_provider_response(
    *,
    kind: str,
    root: Path | None = None,
    response_id: str | None = None,
) -> dict[str, Any]:
    """Create a durable, discoverable journal before provider dispatch."""
    identifier = response_id or str(uuid.uuid4())
    base = (root or response_recovery_root()).resolve()
    base.mkdir(parents=True, exist_ok=True, mode=0o700)
    try:
        os.chmod(base, 0o700)
    except OSError:
        pass
    directory = (base / identifier).resolve()
    try:
        directory.relative_to(base)
    except ValueError as exc:
        raise RouterError("Response recovery path escapes its private root") from exc
    if directory.exists():
        raise RouterError("Response recovery ID already exists")
    directory.mkdir(parents=False, mode=0o700)
    _fsync_directory(base)
    content_path = directory / "assistant-content.md"
    receipt_path = directory / "delivery-receipt.json"
    _atomic_private_text(content_path, "")
    receipt = {
        "schema_version": "1.1",
        "response_id": identifier,
        "kind": kind,
        "prepared_at": datetime.now(timezone.utc).isoformat(),
        "state": "prepared",
        "generation_state": "prepared",
        "artifact_state": "empty",
        "validation_state": "not_attempted",
        "billing_state": "reserved",
        "ingestion_state": "not_attempted",
        "usage_state": "not_used",
        "receipt_generation": 0,
        "commit_id": None,
        "dispatch_recorded": False,
        "durable_response_bytes": 0,
        "response_sha256": "sha256:" + hashlib.sha256(b"").hexdigest(),
        "input_prompt_persisted": False,
        "repository_evidence_persisted": False,
        "provider_envelope_persisted": False,
    }
    _atomic_private_json(receipt_path, receipt)
    return {
        "response_id": identifier,
        "directory": directory,
        "content": "",
        "content_path": content_path,
        "receipt_path": receipt_path,
        "receipt": receipt,
    }


def mark_response_dispatched(capture: dict[str, Any], reservation_id: str) -> None:
    receipt = dict(capture["receipt"])
    receipt.update(
        {
            "state": "dispatched",
            "generation_state": "dispatched",
            "billing_state": "dispatched",
            "dispatch_recorded": True,
            "reservation_id": reservation_id,
            "dispatched_at": datetime.now(timezone.utc).isoformat(),
        }
    )
    _atomic_private_json(capture["receipt_path"], receipt)
    capture["receipt"] = receipt


def capture_provider_response(
    payload: dict[str, Any],
    *,
    kind: str,
    root: Path | None = None,
    response_id: str | None = None,
    prepared: dict[str, Any] | None = None,
    route_provider: str | None = None,
) -> dict[str, Any]:
    """Durably save assistant bytes before billing settlement or validation."""
    capture = prepared or prepare_provider_response(
        kind=kind, root=root, response_id=response_id
    )
    normalized = normalize_provider_result(payload)
    provider_references = provider_reference_data(
        payload, route_provider=route_provider
    )
    content = normalized["content"]
    content_path = capture["content_path"]
    encoded = content.encode("utf-8")
    labels = secret_findings(content) if content else []
    commit_id = str(uuid.uuid4())
    response_hash = "sha256:" + hashlib.sha256(encoded).hexdigest()
    safe_to_synthesize = (
        bool(content)
        and not labels
        and normalized["generation_state"] != "blocked"
    )
    committed_receipt = {
        **capture["receipt"],
        "schema_version": "1.1",
        "response_id": capture["response_id"],
        "kind": kind,
        "commit_id": commit_id,
        "receipt_generation": int(
            capture["receipt"].get("receipt_generation", 0)
        )
        + 1,
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "state": "captured_unvalidated" if content else "failed_empty",
        "generation_state": normalized["generation_state"],
        "artifact_state": "partial"
        if content and not normalized["content_complete"]
        else "complete"
        if content
        else "missing",
        "validation_state": "not_attempted",
        "finish_reason": normalized["finish_reason"],
        "terminal_reason": normalized["terminal_reason"],
        "provider_error_type": normalized["provider_error_type"],
        "provider_error_present": normalized["provider_error_present"],
        **provider_references,
        "transport_deadline_exceeded": normalized[
            "transport_deadline_exceeded"
        ],
        "durable_response_bytes": len(encoded),
        "response_sha256": response_hash,
        "content_complete": normalized["content_complete"],
        "schema_valid": False,
        "safe_to_synthesize": safe_to_synthesize,
        "sensitive_content_labels": labels,
        "chunk_chars": RECOVERY_CHUNK_CHARS,
        "chunk_count": max(1, math.ceil(len(content) / RECOVERY_CHUNK_CHARS))
        if content
        else 0,
        "automatic_retry_started": False,
        "automatic_continuation_started": False,
    }
    receipt_path = capture["receipt_path"]
    staged_receipt = {
        **capture["receipt"],
        "schema_version": "1.1",
        "state": "response_staged",
        "artifact_state": "staging",
        "validation_state": "not_attempted",
        "commit_id": commit_id,
        "pending_response_sha256": response_hash,
        "pending_response_bytes": len(encoded),
        "pending_committed_receipt": committed_receipt,
        "safe_to_synthesize": False,
        "staged_at": datetime.now(timezone.utc).isoformat(),
    }
    _atomic_private_json(receipt_path, staged_receipt)
    capture["receipt"] = staged_receipt
    _atomic_private_text(content_path, content)
    _atomic_private_json(receipt_path, committed_receipt)
    capture.update({"content": content, "receipt": committed_receipt})
    return capture


def finalize_provider_response(
    capture: dict[str, Any],
    *,
    state: str,
    schema_valid: bool,
    observed_cost_usd: float,
    billing_state: str = "confirmed",
) -> dict[str, Any]:
    receipt = dict(capture["receipt"])
    delivered = receipt["durable_response_bytes"] > 0
    compensation_status = (
        "pending_reconciliation"
        if billing_state == "pending_reconciliation" and not delivered
        else "compensation_pending"
        if observed_cost_usd > 0 and not delivered
        else "compensation_not_required"
    )
    compensation_record: dict[str, Any] | None = None
    if compensation_status == "compensation_pending":
        reservation_id = receipt.get("reservation_id")
        if not isinstance(reservation_id, str) or not reservation_id:
            raise RouterError(
                "Paid empty delivery is missing the reservation required for compensation"
            )
        with BudgetStore() as store:
            compensation_record = store.open_compensation(
                reservation_id,
                response_id=capture["response_id"],
            )
    receipt.update(
        {
            "state": state,
            "schema_valid": schema_valid,
            "validation_state": "valid" if schema_valid else "invalid",
            "artifact_state": "blocked"
            if state in {"blocked_sensitive", "blocked_provider_safety"}
            else "missing"
            if not delivered
            else "partial"
            if state == "partial_recoverable"
            else "complete",
            "billing_state": billing_state,
            "observed_cost_usd": observed_cost_usd,
            "delivery_receipted": delivered,
            "compensation_status": compensation_status,
            "compensation_id": compensation_record["compensation_id"]
            if compensation_record
            else None,
            "compensation_state": compensation_record["state"]
            if compensation_record
            else "not_applicable",
            "finalized_at": datetime.now(timezone.utc).isoformat(),
        }
    )
    _atomic_private_json(capture["receipt_path"], receipt)
    capture["receipt"] = receipt
    return {
        "response_id": capture["response_id"],
        "state": state,
        "content_path": str(capture["content_path"]),
        "receipt_path": str(capture["receipt_path"]),
        "durable_response_bytes": receipt["durable_response_bytes"],
        "response_sha256": receipt["response_sha256"],
        "finish_reason": receipt["finish_reason"],
        "terminal_reason": receipt.get("terminal_reason"),
        "provider_error_type": receipt.get("provider_error_type"),
        "provider_generation_id": receipt.get("provider_generation_id"),
        "provider_request_id": receipt.get("provider_request_id"),
        "generation_state": receipt.get("generation_state"),
        "artifact_state": receipt.get("artifact_state"),
        "validation_state": receipt.get("validation_state"),
        "billing_state": receipt.get("billing_state"),
        "content_complete": receipt["content_complete"],
        "schema_valid": schema_valid,
        "safe_to_synthesize": receipt["safe_to_synthesize"],
        "chunk_chars": receipt["chunk_chars"],
        "chunk_count": receipt["chunk_count"],
        "next_chunk": 0 if receipt["chunk_count"] else None,
        "resume_supported": receipt["chunk_count"] > 1 or not receipt["content_complete"],
        "automatic_retry_started": False,
        "automatic_continuation_started": False,
        "delivery_receipted": receipt["delivery_receipted"],
        "compensation_status": receipt["compensation_status"],
        "compensation_id": receipt["compensation_id"],
        "compensation_state": receipt["compensation_state"],
    }


def observed_usage_cost(
    completion: dict[str, Any],
    selected: dict[str, Any],
    *,
    route_provider: str,
) -> tuple[int | None, str]:
    """Return trusted micro-USD cost or an explicit ambiguous result."""
    usage = completion.get("usage")
    if not isinstance(usage, dict):
        return None, "usage_missing"
    reported_cost = usage.get("cost")
    if route_provider == "openrouter" and reported_cost is not None:
        reported_microusd = usd_to_microusd(reported_cost)
        prompt_value = usage.get("prompt_tokens", usage.get("input_tokens"))
        completion_value = usage.get(
            "completion_tokens", usage.get("output_tokens")
        )
        priced_route = any(
            Decimal(str(selected.get(field) or 0)) > 0
            for field in ("prompt_price", "completion_price", "request_price")
        )
        nonzero_usage = False
        try:
            nonzero_usage = int(prompt_value or 0) + int(completion_value or 0) > 0
        except (TypeError, ValueError):
            nonzero_usage = True
        if reported_microusd == 0 and (priced_route or nonzero_usage):
            return None, "openrouter_zero_cost_requires_reconciliation"
        return reported_microusd, "openrouter_response"
    prompt_value = usage.get("prompt_tokens", usage.get("input_tokens"))
    completion_value = usage.get("completion_tokens", usage.get("output_tokens"))
    if prompt_value is None or completion_value is None:
        return None, (
            "direct_usage_missing_token_counts"
            if route_provider == "direct"
            else "openrouter_usage_missing_cost_and_token_counts"
        )
    try:
        prompt_tokens = int(prompt_value)
        completion_tokens = int(completion_value)
    except (TypeError, ValueError):
        return None, "usage_token_counts_invalid"
    if prompt_tokens < 0 or completion_tokens < 0:
        return None, "usage_token_counts_invalid"
    observed = Decimal(prompt_tokens) * Decimal(str(selected["prompt_price"]))
    observed += Decimal(completion_tokens) * Decimal(
        str(selected["completion_price"])
    )
    if selected.get("request_price") is not None:
        observed += Decimal(str(selected["request_price"]))
    return usd_to_microusd(observed), (
        "user_configured_direct_price_calculation"
        if route_provider == "direct"
        else "local_price_snapshot_calculation"
    )


def response_billing_state(
    observed_microusd: int,
    authorized_microusd: int,
    *,
    pending: bool,
) -> str:
    if pending:
        return "pending_reconciliation"
    if observed_microusd > authorized_microusd:
        return "settled_overrun"
    return "confirmed"


def outcome_proven_nonbillable(route_provider: str, status_code: Any) -> bool:
    """Only apply definitive no-bill semantics for a known provider contract."""
    return (
        route_provider == "openrouter"
        and isinstance(status_code, int)
        and not isinstance(status_code, bool)
        and status_code < 500
        and status_code != 408
    )


def _response_directory(response_id: str, root: Path | None = None) -> Path:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]{0,127}", response_id):
        raise RouterError("Response ID is invalid")
    base = (root or response_recovery_root()).resolve()
    return base / response_id


def _open_response_directory_fd(directory: Path) -> int:
    flags = (
        os.O_RDONLY
        | getattr(os, "O_CLOEXEC", 0)
        | getattr(os, "O_DIRECTORY", 0)
        | getattr(os, "O_NOFOLLOW", 0)
    )
    try:
        descriptor = os.open(directory, flags)
    except OSError as exc:
        raise RouterError("Response recovery directory is unsafe or unreadable") from exc
    try:
        metadata = os.fstat(descriptor)
        if not stat.S_ISDIR(metadata.st_mode):
            raise RouterError("Response recovery path is not a directory")
        if hasattr(os, "getuid") and metadata.st_uid != os.getuid():
            raise RouterError("Response recovery directory has an unexpected owner")
        if metadata.st_mode & 0o077:
            raise RouterError("Response recovery directory permissions are too broad")
        return descriptor
    except Exception:
        os.close(descriptor)
        raise


def _open_private_regular_at(
    directory_fd: int,
    name: str,
    *,
    maximum_bytes: int,
    directory: Path | None = None,
) -> tuple[int, os.stat_result]:
    # A FIFO can block in open() before fstat() gets a chance to reject it.
    # Nonblocking mode has no effect on regular files; retain descriptor-based
    # validation so a pathname check cannot introduce a replacement race.
    flags = (
        os.O_RDONLY
        | getattr(os, "O_CLOEXEC", 0)
        | getattr(os, "O_NOFOLLOW", 0)
        | getattr(os, "O_NONBLOCK", 0)
    )
    try:
        if os.open in os.supports_dir_fd:
            descriptor = os.open(name, flags, dir_fd=directory_fd)
        elif directory is not None:
            candidate = directory / name
            if candidate.is_symlink():
                raise OSError("symbolic link refused")
            descriptor = os.open(candidate, flags)
        else:
            raise OSError("descriptor-relative open is unavailable")
    except OSError as exc:
        raise RouterError("Response recovery contains an unsafe or unreadable file") from exc
    try:
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            raise RouterError("Response recovery file is not regular")
        if metadata.st_size < 0 or metadata.st_size > maximum_bytes:
            raise RouterError("Response recovery file exceeds its safety ceiling")
        if hasattr(os, "getuid") and metadata.st_uid != os.getuid():
            raise RouterError("Response recovery file has an unexpected owner")
        if metadata.st_mode & 0o077:
            raise RouterError("Response recovery file permissions are too broad")
        return descriptor, metadata
    except Exception:
        os.close(descriptor)
        raise


def _read_fd_bounded(descriptor: int, maximum_bytes: int) -> bytes:
    chunks: list[bytes] = []
    remaining = maximum_bytes + 1
    while remaining > 0:
        chunk = os.read(descriptor, min(65_536, remaining))
        if not chunk:
            break
        chunks.append(chunk)
        remaining -= len(chunk)
    content = b"".join(chunks)
    if len(content) > maximum_bytes:
        raise RouterError("Response recovery file exceeds its safety ceiling")
    return content


def _load_response_receipt(directory: Path) -> dict[str, Any]:
    directory_fd = _open_response_directory_fd(directory)
    try:
        receipt_fd, metadata = _open_private_regular_at(
            directory_fd,
            "delivery-receipt.json",
            maximum_bytes=MAX_RECOVERY_RECEIPT_BYTES,
            directory=directory,
        )
        try:
            encoded = _read_fd_bounded(receipt_fd, MAX_RECOVERY_RECEIPT_BYTES)
            final_metadata = os.fstat(receipt_fd)
            if (
                final_metadata.st_size != metadata.st_size
                or final_metadata.st_mtime_ns != metadata.st_mtime_ns
            ):
                raise RouterError("Response receipt changed while it was being read")
        finally:
            os.close(receipt_fd)
    finally:
        os.close(directory_fd)
    try:
        receipt = json.loads(encoded.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RouterError("Response recovery receipt is corrupt") from exc
    if not isinstance(receipt, dict):
        raise RouterError("Response recovery receipt is not an object")
    return receipt


def list_response_recoveries(root: Path | None = None) -> dict[str, Any]:
    """List receipt metadata without exposing assistant content."""
    base = (root or response_recovery_root()).resolve()
    if not base.exists():
        return {"status": "available", "response_count": 0, "responses": []}
    responses: list[dict[str, Any]] = []
    for directory in sorted(base.iterdir()):
        if not directory.is_dir() or directory.is_symlink():
            continue
        try:
            receipt = _load_response_receipt(directory)
        except RouterError:
            responses.append(
                {
                    "response_id": directory.name,
                    "state": "corrupt",
                    "receipt_readable": False,
                }
            )
            continue
        responses.append(
            {
                "response_id": receipt.get("response_id", directory.name),
                "kind": receipt.get("kind"),
                "state": receipt.get("state"),
                "generation_state": receipt.get("generation_state"),
                "artifact_state": receipt.get("artifact_state"),
                "validation_state": receipt.get("validation_state"),
                "billing_state": receipt.get("billing_state"),
                "dispatch_recorded": receipt.get("dispatch_recorded", False),
                "durable_response_bytes": receipt.get("durable_response_bytes", 0),
                "content_complete": receipt.get("content_complete", False),
                "safe_to_synthesize": receipt.get("safe_to_synthesize", False),
                "captured_at": receipt.get("captured_at", receipt.get("prepared_at")),
                "receipt_readable": True,
            }
        )
    return {
        "status": "available",
        "response_count": len(responses),
        "responses": responses,
    }


def read_response_recovery(
    response_id: str,
    *,
    offset: int = 0,
    max_chars: int = RECOVERY_CHUNK_CHARS,
    root: Path | None = None,
) -> dict[str, Any]:
    if offset < 0 or max_chars <= 0 or max_chars > RECOVERY_CHUNK_CHARS:
        raise RouterError(
            f"Response reads require offset >= 0 and max_chars <= {RECOVERY_CHUNK_CHARS}"
        )
    directory = _response_directory(response_id, root)
    receipt = _load_response_receipt(directory)
    if receipt.get("response_id") != response_id:
        raise RouterError("Response recovery identity mismatch")
    if not receipt.get("safe_to_synthesize"):
        raise RouterError("Response recovery is blocked from ordinary reading")
    directory_fd = _open_response_directory_fd(directory)
    try:
        content_fd, metadata = _open_private_regular_at(
            directory_fd,
            "assistant-content.md",
            maximum_bytes=MAX_RECOVERY_CONTENT_BYTES,
            directory=directory,
        )
        try:
            digest = hashlib.sha256()
            decoder = codecs.getincrementaldecoder("utf-8")("strict")
            total_chars = 0
            total_bytes = 0
            selected: list[str] = []
            while True:
                encoded_chunk = os.read(content_fd, 65_536)
                if encoded_chunk:
                    total_bytes += len(encoded_chunk)
                    if total_bytes > MAX_RECOVERY_CONTENT_BYTES:
                        raise RouterError(
                            "Response recovery file exceeds its safety ceiling"
                        )
                    digest.update(encoded_chunk)
                    decoded_chunk = decoder.decode(encoded_chunk, final=False)
                    final_chunk = False
                else:
                    decoded_chunk = decoder.decode(b"", final=True)
                    final_chunk = True
                chunk_start = total_chars
                total_chars += len(decoded_chunk)
                wanted_start = max(offset, chunk_start)
                wanted_end = min(offset + max_chars, total_chars)
                if wanted_start < wanted_end:
                    selected.append(
                        decoded_chunk[
                            wanted_start - chunk_start : wanted_end - chunk_start
                        ]
                    )
                if final_chunk:
                    break
            final_metadata = os.fstat(content_fd)
            if (
                final_metadata.st_size != metadata.st_size
                or final_metadata.st_mtime_ns != metadata.st_mtime_ns
            ):
                raise RouterError("Response content changed while it was being read")
        except UnicodeDecodeError as exc:
            raise RouterError("Response recovery content is not valid UTF-8") from exc
        finally:
            os.close(content_fd)
    finally:
        os.close(directory_fd)
    expected_hash = "sha256:" + digest.hexdigest()
    if expected_hash != receipt.get(
        "response_sha256"
    ) or metadata.st_size != receipt.get("durable_response_bytes"):
        raise RouterError("Response recovery integrity check failed")
    chunk = "".join(selected)
    next_offset = offset + len(chunk)
    has_more = next_offset < total_chars
    return {
        "status": "response_chunk",
        "response_id": response_id,
        "state": receipt.get("state"),
        "content": chunk,
        "chunk": {
            "offset": offset,
            "returned_chars": len(chunk),
            "has_more": has_more,
            "next_offset": next_offset if has_more else None,
            "total_chars": total_chars,
        },
    }


def _hash_recovery_content(directory: Path) -> tuple[str, int]:
    directory_fd = _open_response_directory_fd(directory)
    try:
        content_fd, metadata = _open_private_regular_at(
            directory_fd,
            "assistant-content.md",
            maximum_bytes=MAX_RECOVERY_CONTENT_BYTES,
            directory=directory,
        )
        try:
            digest = hashlib.sha256()
            total = 0
            while True:
                chunk = os.read(content_fd, 65_536)
                if not chunk:
                    break
                total += len(chunk)
                if total > MAX_RECOVERY_CONTENT_BYTES:
                    raise RouterError(
                        "Response recovery file exceeds its safety ceiling"
                    )
                digest.update(chunk)
            final_metadata = os.fstat(content_fd)
            if (
                final_metadata.st_size != metadata.st_size
                or final_metadata.st_mtime_ns != metadata.st_mtime_ns
            ):
                raise RouterError("Response content changed while it was being read")
        finally:
            os.close(content_fd)
    finally:
        os.close(directory_fd)
    return "sha256:" + digest.hexdigest(), total


def _append_private_jsonl(path: Path, value: dict[str, Any]) -> None:
    flags = (
        os.O_WRONLY
        | os.O_CREAT
        | os.O_APPEND
        | getattr(os, "O_CLOEXEC", 0)
        | getattr(os, "O_NOFOLLOW", 0)
        | getattr(os, "O_NONBLOCK", 0)
    )
    descriptor = os.open(path, flags, 0o600)
    try:
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            raise RouterError("Response recovery event log is not regular")
        if hasattr(os, "getuid") and metadata.st_uid != os.getuid():
            raise RouterError("Response recovery event log has an unexpected owner")
        os.chmod(path, 0o600)
        encoded = (
            json.dumps(value, sort_keys=True, ensure_ascii=False) + "\n"
        ).encode("utf-8")
        view = memoryview(encoded)
        while view:
            written = os.write(descriptor, view)
            if written <= 0:
                raise OSError("Response recovery event log write made no progress")
            view = view[written:]
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    _fsync_directory(path.parent)


def repair_response_recovery(
    response_id: str,
    *,
    root: Path | None = None,
) -> dict[str, Any]:
    """Complete an interrupted local content commit without provider access."""
    directory = _response_directory(response_id, root)
    receipt = _load_response_receipt(directory)
    if receipt.get("response_id") != response_id:
        raise RouterError("Response recovery identity mismatch")
    if receipt.get("state") != "response_staged":
        raise RouterError("Response recovery is not in a repairable staged state")
    committed = receipt.get("pending_committed_receipt")
    if not isinstance(committed, dict):
        raise RouterError("Staged response is missing its committed receipt")
    if (
        committed.get("response_id") != response_id
        or committed.get("commit_id") != receipt.get("commit_id")
    ):
        raise RouterError("Staged response commit identity mismatch")
    actual_hash, actual_bytes = _hash_recovery_content(directory)
    if (
        actual_hash != receipt.get("pending_response_sha256")
        or actual_bytes != receipt.get("pending_response_bytes")
        or actual_hash != committed.get("response_sha256")
        or actual_bytes != committed.get("durable_response_bytes")
    ):
        raise RouterError("Staged response content does not match its pending commit")
    repaired_at = datetime.now(timezone.utc).isoformat()
    repaired = {
        **committed,
        "repaired_after_interrupted_commit": True,
        "repaired_at": repaired_at,
    }
    _atomic_private_json(directory / "delivery-receipt.json", repaired)
    _append_private_jsonl(
        directory / "repair-events.jsonl",
        {
            "event": "interrupted_commit_repaired",
            "response_id": response_id,
            "commit_id": repaired.get("commit_id"),
            "response_sha256": actual_hash,
            "durable_response_bytes": actual_bytes,
            "created_at": repaired_at,
        },
    )
    return {
        "status": "repaired",
        "response_id": response_id,
        "state": repaired.get("state"),
        "commit_id": repaired.get("commit_id"),
        "response_sha256": actual_hash,
        "durable_response_bytes": actual_bytes,
        "provider_dispatch_performed": False,
    }


def audit_response_recoveries(
    repo_value: str,
    *,
    root: Path | None = None,
) -> dict[str, Any]:
    """Compare response journals, durable bytes, and the project budget ledger."""
    project_id, project_name, _ = budget_project(repo_value)
    base = (root or response_recovery_root()).resolve()
    findings: list[dict[str, Any]] = []
    audited = 0
    with BudgetStore() as store:
        for directory in sorted(base.iterdir()) if base.exists() else []:
            if not directory.is_dir() or directory.is_symlink():
                continue
            audited += 1
            response_id = directory.name
            try:
                receipt = _load_response_receipt(directory)
            except RouterError as exc:
                findings.append(
                    {
                        "response_id": response_id,
                        "severity": "contradiction",
                        "code": "receipt_unreadable",
                        "action": "inspect_private_recovery",
                        "detail": str(exc),
                    }
                )
                continue
            reservation_id = receipt.get("reservation_id")
            reservation = None
            if isinstance(reservation_id, str):
                row = store.connection.execute(
                    "SELECT reservation_id, project_id, state, observed_microusd "
                    "FROM reservations WHERE reservation_id = ?",
                    (reservation_id,),
                ).fetchone()
                if row and row["project_id"] == project_id:
                    reservation = row
                elif row:
                    continue
            if receipt.get("dispatch_recorded") and reservation is None:
                findings.append(
                    {
                        "response_id": response_id,
                        "severity": "contradiction",
                        "code": "dispatched_receipt_missing_project_reservation",
                        "action": "inspect_private_recovery",
                    }
                )
            content_bytes = int(receipt.get("durable_response_bytes") or 0)
            if receipt.get("state") == "response_staged":
                findings.append(
                    {
                        "response_id": response_id,
                        "severity": "attention",
                        "code": "interrupted_content_commit",
                        "action": f"responses repair {response_id}",
                    }
                )
            elif content_bytes > 0:
                try:
                    actual_hash, actual_bytes = _hash_recovery_content(directory)
                except RouterError as exc:
                    findings.append(
                        {
                            "response_id": response_id,
                            "severity": "contradiction",
                            "code": "content_unreadable",
                            "action": "inspect_private_recovery",
                            "detail": str(exc),
                        }
                    )
                else:
                    if (
                        actual_hash != receipt.get("response_sha256")
                        or actual_bytes != content_bytes
                    ):
                        findings.append(
                            {
                                "response_id": response_id,
                                "severity": "contradiction",
                                "code": "content_receipt_integrity_mismatch",
                                "action": "inspect_private_recovery",
                            }
                        )
            if reservation is None:
                continue
            ledger_state = str(reservation["state"])
            receipt_billing = str(receipt.get("billing_state") or "unknown")
            if ledger_state == "released" and content_bytes > 0:
                findings.append(
                    {
                        "response_id": response_id,
                        "severity": "contradiction",
                        "code": "released_reservation_has_delivered_content",
                        "action": "budget history --repo PROJECT",
                    }
                )
            elif ledger_state == "settled" and content_bytes == 0:
                findings.append(
                    {
                        "response_id": response_id,
                        "severity": "attention",
                        "code": "settled_without_durable_delivery",
                        "action": "open_compensation_record",
                    }
                )
            elif ledger_state in {"dispatched", "pending_reconciliation"}:
                findings.append(
                    {
                        "response_id": response_id,
                        "severity": "attention",
                        "code": "billing_reconciliation_required",
                        "action": "budget pending --repo PROJECT",
                    }
                )
            elif ledger_state == "settled" and receipt_billing not in {
                "confirmed",
                "settled_overrun",
            }:
                findings.append(
                    {
                        "response_id": response_id,
                        "severity": "contradiction",
                        "code": "ledger_receipt_billing_disagreement",
                        "action": "inspect_private_recovery",
                    }
                )
    contradictions = sum(
        item["severity"] == "contradiction" for item in findings
    )
    attention = sum(item["severity"] == "attention" for item in findings)
    return {
        "status": "clear" if not findings else "attention_required",
        "project_id": project_id,
        "project_name": project_name,
        "responses_audited": audited,
        "contradiction_count": contradictions,
        "attention_count": attention,
        "unexplained_contradiction_count": contradictions,
        "findings": findings,
        "provider_dispatch_performed": False,
        "automatic_retry_started": False,
    }
