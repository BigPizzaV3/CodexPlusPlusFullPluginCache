import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
PLUGIN_ROOT = REPO_ROOT / "plugins" / "zendesk"
ZENDESK_CONNECTOR_ID = "connector_47d5e934d8f546b98f2d2db564ca04a3"


def test_zendesk_plugin_manifest_and_app_paths_exist() -> None:
    manifest = json.loads((PLUGIN_ROOT / ".codex-plugin" / "plugin.json").read_text())
    app_manifest = json.loads((PLUGIN_ROOT / ".app.json").read_text())

    assert manifest["name"] == "zendesk"
    assert "skills" not in manifest
    assert manifest["apps"] == "./.app.json"
    assert manifest["interface"]["displayName"] == "Zendesk"
    assert app_manifest == {"apps": {"zendesk": {"id": ZENDESK_CONNECTOR_ID}}}
    assert (PLUGIN_ROOT / "assets" / "zendesk.svg").is_file()


def test_zendesk_plugin_is_registered_in_marketplace() -> None:
    marketplace = json.loads((REPO_ROOT / "marketplace.json").read_text())
    entry = next(plugin for plugin in marketplace["plugins"] if plugin["name"] == "zendesk")

    assert entry["source"]["path"] == "./plugins/zendesk"
    assert entry["policy"] == {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL",
    }
    assert entry["category"] == "Business & Operations"
