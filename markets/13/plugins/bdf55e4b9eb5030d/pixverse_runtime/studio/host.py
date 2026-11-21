"""Installed host capabilities; no browser or credential discovery."""

from __future__ import annotations

import json
from pathlib import Path

from .state import plugin_root

HOSTS = {"codex", "claude", "cursor", "portable"}


def plugin_host(root: Path | None = None) -> str:
    root = root or plugin_root()
    profile = root / ".pixverse-runtime.json"
    if profile.is_file():
        payload = json.loads(profile.read_text(encoding="utf-8"))
        if (
            not isinstance(payload, dict)
            or set(payload) != {"schema_version", "host"}
            or payload.get("schema_version") != 1
            or payload.get("host") not in HOSTS
        ):
            raise ValueError("Invalid PixVerse runtime host profile")
        return str(payload["host"])
    if (root / ".codex-plugin/plugin.json").is_file():
        return "codex"
    return "portable"


def browser_requirement() -> str:
    return "iab_handoff" if plugin_host() == "codex" else "host_or_user_browser_handoff"


def portable_browser_handoff(url: str, *, reuse_existing: bool = True) -> dict:
    return {
        "host": plugin_host(),
        "surface": "host_or_user_browser",
        "url": url,
        "reuse_existing": reuse_existing,
        "system_browser_opened": False,
        "instructions": (
            "Use a browser control explicitly available in this host, or return this exact link "
            "for the user to open. Keep an OAuth polling process alive until authorization finishes. "
            "Do not invent browser tools, copy credentials, or open a system browser automatically."
        ),
    }
