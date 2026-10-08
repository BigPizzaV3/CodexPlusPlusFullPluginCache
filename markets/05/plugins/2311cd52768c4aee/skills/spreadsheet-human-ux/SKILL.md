---
name: spreadsheet-human-ux
description: Design or review human-facing spreadsheets, Google Sheets, workbooks, dashboards, trackers, models, simulators, and decision tools so they are easy to understand, operate, resume, and trust. Use when spreadsheet usability, navigation, input safety, visual hierarchy, accessibility, cognitive load, or decision clarity materially affects whether people can use the artifact correctly; pair with technical spreadsheet/formula skills rather than replacing them.
---

# Spreadsheet Human UX

Design the **human interaction layer** of a spreadsheet. Preserve analytical correctness, formulas, provenance, and auditability; do not trade them away for visual polish.

This skill complements spreadsheet execution, data-quality, financial-modeling, and domain-verification skills. It does not own those concerns.

## 1. Preflight the human task

Before changing tabs, cells, or styling, identify:

- **User:** who operates or reads the workbook, and what expertise can be assumed?
- **Task:** what recurring job or decision must they complete?
- **Context:** desktop/mobile, shared/solo, time-pressured/exploratory?
- **Frequency:** one-off, frequent, periodic, or resumed after long gaps?
- **Risk:** what happens if a value is misunderstood or the wrong cell is edited?
- **Complexity:** which inputs, scenarios, calculations, outputs, and evidence are materially necessary?
- **Success:** what should the user be able to answer or do without help?

Treat the user model as runtime context. Never hard-code a named person or Project unless that identity is the actual purpose of the artifact.

## 2. Decide whether a UX layer is warranted

Use this skill when human interaction matters. Do not polish a raw evidence table, archival registry, or machine-oriented dataset merely because it is a spreadsheet.

When a structured backend table must also support frequent human use, preserve the data layer and add a user-facing surface instead of weakening the underlying structure.

## 3. Design the common path first

Optimize the first view and normal workflow for the 80% task. Keep advanced assumptions, calculations, evidence, and audit detail accessible through progressive disclosure.

Prefer the smallest visible information architecture that works. A decision-facing workbook often benefits from a path such as:

**START / DASHBOARD → INPUTS → SCENARIOS / DECISION → DETAIL / MODEL → EVIDENCE / SOURCES**

This is a pattern, not a mandatory template. Read `references/design-patterns.md` when designing or materially restructuring the workbook.

## 4. Make inputs safe and obvious

For every material editable input, make visible:

- human-readable label;
- current value;
- unit/format;
- status or source when material;
- short clarification where ambiguity is likely.

Prefer prevention over warning-after-the-fact: controlled dropdowns, validation bounds, protected formula regions, safe defaults, explicit required fields, and checks for impossible combinations.

Group inputs by **user intent**, not by formula dependency. Reduce typing when options are known, while preserving spreadsheet flexibility where exploration is valuable.

## 5. Make outputs interpretable

A key result should carry enough context to stand on its own: value, unit, relevant period, active scenario/baseline, and a concise interpretation when useful.

Expose the variables that can change the decision. Prefer sensitivities, ranges, or breakevens to false precision when uncertainty is material.

Charts are optional. Use them only when a relationship, trend, sensitivity, or composition is faster to understand visually than as a number or table.

## 6. Reduce cognitive load without hiding logic

Use recognition over recall: visible labels, units, edit conventions, scenario indicators, legends, and nearby explanations.

Use consistent visual semantics for the same kinds of things across the workbook. Favor spacing, alignment, hierarchy, and restrained emphasis over decorative color or dense borders.

Never encode meaning only by color. Keep material calculations and evidence reachable so simplification does not become opacity.

## 7. Preserve agency and resumability

Do not turn a spreadsheet into a rigid pseudo-application. Users should be able to inspect assumptions, understand material calculation logic, safely change scenario inputs, see consequences, and reach evidence.

Design so the workbook remains understandable after time away. Make the current scenario/period, edit conventions, primary result, warnings, and next action easy to recover.

## 8. Design for errors, accessibility, and device constraints

Warnings should explain:
1. what is wrong;
2. why it matters;
3. what to change or check.

Consider missing inputs, stale data, invalid dates/rates, formula errors, contradictory assumptions, impossible values, and scenario-not-selected states.

Maintain readable typography, descriptive headers, logical table structure, adequate contrast, text labels in addition to color, minimal unnecessary merged cells, and meaningful number formats.

For mobile/tablet use, keep the critical path narrow and vertically understandable; do not place essential controls far to the right or depend on hover/comments for core instructions.

## 9. Apply optional domain profiles only when relevant

For financial, investment, fiscal, or other decision models, read `references/financial-decision-model.md`.

Domain profiles add specialized UX concerns; they do not override the core method or stronger domain evidence requirements.

## 10. Validate with realistic human tests

Before delivery or after a material redesign, run the tests that fit the workbook:

- **5-second:** is the purpose and principal result immediately identifiable?
- **Common-task:** can the main task be completed without hunting through technical tabs?
- **Recognition:** are editable cells, units, scenario, and status obvious without memory?
- **Error:** do blank, invalid, extreme, or contradictory inputs fail safely and explain recovery?
- **Resume:** would the workbook still make sense after weeks away?
- **Small-screen:** can the core result and controls still be used on a narrow viewport when relevant?
- **Accessibility:** does meaning survive without color and remain logically readable?
- **Traceability:** can a material result be followed to assumptions/evidence without reverse-engineering the whole workbook?

Use realistic data. Do not declare UX complete from an empty template alone.

## Delivery gate

PASS only when the primary task is obvious, the common path is short, inputs and outputs are unmistakable, major errors are prevented or recoverable, uncertainty is visible, decision-relevant detail remains accessible, the first view is calm and scannable, accessibility/device risks were considered, and formulas/data remain technically correct and traceable.

## Boundaries

Do not:

- hide uncertainty or provenance for aesthetic simplicity;
- expose every technical calculation on the default surface;
- over-engineer a simple one-off sheet;
- make color the only status signal;
- assume a dashboard is useful merely because the workbook has many tabs;
- make the grid rigid when spreadsheet flexibility is valuable;
- optimize visual polish at the expense of correctness or auditability;
- duplicate technical spreadsheet execution rules already owned by another skill.

For the external basis and adaptation provenance, read `references/provenance.md`.
