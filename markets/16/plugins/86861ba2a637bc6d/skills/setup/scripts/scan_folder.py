#!/usr/bin/env python3
"""Profile the CSV and XLSX files in the working folder and propose the finance profile.

Finds the entities, currencies and periods in the files. When two trial
balances are there, counts how many accounts moved at least each candidate
materiality between them ("41 of 180 moved this much last month").

Prints Markdown; saves the machine result to .magnos/runs/setup.json, which
write_profile.py reads for the entities.

  python3 scripts/scan_folder.py              every table file in the working folder (two levels deep)
  python3 scripts/scan_folder.py data/ tb.csv  only these folders and files (inside the working folder)
"""
from __future__ import annotations

import argparse
import datetime as _dt
import os
import re
import sys
from collections import Counter
from decimal import Decimal
from typing import Any, Dict, List, Optional, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import magnos_fin as mf  # noqa: E402

TABLE_EXT = (".csv", ".tsv", ".xlsx", ".xlsm")
SKIP_DIRS = {".git", ".magnos", "node_modules", "__pycache__", ".venv", "venv", "media", ".idea", ".vscode"}
MAX_DEPTH = 2
MAX_BYTES = 50 * 1024 * 1024
MAX_SHEETS = 10
CANDIDATES = [(Decimal(25000), Decimal(10)), (Decimal(10000), Decimal(5)), (Decimal(50000), Decimal(15))]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November", "December"]
SYMBOLS = {"$": "USD", "€": "EUR", "£": "GBP"}
ISO_HINT = re.compile(r"(?<![a-z])(usd|eur|gbp|cad|aud|chf|jpy|sek|nok|dkk|inr|sgd|nzd|zar|mxn|brl|try|pln|hkd|cny)(?![a-z])")


def fail(msg: str) -> None:
    print(msg, file=sys.stderr)
    sys.exit(2)


# ---------------------------------------------------------------- files


def inside(path: str, root: str) -> bool:
    path, root = os.path.realpath(path), os.path.realpath(root)
    return path == root or path.startswith(root + os.sep)


def find_files(targets: List[str], cwd: str) -> Tuple[List[str], List[str]]:
    """Table files to read, and notes about files skipped."""
    found: List[str] = []
    notes: List[str] = []
    for t in targets:
        full = os.path.abspath(os.path.join(cwd, t))
        if not inside(full, cwd):
            fail(f"{t} is outside the working folder; name a file or folder inside {cwd}.")
        if not os.path.exists(full):
            fail(f"{t} does not exist; name a file or folder inside the working folder.")
        if os.path.isfile(full):
            found.append(full)
            continue
        base_depth = full.rstrip(os.sep).count(os.sep)
        for dirpath, dirnames, filenames in os.walk(full):
            dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS and not d.startswith("."))
            if dirpath.count(os.sep) - base_depth >= MAX_DEPTH:
                dirnames[:] = []
            for f in sorted(filenames):
                if f.lower().endswith(TABLE_EXT) and not f.startswith(("~$", ".")):
                    found.append(os.path.join(dirpath, f))
    out = []
    for f in dict.fromkeys(found):
        if os.path.getsize(f) > MAX_BYTES:
            notes.append(f"{os.path.relpath(f, cwd)} skipped: larger than 50 MB")
        else:
            out.append(f)
    return out, notes


def read_tables(path: str) -> List[mf.Table]:
    if path.lower().endswith((".xlsx", ".xlsm")):
        wb = mf.read_xlsx(path)
        return [mf.read_table(path, s) for s in wb.sheet_names[:MAX_SHEETS]]
    return [mf.read_table(path)]


# ---------------------------------------------------------------- columns


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


def pick_column(t: mf.Table, exact: Tuple[str, ...], contains: Tuple[str, ...] = (),
                avoid: Tuple[str, ...] = ()) -> Optional[str]:
    norms = [(c, _norm(c)) for c in t.columns]
    for want in exact:
        for c, n in norms:
            if n == want:
                return c
    for want in contains:
        for c, n in norms:
            if want in n and not any(a in n for a in avoid):
                return c
    return None


def entity_values(t: mf.Table) -> List[str]:
    col = pick_column(t, ("entity", "entitycode", "entityname", "legalentity", "subsidiary", "companycode"),
                      ("entity", "subsidiary"), ("identity",))
    if not col or t.kind(col) not in ("text", "number"):
        return []
    vals = [v.strip() for v in t.col(col) if v.strip()]
    distinct = list(dict.fromkeys(vals))
    if not distinct or len(distinct) > 12 or any(len(v) > 40 for v in distinct):
        return []
    return distinct


def currency_rows(t: mf.Table) -> Counter:
    """Rows per currency: a currency column, else a code in a header, else symbols in the amounts."""
    out: Counter = Counter()
    col = pick_column(t, ("currency", "currencycode", "ccy", "curr", "isocurrency", "transactioncurrency",
                          "reportingcurrency"), ("currency",))
    if col:
        for v in t.col(col):
            v = v.strip()
            if re.fullmatch(r"[A-Za-z]{3}", v):
                out[v.upper()] += 1
            elif v in SYMBOLS:
                out[SYMBOLS[v]] += 1
        if out:
            return out
    for c in t.columns:
        m = ISO_HINT.search(str(c).lower())
        if m and t.kind(c) == "number":
            out[m.group(1).upper()] += len(t)
            return out
    for c in t.columns:
        for v in t.col(c)[:5000]:
            s = v.strip()
            for sym, code in SYMBOLS.items():
                if s and (s.lstrip("(-−").startswith(sym) or s.endswith(sym)) and mf.to_decimal(s) is not None:
                    out[code] += 1
    return out


_MONTH_HEADER = re.compile(r"^([A-Za-z]{3,9})\.?[\s\-'/_]*(\d{2}|\d{4})$")


def header_month(h: str) -> Optional[_dt.date]:
    s = str(h).strip()
    d = mf.parse_date(s)
    if d is not None and mf.to_decimal(s) is None:
        return d.replace(day=1)
    m = _MONTH_HEADER.match(s)
    if m:
        key = m.group(1).lower()
        months = {n.lower(): i + 1 for i, n in enumerate(MONTHS)}
        months.update({n[:3].lower(): i + 1 for i, n in enumerate(MONTHS)})
        months["sept"] = 9
        if key in months:
            y = int(m.group(2))
            return _dt.date(y + 2000 if y < 100 else y, months[key], 1)
    return None


PREFERRED_DATE_NAMES = ("period", "postingdate", "date", "month", "transactiondate", "invoicedate", "gldate",
                        "accountingdate", "postdate", "entrydate", "closedate", "documentdate")


def date_span(t: mf.Table) -> Tuple[Optional[_dt.date], Optional[_dt.date]]:
    """First and last date in the table's period or date columns."""
    cols: List[Tuple[str, bool]] = []  # (column, values are Excel serials)
    for c in t.columns:
        n = _norm(c)
        kind = t.kind(c)
        if kind == "date":
            cols.append((c, False))
        elif kind == "number" and any(k in n for k in ("date", "period", "month")):
            sample = [mf.to_decimal(v) for v in t.col(c)[:200] if v.strip()]
            if sample and all(x is not None and 20000 < x < 80000 for x in sample):
                cols.append((c, True))
    preferred = [x for x in cols if _norm(x[0]) in PREFERRED_DATE_NAMES]
    use = preferred or cols
    first = last = None
    for c, serial in use:
        for v in t.col(c):
            if not v.strip():
                continue
            d = mf.parse_date(str(int(float(v))) if serial else v)
            if d is None:
                continue
            first = d if first is None or d < first else first
            last = d if last is None or d > last else last
    months = [m for m in (header_month(h) for h in t.columns) if m]
    if len(months) >= 3:
        lo, hi = min(months), mf.month_end(max(months))
        first = lo if first is None or lo < first else first
        last = hi if last is None or hi > last else last
    return first, last


def fiscal_hint(t: mf.Table) -> Optional[int]:
    """The fiscal year's first month, from 12 month headers in a row or a fiscal period column."""
    months = [header_month(h) for h in t.columns]
    run: List[_dt.date] = []
    for m in months:
        if m is None:
            if len(run) >= 12:
                break
            run = []
            continue
        if run and (m.year * 12 + m.month) != (run[-1].year * 12 + run[-1].month) + 1:
            if len(run) >= 12:
                break
            run = []
        run.append(m)
    if len(run) == 12:
        return run[0].month
    fp = pick_column(t, ("fiscalperiod", "periodnumber", "fiscalmonth", "fp", "periodno"))
    if fp:
        dcol = next((c for c in t.columns if t.kind(c) == "date"), None)
        if dcol:
            firsts = Counter()
            for row in t.rows:
                if str(row.get(fp, "")).strip() in ("1", "01", "P1", "p1", "P01"):
                    d = mf.parse_date(row.get(dcol, ""))
                    if d:
                        firsts[d.month] += 1
            if firsts:
                return firsts.most_common(1)[0][0]
    return None


# ---------------------------------------------------------------- trial balances


_MON_TOKEN = re.compile(
    r"(?<![a-z])(january|february|march|april|may|june|july|august|september|october|november|december"
    r"|jan|feb|mar|apr|jun|jul|aug|sept|sep|oct|nov|dec)(?![a-z])(?:[\s_\-]*(20\d\d|\d\d)(?!\d))?")
_YM_TOKEN = re.compile(r"(?<!\d)(20\d\d)[\s_\-]?(0[1-9]|1[0-2])(?!\d)")


def period_from_name(path: str) -> Optional[Tuple[Optional[int], int]]:
    name = os.path.splitext(os.path.basename(path))[0].lower()
    m = _YM_TOKEN.search(name)
    if m:
        return int(m.group(1)), int(m.group(2))
    m = _MON_TOKEN.search(name)
    if m:
        mon = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
        tok = "sep" if m.group(1) == "sept" else m.group(1)[:3]
        y = m.group(2)
        year = None if not y else (int(y) + 2000 if len(y) == 2 else int(y))
        return year, mon.index(tok) + 1
    return None


def trial_balance(t: mf.Table) -> Optional[Dict[str, Any]]:
    """Balances by (entity, account) when the table looks like a trial balance."""
    acct = pick_column(t, ("account", "accountnumber", "accountno", "acct", "acctno", "glaccount", "accountcode",
                           "accountid", "glcode"), ("account", "acct"),
                       ("name", "desc", "type", "categ", "group", "class", "title"))
    if not acct:
        return None
    bal = pick_column(t, ("balance", "endingbalance", "closingbalance", "netbalance", "net", "amount", "ytdbalance",
                          "periodend", "value"), ("balance",), ("opening", "beginning", "begin"))
    debit = pick_column(t, ("debit", "debits", "dr"), ("debit",))
    credit = pick_column(t, ("credit", "credits", "cr"), ("credit",))
    use_dc = bool(debit and credit and t.kind(debit) == "number" and t.kind(credit) == "number")
    if not use_dc and (not bal or t.kind(bal) != "number"):
        return None
    ent_col = pick_column(t, ("entity", "entitycode", "entityname", "legalentity", "subsidiary", "companycode"),
                          ("entity", "subsidiary"), ("identity",))
    balances: Dict[Tuple[str, str], Decimal] = {}
    rows = 0
    for row in t.rows:
        a = str(row.get(acct, "")).strip()
        if not a or a.lower().startswith("total"):
            continue
        if use_dc:
            v = (mf.to_decimal(row.get(debit)) or mf.D0) - (mf.to_decimal(row.get(credit)) or mf.D0)
        else:
            v = mf.to_decimal(row.get(bal))
            if v is None:
                continue
        key = (str(row.get(ent_col, "")).strip() if ent_col else "", a)
        balances[key] = balances.get(key, mf.D0) + v
        rows += 1
    if rows < 5 or len(balances) < 0.9 * rows:
        return None  # many rows per account: a ledger, not a trial balance
    looks = (re.search(r"(?<![a-z])(tb|trial)", os.path.basename(t.path).lower())
             or (bal and "balance" in _norm(bal)) or use_dc)
    if not looks:
        return None
    return {"balances": balances, "entity_column": ent_col or ""}


def tb_period(path: str, t: mf.Table) -> Optional[Tuple[Optional[int], int]]:
    pcol = pick_column(t, ("period", "periodend", "asof", "asofdate", "date", "month"))
    if pcol:
        dates = [d for d in (mf.parse_date(v) for v in t.col(pcol)) if d]
        if dates:
            d = max(dates)
            return d.year, d.month
    return period_from_name(path)


def order_pair(a: Tuple[Optional[int], int], b: Tuple[Optional[int], int]) -> bool:
    """True when period a is earlier than period b."""
    ya, ma = a
    yb, mb = b
    if ya is not None and yb is not None:
        return (ya, ma) < (yb, mb)
    if abs(ma - mb) > 6:  # Dec then Jan: the year turned
        return ma > mb
    return ma < mb


def period_label(p: Tuple[Optional[int], int]) -> str:
    y, m = p
    return f"{MONTHS[m - 1][:3]} {y}" if y else MONTHS[m - 1][:3]


def moves(prior: Dict[Tuple[str, str], Decimal], current: Dict[Tuple[str, str], Decimal],
          candidates: List[Tuple[Decimal, Decimal]]) -> Tuple[int, List[Dict[str, Any]]]:
    keys = set(prior) | set(current)
    out = []
    for amt, pct in candidates:
        n = 0
        for k in keys:
            p, c = prior.get(k, mf.D0), current.get(k, mf.D0)
            diff = abs(c - p)
            if diff < amt:
                continue
            if p == 0 or diff / abs(p) * 100 >= pct:
                n += 1
        out.append({"amount": amt, "pct": pct, "accounts_moved": n})
    return len(keys), out


# ---------------------------------------------------------------- main


def symbol(code: str) -> str:
    return {"USD": "$", "EUR": "€", "GBP": "£"}.get(code, code + " ")


def option_label(amt: Decimal, pct: Decimal, code: str) -> str:
    return f"{mf.money(amt, currency=symbol(code))} and {mf.num(pct, 2 if pct != pct.to_integral() else 0)}%"


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Profile the table files in the working folder and propose the finance profile.")
    p.add_argument("paths", nargs="*", default=["."], help="folders or files inside the working folder (default: the working folder)")
    p.add_argument("--json", default=os.path.join(".magnos", "runs", "setup.json"), help="where to save the machine result")
    a = p.parse_args(argv)
    cwd = os.getcwd()
    files, notes = find_files(a.paths, cwd)
    profile = mf.load_profile(cwd)
    has_profile = profile.get("_source") != "defaults"

    per_file: List[Dict[str, Any]] = []
    entities: List[str] = []
    currencies: Counter = Counter()
    currency_files: Counter = Counter()
    first = last = None
    fiscal_hints: Counter = Counter()
    tbs: List[Dict[str, Any]] = []
    for f in files:
        rel = os.path.relpath(f, cwd)
        try:
            tables = read_tables(f)
        except Exception as e:  # a broken or locked file should not stop the scan
            notes.append(f"{rel} skipped: could not be read ({type(e).__name__})")
            continue
        f_rows = 0
        f_ents: List[str] = []
        f_cur: Counter = Counter()
        f_first = f_last = None
        for t in tables:
            if not t.columns:
                continue
            f_rows += len(t)
            for e in entity_values(t):
                if e not in f_ents:
                    f_ents.append(e)
            f_cur.update(currency_rows(t))
            lo, hi = date_span(t)
            if lo and (f_first is None or lo < f_first):
                f_first = lo
            if hi and (f_last is None or hi > f_last):
                f_last = hi
            h = fiscal_hint(t)
            if h:
                fiscal_hints[h] += 1
            tb = trial_balance(t)
            if tb:
                tb.update({"file": rel, "period": tb_period(f, t), "sheet": t.sheet})
                tbs.append(tb)
        for e in f_ents:
            if e not in entities:
                entities.append(e)
        currencies.update(f_cur)
        for code in f_cur:
            currency_files[code] += 1
        if f_first and (first is None or f_first < first):
            first = f_first
        if f_last and (last is None or f_last > last):
            last = f_last
        per_file.append({
            "file": rel, "rows": f_rows, "entities": f_ents,
            "currencies": [c for c, _ in f_cur.most_common()],
            "first": f_first.isoformat() if f_first else None, "last": f_last.isoformat() if f_last else None,
            "trial_balance": any(tb["file"] == rel for tb in tbs),
        })

    # the proposals: current answers first when a profile exists
    found_currency = currencies.most_common(1)[0][0] if currencies else None
    hint = fiscal_hints.most_common(1)[0][0] if fiscal_hints else None
    if has_profile:
        fy = str(profile["fiscal_year_start"])
        fy_why = "your current profile"
    elif hint:
        fy = MONTHS[hint - 1]
        fy_why = "a 12-month budget or a fiscal period column starts in this month"
    else:
        fy = "January"
        fy_why = "no fiscal calendar in the files; calendar year"
    if has_profile:
        cur, cur_why = str(profile["currency"]), "your current profile"
    elif found_currency:
        cur = found_currency
        others = [c for c in currencies if c != cur]
        cur_why = f"{currency_files[cur]} of {len(per_file)} files" + (f"; also found {', '.join(others)}" if others else "")
    else:
        cur, cur_why = "USD", "no currency in the files; the default"
    amt = profile["materiality_amount"] if has_profile else Decimal(25000)
    pct = profile["materiality_pct"] if has_profile else Decimal(10)
    sign = str(profile["variance_sign"]) if has_profile else "favourable-positive"

    candidates = list(CANDIDATES)
    if (amt, pct) not in candidates:
        candidates.insert(0, (amt, pct))
    comparison = None
    dated = [tb for tb in tbs if tb["period"]]
    pair: Optional[Tuple[Dict[str, Any], Dict[str, Any]]] = None
    order_note = ""
    if len(dated) >= 2:
        ordered = list(dated)
        for i in range(len(ordered)):  # a small sort with the year-turn rule
            for j in range(len(ordered) - 1 - i):
                if order_pair(ordered[j + 1]["period"], ordered[j]["period"]):
                    ordered[j], ordered[j + 1] = ordered[j + 1], ordered[j]
        pair = (ordered[-2], ordered[-1])
    elif len(tbs) == 2:
        pair = tuple(sorted(tbs, key=lambda x: x["file"]))  # type: ignore[assignment]
        order_note = "the order comes from the file names"
    if pair:
        prior, current = pair
        n_accounts, counts = moves(prior["balances"], current["balances"], candidates)
        comparison = {
            "prior": prior["file"], "current": current["file"],
            "prior_period": period_label(prior["period"]) if prior["period"] else None,
            "current_period": period_label(current["period"]) if current["period"] else None,
            "accounts": n_accounts, "options": counts, "note": order_note,
        }

    # ---------------------------------------------------------------- the report
    lines: List[str] = []
    if not per_file:
        lines.append("No CSV or XLSX files found in this folder. The profile can still be set: answer the four questions.")
    else:
        ent = (f"{len(entities)} entit{'y' if len(entities) == 1 else 'ies'} ({', '.join(entities)})"
               if entities else "no entity column")
        if currencies:
            codes = [c for c, _ in currencies.most_common()]
            curp = f"amounts in {codes[0]}" if len(codes) == 1 else f"amounts in {', '.join(codes)} (more than one currency)"
        else:
            curp = "no currency stated"
        span = f"periods {mf.month_label(first)} – {mf.month_label(last)}" if first and last else "no dates found"
        lines.append(f"Found {len(per_file)} file{'s' if len(per_file) != 1 else ''}: {ent}, {curp}, {span}.")
        lines.append("")
        rows = []
        for pf in per_file:
            per = "—"
            if pf["first"] and pf["last"]:
                per = f"{mf.month_label(_dt.date.fromisoformat(pf['first']))} – {mf.month_label(_dt.date.fromisoformat(pf['last']))}"
            rows.append([pf["file"] + (" (trial balance)" if pf["trial_balance"] else ""), mf.num(pf["rows"]),
                         ", ".join(pf["entities"]) or "—", ", ".join(pf["currencies"]) or "—", per])
        lines.append(mf.md_table(["File", "Rows", "Entities", "Currency", "Periods"], rows, ["l", "r", "l", "l", "l"]))
    if has_profile:
        lines += ["", f"Current profile: {mf.profile_line(profile)} (.magnos/finance.md). Its answers are the defaults."]
    mat_why = "the Magnos default"
    if comparison:
        first_opt = next(o for o in comparison["options"] if (o["amount"], o["pct"]) == (amt, pct))
        span_txt = (f"from {comparison['prior_period']} to {comparison['current_period']}"
                    if comparison["prior_period"] else f"from {comparison['prior']} to {comparison['current']}")
        mat_why = f"{first_opt['accounts_moved']} of {comparison['accounts']} accounts moved this much {span_txt}"
    if has_profile:
        mat_why = "your current profile" + ("; " + mat_why if comparison else "")
    sign_label = {"favourable-positive": "Favourable positive", "actual-minus-budget": "Actual minus budget"}.get(sign, sign)
    lines += ["", "Proposed answers:", "", mf.md_table(["Question", "Proposed", "Why"], [
        ["Fiscal year starts in", fy, fy_why],
        ["Reporting currency", cur, cur_why],
        ["Materiality for close reviews", option_label(amt, pct, cur), mat_why],
        ["Variances are signed", sign_label, "your current profile" if has_profile else "the Magnos default"],
    ], ["l", "l", "l"])]
    if comparison:
        head = (f"Materiality options, on {comparison['prior']} → {comparison['current']} "
                f"({mf.num(comparison['accounts'])} accounts{'; ' + comparison['note'] if comparison['note'] else ''}):")
        lines += ["", head, "", mf.md_table(["Option", "Accounts that moved this much"], [
            [option_label(o["amount"], o["pct"], cur), f"{mf.num(o['accounts_moved'])} of {mf.num(comparison['accounts'])}"]
            for o in comparison["options"]])]
    elif len(tbs) < 2:
        lines += ["", "No two trial balances to compare, so no account counts for the materiality options."]
    if notes:
        lines += ["", "Skipped: " + "; ".join(notes) + "."]

    data = {
        "folder": cwd,
        "files": per_file,
        "entities": entities,
        "currencies": dict(currencies),
        "first": first.isoformat() if first else None,
        "last": last.isoformat() if last else None,
        "fiscal_year_start_hint": MONTHS[hint - 1] if hint else None,
        "trial_balances": comparison,
        "current_profile": {k: (str(v) if isinstance(v, Decimal) else v) for k, v in profile.items()} if has_profile else None,
        "proposals": {
            "fiscal_year_start": fy, "currency": cur, "materiality_amount": str(amt), "materiality_pct": str(pct),
            "variance_sign": sign, "entities": ", ".join(entities) if entities else (str(profile.get("entities", "")) if has_profile else ""),
        },
        "notes": notes,
    }
    mf.emit("\n".join(lines), data, os.path.join(cwd, a.json))
    return 0


if __name__ == "__main__":
    sys.exit(main())
