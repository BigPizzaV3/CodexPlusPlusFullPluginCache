"""Regression for optional Build_ starter, preserving the older phrase."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SCRIPTS = ROOT / "skills" / "build" / "scripts"
sys.path.insert(0, str(SCRIPTS))
from guide import guidance

class StartPromptTest(unittest.TestCase):
    def test_starter_is_manifest_data_only(self):
        m = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(m["interface"]["defaultPrompt"], ["Press Enter to begin"])
        self.assertEqual(m["interface"]["displayName"], "Build_")
        for field in ("placeholder", "composerPlaceholder", "onClick", "onFocus"):
            self.assertNotIn(field, m["interface"])
    def test_new_and_legacy_starters_welcome_without_build(self):
        for phrase in ("Press Enter to begin", "Press Enter to start"):
            with self.subTest(phrase=phrase):
                r = guidance(phrase)
                self.assertEqual(r["route"], "welcome")
                self.assertFalse(r["build_authorized"])
                self.assertIn("What would you like to make?", r["text"])
    def test_listing_explains_one_press_welcome(self):
        m = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        desc = m["interface"]["longDescription"]
        self.assertIn("press Enter for the welcome", desc)
        self.assertIn("Press Enter to begin", desc)
        self.assertIn("type your app idea immediately", desc)

    def test_direct_app_request_is_untouched(self):
        r = guidance("Build me a counter that saves its value")
        self.assertFalse(r["handled"])
        self.assertEqual(r["route"], "conversation")
    def test_no_repeat_welcome(self):
        self.assertEqual(guidance("Press Enter to begin", already_welcomed=True)["route"], "ask")

if __name__ == "__main__":
    unittest.main()
