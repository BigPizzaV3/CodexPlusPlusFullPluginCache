#!/usr/bin/env python3
"""Prepare and score privacy-preserving blinded Empire utility evaluations."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


class EvaluationError(Exception):
    pass


ROUTES = ("codex_alone", "codex_plus_empire")


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise EvaluationError(f"Unable to read evaluation JSON: {path}") from exc
    if not isinstance(value, dict):
        raise EvaluationError("Evaluation input must be a JSON object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def candidate_id(seed: str, task_id: str, response_hash: str) -> str:
    digest = hashlib.sha256(
        f"{seed}\0{task_id}\0{response_hash}".encode("utf-8")
    ).hexdigest()[:20]
    return f"candidate-{digest}"


def validate_plan(plan: dict[str, Any]) -> tuple[list[str], dict[str, float]]:
    tasks = plan.get("tasks")
    thresholds = plan.get("thresholds")
    if plan.get("schema_version") != 1 or not isinstance(tasks, list):
        raise EvaluationError("Evaluation plan schema is invalid")
    raw_task_ids = [item.get("id") for item in tasks if isinstance(item, dict)]
    if len(raw_task_ids) < 5 or any(
        not isinstance(item, str) or not item for item in raw_task_ids
    ):
        raise EvaluationError("Evaluation plan requires at least five named tasks")
    task_ids = [item for item in raw_task_ids if isinstance(item, str)]
    if len(set(task_ids)) != len(task_ids):
        raise EvaluationError("Evaluation task IDs must be unique")
    if not isinstance(thresholds, dict):
        raise EvaluationError("Evaluation thresholds are missing")
    required = (
        "minimum_verified_finding_gain",
        "maximum_false_positive_delta",
        "minimum_actionable_rate",
        "maximum_cost_per_task_usd",
    )
    parsed: dict[str, float] = {}
    for key in required:
        value = thresholds.get(key)
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise EvaluationError(f"Invalid threshold: {key}")
        parsed[key] = float(value)
    return task_ids, parsed


def prepare(
    plan: dict[str, Any], runs: dict[str, Any]
) -> tuple[dict[str, Any], dict[str, Any]]:
    task_ids, _ = validate_plan(plan)
    seed = runs.get("blinding_seed")
    records = runs.get("runs")
    if not isinstance(seed, str) or len(seed) < 16 or not isinstance(records, list):
        raise EvaluationError("Run manifest requires a private blinding seed and runs")
    by_task: dict[str, dict[str, dict[str, Any]]] = {}
    for item in records:
        if not isinstance(item, dict):
            raise EvaluationError("Run entries must be objects")
        task_id = item.get("task_id")
        route = item.get("route")
        response_hash = item.get("response_hash")
        if task_id not in task_ids or route not in ROUTES:
            raise EvaluationError("Run entry has an unknown task or route")
        if not isinstance(response_hash, str) or not response_hash.startswith("sha256:"):
            raise EvaluationError("Run response hashes must be SHA-256 references")
        by_task.setdefault(task_id, {})[route] = item
    if any(set(by_task.get(task_id, {})) != set(ROUTES) for task_id in task_ids):
        raise EvaluationError("Every task requires both evaluation routes")

    candidates: list[dict[str, Any]] = []
    mapping: list[dict[str, Any]] = []
    for task_id in task_ids:
        for route in ROUTES:
            item = by_task[task_id][route]
            opaque = candidate_id(seed, task_id, item["response_hash"])
            candidates.append(
                {
                    "candidate_id": opaque,
                    "task_id": task_id,
                    "response_hash": item["response_hash"],
                    "response_artifact": f"{opaque}.md",
                }
            )
            mapping.append(
                {
                    "candidate_id": opaque,
                    "task_id": task_id,
                    "route": route,
                    "latency_ms": item.get("latency_ms"),
                    "cost_usd": item.get("cost_usd"),
                    "source_response_artifact": item.get("response_artifact"),
                }
            )
    candidates.sort(key=lambda item: item["candidate_id"])
    return (
        {
            "schema_version": 1,
            "evaluation_id": plan.get("evaluation_id"),
            "blind": True,
            "candidate_count": len(candidates),
            "candidates": candidates,
            "instructions": plan.get("adjudication_instructions"),
        },
        {
            "schema_version": 1,
            "evaluation_id": plan.get("evaluation_id"),
            "private": True,
            "mapping": mapping,
        },
    )


def _average(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def score(
    plan: dict[str, Any], mapping: dict[str, Any], judgments: dict[str, Any]
) -> dict[str, Any]:
    task_ids, thresholds = validate_plan(plan)
    if mapping.get("private") is not True or judgments.get("blind") is not True:
        raise EvaluationError("Scoring requires a private mapping and blind judgments")
    if judgments.get("independent_adjudicator") is not True:
        raise EvaluationError("The adjudicator must be independent of production routing")
    map_rows = mapping.get("mapping")
    judgment_rows = judgments.get("judgments")
    if not isinstance(map_rows, list) or not isinstance(judgment_rows, list):
        raise EvaluationError("Mapping or judgments are missing")
    mapped = {
        row.get("candidate_id"): row
        for row in map_rows
        if isinstance(row, dict) and row.get("route") in ROUTES
    }
    judged = {
        row.get("candidate_id"): row
        for row in judgment_rows
        if isinstance(row, dict)
    }
    if set(mapped) != set(judged) or len(mapped) != len(task_ids) * 2:
        raise EvaluationError("Every blinded candidate must be judged exactly once")

    aggregates: dict[str, dict[str, Any]] = {}
    for route in ROUTES:
        route_rows = [
            (mapped[candidate], judged[candidate])
            for candidate in mapped
            if mapped[candidate]["route"] == route
        ]
        verified = [float(judgment.get("verified_findings", 0)) for _, judgment in route_rows]
        false_positives = [
            float(judgment.get("false_positives", 0)) for _, judgment in route_rows
        ]
        actionable = [1.0 if judgment.get("actionable") is True else 0.0 for _, judgment in route_rows]
        costs = [float(row.get("cost_usd") or 0) for row, _ in route_rows]
        latencies = [float(row.get("latency_ms") or 0) for row, _ in route_rows]
        aggregates[route] = {
            "task_count": len(route_rows),
            "mean_verified_findings": round(_average(verified), 4),
            "mean_false_positives": round(_average(false_positives), 4),
            "actionable_rate": round(_average(actionable), 4),
            "mean_cost_usd": round(_average(costs), 6),
            "mean_latency_ms": round(_average(latencies), 2),
        }

    baseline = aggregates["codex_alone"]
    empire = aggregates["codex_plus_empire"]
    verified_gain = round(
        empire["mean_verified_findings"] - baseline["mean_verified_findings"], 4
    )
    false_positive_delta = round(
        empire["mean_false_positives"] - baseline["mean_false_positives"], 4
    )
    checks = {
        "complete_task_set": all(
            aggregates[route]["task_count"] == len(task_ids) for route in ROUTES
        ),
        "verified_finding_gain": verified_gain
        >= thresholds["minimum_verified_finding_gain"],
        "false_positive_delta": false_positive_delta
        <= thresholds["maximum_false_positive_delta"],
        "actionable_rate": empire["actionable_rate"]
        >= thresholds["minimum_actionable_rate"],
        "cost_ceiling": empire["mean_cost_usd"]
        <= thresholds["maximum_cost_per_task_usd"],
    }
    passed = all(checks.values())
    return {
        "schema_version": 1,
        "evaluation_id": plan.get("evaluation_id"),
        "executed_at": judgments.get("executed_at"),
        "blind": True,
        "independent_adjudicator": True,
        "task_count": len(task_ids),
        "routes": aggregates,
        "verified_finding_gain": verified_gain,
        "false_positive_delta": false_positive_delta,
        "thresholds": thresholds,
        "checks": checks,
        "raw_prompts_persisted": False,
        "raw_responses_persisted": False,
        "passed": passed,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    prepare_parser = sub.add_parser("prepare")
    prepare_parser.add_argument("--plan", type=Path, required=True)
    prepare_parser.add_argument("--runs", type=Path, required=True)
    prepare_parser.add_argument("--blind-output", type=Path, required=True)
    prepare_parser.add_argument("--mapping-output", type=Path, required=True)
    score_parser = sub.add_parser("score")
    score_parser.add_argument("--plan", type=Path, required=True)
    score_parser.add_argument("--mapping", type=Path, required=True)
    score_parser.add_argument("--judgments", type=Path, required=True)
    score_parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            blind, mapping = prepare(load_json(args.plan), load_json(args.runs))
            write_json(args.blind_output, blind)
            write_json(args.mapping_output, mapping)
            result = {"status": "prepared", "candidate_count": blind["candidate_count"]}
        else:
            result = score(
                load_json(args.plan),
                load_json(args.mapping),
                load_json(args.judgments),
            )
            write_json(args.output, result)
        print(json.dumps(result, indent=2))
        return 0
    except EvaluationError as exc:
        print(json.dumps({"status": "error", "error": str(exc)}, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
