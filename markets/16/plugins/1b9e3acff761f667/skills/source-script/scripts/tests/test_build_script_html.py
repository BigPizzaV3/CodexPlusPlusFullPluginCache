"""Structural delivery checks; these do not validate medical evidence."""

import copy
from html.parser import HTMLParser
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


BUILDER = Path(__file__).resolve().parents[1] / "build_script_html.py"
SPEC = importlib.util.spec_from_file_location("script_html", BUILDER)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def fixture():
    return {
        "title": "表示検証用台本", "version": "初稿 v1", "date": "2026-10-26",
        "sections": [
            {"id": "digest", "heading": "ダイジェスト", "role": "digest",
             "items": [{"source": "p-one", "quote": "体験から始めます。"}]},
            {"id": "body", "heading": "台本全文", "role": "spoken", "blocks": [
                {"id": "chapter-one", "heading": "最初の章"},
                {"id": "p-one", "text": "今日は私の体験から始めます。確認した資料です。(*1)"},
                {"id": "p-last", "text": "最後まで収録した本文です。"},
            ]},
            {"id": "references", "heading": "文献・出典", "role": "references", "style": "full"},
            {"id": "notes", "heading": "制作メモ", "role": "notes", "blocks": [
                {"id": "note-one", "text": "構造検証用のダミー。医学資料の検証ではありません。"}
            ]},
        ],
        "references": [{"id": 1, "authors": "表示検証用著者", "title": "ダミー資料", "year": "2026",
                        "url": "https://example.org/test?a=1&b=2", "kind": "構造テスト用",
                        "scope": "内容確認には用いない"}],
    }


class Document(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.ids, self.targets, self.tags, self.text, self.roles, self.strong = [], [], [], [], [], []
        self.in_strong = False
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if attrs.get("href", "").startswith("#"):
            self.targets.append(attrs["href"][1:])
        if "data-role" in attrs:
            self.roles.append(attrs["data-role"])
        if tag == "strong":
            self.in_strong = True

    def handle_endtag(self, tag):
        if tag == "strong":
            self.in_strong = False

    def handle_data(self, text):
        self.text.append(text)
        if self.in_strong:
            self.strong.append(text)


class ScriptHtmlTests(unittest.TestCase):
    def test_complete_long_script_is_static_and_copyable(self):
        data = fixture()
        data["sections"][1]["blocks"].insert(2, {"id": "long", "text": "省略しない本文。" * 1600})
        rendered = MODULE.render_script(data)
        doc = Document(rendered)
        self.assertIn("省略しない本文。" * 1600, ''.join(doc.text))
        self.assertIn("最後まで収録した本文です。", ''.join(doc.text))
        self.assertFalse(set(doc.tags) & {"script", "canvas", "img", "link", "iframe"})
        self.assertIn("font-size:19px", rendered)
        self.assertIn("@media print", rendered)
        self.assertIn('name="viewport"', rendered)
        self.assertIn('data-role="notes"', rendered)

    def test_html_escaping_and_anchor_integrity(self):
        data = fixture()
        data["title"] = '<script>alert("x")</script>'
        data["author"] = '<img src=x onerror=alert(1)>'
        data["sections"][1]["blocks"][2]["text"] = "引用符 < > & をそのまま読む。"
        data["references"][0]["title"] = '<b>資料</b>'
        rendered = MODULE.render_script(data)
        doc = Document(rendered)
        self.assertNotIn("script", doc.tags)
        self.assertNotIn("img", doc.tags)
        self.assertNotIn("b", doc.tags)
        self.assertIn("引用符 < > & をそのまま読む。", ''.join(doc.text))
        self.assertEqual(len(doc.ids), len(set(doc.ids)))
        self.assertTrue(set(doc.targets) <= set(doc.ids))
        self.assertEqual(doc.ids.count("ref-1"), 1)

    def test_digest_continuous_quote_highlights_source_and_links(self):
        rendered = MODULE.render_script(fixture())
        doc = Document(rendered)
        self.assertEqual(''.join(doc.strong), "体験から始めます。")
        self.assertIn('href="#p-one"', rendered)
        self.assertIn('.digest-source{color:#b00020;font-weight:800}', rendered)
        self.assertEqual(doc.roles, ["digest", "spoken", "editorial-citation", "references", "notes"])

    def test_current_and_legacy_citations_share_editor_display_and_reference_links(self):
        for marker in ("(*1)", "（引用文献挿入：1）"):
            with self.subTest(marker=marker):
                data = fixture()
                data["sections"][1]["blocks"][1]["text"] = "今日は私の体験から始めます。確認した資料です。" + marker
                data["sections"][1]["blocks"][2]["text"] = "同じ資料を再利用します。" + marker
                original = copy.deepcopy(data)
                rendered = MODULE.render_script(data)
                doc = Document(rendered)
                self.assertEqual(''.join(doc.text).count("（引用文献挿入：1）"), 2)
                self.assertNotIn("(*1)", rendered)
                self.assertEqual(doc.targets.count("ref-1"), 2)
                self.assertEqual(doc.ids.count("ref-1"), 1)
                self.assertEqual(data, original)

    def test_multiple_reference_numbers_keep_their_own_editor_marker(self):
        data = fixture()
        data["references"].append(dict(data["references"][0], id=12, title="別の構造テスト資料"))
        data["sections"][1]["blocks"][1]["text"] += "（引用文献挿入：12）"
        rendered = MODULE.render_script(data)
        doc = Document(rendered)
        self.assertIn("（引用文献挿入：1）（引用文献挿入：12）", ''.join(doc.text))
        self.assertIn("ref-12", doc.ids)
        self.assertIn("ref-12", doc.targets)

    def test_digest_citation_offsets_and_masks_work_for_old_and_new_input(self):
        for marker in ("(*1)", "（引用文献挿入：1）"):
            with self.subTest(marker=marker):
                data = fixture()
                quote = "資料の要点です。" + marker
                data["sections"][1]["blocks"][1]["text"] = "前置き。" + marker + quote + "本文の続き。"
                data["sections"][0]["items"] = [{"source": "p-one", "quote": quote, "masks": [{"start": 0, "end": 2}]}]
                rendered = MODULE.render_script(data)
                self.assertIn("？？の要点です。", rendered)
                self.assertEqual(''.join(Document(rendered).strong), "資料の要点です。（引用文献挿入：1）")
                data["sections"][0]["items"][0]["masks"] = [{"start": len(quote) - len(marker), "end": len(quote) - 1}]
                with self.assertRaisesRegex(ValueError, "cannot mask citation"):
                    MODULE.render_script(data)
                data["sections"][0]["items"][0] = {"source": "p-one", "quote": quote[:-1]}
                with self.assertRaisesRegex(ValueError, "split a citation"):
                    MODULE.render_script(data)

    def test_explicit_mask_preserves_original_source(self):
        data = fixture()
        data["sections"][0]["items"][0]["masks"] = [{"start": 0, "end": 2}]
        rendered = MODULE.render_script(data)
        self.assertIn("？？から始めます。", rendered)
        self.assertIn('<strong class="digest-source">体験から始めます。</strong>', rendered)

    def test_quote_must_be_present_and_occurrence_explicit_if_ambiguous(self):
        for quote in ("体験です。始めます。", "体験…始めます。", "ない文章"):
            with self.subTest(quote=quote):
                data = fixture()
                data["sections"][0]["items"][0]["quote"] = quote
                with self.assertRaisesRegex(ValueError, "absent"):
                    MODULE.render_script(data)
        data = fixture()
        data["sections"][1]["blocks"][1]["text"] += "体験から始めます。"
        with self.assertRaisesRegex(ValueError, "ambiguous"):
            MODULE.render_script(data)
        data["sections"][0]["items"][0]["occurrence"] = 2
        self.assertIn('<strong class="digest-source">体験から始めます。</strong>', MODULE.render_script(data))

    def test_missing_duplicate_unused_reference_and_ids_rejected(self):
        cases = []
        data = fixture(); data["references"] = []; cases.append(data)
        data = fixture(); data["references"].append(copy.deepcopy(data["references"][0])); cases.append(data)
        data = fixture(); data["references"].append(dict(data["references"][0], id=2)); cases.append(data)
        data = fixture(); data["sections"][1]["blocks"][2]["id"] = "p-one"; cases.append(data)
        data = fixture(); data["sections"][1]["id"] = "ref-1"; cases.append(data)
        data = fixture(); data["sections"] = [s for s in data["sections"] if s["role"] != "references"]; cases.append(data)
        for data in cases:
            with self.subTest(data=data), self.assertRaises(ValueError):
                MODULE.render_script(data)

    def test_unsafe_and_malformed_reference_urls_rejected(self):
        for url in ("javascript:alert(1)", "data:text/html,x", "file:///tmp/x", "//example.org",
                    "https://", "https://user:pass@example.org/x", "https://example.org\n/x",
                    "https://example.org:bad/x", "https://example.org\\evil/x"):
            with self.subTest(url=url):
                data = fixture(); data["references"][0]["url"] = url
                with self.assertRaisesRegex(ValueError, "reference URL"):
                    MODULE.render_script(data)

    def test_bad_citations_and_digest_ranges_rejected(self):
        for marker in ("(*2)", "(*x)", "(*01)", "(*1", "（引用文献挿入：2）",
                       "（引用文献挿入：01）", "（引用文献挿入：0）", "（引用文献挿入：x）",
                       "（引用文献挿入：1", "（引用文献挿入：1、2）", "（引用文献挿入:1）"):
            with self.subTest(marker=marker):
                data = fixture(); data["sections"][1]["blocks"][1]["text"] += marker
                with self.assertRaises(ValueError):
                    MODULE.render_script(data)
        for masks in ([{"start": 0, "end": 99}], [{"start": 0, "end": 9}],
                      [{"start": 3, "end": 4}, {"start": 1, "end": 2}]):
            with self.subTest(masks=masks):
                data = fixture(); data["sections"][0]["items"][0]["masks"] = masks
                with self.assertRaises(ValueError):
                    MODULE.render_script(data)

    def test_zeroichi_preserves_ten_headings_roles_and_reference_numbers(self):
        base = fixture()
        data = {key: value for key, value in base.items() if key != "sections"}
        data["layout"] = "zeroichi"
        data["references"][0].update(bibliography="検証用著者. ダミー資料. 2026. 検証用媒体.",
                                      short="検証用著者. 2026.", summary="研究内容を表さない構造テスト用記述。",
                                      supports="このテストでは表示と番号の対応だけを確認する。")
        data["sections"] = []
        for i, (heading, role) in enumerate(zip(MODULE.ZEROICHI_HEADINGS, MODULE.ZEROICHI_ROLES)):
            section = {"id": f"s{i}", "heading": heading, "role": role}
            if role == "references":
                section["style"] = "short" if i == 8 else "full"
            elif role == "digest":
                section["items"] = base["sections"][0]["items"]
            else:
                section["blocks"] = base["sections"][1]["blocks"] if i == 6 else []
            data["sections"].append(section)
        rendered = MODULE.render_script(data)
        positions = [rendered.index(f'<h2>{heading}</h2>') for heading in MODULE.ZEROICHI_HEADINGS]
        self.assertEqual(positions, sorted(positions))
        doc = Document(rendered)
        self.assertEqual(doc.ids.count("ref-1"), 1)
        self.assertTrue(set(doc.targets) <= set(doc.ids))
        data["sections"][0], data["sections"][1] = data["sections"][1], data["sections"][0]
        with self.assertRaisesRegex(ValueError, "10 fixed headings"):
            MODULE.render_script(data)

    def test_cli_writes_real_file_and_invalid_input_does_not_replace_it(self):
        with tempfile.TemporaryDirectory() as directory:
            source, output = Path(directory) / "input.json", Path(directory) / "script.html"
            source.write_text(json.dumps(fixture(), ensure_ascii=False), encoding="utf-8")
            result = subprocess.run([sys.executable, str(BUILDER), str(source), str(output)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            content = output.read_text(encoding="utf-8")
            self.assertEqual(Path(json.loads(result.stdout)["output"]), output.resolve())
            data = fixture(); data["sections"][0]["items"][0]["quote"] = "不一致"
            source.write_text(json.dumps(data), encoding="utf-8")
            result = subprocess.run([sys.executable, str(BUILDER), str(source), str(output)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(output.read_text(encoding="utf-8"), content)


if __name__ == "__main__":
    unittest.main()
