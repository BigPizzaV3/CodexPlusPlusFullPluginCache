#!/usr/bin/env python3
"""Draw a budget variance as a driver tree or a bridge, as SVG and as Mermaid.

Reads the machine result of variance.py (.magnos/runs/variance.json by default)
and draws it; it computes nothing new. Worse than budget is red, better is green,
and every box or bar shows its signed value.

  python3 scripts/diagram.py                 driver tree: variance_tree.svg + .mmd
  python3 scripts/diagram.py --kind bridge   budget to actual: variance_bridge.svg + .mmd
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from decimal import Decimal
from typing import Any, Dict, List, Optional, Sequence, Tuple
from xml.sax.saxutils import escape

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import magnos_fin as mf  # noqa: E402

JSON_PATH = os.path.join(".magnos", "runs", "variance.json")
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif"
INK, MUTED, NAVY, LINK = "#021627", "#52575D", "#021627", "#C9CCD1"
TONES = {  # fill, stroke, value text
    "worse": ("#FEF2F2", "#FCA5A5", "#B91C1C"),
    "better": ("#F0FDF4", "#86EFAC", "#15803D"),
    "even": ("#F4F5F7", "#D5D8DC", "#2F3A46"),
}
BAR = {"worse": "#DC2626", "better": "#16A34A", "even": "#8E8E93", "total": NAVY}


class InputError(Exception):
    pass


def tone(value: Decimal, favourable: bool) -> str:
    if value == 0:
        return "even"
    return "better" if favourable else "worse"


def fit(text: str, max_chars: int) -> str:
    return text if len(text) <= max_chars else text[:max_chars - 1].rstrip() + "…"


def attr(text: str) -> str:
    return escape(text, {'"': "&quot;"})


# ---------------------------------------------------------------- driver tree

BOX_W, BOX_H, GAP_X, GAP_Y, GROUP_GAP, PAD = 184, 60, 56, 16, 14, 24


def _layout(node: Dict[str, Any], depth: int, state: Dict[str, Any], parent: Optional[int]) -> float:
    node["_depth"] = depth
    kids = node.get("children") or []
    if not kids:
        if state["last_parent"] is not None and state["last_parent"] != parent:
            state["y"] += GROUP_GAP
        node["_cy"] = state["y"] + BOX_H / 2
        state["y"] += BOX_H + GAP_Y
        state["last_parent"] = parent
        state["depth"] = max(state["depth"], depth)
        return node["_cy"]
    ys = [_layout(k, depth + 1, state, id(node)) for k in kids]
    node["_cy"] = (ys[0] + ys[-1]) / 2
    return node["_cy"]


def _walk(node: Dict[str, Any]):
    yield node
    for k in node.get("children") or []:
        yield from _walk(k)


def tree_svg(data: Dict[str, Any]) -> str:
    root = json.loads(json.dumps(data["tree"]))  # a private copy to annotate
    title = f"{data['gap']['line']} against {data['budget_label']} · {data['period']['label']}"
    top = PAD + 30
    state = {"y": float(top), "last_parent": None, "depth": 0}
    _layout(root, 0, state, None)
    width = PAD * 2 + (state["depth"] + 1) * BOX_W + state["depth"] * GAP_X
    plot_bottom = state["y"] - GAP_Y
    height = int(plot_bottom + 52)
    legend = (f"Red is worse than {data['budget_label']}, green is better. "
              + ("Values are better/(worse) than budget." if data.get("sign") != "actual-minus-budget"
                 else "Values are actual less budget."))
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
           f'role="img" aria-label="{attr(title)}" font-family="{attr(FONT)}">',
           f"<title>{escape(title)}</title>",
           f'<rect x="0" y="0" width="{width}" height="{height}" rx="16" fill="#FFFFFF"/>',
           f'<text x="{PAD}" y="{PAD + 14}" font-size="15" font-weight="600" fill="{INK}">{escape(title)}</text>']
    for n in _walk(root):
        x1 = PAD + n["_depth"] * (BOX_W + GAP_X) + BOX_W
        for k in n.get("children") or []:
            x2 = PAD + k["_depth"] * (BOX_W + GAP_X)
            xm = (x1 + x2) / 2
            out.append(f'<path d="M{x1} {n["_cy"]:.1f} C{xm} {n["_cy"]:.1f}, {xm} {k["_cy"]:.1f}, {x2} {k["_cy"]:.1f}" '
                       f'fill="none" stroke="{LINK}" stroke-width="1.5"/>')
    for n in _walk(root):
        v = Decimal(n["value"])
        fill, stroke, ink = TONES[tone(v, n["favourable"])]
        x = PAD + n["_depth"] * (BOX_W + GAP_X)
        y = n["_cy"] - BOX_H / 2
        out.append(f'<g class="box {tone(v, n["favourable"])}"><title>{escape(n["label"])}: {escape(n["display"])}</title>'
                   f'<rect x="{x}" y="{y:.1f}" width="{BOX_W}" height="{BOX_H}" rx="12" fill="{fill}" stroke="{stroke}"/>'
                   f'<text x="{x + 12}" y="{y + 23:.1f}" font-size="12.5" fill="{MUTED}">{escape(fit(n["label"], 24))}</text>'
                   f'<text x="{x + 12}" y="{y + 45:.1f}" font-size="17" font-weight="600" fill="{ink}" '
                   f'style="font-variant-numeric: tabular-nums">{escape(n["display"])}</text></g>')
    out.append(f'<text x="{PAD}" y="{height - 20}" font-size="12" fill="{MUTED}">{escape(legend)}</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


def _mm(text: str) -> str:
    return text.replace('"', "#quot;")


def tree_mermaid(data: Dict[str, Any]) -> str:
    lines = ["flowchart LR"]
    ids: Dict[int, str] = {}
    nodes = list(_walk(data["tree"]))
    for i, n in enumerate(nodes):
        ids[id(n)] = f"n{i}"
        t = tone(Decimal(n["value"]), n["favourable"])
        lines.append(f'  n{i}["{_mm(n["label"])}<br/>{_mm(n["display"])}"]:::{t}')
    for n in nodes:
        for k in n.get("children") or []:
            lines.append(f"  {ids[id(n)]} --> {ids[id(k)]}")
    for name, (fill, stroke, ink) in TONES.items():
        lines.append(f"  classDef {name} fill:{fill},stroke:{stroke},color:{ink}")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- bridge

def nice_step(span: float, target: int = 5) -> float:
    if span <= 0:
        return 1.0
    raw = span / target
    mag = 10 ** int(f"{raw:e}".split("e")[1])
    for m in (1, 2, 2.5, 5, 10):
        if raw <= m * mag:
            return m * mag
    return 10 * mag


def bridge_bars(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    b = data["bridge"]
    bars = [{"label": b["start"]["label"], "value": Decimal(b["start"]["value"]), "display": b["start"]["display"], "kind": "total"}]
    for s in b["steps"]:
        bars.append({"label": s["label"], "value": Decimal(s["value"]), "display": s["display"],
                     "kind": tone(Decimal(s["value"]), s.get("favourable", Decimal(s["value"]) >= 0))})
    bars.append({"label": b["end"]["label"], "value": Decimal(b["end"]["value"]), "display": b["end"]["display"], "kind": "total"})
    return bars


def _wrap(label: str, width: int = 13) -> List[str]:
    if len(label) <= width:
        return [label]
    words, lines, cur = label.split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    lines.append(cur)
    return [fit(lines[0], width + 2), fit(" ".join(lines[1:]), width + 2)] if len(lines) > 2 else lines


def bridge_svg(data: Dict[str, Any]) -> str:
    bars = bridge_bars(data)
    title = f"{data['gap']['line']}, {data['budget_label']} to actual · {data['period']['label']}"
    slot, bar_w, left, top, plot_h = 104, 58, 72, PAD + 44, 280
    width = left + slot * len(bars) + PAD
    levels, run = [], Decimal(0)
    for i, b in enumerate(bars):
        if b["kind"] == "total":
            run = b["value"]
            levels.append((Decimal(0), run))
        else:
            levels.append((run, run + b["value"]))
            run += b["value"]
    lo_v = min(min(a, c) for a, c in levels[1:-1] + [(bars[0]["value"], bars[-1]["value"])])
    hi_v = max(max(a, c) for a, c in levels)
    lo_f, hi_f = float(lo_v), float(hi_v)
    if lo_f > 0 and (hi_f - lo_f) < 0.5 * hi_f:  # small steps: start the axis near the lowest level
        step = nice_step(hi_f - lo_f)
        lo = (lo_f // step) * step - step
    else:
        lo = min(0.0, lo_f)
        step = nice_step(hi_f - lo)
        lo = (lo // step) * step
    hi = -((-hi_f) // step) * step
    if hi <= hi_f:
        hi += step

    def y(v: float) -> float:
        return top + plot_h - (v - lo) / (hi - lo) * plot_h

    height = int(top + plot_h + 64)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
           f'role="img" aria-label="{attr(title)}" font-family="{attr(FONT)}">',
           f"<title>{escape(title)}</title>",
           f'<rect x="0" y="0" width="{width}" height="{height}" rx="16" fill="#FFFFFF"/>',
           f'<text x="{PAD}" y="{PAD + 14}" font-size="15" font-weight="600" fill="{INK}">{escape(title)}</text>']
    t = lo
    while t <= hi + step / 1000:
        yy = y(t)
        out.append(f'<line x1="{left - 6}" y1="{yy:.1f}" x2="{width - PAD}" y2="{yy:.1f}" stroke="#E3E5E8" stroke-width="1"/>')
        out.append(f'<text x="{left - 10}" y="{yy + 4:.1f}" font-size="11" text-anchor="end" fill="{MUTED}">'
                   f'{escape(mf.money(Decimal(str(t))))}</text>')
        t += step
    prev_end = None
    for i, (b, (a, c)) in enumerate(zip(bars, levels)):
        cx = left + slot * i + slot / 2
        x = cx - bar_w / 2
        if b["kind"] == "total":
            y0, y1 = y(max(lo, 0.0)), y(float(c))
        else:
            y0, y1 = y(float(a)), y(float(c))
        ytop, ybot = min(y0, y1), max(y0, y1)
        h = max(ybot - ytop, 1.5)
        color = BAR[b["kind"]]
        out.append(f'<g><title>{escape(b["label"])}: {escape(b["display"])}</title>'
                   f'<rect x="{x:.1f}" y="{ytop:.1f}" width="{bar_w}" height="{h:.1f}" rx="3" fill="{color}"/></g>')
        ink = INK if b["kind"] == "total" else TONES.get(b["kind"], TONES["even"])[2]
        out.append(f'<text x="{cx:.1f}" y="{ytop - 7:.1f}" font-size="12.5" font-weight="600" text-anchor="middle" '
                   f'fill="{ink}">{escape(b["display"])}</text>')
        for j, line in enumerate(_wrap(b["label"])):
            out.append(f'<text x="{cx:.1f}" y="{top + plot_h + 20 + j * 15:.1f}" font-size="12" text-anchor="middle" '
                       f'fill="{MUTED}">{escape(line)}</text>')
        if prev_end is not None:
            out.append(f'<line x1="{prev_end[0]:.1f}" y1="{prev_end[1]:.1f}" x2="{x:.1f}" y2="{prev_end[1]:.1f}" '
                       f'stroke="#7C8085" stroke-width="1" stroke-dasharray="2 3"/>')
        prev_end = (x + bar_w, y(float(c)))
    out.append(f'<line x1="{left - 6}" y1="{y(lo):.1f}" x2="{width - PAD}" y2="{y(lo):.1f}" stroke="#7C8085" stroke-width="1.5"/>')
    legend = f"Red is worse than {data['budget_label']}, green is better."
    if lo > 0:
        legend += f" The axis starts at {mf.money(Decimal(str(lo)))}."
    out.append(f'<text x="{PAD}" y="{height - 12}" font-size="12" fill="{MUTED}">{escape(legend)}</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


def bridge_mermaid(data: Dict[str, Any]) -> str:
    bars = bridge_bars(data)
    lines = ["flowchart LR"]
    for i, b in enumerate(bars):
        cls = "total" if b["kind"] == "total" else b["kind"]
        lines.append(f'  b{i}["{_mm(b["label"])}<br/>{_mm(b["display"])}"]:::{cls}')
    lines.append("  " + " --> ".join(f"b{i}" for i in range(len(bars))))
    for name, (fill, stroke, ink) in TONES.items():
        lines.append(f"  classDef {name} fill:{fill},stroke:{stroke},color:{ink}")
    lines.append(f"  classDef total fill:{NAVY},stroke:{NAVY},color:#FFFFFF")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- command line

def load(path: str) -> Dict[str, Any]:
    if not os.path.exists(path):
        raise InputError(f"No variance result at {path}. Run python3 scripts/variance.py <actuals> <budget> first.")
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, json.JSONDecodeError):
        raise InputError(f"{path} is not a variance result. Run python3 scripts/variance.py again.")
    if "tree" not in data and isinstance(data.get("ytd"), dict):  # a board-pack result
        data = data["ytd"]
    if "tree" not in data or "bridge" not in data:
        raise InputError(f"{path} has no driver tree or bridge. Run python3 scripts/variance.py again.")
    return data


def inside(path: str) -> str:
    full = os.path.abspath(path)
    root = os.path.abspath(os.getcwd())
    if os.path.commonpath([full, root]) != root:
        raise InputError(f"Write the diagram inside the working folder, not {path}.")
    return full


def box_rows(data: Dict[str, Any], kind: str) -> List[List[str]]:
    if kind == "tree":
        return [[n["label"], parent, n["display"]] for n, parent in _parent_walk(data["tree"])]
    return [[b["label"], b["display"]] for b in bridge_bars(data)]


def _parent_walk(node: Dict[str, Any], parent: str = ""):
    yield node, parent
    for k in node.get("children") or []:
        yield from _parent_walk(k, node["label"])


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(prog="diagram.py", description="Draw a variance as a driver tree or a bridge (SVG and Mermaid).")
    ap.add_argument("--kind", choices=["tree", "bridge"], default="tree", help="driver tree (default) or bridge from budget to actual")
    ap.add_argument("--json", default=JSON_PATH, help=f"the variance result to draw (default {JSON_PATH})")
    ap.add_argument("--out", help="file name without extension (default variance_tree or variance_bridge)")
    ap.add_argument("--format", choices=["svg", "mermaid", "both"], default="both")
    a = ap.parse_args(argv)
    try:
        data = load(a.json)
        stem = a.out or f"variance_{a.kind}"
        if stem.lower().endswith((".svg", ".mmd")):
            stem = stem[:-4]
        svg = tree_svg(data) if a.kind == "tree" else bridge_svg(data)
        mmd = tree_mermaid(data) if a.kind == "tree" else bridge_mermaid(data)
        written = []
        if a.format in ("svg", "both"):
            with open(inside(stem + ".svg"), "w", encoding="utf-8") as fh:
                fh.write(svg)
            written.append(stem + ".svg")
        if a.format in ("mermaid", "both"):
            with open(inside(stem + ".mmd"), "w", encoding="utf-8") as fh:
                fh.write(mmd)
            written.append(stem + ".mmd")
    except InputError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    what = "a driver tree" if a.kind == "tree" else f"a bridge from {data['budget_label']} to actual"
    gap = data["gap"]
    md = [f"Drew {gap['line']} against {data['budget_label']} for {data['period']['label']} as {what}. "
          f"Red is worse than {data['budget_label']}, green is better.", ""]
    head = "Better/(worse)" if data.get("sign") != "actual-minus-budget" else "Actual − budget"
    if a.kind == "tree":
        md.append(mf.md_table(["Box", "Part of", head], box_rows(data, a.kind), align=["l", "l", "r"]))
    else:
        md.append(mf.md_table(["Bar", "Value"], box_rows(data, a.kind)))
    md += ["", "```mermaid", mmd.rstrip(), "```", "", f"Wrote {' and '.join(written)}."]
    mf.emit("\n".join(md))
    return 0


if __name__ == "__main__":
    sys.exit(main())
