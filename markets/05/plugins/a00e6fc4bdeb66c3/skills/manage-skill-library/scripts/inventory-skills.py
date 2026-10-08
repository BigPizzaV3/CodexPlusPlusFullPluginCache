#!/usr/bin/env python3
import argparse
import hashlib
import json
import re
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
    for skill_md in sorted(root.glob("*/SKILL.md")):
        folder = skill_md.parent
        files = []
        aggregate = hashlib.sha256()
        for path in sorted(p for p in folder.rglob("*") if p.is_file()):
            data = path.read_bytes()
            rel = str(path.relative_to(folder))
            digest = hashlib.sha256(data).hexdigest()
            aggregate.update(rel.encode()); aggregate.update(digest.encode())
            files.append({"path": rel, "bytes": len(data), "sha256": digest})
        meta = parse_frontmatter(skill_md.read_text(encoding="utf-8", errors="replace"))
        records.append({"name": meta.get("name", folder.name), "description": meta.get("description", ""), "path": str(folder), "aggregate_sha256": aggregate.hexdigest(), "files": files})
    return records

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root")
    parser.add_argument("--json")
    parser.add_argument("--markdown")
    args = parser.parse_args()
    root = Path(args.root).expanduser().resolve()
    records = inventory(root)
    payload = {"root": str(root), "count": len(records), "skills": records}
    rendered = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.json: Path(args.json).write_text(rendered + "\n", encoding="utf-8")
    if args.markdown:
        lines = ["# Persönliche Skill-Bibliothek", "", f"Quelle: `{root}`", "", f"Anzahl: **{len(records)}**", "", "| Skill | Aufgabe | Dateien | Prüfsumme |", "|---|---|---:|---|"]
        lines += [f"| `${r['name']}` | {r['description'].replace('|', '/')} | {len(r['files'])} | `{r['aggregate_sha256']}` |" for r in records]
        Path(args.markdown).write_text("\n".join(lines) + "\n", encoding="utf-8")
    if not args.json and not args.markdown: print(rendered)

if __name__ == "__main__": main()
