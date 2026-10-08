#!/usr/bin/env python3
import hashlib
import json
import os
import re
import sys
from pathlib import Path

PATTERNS = {
    "critical": [r"rm\s+-rf", r"curl[^\n|]*\|\s*(?:sh|bash)", r"wget[^\n|]*\|\s*(?:sh|bash)", r"eval\s*\(", r"exec\s*\("],
    "high": [r"\.ssh", r"keychain", r"cookies?", r"api[_-]?key", r"secret", r"private[_-]?key", r"base64\s+(-d|--decode)", r"sudo\b"],
    "medium": [r"https?://", r"subprocess", r"os\.system", r"child_process", r"chmod\s+777", r"crontab", r"launchctl"],
}
TEXT_EXT = {".md", ".txt", ".py", ".sh", ".js", ".ts", ".json", ".yaml", ".yml", ".toml", ".xml"}

def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] in {"-h", "--help"}:
        print("Usage: scan-skill-static.py PATH", file=sys.stderr)
        return 0 if len(sys.argv) == 2 else 2
    root = Path(sys.argv[1]).expanduser().resolve()
    if not root.exists():
        print(json.dumps({"error": "path not found", "path": str(root)}))
        return 2
    files, findings = [], []
    paths = [root] if root.is_file() else sorted(p for p in root.rglob("*") if p.is_file() or p.is_symlink())
    for path in paths:
        rel = str(path.relative_to(root)) if root.is_dir() else path.name
        if path.is_symlink():
            findings.append({"severity": "high", "file": rel, "line": 0, "match": "symbolic link", "target": os.readlink(path)})
            continue
        data = path.read_bytes()
        files.append({"file": rel, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
        if path.suffix.lower() not in TEXT_EXT or len(data) > 2_000_000:
            continue
        text = data.decode("utf-8", errors="replace")
        for number, line in enumerate(text.splitlines(), 1):
            for severity, patterns in PATTERNS.items():
                for pattern in patterns:
                    if re.search(pattern, line, re.I):
                        findings.append({"severity": severity, "file": rel, "line": number, "pattern": pattern, "excerpt": line[:240]})
    print(json.dumps({"root": str(root), "files": files, "findings": findings, "notice": "Best-effort static scan; manual review required."}, indent=2, ensure_ascii=False))
    return 1 if any(x["severity"] in {"critical", "high"} for x in findings) else 0

if __name__ == "__main__":
    raise SystemExit(main())

