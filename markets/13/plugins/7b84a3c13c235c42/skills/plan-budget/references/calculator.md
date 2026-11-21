# Budget calculator

Requires Python 3.9+. Run the bundled `../scripts/budget.py` with one UTF-8 JSON file path using host-native Python. The path is an argument, not interpolated code. No dependency installation, network request, or output file write occurs. Output JSON goes to stdout; errors go to stderr and exit status is 2.

## Input
`nights`: integer 1–3660. `base_currency`: uppercase three-letter currency code. `rates`: map of currency to base-currency units per one unit of that currency (positive); base currency is implicitly 1. Every item needs exactly `label`, `amount` (nonnegative), `currency`, `basis` (`night`, `month`, `stay`), and `kind` (`recurring`, `one_time`, `deposit`). One-time costs and deposits require stay basis. At least one item, at most 200. `reserve` and optional `target` are in base currency. `contingency_percent` is 0–100, defaults to 0. `reserve` defaults to 0. Explicitly disclose when either default is used. Do not use zero to hide unknown costs.

`amount` can be a decimal string; use strings to preserve supplied precision. All numeric inputs must be finite. Rate freshness and code validity beyond the three-letter format are the planner's responsibility.

## Formulas
Recurring spending = sum of amount × explicit rate × multiplier. Multiplier = nights for night basis, nights / 30 for month basis, 1 for stay basis. Spending = recurring + one_time. Contingency = spending × percent / 100. Cash needed = spending + contingency + refundable deposits + emergency reserve. Headroom = target − cash needed (negative means shortfall). Reserve and deposits are not charged contingency.

Two-decimal display uses half-up rounding; it is not an assertion of the currency's settlement precision. Totals use unrounded values, so displayed rounded lines may differ by a cent from the displayed total. No real-time prices or rates are embedded.

See `../assets/example-input.json` for a fictional arithmetic fixture. Its USD/EUR rate and amounts are synthetic, not recommendations or current quotes.
