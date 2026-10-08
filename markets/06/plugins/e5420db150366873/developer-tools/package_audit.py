#!/usr/bin/env python3
"""Audit parseability and local references across the release tree."""
from __future__ import annotations
import json
import os
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def native(path: Path) -> str:
    value = str(path.resolve())
    return "\\\\?\\" + value if os.name == "nt" and not value.startswith("\\\\?\\") else value


def walk_files() -> list[tuple[str, str]]:
    root = native(ROOT)
    result = []
    for directory, _, filenames in os.walk(root):
        for filename in filenames:
            absolute = os.path.join(directory, filename)
            relative = os.path.relpath(absolute, root).replace("\\", "/")
            result.append((relative, absolute))
    return sorted(result)


def main() -> int:
    errors = []
    json_count = markdown_count = link_count = python_count = 0
    for relative, absolute in walk_files():
        suffix = Path(relative).suffix.lower()
        if suffix == ".json":
            json_count += 1
            try:
                with open(absolute, encoding="utf-8") as handle:
                    json.load(handle)
            except Exception as exc:
                errors.append(f"invalid JSON {relative}: {exc}")
        elif suffix == ".md":
            markdown_count += 1
            with open(absolute, encoding="utf-8") as handle:
                text = handle.read()
            for raw in LINK.findall(text):
                target = raw.strip().split("#", 1)[0]
                if not target or target.startswith(("http://", "https://", "mailto:", "codex://", "/")):
                    continue
                link_count += 1
                target_path = (ROOT / Path(relative).parent / target).resolve()
                if not os.path.exists(native(target_path)):
                    errors.append(f"broken local link {relative} -> {raw}")
        elif suffix == ".py":
            python_count += 1
            try:
                with open(absolute, encoding="utf-8") as handle:
                    compile(handle.read(), relative, "exec")
            except Exception as exc:
                errors.append(f"invalid Python {relative}: {exc}")
    result = {"ok": not errors, "errors": errors, "json_files": json_count,
              "markdown_files": markdown_count, "local_links_checked": link_count,
              "python_files_compiled": python_count, "total_files": len(walk_files())}
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
