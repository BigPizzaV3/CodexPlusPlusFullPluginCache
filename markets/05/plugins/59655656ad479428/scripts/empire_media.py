#!/usr/bin/env python3
"""Minimal OpenRouter image/video generation for Empire LLM Codex."""

from __future__ import annotations

import argparse
import base64
import binascii
import hashlib
import json
import os
import re
import sys
import tempfile
import time
import uuid
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import HTTPRedirectHandler, HTTPSHandler, Request, build_opener

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
REVIEW_SCRIPTS = PLUGIN_ROOT / "skills" / "empire-review" / "scripts"
sys.path.insert(0, str(REVIEW_SCRIPTS))

from empire_budget import (  # noqa: E402
    BudgetError,
    BudgetStore,
    microusd_to_usd,
    project_identity,
    usd_to_microusd,
)
from empire_router import (  # noqa: E402
    ProviderRequestError,
    RouterError,
    credential_required_message,
    git,
    platform_cache_dir,
    platform_data_dir,
    redact_evidence,
    request_json,
    resolve_credential,
    resolve_model_icon,
    secret_findings,
    tls_context,
)

BASE = "https://openrouter.ai"
URLS = {
    "image": f"{BASE}/api/v1/images",
    "video": f"{BASE}/api/v1/videos",
}
CATALOG_TTL = timedelta(minutes=20)
MAX_STALE = timedelta(hours=24)
MAX_REFERENCE_BYTES = 10 * 1024 * 1024
MAX_IMAGE_BYTES = 25 * 1024 * 1024
MAX_VIDEO_BYTES = 250 * 1024 * 1024
MAX_MEDIA_PROMPT_CHARS = 4_000
JOB_ID = re.compile(r"^[A-Za-z0-9_-]{1,160}$")


class MediaError(Exception):
    pass


class RejectRedirects(HTTPRedirectHandler):
    def redirect_request(self, *args: Any, **kwargs: Any) -> None:
        raise MediaError("Video content redirect refused")


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def cache_path(kind: str) -> Path:
    return platform_cache_dir() / f"media-{kind}-models.json"


def media_root() -> Path:
    root = platform_data_dir() / "media"
    root.mkdir(parents=True, exist_ok=True)
    try:
        os.chmod(root, 0o700)
    except OSError:
        pass
    return root


def atomic_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
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
            handle.write(json.dumps(value, indent=2, sort_keys=True) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        try:
            os.chmod(path, 0o600)
        except OSError:
            pass
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def read_json(path: Path) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text())
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def parsed_time(value: Any) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(str(value))
        return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        return None


def credential() -> tuple[str, str]:
    value, source = resolve_credential(("OPENROUTER_API_KEY",), "openrouter")
    if not value:
        raise MediaError(
            credential_required_message(
                "OpenRouter", source, "run the Empire settings setup first"
            )
        )
    return value, source


def validate_media_prompt(value: str) -> str:
    prompt = value.strip()
    if not prompt:
        raise MediaError("A media prompt is required")
    if len(prompt) > MAX_MEDIA_PROMPT_CHARS:
        raise MediaError(
            f"Media prompt exceeds the {MAX_MEDIA_PROMPT_CHARS}-character limit"
        )
    if secret_findings(prompt):
        raise MediaError("Media prompt rejected by secret policy")
    return prompt


def fetch_catalog(kind: str, key: str) -> dict[str, Any]:
    payload = request_json(f"{URLS[kind]}/models", api_key=key)
    rows = payload.get("data")
    if not isinstance(rows, list):
        raise MediaError(f"OpenRouter {kind} catalog is malformed")
    now = utcnow()
    value = {
        "schema_version": "1.0",
        "kind": kind,
        "fetched_at": now.isoformat(),
        "expires_at": (now + CATALOG_TTL).isoformat(),
        "source": f"{URLS[kind]}/models",
        "data": [row for row in rows if isinstance(row, dict)],
    }
    atomic_json(cache_path(kind), value)
    return value


def catalog(kind: str, refresh: bool = False) -> tuple[dict[str, Any], str]:
    cached = read_json(cache_path(kind))
    fetched = parsed_time(cached.get("fetched_at")) if cached else None
    age = utcnow() - fetched if fetched else None
    if cached and not refresh and age is not None and age <= CATALOG_TTL:
        return cached, "fresh_cached"
    key, _ = credential()
    try:
        return fetch_catalog(kind, key), "live"
    except (RouterError, MediaError):
        if cached and age is not None and age <= MAX_STALE:
            return cached, "stale_fallback"
        raise


def model_rows(kind: str, refresh: bool = False) -> dict[str, Any]:
    payload, status = catalog(kind, refresh)
    rows = []
    for item in payload.get("data", []):
        model_id = str(item.get("id", ""))
        if not model_id:
            continue
        row = {
            "id": model_id,
            "name": item.get("name") or model_id,
            "openai": model_id.lower().startswith("openai/"),
            "supported_parameters": item.get("supported_parameters", {}),
            "supported_resolutions": item.get("supported_resolutions", []),
            "supported_aspect_ratios": item.get("supported_aspect_ratios", []),
            "supported_sizes": item.get("supported_sizes", []),
            "supported_durations": item.get("supported_durations", []),
            "supported_frame_images": item.get("supported_frame_images", []),
            "generate_audio": item.get("generate_audio"),
            "seed": item.get("seed"),
            "pricing_skus": item.get("pricing_skus", {}),
            "icon": resolve_model_icon(model_id, str(item.get("name") or model_id)),
        }
        rows.append(row)
    openai_count = sum(1 for row in rows if row["openai"])
    rows = [row for row in rows if not row["openai"]]
    return {
        "status": "ok",
        "kind": kind,
        "catalog_status": status,
        "fetched_at": payload.get("fetched_at"),
        "model_count": len(rows),
        "openai_excluded_count": openai_count,
        "models": rows,
    }


def endpoint_url(model: dict[str, Any]) -> str:
    value = model.get("endpoints")
    if not isinstance(value, str) or not value.startswith("/api/v1/images/models/"):
        raise MediaError("Image model did not publish an endpoint capability URL")
    return urljoin(BASE, value)


def descriptor_accepts(descriptor: Any, value: Any) -> bool:
    if not isinstance(descriptor, dict):
        return False
    kind = descriptor.get("type")
    if kind == "boolean":
        return True
    if kind == "enum":
        return value in descriptor.get("values", [])
    if kind == "range":
        try:
            return (
                Decimal(str(descriptor["min"]))
                <= Decimal(str(value))
                <= Decimal(str(descriptor["max"]))
            )
        except (KeyError, InvalidOperation):
            return False
    return False


def requested_parameters(args: argparse.Namespace) -> dict[str, Any]:
    names = (
        "n",
        "resolution",
        "aspect_ratio",
        "size",
        "quality",
        "output_format",
        "background",
        "duration",
        "generate_audio",
        "seed",
    )
    return {
        name: getattr(args, name)
        for name in names
        if hasattr(args, name) and getattr(args, name) is not None
    }


def image_endpoint_accepts(
    endpoint: dict[str, Any], parameters: dict[str, Any]
) -> bool:
    supported = endpoint.get("supported_parameters")
    if not isinstance(supported, dict):
        return not parameters
    for name, value in parameters.items():
        if name == "n" and value == 1 and name not in supported:
            continue
        if name not in supported or not descriptor_accepts(supported[name], value):
            return False
    return True


def video_model_accepts(model: dict[str, Any], parameters: dict[str, Any]) -> bool:
    mappings = {
        "resolution": "supported_resolutions",
        "aspect_ratio": "supported_aspect_ratios",
        "size": "supported_sizes",
    }
    for name, field in mappings.items():
        if name in parameters:
            values = model.get(field)
            if not isinstance(values, list) or parameters[name] not in values:
                return False
    duration = parameters.get("duration")
    durations = model.get("supported_durations")
    if (
        duration is not None
        and isinstance(durations, list)
        and duration not in durations
    ):
        return False
    if "generate_audio" in parameters:
        audio_capability = model.get("generate_audio")
        if parameters["generate_audio"] is True and audio_capability is not True:
            return False
        if parameters["generate_audio"] is False and audio_capability not in {
            True,
            False,
        }:
            return False
    if parameters.get("seed") is not None and model.get("seed") is False:
        return False
    return True


def decimal_cost(value: Any) -> Decimal | None:
    try:
        result = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError):
        return None
    return result if result.is_finite() and result >= 0 else None


def image_estimate(
    endpoint: dict[str, Any], parameters: dict[str, Any]
) -> Decimal | None:
    lines = endpoint.get("pricing")
    if not isinstance(lines, list) or not lines:
        return None
    count = int(parameters.get("n", 1))
    total = Decimal("0")
    for line in lines:
        if not isinstance(line, dict):
            return None
        cost = decimal_cost(line.get("cost_usd"))
        unit = line.get("unit")
        billable = str(line.get("billable", ""))
        if cost is None:
            return None
        if unit in {"image", "generation", "request"}:
            total += cost * (count if "output" in billable or unit == "image" else 1)
        else:
            return None
    return total


def video_estimate(
    model: dict[str, Any], parameters: dict[str, Any], has_reference: bool = False
) -> Decimal | None:
    skus = model.get("pricing_skus")
    duration = parameters.get("duration")
    if not isinstance(skus, dict) or duration is None:
        return None
    resolution = str(parameters.get("resolution", "")).lower()
    audio = parameters.get("generate_audio")
    mode = "image_to_video" if has_reference else "text_to_video"
    candidates: list[tuple[int, Decimal]] = []
    for raw_name, raw_cost in skus.items():
        name = str(raw_name).lower().replace("-", "_")
        cost = decimal_cost(raw_cost)
        if cost is None or "second" not in name:
            continue
        if name.startswith("cents_per_"):
            cost /= 100
        score = 0
        if name.startswith(mode):
            score += 12
        elif name.startswith("image_to_video") or name.startswith("text_to_video"):
            continue
        if resolution:
            if resolution in name:
                score += 8
            elif re.search(r"(?:480p|720p|1080p|1024p|4k)", name):
                continue
        if audio is True:
            if "with_audio" in name:
                score += 5
            elif "without_audio" in name:
                continue
        elif audio is False:
            if "without_audio" in name:
                score += 5
            elif "with_audio" in name:
                continue
        elif "with_audio" in name:
            score += 1
        candidates.append((score, cost))
    if not candidates:
        return None
    best_score = max(score for score, _ in candidates)
    # When audio/provider defaults remain unspecified, authorize the most
    # expensive equally applicable line rather than understating cost.
    cost = max(cost for score, cost in candidates if score == best_score)
    return cost * int(duration) if cost is not None else None


def normalized_usd(value: Decimal | None) -> str | None:
    return None if value is None else format(value.quantize(Decimal("0.000001")), "f")


def approval_hash(route: dict[str, Any]) -> str:
    content = {
        "kind": route["kind"],
        "model_id": route["model_id"],
        "endpoint_provider": route.get("endpoint_provider"),
        "parameters": route["parameters"],
        "estimated_cost_usd": route.get("estimated_cost_usd"),
        "price_snapshot_id": route["price_snapshot_id"],
        "cost_mode": route.get("cost_mode", "auto"),
    }
    encoded = json.dumps(content, sort_keys=True, separators=(",", ":")).encode()
    return "route-" + hashlib.sha256(encoded).hexdigest()[:24]


def select_route(args: argparse.Namespace) -> dict[str, Any]:
    kind = args.kind
    payload, status = catalog(kind, bool(getattr(args, "refresh", False)))
    parameters = requested_parameters(args)
    requested = getattr(args, "model", None)
    candidates = [
        item
        for item in payload.get("data", [])
        if isinstance(item, dict) and item.get("id")
    ]
    if requested:
        if str(requested).lower().startswith("openai/"):
            raise MediaError(
                "OpenAI media models are outside Empire routing; use the native OpenAI media workflow"
            )
        candidates = [item for item in candidates if item.get("id") == requested]
        if not candidates and status != "live":
            payload, status = catalog(kind, True)
            candidates = [
                item
                for item in payload.get("data", [])
                if isinstance(item, dict) and item.get("id") == requested
            ]
        if not candidates:
            raise MediaError(f"Requested {kind} model is unavailable: {requested}")
    else:
        candidates = [
            item
            for item in candidates
            if not str(item.get("id", "")).lower().startswith("openai/")
        ]

    key, source = credential()
    routes: list[dict[str, Any]] = []
    if kind == "image":

        def image_details(
            model: dict[str, Any],
        ) -> tuple[dict[str, Any], dict[str, Any]] | None:
            try:
                details = request_json(endpoint_url(model), api_key=key)
            except (RouterError, MediaError):
                if requested:
                    raise
                return None
            return model, details

        workers = min(6, max(1, len(candidates)))
        if workers == 1:
            detail_rows = [image_details(model) for model in candidates]
        else:
            with ThreadPoolExecutor(max_workers=workers) as executor:
                detail_rows = list(executor.map(image_details, candidates))
        for detail_row in detail_rows:
            if detail_row is None:
                continue
            model, details = detail_row
            eligibility_parameters = dict(parameters)
            if getattr(args, "reference", []):
                eligibility_parameters["input_references"] = len(args.reference)
            for endpoint in details.get("endpoints", []):
                if not isinstance(endpoint, dict) or not endpoint.get("provider_tag"):
                    continue
                if not image_endpoint_accepts(endpoint, eligibility_parameters):
                    continue
                estimate = image_estimate(endpoint, parameters)
                routes.append(
                    {"model": model, "endpoint": endpoint, "estimate": estimate}
                )
    else:
        for model in candidates:
            if getattr(args, "reference", []) and "first_frame" not in (
                model.get("supported_frame_images") or []
            ):
                continue
            if video_model_accepts(model, parameters):
                routes.append(
                    {
                        "model": model,
                        "endpoint": None,
                        "estimate": video_estimate(
                            model, parameters, bool(getattr(args, "reference", []))
                        ),
                    }
                )
    cost_mode = getattr(args, "cost_mode", "auto")
    if cost_mode == "free":
        routes = [row for row in routes if row["estimate"] == Decimal("0")]
    if not routes:
        if cost_mode == "free":
            raise MediaError(
                "No proven zero-cost media endpoint satisfies the requested parameters; paid fallback is disabled"
            )
        raise MediaError("No current endpoint satisfies the requested media parameters")
    routes.sort(
        key=lambda row: (
            row["estimate"] is None,
            row["estimate"] if row["estimate"] is not None else Decimal("Infinity"),
            str(row["model"].get("id")),
        )
    )
    selected = routes[0]
    model = selected["model"]
    endpoint = selected["endpoint"]
    pricing = endpoint.get("pricing", []) if endpoint else model.get("pricing_skus", {})
    snapshot_payload = json.dumps(
        {
            "provider": "openrouter",
            "model_id": model["id"],
            "media_pricing": pricing,
            "parameters": parameters,
            "catalog_fetched_at": payload.get("fetched_at"),
        },
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    snapshot = "price-" + hashlib.sha256(snapshot_payload).hexdigest()[:20]
    route = {
        "status": "route_ready",
        "kind": kind,
        "selection_mode": "user_pinned" if requested else "automatic",
        "cost_mode": cost_mode,
        "catalog_status": status,
        "catalog_fetched_at": payload.get("fetched_at"),
        "credential_source": source,
        "model_id": model["id"],
        "model_name": model.get("name") or model["id"],
        "endpoint_provider": endpoint.get("provider_tag") if endpoint else None,
        "endpoint_provider_name": endpoint.get("provider_name") if endpoint else None,
        "parameters": parameters,
        "pricing": pricing,
        "estimated_cost_usd": normalized_usd(selected["estimate"]),
        "price_snapshot_id": snapshot,
        "benchmark_evidence": "unavailable",
        "icon": resolve_model_icon(str(model["id"]), str(model.get("name") or "")),
        "requires_explicit_cost_approval": True,
        "warnings": [
            "Estimate is unavailable; supply an explicit maximum cost before dispatch."
        ]
        if selected["estimate"] is None
        else [],
    }
    route["approval_token"] = approval_hash(route)
    if status == "stale_fallback":
        route["warnings"].append(
            "Stale catalog may be inspected, but generation requires live or fresh metadata."
        )
    return route


def project(repo_value: str) -> tuple[str, str]:
    repo = Path(repo_value).expanduser().resolve()
    if not repo.is_dir():
        raise MediaError(f"Repository is not a directory: {repo}")
    try:
        root = Path(git(repo, "rev-parse", "--show-toplevel").strip()).resolve()
    except RouterError:
        root = repo
    return project_identity(root)


def approved_microusd(args: argparse.Namespace, route: dict[str, Any]) -> int:
    if args.approve_route != route["approval_token"]:
        raise MediaError(
            "Route changed or was not explicitly approved; preview it again"
        )
    estimate = route.get("estimated_cost_usd")
    approved = getattr(args, "approve_cost", None)
    if approved is None:
        raise MediaError("Explicit --approve-cost is required before generation")
    value = usd_to_microusd(approved)
    if estimate is not None and value < usd_to_microusd(estimate):
        raise MediaError("Approved cost is below the current route estimate")
    return value


def reserve(args: argparse.Namespace, route: dict[str, Any]) -> tuple[str, int]:
    maximum = approved_microusd(args, route)
    project_id, project_name = project(args.repo)
    with BudgetStore() as store:
        reservation_id, state = store.reserve(
            project_id,
            project_name,
            "openrouter-media",
            route["model_id"],
            maximum,
            route["price_snapshot_id"],
            ttl_seconds=86400 if route["kind"] == "video" else 900,
        )
    if not reservation_id:
        raise MediaError(
            f"Project budget cannot authorize this route: {state.get('status')}"
        )
    return reservation_id, maximum


def release(reservation_id: str) -> None:
    with BudgetStore() as store:
        store.release(reservation_id)


def settle(reservation_id: str, route: dict[str, Any], cost: Any) -> dict[str, Any]:
    observed = usd_to_microusd(str(cost))
    with BudgetStore() as store:
        return store.settle(
            reservation_id,
            observed,
            route["model_id"],
            route["price_snapshot_id"],
        )


def reference_data(path_value: str) -> dict[str, Any]:
    path = Path(path_value).expanduser().resolve()
    if not path.is_file():
        raise MediaError(f"Reference is not a readable file: {path}")
    try:
        if path.stat().st_size > MAX_REFERENCE_BYTES:
            raise MediaError("Reference image exceeds the 10 MB limit")
        with path.open("rb") as handle:
            data = handle.read(MAX_REFERENCE_BYTES + 1)
    except OSError as exc:
        raise MediaError(f"Reference image could not be read: {path}") from exc
    if len(data) > MAX_REFERENCE_BYTES:
        raise MediaError("Reference image exceeds the 10 MB limit")
    mime = sniff_image(data)
    encoded = base64.b64encode(data).decode("ascii")
    return {
        "type": "image_url",
        "image_url": {"url": f"data:{mime};base64,{encoded}"},
    }


def sniff_image(data: bytes) -> str:
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "image/png"
    if data.startswith(b"\xff\xd8\xff"):
        return "image/jpeg"
    if len(data) >= 12 and data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "image/webp"
    raise MediaError("Unsupported or invalid image bytes")


def decode_image(item: dict[str, Any]) -> tuple[bytes, str]:
    encoded = item.get("b64_json")
    if not isinstance(encoded, str):
        raise MediaError("Image response did not contain base64 bytes")
    if len(encoded) > (MAX_IMAGE_BYTES * 4 // 3) + 16:
        raise MediaError("Encoded image exceeds the maximum size")
    try:
        data = base64.b64decode(encoded, validate=True)
    except (binascii.Error, ValueError) as exc:
        raise MediaError("Image response contains invalid base64") from exc
    if len(data) > MAX_IMAGE_BYTES:
        raise MediaError("Image exceeds the 25 MB limit")
    mime = sniff_image(data)
    declared = item.get("media_type")
    if declared is not None and declared != mime:
        raise MediaError("Image MIME does not match its bytes")
    return data, mime


def artifact_path(kind: str, artifact_id: str, suffix: str) -> Path:
    folder = media_root() / artifact_id
    folder.mkdir(mode=0o700, parents=True, exist_ok=False)
    return folder / f"artifact.{suffix}"


def write_private_bytes(path: Path, data: bytes) -> None:
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, "wb") as handle:
        handle.write(data)


def file_sha256(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
            size += len(chunk)
    return digest.hexdigest(), size


def artifact_receipt(path: Path, route: dict[str, Any], cost: Any) -> dict[str, Any]:
    digest, size = file_sha256(path)
    return {
        "artifact_id": path.parent.name,
        "kind": route["kind"],
        "state": "quarantined",
        "path": str(path),
        "sha256": digest,
        "bytes": size,
        "model_id": route["model_id"],
        "endpoint_provider": route.get("endpoint_provider"),
        "actual_cost_usd": normalized_usd(decimal_cost(cost)),
        "icon": route["icon"],
        "repository_changed": False,
    }


def image_generate(args: argparse.Namespace) -> dict[str, Any]:
    route = select_route(args)
    if route.get("catalog_status") == "stale_fallback":
        raise MediaError(
            "Generation is blocked while only a stale catalog is available"
        )
    references = [reference_data(value) for value in args.reference]
    reservation_id, approved = reserve(args, route)
    key, _ = credential()
    body = {"model": route["model_id"], "prompt": args.prompt, **route["parameters"]}
    if route.get("endpoint_provider"):
        body["provider"] = {
            "only": [route["endpoint_provider"]],
            "allow_fallbacks": False,
        }
    if references:
        body["input_references"] = references
    try:
        response = request_json(URLS["image"], api_key=key, body=body, timeout=300)
    except ProviderRequestError:
        release(reservation_id)
        raise
    except RouterError as exc:
        raise MediaError(
            f"Image submission outcome is unknown; reservation {reservation_id} remains pending: {exc}"
        ) from exc
    cost = response.get("usage", {}).get("cost")
    if cost is None:
        cost = route.get("estimated_cost_usd")
    budget = settle(reservation_id, route, cost) if cost is not None else None
    rows = response.get("data")
    if not isinstance(rows, list) or not rows:
        raise MediaError("Image response contained no completed artifact")
    data, mime = decode_image(rows[0])
    suffix = {"image/png": "png", "image/jpeg": "jpg", "image/webp": "webp"}[mime]
    path = artifact_path("image", "img-" + uuid.uuid4().hex, suffix)
    write_private_bytes(path, data)
    receipt = artifact_receipt(path, route, cost)
    receipt.update(
        {
            "status": "completed",
            "mime": mime,
            "reservation_id": reservation_id,
            "approved_max_cost_usd": microusd_to_usd(approved),
            "budget": budget,
            "cost_state": "settled" if budget is not None else "provider_cost_unknown",
        }
    )
    atomic_json(path.parent / "receipt.json", receipt)
    return receipt


def job_path(job_id: str) -> Path:
    if not JOB_ID.fullmatch(job_id):
        raise MediaError("Invalid video job ID")
    return media_root() / "jobs" / f"{job_id}.json"


def save_job(job: dict[str, Any]) -> None:
    atomic_json(job_path(str(job["job_id"])), job)


def load_job(job_id: str) -> dict[str, Any]:
    value = read_json(job_path(job_id))
    if not value:
        raise MediaError(f"Unknown local video job: {job_id}")
    return value


def video_generate(args: argparse.Namespace) -> dict[str, Any]:
    route = select_route(args)
    if route.get("catalog_status") == "stale_fallback":
        raise MediaError(
            "Generation is blocked while only a stale catalog is available"
        )
    if len(args.reference) > 1:
        raise MediaError("The MVP accepts one first-frame video reference")
    frame = reference_data(args.reference[0]) if args.reference else None
    if frame is not None:
        frame["frame_type"] = "first_frame"
    reservation_id, approved = reserve(args, route)
    key, _ = credential()
    body = {"model": route["model_id"], "prompt": args.prompt, **route["parameters"]}
    if frame is not None:
        body["frame_images"] = [frame]
    try:
        response = request_json(URLS["video"], api_key=key, body=body, timeout=60)
    except ProviderRequestError:
        release(reservation_id)
        raise
    except RouterError as exc:
        raise MediaError(
            f"Video submission outcome is unknown; reservation {reservation_id} remains pending: {exc}"
        ) from exc
    job_id = str(response.get("id", ""))
    if not JOB_ID.fullmatch(job_id):
        raise MediaError(
            f"Video submission returned no safe job ID; reservation {reservation_id} remains pending"
        )
    job = {
        "schema_version": "1.0",
        "job_id": job_id,
        "kind": "video",
        "status": response.get("status") or "pending",
        "model_id": route["model_id"],
        "parameters": route["parameters"],
        "reservation_id": reservation_id,
        "approved_max_cost_usd": microusd_to_usd(approved),
        "price_snapshot_id": route["price_snapshot_id"],
        "estimated_cost_usd": route.get("estimated_cost_usd"),
        "icon": route["icon"],
        "created_at": utcnow().isoformat(),
        "updated_at": utcnow().isoformat(),
        "contains_prompt": False,
    }
    save_job(job)
    return job


def video_status(job_id: str) -> dict[str, Any]:
    job = load_job(job_id)
    key, _ = credential()
    response = request_json(f"{URLS['video']}/{job_id}", api_key=key, timeout=30)
    status = str(response.get("status") or job.get("status") or "unknown")
    job["status"] = status
    job["updated_at"] = utcnow().isoformat()
    raw_usage = response.get("usage")
    usage: dict[str, Any] = raw_usage if isinstance(raw_usage, dict) else {}
    cost = usage.get("cost")
    if cost is not None and not job.get("settled"):
        route = {
            "kind": "video",
            "model_id": job["model_id"],
            "price_snapshot_id": job["price_snapshot_id"],
        }
        job["budget"] = settle(job["reservation_id"], route, cost)
        job["actual_cost_usd"] = normalized_usd(decimal_cost(cost))
        job["settled"] = True
    elif status == "failed" and cost is None:
        job["cost_state"] = "provider_cost_unknown"
    if response.get("error"):
        error, _ = redact_evidence(str(response["error"]))
        job["error"] = error[:1000]
    save_job(job)
    return job


def download_video(job: dict[str, Any]) -> dict[str, Any]:
    if job.get("status") != "completed":
        raise MediaError("Video is not complete")
    existing = job.get("artifact")
    if isinstance(existing, dict) and isinstance(existing.get("path"), str):
        existing_path = Path(existing["path"]).expanduser().resolve()
        root = media_root().resolve()
        if root in existing_path.parents and existing_path.is_file():
            digest, size = file_sha256(existing_path)
            if digest == existing.get("sha256") and size == existing.get("bytes"):
                return existing
        raise MediaError("Stored video artifact failed integrity validation")
    key, _ = credential()
    url = f"{URLS['video']}/{job['job_id']}/content?index=0"
    request = Request(
        url,
        headers={
            "Authorization": f"Bearer {key}",
            "Accept": "video/mp4",
            "User-Agent": "empire-media/0.1",
        },
    )
    try:
        opener = build_opener(RejectRedirects(), HTTPSHandler(context=tls_context()))
        with opener.open(request, timeout=120) as response:
            content_length = response.headers.get("Content-Length")
            if content_length and int(content_length) > MAX_VIDEO_BYTES:
                raise MediaError("Video exceeds the 250 MB limit")
            data = response.read(MAX_VIDEO_BYTES + 1)
    except (HTTPError, URLError, TimeoutError, ValueError) as exc:
        raise MediaError(f"Video download failed: {exc}") from exc
    if len(data) > MAX_VIDEO_BYTES:
        raise MediaError("Video exceeds the 250 MB limit")
    if len(data) < 12 or data[4:8] != b"ftyp":
        raise MediaError("Downloaded video is not a valid MP4 container")
    path = artifact_path("video", "vid-" + uuid.uuid4().hex, "mp4")
    write_private_bytes(path, data)
    route = {
        "kind": "video",
        "model_id": job["model_id"],
        "endpoint_provider": None,
        "icon": job["icon"],
    }
    receipt = artifact_receipt(path, route, job.get("actual_cost_usd"))
    receipt.update(
        {
            "status": "completed",
            "mime": "video/mp4",
            "job_id": job["job_id"],
            "reservation_id": job["reservation_id"],
            "approved_max_cost_usd": job["approved_max_cost_usd"],
            "cost_state": "settled" if job.get("settled") else "settlement_pending",
        }
    )
    atomic_json(path.parent / "receipt.json", receipt)
    job["artifact"] = receipt
    save_job(job)
    return receipt


def video_wait(job_id: str, timeout: int) -> dict[str, Any]:
    # Keep every Codex-side poll bounded. The persisted job ID is resumable, so
    # a caller can explicitly request another short poll without hiding a long
    # blocking operation inside one turn.
    deadline = time.monotonic() + max(1, min(timeout, 60))
    delay = 5.0
    while True:
        job = video_status(job_id)
        if job["status"] == "completed":
            return download_video(job)
        if job["status"] == "failed":
            return job
        if time.monotonic() >= deadline:
            return {**job, "status": "timed_out", "resumable": True}
        time.sleep(delay)
        delay = min(30.0, delay * 1.6)


def media_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=("image", "video"))
    parser.add_argument(
        "action", choices=("models", "route", "generate", "status", "wait")
    )
    parser.add_argument("prompt", nargs="?")
    parser.add_argument("--model")
    parser.add_argument("--cost-mode", choices=("auto", "free"), default="auto")
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--approve-route")
    parser.add_argument("--approve-cost")
    parser.add_argument("--reference", action="append", default=[])
    parser.add_argument("--job")
    parser.add_argument("--timeout", type=int, default=45)
    parser.add_argument("--n", type=int)
    parser.add_argument("--resolution")
    parser.add_argument("--aspect-ratio", dest="aspect_ratio")
    parser.add_argument("--size")
    parser.add_argument("--quality")
    parser.add_argument("--output-format", dest="output_format")
    parser.add_argument("--background")
    parser.add_argument("--duration", type=int)
    audio = parser.add_mutually_exclusive_group()
    audio.add_argument("--audio", dest="generate_audio", action="store_true")
    audio.add_argument("--no-audio", dest="generate_audio", action="store_false")
    parser.set_defaults(generate_audio=None)
    parser.add_argument("--seed", type=int)
    return parser


def validate_args(args: argparse.Namespace) -> None:
    if args.action in {"route", "generate"} and not args.prompt:
        raise MediaError("A media prompt is required")
    if args.prompt:
        args.prompt = validate_media_prompt(args.prompt)
    if args.action in {"status", "wait"}:
        if args.kind != "video" or not args.job:
            raise MediaError("Video status/wait requires --job")
    if args.kind == "image" and args.duration is not None:
        raise MediaError("--duration is video-only")
    if args.kind == "video" and args.n is not None:
        raise MediaError("--n is image-only")
    if args.n is not None and not 1 <= args.n <= 10:
        raise MediaError("--n must be between 1 and 10")
    if args.duration is not None and not 1 <= args.duration <= 120:
        raise MediaError("--duration must be between 1 and 120 seconds")


def run(args: argparse.Namespace) -> dict[str, Any]:
    validate_args(args)
    if args.action == "models":
        return model_rows(args.kind, args.refresh)
    if args.action == "route":
        return select_route(args)
    if args.action == "generate":
        return image_generate(args) if args.kind == "image" else video_generate(args)
    if args.action == "status":
        return video_status(args.job)
    return video_wait(args.job, args.timeout)


def main() -> int:
    parser = media_args()
    try:
        result = run(parser.parse_args())
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    except (MediaError, RouterError, BudgetError, ValueError) as exc:
        print(json.dumps({"status": "error", "error": str(exc)}, indent=2))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
