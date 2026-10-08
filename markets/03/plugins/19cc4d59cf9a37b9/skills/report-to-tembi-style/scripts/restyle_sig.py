"""Shared stamp + validation logic for Tembi-restyled reports.

No secret. The stamp is a self-describing marker that binds a content hash to the
file; the validator confirms (a) the Tembi design fingerprint is present and
(b) the content has not changed since it was stamped. Together they reject both
"never restyled" and "restyled then edited without re-running the skill".

Importable (validate / stamp) and runnable as a CLI:

    python restyle_sig.py stamp    in.html [-o out.html]
    python restyle_sig.py validate in.html        # exit 0 = ok, 1 = rejected
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

STAMP_META_NAME = "tembi-restyle"
HASH_ALGO = "sha256"

_STAMP_RE = re.compile(
    r"[ \t]*<meta\s+name=[\"']" + re.escape(STAMP_META_NAME) + r"[\"'][^>]*>\s*\n?",
    re.IGNORECASE,
)
_HEAD_RE = re.compile(r"(<head[^>]*>)", re.IGNORECASE)
_HTML_RE = re.compile(r"(<html[^>]*>)", re.IGNORECASE)
_CONTENT_RE = re.compile(
    r"<meta\s+name=[\"']" + re.escape(STAMP_META_NAME) + r"[\"']\s+content=[\"']([^\"']*)[\"']",
    re.IGNORECASE,
)


def _fingerprint_path() -> Path:
    return Path(__file__).resolve().parent.parent / "assets" / "tembi-restyle-fingerprint.json"


def load_fingerprint(path: Path | None = None) -> dict:
    return json.loads((path or _fingerprint_path()).read_text(encoding="utf-8"))


def canonical_bytes(html: str) -> bytes:
    """Content with every restyle stamp removed and line endings normalized.

    Both stamping and validation hash this, so the stamp tag itself (and its
    volatile timestamp) never affects the hash.
    """
    stripped = _STAMP_RE.sub("", html)
    stripped = stripped.replace("\r\n", "\n").replace("\r", "\n")
    return stripped.encode("utf-8")


def content_hash(html: str) -> str:
    return hashlib.sha256(canonical_bytes(html)).hexdigest()


def stamp(html: str, ts: str | None = None) -> str:
    """Return html with a fresh restyle stamp injected just after <head>."""
    ts = ts or _dt.date.today().isoformat()
    digest = content_hash(html)
    tag = (
        f'<meta name="{STAMP_META_NAME}" '
        f'content="v=1;ts={ts};algo={HASH_ALGO};hash={digest}">'
    )
    without = _STAMP_RE.sub("", html)
    if _HEAD_RE.search(without):
        return _HEAD_RE.sub(lambda m: m.group(1) + "\n  " + tag, without, count=1)
    if _HTML_RE.search(without):
        return _HTML_RE.sub(lambda m: m.group(1) + "\n" + tag, without, count=1)
    return tag + "\n" + without


def _parse_stamp(html: str) -> dict | None:
    m = _CONTENT_RE.search(html)
    if not m:
        return None
    out: dict[str, str] = {}
    for part in m.group(1).split(";"):
        if "=" in part:
            k, _, v = part.partition("=")
            out[k.strip()] = v.strip()
    return out


@dataclass
class ValidationResult:
    ok: bool
    failures: list[str] = field(default_factory=list)
    stamp: dict | None = None

    def as_dict(self) -> dict:
        return {"ok": self.ok, "failures": self.failures, "stamp": self.stamp}


def validate(html: str, fingerprint: dict | None = None) -> ValidationResult:
    """Reject unless the Tembi fingerprint is present AND the stamp hash matches."""
    fp = fingerprint or load_fingerprint()
    failures: list[str] = []
    hay = html.lower()

    req = fp["required_all"]
    for font in req["fonts"]:
        forms = {font.lower(), font.lower().replace(" ", "+")}
        if not any(form in hay for form in forms):
            failures.append(f"missing required font marker: {font}")
    for token in req["tokens"]:
        if token.lower() not in hay:
            failures.append(f"missing required design token: {token}")
    if req["logo_signature"].lower() not in hay:
        failures.append("missing Tembi logo signature")

    forb = fp.get("forbidden_any", {})
    for label, needles in forb.items():
        if label.startswith("_"):
            continue
        for needle in needles:
            if needle.lower() in hay:
                failures.append(f"un-restyled source marker present ({label}): {needle}")

    parsed = _parse_stamp(html)
    if parsed is None:
        failures.append("no tembi-restyle stamp found")
    else:
        embedded = parsed.get("hash", "")
        actual = content_hash(html)
        if not embedded:
            failures.append("stamp has no hash")
        elif embedded != actual:
            failures.append("hash mismatch: content edited since it was stamped")

    return ValidationResult(ok=not failures, failures=failures, stamp=parsed)


def _cli(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Tembi restyle stamp / validate")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sp = sub.add_parser("stamp", help="inject a restyle stamp")
    sp.add_argument("file")
    sp.add_argument("-o", "--out", help="output path (default: overwrite input)")
    sp.add_argument("--ts", help="timestamp (default: today)")
    vp = sub.add_parser("validate", help="validate a stamped file")
    vp.add_argument("file")
    args = ap.parse_args(argv)

    html = Path(args.file).read_text(encoding="utf-8")
    if args.cmd == "stamp":
        out = stamp(html, ts=args.ts)
        dest = Path(args.out or args.file)
        dest.write_text(out, encoding="utf-8")
        print(f"stamped -> {dest}  hash={content_hash(out)}")
        return 0

    result = validate(html)
    if result.ok:
        print("OK: valid Tembi-restyled report")
        return 0
    print("REJECTED: not a valid Tembi-restyled report", file=sys.stderr)
    for f in result.failures:
        print(f"  - {f}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(_cli(sys.argv[1:]))
