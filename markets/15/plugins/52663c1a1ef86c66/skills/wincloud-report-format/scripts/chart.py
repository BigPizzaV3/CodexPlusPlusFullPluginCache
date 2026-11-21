#!/usr/bin/env python3
"""Draw a WinCloud chart as SVG using only the standard library (PNG too when cairosvg is installed).

Usage: python3 chart.py spec.json out.svg
spec: {"type": "bar|hbar|line|donut", "title": "...", "subtitle": "...", "unit": "bookings",
       "categories": ["Jan", "Feb"], "series": [{"name": "Grand Hotel", "values": [10, 12]}]}
"""
import json, math, sys
from xml.sax.saxutils import escape

PALETTE = ["#003352", "#63e7a4", "#6f93ab", "#b7c3cb", "#2d7f63", "#9aa5ad"]  # RBS navy, green, then tints
FONT = "Century Gothic, Arial, sans-serif"
W, H = 760, 420


def fmt(v):
    return f"{v:,.0f}" if abs(v - round(v)) < 1e-9 else f"{v:,.1f}"


def nice_max(v):
    if v <= 0:
        return 1
    p = 10 ** math.floor(math.log10(v))
    return next(m * p for m in (1, 2, 2.5, 5, 10) if m * p >= v)


def text(x, y, s, size=12, anchor="start", weight="normal", fill="#1f2a33"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" '
            f'font-weight="{weight}" fill="{fill}">{escape(str(s))}</text>')


def frame(spec, body, legend):
    head = text(24, 30, spec["title"], 17, weight="bold", fill="#003352")
    if spec.get("subtitle"):
        head += text(24, 50, spec["subtitle"], 12, fill="#5b6670")
    x = 24
    for i, name in enumerate(legend):
        head += f'<rect x="{x}" y="{H - 24}" width="12" height="12" rx="2" fill="{PALETTE[i % len(PALETTE)]}"/>'
        head += text(x + 18, H - 14, name, 12)
        x += 30 + 7 * len(name)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
            f'font-family="{FONT}" role="img" aria-label="{escape(spec["title"], {chr(34): "&quot;"})}">'
            f'<rect width="{W}" height="{H}" fill="#ffffff"/>{head}{body}</svg>')


def axes(spec, vmax, left, top, right, bottom):
    out, unit = "", spec.get("unit", "")
    for i in range(5):
        v = vmax * i / 4
        y = bottom - (bottom - top) * i / 4
        out += f'<line x1="{left}" y1="{y:.1f}" x2="{right}" y2="{y:.1f}" stroke="#e3e8ec"/>'
        out += text(left - 8, y + 4, fmt(v), 11, "end", fill="#5b6670")
    if unit:
        out += text(left, top - 10, unit, 11, fill="#5b6670")
    return out


def bar(spec):
    cats, series = spec["categories"], spec["series"]
    left, top, right, bottom = 60, 80, W - 24, H - 70
    vmax = nice_max(max(max(s["values"]) for s in series))
    body = axes(spec, vmax, left, top, right, bottom)
    slot = (right - left) / len(cats)
    bw = min(48 if len(series) > 1 else 90, slot * 0.8 / len(series))
    skip = max(1, len(cats) // 12)
    labels = bw - 2 >= 7 * max(len(fmt(v)) for s in series for v in s["values"])  # only when every value fits its bar
    for ci, c in enumerate(cats):
        x0 = left + slot * ci + (slot - bw * len(series)) / 2
        for si, s in enumerate(series):
            v = s["values"][ci]
            h = (bottom - top) * v / vmax
            x = x0 + bw * si
            body += f'<rect x="{x:.1f}" y="{bottom - h:.1f}" width="{bw - 2:.1f}" height="{h:.1f}" fill="{PALETTE[si % len(PALETTE)]}"/>'
            if labels:
                body += text(x + (bw - 2) / 2, bottom - h - 5, fmt(v), 11, "middle")
        if ci % skip == 0:
            body += text(left + slot * ci + slot / 2, bottom + 18, c, 12, "middle")
    return frame(spec, body, [s["name"] for s in series] if len(series) > 1 else [])


def hbar(spec):
    cats = [c if len(c) <= 30 else c[:29] + "…" for c in map(str, spec["categories"])]
    series = spec["series"]
    left, top, right, bottom = 24 + 7 * max(len(c) for c in cats), 70, W - 60, H - 50
    vmax = nice_max(max(max(s["values"]) for s in series))
    slot = (bottom - top) / len(cats)
    bh = min(26, slot * 0.8 / len(series))
    body = text(left, top - 8, spec.get("unit", ""), 11, fill="#5b6670")
    for ci, c in enumerate(cats):
        y0 = top + slot * ci + (slot - bh * len(series)) / 2
        body += text(left - 8, top + slot * ci + slot / 2 + 4, c, 12, "end")
        for si, s in enumerate(series):
            v = s["values"][ci]
            w = (right - left) * v / vmax
            body += f'<rect x="{left}" y="{y0 + bh * si:.1f}" width="{w:.1f}" height="{bh - 2:.1f}" fill="{PALETTE[si % len(PALETTE)]}"/>'
            body += text(left + w + 6, y0 + bh * si + bh / 2 + 3, fmt(v), 11)
    return frame(spec, body, [s["name"] for s in series] if len(series) > 1 else [])


def line(spec):
    cats, series = spec["categories"], spec["series"]
    left, top, right, bottom = 60, 80, W - 30, H - 70
    vmax = nice_max(max(max(s["values"]) for s in series))
    body = axes(spec, vmax, left, top, right, bottom)
    step = (right - left) / max(len(cats) - 1, 1)
    skip = max(1, len(cats) // 12)
    for ci, c in enumerate(cats):
        if ci % skip == 0:
            body += text(left + step * ci, bottom + 18, c, 11, "middle")
    for si, s in enumerate(series):
        col = PALETTE[si % len(PALETTE)]
        pts = [(left + step * i, bottom - (bottom - top) * v / vmax) for i, v in enumerate(s["values"])]
        dash = ' stroke-dasharray="6 4"' if s.get("dashed") else ""
        body += f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{col}" stroke-width="2.5"{dash}/>'
        for i, ((x, y), v) in enumerate(zip(pts, s["values"])):
            body += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" fill="{col}"/>'
            if len(cats) <= 12:  # the higher series labels above, the lower below, so labels never cross the other line
                above = all(v >= o["values"][i] for o in series)
                body += text(x, y - 8 if above else y + 17, fmt(v), 10, "middle")
    return frame(spec, body, [s["name"] for s in series] if len(series) > 1 else [])


def donut(spec):
    vals, cats = spec["series"][0]["values"], spec["categories"]
    total, cx, cy, r = sum(vals), 230, 235, 110
    if total <= 0:
        sys.exit("donut needs at least one value above zero; say there is nothing to chart instead")
    body, a = "", -math.pi / 2
    for i, v in enumerate(vals):
        b = a + 2 * math.pi * v / total
        large = 1 if b - a > math.pi else 0
        p = lambda t, rad: (cx + rad * math.cos(t), cy + rad * math.sin(t))
        (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p(a, r), p(b, r), p(b, r * .58), p(a, r * .58)
        if v == total:  # an arc whose ends meet draws nothing, so the only non-zero part is a full ring
            body += (f'<circle cx="{cx}" cy="{cy}" r="{r * .79:.1f}" fill="none" '
                     f'stroke="{PALETTE[i % len(PALETTE)]}" stroke-width="{r * .42:.1f}"/>')
        else:
            body += (f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 {large} 1 {x2:.1f},{y2:.1f} L{x3:.1f},{y3:.1f} '
                     f'A{r * .58:.1f},{r * .58:.1f} 0 {large} 0 {x4:.1f},{y4:.1f}Z" fill="{PALETTE[i % len(PALETTE)]}" stroke="#fff"/>')
        ly = 130 + 34 * i
        body += f'<rect x="440" y="{ly - 11}" width="14" height="14" rx="2" fill="{PALETTE[i % len(PALETTE)]}"/>'
        body += text(462, ly, f"{cats[i]}: {fmt(v)} ({v / total:.0%})", 13)
        a = b
    body += text(cx, cy + 6, fmt(total), 20, "middle", "bold", "#003352")
    return frame(spec, body, [])


def check(spec):
    n = len(spec["categories"])
    for s in spec["series"]:
        name, vals = s.get("name", "series"), s["values"]
        if len(vals) != n:
            sys.exit(f"{name} has {len(vals)} values but there are {n} categories; give one value per category")
        if any(type(v) not in (int, float) or v < 0 for v in vals):
            sys.exit(f"{name} has a value that is not a number of zero or more; charts cannot draw it")


def main():
    spec = json.load(open(sys.argv[1]))
    check(spec)
    svg = {"bar": bar, "hbar": hbar, "line": line, "donut": donut}[spec["type"]](spec)
    out = sys.argv[2]
    open(out, "w").write(svg)
    print("wrote", out)
    try:  # a PNG is easier for some hosts to display; only possible with cairosvg
        import cairosvg
        cairosvg.svg2png(bytestring=svg.encode(), write_to=out.rsplit(".", 1)[0] + ".png", scale=2)
        print("wrote png")
    except Exception:
        pass


if __name__ == "__main__":
    main()
