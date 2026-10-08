#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

def local_resources(text):
    targets = re.findall(r"`((?:references|scripts|assets)/[^`\s]+)(?:\s+[^`]*)?`", text)
    targets += re.findall(r"\]\(\s*(<[^>]+>|[^\s)]+)", text)
    targets += re.findall(r"(?m)^\s*\[[^\]]+\]:\s*(<[^>]+>|\S+)", text)
    for target in dict.fromkeys(targets):
        target = target.strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        yield unquote(parsed.path)

def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] in {"-h", "--help"}:
        print("Usage: static-skill-audit.py SKILL_DIR", file=sys.stderr)
        return 0 if len(sys.argv) == 2 else 2
    root = Path(sys.argv[1]).expanduser().resolve()
    skill = root / "SKILL.md"
    findings = []
    if not skill.is_file():
        findings.append({"severity": "blocking", "issue": "SKILL.md missing"})
    else:
        text = skill.read_text(encoding="utf-8", errors="replace")
        fm = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
        if not fm:
            findings.append({"severity": "blocking", "issue": "YAML frontmatter missing"})
        else:
            head = fm.group(1)
            if not re.search(r"(?m)^name:\s*[^\s]", head):
                findings.append({"severity": "blocking", "issue": "name missing"})
            if not re.search(r"(?m)^description:\s*[^\s]", head):
                findings.append({"severity": "blocking", "issue": "description missing"})
            elif not re.search(r"\b(use when|use for|when (?:a |the )?user|also use)\b", head, re.I):
                findings.append({"severity": "major", "issue": "description lacks explicit trigger context"})
        if re.search(r"\b(TODO|TBD|PLACEHOLDER)\b", text, re.I):
            findings.append({"severity": "major", "issue": "unfinished placeholder found"})
        for rel in local_resources(text):
            if not (root / rel).exists():
                findings.append({"severity": "major", "issue": f"referenced resource missing: {rel}"})
        if len(text.splitlines()) > 500:
            findings.append({"severity": "minor", "issue": "SKILL.md exceeds 500 lines"})
    result = {"skill_dir": str(root), "status": "pass" if not findings else "review", "findings": findings}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 1 if any(x["severity"] == "blocking" for x in findings) else 0

if __name__ == "__main__":
    raise SystemExit(main())
