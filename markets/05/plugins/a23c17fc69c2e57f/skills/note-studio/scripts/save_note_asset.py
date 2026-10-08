#!/usr/bin/env python3
"""Copy a finished note image into a user-visible Desktop folder."""

from __future__ import annotations

import argparse
import ctypes
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import uuid
from datetime import date
from pathlib import Path


INVALID_NAME_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
WHITESPACE = re.compile(r"\s+")


class GUID(ctypes.Structure):
    _fields_ = [
        ("Data1", ctypes.c_uint32),
        ("Data2", ctypes.c_uint16),
        ("Data3", ctypes.c_uint16),
        ("Data4", ctypes.c_ubyte * 8),
    ]


def windows_desktop() -> Path:
    folder_id = uuid.UUID("b4bfcc3a-db2c-424c-b029-7fe99a87c641")
    guid = GUID(
        folder_id.fields[0],
        folder_id.fields[1],
        folder_id.fields[2],
        (ctypes.c_ubyte * 8)(*folder_id.bytes[8:]),
    )
    path_pointer = ctypes.c_void_p()
    shell32 = ctypes.windll.shell32  # type: ignore[attr-defined]
    ole32 = ctypes.windll.ole32  # type: ignore[attr-defined]
    shell32.SHGetKnownFolderPath.argtypes = [
        ctypes.POINTER(GUID),
        ctypes.c_uint32,
        ctypes.c_void_p,
        ctypes.POINTER(ctypes.c_void_p),
    ]
    shell32.SHGetKnownFolderPath.restype = ctypes.c_long
    ole32.CoTaskMemFree.argtypes = [ctypes.c_void_p]
    ole32.CoTaskMemFree.restype = None
    result = shell32.SHGetKnownFolderPath(
        ctypes.byref(guid), 0, None, ctypes.byref(path_pointer)
    )
    if result != 0 or not path_pointer.value:
        raise RuntimeError("Windowsのデスクトップ保存先を確認できません。")
    try:
        return Path(ctypes.wstring_at(path_pointer.value))
    finally:
        ole32.CoTaskMemFree(path_pointer)


def desktop_directory() -> Path:
    if os.name == "nt":
        return windows_desktop()
    if sys.platform.startswith("linux") and shutil.which("xdg-user-dir"):
        result = subprocess.run(
            ["xdg-user-dir", "DESKTOP"],
            check=False,
            capture_output=True,
            text=True,
        )
        candidate = result.stdout.strip()
        if result.returncode == 0 and candidate:
            return Path(candidate).expanduser()
    return Path.home() / "Desktop"


def safe_title(value: str) -> str:
    cleaned = INVALID_NAME_CHARS.sub(" ", value)
    cleaned = WHITESPACE.sub(" ", cleaned).strip(" .")
    if not cleaned:
        return "note記事"
    return cleaned[:48].rstrip(" .") or "note記事"


def file_digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def available_destination(
    directory: Path, stem: str, suffix: str, source: Path
) -> tuple[Path, bool]:
    candidate = directory / f"{stem}{suffix}"
    if not candidate.exists():
        return candidate, False
    if candidate.is_file() and file_digest(candidate) == file_digest(source):
        return candidate, True
    number = 2
    while True:
        candidate = directory / f"{stem}-{number:02d}{suffix}"
        if not candidate.exists():
            return candidate, False
        if candidate.is_file() and file_digest(candidate) == file_digest(source):
            return candidate, True
        number += 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="完成したnote用画像をデスクトップの専用フォルダへ保存します。"
    )
    parser.add_argument("source", type=Path)
    parser.add_argument("--article-title", required=True)
    parser.add_argument(
        "--kind", required=True, choices=("thumbnail", "inline")
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        help="デスクトップ以外へ保存する場合の親フォルダ。",
    )
    parser.add_argument(
        "--date",
        dest="article_date",
        help="保存フォルダの日付。未指定時は実行日。YYYY-MM-DD形式。",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.source.expanduser().resolve()
    if not source.is_file():
        raise SystemExit(f"入力画像が見つかりません: {source}")

    if args.article_date:
        try:
            folder_date = date.fromisoformat(args.article_date).isoformat()
        except ValueError as error:
            raise SystemExit("日付はYYYY-MM-DD形式で指定してください。") from error
    else:
        folder_date = date.today().isoformat()

    output_root = (
        args.output_root.expanduser().resolve()
        if args.output_root
        else desktop_directory()
    )
    if output_root.exists() and not output_root.is_dir():
        raise SystemExit(f"保存先がフォルダではありません: {output_root}")

    article_directory = (
        output_root / "Note Studio" / f"{folder_date}_{safe_title(args.article_title)}"
    )
    article_directory.mkdir(parents=True, exist_ok=True)

    suffix = source.suffix.lower() or ".png"
    stem = "見出し画像" if args.kind == "thumbnail" else "差し絵"
    destination, reused = available_destination(
        article_directory, stem, suffix, source
    )
    if not reused:
        shutil.copy2(source, destination)

    print(
        json.dumps(
            {
                "article_directory": str(article_directory),
                "destination": str(destination),
                "kind": args.kind,
                "reused": reused,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError) as error:
        print(f"画像を保存できません: {error}", file=sys.stderr)
        raise SystemExit(1) from error
