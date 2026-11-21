"""Edition-specific minimisation and checkpoint input controls."""
from __future__ import annotations

import copy
import os
from pathlib import Path
import re
import stat
import tomllib

from .storage import WeatherError, MAX_JSON


def read_selected_file(path, limit=MAX_JSON):
    path = Path(path).absolute()
    if path.is_symlink() or any(p.is_symlink() for p in path.parents):
        raise WeatherError("Selected file must not use symlinks")
    descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(descriptor, "rb") as stream:
        if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
            raise WeatherError("Selected input must be a regular file")
        raw = stream.read(limit + 1)
    if len(raw) > limit:
        raise WeatherError("Selected input exceeds its byte limit")
    return raw


def reference_config(path):
    result = {}
    for line in read_selected_file(path).splitlines():
        stripped = line.strip()
        if stripped.startswith(b"["):
            break  # Only the supported top-level reference fields are relevant.
        match = re.match(rb"(model|model_auto_compact_token_limit|model_auto_compact_token_limit_scope)\s*=", stripped)
        if not match:
            continue
        if len(stripped) > 4096:
            raise WeatherError("Reference field exceeds limit")
        result.update(tomllib.loads(stripped.decode()))
    return result


def check_exports(paths, workspace):
    """Exports are additive and cannot target Codex or plugin-owned storage."""
    selected = [Path(path).absolute() for path in paths if path is not None]
    if len(set(selected)) != len(selected):
        raise WeatherError("Choose different output paths for each export")
    home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")).expanduser().absolute()
    cache = Path(os.environ.get("TOKEN_WEATHER_SKILLS_DATA_DIR", home / "state/token-weather-skills")).expanduser().absolute()
    for path in selected:
        if ".." in path.parts or path.exists() or path.is_symlink() or any(p.is_symlink() for p in path.parents):
            raise WeatherError("Export must use a new file without symlinks")
        if any(path.is_relative_to(root) for root in (home, cache, workspace / ".codex")):
            raise WeatherError("Export must be outside Codex and plugin-owned storage")


def public_weather(report):
    result = copy.deepcopy(report)
    result.pop("thread_id", None)
    for sample in result.get("samples", []):
        sample.pop("turn", None)
    if result.get("last_request"):
        result["last_request"].pop("turn", None)
    if str(result.get("limit_source", "")).startswith("disk candidate:"):
        result["limit_source"] = "explicitly requested local reference configuration"
    if "collection" in result:
        result["collection"] = {key: result["collection"][key] for key in (
            "catching_up", "numeric_samples_retained") if key in result["collection"]}
    return result


def public_replay(report, control=False):
    if control:
        result = {key: copy.deepcopy(report[key]) for key in (
            "schema_version", "kind", "engine_version", "acceptance_scope", "production_promotion",
            "revision", "connected", "interrupt_attempt", "terminal_event", "source_terminal",
            "quiescent", "reasons", "reason") if key in report}
        result.update(inventory=None, member_count=len(report.get("members", {})),
                      active_operation_count=len(report.get("active_operations", [])),
                      unknown_effect_count=len(report.get("unknown_effects", [])))
        return result
    def minimise(value):
        if isinstance(value, dict):
            return {key: minimise(item) for key, item in value.items() if key not in {
                "thread_id", "turn_id", "workspace", "connection_id", "model_fingerprint", "pending_tools"}}
        if isinstance(value, list):
            return [minimise(item) for item in value]
        return value
    return minimise(report)


SECRET = re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{16,}|-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----|\b(?:api[_ -]?key|password|access[_ -]?token|client[_ -]?secret)\s*[:=]\s*\S+", re.I)
SECRET_FIELDS = {"password", "apikey", "accesstoken", "refreshtoken", "clientsecret", "privatekey", "otp", "mfacode"}


def validate_notes(value, workspace):
    """Reject common credential forms; never silently rewrite requested notes.

    Pattern checks are not a sensitive-data detector. The author must still
    choose task-specific text and exclude restricted and unnecessary data.
    """
    def walk(item):
        if isinstance(item, str) and SECRET.search(item):
            raise WeatherError("Remove credentials from checkpoint input")
        if isinstance(item, dict):
            for key, child in item.items():
                if isinstance(key, str) and re.sub(r"[_ -]", "", key.lower()) in SECRET_FIELDS:
                    raise WeatherError("Credential fields are not checkpoint task data")
                walk(key)
                walk(child)
        elif isinstance(item, list):
            for child in item:
                walk(child)
    walk(value)
    if isinstance(value, dict):
        for row in value.get("evidence", []):
            if not isinstance(row, dict):
                raise WeatherError("Evidence record must be an object")
            if row.get("cache_id") is not None:
                raise WeatherError("External verification-cache references are not supported in this edition")
            if row.get("sha256") is not None and (not isinstance(row["sha256"], str) or not re.fullmatch(r"[a-f0-9]{64}", row["sha256"])):
                raise WeatherError("Evidence hash must be a SHA-256 hex digest")
            if row.get("path") is not None:
                path = Path(row["path"])
                if path.is_absolute() or ".." in path.parts or not path.parts:
                    raise WeatherError("Evidence path must be relative to the enrolled workspace")
                target = workspace / path
                if target.is_symlink() or any(p.is_symlink() for p in target.parents):
                    raise WeatherError("Evidence path must not use symlinks")
    return value
