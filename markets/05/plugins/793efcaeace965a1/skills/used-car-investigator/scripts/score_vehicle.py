#!/usr/bin/env python3
"""Deterministic scoring helper for the Used Car Investigator skill.

Input JSON example:
{
  "engine": 12,
  "transmission": 10,
  "maintenance": 11,
  "history": 10,
  "condition": 7,
  "repairability": 8,
  "value": 8,
  "driving": 9,
  "fuel": 3,
  "penalties": [
    {"reason": "unresolved high-cost transmission tail risk", "points": 6}
  ]
}

All category values are points already bounded by their maxima.
"""

import json
import sys

MAXIMA = {
    "engine": 15,
    "transmission": 15,
    "maintenance": 15,
    "history": 12,
    "condition": 8,
    "repairability": 10,
    "value": 10,
    "driving": 10,
    "fuel": 5,
}


def verdict(score: float) -> str:
    if score >= 88:
        return "STRONG BUY"
    if score >= 78:
        return "BUY"
    if score >= 68:
        return "BUY IF PPI PASSES"
    if score >= 55:
        return "HIGH-RISK BUY"
    return "AVOID"


def verdict_options(score: float) -> list[str]:
    """Return the score-band choices allowed by scoring.md.

    The final selection still depends on price, evidence, and hard-risk gates.
    """
    if score >= 88:
        return ["STRONG BUY"]
    if score >= 78:
        return ["BUY"]
    if score >= 68:
        return ["BUY IF PPI PASSES", "NEGOTIATE"]
    if score >= 55:
        return ["NEGOTIATE", "HIGH-RISK BUY"]
    return ["AVOID"]


def main() -> None:
    raw = sys.stdin.read().strip()
    if not raw:
        raise SystemExit("Provide JSON on stdin.")
    data = json.loads(raw)

    category_scores = {}
    for key, max_points in MAXIMA.items():
        value = float(data.get(key, 0))
        if not 0 <= value <= max_points:
            raise ValueError(f"{key} must be between 0 and {max_points}")
        category_scores[key] = value

    subtotal = sum(category_scores.values())
    penalties = data.get("penalties", []) or []
    penalty_total = 0.0
    normalized_penalties = []
    for p in penalties:
        pts = abs(float(p.get("points", 0)))
        penalty_total += pts
        normalized_penalties.append({
            "reason": str(p.get("reason", "unspecified risk")),
            "points": pts,
        })

    final = max(0.0, min(100.0, subtotal - penalty_total))
    out = {
        "category_scores": category_scores,
        "subtotal": round(subtotal, 1),
        "penalties": normalized_penalties,
        "penalty_total": round(penalty_total, 1),
        "final_score": round(final, 1),
        "score_band_verdict": verdict(final),
        "score_band_options": verdict_options(final),
        "warning": "Verdict band is advisory; hard red-flag gates can override it downward.",
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
