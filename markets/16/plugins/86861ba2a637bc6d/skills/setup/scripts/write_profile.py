#!/usr/bin/env python3
"""Write the finance profile, .magnos/finance.md, from the answers to the setup questions.

Values not given keep their current value when the file exists; on a first run
they come from the folder scan (.magnos/runs/setup.json), then from the Magnos
defaults. Lines the person added by hand are kept. Prints what changed and the file.

  python3 scripts/write_profile.py --fiscal-year-start April --currency EUR \
      --materiality '$25K and 10%' --variance-sign favourable-positive
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import sys
from decimal import Decimal
from typing import Dict, List, Optional, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import magnos_fin as mf  # noqa: E402

KEYS = ["fiscal_year_start", "currency", "materiality_amount", "materiality_pct", "variance_sign", "entities", "figure_check"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November", "December"]
SIGNS = {
    "favourable-positive": "favourable-positive", "favourable": "favourable-positive",
    "favourable-is-positive": "favourable-positive", "fav-positive": "favourable-positive",
    "better-positive": "favourable-positive",
    "actual-minus-budget": "actual-minus-budget", "actual-less-budget": "actual-minus-budget",
    "actual-budget": "actual-minus-budget", "raw": "actual-minus-budget",
}
LINE_RE = re.compile(r"^\s*[-*]?\s*([a-z_]+)\s*:\s*(.*?)\s*$")  # the same lines magnos_fin.load_profile reads


def fail(msg: str) -> None:
    print(msg, file=sys.stderr)
    sys.exit(2)


def norm_month(v: str) -> str:
    s = v.strip().lower()
    if s.isdigit() and 1 <= int(s) <= 12:
        return MONTHS[int(s) - 1]
    word = re.split(r"[\s,]+", s)[0] if s else ""
    for m in MONTHS:
        if word and (m.lower() == word or (len(word) >= 3 and m.lower().startswith(word))):
            return m
    fail(f"The fiscal year start must be a month, such as January or April; got {v!r}.")
    return ""


def norm_currency(v: str) -> str:
    s = v.strip()
    sym = {"$": "USD", "€": "EUR", "£": "GBP", "¥": "JPY"}
    if s in sym:
        return sym[s]
    if re.fullmatch(r"[A-Za-z]{3}", s):
        return s.upper()
    fail(f"The currency must be a three-letter code such as USD, EUR or GBP; got {v!r}.")
    return ""


def norm_amount(v: str) -> str:
    d = mf.to_decimal(v)
    if d is None or d <= 0:
        fail(f"The materiality amount must be a positive amount such as 25000 or $25K; got {v!r}.")
    return plain(d)


def norm_pct(v: str) -> str:
    d = mf.to_decimal(v)
    if d is None or d <= 0 or d > 100:
        fail(f"The materiality percentage must be between 0 and 100, such as 10 or 10%; got {v!r}.")
    return plain(d)


def plain(d: Decimal) -> str:
    d = d.normalize()
    return str(d.quantize(Decimal(1))) if d == d.to_integral() else format(d, "f")


def norm_sign(v: str) -> str:
    key = re.sub(r"[\s_]+", "-", v.strip().lower()).replace("favorable", "favourable")
    key = re.sub(r"\(.*?\)", "", key).strip("-")
    if key in SIGNS:
        return SIGNS[key]
    fail("The variance sign must be favourable-positive (better is positive) or actual-minus-budget "
         f"(positive when actual is higher); got {v!r}.")
    return ""


def norm_check(v: str) -> str:
    s = v.strip().lower()
    if s not in ("warn", "block", "off"):
        fail(f"figure_check must be warn, block or off; got {v!r}.")
    return s


def norm_entities(v: str) -> str:
    parts = [p.strip() for p in re.split(r"[,;]", v) if p.strip()]
    return ", ".join(dict.fromkeys(parts))


def split_materiality(v: str) -> Tuple[str, str]:
    """"$25K and 10%" -> ("25000", "10")."""
    m = re.match(r"^\s*(.+?)\s*(?:and|/|,|&|\+)\s*(.+?)\s*$", v)
    if not m:
        fail(f"Write the materiality as an amount and a percentage, such as '$25K and 10%' (single quotes in a shell); got {v!r}.")
    return norm_amount(m.group(1)), norm_pct(m.group(2))


def read_existing(path: str) -> Tuple[Dict[str, str], List[str]]:
    """The profile's values, and any other `key: value` lines to keep as they are."""
    values: Dict[str, str] = {}
    extra: List[str] = []
    if not os.path.exists(path):
        return values, extra
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = LINE_RE.match(line)
            if not m:
                continue
            if m.group(1) in KEYS:
                values[m.group(1)] = m.group(2)
            else:
                extra.append(line.rstrip("\n"))
    return values, extra


def scan_proposals(cwd: str) -> Dict[str, str]:
    path = os.path.join(cwd, ".magnos", "runs", "setup.json")
    try:
        with open(path, encoding="utf-8") as fh:
            return {k: str(v) for k, v in (json.load(fh).get("proposals") or {}).items() if v not in (None, "")}
    except (OSError, ValueError):
        return {}


def render(values: Dict[str, str], extra: List[str], written: str) -> str:
    lines = [
        "# Magnos finance profile",
        "",
        f"Written by /magnos:setup on {written}. Every Magnos skill reads this file. "
        "Change a value here, or run /magnos:setup again.",
        "",
    ]
    for k in KEYS:
        v = values.get(k, "")
        lines.append(f"{k}: {v}".rstrip())
    if extra:
        lines += [""] + extra
    return "\n".join(lines) + "\n"


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Write .magnos/finance.md from the setup answers.")
    p.add_argument("--fiscal-year-start", help="the month the fiscal year starts: January, April, 4 …")
    p.add_argument("--currency", help="the reporting currency: USD, EUR, GBP …")
    p.add_argument("--materiality", help="amount and percentage together, in single quotes: '$25K and 10%%'")
    p.add_argument("--materiality-amount", help="25000 or $25K")
    p.add_argument("--materiality-pct", help="10 or 10%%")
    p.add_argument("--variance-sign", help="favourable-positive or actual-minus-budget")
    p.add_argument("--entities", help='comma-separated: "US, UK, EU"')
    p.add_argument("--figure-check", help="warn (default), block or off")
    p.add_argument("--today", help=argparse.SUPPRESS)
    a = p.parse_args(argv)

    cwd = os.getcwd()
    path = os.path.join(cwd, mf.PROFILE_PATH)
    existing, extra = read_existing(path)
    first_run = not existing
    base: Dict[str, str] = {
        "fiscal_year_start": str(mf.PROFILE_DEFAULTS["fiscal_year_start"]),
        "currency": str(mf.PROFILE_DEFAULTS["currency"]),
        "materiality_amount": plain(mf.PROFILE_DEFAULTS["materiality_amount"]),
        "materiality_pct": plain(mf.PROFILE_DEFAULTS["materiality_pct"]),
        "variance_sign": str(mf.PROFILE_DEFAULTS["variance_sign"]),
        "entities": "",
        "figure_check": str(mf.PROFILE_DEFAULTS["figure_check"]),
    }
    if first_run:
        scan = scan_proposals(cwd)
        for k in ("fiscal_year_start", "currency", "entities"):
            if scan.get(k):
                base[k] = scan[k]
    base.update({k: v for k, v in existing.items() if v != "" or k == "entities"})

    new = dict(base)
    if a.fiscal_year_start:
        new["fiscal_year_start"] = norm_month(a.fiscal_year_start)
    if a.currency:
        new["currency"] = norm_currency(a.currency)
    if a.materiality:
        new["materiality_amount"], new["materiality_pct"] = split_materiality(a.materiality)
    if a.materiality_amount:
        new["materiality_amount"] = norm_amount(a.materiality_amount)
    if a.materiality_pct:
        new["materiality_pct"] = norm_pct(a.materiality_pct)
    if a.variance_sign:
        new["variance_sign"] = norm_sign(a.variance_sign)
    if a.entities is not None:
        new["entities"] = norm_entities(a.entities)
    if a.figure_check:
        new["figure_check"] = norm_check(a.figure_check)
    # values kept from an older file are checked too, so a typo there is caught now
    new["fiscal_year_start"] = norm_month(new["fiscal_year_start"])
    new["currency"] = norm_currency(new["currency"])
    new["materiality_amount"] = norm_amount(new["materiality_amount"])
    new["materiality_pct"] = norm_pct(new["materiality_pct"])
    new["variance_sign"] = norm_sign(new["variance_sign"])
    new["figure_check"] = norm_check(new["figure_check"])

    changes = [(k, existing.get(k, ""), new[k]) for k in KEYS if not first_run and existing.get(k, "") != new[k]]
    today = a.today or _dt.date.today().isoformat()
    written = today
    if not first_run and not changes:
        with open(path, encoding="utf-8") as fh:
            m = re.search(r"on (\d{4}-\d{2}-\d{2})", fh.read())
        written = m.group(1) if m else today
    text = render(new, extra, written)
    if first_run or changes:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)

    prof = mf.load_profile(cwd)
    if first_run:
        head = f"Wrote .magnos/finance.md: {mf.profile_line(prof)}."
    elif changes:
        head = f"Updated .magnos/finance.md: {mf.profile_line(prof)}."
    else:
        head = f"No changes: .magnos/finance.md already holds these answers ({mf.profile_line(prof)})."
    out = [head]
    if changes:
        out += ["", mf.md_table(["Setting", "Was", "Now"], [[k, old or "—", nv or "—"] for k, old, nv in changes],
                                ["l", "l", "l"])]
    out += ["", "```", text.rstrip("\n"), "```"]
    data = {"path": path, "values": new, "changed": [c[0] for c in changes], "first_run": first_run}
    mf.emit("\n".join(out), data, os.path.join(cwd, ".magnos", "runs", "setup-profile.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
