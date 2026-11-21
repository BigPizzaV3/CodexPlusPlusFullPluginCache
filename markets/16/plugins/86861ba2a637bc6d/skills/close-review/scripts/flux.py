#!/usr/bin/env python3
"""Close review: compare two trial balances against materiality, then read the
current month's general ledger to find the cause of each large move.

  python3 scripts/flux.py tb_sep.csv tb_aug.csv --gl gl_export.csv

Trial balances: one row per account with an account number, a name, a type
(asset, liability, equity, revenue, expense) and a balance (or debit and credit
columns). An entity column is optional. P&L accounts carry the month's
activity, balance-sheet accounts the month-end balance.

An account is flagged when its change exceeds both the amount and the
percentage threshold (the finance profile's materiality; --materiality and
--pct override it). For each flagged account the script groups the month's GL
lines by journal, takes the journals that drive the change, and reads their
memo lines:
- a descriptive memo is the cause: the account is "explained";
- a blank or generic memo ("adj", "reclass", "accrual", "JE"), or a pattern
  that needs a person (an entry posted twice, a multi-month charge expensed in
  one month, an accrual released with no payroll run) means it "needs an owner",
  and the script states what the ledger shows.

Prints Markdown; writes close_review_<mon>.md and owner_questions.csv to the
working folder (or --out) and the full result to .magnos/runs/close-review.json.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
from collections import Counter, defaultdict
from decimal import Decimal
from typing import Any, Dict, List, Optional, Sequence, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import magnos_fin as mf  # noqa: E402

D0 = Decimal(0)
SYMBOLS = {"USD": "$", "EUR": "€", "GBP": "£"}
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November", "December"]
TYPE_WORDS = {
    "asset": "asset", "assets": "asset", "current asset": "asset", "other current asset": "asset",
    "fixed asset": "asset", "other asset": "asset", "bank": "asset", "cash": "asset",
    "accounts receivable": "asset", "a/r": "asset",
    "liability": "liability", "liabilities": "liability", "current liability": "liability",
    "other current liability": "liability", "long term liability": "liability", "long-term liability": "liability",
    "accounts payable": "liability", "a/p": "liability", "credit card": "liability",
    "equity": "equity", "capital": "equity",
    "revenue": "revenue", "income": "revenue", "other income": "revenue", "sales": "revenue",
    "expense": "expense", "expenses": "expense", "cost of goods sold": "expense", "cost of sales": "expense",
    "cogs": "expense", "other expense": "expense", "cost of revenue": "expense",
}
DEBIT_NORMAL = {"asset", "expense"}

# Default owners by account range; an --owners CSV replaces them.
DEFAULT_OWNERS = [
    (1000, 1199, "Controller"),      # cash and investments
    (1200, 1299, "AR lead"),         # receivables
    (1300, 1999, "Controller"),      # prepaids, fixed and other assets
    (2000, 2099, "AP lead"),         # payables
    (2100, 2199, "Controller"),      # accrued expenses
    (2200, 2399, "Payroll"),         # accrued compensation, payroll liabilities
    (2400, 2499, "Tax lead"),        # taxes
    (2500, 2599, "Revenue lead"),    # deferred revenue
    (2600, 3999, "Controller"),      # leases, debt, equity
    (4000, 4999, "Revenue lead"),    # revenue
    (5000, 5999, "Controller"),      # cost of revenue
    (6000, 6079, "Payroll"),         # compensation
    (6080, 6399, "Controller"),      # contractors, professional fees, marketing, travel
    (6400, 6499, "AP lead"),         # software and IT
    (6500, 9999, "Controller"),      # facilities, people, insurance, other
]

GENERIC_WORDS = set("""
adj adjs adjust adjusted adjustment adjustments adjusting reclass reclasses reclassed reclassification reclassify
accrual accruals accrue accrued accruing je jes jnl jrnl journal journals entry entries gj true up trueup
correction corrections correct corrected fix fixed misc miscellaneous other others per see attached support backup
month end monthend eom me to record recorded recording reverse reversal reversed reversing book booked booking post
posted posting tbd various sundry the and for of from on in at by with as discussed cfo controller fyi pending temp
temporary plug balance balancing clearing catch catchup manual upload import batch period periods entry
jan feb mar apr may jun jul aug sep sept oct nov dec january february march april june july august september
october november december q1 q2 q3 q4 fy ytd mtd per
""".split())
COMP_WORDS = re.compile(r"bonus|commission|payroll|salar|wage|pto|vacation|incentive", re.I)
DUP_NOUNS = [("amortiz", "Amortization"), ("depreciat", "Depreciation"), ("accru", "Accrual"), ("payroll", "Payroll"),
             ("rent", "Rent"), ("revenue", "Revenue recognition"), ("interest", "Interest"), ("invoice", "Invoice")]
SOURCE_WORDS = [("payroll", "payroll run"), ("journal", "journal"), ("je", "journal"), ("gj", "journal"),
                ("bill pay", "payment"), ("bill", "bill"), ("invoice", "invoice"), ("credit memo", "credit memo"),
                ("check", "check"), ("payment", "payment"), ("deposit", "deposit"), ("card", "card charge")]


class InputError(Exception):
    pass


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    sys.exit(2)


# ---------------------------------------------------------------- reading


def read(path: str, what: str) -> mf.Table:
    if not os.path.exists(path):
        raise InputError(f"Cannot find {path}. Check the file name, or put the {what} in the working folder.")
    try:
        t = mf.read_table(path)
    except Exception:
        raise InputError(f"Cannot read {os.path.basename(path)}. Save the {what} as CSV, TSV or XLSX.")
    if not t.rows:
        raise InputError(f"{os.path.basename(path)} has no rows. Export the {what} again with its data.")
    return t


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


def pick(t: mf.Table, exact: Sequence[str], contains: Sequence[str] = (), exclude: Sequence[str] = (),
         taken: Sequence[Optional[str]] = ()) -> Optional[str]:
    """A column by exact normalized name first, then by a fragment, skipping excluded words."""
    cols = [c for c in t.columns if c not in taken]
    by = {norm(c): c for c in cols}
    for e in exact:
        if norm(e) in by:
            return by[norm(e)]
    for frag in contains:
        for c in cols:
            n = norm(c)
            if norm(frag) in n and not any(norm(x) in n for x in exclude):
                return c
    return None


def acct_code(value: Any) -> str:
    s = str(value).strip()
    if re.fullmatch(r"\d+\.0+", s):
        s = s.split(".")[0]
    m = re.match(r"^([^\s:]+?)(?:\s*[:\-–—]\s+|\s+|$)", s)
    return m.group(1) if m else s


def acct_number(code: str) -> Optional[int]:
    m = re.match(r"^(\d{3,6})", code)
    return int(m.group(1)) if m else None


def type_from_number(code: str, name: str) -> Optional[str]:
    n = acct_number(code)
    if n is None:
        return None
    first = int(str(n)[0])
    if first == 1:
        return "asset"
    if first == 2:
        return "liability"
    if first == 3:
        return "equity"
    if first == 4:
        return "revenue"
    if first >= 5:
        income = re.search(r"(?<![-\w])(income|gains?)\b", name, re.I)
        cost = re.search(r"\b(tax|taxes|expenses?|loss|losses)\b", name, re.I)
        return "revenue" if income and not cost else "expense"
    return None


def read_tb(path: str) -> Dict[str, Any]:
    t = read(path, "trial balance")
    base = os.path.basename(path)
    c_acct = pick(t, ["account", "account number", "account no", "account #", "acct", "acct no", "gl account",
                      "account code", "account id", "number", "no", "code"],
                  ["account", "acct"], exclude=["name", "desc", "type", "categ", "class", "line", "group"])
    if not c_acct:
        raise InputError(f"{base} has no account column. Add a column named account with the account number.")
    c_name = pick(t, ["name", "account name", "description", "account description", "title"],
                  ["name", "descr"], taken=[c_acct])
    c_type = pick(t, ["type", "account type", "class", "account class", "category"], ["type"], taken=[c_acct, c_name])
    c_ent = pick(t, ["entity", "subsidiary", "legal entity", "company"], taken=[c_acct, c_name, c_type])
    c_line = pick(t, ["fs_line", "fs line", "financial statement line", "statement line", "report line", "reporting line",
                      "line", "rollup", "group"], taken=[c_acct, c_name, c_type, c_ent])
    c_bal = pick(t, ["balance", "ending balance", "closing balance", "end balance", "net balance", "balance usd",
                     "period balance", "net", "amount", "activity"], ["balance"], taken=[c_acct, c_name, c_type, c_ent, c_line])
    c_dr = c_cr = None
    if not c_bal:
        c_dr = pick(t, ["debit", "debits", "dr", "debit amount"], ["debit"])
        c_cr = pick(t, ["credit", "credits", "cr", "credit amount"], ["credit"])
        if not (c_dr and c_cr):
            raise InputError(f"{base} has no balance column. Export the trial balance with a balance column, "
                             f"or with debit and credit columns.")
    if c_type:
        mapped = [TYPE_WORDS.get(str(r.get(c_type, "")).strip().lower()) for r in t.rows]
        if sum(1 for m in mapped if m) < 0.8 * len(t.rows):
            c_type = None
    rows: List[Dict[str, Any]] = []
    bad = 0
    for r in t.rows:
        code = acct_code(r.get(c_acct, ""))
        if not code or re.match(r"(?i)^total", code):
            continue
        name = str(r.get(c_name, "")).strip() if c_name else ""
        if c_bal:
            raw = str(r.get(c_bal, "")).strip()
            bal = mf.to_decimal(raw)
            if bal is None:
                if raw:
                    bad += 1
                bal = D0
        else:
            dr = mf.to_decimal(r.get(c_dr, "")) or D0
            cr = mf.to_decimal(r.get(c_cr, "")) or D0
            bal = dr - cr
        typ = TYPE_WORDS.get(str(r.get(c_type, "")).strip().lower()) if c_type else type_from_number(code, name)
        if typ is None:
            raise InputError(f"{base} has no type column, and account {code} does not show its type. Add a type column "
                             f"(asset, liability, equity, revenue or expense).")
        rows.append({"account": code, "name": name, "type": typ,
                     "entity": str(r.get(c_ent, "")).strip() if c_ent else "",
                     "line": str(r.get(c_line, "")).strip() if c_line else "", "balance": bal})
    if bad > 0.05 * max(1, len(rows)):
        raise InputError(f"{base}: the column {c_bal} holds text where amounts should be. Export the balances as numbers.")
    if not rows:
        raise InputError(f"{base} has no account rows. Export the trial balance again with its data.")
    return {"path": path, "rows": rows, "debit_credit": c_bal is None, "types_from_numbers": c_type is None,
            "has_line": bool(c_line), "has_entity": bool(c_ent)}


def signed_convention(rows: List[Dict[str, Any]]) -> bool:
    """True when credits are negative in the file (balances sum to zero), False for natural signs."""
    total = sum((r["balance"] for r in rows), D0)
    natural = sum((r["balance"] if r["type"] in DEBIT_NORMAL else -r["balance"] for r in rows), D0)
    return abs(total) < abs(natural)


def month_of(path: str) -> Tuple[Optional[int], Optional[int]]:
    base = os.path.basename(path).lower()
    m = re.search(r"(20\d\d)[-_ .]?(0[1-9]|1[0-2])(?!\d)", base)
    if m:
        return int(m.group(2)), int(m.group(1))
    year = re.search(r"(?<!\d)(20\d\d)(?!\d)", base)
    for i, full in enumerate(MONTHS):
        ab = full[:3].lower()
        alts = [full.lower(), ab] + (["sept"] if i == 8 else [])
        for a in alts:
            if re.search(rf"(?<![a-z]){a}(?![a-z])", base):
                return i + 1, int(year.group(1)) if year else None
    return None, None


# ---------------------------------------------------------------- the general ledger


def read_gl(path: str, types: Dict[str, str], signed: bool) -> Dict[str, Any]:
    t = read(path, "general ledger export")
    base = os.path.basename(path)
    c_acct = pick(t, ["account", "account number", "account no", "acct", "gl account", "account code", "account id"],
                  ["account", "acct"], exclude=["name", "desc", "type", "categ", "class"])
    if not c_acct:
        raise InputError(f"{base} has no account column. Export the GL with the account number on each line.")
    c_date = pick(t, ["date", "posting date", "gl date", "transaction date", "effective date", "entry date"], ["date"],
                  taken=[c_acct])
    c_jnl = pick(t, ["journal", "journal id", "journal no", "journal number", "je", "je no", "je number", "entry no",
                     "entry number", "document", "document number", "doc no", "doc number", "num", "transaction id",
                     "transaction no", "transaction number", "reference", "ref"], ["journal"], taken=[c_acct, c_date])
    c_src = pick(t, ["source", "source type", "transaction type", "type", "module", "origin"], taken=[c_acct, c_date, c_jnl])
    c_name = pick(t, ["name", "vendor", "customer", "payee", "counterparty", "vendor name", "customer name"],
                  taken=[c_acct, c_date, c_jnl, c_src])
    c_memo = pick(t, ["memo", "description", "line memo", "memo description", "line description", "narrative",
                      "details", "comment", "text", "line memo description"], ["memo", "descr", "narrat"],
                  exclude=["account"], taken=[c_acct, c_date, c_jnl, c_src, c_name])
    c_ent = pick(t, ["entity", "subsidiary", "legal entity", "company"], taken=[c_acct, c_date, c_jnl, c_src, c_name, c_memo])
    c_dr = pick(t, ["debit", "debits", "dr", "debit amount"], ["debit"])
    c_cr = pick(t, ["credit", "credits", "cr", "credit amount"], ["credit"])
    c_amt = None
    if not (c_dr and c_cr):
        c_amt = pick(t, ["amount", "net amount", "net", "value", "amount usd", "signed amount"], ["amount"])
        if not c_amt:
            raise InputError(f"{base} has no amount columns. Export the GL with debit and credit columns, or one signed amount.")
    lines = []
    for i, r in enumerate(t.rows):
        code = acct_code(r.get(c_acct, ""))
        if not code:
            continue
        if c_amt:
            signed_dr = mf.to_decimal(r.get(c_amt, "")) or D0
        else:
            signed_dr = (mf.to_decimal(r.get(c_dr, "")) or D0) - (mf.to_decimal(r.get(c_cr, "")) or D0)
        typ = types.get(code)
        if signed or typ is None or typ in DEBIT_NORMAL:
            amt = signed_dr
        else:
            amt = -signed_dr
        lines.append({
            "n": i + 1, "account": code, "amount": amt,
            "date": mf.parse_date(r.get(c_date, "")) if c_date else None,
            "journal": str(r.get(c_jnl, "")).strip() if c_jnl else "",
            "source": str(r.get(c_src, "")).strip() if c_src else "",
            "name": str(r.get(c_name, "")).strip() if c_name else "",
            "memo": " ".join(str(r.get(c_memo, "")).split()) if c_memo else "",
            "entity": str(r.get(c_ent, "")).strip() if c_ent else "",
        })
    return {"path": path, "lines": lines, "has_memo": bool(c_memo), "has_journal": bool(c_jnl), "has_date": bool(c_date)}


def is_generic(memo: str) -> bool:
    text = re.sub(r"\b[A-Z]{1,5}[-#]?\d[\w-]*\b", " ", memo or "")      # JE-4471, INV 2093, #12
    words = re.findall(r"[a-z][a-z&']+", text.lower())
    meaningful = [w for w in words if len(w) >= 3 and w.strip("'") not in GENERIC_WORDS]
    return len(meaningful) < 2


_PERIOD_RES = [
    re.compile(r"(\d{1,2})/(\d{1,2})/(\d{2,4})\s*(?:[-–—]|to|through|thru)\s*(\d{1,2})/(\d{1,2})/(\d{2,4})", re.I),
    re.compile(r"(\d{4})-(\d{2})-(\d{2})\s*(?:[-–—]|to|through|thru)\s*(\d{4})-(\d{2})-(\d{2})", re.I),
    re.compile(r"([A-Za-z]{3,9})\.?\s+(\d{4})\s*(?:[-–—]|to|through|thru)\s*([A-Za-z]{3,9})\.?\s+(\d{4})", re.I),
]
_ANNUAL_RE = re.compile(r"\b(annual|yearly|12[- ]month|twelve[- ]month|one[- ]year|1[- ]year)\b.{0,30}?"
                        r"\b(renewal|subscription|plan|licen[cs]e|contract|term|fee|prepayment|support)\b", re.I)


def service_months(memo: str) -> Optional[int]:
    """The months a charge covers, when its memo names a service period."""
    if not memo:
        return None
    for i, rx in enumerate(_PERIOD_RES):
        m = rx.search(memo)
        if not m:
            continue
        try:
            if i == 0:
                y1, y2 = int(m[3]), int(m[6])
                y1 += 2000 if y1 < 100 else 0
                y2 += 2000 if y2 < 100 else 0
                a, b = dt.date(y1, int(m[1]), int(m[2])), dt.date(y2, int(m[4]), int(m[5]))
            elif i == 1:
                a, b = dt.date(int(m[1]), int(m[2]), int(m[3])), dt.date(int(m[4]), int(m[5]), int(m[6]))
            else:
                ma, mb = mf.parse_date(f"{m[1]} {m[2]}"), mf.parse_date(f"{m[3]} {m[4]}")
                if not (ma and mb):
                    continue
                a, b = ma, mf.month_end(mb)
        except ValueError:
            continue
        months = round(((b - a).days + 1) / 30.44)
        if months >= 1:
            return months
    if _ANNUAL_RE.search(memo):
        return 12
    return None


# ---------------------------------------------------------------- formatting


def short_date(d: Optional[dt.date]) -> str:
    return f"{d.strftime('%b')} {d.day}" if d else "an undated line"


def cell(s: Any) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ")


def clip(s: str, n: int = 90) -> str:
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def threshold_text(amount: Decimal, sym: str) -> str:
    if amount >= 10000 and amount % 1000 == 0:
        return mf.money(amount, currency=sym)
    return mf.money(amount, unit="1", decimals=2 if amount != amount.to_integral_value() else 0, currency=sym)


def pct_text(p: Decimal) -> str:
    return (mf.num(p) if p == p.to_integral_value() else mf.num(p, 1)) + "%"


def plural(n: int, one: str, many: str) -> str:
    return one if n == 1 else many


# ---------------------------------------------------------------- the review


def journals_for(lines: List[Dict[str, Any]], has_journal: bool) -> List[Dict[str, Any]]:
    groups: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for ln in lines:
        key = ln["journal"] if has_journal and ln["journal"] else f"line {ln['n']}"
        groups[key].append(ln)
    out = []
    for key, ls in groups.items():
        total = sum((x["amount"] for x in ls), D0)
        main = max(ls, key=lambda x: abs(x["amount"]))
        dates = [x["date"] for x in ls if x["date"]]
        out.append({"journal": key, "amount": total, "date": min(dates) if dates else None, "memo": main["memo"],
                    "name": main["name"], "source": main["source"], "lines": len(ls)})
    return out


def source_word(source: str) -> str:
    s = source.lower()
    for key, word in SOURCE_WORDS:
        if re.search(rf"(?<![a-z]){key}", s):
            return word
    return "entry"


def review_account(acc: Dict[str, Any], lines: Optional[List[Dict[str, Any]]], has_journal: bool,
                   month_name: str, sym: str) -> Dict[str, Any]:
    """Classify one flagged account: explained (cause from a memo) or needs an owner (what the ledger shows)."""
    change = acc["change"]
    K = lambda x: mf.money(x, unit="K", decimals=1, currency=sym)   # noqa: E731
    if lines is None:
        return {"status": "owner", "kind": "no_gl", "shows": "No GL export given", "ask": "What explains the change?"}
    if not lines:
        return {"status": "owner", "kind": "no_lines", "shows": f"No {month_name} lines in the GL export",
                "ask": f"The GL export has no {month_name} lines for this account. What explains the change?"}
    groups = journals_for(lines, has_journal)
    direction = 1 if change > 0 else -1
    in_dir = sorted([g for g in groups if g["amount"] * direction > 0], key=lambda g: (-abs(g["amount"]), g["journal"]))
    need = abs(change) * Decimal("0.6")
    drivers, cum = [], D0
    for g in in_dir:
        drivers.append(g)
        cum += abs(g["amount"])
        if cum >= need:
            break
    weak = False
    if not drivers:
        drivers = sorted(groups, key=lambda g: (-abs(g["amount"]), g["journal"]))[:3]
        weak = True
    top = drivers[0]
    base = {"drivers": [dict(g, amount=str(g["amount"]), date=g["date"].isoformat() if g["date"] else None) for g in drivers],
            "coverage": None if weak else str(cum / abs(change))}

    # 1. an entry posted twice
    seen: Dict[Tuple[Decimal, str], Dict[str, Any]] = {}
    dup = None
    for g in in_dir:
        if abs(g["amount"]) < 1000 or not g["memo"].strip() or "payroll" in g["source"].lower():
            continue
        k = (abs(g["amount"]), re.sub(r"\W+", " ", g["memo"].lower()).strip())
        if k in seen:
            other = seen[k]
            close_in_time = not (g["date"] and other["date"]) or abs((g["date"] - other["date"]).days) <= 7
            if close_in_time and 2 * abs(g["amount"]) >= abs(change) * Decimal("0.3"):
                dup = (other, g)
                break
        else:
            seen[k] = g
    if dup:
        a, b = sorted(dup, key=lambda g: g["journal"])
        noun = next((n for key, n in DUP_NOUNS if key in a["memo"].lower()), None)
        shows = f"{noun} doubled: {a['journal']} and {b['journal']}" if noun else \
            f"Same entry posted twice: {a['journal']} and {b['journal']}"
        return dict(base, status="owner", kind="duplicate", shows=shows, journals=[a["journal"], b["journal"]],
                    ask=f"{a['journal']} and {b['journal']} each post {K(abs(a['amount']))} with the memo "
                        f"\"{clip(a['memo'], 60)}\". Should one be reversed?")

    # 2. a multi-month charge expensed in one month
    if acc["type"] == "expense" and change > 0:
        for g in drivers:
            months = service_months(g["memo"])
            if months and months >= 2:
                who = g["name"] or g["journal"]
                shows = "Annual renewal expensed, not prepaid" if months >= 11 else f"{months}-month charge expensed, not prepaid"
                return dict(base, status="owner", kind="expensed_not_prepaid", shows=shows, months=months,
                            journals=[g["journal"]],
                            ask=f"{who} billed {K(g['amount'])} on {short_date(g['date'])} for \"{clip(g['memo'], 60)}\", "
                                f"all expensed in {month_name}. Should it move to prepaid expenses and be expensed "
                                f"over {months} months?")

    # 3. a compensation accrual released with no payroll run
    if acc["type"] == "liability" and acc["natural_change"] < 0 and COMP_WORDS.search(acc["name"]):
        payroll_hit = any("payroll" in g["source"].lower() for g in groups)
        manual = [g for g in drivers if not g["source"] or re.search(r"journal|\bje\b|\bgj\b|general|manual|adjust", g["source"], re.I)]
        if not payroll_hit and manual:
            g = manual[0]
            what = "bonuses" if "bonus" in acc["name"].lower() else "they"
            return dict(base, status="owner", kind="accrual_release", shows="Release with no payroll run",
                        journals=[g["journal"]],
                        ask=f"{g['journal']} on {short_date(g['date'])} released {K(abs(g['amount']))} with no payroll run. "
                            f"Were {what} paid, or should the release be reversed?")

    # 4. a descriptive memo is the cause
    if not weak and not is_generic(top["memo"]):
        return dict(base, status="explained", kind="memo", cause=clip(top["memo"]), journals=[top["journal"]])

    # 5. a generic memo: say what the ledger shows
    memo_txt = f"the memo \"{clip(top['memo'], 40)}\"" if top["memo"].strip() else "no memo"
    if not weak and len(drivers) == 1 and abs(top["amount"]) >= need:
        word = source_word(top["source"])
        shows = f"One {word}, {top['journal']} on {short_date(top['date'])}" if not top["journal"].startswith("line ") \
            else f"One line on {short_date(top['date'])}"
        ask = (f"{top['journal']} on {short_date(top['date'])} posts {K(top['amount'])} with {memo_txt}. "
               f"What is it for, and does it belong in {acc['label']}?")
        return dict(base, status="owner", kind="one_entry", shows=shows, journals=[top["journal"]], ask=ask)
    if weak:
        way = "increase" if change > 0 else "decrease"
        return dict(base, status="owner", kind="no_driver",
                    shows=f"No {month_name} line explains the {way}",
                    journals=[g["journal"] for g in drivers],
                    ask=f"No {month_name} entry moves the account this way; the largest line is {top['journal']} on "
                        f"{short_date(top['date'])} for {K(top['amount'])}. What changed from the prior month?")
    n = len(drivers)
    shows = f"{n} entries; largest {top['journal']} on {short_date(top['date'])}, {K(top['amount'])}"
    ask = (f"{n} entries drive it; the largest is {top['journal']} on {short_date(top['date'])} for {K(top['amount'])}, "
           f"with {memo_txt}. What drove the change?")
    return dict(base, status="owner", kind="generic", shows=shows, journals=[g["journal"] for g in drivers], ask=ask)


def owner_for(code: str, rules: List[Tuple[str, Any, Any, str]]) -> str:
    n = acct_number(code)
    for kind, a, b, owner in rules:
        if kind == "exact" and code == a:
            return owner
    for kind, a, b, owner in rules:
        if kind == "range" and n is not None and a <= n <= b:
            return owner
        if kind == "prefix" and code.startswith(a):
            return owner
    return "Controller"


def read_owners(path: Optional[str]) -> List[Tuple[str, Any, Any, str]]:
    rules: List[Tuple[str, Any, Any, str]] = [("range", lo, hi, o) for lo, hi, o in DEFAULT_OWNERS]
    if not path:
        return rules
    t = read(path, "owners file")
    c_acct = pick(t, ["account", "accounts", "range", "account range", "account number"], ["account"])
    c_owner = pick(t, ["owner", "ask", "who", "name"], ["owner"])
    if not (c_acct and c_owner):
        raise InputError(f"{os.path.basename(path)} needs two columns: account (a number, a range like 6100-6199, "
                         f"or a prefix like 61*) and owner.")
    custom = []
    for r in t.rows:
        spec, owner = str(r.get(c_acct, "")).strip(), str(r.get(c_owner, "")).strip()
        if not spec or not owner:
            continue
        m = re.fullmatch(r"(\d+)\s*[-–]\s*(\d+)", spec)
        if m:
            custom.append(("range", int(m[1]), int(m[2]), owner))
        elif spec.endswith("*"):
            custom.append(("prefix", spec[:-1], None, owner))
        else:
            custom.append(("exact", acct_code(spec), None, owner))
    return custom + rules


# ---------------------------------------------------------------- the P&L summary


def pnl_summary(cur: Dict[str, Any], pri: Dict[str, Any], signed: bool) -> Optional[Dict[str, Any]]:
    def nat(r: Dict[str, Any]) -> Decimal:
        if not signed:
            return r["balance"]
        return r["balance"] if r["type"] in DEBIT_NORMAL else -r["balance"]

    def classify(r: Dict[str, Any], has_line: bool) -> Optional[str]:
        line = r["line"].lower()
        n = acct_number(r["account"])
        if has_line and line:
            if r["type"] == "asset" and re.fullmatch(r"cash( and cash equivalents)?", line):
                return "cash"
            if r["type"] == "revenue" and re.search(r"revenue|sales", line) and not re.search(r"other|interest", line):
                return "revenue"
            if r["type"] == "expense" and re.search(r"cost of (revenue|sales|goods)|cogs", line):
                return "cogs"
            if r["type"] == "expense" and re.search(r"sales|marketing|research|r&d|general|admin|g&a|operating", line):
                return "opex"
            return None
        if n is not None and len(str(n)) == 4:
            if 1000 <= n <= 1099 and r["type"] == "asset":
                return "cash"
            if 4000 <= n <= 4999 and r["type"] == "revenue":
                return "revenue"
            if 5000 <= n <= 5999 and r["type"] == "expense":
                return "cogs"
            if 6000 <= n <= 6999 and r["type"] == "expense":
                return "opex"
            return None
        if r["type"] == "asset" and re.search(r"\b(cash|bank)\b", r["name"], re.I):
            return "cash"
        return None

    def totals(tb: Dict[str, Any]) -> Dict[str, Decimal]:
        out = {"revenue": D0, "cogs": D0, "opex": D0, "cash": D0}
        for r in tb["rows"]:
            c = classify(r, tb["has_line"])
            if c:
                out[c] += nat(r)
        return out

    a, b = totals(pri), totals(cur)
    if a["revenue"] == 0 or b["revenue"] == 0:
        return None
    res = {}
    for k, t in (("prior", a), ("current", b)):
        gp = t["revenue"] - t["cogs"]
        ebitda = gp - t["opex"]
        res[k] = {"revenue": t["revenue"], "cogs": t["cogs"], "opex": t["opex"], "gross_margin": gp / t["revenue"],
                  "ebitda": ebitda, "ebitda_margin": ebitda / t["revenue"], "cash": t["cash"]}
    res["basis"] = "fs_line column" if cur["has_line"] else "account ranges 4000–6999, cash 1000–1099"
    return res


# ---------------------------------------------------------------- main


def main(argv: Optional[Sequence[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Close review: flag accounts that moved more than materiality and "
                                            "find their causes in the GL memo lines.")
    p.add_argument("current", help="the current month's trial balance (CSV, TSV or XLSX)")
    p.add_argument("prior", help="the prior month's trial balance")
    p.add_argument("--gl", help="the current month's GL export, with memo lines")
    p.add_argument("--materiality", help="amount threshold, e.g. 25000 (default: the finance profile, else $25K)")
    p.add_argument("--pct", help="percentage threshold, e.g. 10 (default: the finance profile, else 10%%)")
    p.add_argument("--owners", help="CSV of account (number, range or prefix) and owner; replaces the default owners")
    p.add_argument("--out", help="folder for close_review_<mon>.md and owner_questions.csv (default: working folder)")
    a = p.parse_args(argv)

    try:
        return run(a)
    except InputError as e:
        fail(str(e))
    return 2


def run(a: argparse.Namespace) -> int:
    profile = mf.load_profile()
    sym = SYMBOLS.get(str(profile.get("currency", "USD")).upper(), "$")
    amount = mf.to_decimal(a.materiality) if a.materiality else profile["materiality_amount"]
    pct_thr = mf.to_decimal(str(a.pct).rstrip("%")) if a.pct else profile["materiality_pct"]
    if amount is None or pct_thr is None:
        raise InputError("Materiality must be a number: for example --materiality 25000 --pct 10.")
    if a.materiality or a.pct:
        thr_source = "from the command line"
    elif profile["_source"] == "defaults":
        thr_source = "defaults: there is no .magnos/finance.md"
    else:
        thr_source = "from .magnos/finance.md"

    cur, pri = read_tb(a.current), read_tb(a.prior)
    signed = signed_convention(cur["rows"])

    # periods
    m_cur, y_cur = month_of(a.current)
    m_pri, y_pri = month_of(a.prior)
    gl = None
    types = {r["account"]: r["type"] for r in cur["rows"] + pri["rows"]}
    if a.gl:
        gl = read_gl(a.gl, types, signed)
        if m_cur is None and gl["has_date"]:
            months = Counter((ln["date"].year, ln["date"].month) for ln in gl["lines"] if ln["date"])
            if months:
                (y_cur, m_cur), _ = months.most_common(1)[0]
    if m_cur and not m_pri:
        m_pri = 12 if m_cur == 1 else m_cur - 1
    cur_name = MONTHS[m_cur - 1] if m_cur else "the current month"
    pri_name = MONTHS[m_pri - 1] if m_pri else "the prior month"
    cur_col = MONTHS[m_cur - 1] if m_cur else "Current"
    pri_col = MONTHS[m_pri - 1] if m_pri else "Prior"
    mon = MONTHS[m_cur - 1][:3].lower() if m_cur else ""

    # keys: account, or account and entity when account numbers repeat across entities
    def keyed(tb: Dict[str, Any]) -> Dict[Tuple[str, str], Dict[str, Any]]:
        repeats = Counter(r["account"] for r in tb["rows"])
        use_entity = tb["has_entity"] and any(c > 1 for c in repeats.values())
        out: Dict[Tuple[str, str], Dict[str, Any]] = {}
        for r in tb["rows"]:
            k = (r["account"], r["entity"] if use_entity else "")
            if k in out:
                out[k] = dict(out[k], balance=out[k]["balance"] + r["balance"])
            else:
                out[k] = dict(r)
        return out

    kc, kp = keyed(cur), keyed(pri)
    by_entity = any(k[1] for k in kc) or any(k[1] for k in kp)

    flagged: List[Dict[str, Any]] = []
    keys = list(kc) + [k for k in kp if k not in kc]
    for k in keys:
        rc, rp = kc.get(k), kp.get(k)
        r = rc or rp
        cb = rc["balance"] if rc else D0
        pb = rp["balance"] if rp else D0
        ch = cb - pb
        ratio = None if pb == 0 else ch / abs(pb)
        if abs(ch) > amount and (ratio is None or abs(ratio) * 100 > pct_thr):
            nat_ch = ch if (not signed or r["type"] in DEBIT_NORMAL) else -ch
            label = f"{r['account']} {r['name']}".strip() + (f" ({k[1]})" if by_entity and k[1] else "")
            flagged.append({"key": k, "account": r["account"], "name": r["name"], "entity": k[1] or r["entity"],
                            "type": r["type"], "label": label, "prior": pb, "current": cb, "change": ch,
                            "natural_change": nat_ch, "ratio": ratio})

    # the GL lines of each flagged account, in the current month
    gl_note = ""
    by_acct: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)
    if gl:
        lines = gl["lines"]
        if m_cur and gl["has_date"]:
            in_month = [ln for ln in lines if ln["date"] and ln["date"].month == m_cur and (not y_cur or ln["date"].year == y_cur)]
            if in_month:
                skipped = len(lines) - len(in_month)
                if skipped:
                    gl_note = f"{mf.num(skipped)} GL lines dated outside {cur_name} were left out."
                lines = in_month
        gl_by_entity = by_entity and any(ln["entity"] for ln in lines)
        for ln in lines:
            by_acct[(ln["account"], ln["entity"] if gl_by_entity else "")].append(ln)

    owner_rules = read_owners(a.owners)
    results = []
    for f in flagged:
        gl_lines = None
        if gl:
            gl_lines = by_acct.get(f["key"], []) if (by_entity and any(k[1] for k in by_acct)) else by_acct.get((f["account"], ""), [])
        res = review_account(f, gl_lines, bool(gl and gl["has_journal"]), cur_name, sym)
        if gl_lines:
            net = sum((ln["amount"] for ln in gl_lines), D0)
            expected = f["current"] if f["type"] in ("revenue", "expense") else f["change"]
            res["gl_net"] = net
            res["gl_ties"] = abs(net - expected) < Decimal("0.5")
        f["owner"] = owner_for(f["account"], owner_rules) if res["status"] == "owner" else ""
        results.append(dict(f, **res))

    def order(f: Dict[str, Any]) -> Tuple[Decimal, Decimal]:
        r = f["ratio"]
        return (-(abs(r) if r is not None else Decimal("1e9")), -abs(f["change"]))

    owners = sorted([f for f in results if f["status"] == "owner"], key=order)
    explained = sorted([f for f in results if f["status"] == "explained"], key=order)

    K = lambda x, s=False: mf.money(x, unit="K", decimals=1, currency=sym, signed=s)   # noqa: E731
    P = lambda r: "new" if r is None else mf.pct(r, signed=True)                         # noqa: E731
    thr = f"{threshold_text(amount, sym)} and {pct_text(pct_thr)}"
    n, e, o = len(flagged), len(explained), len(owners)

    # ---- headline
    if n == 0:
        headline = f"No account moved more than {thr} from {pri_name}."
    elif gl is None:
        headline = (f"{n} {plural(n, 'account', 'accounts')} moved more than {thr} from {pri_name}. "
                    f"Add the {cur_name} GL export (--gl) to find their causes.")
    else:
        headline = (f"{n} {plural(n, 'account', 'accounts')} moved more than {thr} from {pri_name}. "
                    f"{e} {plural(e, 'has', 'have')} a clear cause in {plural(e, 'its', 'their')} memo lines; "
                    f"{o} {plural(o, 'needs', 'need')} an owner.")

    owner_rows = [[cell(f["label"]), K(f["prior"]), K(f["current"]), K(f["change"], True), cell(f["shows"]), f["owner"]]
                  for f in owners]
    expl_rows = [[cell(f["label"]), K(f["prior"]), K(f["current"]), K(f["change"], True), cell(f["cause"])] for f in explained]
    out_md = [headline]
    if owner_rows:
        out_md += ["", "**Need an owner**", "",
                   mf.md_table(["Account", pri_col, cur_col, "Change", "What the ledger shows", "Ask"], owner_rows,
                               align=["l", "r", "r", "r", "l", "l"])]
    if expl_rows:
        out_md += ["", "**Clear cause in the memo lines**", "",
                   mf.md_table(["Account", pri_col, cur_col, "Change", "Cause (memo line)"], expl_rows,
                               align=["l", "r", "r", "r", "l"])]

    # ---- P&L summary
    pnl = pnl_summary(cur, pri, signed)
    pnl_block: List[str] = []
    if pnl:
        pr, cu = pnl["prior"], pnl["current"]

        def chg(x: Decimal, y: Decimal) -> Tuple[str, str]:
            return mf.money(y - x, currency=sym, signed=True), ("" if x == 0 else mf.pct((y - x) / abs(x), signed=True))

        rows = []
        for label, k in (("Revenue", "revenue"), ("EBITDA", "ebitda"), ("Cash (month end)", "cash")):
            c1, c2 = chg(pr[k], cu[k])
            rows.append([label, mf.money(pr[k], currency=sym), mf.money(cu[k], currency=sym), c1, c2])
            if k == "revenue":
                rows.append(["Gross margin", mf.pct(pr["gross_margin"]), mf.pct(cu["gross_margin"]),
                             mf.pts((cu["gross_margin"] - pr["gross_margin"]) * 100), ""])
            if k == "ebitda":
                rows.append(["EBITDA margin", mf.pct(pr["ebitda_margin"]), mf.pct(cu["ebitda_margin"]),
                             mf.pts((cu["ebitda_margin"] - pr["ebitda_margin"]) * 100), ""])
        pnl_block = ["", f"**P&L summary** ({pri_col} and {cur_col} activity; cash at month end)", "",
                     mf.md_table(["", pri_col, cur_col, "Change", "Change %"], rows)]
        out_md += pnl_block

    # ---- notes
    notes = []
    untied = [f["label"] for f in results if f.get("gl_ties") is False]
    if untied:
        notes.append(f"Heads up: the GL lines for {', '.join(untied)} do not add up to the trial-balance movement; "
                     f"the GL export may be partial.")
    if gl_note:
        notes.append(gl_note)
    if cur["types_from_numbers"]:
        notes.append("Account types came from the account numbers: 1 assets, 2 liabilities, 3 equity, 4 revenue, 5–9 expenses.")
    notes.append(f"Materiality: {thr} ({thr_source}).")

    # ---- files
    out_dir = a.out or os.getcwd()
    os.makedirs(out_dir, exist_ok=True)
    review_name = f"close_review_{mon}.md" if mon else "close_review.md"
    review_path = os.path.join(out_dir, review_name)
    questions_path = os.path.join(out_dir, "owner_questions.csv")

    by_owner: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for f in owners:
        by_owner[f["owner"]].append(f)
    q_rows = []
    for owner, fs in by_owner.items():
        parts = [f"{f['label']} went from {K(f['prior'])} in {pri_col} to {K(f['current'])} in {cur_col}. {f['ask']}" for f in fs]
        q_rows.append([owner, "; ".join(f["label"] for f in fs), " ".join(parts)])
    mf.write_csv(questions_path, ["owner", "accounts", "question"], q_rows)

    full = [f"# Close review: {cur_col} against {pri_col}", "", headline, "",
            f"Files: {os.path.basename(a.current)} ({cur_col}), {os.path.basename(a.prior)} ({pri_col})"
            + (f", {os.path.basename(a.gl)} ({mf.num(len(gl['lines']))} GL lines)" if gl else "") + ".",
            f"Materiality: {thr} ({thr_source}). An account is flagged when its change exceeds both."]
    if owners:
        full += ["", "## Need an owner", "",
                 mf.md_table(["Account", pri_col, cur_col, "Change", "Change %", "What the ledger shows", "Journals", "Ask"],
                             [[cell(f["label"]), K(f["prior"]), K(f["current"]), K(f["change"], True), P(f["ratio"]),
                               cell(f["shows"]), ", ".join(f.get("journals", [])), f["owner"]] for f in owners],
                             align=["l", "r", "r", "r", "r", "l", "l", "l"])]
    if explained:
        full += ["", "## Clear cause in the memo lines", "",
                 mf.md_table(["Account", pri_col, cur_col, "Change", "Change %", "Cause (memo line)", "Journal"],
                             [[cell(f["label"]), K(f["prior"]), K(f["current"]), K(f["change"], True), P(f["ratio"]),
                               cell(f["cause"]), ", ".join(f.get("journals", []))] for f in explained],
                             align=["l", "r", "r", "r", "r", "l", "l"])]
    if q_rows:
        full += ["", "## Questions by owner", ""] + [f"- **{r[0]}**: {r[2]}" for r in q_rows]
    full += pnl_block
    full += ["", "Memo lines are quoted as data from the GL export. Amounts are in each account's sign as exported."]
    with open(review_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(full) + "\n")

    rel = lambda pth: os.path.relpath(pth, os.getcwd()) if a.out else os.path.basename(pth)   # noqa: E731
    out_md += ["", f"Wrote {rel(review_path)} ({n} {plural(n, 'account', 'accounts')}) and {rel(questions_path)} "
                   f"({len(q_rows)} {plural(len(q_rows), 'owner', 'owners')})."]
    out_md += notes

    def js(f: Dict[str, Any]) -> Dict[str, Any]:
        keep = {k: v for k, v in f.items() if k not in ("key",)}
        for k in ("prior", "current", "change", "natural_change", "ratio", "gl_net"):
            if keep.get(k) is not None:
                keep[k] = str(keep[k])
        return keep

    data = {
        "skill": "close-review",
        "files": {"current": a.current, "prior": a.prior, "gl": a.gl, "review": review_path, "questions": questions_path},
        "period": {"current": cur_col, "prior": pri_col},
        "thresholds": {"amount": str(amount), "pct": str(pct_thr), "source": thr_source},
        "sign_convention": "signed" if signed else "natural",
        "counts": {"accounts": len(kc), "flagged": n, "explained": e, "needs_owner": o},
        "headline": headline,
        "needs_owner": [js(f) for f in owners],
        "explained": [js(f) for f in explained],
        "questions": [{"owner": r[0], "accounts": r[1], "question": r[2]} for r in q_rows],
        "pnl": None if not pnl else {
            k: ({kk: str(vv) for kk, vv in v.items()} if isinstance(v, dict) else v) for k, v in pnl.items()},
    }
    mf.emit("\n".join(out_md), data, os.path.join(mf.magnos_dir(), "runs", "close-review.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
