#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    try:
      return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
      raise SystemExit(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc


def require_file(relative: str) -> None:
    path = ROOT / relative.removeprefix("./")
    if not path.is_file():
        raise SystemExit(f"Missing required file: {relative}")


def require_https_origin_or_mcp(url: str, field: str) -> None:
    if not url.startswith("https://"):
        raise SystemExit(f"{field} must use https:// for publication: {url}")
    if "?" in url or "#" in url or "@" in url.split("://", 1)[1].split("/", 1)[0]:
        raise SystemExit(f"{field} must not include credentials, query, or fragment: {url}")


def main() -> int:
    plugin = load_json(ROOT / "plugin.json")
    if plugin.get("name") != "pretture-erp-ai":
        raise SystemExit("plugin.json name must remain the stable package id pretture-erp-ai")
    if "extensions" not in plugin or "com.openai" not in plugin["extensions"]:
        raise SystemExit("plugin.json must include extensions.com.openai")

    openai = plugin["extensions"]["com.openai"]
    interface = openai.get("interface") or {}
    for key in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        if not interface.get(key):
            raise SystemExit(f"Missing interface.{key}")
    for key in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        require_https_origin_or_mcp(interface[key], f"interface.{key}")

    for asset_key in ("composerIcon", "logo"):
        require_file(interface[asset_key])
    for screenshot in interface.get("screenshots", []):
        require_file(screenshot)

    onboarding = openai.get("onboardingSkill")
    if onboarding:
        require_file(onboarding)

    mcp = load_json(ROOT / "mcp.json")
    server = (mcp.get("mcpServers") or {}).get("pretture-erp")
    if not server:
        raise SystemExit("mcp.json must define mcpServers.pretture-erp")
    if server.get("type") != "streamable-http":
        raise SystemExit("mcpServers.pretture-erp.type must be streamable-http")
    require_https_origin_or_mcp(server.get("url", ""), "mcpServers.pretture-erp.url")
    if not server["url"].endswith("/mcp"):
        raise SystemExit("MCP URL must end with /mcp")

    compat = load_json(ROOT / ".codex-plugin" / "plugin.json")
    if compat.get("name") != plugin["name"]:
        raise SystemExit(".codex-plugin/plugin.json name must match plugin.json")
    load_json(ROOT / ".mcp.json")
    print("Plugin package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
