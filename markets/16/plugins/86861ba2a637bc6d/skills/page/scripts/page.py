#!/usr/bin/env python3
"""Render a page spec (JSON) as one self-contained HTML file.

The page has a title, an eyebrow, a summary, figure tiles, charts (bridge, line,
bars), tables and text blocks, and, when the spec gives several views, a
segmented control that switches between them. Everything is inline: CSS, SVG
charts and a few lines of plain JavaScript. The page makes no network request,
loads no font and works offline, at phone width, in light and dark.

The renderer computes no figure. Every number on the page is in the spec, and the
spec's figures come from the skills' scripts. It checks that each bridge ties.

  python3 scripts/page.py page_september_close.json
  python3 scripts/page.py board_pack_sep_page.json --out september.html --open

The spec format is in references/spec.md.
"""
from __future__ import annotations

import argparse
import html
import json
import math
import os
import subprocess
import sys
from decimal import Decimal
from typing import Any, Dict, List, Optional, Sequence, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import magnos_fin as mf  # noqa: E402

JSON_PATH = os.path.join(".magnos", "runs", "page.json")
BLOCK_TYPES = ("bridge", "line", "bar", "table", "text")
ROLES = ("total", "subtotal", "ratio", "highlight")


class SpecError(Exception):
    """A problem with the spec: exit 2 with one plain sentence."""


def esc(x: Any) -> str:
    return html.escape("" if x is None else str(x), quote=True)


# ---------------------------------------------------------------- numbers (formatting only)

def as_dec(x: Any, where: str) -> Decimal:
    if isinstance(x, bool) or x is None:
        raise SpecError(f"{where} needs a number, not {json.dumps(x)}.")
    d = mf.to_decimal(x)
    if d is None:
        raise SpecError(f"{where} needs a number, not {json.dumps(x)}.")
    return d


def places(d: Decimal) -> int:
    e = d.normalize().as_tuple().exponent
    return min(4, max(0, -e)) if isinstance(e, int) else 0


def show(d: Decimal, signed: bool = False, decimals: Optional[int] = None) -> str:
    s = mf.num(d, places(d) if decimals is None else decimals)
    if signed and d > 0 and any(c in "123456789" for c in s):
        return "+" + s
    return s


def nice_step(span: float, target: int = 4) -> float:
    if span <= 0 or not math.isfinite(span):
        return 1.0
    raw = span / target
    mag = 10 ** math.floor(math.log10(raw))
    for m in (1, 2, 2.5, 5, 10):
        if raw <= m * mag + 1e-12:
            return m * mag
    return 10 * mag


def scale(vmin: float, vmax: float, zero: bool, below: float = 0.15) -> Tuple[float, float, float]:
    """A nice axis (lo, hi, step); starts at zero unless the values sit in a narrow band far from it.

    below: room under the lowest value, as a share of the band (a bridge keeps its totals tall).
    """
    if zero or vmin <= 0 or (vmax - vmin) >= 0.5 * vmax:
        vmin, vmax = min(vmin, 0.0), max(vmax, 0.0)
        pad_lo = pad_hi = 0.0
    else:
        pad_lo, pad_hi = below * (vmax - vmin), 0.1 * (vmax - vmin)
        pad_lo = min(pad_lo, vmin)
    if vmax == vmin:
        vmax = vmin + (abs(vmin) or 1.0)
    step = nice_step(vmax - vmin + pad_lo + pad_hi)
    lo = math.floor((vmin - pad_lo) / step) * step
    hi = math.ceil((vmax + pad_hi) / step) * step
    if hi <= lo:
        hi = lo + step
    return lo, hi, step


def ticks(lo: float, hi: float, step: float) -> List[Decimal]:
    n = int(round((hi - lo) / step))
    dstep = Decimal(repr(step))
    dlo = Decimal(repr(lo)).quantize(dstep) if places(dstep) else Decimal(round(lo))
    return [dlo + dstep * i for i in range(n + 1)]


def tick_label(t: Decimal, step: float) -> str:
    return show(t, decimals=places(Decimal(repr(step))))


# ---------------------------------------------------------------- spec checks

def text_of(x: Any, where: str, required: bool = False) -> str:
    if x is None or x == "":
        if required:
            raise SpecError(f"{where} is missing. Add it to the spec.")
        return ""
    if isinstance(x, (dict, list)):
        raise SpecError(f"{where} must be text.")
    return str(x)


def check_tiles(tiles: Any, where: str) -> List[Dict[str, Any]]:
    if tiles is None:
        return []
    if not isinstance(tiles, list):
        raise SpecError(f"{where} must be a list of tiles.")
    out = []
    for i, t in enumerate(tiles, 1):
        if not isinstance(t, dict):
            raise SpecError(f"{where} tile {i} must be an object with label and value.")
        d = str(t.get("direction") or "").lower() or None
        if d not in (None, "up", "down", "flat"):
            raise SpecError(f"{where} tile {i}: direction must be up, down or flat.")
        tone = str(t.get("tone") or "").lower() or None
        if tone not in (None, "good", "bad", "neutral"):
            raise SpecError(f"{where} tile {i}: tone must be good, bad or neutral.")
        if tone is None:
            tone = {"up": "good", "down": "bad"}.get(d or "", "neutral")
        out.append({"label": text_of(t.get("label"), f"{where} tile {i} label", True),
                    "value": text_of(t.get("value"), f"{where} tile {i} value", True),
                    "change": text_of(t.get("change"), f"{where} tile {i} change"),
                    "direction": d or "flat", "tone": tone, "note": text_of(t.get("note"), f"{where} tile {i} note")})
    return out


def check_block(b: Any, where: str) -> Dict[str, Any]:
    if not isinstance(b, dict):
        raise SpecError(f"{where} must be an object with a type.")
    kind = str(b.get("type") or "").lower()
    if kind == "waterfall":
        kind = "bridge"
    if kind not in BLOCK_TYPES:
        raise SpecError(f"{where} has type '{b.get('type')}'; use one of {', '.join(BLOCK_TYPES)}.")
    title = text_of(b.get("title"), f"{where} title")
    name = f"{where} ({title or kind})"
    out = {"type": kind, "title": title, "subtitle": text_of(b.get("subtitle"), f"{name} subtitle"),
           "note": text_of(b.get("note"), f"{name} note"), "wide": bool(b.get("wide"))}
    if kind == "bridge":
        bars = b.get("bars")
        if not isinstance(bars, list) or len(bars) < 2:
            raise SpecError(f"{name} needs a list of bars: a start total, the steps and an end total.")
        clean = []
        for i, x in enumerate(bars, 1):
            if not isinstance(x, dict):
                raise SpecError(f"{name} bar {i} must be an object with label and value.")
            clean.append({"label": text_of(x.get("label"), f"{name} bar {i} label", True),
                          "short": text_of(x.get("short"), f"{name} bar {i} short"),
                          "value": as_dec(x.get("value"), f"{name} bar {i} ({x.get('label')})"),
                          "total": bool(x.get("total")), "display": text_of(x.get("display"), f"{name} bar {i} display"),
                          "detail": text_of(x.get("detail"), f"{name} bar {i} detail")})
        if not clean[0]["total"]:
            raise SpecError(f"{name}: the first bar must be a total (\"total\": true).")
        if not clean[-1]["total"]:
            raise SpecError(f"{name}: the last bar must be a total (\"total\": true).")
        run = clean[0]["value"]
        for x in clean[1:]:
            if x["total"]:
                if abs(run - x["value"]) > Decimal("1e-9"):
                    raise SpecError(f"The bridge '{title or 'bridge'}' does not tie: the bars before "
                                    f"'{x['label']}' make {show(run)}, but it says {show(x['value'])}. "
                                    f"Copy the figures from the script output again.")
                run = x["value"]
            else:
                run += x["value"]
        out["bars"] = clean
    elif kind in ("line", "bar"):
        xs = b.get("x")
        series = b.get("series")
        if not isinstance(xs, list) or not xs:
            raise SpecError(f"{name} needs x: the list of categories.")
        if not isinstance(series, list) or not series:
            raise SpecError(f"{name} needs series: a list of {{name, values}}.")
        clean_s = []
        for i, s in enumerate(series, 1):
            if not isinstance(s, dict) or not isinstance(s.get("values"), list):
                raise SpecError(f"{name} series {i} needs name and values.")
            if len(s["values"]) != len(xs):
                raise SpecError(f"{name} series {i} has {len(s['values'])} values for {len(xs)} categories.")
            vals = [None if v is None else as_dec(v, f"{name} series {i} value {j}") for j, v in enumerate(s["values"], 1)]
            clean_s.append({"name": text_of(s.get("name"), f"{name} series {i} name") or f"Series {i}",
                            "values": vals, "dashed": bool(s.get("dashed"))})
        out["x"] = [str(x) for x in xs]
        out["series"] = clean_s[:4]
        out["zero"] = bool(b.get("zero", kind == "bar"))
    elif kind == "table":
        cols = b.get("columns")
        rows = b.get("rows")
        if not isinstance(cols, list) or not cols:
            raise SpecError(f"{name} needs columns.")
        if not isinstance(rows, list):
            raise SpecError(f"{name} needs rows.")
        ccols = []
        for i, c in enumerate(cols):
            if isinstance(c, dict):
                ccols.append({"label": text_of(c.get("label"), f"{name} column {i + 1}"),
                              "tone": str(c.get("tone") or ""), "align": str(c.get("align") or ("l" if i == 0 else "r"))})
            else:
                ccols.append({"label": str(c), "tone": "", "align": "l" if i == 0 else "r"})
        crows = []
        for i, r in enumerate(rows, 1):
            cells, role = (r.get("cells"), r.get("role")) if isinstance(r, dict) else (r, None)
            if not isinstance(cells, list):
                raise SpecError(f"{name} row {i} needs a list of cells.")
            if len(cells) != len(ccols):
                raise SpecError(f"{name} row {i} has {len(cells)} cells for {len(ccols)} columns.")
            if role is not None and role not in ROLES:
                raise SpecError(f"{name} row {i}: role must be one of {', '.join(ROLES)}.")
            cc = []
            for c in cells:
                if isinstance(c, dict):
                    cc.append({"text": text_of(c.get("text"), f"{name} row {i} cell"), "tone": str(c.get("tone") or "")})
                else:
                    cc.append({"text": "" if c is None else str(c), "tone": ""})
            crows.append({"cells": cc, "role": role})
        out["columns"], out["rows"] = ccols, crows
    else:  # text
        body = b.get("body")
        items = b.get("items")
        paras = body if isinstance(body, list) else ([body] if body else [])
        out["body"] = [text_of(p, f"{name} body") for p in paras]
        out["items"] = [text_of(p, f"{name} item") for p in (items or [])] if isinstance(items, list) or items is None else []
        out["wide"] = True if b.get("wide") is None else bool(b.get("wide"))
        if not out["body"] and not out["items"]:
            raise SpecError(f"{name} needs body or items.")
    return out


def check(spec: Any) -> Dict[str, Any]:
    if not isinstance(spec, dict):
        raise SpecError("The spec must be a JSON object with at least a title.")
    page = {"title": text_of(spec.get("title"), "The page title", True),
            "eyebrow": text_of(spec.get("eyebrow"), "eyebrow"),
            "footer": text_of(spec.get("footer"), "footer")}
    if not page["footer"] and isinstance(spec.get("source"), dict) and spec["source"].get("files"):
        page["footer"] = "Source: " + ", ".join(str(f) for f in spec["source"]["files"])

    def summary(x: Any, where: str) -> List[str]:
        if x is None:
            return []
        return [text_of(p, where) for p in (x if isinstance(x, list) else [x]) if p]

    def blocks(x: Any, where: str) -> List[Dict[str, Any]]:
        if x is None:
            return []
        if not isinstance(x, list):
            raise SpecError(f"{where} must be a list.")
        return [check_block(b, f"{where} block {i}") for i, b in enumerate(x, 1)]

    base = {"summary": summary(spec.get("summary"), "summary"), "tiles": check_tiles(spec.get("tiles"), "tiles"),
            "blocks": blocks(spec.get("blocks"), "blocks")}
    views = spec.get("views")
    if views is None:
        page["views"] = [dict(base, label="")]
    else:
        if not isinstance(views, list) or not views:
            raise SpecError("views must be a non-empty list of {label, summary, tiles, blocks}.")
        page["views"] = []
        for i, vw in enumerate(views, 1):
            if not isinstance(vw, dict):
                raise SpecError(f"View {i} must be an object with a label.")
            lab = text_of(vw.get("label"), f"View {i} label", True)
            page["views"].append({
                "label": lab,
                "summary": summary(vw["summary"], f"view '{lab}' summary") if "summary" in vw else base["summary"],
                "tiles": check_tiles(vw["tiles"], f"view '{lab}'") if "tiles" in vw else base["tiles"],
                "blocks": blocks(vw["blocks"], f"view '{lab}'") if "blocks" in vw else base["blocks"],
            })
    return page


# ---------------------------------------------------------------- charts

def svg_open(w: int, h: int, cls: str, label: str) -> str:
    return (f'<svg class="chart {cls}" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
            f'aria-label="{esc(label)}" preserveAspectRatio="xMidYMid meet">')


def fit_label(text: str, short: str, px: float, font: float = 12) -> str:
    per = font * 0.55
    if len(text) * per <= px:
        return text
    if short and len(short) * per <= px:
        return short
    keep = max(3, int(px / per) - 1)
    base = short or text
    return base if len(base) <= keep else base[:keep].rstrip() + "…"


def bridge_levels(bars: List[Dict[str, Any]]) -> List[Tuple[Decimal, Decimal]]:
    out, run = [], Decimal(0)
    for b in bars:
        if b["total"]:
            run = b["value"]
            out.append((Decimal(0), run))
        else:
            out.append((run, run + b["value"]))
            run += b["value"]
    return out


def bar_class(b: Dict[str, Any]) -> str:
    if b["total"]:
        return "b-total"
    return "b-up" if b["value"] > 0 else ("b-down" if b["value"] < 0 else "b-flat")


def bar_text(b: Dict[str, Any]) -> str:
    return b["display"] or show(b["value"], signed=not b["total"])


def bridge_svg(blk: Dict[str, Any], wide: bool) -> str:
    bars = blk["bars"]
    lv = bridge_levels(bars)
    ends = [float(c) for _, c in lv] + [float(a) for (a, _), b in zip(lv, bars) if not b["total"]]
    lo, hi, step = scale(min(ends), max(ends), zero=False, below=0.8)
    base = max(lo, 0.0) if lo >= 0 else 0.0
    label = (blk["title"] or "Bridge") + ": " + ", ".join(f"{b['label']} {bar_text(b)}" for b in bars)
    out = []
    if wide:
        W, H, L, R, T, B = 640, 280, 46, 8, 22, 30
        pw, ph = W - L - R, H - T - B
        slot = pw / len(bars)
        bw = min(48.0, slot * 0.62)

        def y(v: float) -> float:
            return T + ph - (v - lo) / (hi - lo) * ph
        out.append(svg_open(W, H, "chart-wide", label))
        for t in ticks(lo, hi, step):
            yy = y(float(t))
            out.append(f'<line class="grid" x1="{L}" y1="{yy:.1f}" x2="{W - R}" y2="{yy:.1f}"/>'
                       f'<text class="ax" x="{L - 8}" y="{yy + 4:.1f}" text-anchor="end">{esc(tick_label(t, step))}</text>')
        prev = None
        for i, (b, (a, c)) in enumerate(zip(bars, lv)):
            cx = L + slot * i + slot / 2
            x = cx - bw / 2
            y0 = y(base if b["total"] else float(a))
            y1 = y(float(c))
            top, h = min(y0, y1), max(abs(y1 - y0), 1.5)
            tip = f"{b['label']}: {bar_text(b)}" + (f" · {b['detail']}" if b["detail"] else "")
            out.append(f'<g><title>{esc(tip)}</title><rect class="{bar_class(b)}" x="{x:.1f}" y="{top:.1f}" '
                       f'width="{bw:.1f}" height="{h:.1f}" rx="2"/></g>')
            out.append(f'<text class="val" x="{cx:.1f}" y="{top - 6:.1f}" text-anchor="middle">{esc(bar_text(b))}</text>')
            out.append(f'<text class="ax" x="{cx:.1f}" y="{H - 10}" text-anchor="middle">'
                       f'{esc(fit_label(b["label"], b["short"], slot - 2))}</text>')
            if prev is not None:
                out.append(f'<line class="link" x1="{prev[0]:.1f}" y1="{prev[1]:.1f}" x2="{x:.1f}" y2="{prev[1]:.1f}"/>')
            prev = (x + bw, y(float(c)))
        out.append(f'<line class="base" x1="{L}" y1="{y(lo):.1f}" x2="{W - R}" y2="{y(lo):.1f}"/>')
    else:
        W, LBL, VAL, ROW = 360, 104, 52, 30
        H = 8 + ROW * len(bars) + 8
        x0, x1 = LBL + 6, W - VAL

        def x(v: float) -> float:
            return x0 + (v - lo) / (hi - lo) * (x1 - x0)
        out.append(svg_open(W, H, "chart-narrow", label))
        prev = None
        for i, (b, (a, c)) in enumerate(zip(bars, lv)):
            yy = 8 + ROW * i
            xa = x(base if b["total"] else float(a))
            xc = x(float(c))
            left, w = min(xa, xc), max(abs(xc - xa), 1.5)
            tip = f"{b['label']}: {bar_text(b)}" + (f" · {b['detail']}" if b["detail"] else "")
            out.append(f'<text class="ax" x="0" y="{yy + 19}">{esc(fit_label(b["label"], b["short"], LBL - 4, 11))}</text>')
            out.append(f'<g><title>{esc(tip)}</title><rect class="{bar_class(b)}" x="{left:.1f}" y="{yy + 6}" '
                       f'width="{w:.1f}" height="18" rx="2"/></g>')
            out.append(f'<text class="val" x="{left + w + 6:.1f}" y="{yy + 19}">{esc(bar_text(b))}</text>')
            if prev is not None:
                out.append(f'<line class="link" x1="{prev[0]:.1f}" y1="{prev[1]:.1f}" x2="{prev[0]:.1f}" y2="{yy + 6}"/>')
            prev = (xc, yy + 24)
    out.append("</svg>")
    return "".join(out)


def series_svg(blk: Dict[str, Any], wide: bool) -> str:
    xs, series, kind = blk["x"], blk["series"], blk["type"]
    vals = [float(v) for s in series for v in s["values"] if v is not None]
    lo, hi, step = scale(min(vals), max(vals), zero=blk["zero"] or kind == "bar")
    label = (blk["title"] or kind) + ": " + "; ".join(
        f"{s['name']} " + ", ".join(f"{x} {'n/a' if v is None else show(v)}" for x, v in zip(xs, s["values"])) for s in series)
    out = []
    n = len(xs)
    if wide or kind == "line":
        W, H = (640, 260) if wide else (360, 220)
        L, R, T, B = (48, 12, 12, 28) if wide else (40, 8, 10, 26)
        pw, ph = W - L - R, H - T - B
        every = max(1, math.ceil(n / (12 if wide else 6)))

        def y(v: float) -> float:
            return T + ph - (v - lo) / (hi - lo) * ph
        out.append(svg_open(W, H, "chart-wide" if wide else "chart-narrow", label))
        for t in ticks(lo, hi, step):
            yy = y(float(t))
            out.append(f'<line class="grid" x1="{L}" y1="{yy:.1f}" x2="{W - R}" y2="{yy:.1f}"/>'
                       f'<text class="ax" x="{L - 8}" y="{yy + 4:.1f}" text-anchor="end">{esc(tick_label(t, step))}</text>')
        if kind == "line":
            def xpos(i: int) -> float:
                return L + (pw / 2 if n == 1 else pw * i / (n - 1))
            for si, s in enumerate(series):
                pts = [(xpos(i), y(float(v))) for i, v in enumerate(s["values"]) if v is not None]
                d = " ".join(("M" if j == 0 else "L") + f"{px:.1f} {py:.1f}" for j, (px, py) in enumerate(pts))
                dash = ' stroke-dasharray="5 4"' if s["dashed"] else ""
                out.append(f'<path class="ln s{si + 1}" d="{d}"{dash}/>')
                for i, v in enumerate(s["values"]):
                    if v is None:
                        continue
                    out.append(f'<g><title>{esc(s["name"])} · {esc(xs[i])}: {esc(show(v))}</title>'
                               f'<circle class="pt s{si + 1}" cx="{xpos(i):.1f}" cy="{y(float(v)):.1f}" r="3"/></g>')
            for i, xl in enumerate(xs):
                if i % every == 0 or i == n - 1:
                    out.append(f'<text class="ax" x="{xpos(i):.1f}" y="{H - 8}" text-anchor="middle">{esc(xl)}</text>')
        else:
            slot = pw / n
            gw = slot * 0.72
            bw = gw / len(series)
            zero_y = y(max(lo, min(0.0, hi)))
            for i, xl in enumerate(xs):
                gx = L + slot * i + (slot - gw) / 2
                for si, s in enumerate(series):
                    v = s["values"][i]
                    if v is None:
                        continue
                    yv = y(float(v))
                    top, h = min(yv, zero_y), max(abs(zero_y - yv), 1)
                    out.append(f'<g><title>{esc(s["name"])} · {esc(xl)}: {esc(show(v))}</title>'
                               f'<rect class="bf s{si + 1}" x="{gx + bw * si + 1:.1f}" y="{top:.1f}" '
                               f'width="{max(bw - 2, 1):.1f}" height="{h:.1f}" rx="2"/></g>')
                    if len(series) == 1 and n <= 16:
                        out.append(f'<text class="val" x="{gx + bw * si + bw / 2:.1f}" y="{top - 5:.1f}" '
                                   f'text-anchor="middle">{esc(show(v))}</text>')
                if i % every == 0 or i == n - 1:
                    out.append(f'<text class="ax" x="{L + slot * i + slot / 2:.1f}" y="{H - 8}" text-anchor="middle">{esc(xl)}</text>')
            out.append(f'<line class="base" x1="{L}" y1="{zero_y:.1f}" x2="{W - R}" y2="{zero_y:.1f}"/>')
    else:  # bars at phone width: one row per category
        W, LBL, VAL = 360, 64, 52
        bh, gap = 9, 12
        row = len(series) * (bh + 2) + gap
        H = 8 + row * n
        x0, x1 = LBL, W - VAL

        def x(v: float) -> float:
            return x0 + (v - lo) / (hi - lo) * (x1 - x0)
        zx = x(max(lo, min(0.0, hi)))
        out.append(svg_open(W, H, "chart-narrow", label))
        for i, xl in enumerate(xs):
            y0 = 8 + row * i
            out.append(f'<text class="ax" x="0" y="{y0 + len(series) * (bh + 2) / 2 + 4:.1f}">{esc(fit_label(xl, "", LBL - 6, 11))}</text>')
            for si, s in enumerate(series):
                v = s["values"][i]
                if v is None:
                    continue
                xv = x(float(v))
                left, w = min(xv, zx), max(abs(xv - zx), 1)
                yy = y0 + si * (bh + 2)
                out.append(f'<g><title>{esc(s["name"])} · {esc(xl)}: {esc(show(v))}</title>'
                           f'<rect class="bf s{si + 1}" x="{left:.1f}" y="{yy}" width="{w:.1f}" height="{bh}" rx="2"/></g>'
                           f'<text class="val sm" x="{max(xv, zx) + 4:.1f}" y="{yy + bh - 1}">{esc(show(v))}</text>')
        out.append(f'<line class="base" x1="{zx:.1f}" y1="4" x2="{zx:.1f}" y2="{H - 4}"/>')
    out.append("</svg>")
    return "".join(out)


def legend(blk: Dict[str, Any]) -> str:
    items = []
    for i, s in enumerate(blk["series"], 1):
        kind = "dash" if s["dashed"] else ("line" if blk["type"] == "line" else "box")
        items.append(f'<span class="key"><i class="sw sw-{kind} s{i}" aria-hidden="true"></i>{esc(s["name"])}</span>')
    return f'<div class="legend">{"".join(items)}</div>'


# ---------------------------------------------------------------- html pieces

ARROW_UP = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16 7h6v6"/><path d="m22 7-8.5 8.5-5-5L2 17"/></svg>'
ARROW_DOWN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16 17h6v-6"/><path d="m22 17-8.5-8.5-5 5L2 7"/></svg>'
ARROW_FLAT = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14"/></svg>'
LOGO = ('<svg class="logo" viewBox="0 0 400 400" aria-hidden="true"><path d="M280 280H180L100 200V400H0V0L280 280Z" class="logo-ink"/>'
        '<path d="M400 400H300V100L400 0V400Z" class="logo-ink"/><path d="M280 252L214 186L280 120V252Z" class="logo-cyan"/></svg>')


def tile_html(t: Dict[str, Any]) -> str:
    icon = {"up": ARROW_UP, "down": ARROW_DOWN}.get(t["direction"], ARROW_FLAT)
    chip = f'<span class="chip tone-{t["tone"]}">{icon}{esc(t["change"])}</span>' if t["change"] else ""
    note = f'<span class="tile-note">{esc(t["note"])}</span>' if t["note"] else ""
    return (f'<div class="tile"><div class="tile-top"><span class="tile-label">{esc(t["label"])}</span>{chip}</div>'
            f'<div class="tile-bottom"><span class="tile-value">{esc(t["value"])}</span>{note}</div></div>')


def tone_of(text: str) -> str:
    s = text.strip()
    if not s or not any(c in "123456789" for c in s):
        return "neutral"
    if s.startswith(("(", "−", "-", "–")):
        return "bad"
    return "good"


def table_html(blk: Dict[str, Any]) -> str:
    cols = blk["columns"]
    head = "".join(f'<th scope="col" class="{"l" if c["align"] == "l" else "r"}">{esc(c["label"])}</th>' for c in cols)
    body = []
    for r in blk["rows"]:
        cells = []
        for i, (c, col) in enumerate(zip(r["cells"], cols)):
            tone = c["tone"] or (tone_of(c["text"]) if col["tone"] == "sign" else "")
            cls = ("l" if col["align"] == "l" else "r") + (f" tone-{tone}" if tone and tone != "neutral" else "")
            tag = "th scope=\"row\"" if i == 0 else "td"
            cells.append(f'<{tag} class="{cls}">{esc(c["text"])}</{tag.split()[0]}>')
        role = f' class="role-{r["role"]}"' if r["role"] else ""
        body.append(f"<tr{role}>{''.join(cells)}</tr>")
    title = f'<h3 class="block-title">{esc(blk["title"])}</h3>' if blk["title"] else ""
    sub = f'<p class="block-sub">{esc(blk["subtitle"])}</p>' if blk["subtitle"] else ""
    note = f'<p class="block-note">{esc(blk["note"])}</p>' if blk["note"] else ""
    return (f'<section class="block block-table{" wide" if blk["wide"] else ""}">{title}{sub}'
            f'<div class="scroll"><table class="grid-table"><thead><tr>{head}</tr></thead>'
            f'<tbody>{"".join(body)}</tbody></table></div>{note}</section>')


def chart_html(blk: Dict[str, Any]) -> str:
    if blk["type"] == "bridge":
        svgs = bridge_svg(blk, True) + bridge_svg(blk, False)
        leg = ""
    else:
        svgs = series_svg(blk, True) + series_svg(blk, False)
        leg = legend(blk)
    title = f'<h3 class="block-title">{esc(blk["title"])}</h3>' if blk["title"] else ""
    sub = f'<p class="block-sub">{esc(blk["subtitle"])}</p>' if blk["subtitle"] else ""
    note = f'<p class="block-note">{esc(blk["note"])}</p>' if blk["note"] else ""
    return (f'<section class="block card block-chart{" wide" if blk["wide"] else ""}"><div class="card-head">{title}{sub}</div>'
            f'{leg}<div class="chart-box">{svgs}</div>{note}</section>')


def text_html(blk: Dict[str, Any]) -> str:
    title = f'<h3 class="block-title">{esc(blk["title"])}</h3>' if blk["title"] else ""
    paras = "".join(f"<p>{esc(p)}</p>" for p in blk["body"])
    items = f'<ul>{"".join(f"<li>{esc(i)}</li>" for i in blk["items"])}</ul>' if blk["items"] else ""
    return f'<section class="block card block-text{" wide" if blk["wide"] else ""}">{title}{paras}{items}</section>'


def view_html(vw: Dict[str, Any], i: int, several: bool) -> str:
    parts = []
    if several:
        parts.append(f'<h2 class="view-title">{esc(vw["label"])}</h2>')
    parts += [f'<p class="summary">{esc(p)}</p>' for p in vw["summary"]]
    if vw["tiles"]:
        parts.append(f'<div class="tiles">{"".join(tile_html(t) for t in vw["tiles"])}</div>')
    blocks = []
    for b in vw["blocks"]:
        if b["type"] == "table":
            blocks.append(table_html(b))
        elif b["type"] == "text":
            blocks.append(text_html(b))
        else:
            blocks.append(chart_html(b))
    if blocks:
        parts.append(f'<div class="blocks">{"".join(blocks)}</div>')
    attrs = f' id="view-{i}" role="tabpanel" aria-labelledby="tab-{i}"' if several else ""
    return f'<div class="view"{attrs}>{"".join(parts)}</div>'


CSS = """
:root{color-scheme:light dark;
--bg:#FFFFFF;--text:#2F3A46;--strong:#021627;--muted:#6B7178;--line:#E9EAEC;--card:#FFFFFF;
--card-line:rgba(10,10,10,.10);--shadow:0 1px 2px rgba(0,0,0,.05);--seg:#F4F5F7;--seg-on:#FFFFFF;
--navy:#021627;--cyan:#00EAFF;--good:#15803D;--bad:#C62828;--neutral:#6B7178;--chip-line:#E9EAEC;
--total-bg:#E3FBFD;--sub-bg:#F6F7F8;--grid:#E6E8EB;--axis:#6B7178;--link:#9AA0A6;
--bar-total:#021627;--bar-up:#00A8B5;--bar-down:#8E8E93;--s1:#021627;--s2:#8E8E93;--s3:#00A8B5;--s4:#B45309}
@media (prefers-color-scheme:dark){:root{
--bg:#0A121A;--text:#D5DDE5;--strong:#F3F6F9;--muted:#8F9BA7;--line:#1E2A36;--card:#0F1A24;
--card-line:rgba(255,255,255,.09);--shadow:none;--seg:#14212D;--seg-on:#26384A;
--good:#4ADE80;--bad:#F87171;--neutral:#8F9BA7;--chip-line:#26323E;
--total-bg:rgba(0,234,255,.10);--sub-bg:rgba(255,255,255,.03);--grid:#1E2A36;--axis:#8F9BA7;--link:#5B6773;
--bar-total:#C7D2DD;--bar-up:#22C3D0;--bar-down:#6B7580;--s1:#E6EDF3;--s2:#7D8792;--s3:#22C3D0;--s4:#F59E0B}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--text);
font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",system-ui,"Helvetica Neue",sans-serif;-webkit-font-smoothing:antialiased}
.page{max-width:1120px;margin:0 auto;padding:36px 24px 40px;display:flex;flex-direction:column;gap:22px}
.head{display:flex;align-items:flex-end;justify-content:space-between;gap:16px;flex-wrap:wrap}
.head-text{display:flex;flex-direction:column;gap:6px;min-width:0}
.eyebrow{display:flex;align-items:center;gap:8px;margin:0;font-size:13px;color:var(--muted)}
.logo{width:18px;height:18px;flex:none}.logo-ink{fill:var(--strong)}.logo-cyan{fill:var(--cyan)}
h1{margin:0;font-size:28px;line-height:34px;font-weight:600;letter-spacing:-.5px;color:var(--strong)}
.seg{display:inline-flex;align-items:center;padding:2px;border-radius:999px;background:var(--seg);gap:0;max-width:100%;overflow-x:auto}
.seg button{appearance:none;border:0;margin:0;background:transparent;color:var(--muted);font:inherit;font-size:12.5px;font-weight:500;
height:28px;padding:0 12px;border-radius:999px;cursor:pointer;white-space:nowrap}
.seg button[aria-selected="true"]{background:var(--seg-on);color:var(--strong);box-shadow:0 1px 2px rgba(0,0,0,.08)}
.seg button:focus-visible{outline:2px solid var(--cyan);outline-offset:1px}
.view{display:flex;flex-direction:column;gap:22px}
.js .view[hidden]{display:none}
.view-title{margin:8px 0 0;font-size:18px;font-weight:600;color:var(--strong)}
.js .view-title{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.summary{margin:0;font-size:16px;line-height:26px;max-width:860px}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:16px}
.tile{display:flex;flex-direction:column;justify-content:space-between;min-height:102px;padding:15px;border-radius:16px;
border:1px solid var(--card-line);background:var(--card);box-shadow:var(--shadow);min-width:0}
.tile-top{display:flex;align-items:flex-start;justify-content:space-between;gap:8px}
.tile-label{font-size:14px;line-height:20px;font-weight:500;padding-top:3px;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.chip{display:inline-flex;align-items:center;gap:4px;height:26px;padding:2px 8px;border-radius:999px;border:1px solid var(--chip-line);
font-size:12px;font-weight:600;white-space:nowrap;flex:none;font-variant-numeric:tabular-nums}
.chip svg{width:12px;height:12px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.tile-bottom{display:flex;flex-direction:column;gap:2px;margin-top:10px}
.tile-value{font-size:24px;line-height:32px;font-weight:600;color:var(--strong);font-variant-numeric:tabular-nums}
.tile-note{font-size:12px;color:var(--muted)}
.tone-good{color:var(--good)}.tone-bad{color:var(--bad)}.tone-neutral{color:var(--neutral)}
.blocks{display:grid;grid-template-columns:minmax(0,1fr);gap:16px;align-items:start}
@media (min-width:880px){.blocks{grid-template-columns:repeat(2,minmax(0,1fr))}.block.wide{grid-column:1/-1}}
.card{border-radius:12px;border:1px solid var(--card-line);background:var(--card);box-shadow:var(--shadow);padding:15px;min-width:0}
.block{min-width:0;display:flex;flex-direction:column;gap:8px}
.block-title{margin:0;font-size:16px;line-height:20px;font-weight:600;letter-spacing:-.3px;color:var(--strong)}
.block-sub,.block-note{margin:0;font-size:12px;line-height:16px;color:var(--muted)}
.block-text p{margin:0}.block-text ul{margin:0;padding-left:20px}
.legend{display:flex;flex-wrap:wrap;gap:14px;font-size:12px;color:var(--muted)}
.key{display:inline-flex;align-items:center;gap:6px}
.sw{display:inline-block;width:14px;height:0;border-top:2px solid}
.sw-dash{border-top-style:dashed}.sw-box{height:10px;width:10px;border:0;border-radius:2px}
.sw.s1{border-color:var(--s1)}.sw.s2{border-color:var(--s2)}.sw.s3{border-color:var(--s3)}.sw.s4{border-color:var(--s4)}
.sw-box.s1{background:var(--s1)}.sw-box.s2{background:var(--s2)}.sw-box.s3{background:var(--s3)}.sw-box.s4{background:var(--s4)}
.chart-box{width:100%}
.chart{display:block;width:100%;height:auto;font-family:inherit;overflow:visible}
.chart-narrow{display:none}
.chart .grid{stroke:var(--grid);stroke-width:1}.chart .base{stroke:var(--axis);stroke-width:1.5}
.chart .link{stroke:var(--link);stroke-width:1;stroke-dasharray:2 3}
.chart .ax{font-size:12px;fill:var(--axis)}.chart-narrow .ax{font-size:11px}
.chart .val{font-size:12px;font-weight:600;fill:var(--text);font-variant-numeric:tabular-nums}.chart .val.sm{font-size:10px;font-weight:500}
.b-total{fill:var(--bar-total)}.b-up{fill:var(--bar-up)}.b-down{fill:var(--bar-down)}.b-flat{fill:var(--grid)}
.ln{fill:none;stroke-width:2;stroke-linejoin:round;stroke-linecap:round}
.ln.s1,.pt.s1{stroke:var(--s1)}.ln.s2,.pt.s2{stroke:var(--s2)}.ln.s3,.pt.s3{stroke:var(--s3)}.ln.s4,.pt.s4{stroke:var(--s4)}
.pt{fill:var(--card);stroke-width:2}
.bf.s1{fill:var(--s1)}.bf.s2{fill:var(--s2)}.bf.s3{fill:var(--s3)}.bf.s4{fill:var(--s4)}
.scroll{overflow-x:auto;-webkit-overflow-scrolling:touch;border-radius:10px 10px 0 0}
.grid-table{width:100%;border-collapse:collapse;font-size:12.5px;font-variant-numeric:tabular-nums}
.grid-table th,.grid-table td{height:32px;padding:0 12px;white-space:nowrap;border-bottom:1px solid var(--line)}
.grid-table thead th{background:var(--navy);color:#FFFFFF;font-weight:600;border-bottom:0}
.grid-table tbody th{font-weight:400;color:var(--text)}
.grid-table .l{text-align:left}.grid-table .r{text-align:right}
.grid-table td.tone-good{color:var(--good)}.grid-table td.tone-bad{color:var(--bad)}
.role-total th,.role-total td,.role-highlight th,.role-highlight td{background:var(--total-bg);font-weight:600}
.role-total th,.role-total td{border-top:1px solid var(--strong)}
.role-subtotal th,.role-subtotal td{background:var(--sub-bg);font-weight:600}
.role-ratio th,.role-ratio td{font-style:italic;color:var(--muted)}
.foot{font-size:12px;color:var(--muted);padding-top:4px}
@media (max-width:600px){
.page{padding:20px 16px 32px;gap:18px}
h1{font-size:22px;line-height:28px}
.head{flex-direction:column;align-items:stretch}
.seg{align-self:flex-start}
.tile{min-height:92px;padding:12px}.tile-value{font-size:20px;line-height:28px}
.chart-wide{display:none}.chart-narrow{display:block}
.summary{font-size:15px;line-height:24px}}
@media (pointer:coarse){.seg button{height:44px;padding:0 16px}}
@media print{.seg{display:none}.view[hidden]{display:flex!important}.js .view-title{position:static;width:auto;height:auto;clip:auto}
.card,.tile{box-shadow:none;break-inside:avoid}body{background:#FFFFFF}}
"""

JS = """
(function(){var d=document;d.documentElement.className+=' js';
var tabs=[].slice.call(d.querySelectorAll('.seg [role=tab]'));
function show(i,focus){tabs.forEach(function(t,j){var on=i===j;t.setAttribute('aria-selected',on?'true':'false');
t.tabIndex=on?0:-1;d.getElementById(t.getAttribute('aria-controls')).hidden=!on;});if(focus)tabs[i].focus();}
tabs.forEach(function(t,i){t.addEventListener('click',function(){show(i)});
t.addEventListener('keydown',function(e){var k=e.key,n=-1;if(k==='ArrowRight')n=(i+1)%tabs.length;
else if(k==='ArrowLeft')n=(i-1+tabs.length)%tabs.length;else if(k==='Home')n=0;else if(k==='End')n=tabs.length-1;
if(n>-1){e.preventDefault();show(n,true);}});});
if(tabs.length)show(0);})();
"""


def render(page: Dict[str, Any]) -> str:
    several = len(page["views"]) > 1
    title = page["title"] + (f" · {page['eyebrow']}" if page["eyebrow"] else "")
    eyebrow = f'<p class="eyebrow">{LOGO}<span>{esc(page["eyebrow"])}</span></p>' if page["eyebrow"] else ""
    seg = ""
    if several:
        btns = "".join(f'<button type="button" role="tab" id="tab-{i}" aria-controls="view-{i}" '
                       f'aria-selected="{"true" if i == 1 else "false"}">{esc(vw["label"])}</button>'
                       for i, vw in enumerate(page["views"], 1))
        seg = f'<div class="seg" role="tablist" aria-label="View">{btns}</div>'
    views = "".join(view_html(vw, i, several) for i, vw in enumerate(page["views"], 1))
    foot = f'<footer class="foot">{esc(page["footer"])}</footer>' if page["footer"] else ""
    script = f"<script>{JS}</script>" if several else ""
    return ("<!doctype html>\n"
            '<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            "<meta http-equiv=\"Content-Security-Policy\" content=\"default-src 'none'; style-src 'unsafe-inline'; "
            "script-src 'unsafe-inline'; img-src data:; base-uri 'none'; form-action 'none'\">\n"
            '<meta name="color-scheme" content="light dark">\n'
            '<meta name="generator" content="magnos page skill">\n'
            f"<title>{esc(title)}</title>\n<style>{CSS}</style>\n</head>\n<body>\n"
            f'<main class="page"><header class="head"><div class="head-text">{eyebrow}<h1>{esc(page["title"])}</h1></div>{seg}</header>'
            f"{views}{foot}</main>\n{script}\n</body>\n</html>\n")


# ---------------------------------------------------------------- command line

def default_out(spec_path: str) -> str:
    stem = os.path.splitext(os.path.basename(spec_path))[0]
    if stem.endswith("_page") and len(stem) > 5:
        stem = stem[:-5]
    return stem + ".html"


def inside(path: str) -> str:
    full = os.path.abspath(path)
    root = os.path.abspath(os.getcwd())
    if os.path.commonpath([full, root]) != root:
        raise SpecError(f"Write the page inside the working folder, not {path}.")
    return full


def open_file(path: str) -> bool:
    """Open with the system's opener: open (macOS), start (Windows), xdg-open (elsewhere)."""
    try:
        if sys.platform == "darwin":
            subprocess.Popen(["open", path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif os.name == "nt":
            os.startfile(path)  # type: ignore[attr-defined]  # the same as "start"
        else:
            subprocess.Popen(["xdg-open", path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except (OSError, AttributeError):
        return False


def counts(page: Dict[str, Any]) -> Dict[str, int]:
    c = {"views": len(page["views"]), "tiles": 0, "charts": 0, "tables": 0, "texts": 0}
    for vw in page["views"]:
        c["tiles"] += len(vw["tiles"])
        for b in vw["blocks"]:
            key = {"table": "tables", "text": "texts"}.get(b["type"], "charts")
            c[key] += 1
    return c


def plural(n: int, word: str) -> str:
    return f"{n} {word}" + ("" if n == 1 else "s")


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(prog="page.py", description="Render a page spec as one self-contained HTML file.")
    ap.add_argument("spec", help="the page spec, a JSON file (see references/spec.md)")
    ap.add_argument("--out", help="the HTML file to write (default: the spec's name with .html)")
    ap.add_argument("--open", action="store_true", help="open the page in the default browser")
    a = ap.parse_args(argv)
    try:
        if not os.path.exists(a.spec):
            raise SpecError(f"Cannot find {a.spec}. Check the path, or write the spec first.")
        try:
            with open(a.spec, encoding="utf-8") as fh:
                spec = json.load(fh, parse_float=Decimal)
        except json.JSONDecodeError as exc:
            raise SpecError(f"{os.path.basename(a.spec)} is not valid JSON (line {exc.lineno}: {exc.msg}). Fix it and run again.")
        page = check(spec)
        out = a.out or default_out(a.spec)
        if not out.lower().endswith((".html", ".htm")):
            out += ".html"
        full = inside(out)
        doc = render(page)
        os.makedirs(os.path.dirname(full) or ".", exist_ok=True)
        with open(full, "w", encoding="utf-8") as fh:
            fh.write(doc)
    except SpecError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    c = counts(page)
    views = ", ".join(vw["label"] for vw in page["views"] if vw["label"])
    lines = [f"Wrote {out}: \"{page['title']}\"" + (f" for {page['eyebrow']}." if page["eyebrow"] else "."),
             f"{plural(c['views'], 'view')}" + (f" ({views})" if views else "") +
             f" · {plural(c['tiles'], 'tile')} · {plural(c['charts'], 'chart')} · {plural(c['tables'], 'table')}. "
             f"One file, {len(doc.encode('utf-8')) // 1024 + 1} KB, no network requests."]
    if a.open:
        lines.append("Opened it in the default browser." if open_file(full)
                     else f"Could not open it here; open {out} in a browser.")
    mf.emit("\n".join(lines), {"tool": "page", "out": out, "title": page["title"], "views": [vw["label"] for vw in page["views"]],
                               "counts": c, "bytes": len(doc.encode("utf-8")), "spec": a.spec}, JSON_PATH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
