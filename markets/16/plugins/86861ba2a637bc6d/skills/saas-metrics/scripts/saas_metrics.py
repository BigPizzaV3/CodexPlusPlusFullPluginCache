#!/usr/bin/env python3
"""SaaS metrics: ARR movement, net and gross revenue retention and logo churn for a period.

Reads a subscription export in one of two shapes:

  snapshots  one row per customer and month: month, customer, ARR (or MRR), and optionally
             seats, renewal date, plan, currency. ARR on a day is the snapshot of the month
             that ends the day before (ARR on Jul 1 = the June snapshot).
  periods    one row per subscription version: customer, ARR (or MRR), start date and end
             date (empty while active; the last active day). Each change ends one row and
             starts the next. ARR on a day is the sum of the rows active the day before.

Each customer is compared between the start and the end of the period: new (no ARR at the
start), churn (no ARR at the end), expansion (more), contraction (less, still paying).

  python3 scripts/saas_metrics.py subscriptions.csv --from 2026-07-01 --to 2026-09-30
  python3 scripts/saas_metrics.py stripe_subs.csv --from 2026-07-01 --to 2026-09-30 --currency USD

Prints Markdown, writes metrics/<period>_saas_metrics.md (or --out) and
.magnos/runs/saas-metrics.json.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import shlex
import sys
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Dict, List, Optional, Sequence, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import magnos_fin as mf  # noqa: E402

D0 = Decimal(0)
JSON_PATH = os.path.join(".magnos", "runs", "saas-metrics.json")
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
LONG = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
        "November", "December"]


class InputError(Exception):
    """A problem with the person's file or flags: exit 2 with one plain sentence."""


@dataclass
class State:
    """One customer on one day."""
    arr: Decimal = D0
    seats: Optional[Decimal] = None
    renewal: Optional[dt.date] = None
    name: str = ""


@dataclass
class Book:
    path: str
    shape: str                       # snapshots or periods
    open_label: str                  # "Jun 30" (the day before the period starts)
    close_label: str                 # "Sep 30"
    opening: Dict[str, State] = field(default_factory=dict)
    closing: Dict[str, State] = field(default_factory=dict)
    notes: List[str] = field(default_factory=list)
    rows: int = 0
    open_source: str = ""
    close_source: str = ""


# ---------------------------------------------------------------- dates

def day(d: dt.date) -> str:
    return f"{MONTHS[d.month - 1]} {d.day}"


def full_day(d: dt.date) -> str:
    return f"{MONTHS[d.month - 1]} {d.day}, {d.year}"


def month_end(y: int, m: int) -> dt.date:
    return mf.month_end(dt.date(y, m, 1))


def parse_month(value: str) -> Optional[Tuple[int, int]]:
    s = str(value or "").strip()
    m = re.fullmatch(r"(\d{4})[-/.]?(?:M)?(\d{1,2})", s, re.I)
    if m and 1 <= int(m[2]) <= 12:
        return int(m[1]), int(m[2])
    d = mf.parse_date(s)
    return (d.year, d.month) if d else None


def period_label(start: dt.date, end: dt.date, fiscal_start: int) -> Tuple[str, str]:
    """("Q3 2026", "q3") for a quarter, ("September 2026", "2026-09") for a month, else dates."""
    q_end_month = (start.month + 1) % 12 + 1
    in_fy = (start.month - fiscal_start) % 12
    if (start.day == 1 and in_fy % 3 == 0 and end == mf.month_end(dt.date(end.year, end.month, 1))
            and end.month == q_end_month and (end - start).days < 95):
        q = in_fy // 3 + 1
        if fiscal_start == 1:
            return f"Q{q} {start.year}", f"q{q}"
        fy = start.year + (1 if start.month >= fiscal_start else 0)
        return f"Q{q} FY{fy}", f"fy{fy}_q{q}"
    if start.day == 1 and end == mf.month_end(start):
        return f"{LONG[start.month - 1]} {start.year}", f"{start.year}-{start.month:02d}"
    return f"{full_day(start)} to {full_day(end)}", f"{start.isoformat()}_{end.isoformat()}"


# ---------------------------------------------------------------- reading

def pick(table: mf.Table, override: Optional[str], *names: str) -> Optional[str]:
    if override:
        if override not in table.columns:
            raise InputError(f"{os.path.basename(table.path)} has no column named '{override}'; "
                             f"its columns are {', '.join(table.columns)}.")
        return override
    return mf.find_column(table, *names)


def load(path: str, start: dt.date, end: dt.date, args: argparse.Namespace) -> Book:
    if not os.path.exists(path):
        raise InputError(f"Cannot find {path}. Check the path, or run the command from the folder that holds it.")
    try:
        t = mf.read_table(path)
    except Exception as exc:
        raise InputError(f"Cannot read {os.path.basename(path)} ({exc.__class__.__name__}). Save it as CSV or XLSX.")
    name = os.path.basename(path)
    if not t.rows:
        raise InputError(f"{name} has no rows. Check that it is the subscription export.")
    cust_id = pick(t, args.customer_column, "customer_id", "account_id", "customer id", "account id", "subscriber_id")
    cust_name = mf.find_column(t, "customer", "customer_name", "account", "account_name", "company", "name")
    if cust_name == cust_id:
        cust_name = None
    key = cust_id or cust_name
    if not key:
        raise InputError(f"{name} has no customer column (looked for customer_id, customer, account). "
                         "Rename the column, or pass --customer-column NAME.")
    arr_col = pick(t, args.arr_column, "arr", "annual recurring revenue", "annualized", "acv")
    mrr_col = None if arr_col else mf.find_column(t, "mrr", "monthly recurring revenue")
    if not arr_col and not mrr_col:
        raise InputError(f"{name} has no ARR or MRR column (looked for arr, mrr). "
                         "Rename the column, or pass --arr-column NAME.")
    seats_col = mf.find_column(t, "seats", "licenses", "licences", "users", "quantity")
    renew_col = mf.find_column(t, "renewal_date", "renewal", "term_end", "contract_end", "renews")
    cur_col = mf.find_column(t, "currency", "ccy", "curr")
    start_col = mf.find_column(t, "start_date", "start", "effective_date", "service_start", "valid_from")
    end_col = mf.find_column(t, "end_date", "end", "cancel_date", "cancelled_at", "canceled_at", "service_end", "valid_to")
    month_col = pick(t, args.month_column, "month", "snapshot", "period", "as_of", "snapshot_date")

    rows = t.rows
    if cur_col:
        found = sorted({r.get(cur_col, "").strip().upper() for r in rows if r.get(cur_col, "").strip()})
        if args.currency:
            rows = [r for r in rows if r.get(cur_col, "").strip().upper() == args.currency.upper()]
            if not rows:
                raise InputError(f"{name} has no rows in {args.currency.upper()}; it holds {', '.join(found)}.")
        elif len(found) > 1:
            raise InputError(f"{name} mixes currencies ({', '.join(found)}). Convert to one currency first, "
                             f"or keep one with --currency {found[0]}.")

    def amount(r: dict) -> Decimal:
        v = mf.to_decimal(r.get(arr_col or mrr_col, ""))
        if v is None:
            return D0
        return v if arr_col else v * 12

    def state_add(states: Dict[str, State], r: dict) -> None:
        k = r.get(key, "").strip()
        if not k:
            return
        s = states.setdefault(k, State(name=(r.get(cust_name, "").strip() if cust_name else k) or k))
        s.arr += amount(r)
        if seats_col:
            v = mf.to_decimal(r.get(seats_col, ""))
            if v is not None:
                s.seats = (s.seats or D0) + v
        if renew_col:
            d = mf.parse_date(r.get(renew_col, ""))
            if d and (s.renewal is None or d > s.renewal):
                s.renewal = d

    open_day = start - dt.timedelta(days=1)
    b = Book(path, "", day(open_day), day(end), rows=len(t.rows))
    if mrr_col:
        b.notes.append(f"{name} gives MRR; ARR is MRR × 12.")
    if month_col and not (start_col and end_col and not args.month_column):
        b.shape = "snapshots"
        by_month: Dict[Tuple[int, int], List[dict]] = {}
        bad = 0
        for r in rows:
            k = parse_month(r.get(month_col, ""))
            if k is None:
                bad += 1
                continue
            by_month.setdefault(k, []).append(r)
        if not by_month:
            raise InputError(f"{name}: the {month_col} column holds no months it can read (use 2026-06 or 2026-06-30).")
        have = sorted(by_month)
        want_open, want_close = (open_day.year, open_day.month), (end.year, end.month)
        for want, what in ((want_open, f"ARR on {full_day(start)}"), (want_close, f"ARR on {full_day(end)}")):
            if want not in by_month:
                raise InputError(f"{name} has no {LONG[want[1] - 1]} {want[0]} snapshot, which {what} needs; "
                                 f"it holds {LONG[have[0][1] - 1]} {have[0][0]} to {LONG[have[-1][1] - 1]} {have[-1][0]}.")
        for r in by_month[want_open]:
            state_add(b.opening, r)
        for r in by_month[want_close]:
            state_add(b.closing, r)
        b.open_source = f"the {LONG[want_open[1] - 1]} {want_open[0]} snapshot"
        b.close_source = f"the {LONG[want_close[1] - 1]} {want_close[0]} snapshot"
        if open_day != month_end(*want_open):
            b.notes.append(f"ARR on {full_day(start)} is read from {b.open_source}, taken at the month end.")
        if end != month_end(*want_close):
            b.notes.append(f"ARR on {full_day(end)} is read from {b.close_source}, taken at the month end.")
        if bad:
            b.notes.append(f"Skipped {bad} rows whose {month_col} could not be read.")
    elif start_col:
        b.shape = "periods"
        for r in rows:
            s = mf.parse_date(r.get(start_col, ""))
            e = mf.parse_date(r.get(end_col, "")) if end_col else None
            if s is None:
                continue
            if s <= open_day and (e is None or e >= open_day):
                state_add(b.opening, r)
            if s <= end and (e is None or e >= end):
                state_add(b.closing, r)
        b.open_source = f"rows active on {full_day(open_day)}"
        b.close_source = f"rows active on {full_day(end)}"
    else:
        raise InputError(f"{name} needs either a month column (one row per customer and month) or a start_date "
                         "column (one row per subscription change). Add one, or pass --month-column NAME.")
    for states in (b.opening, b.closing):
        for k in [k for k, s in states.items() if s.arr <= 0]:
            del states[k]
    if not b.opening:
        raise InputError(f"{name} has no customer with ARR on {full_day(start)}; check --from.")
    return b


# ---------------------------------------------------------------- metrics

def metrics(b: Book) -> dict:
    keys = sorted(set(b.opening) | set(b.closing))
    moves: Dict[str, List[Tuple[str, Decimal]]] = {"new": [], "expansion": [], "contraction": [], "churn": []}
    for k in keys:
        o = b.opening[k].arr if k in b.opening else D0
        e = b.closing[k].arr if k in b.closing else D0
        if o == 0 and e > 0:
            moves["new"].append((k, e))
        elif o > 0 and e == 0:
            moves["churn"].append((k, o))
        elif e > o:
            moves["expansion"].append((k, e - o))
        elif e < o:
            moves["contraction"].append((k, o - e))
    tot = {m: sum((v for _, v in moves[m]), D0) for m in moves}
    start = sum((s.arr for s in b.opening.values()), D0)
    end = sum((s.arr for s in b.closing.values()), D0)
    assert start + tot["new"] + tot["expansion"] - tot["contraction"] - tot["churn"] == end
    retained = start + tot["expansion"] - tot["contraction"] - tot["churn"]
    return {"start": start, "end": end, "moves": moves, "totals": tot, "retained": retained,
            "nrr": retained / start, "grr": (start - tot["contraction"] - tot["churn"]) / start,
            "logo_churn": Decimal(len(moves["churn"])) / len(b.opening),
            "customers_start": len(b.opening), "customers_end": len(b.closing)}


# ---------------------------------------------------------------- the answer

def render(b: Book, r: dict, label: str, start: dt.date, end: dt.date, top: int) -> Tuple[str, dict]:
    tot = r["totals"]
    vals = [r["start"], r["end"]] + list(tot.values())
    big = max(abs(v) for v in vals) >= Decimal(1_000_000)
    dm = 1 if all(v % 100_000 == 0 for v in vals) else 2

    def m(x: Decimal, signed: bool = False) -> str:
        return mf.money(x, "M", decimals=dm, signed=signed) if big else mf.money(x, signed=signed)

    def n(x: Decimal) -> str:  # the bare number in the formulas, in the table's unit
        if big:
            return mf.num(x / Decimal(1_000_000), dm)
        return mf.num(x)

    unit = "$M" if big else "$"
    c = {k: len(v) for k, v in r["moves"].items()}
    on_start, on_end = f"on {day(start)}", f"on {day(end)}"
    change = r["end"] - r["start"]
    disp = {
        "start": m(r["start"]), "new": m(tot["new"], True), "expansion": m(tot["expansion"], True),
        "contraction": m(-tot["contraction"]), "churn": m(-tot["churn"]), "end": m(r["end"]),
        "change": m(abs(change)), "retained": m(r["retained"]),
        "nrr": mf.pct(r["nrr"]), "grr": mf.pct(r["grr"]), "logo_churn": mf.pct(r["logo_churn"]),
    }
    how = {
        "start": f"Sum of ARR of the {mf.num(r['customers_start'])} customers in {b.open_source}",
        "new": f"ARR {on_end} of the {c['new']} customers with no ARR {on_start}",
        "expansion": f"ARR added by the {c['expansion']} customers who pay more {on_end} than {on_start}",
        "contraction": f"ARR lost by the {c['contraction']} customers who pay less {on_end} and still pay",
        "churn": f"ARR {on_start} of the {c['churn']} customers with no ARR {on_end}",
        "end": f"{n(r['start'])} + {n(tot['new'])} + {n(tot['expansion'])} − {n(tot['contraction'])} − {n(tot['churn'])}",
        "nrr": f"({n(r['start'])} + {n(tot['expansion'])} − {n(tot['contraction'])} − {n(tot['churn'])}) ÷ {n(r['start'])}",
        "grr": f"({n(r['start'])} − {n(tot['contraction'])} − {n(tot['churn'])}) ÷ {n(r['start'])}",
        "logo_churn": f"{c['churn']} ÷ {mf.num(r['customers_start'])} customers active {on_start}",
    }
    rows = [
        (f"ARR {on_start}", "start"), ("New", "new"), ("Expansion", "expansion"), ("Contraction", "contraction"),
        ("Churn", "churn"), (f"ARR {on_end}", "end"), ("Net revenue retention", "nrr"),
        ("Gross revenue retention", "grr"), ("Logo churn", "logo_churn"),
    ]
    grew = "grew" if change >= 0 else "fell"
    out = [f"**ARR {grew} {disp['change']} in {label}, to {disp['end']}; net revenue retention was {disp['nrr']} "
           f"and gross revenue retention {disp['grr']}.**", ""]
    out.append(f"Customers active {on_start} pay {disp['retained']} {on_end}, against {disp['start']} {on_start}. "
               f"{c['churn']} of {mf.num(r['customers_start'])} customers left ({disp['logo_churn']} logo churn).")
    out.append("")
    out.append(mf.md_table([label, "Value", "How it is worked out"],
                           [[lab, disp[k], how[k]] for lab, k in rows], align=["l", "r", "l"]))
    out.append("")
    out.append(f"Amounts in the formulas are in {unit}. Source: {os.path.basename(b.path)}, "
               f"{b.open_source} and {b.close_source}.")

    # largest customers
    ranked = sorted(b.closing.items(), key=lambda kv: (-kv[1].arr, kv[0]))[:top]
    has_seats = any(s.seats is not None for s in b.closing.values())
    has_renew = any(s.renewal is not None for s in b.closing.values())
    head = ["Customer", f"ARR {on_end}", "Share of ARR"]
    if has_seats:
        head += [f"Seats {b.open_label}", f"Seats {b.close_label}"]
    if has_renew:
        head.append("Renews")
    trows, largest = [], []
    for k, s in ranked:
        o = b.opening.get(k)
        share = s.arr / r["end"]
        row = [s.name, mf.money(s.arr), mf.pct(share)]
        if has_seats:
            row += [mf.num(o.seats) if o and o.seats is not None else "–", mf.num(s.seats) if s.seats is not None else "–"]
        if has_renew:
            row.append(full_day(s.renewal) if s.renewal else "–")
        trows.append(row)
        largest.append({"customer_id": k, "customer": s.name, "arr": s.arr, "share": share,
                        "arr_start": o.arr if o else D0, "seats_start": o.seats if o else None, "seats_end": s.seats,
                        "renewal": s.renewal.isoformat() if s.renewal else None,
                        "display": {"arr": row[1], "share": row[2]}})
    out += ["", f"## Largest customers {on_end}", ""]
    out.append(mf.md_table(head, trows, align=["l"] + ["r"] * (len(head) - 1)))
    top_share = sum((s.arr for _, s in ranked), D0) / r["end"]
    out.append("")
    out.append(f"The largest customer holds {mf.pct(ranked[0][1].arr / r['end'])} of ARR {on_end}; "
               f"the top {len(ranked)} hold {mf.pct(top_share)}.")

    # customers to watch: large, renewing within six months, or with falling seats
    watch = []
    horizon = end + dt.timedelta(days=183)
    for k, s in ranked:
        share = s.arr / r["end"]
        o = b.opening.get(k)
        fell = (o is not None and o.seats and s.seats is not None and s.seats < o.seats * Decimal("0.9"))
        soon = s.renewal is not None and end < s.renewal <= horizon
        if share >= Decimal("0.05") and (soon or fell):
            without = r["end"] - s.arr
            watch.append({"customer": s.name, "share": share, "renewal": s.renewal, "seats_start": o.seats if o else None,
                          "seats_end": s.seats, "arr": s.arr, "arr_without": without})
    if watch:
        out += ["", "## Customers to watch", ""]
        wrows = []
        for w in watch:
            seats = (f"{mf.num(w['seats_start'])} → {mf.num(w['seats_end'])} "
                     f"({mf.pct((w['seats_end'] - w['seats_start']) / w['seats_start'], signed=True)})"
                     if w["seats_start"] and w["seats_end"] is not None else "–")
            below = "below" if w["arr_without"] < r["start"] else "above"
            wrows.append([w["customer"], mf.money(w["arr"]), mf.pct(w["share"]),
                          full_day(w["renewal"]) if w["renewal"] else "–", seats,
                          f"{mf.money(w['arr_without'])} ({below} {disp['start']} {on_start})"])
        out.append(mf.md_table(["Customer", "ARR", "Share of ARR", "Renews", f"Seats {b.open_label} → {b.close_label}",
                                f"ARR {on_end} without it"], wrows, align=["l", "r", "r", "r", "r", "r"]))
    if b.notes:
        out += ["", "Notes: " + " ".join(b.notes)]
    data = {"file": os.path.abspath(b.path), "shape": b.shape, "rows": b.rows, "period": label,
            "from": start.isoformat(), "to": end.isoformat(),
            "arr_start": r["start"], "arr_end": r["end"], "new": tot["new"], "expansion": tot["expansion"],
            "contraction": tot["contraction"], "churn": tot["churn"], "retained": r["retained"],
            "nrr": r["nrr"], "grr": r["grr"], "logo_churn": r["logo_churn"],
            "customers_start": r["customers_start"], "customers_end": r["customers_end"],
            "counts": c, "display": disp, "how": how, "largest": largest,
            "watch": [{**w, "renewal": w["renewal"].isoformat() if w["renewal"] else None} for w in watch],
            "movements": {k: [{"customer_id": cid, "customer": (b.closing.get(cid) or b.opening.get(cid)).name, "arr": v}
                              for cid, v in sorted(vs, key=lambda x: -x[1])] for k, vs in r["moves"].items()},
            "notes": b.notes}
    return "\n".join(out), data


DEFINITIONS = """## Definitions

- **ARR on a day**: the annual recurring revenue of every customer with a live subscription that day. With monthly snapshots, ARR on the first day of a month is the snapshot of the month before.
- **New**: ARR at the end of the period of customers with no ARR at its start.
- **Expansion**: the increase in ARR of customers who paid at the start and pay more at the end.
- **Contraction**: the decrease in ARR of customers who paid at the start and pay less, but still pay, at the end.
- **Churn**: ARR at the start of customers with no ARR at the end.
- **Net revenue retention**: ARR at the end from the customers active at the start, divided by ARR at the start.
- **Gross revenue retention**: the same, leaving expansion out.
- **Logo churn**: customers who left, divided by customers active at the start.
"""


def main(argv: Optional[Sequence[str]] = None) -> int:
    p = argparse.ArgumentParser(description="ARR movement, net and gross revenue retention and logo churn from a subscription export.")
    p.add_argument("file", help="the subscription export (CSV, TSV or XLSX)")
    p.add_argument("--from", dest="start", help="first day of the period (YYYY-MM-DD); default: the last full quarter in a snapshot file")
    p.add_argument("--to", dest="end", help="last day of the period (YYYY-MM-DD)")
    p.add_argument("--currency", help="keep only rows in this currency")
    p.add_argument("--top", type=int, default=10, help="how many of the largest customers to list (default 10)")
    p.add_argument("--out", help="where to write the summary (default metrics/<period>_saas_metrics.md)")
    p.add_argument("--customer-column", help="the column that identifies the customer")
    p.add_argument("--arr-column", help="the column with ARR")
    p.add_argument("--month-column", help="the column with the snapshot month")
    a = p.parse_args(argv)
    try:
        start, end = resolve_period(a)
        prof = mf.load_profile()
        label, slug = period_label(start, end, mf.fiscal_start_month(prof))
        book = load(a.file, start, end, a)
        r = metrics(book)
    except InputError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    md, data = render(book, r, label, start, end, max(1, a.top))
    out_path = a.out or os.path.join("metrics", f"{slug}_saas_metrics.md")
    cmd = "python3 scripts/saas_metrics.py " + " ".join(shlex.quote(x) for x in
                                                      [os.path.basename(a.file), "--from", start.isoformat(), "--to", end.isoformat()]
                                                      + (["--currency", a.currency] if a.currency else []))
    doc = (f"# SaaS metrics, {label}\n\n{md}\n\n{DEFINITIONS}\n## Re-run\n\nNext period, run the same script on the new "
           f"export with the new dates, from the folder that holds it:\n\n```\n{cmd}\n```\n")
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(doc)
    data["summary_file"] = out_path
    data["profile"] = prof.get("_source")
    mf.emit(md + f"\n\nWrote {out_path}.", data, JSON_PATH)
    return 0


def resolve_period(a: argparse.Namespace) -> Tuple[dt.date, dt.date]:
    start = mf.parse_date(a.start) if a.start else None
    end = mf.parse_date(a.end) if a.end else None
    if a.start and start is None:
        raise InputError(f"--from {a.start} is not a date; write it as YYYY-MM-DD.")
    if a.end and end is None:
        raise InputError(f"--to {a.end} is not a date; write it as YYYY-MM-DD.")
    if start is None or end is None:
        if not os.path.exists(a.file):
            raise InputError(f"Cannot find {a.file}. Check the path, or run the command from the folder that holds it.")
        t = mf.read_table(a.file)
        col = a.month_column or mf.find_column(t, "month", "snapshot", "period", "as_of")
        months = sorted({m for m in (parse_month(v) for v in t.col(col)) if m}) if col else []
        if not months:
            raise InputError("Give the period with --from and --to (YYYY-MM-DD).")
        y, m = months[-1]
        end = end or month_end(y, m)
        q_start = (end.month - 1) // 3 * 3 + 1
        start = start or dt.date(end.year, q_start, 1)
    if start > end:
        raise InputError(f"--from {start.isoformat()} is after --to {end.isoformat()}.")
    return start, end


if __name__ == "__main__":
    sys.exit(main())
