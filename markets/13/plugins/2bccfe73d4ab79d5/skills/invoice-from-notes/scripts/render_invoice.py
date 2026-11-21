#!/usr/bin/env python3
"""Mizar: render canonical invoice JSON -> HTML (always) + PDF (if reportlab is installed).

Usage: python render_invoice.py invoice.json --out invoice.pdf
Writes invoice.html next to --out. Totals come from compute_totals.compute() — never typed in.
Missing required fields => document is labelled DRAFT and shows [PLACEHOLDER] text, never fake values.
"""
import argparse
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compute_totals import compute  # noqa: E402

T = {
    "en": dict(t_invoice="Invoice", t_number="No.", t_date="Date", t_service="Service", t_billto="Bill to",
               t_desc="Description", t_qty="Qty", t_price="Unit price", t_tax="Tax %", t_amount="Amount",
               t_net="Net", t_discount="Discount", t_vat="VAT", t_total="Total", t_due="Due date:",
               t_draft="DRAFT — not a valid invoice until placeholders are filled"),
    "de": dict(t_invoice="Rechnung", t_number="Nr.", t_date="Datum", t_service="Leistung", t_billto="Rechnung an",
               t_desc="Beschreibung", t_qty="Menge", t_price="Einzelpreis", t_tax="USt %", t_amount="Betrag",
               t_net="Netto", t_discount="Rabatt", t_vat="USt", t_total="Gesamt", t_due="Fällig am:",
               t_draft="ENTWURF — erst nach Ausfüllen der Platzhalter gültig"),
}


def ph(v, name, missing):
    if v in (None, "", {}):
        missing.append(name)
        return f"[{name.upper()}]"
    return v


def build(inv):
    missing = []
    lang = inv.get("language", "en") if inv.get("language") in T else "en"
    t = T[lang]
    tot, problems = compute(inv)
    if problems:
        raise SystemExit(json.dumps({"ok": False, "ask_user_for": problems}, indent=2))
    s, c = inv.get("seller") or {}, inv.get("client") or {}
    sp = inv.get("service_period")
    service = inv.get("service_date") or (f"{sp['from']} – {sp['to']}" if sp else None)
    bank = s.get("bank") or {}
    payment = s.get("payment_instructions") or (
        f"IBAN {ph(bank.get('iban'), 'iban', missing)} · BIC {bank.get('bic', '')} · {bank.get('account_holder', s.get('name', ''))}")
    ids = s.get("vat_id") and f"VAT ID {s['vat_id']}" or s.get("tax_number") and f"Tax no. {s['tax_number']}"
    f = dict(
        number=ph(inv.get("number"), "invoice no", missing), issue_date=ph(inv.get("issue_date"), "issue date", missing),
        service=ph(service, "service date", missing), seller_name=ph(s.get("name"), "seller name", missing),
        seller_address=ph(s.get("address"), "seller address", missing), seller_ids=ph(ids, "tax id", missing),
        client_name=ph(c.get("name"), "client name", missing), client_address=ph(c.get("address"), "client address", missing),
        client_ids=" · ".join(x for x in [c.get("vat_id") and f"VAT ID {c['vat_id']}", c.get("po_number") and f"PO {c['po_number']}"] if x),
        due_date=ph(tot["due_date"], "due date", missing), payment=payment,
        tax_note=inv.get("tax_note") or "", notes=inv.get("notes") or "",
    )
    cur = inv.get("currency") or ph(None, "currency", missing)
    rows = []
    for ln, comp in zip(inv["lines"], tot["lines"]):
        rows.append([str(comp["n"]), ln["description"], f"{ln['quantity']} {ln.get('unit', '')}".strip(),
                     ln["unit_price"], comp["tax_rate"], comp["amount"]])
    totals = [(t["t_net"], tot["net"])]
    if tot["discount_total"] != "0.00":
        totals.append((t["t_discount"], "-" + tot["discount_total"]))
    for g in tot["tax_by_rate"]:
        totals.append((f"{t['t_vat']} {g['rate']} % ({g['base']})", g["tax"]))
    totals.append((f"{t['t_total']} {cur}", tot["total"]))
    draft = bool(missing) or inv.get("status") == "draft"
    return t, f, rows, totals, draft, missing, tot, lang


def to_html(t, f, rows, totals, draft, lang, tpl):
    e = lambda x: html.escape(str(x))
    rows_h = "".join("<tr>" + "".join(f'<td class="{"n" if i >= 2 else ""}">{e(v)}</td>' for i, v in enumerate(r)) + "</tr>" for r in rows)
    tot_h = "".join(f'<tr class="{"grand" if k == len(totals) - 1 else ""}"><td>{e(a)}</td><td class="n">{e(b)}</td></tr>' for k, (a, b) in enumerate(totals))
    m = {**t, **{k: e(v) for k, v in f.items()}, "lang": lang, "rows": rows_h, "totals": tot_h,
         "draft_banner": f'<p class="draft">{e(t["t_draft"])}</p>' if draft else ""}
    for k, v in m.items():
        tpl = tpl.replace("{{" + k + "}}", str(v))
    return tpl


def to_pdf(path, t, f, rows, totals, draft):
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
    st = getSampleStyleSheet()
    br = lambda s: html.escape(str(s)).replace("\n", "<br/>")
    el = []
    if draft:
        el.append(Paragraph(f'<font color="#B91C1C"><b>{br(t["t_draft"])}</b></font>', st["Normal"]))
    el += [Paragraph(f'<font color="#1D4ED8">{t["t_invoice"]}</font>', st["Title"]),
           Paragraph(f'{t["t_number"]} {br(f["number"])} · {t["t_date"]} {br(f["issue_date"])} · {t["t_service"]} {br(f["service"])}', st["Normal"]),
           Spacer(1, 12)]
    addr = Table([[Paragraph(f'<b>{br(f["seller_name"])}</b><br/>{br(f["seller_address"])}<br/>{br(f["seller_ids"])}', st["Normal"]),
                   Paragraph(f'<b>{t["t_billto"]}</b><br/>{br(f["client_name"])}<br/>{br(f["client_address"])}<br/>{br(f["client_ids"])}', st["Normal"])]],
                 colWidths=[260, 260])
    el += [addr, Spacer(1, 14)]
    data = [["#", t["t_desc"], t["t_qty"], t["t_price"], t["t_tax"], t["t_amount"]]] + \
           [[r[0], Paragraph(br(r[1]), st["Normal"])] + r[2:] for r in rows]
    tb = Table(data, colWidths=[22, 230, 60, 75, 50, 80], repeatRows=1)
    tb.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EFF6FF")),
                            ("LINEBELOW", (0, 0), (-1, -1), 0.4, colors.lightgrey),
                            ("ALIGN", (2, 0), (-1, -1), "RIGHT"), ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    tt = Table([[a, b] for a, b in totals], colWidths=[200, 90], hAlign="RIGHT")
    tt.setStyle(TableStyle([("ALIGN", (1, 0), (1, -1), "RIGHT"), ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
                            ("LINEABOVE", (0, -1), (-1, -1), 1, colors.black)]))
    el += [tb, Spacer(1, 10), tt, Spacer(1, 14)]
    if f["tax_note"]:
        el.append(Paragraph(br(f["tax_note"]), st["Normal"]))
    el += [Paragraph(f'<b>{t["t_due"]}</b> {br(f["due_date"])}<br/>{br(f["payment"])}', st["Normal"]), Spacer(1, 8),
           Paragraph(f'<font color="#555555">{br(f["notes"])}</font>', st["Normal"])]
    SimpleDocTemplate(path, pagesize=A4, title=f'{t["t_invoice"]} {f["number"]}').build(el)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("invoice")
    ap.add_argument("--out", default="invoice.pdf")
    a = ap.parse_args()
    inv = json.load(open(a.invoice, encoding="utf-8"))
    t, f, rows, totals, draft, missing, tot, lang = build(inv)
    here = os.path.dirname(os.path.abspath(__file__))
    tpl = open(os.path.join(here, "..", "assets", "invoice-template.html"), encoding="utf-8").read()
    html_path = os.path.splitext(a.out)[0] + ".html"
    open(html_path, "w", encoding="utf-8").write(to_html(t, f, rows, totals, draft, lang, tpl))
    files, warn = [html_path], []
    try:
        to_pdf(a.out, t, f, rows, totals, draft)
        files.append(a.out)
    except ImportError:
        warn.append("reportlab not installed — PDF not generated; HTML written (print to PDF)")
    print(json.dumps({"ok": True, "draft": draft, "missing": missing, "files": files, "warnings": warn,
                      "total": tot["total"], "currency": inv.get("currency")}, indent=2))


if __name__ == "__main__":
    main()
