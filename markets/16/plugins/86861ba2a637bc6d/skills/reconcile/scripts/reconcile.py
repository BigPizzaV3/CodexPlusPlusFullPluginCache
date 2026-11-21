#!/usr/bin/env python3
"""Bank reconciliation: match bank statement lines to the cash ledger, group
what is left, and tie the bank balance to the ledger balance.

  python3 scripts/reconcile.py bank_sep.csv gl_cash_sep.csv [--days 3] [--later bank_oct.csv]

Matching, one bank line to one ledger line:
1. exact amount, dates within --days (default 3); among equal candidates, a
   shared reference wins, then the closest date;
2. what is left, on a reference: the check number, or the ledger's reference
   (invoice, payment or wire reference) found on the bank line. Same amount:
   matched. Different amount: an amount difference.

Open items are grouped: in the ledger but not cleared by the bank (checks and
payments, or deposits), in the bank but not booked (bank fees; payouts, refunds
and other items), and amount differences. The tie-out checks that the open
items explain the whole difference between the two balances.

Prints Markdown; writes recon_<mon>.xlsx (Matched, Open items, Draft journal)
to the working folder (or --out) and the full result to .magnos/runs/reconcile.json.
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
WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}
FEE_RE = re.compile(r"\b(fee|fees|service charge|analysis charge|maintenance charge|wire charge|bank charge|overdraft|nsf)\b",
                    re.I)
CHECK_RE = re.compile(r"\b(check|cheque|chk)\b", re.I)
PROCESSORS = ["Stripe", "PayPal", "Adyen", "Shopify", "Square", "Braintree", "GoCardless", "Amazon", "Checkout.com"]


class InputError(Exception):
    pass


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    sys.exit(2)


# ---------------------------------------------------------------- reading


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


def pick(t: mf.Table, exact: Sequence[str], contains: Sequence[str] = (), exclude: Sequence[str] = (),
         taken: Sequence[Optional[str]] = ()) -> Optional[str]:
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


def read(path: str, what: str) -> mf.Table:
    if not os.path.exists(path):
        raise InputError(f"Cannot find {path}. Check the file name, or put the {what} in the working folder.")
    try:
        t = mf.read_table(path)
    except Exception:
        raise InputError(f"Cannot read {os.path.basename(path)}. Save the {what} as CSV, TSV or XLSX.")
    if not t.rows:
        raise InputError(f"{os.path.basename(path)} has no rows. Export the {what} again with its lines.")
    return t


def read_lines(path: str, side: str) -> Dict[str, Any]:
    """side: 'bank' (amount = deposits − withdrawals) or 'ledger' (amount = debits − credits)."""
    what = "bank statement" if side == "bank" else "cash ledger"
    t = read(path, what)
    base = os.path.basename(path)
    c_date = pick(t, ["posting date", "date", "transaction date", "value date", "booking date", "post date",
                      "effective date", "gl date"], ["date"])
    if not c_date:
        raise InputError(f"{base} has no date column. Export the {what} with the date of each line.")
    taken: List[Optional[str]] = [c_date]
    c_amt = pick(t, ["amount", "transaction amount", "net amount", "signed amount", "value"], ["amount"],
                 exclude=["balance"], taken=taken)
    c_in = c_out = None
    if not c_amt:
        if side == "bank":
            c_in = pick(t, ["deposits", "deposit", "credit", "credits", "money in", "paid in", "credit amount"],
                        ["deposit", "credit"], taken=taken)
            c_out = pick(t, ["withdrawals", "withdrawal", "debit", "debits", "money out", "paid out", "debit amount"],
                         ["withdraw", "debit"], taken=taken)
        else:
            c_in = pick(t, ["debit", "debits", "dr", "debit amount"], ["debit"], taken=taken)
            c_out = pick(t, ["credit", "credits", "cr", "credit amount"], ["credit"], taken=taken)
        if not (c_in and c_out):
            raise InputError(f"{base} has no amount column. Export the {what} with an amount column, "
                             f"or with {'deposit and withdrawal' if side == 'bank' else 'debit and credit'} columns.")
    taken += [c_amt, c_in, c_out]
    c_bal = pick(t, ["balance", "running balance", "ledger balance", "closing balance", "end balance"], ["balance"],
                 exclude=["available"], taken=taken)
    taken.append(c_bal)
    if side == "bank":
        c_ref = pick(t, ["check or slip #", "check number", "check no", "check #", "cheque number", "cheque no",
                         "reference", "ref", "ref no", "reference number", "bank reference", "transaction reference"],
                     ["check", "cheque", "ref"], taken=taken)
        taken.append(c_ref)
        c_desc = pick(t, ["description", "transaction description", "narrative", "memo", "payee", "name", "particulars",
                          "details", "text"], ["descr", "narrat", "memo"], taken=taken)
        taken.append(c_desc)
        c_type = pick(t, ["type", "transaction type"], taken=taken)
        c_name = c_memo = c_jnl = c_acct = None
    else:
        c_ref = pick(t, ["reference", "ref", "ref no", "reference number", "check number", "check no", "check #",
                         "document number", "doc number", "doc no", "num", "number"], ["ref"], taken=taken)
        taken.append(c_ref)
        c_acct = pick(t, ["account", "account number", "gl account", "account code"], taken=taken)
        taken.append(c_acct)
        c_jnl = pick(t, ["journal", "journal id", "journal number", "entry", "transaction id", "document"], ["journal"],
                     taken=taken)
        taken.append(c_jnl)
        c_type = pick(t, ["type", "transaction type", "source"], taken=taken)
        taken.append(c_type)
        c_name = pick(t, ["name", "payee", "vendor", "customer", "counterparty"], taken=taken)
        taken.append(c_name)
        c_memo = pick(t, ["memo", "description", "narrative", "details", "line memo", "memo description"],
                      ["memo", "descr"], taken=taken)
        c_desc = None
    lines: List[Dict[str, Any]] = []
    bad_dates = 0
    for i, r in enumerate(t.rows):
        if c_amt:
            amt = mf.to_decimal(r.get(c_amt, ""))
        else:
            a_in, a_out = mf.to_decimal(r.get(c_in, "")), mf.to_decimal(r.get(c_out, ""))
            amt = None if a_in is None and a_out is None else (a_in or D0) - abs(a_out or D0)
        if amt is None or amt == 0:
            continue
        d = mf.parse_date(r.get(c_date, ""))
        if d is None:
            bad_dates += 1
        if side == "bank":
            desc = " ".join(str(r.get(c_desc, "")).split()) if c_desc else ""
            name = memo = ""
        else:
            name = str(r.get(c_name, "")).strip() if c_name else ""
            memo = " ".join(str(r.get(c_memo, "")).split()) if c_memo else ""
            desc = memo if not name or name.lower() in memo.lower() else (f"{name} — {memo}" if memo else name)
        lines.append({
            "i": i, "date": d, "amount": amt, "desc": desc, "name": name, "memo": memo,
            "ref": str(r.get(c_ref, "")).strip() if c_ref else "",
            "type": str(r.get(c_type, "")).strip() if c_type else "",
            "journal": str(r.get(c_jnl, "")).strip() if c_jnl else "",
            "account": str(r.get(c_acct, "")).strip() if c_acct else "",
            "balance": mf.to_decimal(r.get(c_bal, "")) if c_bal else None,
        })
    if not lines:
        raise InputError(f"{base} has no lines with an amount. Export the {what} again with its lines.")
    if bad_dates > 0.05 * len(lines):
        raise InputError(f"{base}: the column {c_date} holds values that are not dates. Export dates as dates.")
    return {"path": path, "lines": lines, "has_balance": bool(c_bal)}


def balances(side: Dict[str, Any]) -> Tuple[Optional[Decimal], Optional[Decimal], bool]:
    """(opening, closing, consistent) from the running balance column, in whatever order the file lists lines."""
    ls = [x for x in side["lines"] if x["date"]]
    if not side["has_balance"] or not ls or any(x["balance"] is None for x in ls):
        return None, None, False
    descending = ls[0]["date"] > ls[-1]["date"]
    first, last = (ls[-1], ls[0]) if descending else (ls[0], ls[-1])
    opening = first["balance"] - first["amount"]
    closing = last["balance"]
    total = sum((x["amount"] for x in side["lines"]), D0)
    return opening, closing, abs(opening + total - closing) < Decimal("0.005")


# ---------------------------------------------------------------- matching


def norm_ref(ref: str) -> str:
    r = re.sub(r"\s+", "", str(ref)).upper()
    return r.lstrip("0") if r.isdigit() else r


def ref_hit(led: Dict[str, Any], bank: Dict[str, Any]) -> bool:
    r = norm_ref(led["ref"])
    if not r:
        return False
    if bank["ref"] and norm_ref(bank["ref"]) == r:
        return True
    raw = led["ref"].strip()
    if len(raw) >= 4 and any(ch.isdigit() for ch in raw):
        return re.search(rf"(?<![A-Za-z0-9]){re.escape(raw)}(?![A-Za-z0-9])", bank["desc"], re.I) is not None
    return False


def match(bank: List[Dict[str, Any]], ledger: List[Dict[str, Any]], days: int) -> Tuple[List[Tuple], List[Tuple]]:
    """Returns (matched pairs (bank, ledger, how), amount-difference pairs (bank, ledger))."""
    pairs: List[Tuple] = []
    by_amt: Dict[Decimal, List[Dict[str, Any]]] = defaultdict(list)
    for b in bank:
        by_amt[b["amount"]].append(b)
    cands = []
    for led in ledger:
        if not led["date"]:
            continue
        for b in by_amt.get(led["amount"], []):
            if not b["date"]:
                continue
            gap = abs((b["date"] - led["date"]).days)
            if gap <= days:
                cands.append((0 if ref_hit(led, b) else 1, gap, b["i"], led["i"], b, led))
    cands.sort(key=lambda c: c[:4])
    used_b, used_l = set(), set()
    for _, gap, bi, li, b, led in cands:
        if bi in used_b or li in used_l:
            continue
        used_b.add(bi)
        used_l.add(li)
        pairs.append((b, led, "amount and date"))
    diffs: List[Tuple] = []
    free_bank = [b for b in bank if b["i"] not in used_b]
    for led in ledger:
        if led["i"] in used_l or not led["ref"]:
            continue
        hits = [b for b in free_bank if b["i"] not in used_b and ref_hit(led, b)]
        if led["date"]:
            hits = [b for b in hits if not b["date"] or abs((b["date"] - led["date"]).days) <= 45]
        if not hits:
            continue
        hits.sort(key=lambda b: (b["amount"] != led["amount"],
                                 abs((b["date"] - led["date"]).days) if b["date"] and led["date"] else 999, b["i"]))
        b = hits[0]
        used_b.add(b["i"])
        used_l.add(led["i"])
        if b["amount"] == led["amount"]:
            pairs.append((b, led, "reference"))
        else:
            diffs.append((b, led))
    return pairs, diffs


# ---------------------------------------------------------------- grouping


def is_check(led: Dict[str, Any]) -> bool:
    return bool(CHECK_RE.search(led["type"]) or re.fullmatch(r"\d{3,7}", led["ref"]) or CHECK_RE.search(led["memo"]))


def bank_kind(b: Dict[str, Any]) -> str:
    desc = b["desc"]
    if b["amount"] < 0 and FEE_RE.search(desc):
        return "fee"
    for p in PROCESSORS:
        if re.search(rf"\b{re.escape(p)}\b", desc, re.I) and (b["amount"] > 0 or re.search(r"payout|transfer|settle", desc, re.I)):
            return f"{p} payout"
    if re.search(r"\brefund", desc, re.I):
        return "refund"
    if re.search(r"\binterest\b", desc, re.I):
        return "interest credit" if b["amount"] > 0 else "interest charge"
    if re.search(r"\breturn(ed)?\b", desc, re.I):
        return "returned item"
    return "deposit" if b["amount"] > 0 else "payment"


def count_phrase(kinds: Counter) -> str:
    parts = []
    for kind, n in sorted(kinds.items(), key=lambda kv: (-kv[1], kv[0])):
        noun = kind if n == 1 else kind + "s"
        parts.append(f"{WORDS.get(n, str(n))} {noun}")
    if len(parts) <= 1:
        return "".join(parts)
    return ", ".join(parts[:-1]) + " and " + parts[-1]


def noun_phrase(kinds: Counter) -> str:
    nouns = []
    for kind in sorted(kinds, key=lambda k: (-kinds[k], k)):
        base = kind.split()[-1] + "s"
        if base not in nouns:
            nouns.append(base)
    return " and ".join(nouns) if len(nouns) <= 2 else ", ".join(nouns[:-1]) + " and " + nouns[-1]


def short(d: Optional[dt.date]) -> str:
    return f"{d.strftime('%b')} {d.day}" if d else "no date"


def span(dates: List[dt.date]) -> str:
    a, b = min(dates), max(dates)
    if a == b:
        return short(a)
    if a.month == b.month:
        return f"{a.strftime('%b')} {a.day}–{b.day}"
    return f"{short(a)}–{short(b)}"


def has_cents(x: Decimal) -> bool:
    return x != x.to_integral_value()


# ---------------------------------------------------------------- main


def main(argv: Optional[Sequence[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Bank reconciliation: match bank lines to the cash ledger, group the "
                                            "open items and tie the balances.")
    p.add_argument("bank", help="the bank statement export (CSV, TSV or XLSX)")
    p.add_argument("ledger", help="the ledger's cash account detail for the same period")
    p.add_argument("--days", type=int, default=3, help="date window for amount matches, in days (default 3)")
    p.add_argument("--later", help="a later bank export, to show when open ledger items cleared")
    p.add_argument("--bank-balance", help="the statement's closing balance, when the file has no running balance")
    p.add_argument("--ledger-balance", help="the ledger balance at the same date, when the file has no running balance")
    p.add_argument("--fee-account", default="6810 Bank charges", help="account for the draft fee journal")
    p.add_argument("--cash-account", help="the cash account to credit in the draft journal (default: from the ledger)")
    p.add_argument("--out", help="folder for recon_<mon>.xlsx (default: working folder)")
    a = p.parse_args(argv)
    try:
        return run(a)
    except InputError as e:
        fail(str(e))
    return 2


def run(a: argparse.Namespace) -> int:
    profile = mf.load_profile()
    sym = SYMBOLS.get(str(profile.get("currency", "USD")).upper(), "$")
    if a.days < 0:
        raise InputError("--days must be zero or more.")
    bank_f, led_f = read_lines(a.bank, "bank"), read_lines(a.ledger, "ledger")
    bank, ledger = bank_f["lines"], led_f["lines"]
    later = read_lines(a.later, "bank")["lines"] if a.later else None

    pairs, diffs = match(bank, ledger, a.days)
    used_b = {b["i"] for b, _, _ in pairs} | {b["i"] for b, _ in diffs}
    used_l = {led["i"] for _, led, _ in pairs} | {led["i"] for _, led in diffs}
    bank_only = [b for b in bank if b["i"] not in used_b]
    led_only = [x for x in ledger if x["i"] not in used_l]

    dates = [x["date"] for x in bank + ledger if x["date"]]
    as_of = max(x["date"] for x in bank if x["date"]) if any(x["date"] for x in bank) else max(dates)
    mon = as_of.strftime("%b").lower()

    # ---- when the open ledger items cleared, from a later statement
    cleared: Dict[int, dt.date] = {}
    if later is not None:
        taken = set()
        for led in sorted(led_only, key=lambda x: x["i"]):
            hits = [b for b in later if b["i"] not in taken and b["amount"] == led["amount"]
                    and (not led["date"] or not b["date"] or b["date"] >= led["date"])]
            hits.sort(key=lambda b: (not ref_hit(led, b), b["date"] or dt.date.max, b["i"]))
            if hits:
                taken.add(hits[0]["i"])
                if hits[0]["date"]:
                    cleared[led["i"]] = hits[0]["date"]

    # ---- groups, in the order a reviewer reads them
    groups: List[Dict[str, Any]] = []
    outflows = [x for x in led_only if x["amount"] < 0]
    inflows = [x for x in led_only if x["amount"] > 0]

    def pending_what(items: List[Dict[str, Any]]) -> str:
        if later is None:
            oldest = min((x["date"] for x in items if x["date"]), default=None)
            return f"Nothing yet; the oldest is from {short(oldest)}" if oldest else "Nothing yet"
        done = [cleared[x["i"]] for x in items if x["i"] in cleared]
        if len(done) == len(items):
            return f"Nothing; they cleared {span(done)}" if len(items) > 1 else f"Nothing; it cleared {span(done)}"
        if not done:
            return "Chase them: not on the later statement either"
        return f"{len(done)} cleared {span(done)}; chase the other {len(items) - len(done)}"

    if outflows:
        all_checks = all(is_check(x) for x in outflows)
        groups.append({"key": "ledger_out", "label": "Checks not cleared yet" if all_checks else "Payments not cleared yet",
                       "side": "Ledger", "items": outflows, "what": pending_what(outflows),
                       "phrase": "checks not cleared" if all_checks else "payments not cleared"})
    if inflows:
        groups.append({"key": "ledger_in", "label": "Deposits not on the statement yet", "side": "Ledger", "items": inflows,
                       "what": pending_what(inflows), "phrase": "deposits not on the statement"})
    fees = [b for b in bank_only if bank_kind(b) == "fee"]
    other = [b for b in bank_only if bank_kind(b) != "fee"]
    if fees:
        groups.append({"key": "bank_fees", "label": "Bank fees not booked", "side": "Bank", "items": fees,
                       "what": f"Book to {a.fee_account}", "phrase": "fees not booked"})
    if other:
        kinds = Counter(bank_kind(b) for b in other)
        groups.append({"key": "bank_other", "label": "Not in the ledger", "side": "Bank", "items": other,
                       "what": f"Book {count_phrase(kinds)}", "phrase": f"{noun_phrase(kinds)} not booked"})
    if diffs:
        groups.append({"key": "amount_diff", "label": "Amount differences", "side": "Both", "items": diffs,
                       "what": "Correct the ledger, or query the bank", "phrase": "amount differences"})

    for g in groups:
        if g["key"] == "amount_diff":
            g["effect"] = sum((b["amount"] - led["amount"] for b, led in g["items"]), D0)
            g["total"] = abs(g["effect"])
        elif g["side"] == "Ledger":
            g["effect"] = -sum((x["amount"] for x in g["items"]), D0)
            g["total"] = abs(g["effect"])
        else:
            g["effect"] = sum((x["amount"] for x in g["items"]), D0)
            g["total"] = abs(g["effect"])

    n_open = sum(len(g["items"]) for g in groups)
    n_bank, n_led, n_match = len(bank), len(ledger), len(pairs)
    by_how = Counter(how for _, _, how in pairs)

    # ---- balances and the tie-out
    b_open, b_close, b_ok = balances(bank_f)
    l_open, l_close, l_ok = balances(led_f)
    if a.bank_balance:
        b_close = mf.to_decimal(a.bank_balance)
        if b_close is None:
            raise InputError("--bank-balance must be a number, for example 3081965.00.")
    if a.ledger_balance:
        l_close = mf.to_decimal(a.ledger_balance)
        if l_close is None:
            raise InputError("--ledger-balance must be a number, for example 2980000.00.")

    cents_g = any(has_cents(g["total"]) for g in groups)
    G = lambda x: mf.money(x, unit="1", decimals=2 if cents_g else 0, currency=sym)   # noqa: E731

    if n_open == 0:
        headline = f"All {mf.num(n_bank)} bank lines match the ledger, and every ledger line is on the statement."
    else:
        headline = (f"{mf.num(n_match)} of {mf.num(n_bank)} bank lines match the ledger. "
                    f"{mf.num(n_open)} {'item is' if n_open == 1 else 'items are'} open, in "
                    f"{WORDS.get(len(groups), str(len(groups)))} {'group' if len(groups) == 1 else 'groups'}:")
    out = [headline]
    if groups:
        out += ["", mf.md_table(["Group", "Items", "Amount", "What to do"],
                                [[g["label"], mf.num(len(g["items"])), G(g["total"]), g["what"]] for g in groups],
                                align=["l", "r", "r", "l"])]

    tie: Dict[str, Any] = {"bank": None, "ledger": None, "difference": None, "explained": None, "ties": None}
    if b_close is None or l_close is None:
        missing = " and ".join(x for x, v in (("--bank-balance", b_close), ("--ledger-balance", l_close)) if v is None)
        tie_text = (f"The tie-out is not done: the files carry no running balance. Rerun with {missing}.")
    else:
        diff = b_close - l_close
        explained = sum((g["effect"] for g in groups), D0)
        ties = abs(diff - explained) < Decimal("0.005")
        tie.update(bank=str(b_close), ledger=str(l_close), difference=str(diff), explained=str(explained), ties=ties)
        cents_t = any(has_cents(x) for x in [b_close, l_close, diff, explained] + [g["effect"] for g in groups])
        T = lambda x: mf.money(x, unit="1", decimals=2 if cents_t else 0, currency=sym)   # noqa: E731
        first = f"On {short(as_of)} the bank shows {T(b_close)} and the ledger {T(l_close)}."
        sign = -1 if diff < 0 else 1
        pieces = []
        for g in sorted([g for g in groups if g["effect"] != 0], key=lambda g: (g["effect"] * sign < 0, groups.index(g))):
            amt = T(abs(g["effect"]))
            if not pieces:
                pieces.append(f"{'' if g['effect'] * sign > 0 else 'minus '}{amt} of {g['phrase']}")
            else:
                pieces.append(f"{'plus' if g['effect'] * sign > 0 else 'less'} {amt} of {g['phrase']}")
        if diff == 0 and n_open == 0:
            tie_text = f"On {short(as_of)} the bank and the ledger both show {T(b_close)}."
        elif ties:
            tie_text = f"{first} The open items explain all of the {T(abs(diff))} difference: {', '.join(pieces)}."
        else:
            gap = diff - explained
            tie_text = (f"{first} The balances do not tie: the open items explain {T(abs(explained))} of the "
                        f"{T(abs(diff))} difference, and {T(abs(gap))} is not explained. Look for lines outside the "
                        f"period, an opening difference, or a balance taken on another date.")
    out += ["", tie_text]

    if groups:
        cents_i = any(has_cents(x["amount"]) for g in groups if g["key"] != "amount_diff" for x in g["items"]) or \
            any(has_cents(b["amount"]) or has_cents(led["amount"]) for b, led in diffs)
        I = lambda x: mf.money(x, unit="1", decimals=2 if cents_i else 0, currency=sym)   # noqa: E731
        rows = []
        for g in groups:
            if g["key"] == "amount_diff":
                for b, led in g["items"]:
                    rows.append([g["label"], short(b["date"]), cell(f"{b['desc']} (ledger: {I(led['amount'])})"),
                                 cell(led["ref"] or b["ref"]), I(b["amount"] - led["amount"])])
            else:
                for x in sorted(g["items"], key=lambda x: (x["date"] or dt.date.min, x["i"])):
                    rows.append([g["label"], short(x["date"]), cell(x["desc"]), cell(x["ref"]), I(x["amount"])])
        out += ["", "**Open items**", "", mf.md_table(["Group", "Date", "Description", "Reference", "Amount"], rows,
                                                      align=["l", "l", "l", "l", "r"])]

    # ---- the workbook
    cash_acct = a.cash_account or next((x["account"] for x in ledger if x["account"]), "") or "Cash"
    out_dir = a.out or os.getcwd()
    os.makedirs(out_dir, exist_ok=True)
    xlsx_path = os.path.join(out_dir, f"recon_{mon}.xlsx")
    matched_rows: List[List[Any]] = [["Bank date", "Bank description", "Bank reference", "Bank amount", "Ledger date",
                                      "Ledger journal", "Ledger reference", "Ledger description", "Ledger amount",
                                      "Matched on", "Days apart"]]
    for b, led, how in sorted(pairs, key=lambda p: (p[0]["date"] or dt.date.min, p[0]["i"])):
        gap = abs((b["date"] - led["date"]).days) if b["date"] and led["date"] else ""
        matched_rows.append([b["date"].isoformat() if b["date"] else "", b["desc"], b["ref"], b["amount"],
                             led["date"].isoformat() if led["date"] else "", led["journal"], led["ref"], led["desc"],
                             led["amount"], how, gap])
    open_rows: List[List[Any]] = [["Group", "Side", "Date", "Description", "Reference", "Amount", "What to do", "Cleared"]]
    for g in groups:
        if g["key"] == "amount_diff":
            for b, led in g["items"]:
                open_rows.append([g["label"], "Bank", b["date"].isoformat() if b["date"] else "", b["desc"], b["ref"],
                                  b["amount"], g["what"], ""])
                open_rows.append([g["label"], "Ledger", led["date"].isoformat() if led["date"] else "", led["desc"],
                                  led["ref"], led["amount"], g["what"], ""])
        else:
            for x in sorted(g["items"], key=lambda x: (x["date"] or dt.date.min, x["i"])):
                open_rows.append([g["label"], g["side"], x["date"].isoformat() if x["date"] else "", x["desc"], x["ref"],
                                  x["amount"], g["what"], cleared[x["i"]].isoformat() if x["i"] in cleared else ""])
    fee_items = next((g["items"] for g in groups if g["key"] == "bank_fees"), [])
    je_rows: List[List[Any]] = [["Date", "Account", "Debit", "Credit", "Memo"]]
    for b in sorted(fee_items, key=lambda x: (x["date"] or dt.date.min, x["i"])):
        je_rows.append([as_of.isoformat(), a.fee_account, -b["amount"], "", f"{b['desc']} ({short(b['date'])})"])
    if fee_items:
        fee_total = -sum((b["amount"] for b in fee_items), D0)
        je_rows.append([as_of.isoformat(), cash_acct, "", fee_total, f"Bank fees on the {short(as_of)} statement, not booked"])
    else:
        je_rows.append(["", "No bank fees to book", "", "", ""])
    mf.write_xlsx(xlsx_path, {"Matched": matched_rows, "Open items": open_rows, "Draft journal": je_rows})

    rel = os.path.relpath(xlsx_path, os.getcwd()) if a.out else os.path.basename(xlsx_path)
    out += ["", f"Matched {mf.num(n_match)}: {mf.num(by_how.get('amount and date', 0))} on amount and date within "
                f"{a.days} {'day' if a.days == 1 else 'days'}, {mf.num(by_how.get('reference', 0))} on reference. "
                f"Bank: {mf.num(n_bank)} lines. Ledger: {mf.num(n_led)} lines.",
            f"Wrote {rel}: Matched ({mf.num(n_match)}), Open items ({mf.num(n_open)}), Draft journal "
            + (f"({G(-sum((b['amount'] for b in fee_items), D0))} of fees to {a.fee_account})." if fee_items else "(no fees).")]
    if bank_f["has_balance"] and not b_ok and not a.bank_balance:
        out.append("Heads up: the bank file's running balance does not agree with its lines; check that the export is complete.")
    if led_f["has_balance"] and not l_ok and not a.ledger_balance:
        out.append("Heads up: the ledger file's running balance does not agree with its lines; check that the export is complete.")
    if b_ok and l_ok and b_open is not None and l_open is not None and b_open != l_open:
        out.append(f"Heads up: the two files open at different balances ({mf.money(b_open, unit='1', currency=sym)} "
                   f"and {mf.money(l_open, unit='1', currency=sym)}); items open at the start of the period are part of "
                   f"the difference.")

    def item(x: Dict[str, Any]) -> Dict[str, Any]:
        return {"date": x["date"].isoformat() if x["date"] else None, "amount": str(x["amount"]), "description": x["desc"],
                "reference": x["ref"], "journal": x["journal"], "cleared": cleared[x["i"]].isoformat() if x["i"] in cleared else None}

    data = {
        "skill": "reconcile",
        "files": {"bank": a.bank, "ledger": a.ledger, "later": a.later, "workbook": xlsx_path},
        "as_of": as_of.isoformat(), "days": a.days,
        "counts": {"bank_lines": n_bank, "ledger_lines": n_led, "matched": n_match,
                   "matched_amount_and_date": by_how.get("amount and date", 0), "matched_reference": by_how.get("reference", 0),
                   "open_items": n_open},
        "headline": headline,
        "groups": [{"key": g["key"], "label": g["label"], "items": len(g["items"]), "amount": str(g["total"]),
                    "effect_on_difference": str(g["effect"]), "what_to_do": g["what"],
                    "lines": ([{"bank": item(b), "ledger": item(led)} for b, led in g["items"]] if g["key"] == "amount_diff"
                              else [item(x) for x in g["items"]])} for g in groups],
        "balances": {"bank_opening": None if b_open is None else str(b_open), "ledger_opening": None if l_open is None else str(l_open)},
        "tie_out": dict(tie, text=tie_text),
        "draft_journal": {"fee_account": a.fee_account, "cash_account": cash_acct,
                          "total": str(-sum((b["amount"] for b in fee_items), D0))},
    }
    mf.emit("\n".join(out), data, os.path.join(mf.magnos_dir(), "runs", "reconcile.json"))
    return 0


def cell(s: Any) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ")


if __name__ == "__main__":
    sys.exit(main())
