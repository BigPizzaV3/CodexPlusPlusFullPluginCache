#!/usr/bin/env python3
"""Validate and compare user-authored equity scenarios; no empirical forecasts."""

import argparse
from datetime import date
from decimal import Decimal, localcontext
import json
import math
from pathlib import Path
import sys


class ValidationError(ValueError):
    """An input does not satisfy the scenario contract."""


def require(condition, message):
    if not condition:
        raise ValidationError(message)


def mapping(value, path):
    require(isinstance(value, dict), f"{path}: expected object")
    return value


def allowed_keys(value, expected, path):
    unknown = set(value) - set(expected)
    require(not unknown, f"{path}: unknown field(s): {', '.join(sorted(unknown))}")


def field(obj, key, path):
    require(key in obj, f"{path}.{key}: required")
    return obj[key]


def string(value, path):
    require(isinstance(value, str) and bool(value.strip()), f"{path}: expected nonempty string")
    return value


def number(value, path, minimum=None, maximum=None):
    require(type(value) in (int, float), f"{path}: expected number, not boolean")
    try:
        value = float(value)
    except (OverflowError, ValueError):
        raise ValidationError(f"{path}: expected finite number") from None
    require(math.isfinite(value), f"{path}: expected finite number")
    require(minimum is None or value >= minimum, f"{path}: below minimum {minimum}")
    require(maximum is None or value <= maximum, f"{path}: above maximum {maximum}")
    return value


def sequence(value, path, nonempty=True):
    require(isinstance(value, list), f"{path}: expected array")
    require(not nonempty or bool(value), f"{path}: must not be empty")
    return value


def finite_result(value, path):
    require(math.isfinite(value), f"{path}: arithmetic overflow; rescale inputs")
    return value


def decimal(value):
    """Preserve the supplied decimal value for event and policy boundaries."""
    return Decimal(str(value))


def probability_total(rows, condition=None):
    return float(sum((decimal(row["probability"]) for row in rows
                      if condition is None or row[condition]), Decimal(0)))


def economic_sensitivity(rows):
    """Exact decimal comparison of validated finite-float scenario inputs.

    Coalesce equivalent payoffs before weighting so splitting a state cannot
    manufacture sensitivity. Zero-probability states carry no economic mass.
    Use terminal cash rather than dividing by a common entry price.
    """
    with localcontext() as context:
        context.prec = 1100
        distribution = {}
        success = Decimal(0)
        severe_loss = Decimal(0)
        for row in rows:
            probability = decimal(row["probability"])
            if probability == 0:
                continue
            payoff = decimal(row["terminal_price"]) + decimal(row["cash_distributions"])
            key = (payoff, decimal(row["benchmark_wealth_multiple"]))
            distribution[key] = distribution.get(key, Decimal(0)) + probability
            if row["success"]:
                success += probability
            if row["severe_loss"]:
                severe_loss += probability
        signature = tuple(sorted((payoff, benchmark, mass)
                                 for (payoff, benchmark), mass in distribution.items()))
        expected_cash = sum((payoff * mass for payoff, _, mass in signature), Decimal(0))
        return signature, (expected_cash, success, severe_loss)


def annualize(wealth, horizon, path):
    if wealth == 0:
        return -1.0
    try:
        return finite_result(math.expm1(math.log(wealth) / horizon), path)
    except OverflowError:
        raise ValidationError(f"{path}: arithmetic overflow; rescale inputs") from None


def calculate_set(raw, path, price, horizon, threshold):
    mapping(raw, path)
    allowed_keys(raw, ("name", "scenarios"), path)
    name = string(field(raw, "name", path), f"{path}.name")
    rows = sequence(field(raw, "scenarios", path), f"{path}.scenarios")
    seen = set()
    metrics = []
    for index, raw_scenario in enumerate(rows):
        sp = f"{path}.scenarios[{index}]"
        row = mapping(raw_scenario, sp)
        allowed_keys(row, ("name", "probability", "terminal_price", "cash_distributions", "benchmark_wealth_multiple"), sp)
        scenario_name = string(field(row, "name", sp), f"{sp}.name")
        require(scenario_name not in seen, f"{sp}.name: duplicate scenario name")
        seen.add(scenario_name)
        probability = number(field(row, "probability", sp), f"{sp}.probability", 0, 1)
        terminal = number(field(row, "terminal_price", sp), f"{sp}.terminal_price", 0)
        cash = number(field(row, "cash_distributions", sp), f"{sp}.cash_distributions", 0)
        benchmark = number(field(row, "benchmark_wealth_multiple", sp), f"{sp}.benchmark_wealth_multiple", 0)
        wealth = finite_result((terminal + cash) / price, f"{sp}.wealth_multiple")
        total_return = wealth - 1.0
        terminal_cash = decimal(terminal) + decimal(cash)
        entry_cash = decimal(price)
        metrics.append({
            "name": scenario_name, "probability": probability,
            "terminal_price": terminal, "cash_distributions": cash,
            "benchmark_wealth_multiple": benchmark,
            "wealth_multiple": wealth, "total_return": total_return,
            "scenario_cagr": annualize(wealth, horizon, f"{sp}.scenario_cagr"),
            "success": terminal_cash > entry_cash and terminal_cash > entry_cash * decimal(benchmark),
            "severe_loss": terminal_cash <= entry_cash * (Decimal(1) - decimal(threshold)),
            "terminal_loss": terminal_cash < entry_cash,
        })
    probability_sum = probability_total(metrics)
    require(math.isclose(probability_sum, 1.0, rel_tol=0, abs_tol=1e-12),
            f"{path}: probabilities must sum to 1 (got {probability_sum!r})")
    expected_wealth = finite_result(math.fsum(row["probability"] * row["wealth_multiple"] for row in metrics), path)
    result = {
        "name": name, "probability_sum": probability_sum,
        "scenarios": metrics, "expected_wealth_multiple": expected_wealth,
        "expected_total_return": expected_wealth - 1.0,
        "annualized_expected_wealth": annualize(expected_wealth, horizon, path),
        "probability_weighted_scenario_cagr": math.fsum(row["probability"] * row["scenario_cagr"] for row in metrics),
        "success_probability": probability_total(metrics, "success"),
        "severe_loss_probability": probability_total(metrics, "severe_loss"),
        "terminal_loss_probability": probability_total(metrics, "terminal_loss"),
        "central_bull_upside_total_return": max(row["total_return"] for row in metrics if row["probability"] > 0),
    }
    signature, comparison_metrics = economic_sensitivity(metrics)
    return result, signature, comparison_metrics


def dominates(left, right):
    comparisons = (
        left["robust_annualized_expected_wealth"] >= right["robust_annualized_expected_wealth"],
        left["robust_success_probability"] >= right["robust_success_probability"],
        left["robust_severe_loss_probability"] <= right["robust_severe_loss_probability"],
    )
    strict = (
        left["robust_annualized_expected_wealth"] > right["robust_annualized_expected_wealth"]
        or left["robust_success_probability"] > right["robust_success_probability"]
        or left["robust_severe_loss_probability"] < right["robust_severe_loss_probability"]
    )
    return all(comparisons) and strict


def analyze(data):
    root = mapping(data, "input")
    allowed_keys(root, ("schema_version", "horizon_years", "currency", "severe_loss_threshold", "policy", "companies"), "input")
    version = field(root, "schema_version", "input")
    require(type(version) is int and version == 1, "schema_version: must be integer 1")
    horizon = number(field(root, "horizon_years", "input"), "horizon_years", 0)
    require(horizon > 0, "horizon_years: must be greater than zero")
    currency = string(field(root, "currency", "input"), "currency")
    threshold = number(field(root, "severe_loss_threshold", "input"), "severe_loss_threshold", 0, 1)
    require(threshold > 0, "severe_loss_threshold: must be greater than zero")
    policy = mapping(field(root, "policy", "input"), "policy")
    allowed_keys(policy, ("min_success_probability", "max_severe_loss_probability"), "policy")
    minimum = number(field(policy, "min_success_probability", "policy"), "policy.min_success_probability", 0, 1)
    maximum = number(field(policy, "max_severe_loss_probability", "policy"), "policy.max_severe_loss_probability", 0, 1)
    companies = sequence(field(root, "companies", "input"), "companies")
    ids = set()
    results = []
    for index, raw in enumerate(companies):
        path = f"companies[{index}]"
        company = mapping(raw, path)
        allowed_keys(company, ("id", "name", "currency", "price", "evidence_eligible", "eligibility_notes", "scenario_sets"), path)
        identifier = string(field(company, "id", path), f"{path}.id")
        require(identifier not in ids, f"{path}.id: duplicate company ID")
        ids.add(identifier)
        name = string(field(company, "name", path), f"{path}.name")
        company_currency = string(field(company, "currency", path), f"{path}.currency")
        require(company_currency == currency, f"{path}.currency: must match run currency {currency}")
        price_data = mapping(field(company, "price", path), f"{path}.price")
        allowed_keys(price_data, ("value", "as_of", "source_id"), f"{path}.price")
        price = number(field(price_data, "value", f"{path}.price"), f"{path}.price.value", 0)
        require(price > 0, f"{path}.price.value: must be greater than zero")
        as_of = string(field(price_data, "as_of", f"{path}.price"), f"{path}.price.as_of")
        try:
            parsed_date = date.fromisoformat(as_of)
        except ValueError:
            raise ValidationError(f"{path}.price.as_of: expected YYYY-MM-DD") from None
        require(parsed_date.isoformat() == as_of, f"{path}.price.as_of: expected YYYY-MM-DD")
        source_id = string(field(price_data, "source_id", f"{path}.price"), f"{path}.price.source_id")
        evidence = field(company, "evidence_eligible", path)
        require(type(evidence) is bool, f"{path}.evidence_eligible: expected boolean")
        notes = sequence(field(company, "eligibility_notes", path), f"{path}.eligibility_notes")
        for note_index, note in enumerate(notes):
            string(note, f"{path}.eligibility_notes[{note_index}]")
        sets = sequence(field(company, "scenario_sets", path), f"{path}.scenario_sets")
        set_names = set()
        calculated = []
        signatures = {}
        sensitivity_metrics = {}
        for set_index, raw_set in enumerate(sets):
            result, signature, comparison_metrics = calculate_set(raw_set, f"{path}.scenario_sets[{set_index}]", price, horizon, threshold)
            require(result["name"] not in set_names, f"{path}.scenario_sets: duplicate set name")
            set_names.add(result["name"])
            signatures[result["name"]] = signature
            sensitivity_metrics[result["name"]] = comparison_metrics
            calculated.append(result)
        require("central" in set_names, f"{path}.scenario_sets: central set is required")
        central = next(row for row in calculated if row["name"] == "central")
        distinct_sensitivity = any(signature != signatures["central"] for key, signature in signatures.items() if key != "central")
        central_cash, central_success, central_loss = sensitivity_metrics["central"]
        adverse_sensitivity = any(
            cash < central_cash or success < central_success or loss > central_loss
            for key, (cash, success, loss) in sensitivity_metrics.items() if key != "central")
        robust_return = min(row["annualized_expected_wealth"] for row in calculated)
        robust_success = min(row["success_probability"] for row in calculated)
        robust_loss = max(row["severe_loss_probability"] for row in calculated)
        reasons = []
        if not evidence:
            reasons.append("Evidence eligibility was not attested.")
        if not distinct_sensitivity:
            reasons.append("At least one numerically distinct sensitivity set is required for ranking.")
        if not adverse_sensitivity:
            reasons.append("At least one adverse sensitivity must lower expected terminal wealth or success probability, or increase severe-loss probability, versus central.")
        if robust_success < minimum:
            reasons.append("Robust success probability is below policy minimum.")
        if robust_loss > maximum:
            reasons.append("Robust severe-loss probability exceeds policy maximum.")
        if robust_return <= 0:
            reasons.append("Robust annualized expected wealth return is not positive.")
        results.append({
            "id": identifier, "name": name, "currency": currency,
            "price": {"value": price, "as_of": as_of, "source_id": source_id},
            "evidence_eligible": evidence, "eligibility_notes": notes,
            "has_distinct_sensitivity": distinct_sensitivity,
            "has_adverse_sensitivity": adverse_sensitivity,
            "scenario_sets": calculated, "central": central,
            "robust_annualized_expected_wealth": robust_return,
            "robust_success_probability": robust_success,
            "robust_severe_loss_probability": robust_loss,
            "eligible": not reasons, "watchlist_reasons": reasons,
            "pareto_frontier": False, "dominated_by": [], "rank": None,
        })
    eligible = [row for row in results if row["eligible"]]
    for row in eligible:
        row["dominated_by"] = sorted(other["id"] for other in eligible if dominates(other, row))
        row["pareto_frontier"] = not row["dominated_by"]
    ordered = sorted(eligible, key=lambda row: (
        not row["pareto_frontier"], -row["robust_annualized_expected_wealth"],
        -row["robust_success_probability"], row["robust_severe_loss_probability"], row["id"]))
    for rank, row in enumerate(ordered, 1):
        row["rank"] = rank
    return {
        "schema_version": 1, "horizon_years": horizon, "currency": currency,
        "severe_loss_threshold": threshold,
        "policy": {"min_success_probability": minimum, "max_severe_loss_probability": maximum},
        "caveats": [
            "Scenario probabilities are user-supplied assumptions, not verified empirical success estimates or guarantees.",
            "Evidence eligibility is a human attestation; this calculator does not verify sources or evidence.",
            "Terminal prices must already reflect dilution; no dilution adjustment is performed.",
            "Cash distributions are added without reinvestment. Reinvestment requires a separately documented alternative model outside this calculator contract.",
            "The adverse-sensitivity gate checks modeled metric direction only; humans must assess economic plausibility, stress magnitude, and comparable stress coverage.",
            "Success requires positive total return AND strict outperformance of the same-state benchmark.",
            "Severe loss is terminal total return at or below the loss threshold, not path drawdown or permanent impairment.",
            "Robust extrema can come from different sensitivity sets; they are not a single joint forecast.",
            "Policy gates use unrounded metrics; event boundaries and probability addition use decimal arithmetic. Probability sums permit only a 1e-12 tolerance and are not normalized.",
            "Rankings compare only supplied companies and scenarios; no ranking establishes the best investment in a market.",
        ],
        "companies": results,
        "ranked_ids": [row["id"] for row in ordered],
        "success_first_eligible_ids": [row["id"] for row in sorted(eligible, key=lambda row: (
            -row["robust_success_probability"], -row["robust_annualized_expected_wealth"],
            row["robust_severe_loss_probability"], row["id"]))],
        "central_bull_upside_eligible_ids": [row["id"] for row in sorted(eligible, key=lambda row: (
            -row["central"]["central_bull_upside_total_return"], row["id"]))],
        "alternative_ordering_note": "Eligible companies only. Bull upside is the highest positive-probability central scenario total return, not its likelihood or an expected return.",
        "watchlist_ids": sorted(row["id"] for row in results if not row["eligible"]),
    }


def reject_constant(value):
    raise ValidationError(f"Nonfinite JSON constant is not allowed: {value}")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"Duplicate JSON object key: {key}")
        result[key] = value
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="UTF-8 scenario input JSON")
    parser.add_argument("--output", type=Path, help="Write UTF-8 result JSON (otherwise stdout)")
    args = parser.parse_args(argv)
    try:
        if args.output:
            same_path = args.input.resolve() == args.output.resolve()
            same_file = args.input.exists() and args.output.exists() and args.input.samefile(args.output)
            require(not (same_path or same_file), "Output must not overwrite input (including links to the same file).")
        data = json.loads(args.input.read_text(encoding="utf-8-sig"), parse_constant=reject_constant, object_pairs_hook=unique_object)
        output = json.dumps(analyze(data), ensure_ascii=False, indent=2, allow_nan=False) + "\n"
        if args.output:
            args.output.write_text(output, encoding="utf-8")
        else:
            if hasattr(sys.stdout, "reconfigure"):
                sys.stdout.reconfigure(encoding="utf-8")
            sys.stdout.write(output)
        return 0
    except (ValidationError, ValueError, OSError, OverflowError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
