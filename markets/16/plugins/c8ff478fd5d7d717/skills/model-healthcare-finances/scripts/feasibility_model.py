#!/usr/bin/env python3
"""Deterministic, offline, 12-month healthcare planning model. Python 3.10+."""
import argparse
import csv
import json
import math
from pathlib import Path


class ModelError(ValueError):
    pass


def fields(obj, required, optional=(), label="input"):
    if not isinstance(obj, dict):
        raise ModelError(f"{label} must be an object")
    missing = set(required) - obj.keys()
    extra = obj.keys() - set(required) - set(optional)
    if missing or extra:
        raise ModelError(f"{label}: missing {sorted(missing)}, unknown {sorted(extra)}")


def number(value, label, minimum=0, maximum=None):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ModelError(f"{label} must be a finite number")
    if value < minimum or (maximum is not None and value > maximum):
        raise ModelError(f"{label} outside permitted range")
    return float(value)


def series(value, label):
    if not isinstance(value, list) or len(value) != 12:
        raise ModelError(f"{label} must contain 12 monthly numbers")
    return [number(x, label) for x in value]


def label(value, name):
    if not isinstance(value, str) or not value.strip() or len(value) > 160:
        raise ModelError(f"{name} must be a nonempty label of at most 160 characters")
    # Prevent spreadsheet formula interpretation in CSV exports.
    if value.lstrip().startswith(("=", "+", "-", "@")) or any(c in value for c in "\r\n\t"):
        raise ModelError(f"{name} contains unsupported spreadsheet/control syntax")
    return value.strip()


def expected_collection(payment):
    if not isinstance(payment, dict):
        raise ModelError("payment must be an object")
    basis = payment.get("basis")
    if basis == "expected_collected":
        fields(payment, ["basis", "amount"])
        return number(payment["amount"], "payment.amount")
    if basis != "allowed":
        raise ModelError("payment.basis must be allowed or expected_collected")
    fields(payment, ["basis", "allowed_amount", "claim_paid_probability", "payer_share",
                     "payer_collection_factor", "patient_collection_rate"])
    amount = number(payment["allowed_amount"], "allowed_amount")
    paid = number(payment["claim_paid_probability"], "claim_paid_probability", maximum=1)
    share = number(payment["payer_share"], "payer_share", maximum=1)
    factor = number(payment["payer_collection_factor"], "payer_collection_factor", maximum=1)
    patient = number(payment["patient_collection_rate"], "patient_collection_rate", maximum=1)
    return amount * paid * (share * factor + (1 - share) * patient)


def model(data):
    fields(data, ["scenario_name", "mode", "currency", "monthly_capacity_minutes",
                  "monthly_fixed_cash_cost", "billing_fee_rate", "collection_lag_weights",
                  "startup_capex", "startup_expense", "annual_depreciation", "opening_cash",
                  "cash_reserve", "services"], ["notes"])
    name = label(data["scenario_name"], "scenario_name")
    if data["mode"] not in ("existing_practice", "standalone") or data["currency"] != "USD":
        raise ModelError("mode must be existing_practice or standalone; currency must be USD")
    capacity = series(data["monthly_capacity_minutes"], "monthly_capacity_minutes")
    fixed = series(data["monthly_fixed_cash_cost"], "monthly_fixed_cash_cost")
    fee = number(data["billing_fee_rate"], "billing_fee_rate", maximum=1)
    weights = data["collection_lag_weights"]
    if not isinstance(weights, list) or not 1 <= len(weights) <= 13:
        raise ModelError("collection_lag_weights must have 1 to 13 entries for lags 0..12")
    weights = [number(w, "collection_lag_weight", maximum=1) for w in weights]
    if not math.isclose(sum(weights), 1, rel_tol=0, abs_tol=1e-9):
        raise ModelError("collection_lag_weights must sum to 1; losses belong in payment assumptions")
    capex, launch, depreciation, opening, reserve = (
        number(data[k], k) for k in ("startup_capex", "startup_expense", "annual_depreciation", "opening_cash", "cash_reserve"))
    raw_services = data["services"]
    if not isinstance(raw_services, list) or not 1 <= len(raw_services) <= 100:
        raise ModelError("services must contain 1 to 100 mutually exclusive encounter profiles")
    services = []
    seen = set()
    for raw in raw_services:
        fields(raw, ["label", "monthly_demand_visits", "minutes_per_visit", "variable_cost_per_visit", "payment"])
        service_name = label(raw["label"], "service.label")
        if service_name in seen:
            raise ModelError("service labels must be unique")
        seen.add(service_name)
        minutes = number(raw["minutes_per_visit"], "minutes_per_visit")
        if minutes <= 0:
            raise ModelError("minutes_per_visit must be greater than zero")
        revenue = expected_collection(raw["payment"])
        cost = number(raw["variable_cost_per_visit"], "variable_cost_per_visit")
        services.append({"label": service_name, "demand": series(raw["monthly_demand_visits"], "monthly_demand_visits"),
                         "minutes": minutes, "revenue": revenue, "cost": cost,
                         "unit_contribution": revenue * (1 - fee) - cost,
                         "actual_visits": 0.0, "earned": 0.0, "variable": 0.0})
    monthly = []
    earned_history = []
    unfinanced_cash = -capex - launch
    minimum_cash = unfinanced_cash
    for month in range(12):
        demand_visits = sum(s["demand"][month] for s in services)
        demand_minutes = sum(s["demand"][month] * s["minutes"] for s in services)
        scale = min(1, capacity[month] / demand_minutes) if demand_minutes else 1
        visits = demand_visits * scale
        used_minutes = demand_minutes * scale
        earned = variable = 0.0
        for s in services:
            actual = s["demand"][month] * scale
            s["actual_visits"] += actual
            s["earned"] += actual * s["revenue"]
            s["variable"] += actual * s["cost"]
            earned += actual * s["revenue"]
            variable += actual * s["cost"]
        earned_history.append(earned)
        received = sum(earned_history[month - lag] * w for lag, w in enumerate(weights) if month >= lag)
        accrual_billing_fee = earned * fee
        cash_billing_fee = received * fee
        contribution = earned - variable - accrual_billing_fee
        recurring_result = contribution - fixed[month] - depreciation / 12
        cash_flow = received - variable - cash_billing_fee - fixed[month]
        unfinanced_cash += cash_flow
        minimum_cash = min(minimum_cash, unfinanced_cash)
        per_visit = contribution / visits if visits else None
        break_even = ((fixed[month] + depreciation / 12) / per_visit
                      if per_visit is not None and per_visit > 0 else None)
        per_visit_minutes = used_minutes / visits if visits else None
        feasible = (break_even * per_visit_minutes <= capacity[month] + 1e-9
                    if break_even is not None else None)
        monthly.append({"month": month + 1, "demand_visits": demand_visits, "completed_visits": visits,
                        "unserved_demand_visits": demand_visits - visits, "capacity_minutes": capacity[month],
                        "used_minutes": used_minutes, "expected_earned_collections": earned, "cash_received": received,
                        "variable_cost": variable, "accrual_billing_fee": accrual_billing_fee,
                        "cash_billing_fee": cash_billing_fee, "fixed_cash_cost": fixed[month],
                        "depreciation": depreciation / 12, "contribution": contribution,
                        "recurring_operating_result": recurring_result, "net_operating_cash_flow": cash_flow,
                        "unfinanced_cumulative_cash": unfinanced_cash, "cash_balance_before_new_funding": opening + unfinanced_cash,
                        "break_even_monthly_visits_at_current_mix": break_even, "break_even_within_current_capacity": feasible})
    def total(key):
        return sum(row[key] for row in monthly)
    warnings = []
    if total("unserved_demand_visits") > 1e-8:
        warnings.append("Demand exceeds modeled capacity; encounter mix is scaled proportionately, not clinically prioritized.")
    if any(s["unit_contribution"] <= 0 for s in services):
        warnings.append("At least one encounter profile has nonpositive contribution; increasing that profile alone cannot cover fixed costs.")
    if any(row["break_even_within_current_capacity"] is False for row in monthly):
        warnings.append("At least one month's operating break-even is beyond its current capacity.")
    if total("completed_visits") == 0:
        warnings.append("No completed visits are modeled; break-even mix is undefined.")
    receivables = max(0, total("expected_earned_collections") - total("cash_received"))
    if receivables > 0:
        warnings.append("Year-end expected receivables remain uncollected within the 12-month horizon; these are timing, not a second bad-debt adjustment.")
    summary = {"scenario_name": name, "mode": data["mode"], "currency": "USD", "horizon_months": 12,
               "completed_visits": total("completed_visits"), "unserved_demand_visits": total("unserved_demand_visits"),
               "expected_earned_collections": total("expected_earned_collections"), "cash_received": total("cash_received"),
               "year_end_expected_receivables": receivables, "variable_cost": total("variable_cost"),
               "accrual_billing_fee": total("accrual_billing_fee"), "contribution": total("contribution"),
               "fixed_cash_cost": sum(fixed), "annual_depreciation": depreciation,
               "recurring_operating_result": total("recurring_operating_result"), "startup_expense": launch,
               "first_year_operating_result_after_startup_expense": total("recurring_operating_result") - launch,
               "startup_capex": capex, "net_operating_cash_flow": total("net_operating_cash_flow"),
               "cash_change_including_startup": unfinanced_cash, "opening_cash": opening,
               "ending_cash_before_new_funding": opening + unfinanced_cash,
               "peak_cumulative_cash_deficit": max(0, -minimum_cash), "cash_reserve": reserve,
               "total_initial_liquidity_required": max(0, -minimum_cash) + reserve,
               "additional_funding_required": max(0, -minimum_cash + reserve - opening),
               "warnings": warnings,
               "limitations": ["Planning estimates, not actual payment predictions or accounting statements.",
                               "One shared capacity pool with proportionate encounter mix; no optimization or clinical triage.",
                               "Variable costs paid in service month; fixed cash costs paid as entered; billing fees paid when collections arrive.",
                               "No opening receivables, inventory payment terms, debt service, taxes, grants, downstream revenue, or salvage value.",
                               "Break-even excludes startup recovery, collection delays, growth steps, and changes in encounter mix.",
                               "Collection-lag distribution is shared across profiles; use separate checked models if timing differs materially."]}
    economics = [{"service_label": s["label"], "expected_collection_per_visit": s["revenue"],
                  "variable_cost_per_visit": s["cost"], "billing_fee_per_visit": s["revenue"] * fee,
                  "contribution_per_visit": s["unit_contribution"], "minutes_per_visit": s["minutes"],
                  "annual_completed_visits": s["actual_visits"], "annual_expected_earned_collections": s["earned"]}
                 for s in services]
    result = {"summary": summary, "monthly": monthly, "service_economics": economics}
    def check_finite(item):
        if isinstance(item, dict):
            for value in item.values():
                check_finite(value)
        elif isinstance(item, list):
            for value in item:
                check_finite(value)
        elif isinstance(item, float) and not math.isfinite(item):
            raise ModelError("Inputs exceed supported numerical scale; no result can be produced")
    check_finite(result)
    return result


def write_outputs(result, output_dir):
    target = Path(output_dir)
    target.mkdir(parents=True, exist_ok=False)
    (target / "summary.json").write_text(json.dumps(result["summary"], indent=2, allow_nan=False) + "\n", encoding="utf-8")
    for filename, rows in (("monthly.csv", result["monthly"]), ("service-economics.csv", result["service_economics"])):
        with (target / filename).open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8-sig"))
        result = model(data)
        if args.output_dir:
            write_outputs(result, args.output_dir)
        print(json.dumps(result["summary"], indent=2, allow_nan=False))
    except (ModelError, OSError, ValueError) as exc:
        parser.exit(2, f"Model not produced: {exc}\n")


if __name__ == "__main__":
    main()
