#!/usr/bin/env python3
"""Validate a script-linked asset plan and render an offline selection page.

Usage: python3 render_choices.py plan.json --script source.md --output choices.html
Only Python's standard library is required. Nothing is uploaded or downloaded.
Preview files must be inside the plan directory, at most 20 MiB each / 60 MiB total.
"""

import argparse
import base64
import hashlib
import json
from pathlib import Path
import re
import sys


MAX_PREVIEW_BYTES = 20 * 1024 * 1024
MAX_TOTAL_PREVIEW_BYTES = 60 * 1024 * 1024
PREVIEW_TYPES = {
    ".png": ("image", "image/png"),
    ".jpg": ("image", "image/jpeg"),
    ".jpeg": ("image", "image/jpeg"),
    ".gif": ("image", "image/gif"),
    ".webp": ("image", "image/webp"),
    ".mp4": ("video", "video/mp4"),
    ".webm": ("video", "video/webm"),
}


class PlanError(ValueError):
    pass


def require_object(value, location):
    if not isinstance(value, dict):
        raise PlanError(f"{location}: オブジェクトが必要です")
    return value


def require_text(value, location):
    if not isinstance(value, str) or not value.strip():
        raise PlanError(f"{location}: 空ではない文字列が必要です")
    return value


def require_list(value, location, nonempty=True):
    if not isinstance(value, list) or (nonempty and not value):
        raise PlanError(f"{location}: {'空ではない' if nonempty else ''}配列が必要です")
    return value


def count_occurrences(text, quote):
    """Count overlaps too: 'aaa' occurs twice in 'aaaa'."""
    count, start = 0, 0
    while True:
        position = text.find(quote, start)
        if position == -1:
            return count
        count += 1
        start = position + 1


def has_media_signature(content, suffix):
    if suffix == ".png":
        return content.startswith(b"\x89PNG\r\n\x1a\n")
    if suffix in (".jpg", ".jpeg"):
        return content.startswith(b"\xff\xd8\xff")
    if suffix == ".gif":
        return content.startswith((b"GIF87a", b"GIF89a"))
    if suffix == ".webp":
        return content[:4] == b"RIFF" and content[8:12] == b"WEBP"
    if suffix == ".mp4":
        return content[4:8] == b"ftyp"
    if suffix == ".webm":
        return content.startswith(b"\x1a\x45\xdf\xa3")
    return False


def embed_preview(preview, plan_dir, location, budget):
    require_object(preview, location)
    kind = preview.get("kind")
    if kind not in ("image", "video"):
        raise PlanError(f"{location}.kind: image または video が必要です")
    relative = Path(require_text(preview.get("path"), f"{location}.path"))
    path = (plan_dir / relative).resolve()
    if relative.is_absolute() or not path.is_relative_to(plan_dir):
        raise PlanError(f"{location}.path: 素材計画と同じフォルダ以下の相対パスを指定してください")
    if not path.is_file():
        raise PlanError(f"{location}.path: 実ファイルがありません: {relative}")
    media_type = PREVIEW_TYPES.get(path.suffix.lower())
    if not media_type or media_type[0] != kind:
        raise PlanError(f"{location}: 対応する画像 PNG/JPEG/GIF/WebP または動画 MP4/WebM が必要です")
    size = path.stat().st_size
    if size == 0 or size > MAX_PREVIEW_BYTES:
        raise PlanError(f"{location}: プレビューは空ではない 20 MiB 以下のファイルにしてください")
    if budget[0] + size > MAX_TOTAL_PREVIEW_BYTES:
        raise PlanError("プレビューの合計が 60 MiB を超えます。軽量のプレビューにしてください")
    content = path.read_bytes()
    if not has_media_signature(content, path.suffix.lower()):
        raise PlanError(f"{location}: 拡張子とファイル内容が一致しません")
    budget[0] += len(content)
    encoded = base64.b64encode(content).decode("ascii")
    return {"kind": kind, "data_url": f"data:{media_type[1]};base64,{encoded}"}


def validate_plan(plan, source_bytes, plan_dir):
    require_object(plan, "plan")
    plan_id = require_text(plan.get("plan_id"), "plan_id")
    source = require_object(plan.get("source"), "source")
    source = {key: require_text(source.get(key), f"source.{key}")
              for key in ("title", "version", "sha256")}
    if not re.fullmatch(r"[0-9a-fA-F]{64}", source["sha256"]):
        raise PlanError("source.sha256: 64 桁の SHA-256 が必要です")
    actual_hash = hashlib.sha256(source_bytes).hexdigest()
    if actual_hash != source["sha256"].lower():
        raise PlanError("source.sha256: 台本の内容と一致しません。現在の台本から素材計画を確認し直してください")
    source["sha256"] = actual_hash
    try:
        script = source_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise PlanError("台本を UTF-8 のテキストファイルにしてください") from exc

    scenes = []
    scene_ids = set()
    budget = [0]
    for index, raw_scene in enumerate(require_list(plan.get("scenes"), "scenes")):
        location = f"scenes[{index}]"
        require_object(raw_scene, location)
        scene = {key: require_text(raw_scene.get(key), f"{location}.{key}")
                 for key in ("id", "label", "quote", "message", "recommended")}
        if scene["id"] in scene_ids:
            raise PlanError(f"{location}.id: 場面 ID が重複しています: {scene['id']}")
        scene_ids.add(scene["id"])
        quote_count = count_occurrences(script, scene["quote"])
        if quote_count != 1:
            raise PlanError(f"{location}.quote: 台本内に {quote_count} 回あります。場所を一意に特定できる実際の台本文を指定してください")
        options = []
        option_ids = set()
        for option_index, raw_option in enumerate(require_list(raw_scene.get("options"), f"{location}.options")):
            option_location = f"{location}.options[{option_index}]"
            require_object(raw_option, option_location)
            option = {key: require_text(raw_option.get(key), f"{option_location}.{key}")
                      for key in ("id", "type", "title", "concept", "reason", "format", "delivery_status")}
            if option["id"] in option_ids:
                raise PlanError(f"{option_location}.id: この場面の候補 ID が重複しています: {option['id']}")
            option_ids.add(option["id"])
            if option["delivery_status"] != "proposal":
                raise PlanError(f"{option_location}.delivery_status: この選択画面では proposal だけを扱います")
            option["requirements"] = [require_text(item, f"{option_location}.requirements[{req_index}]")
                                      for req_index, item in enumerate(require_list(raw_option.get("requirements"), f"{option_location}.requirements", nonempty=False))]
            if "preview" in raw_option:
                option["preview"] = embed_preview(raw_option["preview"], plan_dir.resolve(), f"{option_location}.preview", budget)
            options.append(option)
        if scene["recommended"] not in option_ids:
            raise PlanError(f"{location}.recommended: 推奨候補の ID が options にありません")
        scene["options"] = options
        scenes.append(scene)
    return {"plan_id": plan_id, "source": source, "scenes": scenes}


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise PlanError(f"JSON のキーが重複しています: {key}")
        result[key] = value
    return result


def render(plan_path, script_path, output_path):
    plan = json.loads(plan_path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicate_keys)
    normalized = validate_plan(plan, script_path.read_bytes(), plan_path.parent)
    template_path = Path(__file__).resolve().parent.parent / "assets" / "choices-template.html"
    template = template_path.read_text(encoding="utf-8")
    marker = "__ASSET_PLAN_JSON__"
    if template.count(marker) != 1:
        raise PlanError("HTML テンプレートの埋め込み位置が不正です")
    embedded = json.dumps(normalized, ensure_ascii=False, separators=(",", ":"))
    for character, replacement in (("&", "\\u0026"), ("<", "\\u003c"), (">", "\\u003e"), ("\u2028", "\\u2028"), ("\u2029", "\\u2029")):
        embedded = embedded.replace(character, replacement)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(template.replace(marker, embedded), encoding="utf-8")
    return len(normalized["scenes"])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path, help="ChatGPT が作成した素材計画 JSON")
    parser.add_argument("--script", required=True, type=Path, help="この計画の元となった UTF-8 台本")
    parser.add_argument("--output", required=True, type=Path, help="保存する自己完結 HTML")
    args = parser.parse_args(argv)
    try:
        protected_paths = {args.plan.resolve(), args.script.resolve(), Path(__file__).resolve(),
                           (Path(__file__).resolve().parent.parent / "assets" / "choices-template.html")}
        if args.output.resolve() in protected_paths:
            raise PlanError("出力先には入力ファイル・実行ファイル・テンプレート以外を指定してください")
        count = render(args.plan, args.script, args.output)
    except (PlanError, OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"素材計画を出力できません: {exc}", file=sys.stderr)
        return 1
    print(f"{count} 場面の選択画面を作成しました: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
