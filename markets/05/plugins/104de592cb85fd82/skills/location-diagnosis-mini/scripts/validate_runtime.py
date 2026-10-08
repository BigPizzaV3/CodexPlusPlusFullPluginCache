#!/usr/bin/env python3
"""Validate a mounted or materialized fixed-renderer runtime without dependencies."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path, PurePosixPath
from typing import Any


SKILL_DIR = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = SKILL_DIR / "references" / "runtime-manifest.json"


class RuntimeValidationError(Exception):
    pass


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(65_536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_relative_path(value: str) -> PurePosixPath:
    relative = PurePosixPath(value)
    if relative.is_absolute() or not relative.parts or ".." in relative.parts:
        raise RuntimeValidationError(f"unsafe runtime path: {value}")
    return relative


def validate_runtime(root: Path, manifest_path: Path) -> tuple[str, int]:
    try:
        manifest: dict[str, Any] = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeValidationError(f"runtime manifestを読めません: {exc}") from exc
    if manifest.get("schema_version") != 1:
        raise RuntimeValidationError("runtime manifest schema_versionは1が必要です")
    bundle_version = manifest.get("bundle_version")
    files = manifest.get("files")
    if not isinstance(bundle_version, str) or not isinstance(files, dict) or not files:
        raise RuntimeValidationError("runtime manifestのversionまたはfilesが不正です")

    resolved_root = root.resolve()
    for relative_text, expected in files.items():
        if not isinstance(relative_text, str) or not isinstance(expected, dict):
            raise RuntimeValidationError("runtime manifestのfile entryが不正です")
        relative = safe_relative_path(relative_text)
        target = resolved_root.joinpath(*relative.parts)
        try:
            resolved_target = target.resolve(strict=True)
        except OSError as exc:
            raise RuntimeValidationError(f"runtime fileがありません: {relative_text}") from exc
        if resolved_root not in resolved_target.parents or not resolved_target.is_file():
            raise RuntimeValidationError(f"runtime fileがroot外または通常fileではありません: {relative_text}")
        expected_bytes = expected.get("bytes")
        expected_sha256 = expected.get("sha256")
        if not isinstance(expected_bytes, int) or not isinstance(expected_sha256, str):
            raise RuntimeValidationError(f"runtime manifest entryが不正です: {relative_text}")
        actual_bytes = resolved_target.stat().st_size
        actual_sha256 = sha256_file(resolved_target)
        if actual_bytes != expected_bytes or actual_sha256 != expected_sha256:
            raise RuntimeValidationError(
                f"runtime fileが公式resourceと一致しません: {relative_text} "
                f"bytes={actual_bytes}/{expected_bytes} sha256={actual_sha256}/{expected_sha256}"
            )
    return bundle_version, len(files)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=SKILL_DIR, help="Mounted or materialized skill root")
    parser.add_argument("--manifest", type=Path, help="Runtime manifest path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest_path = args.manifest or args.root / "references" / "runtime-manifest.json"
    try:
        bundle_version, file_count = validate_runtime(args.root, manifest_path)
    except RuntimeValidationError as exc:
        print(f"RUNTIME INVALID: {exc}", file=sys.stderr)
        return 1
    print(f"RUNTIME VALID: {bundle_version} / {file_count} canonical files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
