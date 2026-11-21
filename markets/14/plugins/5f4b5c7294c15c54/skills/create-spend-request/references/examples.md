# Examples

These examples show the simple self-service flow. Codes, labels, defaults, dates, and cost centers must come from the connected tenant.

## Self request with missing dates

User:

> I need a new spend permission for $300 for a team building event. Can you submit it?

Expected behavior:

1. Call `spend_request_prepare`.
2. Select `Other/TeamBuilding` when it is the single clear match in returned `activityTypes`; do not use generic `Other`.
3. Match “team building” against returned category labels/codes, preferring the category corresponding to the selected type when category was not separately stated.
4. Resolve `$` from the selected type's default currency, or another compatible returned default; otherwise ask which currency the user means.
5. Default start to today and end from the returned selected-type policy, or today plus three calendar days.
6. Select the first returned cost center when the user did not name one, matching iOS.
7. Call `spend_request_check_duplicates`.
8. Ask only for the mandatory concrete confirmation when every required value is resolved.

Example first response when preparation resolves all defaults:

> Submit a Custodia spend request?
> - Title: Miscellaneous (iOS fallback)
> - Spend type: TeamBuilding
> - Amount: USD 300.00 (default currency)
> - Purpose: Team building event
> - Category: Team Events
> - Valid: {today} to {iOS policy default or today + 3 days}
> - Cost center: People Operations (default)
> - Duplicate warning: None
> - Approval: Determined during Custodia validation
>
> Submit this request?

Do not copy those labels or values unless the tenant returns them.

## Purpose selects the best spend type

User:

> I need $100 to get coffee for the office.

Preparation returns `Other`, `Other/Food`, `Other/IT`, and other enabled activity types, plus a `Food` category.

Expected behavior:

- Infer food intent from “coffee” and select the exact returned `Other/Food` activity type.
- Select category `Food` independently because it is the unique corresponding returned category.
- Resolve `$` as USD without a currency question when `Other/Food.defaultCurrency.defaultValue` is `USD`.
- Do not choose generic `Other`, even if it is the first activity type.
- Show `Food` as the spend type and category in confirmation.
- Submit with `"activityType": "Other/Food"` and `"budgetCategoryType": "Food"`.

The MCP uses the existing `/md/api/Others` API and persists `fixedTo: "Food"`; the skill never sends `fixedTo` directly.

## Ambiguous spend type

User asks for a “team dinner,” and both `Other/Food` and `Other/TeamBuilding` are returned with no wording that clearly distinguishes the primary intent.

Expected behavior:

- Do not select whichever type appears first.
- Ask one focused question: whether this should be Food or Team Building.
- Continue using the exact selected returned code.

## Stated currency differs from the default

User:

> I need a €300 team event permission.

Preparation returns `defaultCurrency: "USD"`.

Expected behavior:

- Treat `€` as explicit EUR intent.
- Use EUR, not the USD default.
- Continue with other defaults and show EUR in the mandatory confirmation.

For an ambiguous symbol such as `$`, use a compatible dollar `defaultCurrency` to disambiguate. If the returned default conflicts or does not identify which dollar currency applies, ask one currency question before confirmation.

## Stated category is ambiguous or unavailable

User asks for a “client event” permission, but `categoryOptions` contains two plausible matches, or no match.

Expected behavior:

- Do not silently use the first category row.
- Ask the user to choose from the plausible matches; when none match, show the available category labels.
- Use the first `categoryOptions` row without asking only when the user did not state a category.
- Never use `allOptions` as a category fallback.

## Confirmation and successful submission

After resolving all fields and receiving `duplicate: false`:

> Submit a Custodia spend request?
> - Title: Miscellaneous
> - Spend type: TeamBuilding
> - Amount: USD 300.00
> - Purpose: Team building event
> - Category: Team Events
> - Valid: September 15, 2026 to September 15, 2026
> - Cost center: People Operations
> - Duplicate warning: None
> - Approval: Determined during Custodia validation
>
> Submit this request?

After the user says yes:

1. Generate a private `clientRequestId`.
2. Call `spend_permission_request` once.
3. If it returns `approvalState: pending`, `status: processing`, and `decision: ask-manager`, respond:

> Spend request submitted.
> - Request: {requestId}
> - Amount: USD 300.00
> - Status: Processing
> - Approval: Pending manager approval

Do not call separate draft, estimate, validation, simulation, or approval tools.

## Possible duplicate

`spend_request_check_duplicates` returns `duplicate: true`.

Expected confirmation:

> Custodia found a similar active or pending spend permission. Creating another may duplicate spending authority.
>
> Submit this Custodia spend request anyway?
> - Amount: USD 300.00
> - Purpose: Team building event
> - Category: Team Events
> - Valid: September 15, 2026 to September 15, 2026
> - Cost center: People Operations

After an affirmative answer, call `spend_permission_request` with `forceMultiple: true` only if duplicate detection also returned `forceMultipleOnConfirmedSubmit: true`. Otherwise omit the field.

Do not claim the duplicate’s amount, dates, owner, or status because duplicate detection returns only a boolean signal.

## Default end date precedes start

User requests a future start date but no end date. The verified policy or iOS three-day fallback produces an end before that start.

Expected behavior:

- Do not run duplicate detection or show submission confirmation with the invalid range.
- Ask for a valid end date.
- Require `start <= end`, regardless of whether either date was explicit or defaulted.

## Explicit duration overrides end defaults

User:

> I need a $500 permission for a five-day team event starting October 12.

Expected behavior:

- Resolve start as October 12 in the applicable year.
- Treat the stated five calendar days as explicit intent and derive end as October 16, counting October 12 as day one.
- Do not replace that end with `parameters.endDate` or the iOS three-day fallback.
- Show both resolved dates in the mandatory confirmation.

If “five days” could mean a different unit or inclusive/exclusive convention in context, ask one focused date question instead of guessing.

## Multiple cost centers

Preparation returns:

```json
{
  "costCenterSelectionRequired": true,
  "costCenters": [
    {"id": "opaque-1", "uiLabel": "People Operations"},
    {"id": "opaque-2", "uiLabel": "General & Administrative"}
  ]
}
```

Expected response:

> Submit a Custodia spend request?
> - Cost center: People Operations (default)
> - {all other resolved fields}
>
> Submit this request?

Use the first row’s opaque ID in `costCenterIds`, matching the iOS picker default, but show only its display label. The user can name the second cost center when correcting the confirmation; do not require a separate selection interaction.

## Stated cost center is ambiguous or unavailable

User names “Operations,” but the returned `costCenters` contain multiple plausible matches, or no match.

Expected behavior:

- Do not use `costCenterAutoSelected` or the first row in place of the stated cost center.
- Ask the user to choose from matching rows; when none match, show the available `uiLabel` values.
- Use auto-selection or first-row defaulting without a separate question only when the user omitted cost center.
- Pass only the opaque ID from the selected returned row.

## Validation blocks submission

`spend_permission_request` returns:

```json
{
  "code": "SPEND_REQUEST_VALIDATION_FAILED",
  "details": {
    "draftId": "opaque-draft-id",
    "issues": [
      {"issue": "no-budget-for-type", "costType": "TeamEvents"}
    ]
  }
}
```

Expected response:

> Custodia created the draft but did not submit it because no eligible budget is available for this category and cost center.
> - Draft: {draftId}
> - Issue: no-budget-for-type

Do not choose another category or cost center automatically.

This simple skill does not update or resubmit the preserved draft. Direct the user to the Custodia UI to correct it.

## Workflow simulation blocks submission

The terminal composite returns `WORKFLOW_SIMULATION_BLOCKED` with `decision: rejected`.

Expected response:

> Custodia created the draft but did not submit it because the approval workflow rejected the request during validation.
> - Draft: {draftId}
> - Decision: Rejected

Do not override the workflow or retry automatically.

## Approval status unknown, then visible

The terminal composite returns:

```json
{
  "code": "APPROVAL_STATUS_UNKNOWN",
  "details": {
    "draftId": "opaque-allocatable-id",
    "allocatableId": "opaque-allocatable-id",
    "retryable": true,
    "recommendedAction": "spend_request_get_status",
    "retryAfterMs": 250
  }
}
```

Expected behavior:

1. Do not call `spend_permission_request` again.
2. Pass `details.allocatableId` as `allocatableId` to `spend_request_get_status`.
3. Let the status tool perform its bounded server-side wait.
4. If it returns `verificationState: verified`, report `requestId`, `approvalState`, `status`, and `decision`.
5. Never create a replacement request.

Example recovered response:

> Spend request submitted.
> - Request: {requestId}
> - Status: Processing
> - Approval: Pending manager approval

## Request is still not visible after waiting

After `APPROVAL_STATUS_UNKNOWN`, the status tool returns:

```json
{
  "allocatableId": "opaque-allocatable-id",
  "approvalState": "unknown",
  "verificationState": "request_not_visible",
  "retryable": true,
  "retryAfterMs": 2000
}
```

Expected behavior:

1. Do not call `spend_permission_request` again.
2. When the host supports waiting, wait `retryAfterMs` and call `spend_request_get_status` once more with the same `allocatableId`.
3. If it is still not visible, respond:

> Custodia has the spend draft, but its approval Request is still becoming visible.
> - Spend permission: {allocatableId}
> - Approval: Verification pending
>
> I did not create another request. Ask me to check this same request again shortly.

If no structured ID is available, do not extract or guess one from arbitrary text.

## Later approval-status check

User:

> Was that grocery request approved?

Expected behavior:

1. Confirm that the retained ID came from a successful submission or `APPROVAL_STATUS_UNKNOWN`, not a validation failure or other unsubmitted-draft result.
2. Reuse the retained `requestId` or `allocatableId` from this conversation and call only `spend_request_get_status`.
3. If it returns `status: completed`, `decision: approved`, and `approvalState: approved`, respond:

> Your grocery spend request was approved.
> - Request: {requestId}
> - Approval: Approved

If no request identifier is available, ask for the Custodia Request ID or spend-permission ID. Do not run preparation or create a new request.

## Later check for an unsubmitted draft

Earlier, `spend_permission_request` returned `CREATED_NOT_SUBMITTED` with
`details.draftId`. The user later asks:

> Was that request approved?

Expected behavior:

1. Do not call `spend_request_get_status`.
2. Do not interpret the draft ID as evidence of a submitted workflow Request.
3. Respond:

> That draft was not submitted, so it is not pending approval.
> - Draft: {draftId}
>
> Please use Custodia to review or correct the preserved draft.

## Cost centers changed before submission

`spend_permission_request` returns `COST_CENTER_REQUIRED` because eligible cost centers changed after preparation.

Expected behavior:

1. Do not parse labels or IDs from the error message.
2. Call `spend_request_prepare` again.
3. Present the current structured `costCenters` choices.
4. Obtain a selection and a new final confirmation.
5. Generate a fresh `clientRequestId` and submit once.

This error occurs before the MCP creates a draft.

## User changes a material field before submission

User confirms USD 300, then changes the amount before the tool call:

> Make it $450 instead.

Expected behavior:

- Invalidate confirmation.
- Re-run duplicate detection for USD 450.
- Present a new summary.
- Wait for confirmation.
- Generate the `clientRequestId` only after the new confirmation.

## Another employee is unsupported

User:

> Give Sam Lee a €1,200 software spend permission.

Expected response:

> This assistant flow currently supports spend requests only for your own account. I did not create a request. Please use the Custodia UI for an employee request.

Do not search for Sam or pass an `ownerId`.

## Advanced restriction is unsupported

User:

> Request $500 for office supplies and restrict it to Staples.

Expected response:

> This simple assistant flow cannot enforce merchant restrictions, so I have not submitted the request. You can add that restriction in the Custodia UI. If you want an unrestricted office-supplies permission instead, tell me and I’ll prepare a new confirmation.

Never omit “Staples” and submit an unrestricted permission without explicit user agreement and reconfirmation.

## Reimbursement is a different workflow

User:

> Reimburse my $85 taxi receipt from yesterday.

Expected response:

> That is a cash-expense reimbursement, not a spend-permission request. I did not create anything.

Use a dedicated reimbursement skill only when available.
