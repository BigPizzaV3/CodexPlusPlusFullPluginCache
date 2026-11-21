#!/usr/bin/env python3
"""Build the CallRail agency health check spreadsheet.

Usage: python build_report.py <input.json> <output.xlsx> [--all]

Tabs:
  Overview      internal: every company, status, top issue, owner, link to its tab
  <Company>     client-ready report for each company that needs attention
                (--all adds a tab for Healthy companies too)
  Not Checked   internal: what couldn't be checked
Input format: references/report-format.md
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from report_common import (
    CHECK_RESULT,
    SNAPSHOT,
    STATUS,
    load,
    period_text,
    status_text,
    trend,
    wanted,
)

try:
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    sys.exit("openpyxl is required: pip install openpyxl")

NAVY = "1F2A44"
HEADER_FILL = PatternFill("solid", fgColor=NAVY)
HEADER_FONT = Font(bold=True, color="FFFFFF")
SECTION_FONT = Font(bold=True, size=12, color=NAVY)
LINK_FONT = Font(color="0563C1", underline="single")
WRAP = Alignment(wrap_text=True, vertical="top")
THIN = Border(bottom=Side(style="thin", color="D0D5DD"))


def fill(hex_):
    return PatternFill("solid", fgColor=hex_)


def header_row(ws, row, headers):
    for col, text in enumerate(headers, start=1):
        c = ws.cell(row=row, column=col, value=text)
        c.fill = HEADER_FILL
        c.font = HEADER_FONT
        c.alignment = Alignment(vertical="center", wrap_text=True)


def safe_tab_name(name, used):
    base = re.sub(r"[\[\]\*\?/\\:]", "", name or "Company").strip() or "Company"
    base = base[:28].rstrip("' ")
    candidate, n = base, 2
    while candidate.lower() in used or candidate.lower() in ("overview", "not checked"):
        suffix = f" {n}"
        candidate = base[: 31 - len(suffix)] + suffix
        n += 1
    used.add(candidate.lower())
    return candidate


def section(ws, row, title):
    ws.cell(row=row, column=1, value=title).font = SECTION_FONT
    return row + 1


def client_tab(wb, c, tab, data):
    ws = wb.create_sheet(tab)
    st = STATUS[c["status"]]
    ws.sheet_properties.tabColor = st["color"]
    ws.sheet_view.showGridLines = False
    for i, w in enumerate([22, 34, 40, 40, 16], start=1):
        ws.column_dimensions[get_column_letter(i)].width = w

    ws["A1"] = c.get("name")
    ws["A1"].font = Font(bold=True, size=16, color=NAVY)
    ws["A2"] = "Call tracking health check"
    ws["A2"].font = Font(size=11, color="555555")
    ws["A3"] = period_text(data)
    ws["A3"].font = Font(size=10, color="555555")
    if data.get("agency_name"):
        ws["D1"] = f"Prepared by {data['agency_name']}"
        ws["D1"].font = Font(size=10, color="555555")
    back = ws["E1"]
    back.value = "← Overview"
    back.hyperlink = "#'Overview'!A1"
    back.font = LINK_FONT

    ws["A5"] = status_text(c["status"])
    ws["A5"].font = Font(bold=True, size=12, color=st["color"])
    ws["A5"].fill = fill(st["tint"])
    ws.merge_cells("A5:B5")
    ws["C5"] = c.get("summary") or ""
    ws["C5"].alignment = WRAP
    ws.merge_cells("C5:E5")
    ws.row_dimensions[5].height = 32

    row = section(ws, 7, "This month at a glance")
    snap = c.get("snapshot") or {}
    for key, label, suffix in SNAPSHOT:
        m = snap.get(key)
        if not m:
            continue
        value, change = trend(m.get("current"), m.get("prior"), suffix)
        ws.cell(row=row, column=1, value=label).font = Font(bold=True)
        ws.cell(row=row, column=2, value=value).font = Font(size=12, bold=True)
        ws.cell(row=row, column=3, value=change).font = Font(color="555555")
        row += 1

    row = section(ws, row + 1, "What's working")
    for line in c.get("working") or ["Nothing stood out this month."]:
        ws.cell(row=row, column=1, value="✓").font = Font(
            bold=True, color=STATUS["healthy"]["color"]
        )
        cell = ws.cell(row=row, column=2, value=line)
        cell.alignment = WRAP
        ws.merge_cells(start_row=row, start_column=2, end_row=row, end_column=5)
        row += 1

    row = section(ws, row + 1, "What needs attention")
    if c["findings"]:
        header_row(
            ws,
            row,
            ["Status", "What we found", "Why it matters", "How to fix it", "Who"],
        )
        for f in c["findings"]:
            row += 1
            fs = STATUS[f["level"]]
            vals = [
                status_text(f["level"]),
                f.get("issue"),
                f.get("impact"),
                f.get("fix"),
                f.get("owner"),
            ]
            for col, v in enumerate(vals, start=1):
                cell = ws.cell(row=row, column=col, value=v)
                cell.alignment = WRAP
                cell.border = THIN
            ws.cell(row=row, column=1).font = Font(bold=True, color=fs["color"])
            ws.cell(row=row, column=1).fill = fill(fs["tint"])
    else:
        ws.cell(row=row, column=1, value="Nothing needs attention right now.")

    row = section(ws, row + 2, "What we checked")
    header_row(ws, row, ["Area", "Check", "Result", "Note", ""])
    for chk in c.get("checks") or []:
        row += 1
        sym, text = CHECK_RESULT.get(chk.get("result"), ("?", chk.get("result")))
        ws.cell(row=row, column=1, value=chk.get("area"))
        ws.cell(row=row, column=2, value=chk.get("name"))
        rc = ws.cell(row=row, column=3, value=f"{sym} {text}")
        if chk.get("result") in ("action", "watch"):
            rc.font = Font(bold=True, color=STATUS[chk["result"]]["color"])
        elif chk.get("result") == "pass":
            rc.font = Font(color=STATUS["healthy"]["color"])
        ws.cell(row=row, column=4, value=chk.get("note") or "").alignment = WRAP
        for col in range(1, 5):
            ws.cell(row=row, column=col).border = THIN

    ws.print_options.horizontalCentered = True
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    return ws


def store_formulas_as_text(wb):
    for ws in wb:
        for row in ws.iter_rows():
            for cell in row:
                if cell.data_type == "f":
                    cell.data_type = "s"
                    cell.quotePrefix = True


def main(src, dst, include_all=False):
    data = load(src)
    companies = data["companies"]
    wb = Workbook()
    ov = wb.active
    ov.title = "Overview"
    ov.sheet_view.showGridLines = False

    counts = {k: sum(1 for c in companies if c["status"] == k) for k in STATUS}
    scope = data.get("scope") or f"{len(companies)} active companies"
    ov["A1"] = f"Health check: {data.get('account_name', '')}"
    ov["A1"].font = Font(bold=True, size=16, color=NAVY)
    ov["A2"] = period_text(data) + f". Run {data.get('run_date', '')}."
    line = (
        f"{status_text('action')}: {counts['action']}    {status_text('watch')}: {counts['watch']}    "
        f"{status_text('healthy')}: {counts['healthy']}    across {scope}"
    )
    if data.get("disabled_companies") and not data.get("scope"):
        line += f" ({data['disabled_companies']} disabled skipped)"
    ov["A3"] = line
    ov["A3"].font = Font(bold=True)
    ov["A4"] = (
        "Internal view for your team. Each client's tab is written so you can share it with that client."
    )
    ov["A4"].font = Font(italic=True, color="555555")
    if not data.get("website_tiers_available", {}).get("tier2"):
        ov["A5"] = (
            "Number swapping wasn't tested in a browser. Website results only confirm "
            "the business number is on each page."
        )
        ov["A5"].font = Font(italic=True, color="555555")

    start = 7
    patterns = data.get("account_patterns") or []
    problems = data.get("widespread_problems") or []
    if patterns or problems:
        ov.cell(row=7, column=1, value="Across your account").font = SECTION_FONT
        r0 = 8
        for p in patterns:
            ov.cell(row=r0, column=1, value="Opportunity").font = Font(
                bold=True, color="2B6CB0"
            )
            text = (
                f"{p.get('title', '')}. {p.get('detail', '')} {p.get('opportunity', '')} "
                f"Next step: {p.get('next_step', '')}"
            )
            cell = ov.cell(row=r0, column=2, value=text)
            cell.alignment = WRAP
            ov.merge_cells(start_row=r0, start_column=2, end_row=r0, end_column=7)
            ov.row_dimensions[r0].height = 45
            r0 += 1
        for line in problems:
            ov.cell(row=r0, column=1, value="Pattern").font = Font(
                bold=True, color=STATUS["watch"]["color"]
            )
            cell = ov.cell(row=r0, column=2, value=line)
            cell.alignment = WRAP
            ov.merge_cells(start_row=r0, start_column=2, end_row=r0, end_column=7)
            r0 += 1
        start = r0 + 1
    headers = [
        "Status",
        "Client",
        "Top issue (or what's working)",
        "Who fixes it",
        "Issues",
        "Calls",
        "vs. last month",
        "Report",
    ]
    header_row(ov, start, headers)
    used, r, tabs = set(), start, []
    for c in companies:
        r += 1
        f0 = c["findings"][0] if c["findings"] else None
        top = f0["issue"] if f0 else ((c.get("working") or ["No issues found."])[0])
        calls = (c.get("snapshot") or {}).get("calls") or {}
        value, change = trend(calls.get("current"), calls.get("prior"))
        row = [
            status_text(c["status"]),
            c.get("name"),
            top,
            f0.get("owner") if f0 else "",
            len(c["findings"]),
            value,
            change,
            "",
        ]
        for col, v in enumerate(row, start=1):
            cell = ov.cell(row=r, column=col, value=v)
            cell.alignment = WRAP
            cell.border = THIN
        st = STATUS[c["status"]]
        ov.cell(row=r, column=1).fill = fill(st["tint"])
        ov.cell(row=r, column=1).font = Font(bold=True, color=st["color"])
        if wanted(c, include_all):
            tabs.append((c, safe_tab_name(c.get("name"), used), r))
    ov.freeze_panes = ov.cell(row=start + 1, column=1)
    ov.auto_filter.ref = f"A{start}:{get_column_letter(len(headers))}{r}"
    for i, w in enumerate([20, 34, 60, 16, 8, 8, 20, 12], start=1):
        ov.column_dimensions[get_column_letter(i)].width = w

    for c, tab, ov_row in tabs:
        client_tab(wb, c, tab, data)
        link = ov.cell(row=ov_row, column=8, value="Open →")
        link.hyperlink = f"#'{tab}'!A1"
        link.font = LINK_FONT

    nc = wb.create_sheet("Not Checked")
    header_row(nc, 1, ["Client", "What wasn't checked"])
    r = 1
    for c in companies:
        for reason in c.get("not_checked", []):
            r += 1
            nc.cell(row=r, column=1, value=c.get("name"))
            nc.cell(row=r, column=2, value=reason).alignment = WRAP
    nc.column_dimensions["A"].width = 34
    nc.column_dimensions["B"].width = 80

    store_formulas_as_text(wb)
    wb.save(dst)
    print(
        f"Saved {dst}: {len(companies)} companies, {len(tabs)} client tabs "
        f"({counts['action']} action, {counts['watch']} watch, {counts['healthy']} healthy)"
    )


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--all"]
    if len(args) != 2:
        sys.exit(__doc__)
    main(args[0], args[1], include_all="--all" in sys.argv)
