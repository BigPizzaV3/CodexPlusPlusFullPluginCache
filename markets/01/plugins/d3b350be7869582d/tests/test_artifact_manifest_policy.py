from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_artifacts_module():
    path = ROOT / "shared" / "artifacts.py"
    spec = importlib.util.spec_from_file_location("ib_artifacts", path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ArtifactManifestPolicyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.artifacts = load_artifacts_module()

    def test_write_manifest_accepts_workbook_primary_and_support_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            out = Path(tmpdir)
            workbook = out / "model.xlsx"
            workbook.write_bytes(b"placeholder")
            manifest = self.artifacts.write_artifact_manifest(
                out,
                "unit-test-skill",
                "workbook",
                workbook,
                support_artifacts=[
                    self.artifacts.artifact_item(
                        out / "support" / "raw.csv",
                        "support_artifact",
                        "csv",
                        "Raw support data.",
                        False,
                        True,
                        "CSV is support data.",
                    )
                ],
            )
            self.assertEqual(manifest["primary_human_deliverable"], str(workbook))
            self.assertFalse(manifest["support_artifacts_user_visible_default"])
            self.assertTrue((out / "manifest.json").exists())

    def test_write_manifest_preserves_optional_routing_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            out = Path(tmpdir)
            report = out / "deal_committee.html"
            report.write_text("<html></html>", encoding="utf-8")
            routing = self.artifacts.routing_context(
                "deal_committee",
                "memo-builder",
                ["model-audit-tieout", "ib-deck-qc"],
                "high",
                ["cim_teardown_to_memo_builder", "pitch_deck_builder_to_ib_deck_qc"],
                "Broad committee prompt routed to memo-builder for synthesis with model audit and deck QC gates.",
            )
            manifest = self.artifacts.write_artifact_manifest(
                out,
                "memo-builder",
                "html_report",
                report,
                routing=routing,
            )
            self.assertEqual(manifest["transaction_workflow"], "deal_committee")
            self.assertEqual(manifest["lead_skill"], "memo-builder")
            self.assertIn("ib-deck-qc", manifest["supporting_skills"])
            self.assertEqual(manifest["routing_confidence"], "high")
            self.assertIn("pitch_deck_builder_to_ib_deck_qc", manifest["handoff_contracts_used"])
            self.assertIn("committee prompt", manifest["routing_reason"])

    def test_support_formats_cannot_be_primary_by_default(self) -> None:
        base = {
            "manifest_version": "1.0",
            "skill": "bad-skill",
            "artifact_mode": "html_report",
            "output_dir": "/tmp/out",
            "first_read": {
                "path": "/tmp/out/raw.json",
                "role": "primary human deliverable",
                "why": "bad",
            },
            "human_deliverables": [],
            "companion_deliverables": [],
            "support_artifacts": [],
            "agent_artifacts": [],
            "support_artifacts_user_visible_default": False,
            "blocked_or_partial_status": {"status": "complete", "reason": "", "missing_inputs": []},
            "final_response_guidance": {
                "lead_with": "primary_human_deliverable",
                "mention_support_artifacts": "only_briefly_unless_requested",
            },
            "discipline_note": "Use the human deliverable as the main output; support artifacts are for audit/import/debug only.",
        }
        for bad_path in ["/tmp/out/raw.json", "/tmp/out/raw.csv", "/tmp/out/report.md"]:
            with self.subTest(path=bad_path):
                manifest = dict(base, primary_human_deliverable=bad_path)
                with self.assertRaises(ValueError):
                    self.artifacts.validate_artifact_manifest(manifest)

    def test_workbook_helper_enforces_first_visible_sheet(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            workbook = Path(tmpdir) / "book.xlsx"
            self.artifacts.write_cover_first_workbook(
                workbook,
                [["Cover"], ["First read", "Open this first"]],
                {"Data": [["Metric", "Value"], ["Revenue", 10]]},
            )
            self.assertEqual(self.artifacts.assert_first_visible_sheet(workbook), "Cover")


if __name__ == "__main__":
    unittest.main()
