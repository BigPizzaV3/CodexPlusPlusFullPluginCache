#!/usr/bin/env python3
"""Data profile: what each exported file is, and where it can mislead, before any analysis.

Per file: rows, columns and their kinds, the grain (the key that makes a row unique), the
period covered and whether the last month is complete, entities, currencies, duplicate keys
and rows, empty values and the total of each numeric column. When the last month stops
early and the month before is in the file, it compares the same days of both months.

Across files: for each shared key, whether a join is one-to-one, one-to-many or
many-to-many, and how much a one-to-many join would count the "one" side's amounts twice,
by quarter and by entity.

  python3 scripts/profile.py gl_export_sep21.csv
  python3 scripts/profile.py deals.csv line_items.csv --as-of 2026-10-04

Prints Markdown and saves .magnos/runs/profile.json. Writes nothing else.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
from collections import Counter, OrderedDict
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any, Dict, List, Optional, Sequence, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import magnos_fin as mf  # noqa: E402

D0 = Decimal(0)
JSON_PATH = os.path.join(".magnos", "runs", "profile.json")
MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
LONG = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
        "November", "December"]
MONEY_WORDS = ["amount", "arr", "mrr", "revenue", "bookings", "value", "total", "balance", "debit", "credit",
               "net", "price", "cost", "quota", "acv", "tcv"]
ENTITY_COLS = ("entity", "legal entity", "company", "subsidiary", "region", "country", "business unit")
CURRENCY_COLS = ("currency", "currency code", "ccy", "curr")
CATEGORY_COLS = ("account type", "account_type", "type", "category", "account category", "class", "account class",
                 "fs line", "statement line")
ACCOUNT_COLS = ("account name", "account_name", "account description", "account", "gl account")


class InputError(Exception):
    """A problem with the person's files or flags: exit 2 with one plain sentence."""


# ---------------------------------------------------------------- small helpers

def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


def day(d: dt.date) -> str:
    return f"{MON[d.month - 1]} {d.day}, {d.year}"


def short_day(d: dt.date) -> str:
    return f"{MON[d.month - 1]} {d.day}"


def month_end(d: dt.date) -> dt.date:
    return mf.month_end(d)


def last_business_day(d: dt.date) -> dt.date:
    e = month_end(d)
    while e.weekday() >= 5:
        e -= dt.timedelta(days=1)
    return e


def quarter(d: dt.date, fiscal_start: int) -> Tuple[Tuple[int, int], str]:
    q = (d.month - fiscal_start) % 12 // 3 + 1
    if fiscal_start == 1:
        return (d.year, q), f"Q{q} {d.year}"
    fy = d.year + (1 if d.month >= fiscal_start else 0)
    return (fy, q), f"Q{q} FY{fy}"


def is_id_like(name: str) -> bool:
    n = norm(name)
    return n.endswith("id") or n in ("key", "entryno", "lineno", "documentno", "docno", "number", "invoiceno",
                                     "invoicenumber", "journalno") or n.endswith("number")


def count(n: int, one: str, many: Optional[str] = None) -> str:
    return f"{mf.num(n)} {one if n == 1 else (many or one + 's')}"


def is_rate_like(name: str) -> bool:
    """Per-unit numbers whose sum means nothing: prices, rates, percentages."""
    n = norm(name)
    return any(w in n for w in ("price", "rate", "pct", "percent", "margin", "ratio", "fx", "discount"))


def is_code_like(name: str) -> bool:
    """Numbers that label rather than measure: account codes, years, postcodes."""
    n = norm(name)
    return n in ("account", "accountno", "accountnumber", "accountcode", "glaccount", "code", "zip", "zipcode",
                 "postcode", "postalcode", "year", "fiscalyear", "month", "period", "quarter", "costcenter",
                 "costcentre", "department", "dept", "sic", "naics") or n.endswith("code")


def money_rank(name: str) -> Optional[int]:
    n = norm(name)
    for i, w in enumerate(MONEY_WORDS):
        if w in n:
            return i
    return None


def unit_for(values: Sequence[Decimal]) -> str:
    big = max((abs(v) for v in values), default=D0)
    return "M" if big >= Decimal(1_000_000) else ("K" if big >= Decimal(10_000) else "1")


def money_as(x: Decimal, unit: str, signed: bool = False, cur: str = "$") -> str:
    return mf.money(x, unit, decimals=2 if unit == "M" else 0, signed=signed, currency=cur)


SYMBOLS = {"USD": "$", "EUR": "€", "GBP": "£"}


# ---------------------------------------------------------------- one file

@dataclass
class Column:
    name: str
    kind: str
    empty: int
    distinct: int
    total: Optional[Decimal] = None
    first: Optional[dt.date] = None
    last: Optional[dt.date] = None
    decimals: int = 0
    money: bool = False
    low: Optional[Decimal] = None
    high: Optional[Decimal] = None


@dataclass
class FileProfile:
    path: str
    table: mf.Table
    columns: List[Column] = field(default_factory=list)
    grain: str = ""
    key: Optional[List[str]] = None
    duplicate_rows: int = 0
    duplicate_keys: Dict[str, Any] = field(default_factory=dict)
    date_col: Optional[str] = None
    dates: List[Optional[dt.date]] = field(default_factory=list)
    monthly: bool = False
    first: Optional[dt.date] = None
    last: Optional[dt.date] = None
    partial: Optional[dict] = None
    future: int = 0
    entity_col: Optional[str] = None
    entities: List[Tuple[str, int]] = field(default_factory=list)
    currency_col: Optional[str] = None
    currencies: List[Tuple[str, int]] = field(default_factory=list)
    symbols: Dict[str, List[str]] = field(default_factory=dict)
    amount_col: Optional[str] = None
    same_days: Optional[dict] = None
    months: List[dict] = field(default_factory=list)
    sheets: List[str] = field(default_factory=list)
    total_rows: List[str] = field(default_factory=list)
    heads_up: List[dict] = field(default_factory=list)

    @property
    def name(self) -> str:
        return os.path.basename(self.path)

    @property
    def symbol(self) -> str:
        if len(self.currencies) == 1:
            return SYMBOLS.get(self.currencies[0][0].upper(), "")
        return "$" if not self.currencies else ""


def skip_title_rows(t: mf.Table) -> mf.Table:
    """Exports often start with a title line ("Trial balance as of …"): use the first full row as the header."""
    for _ in range(5):
        auto = sum(1 for c in t.columns if re.fullmatch(r"col\d+", c))
        if auto * 2 < len(t.columns) or not t.rows:
            break
        first = t.rows[0]
        header: List[str] = []
        for i, c in enumerate(t.columns):
            h = str(first.get(c, "")).strip() or f"col{i + 1}"
            while h in header:
                h += "_"
            header.append(h)
        rows = [{h: r.get(c, "") for h, c in zip(header, t.columns)} for r in t.rows[1:]]
        t = mf.Table(header, rows, t.path, t.sheet)
    return t


def read(path: str) -> Tuple[mf.Table, List[str]]:
    if not os.path.exists(path):
        raise InputError(f"Cannot find {path}. Check the path, or run the command from the folder that holds it.")
    if os.path.isdir(path):
        raise InputError(f"{path} is a folder. Name the exported files inside it.")
    if not path.lower().endswith((".csv", ".tsv", ".txt", ".xlsx", ".xlsm")):
        raise InputError(f"{os.path.basename(path)} is not a CSV, TSV or XLSX file. Export it as one of those.")
    try:
        t = mf.read_table(path)
        sheets = mf.read_xlsx(path).sheet_names if path.lower().endswith((".xlsx", ".xlsm")) else []
    except Exception as exc:
        raise InputError(f"Cannot read {os.path.basename(path)} ({exc.__class__.__name__}). Save it as CSV or XLSX and try again.")
    if not t.columns:
        raise InputError(f"{os.path.basename(path)} is empty. Check that it is the right export.")
    return skip_title_rows(t), sheets


def profile_file(path: str, as_of: dt.date, fiscal_start: int) -> FileProfile:
    t, sheets = read(path)
    p = FileProfile(path, t, sheets=sheets)
    rows = t.rows
    # columns
    for c in t.columns:
        vals = t.col(c)
        kind = t.kind(c)
        col = Column(c, kind, sum(1 for v in vals if not str(v).strip()), len({v for v in vals if str(v).strip()}))
        if kind == "number" and (is_code_like(c) or is_id_like(c)):
            col.kind = "code"
        elif kind == "number":
            nums = [mf.to_decimal(v) for v in vals]
            if is_rate_like(c):
                ok = [v for v in nums if v is not None]
                col.low, col.high = (min(ok), max(ok)) if ok else (None, None)
            else:
                col.total = sum((v for v in nums if v is not None), D0)
            col.decimals = max((max(0, -v.as_tuple().exponent) for v in nums if v is not None), default=0)
            col.money = money_rank(c) is not None and not is_id_like(c)
            sy = sorted({ch for v in vals for ch in str(v) if ch in "$€£"})
            if sy:
                p.symbols[c] = sy
        elif kind == "date":
            ds = [d for d in (mf.parse_date(v) for v in vals) if d]
            col.first, col.last = (min(ds), max(ds)) if ds else (None, None)
        p.columns.append(col)
    cols = {c.name: c for c in p.columns}
    # duplicate rows, then the grain of the rows that remain
    seen: Dict[Tuple, int] = {}
    for r in rows:
        k = tuple(r.get(c, "") for c in t.columns)
        seen[k] = seen.get(k, 0) + 1
    p.duplicate_rows = sum(v - 1 for v in seen.values() if v > 1)
    uniq = [dict(zip(t.columns, k)) for k in seen]
    n = len(uniq)
    ids = [c for c in t.columns if is_id_like(c) and cols[c].empty == 0]
    dates = [c for c in t.columns if cols[c].kind == "date"]
    for c in ids:
        if len({r.get(c, "") for r in uniq}) == n:
            p.key, p.grain = [c], f"one row per {c}"
            break
    if not p.key:
        for c in ids:
            for d in dates:
                if len({(r.get(d, ""), r.get(c, "")) for r in uniq}) == n:
                    p.key, p.grain = [d, c], f"one row per {d} and {c}"
                    break
            if p.key:
                break
    if not p.key:
        for c in t.columns:
            if cols[c].kind == "text" and cols[c].empty == 0 and len({r.get(c, "") for r in uniq}) == n and n > 1:
                p.key, p.grain = [c], f"one row per {c}"
                break
    if not p.key:
        p.grain = "no column identifies a row"
        if ids:
            cnt = Counter(r.get(ids[0], "") for r in uniq)
            dup = {k: v for k, v in cnt.items() if v > 1}
            p.duplicate_keys = {"column": ids[0], "values": len(dup), "rows": sum(dup.values()),
                                "examples": sorted(dup)[:5]}
    if p.key and p.duplicate_rows:
        p.grain += f" once {count(p.duplicate_rows, 'exact duplicate row')} {'is' if p.duplicate_rows == 1 else 'are'} removed"
    # total rows inside the data: a column total counts them twice
    label_col = next((c for c in t.columns if cols[c].kind == "text"), None)
    if label_col:
        p.total_rows = [r.get(label_col, "").strip() for r in rows
                        if re.match(r"^(grand\s+)?(sub)?total\b", r.get(label_col, "").strip(), re.I)]
    # dates and the period
    if dates:
        ranked = sorted(dates, key=lambda c: (0 if re.search(r"month|period|snapshot", c, re.I) else
                                              1 if re.search(r"post|close|date|day|booked", c, re.I) else 2,
                                              t.columns.index(c)))
        p.date_col = ranked[0]
        raw = t.col(p.date_col)
        p.dates = [mf.parse_date(v) for v in raw]
        ds = [d for d in p.dates if d]
        if ds:
            p.first, p.last = min(ds), max(ds)
            p.monthly = all(d.day == 1 for d in ds) or all(re.fullmatch(r"\s*\d{4}-\d{1,2}\s*|\s*[A-Za-z]{3,9}\.? \d{4}\s*", v)
                                                            for v in raw if str(v).strip())
            p.future = sum(1 for d in ds if d > as_of)
            if not p.monthly:
                lb = last_business_day(p.last)
                if p.last < lb:
                    p.partial = {"month": LONG[p.last.month - 1] + f" {p.last.year}", "month_name": LONG[p.last.month - 1],
                                 "last": p.last.isoformat(), "days": p.last.day, "days_in_month": month_end(p.last).day,
                                 "last_business_day": lb.isoformat()}
    # entities and currencies
    for cand in ENTITY_COLS:
        c = mf.find_column(t, cand)
        if c and cols[c].kind == "text" and 1 <= cols[c].distinct <= 20 and c not in (p.key or []):
            p.entity_col = c
            p.entities = Counter(r.get(c, "").strip() for r in rows if r.get(c, "").strip()).most_common()
            break
    c = mf.find_column(t, *CURRENCY_COLS)
    if c and cols[c].kind == "text":
        p.currency_col = c
        p.currencies = Counter(r.get(c, "").strip().upper() for r in rows if r.get(c, "").strip()).most_common()
    money_cols = [x for x in p.columns if x.kind == "number" and x.money]
    if money_cols:
        p.amount_col = sorted(money_cols, key=lambda x: (money_rank(x.name), t.columns.index(x.name)))[0].name
    # by month
    if p.date_col and p.first:
        by: "OrderedDict[Tuple[int, int], dict]" = OrderedDict()
        for r, d in zip(rows, p.dates):
            if not d:
                continue
            m = by.setdefault((d.year, d.month), {"rows": 0, "amount": D0, "days": set()})
            m["rows"] += 1
            m["days"].add(d.day)
            if p.amount_col:
                v = mf.to_decimal(r.get(p.amount_col, ""))
                if v is not None:
                    m["amount"] += v
        for (y, mo), m in sorted(by.items()):
            last_d = dt.date(y, mo, max(m["days"]))
            p.months.append({"month": f"{MON[mo - 1]} {y}", "key": f"{y}-{mo:02d}", "rows": m["rows"],
                             "amount": m["amount"], "last": last_d.isoformat()})
    if p.partial:
        p.same_days = same_days(p)
    # heads up
    if p.partial:
        pt = p.partial
        p.heads_up.append({"kind": "partial_period", "file": p.name,
                           "title": f"{pt['month_name']} stops on {short_day(p.last)}",
                           "text": f"{p.name} ends on {day(p.last)}, so {pt['month_name']} has {pt['days']} of its "
                                   f"{pt['days_in_month']} days."})
    if len(p.currencies) > 1:
        p.heads_up.append({"kind": "mixed_currency", "file": p.name, "title": f"{p.name} mixes currencies",
                           "text": f"{p.currency_col} holds " + ", ".join(f"{k} ({count(v, 'row')})" for k, v in p.currencies)
                                   + "; a total adds them as if they were one currency."})
    for col_name, sy in p.symbols.items():
        if len(sy) > 1:
            p.heads_up.append({"kind": "mixed_currency", "file": p.name, "title": f"{col_name} mixes currency symbols",
                               "text": f"{col_name} in {p.name} has amounts in {' and '.join(sy)}; a total adds them as one currency."})
    if p.duplicate_rows:
        p.heads_up.append({"kind": "duplicates", "file": p.name, "title": f"{p.name} has duplicate rows",
                           "text": f"{count(p.duplicate_rows, 'row')} of {p.name} "
                                   f"{'is an exact copy' if p.duplicate_rows == 1 else 'are exact copies'} of another row; "
                                   f"a total counts {'it' if p.duplicate_rows == 1 else 'them'} twice."})
    if p.total_rows:
        p.heads_up.append({"kind": "total_rows", "file": p.name, "title": f"{p.name} holds its own total rows",
                           "text": f"{count(len(p.total_rows), 'row')} of {p.name} "
                                   f"({', '.join(sorted(set(p.total_rows)))}) {'is a total' if len(p.total_rows) == 1 else 'are totals'}; "
                                   "summing a column counts those amounts twice."})
    if p.duplicate_keys.get("values"):
        dk = p.duplicate_keys
        p.heads_up.append({"kind": "duplicates", "file": p.name, "title": f"{dk['column']} repeats in {p.name}",
                           "text": f"{count(dk['values'], 'value')} of {dk['column']} "
                                   f"{'appears' if dk['values'] == 1 else 'appear'} on more than one row "
                                   f"({count(dk['rows'], 'row')}, with different values elsewhere), so {dk['column']} does not identify a row."})
    return p


def same_days(p: FileProfile) -> Optional[dict]:
    """The partial last month against the same days, and all, of the month before."""
    t = p.table
    cur = p.last
    prev_end = cur.replace(day=1) - dt.timedelta(days=1)
    prev_start = prev_end.replace(day=1)
    if not p.first or p.first > prev_start + dt.timedelta(days=3):
        return None
    cut = cur.day
    if not p.amount_col:
        return None
    cat = None
    for cand in CATEGORY_COLS:
        c = mf.find_column(t, cand)
        if c and t.kind(c) == "text" and 2 <= len({v for v in t.col(c) if v.strip()}) <= 15:
            cat = c
            break
    acct = mf.find_column(t, *ACCOUNT_COLS)
    windows = {"cur": (cur.replace(day=1), cur), "prev_same": (prev_start, prev_start.replace(day=min(cut, prev_end.day))),
               "prev": (prev_start, prev_end)}
    sums: Dict[str, Dict[str, Decimal]] = {w: {} for w in windows}
    late: Dict[str, List[Decimal]] = {}
    for r, d in zip(t.rows, p.dates):
        if not d:
            continue
        v = mf.to_decimal(r.get(p.amount_col, ""))
        if v is None:
            continue
        g = r.get(cat, "").strip() if cat else "All rows"
        for w, (lo, hi) in windows.items():
            if lo <= d <= hi:
                sums[w][g] = sums[w].get(g, D0) + v
        if acct and prev_start <= d <= prev_end:
            bucket = late.setdefault(r.get(acct, "").strip(), [D0, D0])
            bucket[1 if d.day > cut else 0] += v
    groups = list(OrderedDict.fromkeys([g for w in ("prev", "cur") for g in sums[w]]))
    order = {g: i for i, g in enumerate(groups)}

    def is_rev(g: str) -> bool:
        n = g.lower().strip()
        if any(w in n for w in ("cost", "expense", "marketing")):
            return False
        return "revenue" in n or n in ("sales", "net sales", "income", "turnover", "other income")

    def is_cogs(g: str) -> bool:
        n = g.lower()
        return any(w in n for w in ("cost of revenue", "cost of sales", "cost of goods", "cogs", "direct cost"))

    groups.sort(key=lambda g: (0 if is_rev(g) else 1 if is_cogs(g) else 2, order[g]))
    flip = {g: sums["prev"].get(g, sums["cur"].get(g, D0)) < 0 for g in groups}
    shown = {w: {g: (-sums[w].get(g, D0) if flip[g] else sums[w].get(g, D0)) for g in groups} for w in windows}
    rows = [{"group": g, **{w: shown[w][g] for w in windows}} for g in groups]
    margin = None
    rev = [g for g in groups if is_rev(g)]
    cogs = [g for g in groups if is_cogs(g)]
    if rev and cogs:
        margin = {}
        for w in windows:
            rv = sum((shown[w][g] for g in rev), D0)
            cg = sum((shown[w][g] for g in cogs), D0)
            margin[w] = None if rv == 0 else (rv - cg) / rv
    late_accounts = []
    days_after = prev_end.day - cut
    bar = max(Decimal("0.6"), Decimal(days_after) / prev_end.day * Decimal("1.5"))
    month_abs = sum((abs(x) + abs(y) for x, y in late.values()), D0)
    for name, (before, after) in late.items():
        tot = before + after
        if tot == 0 or month_abs == 0 or abs(tot) < month_abs * Decimal("0.005"):
            continue
        share = after / tot
        if share >= bar:
            late_accounts.append({"account": name, "share_after": share, "before": before, "after": after})
    late_accounts.sort(key=lambda x: -abs(x["before"] + x["after"]))
    combined = None
    if late_accounts:
        early = sum((x["before"] for x in late_accounts), D0)
        later = sum((x["after"] for x in late_accounts), D0)
        combined = later / (early + later)
    return {"category": cat, "cut_day": cut, "rows": rows, "margin": margin, "margin_after": len(rev) + len(cogs),
            "flipped": [g for g in groups if flip[g]],
            "windows": {w: [lo.isoformat(), hi.isoformat()] for w, (lo, hi) in windows.items()},
            "labels": {"cur": f"{MON[cur.month - 1]} 1–{cut}", "prev_same": f"{MON[prev_start.month - 1]} 1–{cut}",
                       "prev": LONG[prev_start.month - 1]},
            "late_accounts": late_accounts, "late_combined": combined, "account_col": acct,
            "prev_month": LONG[prev_start.month - 1], "prev_month_short": MON[prev_start.month - 1]}


# ---------------------------------------------------------------- across files

def joins(files: List[FileProfile], fiscal_start: int) -> Tuple[List[dict], List[dict]]:
    out, heads = [], []
    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            a, b = files[i], files[j]
            shared = [(ca, cb) for ca in a.table.columns for cb in b.table.columns if norm(ca) == norm(cb)]
            for ca, cb in shared:
                va = [r.get(ca, "").strip() for r in a.table.rows if r.get(ca, "").strip()]
                vb = [r.get(cb, "").strip() for r in b.table.rows if r.get(cb, "").strip()]
                if not va or not vb:
                    continue
                ua, ub = len(set(va)) == len(va), len(set(vb)) == len(vb)
                kind_a = a.table.kind(ca)
                if not (is_id_like(ca) or (kind_a == "text" and (ua or ub))):
                    continue
                common = set(va) & set(vb)
                if not common:
                    continue
                if ua and ub:
                    out.append({"files": [a.name, b.name], "key": ca, "kind": "one-to-one", "matched": len(common)})
                    continue
                if not ua and not ub:
                    if is_id_like(ca):
                        ca_cnt, cb_cnt = Counter(va), Counter(vb)
                        rows = sum(ca_cnt[k] * cb_cnt[k] for k in common)
                        j_ = {"files": [a.name, b.name], "key": ca, "kind": "many-to-many", "matched": len(common),
                              "join_rows": rows}
                        out.append(j_)
                        heads.append({"kind": "many_to_many", "title": f"{a.name} and {b.name} both repeat {ca}",
                                      "text": f"Joining them on {ca} gives {mf.num(rows)} rows: every repeat on one side "
                                              f"multiplies the rows of the other."})
                    continue
                one, many, k1, k2 = (a, b, ca, cb) if ua else (b, a, cb, ca)
                j_ = one_to_many(one, many, k1, k2, fiscal_start)
                out.append(j_)
                if j_.get("over_total"):
                    heads.append(j_["heads_up"])
    return out, heads


def one_to_many(one: FileProfile, many: FileProfile, k1: str, k2: str, fiscal_start: int) -> dict:
    cnt = Counter(r.get(k2, "").strip() for r in many.table.rows if r.get(k2, "").strip())
    one_keys = {r.get(k1, "").strip() for r in one.table.rows}
    matched = [r for r in one.table.rows if r.get(k1, "").strip() in cnt]
    repeated = [r for r in matched if cnt[r[k1].strip()] > 1]
    res: Dict[str, Any] = {"files": [one.name, many.name], "key": k1, "kind": "one-to-many", "one": one.name,
                           "many": many.name, "one_rows": len(one.table.rows), "many_rows": len(many.table.rows),
                           "matched": len(matched), "repeated": len(repeated),
                           "max_per_key": max(cnt.values()) if cnt else 0,
                           "one_unmatched": len(one.table.rows) - len(matched),
                           "many_unmatched": sum(v for k, v in cnt.items() if k not in one_keys)}
    amt = one.amount_col
    if not amt:
        return res
    sym = one.symbol or "$"
    before = after = D0
    groups: "OrderedDict[Tuple, dict]" = OrderedDict()
    ent_groups: Dict[Tuple, Dict[str, dict]] = {}
    dates = dict(zip(map(id, one.table.rows), one.dates)) if one.date_col else {}
    for r in matched:
        v = mf.to_decimal(r.get(amt, "")) or D0
        n = cnt[r[k1].strip()]
        before += v
        after += v * n
        d = dates.get(id(r))
        qk, ql = quarter(d, fiscal_start) if d else ((9999, 9), "No date")
        g = groups.setdefault(qk, {"label": ql, "rows": 0, "repeated": 0, "before": D0, "after": D0})
        g["rows"] += 1
        g["repeated"] += 1 if n > 1 else 0
        g["before"] += v
        g["after"] += v * n
        if one.entity_col:
            e = r.get(one.entity_col, "").strip() or "(blank)"
            eg = ent_groups.setdefault(qk, {}).setdefault(e, {"rows": 0, "before": D0, "after": D0})
            eg["rows"] += 1
            eg["before"] += v
            eg["after"] += v * n
    res.update({"amount": amt, "before": before, "after": after, "over_total": after - before})
    qrows = [dict(g, over=g["after"] - g["before"], key=k) for k, g in sorted(groups.items())]
    res["by_quarter"] = [{**q, "key": list(q["key"])} for q in qrows]
    hit = [q for q in qrows if q["over"] != 0]
    res["by_entity"] = []
    if one.entity_col:
        for q in hit:
            for e, eg in sorted(ent_groups.get(q["key"], {}).items(), key=lambda kv: -kv[1]["after"]):
                res["by_entity"].append({"quarter": q["label"], "entity": e, **eg, "over": eg["after"] - eg["before"]})
    # a column on the many side that adds up to the same amount
    matched_keys = {x[k1].strip() for x in matched}
    for c in many.columns:
        if c.kind == "number" and c.money and c.name != k2:
            tot = sum((mf.to_decimal(r.get(c.name, "")) or D0 for r in many.table.rows
                       if r.get(k2, "").strip() in matched_keys), D0)
            if tot == before:
                res["use_instead"] = c.name
                break
    if res["over_total"]:
        u = unit_for([before, after])
        text = (f"{one.name} has one row per {k1}; {many.name} has up to {res['max_per_key']} rows per {k1}. "
                f"Joining them repeats {mf.num(len(repeated))} {k1} values, and summing {amt} after the join gives "
                f"{money_as(after, u, cur=sym)} instead of {money_as(before, u, cur=sym)} "
                f"({money_as(after - before, u, signed=True, cur=sym)}).")
        if len(hit) == 1 and hit[0]["label"] != "No date":
            q = hit[0]
            uq = unit_for([q["before"], q["after"]])
            text += (f" All of it falls in {q['label']}: {money_as(q['after'], uq, cur=sym)} instead of "
                     f"{money_as(q['before'], uq, cur=sym)}.")
        noun = re.sub(r"[\s_-]*(id|key|no|number|code)$", "", k1, flags=re.I).strip(" _-")
        what = f"{noun}s" if noun else f"rows of {one.name}"
        res["heads_up"] = {"kind": "one_to_many", "title": f"The join counts {mf.num(len(repeated))} {what} more than once",
                           "text": text}
    return res


# ---------------------------------------------------------------- the answer

def fmt_total(c: Column, sym: str) -> str:
    if c.total is None:
        return ""
    d = min(c.decimals, 2)
    if c.money:
        return mf.money(c.total, "1", decimals=d, currency=sym or "")
    return mf.num(c.total, d)


def render_file(p: FileProfile) -> List[str]:
    t = p.table
    sym = p.symbol
    out = [f"## {p.name}", ""]
    facts = [["Rows", mf.num(len(t.rows))], ["Columns", mf.num(len(t.columns))], ["Grain", p.grain]]
    if p.sheets and len(p.sheets) > 1:
        facts.append(["Sheets", f"read {p.sheets[0]}; also holds {', '.join(p.sheets[1:])}"])
    if p.date_col and p.first:
        span = f"{p.date_col}: {p.months[0]['month']} to {p.months[-1]['month']}, monthly" if p.monthly else \
            f"{p.date_col}: {day(p.first)} to {day(p.last)}"
        facts.append(["Period", span])
        if p.monthly:
            facts.append(["Last period", f"{p.months[-1]['month']} (monthly rows; no days to check)"])
        elif p.partial:
            pt = p.partial
            facts.append(["Last period", f"incomplete: {pt['month_name']} has {pt['days']} of its {pt['days_in_month']} days "
                                         f"(the month's last business day is {short_day(dt.date.fromisoformat(pt['last_business_day']))})"])
        else:
            facts.append(["Last period", f"{LONG[p.last.month - 1]} {p.last.year} is complete"])
        if p.future:
            facts.append(["Future dates", f"{mf.num(p.future)} rows are dated after {day(AS_OF[0])}"])
    else:
        facts.append(["Period", "no date column"])
    if p.entity_col:
        facts.append(["Entities", f"{p.entity_col}: " + ", ".join(f"{k} ({count(v, 'row')})" for k, v in p.entities)])
    if p.currency_col:
        cur_tot: Dict[str, Decimal] = {}
        if p.amount_col and len(p.currencies) > 1:
            for r in t.rows:
                v = mf.to_decimal(r.get(p.amount_col, ""))
                if v is not None:
                    k = r.get(p.currency_col, "").strip().upper()
                    cur_tot[k] = cur_tot.get(k, D0) + v
        facts.append(["Currencies", ", ".join(
            f"{k} ({count(v, 'row')}" + (f", {p.amount_col} {mf.num(cur_tot.get(k, D0), min(2, next(c.decimals for c in p.columns if c.name == p.amount_col)))})" if cur_tot else ")")
            for k, v in p.currencies)])
    elif p.symbols:
        facts.append(["Currencies", "symbols in amounts: " + ", ".join(sorted({s for v in p.symbols.values() for s in v}))])
    else:
        facts.append(["Currencies", "no currency column"])
    dups = []
    if p.duplicate_rows:
        dups.append(count(p.duplicate_rows, "exact duplicate row"))
    if p.duplicate_keys.get("values"):
        dk = p.duplicate_keys
        dups.append(f"{dk['column']}: {count(dk['values'], 'value')} repeat ({count(dk['rows'], 'row')})")
    facts.append(["Duplicates", "; ".join(dups) if dups else "none"])
    if p.total_rows:
        facts.append(["Total rows", f"{count(len(p.total_rows), 'row')}: {', '.join(sorted(set(p.total_rows)))}"])
    empties = [f"{c.name} {mf.num(c.empty)}" for c in p.columns if c.empty]
    facts.append(["Empty values", ", ".join(empties) if empties else "none"])
    out.append(mf.md_table(["", p.name], facts, align=["l", "l"]))
    out += ["", mf.md_table(["Column", "Kind", "Empty", "Distinct", "Total or range"], [
        [c.name, c.kind, mf.num(c.empty), mf.num(c.distinct),
         fmt_total(c, sym) if c.total is not None else
         (f"{mf.num(c.low, min(c.decimals, 2))} to {mf.num(c.high, min(c.decimals, 2))}" if c.low is not None else
          (f"{c.first.isoformat()} to {c.last.isoformat()}" if c.first else ""))]
        for c in p.columns], align=["l", "l", "r", "r", "r"])]
    if p.months and len(p.months) <= 13 and p.date_col:
        head = ["Month", "Rows", "Last date"] + ([f"{p.amount_col}"] if p.amount_col else [])
        rows = [[m["month"], mf.num(m["rows"]), m["last"]] + ([mf.money(m["amount"], "1", decimals=0, currency=sym or "")]
                                                             if p.amount_col else []) for m in p.months]
        out += ["", mf.md_table(head, rows, align=["l", "r", "r", "r"])]
    sd = p.same_days
    if sd:
        lab = sd["labels"]
        out += ["", f"### {lab['cur']} against the same days of {sd['prev_month']}", ""]
        rows = []
        for r in sd["rows"]:
            rows.append([r["group"]] + [mf.money(r[w], "1", decimals=0, currency=sym or "") for w in ("cur", "prev_same", "prev")])
        if sd["margin"]:
            m = sd["margin"]
            rows.insert(sd["margin_after"],
                        ["Gross margin"] + [mf.pct(m[w]) if m[w] is not None else "–" for w in ("cur", "prev_same", "prev")])
        out.append(mf.md_table([sd["category"] or "", lab["cur"], lab["prev_same"], lab["prev"]], rows))
        if sd["flipped"]:
            out += ["", f"{', '.join(sd['flipped'])} shown as positive amounts; {p.name} signs them negative."]
        if sd["late_accounts"]:
            la = sd["late_accounts"]
            names = " and ".join([", ".join(x["account"] for x in la[:-1]), la[-1]["account"]] if len(la) > 1 else [la[0]["account"]])
            each = ""
            if len(la) > 1:
                each = " (" + ", ".join(x["account"] + " " + mf.pct(x["share_after"], 0) for x in la) + ")"
            out += ["", f"Posted late: in {sd['prev_month']}, {mf.pct(sd['late_combined'], 0)} of {names} "
                        f"posted after {sd['prev_month_short']} {sd['cut_day']}{each}."]
    out.append("")
    return out


def render_join(j: dict, files: Dict[str, FileProfile]) -> List[str]:
    if j["kind"] == "one-to-one":
        return [f"- {j['files'][0]} and {j['files'][1]} join one-to-one on {j['key']} ({mf.num(j['matched'])} keys match)."]
    if j["kind"] == "many-to-many":
        return [f"- **{j['files'][0]} and {j['files'][1]} both repeat {j['key']}**: a join gives {mf.num(j['join_rows'])} rows."]
    one = files[j["one"]]
    sym = one.symbol or "$"
    out = [f"- **{j['one']} → {j['many']} is one-to-many on {j['key']}**: {mf.num(j['matched'])} of "
           f"{mf.num(j['one_rows'])} rows of {j['one']} match; {mf.num(j['repeated'])} of them have 2 or more rows in "
           f"{j['many']} (up to {j['max_per_key']})."]
    if j["one_unmatched"] or j["many_unmatched"]:
        out.append(f"  {mf.num(j['one_unmatched'])} rows of {j['one']} have no match; "
                   f"{mf.num(j['many_unmatched'])} rows of {j['many']} have no match.")
    if j.get("over_total"):
        u = unit_for([j["before"], j["after"]])
        out.append(f"  Summing {j['amount']} after the join gives {money_as(j['after'], u, cur=sym)} instead of "
                   f"{money_as(j['before'], u, cur=sym)} ({money_as(j['over_total'], u, signed=True, cur=sym)}).")
        hit = [q for q in j["by_quarter"] if q["over"] != 0]
        u = unit_for([q["after"] for q in hit])
        out += ["", mf.md_table(["Quarter", f"Rows of {j['one']}", "Repeated", f"{j['amount']} on {j['one']}",
                                 "After the join", "Overstated"],
                                [[q["label"], mf.num(q["rows"]), mf.num(q["repeated"]), money_as(q["before"], u, cur=sym),
                                  money_as(q["after"], u, cur=sym), money_as(q["over"], u, signed=True, cur=sym)] for q in hit])]
        if j["by_entity"]:
            u = unit_for([e["after"] for e in j["by_entity"]])
            out += ["", mf.md_table(["Quarter", one.entity_col, f"Rows of {j['one']}", f"{j['amount']} on {j['one']}",
                                     "After the join", "Overstated"],
                                    [[e["quarter"], e["entity"], mf.num(e["rows"]), money_as(e["before"], u, cur=sym),
                                      money_as(e["after"], u, cur=sym), money_as(e["over"], u, signed=True, cur=sym)]
                                     for e in j["by_entity"]], align=["l", "l", "r", "r", "r", "r"])]
        fix = f"Sum {j['amount']} on {j['one']} before the join"
        if j.get("use_instead"):
            fix += f", or sum {j['use_instead']} from {j['many']}, which adds up to the same {money_as(j['before'], unit_for([j['before']]), cur=sym)}"
        out += ["", fix + "."]
    return out


AS_OF: List[dt.date] = [dt.date.today()]


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Profile exported files before analysis: grain, period, completeness, "
                                             "entities, currencies, duplicates, totals, and joins across files.")
    ap.add_argument("files", nargs="+", help="CSV, TSV or XLSX exports")
    ap.add_argument("--as-of", help="today's date for future-dated rows (YYYY-MM-DD; default today)")
    a = ap.parse_args(argv)
    try:
        if a.as_of:
            d = mf.parse_date(a.as_of)
            if d is None:
                raise InputError(f"--as-of {a.as_of} is not a date; write it as YYYY-MM-DD.")
            AS_OF[0] = d
        prof = mf.load_profile()
        fs = mf.fiscal_start_month(prof)
        files = [profile_file(f, AS_OF[0], fs) for f in a.files]
        names = [p.name for p in files]
        if len(set(names)) != len(names):
            raise InputError("Two of the files have the same name; profile them one folder at a time.")
        js, join_heads = joins(files, fs)
    except InputError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    heads = [h for p in files for h in p.heads_up] + join_heads
    n = len(files)
    lead = f"Profiled {mf.num(n)} {'file' if n == 1 else 'files'}"
    if not heads:
        headline = f"**{lead}; nothing in them looks likely to make a figure wrong.**"
    elif len(heads) == 1:
        headline = f"**{lead}. Heads up: {heads[0]['title']}.**"
    else:
        headline = f"**{lead}; {len(heads)} things may make a figure wrong.**"
    out = [headline, ""]
    if heads:
        out += ["## Heads up", ""]
        out += [f"- **{h['title']}.** {h['text']}" for h in heads]
        out.append("")
    for p in files:
        out += render_file(p)
    if n > 1:
        out += ["## Across files", ""]
        by_name = {p.name: p for p in files}
        lines = [x for j in js for x in render_join(j, by_name)]
        out += lines if lines else ["- The files share no key column."]
        out.append("")
    if prof.get("_source") == "defaults" and any(j.get("by_quarter") for j in js):
        out.append("Quarters follow a calendar year (no .magnos/finance.md; run setup to set the fiscal year).")
    md = "\n".join(out).rstrip()
    data = {"as_of": AS_OF[0].isoformat(), "heads_up": heads, "joins": js, "files": [file_json(p) for p in files]}
    mf.emit(md, data, JSON_PATH)
    return 0


def file_json(p: FileProfile) -> dict:
    return {"file": os.path.abspath(p.path), "name": p.name, "rows": len(p.table.rows), "grain": p.grain, "key": p.key,
            "columns": [{"name": c.name, "kind": c.kind, "empty": c.empty, "distinct": c.distinct, "total": c.total,
                         "first": c.first.isoformat() if c.first else None, "last": c.last.isoformat() if c.last else None}
                        for c in p.columns],
            "date_column": p.date_col, "first": p.first.isoformat() if p.first else None,
            "last": p.last.isoformat() if p.last else None, "monthly": p.monthly, "partial": p.partial,
            "future_rows": p.future, "entity_column": p.entity_col, "entities": p.entities,
            "currency_column": p.currency_col, "currencies": p.currencies, "duplicate_rows": p.duplicate_rows,
            "duplicate_keys": p.duplicate_keys, "total_rows": p.total_rows, "amount_column": p.amount_col, "months": p.months,
            "same_days": p.same_days, "heads_up": p.heads_up}


if __name__ == "__main__":
    sys.exit(main())
