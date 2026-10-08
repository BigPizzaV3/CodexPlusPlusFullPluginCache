"""Rollout contract for the maintained Codex Replay plugin."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
CATALOG_ROOT = PLUGIN_ROOT.parents[1]


class MaintainedCatalogTests(unittest.TestCase):
    def test_replay_remains_codex_only_and_statsig_gated(self) -> None:
        marketplace = json.loads((CATALOG_ROOT / "marketplace.json").read_text(encoding="utf-8"))
        entries = [entry for entry in marketplace["plugins"] if entry["name"] == "codex-replay"]

        self.assertEqual(len(entries), 1)
        self.assertEqual(
            entries[0]["source"],
            {"source": "local", "path": "./plugins/codex-replay"},
        )
        self.assertEqual(
            entries[0]["policy"],
            {
                "installation": "AVAILABLE",
                "authentication": "ON_INSTALL",
                "products": ["CODEX"],
                "statsigGate": "codex_replay_early_access",
            },
        )


if __name__ == "__main__":
    unittest.main()
