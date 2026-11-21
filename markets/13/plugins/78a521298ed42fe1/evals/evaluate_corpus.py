"""Validate the golden prompt corpus and score supplied ChatGPT traces offline."""

from __future__ import annotations

import argparse
import json
import math
import statistics
from datetime import date
from pathlib import Path
from typing import Any, Iterable

CORPUS_PATH = Path(__file__).with_name("eval_corpus.json")
EXPECTED_CATEGORY_COUNTS = {"direct": 30, "indirect": 30, "ambiguous": 20, "negative": 20}
EXPECTED_TOOL_NAMES = frozenset(
    {
        "search_flights",
        "search_hotels",
        "get_hotel_details",
        "get_hotel_rooms",
        "find_places",
        "create_itinerary",
        "save_trip",
        "get_saved_trip",
    }
)
EXPECTED_OUTCOME_BY_CATEGORY = {
    "direct": "call",
    "indirect": "call",
    "ambiguous": "clarify",
    "negative": "no_action",
}
VALID_OUTCOMES = frozenset({"call", "clarify", "no_action"})


def load_corpus(path: Path = CORPUS_PATH) -> dict[str, Any]:
    """Load the machine-readable fixture source from JSON."""
    try:
        with path.open("r", encoding="utf-8") as stream:
            corpus = json.load(stream)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid corpus JSON in {path}: {exc.msg}") from exc
    if not isinstance(corpus, dict):
        raise ValueError("Corpus root must be a JSON object")
    return corpus


def validate_corpus(corpus: dict[str, Any] | None = None) -> dict[str, Any]:
    """Validate corpus shape/counts only; this is not model-quality evidence."""
    corpus = load_corpus() if corpus is None else corpus
    if corpus.get("schema_version") != 1:
        raise ValueError("Unsupported corpus schema_version; expected 1")
    evaluation_date = corpus.get("evaluation_date")
    if not isinstance(evaluation_date, str):
        raise ValueError("Corpus needs an ISO evaluation_date")
    try:
        date.fromisoformat(evaluation_date)
    except ValueError as exc:
        raise ValueError("Corpus evaluation_date must be an ISO date") from exc
    if set(corpus.get("tool_names", [])) != EXPECTED_TOOL_NAMES:
        raise ValueError("Corpus tool_names must contain exactly the eight supported tools")
    if corpus.get("category_counts") != EXPECTED_CATEGORY_COUNTS:
        raise ValueError(f"Expected category counts {EXPECTED_CATEGORY_COUNTS}")

    fixtures = corpus.get("fixtures")
    if not isinstance(fixtures, list):
        raise ValueError("Corpus fixtures must be a JSON array")
    counts: dict[str, int] = {}
    ids: set[str] = set()
    prompts: set[str] = set()
    expected_context = (
        f"Evaluation reference date: {evaluation_date}. Resolve relative dates against "
        "this fixed date, not the current wall clock. This context is for offline "
        "evaluation and does not imply that provider searches will be replayed."
    )

    for fixture in fixtures:
        if not isinstance(fixture, dict):
            raise ValueError("Every fixture must be a JSON object")
        fixture_id = fixture.get("id")
        if not isinstance(fixture_id, str) or not fixture_id:
            raise ValueError("Every fixture needs a non-empty string id")
        if fixture_id in ids:
            raise ValueError(f"Duplicate fixture id: {fixture_id}")
        ids.add(fixture_id)

        category = fixture.get("category")
        if category not in EXPECTED_CATEGORY_COUNTS:
            raise ValueError(f"Fixture {fixture_id} has an invalid category")
        counts[category] = counts.get(category, 0) + 1
        prompt = fixture.get("prompt")
        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError(f"Fixture {fixture_id} has no prompt")
        if prompt in prompts:
            raise ValueError(f"Duplicate fixture prompt: {fixture_id}")
        prompts.add(prompt)
        if fixture.get("evaluation_context") != expected_context:
            raise ValueError(f"Fixture {fixture_id} does not use the fixed evaluation date context")

        outcome = fixture.get("expected_outcome")
        sequence = fixture.get("expected_tool_sequence")
        required = fixture.get("required_inputs")
        criteria = fixture.get("quality_criteria")
        if outcome not in VALID_OUTCOMES or outcome != EXPECTED_OUTCOME_BY_CATEGORY[category]:
            raise ValueError(f"Fixture {fixture_id} has an invalid outcome for {category}")
        if not isinstance(sequence, list) or any(tool not in EXPECTED_TOOL_NAMES for tool in sequence):
            raise ValueError(f"Fixture {fixture_id} has an invalid tool sequence")
        if (outcome == "call") != bool(sequence):
            raise ValueError(f"Fixture {fixture_id} has an inconsistent outcome and tool sequence")
        if not isinstance(required, list) or any(not isinstance(value, str) or not value for value in required):
            raise ValueError(f"Fixture {fixture_id} has invalid required_inputs")
        if category != "negative" and not required:
            raise ValueError(f"Fixture {fixture_id} must document required inputs")
        if not isinstance(criteria, list) or len(criteria) < 2 or any(not isinstance(value, str) or not value for value in criteria):
            raise ValueError(f"Fixture {fixture_id} needs at least two quality criteria")

    if len(fixtures) != 100:
        raise ValueError(f"Expected exactly 100 fixtures, found {len(fixtures)}")
    if counts != EXPECTED_CATEGORY_COUNTS:
        raise ValueError(f"Expected category counts {EXPECTED_CATEGORY_COUNTS}, found {counts}")
    return {
        "status": "passed",
        "fixture_count": len(fixtures),
        "category_counts": counts,
        "unique_ids": len(ids),
        "unique_prompts": len(prompts),
        "evaluation_date": evaluation_date,
        "evidence_scope": "fixture structure only; no live model or provider performance measured",
    }


def evaluate_trace_rows(
    trace_rows: Iterable[dict[str, Any]],
    corpus: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Score caller-supplied trace data; provenance is not independently verified."""
    corpus = load_corpus() if corpus is None else corpus
    validate_corpus(corpus)
    fixtures = corpus["fixtures"]
    fixture_by_id = {fixture["id"]: fixture for fixture in fixtures}

    normalized: list[tuple[dict[str, Any], list[str], str, float, bool, str]] = []
    seen: set[str] = set()
    for trace in trace_rows:
        if not isinstance(trace, dict):
            raise ValueError("Each trace row must be a JSON object")
        fixture_id = trace.get("fixture_id")
        if not isinstance(fixture_id, str) or fixture_id not in fixture_by_id:
            raise ValueError(f"Unknown fixture_id in trace: {fixture_id!r}")
        if fixture_id in seen:
            raise ValueError(f"Duplicate trace for fixture_id: {fixture_id}")
        seen.add(fixture_id)

        sequence = trace.get("tool_sequence")
        outcome = trace.get("observed_outcome")
        latency = trace.get("latency_ms")
        completed = trace.get("completed")
        completion_output = trace.get("completion_output")
        if not isinstance(sequence, list) or any(not isinstance(tool, str) or not tool for tool in sequence):
            raise ValueError(f"Trace {fixture_id} needs tool_sequence as a list of tool names")
        if outcome not in VALID_OUTCOMES:
            raise ValueError(f"Trace {fixture_id} has an invalid observed_outcome")
        if isinstance(latency, bool) or not isinstance(latency, (int, float)) or not math.isfinite(latency) or latency < 0:
            raise ValueError(f"Trace {fixture_id} needs a non-negative finite latency_ms")
        if not isinstance(completed, bool):
            raise ValueError(f"Trace {fixture_id} needs a boolean completed field")
        if not isinstance(completion_output, str):
            raise ValueError(f"Trace {fixture_id} needs completion_output as a string")
        normalized.append(
            (fixture_by_id[fixture_id], sequence, outcome, float(latency), completed, completion_output)
        )

    expected_call_rows = [row for row in normalized if row[0]["expected_outcome"] == "call"]
    activated_rows = [
        row for row in expected_call_rows
        if any(tool in row[1] for tool in row[0]["expected_tool_sequence"])
    ]
    missed_activation_ids = [
        row[0]["id"] for row in expected_call_rows
        if not any(tool in row[1] for tool in row[0]["expected_tool_sequence"])
    ]
    incorrect_tool_choice_ids = [
        expected["id"] for expected, actual, *_ in normalized
        if actual != expected["expected_tool_sequence"]
    ]
    outcome_mismatch_ids = [
        expected["id"] for expected, _, actual_outcome, *_ in normalized
        if actual_outcome != expected["expected_outcome"]
    ]
    unexpected_tool_ids = [
        expected["id"] for expected, actual, *_ in normalized
        if expected["expected_outcome"] != "call" and bool(actual)
    ]

    category_metrics: dict[str, Any] = {}
    for category in EXPECTED_CATEGORY_COUNTS:
        all_category_fixtures = [fixture for fixture in fixtures if fixture["category"] == category]
        category_expected = [row for row in normalized if row[0]["category"] == category]
        category_calls = [row for row in category_expected if row[0]["expected_outcome"] == "call"]
        expected_call_fixtures = [
            fixture for fixture in all_category_fixtures if fixture["expected_outcome"] == "call"
        ]
        category_activated = [
            row for row in category_calls
            if any(tool in row[1] for tool in row[0]["expected_tool_sequence"])
        ]
        category_missed = [
            row[0]["id"] for row in category_calls
            if not any(tool in row[1] for tool in row[0]["expected_tool_sequence"])
        ]
        category_incorrect = [
            expected["id"] for expected, actual, *_ in category_expected
            if actual != expected["expected_tool_sequence"]
        ]
        category_exact = len(category_expected) - len(category_incorrect)
        category_metrics[category] = {
            "fixture_count": len(all_category_fixtures),
            "expected_call_fixtures": len(expected_call_fixtures),
            "trace_count": len(category_expected),
            "traced_expected_call_fixtures": len(category_calls),
            "activated_fixtures": len(category_activated),
            "missed_activation_ids": category_missed,
            "activation_rate": len(category_activated) / len(category_calls) if category_calls else None,
            "activation_coverage": (
                len(category_activated) / len(expected_call_fixtures)
                if expected_call_fixtures
                else None
            ),
            "untraced_expected_call_ids": sorted(
                {fixture["id"] for fixture in expected_call_fixtures}
                - {row[0]["id"] for row in category_calls}
            ),
            "incorrect_tool_choice_ids": category_incorrect,
            "exact_tool_sequence_count": category_exact,
            "tool_sequence_accuracy": category_exact / len(category_expected) if category_expected else None,
        }

    exact_sequence_count = len(normalized) - len(incorrect_tool_choice_ids)
    exact_outcome_count = len(normalized) - len(outcome_mismatch_ids)
    latencies = [row[3] for row in normalized]
    sorted_latencies = sorted(latencies)
    p95_latency = (
        sorted_latencies[max(0, math.ceil(0.95 * len(sorted_latencies)) - 1)]
        if sorted_latencies
        else None
    )
    return {
        "evidence_scope": "caller-supplied traces only; provenance is not independently verified",
        "fixture_count": len(fixtures),
        "trace_count": len(normalized),
        "missing_trace_ids": sorted(set(fixture_by_id) - seen),
        "trace_coverage": len(normalized) / len(fixtures) if fixtures else 0.0,
        "expected_call_fixture_count": sum(
            fixture["expected_outcome"] == "call" for fixture in fixtures
        ),
        "expected_call_trace_count": len(expected_call_rows),
        "activation_count": len(activated_rows),
        "activation_rate": len(activated_rows) / len(expected_call_rows) if expected_call_rows else None,
        "activation_coverage": (
            len(activated_rows)
            / sum(fixture["expected_outcome"] == "call" for fixture in fixtures)
            if any(fixture["expected_outcome"] == "call" for fixture in fixtures)
            else None
        ),
        "missed_activation_ids": missed_activation_ids,
        "incorrect_tool_choice_ids": incorrect_tool_choice_ids,
        "unexpected_tool_call_ids": unexpected_tool_ids,
        "exact_tool_sequence_count": exact_sequence_count,
        "tool_sequence_accuracy": exact_sequence_count / len(normalized) if normalized else None,
        "outcome_mismatch_ids": outcome_mismatch_ids,
        "outcome_accuracy": exact_outcome_count / len(normalized) if normalized else None,
        "activation_by_category": category_metrics,
        "completed_count": sum(1 for row in normalized if row[4]),
        "completion_rate": sum(1 for row in normalized if row[4]) / len(normalized) if normalized else None,
        "completion_output_count": sum(1 for row in normalized if row[5].strip()),
        "completion_output_coverage": sum(1 for row in normalized if row[5].strip()) / len(normalized) if normalized else None,
        "latency_ms": {
            "sample_count": len(latencies),
            "mean": statistics.fmean(latencies) if latencies else None,
            "median": statistics.median(latencies) if latencies else None,
            "p95_nearest_rank": p95_latency,
        },
    }


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on {path}:{line_number}: {exc.msg}") from exc
            if not isinstance(row, dict):
                raise ValueError(f"Expected a JSON object on {path}:{line_number}")
            rows.append(row)
    return rows


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=CORPUS_PATH, help="Corpus JSON path")
    parser.add_argument(
        "--trace-file",
        type=Path,
        help="Optional JSONL file of caller-supplied recorded ChatGPT traces; no API calls are made.",
    )
    args = parser.parse_args(argv)
    corpus = load_corpus(args.corpus)
    report: dict[str, Any] = {
        "evaluation_mode": "offline trace scoring; no model or provider API calls are made",
        "fixture_validation": validate_corpus(corpus),
    }
    if args.trace_file:
        report["recorded_trace_evaluation"] = evaluate_trace_rows(_read_jsonl(args.trace_file), corpus)
    else:
        report["recorded_trace_evaluation"] = None
        report["live_evidence"] = "No trace file supplied; no live model or provider evaluation was performed."
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
