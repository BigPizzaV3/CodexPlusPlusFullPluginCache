---
name: mayretire-create-plan
description: Create a Canadian retirement plan through a guided interview and MayRetire MCP when the user has no exported plan or asks to build a new one.
---

# Create a MayRetire plan

The remote MayRetire MCP cannot read a user's account, browser storage, or local
files. Explain that supplied financial data is sent through the assistant to
MayRetire's server for processing. Do not request credentials, government IDs,
payment-card details, or health information. Ask the user for missing material
facts in short batches; distinguish unknown values from real zeros. Engine
defaults and templates are not recommendations.

Read [the guided interview](references/creating-a-plan.md) before constructing
a plan. Use `describe` for unfamiliar fields and collections. Call
`create_plan_payload` with the answers, then `validate_plan_payload` and
`inspect_plan_payload` on the returned complete plan. Review the household,
timeline, goals, benefits, accounts, employment, portfolios, and material
assumptions with the user. Do not calculate while material amounts remain
unknown. Once the baseline is confirmed, use `calculate_plan_payload` and
explain its active success criteria. Return the complete plan JSON when the
user wants to keep or import it; the remote service does not save it to an
account. Use `plan_handoff_url` only when the user asks to view it in MayRetire.

For interface guidance, consult the bundled
[MayRetire tutorial](../mayretire-app-assistant/references/MayRetire_Tutorial.md)
and its relevant screenshots. For the new JSON plan, rely on `describe`,
`inspect_plan_payload`, and calculation results to decide which fields actually
apply. Link the public tutorial when explaining where users enter a setting.

For detailed interpretation after creation, use the `mayretire` skill's
topic-specific references. Do not present projections as personalized
financial, tax, or legal advice.
