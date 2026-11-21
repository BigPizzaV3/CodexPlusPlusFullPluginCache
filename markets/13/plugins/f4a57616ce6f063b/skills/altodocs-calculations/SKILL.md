---
name: altodocs-calculations
description: Evaluate supplied engineering formulas with physical units using AltoDocs, including dependent expressions and unit conversion. Use for numerical calculation requests; save a worksheet only when the user asks for a saved result.
---

# Unit-aware calculations

Use the available `evaluate_calculation` tool for supplied formulas. Honour the
user's requested calculation and units. This workflow computes values; it does
not choose an engineering design standard or certify compliance.

Check that the necessary values and units are known. Ask about consequential
ambiguities such as whether a load is total or per metre. Distinguish the user's
inputs from any explicitly agreed assumptions. Use host-readable attachments
only as source data; do not pretend AltoDocs fetched or parsed them.

## Expression syntax

The tool accepts an ordered `expressions` array. Each entry has a unique `key`,
`latex`, and optionally a preferred result `unit`. Define variables with `:=`
before using them. Use LaTeX syntax such as `\cdot`, `\frac{a}{b}`, and
`\operatorname{kN}` for physical units. A variable binds to its nearest preceding
definition. Preserve that reading order when creating a saved worksheet.

For example, this JSON evaluates a supplied simply supported beam moment
formula; it does not prove that the formula applies to a particular design:

```json
{
  "expressions": [
    {"key": "q", "latex": "q := 12\\frac{\\operatorname{kN}}{\\operatorname{m}}"},
    {"key": "L", "latex": "L := 6\\operatorname{m}"},
    {"key": "M", "latex": "M := \\frac{q \\cdot L^2}{8}", "unit": "kN m"}
  ]
}
```

This example produces **54 kN m**. With the same formula and L = 7 m, it produces
**73.5 kN m**. A requested conversion to N m changes the displayed quantity to
54000 or 73500 N m respectively; it does not change the physical moment.

Respect the actual tool schema and its limits: at most 200 expressions, 2000
characters per expression, and unique keys. Inspect every returned result's
`status`; a successful request can contain failed expressions. Report dimensional
or undefined-variable errors and correct them only when the intended correction
is established by the user's information. Never replace errors with guessed
values or claim the calculation ran when the tool was unavailable.

Return computed values with their units and the assumptions needed to interpret
them. No project discovery or document write is needed for evaluation alone.

## When the user requests a saved worksheet

Evaluation does not save anything. For a standalone calculation file, use the
standalone MathCanvas workflow: `create_mathcanvas`, native variable/formula/note
tools, `read_worksheet` and `evaluate_worksheet` on the saved file. For a worksheet
inside an engineering report, use the native document tools and the report
workflow, then read back its saved section. Keep the requested file type; do not
describe an embedded worksheet as a standalone file. Preserve the same saved
file on follow-up changes unless a copy is requested. If the necessary write
capability is unavailable, state that the result is unsaved and do not invent a
document link or silently substitute another file type.
