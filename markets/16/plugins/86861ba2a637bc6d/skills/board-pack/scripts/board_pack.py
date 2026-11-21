#!/usr/bin/env python3
"""Board pack: one page on the month in Finance plain, and the same content as a page spec.

Combines, from a P&L export of actuals and a budget export:
- the variance against budget for the year to date and for the latest month;
- the movement from the month before.

Writes board_pack_<mon>.md (one paragraph, a KPI table, the lines that explain the
gap, what moved, one next step) and board_pack_<mon>_page.json, a spec the page
skill renders as a self-contained HTML page.

  python3 scripts/board_pack.py pnl_monthly.csv budget_fy26_v3.csv --company "Harbor & Pine"

The arithmetic lives in scripts/variance.py, a byte-identical copy of the variance
skill's engine.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
from decimal import Decimal
from typing import Any, Dict, List, Optional, Sequence, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import magnos_fin as mf  # noqa: E402
import variance as v  # noqa: E402

D0 = Decimal(0)
JSON_PATH = os.path.join(".magnos", "runs", "board-pack.json")
InputError = v.InputError


# ---------------------------------------------------------------- small helpers

def inside(path: str) -> str:
    full = os.path.abspath(path)
    root = os.path.abspath(os.getcwd())
    if os.path.commonpath([full, root]) != root:
        raise InputError(f"Write the board pack inside the working folder, not {path}.")
    return full


def signed_pct(r: Optional[Decimal]) -> str:
    return "n/a" if r is None else mf.pct(r, signed=True)


def direction(x: Optional[Decimal], shown: str) -> str:
    """up, down, or flat when the change is zero as shown."""
    if x is None or x == 0 or not any(ch in "123456789" for ch in shown):
        return "flat"
    return "up" if x > 0 else "down"


def revenue_row(res: Dict[str, Any]) -> Dict[str, Any]:
    """The revenue line, or Total revenue when there are several."""
    rev = [r for r in res["leaves"] if r["type"] == "revenue"]
    if len(rev) == 1:
        return rev[0]
    return next(r for r in res["rows"] if r["line"] == "Total revenue")


def tile(label: str, value: str, change: str, raw: Optional[Decimal], higher_is_better: bool = True,
         note: Optional[str] = None) -> Dict[str, Any]:
    d = direction(raw, change)
    tone = "neutral" if d == "flat" else ("good" if (d == "up") == higher_is_better else "bad")
    out = {"label": label, "value": value, "change": change, "direction": d, "tone": tone}
    if note:
        out["note"] = note
    return out


def jnum(x: Decimal) -> Any:
    """A Decimal as a JSON number: int when whole."""
    return int(x) if x == x.to_integral_value() else float(str(x))


def as_of_label(text: Optional[str]) -> str:
    d = mf.parse_date(text) if text else _dt.date.today()
    if d is None:
        raise InputError(f"Cannot read --as-of '{text}'. Write it like 2026-10-04.")
    return f"{v.SHORT[d.month - 1]} {d.day}, {d.year}"


def month_values(p: v.Pnl, months: Sequence[str]) -> Dict[str, List[Decimal]]:
    """Revenue, cost of revenue, operating expenses and EBITDA for each month."""
    out: Dict[str, List[Decimal]] = {"revenue": [], "cogs": [], "opex": [], "ebitda": []}
    for m in months:
        s = {t: sum((vals.get(m, D0) for n, vals in p.lines.items() if p.types.get(n) == t), D0)
             for t in ("revenue", "cogs", "opex")}
        for t in ("revenue", "cogs", "opex"):
            out[t].append(s[t])
        out["ebitda"].append(s["revenue"] - s["cogs"] - s["opex"])
    return out


def rounded_bridge(start: Decimal, steps: List[Tuple[str, str, Decimal]], end: Decimal,
                   scale: Decimal, places: int) -> Tuple[Decimal, List[Tuple[str, str, Decimal]], Decimal, Decimal]:
    """Round to the chart's unit and keep the bridge tied: any rounding goes into the largest step."""
    q = Decimal(1).scaleb(-places)

    def r(x: Decimal) -> Decimal:
        return (x / scale).quantize(q)
    s0, e0 = r(start), r(end)
    rs = [(lab, short, r(x)) for lab, short, x in steps]
    residual = e0 - s0 - sum((x for _, _, x in rs), D0)
    if residual and rs:
        i = max(range(len(rs)), key=lambda j: abs(rs[j][2]))
        lab, short, x = rs[i]
        rs[i] = (lab, short, x + residual)
    return s0, rs, e0, residual


# ---------------------------------------------------------------- the pack

def build(a: argparse.Namespace) -> Dict[str, Any]:
    profile = mf.load_profile()
    overrides = v.read_overrides(a.line_type)
    act = v.load_pnl(a.actuals, overrides, a.year, sheet=a.sheet)
    bud = v.load_pnl(a.budget, overrides, a.year, version=a.version, sheet=a.sheet)
    have = act.months()
    month = v.parse_month(a.month) if a.month else have[-1]
    if a.month and not month:
        raise InputError(f"Cannot read the month '{a.month}'. Write it like 2026-09.")
    if month not in have:
        raise InputError(f"{act.name} has no actuals for {v.long_label(month)}; it covers {v.period_label(have)}.")
    ytd_m = v.ytd_months(month, mf.fiscal_start_month(profile))
    missing = [m for m in ytd_m if m not in have]
    if missing:
        raise InputError(f"{act.name} has no actuals for {v.period_label(missing)}, which the year to date needs.")
    bmiss = [m for m in ytd_m if m not in bud.months()]
    if bmiss:
        raise InputError(f"{bud.name} has no budget for {v.period_label(bmiss)}. Use a budget that covers the year to date.")
    ytd = v.compare(act, bud, ytd_m, a.label)
    mon = v.compare(act, bud, [month], a.label)
    if ytd["bottom"]["line"] != "EBITDA":
        raise InputError("The board pack needs revenue and cost lines to derive EBITDA. "
                         "Check the line types with --line-type.")
    prior = v.add_months(month, -1)
    mov = v.movement(act, month, prior) if prior in have else None
    lab = ytd["budget_label"]
    scale, unit_label = v.choose_scale([r["actual"] for r in ytd["rows"]] + [r["budget"] for r in ytd["rows"]], a.unit)
    places = 2 if unit_label == "$M" else 0
    t = mov["totals"] if mov else None
    rev_now = sum((r["actual"] for r in mon["leaves"] if r["type"] == "revenue"), D0)
    big = abs(rev_now) >= Decimal(1_000_000)

    def kv(x: Decimal) -> str:  # KPI values: millions when monthly revenue is $1M or more
        return mf.money(x, unit="M") if big else mf.money(x)

    mname, pname = v.month_name(month), v.month_name(prior)
    per_m, per_y = v.long_label(month), ytd["period"]["label"]
    eb_m, eb_y = mon["bottom"], ytd["bottom"]
    gm_m, gm_mb = v.ratio(mon, "gross_margin", "actual"), v.ratio(mon, "gross_margin", "budget")
    gm_y, gm_yb = v.ratio(ytd, "gross_margin", "actual"), v.ratio(ytd, "gross_margin", "budget")
    em_m, em_mb = v.ratio(mon, "ebitda_margin", "actual"), v.ratio(mon, "ebitda_margin", "budget")
    em_y, em_yb = v.ratio(ytd, "ebitda_margin", "actual"), v.ratio(ytd, "ebitda_margin", "budget")
    rev_m, rev_y = revenue_row(mon), revenue_row(ytd)

    def pts_of(a_: Optional[Decimal], b_: Optional[Decimal]) -> Optional[Decimal]:
        return None if a_ is None or b_ is None else (a_ - b_) * 100

    ratios = []  # every ratio the pack prints, for the ledger
    for name, (am, bm, ay, by) in (("Gross margin", (gm_m, gm_mb, gm_y, gm_yb)), ("EBITDA margin", (em_m, em_mb, em_y, em_yb))):
        if am is None:
            continue
        ratios += [(f"{name}, {per_m}", am, mf.pct(am)), (f"{name}, {per_m}, {lab}", bm, mf.pct(bm)),
                   (f"{name}, {per_y}", ay, mf.pct(ay)), (f"{name}, {per_y}, {lab}", by, mf.pct(by)),
                   (f"{name} vs {lab}, {per_m}, pts", pts_of(am, bm), mf.pts(pts_of(am, bm))),
                   (f"{name} vs {lab}, {per_y}, pts", pts_of(ay, by), mf.pts(pts_of(ay, by)))]

    # ---- the paragraph
    sents = []
    if t:
        ch = t["ebitda"]["change"]
        how = "unchanged on" if ch == 0 else ("up" if ch > 0 else "down")
        p = f" ({mf.pct(abs(t['ebitda']['pct']))})" if t["ebitda"]["pct"] is not None and ch else ""
        sents.append(f"EBITDA is {kv(eb_m['actual'])} for {per_m}, "
                     + (f"unchanged on {pname}." if ch == 0 else f"{how} {mf.money(abs(ch))}{p} on {pname}."))
        rc = t["revenue"]["change"]
        if rc:
            sents.append(f"Revenue {'rose' if rc > 0 else 'fell'} {mf.money(abs(rc))} "
                         f"({mf.pct(abs(t['revenue']['pct']))}) to {kv(t['revenue']['current'])}.")
        gp = t["gross_margin"]
        if gp["pts"] is not None and gp["current"] is not None:
            shown = mf.pts(abs(gp["pts"]), signed=False)
            if shown == "0.0 pts":
                sents.append(f"Gross margin held at {mf.pct(gp['current'])}.")
            else:
                sents.append(f"Gross margin {'rose' if gp['pts'] > 0 else 'fell'} {shown} to {mf.pct(gp['current'])}.")
    else:
        sents.append(f"EBITDA is {kv(eb_m['actual'])} for {per_m}.")
    for res, lead in ((mon, f"{mname} EBITDA is"), (ytd, f"Year to date, EBITDA is {kv(eb_y['actual'])},")):
        b = res["bottom"]
        ref = b["actual"]
        if b["diff"] == 0:
            sents.append(f"{lead} on {lab}.")
            continue
        where = "above" if b["diff"] > 0 else "below"
        pc = f" ({v.pct_words(b['pct'])})" if b["pct"] is not None else ""
        sents.append(f"{lead} {v.amt(abs(b['diff']), ref)}{pc} {where} {lab}.")
    paragraph = " ".join(sents)

    # ---- the KPI table
    def kpi_pct(r: Optional[Decimal]) -> str:
        return v.table_pct(r)

    def kpi_pts(x: Optional[Decimal]) -> str:
        return "n/a" if x is None else v.table_pts(x)

    cols = ["KPI", v.short_label(month)]
    if t:
        cols.append(f"vs {v.short_label(prior)}")
    cols += [f"vs {lab}", per_y, f"vs {lab}"]
    kpis = []

    def kpi_row(name: str, now: str, mom: Optional[str], vs_b: str, ytd_v: str, vs_by: str) -> List[str]:
        row = [name, now] + ([mom or "n/a"] if t else []) + [vs_b, ytd_v, vs_by]
        kpis.append(row)
        return row

    kpi_row("Revenue", kv(rev_m["actual"]), kpi_pct(t["revenue"]["pct"]) if t else None,
            kpi_pct(rev_m["better_pct"]), kv(rev_y["actual"]), kpi_pct(rev_y["better_pct"]))
    if gm_m is not None:
        kpi_row("Gross margin", mf.pct(gm_m), kpi_pts(t["gross_margin"]["pts"]) if t else None,
                kpi_pts(pts_of(gm_m, gm_mb)), mf.pct(gm_y), kpi_pts(pts_of(gm_y, gm_yb)))
    kpi_row("EBITDA", kv(eb_m["actual"]), kpi_pct(t["ebitda"]["pct"]) if t else None,
            kpi_pct(eb_m["better_pct"]), kv(eb_y["actual"]), kpi_pct(eb_y["better_pct"]))
    if em_m is not None:
        kpi_row("EBITDA margin", mf.pct(em_m), kpi_pts(t["ebitda_margin"]["pts"]) if t else None,
                kpi_pts(pts_of(em_m, em_mb)), mf.pct(em_y), kpi_pts(pts_of(em_y, em_yb)))

    # ---- the lines that explain the gap
    d = ytd["drivers"]
    mon_by = {v.norm(r["line"]): r for r in mon["leaves"]}
    drow = []
    for r in d["lines"]:
        m = mon_by.get(v.norm(r["line"]))
        drow.append([r["line"], v.table_better(r["better"], scale),
                     "n/a" if r.get("share") is None else v.table_pct(r["share"], decimals=0),
                     "n/a" if m is None else v.table_better(m["better"], scale)])

    # ---- the next step
    nxt = ""
    cost_driver = next((r for r in d["lines"] if r["type"] in ("cogs", "opex")), None)
    rev_driver = next((r for r in d["lines"] if r["type"] == "revenue"), None)
    if cost_driver is not None:
        who = v.lower_first(cost_driver["line"])
        nxt = (f"ask the owner of {who} which costs are above {lab}." if not cost_driver["favourable"]
               else f"ask the owner of {who} whether the saving against {lab} will last.")
    elif rev_driver is not None:
        nxt = (f"ask the sales lead which deals moved revenue below {lab}." if not rev_driver["favourable"]
               else f"ask the sales lead which deals lifted revenue above {lab}.")

    # ---- what moved
    moved = []
    if mov:
        for r in mov["rows"]:
            moved.append([r["line"], v.table_amount(r["prior"], scale), v.table_amount(r["current"], scale),
                          v.table_better(r["effect"], scale)])
        moved.append(["**EBITDA**", v.table_amount(t["ebitda"]["prior"], scale), v.table_amount(t["ebitda"]["current"], scale),
                      v.table_better(t["ebitda"]["change"], scale)])

    # ---- markdown
    company = a.company or profile.get("company") or ""
    title = f"# {company + ' · ' if company else ''}{per_m} board pack"
    md = [title, "", paragraph, "", mf.md_table(cols, kpis)]
    if d["lines"]:
        md += ["", f"## The lines that explain the gap to {lab}", "", v.drivers_sentence(ytd), "",
               mf.md_table(["Line", f"{per_y} better/(worse), {unit_label}", "Share of the gap",
                            f"{v.short_label(month)} better/(worse), {unit_label}"], drow), ""]
        md += [f"- {v.line_sentence(r, ytd)}" for r in d["lines"]]
    if moved:
        md += ["", f"## What moved from {pname}", "",
               mf.md_table([unit_label, v.short_label(prior), v.short_label(month), "Effect on EBITDA"], moved)]
    if nxt:
        md += ["", f"**Next step:** {nxt}"]
    md += ["", f"Source: {act.name} (actuals) and {bud.name} ({lab}). Made by the magnos board-pack skill."]
    markdown = "\n".join(md)

    # ---- the page spec
    spec = page_spec(a, act, bud, ytd, mon, mov, month, prior, scale, unit_label, places, kv, paragraph,
                     nxt, company, gm_m, gm_y, gm_yb, em_m, em_y, em_yb, rev_y, eb_y, lab)
    return {"act": act, "bud": bud, "ytd": ytd, "mon": mon, "mov": mov, "month": month, "prior": prior,
            "markdown": markdown, "spec": spec, "scale": scale, "unit_label": unit_label, "profile": profile,
            "paragraph": paragraph, "next_step": nxt, "kpis": {"columns": cols, "rows": kpis}, "ratios": ratios}


def page_spec(a, act, bud, ytd, mon, mov, month, prior, scale, unit_label, places, kv, paragraph,
              nxt, company, gm_m, gm_y, gm_yb, em_m, em_y, em_yb, rev_y, eb_y, lab) -> Dict[str, Any]:
    mname, pname = v.month_name(month), v.month_name(prior)
    views = []
    t = mov["totals"] if mov else None
    cap = lab[0].upper() + lab[1:]

    def sgn(x: Decimal) -> str:
        s = mf.num(x, places)
        return ("+" + s) if x > 0 and s.strip("0.,") else s

    if mov:
        ch = t["ebitda"]["change"]
        title = (f"{mname} close: EBITDA {'up' if ch > 0 else 'down'} {mf.money(abs(ch))} on {pname}"
                 if ch else f"{mname} close: EBITDA unchanged on {pname}")
        # summary in the order of the bridge
        s = []
        rc = t["revenue"]["change"]
        if rc:
            s.append(f"Revenue {'rose' if rc > 0 else 'fell'} {mf.money(abs(rc))} to {kv(t['revenue']['current'])}.")
        cc = t["cogs"]["change"]
        if cc > 0 and rc > 0:
            s.append(f"Higher cost of revenue took back {mf.money(cc)} of it.")
        elif cc:
            s.append(f"Cost of revenue {'rose' if cc > 0 else 'fell'} {mf.money(abs(cc))}.")
        oc = t["opex"]["change"]
        if oc:
            s.append(f"Operating expenses {'rose' if oc > 0 else 'fell'} {mf.money(abs(oc))}.")
        em = t["ebitda_margin"]["current"]
        s.append(f"EBITDA ended at {kv(t['ebitda']['current'])}" + (f", a {mf.pct(em)} margin." if em is not None else "."))
        tiles = [tile("Revenue", kv(t["revenue"]["current"]), signed_pct(t["revenue"]["pct"]), t["revenue"]["change"])]
        if t["gross_margin"]["current"] is not None:
            tiles.append(tile("Gross margin", mf.pct(t["gross_margin"]["current"]), mf.pts(t["gross_margin"]["pts"]),
                              t["gross_margin"]["pts"]))
        tiles.append(tile("EBITDA", kv(t["ebitda"]["current"]), signed_pct(t["ebitda"]["pct"]), t["ebitda"]["change"]))
        if em is not None:
            tiles.append(tile("EBITDA margin", mf.pct(em), mf.pts(t["ebitda_margin"]["pts"]), t["ebitda_margin"]["pts"]))
        steps = [(r["line"], v.short_name(r["line"]), r["effect"]) for r in mov["rows"]]
        s0, rs, e0, plug = rounded_bridge(t["ebitda"]["prior"], steps, t["ebitda"]["current"], scale, places)
        bars = [{"label": v.short_label(prior)[:3], "value": jnum(s0), "total": True}]
        bars += [{"label": lab_, "short": short, "value": jnum(x)} for lab_, short, x in rs]
        bars.append({"label": v.short_label(month)[:3], "value": jnum(e0), "total": True})
        bridge = {"type": "bridge", "title": f"EBITDA, {pname} to {mname}", "subtitle": unit_label, "bars": bars}
        if plug:
            bridge["note"] = f"Rounding of {sgn(plug)} sits in the largest step."
        rows = []
        for r in mov["rows"]:
            rows.append({"cells": [r["line"], v.table_amount(r["prior"], scale), v.table_amount(r["current"], scale),
                                   sgn((r["effect"] / scale).quantize(Decimal(1).scaleb(-places)))],
                         "role": "highlight" if r["type"] == "revenue" else None})
        rows.append({"cells": ["EBITDA", v.table_amount(t["ebitda"]["prior"], scale), v.table_amount(t["ebitda"]["current"], scale),
                               sgn((t["ebitda"]["change"] / scale).quantize(Decimal(1).scaleb(-places)))], "role": "total"})
        table = {"type": "table", "title": "What moved",
                 "columns": [unit_label, v.SHORT[int(prior[5:7]) - 1], v.SHORT[int(month[5:7]) - 1],
                             {"label": "Effect on EBITDA", "tone": "sign"}], "rows": rows}
        views.append({"label": f"vs {pname}", "summary": " ".join(s), "tiles": tiles, "blocks": [bridge, table]})
    else:
        title = f"{mname} close: EBITDA {kv(mon['bottom']['actual'])}"

    # vs budget, year to date
    b = ytd["bottom"]
    per_y = ytd["period"]["label"]
    note = f"{per_y} vs {lab}"
    vt = [tile("Revenue", kv(rev_y["actual"]), signed_pct(rev_y["better_pct"]), rev_y["better"], note=note)]
    if gm_y is not None:
        x = (gm_y - gm_yb) * 100
        vt.append(tile("Gross margin", mf.pct(gm_y), mf.pts(x), x, note=note))
    vt.append(tile("EBITDA", kv(b["actual"]), signed_pct(b["better_pct"]), b["better"], note=note))
    if em_y is not None:
        x = (em_y - em_yb) * 100
        vt.append(tile("EBITDA margin", mf.pct(em_y), mf.pts(x), x, note=note))
    steps = [(r["line"], v.short_name(r["line"]), r["better"]) for r in ytd["leaves"]]
    s0, rs, e0, plug = rounded_bridge(b["budget"], steps, b["actual"], scale, places)
    bars = [{"label": cap, "short": "Budget", "value": jnum(s0), "total": True}]
    bars += [{"label": lab_, "short": short, "value": jnum(x)} for lab_, short, x in rs]
    bars.append({"label": "Actual", "value": jnum(e0), "total": True})
    ybridge = {"type": "bridge", "title": f"EBITDA, {lab} to actual, {per_y}", "subtitle": unit_label, "bars": bars}
    if plug:
        ybridge["note"] = f"Rounding of {sgn(plug)} sits in the largest step."
    roles = {"Gross profit": "subtotal", "Operating expenses": "subtotal", "Total revenue": "subtotal", "EBITDA": "total"}
    vrows = []
    for r in ytd["rows"]:
        vrows.append({"cells": [r["line"], v.table_amount(r["actual"], scale), v.table_amount(r["budget"], scale),
                                v.table_better(r["better"], scale), v.table_pct(r["better_pct"])],
                      "role": roles.get(r["line"]) if r["kind"] == "computed" else None})
    if gm_y is not None:
        vrows.append({"cells": ["Gross margin", mf.pct(gm_y), mf.pct(gm_yb), v.table_pts((gm_y - gm_yb) * 100), ""], "role": "ratio"})
    if em_y is not None:
        vrows.append({"cells": ["EBITDA margin", mf.pct(em_y), mf.pct(em_yb), v.table_pts((em_y - em_yb) * 100), ""], "role": "ratio"})
    vtable = {"type": "table", "title": f"{per_y} against {lab}",
              "columns": [unit_label, "Actual", cap, {"label": "Better/(worse)", "tone": "sign"}, {"label": "%", "tone": "sign"}],
              "rows": vrows}
    months = ytd["period"]["months"]
    am, bm = month_values(act, months), month_values(bud, months)
    q = Decimal(1).scaleb(-places)
    x_labels = [v.SHORT[int(m[5:7]) - 1] for m in months]
    line = {"type": "line", "title": "Revenue by month", "subtitle": unit_label, "x": x_labels,
            "series": [{"name": "Actual", "values": [jnum((x / scale).quantize(q)) for x in am["revenue"]]},
                       {"name": cap, "values": [jnum((x / scale).quantize(q)) for x in bm["revenue"]], "dashed": True}]}
    bar = {"type": "bar", "title": "EBITDA by month", "subtitle": unit_label, "x": x_labels,
           "series": [{"name": "Actual", "values": [jnum((x / scale).quantize(q)) for x in am["ebitda"]]},
                      {"name": cap, "values": [jnum((x / scale).quantize(q)) for x in bm["ebitda"]]}]}
    mb = mon["bottom"]
    vs = []
    if mb["diff"]:
        pc = f" ({v.pct_words(mb['pct'])})" if mb["pct"] is not None else ""
        vs.append(f"{mname} EBITDA is {kv(mb['actual'])}, {v.amt(abs(mb['diff']), mb['actual'])}{pc} "
                  f"{'above' if mb['diff'] > 0 else 'below'} {lab}.")
    if b["diff"]:
        pc = f" ({v.pct_words(b['pct'])})" if b["pct"] is not None else ""
        vs.append(f"Year to date, EBITDA is {kv(b['actual'])}, {v.amt(abs(b['diff']), b['actual'])}{pc} "
                  f"{'above' if b['diff'] > 0 else 'below'} {lab}.")
    ds = v.drivers_sentence(ytd)
    if ds:
        vs.append(ds.split(". ")[0].rstrip(".") + ".")
    blocks = [ybridge, vtable, line, bar]
    if nxt:
        blocks.append({"type": "text", "title": "Next step", "body": nxt[0].upper() + nxt[1:]})
    views.append({"label": "vs budget", "summary": " ".join(vs), "tiles": vt, "blocks": blocks})
    spec: Dict[str, Any] = {"title": title}
    if company:
        spec["eyebrow"] = company
    spec["views"] = views
    spec["footer"] = f"Made by the magnos board-pack skill from {act.name} and {bud.name} · {as_of_label(a.as_of)}"
    spec["source"] = {"skill": "board-pack", "files": [act.name, bud.name], "run": JSON_PATH.replace(os.sep, "/")}
    return spec


def log_movement(mov: Optional[Dict[str, Any]], scale: Decimal, unit_label: str, tool: str = "board-pack") -> None:
    """The month-on-month figures, with the table's own display, in the ledger."""
    if not mov:
        return
    per = f"{v.short_label(mov['month'])} vs {v.short_label(mov['prior'])}"
    u = f", {unit_label}" if unit_label != "$" else ""
    for r in mov["rows"]:
        for key in ("prior", "current", "change", "effect"):
            disp = v.table_better(r[key], scale) if key == "effect" else v.table_amount(r[key], scale)
            mf.ledger_append({"label": f"{r['line']} {key}, {per}{u}", "value": r[key], "display": disp, "tool": tool})
    for k, x in mov["totals"].items():
        for key, val in x.items():
            if val is None:
                continue
            e = {"label": f"{k} {key}, {per}", "value": val, "tool": tool}
            if k in ("revenue", "cogs", "opex", "gross_profit", "ebitda") and key in ("prior", "current", "change"):
                e["display"] = v.table_better(val, scale) if key == "change" else v.table_amount(val, scale)
            mf.ledger_append(e)


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(prog="board_pack.py", description="One page on the month: variance, movement, the lines that explain the gap, one next step.")
    ap.add_argument("actuals", help="P&L actuals by month (CSV, TSV or XLSX; wide or long)")
    ap.add_argument("budget", help="budget or forecast by month")
    ap.add_argument("--month", help="the month of the pack, like 2026-09 (default: the last month of actuals)")
    ap.add_argument("--company", help="company name for the title (default: 'company' in .magnos/finance.md)")
    ap.add_argument("--out", help="the Markdown file (default board_pack_<mon>.md)")
    ap.add_argument("--page-out", help="the page spec (default board_pack_<mon>_page.json)")
    ap.add_argument("--as-of", help="date for the page footer, like 2026-10-04 (default: today)")
    ap.add_argument("--line-type", action="append", default=[], metavar="FILE|LINE=TYPE",
                    help="set a line's type: revenue, cogs, opex, below or ignore")
    ap.add_argument("--version", help="budget version when the budget file holds several")
    ap.add_argument("--label", help="how to name the budget (default from the file: 'budget v3')")
    ap.add_argument("--unit", choices=["1", "K", "M"], help="table unit (default: $K from $100K)")
    ap.add_argument("--year", type=int, help="year for month columns that have none")
    ap.add_argument("--sheet", help="sheet name in an XLSX file")
    ap.add_argument("--json", default=JSON_PATH, help=f"where to save the machine result (default {JSON_PATH})")
    a = ap.parse_args(argv)
    try:
        r = build(a)
        mon_slug = v.SHORT[int(r["month"][5:7]) - 1].lower()
        md_path = a.out or f"board_pack_{mon_slug}.md"
        spec_path = a.page_out or f"board_pack_{mon_slug}_page.json"
        with open(inside(md_path), "w", encoding="utf-8") as fh:
            fh.write(r["markdown"] + "\n")
        with open(inside(spec_path), "w", encoding="utf-8") as fh:
            json.dump(r["spec"], fh, indent=2, ensure_ascii=False)
            fh.write("\n")
    except InputError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    v.log_figures(r["ytd"], "board-pack", r["scale"], r["unit_label"])
    v.log_figures(r["mon"], "board-pack", r["scale"], r["unit_label"])
    log_movement(r["mov"], r["scale"], r["unit_label"])
    for label, value, display in r["ratios"]:
        mf.ledger_append({"label": label, "value": value, "display": display, "tool": "board-pack"})
    tail = ["", f"Wrote {md_path} and {spec_path}. To make the page, run the page skill on {spec_path}."]
    notes = r["act"].notes + r["bud"].notes + r["ytd"]["notes"]
    tail += notes
    if not r["mov"]:
        tail.append(f"No actuals for {v.long_label(r['prior'])}, so the pack has no movement from the month before.")
    if r["profile"].get("_source") == "defaults":
        tail.append("Used the default finance profile: favourable variances positive, fiscal year from January. "
                    "Run /magnos:setup to set yours.")
    data = {
        "tool": "board-pack", "month": r["month"], "prior": r["prior"],
        "files": {"markdown": md_path, "page_spec": spec_path, "actuals": r["act"].name, "budget": r["bud"].name},
        "paragraph": r["paragraph"], "kpis": r["kpis"], "next_step": r["next_step"],
        "ytd": v.to_json(r["ytd"], r["act"], r["bud"], r["scale"], r["unit_label"], "favourable", "", r["profile"]),
        "month_variance": v.to_json(r["mon"], r["act"], r["bud"], r["scale"], r["unit_label"], "favourable", "", r["profile"]),
        "movement": v.jsonable(r["mov"]), "markdown": r["markdown"],
    }
    mf.emit(r["markdown"] + "\n" + "\n".join(tail), data, a.json)
    return 0


if __name__ == "__main__":
    sys.exit(main())
