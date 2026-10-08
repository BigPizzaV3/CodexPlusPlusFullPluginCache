#!/usr/bin/env python3
"""Validate a ROGNALIA Location Diagnosis Mini report JSON without dependencies."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlparse


RATING_LABELS = {
    1: "見送り推奨",
    2: "見送り寄り",
    3: "条件次第",
    4: "前向きに検討",
    5: "積極検討",
}
CONFIDENCE_VALUES = {"high", "medium", "low"}
EVIDENCE_STATUSES = {"confirmed", "estimated", "reference", "not_found", "field_check"}
METRIC_ACQUISITION_STATUSES = {
    "取得済み", "上位地域で代替", "地点照合が必要", "初期診断では未取得", "対象外",
}
BASELINE_ACQUISITION_STATUSES = METRIC_ACQUISITION_STATUSES | {"一部未取得"}
AXIS_IDS = [f"R{i}" for i in range(1, 9)]
BASELINE_IDS = [f"D{i}" for i in range(1, 5)]
FORBIDDEN_KEYS = {"score", "probability", "success_rate", "rank", "ranking", "weight"}
FORBIDDEN_COPY = ("Powered by", "Copyright", "©", "無料版", "必ず成功", "売上保証", "ROGNALIAなら取得")
EMOJI_RE = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF]")
SOURCE_ID_RE = re.compile(r"^S([1-9][0-9]?)$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MAX_BASELINE_METRICS = 14


class ValidationError(Exception):
    pass


def fail(path: str, message: str) -> None:
    raise ValidationError(f"{path}: {message}")


def require_object(value: Any, path: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail(path, "objectが必要です")
    return value


def require_list(value: Any, path: str, minimum: int, maximum: int) -> list[Any]:
    if not isinstance(value, list):
        fail(path, "arrayが必要です")
    if not minimum <= len(value) <= maximum:
        fail(path, f"件数は{minimum}〜{maximum}件にしてください")
    return value


def require_string(value: Any, path: str, minimum: int = 1, maximum: int = 10_000) -> str:
    if not isinstance(value, str):
        fail(path, "stringが必要です")
    value = value.strip()
    if not minimum <= len(value) <= maximum:
        fail(path, f"文字数は{minimum}〜{maximum}字にしてください")
    if "<script" in value.lower() or "javascript:" in value.lower():
        fail(path, "実行可能なHTMLまたはURLは使用できません")
    if EMOJI_RE.search(value):
        fail(path, "絵文字は使用できません")
    for token in FORBIDDEN_COPY:
        if token.lower() in value.lower():
            fail(path, f"禁止表現 `{token}` が含まれています")
    return value


def require_date(value: Any, path: str) -> str:
    text = require_string(value, path, 10, 10)
    if not DATE_RE.match(text):
        fail(path, "YYYY-MM-DD形式が必要です")
    try:
        date.fromisoformat(text)
    except ValueError as exc:
        fail(path, f"実在する日付が必要です: {exc}")
    return text


def require_exact_keys(obj: dict[str, Any], path: str, required: Iterable[str], optional: Iterable[str] = ()) -> None:
    required_set = set(required)
    allowed = required_set | set(optional)
    missing = sorted(required_set - set(obj))
    extra = sorted(set(obj) - allowed)
    if missing:
        fail(path, f"必須fieldがありません: {', '.join(missing)}")
    if extra:
        fail(path, f"未定義fieldがあります: {', '.join(extra)}")


def source_ids(value: Any, path: str, known_sources: set[str] | None = None, maximum: int = 6) -> list[str]:
    items = require_list(value, path, 0, maximum)
    ids: list[str] = []
    for index, item in enumerate(items):
        sid = require_string(item, f"{path}[{index}]", 2, 3)
        if not SOURCE_ID_RE.match(sid):
            fail(f"{path}[{index}]", "S1〜S99形式が必要です")
        ids.append(sid)
    if len(ids) != len(set(ids)):
        fail(path, "source IDが重複しています")
    if known_sources is not None:
        unknown = sorted(set(ids) - known_sources)
        if unknown:
            fail(path, f"sourcesに存在しないIDがあります: {', '.join(unknown)}")
    return ids


def validate_evidence_item(value: Any, path: str, known_sources: set[str]) -> None:
    obj = require_object(value, path)
    require_exact_keys(obj, path, ["title", "detail", "status", "source_ids"])
    require_string(obj["title"], f"{path}.title", 1, 28)
    require_string(obj["detail"], f"{path}.detail", 1, 110)
    status = require_string(obj["status"], f"{path}.status", 1, 20)
    if status not in EVIDENCE_STATUSES:
        fail(f"{path}.status", "根拠状態が不正です")
    refs = source_ids(obj["source_ids"], f"{path}.source_ids", known_sources)
    if status in {"confirmed", "estimated", "reference"} and not refs:
        fail(f"{path}.source_ids", f"{status}にはsource IDが必要です")


def validate_sources(value: Any) -> tuple[list[dict[str, Any]], set[str]]:
    sources = require_list(value, "sources", 1, 32)
    ids: list[str] = []
    for index, raw in enumerate(sources):
        path = f"sources[{index}]"
        obj = require_object(raw, path)
        require_exact_keys(obj, path, ["id", "title", "url", "publisher", "checked_at", "as_of", "supports"])
        sid = require_string(obj["id"], f"{path}.id", 2, 3)
        if not SOURCE_ID_RE.match(sid):
            fail(f"{path}.id", "S1〜S99形式が必要です")
        ids.append(sid)
        require_string(obj["title"], f"{path}.title", 1, 100)
        url = require_string(obj["url"], f"{path}.url", 10, 2_000)
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            fail(f"{path}.url", "完全なhttp(s) URLが必要です")
        require_string(obj["publisher"], f"{path}.publisher", 1, 80)
        require_date(obj["checked_at"], f"{path}.checked_at")
        require_string(obj["as_of"], f"{path}.as_of", 1, 50)
        supports = require_list(obj["supports"], f"{path}.supports", 1, 8)
        seen_supports: set[str] = set()
        for support_index, support in enumerate(supports):
            support_id = require_string(support, f"{path}.supports[{support_index}]", 2, 2)
            if support_id not in set(AXIS_IDS + BASELINE_IDS):
                fail(f"{path}.supports[{support_index}]", "R1〜R8またはD1〜D4が必要です")
            seen_supports.add(support_id)
        if len(seen_supports) != len(supports):
            fail(f"{path}.supports", "support IDが重複しています")
    if len(ids) != len(set(ids)):
        fail("sources", "source IDが重複しています")
    expected = [f"S{i}" for i in range(1, len(ids) + 1)]
    if ids != expected:
        fail("sources", "source IDはS1から欠番なく順番に並べてください")
    return sources, set(ids)


def validate_metric(value: Any, path: str, known_sources: set[str]) -> tuple[str, set[str]]:
    obj = require_object(value, path)
    require_exact_keys(
        obj,
        path,
        ["name", "display_value", "as_of", "geography", "acquisition_status", "source_ids"],
        ["numeric_value", "unit"],
    )
    require_string(obj["name"], f"{path}.name", 1, 40)
    require_string(obj["display_value"], f"{path}.display_value", 1, 40)
    if "numeric_value" in obj and obj["numeric_value"] is not None:
        if not isinstance(obj["numeric_value"], (int, float)) or isinstance(obj["numeric_value"], bool):
            fail(f"{path}.numeric_value", "0以上の数値またはnullが必要です")
        if obj["numeric_value"] < 0:
            fail(f"{path}.numeric_value", "負数は使用できません")
    if "unit" in obj:
        require_string(obj["unit"], f"{path}.unit", 0, 20)
    require_string(obj["as_of"], f"{path}.as_of", 1, 40)
    require_string(obj["geography"], f"{path}.geography", 1, 80)
    acquisition = require_string(obj["acquisition_status"], f"{path}.acquisition_status", 1, 20)
    if acquisition not in METRIC_ACQUISITION_STATUSES:
        fail(f"{path}.acquisition_status", "取得状態が不正です")
    refs = source_ids(obj["source_ids"], f"{path}.source_ids", known_sources)
    if acquisition in {"取得済み", "上位地域で代替"} and not refs:
        fail(f"{path}.source_ids", "取得済みまたは上位地域代替にはsource IDが必要です")
    return acquisition, set(refs)


def validate_chart(
    value: Any,
    path: str,
    known_sources: set[str],
    acquisition: str,
    baseline_id: str,
    chartable_sources: set[str],
) -> None:
    if value is None:
        return
    if acquisition == "対象外":
        fail(path, "対象外のbaselineへchartを置けません")
    if baseline_id == "D4":
        fail(path, "D4は固定chartの対象外です")
    obj = require_object(value, path)
    require_exact_keys(obj, path, ["type", "title", "unit", "as_of", "geography", "source_ids", "items"])
    chart_type = require_string(obj["type"], f"{path}.type", 1, 20)
    if chart_type not in {"bar_pair", "stacked_share"}:
        fail(f"{path}.type", "bar_pairまたはstacked_shareが必要です")
    require_string(obj["title"], f"{path}.title", 1, 50)
    require_string(obj["unit"], f"{path}.unit", 0, 20)
    require_string(obj["as_of"], f"{path}.as_of", 1, 50)
    require_string(obj["geography"], f"{path}.geography", 1, 80)
    refs = source_ids(obj["source_ids"], f"{path}.source_ids", known_sources)
    if not refs:
        fail(f"{path}.source_ids", "chartにはsource IDが必要です")
    unsupported_refs = sorted(set(refs) - chartable_sources)
    if unsupported_refs:
        fail(
            f"{path}.source_ids",
            "取得済みまたは上位地域代替のmetricで裏付けられないIDがあります: "
            + ", ".join(unsupported_refs),
        )
    expected_count = (2, 2) if chart_type == "bar_pair" else (3, 4)
    items = require_list(obj["items"], f"{path}.items", *expected_count)
    values: list[float] = []
    for index, raw in enumerate(items):
        item_path = f"{path}.items[{index}]"
        item = require_object(raw, item_path)
        require_exact_keys(item, item_path, ["label", "value", "display_value"])
        require_string(item["label"], f"{item_path}.label", 1, 30)
        require_string(item["display_value"], f"{item_path}.display_value", 1, 30)
        number = item["value"]
        if not isinstance(number, (int, float)) or isinstance(number, bool) or number < 0:
            fail(f"{item_path}.value", "0以上の数値が必要です")
        values.append(float(number))
    if max(values) <= 0:
        fail(f"{path}.items", "全値0のchartは使用できません")
    if chart_type == "stacked_share" and abs(sum(values) - 100.0) > 0.2:
        fail(f"{path}.items", "stacked_shareの合計は100にしてください")


def validate_baselines(value: Any, known_sources: set[str]) -> None:
    baselines = require_list(value, "baselines", 4, 4)
    ids: list[str] = []
    total_metric_count = 0
    for index, raw in enumerate(baselines):
        path = f"baselines[{index}]"
        obj = require_object(raw, path)
        require_exact_keys(obj, path, ["id", "title", "acquisition_status", "summary", "metrics", "chart"])
        baseline_id = require_string(obj["id"], f"{path}.id", 2, 2)
        ids.append(baseline_id)
        if baseline_id not in BASELINE_IDS:
            fail(f"{path}.id", "D1〜D4が必要です")
        require_string(obj["title"], f"{path}.title", 1, 40)
        acquisition = require_string(obj["acquisition_status"], f"{path}.acquisition_status", 1, 20)
        if acquisition not in BASELINE_ACQUISITION_STATUSES:
            fail(f"{path}.acquisition_status", "取得状態が不正です")
        require_string(obj["summary"], f"{path}.summary", 1, 130)
        metrics = require_list(obj["metrics"], f"{path}.metrics", 0, 5)
        total_metric_count += len(metrics)
        metric_statuses: list[str] = []
        chartable_sources: set[str] = set()
        for metric_index, metric in enumerate(metrics):
            metric_status, metric_sources = validate_metric(
                metric, f"{path}.metrics[{metric_index}]", known_sources
            )
            metric_statuses.append(metric_status)
            if metric_status in {"取得済み", "上位地域で代替"}:
                chartable_sources.update(metric_sources)
        if metric_statuses:
            applicable_statuses = [status for status in metric_statuses if status != "対象外"]
            if not applicable_statuses:
                expected_acquisition = "対象外"
            elif "地点照合が必要" in applicable_statuses:
                expected_acquisition = "地点照合が必要"
            elif "初期診断では未取得" in applicable_statuses:
                usable_statuses = {"取得済み", "上位地域で代替"}
                expected_acquisition = (
                    "一部未取得"
                    if any(status in usable_statuses for status in applicable_statuses)
                    else "初期診断では未取得"
                )
            elif "上位地域で代替" in applicable_statuses:
                expected_acquisition = "上位地域で代替"
            else:
                expected_acquisition = "取得済み"
            if acquisition != expected_acquisition:
                fail(
                    f"{path}.acquisition_status",
                    f"metricの取得状態を保守的に集約した `{expected_acquisition}` が必要です",
                )
        elif acquisition == "一部未取得":
            fail(
                f"{path}.acquisition_status",
                "一部未取得には、取得済みまたは上位地域代替と未取得のmetricが必要です",
            )
        validate_chart(
            obj["chart"],
            f"{path}.chart",
            known_sources,
            acquisition,
            baseline_id,
            chartable_sources,
        )
    if total_metric_count > MAX_BASELINE_METRICS:
        fail(
            "baselines.metrics",
            f"A4の可読性を保つため、D1〜D4全体で{MAX_BASELINE_METRICS}件以内に絞ってください",
        )
    if ids != BASELINE_IDS:
        fail("baselines", "D1〜D4を固定順で1件ずつ置いてください")


def validate_axes(value: Any, known_sources: set[str]) -> None:
    axes = require_list(value, "research_axes", 8, 8)
    ids: list[str] = []
    for index, raw in enumerate(axes):
        path = f"research_axes[{index}]"
        obj = require_object(raw, path)
        require_exact_keys(obj, path, ["id", "title", "status", "finding", "meaning", "source_ids"])
        axis_id = require_string(obj["id"], f"{path}.id", 2, 2)
        ids.append(axis_id)
        require_string(obj["title"], f"{path}.title", 1, 40)
        status = require_string(obj["status"], f"{path}.status", 1, 20)
        if status not in EVIDENCE_STATUSES:
            fail(f"{path}.status", "根拠状態が不正です")
        require_string(obj["finding"], f"{path}.finding", 1, 140)
        require_string(obj["meaning"], f"{path}.meaning", 1, 100)
        refs = source_ids(obj["source_ids"], f"{path}.source_ids", known_sources)
        if status in {"confirmed", "estimated", "reference"} and not refs:
            fail(f"{path}.source_ids", f"{status}にはsource IDが必要です")
    if ids != AXIS_IDS:
        fail("research_axes", "R1〜R8を固定順で1件ずつ置いてください")


def validate_string_list(value: Any, path: str, minimum: int, maximum: int, item_maximum: int) -> None:
    items = require_list(value, path, minimum, maximum)
    for index, item in enumerate(items):
        require_string(item, f"{path}[{index}]", 1, item_maximum)


def derive_confidence(rating: int, axes: list[dict[str, Any]], risks: dict[str, list[Any]]) -> str:
    """Return the public, deterministic confidence band for the screening rating."""
    if rating == 1 and risks["confirmed_blockers"]:
        return "high"
    supported_axes = sum(axis["status"] in {"confirmed", "estimated"} for axis in axes)
    critical_count = len(risks["critical_unknowns"])
    conflict_count = len(risks["conflicts"])
    if supported_axes >= 7 and critical_count == 0 and conflict_count == 0:
        return "high"
    if supported_axes >= 5 and critical_count <= 2 and conflict_count <= 1:
        return "medium"
    return "low"


def validate_report(data: Any) -> None:
    root = require_object(data, "$root")
    required = [
        "schema_version", "address", "business", "research_date", "evaluation", "conclusion",
        "assumptions", "strengths", "concerns", "flip_conditions", "coverage", "baselines",
        "research_axes", "industry_analysis", "risks", "field_checks", "additional_data", "sources",
    ]
    require_exact_keys(root, "$root", required)
    if root["schema_version"] != "2.1":
        fail("schema_version", "2.1が必要です")
    require_string(root["address"], "address", 5, 180)
    require_string(root["business"], "business", 1, 80)
    require_date(root["research_date"], "research_date")
    evaluation = require_object(root["evaluation"], "evaluation")
    require_exact_keys(evaluation, "evaluation", ["rating", "label", "confidence"])
    rating = evaluation["rating"]
    if not isinstance(rating, int) or isinstance(rating, bool) or rating not in RATING_LABELS:
        fail("evaluation.rating", "1〜5の整数が必要です")
    label = require_string(evaluation["label"], "evaluation.label", 1, 20)
    if label != RATING_LABELS[rating]:
        fail("evaluation.label", f"rating {rating}の表示は`{RATING_LABELS[rating]}`です")
    confidence = require_string(evaluation["confidence"], "evaluation.confidence", 1, 10)
    if confidence not in CONFIDENCE_VALUES:
        fail("evaluation.confidence", "high、medium、lowのいずれかが必要です")
    require_string(root["conclusion"], "conclusion", 1, 200)
    validate_string_list(root["assumptions"], "assumptions", 0, 3, 100)

    sources, known_sources = validate_sources(root["sources"])

    for key in ("strengths", "concerns"):
        items = require_list(root[key], key, 1, 3)
        for index, item in enumerate(items):
            validate_evidence_item(item, f"{key}[{index}]", known_sources)
    validate_string_list(root["flip_conditions"], "flip_conditions", 1, 3, 100)

    coverage = require_object(root["coverage"], "coverage")
    require_exact_keys(coverage, "coverage", ["axes_completed", "opened_source_count", "critical_unknown_count", "summary"])
    if coverage["axes_completed"] != 8:
        fail("coverage.axes_completed", "8が必要です")
    if coverage["opened_source_count"] != len(sources):
        fail("coverage.opened_source_count", "sources件数と一致させてください")
    require_string(coverage["summary"], "coverage.summary", 1, 120)

    validate_baselines(root["baselines"], known_sources)
    validate_axes(root["research_axes"], known_sources)

    industry = require_object(root["industry_analysis"], "industry_analysis")
    industry_fields = [
        "lens", "customer_purpose", "movement_mode", "demand_periods", "direct_competition",
        "substitute_competition", "synergies", "fit_observations", "competition_observations",
    ]
    require_exact_keys(industry, "industry_analysis", industry_fields)
    require_string(industry["lens"], "industry_analysis.lens", 1, 100)
    require_string(industry["customer_purpose"], "industry_analysis.customer_purpose", 1, 100)
    require_string(industry["movement_mode"], "industry_analysis.movement_mode", 1, 50)
    validate_string_list(industry["demand_periods"], "industry_analysis.demand_periods", 0, 4, 60)
    for key in ("direct_competition", "substitute_competition", "synergies"):
        items = require_list(industry[key], f"industry_analysis.{key}", 0, 4)
        for index, item in enumerate(items):
            validate_evidence_item(item, f"industry_analysis.{key}[{index}]", known_sources)
    observation_groups: dict[str, list[dict[str, Any]]] = {}
    for key in ("fit_observations", "competition_observations"):
        items = require_list(industry[key], f"industry_analysis.{key}", 1, 4)
        observation_groups[key] = items
        for index, item in enumerate(items):
            validate_evidence_item(item, f"industry_analysis.{key}[{index}]", known_sources)
    fit_titles = {item["title"].strip() for item in observation_groups["fit_observations"]}
    competition_titles = {
        item["title"].strip() for item in observation_groups["competition_observations"]
    }
    fit_details = {item["detail"].strip() for item in observation_groups["fit_observations"]}
    competition_details = {
        item["detail"].strip() for item in observation_groups["competition_observations"]
    }
    duplicated_titles = sorted(fit_titles & competition_titles)
    duplicated_details = sorted(fit_details & competition_details)
    if duplicated_titles or duplicated_details:
        duplicated = duplicated_titles or duplicated_details
        fail(
            "industry_analysis.competition_observations",
            "業態適合所見と同じ所見を再掲できません: " + "、".join(duplicated),
        )

    risks = require_object(root["risks"], "risks")
    require_exact_keys(risks, "risks", ["confirmed_blockers", "conflicts", "critical_unknowns"])
    risk_limits = {"confirmed_blockers": 3, "conflicts": 3, "critical_unknowns": 5}
    for key, maximum in risk_limits.items():
        items = require_list(risks[key], f"risks.{key}", 0, maximum)
        for index, item in enumerate(items):
            validate_evidence_item(item, f"risks.{key}[{index}]", known_sources)
    if coverage["critical_unknown_count"] != len(risks["critical_unknowns"]):
        fail("coverage.critical_unknown_count", "risks.critical_unknowns件数と一致させてください")

    validate_string_list(root["field_checks"], "field_checks", 5, 5, 90)
    additional = require_list(root["additional_data"], "additional_data", 1, 3)
    for index, raw in enumerate(additional):
        path = f"additional_data[{index}]"
        obj = require_object(raw, path)
        require_exact_keys(obj, path, ["name", "method", "decision_use"])
        require_string(obj["name"], f"{path}.name", 1, 50)
        require_string(obj["method"], f"{path}.method", 1, 90)
        require_string(obj["decision_use"], f"{path}.decision_use", 1, 90)

    blockers = risks["confirmed_blockers"]
    if any(item["status"] != "confirmed" for item in blockers):
        fail("risks.confirmed_blockers", "blockerはすべてconfirmedにしてください")
    if blockers and rating != 1:
        fail("evaluation.rating", "地点一致したconfirmed blockerがある場合は1にしてください")
    if rating == 1 and not blockers:
        fail("evaluation.rating", "1には地点一致したconfirmed blockerが必要です")

    axis_by_id = {item["id"]: item for item in root["research_axes"]}
    supported_axes = sum(
        item["status"] in {"confirmed", "estimated"}
        for item in root["research_axes"]
    )
    if rating >= 4:
        for axis_id in ("R2", "R3", "R4"):
            if axis_by_id[axis_id]["status"] not in {"confirmed", "estimated"}:
                fail("evaluation.rating", f"4以上には{axis_id}の確認済みまたは推定根拠が必要です")
        if supported_axes < 5:
            fail("evaluation.rating", "4以上には主要8軸中5軸以上の確認済みまたは推定根拠が必要です")
    if rating == 5:
        if supported_axes < 7 or risks["critical_unknowns"] or risks["conflicts"]:
            fail("evaluation.rating", "5には7軸以上の根拠と、critical unknown・不一致0件が必要です")
    if rating == 4 and len(risks["critical_unknowns"]) > 1:
        fail("evaluation.rating", "4では結論反転級の未確認を1件以内にしてください")
    if rating == 2 and not any(
        item["status"] in {"confirmed", "estimated"} for item in root["concerns"]
    ):
        fail("evaluation.rating", "2には確認済みまたは推定の不利な材料が必要です")

    expected_confidence = derive_confidence(rating, root["research_axes"], risks)
    if confidence != expected_confidence:
        fail(
            "evaluation.confidence",
            f"根拠状態から`{expected_confidence}`を設定してください",
        )

    def walk(value: Any, path: str = "$root") -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                if key.lower() in FORBIDDEN_KEYS:
                    fail(f"{path}.{key}", "score、rank、weight等のfieldは使用できません")
                walk(child, f"{path}.{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, f"{path}[{index}]")
        elif isinstance(value, str):
            require_string(value, path, 0, 10_000)

    walk(root)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report_json", type=Path, help="Report JSON path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        raw = args.report_json.read_text(encoding="utf-8")
        data = json.loads(raw)
        validate_report(data)
    except (OSError, json.JSONDecodeError, ValidationError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    print(
        f"VALID: schema 2.1 / rating {data['evaluation']['rating']}/5 / "
        f"confidence {data['evaluation']['confidence']} / {len(data['sources'])} sources / 8 axes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
