# Spreadsheet contract

Use these defaults when no project-specific template overrides them. Do not add columns or tabs just because they are available here.

## Feature List

Default columns: `Section | Feature | Function | Description | Priority | Planned Milestone`.

- Section groups related product capabilities. Merge contiguous identical sections; merge repeated feature names only within the same section.
- Feature is the capability or system. Function is an existing meaningful subdivision, not a compulsory label on every row. Detailed implementation tasks belong in the plan.
- Description states behavior and scope concisely. New authorized descriptions go directly into blank cells. Proposed changes to an existing accepted description stay in its note until authorized. When a proposal is promoted, remove duplicate proposal text from the note while preserving unrelated owner decisions.
- Priority uses the owner's scale. If none exists, propose a small explicit scale such as 1 = essential, 2 = important, 3 = deferrable. Never interpret priority as completion status.
- Planned Milestone references the live milestone-name range, rather than a manually duplicated option list. Default to a primary delivery milestone; ask/preserve the owner's multiple-selection convention when needed. Use blank for unscheduled work unless another convention is agreed. Explain blank in the header note; do not invent a Backlog milestone to populate the dropdown.

## Milestone Plan

Default columns: `Milestone | Milestone OKR | Section | Feature | Function | Description | PIC | GD | Art | Dev | Visual | QA`.

Adapt discipline columns to actual team workflow. Visual means visual integration/review when retained from a template; it does not imply an additional team member.

- Milestone: short stable name, optionally with an ordering code; no dates or durations.
- Milestone OKR: start/end weeks or dates, estimated duration, Objective and measurable Key Results. Merge per milestone and align text at the top for readability.
- Section/Feature: correspond to the backlog. Merge contiguous groups only within each milestone; never merge across milestone boundaries.
- Function: a concrete smaller increment when needed; otherwise blank.
- Description: that milestone's deliverable. Do not add per-row source-copy notes by default; the backlog is the detail reference.
- PIC: editable dropdown with agreed names or roles. Status dropdowns use agreed values; initialize only new work, preserving live progress on revisions.
- Design, art, implementation, integration and QA tasks can exist here without becoming standalone product features. Work outside the agreed team's responsibility stays outside this plan, with necessary handoff dependencies summarized in the relevant OKR or deliverable.

Example OKR shape: `Weeks 08–12 · 5 weeks`, followed by an Objective such as completing the core-to-meta loop, then KRs for playable coverage, save/reward edge cases and observed onboarding completion. Select actual thresholds from the brief; this example is not a universal benchmark.

## Presentation and native controls

Follow the supplied native template. Otherwise use a dark readable header, restrained milestone fills, neutral section fills, thin borders, wrapped descriptions, sensible column widths and frozen headers. Freeze only enough columns to retain useful reading width. Avoid explanatory banner rows and extra administrative columns.

For Google Sheets, use a native dropdown-from-range tied to the actual milestone column or a dynamic range derived from it. A dropdown spanning merged milestone blocks must expose the non-empty names correctly. Verify that names remain valid after row deletion, reordering or tab renaming. Do not assume editing the source label rewrites existing selected values; explicitly reconcile those values after renaming.

Preserve native chip/multi-select metadata through supported operations where possible. Basic validation is not proof of multi-select capability. If the available API cannot preserve or configure the requested behavior, disclose that precise limitation rather than silently changing it or claiming success. Do not convert a merged sheet into a native table merely to obtain chip styling.

Match rows using stable IDs if present, otherwise a normalized Section/Feature/Function key with duplicate checks. Do not force visible ID columns into a compact owner-approved template. Maintain an internal coverage map during construction and verification.
