#!/usr/bin/env python3
"""Standard-library deterministic calculations for public-equity research.

Functions never fetch data. Callers must provide source-traceable, unit-consistent
inputs and preserve the returned reconciliation diagnostics.
"""
from __future__ import annotations

import math
from statistics import mean, pstdev


def _require_rate(value: float, name: str, allow_negative: bool = False) -> None:
    lower = -1.0 if allow_negative else 0.0
    if not lower <= value <= 1.0:
        raise ValueError(f"{name} must be between {lower} and 1")


def _safe_div(numerator: float, denominator: float, name: str) -> float:
    if denominator == 0:
        raise ValueError(f"{name} denominator cannot be zero")
    return numerator / denominator


# Accounting -----------------------------------------------------------------

def three_statement_reconcile(assets: float, liabilities: float, equity: float,
                              beginning_cash: float, ending_cash: float,
                              cfo: float, cfi: float, cff: float,
                              fx_other: float = 0.0, tolerance: float = 1e-6) -> dict:
    balance_residual = assets - liabilities - equity
    cash_residual = ending_cash - beginning_cash - cfo - cfi - cff - fx_other
    return {
        "balance_sheet_residual": balance_residual,
        "cash_flow_residual": cash_residual,
        "balance_sheet_pass": abs(balance_residual) <= tolerance,
        "cash_flow_pass": abs(cash_residual) <= tolerance,
        "pass": abs(balance_residual) <= tolerance and abs(cash_residual) <= tolerance,
    }


def cash_flow_reconcile(net_income: float, noncash_items: float,
                        change_working_capital: float, other_operating: float,
                        reported_cfo: float, tolerance: float = 1e-6) -> dict:
    calculated = net_income + noncash_items - change_working_capital + other_operating
    residual = reported_cfo - calculated
    return {"calculated_cfo": calculated, "reported_cfo": reported_cfo,
            "residual": residual, "pass": abs(residual) <= tolerance}


def share_count_bridge(beginning_shares: float, issuance: float = 0.0,
                       sbc_issuance: float = 0.0, option_dilution: float = 0.0,
                       convertible_dilution: float = 0.0, repurchases: float = 0.0,
                       ending_shares: float | None = None, tolerance: float = 1e-6) -> dict:
    calculated = beginning_shares + issuance + sbc_issuance + option_dilution + convertible_dilution - repurchases
    result = {"calculated_ending_shares": calculated,
              "gross_dilution": issuance + sbc_issuance + option_dilution + convertible_dilution,
              "repurchases": repurchases}
    if ending_shares is not None:
        result.update({"reported_ending_shares": ending_shares,
                       "residual": ending_shares - calculated,
                       "pass": abs(ending_shares - calculated) <= tolerance})
    return result


def working_capital_metrics(accounts_receivable: float, inventory: float,
                            accounts_payable: float, revenue: float, cogs: float,
                            days: float = 365.0) -> dict:
    dso = _safe_div(accounts_receivable * days, revenue, "DSO")
    dio = _safe_div(inventory * days, cogs, "DIO")
    dpo = _safe_div(accounts_payable * days, cogs, "DPO")
    return {"dso": dso, "dio": dio, "dpo": dpo, "cash_conversion_cycle": dso + dio - dpo}


def lease_normalization(rent_expense: float, imputed_interest: float,
                        lease_liability: float, reported_ebitda: float,
                        reported_debt: float) -> dict:
    if rent_expense < 0 or imputed_interest < 0 or lease_liability < 0:
        raise ValueError("lease inputs cannot be negative")
    depreciation_component = max(rent_expense - imputed_interest, 0.0)
    return {"lease_adjusted_ebitda": reported_ebitda + rent_expense,
            "lease_adjusted_debt": reported_debt + lease_liability,
            "imputed_interest": imputed_interest,
            "imputed_depreciation": depreciation_component}


def sbc_dilution(beginning_shares: float, ending_shares: float, repurchased_shares: float,
                 sbc_expense: float, revenue: float, free_cash_flow: float) -> dict:
    gross_issuance = ending_shares - beginning_shares + repurchased_shares
    return {"net_share_change": ending_shares - beginning_shares,
            "gross_issuance_estimate": gross_issuance,
            "sbc_percent_revenue": _safe_div(sbc_expense, revenue, "SBC/revenue"),
            "fcf_after_sbc_repurchase": free_cash_flow - sbc_expense}


def tax_normalization(pre_tax_income: float, reported_tax: float,
                      discrete_items: float = 0.0, statutory_rate: float | None = None) -> dict:
    normalized_tax = reported_tax - discrete_items
    result = {"reported_effective_rate": _safe_div(reported_tax, pre_tax_income, "reported tax rate"),
              "normalized_tax": normalized_tax,
              "normalized_effective_rate": _safe_div(normalized_tax, pre_tax_income, "normalized tax rate")}
    if statutory_rate is not None:
        _require_rate(statutory_rate, "statutory_rate")
        result["normalized_vs_statutory"] = result["normalized_effective_rate"] - statutory_rate
    return result


# Valuation ------------------------------------------------------------------

def terminal_value_gordon(final_cash_flow: float, discount_rate: float, perpetual_growth: float) -> float:
    _require_rate(discount_rate, "discount_rate")
    _require_rate(perpetual_growth, "perpetual_growth", allow_negative=True)
    if discount_rate <= perpetual_growth:
        raise ValueError("discount_rate must exceed perpetual_growth")
    return final_cash_flow * (1 + perpetual_growth) / (discount_rate - perpetual_growth)


def dcf(cash_flows: list[float], discount_rate: float, perpetual_growth: float,
        net_debt: float = 0.0, non_operating_assets: float = 0.0,
        minority_interest: float = 0.0, preferred_equity: float = 0.0,
        diluted_shares: float | None = None) -> dict:
    if not cash_flows:
        raise ValueError("cash_flows cannot be empty")
    _require_rate(discount_rate, "discount_rate")
    pv_explicit = sum(cf / (1 + discount_rate) ** year for year, cf in enumerate(cash_flows, 1))
    terminal = terminal_value_gordon(cash_flows[-1], discount_rate, perpetual_growth)
    pv_terminal = terminal / (1 + discount_rate) ** len(cash_flows)
    enterprise_value = pv_explicit + pv_terminal
    equity_value = enterprise_value - net_debt + non_operating_assets - minority_interest - preferred_equity
    result = {"pv_explicit": pv_explicit, "terminal_value": terminal,
              "pv_terminal": pv_terminal, "terminal_value_weight": pv_terminal / enterprise_value,
              "enterprise_value": enterprise_value, "equity_value": equity_value}
    if diluted_shares is not None:
        if diluted_shares <= 0:
            raise ValueError("diluted_shares must be positive")
        result["value_per_share"] = equity_value / diluted_shares
    return result


def reverse_dcf_implied_growth(enterprise_value: float, starting_cash_flow: float,
                               years: int, discount_rate: float, perpetual_growth: float,
                               lower: float = -0.50, upper: float = 1.00,
                               iterations: int = 200) -> dict:
    if enterprise_value <= 0 or years <= 0:
        raise ValueError("enterprise_value and years must be positive")
    def value(growth: float) -> float:
        flows = [starting_cash_flow * (1 + growth) ** year for year in range(1, years + 1)]
        return dcf(flows, discount_rate, perpetual_growth)["enterprise_value"]
    lo, hi = lower, upper
    if not (value(lo) <= enterprise_value <= value(hi)):
        raise ValueError("implied growth not bracketed by lower and upper")
    for _ in range(iterations):
        mid = (lo + hi) / 2
        if value(mid) < enterprise_value:
            lo = mid
        else:
            hi = mid
    growth = (lo + hi) / 2
    return {"implied_growth": growth, "reconstructed_enterprise_value": value(growth),
            "target_enterprise_value": enterprise_value}


def multiples_valuation(metric: float, multiple: float, net_debt: float = 0.0,
                        diluted_shares: float | None = None, is_enterprise_multiple: bool = True) -> dict:
    if multiple < 0:
        raise ValueError("multiple cannot be negative")
    headline = metric * multiple
    enterprise_value = headline if is_enterprise_multiple else None
    equity_value = headline - net_debt if is_enterprise_multiple else headline
    result = {"headline_value": headline, "enterprise_value": enterprise_value, "equity_value": equity_value}
    if diluted_shares is not None:
        if diluted_shares <= 0:
            raise ValueError("diluted_shares must be positive")
        result["value_per_share"] = equity_value / diluted_shares
    return result


def sum_of_parts(parts: list[dict], corporate_adjustments: float = 0.0,
                 net_debt: float = 0.0, diluted_shares: float | None = None) -> dict:
    if not parts:
        raise ValueError("parts cannot be empty")
    detail = []
    for part in parts:
        name, metric, multiple = part["name"], float(part["metric"]), float(part["multiple"])
        detail.append({"name": name, "value": metric * multiple})
    enterprise_value = sum(p["value"] for p in detail) + corporate_adjustments
    equity_value = enterprise_value - net_debt
    result = {"parts": detail, "enterprise_value": enterprise_value, "equity_value": equity_value}
    if diluted_shares is not None:
        if diluted_shares <= 0:
            raise ValueError("diluted_shares must be positive")
        result["value_per_share"] = equity_value / diluted_shares
    return result


def residual_income(book_value: float, forecast_roe: list[float], cost_of_equity: float,
                    payout_ratio: float = 0.0, terminal_roe: float | None = None) -> dict:
    _require_rate(cost_of_equity, "cost_of_equity")
    _require_rate(payout_ratio, "payout_ratio")
    if book_value <= 0 or not forecast_roe:
        raise ValueError("positive book_value and forecast_roe are required")
    pv_residual = 0.0
    current_book = book_value
    schedule = []
    for year, roe in enumerate(forecast_roe, 1):
        earnings = current_book * roe
        residual = earnings - current_book * cost_of_equity
        pv = residual / (1 + cost_of_equity) ** year
        schedule.append({"year": year, "beginning_book": current_book, "earnings": earnings, "residual_income": residual, "pv": pv})
        pv_residual += pv
        current_book += earnings * (1 - payout_ratio)
    terminal_value = 0.0
    if terminal_roe is not None:
        terminal_residual = current_book * (terminal_roe - cost_of_equity)
        terminal_value = terminal_residual / cost_of_equity / (1 + cost_of_equity) ** len(forecast_roe)
    return {"book_value": book_value, "pv_residual_income": pv_residual,
            "pv_terminal_residual_income": terminal_value,
            "equity_value": book_value + pv_residual + terminal_value, "schedule": schedule}


def scenario_valuation(values: list[float], probabilities: list[float], tolerance: float = 1e-9) -> dict:
    if not values or len(values) != len(probabilities):
        raise ValueError("values and probabilities must have equal nonzero length")
    if any(p < 0 for p in probabilities):
        raise ValueError("probabilities cannot be negative")
    if abs(sum(probabilities) - 1.0) > tolerance:
        raise ValueError("probabilities must sum to 1")
    expected = sum(v * p for v, p in zip(values, probabilities))
    variance = sum(p * (v - expected) ** 2 for v, p in zip(values, probabilities))
    return {"expected_value": expected, "standard_deviation": math.sqrt(variance),
            "minimum": min(values), "maximum": max(values)}


# Forensics ------------------------------------------------------------------

def accruals(net_income: float, cfo: float, average_assets: float) -> dict:
    accrual_amount = net_income - cfo
    return {"accrual_amount": accrual_amount,
            "accrual_ratio": _safe_div(accrual_amount, average_assets, "accrual ratio")}


def beneish_m_score(dsri: float, gmi: float, aqi: float, sgi: float,
                    depi: float, sgai: float, lvgi: float, tata: float) -> dict:
    score = -4.84 + 0.920 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi + 0.115 * depi - 0.172 * sgai + 4.679 * tata - 0.327 * lvgi
    return {"m_score": score, "screen_flag": score > -1.78,
            "interpretation": "diagnostic screen only; not evidence of fraud"}


def cash_conversion(net_income: float, cfo: float, free_cash_flow: float | None = None) -> dict:
    result = {"cfo_to_net_income": _safe_div(cfo, net_income, "CFO/net income")}
    if free_cash_flow is not None:
        result["fcf_to_net_income"] = _safe_div(free_cash_flow, net_income, "FCF/net income")
    return result


def working_capital_anomalies(revenue_growth: float, receivables_growth: float,
                              inventory_growth: float, payables_growth: float,
                              threshold: float = 0.10) -> dict:
    spreads = {"receivables_vs_revenue": receivables_growth - revenue_growth,
               "inventory_vs_revenue": inventory_growth - revenue_growth,
               "payables_vs_revenue": payables_growth - revenue_growth}
    return {"spreads": spreads, "flags": [name for name, value in spreads.items() if abs(value) >= threshold]}


def disclosure_drift(old_text: str, new_text: str) -> dict:
    old_tokens = set(old_text.lower().split())
    new_tokens = set(new_text.lower().split())
    union = old_tokens | new_tokens
    similarity = 1.0 if not union else len(old_tokens & new_tokens) / len(union)
    return {"jaccard_similarity": similarity,
            "added_terms": sorted(new_tokens - old_tokens),
            "removed_terms": sorted(old_tokens - new_tokens),
            "material_review_required": similarity < 0.80}


# Risk -----------------------------------------------------------------------

def liquidity_runway(cash: float, committed_undrawn: float, restricted_cash: float,
                      mandatory_uses: float, periodic_cash_burn: float | None = None) -> dict:
    usable = cash + committed_undrawn - restricted_cash - mandatory_uses
    result = {"usable_liquidity": usable}
    if periodic_cash_burn is not None:
        if periodic_cash_burn <= 0:
            raise ValueError("periodic_cash_burn must be positive")
        result["runway_periods"] = usable / periodic_cash_burn
    return result


def debt_maturity_schedule(maturities: dict[str, float], annual_free_cash_flow: float,
                           starting_cash: float = 0.0) -> dict:
    cumulative = 0.0
    detail = []
    available = starting_cash
    for period in sorted(maturities):
        amount = float(maturities[period])
        cumulative += amount
        available += annual_free_cash_flow
        gap = available - amount
        detail.append({"period": period, "maturity": amount, "available_before_refinancing": available, "surplus_or_gap": gap})
        available = max(gap, 0.0)
    return {"total_maturities": cumulative, "schedule": detail,
            "minimum_surplus_or_gap": min((x["surplus_or_gap"] for x in detail), default=0.0)}


def covenant_headroom(metric: float, covenant_limit: float, direction: str = "maximum") -> dict:
    if direction not in {"maximum", "minimum"}:
        raise ValueError("direction must be maximum or minimum")
    headroom = covenant_limit - metric if direction == "maximum" else metric - covenant_limit
    denominator = abs(covenant_limit) if covenant_limit else 1.0
    return {"headroom": headroom, "headroom_percent_of_limit": headroom / denominator, "pass": headroom >= 0}


def refinancing_stress(debt_to_refinance: float, current_rate: float, stressed_rate: float,
                       stressed_ebitda: float, existing_interest: float = 0.0) -> dict:
    incremental_interest = debt_to_refinance * (stressed_rate - current_rate)
    total_interest = existing_interest + debt_to_refinance * stressed_rate
    return {"incremental_interest": incremental_interest, "stressed_interest": total_interest,
            "stressed_interest_coverage": _safe_div(stressed_ebitda, total_interest, "interest coverage")}


def dilution_stress(cash_shortfall: float, issue_price: float, existing_shares: float,
                    discount: float = 0.0) -> dict:
    _require_rate(discount, "discount")
    effective_price = issue_price * (1 - discount)
    if effective_price <= 0 or existing_shares <= 0:
        raise ValueError("effective issue price and existing shares must be positive")
    new_shares = cash_shortfall / effective_price
    total = existing_shares + new_shares
    return {"effective_issue_price": effective_price, "new_shares": new_shares,
            "post_money_shares": total, "new_holder_ownership": new_shares / total,
            "existing_holder_dilution": new_shares / total}


# Forecasts, management, confidence, and research budget ---------------------

def forecast_error(forecast: float, actual: float, attribution: dict[str, float], tolerance: float = 1e-6) -> dict:
    error = actual - forecast
    attributed = sum(attribution.values())
    residual = error - attributed
    return {"forecast": forecast, "actual": actual, "error": error,
            "attribution": attribution, "attributed_total": attributed,
            "residual": residual, "pass": abs(residual) <= tolerance}


def forecast_bias(errors: list[float]) -> dict:
    if not errors:
        raise ValueError("errors cannot be empty")
    return {"mean_error": mean(errors), "mean_absolute_error": mean(abs(x) for x in errors),
            "root_mean_square_error": math.sqrt(mean(x * x for x in errors)),
            "error_standard_deviation": pstdev(errors)}


def management_credibility(outcomes: list[dict]) -> dict:
    weights = {"met": 1.0, "partially_met": 0.5, "missed": 0.0, "withdrawn": 0.0}
    scored = [o for o in outcomes if o.get("outcome") in weights]
    if not scored:
        return {"score": None, "scored_predictions": 0, "not_scored": len(outcomes)}
    total_weight = sum(float(o.get("materiality_weight", 1.0)) for o in scored)
    score = sum(weights[o["outcome"]] * float(o.get("materiality_weight", 1.0)) for o in scored) / total_weight
    return {"score": score * 100, "scored_predictions": len(scored), "not_scored": len(outcomes) - len(scored)}


CONFIDENCE_WEIGHTS = {"evidence_coverage": 0.25, "source_quality": 0.20,
                      "historical_consistency": 0.15, "model_reconciliation": 0.15,
                      "contradiction_resolution": 0.10, "forecast_uncertainty": 0.10,
                      "evidence_freshness": 0.05}


def research_confidence(components: dict[str, float], mandatory_gate_open: bool = False,
                        critical_input_unprovenanced: bool = False,
                        point_in_time_breach: bool = False) -> dict:
    missing = set(CONFIDENCE_WEIGHTS) - set(components)
    if missing:
        raise ValueError(f"missing confidence components: {sorted(missing)}")
    for name, score in components.items():
        if not 0 <= score <= 100:
            raise ValueError(f"{name} must be 0-100")
    raw = sum(components[name] * weight for name, weight in CONFIDENCE_WEIGHTS.items())
    cap = mandatory_gate_open or critical_input_unprovenanced or point_in_time_breach
    final = min(raw, 59.0) if cap else raw
    return {"raw_score": raw, "weighted_score": final, "gate_cap_applied": cap,
            "status": "RESEARCH_INCOMPLETE" if cap else "SCORED"}


def evidence_freshness(source_age_days: float, shelf_life_days: float) -> dict:
    if source_age_days < 0 or shelf_life_days <= 0:
        raise ValueError("source age must be nonnegative and shelf life positive")
    ratio = source_age_days / shelf_life_days
    score = 100.0 if ratio <= 0.25 else max(0.0, 100.0 * (1.0 - (ratio - 0.25) / 1.25))
    return {"age_to_shelf_life": ratio, "freshness_score": score, "stale": source_age_days > shelf_life_days}


def evoi_priority(decision_impact: float, change_probability: float,
                  uncertainty_reduction: float, dependency_multiplier: float,
                  cost_hours: float) -> dict:
    for name, value in {"decision_impact": decision_impact, "change_probability": change_probability,
                        "uncertainty_reduction": uncertainty_reduction}.items():
        if not 0 <= value <= 1:
            raise ValueError(f"{name} must be 0-1")
    if not 1 <= dependency_multiplier <= 2 or cost_hours <= 0:
        raise ValueError("dependency_multiplier must be 1-2 and cost_hours positive")
    score = decision_impact * change_probability * uncertainty_reduction * dependency_multiplier / max(cost_hours, 0.25)
    return {"priority_score": score,
            "inputs": {"decision_impact": decision_impact, "change_probability": change_probability,
                       "uncertainty_reduction": uncertainty_reduction, "dependency_multiplier": dependency_multiplier,
                       "cost_hours": cost_hours}}
