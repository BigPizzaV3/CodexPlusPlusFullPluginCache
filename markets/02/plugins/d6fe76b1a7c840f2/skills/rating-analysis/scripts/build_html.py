#!/usr/bin/env python3
"""Build a Moody's Rating Analysis Report as a single self-contained HTML file.

Takes the same payload.json used by build_pptx.py and renders the identical
23 sections as an HTML page with Moody's brand palette, inline charts
(rendered as pure inline SVG — no JS or external libraries), tables, and bullet lists.

Usage:
    python build_html.py <payload.json> <output.html>
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Brand palette (matches build_pptx.py)
# ---------------------------------------------------------------------------
NAVY        = "#040826"
BRIGHT_BLUE = "#005eff"
MID_BLUE    = "#5c068c"
PURPLE      = "#c64809"
PALE        = "#bed6ff"
VERY_PALE   = "#CFD0E1"
PINK        = "#ba0168"
TEAL        = "#5eb6bc"
GOLD        = "#c7ab21"
LIGHT_GRAY  = "#e1e2e1"
TEXT_DARK   = "#222222"
TEXT_MUTED  = "#666B73"
WHITE       = "#FFFFFF"
HEADER_FILL = "#E9EAEE"
GRID_LINE   = "#CFD0E1"

PIE_PALETTE = [BRIGHT_BLUE, TEAL, GOLD, MID_BLUE, PURPLE, PINK, PALE, VERY_PALE]
SCATTER_COLORS = [BRIGHT_BLUE, PINK, TEAL, GOLD, MID_BLUE, PURPLE]
OUTLOOK_PALETTE = {
    "stable":       "#e1e2e1",  # light gray
    "positive":     "#5eb6bc",  # teal
    "negative":     "#f09615",  # amber
    "under review": "#005eff",  # bright blue
}

RATING_SCALE = {
    21:"Aaa", 20:"Aa1", 19:"Aa2", 18:"Aa3",
    17:"A1",  16:"A2",  15:"A3",
    14:"Baa1",13:"Baa2",12:"Baa3",
    11:"Ba1", 10:"Ba2",  9:"Ba3",
     8:"B1",   7:"B2",   6:"B3",
     5:"Caa1", 4:"Caa2", 3:"Caa3",
     2:"Ca",   1:"C",
}

_NOTCH = {v: k for k, v in RATING_SCALE.items()}

_TAG_RE = re.compile(r"<[^>]+>")


def html_to_text(s):
    if s is None:
        return ""
    s = str(s)
    s = (s.replace("</p>", "\n\n")
          .replace("<br>", "\n").replace("<br/>", "\n").replace("<br />", "\n")
          .replace("<li>", "• ").replace("</li>", "\n"))
    s = _TAG_RE.sub("", s)
    s = (s.replace("&amp;", "&").replace("&nbsp;", " ")
          .replace("&rarr;", "→").replace("&#39;", "'")
          .replace("&quot;", '"').replace("&lt;", "<").replace("&gt;", ">"))
    return "\n".join(line.rstrip() for line in s.splitlines()).strip()


def esc(s):
    """HTML-escape a string for safe inline output."""
    return (str(s or "")
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;"))


def bullets_html(items, bullet="•"):
    """Render a list of strings as <ul> bullet items."""
    if not items:
        return ""
    if isinstance(items, str):
        items = [items] if items.strip() else []
    lines = []
    for it in items:
        if it is None:
            continue
        text = html_to_text(str(it))
        if text:
            lines.append(f"<li>{esc(text)}</li>")
    return f"<ul>{''.join(lines)}</ul>" if lines else ""


def bold_prefix_bullets_html(items):
    """Render [{bold, text}] or strings as <ul> with bolded prefix."""
    if not items:
        return ""
    lines = []
    for item in items:
        if isinstance(item, dict):
            prefix = html_to_text(item.get("bold") or item.get("prefix")
                                   or item.get("date") or "")
            rest = html_to_text(item.get("text") or item.get("summary") or "")
        elif isinstance(item, (tuple, list)) and len(item) >= 2:
            prefix, rest = str(item[0]), str(item[1])
        else:
            prefix, rest = "", html_to_text(str(item))
        if prefix and rest:
            lines.append(f"<li><strong>{esc(prefix)}</strong> – {esc(rest)}</li>")
        elif prefix:
            lines.append(f"<li><strong>{esc(prefix)}</strong></li>")
        else:
            lines.append(f"<li>{esc(rest)}</li>")
    return f"<ul>{''.join(lines)}</ul>" if lines else ""


def table_html(headers, rows, *, first_col_bold=False, col_widths=None):
    """Generate an HTML table."""
    total_w = sum(col_widths) if col_widths else None
    th_parts = []
    for i, h in enumerate(headers):
        style = ""
        if col_widths and i < len(col_widths):
            pct = round(col_widths[i] / total_w * 100, 1)
            style = f' style="width:{pct}%"'
        th_parts.append(f"<th{style}>{esc(h)}</th>")
    thead = f"<thead><tr>{''.join(th_parts)}</tr></thead>"
    body_rows = []
    for row in rows:
        tds = []
        for j, val in enumerate(row):
            bold = first_col_bold and j == 0
            content = f"<strong>{esc(val)}</strong>" if bold else esc(val)
            tds.append(f"<td>{content}</td>")
        body_rows.append(f"<tr>{''.join(tds)}</tr>")
    tbody = f"<tbody>{''.join(body_rows)}</tbody>"
    return f"<table>{thead}{tbody}</table>"


def _normalize_categorized(section):
    if isinstance(section, str):
        out = []
        for chunk in section.split("<strong")[1:]:
            _, _, rest = chunk.partition(">")
            name, _, tail = rest.partition("</strong>")
            items = []
            if "<ul>" in tail and "</ul>" in tail:
                ul = tail.split("<ul>", 1)[1].split("</ul>", 1)[0]
                for li in ul.split("<li>")[1:]:
                    t = li.split("</li>", 1)[0].strip()
                    t = t.replace("&amp;", "&").replace("&nbsp;", " ")
                    if t:
                        items.append(t)
            out.append({"name": name.replace("&amp;", "&").strip(), "items": items})
        return out
    if isinstance(section, list):
        result = []
        for g in section:
            if isinstance(g, dict):
                result.append({
                    "name": g.get("name") or g.get("category") or "",
                    "items": g.get("items") or [],
                })
        return result
    if isinstance(section, dict):
        if section.get("groups"):
            return _normalize_categorized(section["groups"])
        if section.get("html"):
            return _normalize_categorized(section["html"])
    return []


# ---------------------------------------------------------------------------
# Chart builders (emit pure inline SVG — no JS, no external libraries)
#
# The report renders inside a sandboxed about:srcdoc iframe (Teams / M365
# Copilot host) that blocks external CDN scripts and cannot be relied on to
# execute JS. All charts are therefore computed here in Python and emitted as
# static SVG so they render everywhere — srcdoc, PDF export, print, email.
# Motion is added with CSS animations only (see CSS block), so it stays
# JS-free and honours prefers-reduced-motion.
# ---------------------------------------------------------------------------

def _fmt_num(v, y_format=None):
    """Format a value the way the old Chart.js tick/datalabel callbacks did."""
    if v is None:
        return ""
    v = float(v)
    if y_format == "#,##0":
        return f"{v:,.0f}"
    if y_format and "%" in y_format:
        return f"{v:.1f}%"
    if y_format and "x" in y_format:
        return f"{v:.1f}x"
    if v.is_integer():
        return f"{v:.0f}"
    return f"{v:g}"


def _nice_ticks(lo, hi, count=4):
    """Evenly spaced tick values spanning [lo, hi] inclusive."""
    if hi <= lo:
        hi = lo + 1
    step = (hi - lo) / count
    return [lo + step * i for i in range(count + 1)]


def _truncate(s, n):
    s = str(s)
    return s if len(s) <= n else s[: max(1, n - 1)] + "…"


def _svg_open(height, vw=480):
    return (f'<svg viewBox="0 0 {vw} {int(height)}" width="100%" '
            f'style="height:auto;display:block;'
            f'font-family:Arial,Helvetica,sans-serif" '
            f'role="img" xmlns="http://www.w3.org/2000/svg">')


def _chart_wrap(title, svg):
    return f"""
<div class="chart-wrap">
  {f'<div class="chart-title">{esc(title)}</div>' if title else ''}
  {svg}
</div>"""


def bar_chart_html(title, categories, values, *, color=BRIGHT_BLUE,
                   y_format=None, width="100%", height=280, horizontal=False,
                   x_label="", y_label=""):
    cats = [str(c) for c in categories]
    vals = [float(v) if v is not None else 0.0 for v in values]
    VW, VH = 480, int(height)
    n = len(vals) or 1
    p = [_svg_open(VH, VW)]

    # For horizontal bars the categories sit on Y and values on X.
    cat_axis_label = y_label if horizontal else x_label
    val_axis_label = x_label if horizontal else y_label

    vmax = max(vals + [0.0])
    vmin = min(vals + [0.0])
    lo = min(0.0, vmin)

    if horizontal:
        ML, MR, MT = 94, 46, 8
        MB = 34 if val_axis_label else 20
        plot_w, plot_h = VW - ML - MR, VH - MT - MB
        hi = vmax * 1.02 if vmax > 0 else 1.0
        span = (hi - lo) or 1.0
        xat = lambda v: ML + (v - lo) / span * plot_w
        band = plot_h / n
        bar_h = min(band * 0.6, 26)
        for t in _nice_ticks(lo, hi, 4):
            gx = xat(t)
            p.append(f'<line x1="{gx:.1f}" y1="{MT}" x2="{gx:.1f}" y2="{MT+plot_h:.1f}" stroke="{GRID_LINE}" stroke-width="1"/>')
            p.append(f'<text x="{gx:.1f}" y="{MT+plot_h+14:.1f}" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">{esc(_fmt_num(t, y_format))}</text>')
        for i, v in enumerate(vals):
            cy = MT + band * i + band / 2
            x0, x1 = xat(min(0.0, v)), xat(max(0.0, v))
            delay = f"{i*0.06:.2f}s"
            p.append(f'<rect class="svg-bar-h" style="animation-delay:{delay}" x="{x0:.1f}" y="{cy-bar_h/2:.1f}" width="{max(0.0,x1-x0):.1f}" height="{bar_h:.1f}" fill="{color}"/>')
            p.append(f'<text class="svg-lbl" style="animation-delay:{delay}" x="{x1+4:.1f}" y="{cy:.1f}" fill="{TEXT_DARK}" font-size="10" font-weight="bold" text-anchor="start" dominant-baseline="middle">{esc(_fmt_num(v, y_format))}</text>')
            p.append(f'<text x="{ML-6}" y="{cy:.1f}" fill="{TEXT_MUTED}" font-size="10" text-anchor="end" dominant-baseline="middle">{esc(_truncate(cats[i], 18))}</text>')
        if val_axis_label:
            p.append(f'<text x="{ML+plot_w/2:.1f}" y="{VH-4}" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">{esc(val_axis_label)}</text>')
    else:
        ML, MR, MT = 48, 16, 22
        MB = 40 if cat_axis_label else 30
        plot_w, plot_h = VW - ML - MR, VH - MT - MB
        hi = vmax * 1.15 if vmax > 0 else 1.0
        span = (hi - lo) or 1.0
        yat = lambda v: MT + plot_h - (v - lo) / span * plot_h
        band = plot_w / n
        bar_w = min(band * 0.6, 48)
        for t in _nice_ticks(lo, hi, 4):
            gy = yat(t)
            p.append(f'<line x1="{ML}" y1="{gy:.1f}" x2="{ML+plot_w:.1f}" y2="{gy:.1f}" stroke="{GRID_LINE}" stroke-width="1"/>')
            p.append(f'<text x="{ML-6}" y="{gy+3:.1f}" fill="{TEXT_MUTED}" font-size="10" text-anchor="end">{esc(_fmt_num(t, y_format))}</text>')
        for i, v in enumerate(vals):
            cx = ML + band * i + band / 2
            y0, y1 = yat(min(0.0, v)), yat(max(0.0, v))
            delay = f"{i*0.06:.2f}s"
            p.append(f'<rect class="svg-bar-v" style="animation-delay:{delay}" x="{cx-bar_w/2:.1f}" y="{min(y0,y1):.1f}" width="{bar_w:.1f}" height="{abs(y1-y0):.1f}" fill="{color}"/>')
            p.append(f'<text class="svg-lbl" style="animation-delay:{delay}" x="{cx:.1f}" y="{min(y0,y1)-4:.1f}" fill="{TEXT_DARK}" font-size="10" font-weight="bold" text-anchor="middle">{esc(_fmt_num(v, y_format))}</text>')
            p.append(f'<text x="{cx:.1f}" y="{MT+plot_h+14:.1f}" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">{esc(_truncate(cats[i], 12))}</text>')
        if cat_axis_label:
            p.append(f'<text x="{ML+plot_w/2:.1f}" y="{VH-4}" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">{esc(cat_axis_label)}</text>')

    p.append("</svg>")
    return _chart_wrap(title, "\n  ".join(p))


def line_chart_html(title, categories, values, *, color=BRIGHT_BLUE,
                    rating_scale=False, height=240):
    cats = [str(c) for c in categories]
    vals = [float(v) if v is not None else None for v in values]
    VW, VH = 480, int(height)
    n = len(vals)
    p = [_svg_open(VH, VW)]
    ML, MR, MT, MB = 54, 16, 12, 28
    plot_w, plot_h = VW - ML - MR, VH - MT - MB
    clean = [v for v in vals if v is not None]

    if rating_scale:
        if clean:
            current = int(round(max(clean)))
            lo = max(1, current - 5)
            hi = min(21, current + 5)
        else:
            lo, hi = 1, 21
        ticks = list(range(lo, hi + 1))
        ylabel = lambda t: RATING_SCALE.get(int(round(t)), "")
    else:
        if clean:
            lo, hi = min(clean), max(clean)
            if lo == hi:
                lo, hi = lo - 1, hi + 1
            pad = (hi - lo) * 0.1
            lo, hi = lo - pad, hi + pad
        else:
            lo, hi = 0.0, 1.0
        ticks = _nice_ticks(lo, hi, 4)
        ylabel = lambda t: _fmt_num(t)

    span = (hi - lo) or 1.0
    yat = lambda v: MT + plot_h - (v - lo) / span * plot_h
    xat = lambda i: ML + (plot_w * (i / (n - 1)) if n > 1 else plot_w / 2)

    for t in ticks:
        gy = yat(t)
        p.append(f'<line x1="{ML}" y1="{gy:.1f}" x2="{ML+plot_w:.1f}" y2="{gy:.1f}" stroke="{GRID_LINE}" stroke-width="1"/>')
        p.append(f'<text x="{ML-6}" y="{gy+3:.1f}" fill="{TEXT_MUTED}" font-size="10" text-anchor="end">{esc(ylabel(t))}</text>')
    for i, c in enumerate(cats):
        p.append(f'<text x="{xat(i):.1f}" y="{MT+plot_h+16:.1f}" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">{esc(c)}</text>')

    # spanGaps: connect only the non-null points, in order
    pts = [(xat(i), yat(v)) for i, v in enumerate(vals) if v is not None]
    if len(pts) > 1:
        d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        p.append(f'<polyline class="svg-line" pathLength="1" points="{d}" fill="none" stroke="{color}" stroke-width="2"/>')
    for j, (x, y) in enumerate(pts):
        p.append(f'<circle class="svg-pt" style="animation-delay:{0.6+j*0.08:.2f}s" cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{color}"/>')

    p.append("</svg>")
    return _chart_wrap(title, "\n  ".join(p))


def pie_chart_html(title, labels, values, *, colors=None, use_legend=True,
                   height=260):
    labs = [str(l) for l in labels]
    vals = [float(v or 0) for v in values]
    palette = list(colors) if colors else PIE_PALETTE
    used = [palette[i % len(palette)] for i in range(len(labs))]
    total = sum(vals)
    VW, VH = 480, int(height)
    p = [_svg_open(VH, VW)]

    legend_h = (((len(labs) + 1) // 2) * 16 + 8) if use_legend else 0
    cx = VW / 2
    cy = (VH - legend_h) / 2
    r = max(10.0, min(cx, cy) - 12)

    if total <= 0:
        p.append(f'<text x="{cx:.1f}" y="{cy:.1f}" fill="{TEXT_MUTED}" font-size="12" text-anchor="middle">No data</text>')
    else:
        ang = -math.pi / 2  # start at 12 o'clock
        for i, v in enumerate(vals):
            frac = v / total
            if frac <= 0:
                continue
            a2 = ang + frac * 2 * math.pi
            delay = f"{i*0.08:.2f}s"
            if frac >= 0.9999:
                p.append(f'<circle class="svg-slice" style="animation-delay:{delay}" cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{used[i]}"/>')
            else:
                x1, y1 = cx + r * math.cos(ang), cy + r * math.sin(ang)
                x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
                large = 1 if frac > 0.5 else 0
                p.append(f'<path class="svg-slice" style="animation-delay:{delay}" d="M {cx:.1f} {cy:.1f} L {x1:.1f} {y1:.1f} A {r:.1f} {r:.1f} 0 {large} 1 {x2:.1f} {y2:.1f} Z" fill="{used[i]}" stroke="#ffffff" stroke-width="2"/>')
            if frac >= 0.05:
                mid = (ang + a2) / 2
                lx, ly = cx + r * 0.6 * math.cos(mid), cy + r * 0.6 * math.sin(mid)
                p.append(f'<text class="svg-lbl" style="animation-delay:{delay}" x="{lx:.1f}" y="{ly:.1f}" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle" dominant-baseline="middle">{frac*100:.1f}%</text>')
            ang = a2

    if use_legend and total > 0:
        lgy = VH - legend_h + 4
        col_w = VW / 2
        for i, lab in enumerate(labs):
            row, col = divmod(i, 2)
            lx = 16 + col * col_w
            ly = lgy + row * 16
            p.append(f'<rect x="{lx:.1f}" y="{ly:.1f}" width="10" height="10" fill="{used[i]}"/>')
            p.append(f'<text x="{lx+14:.1f}" y="{ly+9:.1f}" fill="{TEXT_DARK}" font-size="10">{esc(_truncate(lab, 26))}</text>')

    p.append("</svg>")
    return _chart_wrap(title, "\n  ".join(p))


def scatter_chart_html(title, points, *, x_label="", y_label="", height=280):
    clean = []
    for pt in (points or []):
        x, y = pt.get("x"), pt.get("y")
        if x is None or y is None:
            continue
        try:
            clean.append((pt.get("company", ""), float(x), float(y)))
        except (TypeError, ValueError):
            continue

    VW, VH = 480, int(height)
    p = [_svg_open(VH, VW)]
    ML, MR, MT = 52, 40, 16
    MB = 40 if x_label else 30
    plot_w, plot_h = VW - ML - MR, VH - MT - MB

    xs = [x for _, x, _ in clean] or [0.0, 1.0]
    ys = [y for _, _, y in clean] or [0.0, 1.0]
    xlo, xhi = min(xs), max(xs)
    ylo, yhi = min(ys), max(ys)
    if xlo == xhi:
        xlo, xhi = xlo - 1, xhi + 1
    if ylo == yhi:
        ylo, yhi = ylo - 1, yhi + 1
    xpad, ypad = (xhi - xlo) * 0.15, (yhi - ylo) * 0.15
    xlo, xhi = xlo - xpad, xhi + xpad
    ylo, yhi = ylo - ypad, yhi + ypad
    xat = lambda v: ML + (v - xlo) / (xhi - xlo) * plot_w
    yat = lambda v: MT + plot_h - (v - ylo) / (yhi - ylo) * plot_h

    for t in _nice_ticks(xlo, xhi, 4):
        gx = xat(t)
        p.append(f'<line x1="{gx:.1f}" y1="{MT}" x2="{gx:.1f}" y2="{MT+plot_h:.1f}" stroke="{GRID_LINE}" stroke-width="1"/>')
        p.append(f'<text x="{gx:.1f}" y="{MT+plot_h+14:.1f}" fill="{TEXT_MUTED}" font-size="9" text-anchor="middle">{esc(_fmt_num(t))}</text>')
    for t in _nice_ticks(ylo, yhi, 4):
        gy = yat(t)
        p.append(f'<line x1="{ML}" y1="{gy:.1f}" x2="{ML+plot_w:.1f}" y2="{gy:.1f}" stroke="{GRID_LINE}" stroke-width="1"/>')
        p.append(f'<text x="{ML-6}" y="{gy+3:.1f}" fill="{TEXT_MUTED}" font-size="9" text-anchor="end">{esc(_fmt_num(t))}</text>')

    half = 22  # diamond half-diagonal (matches old pointRadius 28 look)
    for i, (name, x, y) in enumerate(clean):
        col = SCATTER_COLORS[i % len(SCATTER_COLORS)]
        px, py = xat(x), yat(y)
        delay = f"{i*0.08:.2f}s"
        pts = f"{px:.1f},{py-half:.1f} {px+half:.1f},{py:.1f} {px:.1f},{py+half:.1f} {px-half:.1f},{py:.1f}"
        p.append(f'<polygon class="svg-mark" style="animation-delay:{delay}" points="{pts}" fill="{col}"/>')
        p.append(f'<text class="svg-lbl" style="animation-delay:{delay}" x="{px:.1f}" y="{py:.1f}" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle" dominant-baseline="middle">{esc(_truncate(name, 8))}</text>')

    if x_label:
        p.append(f'<text x="{ML+plot_w/2:.1f}" y="{VH-4}" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle">{esc(x_label)}</text>')
    if y_label:
        yc = MT + plot_h / 2
        p.append(f'<text x="12" y="{yc:.1f}" fill="{TEXT_MUTED}" font-size="10" text-anchor="middle" transform="rotate(-90 12 {yc:.1f})">{esc(y_label)}</text>')

    p.append("</svg>")
    return _chart_wrap(title, "\n  ".join(p))


# ---------------------------------------------------------------------------
# Section builders — one function per slide/section
# ---------------------------------------------------------------------------

def section_header(title, part=None):
    part_html = f'<span class="section-part">{esc(part)}</span>' if part else ""
    return f"""<div class="section-header">{part_html}<h2>{esc(title)}</h2></div>"""


def build_cover(data):
    company = data.get("target_company", "")
    sector = data.get("sector", "")
    date = data.get("report_date", "")
    return f"""
<section class="slide cover">
  <div class="cover-inner">
    <div class="cover-badge">MOODY'S ANALYTICS</div>
    <h1 class="cover-company">{esc(company)}</h1>
    <div class="cover-sub">Rating Analysis Deck</div>
    <div class="cover-meta">
      <span>{esc(sector)}</span>
      <span class="divider">|</span>
      <span>Report date: {esc(date)}</span>
    </div>
  </div>
</section>"""


def build_agenda(data):
    items = [
        ("01", "Sector Analysis",
         "Macro context, sector outlook and recent rating actions"),
        ("02", "Company Credit Overview",
         "Financial profile, SWOT, strategy and news"),
        ("03", "Company Positioning vs. Peers",
         "Benchmarking on leverage, profitability, scorecard and ESG"),
    ]
    cards = ""
    for num, title, desc in items:
        cards += f"""
<div class="agenda-card">
  <div class="agenda-num">{num}</div>
  <div class="agenda-title">{title}</div>
  <div class="agenda-desc">{esc(desc)}</div>
</div>"""
    return f"""
<section class="slide">
  {section_header("Agenda")}
  <div class="agenda-grid">{cards}</div>
</section>"""


def build_divider(title):
    return f"""
<section class="slide divider-slide">
  <div class="divider-inner">
    <div class="divider-label">PART</div>
    <h2 class="divider-title">{esc(title.upper())}</h2>
  </div>
</section>"""


def build_sector_overview(data):
    sec = data.get("sections", {}).get("sector_overview", {}) or {}
    sector = data.get("sector", "")
    cols = [
        ("SECTOR OVERVIEW", sec.get("overview_bullets", [])),
        ("WHAT TO LOOK OUT FOR?", sec.get("watchlist_bullets", [])),
        ("KEY TAKEAWAYS", sec.get("takeaway_bullets", [])),
    ]
    grid = ""
    for col_title, items in cols:
        grid += f"""
<div class="three-col-card">
  <div class="col-header">{esc(col_title)}</div>
  {bullets_html(items)}
</div>"""
    return f"""
<section class="slide">
  {section_header(f"{sector} – Sector Overview", "Part 1 · Sector Analysis")}
  <div class="three-col-grid">{grid}</div>
  <div class="source">Source: Moodys.com</div>
</section>"""


def build_moodys_view(data):
    mv = data.get("sections", {}).get("moodys_view", {}) or {}
    sector = data.get("sector", "")
    summary = html_to_text(mv.get("outlook_summary", ""))
    positioning = html_to_text(mv.get("company_positioning", ""))
    dist = mv.get("outlook_distribution") or []

    pie_html = ""
    if dist:
        labels = [d.get("category", "") for d in dist]
        values = [d.get("count", d.get("percentage", 0)) for d in dist]
        colors = [OUTLOOK_PALETTE.get(str(d.get("category", "")).lower(), BRIGHT_BLUE)
                  for d in dist]
        pie_html = pie_chart_html("Moody's Outlook Distribution",
                                  labels, values, colors=colors, height=220)

    text_html = ""
    if summary:
        text_html += f'<p class="outlook-summary">{esc(summary)}</p>'
    if positioning:
        text_html += f'<p class="company-positioning"><strong>Company positioning:</strong> {esc(positioning)}</p>'

    return f"""
<section class="slide">
  {section_header(f"{sector} – Moody's View", "Part 1 · Sector Analysis")}
  <div class="two-col-layout">
    <div class="col">{text_html}</div>
    <div class="col">{pie_html}</div>
  </div>
  <div class="source">Source: Moodys.com</div>
</section>"""


def build_macro_outlook(data):
    macro = data.get("sections", {}).get("macro_outlook", {}) or {}
    tbl = macro.get("gdp_table", {}) or {}
    years = tbl.get("year_columns", []) or []
    rows = tbl.get("rows", []) or []
    commentary = macro.get("gdp_commentary", []) or []

    table_html_str = ""
    if years and rows:
        headers = ["Country"] + [f"{y} GDP Growth" for y in years]
        body = [[r.get("country", "")] + list(r.get("values", [])) for r in rows]
        col_widths = [2.0] + [1.2] * len(years)
        table_html_str = table_html(headers, body, col_widths=col_widths)

    return f"""
<section class="slide">
  {section_header("Global Macro Outlook", "Part 1 · Sector Analysis")}
  {bullets_html(commentary)}
  {table_html_str}
  <div class="source">Source: Moodys.com</div>
</section>"""


def build_rating_actions(data):
    actions = data.get("sections", {}).get("rating_actions_ytd", []) or []
    items = []
    for a in actions[:10]:
        date = a.get("date", "")
        company = a.get("company", "")
        summary = a.get("summary", "")
        prefix = f"{date} – {company}" if company else date
        items.append({"bold": prefix, "text": summary})
    return f"""
<section class="slide">
  {section_header("Moody's Rating Actions – YTD", "Part 1 · Sector Analysis")}
  {bold_prefix_bullets_html(items)}
  <div class="source">Source: Moodys.com</div>
</section>"""


def build_financial_analysis(data):
    company = data.get("target_company", "")
    fa = data.get("sections", {}).get("financial_analysis", {}) or {}
    commentary = fa.get("commentary", []) or []
    if isinstance(commentary, str):
        commentary = [commentary] if commentary.strip() else []
    history = fa.get("rating_history", []) or []

    # Sort oldest → newest
    _MONTH_MAP = {"jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,
                  "jul":7,"aug":8,"sep":9,"oct":10,"nov":11,"dec":12}
    def _date_key(e):
        raw = e.get("date", "")
        m = re.search(r"(\d{4})", raw)
        year = int(m.group(1)) if m else 0
        mn = re.search(r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)",
                       raw.lower())
        month = _MONTH_MAP.get(mn.group(1), 0) if mn else 0
        return (year, month)
    history = sorted(history, key=_date_key)

    chart_data = [_NOTCH.get(e.get("rating", ""), 0) for e in history] if history \
        else (fa.get("rating_chart_data", []) or [])

    line_html = ""
    if chart_data:
        cats = [e.get("date", f"P{i+1}") for i, e in enumerate(history)]
        if len(cats) < len(chart_data):
            cats += [f"P{i+1}" for i in range(len(cats), len(chart_data))]
        elif len(cats) > len(chart_data):
            cats = cats[:len(chart_data)]
        if len(chart_data) == 1:
            import datetime
            today_label = datetime.date.today().strftime("%b %Y")
            cats = cats + [today_label]
            chart_data = chart_data + [chart_data[0]]
        line_html = line_chart_html(
            f"Moody's Rating History for {company}",
            cats, chart_data, color=BRIGHT_BLUE, rating_scale=True, height=200)

    rationale_items = []
    for h in history:
        rationale_items.append({"bold": h.get("date", ""),
                                 "text": h.get("reason", h.get("rating", ""))})

    return f"""
<section class="slide">
  {section_header(f"{company} Financial Analysis", "Part 2 · Company Credit Overview")}
  <div class="two-col-layout">
    <div class="col">
      {bullets_html(commentary)}
    </div>
    <div class="col">
      {line_html}
      <div class="subsection-title">Moody's rating rationale</div>
      {bold_prefix_bullets_html(rationale_items)}
    </div>
  </div>
  <div class="source">Source: Moodys.com, Company filings</div>
</section>"""


def build_revenue_distribution(data):
    company = data.get("target_company", "")
    rd = data.get("sections", {}).get("revenue_distribution", {}) or {}
    commentary = rd.get("commentary", []) or []
    geo = rd.get("by_geography", []) or []
    seg = rd.get("by_segment", []) or []

    def _clean(items):
        out = []
        for it in (items or []):
            name = str(it.get("name", "")).strip()
            try:
                pct = float(it.get("percentage", 0) or 0)
            except (TypeError, ValueError):
                pct = 0.0
            if name and pct > 0:
                out.append((name, pct))
        return out

    geo_clean = _clean(geo)
    seg_clean = _clean(seg)

    geo_chart = pie_chart_html(f"{company} Revenue by Region",
                               [n for n, _ in geo_clean],
                               [p for _, p in geo_clean],
                               height=240) if geo_clean else ""
    seg_chart = pie_chart_html(f"{company} Revenue by Segment",
                               [n for n, _ in seg_clean],
                               [p for _, p in seg_clean],
                               height=240) if seg_clean else ""

    return f"""
<section class="slide">
  {section_header("Revenue Distribution", "Part 2 · Company Credit Overview")}
  {bullets_html(commentary)}
  <div class="two-col-layout">
    <div class="col">{geo_chart}</div>
    <div class="col">{seg_chart}</div>
  </div>
  <div class="source">Source: Moodys.com, Company filings</div>
</section>"""


def build_swot(data):
    swot = data.get("sections", {}).get("swot", {}) or {}
    quads = [
        ("Strengths",     swot.get("strengths", []),     "swot-s"),
        ("Weaknesses",    swot.get("weaknesses", []),     "swot-w"),
        ("Opportunities", swot.get("opportunities", []), "swot-o"),
        ("Threats",       swot.get("threats", []),       "swot-t"),
    ]
    cells = ""
    for label, items, cls in quads:
        cells += f"""
<div class="swot-cell {cls}">
  <div class="swot-label">{label}</div>
  {bullets_html(items)}
</div>"""
    return f"""
<section class="slide">
  {section_header("SWOT Analysis", "Part 2 · Company Credit Overview")}
  <div class="swot-grid">{cells}</div>
  <div class="source">Source: Moodys.com, Company filings</div>
</section>"""


def build_key_metrics(data):
    company = data.get("target_company", "")
    km = data.get("sections", {}).get("key_metrics", {}) or {}
    periods = km.get("periods", []) or []
    charts_def = [
        ("Revenue",        km.get("revenue", []),     "#,##0"),
        ("EBIT Margin",    km.get("ebit_margin", []), "0.0%"),
        ("Debt / EBITDA",  km.get("debt_ebitda", []), "0.0x"),
        ("RCF / Net Debt", km.get("rcf_net_debt", []), "0.0%"),
    ]
    charts_html = ""
    for title, vals, fmt in charts_def:
        cats = periods[:len(vals)] if periods else [f"P{k+1}" for k in range(len(vals))]
        if vals:
            charts_html += f'<div class="col">{bar_chart_html(title, cats, vals, color=BRIGHT_BLUE, y_format=fmt, height=220)}</div>'
        else:
            charts_html += f'<div class="col"><div class="no-data">{esc(title)}<br>(no data)</div></div>'

    return f"""
<section class="slide">
  {section_header(f"Key Financial Metrics – {company}", "Part 2 · Company Credit Overview")}
  <div class="two-col-layout">{charts_html}</div>
  <div class="two-col-layout">{''}</div>
  <div class="source">Source: Moodys.com, Company filings</div>
</section>"""


def _build_key_metrics_four(data):
    """Render four charts in a 2×2 grid."""
    company = data.get("target_company", "")
    km = data.get("sections", {}).get("key_metrics", {}) or {}
    periods = km.get("periods", []) or []
    charts_def = [
        ("Revenue",        km.get("revenue", []),     "#,##0"),
        ("EBIT Margin",    km.get("ebit_margin", []), "0.0%"),
        ("Debt / EBITDA",  km.get("debt_ebitda", []), "0.0x"),
        ("RCF / Net Debt", km.get("rcf_net_debt", []), "0.0%"),
    ]
    row1 = row2 = ""
    for i, (title, vals, fmt) in enumerate(charts_def):
        cats = periods[:len(vals)] if periods else [f"P{k+1}" for k in range(len(vals))]
        cell = ""
        if vals:
            cell = f'<div class="col">{bar_chart_html(title, cats, vals, color=BRIGHT_BLUE, y_format=fmt, height=200)}</div>'
        else:
            cell = f'<div class="col"><div class="no-data">{esc(title)}<br>(no data)</div></div>'
        if i < 2:
            row1 += cell
        else:
            row2 += cell

    return f"""
<section class="slide">
  {section_header(f"Key Financial Metrics – {company}", "Part 2 · Company Credit Overview")}
  <div class="two-col-layout">{row1}</div>
  <div class="two-col-layout" style="margin-top:12px">{row2}</div>
  <div class="source">Source: Moodys.com, Company filings</div>
</section>"""


def build_strategic_updates(data):
    company = data.get("target_company", "")
    sup = data.get("sections", {}).get("strategic_updates", {}) or {}
    return f"""
<section class="slide">
  {section_header(f"{company} Strategic Updates", "Part 2 · Company Credit Overview")}
  <div class="two-col-layout">
    <div class="col">
      <div class="col-header">RECENT DEVELOPMENTS</div>
      {bullets_html(sup.get("recent", []))}
    </div>
    <div class="col">
      <div class="col-header">FORWARD LOOKING</div>
      {bullets_html(sup.get("forward", []))}
    </div>
  </div>
  <div class="source">Source: Moodys.com, Company filings</div>
</section>"""


def build_categorized(data, section_key, title, source):
    groups = _normalize_categorized(data.get("sections", {}).get(section_key))
    content = ""
    for g in groups:
        name = g.get("name", "")
        items = g.get("items") or []
        bullets = []
        for it in items:
            if isinstance(it, dict):
                prefix = it.get("date") or it.get("when") or ""
                body = it.get("text") or it.get("summary") or ""
                bullets.append({"bold": f"{prefix} →" if prefix else "", "text": body})
            else:
                bullets.append(str(it))
        bullets_rendered = ""
        if any(isinstance(b, dict) for b in bullets):
            bullets_rendered = bold_prefix_bullets_html(bullets)
        else:
            bullets_rendered = bullets_html(bullets)
        content += f"""
<div class="category-group">
  <div class="category-name">{esc(name)}</div>
  {bullets_rendered}
</div>"""
    return f"""
<section class="slide">
  {section_header(title, "Part 2 · Company Credit Overview")}
  {content}
  <div class="source">Source: {esc(source)}</div>
</section>"""


def build_peer_summary(data):
    ps = data.get("sections", {}).get("peer_summary", {}) or {}
    table = ps.get("table", []) or []
    commentary = ps.get("commentary", []) or []
    if isinstance(commentary, str):
        commentary = [commentary] if commentary.strip() else []

    table_html_str = ""
    if table:
        fields = [
            ("Country", "country"),
            ("Market Capitalization", "market_cap"),
            ("Moody's Ratings", "rating"),
            ("Outlook", "outlook"),
            ("Business Mix", "business_mix"),
        ]
        headers = [""] + [c.get("company", "") for c in table]
        body = []
        for label, key in fields:
            body.append([label] + [str(c.get(key, "") or "") for c in table])
        col_widths = [1.6] + [1.0] * len(table)
        table_html_str = table_html(headers, body, first_col_bold=True,
                                    col_widths=col_widths)

    return f"""
<section class="slide">
  {section_header("Peer Comparison Summary", "Part 3 · Company Positioning vs. Peers")}
  {bullets_html(commentary)}
  {table_html_str}
  <div class="source">Source: Moodys.com, Company filings</div>
</section>"""


def build_peer_financials(data):
    pf = data.get("sections", {}).get("peer_financials", {}) or {}
    columns = pf.get("columns", []) or []
    rows = pf.get("rows", []) or []

    table_html_str = ""
    if rows and columns:
        headers = ["Financial Items (in millions)"] + [r.get("company", "") for r in rows]
        body = [["Period"]   + [str(r.get("period", "") or "") for r in rows],
                ["Currency"] + [str(r.get("currency", "") or "") for r in rows]]
        for i, label in enumerate(columns):
            body.append([label] + [str((r.get("values") or [])[i]
                                       if i < len(r.get("values", [])) else "")
                                   for r in rows])
        col_widths = [2.0] + [1.0] * len(rows)
        table_html_str = table_html(headers, body, first_col_bold=True,
                                    col_widths=col_widths)

    return f"""
<section class="slide">
  {section_header("Detailed Peer Comparison", "Part 3 · Company Positioning vs. Peers")}
  {table_html_str}
  <div class="source">Source: Moodys.com, Company filings</div>
</section>"""


def _build_peer_bars(data, section_key, title, chart_defs):
    section = data.get("sections", {}).get(section_key, {}) or {}
    commentary = section.get("commentary")
    if isinstance(commentary, str):
        commentary = [commentary]

    # Map fmt string → human-readable unit for the value-axis title
    _unit_labels = {
        "#,##0":  "USD M",
        "0.0%":   "%",
        "0.0x":   "x",
    }

    charts_html = ""
    for chart_title, key, fmt in chart_defs:
        entries = section.get(key, []) or []
        clean = [(e.get("company", ""), e.get("value"), e.get("period", ""))
                 for e in entries if e.get("value") is not None]
        if not clean:
            continue
        clean.sort(key=lambda p: (p[1] if p[1] is not None else -1e9))

        # Always include the period in the bar label so the date of financials
        # is visible directly on the chart, regardless of whether periods differ.
        cat_labels = [f"{c[0]}\n({c[2]})" if c[2] else c[0] for c in clean]

        # Value-axis title: metric name + unit (e.g. "Debt / EBITDA (x)")
        unit = _unit_labels.get(fmt, "")
        val_axis_title = f"{chart_title} ({unit})" if unit else chart_title

        charts_html += (
            f'<div class="col">'
            f'{bar_chart_html(chart_title, cat_labels, [c[1] for c in clean], color=BRIGHT_BLUE, y_format=fmt, height=280, horizontal=True, x_label=val_axis_title)}'
            f'</div>'
        )

    return f"""
<section class="slide">
  {section_header(title, "Part 3 · Company Positioning vs. Peers")}
  {bullets_html(commentary)}
  <div class="two-col-layout">{charts_html}</div>
  <div class="source">Source: Moodys.com, Company filings</div>
</section>"""


def build_peer_debt(data):
    return _build_peer_bars(data, "peer_debt_charts",
                            "Peer Comparison – Debt",
                            [("Debt / EBITDA", "debt_ebitda", "0.0x"),
                             ("RCF / Net Debt", "rcf_net_debt", "0.0%")])


def build_peer_profitability(data):
    return _build_peer_bars(data, "peer_profitability_charts",
                            "Peer Comparison – Profitability",
                            [("Revenue", "revenue", "#,##0"),
                             ("EBIT Margin", "ebit_margin", "0.0%")])


def build_peer_scatter(data):
    ps = data.get("sections", {}).get("peer_scatter", {}) or {}
    commentary = ps.get("commentary")
    if isinstance(commentary, str):
        commentary = [commentary]
    sc1 = ps.get("margin_vs_leverage", []) or []
    sc2 = ps.get("fcf_vs_rcf", []) or []

    chart1 = scatter_chart_html("EBIT Margin vs Debt/EBITDA", sc1,
                                 x_label="Debt/EBITDA", y_label="EBIT Margin (%)",
                                 height=260)
    chart2 = scatter_chart_html("FCF/Debt vs RCF / Debt", sc2,
                                 x_label="RCF / Debt", y_label="FCF / Debt",
                                 height=260)

    return f"""
<section class="slide">
  {section_header("Peer Comparison – Scatter Plots", "Part 3 · Company Positioning vs. Peers")}
  {bullets_html(commentary)}
  <div class="two-col-layout">
    <div class="col">{chart1}</div>
    <div class="col">{chart2}</div>
  </div>
  <div class="source">Source: Moodys.com, Company filings</div>
</section>"""


def build_scorecard(data):
    sc = data.get("sections", {}).get("scorecard", {}) or {}
    companies = sc.get("companies", []) or []
    factors = sc.get("factors", []) or []
    is_header = sc.get("is_header", []) or []
    values = sc.get("values", []) or []

    if not companies or not factors:
        return f"""<section class="slide">
  {section_header("Peer Scorecard Outcome Comparison", "Part 3 · Company Positioning vs. Peers")}
  <p class="no-data">No scorecard data available.</p>
  <div class="source">Source: Moodys.com</div>
</section>"""

    headers = ["Factors"]
    for name in companies:
        headers.append(name)
        headers.append("")
    sub_header = [""] + ["Measure", "Score"] * len(companies)
    body = [sub_header]
    header_row_indices = []

    for idx, label in enumerate(factors):
        hdr = is_header[idx] if idx < len(is_header) else False
        row = [label]
        rv = values[idx] if idx < len(values) else []
        for i in range(len(companies)):
            pair = rv[i + 1] if i + 1 < len(rv) else []
            measure = pair[0] if len(pair) > 0 else ""
            score   = pair[1] if len(pair) > 1 else ""
            row.append(str(measure))
            row.append(str(score))
        body.append(row)
        if hdr:
            header_row_indices.append(len(body) - 1)

    col_widths = [2.4] + [0.65] * (len(headers) - 1)

    # Build table manually to support header-row highlighting
    total_w = sum(col_widths)
    th_parts = []
    for i, h in enumerate(headers):
        pct = round(col_widths[i] / total_w * 100, 1)
        th_parts.append(f'<th style="width:{pct}%">{esc(h)}</th>')
    thead = f"<thead><tr>{''.join(th_parts)}</tr></thead>"

    body_rows_html = []
    for ri, row in enumerate(body):
        is_hdr_row = ri in header_row_indices
        row_style = ' class="scorecard-header-row"' if is_hdr_row else ""
        tds = []
        for j, val in enumerate(row):
            bold = j == 0
            content = f"<strong>{esc(val)}</strong>" if (bold or is_hdr_row) else esc(val)
            tds.append(f"<td>{content}</td>")
        body_rows_html.append(f"<tr{row_style}>{''.join(tds)}</tr>")
    tbody = f"<tbody>{''.join(body_rows_html)}</tbody>"

    return f"""
<section class="slide">
  {section_header("Peer Scorecard Outcome Comparison", "Part 3 · Company Positioning vs. Peers")}
  <div class="scorecard-wrap"><table class="scorecard-table">{thead}{tbody}</table></div>
  <div class="source">Source: Moodys.com</div>
</section>"""


def build_esg(data):
    company = data.get("target_company", "")
    esg = data.get("sections", {}).get("esg_analysis", {}) or {}
    rows = esg.get("table", []) or []
    commentary = esg.get("commentary", []) or []
    if isinstance(commentary, str):
        commentary = [commentary] if commentary.strip() else []

    table_html_str = ""
    if rows:
        headers = ["Company", "CIS", "Env.", "Social", "Gov."]
        body = [[r.get("company", ""), r.get("cis", ""), r.get("environmental", ""),
                 r.get("social", ""), r.get("governance", "")] for r in rows]
        table_html_str = table_html(headers, body, first_col_bold=True,
                                    col_widths=[1.5, 1.0, 0.9, 0.9, 0.9])

    return f"""
<section class="slide">
  {section_header("ESG Analysis", "Part 3 · Company Positioning vs. Peers")}
  <div class="two-col-layout">
    <div class="col">
      <div class="col-header">ESG TABLE</div>
      {table_html_str}
    </div>
    <div class="col">
      <div class="col-header">{esc(company.upper())} ESG</div>
      {bullets_html(commentary)}
    </div>
  </div>
  <div class="source">Source: Moodys.com, Company filings</div>
</section>"""


def build_sources(data):
    """Render the Citations section using the canonical moodys-skills:citations markup.

    Each source entry supports: title, source, date, url, tool.
    Sources are rendered as numbered [n] references with hyperlinked titles
    and muted publisher/date metadata — per the shared-citations-css contract.
    """
    sources = data.get("sources", []) or []
    if not sources:
        return f"""<section class="slide">
  {section_header("Citations")}
  <p class="muted">No sources listed.</p>
</section>"""

    items_html = ""
    for i, s in enumerate(sources, start=1):
        title  = s.get("title", "")
        source = s.get("source", "")
        date   = s.get("date", "")
        url    = s.get("url", "")
        meta_parts = [p for p in [source, date] if p]
        meta   = " • ".join(meta_parts)
        title_part = (
            f'<a href="{esc(url)}" target="_blank" class="source-title">{esc(title)}</a>'
            if url else f'<span class="source-title">{esc(title)}</span>'
        )
        items_html += (
            f'<div class="source-item">'
            f'<span class="source-num">[{i}]</span>'
            f'{title_part}'
            f'<span class="source-meta">({esc(meta)})</span>'
            f'</div>'
        )

    return f"""
<section class="slide">
  {section_header("Citations")}
  <div class="sources-section">
    <div class="sources-heading">Citations</div>
    <div id="rp-sources">{items_html}</div>
  </div>
</section>"""


def build_thank_you(data):
    sector = data.get("sector", "")
    date = data.get("report_date", "")
    return f"""
<section class="slide cover thank-you">
  <div class="cover-inner">
    <div class="cover-badge">MOODY'S ANALYTICS</div>
    <h1 class="cover-company">Thank You</h1>
    <div class="cover-meta">
      <span>{esc(sector)}</span>
      <span class="divider">|</span>
      <span>{esc(date)}</span>
    </div>
  </div>
</section>"""


def build_disclaimer():
    return f"""
<section class="slide disclaimer">
  <div class="section-header"><h2>Disclaimer</h2></div>
  <p class="disclaimer-text">
    © {__import__('datetime').date.today().year} Moody's Corporation, Moody's Investors Service, Inc.,
    Moody's Analytics, Inc. and/or their licensors and affiliates (collectively, "MOODY'S").
    All rights reserved. This report has been prepared solely for informational purposes and
    does not constitute investment advice. The information herein is based on sources believed
    to be reliable but MOODY'S does not guarantee its accuracy or completeness. MOODY'S
    ratings, assessments, other opinions and publications are not intended for use by retail
    investors and it would be reckless and inappropriate for retail investors to use
    MOODY'S ratings or publications when making an investment decision.
  </p>
</section>"""


# ---------------------------------------------------------------------------
# CSS + HTML scaffold
# ---------------------------------------------------------------------------

CSS = f"""
:root {{
  --navy:      {NAVY};
  --bright:    {BRIGHT_BLUE};
  --mid:       {MID_BLUE};
  --purple:    {PURPLE};
  --pale:      {PALE};
  --very-pale: {VERY_PALE};
  --pink:      {PINK};
  --teal:      {TEAL};
  --gold:      {GOLD};
  --gray:      {LIGHT_GRAY};
  --text:      {TEXT_DARK};
  --muted:     {TEXT_MUTED};
  --white:     {WHITE};
  --header-bg: {HEADER_FILL};
  --grid:      {GRID_LINE};
}}

*, *::before, *::after {{ box-sizing: border-box; }}

body {{
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 14px;
  color: var(--text);
  background: #f0f2f5;
  line-height: 1.45;
}}

/* ---- Slides ---- */
.slide {{
  background: var(--white);
  max-width: 1100px;
  margin: 28px auto;
  border-radius: 6px;
  box-shadow: 0 2px 12px rgba(0,0,0,.10);
  padding: 32px 40px 24px;
  position: relative;
}}

/* ---- Cover ---- */
.slide.cover {{
  background: linear-gradient(135deg, #1a2080 0%, #2d3494 100%);
  color: var(--white);
  min-height: 260px;
  display: flex;
  align-items: center;
}}
.cover-inner {{ text-align: center; width: 100%; }}
.cover-badge {{
  display: inline-block;
  background: var(--bright);
  color: var(--white);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 2px;
  padding: 4px 14px;
  border-radius: 3px;
  margin-bottom: 20px;
}}
h1.cover-company {{
  font-size: 36px;
  font-weight: 700;
  margin: 0 0 10px;
  color: var(--white);
}}
.cover-sub {{ font-size: 18px; opacity: .85; margin-bottom: 16px; }}
.cover-meta {{ font-size: 13px; opacity: .75; }}
.cover-meta .divider {{ margin: 0 12px; }}

/* ---- Divider slide ---- */
.slide.divider-slide {{
  background: var(--bright);
  color: var(--white);
  min-height: 120px;
  display: flex;
  align-items: center;
}}
.divider-inner {{ text-align: center; width: 100%; }}
.divider-label {{
  font-size: 11px; letter-spacing: 3px; opacity: .75; margin-bottom: 8px;
}}
h2.divider-title {{
  font-size: 28px; font-weight: 700; color: var(--white); margin: 0;
}}

/* ---- Section header ---- */
.section-header {{
  border-left: 5px solid var(--bright);
  padding-left: 14px;
  margin-bottom: 20px;
}}
.section-part {{
  display: block;
  font-size: 11px;
  color: var(--bright);
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  margin-bottom: 4px;
}}
.section-header h2 {{
  margin: 0;
  font-size: 20px;
  font-weight: 700;
  color: var(--navy);
}}

/* ---- Agenda ---- */
.agenda-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 8px;
}}
.agenda-card {{
  border: 1px solid var(--very-pale);
  border-radius: 5px;
  padding: 20px;
}}
.agenda-num {{
  font-size: 48px;
  font-weight: 700;
  color: var(--bright);
  font-family: 'Times New Roman', serif;
  line-height: 1;
  margin-bottom: 8px;
}}
.agenda-title {{
  font-size: 16px;
  font-weight: 700;
  margin-bottom: 6px;
  color: var(--navy);
}}
.agenda-desc {{ font-size: 12px; color: var(--muted); }}

/* ---- Three-col grid ---- */
.three-col-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin-bottom: 12px;
}}
.three-col-card {{
  background: #f8f9fb;
  border-radius: 5px;
  padding: 16px;
  border-top: 3px solid var(--bright);
}}
.col-header {{
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--navy);
  margin-bottom: 10px;
}}

/* ---- Two-col layout ---- */
.two-col-layout {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  margin-bottom: 12px;
}}
.col {{ min-width: 0; }}

/* ---- Lists ---- */
ul {{ margin: 6px 0 10px 0; padding-left: 18px; }}
li {{ margin-bottom: 5px; line-height: 1.45; }}

/* ---- Tables ---- */
table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 12px;
  margin-bottom: 10px;
}}
th {{
  background: var(--header-bg);
  font-weight: 700;
  padding: 8px 10px;
  text-align: left;
  border: 1px solid var(--grid);
}}
td {{
  padding: 7px 10px;
  border: 1px solid var(--grid);
  vertical-align: top;
}}
tr:nth-child(even) td {{ background: #fafbfc; }}
.scorecard-wrap {{ overflow-x: auto; }}
.scorecard-table {{ font-size: 11px; }}
.scorecard-table th, .scorecard-table td {{ padding: 5px 7px; }}
tr.scorecard-header-row td {{
  background: var(--header-bg) !important;
  font-weight: 700;
}}

/* ---- SWOT ---- */
.swot-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-bottom: 12px;
}}
.swot-cell {{
  border-radius: 5px;
  padding: 16px;
}}
.swot-label {{
  font-size: 13px;
  font-weight: 700;
  margin-bottom: 8px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}}
.swot-s {{ background: #e8f4f8; border-top: 3px solid {TEAL}; }}
.swot-w {{ background: #fff3e0; border-top: 3px solid {GOLD}; }}
.swot-o {{ background: #e8f5e9; border-top: 3px solid #66bb6a; }}
.swot-t {{ background: #fce4ec; border-top: 3px solid {PINK}; }}

/* ---- Charts ---- */
.chart-wrap {{ margin-bottom: 10px; }}
.chart-title {{
  font-size: 12px;
  font-weight: 700;
  text-align: center;
  color: var(--text);
  margin-bottom: 6px;
}}

/* ---- SVG chart animations (CSS-only, JS-free) ---- */
@keyframes svgGrowV {{ from {{ transform: scaleY(0); }} to {{ transform: scaleY(1); }} }}
@keyframes svgGrowH {{ from {{ transform: scaleX(0); }} to {{ transform: scaleX(1); }} }}
@keyframes svgFade  {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
@keyframes svgPop   {{ from {{ opacity: 0; transform: scale(0.5); }} to {{ opacity: 1; transform: scale(1); }} }}
@keyframes svgDraw  {{ to {{ stroke-dashoffset: 0; }} }}

.svg-bar-v {{ transform-box: fill-box; transform-origin: bottom; animation: svgGrowV .6s ease-out both; }}
.svg-bar-h {{ transform-box: fill-box; transform-origin: left;   animation: svgGrowH .6s ease-out both; }}
.svg-slice {{ transform-box: fill-box; transform-origin: center; animation: svgFade .5s ease-out both; }}
.svg-mark  {{ transform-box: fill-box; transform-origin: center; animation: svgPop  .5s ease-out both; }}
.svg-line  {{ stroke-dasharray: 1; stroke-dashoffset: 1; animation: svgDraw 1s ease-out forwards; }}
.svg-pt    {{ animation: svgFade .4s ease-out both; }}
.svg-lbl   {{ animation: svgFade .5s ease-out both; }}

@media (prefers-reduced-motion: reduce) {{
  .svg-bar-v, .svg-bar-h, .svg-slice, .svg-mark, .svg-pt, .svg-lbl {{ animation: none; }}
  .svg-line {{ animation: none; stroke-dashoffset: 0; }}
}}

/* ---- Category groups ---- */
.category-group {{ margin-bottom: 16px; }}
.category-name {{
  font-size: 13px;
  font-weight: 700;
  color: var(--navy);
  margin-bottom: 6px;
  padding-bottom: 4px;
  border-bottom: 2px solid var(--very-pale);
}}

/* ---- Outlook / positioning ---- */
.outlook-summary {{ font-size: 14px; line-height: 1.6; margin-bottom: 12px; }}
.company-positioning {{ font-size: 13px; color: var(--muted); }}

/* ---- Subsection ---- */
.subsection-title {{
  font-size: 12px;
  font-weight: 700;
  color: var(--navy);
  margin: 12px 0 4px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}}

/* ---- Misc ---- */
.source {{
  font-size: 10px;
  color: var(--muted);
  margin-top: 10px;
  border-top: 1px solid var(--grid);
  padding-top: 6px;
}}
.no-data {{
  text-align: center;
  color: var(--muted);
  font-size: 12px;
  padding: 30px;
  background: #f8f9fb;
  border-radius: 4px;
}}
.muted {{ color: var(--muted); }}
.disclaimer-text {{
  font-size: 11px;
  color: var(--muted);
  line-height: 1.6;
}}
a {{ color: var(--bright); }}

/* ---- Thank-you slide ---- */
.thank-you h1 {{ font-size: 42px; }}


/* BEGIN shared-citations-css (moodys-skills:citations contract) */
.cite-ref {{ font-size: 11px; color: var(--bright); font-weight: 600; text-decoration: none; }}
a.cite-ref {{ cursor: pointer; }}
a.cite-ref:hover {{ text-decoration: underline; }}
span.cite-ref {{ cursor: default; }}
.sources-section {{ padding-top: 24px; margin-top: 4px; }}
.sources-heading {{
  font-size: 14px; font-weight: 700; color: var(--navy);
  padding-bottom: 7px; border-bottom: 2px solid var(--navy); margin-bottom: 12px;
}}
.source-item {{
  padding: 5px 0; border-bottom: 1px solid var(--grid);
  font-size: 11px; color: var(--text); line-height: 1.6;
}}
.source-num {{ font-weight: 700; color: var(--navy); margin-right: 6px; }}
.source-title {{ color: var(--bright); text-decoration: none; }}
a.source-title:hover {{ text-decoration: underline; }}
.source-meta {{ color: var(--muted); margin-left: 4px; }}
/* END shared-citations-css */
/* ---- Print ---- */
@media print {{
  body {{ background: white; }}
  .slide {{ box-shadow: none; margin: 0; border-radius: 0; page-break-after: always; }}
}}
"""


def wrap_html(body_content, data):
    company = data.get("target_company", "")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Rating Analysis – {esc(company)}</title>
  <!-- Charts are pure inline SVG (no JS, no external libraries) — see build_html.py -->
  <style>
{CSS}
  </style>
</head>
<body>
{body_content}
</body>
</html>"""


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

def build(payload: dict, out_path: Path) -> None:
    sections = []

    sections.append(build_cover(payload))                              # 1
    sections.append(build_agenda(payload))                            # 2

    sections.append(build_divider("Sector Analysis"))                 # 3
    sections.append(build_sector_overview(payload))                   # 4
    sections.append(build_moodys_view(payload))                       # 5
    sections.append(build_macro_outlook(payload))                     # 6
    sections.append(build_rating_actions(payload))                    # 7

    sections.append(build_divider("Company Credit Overview"))         # 8
    sections.append(build_financial_analysis(payload))                # 9
    sections.append(build_revenue_distribution(payload))              # 10
    sections.append(build_swot(payload))                              # 11
    sections.append(_build_key_metrics_four(payload))                 # 12
    sections.append(build_strategic_updates(payload))                 # 13
    sections.append(build_categorized(payload, "news_mna",
                    "News / M&A / Leadership", "Web search"))         # 14
    sections.append(build_categorized(payload, "external_trends",
                    "External Trends / Pressures / Reputational Risks",
                    "Web search"))                                     # 15

    sections.append(build_divider("Company Positioning vs. Peers"))   # 16
    sections.append(build_peer_summary(payload))                      # 17
    sections.append(build_peer_financials(payload))                   # 18
    sections.append(build_peer_debt(payload))                         # 19
    sections.append(build_peer_profitability(payload))                # 20
    sections.append(build_peer_scatter(payload))                      # 21
    sections.append(build_scorecard(payload))                         # 22
    sections.append(build_esg(payload))                               # 23

    sections.append(build_sources(payload))                           # 24
    sections.append(build_thank_you(payload))                         # 25
    sections.append(build_disclaimer())                               # 26

    body = "\n".join(sections)
    html = wrap_html(body, payload)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: build_html.py <payload.json> <output.html>",
              file=sys.stderr)
        return 2
    with Path(sys.argv[1]).open("r", encoding="utf-8") as f:
        payload = json.load(f)
    build(payload, Path(sys.argv[2]))
    print(f"Wrote {sys.argv[2]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
