---
name: drugfree-calculator
description: Open DrugFree when the user asks for its nonclinical day count, milestones or optional savings calculator.
---

# DrugFree

Call open_drugfree with an empty object. Enter calculation values in the interactive UI. Do not send personal values as tool arguments.

Use a day count in the UI, optionally a calendar date after the local privacy notice. Calendar progress = calendar days between the selected date and today in the selected timezone; the starting day is day 0. Assumed savings = days × optional assumed daily amount; this is an estimate, not actual financial data. Milestones: 1, 7, 30, 90, 180, 365 days; these are arbitrary calendar markers, not health claims. Example: 7 days × 3.50 EUR = 24.50 EUR. Without UI, provide these formulas or a fictional example; do not ask for sensitive personal details in chat.

This tool cannot assess withdrawal, diagnose, recommend doses, tapering or treatment, or certify recovery. For withdrawal concerns seek a qualified healthcare professional; do not use this counter to decide how to stop or change medication. If there is immediate danger, contact local emergency services.

Do not ask for substances, diagnoses, treatment details, journal text, medical targets or weight. Do not recommend purchases or upgrades. Do not describe chat messages or MCP requests as local. Only calculator UI values stay in its ephemeral memory. If UI is unavailable, explain the formula and use fictional examples; do not solicit sensitive dates in chat.
