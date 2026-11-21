#!/usr/bin/env python3
"""Mizar: exact invoice totals with Decimal (stdlib only).

Usage:  python compute_totals.py invoice.json [--write]
Reads the canonical invoice JSON (assets/invoice-schema.json), prints totals JSON.
--write  stores computed line amounts + totals back into the file under "computed".
Exit 1 with a list of problems if required numeric inputs are missing/invalid —
the skill must then ASK the user, never fill values in.
"""
import json
import sys
from datetime import date, timedelta
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

CENT = Decimal("0.01")


def d(v, field, problems):
    if v is None or str(v).strip() == "":
        problems.append(f"missing {field}")
        return None
    try:
        return Decimal(str(v).replace(",", "."))
    except InvalidOperation:
        problems.append(f"invalid number in {field}: {v!r}")
        return None


def r2(x):
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def compute(inv):
    problems = []
    incl = bool(inv.get("prices_include_tax"))
    lines_out = []
    groups = {}  # rate -> base (net)
    for i, ln in enumerate(inv.get("lines") or [], 1):
        q = d(ln.get("quantity"), f"lines[{i}].quantity", problems)
        p = d(ln.get("unit_price"), f"lines[{i}].unit_price", problems)
        t = d(ln.get("tax_rate"), f"lines[{i}].tax_rate", problems)
        if None in (q, p, t):
            continue
        amount = r2(q * p)
        net = r2(amount / (1 + t / 100)) if incl else amount
        lines_out.append({"n": i, "amount": str(amount), "net": str(net), "tax_rate": str(t.normalize())})
        groups[t] = groups.get(t, Decimal(0)) + net
    if not inv.get("lines"):
        problems.append("no line items")
    if problems:
        return None, problems

    net_total = sum(groups.values(), Decimal(0))
    disc = inv.get("discount")
    discount_total = Decimal(0)
    if disc:
        val = d(disc.get("value"), "discount.value", problems)
        if problems:
            return None, problems
        discount_total = r2(net_total * val / 100) if disc.get("type") == "percent" else r2(val)
    # pro-rata discount per rate; last group absorbs rounding remainder
    tax_by_rate, allocated = [], Decimal(0)
    rates = sorted(groups)
    for k, rate in enumerate(rates):
        base = groups[rate]
        if discount_total and net_total:
            share = discount_total - allocated if k == len(rates) - 1 else r2(discount_total * base / net_total)
            allocated += share
            base = base - share
        tax = r2(base * rate / 100)
        tax_by_rate.append({"rate": str(rate.normalize()), "base": str(r2(base)), "tax": str(tax)})
    tax_total = sum((Decimal(x["tax"]) for x in tax_by_rate), Decimal(0))
    net_after = r2(net_total - discount_total)
    total = net_after + tax_total
    if 0 in groups and not inv.get("tax_note"):
        problems.append("a line has 0% tax but tax_note (exemption / reverse-charge text) is missing")

    due = None
    try:
        if inv.get("due_date"):
            due = inv["due_date"]
        elif inv.get("issue_date") and inv.get("payment_terms_days") is not None:
            due = (date.fromisoformat(inv["issue_date"]) + timedelta(days=int(inv["payment_terms_days"]))).isoformat()
    except ValueError:
        problems.append("invalid issue_date / payment_terms_days")

    out = {
        "currency": inv.get("currency"),
        "lines": lines_out,
        "net": str(r2(net_total)),
        "discount_total": str(r2(discount_total)),
        "net_after_discount": str(net_after),
        "tax_by_rate": tax_by_rate,
        "tax_total": str(r2(tax_total)),
        "total": str(r2(total)),
        "due_date": due,
        "warnings": problems,  # non-blocking at this point
    }
    return out, []


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    path = sys.argv[1]
    inv = json.load(open(path, encoding="utf-8"))
    out, problems = compute(inv)
    if problems:
        print(json.dumps({"ok": False, "ask_user_for": problems}, indent=2))
        return 1
    if "--write" in sys.argv:
        inv["computed"] = out
        json.dump(inv, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(json.dumps({"ok": True, **out}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
