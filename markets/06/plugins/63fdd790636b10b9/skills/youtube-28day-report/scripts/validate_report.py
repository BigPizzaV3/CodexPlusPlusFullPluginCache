#!/usr/bin/env python3
"""Check a finished report's HTML structure. No network or source-data verification."""
import argparse
import json
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

VIDEO_ID = re.compile(r"^[A-Za-z0-9_-]{11}$")
TOKEN = re.compile(r"\{\{[A-Z][A-Z0-9_]*\}\}")


class Report(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.nodes = []
        self.text = []
        self.skip = 0
        self.errors = []
        self.ids = []
        self.anchors = []
        self.links = []
        self.frames = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.nodes.append((tag, a))
        if tag in ("script", "style"):
            self.skip += 1
        if a.get("id"):
            self.ids.append(a["id"])
        if tag == "details" or a.get("role") in ("tab", "tabpanel"):
            self.errors.append("折り畳み・タブ表示を使わず、本文を全展開してください。")
        if "hidden" in a:
            self.errors.append("非表示の要素があります。本文を隠していないか確認してください。")
        if re.search(r"(?:display\s*:\s*none|visibility\s*:\s*hidden)", a.get("style", ""), re.I):
            self.errors.append("インラインCSSに非表示指定があります。")
        if tag == "a":
            href = a.get("href", "")
            self.links.append(href)
            if href.startswith("#"):
                self.anchors.append(href[1:])
            if href.startswith("javascript:"):
                self.errors.append("リンク先に実行コードがあります。通常のURLにしてください。")
        if tag == "iframe":
            self.frames.append(a)
        if tag == "img":
            self.images.append(a)

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)

    def handle_data(self, text):
        if not self.skip:
            self.text.append(text)


def watch_id(url):
    p = urlsplit(url)
    if p.hostname in ("youtube.com", "www.youtube.com", "m.youtube.com"):
        return parse_qs(p.query).get("v", [None])[0]
    if p.hostname == "youtu.be":
        return p.path.strip("/")
    return None


def validate(path, template=False):
    source = Path(path).read_text(encoding="utf-8")
    doc = Report()
    doc.feed(source)
    errors = list(doc.errors)
    warnings = []
    tokens = sorted(set(TOKEN.findall(source)))
    if tokens and not template:
        errors.append("置換前の項目が残っています: " + ", ".join(tokens))
    if not any(t == "html" and a.get("lang", "").startswith("ja") for t, a in doc.nodes):
        errors.append("HTMLの言語を日本語に指定してください。")
    if not any(t == "meta" and a.get("name") == "viewport" for t, a in doc.nodes):
        errors.append("スマートフォン向けviewport指定がありません。")
    for ident, count in Counter(doc.ids).items():
        if count > 1:
            errors.append("重複するID: " + ident)
    for target in set(doc.anchors):
        if template and TOKEN.search(target):
            continue
        if target and target not in doc.ids:
            errors.append("移動先がないページ内リンク: #" + target)
    links = {watch_id(x) for x in doc.links}
    thumbnails = set()
    for img in doc.images:
        if not img.get("alt"):
            warnings.append("説明のない画像があります。altを確認してください。")
        match = re.search(r"/(?:vi|vi_webp)/([^/]+)/", img.get("src", ""))
        if match:
            thumbnails.add(match.group(1))
    embed_ids = []
    for frame in doc.frames:
        src = frame.get("src", "")
        p = urlsplit(src)
        if p.hostname not in ("www.youtube.com", "youtube.com", "www.youtube-nocookie.com", "youtube-nocookie.com"):
            errors.append("YouTube以外の埋め込みがあります。必要性とリンク先を確認してください。")
            continue
        ident = p.path.removeprefix("/embed/").strip("/")
        if template and TOKEN.search(ident):
            continue
        if not p.path.startswith("/embed/") or not VIDEO_ID.fullmatch(ident):
            errors.append("YouTubeの埋め込みIDが不正です: " + ident)
            continue
        embed_ids.append(ident)
        if not frame.get("title"):
            errors.append("埋め込みに動画名のtitle指定がありません: " + ident)
        if parse_qs(p.query).get("autoplay", ["0"])[0] != "0":
            errors.append("動画の自動再生を止めてください: " + ident)
        if ident not in links:
            errors.append("埋め込みと一致する常時表示用YouTubeリンクがありません: " + ident)
        if ident not in thumbnails:
            warnings.append("埋め込みに対応する外部サムネイルを検出できません。埋込画像や未取得表示を確認: " + ident)
    if not embed_ids and not template:
        warnings.append("動画の埋め込みがありません。参考動画の確認状況を確かめてください。")
    text = " ".join(doc.text)
    if "**" in text:
        errors.append("本文にMarkdownの太字記号が残っています。")
    if not any(t == "h1" for t, _ in doc.nodes):
        errors.append("レポートの見出しh1がありません。")
    return {
        "file": str(Path(path).resolve()),
        "ok": not errors,
        "errors": list(dict.fromkeys(errors)),
        "warnings": list(dict.fromkeys(warnings)),
        "counts": {"images": len(doc.images), "youtube_embeds": len(embed_ids), "links": len(doc.links)},
        "requires_manual_review": [
            "元データとの数値・期間・分母の一致、外部候補の実在と推薦理由",
            "CSS・JavaScriptを含む全展開表示、画面幅ごとの文字切れ・重なり",
            "実画像の一致、動画の再生可否、次月引継ぎメモの内容",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html_file")
    parser.add_argument("--template", action="store_true", help="Allow unfilled template tokens")
    args = parser.parse_args()
    result = validate(args.html_file, args.template)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
