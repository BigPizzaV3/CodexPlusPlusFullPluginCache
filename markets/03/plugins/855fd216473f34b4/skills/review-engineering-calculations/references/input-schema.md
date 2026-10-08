# Normalized calculation input

Pass a UTF-8 JSON object to `check-calculations.py`:

```json
{
  "package_name": "Pump sizing memo",
  "calculations": [
    {
      "id": "CALC-01",
      "location": "memo.pdf page 4, Eq. 7",
      "expression": "rho * g * Q * H / eta",
      "variables": {
        "rho": {"value": 1000, "unit": "kg/m^3"},
        "g": {"value": 9.81, "unit": "m/s^2"},
        "Q": {"value": 0.02, "unit": "m^3/s"},
        "H": {"value": 30, "unit": "m"},
        "eta": {"value": 0.75, "unit": "1"}
      },
      "expected": {"value": 7.848, "unit": "kW"},
      "tolerance": {"relative": 0.001, "absolute": 0.001}
    }
  ]
}
```

Each calculation requires `id`, `location`, `expression`, `variables`, and `expected`. Variable names must start with a letter or underscore and contain only letters, digits, and underscores. Supported expression operations are numeric constants, variables, parentheses, `+`, `-`, `*`, `/`, `**`, and `sqrt(...)`. The exponent must be a dimensionless numeric value.

Use explicit units. Use `1` for dimensionless values and `%` for percentage inputs stored as a displayed percent. Temperatures use `K`, `degC`, or `degF`; temperature differences use `delta_K`, `delta_C`, or `delta_F`. Do not use offset temperatures in multiplication or division.

The normalizer must copy source values exactly. When a variable, unit, equation, or expected result is missing, preserve that gap rather than inferring it.
