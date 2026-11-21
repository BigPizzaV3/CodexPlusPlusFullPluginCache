#!/usr/bin/env python3
"""Budget variance: actuals against budget by P&L line, for a month or the year to date.

Reads two exports (CSV, TSV or XLSX). Each may be wide (one column per month) or
long (one row per line and month, with month, line and amount columns). Every
line is read as revenue, cost of revenue, operating expense or below EBITDA, so
that "favourable" is right for each; gross profit, operating expenses and EBITDA
are derived, never read. The answer names the lines that explain most of the gap.

  python3 scripts/variance.py pnl_monthly.csv budget_fy26_v3.csv --to 2026-08
  python3 scripts/variance.py pnl_monthly.csv budget_fy26_v3.csv --month 2026-08
  python3 scripts/variance.py actuals.xlsx budget.xlsx --line-type "Hosting=cogs"

The full result goes to .magnos/runs/variance.json; scripts/diagram.py draws it.
This file is also the engine of the board-pack skill, which keeps a byte-identical
copy in its own scripts/ folder.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import os
import re
import sys
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any, Dict, List, Optional, Sequence, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import magnos_fin as mf  # noqa: E402

D0 = Decimal(0)
JSON_PATH = os.path.join(".magnos", "runs", "variance.json")
SHORT = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
LONG = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
        "October", "November", "December"]
TYPES = ("revenue", "cogs", "opex", "below", "ignore")
TYPE_WORDS = {
    "revenue": "revenue", "income": "revenue", "sales": "revenue",
    "cogs": "cogs", "costofrevenue": "cogs", "costofsales": "cogs", "direct": "cogs", "directcost": "cogs",
    "opex": "opex", "cost": "opex", "expense": "opex", "operating": "opex", "operatingexpense": "opex",
    "below": "below", "belowebitda": "below", "other": "below",
    "ignore": "ignore", "skip": "ignore",
}
TYPE_NAMES = {"revenue": "revenue", "cogs": "cost of revenue", "opex": "operating expenses",
              "below": "below EBITDA (left out)", "ignore": "ignored"}


class InputError(Exception):
    """A problem with the person's files or flags: exit 2 with one plain sentence."""


# ---------------------------------------------------------------- months

def month_key(y: int, m: int) -> str:
    return f"{y:04d}-{m:02d}"


def add_months(key: str, n: int) -> str:
    y, m = int(key[:4]), int(key[5:7])
    t = y * 12 + (m - 1) + n
    return month_key(t // 12, t % 12 + 1)


def month_range(start: str, end: str) -> List[str]:
    out, k = [], start
    while k <= end:
        out.append(k)
        k = add_months(k, 1)
    return out


_MON_ALT = {m.lower(): i for i, m in enumerate(SHORT, 1)}
_MON_ALT.update({m.lower(): i for i, m in enumerate(LONG, 1)})
_MON_ALT["sept"] = 9


def parse_month(value: Any, year: Optional[int] = None) -> Optional[str]:
    """"2026-08", "Aug 2026", "August 2026", "Aug-26", "08/2026", "2026-08-31" -> "2026-08"."""
    s = str(value or "").strip()
    if not s:
        return None
    m = re.fullmatch(r"([A-Za-z]{3,9})\.?[\s\-'_/]*(\d{2}|\d{4})", s)
    if m and m[1].lower() in _MON_ALT:
        y = int(m[2]) + (2000 if len(m[2]) == 2 else 0)
        return month_key(y, _MON_ALT[m[1].lower()])
    m = re.fullmatch(r"(\d{1,2})[/\-.](\d{4})", s)
    if m and 1 <= int(m[1]) <= 12:
        return month_key(int(m[2]), int(m[1]))
    m = re.fullmatch(r"(\d{4})[/\-.]?(?:M|P)?(\d{1,2})", s, re.I)
    if m and 1 <= int(m[2]) <= 12 and 1900 < int(m[1]) < 2200:
        return month_key(int(m[1]), int(m[2]))
    if year and s.lower().rstrip(".") in _MON_ALT:
        return month_key(year, _MON_ALT[s.lower().rstrip(".")])
    d = mf.parse_date(s)
    if d is not None and 1900 < d.year < 2200:
        return month_key(d.year, d.month)
    return None


def short_label(key: str) -> str:
    return f"{SHORT[int(key[5:7]) - 1]} {key[:4]}"


def long_label(key: str) -> str:
    return f"{LONG[int(key[5:7]) - 1]} {key[:4]}"


def month_name(key: str) -> str:
    return LONG[int(key[5:7]) - 1]


def period_label(months: Sequence[str]) -> str:
    """["2026-01".."2026-08"] -> "Jan–Aug 2026"; one month -> "August 2026"."""
    if not months:
        return ""
    a, b = months[0], months[-1]
    if a == b:
        return long_label(a)
    if a[:4] == b[:4]:
        return f"{SHORT[int(a[5:7]) - 1]}–{SHORT[int(b[5:7]) - 1]} {a[:4]}"
    return f"{short_label(a)}–{short_label(b)}"


def ytd_months(end: str, fiscal_start: int) -> List[str]:
    y, m = int(end[:4]), int(end[5:7])
    start_y = y if m >= fiscal_start else y - 1
    return month_range(month_key(start_y, fiscal_start), end)


# ---------------------------------------------------------------- lines

def norm(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", str(name).lower().replace("&", "and"))


_SUBTOTAL_RE = re.compile(
    r"^(total\b|gross (profit|margin)|(adjusted |adj\.? )?ebitda|ebit\b|operating (income|profit|loss|result)|"
    r"net (income|profit|loss|result|operating)|contribution (margin|profit)|(income|profit|loss|earnings) before)")
_COGS_WORDS = ("cost of revenue", "cost of sales", "cost of goods", "cost of services", "cogs", "direct cost")
_BELOW_WORDS = ("depreciation", "amortization", "amortisation", "interest", "income tax", "tax expense",
                "taxes", "other income", "other expense", "foreign exchange", "fx gain", "fx loss",
                "gain on", "loss on", "impairment")
_STRONG_REVENUE = ("revenue", "turnover")
_OPEX_WORDS = ("marketing", "expense", "r&d", "research", "development", "engineering", "g&a", "general",
               "admin", "payroll", "salar", "wage", "rent", "software", "travel", "professional", "legal",
               "consult", "office", "insurance", "benefit", "opex", "operating", "facilit", "recruit",
               "bank charge", "utilit", "bonus", "commission", "headcount", "contractor")
_WEAK_REVENUE = ("sales", "income", "subscription", "bookings", "billings")


def classify(name: str) -> Tuple[str, str]:
    """(type, how): type is revenue, cogs, opex or below; how is name, account or default."""
    low = " " + str(name).lower().replace("&", " & ").replace("  ", " ") + " "
    low = re.sub(r"\s+", " ", low)
    flat = str(name).lower()
    if any(w in flat for w in _COGS_WORDS):
        return "cogs", "name"
    if any(w in flat for w in _BELOW_WORDS):
        return "below", "name"
    if any(w in flat for w in _STRONG_REVENUE):
        return "revenue", "name"
    if any(w in flat for w in _OPEX_WORDS) or re.search(r"\br ?& ?d\b|\bg ?& ?a\b", low):
        return "opex", "name"
    if any(w in flat for w in _WEAK_REVENUE):
        return "revenue", "name"
    m = re.match(r"\s*(\d)\d{3}", str(name))
    if m:
        return {"4": "revenue", "5": "cogs", "6": "opex", "7": "opex", "8": "below", "9": "below"}.get(m[1], "opex"), "account"
    return "opex", "default"


def subtotal_kind(name: str) -> Optional[str]:
    """None for an ordinary line; else gross_profit, ebitda, total:<type>, ratio or other."""
    low = str(name).strip().lower()
    if "%" in low or re.search(r"\b(ratio|percent|per cent)\b", low):
        return "ratio"
    if not _SUBTOTAL_RE.match(low):
        return None
    if low.startswith("gross profit"):
        return "gross_profit"
    if low.startswith("gross margin"):
        return "ratio"
    if re.match(r"ebitda\b", low):
        return "ebitda"
    if low.startswith("total"):
        rest = re.sub(r"^total\s*", "", low)
        if not rest:
            return "other"
        if "operating" in rest or rest in ("opex", "expenses", "operating expenses", "costs", "overheads"):
            return "total:opex"
        return "total:" + classify(rest)[0]
    return "other"


def parse_type(word: str) -> str:
    t = TYPE_WORDS.get(norm(word))
    if not t:
        raise InputError(f"Unknown line type '{word}'. Use revenue, cogs, opex, below or ignore.")
    return t


def read_overrides(specs: Sequence[str]) -> Dict[str, str]:
    """--line-type values: a CSV file with line,type columns, or "Line name=type"."""
    out: Dict[str, str] = {}
    for spec in specs or []:
        if os.path.isfile(spec):
            t = mf.read_table(spec)
            lc = mf.find_column(t, "line", "name", "account")
            tc = mf.find_column(t, "type", "class", "kind")
            if not lc or not tc:
                raise InputError(f"{spec} needs two columns, line and type.")
            for r in t.rows:
                if r.get(lc, "").strip():
                    out[norm(r[lc])] = parse_type(r.get(tc, ""))
        elif "=" in spec:
            name, word = spec.rsplit("=", 1)
            out[norm(name)] = parse_type(word)
        else:
            raise InputError(f"--line-type '{spec}' is neither a file nor 'Line name=type'.")
    return out


# ---------------------------------------------------------------- loading

@dataclass
class Pnl:
    path: str
    lines: Dict[str, Dict[str, Decimal]] = field(default_factory=dict)   # name -> month -> amount
    types: Dict[str, str] = field(default_factory=dict)                  # name -> type
    how: Dict[str, str] = field(default_factory=dict)                    # name -> name/account/default/override
    reported: Dict[str, Dict[str, Decimal]] = field(default_factory=dict)  # subtotal kind -> month -> amount
    reported_names: Dict[str, str] = field(default_factory=dict)
    version: Optional[str] = None
    entities: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)
    layout: str = ""

    @property
    def name(self) -> str:
        return os.path.basename(self.path)

    def months(self) -> List[str]:
        ks = set()
        for vals in self.lines.values():
            ks.update(vals)
        return sorted(ks)

    def total(self, name: str, months: Sequence[str]) -> Decimal:
        vals = self.lines.get(name, {})
        return sum((vals.get(m, D0) for m in months), D0)


def _check_file(path: str) -> None:
    if not os.path.exists(path):
        raise InputError(f"Cannot find {path}. Check the path, or run the command from the folder that holds it.")
    if os.path.isdir(path):
        raise InputError(f"{path} is a folder. Name the exported file inside it.")


def load_pnl(path: str, overrides: Optional[Dict[str, str]] = None, year: Optional[int] = None,
             version: Optional[str] = None, sheet: Optional[str] = None) -> Pnl:
    """Read a P&L export (wide or long) into monthly amounts per line."""
    _check_file(path)
    try:
        table = mf.read_table(path, sheet=sheet)
    except Exception as exc:  # unreadable workbook, bad encoding
        raise InputError(f"Cannot read {os.path.basename(path)} ({exc.__class__.__name__}). Save it as CSV or XLSX and try again.")
    if not table.columns or not table.rows:
        raise InputError(f"{os.path.basename(path)} has no rows. Check that it is the right export.")
    p = Pnl(path)
    overrides = overrides or {}
    month_cols = [c for c in table.columns if parse_month(c, year)]
    ver_col = mf.find_column(table, "version", "scenario")
    ent_col = mf.find_column(table, "entity", "company", "subsidiary")
    rows = table.rows
    if ver_col and ver_col not in month_cols:
        found = sorted({r.get(ver_col, "").strip() for r in rows if r.get(ver_col, "").strip()})
        if version:
            rows = [r for r in rows if norm(r.get(ver_col, "")) == norm(version)]
            if not rows:
                raise InputError(f"{p.name} has no version '{version}'; it holds {', '.join(found)}.")
            p.version = version
        elif len(found) > 1:
            raise InputError(f"{p.name} holds {len(found)} versions ({', '.join(found)}); pick one with --version.")
        elif found:
            p.version = found[0]
    entities = set()
    if month_cols:
        p.layout = "wide"
        line_col = mf.find_column(table, "line", "line item", "account name", "account", "category", "name", "description", "item")
        if line_col in month_cols or line_col in (ver_col, ent_col):
            line_col = None
        if not line_col:
            for c in table.columns:
                if c not in month_cols and c not in (ver_col, ent_col) and table.kind(c) == "text":
                    line_col = c
                    break
        if not line_col:
            raise InputError(f"{p.name} has month columns but no column that names the lines. Add a 'Line' column.")
        for r in rows:
            name = r.get(line_col, "").strip()
            if not name:
                continue
            if ent_col and r.get(ent_col, "").strip():
                entities.add(r[ent_col].strip())
            for c in month_cols:
                v = mf.to_decimal(r.get(c, ""))
                if v is None:
                    continue
                k = parse_month(c, year)
                bucket = p.lines.setdefault(name, {})
                bucket[k] = bucket.get(k, D0) + v
    else:
        p.layout = "long"
        mcol = mf.find_column(table, "month", "period", "date", "posting date", "fiscal period")
        acol = mf.find_column(table, "amount", "value", "actual", "actuals", "budget", "balance", "net amount", "net", "total")
        lcol = mf.find_column(table, "line", "line item", "account name", "account", "category", "name", "description", "item")
        if not mcol:
            raise InputError(f"{p.name} has neither month columns nor a month column. Export it by month, or add a 'Month' column.")
        if not acol:
            raise InputError(f"{p.name} has no amount column. Name it 'Amount'.")
        if not lcol:
            raise InputError(f"{p.name} has no column that names the lines. Name it 'Line'.")
        bad = 0
        for r in rows:
            name = r.get(lcol, "").strip()
            k = parse_month(r.get(mcol, ""), year)
            v = mf.to_decimal(r.get(acol, ""))
            if not name or v is None:
                continue
            if k is None:
                bad += 1
                continue
            if ent_col and r.get(ent_col, "").strip():
                entities.add(r[ent_col].strip())
            bucket = p.lines.setdefault(name, {})
            bucket[k] = bucket.get(k, D0) + v
        if bad:
            p.notes.append(f"Skipped {bad} rows of {p.name} whose month could not be read.")
    if not p.lines:
        raise InputError(f"{p.name} has no amounts by month. Check that it is a P&L by month.")
    p.entities = sorted(entities)
    if len(p.entities) > 1:
        p.notes.append(f"Summed {len(p.entities)} entities in {p.name}: {', '.join(p.entities)}.")
    _classify_lines(p, overrides)
    _normalise_signs(p)
    return p


def _classify_lines(p: Pnl, overrides: Dict[str, str]) -> None:
    kinds = {name: (None if norm(name) in overrides else subtotal_kind(name)) for name in p.lines}
    for name, kind in kinds.items():
        if kind is None:
            if norm(name) in overrides:
                p.types[name], p.how[name] = overrides[norm(name)], "override"
            else:
                p.types[name], p.how[name] = classify(name)
    for name, kind in kinds.items():
        if kind and kind.startswith("total:"):
            t = kind.split(":", 1)[1]
            if any(p.types.get(n) == t for n, k in kinds.items() if k is None):
                kinds[name] = "total"
                p.reported["total:" + t] = p.lines[name]
                p.reported_names["total:" + t] = name
            else:  # the only line of its kind: keep it as a line
                p.types[name], p.how[name] = t, "name"
                kinds[name] = None
        elif kind in ("gross_profit", "ebitda"):
            p.reported[kind] = p.lines[name]
            p.reported_names[kind] = name
    skipped = [n for n, k in kinds.items() if k is not None]
    for n in skipped:
        del p.lines[n]
    if skipped:
        p.notes.append(f"Left out the subtotal rows of {p.name} ({', '.join(skipped)}) and derived them instead.")
    for n in [n for n, t in p.types.items() if t == "ignore"]:
        p.lines.pop(n, None)


def _normalise_signs(p: Pnl) -> None:
    """Revenue and costs as positive amounts, whatever sign the export used."""
    groups = {"revenue": ("revenue",), "costs": ("cogs", "opex", "below")}
    for label, types in groups.items():
        names = [n for n in p.lines if p.types.get(n) in types]
        total = sum((sum(p.lines[n].values(), D0) for n in names), D0)
        if names and total < 0:
            for n in names:
                p.lines[n] = {k: -v for k, v in p.lines[n].items()}
            p.notes.append(f"{p.name} shows {label} as negative amounts; read them as positive.")
            if label == "revenue":
                for kind in ("gross_profit", "ebitda", "total:revenue"):
                    if kind in p.reported:
                        p.reported[kind] = {k: -v for k, v in p.reported[kind].items()}


# ---------------------------------------------------------------- formatting

def amt(x: Decimal, ref: Optional[Decimal] = None, signed: bool = False) -> str:
    """Money for prose: millions when the main figure is $1M or more and this one $100K or more."""
    ref = x if ref is None else ref
    if abs(ref) >= Decimal(1_000_000) and abs(x) >= Decimal(100_000):
        return mf.money(x, unit="M", signed=signed)
    return mf.money(x, signed=signed)


def pct_words(r: Optional[Decimal]) -> str:
    """A ratio for prose: 0 decimals from 10%, 1 decimal below."""
    if r is None:
        return ""
    return mf.pct(abs(r), decimals=0 if abs(r) >= Decimal("0.1") else 1)


def paren(text: str, negative: bool) -> str:
    return f"({text})" if negative else text


def table_amount(x: Decimal, scale: Decimal) -> str:
    return mf.num(x / scale)


def table_better(x: Decimal, scale: Decimal, mode: str = "favourable") -> str:
    if mode == "actual-minus-budget":
        q = x / scale
        s = mf.num(abs(q))
        return s if s == "0" else (("+" if q > 0 else mf.MINUS) + s)
    return paren(mf.num(abs(x / scale)), mf.num(abs(x / scale)) != "0" and x < 0)


def table_pct(r: Optional[Decimal], decimals: int = 1, mode: str = "favourable") -> str:
    if r is None:
        return "n/a"
    if mode == "actual-minus-budget":
        return mf.pct(r, decimals=decimals, signed=True)
    s = mf.pct(abs(r), decimals=decimals)
    return paren(s, r < 0 and s.strip("0.%") != "")


def table_pts(x: Decimal) -> str:
    s = mf.pts(abs(x), signed=False)
    return paren(s, x < 0 and not re.fullmatch(r"0\.0 pts", s))


def lower_first(name: str) -> str:
    """"Sales and marketing" -> "sales and marketing"; "R&D" stays."""
    if len(name) > 1 and name[0].isupper() and name[1].islower():
        return name[0].lower() + name[1:]
    return name


def join_names(names: Sequence[str], first_upper: bool = True) -> str:
    ns = [lower_first(n) for n in names]
    if first_upper and ns:
        ns[0] = names[0]
    if len(ns) <= 1:
        return "".join(ns)
    return ", ".join(ns[:-1]) + " and " + ns[-1]


def short_name(name: str) -> str:
    """A label short enough for a chart axis."""
    known = {"costofrevenue": "Cost of rev.", "costofsales": "Cost of sales", "salesandmarketing": "S&M",
             "generalandadministrative": "G&A", "researchanddevelopment": "R&D", "operatingexpenses": "Opex"}
    if norm(name) in known:
        return known[norm(name)]
    return name if len(name) <= 12 else name[:11].rstrip() + "…"


def choose_scale(values: Sequence[Decimal], unit: Optional[str] = None) -> Tuple[Decimal, str]:
    u = (unit or "").upper()
    if u in ("1", "$", "USD"):
        return Decimal(1), "$"
    if u == "K":
        return Decimal(1000), "$K"
    if u == "M":
        return Decimal(1_000_000), "$M"
    big = max((abs(v) for v in values), default=D0)
    if big >= Decimal("1e9"):
        return Decimal(1_000_000), "$M"
    if big >= Decimal(100_000):
        return Decimal(1000), "$K"
    return Decimal(1), "$"


# ---------------------------------------------------------------- the comparison

def budget_label(p: Pnl, override: Optional[str] = None) -> str:
    if override:
        return override
    base = p.name.lower()
    kind = "forecast" if re.search(r"forecast|fcst|reforecast", base) else "budget"
    ver = p.version
    if not ver:
        m = re.search(r"(?:^|[^a-z0-9])(v\d+)(?:[^a-z0-9]|$)", base)
        ver = m[1] if m else None
    if ver and re.search(r"budget|forecast|plan", ver, re.I):
        return ver
    return f"{kind} {ver}" if ver else kind


def _row(name: str, kind: str, rtype: str, actual: Decimal, budget: Decimal, is_cost: bool) -> Dict[str, Any]:
    v = mf.variance(actual, budget, is_cost=is_cost, label=name, log=False)
    p = None if v["pct"] is None else Decimal(v["pct"])
    better = Decimal(v["better"])
    return {
        "line": name, "kind": kind, "type": rtype, "is_cost": is_cost,
        "actual": actual, "budget": budget, "diff": Decimal(v["diff"]), "better": better,
        "pct": p, "better_pct": None if p is None else (-p if is_cost else p),
        "favourable": better >= 0,
    }


def compare(act: Pnl, bud: Pnl, months: Sequence[str], label: Optional[str] = None) -> Dict[str, Any]:
    """Rows for every line and the derived totals over the months, plus drivers, tree and bridge."""
    keys: Dict[str, Tuple[str, str]] = {}  # norm -> (display name, type)
    for name, t in act.types.items():
        if name in act.lines:
            keys.setdefault(norm(name), (name, t))
    for name, t in bud.types.items():
        if name in bud.lines:
            keys.setdefault(norm(name), (name, t))
    bud_by_norm = {norm(n): n for n in bud.lines}
    act_by_norm = {norm(n): n for n in act.lines}
    leaf: Dict[str, List[Dict[str, Any]]] = {"revenue": [], "cogs": [], "opex": [], "below": []}
    notes: List[str] = []
    for k, (name, t) in keys.items():
        a = act.total(act_by_norm[k], months) if k in act_by_norm else D0
        b = bud.total(bud_by_norm[k], months) if k in bud_by_norm else D0
        if k not in bud_by_norm:
            notes.append(f"{name} has no budget line; its budget is read as zero.")
        if k not in act_by_norm:
            notes.append(f"{name} is in the budget only; its actual is read as zero.")
        leaf.setdefault(t, []).append(_row(name, "line", t, a, b, t != "revenue"))

    def total(rows: List[Dict[str, Any]], key: str) -> Decimal:
        return sum((r[key] for r in rows), D0)

    rows: List[Dict[str, Any]] = []
    rev, cogs, opex = leaf["revenue"], leaf["cogs"], leaf["opex"]
    rows += rev
    rev_a, rev_b = total(rev, "actual"), total(rev, "budget")
    if len(rev) > 1:
        rows.append(_row("Total revenue", "computed", "revenue", rev_a, rev_b, False))
    rows += cogs
    gp = None
    if rev and cogs:
        gp = _row("Gross profit", "computed", "gross_profit", rev_a - total(cogs, "actual"), rev_b - total(cogs, "budget"), False)
        rows.append(gp)
    rows += opex
    ox = None
    if opex:
        ox = _row("Operating expenses", "computed", "opex_total", total(opex, "actual"), total(opex, "budget"), True)
        rows.append(ox)
    if rev and (cogs or opex):
        cost_a = total(cogs, "actual") + total(opex, "actual")
        cost_b = total(cogs, "budget") + total(opex, "budget")
        bottom = _row("EBITDA", "computed", "ebitda", rev_a - cost_a, rev_b - cost_b, False)
    elif rev:
        bottom = rows[-1] if len(rev) > 1 else rev[0]
    else:
        bottom = _row("Total costs", "computed", "cost_total", total(cogs + opex, "actual"), total(cogs + opex, "budget"), True)
    if bottom not in rows:
        rows.append(bottom)
    below = leaf["below"]
    if below:
        notes.append(f"Left out of EBITDA as below-the-line items: {join_names([r['line'] for r in below])}.")

    # shares of the gap for the lines that are not derived
    leaves = rev + cogs + opex
    gap = bottom["better"]
    for r in leaves:
        r["share"] = None if gap == 0 else r["better"] / gap

    # tie the derived totals to the subtotal rows the export carried
    for p in (act, bud):
        derived = {"gross_profit": (gp, "actual" if p is act else "budget"),
                   "ebitda": (bottom if bottom["line"] == "EBITDA" else None, "actual" if p is act else "budget")}
        tied = []
        for kind, (row, side) in derived.items():
            if row is None or kind not in p.reported:
                continue
            rep = sum((p.reported[kind].get(m, D0) for m in months), D0)
            if abs(rep - row[side]) >= Decimal("0.5"):
                notes.append(f"Heads up: the {p.reported_names[kind]} row of {p.name} is {mf.money(rep)} for "
                             f"{period_label(months)}, but its lines give {mf.money(row[side])}.")
            else:
                tied.append(p.reported_names[kind])
        if tied:
            notes.append(f"The {join_names(tied)} rows of {p.name} tie to the derived figures for {period_label(months)}.")

    out = {
        "period": {"from": months[0], "to": months[-1], "months": list(months), "label": period_label(months)},
        "budget_label": label or budget_label(bud),
        "rows": rows, "leaves": leaves, "below": below, "bottom": bottom, "gross_profit": gp, "opex": ox,
        "notes": notes,
    }
    out["drivers"] = drivers(out)
    out["tree"] = tree(out)
    out["bridge"] = bridge(out)
    return out


def drivers(res: Dict[str, Any], most: int = 3) -> Dict[str, Any]:
    """The fewest lines (at most three) on the gap's side that together reach the gap."""
    gap = res["bottom"]["better"]
    leaves = [r for r in res["leaves"] if r["better"] != 0]
    if gap == 0:
        picked = sorted(leaves, key=lambda r: -abs(r["better"]))[:2]
        return {"lines": picked, "explained": sum((r["better"] for r in picked), D0), "share": None,
                "offsets": [], "offset": D0, "offset_share": None}
    same = sorted([r for r in leaves if (r["better"] > 0) == (gap > 0)], key=lambda r: -abs(r["better"]))
    picked: List[Dict[str, Any]] = []
    run = D0
    for r in same:
        if len(picked) >= most:
            break
        picked.append(r)
        run += r["better"]
        if abs(run) >= abs(gap):
            break
    offsets = sorted([r for r in leaves if (r["better"] > 0) != (gap > 0)], key=lambda r: -abs(r["better"]))
    off = sum((r["better"] for r in offsets), D0)
    return {"lines": picked, "explained": run, "share": run / gap, "offsets": offsets,
            "offset": off, "offset_share": None if gap == 0 else -off / gap}


def _node(label: str, row: Optional[Dict[str, Any]], value: Optional[Decimal] = None,
          favourable: Optional[bool] = None, children: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    v = row["better"] if row is not None else value
    return {"label": label, "value": v, "diff": None if row is None else row["diff"],
            "favourable": (v >= 0) if favourable is None else favourable, "children": children or []}


def _cap(children: List[Dict[str, Any]], most: int = 8) -> List[Dict[str, Any]]:
    if len(children) <= most:
        return children
    keep = sorted(children, key=lambda c: -abs(c["value"]))[:most - 1]
    rest = [c for c in children if c not in keep]
    v = sum((c["value"] for c in rest), D0)
    order = [c for c in children if c in keep]
    return order + [_node(f"Other {len(rest)} lines", None, v)]


def tree(res: Dict[str, Any]) -> Dict[str, Any]:
    """EBITDA, then gross profit and operating expenses, then their lines."""
    bottom = res["bottom"]
    root_label = f"{bottom['line']} vs {res['budget_label']}"
    rev = [r for r in res["leaves"] if r["type"] == "revenue"]
    cogs = [r for r in res["leaves"] if r["type"] == "cogs"]
    opex = [r for r in res["leaves"] if r["type"] == "opex"]
    kids: List[Dict[str, Any]] = []
    if bottom["line"] == "EBITDA":
        if res["gross_profit"] is not None:
            kids.append(_node("Gross profit", res["gross_profit"], children=_cap([_node(r["line"], r) for r in rev + cogs])))
        else:
            kids += [_node(r["line"], r) for r in rev]
        if res["opex"] is not None:
            kids.append(_node("Operating expenses", res["opex"], children=_cap([_node(r["line"], r) for r in opex])))
    else:
        kids = [_node(r["line"], r) for r in res["leaves"]]
    return _node(root_label, bottom, children=_cap(kids))


def bridge(res: Dict[str, Any]) -> Dict[str, Any]:
    """Budget to actual for the bottom line, one step per line."""
    bottom = res["bottom"]
    steps = [(r["line"], r["better"]) for r in res["leaves"]]
    if len(steps) > 9:
        keep = set(n for n, _ in sorted(steps, key=lambda s: -abs(s[1]))[:8])
        other = sum((v for n, v in steps if n not in keep), D0)
        steps = [(n, v) for n, v in steps if n in keep] + [(f"Other {len(res['leaves']) - 8} lines", other)]
    if bottom["is_cost"]:  # a cost total walks with the cost amounts themselves
        steps = [(n, -v) for n, v in steps]
    start = (f"{res['budget_label'][0].upper()}{res['budget_label'][1:]}", bottom["budget"])
    b = mf.bridge(start, steps, end_label="Actual", expected_end=bottom["actual"], log=False)
    return {"metric": bottom["line"], "start": {"label": start[0], "value": bottom["budget"]},
            "steps": [{"label": n, "value": v, "favourable": (v <= 0) if bottom["is_cost"] else (v >= 0)}
                      for n, v in steps],
            "end": {"label": "Actual", "value": bottom["actual"]}, "ties": b["ties"]}


# ---------------------------------------------------------------- month against month

def movement(act: Pnl, month: str, prior: str) -> Dict[str, Any]:
    """Each line in two months of actuals, with its effect on EBITDA (better positive)."""
    rows = []
    by_type: Dict[str, List[str]] = {}
    for name, t in act.types.items():
        if name in act.lines and t in ("revenue", "cogs", "opex"):
            by_type.setdefault(t, []).append(name)

    def val(name: str, m: str) -> Decimal:
        return act.lines[name].get(m, D0)

    def sums(t: str, m: str) -> Decimal:
        return sum((val(n, m) for n in by_type.get(t, [])), D0)

    for t in ("revenue", "cogs", "opex"):
        for n in by_type.get(t, []):
            a, b = val(n, prior), val(n, month)
            ch = b - a
            rows.append({"line": n, "type": t, "kind": "line", "prior": a, "current": b, "change": ch,
                         "effect": ch if t == "revenue" else -ch, "pct": mf.safe_div(ch, abs(a)) if a else None})
    tot = {}
    for m in (prior, month):
        r, c, o = sums("revenue", m), sums("cogs", m), sums("opex", m)
        tot[m] = {"revenue": r, "cogs": c, "opex": o, "gross_profit": r - c, "ebitda": r - c - o,
                  "gross_margin": mf.safe_div(r - c, r) if r else None,
                  "ebitda_margin": mf.safe_div(r - c - o, r) if r else None}
    a, b = tot[prior], tot[month]

    def change(key: str) -> Dict[str, Any]:
        ch = b[key] - a[key]
        return {"prior": a[key], "current": b[key], "change": ch, "pct": mf.safe_div(ch, abs(a[key])) if a[key] else None}

    out = {"month": month, "prior": prior, "rows": rows, "totals": {k: change(k) for k in ("revenue", "cogs", "opex", "gross_profit", "ebitda")}}
    for k in ("gross_margin", "ebitda_margin"):
        out["totals"][k] = {"prior": a[k], "current": b[k],
                            "pts": None if a[k] is None or b[k] is None else (b[k] - a[k]) * 100}
    return out


def ratio(res: Dict[str, Any], key: str, side: str) -> Optional[Decimal]:
    """Gross margin or EBITDA margin of a comparison, actual or budget."""
    rev = sum((r[side] for r in res["leaves"] if r["type"] == "revenue"), D0)
    if rev == 0:
        return None
    if key == "gross_margin":
        return None if res["gross_profit"] is None else res["gross_profit"][side] / rev
    return res["bottom"][side] / rev if res["bottom"]["line"] == "EBITDA" else None


# ---------------------------------------------------------------- the answer

def headline(res: Dict[str, Any]) -> str:
    b = res["bottom"]
    verb = "are" if b["line"].lower().endswith("costs") else "is"
    first = f"{b['line']} {verb} {amt(b['actual'])} for {res['period']['label']}."
    if b["diff"] == 0:
        return f"{first} This is on {res['budget_label']}."
    where = "above" if b["diff"] > 0 else "below"
    p = f" ({pct_words(b['pct'])})" if b["pct"] is not None else ""
    return f"{first} This is {amt(abs(b['diff']), b['actual'])}{p} {where} {res['budget_label']}."


def line_sentence(r: Dict[str, Any], res: Dict[str, Any]) -> str:
    verb = "are" if r["line"].lower().endswith(("costs", "expenses")) else "is"
    s = f"{r['line']} {verb} {amt(r['actual'])} for {res['period']['label']}."
    if r["diff"] == 0:
        return s + f" This is on {res['budget_label']}."
    where = "above" if r["diff"] > 0 else "below"
    p = f" ({pct_words(r['pct'])})" if r["pct"] is not None else ""
    return s + f" This is {amt(abs(r['diff']), r['actual'])}{p} {where} {res['budget_label']}."


def drivers_sentence(res: Dict[str, Any]) -> str:
    d = res["drivers"]
    ref = res["bottom"]["actual"]
    names = [r["line"] for r in d["lines"]]
    if not names:
        return ""
    if d["share"] is None:
        return f"{join_names(names)} moved the most; the net gap is zero."
    gap = abs(res["bottom"]["better"])
    verb = "explains" if len(names) == 1 else "explain"
    s = (f"{join_names(names)} {verb} {amt(abs(d['explained']), ref)}, "
         f"{mf.pct(abs(d['share']), decimals=0)} of the {amt(gap, ref)} gap.")
    if d["offsets"]:
        on = [r["line"] for r in d["offsets"][:3]]
        more = len(d["offsets"]) - len(on)
        lead = join_names(on) + (f" and {more} more" if more else "")
        s += f" {lead} offset {amt(abs(d['offset']), ref)} ({mf.pct(abs(d['offset_share']), decimals=0)})."
    return s


def render(res: Dict[str, Any], scale: Decimal, unit_label: str, mode: str = "favourable") -> str:
    lab = res["budget_label"]
    cap = lab[0].upper() + lab[1:]
    head = "Better/(worse)" if mode == "favourable" else "Actual − budget"
    out = [headline(res), ""]
    trs = []
    for r in res["rows"] + res["below"]:
        name = f"**{r['line']}**" if r["kind"] == "computed" else r["line"]
        val = r["better"] if mode == "favourable" else r["diff"]
        p = r["better_pct"] if mode == "favourable" else r["pct"]
        trs.append([name, table_amount(r["actual"], scale), table_amount(r["budget"], scale),
                    table_better(val, scale, mode), table_pct(p, mode=mode)])
    out.append(mf.md_table([f"{res['period']['label']}, {unit_label}", "Actual", cap, head, "%"], trs))
    d = res["drivers"]
    if d["lines"]:
        out += ["", "## The lines that explain most of the gap", "", drivers_sentence(res), ""]
        dr = [[r["line"], table_better(r["better"], scale, mode),
               "n/a" if r.get("share") is None else table_pct(r["share"], decimals=0)] for r in d["lines"]]
        if len(d["lines"]) > 1:
            dr.append(["Together", table_better(d["explained"], scale, mode),
                       "n/a" if d["share"] is None else table_pct(d["share"], decimals=0)])
        out.append(mf.md_table(["Line", f"{head}, {unit_label}", "Share of the gap"], dr))
        out.append("")
        out += [f"- {line_sentence(r, res)}" for r in d["lines"]]
    return "\n".join(out)


def classification_line(act: Pnl) -> str:
    groups: Dict[str, List[str]] = {}
    for n, t in act.types.items():
        if n in act.lines:
            groups.setdefault(t, []).append(n)
    parts = [f"{TYPE_NAMES[t]}: {', '.join(groups[t])}" for t in ("revenue", "cogs", "opex", "below") if groups.get(t)]
    guessed = [n for n, h in act.how.items() if h == "default" and n in act.lines]
    s = "Lines read as " + "; ".join(parts) + "."
    if guessed:
        s += f" Read as operating expenses by default: {', '.join(guessed)}; fix with --line-type \"Line=type\"."
    return s


# ---------------------------------------------------------------- machine result

def jsonable(x: Any) -> Any:
    if isinstance(x, Decimal):
        return str(x)
    if isinstance(x, dict):
        return {k: jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonable(v) for v in x]
    return x


def display_tree(node: Dict[str, Any], mode: str = "favourable") -> Dict[str, Any]:
    v = node["value"] if mode == "favourable" or node.get("diff") is None else node["diff"]
    return {"label": node["label"], "value": str(v), "display": mf.money(v, signed=True),
            "favourable": node["favourable"], "children": [display_tree(c, mode) for c in node["children"]]}


def to_json(res: Dict[str, Any], act: Pnl, bud: Pnl, scale: Decimal, unit_label: str, mode: str,
            markdown: str, profile: Dict[str, Any]) -> Dict[str, Any]:
    def row(r: Dict[str, Any]) -> Dict[str, Any]:
        out = {k: r.get(k) for k in ("line", "kind", "type", "actual", "budget", "diff", "better", "pct",
                                     "better_pct", "favourable", "share")}
        out["display"] = {"actual": table_amount(r["actual"], scale), "budget": table_amount(r["budget"], scale),
                          "better": table_better(r["better"], scale), "pct": table_pct(r["better_pct"]),
                          "actual_money": amt(r["actual"]), "better_money": mf.money(r["better"], signed=True)}
        return out
    d = res["drivers"]
    months = res["period"]["months"]
    b = res["bridge"]
    return jsonable({
        "tool": "variance",
        "files": {"actuals": act.name, "budget": bud.name},
        "period": res["period"],
        "budget_label": res["budget_label"],
        "sign": "favourable-positive" if mode == "favourable" else "actual-minus-budget",
        "unit": {"scale": scale, "label": unit_label},
        "headline": headline(res),
        "rows": [row(r) for r in res["rows"]],
        "below_ebitda": [row(r) for r in res["below"]],
        "gap": row(res["bottom"]),
        "drivers": {"lines": [r["line"] for r in d["lines"]], "explained": d["explained"], "share": d["share"],
                    "offset_lines": [r["line"] for r in d["offsets"]], "offset": d["offset"],
                    "offset_share": d["offset_share"], "sentence": drivers_sentence(res),
                    "statements": [line_sentence(r, res) for r in d["lines"]]},
        "tree": display_tree(res["tree"], mode),
        "bridge": {"metric": b["metric"], "ties": b["ties"],
                   "start": dict(b["start"], display=mf.money(b["start"]["value"])),
                   "steps": [dict(s, display=mf.money(s["value"], signed=True)) for s in b["steps"]],
                   "end": dict(b["end"], display=mf.money(b["end"]["value"]))},
        "monthly": {"months": months, "lines": {
            r["line"]: {"type": r["type"],
                        "actual": [act.lines.get(_find(act, r["line"]), {}).get(m, D0) for m in months],
                        "budget": [bud.lines.get(_find(bud, r["line"]), {}).get(m, D0) for m in months]}
            for r in res["leaves"]}},
        "notes": act.notes + bud.notes + res["notes"],
        "profile": profile.get("_source", "defaults"),
        "markdown": markdown,
    })


def _find(p: Pnl, name: str) -> str:
    for n in p.lines:
        if norm(n) == norm(name):
            return n
    return name


def log_figures(res: Dict[str, Any], tool: str = "variance", scale: Decimal = Decimal(1), unit_label: str = "$") -> None:
    """Put every printed figure in the session's ledger so the figure check can trace it.

    Each entry keeps the exact value and, as display, the figure as the table prints
    it ("35,590" in $K): the figure check reads plain grouped numbers at face value.
    """
    period = res["period"]["label"]
    lab = res["budget_label"]
    u = f", {unit_label}" if unit_label != "$" else ""
    for r in res["rows"] + res["below"]:
        n = r["line"]
        entries = [
            (f"{n} actual, {period}{u}", r["actual"], table_amount(r["actual"], scale), f"sum of {n} for {period}"),
            (f"{n} {lab}, {period}{u}", r["budget"], table_amount(r["budget"], scale), f"sum of {n} in {lab} for {period}"),
            (f"{n} better/(worse) than {lab}, {period}{u}", r["better"], table_better(r["better"], scale),
             f"{mf.num(r['budget'])} − {mf.num(r['actual'])}" if r["is_cost"] else f"{mf.num(r['actual'])} − {mf.num(r['budget'])}"),
        ]
        if r["better_pct"] is not None:
            entries.append((f"{n} better/(worse) %, {period}", r["better_pct"], table_pct(r["better_pct"]),
                            f"{mf.num(r['better'])} ÷ {mf.num(abs(r['budget']))}"))
        if r.get("share") is not None:
            entries.append((f"{n} share of the gap, {period}", r["share"], table_pct(r["share"], decimals=0),
                            f"{mf.num(r['better'])} ÷ {mf.num(res['bottom']['better'])}"))
        for label, value, display, formula in entries:
            mf.ledger_append({"label": label, "value": value, "display": display, "formula": formula, "tool": tool})
    d = res["drivers"]
    for label, value, display in (("drivers explain", d["explained"], table_better(d["explained"], scale)),
                                  ("drivers share of the gap", d["share"], None),
                                  ("offsets", d["offset"], table_better(d["offset"], scale)),
                                  ("offsets share of the gap", d["offset_share"], None)):
        if value is not None:
            e = {"label": f"{label}, {period}", "value": value, "tool": tool}
            if display:
                e["display"] = display
            mf.ledger_append(e)


# ---------------------------------------------------------------- command line

def pick_months(act: Pnl, bud: Pnl, a: argparse.Namespace, fiscal_start: int) -> List[str]:
    have = act.months()
    if a.month:
        k = parse_month(a.month)
        if not k:
            raise InputError(f"Cannot read the month '{a.month}'. Write it like 2026-08.")
        months = [k]
    else:
        end = parse_month(a.to) if a.to else have[-1]
        if a.to and not end:
            raise InputError(f"Cannot read --to '{a.to}'. Write it like 2026-08.")
        start = parse_month(getattr(a, "from_")) if getattr(a, "from_", None) else ytd_months(end, fiscal_start)[0]
        if not start:
            raise InputError(f"Cannot read --from '{a.from_}'. Write it like 2026-01.")
        if start > end:
            raise InputError("--from comes after --to. Swap them.")
        months = month_range(start, end)
    missing = [m for m in months if m not in have]
    if missing:
        raise InputError(f"{act.name} has no actuals for {period_label(missing)}; it covers "
                         f"{period_label(have)}. Choose months inside it.")
    bmiss = [m for m in months if m not in bud.months()]
    if bmiss:
        raise InputError(f"{bud.name} has no budget for {period_label(bmiss)}. Choose months it covers.")
    return months


def sign_mode(flag: Optional[str], profile: Dict[str, Any]) -> str:
    s = (flag or str(profile.get("variance_sign", "favourable-positive"))).lower()
    return "actual-minus-budget" if ("actual" in s and "budget" in s) else "favourable"


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(prog="variance.py", description="Actuals against budget by P&L line, with the lines that explain the gap.")
    ap.add_argument("actuals", help="P&L actuals by month (CSV, TSV or XLSX; wide or long)")
    ap.add_argument("budget", help="budget or forecast by month, same layouts")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--month", help="one month, like 2026-08")
    g.add_argument("--to", help="last month of the period (default: the last month of actuals)")
    ap.add_argument("--from", dest="from_", help="first month (default: the start of the fiscal year)")
    ap.add_argument("--line-type", action="append", default=[], metavar="FILE|LINE=TYPE",
                    help="set a line's type: revenue, cogs, opex, below or ignore (a CSV with line,type works too)")
    ap.add_argument("--version", help="budget version to use when the budget file holds several")
    ap.add_argument("--label", help="how to name the budget in the answer (default from the file: 'budget v3')")
    ap.add_argument("--unit", choices=["1", "K", "M"], help="table unit (default: $K from $100K)")
    ap.add_argument("--sign", choices=["favourable", "actual-minus-budget"], help="override the profile's sign convention")
    ap.add_argument("--year", type=int, help="year for month columns that have none ('Jan', 'Feb')")
    ap.add_argument("--sheet", help="sheet name in an XLSX file")
    ap.add_argument("--json", default=JSON_PATH, help=f"where to save the machine result (default {JSON_PATH})")
    a = ap.parse_args(argv)
    if a.from_ and a.month:
        ap.error("use --month alone, or --from with --to")
    try:
        profile = mf.load_profile()
        overrides = read_overrides(a.line_type)
        act = load_pnl(a.actuals, overrides, a.year, sheet=a.sheet)
        bud = load_pnl(a.budget, overrides, a.year, version=a.version, sheet=a.sheet)
        months = pick_months(act, bud, a, mf.fiscal_start_month(profile))
        res = compare(act, bud, months, a.label)
        mode = sign_mode(a.sign, profile)
        values = [r["actual"] for r in res["rows"]] + [r["budget"] for r in res["rows"]]
        scale, unit_label = choose_scale(values, a.unit)
        md = render(res, scale, unit_label, mode)
        notes = [classification_line(act)] + act.notes + bud.notes + res["notes"]
        tail = ["", *notes]
        if profile.get("_source") == "defaults":
            tail.append("Used the default finance profile: favourable variances positive, fiscal year from January. "
                        "Run /magnos:setup to set yours.")
        tail.append(f"Saved {a.json}. Draw the gap with: python3 scripts/diagram.py --kind tree (or --kind bridge).")
        markdown = md + "\n" + "\n".join(tail)
        log_figures(res, "variance", scale, unit_label)
        mf.emit(markdown, to_json(res, act, bud, scale, unit_label, mode, md, profile), a.json)
        return 0
    except InputError as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
