#!/usr/bin/env python3
"""Build a 1-page, client-ready PDF health check per company.

Usage: python build_client_pdfs.py <input.json> <output_folder> [--all]

By default only companies that need attention get a PDF. --all includes Healthy ones.
Input format: references/report-format.md
"""

import glob
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
    trend,
    wanted,
)

try:
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (
        Paragraph,
        SimpleDocTemplate,
        Spacer,
        Table,
        TableStyle,
    )
except ImportError:
    sys.exit("reportlab is required: pip install reportlab")

# Use a font with the check/cross symbols if one is available; otherwise fall back to text.
FONT, BOLD, SYMBOLS = "Helvetica", "Helvetica-Bold", False
for path in (
    glob.glob("/usr/share/fonts/**/DejaVuSans.ttf", recursive=True)
    + glob.glob("/Library/Fonts/**/DejaVuSans.ttf", recursive=True)
    + glob.glob(os.path.expanduser("~/Library/Fonts/DejaVuSans.ttf"))
):
    bold = path.replace("DejaVuSans.ttf", "DejaVuSans-Bold.ttf")
    try:
        pdfmetrics.registerFont(TTFont("DV", path))
        pdfmetrics.registerFont(
            TTFont("DV-Bold", bold if os.path.exists(bold) else path)
        )
        FONT, BOLD, SYMBOLS = "DV", "DV-Bold", True
        break
    except Exception:  # noqa: BLE001, S112
        continue

ASCII = {"✕": "X", "✓": "OK", "▲": "up", "▼": "down", "–": "-", "←": "<-"}


def t(text):
    text = "" if text is None else str(text)
    if not SYMBOLS:
        for k, v in ASCII.items():
            text = text.replace(k, v)
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def hexc(h):
    return colors.HexColor("#" + h)


NAVY = hexc("1F2A44")
GREY = hexc("555555")
LINE = hexc("D0D5DD")

S = {
    "title": ParagraphStyle(
        "title", fontName=BOLD, fontSize=17, leading=21, textColor=NAVY
    ),
    "sub": ParagraphStyle("sub", fontName=FONT, fontSize=9, leading=12, textColor=GREY),
    "h": ParagraphStyle(
        "h",
        fontName=BOLD,
        fontSize=11.5,
        leading=15,
        textColor=NAVY,
        spaceBefore=8,
        spaceAfter=3,
    ),
    "body": ParagraphStyle(
        "body", fontName=FONT, fontSize=9, leading=12, alignment=TA_LEFT
    ),
    "small": ParagraphStyle(
        "small", fontName=FONT, fontSize=8, leading=10, textColor=GREY
    ),
    "cell": ParagraphStyle("cell", fontName=FONT, fontSize=8, leading=10),
    "cellb": ParagraphStyle("cellb", fontName=BOLD, fontSize=8, leading=10),
    "big": ParagraphStyle(
        "big", fontName=BOLD, fontSize=13, leading=15, textColor=NAVY
    ),
}


def status_para(code, size=10):
    st = STATUS[code]
    sym = st["symbol"] if SYMBOLS else ASCII.get(st["symbol"], st["symbol"])
    style = ParagraphStyle(
        "st",
        fontName=BOLD,
        fontSize=size,
        leading=size + 3,
        textColor=hexc(st["color"]),
    )
    return Paragraph(t(f"{sym} {st['label']}"), style)


def safe_filename(name):
    return re.sub(r'[\\/:*?"<>|]+', "-", name or "Company").strip()[:80]


def build(c, data, out_dir):
    name = c.get("name") or "Company"
    path = os.path.join(
        out_dir,
        f"{safe_filename(name)} - CallRail health check - {data.get('run_date', '')}.pdf",
    )
    doc = SimpleDocTemplate(
        path,
        pagesize=letter,
        leftMargin=0.6 * inch,
        rightMargin=0.6 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.55 * inch,
        title=f"{name} call tracking health check",
    )
    width = letter[0] - 1.2 * inch
    story = []

    story.append(Paragraph(t(name), S["title"]))
    sub = "Call tracking health check · " + period_text(data)
    if data.get("agency_name"):
        sub += f" · Prepared by {data['agency_name']}"
    story.append(Paragraph(t(sub), S["sub"]))
    story.append(Spacer(1, 8))

    st = STATUS[c["status"]]
    banner = Table(
        [
            [
                status_para(c["status"], 12),
                Paragraph(t(c.get("summary") or ""), S["body"]),
            ]
        ],
        colWidths=[2.0 * inch, width - 2.0 * inch],
    )
    banner.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), hexc(st["tint"])),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    story.append(banner)

    # Snapshot tiles
    snap = c.get("snapshot") or {}
    tiles = []
    for key, label, suffix in SNAPSHOT:
        m = snap.get(key)
        if not m or m.get("current") is None:
            continue
        value, change = trend(m.get("current"), m.get("prior"), suffix)
        tiles.append(
            [
                Paragraph(t(label), S["small"]),
                Paragraph(t(value), S["big"]),
                Paragraph(t(change), S["small"]),
            ]
        )
    if tiles:
        story.append(Paragraph("This month at a glance", S["h"]))
        cols = [[tile[i] for tile in tiles] for i in range(3)]
        tw = width / len(tiles)
        tbl = Table(cols, colWidths=[tw] * len(tiles))
        tbl.setStyle(
            TableStyle(
                [
                    ("BOX", (0, 0), (-1, -1), 0.5, LINE),
                    ("INNERGRID", (0, 0), (-1, -1), 0, colors.white),
                    ("LINEAFTER", (0, 0), (-2, -1), 0.5, LINE),
                    ("TOPPADDING", (0, 0), (-1, -1), 3),
                    ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ]
            )
        )
        story.append(tbl)

    story.append(Paragraph("What's working", S["h"]))
    ok = "✓" if SYMBOLS else "+"
    for line in c.get("working") or ["Nothing stood out this month."]:
        story.append(Paragraph(t(f"{ok}  {line}"), S["body"]))

    story.append(Paragraph("What needs attention", S["h"]))
    if c["findings"]:
        rows = [
            [
                Paragraph(h, S["cellb"])
                for h in (
                    "Status",
                    "What we found",
                    "Why it matters",
                    "How to fix it",
                    "Who",
                )
            ]
        ]
        for f in c["findings"]:
            rows.append(
                [
                    status_para(f["level"], 8),
                    Paragraph(t(f.get("issue")), S["cell"]),
                    Paragraph(t(f.get("impact")), S["cell"]),
                    Paragraph(t(f.get("fix")), S["cell"]),
                    Paragraph(t(f.get("owner")), S["cell"]),
                ]
            )
        tbl = Table(
            rows,
            colWidths=[
                1.05 * inch,
                1.65 * inch,
                1.65 * inch,
                2.2 * inch,
                width - 6.55 * inch,
            ],
            repeatRows=1,
        )
        tbl.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), hexc("EEF1F6")),
                    ("LINEBELOW", (0, 0), (-1, -1), 0.5, LINE),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ]
            )
        )
        story.append(tbl)
    else:
        story.append(Paragraph("Nothing needs attention right now.", S["body"]))

    checks = c.get("checks") or []
    if checks:
        story.append(Paragraph("What we checked", S["h"]))
        cells, last_area = [], None
        for chk in checks:
            if chk.get("area") != last_area:
                last_area = chk.get("area")
                cells.append(Paragraph(t(last_area or ""), S["cellb"]))
            sym, text = CHECK_RESULT.get(chk.get("result"), ("?", chk.get("result")))
            color = {
                "pass": STATUS["healthy"]["color"],
                "action": STATUS["action"]["color"],
                "watch": STATUS["watch"]["color"],
            }.get(chk.get("result"), "777777")
            style = ParagraphStyle("c", parent=S["cell"], textColor=hexc(color))
            label = f"{sym} {chk.get('name')}"
            if chk.get("result") not in ("pass", "action", "watch"):
                label += f" ({chk.get('note') or text.lower()})"
            cells.append(Paragraph(t(label), style))
        half = (len(cells) + 1) // 2
        grid = [
            [cells[i], cells[i + half] if i + half < len(cells) else ""]
            for i in range(half)
        ]
        tbl = Table(grid, colWidths=[width / 2, width / 2])
        tbl.setStyle(
            TableStyle(
                [
                    ("TOPPADDING", (0, 0), (-1, -1), 1),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                ]
            )
        )
        story.append(tbl)
        legend = (
            "✓ passed   ✕ needs action   ! keep an eye on   – doesn't apply or too few calls   "
            "? couldn't check"
        )
        story.append(Spacer(1, 3))
        story.append(Paragraph(t(legend), S["small"]))

    doc.build(story)
    return path


def main(src, out_dir, include_all=False):
    data = load(src)
    os.makedirs(out_dir, exist_ok=True)
    made = [
        build(c, data, out_dir) for c in data["companies"] if wanted(c, include_all)
    ]
    print(f"Saved {len(made)} client PDFs to {out_dir}")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--all"]
    if len(args) != 2:
        sys.exit(__doc__)
    main(args[0], args[1], include_all="--all" in sys.argv)
