#!/usr/bin/env python3
"""Safely recompute normalized engineering arithmetic with dimensional checks."""

from __future__ import annotations

import argparse
import ast
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

Dims = tuple[float, float, float, float, float]  # mass, length, time, current, temperature
ZERO: Dims = (0, 0, 0, 0, 0)


@dataclass(frozen=True)
class Unit:
    scale: float
    dims: Dims
    offset: float = 0.0
    absolute_temperature: bool = False


@dataclass(frozen=True)
class Quantity:
    value: float
    dims: Dims
    absolute_temperature: bool = False


def d(m=0, l=0, t=0, i=0, temp=0) -> Dims:
    return (m, l, t, i, temp)


UNITS: dict[str, Unit] = {
    "": Unit(1, ZERO), "1": Unit(1, ZERO), "%": Unit(0.01, ZERO),
    "m": Unit(1, d(l=1)), "mm": Unit(1e-3, d(l=1)), "cm": Unit(1e-2, d(l=1)), "km": Unit(1e3, d(l=1)), "in": Unit(0.0254, d(l=1)), "ft": Unit(0.3048, d(l=1)),
    "m^2": Unit(1, d(l=2)), "mm^2": Unit(1e-6, d(l=2)), "cm^2": Unit(1e-4, d(l=2)), "in^2": Unit(0.0254**2, d(l=2)), "ft^2": Unit(0.3048**2, d(l=2)),
    "m^3": Unit(1, d(l=3)), "L": Unit(1e-3, d(l=3)), "ft^3": Unit(0.3048**3, d(l=3)),
    "kg": Unit(1, d(m=1)), "g": Unit(1e-3, d(m=1)), "lbm": Unit(0.45359237, d(m=1)),
    "s": Unit(1, d(t=1)), "min": Unit(60, d(t=1)), "h": Unit(3600, d(t=1)),
    "m/s": Unit(1, d(l=1, t=-1)), "ft/s": Unit(0.3048, d(l=1, t=-1)),
    "m/s^2": Unit(1, d(l=1, t=-2)), "ft/s^2": Unit(0.3048, d(l=1, t=-2)),
    "N": Unit(1, d(m=1, l=1, t=-2)), "kN": Unit(1000, d(m=1, l=1, t=-2)), "lbf": Unit(4.4482216152605, d(m=1, l=1, t=-2)),
    "Pa": Unit(1, d(m=1, l=-1, t=-2)), "kPa": Unit(1e3, d(m=1, l=-1, t=-2)), "MPa": Unit(1e6, d(m=1, l=-1, t=-2)), "psi": Unit(6894.757293168, d(m=1, l=-1, t=-2)),
    "J": Unit(1, d(m=1, l=2, t=-2)), "kJ": Unit(1e3, d(m=1, l=2, t=-2)), "Btu": Unit(1055.05585262, d(m=1, l=2, t=-2)), "ft*lbf": Unit(1.3558179483314, d(m=1, l=2, t=-2)), "kWh": Unit(3.6e6, d(m=1, l=2, t=-2)),
    "W": Unit(1, d(m=1, l=2, t=-3)), "kW": Unit(1e3, d(m=1, l=2, t=-3)), "hp": Unit(745.699871582, d(m=1, l=2, t=-3)),
    "Hz": Unit(1, d(t=-1)), "rpm": Unit(1/60, d(t=-1)),
    "A": Unit(1, d(i=1)), "V": Unit(1, d(m=1, l=2, t=-3, i=-1)), "kV": Unit(1e3, d(m=1, l=2, t=-3, i=-1)),
    "ohm": Unit(1, d(m=1, l=2, t=-3, i=-2)), "F": Unit(1, d(m=-1, l=-2, t=4, i=2)), "H": Unit(1, d(m=1, l=2, t=-2, i=-2)),
    "K": Unit(1, d(temp=1), 0, True), "degC": Unit(1, d(temp=1), 273.15, True), "degF": Unit(5/9, d(temp=1), 459.67, True),
    "delta_K": Unit(1, d(temp=1)), "delta_C": Unit(1, d(temp=1)), "delta_F": Unit(5/9, d(temp=1)),
    "kg/m^3": Unit(1, d(m=1, l=-3)), "lbm/ft^3": Unit(16.01846337396, d(m=1, l=-3)),
    "m^3/s": Unit(1, d(l=3, t=-1)), "L/s": Unit(1e-3, d(l=3, t=-1)), "gpm": Unit(6.30901964e-5, d(l=3, t=-1)), "cfs": Unit(0.028316846592, d(l=3, t=-1)),
    "N*m": Unit(1, d(m=1, l=2, t=-2)), "kN*m": Unit(1000, d(m=1, l=2, t=-2)), "lbf*ft": Unit(1.3558179483314, d(m=1, l=2, t=-2)),
    "J/(kg*K)": Unit(1, d(l=2, t=-2, temp=-1)), "kJ/(kg*K)": Unit(1000, d(l=2, t=-2, temp=-1)), "Btu/(lbm*delta_F)": Unit(4186.80058485, d(l=2, t=-2, temp=-1)),
    "W/(m*K)": Unit(1, d(m=1, l=1, t=-3, temp=-1)),
}


class CalculationError(ValueError):
    pass


def add_dims(left: Dims, right: Dims, sign: int = 1) -> Dims:
    return tuple(a + sign * b for a, b in zip(left, right))  # type: ignore[return-value]


def close_dims(left: Dims, right: Dims) -> bool:
    return all(abs(a - b) < 1e-9 for a, b in zip(left, right))


def to_si(value: float, unit_name: str) -> Quantity:
    if unit_name not in UNITS:
        raise CalculationError(f"Unsupported unit: {unit_name}")
    unit = UNITS[unit_name]
    si_value = (value + unit.offset) * unit.scale if unit.absolute_temperature else value * unit.scale
    return Quantity(si_value, unit.dims, unit.absolute_temperature)


def from_si(quantity: Quantity, unit_name: str) -> float:
    if unit_name not in UNITS:
        raise CalculationError(f"Unsupported result unit: {unit_name}")
    unit = UNITS[unit_name]
    if not close_dims(quantity.dims, unit.dims):
        raise CalculationError(f"Result dimension {quantity.dims} does not match expected unit {unit_name} dimension {unit.dims}")
    return quantity.value / unit.scale - unit.offset if unit.absolute_temperature else quantity.value / unit.scale


class Evaluator(ast.NodeVisitor):
    def __init__(self, variables: dict[str, Quantity]): self.variables = variables

    def visit_Expression(self, node: ast.Expression) -> Quantity: return self.visit(node.body)
    def visit_Constant(self, node: ast.Constant) -> Quantity:
        if isinstance(node.value, bool) or not isinstance(node.value, (int, float)): raise CalculationError("Only numeric constants are allowed")
        return Quantity(float(node.value), ZERO)
    def visit_Name(self, node: ast.Name) -> Quantity:
        if node.id not in self.variables: raise CalculationError(f"Missing variable: {node.id}")
        return self.variables[node.id]
    def visit_UnaryOp(self, node: ast.UnaryOp) -> Quantity:
        value = self.visit(node.operand)
        if isinstance(node.op, ast.USub): return Quantity(-value.value, value.dims, value.absolute_temperature)
        if isinstance(node.op, ast.UAdd): return value
        raise CalculationError("Unsupported unary operator")
    def visit_BinOp(self, node: ast.BinOp) -> Quantity:
        left, right = self.visit(node.left), self.visit(node.right)
        if isinstance(node.op, (ast.Add, ast.Sub)):
            if not close_dims(left.dims, right.dims): raise CalculationError(f"Cannot add or subtract dimensions {left.dims} and {right.dims}")
            if left.absolute_temperature and right.absolute_temperature and isinstance(node.op, ast.Add): raise CalculationError("Adding two absolute temperatures is not supported")
            return Quantity(left.value + right.value if isinstance(node.op, ast.Add) else left.value - right.value, left.dims, left.absolute_temperature and not right.absolute_temperature)
        if left.absolute_temperature or right.absolute_temperature: raise CalculationError("Absolute temperatures cannot be multiplied, divided, or exponentiated; use a temperature difference")
        if isinstance(node.op, ast.Mult): return Quantity(left.value * right.value, add_dims(left.dims, right.dims))
        if isinstance(node.op, ast.Div):
            if right.value == 0: raise CalculationError("Division by zero")
            return Quantity(left.value / right.value, add_dims(left.dims, right.dims, -1))
        if isinstance(node.op, ast.Pow):
            if right.dims != ZERO: raise CalculationError("Exponent must be dimensionless")
            exponent = right.value
            return Quantity(left.value ** exponent, tuple(value * exponent for value in left.dims))  # type: ignore[arg-type]
        raise CalculationError("Unsupported binary operator")
    def visit_Call(self, node: ast.Call) -> Quantity:
        if not isinstance(node.func, ast.Name) or node.func.id != "sqrt" or len(node.args) != 1 or node.keywords: raise CalculationError("Only sqrt(value) is allowed")
        value = self.visit(node.args[0])
        if value.value < 0: raise CalculationError("sqrt received a negative value")
        return Quantity(math.sqrt(value.value), tuple(component / 2 for component in value.dims))  # type: ignore[arg-type]
    def generic_visit(self, node: ast.AST) -> Any: raise CalculationError(f"Unsupported expression element: {type(node).__name__}")


def evaluate(expression: str, variables: dict[str, Quantity]) -> Quantity:
    try: tree = ast.parse(expression, mode="eval")
    except SyntaxError as exc: raise CalculationError(f"Invalid expression syntax: {exc.msg}") from exc
    return Evaluator(variables).visit(tree)


def severity_for(expected_si: float, actual_si: float, rel_error: float) -> str:
    if expected_si * actual_si < 0 and abs(expected_si - actual_si) > 1e-12: return "critical"
    ratio = max(abs(expected_si), abs(actual_si)) / max(min(abs(expected_si), abs(actual_si)), 1e-30)
    if ratio >= 10 and rel_error >= 0.9: return "critical"
    return "major"


def check_calculation(calc: dict[str, Any]) -> dict[str, Any]:
    calc_id, location = str(calc.get("id", "unknown")), str(calc.get("location", "unspecified"))
    base = {"calculation_id": calc_id, "location": location}
    issues: list[dict[str, str]] = []
    try:
        if not isinstance(calc.get("variables"), dict): raise CalculationError("variables must be an object")
        variables = {name: to_si(float(spec["value"]), str(spec["unit"])) for name, spec in calc["variables"].items()}
        result = evaluate(str(calc["expression"]), variables)
        expected_spec = calc["expected"]
        expected = to_si(float(expected_spec["value"]), str(expected_spec["unit"]))
        if not close_dims(result.dims, expected.dims): raise CalculationError(f"Expression dimension {result.dims} does not match expected result dimension {expected.dims}")
        independent_value = from_si(result, str(expected_spec["unit"]))
        absolute_error = abs(independent_value - float(expected_spec["value"]))
        relative_error = absolute_error / max(abs(float(expected_spec["value"])), 1e-30)
        tolerance = calc.get("tolerance", {})
        absolute_tolerance = float(tolerance.get("absolute", 1e-9))
        relative_tolerance = float(tolerance.get("relative", 1e-6))
        passed = absolute_error <= absolute_tolerance or relative_error <= relative_tolerance
        if not passed:
            severity = severity_for(expected.value, result.value, relative_error)
            issues.append({"severity": severity, "type": "result_mismatch", "evidence": f"Independent result {independent_value:.12g} {expected_spec['unit']} differs from expected {expected_spec['value']} {expected_spec['unit']} (relative error {relative_error:.3%})."})
        return {**base, "status": "pass" if passed else "finding", "independent_result": {"value": independent_value, "unit": expected_spec["unit"]}, "expected_result": expected_spec, "absolute_error": absolute_error, "relative_error": relative_error, "dimensional_consistency": True, "issues": issues}
    except (KeyError, TypeError, ValueError, OverflowError, ZeroDivisionError) as exc:
        message = str(exc)
        issue_type = "missing_input" if "Missing variable" in message or isinstance(exc, KeyError) else "unsupported_or_inconsistent"
        return {**base, "status": "unsupported", "independent_result": None, "expected_result": calc.get("expected"), "dimensional_consistency": False, "issues": [{"severity": "major", "type": issue_type, "evidence": message}]}


def run(package: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(package.get("calculations"), list): raise CalculationError("Top-level calculations must be an array")
    results = [check_calculation(calc) for calc in package["calculations"]]
    counts = {level: sum(1 for result in results for issue in result["issues"] if issue["severity"] == level) for level in ("critical", "major", "minor", "observation")}
    return {"package_name": package.get("package_name", "Unnamed calculation package"), "summary": {"calculations": len(results), "passed": sum(result["status"] == "pass" for result in results), "unsupported": sum(result["status"] == "unsupported" for result in results), "findings_by_severity": counts}, "results": results, "disclaimer": "Preliminary deterministic arithmetic and dimensional check only; not engineering approval, certification, sealing, or code-compliance review."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        package = json.loads(args.input.read_text(encoding="utf-8"))
        result = run(package)
    except (OSError, json.JSONDecodeError, CalculationError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 2
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output: args.output.write_text(rendered, encoding="utf-8")
    else: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
