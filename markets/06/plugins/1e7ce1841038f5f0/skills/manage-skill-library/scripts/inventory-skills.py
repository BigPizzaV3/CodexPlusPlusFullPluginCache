#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import re
import stat
from pathlib import Path

def parse_frontmatter(text):
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    values = {}
    if match:
        for line in match.group(1).splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                values[key.strip()] = value.strip().strip('"\'')
    return values

def inventory(root):
    records = []
    skipped_roots = []
    for folder in sorted(root.iterdir()):
        if folder.is_symlink():
            skipped_roots.append({"path": folder.name, "kind": "symlink", "status": "SKIPPED_NO_FOLLOW"})
            continue
        if not folder.is_dir():
            continue
        skill_md = folder / "SKILL.md"
        if skill_md.is_symlink():
            skipped_roots.append({"path": str(skill_md.relative_to(root)), "kind": "symlink", "status": "SKIPPED_NO_FOLLOW"})
            continue
        if not skill_md.is_file():
            continue
        files = []
        skipped = []
        source = None
        aggregate = hashlib.sha256()
        paths = []
        def walk_error(error):
            raise error
        for parent, dirs, names in os.walk(folder, followlinks=False, onerror=walk_error):
            for name in sorted(dirs + names):
                path = Path(parent) / name
                if path.is_symlink():
                    skipped.append({"path": str(path.relative_to(folder)), "kind": "symlink", "status": "SKIPPED_NO_FOLLOW"})
                    if name in dirs:
                        dirs.remove(name)
                elif name in names:
                    paths.append(path)
        for path in sorted(paths):
            # Refuse special files and final-component link substitutions as well.
            if not stat.S_ISREG(path.lstat().st_mode):
                skipped.append({"path": str(path.relative_to(folder)), "kind": "special_file", "status": "SKIPPED"})
                continue
            flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
            with os.fdopen(os.open(path, flags), "rb") as stream:
                if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                    raise OSError(f"Not a regular file: {path}")
                data = stream.read()
            rel = str(path.relative_to(folder))
            digest = hashlib.sha256(data).hexdigest()
            aggregate.update(rel.encode()); aggregate.update(digest.encode())
            files.append({"path": rel, "bytes": len(data), "sha256": digest})
            if path == skill_md:
                source = data.decode("utf-8", errors="replace")
        if source is None:
            raise OSError(f"Readable regular SKILL.md required: {skill_md}")
        meta = parse_frontmatter(source)
        records.append({"name": meta.get("name", folder.name), "description": meta.get("description", ""), "path": str(folder), "aggregate_sha256": aggregate.hexdigest(), "files": files, "skipped_entries": skipped, "status": "incomplete" if skipped else "complete"})
    return records, skipped_roots

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root")
    parser.add_argument("--json")
    parser.add_argument("--markdown")
    args = parser.parse_args()
    try:
        root = Path(args.root).expanduser().resolve()
        if not root.is_dir():
            parser.error(f"Library root is not an existing directory: {root}")
        records, skipped_roots = inventory(root)
    except (OSError, RuntimeError) as error:
        parser.error(f"Inventory failed: {error}")
    incomplete = bool(skipped_roots) or any(r["skipped_entries"] for r in records)
    payload = {"root": str(root), "count": len(records), "status": "review" if incomplete else "complete", "skipped_entries": skipped_roots, "skills": records}
    rendered = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.json: Path(args.json).write_text(rendered + "\n", encoding="utf-8")
    if args.markdown:
        lines = ["# Persönliche Skill-Bibliothek", "", f"Quelle: `{root}`", "", f"Anzahl: **{len(records)}**", "", "| Skill | Aufgabe | Dateien | Prüfsumme |", "|---|---|---:|---|"]
        lines += [f"| `${r['name']}` | {r['description'].replace('|', '/')} | {len(r['files'])} | `{r['aggregate_sha256']}` |" for r in records]
        if incomplete:
            lines += ["", "REVIEW: Links/special files skipped without reading targets; inventory is incomplete."]
            lines += [f"- {x['path']}: {x['status']}" for x in skipped_roots]
            lines += [f"- {r['name']}/{x['path']}: {x['status']}" for r in records for x in r['skipped_entries']]
        Path(args.markdown).write_text("\n".join(lines) + "\n", encoding="utf-8")
    if not args.json and not args.markdown: print(rendered)
    return 1 if incomplete else 0

if __name__ == "__main__": raise SystemExit(main())
