#!/usr/bin/env python3
"""Render a self-contained CarSleuth HTML report from compact JSON.

The renderer owns layout and styling so the investigating model only writes
structured findings. All user-supplied strings are HTML-escaped.
"""

from __future__ import annotations

import argparse
import html
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


def esc(value: object) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def values(value: object) -> list:
    return value if isinstance(value, list) else []


def safe_url(value: object) -> str:
    raw = str(value or "").strip()
    parsed = urlparse(raw)
    return raw if parsed.scheme == "https" and parsed.netloc else ""


def validate_report(data: dict, mode: str) -> tuple[list[str], list[str]]:
    """Return fatal schema errors and non-fatal quality warnings."""
    errors: list[str] = []
    warnings: list[str] = []
    vehicle = data.get("vehicle") if isinstance(data.get("vehicle"), dict) else {}
    verdict = data.get("verdict") if isinstance(data.get("verdict"), dict) else {}
    dealer = data.get("dealer") if isinstance(data.get("dealer"), dict) else {}
    sections = [item for item in values(data.get("sections")) if isinstance(item, dict)]

    if not vehicle.get("title"):
        errors.append("vehicle.title is required")
    for field in ("label", "confidence", "summary"):
        if not verdict.get(field):
            errors.append(f"verdict.{field} is required")
    try:
        score = float(verdict.get("score"))
        if not 0 <= score <= 100:
            raise ValueError
    except (TypeError, ValueError):
        errors.append("verdict.score must be a number from 0 to 100")
    if len(values(verdict.get("metrics"))) != 4:
        errors.append("verdict.metrics must contain exactly four items")
    for field in ("name", "risk", "note"):
        if not dealer.get(field):
            errors.append(f"dealer.{field} is required")

    lower, upper = (8, 12) if mode == "standard" else (8, 16)
    if not lower <= len(sections) <= upper:
        errors.append(f"{mode} mode requires {lower}–{upper} sections; found {len(sections)}")

    section_types = {str(section.get("type", "prose")).lower() for section in sections}
    for required in ("scorebars", "numbered", "questions", "sources"):
        if required not in section_types:
            errors.append(f"a {required} section is required")

    source_sections = [section for section in sections if str(section.get("type", "")).lower() == "sources"]
    source_items = values(source_sections[-1].get("items")) if source_sections else []
    source_lower, source_upper = (5, 10) if mode == "standard" else (10, 18)
    if not source_lower <= len(source_items) <= source_upper:
        errors.append(
            f"{mode} mode requires {source_lower}–{source_upper} sources; found {len(source_items)}"
        )
    for index, item in enumerate(source_items, start=1):
        url = item.get("url") if isinstance(item, dict) else ""
        if not safe_url(url):
            errors.append(f"source {index} must use a valid HTTPS URL")
            continue
        parsed = urlparse(str(url))
        if parsed.path in {"", "/"} and not parsed.query:
            warnings.append(f"source {index} is a homepage; prefer a claim-specific page")

    return errors, warnings


def status_class(value: object) -> str:
    key = str(value or "").lower()
    if "verif" in key or key in {"a", "confirmed"}:
        return "verified"
    if "claim" in key or "seller" in key:
        return "claim"
    if "risk" in key or "warning" in key:
        return "risk"
    return "unknown"


def heading(section: dict) -> str:
    title = esc(section.get("title", ""))
    lede = section.get("lede")
    out = [f'<section class="section"><h2>{title}</h2>']
    if lede:
        out.append(f'<p class="lede">{esc(lede)}</p>')
    return "".join(out)


def note(section: dict) -> str:
    value = section.get("note")
    return f'<p class="note">{esc(value)}</p>' if value else ""


def render_bullets(section: dict, numbered: bool = False) -> str:
    tag = "ol" if numbered else "ul"
    klass = "number-list" if numbered else "bullet-list"
    items = "".join(f"<li>{esc(item)}</li>" for item in values(section.get("items")))
    return f'{heading(section)}<{tag} class="{klass}">{items}</{tag}>{note(section)}</section>'


def render_specs(section: dict) -> str:
    items = []
    for item in values(section.get("items")):
        if not isinstance(item, dict):
            continue
        status = item.get("status")
        badge = ""
        if status:
            badge = f'<span class="tag tag-{status_class(status)}">{esc(status)}</span>'
        items.append(
            '<div class="spec">'
            f'<div class="spec-label">{esc(item.get("label"))}</div>'
            f'<div class="spec-value">{esc(item.get("value"))}{badge}</div>'
            "</div>"
        )
    return f'{heading(section)}<div class="spec-grid">{"".join(items)}</div>{note(section)}</section>'


def render_risks(section: dict) -> str:
    cards = []
    for item in values(section.get("items")):
        if not isinstance(item, dict):
            continue
        severity = item.get("severity")
        evidence = item.get("evidence")
        sev = f'<span class="severity">Severity {esc(severity)}</span>' if severity not in (None, "") else ""
        ev = f'<span class="evidence">Evidence {esc(evidence)}</span>' if evidence else ""
        cards.append(
            '<article class="risk-card">'
            f'<div class="risk-head">{sev}<span class="risk-title">{esc(item.get("title"))}</span>{ev}</div>'
            f'<div class="risk-body">{esc(item.get("body"))}</div>'
            "</article>"
        )
    score = section.get("score")
    score_note = f'<div class="callout">{esc(score)}</div>' if score else ""
    return f'{heading(section)}{"".join(cards)}{score_note}{note(section)}</section>'


def render_table(section: dict) -> str:
    columns = [str(x) for x in values(section.get("columns"))]
    head = "".join(f"<th>{esc(column)}</th>" for column in columns)
    body_rows = []
    for row in values(section.get("rows")):
        if isinstance(row, dict):
            cells = [row.get(column, row.get(str(index), "")) for index, column in enumerate(columns)]
        elif isinstance(row, list):
            cells = row
        else:
            continue
        padded = list(cells) + [""] * max(0, len(columns) - len(cells))
        body_rows.append("<tr>" + "".join(f"<td>{esc(cell)}</td>" for cell in padded[: len(columns)]) + "</tr>")
    return (
        f'{heading(section)}<div class="table-wrap"><table><thead><tr>{head}</tr></thead>'
        f'<tbody>{"".join(body_rows)}</tbody></table></div>{note(section)}</section>'
    )


def render_scores(section: dict) -> str:
    rows = []
    for item in values(section.get("items")):
        if not isinstance(item, dict):
            continue
        try:
            score = float(item.get("score", 0))
            maximum = float(item.get("max", 1))
        except (TypeError, ValueError):
            score, maximum = 0.0, 1.0
        maximum = maximum if maximum > 0 else 1.0
        pct = max(0.0, min(100.0, score / maximum * 100))
        shown_score = int(score) if score.is_integer() else score
        shown_max = int(maximum) if maximum.is_integer() else maximum
        rows.append(
            '<div class="score-row">'
            f'<div class="score-label">{esc(item.get("label"))}</div>'
            f'<div class="bar"><div class="bar-fill" style="width:{pct:.1f}%"></div></div>'
            f'<div class="score-points mono">{esc(shown_score)}/{esc(shown_max)}</div>'
            "</div>"
        )
    chips = []
    if section.get("subtotal"):
        chips.append(f'<span class="chip">Subtotal {esc(section["subtotal"])}</span>')
    if section.get("penalty"):
        chips.append(f'<span class="chip chip-penalty">{esc(section["penalty"])}</span>')
    if section.get("final"):
        chips.append(f'<span class="chip chip-final">Final {esc(section["final"])}</span>')
    return (
        f'{heading(section)}<div class="score-bars">{"".join(rows)}</div>'
        f'<div class="chips">{"".join(chips)}</div>{note(section)}</section>'
    )


def render_tiles(section: dict) -> str:
    items = []
    for item in values(section.get("items")):
        if not isinstance(item, dict):
            continue
        items.append(
            '<div class="tile">'
            f'<div class="tile-label">{esc(item.get("label"))}</div>'
            f'<div class="tile-value">{esc(item.get("value"))}</div>'
            "</div>"
        )
    return f'{heading(section)}<div class="tiles">{"".join(items)}</div>{note(section)}</section>'


def render_callout(section: dict) -> str:
    style = str(section.get("style", "info")).lower()
    klass = "callout-danger" if style == "danger" else "callout-warn" if style == "warn" else ""
    return f'{heading(section)}<div class="callout {klass}">{esc(section.get("body"))}</div>{note(section)}</section>'


def render_sources(section: dict) -> str:
    items = []
    for item in values(section.get("items")):
        if not isinstance(item, dict):
            continue
        url = safe_url(item.get("url"))
        title = esc(item.get("title") or url or "Source")
        label = f'<a href="{esc(url)}" target="_blank" rel="noreferrer">{title}</a>' if url else title
        items.append(
            '<div class="source">'
            f'<div>{label}</div><div class="source-note">{esc(item.get("note"))}</div>'
            "</div>"
        )
    return f'{heading(section)}<div class="source-list">{"".join(items)}</div>{note(section)}</section>'


def render_prose(section: dict) -> str:
    paragraphs = section.get("paragraphs")
    if not isinstance(paragraphs, list):
        paragraphs = [section.get("body", "")]
    body = "".join(f'<p class="lede">{esc(paragraph)}</p>' for paragraph in paragraphs if paragraph)
    return f"{heading(section)}{body}{note(section)}</section>"


def render_section(section: object) -> str:
    if not isinstance(section, dict):
        return ""
    section_type = str(section.get("type", "prose")).lower()
    if section_type in {"bullets", "questions"}:
        return render_bullets(section)
    if section_type == "numbered":
        return render_bullets(section, numbered=True)
    if section_type == "specs":
        return render_specs(section)
    if section_type == "risks":
        return render_risks(section)
    if section_type == "table":
        return render_table(section)
    if section_type == "scorebars":
        return render_scores(section)
    if section_type == "tiles":
        return render_tiles(section)
    if section_type == "callout":
        return render_callout(section)
    if section_type == "sources":
        return render_sources(section)
    return render_prose(section)


def render_hero(data: dict) -> str:
    vehicle = data.get("vehicle") if isinstance(data.get("vehicle"), dict) else {}
    verdict = data.get("verdict") if isinstance(data.get("verdict"), dict) else {}
    title = vehicle.get("title") or data.get("title") or "Used Car Investigation"
    meta = "".join(f"<span>{esc(item)}</span>" for item in values(vehicle.get("meta")))
    try:
        score = max(0.0, min(100.0, float(verdict.get("score", 0))))
    except (TypeError, ValueError):
        score = 0.0
    circumference = 150.8
    dash = circumference * score / 100
    score_shown = int(score) if score.is_integer() else score
    metrics = []
    for item in values(verdict.get("metrics"))[:4]:
        if not isinstance(item, dict):
            continue
        metrics.append(
            '<div class="metric">'
            f'<div class="metric-label">{esc(item.get("label"))}</div>'
            f'<div class="metric-value">{esc(item.get("value"))}</div>'
            "</div>"
        )
    return (
        f'<header><h1>{esc(title)}</h1><div class="meta">{meta}</div></header>'
        '<section class="hero">'
        '<div class="hero-banner"><div>'
        f'<div class="verdict">{esc(verdict.get("label", "REVIEW"))}</div>'
        f'<div class="confidence">Confidence: {esc(verdict.get("confidence", "Unknown"))}</div></div>'
        '<div class="score-ring"><svg viewBox="0 0 58 58">'
        '<circle class="score-track" cx="29" cy="29" r="24"></circle>'
        f'<circle class="score-fill" cx="29" cy="29" r="24" stroke-dasharray="{dash:.2f} {circumference:.2f}"></circle>'
        f'</svg><div class="score-number mono">{esc(score_shown)}</div></div></div>'
        f'<div class="metrics">{"".join(metrics)}</div>'
        f'<div class="hero-summary">{esc(verdict.get("summary"))}</div></section>'
    )


def render_dealer(data: dict) -> str:
    dealer = data.get("dealer")
    if not isinstance(dealer, dict) or not dealer:
        return ""
    return (
        '<section class="dealer">'
        f'<div class="dealer-grade mono">{esc(dealer.get("grade", "—"))}</div>'
        '<div>'
        f'<div class="dealer-name">{esc(dealer.get("name"))}</div>'
        f'<div class="dealer-risk">Dealer risk: {esc(dealer.get("risk", "Unknown"))}</div>'
        f'<div class="dealer-note">{esc(dealer.get("note"))}</div>'
        "</div></section>"
    )


def render(data: dict, template: str) -> str:
    vehicle = data.get("vehicle") if isinstance(data.get("vehicle"), dict) else {}
    page_title = str(data.get("page_title") or vehicle.get("title") or "CarSleuth Report")
    body = render_hero(data) + render_dealer(data)
    body += "".join(render_section(section) for section in values(data.get("sections")))
    generated = data.get("generated") or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return (
        template.replace("{{TITLE}}", esc(page_title))
        .replace("{{BODY}}", body)
        .replace("{{GENERATED}}", esc(generated))
    )


def load_json(path: str) -> dict:
    if path == "-":
        raw = sys.stdin.read()
    else:
        raw = Path(path).read_text(encoding="utf-8")
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("Report JSON must be an object.")
    return data


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", "-i", default="-", help="JSON file path, or - for stdin")
    parser.add_argument("--output", "-o", required=True, help="Destination HTML path")
    parser.add_argument("--template", help="Optional template override")
    parser.add_argument("--mode", choices=("standard", "deep"), default="standard")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    template_path = Path(args.template) if args.template else script_dir.parent / "assets" / "report-template.html"
    template = template_path.read_text(encoding="utf-8")
    data = load_json(args.input)
    errors, warnings = validate_report(data, args.mode)
    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)
    if errors:
        parser.error("report validation failed:\n- " + "\n- ".join(errors))
    output = Path(args.output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render(data, template), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
