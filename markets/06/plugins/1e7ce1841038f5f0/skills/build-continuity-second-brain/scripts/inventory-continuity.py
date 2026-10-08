#!/usr/bin/env python3
"""Create a read-only, portable inventory of a continuity workspace.

The script never follows symlinks and never reads file contents unless --hash is
explicitly requested. It writes only to an explicit --json or --markdown path;
otherwise JSON is printed to stdout.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_EXCLUDES = {".git", "node_modules", ".venv", "__pycache__", ".DS_Store"}


def sha256_file(path: Path, max_bytes: int) -> tuple[str | None, str | None]:
    size = path.stat().st_size
    if size > max_bytes:
        return None, f"not hashed: {size} bytes exceeds limit {max_bytes}"
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest(), None


def inventory(
    root: Path,
    include_hashes: bool,
    max_hash_bytes: int,
    excludes: set[str],
    include_absolute_root: bool,
) -> dict:
    root = root.resolve(strict=True)
    if not root.is_dir():
        raise ValueError(f"Root is not a directory: {root}")

    files: list[dict] = []
    directories: list[str] = ["."]
    symlinks: list[dict] = []
    skipped: list[dict] = []
    errors: list[dict] = []

    for current, dirnames, filenames in os.walk(root, topdown=True, followlinks=False):
        current_path = Path(current)
        retained_dirs: list[str] = []
        for dirname in sorted(dirnames):
            path = current_path / dirname
            relative = path.relative_to(root).as_posix()
            try:
                if path.is_symlink():
                    symlinks.append({"path": relative, "target": os.readlink(path), "kind": "directory"})
                elif dirname in excludes:
                    skipped.append({"path": relative, "reason": "default exclusion"})
                else:
                    retained_dirs.append(dirname)
                    directories.append(relative)
            except OSError as exc:
                errors.append({"path": relative, "error": str(exc)})
        dirnames[:] = retained_dirs

        for filename in sorted(filenames):
            path = current_path / filename
            relative = path.relative_to(root).as_posix()
            if filename in excludes:
                skipped.append({"path": relative, "reason": "default exclusion"})
                continue
            try:
                if path.is_symlink():
                    symlinks.append({"path": relative, "target": os.readlink(path), "kind": "file"})
                    continue
                info = path.stat()
                if not stat.S_ISREG(info.st_mode):
                    skipped.append({"path": relative, "reason": "not a regular file"})
                    continue
                record = {
                    "path": relative,
                    "size_bytes": info.st_size,
                    "modified_utc": datetime.fromtimestamp(info.st_mtime, timezone.utc).isoformat(),
                    "extension": path.suffix.lower(),
                }
                if include_hashes:
                    digest, note = sha256_file(path, max_hash_bytes)
                    record["sha256"] = digest
                    if note:
                        record["hash_note"] = note
                files.append(record)
            except (OSError, ValueError) as exc:
                errors.append({"path": relative, "error": str(exc)})

    return {
        "schema": "continuity-inventory-v1",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "root_name": root.name,
        "root_path_local": str(root) if include_absolute_root else None,
        "hashes_enabled": include_hashes,
        "summary": {
            "directories": len(directories),
            "files": len(files),
            "symlinks": len(symlinks),
            "skipped": len(skipped),
            "errors": len(errors),
            "total_file_bytes": sum(item["size_bytes"] for item in files),
        },
        "directories": sorted(directories),
        "files": sorted(files, key=lambda item: item["path"]),
        "symlinks": sorted(symlinks, key=lambda item: item["path"]),
        "skipped": sorted(skipped, key=lambda item: item["path"]),
        "errors": sorted(errors, key=lambda item: item["path"]),
    }


def markdown_report(data: dict) -> str:
    summary = data["summary"]
    lines = [
        "# Continuity workspace inventory",
        "",
        f"- Generated: {data['generated_utc']}",
        f"- Root name: `{data['root_name']}`",
        f"- Files: {summary['files']}",
        f"- Directories: {summary['directories']}",
        f"- Symlinks: {summary['symlinks']}",
        f"- Skipped: {summary['skipped']}",
        f"- Errors: {summary['errors']}",
        "",
        "## Files",
        "",
        "| Path | Bytes | Modified UTC | SHA-256 |",
        "|---|---:|---|---|",
    ]
    for item in data["files"]:
        digest = item.get("sha256") or item.get("hash_note") or "not requested"
        lines.append(f"| `{item['path']}` | {item['size_bytes']} | {item['modified_utc']} | {digest} |")
    lines.extend(["", "## Symlinks", ""])
    if data["symlinks"]:
        for item in data["symlinks"]:
            lines.append(f"- `{item['path']}` -> `{item['target']}` ({item['kind']})")
    else:
        lines.append("- None")
    lines.extend(["", "## Errors", ""])
    if data["errors"]:
        for item in data["errors"]:
            lines.append(f"- `{item['path']}`: {item['error']}")
    else:
        lines.append("- None")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a read-only continuity workspace inventory")
    parser.add_argument("root", type=Path)
    parser.add_argument("--json", dest="json_path", type=Path)
    parser.add_argument("--markdown", dest="markdown_path", type=Path)
    parser.add_argument("--hash", action="store_true", help="Read regular files and calculate SHA-256")
    parser.add_argument("--max-hash-bytes", type=int, default=100_000_000)
    parser.add_argument("--exclude", action="append", default=[], help="Additional exact file or directory name to skip")
    parser.add_argument(
        "--include-absolute-root",
        action="store_true",
        help="Include the machine-specific absolute root path; omit for portable or shareable reports",
    )
    args = parser.parse_args()

    data = inventory(
        args.root,
        args.hash,
        args.max_hash_bytes,
        DEFAULT_EXCLUDES | set(args.exclude),
        args.include_absolute_root,
    )
    json_text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"

    if args.json_path:
        args.json_path.parent.mkdir(parents=True, exist_ok=True)
        args.json_path.write_text(json_text, encoding="utf-8")
    if args.markdown_path:
        args.markdown_path.parent.mkdir(parents=True, exist_ok=True)
        args.markdown_path.write_text(markdown_report(data), encoding="utf-8")
    if not args.json_path and not args.markdown_path:
        print(json_text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
