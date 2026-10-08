#!/usr/bin/env python3
"""Reproducible Horizon Forge arithmetic. Standard library only; no network."""
from __future__ import annotations

import argparse
from datetime import date
import json
import math
from pathlib import Path
import sys

GROWTH = {"demand": .20, "adoption": .20, "feasibility": .20, "scale": .25, "resilience": .15}
OVERLOOKED = {"provision_gap": .25, "attention_gap": .20, "bottleneck": .20, "inflection": .20, "accessibility": .15}
CONFIDENCE = {"high", "medium", "low", "insufficient"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def number(value, label, low=None, high=None):
    require(type(value) in (int, float) and math.isfinite(value), f"{label}: finite number required")
    require(low is None or value >= low, f"{label}: below {low}")
    require(high is None or value <= high, f"{label}: above {high}")
    return value


def string(value, label):
    require(isinstance(value, str) and bool(value.strip()), f"{label}: nonempty string required")
    return value


def object_(value, label):
    require(isinstance(value, dict), f"{label}: object required")
    return value


def sequence(value, label):
    require(isinstance(value, list) and bool(value), f"{label}: nonempty array required")
    return value


def iso_date(value, label):
    string(value, label)
    try:
        result = date.fromisoformat(value)
    except ValueError:
        raise ValueError(f"{label}: ISO date YYYY-MM-DD required") from None
    require(result.isoformat() == value, f"{label}: ISO date YYYY-MM-DD required")
    return result


def weights(value, default):
    result = default.copy() if value is None else object_(value, "weights").copy()
    require(set(result) == set(default), "weight keys must match rubric exactly")
    for key, val in result.items():
        number(val, f"weight {key}", 0)
    require(math.isclose(sum(result.values()), 1, rel_tol=0, abs_tol=1e-9), "weights must sum to 1")
    return result


def rating(components, rubric):
    object_(components, "components")
    require(set(components) == set(rubric), "component keys must match rubric exactly; use null for unknown")
    known, covered = 0., 0.
    missing = []
    for key, weight in rubric.items():
        val = components[key]
        if val is None:
            missing.append(key)
        else:
            known += weight * number(val, key, 0, 5)
            covered += weight
    lower = 20 * known
    upper = lower + 100 * (1 - covered)
    return {"score": round(lower, 2) if not missing else None,
            "bounds": [round(lower, 2), round(upper, 2)],
            "coverage": round(covered, 6), "missing": missing}


def scores(payload):
    object_(payload, "input")
    gw = weights(payload.get("growth_weights"), GROWTH)
    ow = weights(payload.get("overlooked_weights"), OVERLOOKED)
    scope = string(payload.get("comparison_scope"), "comparison_scope")
    rows, seen = [], set()
    candidates = sequence(payload.get("candidates"), "candidates")
    for item in candidates:
        object_(item, "candidate")
        name = string(item.get("name"), "candidate name")
        require(name not in seen, f"duplicate candidate: {name}")
        seen.add(name)
        confidence = item.get("confidence")
        require(confidence in CONFIDENCE, "invalid confidence label")
        growth = rating(item.get("growth"), gw)
        overlooked = rating(item.get("overlooked"), ow)
        notes = object_(item.get("rationale"), "rationale")
        for key, val in {**item["growth"], **item["overlooked"]}.items():
            if val is not None:
                string(notes.get(key), f"rationale.{key}")
        reason = string(item.get("confidence_reason"), "confidence_reason")
        eligible = not growth["missing"] and confidence in {"high", "medium"}
        rows.append({"name": name, "growth": growth, "overlooked": overlooked,
                     "confidence": confidence, "confidence_reason": reason,
                     "rationale": notes, "ranking_status": "eligible" if eligible else "provisional",
                     "rank": None, "weight_sensitivity_rank_range": None})
    eligible = [r for r in rows if r["ranking_status"] == "eligible"]
    raw = {c["name"]: c["growth"] for c in candidates}
    variants = [gw]
    for key in gw:
        for factor in (.5, 1.5):
            changed = gw.copy()
            changed[key] *= factor
            total = sum(changed.values())
            if total:
                variants.append({k: v / total for k, v in changed.items()})
    ranks = {r["name"]: [] for r in eligible}
    for i, variant in enumerate(variants):
        values = {r["name"]: 20 * sum(variant[k] * raw[r["name"]][k] for k in variant) for r in eligible}
        for row in eligible:
            val = values[row["name"]]
            rank = 1 + sum(v > val + 1e-9 for v in values.values())
            ranks[row["name"]].append(rank)
            if i == 0:
                row["rank"] = rank
    for row in eligible:
        rr = ranks[row["name"]]
        row["weight_sensitivity_rank_range"] = [min(rr), max(rr)]
    rows.sort(key=lambda r: (r["rank"] is None, r["rank"] or 0, r["name"]))
    return {"rubric_version": "1.0", "comparison_scope": scope, "growth_weights": gw,
            "overlooked_weights": ow, "candidates": rows,
            "sensitivity_variants": len(variants),
            "notes": ["Ratings are judgment indices, not probabilities.",
                      "Missing growth inputs and low/insufficient confidence are excluded from main ranking.",
                      "Rank sensitivity tests weights only, not uncertainty in evidence or economic assumptions.",
                      "Rationales are preserved but factual support must be audited by the research agent."]}


def cagr(base, terminal, years):
    if base == 0:
        return None
    return (terminal / base) ** (1 / years) - 1


def scenarios(payload):
    object_(payload, "input")
    for key in ("market", "geography", "metric", "currency", "units", "price_basis", "baseline_source"):
        string(payload.get(key), key)
    for key in ("baseline_year", "horizon_year"):
        require(type(payload.get(key)) is int and 1 <= payload[key] <= 9999, f"{key}: year integer required")
    years = payload["horizon_year"] - payload["baseline_year"]
    require(years > 0, "horizon_year must follow baseline_year")
    base = number(payload.get("baseline_size"), "baseline_size", 0)
    mode = payload.get("mode")
    require(mode in {"weighted", "exploratory"}, "mode must be weighted or exploratory")
    if mode == "weighted":
        require(payload.get("partition_confirmed") is True, "weighted scenarios require partition_confirmed=true")
        string(payload.get("partition_definition"), "partition_definition")
    seen, rows = set(), []
    for item in sequence(payload.get("scenarios"), "scenarios"):
        object_(item, "scenario")
        name = string(item.get("name"), "scenario name")
        require(name not in seen, "duplicate scenario name")
        seen.add(name)
        terminal = number(item.get("terminal_size"), "terminal_size", 0)
        assumption = string(item.get("assumptions"), "assumptions")
        probability = item.get("probability")
        if mode == "weighted":
            number(probability, "probability", 0, 1)
            string(item.get("probability_basis"), "probability_basis")
        else:
            require(probability is None, "exploratory scenarios must not supply probabilities")
        rows.append({"name": name, "terminal_size": terminal, "probability": probability,
                     "added_annual_size": terminal - base, "cagr": cagr(base, terminal, years),
                     "assumptions": assumption, "probability_basis": item.get("probability_basis")})
    expected = None
    if mode == "weighted":
        require(math.isclose(sum(r["probability"] for r in rows), 1, rel_tol=0, abs_tol=1e-9), "scenario probabilities must sum to 1")
        end = sum(r["probability"] * r["terminal_size"] for r in rows)
        expected = {"terminal_size": end, "added_annual_size": end - base,
                    "cagr_of_expected_terminal_size": cagr(base, end, years),
                    "expected_cagr": None if base == 0 else sum(r["probability"] * r["cagr"] for r in rows)}
    metadata = {k: v for k, v in payload.items() if k != "scenarios"}
    return {"basis": metadata, "scenarios": rows, "expected": expected,
            "notes": ["Weighted terminal sizes must represent conditional means within an exhaustive non-overlapping partition.",
                      "Scenario ranges are not statistical confidence intervals; CAGR is undefined from zero baseline.",
                      "Event probability is not inferred from scenario means."]}


def calibrate(payload):
    object_(payload, "input")
    cutoff = iso_date(payload.get("evaluation_date"), "evaluation_date")
    policy = string(payload.get("vintage_policy"), "vintage_policy")
    sequence(payload.get("forecasts"), "forecasts")
    seen, resolved, pending = set(), [], []
    for item in payload["forecasts"]:
        object_(item, "forecast")
        event = string(item.get("event_id"), "event_id")
        require(event not in seen, "duplicate event_id: select one forecast vintage per event")
        seen.add(event)
        p = number(item.get("probability"), "probability", 0, 1)
        forecast_date = iso_date(item.get("forecast_date"), "forecast_date")
        deadline = iso_date(item.get("deadline"), "deadline")
        require(forecast_date <= cutoff and forecast_date < deadline, "forecast must precede deadline and not follow evaluation date")
        string(item.get("question"), "question")
        string(item.get("resolution_rule"), "resolution_rule")
        outcome = item.get("outcome")
        bp = item.get("baseline_probability")
        if bp is not None:
            number(bp, "baseline_probability", 0, 1)
        if outcome is None:
            pending.append(event)
            continue
        require(type(outcome) is int and outcome in (0, 1), "outcome must be 0, 1, or null")
        resolved_on = iso_date(item.get("resolved_on"), "resolved_on")
        require(forecast_date < resolved_on <= cutoff, "resolution must follow forecast and be no later than evaluation date")
        # Resolution before the deadline can be legitimate for an occurrence-by-date event.
        string(item.get("resolution_source"), "resolution_source")
        resolved.append({"event_id": event, "probability": p, "outcome": outcome,
                         "brier": (p - outcome) ** 2,
                         "baseline_brier": None if bp is None else (bp - outcome) ** 2,
                         "lead_days": (deadline - forecast_date).days})
    n = len(resolved)
    brier = sum(r["brier"] for r in resolved) / n if n else None
    comparable = [r for r in resolved if r["baseline_brier"] is not None]
    comparator = None
    if comparable:
        count = len(comparable)
        model_mean = sum(r["brier"] for r in comparable) / count
        baseline_mean = sum(r["baseline_brier"] for r in comparable) / count
        comparator = {"n": count, "model_brier_same_subset": model_mean,
                      "baseline_brier_same_subset": baseline_mean,
                      "skill_score": None if baseline_mean == 0 else 1 - model_mean / baseline_mean}
    bins = []
    for index in range(5):
        members = [r for r in resolved if min(int(r["probability"] * 5), 4) == index]
        if members:
            bins.append({"lower": index / 5, "upper": (index + 1) / 5, "n": len(members),
                         "mean_probability": sum(r["probability"] for r in members) / len(members),
                         "observed_frequency": sum(r["outcome"] for r in members) / len(members)})
    return {"evaluation_date": cutoff.isoformat(), "vintage_policy": policy,
            "resolved_count": n, "pending_count": len(pending), "pending_event_ids": pending,
            "brier": brier, "comparator": comparator, "reliability_bins": bins,
            "resolved_events": resolved,
            "notes": ["Brier score: mean squared probability error; lower is better (binary convention 0 to 1).",
                      "Bins are descriptive; small samples and correlated events do not establish calibration.",
                      "Select comparable lead times; truthful outcome resolution and source support require external audit."]}


def reject_constant(value):
    raise ValueError(f"invalid JSON numeric constant: {value}")


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("scores", "scenarios", "calibrate"))
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8-sig"), parse_constant=reject_constant, object_pairs_hook=unique_keys)
        result = {"scores": scores, "scenarios": scenarios, "calibrate": calibrate}[args.mode](payload)
        rendered = json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
        if args.output:
            # Avoid silently destroying evidence or a previous forecast.
            with args.output.open("x", encoding="utf-8") as handle:
                handle.write(rendered)
        else:
            print(rendered, end="")
    except (ValueError, OSError, OverflowError, TypeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
