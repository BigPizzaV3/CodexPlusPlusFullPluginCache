"""Renderer regressions using colored fixture PNGs, not medical illustrations."""
from __future__ import annotations

import argparse
import base64
import contextlib
from html.parser import HTMLParser
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_handoff as handoff
from test_multi_image import png


class Markup(HTMLParser):
    def __init__(self, document):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.json_text = ""
        self.in_data = False
        self.feed(document)
        self.close()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if tag == "script" and attrs.get("id") == "handoff-data":
            self.in_data = True

    def handle_endtag(self, tag):
        if tag == "script":
            self.in_data = False

    def handle_data(self, data):
        if self.in_data:
            self.json_text += data


def fixture(root, count=3):
    (root / "input").mkdir()
    source = root / "source.md"
    source.write_text("# 表示確認専用\n\n候補を選ぶ表示を確認します。\n", encoding="utf-8")
    styles = list(handoff.MEDICAL_STYLES)[:count]
    options = []
    for index, style in enumerate(styles):
        path = "input/variant-" + str(index) + ".png"
        (root / path).write_bytes(png((20 + index * 35, 100, 170)))
        options.append({"id": "option-" + str(index), "title": "検査用色面 " + str(index), "type": "検査用", "reason": "比較表示の確認", "description": "医療画像ではないテスト用色面", "mode": "square", "status": "ready", "files": [path], "medical_visual": {"style": style, "explanation": "表示範囲の検査用テキスト", "review": {"status": "passed", "evidence": "テスト用データ。医学的な確認の記録ではない", "references": ["表示テストのfixture"]}}})
    case = {"case_id": "variant-render-test", "title": "候補表示のテスト", "doctor_id": "fixture-doctor", "source": {"path": "source.md", "version": "1", "sha256": handoff.sha256(source)}, "profile": {"id": "fixture-doctor", "version": "1", "design_version": "1"}, "design": {"background": "#ffffff", "ink": "#111111", "accent": "#117777"}, "scenes": [{"id": "scene-1", "quote": "候補を選ぶ表示を確認します。", "end_cue": "発話の終わり", "duration": 5, "placement": "本文の指定位置", "selected": "option-0", "options": options, "medical_variants": {"target_count": count, "option_ids": [x["id"] for x in options], "reason": "表現方法を比較するテスト"}}]}
    path = root / "case.json"
    path.write_text(json.dumps(case, ensure_ascii=False), encoding="utf-8")
    return path, case


class VariantDisplayTests(unittest.TestCase):
    def test_three_to_five_options_open_with_all_previews_and_zip_originals(self):
        for count in (3, 4, 5):
            with self.subTest(count=count), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary).resolve()
                path, original = fixture(root, count)
                output, archive = root / "delivery", root / "delivery.zip"
                with contextlib.redirect_stdout(io.StringIO()):
                    handoff.run(argparse.Namespace(case=str(path), output=str(output), zip=str(archive), replace=False, require_complete=False))
                expected_ids = [x["id"] for x in original["scenes"][0]["options"]]
                for name in ("script.html", "index.html", "preview.html"):
                    document = (output / name).read_text(encoding="utf-8")
                    markup = Markup(document)
                    panels = [a for tag, a in markup.tags if a.get("class") == "option-panel"]
                    self.assertEqual([a["data-option-id"] for a in panels], expected_ids)
                    choices = [a for tag, a in markup.tags if tag == "details" and "medical-choices" in a.get("class", "")]
                    self.assertEqual(len(choices), 1)
                    self.assertIn("open", choices[0])
                    self.assertIn(f"比較用素材：実ファイルあり {count} / {count}案", document)
                    self.assertIn("解剖関係を重視", document)
                    self.assertIn("かわいい概念表現", document)
                    self.assertIn("伝える内容・表現の範囲", document)
                    self.assertNotIn("医学的正確さ保証", document)
                    images = [a for tag, a in markup.tags if tag == "img"]
                    self.assertEqual(len(images), count + 1)  # selected + every alternative
                    for index in range(count):
                        image = next(a for a in images if a.get("alt") == "検査用色面 " + str(index))
                        if name == "preview.html":
                            self.assertEqual(base64.b64decode(image["src"].split(",", 1)[1]), (root / f"input/variant-{index}.png").read_bytes())
                        else:
                            self.assertEqual(image["src"], f"assets/variant-{index}.png")
                    data = json.loads(markup.json_text)
                    self.assertEqual(data["scenes"][0]["selected"], "option-0")
                    self.assertEqual([x["id"] for x in data["scenes"][0]["options"]], expected_ids)
                    self.assertIn("別案の選択だけでは、この素材は差し替わりません", document)
                manifest = json.loads((output / "manifest.json").read_text())
                self.assertEqual(manifest["counts"]["selected_ready_still_files"], 1)
                self.assertEqual(manifest["counts"]["alternative_ready_still_files"], count - 1)
                self.assertEqual(manifest["scenes"][0]["medical_variants"], original["scenes"][0]["medical_variants"])
                self.assertEqual((output / "source-script.md").read_bytes(), (root / "source.md").read_bytes())
                with zipfile.ZipFile(archive) as packed:
                    for index in range(count):
                        self.assertEqual(packed.read(f"assets/variant-{index}.png"), (root / f"input/variant-{index}.png").read_bytes())

    def test_pending_option_does_not_inflate_ready_count_or_alternative_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            path, case = fixture(root)
            option = case["scenes"][0]["options"][2]
            option.update(status="pending", files=[])
            path.write_text(json.dumps(case), encoding="utf-8")
            case = handoff.validate(path)[0]
            self.assertIn("実ファイルあり 2 / 3案", handoff.card(case["scenes"][0]))
            self.assertEqual(handoff.counts(case)["alternative_ready_still_files"], 1)
            self.assertEqual(handoff.package_status(case), "partial")

    def test_metadata_is_escaped_and_not_an_accuracy_badge(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            path, case = fixture(root)
            attack = '<script>alert("x")</script><img src=x onerror=alert(1)>'
            scene = case["scenes"][0]
            scene["medical_variants"]["reason"] = attack
            visual = scene["options"][0]["medical_visual"]
            visual["explanation"] = attack
            visual["review"].update(evidence=attack, references=[attack])
            path.write_text(json.dumps(case), encoding="utf-8")
            validated = handoff.validate(path)[0]
            document = handoff.card(validated["scenes"][0])
            self.assertNotIn(attack, document)
            self.assertIn("&lt;script&gt;", document)
            self.assertEqual(sum(tag == "script" for tag, _ in Markup(document).tags), 0)
            self.assertNotIn("医学的正確さ保証", document)

    def test_legacy_options_remain_collapsed_and_ready_file_reuse_is_deduplicated(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            path, case = fixture(root)
            scene = case["scenes"][0]
            del scene["medical_variants"]
            for option in scene["options"]:
                del option["medical_visual"]
            scene["options"][1]["files"] = scene["options"][0]["files"][:]
            scene["options"][2]["poster"] = scene["options"][2]["files"][0]
            path.write_text(json.dumps(case), encoding="utf-8")
            case = handoff.validate(path)[0]
            document = handoff.card(case["scenes"][0])
            choices = [a for tag, a in Markup(document).tags if tag == "details"]
            self.assertEqual(choices, [{"class": "choices"}])
            self.assertNotIn("medical-options-grid", document)
            self.assertEqual(handoff.counts(case)["alternative_ready_still_files"], 0)

    def test_variant_group_rejects_invalid_ids_or_target(self):
        for values in ({"target_count": 2}, {"target_count": True}, {"option_ids": ["option-0", "option-0", "option-2"]}, {"option_ids": ["option-0", "option-1", "missing"]}):
            with self.subTest(values=values), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary).resolve()
                path, case = fixture(root)
                case["scenes"][0]["medical_variants"].update(values)
                path.write_text(json.dumps(case), encoding="utf-8")
                with self.assertRaises(handoff.ValidationError):
                    handoff.validate(path)

    @unittest.skipUnless(shutil.which("node"), "Node is needed to exercise the existing browser export code")
    def test_browser_export_keeps_original_selection_and_new_choice_id(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            path, _ = fixture(root)
            case, _, _, source_hash, _, _ = handoff.validate(path)
            data = handoff.client_data(case, source_hash, "partial")
            script = r'''
const fs = require('fs'), vm = require('vm');
const input = JSON.parse(fs.readFileSync(0, 'utf8'));
const nodes = new Map();
const make = () => ({textContent:'',value:'',dataset:{},classList:{toggle(){}},handlers:{},addEventListener(k,v){this.handlers[k]=v},appendChild(){},remove(){},click(){},setSelectionRange(){}});
function node(id){if(!nodes.has(id)) nodes.set(id,make());return nodes.get(id)}
node('handoff-data').textContent=JSON.stringify(input.data);
const radios = [...input.data.scenes[0].options.map(o=>o.id),'__none__','__unselected__'].map(value=>Object.assign(make(),{value,checked:false}));
const card = Object.assign(make(),{dataset:{scene:'scene-1'},querySelector:s=>node(s),querySelectorAll:s=>s==='input[type=radio]'?radios:[]});
let blob;
const document={body:{dataset:{},appendChild(){}},getElementById:node,querySelector:node,querySelectorAll:s=>s==='[data-scene]'?[card]:[],createElement:make};
const context={document,localStorage:{getItem(){return null},setItem(){}},URL:{createObjectURL(b){blob=b;return 'blob:test'},revokeObjectURL(){}},Blob,Date,Map,JSON,Boolean,window:{confirm(){return false}},setTimeout(){}};
vm.runInNewContext(input.script,context);
radios[1].checked=true;radios[1].handlers.change();
node('export-json').handlers.click();
blob.text().then(text=>process.stdout.write(text));
'''
            result = subprocess.run([shutil.which("node"), "-e", script], input=json.dumps({"data": data, "script": (handoff.ASSET_ROOT / "app.js").read_text()}), text=True, capture_output=True, check=True, timeout=10)
            exported = json.loads(result.stdout)
            self.assertEqual(exported["selection_status"], "changes_pending")
            self.assertEqual(exported["selections"][0]["selected"], "option-1")
            self.assertEqual(exported["selections"][0]["original_selected"], "option-0")
            self.assertEqual(data["scenes"][0]["selected"], "option-0")


if __name__ == "__main__":
    unittest.main()
