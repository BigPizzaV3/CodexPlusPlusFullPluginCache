"""Citation display regressions; fixtures are not medical evidence."""
from __future__ import annotations

import argparse
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_handoff as handoff


def fixture(root):
    source = ("# 構造確認用原稿\n\n"
              "## 本文\n\n"
              "最初の資料です。(*1)続けて説明します。\n\n"
              "別の資料です。（引用文献挿入：2）最後の説明です。\n\n"
              "## 引用論文\n\n"
              "(*1) 表示テスト資料 A。https://example.org/one\n\n"
              "(*2) 表示テスト資料 B。https://example.org/two\n")
    (root / "source.md").write_text(source, encoding="utf-8")
    quote = "最初の資料です。(*1)"
    case = {"case_id": "citation-regression", "title": "引用表示の確認", "doctor_id": "test-doctor",
            "source": {"path": "source.md", "version": "1", "sha256": handoff.sha256(root / "source.md")},
            "profile": {"id": "test-doctor", "version": "1", "design_version": "1"},
            "design": {"background": "#ffffff", "ink": "#111111", "accent": "#117777"},
            "scenes": [{"id": "scene-1", "quote": quote, "end_cue": "説明の終わり", "duration": 5,
                        "placement": "本文の横", "selected": None, "omit": True, "options": []}],
            "digest": [{"quote": quote, "display": "？？の資料です。(*1)", "status": "approved"}]}
    path = root / "case.json"
    path.write_text(json.dumps(case, ensure_ascii=False), encoding="utf-8")
    return path, case, source


class CitationMarkerTests(unittest.TestCase):
    def test_rendering_keeps_source_offsets_digest_and_bibliography_numbers(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            path, original_case, original_source = fixture(root)
            case, source, _, _, _, _ = handoff.validate(path)
            rendered = handoff.manuscript(case, source)
            self.assertIn('<strong class="digest-highlight" id="digest-source-1">最初の資料です。（引用文献挿入：1）</strong>', rendered)
            self.assertIn("続けて説明します。", rendered)
            self.assertIn("別の資料です。（引用文献挿入：2）最後の説明です。", rendered)
            self.assertIn("(*1) 表示テスト資料 A。", rendered)
            self.assertIn("(*2) 表示テスト資料 B。", rendered)
            self.assertLess(rendered.index("最初の資料です。"), rendered.index('data-scene="scene-1"'))
            self.assertLess(rendered.index('data-scene="scene-1"'), rendered.index("別の資料です。"))
            self.assertIn("？？の資料です。（引用文献挿入：1）", handoff.digest_html(case))
            markdown = handoff.editor_markdown(case, source)
            self.assertIn("最初の資料です。（引用文献挿入：1）続けて説明します。", markdown)
            self.assertIn("(*1) 表示テスト資料 A。", markdown)
            self.assertEqual(source, original_source)
            self.assertEqual(case["digest"][0]["quote"], original_case["digest"][0]["quote"])
            self.assertEqual((root / "source.md").read_text(), original_source)

    def test_packaged_prompter_omits_markers_and_original_sources_are_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            path, case, source = fixture(root)
            prompter = "最初の資料です。(*1)続けて説明します。\n\n別の資料です。（引用文献挿入：2）最後の説明です。\n"
            (root / "prompter.md").write_text(prompter, encoding="utf-8")
            case["prompter_path"] = "prompter.md"
            path.write_text(json.dumps(case, ensure_ascii=False), encoding="utf-8")
            output, archive = root / "delivery", root / "delivery.zip"
            with contextlib.redirect_stdout(io.StringIO()):
                handoff.run(argparse.Namespace(case=str(path), output=str(output), zip=str(archive), replace=False, require_complete=False))
            expected = "最初の資料です。続けて説明します。\n\n別の資料です。最後の説明です。\n"
            self.assertEqual((output / "台本_プロンプター用.md").read_text(), expected)
            self.assertEqual((root / "prompter.md").read_text(), prompter)
            self.assertEqual((output / "source-script.md").read_text(), source)
            self.assertIn("（引用文献挿入：1）", (output / "台本_編集用.md").read_text())
            self.assertIn("（引用文献挿入：1）", (output / "配置CSV.csv").read_text())
            report = json.loads((output / "manifest.json").read_text())
            self.assertEqual(report["preview"]["source_coverage"], "complete")
            self.assertEqual(report["source"]["sha256"], handoff.sha256(root / "source.md"))
            with zipfile.ZipFile(archive) as zipped:
                self.assertEqual(zipped.read("台本_プロンプター用.md").decode(), expected)
                self.assertEqual(zipped.read("source-script.md").decode(), source)
                self.assertIsNone(zipped.testzip())

    def test_digest_cannot_split_citation_with_legacy_or_current_input(self):
        for quote in ("最初の資料です。(*1", "*1)続けて", "別の資料です。（引用文献挿入：2", "引用文献挿入：2）"):
            with self.subTest(quote=quote), tempfile.TemporaryDirectory() as directory:
                root = Path(directory).resolve()
                path, case, _ = fixture(root)
                case["digest"][0]["quote"] = quote
                path.write_text(json.dumps(case, ensure_ascii=False), encoding="utf-8")
                with self.assertRaisesRegex(handoff.ValidationError, "マーカーの途中"):
                    handoff.validate(path)

    def test_malformed_body_markers_fail_instead_of_becoming_readable_text(self):
        for marker in ("(*x)", "(*01)", "（引用文献挿入：0）", "（引用文献挿入：2", "（引用文献挿入：1、2）"):
            with self.subTest(marker=marker), tempfile.TemporaryDirectory() as directory:
                root = Path(directory).resolve()
                path, case, source = fixture(root)
                source = source.replace("別の資料です。（引用文献挿入：2）", "別の資料です。" + marker)
                (root / "source.md").write_text(source, encoding="utf-8")
                case["source"]["sha256"] = handoff.sha256(root / "source.md")
                path.write_text(json.dumps(case, ensure_ascii=False), encoding="utf-8")
                with self.assertRaisesRegex(handoff.ValidationError, "引用文献マーカー"):
                    handoff.validate(path)

    def test_ordinary_numbering_is_not_assumed_to_be_citation(self):
        raw = "候補(1)と[2]を比較します。文献です。(*12)"
        self.assertEqual(handoff.citation_text(raw), "候補(1)と[2]を比較します。文献です。（引用文献挿入：12）")
        self.assertEqual(handoff.prompter_text(raw), "候補(1)と[2]を比較します。文献です。")

    def test_bibliography_boundary_does_not_change_the_following_script(self):
        for heading in ("【引用論文】", "引用論文（簡易リスト）", "引用論文まとめ（詳細解説）", "参考文献 (確認した資料)"):
            with self.subTest(heading=heading):
                source = "## " + heading + "\n\n(*1) 資料名\n\n### 補足\n\n(*1) 文献の説明\n\n## まとめ\n\n本文です。(*1)\n"
                case = {"title": "構造確認用", "scenes": [], "digest": []}
                rendered = handoff.manuscript(case, source)
                markdown = handoff.editor_markdown(case, source)
                for output in (rendered, markdown):
                    self.assertIn("(*1) 資料名", output)
                    self.assertIn("(*1) 文献の説明", output)
                    self.assertIn("本文です。（引用文献挿入：1）", output)
                    self.assertNotIn("（引用文献挿入：1） 資料名", output)

    def test_html_link_and_escaping_survive_marker_normalization(self):
        raw = "<説明> & [資料です。(*1)](https://example.org/?a=1&b=2)"
        rendered = handoff.inline(raw)
        self.assertIn("&lt;説明&gt; &amp;", rendered)
        self.assertIn('href="https://example.org/?a=1&amp;b=2"', rendered)
        self.assertIn(">資料です。（引用文献挿入：1）</a>", rendered)

    def test_link_destinations_are_preserved_in_html_markdown_and_prompter(self):
        url = "https://example.org/(*1)?a=1&b=2"
        raw = "資料です。(*1) [参照資料(*1)](" + url + ") 補足 " + url
        normalized = handoff.citation_text(raw)
        self.assertEqual(normalized, "資料です。（引用文献挿入：1） [参照資料（引用文献挿入：1）](" + url + ") 補足 " + url)
        self.assertEqual(handoff.prompter_text(raw), "資料です。 [参照資料](" + url + ") 補足 " + url)
        rendered = handoff.inline(raw)
        self.assertIn('href="https://example.org/(*1)?a=1&amp;b=2"', rendered)
        self.assertIn(">参照資料（引用文献挿入：1）</a>", rendered)
        self.assertIn("補足 https://example.org/(*1)?a=1&amp;b=2", rendered)


if __name__ == "__main__":
    unittest.main()
