import json
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
DATASITE_APP_ID = "asdk_app_69eba17551ac81918231c83822b703b6"


def test_investment_banking_declares_datasite_app_dependency() -> None:
    manifest = json.loads((PLUGIN_ROOT / ".codex-plugin" / "plugin.json").read_text())
    app_config = json.loads((PLUGIN_ROOT / ".app.json").read_text())

    assert manifest["apps"] == "./.app.json"
    assert app_config["apps"]["datasite"]["id"] == DATASITE_APP_ID
