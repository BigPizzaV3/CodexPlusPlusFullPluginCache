#!/usr/bin/env python3
"""Check a saved Reteno email model against its packaged Fiteno template.

Compares the live model's block count, font families, font resources, and native
preheader with the packaged template, and confirms the packaged model is intact.
Prints {"ok": bool, "problems": [...]} and exits 0 when every check passes.

Usage:
  python check_fiteno_template.py --template-dir <slug dir> --live-model <downloaded.json>
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

STRUCTURED = re.compile(r'"fontFamily"\s*:\s*"([^"]*)"')
INLINE = re.compile(r'font-family\s*:\s*((?:&#39;|[^;"\\])+)', re.I)


def blocks(model):
    return sum(len(container.get("blocks", []))
               for stripe in model.get("stripes", [])
               for structure in stripe.get("structures", [])
               for column in structure.get("columns", [])
               for container in column.get("containers", []))


def font_families(model):
    """Every font stack the email uses, ignoring quoting and spacing."""
    text = json.dumps({k: v for k, v in model.items() if k != "resources"})
    norm = lambda stack: re.sub(r"['\"]|&#39;|\s+", "", stack).lower()
    return {norm(s) for s in STRUCTURED.findall(text)} | {norm(s) for s in INLINE.findall(text)}


def preheader(model):
    return ((model.get("metadata") or {}).get("preheader") or {}).get("text") or ""


def check(template_dir, live):
    meta = json.loads((template_dir / "metadata.json").read_text(encoding="utf-8"))
    raw = (template_dir / "model.json").read_bytes()
    source = json.loads(raw)
    problems = []
    if hashlib.sha256(raw).hexdigest() != meta["modelSha256"]:
        problems.append("packaged model.json does not match metadata.json modelSha256")
    got = blocks(live)
    if got != meta["blockCount"]:
        problems.append(f"blocks {got}, expected {meta['blockCount']}"
                        + (" (only the shell placeholder: the model did not land)" if got == 1 else ""))
    if font_families(live) != font_families(source):
        problems.append("font families differ from the packaged template")
    fonts = (live.get("resources") or {}).get("fonts") or []
    if (source.get("resources") or {}).get("fonts") and not fonts:
        problems.append("font resources missing")
    if any(f.get("url") and not str(f["url"]).startswith("https://") for f in fonts):
        problems.append("a font resource URL is not https")
    want = (meta.get("preheader") or "").strip()
    if want and preheader(live).strip() != want:
        problems.append("preheader missing or different")
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--template-dir", required=True, type=Path)
    parser.add_argument("--live-model", required=True, type=Path)
    args = parser.parse_args()
    problems = check(args.template_dir, json.loads(args.live_model.read_text(encoding="utf-8")))
    print(json.dumps({"ok": not problems, "problems": problems}))
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
