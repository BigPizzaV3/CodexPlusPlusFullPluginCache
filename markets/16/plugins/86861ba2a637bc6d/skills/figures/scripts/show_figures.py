#!/usr/bin/env python3
"""List every figure of the last answer with its source: ✓ traced, ✕ not traced.

Reads .magnos/figures.json, which the plugin's Stop hook writes after each
answer in Claude Code and Codex. Where there is no hook, check an answer here:

  python3 scripts/show_figures.py                                   the last check
  python3 scripts/show_figures.py --text answer.txt --evidence tb_sep.csv calc_out.txt --ledger

In --text mode the evidence is: CSV, TSV and XLSX files as read (a figure
needs three significant digits to match a raw file), other files as computed
output, and with --ledger the calculator's ledger (.magnos/ledger.jsonl). The
result is saved to .magnos/figures.json, as the hook does.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
from decimal import Decimal
from typing import Any, Dict, List, Optional

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import magnos_fin as mf  # noqa: E402

NOT_FOUND = "not found in any file or calculation"


def fail(msg: str) -> None:
    print(msg, file=sys.stderr)
    sys.exit(2)


def build_evidence(paths: List[str], use_ledger: bool, cwd: str) -> mf.Evidence:
    ev = mf.Evidence()
    for p in paths:
        if not os.path.isfile(p):
            fail(f"Evidence file {p} does not exist; name files in the working folder.")
        name = os.path.basename(p)
        low = p.lower()
        if low.endswith((".xlsx", ".xlsm")):
            wb = mf.read_xlsx(p)
            for sheet in wb.sheet_names:
                for ref, c in wb.cells(sheet).items():
                    src = f"{name} · {sheet}!{ref}"
                    if isinstance(c.value, Decimal):
                        ev.add_value(c.value, src, strong=False)
                    elif isinstance(c.value, str) and c.value.strip():
                        ev.add_text(c.value, src, strong=False)
        elif low.endswith((".csv", ".tsv")):
            t = mf.read_table(p)
            for i, row in enumerate(t.rows, start=2):
                for col in t.columns:
                    v = str(row.get(col, "")).strip()
                    if not v:
                        continue
                    src = f"{name} · {col}, row {i}"
                    d = mf.to_decimal(v)
                    if d is not None:
                        ev.add_value(d, src, strong=False)
                    else:
                        ev.add_text(v, src, strong=False)
        else:  # script output, notes, the person's message: computed or stated
            with open(p, encoding="utf-8", errors="replace") as fh:
                ev.add_text(fh.read(), name, strong=True)
    if use_ledger:
        for e in mf.ledger_read(cwd):
            src = f"calc · {e.get('formula') or e.get('label', '')}"
            ev.add_value(e.get("value"), src)
            ev.add_text(str(e.get("display", "")), src)
    return ev


def run_check(text: str, ev: mf.Evidence) -> Dict[str, Any]:
    traces = mf.trace_figures(text, ev)
    rep = mf.figures_report(traces)
    for fig, t in zip(rep["figures"], traces):
        s = t.figure.start
        a, b = max(0, s - 60), min(len(text), s + len(t.figure.raw) + 40)
        while 0 < a < s and not text[a - 1].isspace():  # start and end on whole words
            a += 1
        while s + len(t.figure.raw) < b < len(text) and not text[b].isspace():
            b -= 1
        fig["context"] = text[a:b].replace("\n", " ").strip()
    rep["checked_at"] = _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")
    rep["session_id"] = ""
    rep["answer_excerpt"] = text[:300]
    rep["checked_by"] = "figures skill"
    return rep


def when(iso: str) -> str:
    try:
        d = _dt.datetime.fromisoformat(str(iso).replace("Z", "+00:00"))
    except ValueError:
        return ""
    if d.tzinfo is not None:
        d = d.astimezone(_dt.timezone.utc)
        return d.strftime("%Y-%m-%d %H:%M UTC")
    return d.strftime("%Y-%m-%d %H:%M")


def render(rep: Dict[str, Any]) -> str:
    figs: List[Dict[str, Any]] = list(rep.get("figures") or [])
    total = int(rep.get("total", len(figs)))
    traced = int(rep.get("traced", sum(1 for f in figs if f.get("traced"))))
    untraced = total - traced
    if total == 0:
        return "The last answer has no figures to check."
    if untraced == 0:
        head = f"All {total} figures in the last answer are traced to a file or a calculation."
    else:
        head = (f"{traced} of {total} figures in the last answer are traced; "
                f"{untraced} {'is' if untraced == 1 else 'are'} not.")
    lines = [head]
    stamp = when(rep.get("checked_at", ""))
    if stamp:
        lines.append(f"Checked {stamp}.")
    lines.append("")
    for f in figs:
        ok = bool(f.get("traced"))
        lines.append(f"{'✓' if ok else '✕'} {f.get('raw', '')}  {f.get('source') or (NOT_FOUND if not ok else '')}".rstrip())
        if not ok and f.get("context"):
            lines.append(f"   in: “…{f['context']}…”")
    lines.append("")
    summary = f"{total} figures · {traced} traced"
    if untraced:
        summary += f" · {untraced} not traced"
    lines.append(summary)
    return "\n".join(lines)


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="List the figures of the last answer with their sources.")
    p.add_argument("--text", help="check this answer instead of reading the last check ('-' reads stdin)")
    p.add_argument("--evidence", nargs="*", default=[], help="files the figures may come from")
    p.add_argument("--ledger", action="store_true", help="also trace to the calculator's ledger")
    p.add_argument("--file", default=os.path.join(".magnos", "figures.json"), help="the last check (default .magnos/figures.json)")
    p.add_argument("--no-save", action="store_true", help="in --text mode, do not write .magnos/figures.json")
    p.add_argument("--strict", action="store_true", help="exit 1 when a figure is not traced")
    a = p.parse_args(argv)
    cwd = os.getcwd()

    if a.text:
        if a.text == "-":
            text = sys.stdin.read()
        else:
            if not os.path.isfile(a.text):
                fail(f"{a.text} does not exist; save the answer to a text file and pass its path.")
            with open(a.text, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        rep = run_check(text, build_evidence(a.evidence, a.ledger, cwd))
        if not a.no_save:
            path = os.path.join(cwd, a.file)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(rep, fh, indent=2, ensure_ascii=False)
    else:
        path = os.path.join(cwd, a.file)
        if not os.path.exists(path):
            fail("No figure check yet: .magnos/figures.json does not exist. In Claude Code and Codex the Magnos "
                 "Stop hook writes it after an answer with figures; elsewhere run show_figures.py --text answer.txt "
                 "--evidence <files> --ledger.")
        try:
            with open(path, encoding="utf-8") as fh:
                rep = json.load(fh)
        except ValueError:
            fail(f"{a.file} is not valid JSON; run the check again to rewrite it.")
    mf.emit(render(rep), rep, os.path.join(cwd, ".magnos", "runs", "figures.json"))
    return 1 if a.strict and int(rep.get("untraced", 0)) else 0


if __name__ == "__main__":
    sys.exit(main())
