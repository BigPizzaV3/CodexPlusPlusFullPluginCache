"""Regression coverage for a scene containing an ordered still-image sequence.

Run with: python -m unittest discover -s skills/editor-handoff/scripts/tests -v
No network, generated medical material, browser, or external fixture is needed.
"""
from __future__ import annotations

import base64
from html.parser import HTMLParser
import json
from pathlib import Path
import struct
import sys
import tempfile
import unittest
import zlib

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_handoff as handoff
import preview_renderer as preview


class Images(HTMLParser):
    def __init__(self, document):
        super().__init__(convert_charrefs=True)
        self.items = []
        self.feed(document)
        self.close()

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            self.items.append(dict(attrs))


def png(rgb):
    """A small valid RGB PNG with a distinct payload for each supplied color."""
    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xffffffff)
    header = struct.pack(">IIBBBBB", 12, 12, 8, 2, 0, 0, 0)
    pixels = (b"\0" + bytes(rgb) * 12) * 12
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header) + chunk(b"IDAT", zlib.compress(pixels)) + chunk(b"IEND", b"")


def option(title, files, status="ready", mode="square"):
    return {"id": "recommended", "title": title, "type": "確認用の画像", "reason": "表示を確認", "description": "確認用", "mode": mode, "status": status, "files": files}


class MultiImageTests(unittest.TestCase):
    def test_private_link_default_preserves_content_and_separates_delivery_checks(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "assets").mkdir()
            still = root / "assets" / "still.png"
            still.write_bytes(png((30, 100, 160)))
            source_path = root / "source.md"
            source_path.write_text("# 確認用原稿\n\n本文も素材も省略せず確認します。\n", encoding="utf-8")
            source_hash = handoff.sha256(source_path)
            item = option("確認用図解", ["assets/still.png"])
            item.update(kind="diagram", production={"method": "layout", "tool": "test-fixture", "evidence": "確認用PNGを作成", "review": {"status": "passed", "evidence": "確認用画像の記録", "files_sha256": {"assets/still.png": handoff.sha256(still)}}})
            quality = {"version": 1, "source_sha256": source_hash, "capabilities": {name: {"status": "not_needed", "evidence": "この確認用素材では使用しない"} for name in ("image_generation", "video_generation")}, "profile_assets": [{"role": role, "status": "not_applicable", "evidence": "確認用案件に本人素材は不要"} for role in ("intro", "ending", "gift")], "reviews": {name: {"status": "passed", "evidence": "確認用案件を点検"} for name in ("material_mix", "visual", "editor_ready")}}
            quality["capabilities"]["file_output"] = {"status": "verified", "tool": "test-fixture", "evidence": "PNGと原稿を出力・読み戻し"}
            case = {"case_id": "private-link-regression", "title": "確認リンクの既定動作", "doctor_id": "test-doctor", "source": {"path": "source.md", "version": "1", "sha256": source_hash}, "profile": {"id": "test-doctor", "version": "1", "design_version": "1"}, "design": {"background": "#ffffff", "ink": "#111111", "accent": "#117777"}, "scenes": [{"id": "scene-1", "purpose": "全文と画像の確認", "quote": "本文も素材も省略せず確認します。", "end_cue": "発話の終わり", "duration": 5, "placement": "本文の指定位置", "selected": "recommended", "options": [item]}], "quality": quality}
            case_path = root / "case.json"
            case_path.write_text(json.dumps(case, ensure_ascii=False), encoding="utf-8")
            case, source, source_path, source_hash, assets, _ = handoff.validate(case_path)
            output = root / "delivery"
            manifest = handoff.package(case, source, source_path, source_hash, assets, output)
            self.assertEqual(manifest["status"], "complete")
            self.assertEqual(manifest["preview"]["inline"]["status"], "not_applicable")
            self.assertFalse((output / "preview-parts").exists())
            self.assertEqual(manifest["preview"]["source_coverage"], "complete")
            self.assertEqual(manifest["preview"]["delivery"]["required_visibility"], "private")
            document = (output / "preview.html").read_text(encoding="utf-8")
            self.assertIn("確認のためのZIP展開は不要です", document)
            self.assertNotIn("<b>ZIP全体を展開</b>", document)
            self.assertEqual(base64.b64decode(Images(document).items[0]["src"].split(",", 1)[1]), still.read_bytes())
            self.assertEqual((output / "source-script.md").read_bytes(), source_path.read_bytes())
            self.assertEqual((output / "assets/still.png").read_bytes(), still.read_bytes())
            checks = manifest["quality"]["host_checks"]
            self.assertEqual(checks["hosted"]["status"], "not_run")
            self.assertEqual(checks["browser"]["status"], "not_run")
            self.assertEqual(checks["chat_preview"]["status"], "not_applicable")
            case["quality"]["host_checks"] = {"hosted": {"status": "passed", "evidence": "配信応答だけを取得", "url": "https://review.example.test"}}
            unverified = handoff.assess_quality(case, root)
            self.assertEqual(unverified["host_checks"]["hosted"]["status"], "not_run")
            self.assertTrue(any(x["code"] == "host.private_unverified" for x in unverified["blockers"]))
            case["quality"]["host_checks"]["hosted"]["visibility"] = "public"
            self.assertEqual(handoff.assess_quality(case, root)["host_checks"]["hosted"]["status"], "failed")
            case["quality"]["host_checks"]["hosted"].update(visibility="private", evidence="配信成功とget_siteのprivateを確認")
            case["quality"]["host_checks"]["chat_preview"] = {"status": "not_run", "evidence": "旧形式の会話表示未確認記録"}
            verified = handoff.assess_quality(case, root)
            self.assertEqual(verified["status"], "passed")
            self.assertEqual(verified["host_checks"]["hosted"]["status"], "passed")
            self.assertEqual(verified["host_checks"]["browser"]["status"], "not_run")

    def test_three_images_in_script_gallery_standalone_and_all_inline_parts(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "assets").mkdir()
            names = ["step-a.png", "step-b.png", "step-c.png", "single.png", "reference.png"]
            payloads = {}
            for index, name in enumerate(names):
                payloads[name] = png((index * 40, 90, 170))
                (root / "assets" / name).write_bytes(payloads[name])
            source = "# 確認用原稿\n\n順番に三つの画像を使います。\n\n一枚の画像を使います。\n\n最初の画像をもう一度使います。\n\nここは制作待ちです。\n"
            source_path = root / "source.md"
            source_path.write_text(source, encoding="utf-8")
            triple = option("連続画像", ["assets/" + name for name in names[:3]])
            single = option("単独画像", ["assets/single.png"])
            reused = option("再利用画像", ["assets/step-a.png"])
            pending = option("未制作素材", [], status="pending")
            pending["poster"] = "assets/reference.png"
            scenes = []
            for index, (quote, item) in enumerate(zip(source.splitlines()[2::2], (triple, single, reused, pending))):
                scenes.append({"id": "scene-" + str(index), "quote": quote, "end_cue": "発話の終わり", "duration": 8, "placement": "本文の指定位置", "selected": "recommended", "options": [item]})
            case = {"case_id": "renderer-regression", "title": "複数画像の確認", "doctor_id": "test-doctor", "source": {"path": "source.md", "version": "1", "sha256": handoff.sha256(source_path)}, "profile": {"id": "test-doctor", "version": "1", "design_version": "1"}, "design": {"background": "#ffffff", "ink": "#111111", "accent": "#117777"}, "scenes": scenes, "preview": {"inline_requested": True}}
            case_path = root / "case.json"
            case_path.write_text(json.dumps(case, ensure_ascii=False), encoding="utf-8")
            case, source, source_path, source_hash, assets, _ = handoff.validate(case_path)
            output = root / "delivery"
            manifest = handoff.package(case, source, source_path, source_hash, assets, output)
            documents = {name: (output / name).read_text(encoding="utf-8") for name in ("script.html", "index.html", "preview.html")}
            documents["inline"] = "".join(path.read_text(encoding="utf-8") for path in sorted((output / "preview-parts").glob("*.html")))
            for name, document in documents.items():
                with self.subTest(output=name):
                    images = Images(document).items
                    sequence = [image for image in images if image.get("alt", "").startswith("連続画像")]
                    expected_names = names[:3] * 2  # adopted visual, then option preview
                    self.assertEqual(len(sequence), 6)
                    self.assertEqual([next(filename for filename in names[:3] if filename in image["alt"]) for image in sequence], expected_names)
                    for image, filename in zip(sequence, expected_names):
                        if name in {"preview.html", "inline"}:
                            self.assertEqual(base64.b64decode(image["src"].split(",", 1)[1]), payloads[filename])
                        else:
                            self.assertEqual(image["src"], "assets/" + filename)
                    self.assertEqual(sum(image.get("alt") == "単独画像" for image in images), 2)
                    self.assertEqual(sum(image.get("alt") == "再利用画像" for image in images), 2)
                    self.assertEqual(sum(image.get("alt") == "制作前の参考画像" for image in images), 2)
                    self.assertEqual(document.count("制作待ち。本編に使用できる完成素材はまだありません。"), 2)
                    for index, filename in enumerate(names[:3], 1):
                        self.assertIn(f"画像 {index} / 3 · {filename}", document)
                    self.assertIn("採用・完成済み 3場面（静止画 3場面／動画 0場面）", document)
                    self.assertIn("採用素材の実ファイル：静止画 4枚／動画 0本", document)
            self.assertEqual(manifest["counts"]["selected_ready_stills"], 3)
            self.assertEqual(manifest["counts"]["selected_ready_still_files"], 4)
            self.assertEqual(manifest["counts"]["selected_ready_videos"], 0)
            self.assertEqual(manifest["counts"]["selected_ready_video_files"], 0)
            readme = (output / "README.txt").read_text(encoding="utf-8")
            self.assertIn("採用・完成済みの場面数: 静止画 3場面 / 動画 0場面", readme)
            self.assertIn("採用素材の実ファイル数: 静止画 4枚 / 動画 0本", readme)
            self.assertEqual(manifest["preview"]["source_coverage"], "complete")
            self.assertEqual(manifest["preview"]["inline"]["source_coverage"], "complete")
            self.assertEqual(manifest["preview"]["blockers"], [])
            self.assertEqual((output / "source-script.md").read_bytes(), source_path.read_bytes())
            for filename, payload in payloads.items():
                self.assertEqual((output / "assets" / filename).read_bytes(), payload)

    def test_single_image_video_pending_and_unselected_markup_are_unchanged(self):
        single = option('題名 & "引用"', ["assets/still.png"])
        single["_files"] = single["files"]
        self.assertEqual(handoff.media_html(single), '<a href="assets/still.png" target="_blank" rel="noreferrer"><img loading="lazy" src="assets/still.png" alt="題名 &amp; &quot;引用&quot;"></a>')
        motion = option("動画", ["assets/clip.mp4", "assets/still.png"], mode="motion")
        motion.update(_files=motion["files"], _poster="assets/poster.png")
        self.assertEqual(handoff.media_html(motion), '<video controls playsinline preload="metadata" poster="assets/poster.png" src="assets/clip.mp4"></video>')
        pending = option("制作待ち", ["assets/still.png"], status="pending")
        pending.update(_files=pending["files"], _poster="assets/poster.png")
        self.assertEqual(handoff.media_html(pending), '<img src="assets/poster.png" alt="制作前の参考画像"><div class="placeholder">制作待ち。本編に使用できる完成素材はまだありません。</div>')
        self.assertEqual(handoff.media_html(None), '<div class="placeholder">この位置の素材を選んでください。</div>')

    def test_display_budget_counts_all_images_without_changing_single_image_policy(self):
        self.assertEqual(preview.card_image_targets('<figure class="asset-card"><img src="a.png"><img src="a.png"></figure>'), {})
        document = '<figure class="asset-card">' + ''.join('<div><img src="' + name + '" /></div>' for name in ["a.png", "b.png", "c.png"] * 2) + '</figure>'
        self.assertEqual(preview.card_image_targets(document), {name: preview.IMAGE_TARGET // 3 for name in ("a.png", "b.png", "c.png")})

    def test_file_counts_deduplicate_reuse_and_exclude_posters_and_unselected_options(self):
        triple = option("3画像", ["input/a.png", "input/b.png", "input/c.png"])
        # Resolved delivery paths take precedence over source paths when present.
        triple["_files"] = ["assets/a.png", "assets/b.png", "assets/c.png"]
        reused = option("1画像を再利用", ["assets/a.png"])
        motion = option("動画", ["assets/clip.mp4", "assets/poster.png"], mode="motion")
        motion["poster"] = "assets/poster.png"
        motion_again = option("動画を再利用", ["input/clip.mp4", "input/poster.png"], mode="motion")
        motion_again.update(_files=["assets/clip.mp4", "assets/poster.png"], _poster="assets/poster.png")
        pending = option("未制作", ["assets/pending.png"], status="pending")
        unselected = option("未採用", ["assets/unused.png"])
        unselected["id"] = "alternative"
        scenes = [{"selected": "recommended", "options": [item, unselected]} for item in (triple, reused, motion, motion_again, pending)]
        counts = handoff.counts({"scenes": scenes})
        self.assertEqual(counts["selected_ready_stills"], 2)
        self.assertEqual(counts["selected_ready_videos"], 2)
        self.assertEqual(counts["selected_ready_still_files"], 3)
        self.assertEqual(counts["selected_ready_video_files"], 1)
        self.assertEqual(counts["pending_scenes"], 1)


if __name__ == "__main__":
    unittest.main()

