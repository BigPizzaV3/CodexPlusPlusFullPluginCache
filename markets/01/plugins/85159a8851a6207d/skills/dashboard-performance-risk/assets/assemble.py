#!/usr/bin/env python3
"""Assemble an MSCI IndexAI dashboard from the shared, dashboard-agnostic shell.

EVERY dashboard MUST be built through this so the header/logo, Refresh (with live date
resolution), disclaimers (sample + AI + compliance + verbatim Notice), brand, and responsive
layout are identical and current across all dashboards. The dashboard author only supplies the
dashboard-SPECIFIC parts: title, subtitle, as-of label, body HTML, the refresh CALLS, and the
render(payload) body. The common chrome is never hand-authored per dashboard.

Each refresh call is { "key", "tool", "args" } where tool is "fetch_index_data" or
"fetch_index_timeseries" and args is that tool's input object. The as-of date + range control fills
three placeholders inside args at update time: "<DATE>" and "<END>" -> the as-of date (live-resolved
latest business date, or the date the user picks), and "<START>" -> the range start computed from
that date and the selected range. (The parameter is still named `queries` and the shell slot
`__QUERIES_JSON__` for backward compatibility; it now carries call specs.)

Usage (from the skill, with cwd = the skill folder):

    from assets.assemble import assemble  # or import by path
    assemble(
        out_path="/mnt/user-data/outputs/<name>.html",
        title="Index & Security Analyzer",
        subtitle="Index tab + Security tab — one dashboard",
        asof_label="Data via MSCI MCP · GRTR · USD · as-of 2026-06-15 · 1Y",
        snapshot_date="20260615",
        body_html="<div class='panelwrap'>…dashboard-specific views…</div>",
        queries=[{"key":"perf","tool":"fetch_index_data",
                  "args":{"codes":["990100"],"date":"<DATE>","variant":"GRTR",
                          "datapoints":["equity_index.performance.period_returns.period",
                                        "equity_index.performance.period_returns.returns"],"page_size":20}}],
        render_body="/* JS: read payload.perf.list_tables …, update the DOM in place */",
        approx=False,   # True only if an off-spec/methodology-sensitive metric is shown
        extra_disclaimers=None,  # list[str]; a datapoint-mandated block (e.g. the Index Inclusion
                                  # Module 9-point disclaimer used by §5), rendered verbatim and
                                  # separate from the approx block. Omit/None when not applicable.
    )
"""
import html, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
SHELL = HERE / "dashboard-shell.html"
NOTICE = HERE / "disclaimer-notice.txt"
LOGO = HERE / "logos" / "msci-logo-white.svg"

APPROX_HTML = ('<div class="approx">Note: This calculation is an approximation generated outside of '
  "MSCI's official index methodology framework. MSCI-methodology-aligned risk and performance analytics "
  "will be available through the MSCI connector in a future release. This output should not be interpreted "
  'as an MSCI-endorsed metric</div>')

def _extra_disclaimers_html(extra_disclaimers):
    # Datapoint-mandated disclaimers (e.g. the Index Inclusion Module block) — rendered verbatim,
    # one per supplied string, kept separate from the approximation block above.
    return "".join(f'<div class="extra">{html.escape(d)}</div>' for d in (extra_disclaimers or []))

def _notice_html():
    paras = [p.strip() for p in NOTICE.read_text(encoding="utf-8").split("\n\n") if p.strip()]
    body = [p for p in paras if p.lower() != "notice and disclaimer"]   # drop the title line
    return "".join(f"<p>{html.escape(p)}</p>" for p in body), len(body)

def _logo_html():
    svg = re.search(r"<svg.*?</svg>", LOGO.read_text(encoding="utf-8"), re.S).group(0)
    return re.sub(r"<svg ", '<svg class="logo" ', svg, count=1)

def assemble(out_path, title, subtitle, asof_label, snapshot_date,
             body_html, queries, render_body, approx=False, extra_disclaimers=None):
    shell = SHELL.read_text(encoding="utf-8")
    # Strip the shell's own leading documentation comment (it lists slot names like __TITLE__ in
    # plain text for humans reading the raw template) BEFORE doing replacements below — otherwise
    # the blind string-replace also matches those literal mentions and duplicates the entire
    # header/logo/body/notice/JS payload inside that HTML comment in every assembled dashboard.
    shell = re.sub(r"<!--\s*MSCI IndexAI DASHBOARD SHELL.*?-->\n?", "", shell, count=1, flags=re.S)
    notice_html, n = _notice_html()
    extra_html = _extra_disclaimers_html(extra_disclaimers)
    repl = {
        "__TITLE__": title,
        "__SUBTITLE__": subtitle,
        "__ASOF__": asof_label,
        "__SNAPSHOT_DATE__": snapshot_date,
        "__MSCI_LOGO__": _logo_html(),
        "__DASHBOARD_BODY__": body_html,
        "__FULL_NOTICE__": notice_html,
        "__EXTRA_DISCLAIMERS__": extra_html,
        "__APPROX_DISCLAIMER__": APPROX_HTML if approx else "",
        "__QUERIES_JSON__": json.dumps(queries),
        "__RENDER_BODY__": render_body,
    }
    for k, v in repl.items():
        shell = shell.replace(k, v)
    # fail loudly if any slot was left unfilled
    leftover = re.findall(r"__[A-Z_]+__", shell)
    if leftover:
        raise SystemExit(f"Unfilled shell slots: {sorted(set(leftover))}")
    pathlib.Path(out_path).write_text(shell, encoding="utf-8")
    # post-build verification: every common element is present
    checks = {
        "viewport": 'name="viewport"' in shell,
        "brand var (smokey)": "#0626A9" in shell,
        "white logo": 'class="logo"' in shell,
        "refresh button": 'id="refreshBtn"' in shell,
        "date resolution": "resolveLatestDate" in shell,
        "responsive kpis": "repeat(auto-fit,minmax(84px,1fr))" in shell,
        "sample disclaimer": "is not maintained as a deliverable" in shell,
        "AI disclaimer": "AI-generated. This dashboard was assembled" in shell,
        "compliance line": "For informational purposes only" in shell,
        f"verbatim notice ({n} paras)": notice_html in shell and n >= 14,
        "approx only when asked": (("approx" in shell) == bool(approx)) or (not approx),
        "extra disclaimers round-trip": (not extra_disclaimers) or all(
            html.escape(d) in shell for d in extra_disclaimers
        ),
        "no doc-comment duplication": "DASHBOARD SHELL" not in shell and shell.count(_logo_html()) == 1,
    }
    missing = [k for k, ok in checks.items() if not ok]
    if missing:
        raise SystemExit(f"Common-chrome check FAILED: {missing}")
    return out_path, checks

if __name__ == "__main__":
    # self-test: assemble a tiny dummy dashboard and confirm all common chrome is present
    out, checks = assemble(
        out_path="/tmp/_shell_selftest.html",
        title="Self Test", subtitle="shell assembly check",
        asof_label="Data via MSCI MCP · as-of 2026-06-15", snapshot_date="20260615",
        body_html='<div class="panelwrap"><div class="kpis"><div class="kpi"><div class="l">YTD</div><div class="v pos">6.60%</div></div></div></div>',
        queries=[{"key":"perf","tool":"fetch_index_data","args":{"codes":["990100"],"date":"<DATE>","variant":"GRTR","datapoints":["equity_index.performance.period_returns.period","equity_index.performance.period_returns.returns"],"page_size":20}}],
        render_body="try{var a=payload;}catch(e){}",
        approx=False,
        extra_disclaimers=["Self-test datapoint-mandated disclaimer — line 1.\nLine 2 of the same block."],
    )
    for k, ok in checks.items():
        print(("  OK  " if ok else "  XX  ") + k)
    print("assembled:", out)
