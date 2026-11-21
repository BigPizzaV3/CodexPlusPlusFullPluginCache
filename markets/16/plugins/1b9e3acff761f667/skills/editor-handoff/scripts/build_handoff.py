#!/usr/bin/env python3
"""Build a portable editor handoff from verified source and existing media.
Python 3.10+, standard library only. No image/video generation occurs here.
Usage: python build_handoff.py case.json --output delivery --zip delivery.zip
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import html
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import tempfile
import urllib.parse
import unicodedata
import xml.etree.ElementTree as ET
import zipfile
from preview_renderer import build_previews
from quality_gate import assess_quality

GENERATOR = "dr-shigyo-editor-handoff/1"
ASSET_ROOT = Path(__file__).resolve().parents[1] / "assets"
ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,99}\Z")
COL = re.compile(r"#[0-9a-fA-F]{6}\Z")
IMAGES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".avif"}
VIDEOS = {".mp4", ".webm", ".mov", ".m4v"}
MODES = {"square": "正方形インサート", "full": "全画面の静止画", "motion": "全画面の動画", "overlay": "画像を重ねる"}
STATUS = {"ready": "実ファイルあり", "proposal": "未制作の案", "pending": "制作待ち"}
MEDICAL_STYLES = {"anatomical": "解剖関係を重視", "cute": "かわいい概念表現", "schematic": "要点だけの模式図", "context": "全体と部位の関係", "metaphor": "たとえで理解"}
CITATION = re.compile(r"(?:\(\*(?P<legacy>[1-9][0-9]*)\)|（引用文献挿入：(?P<number>[1-9][0-9]*)）)")
REFERENCE_HEADINGS = {"引用論文", "引用論文まとめ", "引用文献", "参考文献", "文献一覧", "文献・出典", "参考文献・出典", "参考資料・出典", "出典一覧"}
esc = lambda value: html.escape(str(value), quote=True)


class ValidationError(ValueError):
    pass


def require(ok, message):
    if not ok:
        raise ValidationError(message)


def citation_text(raw, replacement=None):
    """Render explicit reference markers; bare (1)/[1] may be ordinary script text."""
    def visible(value):
        # A bare URL is also a destination, not editable citation text.
        parts = re.split(r"(https?://[^\s<>]+)", value)
        return "".join(part if index % 2 else CITATION.sub(
            lambda match: ("（引用文献挿入：" + (match["number"] or match["legacy"]) + "）") if replacement is None else replacement, part)
            for index, part in enumerate(parts))
    pieces, cursor = [], 0
    for start, end, label, url in markdown_links(raw):
        pieces += [visible(raw[cursor:start]), "[" + visible(label) + "](" + url + ")"]
        cursor = end
    pieces.append(visible(raw[cursor:]))
    return "".join(pieces)


def markdown_links(raw):
    """Yield HTTP(S) Markdown links, including balanced parentheses in the URL."""
    cursor = 0
    for match in re.finditer(r"\[([^\]\n]+)\]\((https?://)", raw):
        if match.start() < cursor:
            continue
        url_start = match.start(2)
        depth, end = 1, url_start
        while end < len(raw) and not raw[end].isspace():
            if raw[end] == "(":
                depth += 1
            elif raw[end] == ")":
                depth -= 1
                if depth == 0:
                    yield match.start(), end + 1, match[1], raw[url_start:end]
                    cursor = end + 1
                    break
            end += 1


def validate_citation_markers(raw):
    remaining = CITATION.sub("", raw)
    require("(*" not in remaining and "引用文献挿入" not in remaining,
            "引用文献マーカーは（引用文献挿入：1）の形式で指定してください（番号は正の整数）")


def prompter_text(raw):
    """Editorial reference cues are never read aloud; retain all other wording."""
    validate_citation_markers(raw)
    return citation_text(raw, replacement="")


def sha256(path):
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for data in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(data)
    return value.hexdigest()


def no_symlinks(path):
    path = path.absolute()
    for part in [*reversed(path.parents), path]:
        require(not part.is_symlink(), f"シンボリックリンクは使用できません: {part}")


def text_field(obj, name, context, empty=False):
    value = obj.get(name)
    require(isinstance(value, str) and (empty or bool(value.strip())), f"{context}.{name}: 文字列が必要です")
    require("\x00" not in value, f"{context}.{name}: NUL文字は使用できません")
    return value


def numeric(value, context):
    require(type(value) in (int, float) and math.isfinite(value) and value > 0, f"{context}: 正の数が必要です")


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, f"JSONのキーが重複しています: {key}")
            result[key] = value
        return result
    def invalid_number(value):
        raise ValidationError(f"不正なJSON数値: {value}")
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"), object_pairs_hook=unique, parse_constant=invalid_number)
    except (json.JSONDecodeError, UnicodeError) as error:
        raise ValidationError(f"JSONを読み込めません: {error}") from error


def safe_input(root, value, context):
    require(isinstance(value, str) and bool(value), f"{context}: ファイルの相対パスが必要です")
    parts = PurePosixPath(value)
    require(not parts.is_absolute() and not any(p in ("", ".", "..") for p in value.split("/")), f"{context}: 絶対パス・./・../は使用できません")
    require(not re.search(r"[\\:\x00-\x1f\x7f]", value), f"{context}: 不正なパス文字です")
    path = root.joinpath(*parts.parts)
    no_symlinks(path)
    require(path.is_file() and path.stat().st_size > 0, f"{context}: 空でない実ファイルが必要です: {value}")
    require(path.resolve().is_relative_to(root), f"{context}: 入力フォルダ外の参照です")
    return path


def valid_media(path):
    suffix = path.suffix.lower()
    require(suffix in IMAGES | VIDEOS | {".pdf"}, f"未対応の素材形式です: {path.name}")
    with path.open("rb") as stream:
        head = stream.read(64)
    checks = {
        ".png": head.startswith(b"\x89PNG\r\n\x1a\n"),
        ".jpg": head.startswith(b"\xff\xd8\xff"), ".jpeg": head.startswith(b"\xff\xd8\xff"),
        ".gif": head.startswith((b"GIF87a", b"GIF89a")),
        ".webp": head.startswith(b"RIFF") and head[8:12] == b"WEBP",
        ".pdf": head.startswith(b"%PDF-"), ".webm": head.startswith(b"\x1a\x45\xdf\xa3"),
        ".mp4": b"ftyp" in head[:32], ".m4v": b"ftyp" in head[:32],
        ".mov": any(x in head[:32] for x in (b"ftyp", b"moov", b"mdat")),
        ".avif": b"ftyp" in head[:32] and any(x in head[:64] for x in (b"avif", b"avis")),
    }
    if suffix == ".svg":
        raw = path.read_text(encoding="utf-8-sig")
        require(not re.search(r"<!DOCTYPE|<!ENTITY", raw, re.I), f"SVGの外部定義は使用できません: {path.name}")
        try:
            tree = ET.fromstring(raw)
        except ET.ParseError as error:
            raise ValidationError(f"SVGを解析できません: {path.name}") from error
        require(tree.tag.rsplit("}", 1)[-1] == "svg", f"SVGではありません: {path.name}")
        for node in tree.iter():
            require(node.tag.rsplit("}", 1)[-1].lower() not in {"script", "foreignobject", "iframe", "a"}, f"SVGの実行要素は禁止です: {path.name}")
            for key, value in node.attrib.items():
                key = key.rsplit("}", 1)[-1].lower()
                require(not key.startswith("on"), f"SVGのイベント属性は禁止です: {path.name}")
                if key in {"href", "src"}:
                    require(value.startswith("#") or value.startswith("data:image/"), f"SVGの外部参照は禁止です: {path.name}")
        for url in re.findall(r"url\(\s*['\"]?([^)'\"\s]+)", raw, re.I):
            require(url.startswith("#"), f"SVGの外部CSS参照は禁止です: {path.name}")
        require(not re.search(r"@import", raw, re.I), f"SVGのCSS importは禁止です: {path.name}")
    else:
        require(checks[suffix], f"拡張子とファイル形式が一致しません: {path.name}")


def unique_quote(source, quote, context):
    start = source.find(quote)
    require(start >= 0, f"{context}: 引用が原稿に存在しません: {quote[:70]}")
    require(source.find(quote, start + 1) < 0, f"{context}: 引用が複数あります。前後を含め一意にしてください: {quote[:70]}")
    return start


def validate(case_path):
    no_symlinks(case_path)
    require(case_path.is_file(), "case.json が見つかりません")
    case_path = case_path.resolve()
    root, case = case_path.parent, read_json(case_path)
    require(isinstance(case, dict), "case.json はオブジェクトにしてください")
    for key in ("case_id", "title", "doctor_id"):
        text_field(case, key, "case")
    require(ID.fullmatch(case["case_id"]), "case_id は英数字・ハイフン・アンダースコアで指定してください")
    for key in ("source", "profile", "design"):
        require(isinstance(case.get(key), dict), f"case.{key}: オブジェクトが必要です")
    source_path = safe_input(root, case["source"].get("path"), "source.path")
    text_field(case["source"], "version", "source")
    expected_hash = text_field(case["source"], "sha256", "source")
    require(re.fullmatch(r"[a-fA-F0-9]{64}", expected_hash), "source.sha256 はSHA-256値が必要です")
    actual_hash = sha256(source_path)
    require(actual_hash == expected_hash.lower(), "原稿のSHA-256が一致しません。case.jsonを更新してから再生成してください")
    try:
        source = source_path.read_text(encoding="utf-8-sig")
    except UnicodeError as error:
        raise ValidationError("原稿はUTF-8 Markdownにしてください") from error
    require(bool(source.strip()), "原稿が空です")
    for _, _, raw, _, is_body in script_blocks(source):
        if is_body:
            validate_citation_markers(raw)
    for key in ("id", "version", "design_version"):
        text_field(case["profile"], key, "profile")
    require(case["profile"]["id"] == case["doctor_id"], "doctor_id と profile.id が一致しません")
    for key in ("background", "ink", "accent"):
        require(COL.fullmatch(text_field(case["design"], key, "design")), f"design.{key}: #RRGGBBで指定してください")
    require(isinstance(case.get("scenes"), list), "scenes は配列が必要です")
    require(isinstance(case.get("digest", []), list), "digest は配列が必要です")
    inputs = {case_path, source_path}
    assets, destinations = {}, {}

    def register(value, context, category="assets"):
        path = safe_input(root, value, context)
        valid_media(path)
        inputs.add(path)
        destination = category + "/" + path.name
        key = unicodedata.normalize("NFC", destination).casefold()
        if key in destinations:
            require(destinations[key] == path, f"素材ファイル名が衝突しています。名前を変えてください: {path.name}")
        destinations[key] = path
        # Category is part of the key: a file may legitimately be both a recording and an option.
        assets[(category, value)] = {"source": path, "path": destination, "sha256": sha256(path), "bytes": path.stat().st_size}
        return destination

    seen_scenes = set()
    for index, scene in enumerate(case["scenes"]):
        context = f"scenes[{index}]"
        require(isinstance(scene, dict), f"{context}: オブジェクトが必要です")
        sid = text_field(scene, "id", context)
        require(ID.fullmatch(sid) and sid not in seen_scenes, f"{context}.id: 不正または重複したIDです")
        seen_scenes.add(sid)
        quote = text_field(scene, "quote", context)
        scene["_start"] = unique_quote(source, quote, context)
        for key in ("end_cue", "placement"):
            text_field(scene, key, context)
        duration = scene.get("duration")
        require((isinstance(duration, str) and bool(duration.strip())) or (type(duration) in (int, float) and math.isfinite(duration) and duration > 0), f"{context}.duration: 目安の説明または秒数が必要です")
        require("selected" in scene, f"{context}.selected がありません")
        selected = scene["selected"]
        require(selected is None or isinstance(selected, str), f"{context}.selected: IDかnullが必要です")
        require(type(scene.get("omit", False)) is bool, f"{context}.omit: 真偽値が必要です")
        require(not scene.get("omit") or selected is None, f"{context}: omit:true と選択IDは同時に使えません")
        require(isinstance(scene.get("options"), list), f"{context}.options: 配列が必要です")
        seen_options = set()
        for opt_index, option in enumerate(scene["options"]):
            op = f"{context}.options[{opt_index}]"
            require(isinstance(option, dict), f"{op}: オブジェクトが必要です")
            oid = text_field(option, "id", op)
            require(ID.fullmatch(oid) and oid not in seen_options and oid not in {"__none__", "__unselected__"}, f"{op}.id: 不正または重複したIDです")
            seen_options.add(oid)
            for key in ("title", "type", "reason", "description"):
                text_field(option, key, op, empty=key in {"reason", "description"})
            require(isinstance(option.get("mode"), str) and option["mode"] in MODES, f"{op}.mode: square/full/motion/overlayが必要です")
            require(isinstance(option.get("status"), str) and option["status"] in STATUS, f"{op}.status: ready/proposal/pendingが必要です")
            if "medical_visual" in option:
                medical = option["medical_visual"]
                require(isinstance(medical, dict), f"{op}.medical_visual: オブジェクトが必要です")
                require(isinstance(medical.get("style"), str) and medical["style"] in MEDICAL_STYLES, f"{op}.medical_visual.style: 対応する表現方法が必要です")
                text_field(medical, "explanation", op + ".medical_visual")
                if "review" in medical:
                    review = medical["review"]
                    require(isinstance(review, dict), f"{op}.medical_visual.review: オブジェクトが必要です")
                    require(isinstance(review.get("references", []), list) and all(isinstance(x, str) for x in review.get("references", [])), f"{op}.medical_visual.review.references: 文字列の配列が必要です")
            require(isinstance(option.get("files"), list), f"{op}.files: 配列が必要です")
            require(all(isinstance(x, str) for x in option["files"]), f"{op}.files: パスは文字列にしてください")
            require(len(option["files"]) == len(set(option["files"])), f"{op}.files: ファイルが重複しています")
            option["_files"] = [register(value, op + ".files") for value in option["files"]]
            if option.get("poster"):
                poster = register(option["poster"], op + ".poster")
                require(Path(poster).suffix.lower() in IMAGES, f"{op}.poster: 静止画像が必要です")
                option["_poster"] = poster
            if option["status"] == "ready":
                allowed = {".mp4", ".webm"} if option["mode"] == "motion" else IMAGES
                require(any(Path(x).suffix.lower() in allowed for x in option["_files"]), f"{op}: ready には実際の表示用ファイルが必要です（動画はMP4/WebM）")
        require(selected is None or selected in seen_options, f"{context}.selected: 候補にないIDです")
        if "medical_variants" in scene:
            variants = scene["medical_variants"]
            require(isinstance(variants, dict), f"{context}.medical_variants: オブジェクトが必要です")
            target = variants.get("target_count")
            require(type(target) is int and 3 <= target <= 5, f"{context}.medical_variants.target_count: 3〜5の整数が必要です")
            ids = variants.get("option_ids")
            require(isinstance(ids, list) and all(isinstance(x, str) for x in ids), f"{context}.medical_variants.option_ids: IDの配列が必要です")
            require(len(ids) == target and len(set(ids)) == len(ids) and set(ids) <= seen_options, f"{context}.medical_variants.option_ids: target_countと同数の、重複しない実在の候補IDが必要です")
            text_field(variants, "reason", context + ".medical_variants")

    intervals = []
    for index, item in enumerate(case.get("digest", [])):
        context = f"digest[{index}]"
        require(isinstance(item, dict), f"{context}: オブジェクトが必要です")
        quote = text_field(item, "quote", context)
        text_field(item, "display", context)
        require(isinstance(item.get("status"), str) and item["status"] in {"approved", "proposed"}, f"{context}.status: approved/proposedが必要です")
        start = unique_quote(source, quote, context)
        end = start + len(quote)
        for marker in CITATION.finditer(source):
            require(not (marker.start() < start < marker.end() or marker.start() < end < marker.end()),
                    f"{context}: ダイジェストで引用文献マーカーの途中を切り抜くことはできません")
        require(all(end <= a or start >= b for a, b in intervals), f"{context}: ダイジェストの抜き出し範囲が重複しています")
        intervals.append((start, end))
        item["_start"] = start
    if "recording" in case:
        rec = case["recording"]
        require(isinstance(rec, dict), "recording はオブジェクトにしてください")
        rec["_file"] = register(rec.get("file"), "recording.file", "media")
        require(Path(rec["_file"]).suffix.lower() in VIDEOS, "recording.file は動画が必要です")
        for key in ("duration_seconds", "width", "height", "fps"):
            if key in rec:
                numeric(rec[key], "recording." + key)
        for key in ("width", "height"):
            if key in rec:
                require(type(rec[key]) is int, f"recording.{key}: 整数が必要です")
        if "has_audio" in rec:
            require(type(rec["has_audio"]) is bool, "recording.has_audio: 真偽値が必要です")
    if case.get("prompter_path"):
        path = safe_input(root, case["prompter_path"], "prompter_path")
        require(path.suffix.lower() in {".md", ".txt"}, "プロンプター原稿はMarkdownまたはテキストにしてください")
        inputs.add(path)
        case["_prompter"] = path
        # Validate before output writes; keep the supplied source file untouched.
        case["_prompter_text"] = prompter_text(path.read_text(encoding="utf-8-sig"))
    require(isinstance(case.get("notes", []), list) and all(isinstance(x, str) for x in case.get("notes", [])), "notes は文字列の配列が必要です")
    preview = case.get("preview", {})
    require(isinstance(preview, dict), "preview はオブジェクトにしてください")
    require(type(preview.get("inline_requested", False)) is bool, "preview.inline_requested は真偽値が必要です")
    case["_quality_report"] = assess_quality(case, root)
    return case, source, source_path, actual_hash, assets, inputs


def href(path):
    return esc(urllib.parse.quote(path, safe="/"))


def inline(raw, citations=True):
    def text(value):
        value = citation_text(value) if citations else value
        return re.sub(r"\*\*([^\n]+?)\*\*", r"<strong>\1</strong>", esc(value))
    # Parse links before normalizing text so reference-looking URL text is intact.
    pieces, cursor = [], 0
    for start, end, label, url in markdown_links(raw):
        pieces += [text(raw[cursor:start]),
                   f'<a href="{esc(url)}" target="_blank" rel="noreferrer">{text(label)}</a>']
        cursor = end
    pieces.append(text(raw[cursor:]))
    return "".join(pieces)


def source_fragment(raw, offset, case, anchored, citations=True):
    bits, cursor = [], 0
    for index, item in sorted(enumerate(case.get("digest", []), 1), key=lambda value: value[1]["_start"]):
        a, b = max(offset, item["_start"]), min(offset + len(raw), item["_start"] + len(item["quote"]))
        if a >= b:
            continue
        bits.append(inline(raw[cursor:a - offset], citations))
        ident = f' id="digest-source-{index}"' if index not in anchored else ""
        anchored.add(index)
        bits.append(f'<strong class="digest-highlight"{ident}>{inline(raw[a - offset:b - offset], citations)}</strong>')
        cursor = b - offset
    bits.append(inline(raw[cursor:], citations))
    return "".join(bits)


def blocks(source):
    """Preserve every original heading and nonempty paragraph; do not reflow."""
    offset, buffer, start = 0, [], 0
    for line in source.splitlines(keepends=True):
        heading = re.match(r"^(#{1,6})[ \t]+(.+?)[\r\n]*$", line)
        if not line.strip() or heading:
            if buffer:
                yield "paragraph", start, "".join(buffer).rstrip("\r\n"), 0
                buffer = []
            if heading:
                yield "heading", offset + heading.start(2), heading.group(2).rstrip("\r\n"), len(heading.group(1))
        else:
            if not buffer:
                start = offset
            buffer.append(line)
        offset += len(line)
    if buffer:
        yield "paragraph", start, "".join(buffer).rstrip("\r\n"), 0


def script_blocks(source):
    """Keep original offsets and bibliography numbering when formatting the body."""
    reference_level = None
    for kind, start, raw, level in blocks(source):
        if kind == "heading":
            if reference_level is not None and level <= reference_level:
                reference_level = None
            heading = re.sub(r"[*_`【】\[\]]", "", raw).strip()
            heading = re.sub(r"(?:（[^（）]*）|\([^()]*\))\s*$", "", heading).strip()
            if heading in REFERENCE_HEADINGS:
                reference_level = level
        yield kind, start, raw, level, kind == "paragraph" and reference_level is None


def media_html(option):
    if not option:
        return '<div class="placeholder">この位置の素材を選んでください。</div>'
    files = option["_files"]
    if option["status"] != "ready":
        poster = option.get("_poster")
        preview = f'<img src="{href(poster)}" alt="制作前の参考画像">' if poster else ""
        return preview + f'<div class="placeholder">{STATUS[option["status"]]}。本編に使用できる完成素材はまだありません。</div>'
    if option["mode"] == "motion":
        primary = next(x for x in files if Path(x).suffix.lower() in {".mp4", ".webm"})
        poster = f' poster="{href(option["_poster"])}"' if option.get("_poster") else ""
        return f'<video controls playsinline preload="metadata"{poster} src="{href(primary)}"></video>'
    images = [x for x in files if Path(x).suffix.lower() in IMAGES]
    if len(images) == 1:
        primary = images[0]
        return f'<a href="{href(primary)}" target="_blank" rel="noreferrer"><img loading="lazy" src="{href(primary)}" alt="{esc(option["title"])}"></a>'
    # A sequence is one option, but every supplied still is part of its preview.
    # Preserve the author-provided order instead of silently showing only page 1.
    items = []
    for index, filename in enumerate(images, 1):
        label = f"画像 {index} / {len(images)} · {Path(filename).name}"
        items.append(f'<div class="media-item"><p class="initial-note">{esc(label)}</p><a href="{href(filename)}" target="_blank" rel="noreferrer"><img loading="lazy" src="{href(filename)}" alt="{esc(option["title"])} — {esc(label)}"></a></div>')
    return '<div class="media-sequence">' + ''.join(items) + '</div>'


def medical_visual_html(option):
    """Display the declared explanation and review, without judging anatomy."""
    medical = option.get("medical_visual")
    if not medical:
        return ""
    review = medical.get("review", {})
    evidence = review.get("evidence", "")
    references = review.get("references", [])
    review_html = ""
    if evidence or references:
        sources = '<ul>' + ''.join('<li>' + esc(value) + '</li>' for value in references) + '</ul>' if references else ''
        review_html = '<details class="medical-review"><summary>確認記録と参考資料</summary><p>' + esc(evidence) + '</p>' + sources + '</details>'
    return '<div class="medical-explanation"><span class="medical-style">' + MEDICAL_STYLES[medical["style"]] + '</span><p><b>伝える内容・表現の範囲：</b>' + esc(medical["explanation"]) + '</p>' + review_html + '</div>'


def card(scene):
    selected = next((o for o in scene["options"] if o["id"] == scene["selected"]), None)
    sid = scene["id"]
    omitted = scene.get("omit", False)
    title = selected["title"] if selected else "素材なしで確定" if omitted else "素材の選択待ち"
    label = STATUS[selected["status"]] if selected else "素材なしで確定" if omitted else "未選択"
    option_items = []
    for option in scene["options"]:
        links = " ".join(f'<a href="{href(f)}" download>{esc(Path(f).name)}</a>' for f in option["_files"])
        option_items.append(f'''<div class="option-panel" data-option-id="{esc(option['id'])}">
<div class="option-head"><label><input type="radio" name="select-{sid}" value="{esc(option['id'])}" {'checked' if scene['selected'] == option['id'] else ''}> {esc(option['title'])}</label><span>{STATUS[option['status']]} · {MODES[option['mode']]}</span></div>
<p>{esc(option['reason'])}</p><p>{esc(option['description'])}</p>{medical_visual_html(option)}<div class="option-preview">{media_html(option)}</div><div class="downloads">{links}</div></div>''')
    choices = ''.join(option_items)
    choices_class, choices_open = "choices", ""
    variants = scene.get("medical_variants")
    if variants:
        ready = sum(option["status"] == "ready" for option in scene["options"] if option["id"] in variants["option_ids"])
        choices_class, choices_open = "choices medical-choices", " open"
        choices = f'<div class="medical-comparison"><p class="variant-count"><b>比較用素材：実ファイルあり {ready} / {variants["target_count"]}案</b></p><p>{esc(variants["reason"])}</p><p>各案の「伝える内容・表現の範囲」を見て選んでください。</p></div><div class="medical-options-grid">{choices}</div>'
    duration = str(scene["duration"]) + ("秒" if type(scene["duration"]) in (int, float) else "")
    downloads = "" if not selected or selected["status"] != "ready" else "".join(f'<a class="download" href="{href(f)}" download>{esc(Path(f).name)} を保存</a>' for f in selected["_files"])
    visual = '<div class="placeholder">この位置は話者映像のまま進めます。</div>' if omitted else media_html(selected)
    return f'''<figure class="asset-card" id="asset-{sid}" data-scene="{sid}">
<figcaption><span class="asset-id">{sid}</span><div><span class="mode">{MODES[selected['mode']] if selected else '表示方法を選択'}</span><h3>{esc(title)}</h3></div><span class="status">{label}</span></figcaption>
<p class="change-state" aria-live="polite"></p>
<div class="asset-body"><div class="visual">{visual}<p class="initial-note">現在の納品内容（別案の選択だけでは、この素材は差し替わりません）</p></div><div class="direction"><dl>
<dt>表示を始める発話</dt><dd class="quote">{esc(citation_text(scene['quote']))}</dd><dt>配置</dt><dd>{esc(scene['placement'])}</dd><dt>表示時間の目安</dt><dd>{esc(duration)}</dd><dt>終わり・切り替え</dt><dd>{esc(scene['end_cue'])}</dd></dl><div class="downloads">{downloads}</div></div></div>
<details class="{choices_class}"{choices_open}><summary>素材の候補を比較・選択する（{len(scene['options'])}案 ＋ 素材なし）</summary>{choices}<label class="none-option"><input type="radio" name="select-{sid}" value="__none__" {'checked' if omitted else ''}> 素材なし（この位置は話者映像のまま）</label><label class="none-option"><input type="radio" name="select-{sid}" value="__unselected__" {'checked' if scene['selected'] is None and not omitted else ''}> まだ決めない</label></details>
<label class="memo-label" for="memo-{sid}">この素材の修正メモ</label><textarea id="memo-{sid}" class="scene-memo" placeholder="例：文字を少なく／配色を本人の設定に合わせる"></textarea></figure>'''


def digest_html(case):
    items = []
    for index, item in enumerate(case.get("digest", []), 1):
        state = "確定" if item["status"] == "approved" else "提案・未確定"
        items.append(f'<li><strong class="digest-highlight">{esc(citation_text(item["display"]))}</strong> <span class="tag">{state}</span> <a href="script.html#digest-source-{index}">本文へ</a></li>')
    if not items:
        return ""
    return '<section class="digest-box" id="digest"><h2>冒頭ダイジェスト</h2><ul>' + "".join(items) + '</ul><p>箇条書きは表示用の文言です。本文の太赤字が実際の抜き出し範囲です。伏せ字は本編原稿を書き換えません。</p></section>'


def manuscript(case, source):
    positions = sorted((s["_start"] + len(s["quote"]), i, s) for i, s in enumerate(case["scenes"]))
    content, toc, cursor, count = [], [], 0, 0
    anchored = set()
    for kind, start, raw, level, is_body in script_blocks(source):
        fragment = source_fragment(raw, start, case, anchored, citations=is_body)
        if kind == "heading":
            count += 1
            tag = min(level + 1, 6)
            content.append(f'<h{tag} class="source-heading" id="heading-{count}">{fragment}</h{tag}>')
            plain = re.sub(r"[*_\x60]+", "", raw)
            toc.append(f'<a href="#heading-{count}">{esc(plain)}</a>')
        else:
            content.append(f'<p class="source-text">{fragment}</p>')
        while cursor < len(positions) and positions[cursor][0] <= start + len(raw):
            content.append(card(positions[cursor][2]))
            cursor += 1
    while cursor < len(positions):
        content.append(card(positions[cursor][2]))
        cursor += 1
    digest_link = '<a href="#digest">ダイジェスト</a>' if case.get("digest") else ""
    return '<div class="script-layout"><aside class="toc"><b>台本の流れ</b><a href="#start">編集ガイド</a>' + digest_link + "".join(toc) + '</aside><article class="manuscript">' + "".join(content) + '</article></div>'


def counts(case):
    selected = [next((o for o in s["options"] if o["id"] == s["selected"]), None) for s in case["scenes"]]
    # Keep the existing scene-count fields stable. File counts are separate:
    # one scene may contain several stills, and several scenes may reuse a file.
    still_files, video_files = set(), set()
    for option in selected:
        if option is None or option["status"] != "ready":
            continue
        poster = option.get("_poster", option.get("poster"))
        for filename in option.get("_files", option.get("files", [])):
            if filename == poster:
                continue
            suffix = Path(filename).suffix.lower()
            if suffix in IMAGES:
                still_files.add(filename)
            elif suffix in VIDEOS:
                video_files.add(filename)
    alternative_stills, alternative_videos = set(), set()
    for scene in case["scenes"]:
        for option in scene["options"]:
            if option["status"] != "ready" or option["id"] == scene["selected"]:
                continue
            poster = option.get("_poster", option.get("poster"))
            for filename in option.get("_files", option.get("files", [])):
                if filename == poster:
                    continue
                suffix = Path(filename).suffix.lower()
                if suffix in IMAGES:
                    alternative_stills.add(filename)
                elif suffix in VIDEOS:
                    alternative_videos.add(filename)
    return {
        "selected_ready_stills": sum(o is not None and o["status"] == "ready" and o["mode"] != "motion" for o in selected),
        "selected_ready_videos": sum(o is not None and o["status"] == "ready" and o["mode"] == "motion" for o in selected),
        "selected_ready_still_files": len(still_files),
        "selected_ready_video_files": len(video_files),
        "alternative_ready_still_files": len(alternative_stills - still_files),
        "alternative_ready_video_files": len(alternative_videos - video_files),
        "pending_scenes": sum(not s.get("omit") and (o is None or o["status"] != "ready") for s, o in zip(case["scenes"], selected)),
        "omitted_scenes": sum(bool(s.get("omit")) for s in case["scenes"]),
        "proposed_digest": sum(d["status"] == "proposed" for d in case.get("digest", [])),
        "recordings": int("recording" in case),
    }


def guide(case):
    recording = case.get("recording")
    if recording:
        audio = "音声未確認" if "has_audio" not in recording else "音声あり" if recording["has_audio"] else "音声なし"
        duration = f"{recording['duration_seconds']:g}秒" if "duration_seconds" in recording else "長さ未確認"
        dimensions = f"{recording['width']} × {recording['height']}" if "width" in recording and "height" in recording else "画面サイズ未確認"
        fps = f"{recording['fps']:g} fps" if "fps" in recording else "fps未確認"
        rec = f'''<div class="recording-grid"><video controls playsinline preload="metadata" src="{href(recording['_file'])}"></video><div><h3>撮影動画</h3><p>{esc(Path(recording['_file']).name)}</p><p>{duration} · {dimensions} · {fps} · {audio}</p><a class="download" href="{href(recording['_file'])}" download>撮影動画を開く／保存</a><p>再圧縮せず、入力と同じデータを同梱しています。</p></div></div>'''
    else:
        rec = '<p class="notice">撮影動画は未登録（未撮影・別送）。この一式には撮影動画を含みません。撮影後は原音声の該当発話に合わせて素材を配置してください。</p>'
    notes = '<ul>' + "".join(f'<li>{esc(n)}</li>' for n in case.get("notes", [])) + '</ul>' if case.get("notes") else ""
    return f'''<section class="guide" id="start"><span class="eyebrow">START HERE</span><h2>このページを上から読んで、編集を始める。</h2><ol class="workflow"><li><b>ZIP全体を展開</b><span>Macはダブルクリック、Windowsは「すべて展開」。展開した script.html をブラウザーで開きます。</span></li><li><b>台本と撮影音声を確認</b><span>素材カードの引用を音声から探します。表示秒数は目安で、撮影動画のタイムコードではありません。</span></li><li><b>指定の位置に素材を配置</b><span>実ファイルのある採用素材を使います。未制作の案は、本編用の完成素材には含めません。</span></li></ol><p class="folder-note"><b>フォルダごと保管してください。</b>script.html だけ移動すると画像や動画が開けなくなります。台本・素材の閲覧と選択書き出しはオフラインで使えます。外部の参考リンクを開くときだけインターネットが必要です。</p>{rec}{notes}</section>'''


def json_safe(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def client_data(case, source_hash, package_status):
    return {"schema_version": 1, "case_id": case["case_id"], "title": case["title"], "doctor_id": case["doctor_id"],
            "source": {"sha256": source_hash, "version": case["source"]["version"]}, "profile": {k: case["profile"][k] for k in ("id", "version", "design_version")}, "package_status": package_status,
            "scenes": [{"id": s["id"], "selected": s["selected"], "omit": s.get("omit", False),
                        "options": [{"id": o["id"], "title": o["title"], "status": o["status"], "mode": o["mode"]} for o in s["options"]]} for s in case["scenes"]]}


def package_status(case):
    c = counts(case)
    return "partial" if c["pending_scenes"] or c["proposed_digest"] or case.get("_quality_report", {}).get("status") != "passed" else "complete"


def quality_html(case):
    report = case.get("_quality_report", {})
    blockers = report.get("blockers", [])
    issues = '<ul>' + ''.join('<li>' + esc((item.get("scene_id", "") + " " + item["message"]).strip()) + '</li>' for item in blockers) + '</ul>' if blockers else '<p>素材構成・実ファイル・制作と目視確認の記録を確認済みです。</p>'
    labels = {"passed": "確認済み", "not_run": "未確認", "failed": "要修正", "not_applicable": "対象外"}
    hosts = []
    for key, label in (("hosted", "限定アクセスの確認ページ配信"), ("browser", "ブラウザーでの表示・再生・操作"), ("chat_preview", "ChatGPT会話内の表示")):
        item = report.get("host_checks", {}).get(key, {"status": "not_run", "evidence": "実操作は未確認"})
        if key == "chat_preview" and item.get("status") == "not_applicable":
            continue
        hosts.append('<li>' + label + '：' + labels.get(item.get("status"), "未確認") + ' — ' + esc(item.get("evidence", "")) + '</li>')
    return '<section class="guide quality-summary"><h2>納品前の確認</h2>' + issues + '<ul>' + ''.join(hosts) + '</ul><p>ファイルの検査と、実際の画面での確認は別に記録しています。</p></section>'


def shell(case, source_hash, body, gallery=False):
    c = counts(case)
    status = package_status(case)
    label = "要確認・制作待ちあり" if status == "partial" else "採用素材・台本の確認記録あり"
    ready = c["selected_ready_stills"] + c["selected_ready_videos"]
    alternatives = f'<p>比較用の別案ファイル：静止画 {c["alternative_ready_still_files"]}枚／動画 {c["alternative_ready_video_files"]}本（採用済みファイルを除く。同梱済み）</p>' if c["alternative_ready_still_files"] or c["alternative_ready_video_files"] else ""
    links = '<a href="台本_編集用.md" download>編集用Markdown</a><a href="配置CSV.csv" download>配置CSV</a><a href="source-script.md" download>元原稿</a>'
    if case.get("_prompter"):
        links += '<a href="台本_プロンプター用.md" download>プロンプター原稿</a>'
    subtitle = "候補の比較と修正を反映するには、選択結果をJSONまたは依頼文で書き出してください。" if gallery else "指定の発話・素材・切り替え指示を、本文の同じ位置で確認できます。"
    return f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'self' file:; style-src 'self' file:; img-src 'self' file: data:; media-src 'self' file: blob:; connect-src 'none'; font-src 'self'; base-uri 'none'; form-action 'none'"><title>{esc(case['title'])}｜編集用台本</title><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="theme.css"><script src="app.js" defer></script></head><body>
<header><small>Dr.SHI-GYO · EDITOR HANDOFF</small><h1>{esc(case['title'])}</h1><p>{subtitle}</p></header><div class="toolbar"><nav><a href="script.html" {'aria-current="page"' if not gallery else ''}>台本と素材</a><a href="index.html" {'aria-current="page"' if gallery else ''}>素材の選択肢</a></nav><div class="links">{links}</div></div><main>
<section class="summary"><div><strong id="package-status">{label}</strong><p>採用・完成済み {ready}場面（静止画 {c['selected_ready_stills']}場面／動画 {c['selected_ready_videos']}場面） · 素材なし確定 {c['omitted_scenes']}か所 · 制作／選択待ち {c['pending_scenes']}か所</p><p>採用素材の実ファイル：静止画 {c['selected_ready_still_files']}枚／動画 {c['selected_ready_video_files']}本（同じファイルの再利用は1点。動画ポスターを除く）</p><p>別案・未制作の案・参考画像は、採用素材の数に含めません。</p>{alternatives}<p id="selection-status" aria-live="polite">選択変更はありません。</p></div></section>
{quality_html(case)}
{guide(case) if not gallery else '<p class="notice">現在の納品内容と別案を比較できます。別案を選んでも実ファイルと台本は自動更新されません。変更待ちとして書き出し、再生成後のZIPを編集者に渡してください。</p>'}
<section class="export-panel" id="export"><div><h2>選択と修正を次の制作へ渡す</h2><p>選択結果はこのブラウザー内で可能な範囲で保存します。確実に残すには書き出してください。JSONの読み込みで続きから再開できます。</p><p class="storage-state" aria-live="polite"></p></div><div class="export-actions"><button type="button" id="export-json">選択結果JSONを保存</button><button type="button" id="export-request">修正依頼文を保存</button><label class="upload-label">選択結果JSONを読み込む<input type="file" id="import-json" accept=".json,application/json"></label><button type="button" id="reset-choices">このページの選択を初期化</button></div></section>
{digest_html(case) if not gallery else ''}<div class="script-search"><label for="search-query">ページ内を探す</label><input type="search" id="search-query" placeholder="発話・素材名を入力"><button type="button" id="search-next">次の一致</button><output id="search-count" aria-live="polite"></output></div>{body}
<section class="guide closing"><h2>書き出す前の確認</h2><ul><li>原稿と実際の発話を照合し、語尾や必要な説明を切らない。</li><li>素材の縦横比を保ち、顔・手・字幕と重ねない。図表の数値・単位・出典を変えない。</li><li>全画面素材の間も、指定された本編音声を継続する。</li><li>指示文字・素材ID・未制作の案を完成映像に残さない。</li><li>採用内容を変更した場合は、更新された納品一式で編集する。</li></ul></section></main>
<footer>原稿 v{esc(case['source']['version'])} · 本人設定 v{esc(case['profile']['version'])} · デザイン v{esc(case['profile']['design_version'])}<br>この一式は編集用素材と台本です。編集・書き出し済みの本編動画ではありません。</footer><script id="handoff-data" type="application/json">{json_safe(client_data(case, source_hash, status))}</script></body></html>'''


def clean(value):
    if isinstance(value, dict):
        return {k: clean(v) for k, v in value.items() if not k.startswith("_")}
    if isinstance(value, list):
        return [clean(v) for v in value]
    return value


def markdown_card(scene):
    option = next((o for o in scene["options"] if o["id"] == scene["selected"]), None)
    title = option["title"] if option else "素材なしで確定" if scene.get("omit") else "未選択"
    lines = [f"> **素材 {scene['id']}**：{title}", f"> 表示開始：{citation_text(scene['quote'])}",
             f"> 配置：{scene['placement']}", f"> 目安：{scene['duration']}", f"> 切り替え：{scene['end_cue']}"]
    if option:
        lines += [f"> 状態：{STATUS[option['status']]} · {MODES[option['mode']]}"]
        lines += [f"> ファイル：[{Path(f).name}]({urllib.parse.quote(f, safe='/')})" for f in option["_files"]]
    return lines + [""]


def editor_markdown(case, source):
    lines = [f"# {case['title']}｜編集用台本", "", "素材の表示目安は撮影タイムコードではありません。実際の発話に合わせて配置してください。", ""]
    if case.get("digest"):
        lines += ["## 冒頭ダイジェスト", ""]
    for item in case.get("digest", []):
        label = "確定" if item["status"] == "approved" else "提案・未確定"
        lines.append(f"- **{citation_text(item['display'])}**（{label}）")
    if case.get("digest"):
        lines += ["", "本文の抜き出し範囲は script.html で太赤字に表示しています。"]
    lines += ["", "---", ""]
    positions = sorted((s["_start"] + len(s["quote"]), i, s) for i, s in enumerate(case["scenes"]))
    cursor = 0
    for kind, start, raw, level, is_body in script_blocks(source):
        rendered = citation_text(raw) if is_body else raw
        lines += ["#" * level + " " + rendered if kind == "heading" else rendered, ""]
        while cursor < len(positions) and positions[cursor][0] <= start + len(raw):
            lines += markdown_card(positions[cursor][2])
            cursor += 1
    while cursor < len(positions):
        lines += markdown_card(positions[cursor][2])
        cursor += 1
    return "\n".join(lines)


def csv_cell(value):
    value = str(value)
    return "'" + value if value.lstrip().startswith(("=", "+", "-", "@", "\t", "\r")) else value


def package(case, source, source_path, source_hash, assets, output):
    output.mkdir()
    for item in assets.values():
        destination = output / item["path"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.exists():
            shutil.copyfile(item["source"], destination)
        require(sha256(destination) == item["sha256"], f"コピーの照合に失敗しました: {item['path']}")
    shutil.copyfile(source_path, output / "source-script.md")
    if case.get("_prompter"):
        (output / "台本_プロンプター用.md").write_text(case["_prompter_text"], encoding="utf-8")
    for name in ("style.css", "app.js"):
        require((ASSET_ROOT / name).is_file(), f"rendererのファイルがありません: {name}")
        shutil.copyfile(ASSET_ROOT / name, output / name)
    (output / "theme.css").write_text(":root{" + ";".join(f"--{key}:{value}" for key, value in case["design"].items() if key in {"background", "ink", "accent"}) + "}\n", encoding="utf-8")
    (output / "script.html").write_text(shell(case, source_hash, manuscript(case, source)), encoding="utf-8")
    (output / "index.html").write_text(shell(case, source_hash, '<div class="gallery">' + "".join(card(s) for s in sorted(case["scenes"], key=lambda s: s["_start"])) + '</div>', True), encoding="utf-8")
    inline_requested = case.get("preview", {}).get("inline_requested", False)
    preview_report = build_previews(output, source_hash, inline_requested=inline_requested)
    preview_errors = [x for x in preview_report.get("blockers", []) if "coverage_mismatch" in x]
    if preview_errors:
        q = case["_quality_report"]
        q["status"] = "needs_review"
        q["blockers"].extend({"code": "preview." + err, "message": "台本全文プレビューの内容または容量を確認してください: " + err} for err in preview_errors)
        (output / "script.html").write_text(shell(case, source_hash, manuscript(case, source)), encoding="utf-8")
        (output / "index.html").write_text(shell(case, source_hash, '<div class="gallery">' + "".join(card(s) for s in sorted(case["scenes"], key=lambda s: s["_start"])) + '</div>', True), encoding="utf-8")
        if (output / "preview-parts").is_dir():
            shutil.rmtree(output / "preview-parts")
        preview_report = build_previews(output, source_hash, inline_requested=inline_requested)
    (output / "quality-report.json").write_text(json.dumps(case["_quality_report"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (output / "台本_編集用.md").write_text(editor_markdown(case, source), encoding="utf-8")
    with (output / "配置CSV.csv").open("w", newline="", encoding="utf-8-sig") as stream:
        writer = csv.writer(stream)
        writer.writerow(["素材ID", "選択ID", "状態", "素材名", "表示方法", "表示開始の発話", "表示時間の目安", "配置", "終わり・切り替え", "ファイル"])
        for scene in sorted(case["scenes"], key=lambda s: s["_start"]):
            option = next((o for o in scene["options"] if o["id"] == scene["selected"]), None)
            row = [scene["id"], scene["selected"] or "", STATUS[option["status"]] if option else "素材なし確定" if scene.get("omit") else "未選択", option["title"] if option else "", MODES[option["mode"]] if option else "", citation_text(scene["quote"]), scene["duration"], scene["placement"], scene["end_cue"], " | ".join(option["_files"]) if option else ""]
            writer.writerow([csv_cell(x) for x in row])
    c = counts(case)
    status = package_status(case)
    readme = f"""{case['title']}｜編集者向け納品一式

1. ZIP全体を展開してください。Windowsは「すべて展開」、Macはダブルクリック。
2. 展開したフォルダの script.html をSafari / Chrome / Edgeで開いてください。
3. 本文中の指定発話に合わせて、実ファイルがある採用素材を配置してください。

script.html だけを移動せず、同じフォルダのファイル・フォルダを一緒に保管してください。
ローカルサーバー、追加アプリ、ネット接続は閲覧に不要です。外部リンクにはネット接続が必要です。
動画がブラウザーで再生できない場合は、同梱の動画を編集ソフトで開いてください。

現在の状態: {status}
品質確認: {case["_quality_report"]["status"]}（詳細はquality-report.jsonとHTMLの納品前の確認）
確認ページの配信・限定アクセスと、ブラウザーでの表示・再生・操作は品質記録内のhost_checksに別々に記録します。未実施を確認済みとしません。
最終確認はChatGPTから案内する限定アクセスの確認リンクを使います。会話内の分割表示は明示的に希望された場合だけ用意します。
採用・完成済みの場面数: 静止画 {c['selected_ready_stills']}場面 / 動画 {c['selected_ready_videos']}場面
採用素材の実ファイル数: 静止画 {c['selected_ready_still_files']}枚 / 動画 {c['selected_ready_video_files']}本
比較用の別案ファイル数: 静止画 {c['alternative_ready_still_files']}枚 / 動画 {c['alternative_ready_video_files']}本（採用済みファイルを除く。同梱済み）
同じファイルの再利用は1点として数え、動画ポスターは実ファイル数から除きます。
制作または選択待ち: {c['pending_scenes']} / 素材なし確定: {c['omitted_scenes']}
ダイジェスト未確定: {c['proposed_digest']}
撮影動画: {'同梱（無再圧縮）' if case.get('recording') else '未登録（未撮影・別送）。同梱なし'}

script.html: 台本と採用素材、編集指示、ダイジェスト
index.html: 素材の候補と修正メモ
preview.html: 台本全文と素材の自己完結確認ページ（容量内で生成。Sitesへの配信元にも使用）
preview-parts/: 明示的に希望された場合だけ生成する会話内表示用。番号順の全パートで台本全文を表示
preview-report.json: 本文・素材の網羅性、容量、未実施の表示確認を記録
台本_編集用.md / 配置CSV.csv: 編集指示の別形式
source-script.md: 入力原稿の原本（バイト単位で保存）
manifest.json: 原稿・本人設定・デザインの版、素材ファイルとSHA-256

選択肢を変更すると「変更待ち」になります。変更だけでは素材やZIPは更新されません。
「選択結果JSON」または「修正依頼文」を保存してChatGPTへ渡すか、同じチャットで修正箇所を伝えてください。
ChatGPTが確認ページと納品一式を更新します。同じ案件の確認ページは同じURLを使います。
ブラウザー保存が使えない場合でも、JSON書き出し・読み込みで作業を継続できます。
未制作の案・参考画像・未選択候補は採用済み完成素材の数に含めません。
この一式は編集用の素材と台本であり、編集・書き出し済みの本編動画ではありません。
"""
    (output / "README.txt").write_text(readme, encoding="utf-8")
    file_records = [{"path": p.relative_to(output).as_posix(), "bytes": p.stat().st_size, "sha256": sha256(p)} for p in sorted(output.rglob("*")) if p.is_file()]
    scene_records = []
    for scene in case["scenes"]:
        record = clean(scene)
        for option, original in zip(record["options"], scene["options"]):
            option["files"] = original["_files"]
            if original.get("_poster"):
                option["poster"] = original["_poster"]
        scene_records.append(record)
    manifest = {"schema_version": 1, "generator": GENERATOR, "case_id": case["case_id"], "title": case["title"], "doctor_id": case["doctor_id"],
                "status": status, "counts": c, "source": {"path": "source-script.md", "sha256": source_hash, "version": case["source"]["version"]},
                "profile": {k: case["profile"][k] for k in ("id", "version", "design_version")}, "design": {k: case["design"][k] for k in ("background", "ink", "accent")}, "scenes": scene_records, "digest": clean(case.get("digest", [])), "files": file_records}
    manifest["preview"] = preview_report
    manifest["quality"] = case["_quality_report"]
    if case.get("recording"):
        manifest["recording"] = {k: case["recording"][k] for k in ("duration_seconds", "width", "height", "fps", "has_audio") if k in case["recording"]}
        manifest["recording"]["file"] = case["recording"]["_file"]
    if case.get("_prompter"):
        manifest["prompter_path"] = "台本_プロンプター用.md"
    (output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def output_guard(output, zip_path, inputs, case, replace):
    no_symlinks(output)
    require(not any(p == output or p.is_relative_to(output) for p in inputs), "出力先が入力ファイルを含んでいます。別フォルダを指定してください")
    require(not output.is_file(), "出力先はフォルダにしてください")
    if output.exists() and any(output.iterdir()):
        require(replace, "出力先が空ではありません。別名にするか --replace を指定してください")
        manifest = output / "manifest.json"
        require(manifest.is_file(), "既存出力にmanifest.jsonがありません。上書きできません")
        no_symlinks(manifest)
        old = read_json(manifest)
        require(old.get("generator") == GENERATOR and old.get("case_id") == case["case_id"], "別の成果物や案件のフォルダは上書きできません")
        allowed = {x["path"] for x in old.get("files", [])} | {"manifest.json"}
        for item in output.rglob("*"):
            no_symlinks(item)
            require(not item.is_file() or item.relative_to(output).as_posix() in allowed, "既存出力に追加ファイルがあります。別名の出力先を指定してください")
    if zip_path:
        no_symlinks(zip_path)
        require(zip_path.suffix.lower() == ".zip", "ZIP出力の拡張子は.zipにしてください")
        require(zip_path not in inputs and not zip_path.is_relative_to(output), "ZIP出力を入力ファイルまたは出力フォルダ内に置けません")
        if zip_path.exists():
            require(replace, "ZIPが既にあります。別名にするか --replace を指定してください")
            require(zip_path.is_file() and zipfile.is_zipfile(zip_path), "既存ファイルはこのrendererのZIPではありません")
            with zipfile.ZipFile(zip_path) as z:
                try:
                    old = json.loads(z.read("manifest.json"))
                except (KeyError, json.JSONDecodeError, UnicodeError) as error:
                    raise ValidationError("既存ZIPのmanifestを確認できません") from error
                require(old.get("generator") == GENERATOR and old.get("case_id") == case["case_id"], "別の案件のZIPは上書きできません")


def run(args):
    case_path = Path(args.case).absolute()
    case, source, source_path, source_hash, assets, inputs = validate(case_path)
    output = Path(args.output).absolute()
    zip_path = Path(args.zip).absolute() if args.zip else None
    no_symlinks(output)
    output = output.resolve()
    if zip_path:
        no_symlinks(zip_path)
        zip_path = zip_path.resolve()
    output_guard(output, zip_path, inputs, case, args.replace)
    output.parent.mkdir(parents=True, exist_ok=True)
    if zip_path:
        zip_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".handoff-build-", dir=output.parent) as stage:
        built = Path(stage) / "delivery"
        manifest = package(case, source, source_path, source_hash, assets, built)
        zip_tmp = None
        if zip_path:
            descriptor, temporary = tempfile.mkstemp(prefix=".handoff-", suffix=".zip", dir=zip_path.parent)
            os.close(descriptor)
            zip_tmp = Path(temporary)
        try:
            if zip_tmp:
                with zipfile.ZipFile(zip_tmp, "w", allowZip64=True) as archive:
                    for path in sorted(built.rglob("*")):
                        if path.is_file():
                            compressed = path.suffix.lower() in VIDEOS | IMAGES | {".pdf"}
                            archive.write(path, path.relative_to(built).as_posix(), compress_type=zipfile.ZIP_STORED if compressed else zipfile.ZIP_DEFLATED)
                with zipfile.ZipFile(zip_tmp) as archive:
                    require(archive.testzip() is None, "ZIP整合性チェックに失敗しました")
            output_guard(output, zip_path, inputs, case, args.replace)
            if output.exists():
                shutil.rmtree(output)
            os.replace(built, output)
            if zip_tmp:
                os.replace(zip_tmp, zip_path)
        finally:
            if zip_tmp and zip_tmp.exists():
                zip_tmp.unlink()
    print(json.dumps({"output": str(output), "zip": str(zip_path) if zip_path else None,
                      "status": manifest["status"], "counts": manifest["counts"],
                      "source_sha256": source_hash, "quality": manifest["quality"]["status"],
                      "quality_blockers": len(manifest["quality"]["blockers"])}, ensure_ascii=False))
    return 3 if getattr(args, "require_complete", False) and manifest["status"] != "complete" else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", help="case.json のパス")
    parser.add_argument("--output", required=True, help="納品フォルダ")
    parser.add_argument("--zip", help="同じ内容を保存するZIP（任意）")
    parser.add_argument("--replace", action="store_true", help="同じcase_idの既存生成物のみ再生成する")
    parser.add_argument("--require-complete", action="store_true", help="下書きも保存するが、品質確認が未完了なら終了コード3を返す")
    args = parser.parse_args()
    try:
        return run(args)
    except (ValidationError, OSError, zipfile.BadZipFile) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

