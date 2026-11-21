"""Completion checks for actual, independently reviewed medical image choices.

Fixtures are tiny synthetic PNGs, never claimed to be medical illustrations.
The tests establish metadata/file validation only, not medical correctness.
"""
from __future__ import annotations

import copy
from pathlib import Path
import struct
import sys
import tempfile
import unittest
import zlib

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from quality_gate import assess_quality, file_hash


def png(value):
    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xffffffff)
    header = struct.pack(">IIBBBBB", 8, 8, 8, 2, 0, 0, 0)
    pixels = (b"\0" + bytes((value, 90, 170)) * 8) * 8
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header) + chunk(b"IDAT", zlib.compress(pixels)) + chunk(b"IEND", b"")


class MedicalVariantTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / "assets").mkdir()
        self.case = self.fixture()

    def fixture(self, count=3):
        styles = ["anatomical", "cute", "schematic", "context", "metaphor", "schematic"]
        options = []
        for index in range(count):
            rel = f"assets/variant-{index}.png"
            path = self.root / rel
            path.write_bytes(png(index * 30))
            options.append({"id": f"variant-{index}", "kind": "illustration", "title": f"案{index}",
                            "reason": "構図の異なる比較用画像", "mode": "square", "status": "ready", "files": [rel],
                            "production": {"method": "image_generation", "tool": "test-fixture", "evidence": "合成PNGの試験データ", "review": {
                                "status": "passed", "evidence": "試験用の確認記録", "files_sha256": {rel: file_hash(path)}}},
                            "medical_visual": {"style": styles[index], "explanation": "試験用PNGで表示と記録だけを検証", "review": {
                                "status": "passed", "evidence": "試験用の申告で医学的妥当性を保証しない", "references": ["試験資料の記述・位置"] if index == 0 else []}}})
        capabilities = {name: {"status": "verified", "tool": "test-fixture", "evidence": "試験用の機能確認記録"} for name in ("image_generation", "file_output")}
        capabilities["video_generation"] = {"status": "not_needed", "evidence": "静止画だけの試験"}
        return {"source": {"sha256": "source-hash"}, "quality": {"version": 1, "source_sha256": "source-hash",
                "capabilities": capabilities,
                "profile_assets": [{"role": role, "status": "not_applicable", "evidence": "試験で本人素材不要"} for role in ("intro", "ending", "gift")],
                "reviews": {name: {"status": "passed", "evidence": "試験用申告"} for name in ("material_mix", "visual", "editor_ready")}},
                "scenes": [{"id": "medical-scene", "purpose": "医学説明用素材の比較", "selected": "variant-0", "options": options,
                            "medical_variants": {"target_count": count, "option_ids": [o["id"] for o in options], "reason": "比較して選ぶため"}}]}

    @property
    def scene(self):
        return self.case["scenes"][0]

    def report(self):
        return assess_quality(self.case, self.root)

    def codes(self):
        return {item["code"] for item in self.report()["blockers"]}

    def assertBlocked(self, code):
        self.assertIn("medical_variants." + code, self.codes())
        self.assertEqual(self.report()["status"], "needs_review")

    def test_three_four_and_five_actual_independent_choices_pass(self):
        for count in (3, 4, 5):
            with self.subTest(count=count):
                self.case = self.fixture(count)
                report = self.report()
                self.assertEqual(report["blockers"], [])
                self.assertEqual(report["status"], "passed")
                self.assertIn("自動判定ではありません", report["medical_variant_review"])

    def test_two_six_and_noninteger_target_counts_block(self):
        for count in (2, 6):
            with self.subTest(count=count):
                self.case = self.fixture(count)
                self.assertBlocked("count")
        for count in (True, "3", 3.0, None, {}):
            with self.subTest(count=count):
                self.case = self.fixture()
                self.scene["medical_variants"]["target_count"] = count
                self.assertBlocked("count")

    def test_anatomical_and_cute_are_both_required(self):
        for index in (0, 1):
            with self.subTest(removed_style=index):
                self.case = self.fixture()
                self.scene["options"][index]["medical_visual"]["style"] = "schematic"
                self.assertBlocked("required_styles")

    def test_missing_duplicate_unknown_and_wrong_number_ids_block(self):
        for ids, code in (([], "ids"), (["variant-0", "variant-1"], "ids"),
                          (["variant-0", "variant-1", "variant-1"], "ids"),
                          (["variant-0", "variant-1", "missing"], "unknown_option"),
                          (["variant-0", "variant-1", {}], "ids")):
            with self.subTest(ids=ids):
                self.case = self.fixture()
                self.scene["medical_variants"]["option_ids"] = ids
                self.assertBlocked(code)
        self.case = self.fixture()
        self.scene["options"].append(copy.deepcopy(self.scene["options"][1]))
        self.assertBlocked("unknown_option")

    def test_ready_extra_option_can_be_selected_but_pending_extra_cannot(self):
        self.case = self.fixture(4)
        self.scene["medical_variants"].update(target_count=3, option_ids=["variant-0", "variant-1", "variant-2"])
        self.scene["selected"] = "variant-3"
        self.assertEqual(self.report()["status"], "passed")
        self.scene["options"][3]["status"] = "pending"
        self.assertIn("scene.pending", self.codes())
        self.assertEqual(self.report()["status"], "needs_review")

    def test_extra_selection_does_not_waive_unfinished_comparison_group(self):
        self.case = self.fixture(4)
        self.scene["medical_variants"].update(target_count=3, option_ids=["variant-0", "variant-1", "variant-2"])
        self.scene["selected"] = "variant-3"
        self.scene["options"][1]["status"] = "pending"
        self.assertBlocked("pending")

    def test_nonselected_proposal_or_pending_cannot_complete(self):
        for status in ("proposal", "pending"):
            with self.subTest(status=status):
                self.case = self.fixture()
                self.scene["options"][1]["status"] = status
                self.assertBlocked("pending")

    def test_nonselected_missing_production_tool_evidence_or_method_blocks(self):
        for field in ("method", "tool", "evidence"):
            with self.subTest(field=field):
                self.case = self.fixture()
                del self.scene["options"][1]["production"][field]
                self.assertBlocked("production")
        self.case = self.fixture()
        self.case["quality"]["capabilities"]["image_generation"]["status"] = "not_tested"
        self.assertBlocked("tool_unverified")

    def test_nonselected_unreviewed_or_stale_visual_output_blocks(self):
        for state in ("failed", "pending", None):
            with self.subTest(state=state):
                self.case = self.fixture()
                self.scene["options"][1]["production"]["review"]["status"] = state
                self.assertBlocked("visual_review")
        self.case = self.fixture()
        rel = self.scene["options"][1]["files"][0]
        (self.root / rel).write_bytes(png(250))
        self.assertBlocked("review_stale")

    def test_medical_review_and_anatomical_reference_are_required(self):
        for index in (0, 1, 2):
            with self.subTest(index=index):
                self.case = self.fixture()
                self.scene["options"][index]["medical_visual"]["review"]["status"] = "pending"
                self.assertBlocked("medical_review")
        self.case = self.fixture()
        self.scene["options"][0]["medical_visual"]["review"]["references"] = []
        self.assertBlocked("references")
        self.case = self.fixture()
        self.scene["options"][1]["medical_visual"]["review"]["references"] = [""]
        self.assertBlocked("references")

    def test_same_path_or_renamed_identical_bytes_are_not_alternatives(self):
        first, second = self.scene["options"][:2]
        second["files"] = first["files"][:]
        second["production"]["review"]["files_sha256"] = first["production"]["review"]["files_sha256"].copy()
        self.assertBlocked("duplicate_image")
        self.case = self.fixture()
        first, second = self.scene["options"][:2]
        target = self.root / second["files"][0]
        target.write_bytes((self.root / first["files"][0]).read_bytes())
        second["production"]["review"]["files_sha256"][second["files"][0]] = file_hash(target)
        self.assertBlocked("duplicate_image")

    def test_missing_nonimage_empty_or_malformed_files_do_not_count(self):
        for files, code in (([], "files"), ({}, "files"), ([None], "files"), (["missing.png"], "missing_file"),
                            (["assets/not-an-image.txt"], "image_required"), (["assets/fake.png"], "image_format")):
            with self.subTest(files=files):
                self.case = self.fixture()
                self.scene["options"][1]["files"] = files
                for name in ("not-an-image.txt", "fake.png"):
                    (self.root / "assets" / name).write_text("not an image", encoding="utf-8")
                self.assertBlocked(code)

    def test_cute_or_anatomical_cannot_be_relabelled_layout(self):
        for index in (0, 1):
            with self.subTest(index=index):
                self.case = self.fixture()
                self.scene["options"][index]["production"]["method"] = "layout"
                self.assertBlocked("illustration_required")

    def test_nonselected_invalid_kind_or_video_production_is_not_an_image_choice(self):
        for field, value, code in (("kind", "video", "image_required"), ("kind", "unknown", "image_required"),
                                   ("mode", "motion", "image_required")):
            with self.subTest(field=field, value=value):
                self.case = self.fixture()
                self.scene["options"][2][field] = value
                self.assertBlocked(code)
        self.case = self.fixture()
        self.scene["options"][2]["production"]["method"] = "video_generation"
        self.assertBlocked("production")

    def test_blank_explanation_review_evidence_or_group_reason_blocks(self):
        self.scene["medical_variants"]["reason"] = " "
        self.assertBlocked("reason")
        self.case = self.fixture()
        self.scene["options"][1]["medical_visual"]["explanation"] = " "
        self.assertBlocked("explanation")
        self.case = self.fixture()
        self.scene["options"][1]["medical_visual"]["review"]["evidence"] = " "
        self.assertBlocked("medical_review")

    def test_schematic_svg_can_be_a_real_distinct_choice(self):
        option = self.scene["options"][2]
        rel = "assets/schematic.svg"
        path = self.root / rel
        path.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="8" height="8"><circle cx="4" cy="4" r="3"/></svg>', encoding="utf-8")
        option.update(kind="diagram", files=[rel])
        option["production"].update(method="layout")
        option["production"]["review"]["files_sha256"] = {rel: file_hash(path)}
        self.assertEqual(self.report()["status"], "passed")

    def test_valid_explicit_omit_skips_production_not_schema(self):
        legacy = copy.deepcopy(self.scene)
        legacy.pop("medical_variants")
        legacy["id"] = "legacy-adopted"
        self.case["scenes"].append(legacy)
        self.scene.update(omit=True, selected=None, omission_basis="user", omission_reason="本人がこの場面を省略")
        for option in self.scene["options"]:
            option.update(status="proposal", files=[])
            option.pop("production")
            option.pop("medical_visual")
        self.assertEqual(self.report()["status"], "passed")
        self.scene["medical_variants"]["target_count"] = 6
        self.assertBlocked("count")

    def test_unexplained_omission_does_not_hide_unfinished_choices(self):
        self.scene.update(omit=True, selected=None)
        self.scene["options"][1]["status"] = "pending"
        self.assertBlocked("pending")
        self.assertIn("scene.omission", self.codes())

    def test_legacy_cases_without_group_keep_existing_behavior(self):
        self.scene.pop("medical_variants")
        self.scene["options"][1].update(status="proposal", files=[])
        self.scene["options"][1].pop("production")
        self.assertEqual(self.report()["status"], "passed")
        self.assertNotIn("medical_variant_review", self.report())

    def test_malformed_new_metadata_returns_blockers_without_crashing(self):
        for group in (None, [], "yes", True, {}):
            with self.subTest(group=group):
                self.case = self.fixture()
                self.scene["medical_variants"] = group
                self.assertEqual(self.report()["status"], "needs_review")
        for field, value in (("medical_visual", []), ("medical_visual", None), ("medical_visual", {"style": []}),
                             ("medical_visual", {"style": "cute", "review": []}), ("production", [])):
            with self.subTest(field=field, value=value):
                self.case = self.fixture()
                self.scene["options"][1][field] = value
                self.assertEqual(self.report()["status"], "needs_review")


if __name__ == "__main__":
    unittest.main()
