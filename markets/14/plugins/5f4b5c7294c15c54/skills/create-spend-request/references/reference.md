# Custodia MCP Contract: Simple Self-Service Spend Request

This skill targets the four domain tools exposed by the Custodia MCP. Tool schemas and descriptions are authoritative. Never replace a missing domain tool with generic HTTP, browser, shell, or CRUD access.

## Supported domain model

The flow creates a self-owned, one-time activity through the existing `Other` model while preserving the best-fitting enabled `Other/<type>` variant:

```text
spend_request_prepare
  → spend_request_check_duplicates
  → user confirmation
  → spend_permission_request
      → deterministic Other draft
      → persistent estimate
      → saved server estimate
      → pre-request validation
      → approval workflow simulation
      → request approval
  → workflow Request
  → eventual Allocation / spend permission after approval
```

The submission composite owns the internal write sequence. The skill must not try to reproduce it with lower-level tools.

## Required tools

### `spend_request_prepare`

Read-only preparation for the authenticated user.

Call with:

```json
{}
```

An optional `category` may narrow returned options, but it must be a value selected from a prior preparation response. Do not pass `userId` or `companyId`.

Expected response fields:

- `activityType`: the base model, `Other`.
- `activityTypes`: company-enabled, self-creatable `Other` type codes intersected with the user’s ACL-filtered options. These are the authoritative candidates for semantic spend-type selection.
- `categoryOptions` and `allOptions`: live tenant codes and safe labels.
- `defaultCurrency`: unambiguous user/activity default when available.
- `parameters`: current user/type policy and defaults.
- `costCenters`: eligible rows with opaque `id` and safe `uiLabel`.
- `costCenterSelectionRequired`: true when multiple eligible rows require visible review; this skill may still apply the iOS first-row default when the user omitted cost center.
- `costCenterAutoSelected`: the sole eligible cost center when unambiguous.

Preparation does not create a draft.

### `spend_request_check_duplicates`

Read-only advisory duplicate detection.

Required arguments:

```json
{
  "budgetCategoryType": "Other/OfficeSpend",
  "amount": 300,
  "currency": "USD",
  "start": "2026-09-15",
  "end": "2026-09-15"
}
```

Do not pass owner/company IDs. `boundToCardId` is outside this skill’s simple flow.

Response behavior:

- `duplicate: false`: continue to confirmation.
- `duplicate: true`: explicitly warn the user.
- `forceMultipleOnConfirmedSubmit: true`: pass `forceMultiple: true` only when `duplicate` is also true and the user confirms continuing.
- `forceMultipleOnConfirmedSubmit: false` or absent: omit `forceMultiple`, even when the user confirms the duplicate.

The tool returns a duplicate signal, not a matching permission summary. Never invent matching request details.

### `spend_permission_request`

Terminal write composite. Call only after explicit user confirmation.

Required arguments:

- `clientRequestId`: private stable ID generated after confirmation.
- `name`: explicit/returned activity title or the iOS fallback `Miscellaneous`.
- `amount`: positive JSON number.
- `currency`: three-letter ISO currency.
- `start` and `end`: concrete ISO dates.
- `budgetCategoryType`: exact returned category code.

Supported optional arguments for this skill:

- `description`.
- `purpose`.
- `costCenterIds`, selected from preparation.
- `forceMultiple`, only for a confirmed duplicate when `forceMultipleOnConfirmedSubmit` is true.
- `activityType`, copied exactly from the selected `spend_request_prepare.activityTypes[].code`; generic `Other` remains the fallback only when no more specific type uniquely matches.

Do not pass `ownerId` or `companyId`. Do not pass advanced fields absent from the schema.

The composite performs these existing backend operations:

1. Read an existing Request by deterministic allocatable ID.
2. `PUT /md/api/Others`, persisting the selected `Other/<type>` suffix as `fixedTo` (`Other` maps to `*`).
3. `POST /md/api/Others/:id/estimate` with persistence.
4. `PATCH /md/api/Others/:id` with the server estimate.
5. `POST /md/api/Others/:id/validate-pre-request`.
6. `POST /md/api/Others/:id/simulateWorkflow` with scenario `approval`.
7. `POST /md/api/Others/:id/request-approval`.
8. Read back the workflow Request when approval completion is uncertain.

Expected success fields:

- `id`: associated Other allocatable ID.
- `requestId`: authoritative workflow Request ID.
- `status`: authoritative Request status.
- `decision`: workflow decision when available.
- `approvalState`: normalized approval result: `pending`, `approved`, `rejected`, `canceled`, `failed`, or `unknown`.
- Confirmed request summary fields.

`processing` means pending approval. It does not mean approved.

### `spend_request_get_status`

Read-only authoritative Request lookup by associated allocatable ID or workflow Request ID. The tool performs a short bounded server-side wait so callers do not need a sleep primitive to bridge normal post-submission visibility lag.

Call with exactly one identifier:

```json
{
  "allocatableId": "<id returned by the submission tool or structured error>"
}
```

or:

```json
{
  "requestId": "<workflow Request id returned by submission or an earlier status check>"
}
```

Do not pass user/company IDs.

Use after an uncertain submit result, when reading the status of the just-submitted draft, or when the user later asks whether it was approved. If a Request is found, never submit again.

Status response fields:

- `verificationState: verified`: `approvalState`, `status`, and `decision` describe the authoritative Request.
- `verificationState: request_not_visible`: the self-owned draft exists, but its Request is not visible after the bounded wait. This does not prove that the draft was submitted. Retry once after `retryAfterMs` only when the ID came from `APPROVAL_STATUS_UNKNOWN`; otherwise report that no workflow Request is visible and the draft may be unsubmitted.
- `SPEND_REQUEST_NOT_FOUND`: neither the scoped workflow Request nor, for allocatable lookup, the scoped draft was found.

Map recovery error fields explicitly: pass `details.allocatableId` as `allocatableId`; if it is absent, pass `details.draftId` as `allocatableId`. Do not pass either value as `requestId`.

## Identity and authorization

This skill is self-service only:

- MCP authorization requires `Activity/CreateRequest`.
- The MCP derives user and company from the authenticated session.
- Owner/company arguments should be omitted.
- On-behalf-of and cross-company requests are rejected.
- The selected `Other` option remains subject to backend feature, profile, cost-center, and budget policy.

## Field resolution rules

- **Amount:** Positive JSON number from the user. Do not default it in this simple flow: iOS applies `defaultAmount` only with a selected budget and available balance, which are out of scope.
- **Currency:** ISO code, currency name, or symbol is explicit intent. Normalize an unambiguous name to ISO. When omitted or ambiguous, prefer the selected `activityTypes` row's `defaultCurrency.defaultValue`, then the top-level `defaultCurrency`. Use a compatible returned default to disambiguate an ambiguous term; never override a conflicting stated currency or ask merely because it differs from a default. Ask only when the stated term remains ambiguous after applying those compatible defaults.
- **Spend type:** Match the user's complete intent against the live `activityTypes` codes. Select a specific `Other/<type>` automatically when it is the single clear semantic fit; coffee, meals, catering, and groceries map to `Other/Food` only when that exact type is present. Ask only when multiple specific returned types are genuinely plausible. Use generic `Other` only when no specific type meaningfully fits and `Other` is returned. List order is never a spend-type default.
- **Category:** Resolve a stated category to an exact `categoryOptions` code or a unique semantic match against its code/label. Ask the user to choose from matching or available `categoryOptions` when stated intent has multiple matches or no match; never replace it with an unrelated default. When category is omitted, first match the selected spend-type suffix to `categoryOptions` (for example `Other/Food` to `Food`). Use the first row only when neither user intent nor the selected type resolves a category. Never use `allOptions` as a category fallback.
- **Start:** Explicit user date first; otherwise today in the user/host local calendar.
- **End:** Explicit user date first; otherwise derive it from an explicit duration and the resolved start; otherwise use a verified selected-type date policy; otherwise use today plus three calendar days. For an unambiguous `N` calendar-day duration, count start as day one (`end = start + (N - 1)` calendar days). Ask when the duration's units or inclusivity are ambiguous. Validate `start <= end` after applying any explicit or default source and ask for a valid end date when it fails.
- **Purpose:** Preserve clear intent from the user’s request. Ask only when no purpose can be identified.
- **Name:** Explicit user title first, then returned selected-type `activityTitle`, then `Miscellaneous`. A category label is not a title fallback.
- **Cost center:** Resolve a stated cost center to an exact or unique semantic match against returned `costCenters.code`, `name`, or `uiLabel`. Ask the user to choose from matching or available rows when stated intent has multiple matches or no match; never substitute an auto-selected or first-row default. Only when cost center was omitted, use `costCenterAutoSelected`, then the first returned row as the iOS picker default.
- **Activity type:** Exact selected live code such as `Other/Food`; the MCP still uses the existing `Others` backend API and maps the suffix to `fixedTo`.
- **Fixed target and estimate:** Owned by the MCP/backend; do not construct them.

## iOS default parity

When the user omits a value, mirror `CreateOtherActivityViewController`:

1. The authenticated user/company is implicit.
2. Select the best-fitting enabled allocatable type before field defaults. A clear office-coffee request selects `Other/Food` when available, matching the native type-selection screen.
3. When category is not explicit, prefer the category matching the selected type's suffix; only then use the first `categoryOptions` row. iOS does not use `allOptions` as a category fallback.
4. The first user cost center is selected when none was chosen.
5. The selected activity type's default currency is preferred when returned; otherwise use the unambiguous activity default returned by Custodia.
6. Start is today.
7. When the user supplied neither an end date nor a duration, end initially defaults to today plus three calendar days, regardless of an explicit start date.
8. In that defaulting case, a returned `endDate` policy overrides the three-day end only when the MCP data clearly corresponds to the selected activity type:
   - `endOfMonth`: if the number of days in the current month is greater than `daysToNextMonth`, use the end of the current month; otherwise add two calendar months to today. This mirrors the current iOS implementation.
   - `endOfQuarter`: add one calendar quarter, matching the iOS implementation.
9. The selected allocatable type’s `activityTitle` is used when available; otherwise the title is `Miscellaneous`. The budget-category label is not used as the title fallback.

Apply defaults to the working draft without asking separate questions. Every applied default must still appear in the mandatory confirmation. Explicit user values always win.

The current preparation composite loads parameters for model `Other`. Treat that date policy as selected-type parity only when the selected type’s `appCode` is also `Other`; otherwise use the three-day iOS fallback.

Do not default amount in this simple flow and do not fabricate a purpose.

## Confirmation and duplicate behavior

Complete preparation and duplicate detection before the write.

The confirmation must show:

- Title.
- Selected spend type.
- Amount and currency.
- Purpose.
- Category display label.
- Concrete dates.
- Cost-center display label or backend-default explanation.
- Duplicate warning when applicable.
- Which category, currency, dates, or cost center were defaulted.

One explicit confirmation may authorize both continuing with a detected duplicate and submitting, provided the warning is in that same summary.

When preparation plus iOS defaults resolve every required field, this confirmation should be the first and only question asked.

Any material change invalidates confirmation and requires duplicate rechecking. Generate `clientRequestId` after confirmation, not while preparing.

## Idempotency and recovery

`clientRequestId` is the stable identity for one draft:

- Generate it once after confirmation.
- Keep it private.
- Include it unchanged in the one confirmed submission payload.
- Never submit concurrently.
- Do not automatically retry `spend_permission_request` after any write-capable stage. The transport can apply its own idempotency key, which the skill does not control.
- Recover an uncertain result only through `spend_request_get_status` when a structured allocatable ID is available.
- The status tool owns the initial bounded wait. A `request_not_visible` response is a retryable read state, not permission to submit again.

If a material change happens before the first write, reconfirm and generate a fresh ID. If validation already created and preserved a draft, report it and stop; this simple skill does not update preserved drafts.

## Error contract

Handle known errors without issuing a replacement submission:

- `SPEND_REQUEST_VALIDATION_FAILED`: read `details.issues` and `details.draftId`; report the safe policy issue.
- `WORKFLOW_SIMULATION_BLOCKED`: read `details.decision`, `details.explanation`, `details.code`, and `details.draftId`.
- `COST_CENTER_REQUIRED`: no draft was created. Re-run `spend_request_prepare`, resolve the current cost-center ID from its structured response, reconfirm, and generate a fresh `clientRequestId`. Do not parse IDs from the error message or use `cost_centers_list_mine`.
- `APPROVAL_STATUS_UNKNOWN`: read `details.allocatableId` or `details.draftId`, pass it as `allocatableId` to `spend_request_get_status`, and follow `retryAfterMs`. This means approval may already have been accepted.
- `CREATED_NOT_SUBMITTED`: retain the existing draft identity, report the safe reason, and do not call the status tool or describe the draft as pending approval.
- `verificationState: request_not_visible`: the draft exists but submission is not established. Treat it as pending verification only when recovering `APPROVAL_STATUS_UNKNOWN`; for other provenance, say it may be unsubmitted.
- `SPEND_REQUEST_NOT_FOUND`: no matching self-owned Request or draft was found; do not automatically resubmit.

If an unknown-result error does not expose a structured allocatable/draft ID, do not parse or guess an ID. Direct the user to verify the request in Custodia and do not retry submission.

## Unsupported inputs

The merged submission schema does not support merchant restrictions, card binding, purchase orders, keywords, budget selection, transaction limits, ATM controls, recurring behavior, or on-behalf-of creation.

If any is material to the user’s request:

1. Explain that the simple assistant flow cannot enforce it.
2. Do not silently remove it.
3. Offer the Custodia UI or a dedicated supported workflow.
4. Submit without it only after the user explicitly changes the request and reconfirms.
