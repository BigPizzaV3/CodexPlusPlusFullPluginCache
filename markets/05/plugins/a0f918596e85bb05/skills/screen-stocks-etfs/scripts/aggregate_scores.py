#!/usr/bin/env python3
"""Aggregate blind panel scores, debate revisions, and scenario sensitivity."""

import json
import math
import sys
from pathlib import Path

DEFAULT_WEIGHTS = {
    "portfolio_manager": 20,
    "global_macro_strategist": 15,
    "geopolitical_risk_analyst": 10,
    "market_strategist": 10,
    "fundamental_research_analyst": 25,
    "portfolio_construction_analyst": 20,
}

def load_payload(path: str) -> dict:
    if path == "-":
        return json.load(sys.stdin)
    with Path(path).open(encoding="utf-8") as handle:
        return json.load(handle)

def validate_weights(weights: dict) -> None:
    if abs(sum(float(value) for value in weights.values()) - 100) > 0.001:
        raise ValueError("Committee weights must total 100")

def merged_scores(candidate: dict, include_revisions: bool) -> dict:
    scores = dict(candidate.get("judge_scores", {}))
    if include_revisions:
        scores.update(candidate.get("post_debate_judge_scores", {}))
    return scores

def score_snapshot(candidate: dict, weights: dict, include_revisions: bool, require_complete_panel: bool) -> dict:
    observations = []
    scores = merged_scores(candidate, include_revisions)
    missing_members = [member for member in weights if member not in scores]
    if require_complete_panel and missing_members:
        names = ", ".join(missing_members)
        raise ValueError(f"Incomplete Full Panel for {candidate['ticker']}; missing: {names}")
    for member, weight in weights.items():
        result = scores.get(member)
        if not result or result.get("abstain"):
            continue
        score = float(result["score"])
        confidence = float(result.get("confidence", 0.5))
        if not 0 <= score <= 10 or not 0 <= confidence <= 1:
            raise ValueError(f"Invalid score/confidence for {candidate['ticker']}:{member}")
        effective_weight = float(weight) * confidence
        observations.append({"committee_member": member, "score": score, "effective_weight": effective_weight})
    if not observations:
        return {"status": "insufficient_data"}
    weight_sum = sum(item["effective_weight"] for item in observations)
    mean = sum(item["score"] * item["effective_weight"] for item in observations) / weight_sum
    variance = sum(item["effective_weight"] * (item["score"] - mean) ** 2 for item in observations) / weight_sum
    disagreement = math.sqrt(variance)
    missing = int(candidate.get("missing_critical_data", 0))
    hard_gate = candidate.get("hard_gate", "pass")
    disagreement_penalty = 0.35 * disagreement
    missing_data_penalty = 0.50 * missing
    gate_penalty = 0.0
    final = max(0.0, min(10.0, mean - disagreement_penalty - missing_data_penalty))
    if hard_gate == "fail":
        final = 0.0
    elif hard_gate == "caution":
        gate_penalty = 0.5
        final = max(0.0, final - gate_penalty)
    high = max(observations, key=lambda item: item["score"])
    low = min(observations, key=lambda item: item["score"])
    return {
        "status": "scored",
        "final_score": round(final, 2),
        "confidence_weighted_mean": round(mean, 2),
        "committee_disagreement": round(disagreement, 2),
        "disagreement_penalty": round(disagreement_penalty, 2),
        "missing_data_penalty": round(missing_data_penalty, 2),
        "gate_penalty": round(gate_penalty, 2),
        "score_equation": (
            f"{mean:.2f} - {disagreement_penalty:.2f} - {missing_data_penalty:.2f} - {gate_penalty:.2f} = {final:.2f}"
            if hard_gate != "fail" else f"hard gate failed; final score = {final:.2f}"
        ),
        "highest_member": high["committee_member"],
        "highest_score": round(high["score"], 2),
        "lowest_member": low["committee_member"],
        "lowest_score": round(low["score"], 2),
        "hard_gate": hard_gate,
        "missing_critical_data": missing,
        "members_scored": len(observations),
        "members_abstained": len(weights) - len(observations),
    }

def scenario_summary(candidate: dict) -> dict:
    scenarios = candidate.get("scenario_scores", {})
    if not scenarios:
        return {}
    values = []
    weighted_total = 0.0
    probability_total = 0.0
    for name, entry in scenarios.items():
        if isinstance(entry, dict):
            score = float(entry["score"])
            probability = entry.get("probability")
        else:
            score = float(entry)
            probability = None
        if not 0 <= score <= 10:
            raise ValueError(f"Invalid scenario score for {candidate['ticker']}:{name}")
        values.append(score)
        if probability is not None:
            probability = float(probability)
            if not 0 <= probability <= 1:
                raise ValueError(f"Invalid scenario probability for {candidate['ticker']}:{name}")
            weighted_total += score * probability
            probability_total += probability
    average = weighted_total / probability_total if probability_total > 0 else sum(values) / len(values)
    return {
        "scenario_average": round(average, 2),
        "scenario_low": round(min(values), 2),
        "scenario_high": round(max(values), 2),
        "scenario_sensitivity": round(max(values) - min(values), 2),
    }

def aggregate(candidate: dict, weights: dict, require_complete_panel: bool) -> dict:
    baseline = score_snapshot(candidate, weights, include_revisions=False, require_complete_panel=require_complete_panel)
    if baseline["status"] != "scored":
        return {"ticker": candidate["ticker"], "status": "insufficient_data"}
    has_revisions = bool(candidate.get("post_debate_judge_scores"))
    revised = score_snapshot(candidate, weights, include_revisions=True, require_complete_panel=require_complete_panel) if has_revisions else baseline
    result = {
        "ticker": candidate["ticker"],
        "status": "scored",
        **revised,
        "baseline_score": baseline["final_score"],
        "debate_delta": round(revised["final_score"] - baseline["final_score"], 2),
    }
    result.update(scenario_summary(candidate))
    return result

def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: aggregate_scores.py <scores.json|->")
    payload = load_payload(sys.argv[1])
    weights = payload.get("weights", DEFAULT_WEIGHTS)
    validate_weights(weights)
    mode = payload.get("mode", "quick_scan")
    require_complete_panel = mode in {"full_panel", "panel_debate"}
    ranked = [aggregate(candidate, weights, require_complete_panel) for candidate in payload["candidates"]]
    ranked.sort(key=lambda item: item.get("final_score", -1), reverse=True)
    json.dump({"ranking": ranked}, sys.stdout, indent=2)
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()
