#!/usr/bin/env python3
"""Preview, create or check a small shared KB. Existing files are never replaced."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets" / "vault"
MARKER = ".kb-bootstrap.json"
SCHEMA = 1
EXTRA_DIRS = ("00_System/Decisions/Records", "00_System/Work/Archive", "99_Archive")
TOKEN = re.compile(r"\{\{([A-Z_]+)\}\}")


def label(value):
    if not value.strip() or any(ord(char) < 32 or ord(char) == 127 for char in value):
        raise argparse.ArgumentTypeError("use a nonempty single-line value")
    return value.strip()


def markdown(value):
    return re.sub(r"([\\`*_{}\[\]<>#!|])", r"\\\1", value)


def templates(project, owner, objective):
    today = dt.date.today().isoformat()
    values = {"PROJECT": markdown(project), "PROJECT_YAML": json.dumps(project),
              "OWNER": markdown(owner), "OWNER_YAML": json.dumps(owner),
              "OBJECTIVE": markdown(objective), "DATE": today}
    result = {}
    for asset in sorted(ASSETS.rglob("*.tmpl")):
        relative = asset.relative_to(ASSETS).as_posix()[:-5]
        result[relative] = TOKEN.sub(lambda match: values[match[1]], asset.read_text(encoding="utf-8"))
    if not result:
        raise ValueError("bundled KB templates are missing")
    return result


def safe_target(root, relative, directory=False):
    target = root / relative
    for part in (target, *target.parents):
        if part == root.parent:
            break
        if part.is_symlink():
            raise ValueError(f"refusing symlink in managed path: {relative}")
        if part != target and part.exists() and not part.is_dir():
            raise ValueError(f"parent is not a directory: {relative}")
    if target.exists() and (target.is_dir() != directory or (not directory and not target.is_file())):
        raise ValueError(f"unexpected file type at managed path: {relative}")
    return target


def inspect_root(root, project):
    if root.is_symlink() or (root.exists() and not root.is_dir()):
        raise ValueError("KB root must be a directory, not a file or symlink")
    marker = safe_target(root, MARKER)
    if marker.exists():
        data = json.loads(marker.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or data.get("schema") != SCHEMA or data.get("project") != project:
            raise ValueError("bootstrap marker has a different schema/project; map the existing KB instead")
    elif root.exists() and any(path.name != ".DS_Store" for path in root.iterdir()):
        raise ValueError("nonempty KB without a matching bootstrap marker; use the existing-KB adoption workflow")
    return marker


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", help="Explicit target KB directory")
    parser.add_argument("--project", required=True, type=label)
    parser.add_argument("--owner", default="Unassigned", type=label)
    parser.add_argument("--objective", default="Not supplied", type=label,
                        help="Supplied first work objective; recorded before later enrichment")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--apply", action="store_true", help="Create missing starter files; never overwrite")
    modes.add_argument("--check", action="store_true", help="Read-only starter structure check")
    args = parser.parse_args()
    root = Path(args.root).expanduser().absolute()
    created = []
    try:
        contents = templates(args.project, args.owner, args.objective)
        marker = inspect_root(root, args.project)
        paths = {name: safe_target(root, name) for name in contents}
        directories = {safe_target(root, name, directory=True) for name in EXTRA_DIRS}
        directories.update(path.parent for path in paths.values())
        # Preflight all parents before any write so layout conflicts cannot half-create a KB.
        for directory in directories:
            safe_target(root, directory.relative_to(root), directory=True)
        missing = [name for name, path in paths.items() if not path.exists()]
        preserved = [name for name in paths if name not in missing]
        missing_dirs = sorted(path.relative_to(root).as_posix() for path in directories if not path.exists())
        if args.check:
            problems = [f"missing file: {name}" for name in missing]
            problems.extend(f"missing directory: {name}" for name in missing_dirs)
            if not marker.exists():
                problems.append("missing bootstrap marker")
            for name in preserved:
                text = paths[name].read_text(encoding="utf-8")
                if not text.strip() or TOKEN.search(text):
                    problems.append(f"empty or unrendered starter: {name}")
            if "CLAUDE.md" in preserved and not re.search(
                    r"^@AGENTS\.md\s*$", paths["CLAUDE.md"].read_text(encoding="utf-8"), re.MULTILINE):
                problems.append("Claude adapter no longer imports the shared AGENTS.md")
            print(json.dumps({"root": str(root), "mode": "check", "structure_complete": not problems,
                              "problems": problems, "host_behavior": "not_tested"}, indent=2))
            return 1 if problems else 0
        if args.apply:
            root.mkdir(parents=True, exist_ok=True)
            if not marker.exists():
                with marker.open("x", encoding="utf-8") as stream:
                    json.dump({"schema": SCHEMA, "project": args.project}, stream, indent=2)
                    stream.write("\n")
                created.append(MARKER)
            for directory in sorted(directories, key=lambda path: len(path.parts)):
                directory.mkdir(parents=True, exist_ok=True)
            for name in missing:
                # Exclusive creation also preserves a file created after the preflight.
                with paths[name].open("x", encoding="utf-8") as stream:
                    stream.write(contents[name])
                created.append(name)
        print(json.dumps({"root": str(root), "mode": "apply" if args.apply else "preview",
                          "create": missing, "create_directories": missing_dirs,
                          "created": created, "preserved": preserved,
                          "next": "Read and adapt project facts; run structure check, KB lint and host handoff checks."}, indent=2))
        return 0
    except (OSError, ValueError, KeyError) as error:
        print(json.dumps({"root": str(root), "error": str(error), "created": created}, indent=2))
        return 2


if __name__ == "__main__":
    sys.exit(main())
