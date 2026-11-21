#!/usr/bin/env python3
"""Quota attainment by rep for a quarter, with the last three quarters and next quarter's coverage.

Reads a deals export (one row per deal: rep, amount, close date, and a stage when it holds
open deals) and a quota file, wide (one row per rep, one column per quarter: 2026Q3 or
"Q3 2026") or long (rep, quarter, quota). Bookings are closed-won deals closing in the
quarter; pipeline is open deals closing in the next quarter.

  python3 scripts/attainment.py deals.csv quotas.csv --quarter 2026Q3
  python3 scripts/attainment.py deals.csv quotas.csv --quarter 2026Q3 --history

Prints Markdown and saves .magnos/runs/attainment.json. Writes nothing else.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
from decimal import Decimal
from typing import Dict, Optional, Sequence, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import magnos_fin as mf  # noqa: E402

D0 = Decimal(0)
JSON_PATH = os.path.join(".magnos", "runs", "attainment.json")
REP_COLS = ("rep", "sales_rep", "owner", "deal_owner", "owner_name", "account_executive", "ae", "salesperson", "seller")
AMOUNT_COLS = ("amount", "bookings", "acv", "deal_value", "value", "arr", "tcv")
DATE_COLS = ("close_date", "closed_date", "closedate", "close", "booked_date", "date")
STAGE_COLS = ("stage", "deal_stage", "status")

Quarter = Tuple[int, int]  # (year, quarter)


class InputError(Exception):
    """A problem with the person's files or flags: exit 2 with one plain sentence."""


def parse_quarter(text: str) -> Optional[Quarter]:
    s = str(text or "").strip().upper().replace(" ", "")
    for pat in (r"(?:FY)?(\d{4})[-_/]?Q([1-4])", r"Q([1-4])[-_/]?(?:FY)?(\d{4})", r"(?:FY)?(\d{2})[-_/]?Q([1-4])",
                r"Q([1-4])[-_/]?(?:FY)?(\d{2})"):
        m = re.fullmatch(pat, s)
        if m:
            a, b = m.groups()
            year, q = (a, b) if pat.startswith("(?:FY)?(") else (b, a)
            y = int(year)
            return (y + 2000 if y < 100 else y, int(q))
    return None


def label(q: Quarter) -> str:
    return f"Q{q[1]} {q[0]}"


def shift(q: Quarter, n: int) -> Quarter:
    i = q[0] * 4 + (q[1] - 1) + n
    return (i // 4, i % 4 + 1)


def quarter_of(d: dt.date, fiscal_start: int) -> Quarter:
    q = (d.month - fiscal_start) % 12 // 3 + 1
    year = d.year if fiscal_start == 1 else d.year + (1 if d.month >= fiscal_start else 0)
    return (year, q)


def column(t: mf.Table, override: Optional[str], what: str, flag: str, names: Sequence[str], required: bool = True) -> Optional[str]:
    name = os.path.basename(t.path)
    if override:
        if override not in t.columns:
            raise InputError(f"{name} has no column named '{override}'; its columns are {', '.join(t.columns)}.")
        return override
    c = mf.find_column(t, *names)
    if not c and required:
        raise InputError(f"{name} has no {what} column (looked for {', '.join(names[:4])}). "
                         f"Rename the column, or pass {flag} NAME.")
    return c


def read(path: str) -> mf.Table:
    if not os.path.exists(path):
        raise InputError(f"Cannot find {path}. Check the path, or run the command from the folder that holds it.")
    try:
        t = mf.read_table(path)
    except Exception as exc:
        raise InputError(f"Cannot read {os.path.basename(path)} ({exc.__class__.__name__}). Save it as CSV or XLSX.")
    if not t.rows:
        raise InputError(f"{os.path.basename(path)} has no rows. Check that it is the right export.")
    return t


def load_quotas(t: mf.Table, rep_override: Optional[str]) -> Tuple[Dict[str, Dict[Quarter, Decimal]], Dict[str, str], Dict[str, str]]:
    """rep key -> quarter -> quota; rep key -> name as written; rep key -> region (when there is one)."""
    rep = column(t, rep_override, "rep", "--quota-rep-column", REP_COLS + ("name",))
    region = mf.find_column(t, "region", "entity", "team", "territory")
    names, regions, out = {}, {}, {}
    wide = {c: parse_quarter(c) for c in t.columns if parse_quarter(c)}
    if wide:
        for r in t.rows:
            k = r.get(rep, "").strip().lower()
            if not k:
                continue
            names[k] = r[rep].strip()
            if region:
                regions[k] = r.get(region, "").strip()
            for c, q in wide.items():
                v = mf.to_decimal(r.get(c, ""))
                if v is not None:
                    out.setdefault(k, {})[q] = out.setdefault(k, {}).get(q, D0) + v
        return out, names, regions
    qcol = mf.find_column(t, "quarter", "period", "fiscal_quarter")
    vcol = mf.find_column(t, "quota", "target", "amount")
    if not qcol or not vcol:
        raise InputError(f"{os.path.basename(t.path)} has neither quarter columns (such as 2026Q3) nor quarter and "
                         "quota columns. Add one quota column per quarter, named like 2026Q3.")
    for r in t.rows:
        k = r.get(rep, "").strip().lower()
        q = parse_quarter(r.get(qcol, ""))
        v = mf.to_decimal(r.get(vcol, ""))
        if not k or not q or v is None:
            continue
        names[k] = r[rep].strip()
        if region:
            regions[k] = r.get(region, "").strip()
        out.setdefault(k, {})[q] = out.setdefault(k, {}).get(q, D0) + v
    return out, names, regions


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Quota attainment by rep for a quarter.")
    ap.add_argument("deals", help="deals export: one row per deal")
    ap.add_argument("quotas", help="quotas: one row per rep with a column per quarter, or rep, quarter, quota")
    ap.add_argument("--quarter", help="the quarter, such as 2026Q3 (default: the last quarter with closed deals and quotas)")
    ap.add_argument("--history", action="store_true", help="add the last three quarters per rep and next quarter's coverage")
    ap.add_argument("--rep-column", help="the deals column with the rep")
    ap.add_argument("--amount-column", help="the deals column with the amount")
    ap.add_argument("--date-column", help="the deals column with the close date")
    ap.add_argument("--stage-column", help="the deals column with the stage")
    ap.add_argument("--quota-rep-column", help="the quotas column with the rep")
    a = ap.parse_args(argv)
    try:
        md, data = run(a)
    except InputError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    mf.emit(md, data, JSON_PATH)
    return 0


def run(a: argparse.Namespace) -> Tuple[str, dict]:
    deals = read(a.deals)
    qt = read(a.quotas)
    rep_c = column(deals, a.rep_column, "rep", "--rep-column", REP_COLS)
    amt_c = column(deals, a.amount_column, "amount", "--amount-column", AMOUNT_COLS)
    date_c = column(deals, a.date_column, "close date", "--date-column", DATE_COLS)
    stage_c = column(deals, a.stage_column, "stage", "--stage-column", STAGE_COLS, required=False)
    quotas, qnames, regions = load_quotas(qt, a.quota_rep_column)
    if not quotas:
        raise InputError(f"{os.path.basename(a.quotas)} holds no quotas it can read.")
    fs = mf.fiscal_start_month(mf.load_profile())

    won: Dict[str, Dict[Quarter, Decimal]] = {}
    pipe: Dict[str, Dict[Quarter, Decimal]] = {}
    names: Dict[str, str] = dict(qnames)
    counts: Dict[Quarter, int] = {}
    skipped = 0
    for r in deals.rows:
        k = r.get(rep_c, "").strip().lower()
        v = mf.to_decimal(r.get(amt_c, ""))
        d = mf.parse_date(r.get(date_c, ""))
        if not k or v is None or d is None:
            skipped += 1
            continue
        names.setdefault(k, r[rep_c].strip())
        q = quarter_of(d, fs)
        stage = r.get(stage_c, "").strip().lower() if stage_c else "won"
        if "lost" in stage:
            continue
        if "won" in stage or "closed" in stage or not stage_c:
            won.setdefault(k, {})[q] = won.setdefault(k, {}).get(q, D0) + v
            counts[q] = counts.get(q, 0) + 1
        else:
            pipe.setdefault(k, {})[q] = pipe.setdefault(k, {}).get(q, D0) + v
    if a.quarter:
        quarter = parse_quarter(a.quarter)
        if not quarter:
            raise InputError(f"--quarter {a.quarter} is not a quarter; write it like 2026Q3.")
    else:
        both = sorted(set(counts) & {q for v in quotas.values() for q in v})
        if not both:
            raise InputError("No quarter has both closed deals and quotas; name one with --quarter, like 2026Q3.")
        quarter = both[-1]
    if not any(quarter in v for v in quotas.values()):
        have = sorted({q for v in quotas.values() for q in v})
        raise InputError(f"{os.path.basename(a.quotas)} has no quota for {label(quarter)}; it holds "
                         f"{', '.join(label(q) for q in have)}.")

    reps = [k for k in quotas if quarter in quotas[k]]

    def att(k: str, q: Quarter) -> Optional[Decimal]:
        quota = quotas.get(k, {}).get(q)
        if not quota:
            return None
        return won.get(k, {}).get(q, D0) / quota

    rows = []
    for k in reps:
        b = won.get(k, {}).get(quarter, D0)
        quota = quotas[k][quarter]
        rows.append({"rep": names[k], "key": k, "region": regions.get(k, ""), "bookings": b, "quota": quota,
                     "attainment": b / quota if quota else None, "hit": b >= quota})
    rows.sort(key=lambda r: (-(r["attainment"] or D0), r["rep"]))
    team_b = sum((r["bookings"] for r in rows), D0)
    team_q = sum((r["quota"] for r in rows), D0)
    hit = [r for r in rows if r["hit"]]
    missed = sorted([r for r in rows if not r["hit"]], key=lambda r: (r["attainment"] or D0, r["rep"]))
    ql = label(quarter)
    out = [f"**{len(hit)} of {len(rows)} reps hit their {ql} quota. The team reached "
           f"{mf.pct(team_b / team_q, 0)} ({mf.money(team_b)} against {mf.money(team_q)}).**", ""]
    if missed:
        out.append(f"{'This rep' if len(missed) == 1 else f'These {len(missed)} reps'} missed:")
        out.append("")
        out.append(mf.md_table(["Rep", "Bookings", "Quota", "Attainment"],
                               [[r["rep"], mf.money(r["bookings"]), mf.money(r["quota"]), mf.pct(r["attainment"], 0)] for r in missed]))
        out.append("")
    has_region = any(r["region"] for r in rows)
    head = ["Rep"] + (["Region"] if has_region else []) + ["Bookings", "Quota", "Attainment", "Hit"]
    out += [f"## All reps, {ql}", ""]
    out.append(mf.md_table(head, [[r["rep"]] + ([r["region"]] if has_region else []) +
                                  [mf.money(r["bookings"]), mf.money(r["quota"]),
                                   mf.pct(r["attainment"], 0) if r["attainment"] is not None else "–",
                                   "yes" if r["hit"] else "no"] for r in rows],
                           align=["l"] * (1 + has_region) + ["r", "r", "r", "l"]))
    no_quota = {k: v[quarter] for k, v in won.items() if quarter in v and k not in reps}
    if no_quota:
        out += ["", "Bookings without a quota (left out of the team figure): " +
                ", ".join(f"{names[k]} {mf.money(v)}" for k, v in sorted(no_quota.items()))]
    if skipped:
        out += ["", f"Skipped {skipped} deal rows without a rep, an amount or a close date."]
    data = {"quarter": ql, "deals": os.path.abspath(a.deals), "quotas": os.path.abspath(a.quotas),
            "team": {"bookings": team_b, "quota": team_q, "attainment": team_b / team_q,
                     "display": {"bookings": mf.money(team_b), "quota": mf.money(team_q), "attainment": mf.pct(team_b / team_q, 0)}},
            "hit": len(hit), "reps": len(rows),
            "by_rep": [{**{k: v for k, v in r.items() if k != "key"},
                        "display": {"bookings": mf.money(r["bookings"]), "quota": mf.money(r["quota"]),
                                    "attainment": mf.pct(r["attainment"], 0) if r["attainment"] is not None else None}}
                       for r in rows],
            "missed": [r["rep"] for r in missed], "bookings_without_quota": no_quota}

    if a.history:
        qs = [shift(quarter, -2), shift(quarter, -1), quarter]
        out += ["", "## Attainment, last three quarters", ""]
        hist = []
        for r in sorted(rows, key=lambda r: r["rep"]):
            vals = [att(r["key"], q) for q in qs]
            hist.append({"rep": r["rep"], "attainment": {label(q): v for q, v in zip(qs, vals)},
                         "missed_all": all(v is not None and v < 1 for v in vals),
                         "falling": all(v is not None for v in vals) and vals[0] > vals[1] > vals[2]})
        hist.sort(key=lambda h: (not h["missed_all"], h["rep"]))
        out.append(mf.md_table(["Rep"] + [label(q) for q in qs],
                               [[h["rep"]] + [mf.pct(v, 0) if v is not None else "–" for v in h["attainment"].values()]
                                for h in hist]))
        streak = [h for h in hist if h["missed_all"]]
        out.append("")
        if streak:
            for h in streak:
                vals = ", ".join(f"{k} {mf.pct(v, 0)}" for k, v in h["attainment"].items())
                trend = "; each quarter is lower than the one before" if h["falling"] else ""
                out.append(f"{h['rep']} missed quota in all three quarters ({vals}){trend}.")
        else:
            out.append("No rep missed quota in all three quarters.")
        nq = shift(quarter, 1)
        nl = label(nq)
        cov = []
        for r in rows:
            p = pipe.get(r["key"], {}).get(nq, D0)
            quota = quotas.get(r["key"], {}).get(nq)
            cov.append({"rep": r["rep"], "key": r["key"], "pipeline": p, "quota": quota,
                        "coverage": (p / quota) if quota else None})
        out += ["", f"## {nl} pipeline against quota", ""]
        if not any(c["pipeline"] for c in cov):
            out.append(f"{os.path.basename(a.deals)} holds no open deals closing in {nl}.")
        else:
            cov.sort(key=lambda c: (c["coverage"] if c["coverage"] is not None else Decimal(10 ** 9), c["rep"]))
            tp = sum((c["pipeline"] for c in cov), D0)
            tq = sum((c["quota"] or D0 for c in cov), D0)
            trows = [[c["rep"], mf.money(c["pipeline"]), mf.money(c["quota"]) if c["quota"] else "–",
                      mf.multiple(c["coverage"]) if c["coverage"] is not None else "–"] for c in cov]
            trows.append(["Team", mf.money(tp), mf.money(tq), mf.multiple(tp / tq) if tq else "–"])
            out.append(mf.md_table(["Rep", "Open pipeline", f"{nl} quota", "Coverage"], trows))
            out.append("")
            for h in streak:
                c = next(x for x in cov if x["rep"] == h["rep"])
                rp = tp - c["pipeline"]
                rq = tq - (c["quota"] or D0)
                if c["coverage"] is not None and rq:
                    out.append(f"{c['rep']} has {mf.money(c['pipeline'])} of {nl} pipeline against a {mf.money(c['quota'])} "
                               f"quota ({mf.multiple(c['coverage'])} coverage); the rest of the team has "
                               f"{mf.multiple(rp / rq)} ({mf.money(rp)} against {mf.money(rq)}).")
            data["coverage"] = {"quarter": nl, "team_pipeline": tp, "team_quota": tq,
                                "by_rep": [{k: v for k, v in c.items() if k != "key"} for c in cov]}
        data["history"] = hist
    return "\n".join(out).rstrip(), data


if __name__ == "__main__":
    sys.exit(main())
