#!/usr/bin/env python3
"""Render a validated ROGNALIA Location Diagnosis Mini report as self-contained HTML."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import math
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlsplit, urlunsplit

from validate_report import EMOJI_RE, RATING_LABELS, ValidationError, validate_report


SKILL_DIR = Path(__file__).resolve().parent.parent
ASSET_DIR = SKILL_DIR / "assets"
TEMPLATE_PATH = ASSET_DIR / "report-template.html"
ICONS_PATH = ASSET_DIR / "report-icons.svg"
WORDMARK_PATH = ASSET_DIR / "rognalia-wordmark.svg"
QR_PATH = ASSET_DIR / "location-intelligence-qr.svg"

WORDMARK_SHA256 = "ab869c820b535640369c2a5622be60ea8dd0a1fcd699312a2aa660e7715253df"
QR_SHA256 = "6c61e0ce5d36191127297bf3b02782f0eaa0aa173bf874fb6dfd52dc7d74bebd"
ICONS_SHA256 = "af19f7dc40c5adcc1f2ef911a029680c7d0dd4f5ec15aa012921abda4dd7d3d8"
TEMPLATE_SHA256 = "f80556916b4c6fbf8d92cc53634a123240d901ebb715dc4c3f10d6254089a4f7"

FIXED_PAGE_TITLES = (
    "初期スクリーニング判定",
    "判定を支える要因と、判定を抑える要因",
    "需要の土台 — 範囲と時点の異なる4系列",
    "8つの調査軸 — 事実と判断への含意",
    "業態適合 — 人の流れを需要へつなぐ",
    "競合と相乗 — 役割の重なりと分け方",
    "判定が変わる条件と、次に取るべき検証",
    "判断に使った公開情報と調査範囲",
)

DISCLAIMER = (
    "本レポートは、AIを用いて調査日時点の公開Web情報を整理した初期スクリーニングです。"
    "実際の物件条件、受入・提供能力、店舗オペレーションによって評価は変わります。"
    "出店可否、売上・収益を保証しません。現地確認と追加調査を踏まえ、最終判断は必ず人が行ってください。"
)
CTA_URL = "https://rognalia.com/location-intelligence/"
SOURCES_PER_PAGE = 16
RISK_PAGE_THRESHOLD = 3
BASELINE_DENSE_METRIC_THRESHOLD = 12

STATUS_LABELS = {
    "confirmed": "確認済み",
    "estimated": "推定",
    "reference": "参考情報",
    "not_found": "公開情報では確認できず",
    "field_check": "現地・資料確認",
}
STATUS_CLASSES = {
    "confirmed": "is-confirmed",
    "estimated": "is-estimated",
    "reference": "is-reference",
    "not_found": "is-notfound",
    "field_check": "is-fieldcheck",
}
ACQUISITION_CLASSES = {
    "取得済み": "is-confirmed",
    "上位地域で代替": "is-proxy",
    "地点照合が必要": "is-fieldcheck",
    "一部未取得": "is-partial",
    "初期診断では未取得": "is-notfound",
    "対象外": "is-reference",
}
CONFIDENCE_LABELS = {"high": "高", "medium": "中", "low": "低"}
CONFIDENCE_ORDER = ("low", "medium", "high")


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def normalize_wordmark_accessibility(svg: str) -> str:
    """Keep the canonical traced paths while removing production-note alt copy."""
    svg = svg.replace('aria-labelledby="title desc"', 'aria-labelledby="title"', 1)
    svg = re.sub(
        r'<title id="title">.*?</title>',
        '<title id="title">ROGNALIA</title>',
        svg,
        count=1,
        flags=re.DOTALL,
    )
    return re.sub(r'\s*<desc id="desc">.*?</desc>', "", svg, count=1, flags=re.DOTALL)


def verified_text_asset(path: Path, expected_sha256: str, label: str) -> str:
    """Read a canonical UTF-8 asset and reject substitutions before rendering."""
    try:
        payload = path.read_bytes()
    except OSError as exc:
        raise ValidationError(f"{label}: canonical assetを読めません: {exc}") from exc
    actual_sha256 = hashlib.sha256(payload).hexdigest()
    if actual_sha256 != expected_sha256:
        raise ValidationError(
            f"{label}: canonical assetのSHA-256が一致しません "
            f"({actual_sha256} != {expected_sha256})"
        )
    try:
        return payload.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValidationError(f"{label}: canonical assetがUTF-8ではありません") from exc


def canonical_wordmark() -> str:
    return normalize_wordmark_accessibility(
        verified_text_asset(WORDMARK_PATH, WORDMARK_SHA256, "wordmark")
    )


def canonical_qr() -> str:
    return verified_text_asset(QR_PATH, QR_SHA256, "closing QR")


def canonical_template() -> str:
    return verified_text_asset(TEMPLATE_PATH, TEMPLATE_SHA256, "report template")


def canonical_icons() -> str:
    return verified_text_asset(ICONS_PATH, ICONS_SHA256, "report icons")


def icon(name: str, class_name: str = "icon") -> str:
    return (
        f'<svg class="{esc(class_name)}" aria-hidden="true" focusable="false">'
        f'<use href="#i-{esc(name)}"/></svg>'
    )


def refs(ids: Iterable[str]) -> str:
    values = list(ids)
    if not values:
        return ""
    return f'<span class="src">{esc("・".join(values))}</span>'


def status_chip(status: str) -> str:
    return (
        f'<span class="st {STATUS_CLASSES[status]}">'
        f'{icon("source", "sy")}{esc(STATUS_LABELS[status])}</span>'
    )


def acquisition_chip(status: str) -> str:
    return f'<span class="acq {ACQUISITION_CLASSES[status]}">{esc(status)}</span>'


def short(value: str, limit: int) -> str:
    value = value.strip()
    if len(value) <= limit:
        return value
    return value[: max(1, limit - 1)].rstrip() + "…"


def first_sentence(value: str, limit: int = 92) -> str:
    sentence = value.strip().split("。", 1)[0].strip()
    if sentence and len(sentence) <= limit:
        return sentence + "。"
    return short(value.strip(), limit)


def japanese_date(value: str) -> str:
    parsed = date.fromisoformat(value)
    return f"{parsed.year}年{parsed.month}月{parsed.day}日"


def page_shell(
    *,
    number: int,
    total: int,
    section_label: str,
    kicker: str,
    title: str,
    lead: str,
    scope: str,
    body: str,
    wordmark_svg: str,
    extra_class: str = "",
) -> str:
    classes = f"sheet report-page {extra_class}".strip()
    lead_markup = f'<p class="lead">{esc(lead)}</p>' if lead else ""
    return f"""
<section class="{classes}" data-page="{number}" aria-label="{esc(section_label)}">
  <div class="tk tk-tl"></div><div class="tk tk-tr"></div><div class="tk tk-bl"></div><div class="tk tk-br"></div>
  <header class="hd">
    <span class="hd-l"><span class="header-wordmark" aria-label="ROGNALIA">{wordmark_svg}</span><span class="hd-sep">|</span><span>立地診断 mini</span></span>
    <span class="hd-r">{esc(scope)}<b>{esc(section_label)}</b></span>
  </header>
  <p class="kick">{esc(kicker)}</p>
  <h1 class="pt">{esc(title)}</h1>
  {lead_markup}
  <main class="page-content">{body}</main>
  <footer class="ft">
    <p class="disc">{esc(DISCLAIMER)}</p>
    <div class="meta">
      <span class="fl"><span class="footer-wordmark" aria-label="ROGNALIA">{wordmark_svg}</span><span>立地診断 mini</span></span>
      <span class="pg"><b>{number}</b> / {total}</span>
    </div>
  </footer>
</section>"""


def block_heading(label: str, title: str = "", note: str = "") -> str:
    title_markup = f'<span class="t">{esc(title)}</span>' if title else ""
    note_markup = f'<span class="note">{esc(note)}</span>' if note else ""
    return f'<div class="blk-h"><span class="no">{esc(label)}</span>{title_markup}{note_markup}</div>'


def evidence_row(item: dict[str, Any]) -> str:
    return (
        '<div class="ev">'
        f'<p class="et">{esc(item["title"])}</p>'
        f'<p class="ed">{esc(item["detail"])}</p>'
        f'<div class="em">{status_chip(item["status"])}{refs(item["source_ids"])}</div>'
        "</div>"
    )


def render_toc(has_risk_page: bool) -> str:
    entries = [
        ("01", "判定"),
        ("02", "論拠"),
        ("03", "基礎数値"),
        ("04", "調査軸"),
        ("05", "業態適合"),
        ("06", "競合・相乗"),
    ]
    if has_risk_page:
        entries.append(("07", "反証監査"))
        entries.append(("08", "検証計画"))
        entries.append(("09", "出典・監査"))
    else:
        entries.append(("07", "検証計画"))
        entries.append(("08", "出典・監査"))
    cells = "".join(
        f'<div class="{"cur" if index == 0 else ""}"><b>{number}</b>{esc(label)}</div>'
        for index, (number, label) in enumerate(entries)
    )
    return f'<nav class="toc" style="--toc-count:{len(entries)}" aria-label="構成">{cells}</nav>'


def rating_scale(rating: int) -> str:
    steps = []
    for level, label in RATING_LABELS.items():
        selected = " sel" if level == rating else ""
        aria = ' aria-current="true"' if level == rating else ""
        steps.append(
            f'<div class="cell{selected}"{aria}><span class="n">{level}</span>'
            f'<span class="l">{esc(label)}</span></div>'
        )
    marker_position = (rating - 0.5) * 20
    return (
        f'<div class="scale-wrap" style="--marker-position:{marker_position:.1f}%">'
        '<span class="marker">判定<i></i></span>'
        f'<div class="scale" role="img" aria-label="5段階の一次判定">{"".join(steps)}</div>'
        '<div class="scale-axis"><span>← 見送り方向</span><span>積極方向 →</span></div></div>'
    )


def confidence_band(confidence: str) -> str:
    steps = "".join(
        f'<span class="{"on" if item == confidence else ""}">{esc(CONFIDENCE_LABELS[item])}</span>'
        for item in CONFIDENCE_ORDER
    )
    return f'<div class="conf-steps">{steps}</div>'


def render_cover(data: dict[str, Any], has_risk_page: bool, source_section: str) -> str:
    evaluation = data["evaluation"]
    rating = evaluation["rating"]
    supported_axes = sum(
        axis["status"] in {"confirmed", "estimated"} for axis in data["research_axes"]
    )
    blocker_count = len(data["risks"]["confirmed_blockers"])
    critical_count = len(data["risks"]["critical_unknowns"])
    assumptions = data["assumptions"] or ["追加前提なし"]
    assumption_rows = "".join(
        f'<li><span class="an">前提 {index:02d}</span><span>{esc(item)}</span></li>'
        for index, item in enumerate(assumptions, 1)
    )
    return f"""
<div class="idg">
  <div class="dt r1">診断地点</div><div class="dd r1 addr">{esc(data['address'])}</div>
  <div class="dt r1">調査日</div><div class="dd r1 sm">{esc(japanese_date(data['research_date']))}</div>
  <div class="dt">想定業態</div><div class="dd sm">{esc(data['business'])}</div>
  <div class="dt">資料種別</div><div class="dd sm"><span class="doc-type"><span>立地診断 mini</span><span>（初期スクリーニング）</span></span></div>
</div>
<div class="vgrid">
  <div><p class="v-cap">一次判定</p><p class="v-label">{esc(evaluation['label'])}</p>
    <p class="v-sub">5段階中 <b>{rating}</b></p></div>
  {rating_scale(rating)}
</div>
<div class="conf">
  <div class="cl">根拠確度<b>{esc(CONFIDENCE_LABELS[evaluation['confidence']])}</b></div>
  {confidence_band(evaluation['confidence'])}
  <p class="cd">根拠確度は、一次判定とは別に公開情報の充足度を示す指標。主要8軸の根拠確認 {supported_axes}/8、参照出典 {len(data['sources'])}件、結論反転級の未確認 {critical_count}件、確認済みの重大阻害要因 {blocker_count}件。</p>
</div>
<div class="blk">{block_heading('結論', note='要因の詳細は 02')}<p class="concl">{esc(data['conclusion'])}</p></div>
<div class="blk">{block_heading('前提', note=f'本診断の範囲を規定する{len(assumptions)}条件')}<ul class="assump">{assumption_rows}</ul></div>
<div class="legend">
  {status_chip('confirmed')}<span>公開情報で確認した事実</span>
  {status_chip('estimated')}<span>確認事実からの推定</span>
  {status_chip('field_check')}<span>内見・資料で確定</span>
  <span>S番号＝出典登録簿（{esc(source_section)}）への参照</span>
</div>
{render_toc(has_risk_page)}"""


def render_case_page(data: dict[str, Any], verification_section: str) -> tuple[str, str]:
    strengths = "".join(evidence_row(item) for item in data["strengths"])
    concerns = "".join(evidence_row(item) for item in data["concerns"])
    industry = data["industry_analysis"]
    chips = [
        industry["lens"],
        industry["movement_mode"],
        *industry["demand_periods"][:2],
    ]
    chip_markup = "".join(f'<span class="chip">{esc(short(item, 32))}</span>' for item in chips)
    risks = data["risks"]
    risk_count = sum(len(values) for values in risks.values())
    audit_text = (
        "調査範囲では、地点一致した重大阻害要因、不一致、結論反転級の未確認はない。"
        if risk_count == 0
        else f"重大阻害{len(risks['confirmed_blockers'])}件、不一致{len(risks['conflicts'])}件、結論反転級の未確認{len(risks['critical_unknowns'])}件。該当項目が次の判断条件となる。"
    )
    lead = "現時点の一次判定は、以下の支持材料と懸念のバランスによる。"
    body = f"""
<div class="blk">{block_heading('支持', f'判定を押し上げる{len(data["strengths"])}要因', '状態記号と出典は01の凡例に対応')}{strengths}</div>
<div class="blk">{block_heading('懸念', f'判定を抑える{len(data["concerns"])}要因', f'確認項目は {verification_section}')}{concerns}</div>
<div class="plan"><b>業態設計へ織り込む前提</b><div class="chips">{chip_markup}</div>
  <p>想定業態の成立性は、来店目的、移動手段、需要時間帯の組み合わせで変わる。</p></div>
<p class="note-line">{esc(audit_text)}</p>"""
    return lead, body


def render_metrics(metrics: list[dict[str, Any]]) -> str:
    if not metrics:
        return '<p class="dwarn">確認値なし。取得状態と理由のみ。</p>'
    return '<div class="mrow">' + "".join(
        '<div class="metric">'
        f'<p class="mn">{esc(metric["name"])}</p>'
        f'<p class="mv">{esc(metric["display_value"])}</p>'
        f'<p class="mm">{esc(metric["as_of"])}｜{esc(short(metric["geography"], 34))} {refs(metric["source_ids"])}</p>'
        "</div>"
        for metric in metrics
    ) + "</div>"


def render_chart(chart: dict[str, Any] | None, acquisition_status: str) -> str:
    if chart is None:
        return (
            '<div class="nochart"><b>図表なし</b>'
            f'<p>{esc(acquisition_status)}。同一定義で比較できる確認値が揃わず、図示なし。欠損は0を意味しない。</p></div>'
        )
    meta = f'{chart["as_of"]}｜{chart["geography"]} {refs(chart["source_ids"])}'
    if chart["type"] == "bar_pair":
        maximum = max(float(item["value"]) for item in chart["items"])
        rows = []
        for index, item in enumerate(chart["items"]):
            width = 100 * float(item["value"]) / maximum if maximum else 0
            rows.append(
                '<div class="bar-row">'
                f'<span class="bar-label">{esc(item["label"])}</span>'
                f'<span class="bar-track"><span class="bar-fill{" accent" if index == len(chart["items"]) - 1 else ""}" style="--bar-width:{width:.2f}%"></span></span>'
                f'<b class="bar-value">{esc(item["display_value"])}</b></div>'
            )
        return (
            f'<p class="fig-cap">{esc(chart["title"])}</p><div class="bar-chart">{"".join(rows)}</div>'
            f'<p class="fig-meta">{meta}</p>'
        )
    fills = ("ink", "violet", "soft", "muted")
    segments = "".join(
        f'<span class="stack-segment {fills[index]}" style="--seg-width:{float(item["value"]):.2f}%"></span>'
        for index, item in enumerate(chart["items"])
    )
    legend = "".join(
        f'<span class="legend-item"><i class="{fills[index]}"></i>{esc(item["label"])} {esc(item["display_value"])}</span>'
        for index, item in enumerate(chart["items"])
    )
    return (
        f'<p class="fig-cap">{esc(chart["title"])}</p><div class="stacked-bar">{segments}</div>'
        f'<div class="chart-legend">{legend}</div><p class="fig-meta">{meta}</p>'
    )


def render_baseline_strip(item: dict[str, Any]) -> str:
    return f"""
<section class="dstrip" data-baseline="{esc(item['id'])}">
  <div><p class="did">{esc(item['id'])}</p><p class="dtt">{esc(item['title'])}</p>{acquisition_chip(item['acquisition_status'])}</div>
  <div><p class="dsum">{esc(item['summary'])}</p>{render_metrics(item['metrics'])}</div>
  <div class="chart">{render_chart(item['chart'], item['acquisition_status'])}</div>
</section>"""


def render_demand_page(data: dict[str, Any]) -> tuple[str, str]:
    body = "".join(render_baseline_strip(item) for item in data["baselines"])
    lead = "居住、事業集積、活動需要、変化・制約の4系列。範囲と時点が異なるため、数値は合算できない。"
    return lead, body


def render_axis_table(data: dict[str, Any]) -> str:
    rows = []
    for axis in data["research_axes"]:
        highlight = " class=\"hl\"" if axis["status"] in {"field_check", "not_found"} else ""
        rows.append(
            f'<tr{highlight} data-research-id="{esc(axis["id"])}">'
            f'<td class="ax"><b>{esc(axis["id"])} {esc(axis["title"])}</b>{status_chip(axis["status"])}{refs(axis["source_ids"])}</td>'
            f'<td>{esc(axis["finding"])}</td><td>{esc(axis["meaning"])}</td></tr>'
        )
    return (
        '<table class="rt"><colgroup><col style="width:18%"><col style="width:48%"><col style="width:34%"></colgroup>'
        '<thead><tr><th>軸</th><th>確認した事実</th><th>判断への含意</th></tr></thead>'
        f'<tbody>{"".join(rows)}</tbody></table>'
    )


def render_research_page(data: dict[str, Any]) -> tuple[str, str]:
    unresolved = sum(
        axis["status"] in {"field_check", "not_found"} for axis in data["research_axes"]
    )
    lead = (
        f"各調査軸の事実と、出店判断への影響。"
        f"現地・資料で確定すべき軸は{unresolved}件で、次の判断条件となる。"
    )
    return lead, render_axis_table(data)


def diagram_node(title: str, copy: str, css: str) -> str:
    return (
        f'<div class="dnode {css}"><span>{esc(title)}</span>'
        f'<strong>{esc(short(copy, 58))}</strong></div>'
    )


def render_demand_diagram(data: dict[str, Any]) -> str:
    axes = {item["id"]: item for item in data["research_axes"]}
    industry = data["industry_analysis"]
    synergy_names = "・".join(item["title"] for item in industry["synergies"]) or "相乗施設は要確認"
    demand_periods = industry["demand_periods"]
    period_lines = "<br>".join(esc(period) for period in demand_periods) or "需要時間帯は要確認"
    return f"""
<div class="demand-diagram" role="img" aria-label="アクセス、相乗施設、想定業態、需要時間帯の接続図">
  <svg class="diagram-lines" viewBox="0 0 760 235" preserveAspectRatio="none" aria-hidden="true">
    <defs><marker id="arrow-violet" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#6F3FE5"/></marker></defs>
    <path d="M210 56 C275 56 280 118 340 118" />
    <path d="M210 178 C275 178 280 118 340 118" />
    <path class="accent" d="M420 118 C490 118 495 56 552 56" marker-end="url(#arrow-violet)" />
    <path class="accent" d="M420 118 C490 118 495 178 552 178" marker-end="url(#arrow-violet)" />
  </svg>
  {diagram_node('アクセス', axes['R2']['finding'], 'left top')}
  {diagram_node('相乗施設', synergy_names, 'left bottom')}
  {diagram_node('想定業態', data['business'], 'center')}
  {diagram_node('来店目的', industry['customer_purpose'], 'right top')}
  <div class="dnode right bottom demand-periods" data-period-count="{len(demand_periods)}">
    <span>需要時間帯</span><strong>{period_lines}</strong>
  </div>
</div>"""


def render_fit_observations(items: list[dict[str, Any]]) -> str:
    return "".join(
        '<div class="obs">'
        f'<p class="ot">{esc(item["title"])}</p><p>{esc(item["detail"])}</p>'
        f'<p class="om">{status_chip(item["status"])}{refs(item["source_ids"])}</p></div>'
        for item in items
    )


def render_format_fit_page(data: dict[str, Any]) -> tuple[str, str]:
    industry = data["industry_analysis"]
    periods = " / ".join(industry["demand_periods"]) or "業態前提から一意に定めず"
    lens = f"""
<div class="lens">
  <div class="lt r1">業態レンズ</div><div class="lv r1">{esc(industry['lens'])}</div>
  <div class="lt">来店目的</div><div class="lv">{esc(industry['customer_purpose'])}</div>
  <div class="lt">移動手段</div><div class="lv">{esc(industry['movement_mode'])}</div>
  <div class="lt">需要時間帯</div><div class="lv">{esc(periods)}</div>
</div>"""
    diagram = (
        '<div class="fig-h"><span class="t">需要接続図 — 空間 × 時間</span>'
        '<span class="note">確認事実と業態仮説の関係</span></div>'
        + render_demand_diagram(data)
    )
    observations = (
        f'<div class="blk">{block_heading("所見", f"業態適合の{len(industry["fit_observations"])}所見")}'
        + render_fit_observations(industry["fit_observations"]) + "</div>"
    )
    lead = (
        f"{short(industry['movement_mode'], 24)}の人流を、"
        "想定時間帯の来店につなげられるかが、業態適合を左右する。"
    )
    return lead, lens + diagram + observations


def competition_rows(items: list[dict[str, Any]], kind: str) -> str:
    return "".join(
        '<tr><td class="cn"><b>'
        f'{esc(item["title"])}</b>{refs(item["source_ids"])}</td>'
        f'<td><span class="kind">{esc(kind)}</span></td>'
        f'<td>{esc(item["detail"])}</td><td>{status_chip(item["status"])}</td></tr>'
        for item in items
    )


def synergy_rows(items: list[dict[str, Any]]) -> str:
    if not items:
        return '<div class="missing-state">相乗施設：初期診断での確認情報なし。</div>'
    return "".join(
        '<div class="obs"><p class="ot">'
        f'{esc(item["title"])}</p><p>{esc(item["detail"])}</p>'
        f'<p class="om">{status_chip(item["status"])}{refs(item["source_ids"])}</p></div>'
        for item in items
    )


def render_competition_page(data: dict[str, Any]) -> tuple[str, str]:
    industry = data["industry_analysis"]
    rows = (
        competition_rows(industry["direct_competition"], "直接")
        + competition_rows(industry["substitute_competition"], "代替")
    )
    if not rows:
        rows = '<tr><td colspan="4" class="missing-state">競合：初期診断での確認情報なし。</td></tr>'
    body = f"""
<div class="blk">{block_heading('競合', '役割の重なりと分け方', '直接＝同じ目的、代替＝別の方法で同じ用事')}
<table class="ct"><colgroup><col style="width:27%"><col style="width:11%"><col style="width:50%"><col style="width:12%"></colgroup>
<thead><tr><th>対象</th><th>区分</th><th>確認内容</th><th>状態</th></tr></thead><tbody>{rows}</tbody></table></div>
<div class="blk">{block_heading('相乗', '隣接施設との接続仮説', '施設の存在と顧客接続を分ける')}{synergy_rows(industry['synergies'])}</div>
<div class="blk">{block_heading('所見', '競合・相乗を踏まえた読み取り')}{render_fit_observations(industry['competition_observations'])}</div>"""
    lead = "直接競合、代替競合、相乗施設が、来店目的と時間帯のどこで重なり、どこで分かれるか。"
    return lead, body


def risk_entries(risks: dict[str, list[dict[str, Any]]]) -> str:
    groups = [
        ("重大阻害", "is-high", risks["confirmed_blockers"]),
        ("不一致", "is-mid", risks["conflicts"]),
        ("要確認", "is-low", risks["critical_unknowns"]),
    ]
    rows = []
    for label, css, items in groups:
        for item in items:
            rows.append(
                '<li class="risk-item">'
                f'<span class="risk-level {css}">{esc(label)}</span>'
                f'<p class="risk-copy"><strong>{esc(item["title"])}</strong> {esc(item["detail"])} '
                f'{status_chip(item["status"])} {refs(item["source_ids"])}</p></li>'
            )
    return "".join(rows)


def render_audit_page(data: dict[str, Any]) -> tuple[str, str]:
    risks = data["risks"]
    total = sum(len(values) for values in risks.values())
    lead = (
        f"重大阻害{len(risks['confirmed_blockers'])}件、不一致{len(risks['conflicts'])}件、"
        f"結論反転級の未確認{len(risks['critical_unknowns'])}件。一次判定とは別枠の監査対象。"
    )
    d4 = next(item for item in data["baselines"] if item["id"] == "D4")
    body = f"""
<div class="cov compact">
  <div><p class="cl2">監査対象</p><p class="cv2">{total}<small>件</small></p></div>
  <div><p class="cl2">重大阻害</p><p class="cv2">{len(risks['confirmed_blockers'])}<small>件</small></p></div>
  <div><p class="cl2">不一致</p><p class="cv2">{len(risks['conflicts'])}<small>件</small></p></div>
  <div><p class="cl2">結論反転級の未確認</p><p class="cv2">{len(risks['critical_unknowns'])}<small>件</small></p></div>
</div>
<div class="blk">{block_heading('監査', '判定と分けて残す論点', '未確認を不存在や自動減点へ変換しない')}<ul class="risk-list">{risk_entries(risks)}</ul></div>
<div class="blk">{block_heading('D4', f'{d4["title"]}', d4['acquisition_status'])}<p class="dsum">{esc(d4['summary'])}</p>{render_metrics(d4['metrics'])}</div>"""
    return lead, body


def render_inline_risks(data: dict[str, Any]) -> str:
    risks = data["risks"]
    count = sum(len(values) for values in risks.values())
    if count == 0:
        return '<p class="note-line audit-zero">調査範囲では、地点一致した重大阻害要因、不一致、結論反転級の未確認はない。</p>'
    return f'<div class="inline-risk"><ul class="risk-list">{risk_entries(risks)}</ul></div>'


def render_conditions(data: dict[str, Any]) -> str:
    field_checks = data["field_checks"]
    additional = data["additional_data"]
    rows = []
    for index, condition in enumerate(data["flip_conditions"], 1):
        check_index = min(index - 1, len(field_checks) - 1)
        data_index = min(index - 1, len(additional) - 1)
        linked = (
            f'現地確認{check_index + 1:02d}（{short(field_checks[check_index], 42)}）'
            f'／追加データ{data_index + 1:02d}（{short(additional[data_index]["name"], 24)}）'
        )
        rows.append(
            '<div class="cond">'
            f'<p class="cno">条件<b>{index:02d}</b></p>'
            f'<p class="cb">{esc(condition)}</p>'
            f'<p class="cv"><b>対応する検証</b>{esc(linked)}</p></div>'
        )
    return "".join(rows)


def render_field_checks(items: list[str]) -> str:
    return '<ul class="fc">' + "".join(
        '<li><span class="cb2"></span>'
        f'<span class="fn">{index:02d}</span><span>{esc(item)}</span></li>'
        for index, item in enumerate(items, 1)
    ) + "</ul>"


def render_additional_data(items: list[dict[str, Any]]) -> str:
    return (
        '<table class="at"><colgroup><col style="width:22%"><col style="width:35%"><col style="width:43%"></colgroup>'
        '<thead><tr><th>取得するもの</th><th>方法</th><th>意思決定への使い方</th></tr></thead><tbody>'
        + "".join(
            f'<tr><td class="an2">{index:02d} {esc(item["name"])}</td>'
            f'<td>{esc(item["method"])}</td><td>{esc(item["decision_use"])}</td></tr>'
            for index, item in enumerate(items, 1)
        ) + "</tbody></table>"
    )


def render_verification_page(data: dict[str, Any], include_inline_risks: bool) -> tuple[str, str]:
    body = ""
    if include_inline_risks:
        body += render_inline_risks(data)
    body += f"""
<div class="blk">{block_heading('反転条件', '満たせないと判定が変わる条件', '確認結果を一次判定へ戻す')}{render_conditions(data)}</div>
<div class="blk">{block_heading('現地確認', '内見・観察チェックリスト（5項目）', '□は確認欄')}{render_field_checks(data['field_checks'])}</div>
<div class="blk">{block_heading('追加データ', f'取得すべき{len(data["additional_data"])}つの材料')}{render_additional_data(data['additional_data'])}</div>"""
    lead = f"次の{len(data['flip_conditions'])}条件の確認結果により、一次判定は上下いずれにも動く。"
    return lead, body


def display_url(url: str) -> str:
    parsed = urlsplit(url)
    display = urlunsplit(("", parsed.netloc, parsed.path or "/", "", ""))
    display = display.lstrip("//")
    if len(display) > 66:
        display = display[:63] + "..."
    return display


def source_item(source: dict[str, Any]) -> str:
    return (
        '<li class="sr">'
        f'<span class="sid2">{esc(source["id"])}</span><div>'
        f'<a class="t2" href="{esc(source["url"])}" target="_blank" rel="noopener noreferrer">{esc(source["title"])}</a>'
        f'<p class="u2">{esc(display_url(source["url"]))}</p>'
        f'<p class="m2">{esc(source["publisher"])}<span class="sp">|</span>{esc(source["as_of"])}'
        f'<span class="sp">|</span>支持 <b>{esc("・".join(source["supports"]))}</b></p></div></li>'
    )


def render_source_register(sources: list[dict[str, Any]]) -> str:
    split_at = math.ceil(len(sources) / 2)
    columns = (sources[:split_at], sources[split_at:])
    return '<div class="sreg">' + "".join(
        f'<ul>{"".join(source_item(source) for source in column)}</ul>' for column in columns
    ) + "</div>"


def balanced_chunks(items: list[dict[str, Any]], maximum: int) -> list[list[dict[str, Any]]]:
    page_count = math.ceil(len(items) / maximum)
    base, extra = divmod(len(items), page_count)
    chunks = []
    offset = 0
    for index in range(page_count):
        size = base + (1 if index < extra else 0)
        chunks.append(items[offset:offset + size])
        offset += size
    return chunks


def qr_markup() -> str:
    qr_svg = canonical_qr()
    return (
        '<div class="qrc"><span class="closing-qr" aria-label="ROGNALIA立地診断ページのQRコード">'
        f'{qr_svg}</span><span>立地診断ページ</span></div>'
    )


def closing_block() -> str:
    return f"""
<aside class="handoff">
  <div><h3>この先の出店判断を、さらに進めたい場合</h3>
  <p class="hb">1地点の詳細な立地診断、出店候補地の探索、複数候補の比較、既存店ベンチマーク、自社専用モデルの構築、候補地評価のセカンドオピニオンまで。次の出店判断に必要な材料を、ROGNALIAが整理します。</p>
  <a class="url" href="{CTA_URL}">{CTA_URL}</a></div>
  {qr_markup()}
</aside>"""


def source_audit(data: dict[str, Any]) -> str:
    risks = data["risks"]
    risk_count = sum(len(values) for values in risks.values())
    return f"""
<div class="cov">
  <div><p class="cl2">調査軸</p><p class="cv2">{data['coverage']['axes_completed']}<small>/8 完了</small></p></div>
  <div><p class="cl2">参照出典</p><p class="cv2">{len(data['sources'])}<small>件</small></p></div>
  <div><p class="cl2">結論反転級の未確認</p><p class="cv2">{len(risks['critical_unknowns'])}<small>件</small></p></div>
  <div><p class="cl2">重大阻害・不一致</p><p class="cv2">{len(risks['confirmed_blockers']) + len(risks['conflicts'])}<small>件</small></p></div>
</div>
<p class="audit-note">出典登録簿の収録基準：公開Webで本文まで確認した情報のみ。検索結果の抜粋、本文を確認できないURL、地点の一致しない値は確認済み根拠に含めない。対象はR1〜R8・D1〜D4、監査対象は{risk_count}件。</p>"""


def render_source_pages(
    data: dict[str, Any],
    *,
    total_pages: int,
    start_number: int,
    source_section: str,
    wordmark_svg: str,
) -> list[str]:
    chunks = balanced_chunks(data["sources"], SOURCES_PER_PAGE)
    pages = []
    for index, chunk in enumerate(chunks):
        first = index == 0
        last = index == len(chunks) - 1
        section_label = source_section if first else f"{source_section} 出典続き"
        title = "判断に使った公開情報と調査範囲" if first else "出典登録簿（続き）"
        lead = (
            f"主要な判断根拠は、{len(data['sources'])}件の公開出典から確認できる。"
            if first else
            f"出典ID {chunk[0]['id']}〜{chunk[-1]['id']}を収録する。"
        )
        body = ""
        if first:
            body += source_audit(data)
        body += (
            f'<div class="blk source-block">{block_heading("出典", f"出典登録簿 {chunk[0]["id"]}〜{chunk[-1]["id"]}", "発行主体｜情報時点｜支持軸")}'
            '<p class="sreg-key">各項目の下段は、発行主体<span class="sp">|</span>情報時点<span class="sp">|</span>支持軸の順。</p>'
            f'{render_source_register(chunk)}</div>'
        )
        if last:
            assumptions = " / ".join(data["assumptions"]) if data["assumptions"] else "追加前提なし"
            body += (
                '<div class="method-note"><strong>調査範囲と前提</strong>'
                f'<p>{esc(data["coverage"]["summary"])}</p><p>前提: {esc(assumptions)}</p></div>'
                + closing_block()
            )
        else:
            body += '<div class="method-note"><strong>出典は次ページへ続きます</strong><p>出典IDは全ページで連番です。</p></div>'
        source_page_class = "source-page"
        if len(chunk) >= 15:
            source_page_class += " source-page-dense"
        pages.append(
            page_shell(
                number=start_number + index,
                total=total_pages,
                section_label=section_label,
                kicker="SOURCES & AUDIT",
                title=title,
                lead=lead,
                scope=f"{short(data['address'], 30)}｜調査日 {data['research_date'].replace('-', '.')}",
                body=body,
                wordmark_svg=wordmark_svg,
                extra_class=source_page_class,
            )
        )
    return pages


def build_html(data: dict[str, Any]) -> str:
    template = canonical_template()
    sprite = canonical_icons()
    wordmark = canonical_wordmark()
    risks = data["risks"]
    risk_count = sum(len(values) for values in risks.values())
    has_risk_page = risk_count >= RISK_PAGE_THRESHOLD
    source_chunks = balanced_chunks(data["sources"], SOURCES_PER_PAGE)
    total_pages = 7 + (1 if has_risk_page else 0) + len(source_chunks)
    if not 8 <= total_pages <= 10:
        raise ValidationError("page_count: 8〜10ページに収まりません")

    verification_number = 8 if has_risk_page else 7
    source_start = verification_number + 1
    source_section = f"{source_start:02d}"
    scope = f"{short(data['address'], 30)}｜調査日 {data['research_date'].replace('-', '.')}"
    baseline_metric_count = sum(len(item["metrics"]) for item in data["baselines"])
    baseline_page_class = "baseline-page"
    if baseline_metric_count >= BASELINE_DENSE_METRIC_THRESHOLD:
        baseline_page_class += " baseline-page-dense"

    cover_body = render_cover(data, has_risk_page, source_section)
    case_lead, case_body = render_case_page(data, f"{verification_number:02d}")
    demand_lead, demand_body = render_demand_page(data)
    research_lead, research_body = render_research_page(data)
    fit_lead, fit_body = render_format_fit_page(data)
    competition_lead, competition_body = render_competition_page(data)

    pages = [
        page_shell(
            number=1,
            total=total_pages,
            section_label="01 判定",
            kicker="01｜VERDICT",
            title="初期スクリーニング判定",
            lead=first_sentence(data["conclusion"]),
            scope=scope,
            body=cover_body,
            wordmark_svg=wordmark,
        ),
        page_shell(
            number=2,
            total=total_pages,
            section_label="02 論拠",
            kicker="02｜CASE",
            title="判定を支える要因と、判定を抑える要因",
            lead=case_lead,
            scope=scope,
            body=case_body,
            wordmark_svg=wordmark,
        ),
        page_shell(
            number=3,
            total=total_pages,
            section_label="03 基礎数値",
            kicker="03｜BASELINES D1–D4",
            title="需要の土台 — 範囲と時点の異なる4系列",
            lead=demand_lead,
            scope=scope,
            body=demand_body,
            wordmark_svg=wordmark,
            extra_class=baseline_page_class,
        ),
        page_shell(
            number=4,
            total=total_pages,
            section_label="04 調査軸",
            kicker="04｜RESEARCH R1–R8",
            title="8つの調査軸 — 事実と判断への含意",
            lead=research_lead,
            scope=scope,
            body=research_body,
            wordmark_svg=wordmark,
        ),
        page_shell(
            number=5,
            total=total_pages,
            section_label="05 業態適合",
            kicker="05｜FORMAT FIT",
            title="業態適合 — 人の流れを需要へつなぐ",
            lead=fit_lead,
            scope=scope,
            body=fit_body,
            wordmark_svg=wordmark,
        ),
        page_shell(
            number=6,
            total=total_pages,
            section_label="06 競合・相乗",
            kicker="06｜COMPETITION & SYNERGY",
            title="競合と相乗 — 役割の重なりと分け方",
            lead=competition_lead,
            scope=scope,
            body=competition_body,
            wordmark_svg=wordmark,
        ),
    ]
    if has_risk_page:
        audit_lead, audit_body = render_audit_page(data)
        pages.append(
            page_shell(
                number=7,
                total=total_pages,
                section_label="07 反証監査",
                kicker="07｜COUNTEREVIDENCE",
                title="重大阻害・不一致・未確認の監査",
                lead=audit_lead,
                scope=scope,
                body=audit_body,
                wordmark_svg=wordmark,
            )
        )

    verification_lead, verification_body = render_verification_page(
        data, include_inline_risks=not has_risk_page
    )
    pages.append(
        page_shell(
            number=verification_number,
            total=total_pages,
            section_label=f"{verification_number:02d} 検証計画",
            kicker=f"{verification_number:02d}｜VERIFICATION",
            title="判定が変わる条件と、次に取るべき検証",
            lead=verification_lead,
            scope=scope,
            body=verification_body,
            wordmark_svg=wordmark,
            extra_class="verification-page",
        )
    )
    pages.extend(
        render_source_pages(
            data,
            total_pages=total_pages,
            start_number=source_start,
            source_section=source_section,
            wordmark_svg=wordmark,
        )
    )

    replacements = {
        "{{DOCUMENT_TITLE}}": esc(
            f"ROGNALIA 立地診断 mini｜{data['address']} × {data['business']}"
        ),
        "{{SVG_SPRITE}}": sprite,
        "{{REPORT_PAGES}}": "\n".join(pages),
    }
    for placeholder, value in replacements.items():
        template = template.replace(placeholder, value)
    qa_html(template, total_pages, len(data["sources"]))
    return template


def qa_html(document: str, expected_pages: int, expected_sources: int) -> None:
    if "{{" in document or "}}" in document:
        raise ValidationError("html: 未解決placeholderがあります")
    if document.count('class="sheet report-page') != expected_pages:
        raise ValidationError("html: report page数が一致しません")
    if document.count(DISCLAIMER) != expected_pages:
        raise ValidationError("html: 固定免責の件数がpage数と一致しません")
    if document.count('class="header-wordmark"') != expected_pages:
        raise ValidationError("html: header wordmarkの件数がpage数と一致しません")
    if document.count('class="footer-wordmark"') != expected_pages:
        raise ValidationError("html: footer wordmarkの件数がpage数と一致しません")
    wordmark = canonical_wordmark()
    if document.count(wordmark) != expected_pages * 2:
        raise ValidationError("html: 正式wordmarkの実体が全header・footerに一致しません")
    qr_svg = canonical_qr()
    if document.count(qr_svg) != 1:
        raise ValidationError("html: 固定QR assetは最終pageに1件必要です")
    template = canonical_template()
    style_start = template.index("<style>")
    style_end = template.index("</style>", style_start) + len("</style>")
    canonical_style = template[style_start:style_end]
    if document.count(canonical_style) != 1:
        raise ValidationError("html: canonical stylesheetと一致しません")
    for title in FIXED_PAGE_TITLES:
        if document.count(f'<h1 class="pt">{title}</h1>') != 1:
            raise ValidationError(f"html: 固定page見出しが一致しません: {title}")
    for token in ("--red", "--green", "#B44545", "#286B52"):
        if token.lower() in document.lower():
            raise ValidationError(f"html: 標準palette外の意味色が含まれています: {token}")
    if document.count('class="scale"') != 1:
        raise ValidationError("html: 一次判定scaleは1件必要です")
    if document.count('class="cell') != 5:
        raise ValidationError("html: 一次判定scaleは5区分必要です")
    if document.count("cell sel") != 1:
        raise ValidationError("html: 一次判定scaleの現在値は1件必要です")
    if document.count('class="sr"') != expected_sources:
        raise ValidationError("html: 出典登録数がsources件数と一致しません")
    for research_id in [f"R{index}" for index in range(1, 9)]:
        if document.count(f'data-research-id="{research_id}"') != 1:
            raise ValidationError(f"html: {research_id}は1件必要です")
    for baseline_id in [f"D{index}" for index in range(1, 5)]:
        if document.count(f'data-baseline="{baseline_id}"') != 1:
            raise ValidationError(f"html: {baseline_id}は1件必要です")
    if document.count('onclick="window.print()"') != 1:
        raise ValidationError("html: window.print handlerは1件必要です")
    if "@media screen and (max-width: 600px)" not in document:
        raise ValidationError("html: mobile reader layoutがありません")
    mobile_css = document.split("@media screen and (max-width: 600px)", 1)[1].split(
        "@media screen and (max-width: 360px)", 1
    )[0]
    for rule in ("zoom: 1 !important", "height: auto", "grid-template-columns: 1fr"):
        if rule not in mobile_css:
            raise ValidationError(f"html: mobile reader layoutの必須ruleがありません: {rule}")
    if document.index("@media screen and (max-width: 600px)") > document.index("@media print"):
        raise ValidationError("html: mobile reader layoutはprint ruleより前に置く必要があります")
    if re.search(r"<script\b", document, re.IGNORECASE):
        raise ValidationError("html: script要素は使用できません")
    if re.search(
        r"<(?:img|script|link)[^>]+(?:src|href)=['\"]https?://",
        document,
        re.IGNORECASE,
    ):
        raise ValidationError("html: remote resourceは使用できません")
    if EMOJI_RE.search(document):
        raise ValidationError("html: 絵文字は使用できません")
    for token in ("Powered by", "Copyright", "©", "radar-chart"):
        if token.lower() in document.lower():
            raise ValidationError(f"html: 禁止表現 {token} が含まれています")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report_json", type=Path, help="Validated report JSON")
    parser.add_argument("--output", "-o", required=True, type=Path, help="Output HTML path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        data = json.loads(args.report_json.read_text(encoding="utf-8"))
        validate_report(data)
        document = build_html(data)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(document, encoding="utf-8")
    except (OSError, json.JSONDecodeError, ValidationError) as exc:
        print(f"RENDER FAILED: {exc}", file=sys.stderr)
        return 1
    pages = document.count('class="sheet report-page')
    print(f"RENDERED: {args.output} / A4 {pages} pages / {len(data['sources'])} sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
