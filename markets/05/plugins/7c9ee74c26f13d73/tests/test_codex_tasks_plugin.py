from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE_ROOT = PLUGIN_ROOT.parents[1]
CODEX_TASKS_APP_ID = "connector_openai_codex_tasks"


class CodexTasksPluginTests(unittest.TestCase):
    def test_plugin_binds_the_required_codex_tasks_connector(self) -> None:
        manifest = json.loads(
            (PLUGIN_ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8")
        )
        app_manifest = json.loads((PLUGIN_ROOT / ".app.json").read_text(encoding="utf-8"))

        self.assertEqual(manifest["name"], "codex-tasks")
        self.assertEqual(manifest["skills"], "./skills/")
        self.assertEqual(manifest["apps"], "./.app.json")
        self.assertNotIn("mcpServers", manifest)
        self.assertEqual(manifest["interface"]["displayName"], "Codex Tasks (Internal/CCA)")
        self.assertIn("CCA remote-task adapter", manifest["interface"]["longDescription"])
        self.assertEqual(
            app_manifest,
            {"apps": {"codex_tasks": {"id": CODEX_TASKS_APP_ID, "required": True}}},
        )

    def test_catalog_is_manually_available_with_connector_managed_access(self) -> None:
        marketplace = json.loads((MARKETPLACE_ROOT / "marketplace.json").read_text("utf-8"))

        self.assertEqual(
            [entry for entry in marketplace["plugins"] if entry["name"] == "codex-tasks"],
            [
                {
                    "name": "codex-tasks",
                    "source": {
                        "source": "local",
                        "path": "./plugins/codex-tasks",
                    },
                    "policy": {
                        "installation": "AVAILABLE",
                        "authentication": "ON_USE",
                    },
                    "category": "Productivity",
                }
            ],
        )

    def test_creation_skill_example_is_a_valid_minimal_request(self) -> None:
        skill = (PLUGIN_ROOT / "skills/create-codex-task/SKILL.md").read_text(encoding="utf-8")

        example = re.search(r"```json\s*(.*?)\s*```", skill, re.DOTALL)
        self.assertIsNotNone(example)
        assert example is not None
        request = json.loads(example.group(1))

        self.assertEqual(
            set(request),
            {"thread_start_params", "turn_start_params"},
        )
        self.assertEqual(
            set(request["thread_start_params"]),
            {"approvalPolicy", "approvalsReviewer", "sandbox", "environments"},
        )
        self.assertEqual(request["thread_start_params"]["approvalPolicy"], "on-request")
        self.assertEqual(request["thread_start_params"]["approvalsReviewer"], "auto_review")
        self.assertEqual(request["thread_start_params"]["sandbox"], "workspace-write")
        self.assertEqual(
            set(request["thread_start_params"]["environments"][0]),
            {"environmentId", "cwd"},
        )
        self.assertEqual(set(request["turn_start_params"]), {"input"})

    def test_plugin_contains_only_the_creation_skill(self) -> None:
        self.assertEqual(
            [path.name for path in (PLUGIN_ROOT / "skills").iterdir() if path.is_dir()],
            ["create-codex-task"],
        )


if __name__ == "__main__":
    unittest.main()
