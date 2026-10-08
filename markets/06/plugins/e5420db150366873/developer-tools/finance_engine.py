#!/usr/bin/env python3
"""Deterministic finance calculations used by the plugin.

All functions are pure and use only the Python standard library. Inputs must be
sourced and unit-consistent before use. The script does not fetch market data.
"""
from __future__ import annotations
import argparse
import json
import math
from typing import Iterable, Sequence


def cagr(begin: float, end: float, years: float) -> float:
    if begin <= 0 or end < 0 or years <= 0:
        raise ValueError("CAGR requires begin > 0, end >= 0, years > 0")
    return (end / begin) ** (1.0 / years) - 1.0


def nopat(operating_income: float, cash_tax_rate: float) -> float:
    return operating_income * (1.0 - cash_tax_rate)


def roic(nopat_value: float, average_invested_capital: float) -> float:
    if average_invested_capital == 0:
        raise ValueError("average invested capital cannot be zero")
    return nopat_value / average_invested_capital


def fcff(nopat_value: float, depreciation_amortization: float, capex: float, change_nwc: float, other_non_cash: float = 0.0) -> float:
    return nopat_value + depreciation_amortization + other_non_cash - capex - change_nwc


def wacc(equity_value: float, debt_value: float, cost_equity: float, pre_tax_cost_debt: float, marginal_tax_rate: float) -> float:
    total = equity_value + debt_value
    if total <= 0:
        raise ValueError("equity + debt must be positive")
    return (equity_value / total) * cost_equity + (debt_value / total) * pre_tax_cost_debt * (1.0 - marginal_tax_rate)


def terminal_value_gordon(final_fcff: float, discount_rate: float, perpetual_growth: float) -> float:
    if discount_rate <= perpetual_growth:
        raise ValueError("discount rate must exceed perpetual growth")
    return final_fcff * (1.0 + perpetual_growth) / (discount_rate - perpetual_growth)


def dcf_fcff(fcff_values: Sequence[float], discount_rate: float, perpetual_growth: float, net_debt: float = 0.0, non_operating_assets: float = 0.0, minority_interest: float = 0.0, diluted_shares: float | None = None):
    if not fcff_values:
        raise ValueError("at least one FCFF value is required")
    pv_explicit = sum(cf / ((1.0 + discount_rate) ** t) for t, cf in enumerate(fcff_values, start=1))
    tv = terminal_value_gordon(fcff_values[-1], discount_rate, perpetual_growth)
    pv_tv = tv / ((1.0 + discount_rate) ** len(fcff_values))
    enterprise_value = pv_explicit + pv_tv
    equity_value = enterprise_value - net_debt + non_operating_assets - minority_interest
    result = {
        "pv_explicit_fcff": pv_explicit,
        "terminal_value_at_horizon": tv,
        "pv_terminal_value": pv_tv,
        "enterprise_value": enterprise_value,
        "equity_value": equity_value,
    }
    if diluted_shares is not None:
        if diluted_shares <= 0:
            raise ValueError("diluted shares must be positive")
        result["equity_value_per_share"] = equity_value / diluted_shares
    return result


def enterprise_to_equity(enterprise_value: float, debt: float = 0.0, preferred: float = 0.0, minority_interest: float = 0.0, cash: float = 0.0, non_operating_assets: float = 0.0) -> float:
    return enterprise_value - debt - preferred - minority_interest + cash + non_operating_assets


def days_sales_outstanding(accounts_receivable: float, revenue: float, days: float = 365.0) -> float:
    if revenue == 0:
        raise ValueError("revenue cannot be zero")
    return accounts_receivable / revenue * days


def days_inventory_outstanding(inventory: float, cogs: float, days: float = 365.0) -> float:
    if cogs == 0:
        raise ValueError("COGS cannot be zero")
    return inventory / cogs * days


def days_payables_outstanding(accounts_payable: float, cogs: float, days: float = 365.0) -> float:
    if cogs == 0:
        raise ValueError("COGS cannot be zero")
    return accounts_payable / cogs * days


def cash_conversion_cycle(dso: float, dio: float, dpo: float) -> float:
    return dso + dio - dpo


def accrual_ratio_balance_sheet(change_non_cash_working_capital: float, depreciation_amortization: float, change_other_net_operating_assets: float, average_total_assets: float) -> float:
    if average_total_assets == 0:
        raise ValueError("average total assets cannot be zero")
    accruals = change_non_cash_working_capital - depreciation_amortization + change_other_net_operating_assets
    return accruals / average_total_assets


def cash_conversion(net_income: float, cfo: float) -> float:
    if net_income == 0:
        raise ValueError("net income cannot be zero")
    return cfo / net_income


def price_volume_mix_bridge(base_units: float, base_price: float, new_units: float, new_price: float):
    base_revenue = base_units * base_price
    new_revenue = new_units * new_price
    volume_effect = (new_units - base_units) * base_price
    price_effect = (new_price - base_price) * base_units
    interaction = (new_units - base_units) * (new_price - base_price)
    return {
        "base_revenue": base_revenue,
        "new_revenue": new_revenue,
        "total_change": new_revenue - base_revenue,
        "volume_effect": volume_effect,
        "price_effect": price_effect,
        "interaction_mix_effect": interaction,
        "reconciliation": volume_effect + price_effect + interaction,
    }


def diluted_share_count(basic_shares: float, incremental_options_rsus: float = 0.0, convertibles: float = 0.0, other_dilution: float = 0.0) -> float:
    total = basic_shares + incremental_options_rsus + convertibles + other_dilution
    if total <= 0:
        raise ValueError("diluted share count must be positive")
    return total


def scenario_expected_value(values: Sequence[float], probabilities: Sequence[float], tolerance: float = 1e-9) -> float:
    if len(values) != len(probabilities) or not values:
        raise ValueError("values and probabilities must have equal nonzero length")
    if any(p < 0 for p in probabilities):
        raise ValueError("probabilities cannot be negative")
    total_p = sum(probabilities)
    if abs(total_p - 1.0) > tolerance:
        raise ValueError(f"probabilities must sum to 1.0; got {total_p}")
    return sum(v * p for v, p in zip(values, probabilities))


def liquidity_runway(cash: float, committed_undrawn: float, restricted_cash: float, mandatory_uses: float, periodic_cash_burn: float | None = None):
    available = cash + committed_undrawn - restricted_cash - mandatory_uses
    result = {"usable_liquidity": available}
    if periodic_cash_burn is not None:
        if periodic_cash_burn <= 0:
            raise ValueError("periodic cash burn must be positive")
        result["runway_periods"] = available / periodic_cash_burn
    return result


def implied_perpetual_growth(enterprise_value: float, explicit_fcff: Sequence[float], discount_rate: float):
    if not explicit_fcff:
        raise ValueError("explicit FCFF required")
    pv_explicit = sum(cf / ((1 + discount_rate) ** t) for t, cf in enumerate(explicit_fcff, start=1))
    pv_terminal_needed = enterprise_value - pv_explicit
    if pv_terminal_needed <= 0:
        raise ValueError("enterprise value is not greater than PV of explicit FCFF")
    horizon = len(explicit_fcff)
    tv_needed = pv_terminal_needed * ((1 + discount_rate) ** horizon)
    last_cf = explicit_fcff[-1]
    # TV = CF*(1+g)/(r-g), solve algebraically for g.
    numerator = tv_needed * discount_rate - last_cf
    denominator = tv_needed + last_cf
    return numerator / denominator


def _run_cli():
    parser = argparse.ArgumentParser(description="Deterministic public-equity finance calculations")
    parser.add_argument("function", choices=["dcf", "wacc", "scenario_ev", "pvm", "liquidity"])
    parser.add_argument("json_args", help="JSON object of keyword arguments")
    args = parser.parse_args()
    kwargs = json.loads(args.json_args)
    funcs = {"dcf": dcf_fcff, "wacc": wacc, "scenario_ev": scenario_expected_value, "pvm": price_volume_mix_bridge, "liquidity": liquidity_runway}
    result = funcs[args.function](**kwargs)
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    _run_cli()
