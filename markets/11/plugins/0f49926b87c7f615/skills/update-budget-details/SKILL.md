---
name: update-budget-details
description: Find Grid budget details and preview confirmed cost changes or spreadsheet detail imports, including shared-bid impacts, duplicate decisions, and Estimate versus Running phase selection.
---

# Review and update Grid budget details

Use the connected Grid MCP schemas and choose the named operation:

- Create: `grid.preview_create_details` / `grid.apply_create_details`.
- Edit values or formulas: `grid.preview_update_details` / `grid.apply_update_details`.
- Add links: `grid.preview_add_detail_budget_links` / `grid.apply_add_detail_budget_links`.
- Replace links: `grid.preview_replace_detail_budget_links` / `grid.apply_replace_detail_budget_links`.
- Remove links: `grid.preview_remove_detail_budget_links` / `grid.apply_remove_detail_budget_links`.

Each batch contains one operation. New details may include initial associations
with action=add. Updates preserve links; link tools preserve values and require
values={}. Retired generic detail and budget-named tools are not advertised.

1. Resolve the project and use `grid.list_details` to discover existing records.
   Updates use the existing detail ID. Never choose or create a budget merely
   to edit a detail. Follow pagination until next_after_id is null.
2. Prepare only requested values. Omitted fields and associations are preserved.
   Use the matching add/replace/remove link operation only when the user asks
   to change links. Budget memberships may have no lines. Multiple lines in a budget use
   positive allocation percentages totaling 100 per budget for Estimate/Running.
   Existing Actuals support only link operations: preserve their IDs, values,
   phases, source documents and settlement. Actual allocations total 100 across
   all linked budgets (for example, 50/50), not 100 in each. Never move an
   Estimate/Running row to Actual or copy an existing Actual to code it. Show
   every affected source budget and derived composite impact.
3. Discover globals with `grid.list_project_globals`. Send live expressions in
   values.formulas; omit the numeric input for that field. An explicit numeric
   input replaces its formula. Omitted expressions stay live. Global edits use
   their own preview/confirmation, followed by a fresh detail preview. Preserve
   decimal fringe rates and stored duration units.
4. For spreadsheets, parse the workbook in the client and send normalized
   create rows, never a file path. Preserve groups, unique source IDs, explicit
   zeros and source_total; exclude headers/subtotals. Resolve duplicates and
   source reconciliation before confirmation. First-detail replacement of line
   pricing requires an explicit convert/replace choice.
5. Preview the exact rows. Show old/new values, expressions and resolved globals,
   old/new associations, warnings and affected line totals. Selected detail totals
   are not the complete project budget. Explain unsupported overtime, adjustments,
   direct line formulas, or conflicting shared global scopes; do not approximate.
6. Obtain confirmation of that preview. Apply the unchanged input with
   expected_revision, a fresh request_id UUID and confirm_preview=true. Retry
   transient failures with identical input and UUID; changed intent or stale data
   requires a new preview and confirmation.
7. Verify saved IDs, values, live formulas and association state with
   grid.list_details. Use returned provenance to reconcile imported source rows.

## Review a saved Actual against Running

Cost capture and Running review are separate decisions. For an automatic follow-up
on a new confirmed Actual or new budget target, inspect `automatic_running_review`
for each source bid. `skip_collapsed` means do not ask the Running question and do
not supply a default Replace/Add/Remaining, null decision or legacy full coverage.
Keep ordinary cost capture, coding, duplicate checks and write confirmation intact.
`eligible` is eligibility only: read fresh `grid.get_forecast_reconciliation_context`
after capture, resolve an exact saved Actual and Running detail/allowance, then
follow `requires_decision` and existing line finality. Ordinary corrections do not
require a new closure question. `unavailable` is unresolved, not permission to skip
or infer an answer. Resolve missing/malformed source settings before reconciliation.

For a producer's explicit request to edit/reconcile Running, use the same context
and `grid.preview_forecast_reconciliation` even when its section is collapsed.
When a decision is needed, ask Replace Running, Add to Running, or set what is
still expected. Remaining includes open commitments. Show the complete financial
preview and affected source budgets, then obtain confirmation before applying
with unchanged selection/decision, preview time/revision and a stable request UUID.
A closed scope needs no new closure question; any separate null-decision apply
still requires its supported confirmed preview. Never set financial
`requires_decision` false merely to suppress a prompt.

For shared/multi-bid targets evaluate every bid independently. A collapsed sibling
cannot suppress an expanded bid's eligible review. Do not apply one shared-scope
mutation if that would silently reconcile a collapsed sibling; retain unresolved
matching until an explicitly supported scope is selected. Legacy document import
can defer collapsed, unavailable or already-reviewed Running matches while still
saving independent cost. A warning is not completed reconciliation or a reason
to import the Actual again. Time-card coding and Wrapbook import/recovery policies are live guidance outside
their cost revisions and receipts; always read fresh forecast context after saving.

These tools operate on saved Actuals and never change payments. Unsupported FX,
split assignments, formulas or commitment fulfillment remain unresolved. Use the
deployment's advertised schemas and refresh stale previews. Stored phase amounts
remain authored values; derived Running after Replace can still track Actuals.
The collapse question policy does not itself freeze that calculated number. Do
not present legacy phase fields as reconciled current totals or claim frozen
Running while the retained-value reader work is pending. Durable history is a
separate workflow from session Undo/Redo.
