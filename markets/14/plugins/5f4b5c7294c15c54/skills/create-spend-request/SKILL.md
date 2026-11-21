---
name: create-spend-request
description: Creates, submits, and checks approval status for a simple Custodia spend permission through the authenticated Custodia MCP. Use when a user asks for spending authority for themselves or asks whether a request from this conversation was approved.
metadata:
  product: Custodia
  operation: create-spend-request
---

# Create or Check a Custodia Spend Request

Create a standard one-time activity backed by Custodia's `Other` model for the authenticated user. Select the best-fitting enabled `Other/<type>` variant from the user's live options instead of defaulting every request to generic `Other`. A successful submission creates an Allocatable draft and a workflow Request. It becomes an Allocation (spend permission) only after approval.

## Requirements

Creating a request requires an authenticated Custodia MCP connection exposing `spend_request_prepare`, `spend_request_check_duplicates`, `spend_permission_request`, and `spend_request_get_status`. A status-only follow-up requires `spend_request_get_status`. If the tools required for the requested path are unavailable, stop before collecting confirmation or attempting a write and use the bundled `reconnect-custodia` workflow. A local plugin selector such as `custodia-chatgpt-plugin@local-repo` is not a registered app ID; never pass it to `plugin_management.get_app_permissions` or claim that its response proves the local plugin is not installed.

Read [references/reference.md](references/reference.md) before calling tools. Use [references/examples.md](references/examples.md) for confirmation and result wording.

## Scope

Use this workflow only when all of the following are true:

- The authenticated user is requesting a spend permission for themselves, or checking the approval status of their own request.
- The request fits a standard, one-time `Other` or `Other/<type>` activity returned by Custodia.
- The request needs only amount, currency, dates, purpose, category, and an eligible cost center.

Do not use this skill for:

- Creating for another employee or company.
- Merchant restrictions, card binding, purchase orders, keywords, transaction limits, ATM controls, or other advanced options.
- Trips, client meetings, reimbursements, emergency budgets, mileage, bulk, recurring, split, merge, or changes to existing permissions.
- Approving or rejecting a pending request.

If the user asks for unsupported options, explain that this simple assistant flow cannot enforce them. Offer the Custodia UI or a dedicated skill. Never silently drop a requested restriction and submit a broader permission.

## Non-negotiable rules

1. Use only authenticated Custodia MCP tools. Never call Custodia HTTP endpoints directly or request credentials in chat.
2. Use the exact self-service tool sequence described below. Do not substitute generic CRUD or network tools.
3. Never pass `ownerId` or `companyId`; the MCP binds both to the authenticated session.
4. Never invent category codes, currencies, dates, defaults, cost centers, or policy values.
5. Pass `amount` as a positive JSON number and `currency` as a three-letter ISO code.
6. Select the most specific, uniquely matching code from `activityTypes` using the user's stated purpose and wording. Never default to generic `Other` merely because it is first.
7. Apply the iOS-aligned defaults below whenever the user did not provide a value. Do not ask the user to choose a value that Custodia can default.
8. Show one concrete final summary and obtain an affirmative answer before calling `spend_permission_request`.
9. Generate `clientRequestId` only after confirmation and keep it private. Preserve it in the submitted payload, but do not automatically retry a write-capable submission.
10. Pass `forceMultiple: true` only when duplicate detection returned both `duplicate: true` and `forceMultipleOnConfirmedSubmit: true`, and the user explicitly confirmed continuing.
11. Treat `spend_permission_request` as one terminal composite. It creates, estimates, validates, simulates, and submits; do not attempt those steps separately.
12. Never claim that `processing` means approved. Say “pending approval.”
13. Never create a replacement request after an unknown submission result.
14. Status checks are read-only. Reuse the retained allocatable or workflow Request ID; never restart the creation flow merely to learn approval status.

## Workflow

### 0. Handle a status-only follow-up

When the user asks whether a request was approved, completed, rejected, or is still pending:

1. First identify how the retained ID was produced. A successful submission or `APPROVAL_STATUS_UNKNOWN` is eligible for status recovery. An ID from `SPEND_REQUEST_VALIDATION_FAILED`, `WORKFLOW_SIMULATION_BLOCKED`, or `CREATED_NOT_SUBMITTED` identifies a preserved but unsubmitted draft.
2. For a known unsubmitted draft, do not call `spend_request_get_status` and do not describe it as pending approval. Report that the earlier workflow did not submit it and direct the user to Custodia.
3. Otherwise reuse the retained `allocatableId` or `requestId` and call `spend_request_get_status` directly with exactly one ID. Do not call prepare, duplicate detection, or submission.
4. If `verificationState` is `verified`, report `approvalState` and retain the raw `status` and `decision` as supporting detail.
5. If `verificationState` is `request_not_visible`, use the retained provenance. Only an ID from `APPROVAL_STATUS_UNKNOWN` may be described as “verification pending” and retried once after `retryAfterMs`. For an ID with unknown provenance, say that the draft exists but no workflow Request is visible; it may never have been submitted.
6. If no ID is available in the conversation, ask the user for the Custodia allocatable/draft ID or workflow Request ID. Never guess an ID.

### 1. Parse the request without writing

Extract only facts the user stated:

- Amount and currency.
- Business purpose.
- Start and end dates or duration.
- Spend-type concept and category concept.
- Optional cost-center name or code.
- Optional explicit activity title.

Do not map free text directly to an internal category code.

If the user names another employee, company, or an unsupported restriction, stop and explain that this skill supports only a simple self-service request.

### 2. Prepare live Custodia values

Call `spend_request_prepare` with no identity fields:

```json
{}
```

Use its response as the only source for:

- Self-creatable `Other` activity types.
- `categoryOptions` and `allOptions`.
- `defaultCurrency`.
- Type/user `parameters`.
- Eligible `costCenters`.
- `costCenterAutoSelected` and `costCenterSelectionRequired`.

Stop without writing if no eligible type or category is returned.

Resolve fields with this precedence: explicit user value, Custodia-returned default/policy, then the iOS fallback defined below.

- **Spend type:** Match the complete user request—especially its purpose, goods, service, or event—against the exact live `activityTypes[].code` values. Prefer a specific `Other/<type>` over generic `Other` when it is the single clear semantic fit. For example, coffee, meals, catering, or groceries should select `Other/Food` when that exact type is returned; software or computer equipment should select `Other/IT` when uniquely appropriate. Treat these as semantic examples, not hard-coded availability: never select a type absent from the response. If two specific types are genuinely plausible, ask the user to choose between their safe code suffixes. If no specific type meaningfully fits, use generic `Other` only when returned. Never use list order to choose a type.
- **Category:** Resolve this independently from the spend type and use only `categoryOptions`; `allOptions` is not a valid category fallback. When the user states a category, require an exact code or unique semantic match against returned codes/labels. If that stated category has no match or multiple matches, ask the user to choose from the matching or available `categoryOptions`; never replace stated intent with the first row. When category is omitted but the selected spend type has a suffix such as `Food`, first use an exact or unique semantic match for that suffix in `categoryOptions`. Only when neither user intent nor the selected type resolves a category, use the first `categoryOptions` row, matching the iOS picker default. Show its label in confirmation.
- **Currency:** Treat an ISO code, currency name, or symbol as explicit currency intent. Normalize an unambiguous name such as “euros” to its ISO code. For omitted or ambiguous currency, prefer the selected activity type's `defaultCurrency.defaultValue`, then the top-level `defaultCurrency`. Use a returned default to disambiguate a compatible term such as “dollars”/`$`; never let a default replace a conflicting stated name or symbol. Preserve an unambiguous stated currency without asking merely because it differs from a default. Ask only when the stated term remains ambiguous after applying compatible selected-type and top-level defaults.
- **Start:** Use the user’s date; otherwise use today in the user/host local calendar, matching iOS.
- **End:** Use the user’s end date. If the user instead states a duration, derive end from the resolved start before considering any policy or fallback; for an unambiguous `N` calendar-day duration, count start as day one, so `end = start + (N - 1)` calendar days. Otherwise apply returned `parameters.endDate` only when it is clearly for the selected activity type. If no verified policy applies, use today plus three calendar days, matching iOS. Ask when duration units or inclusivity are ambiguous. After resolving dates from any source, require `start <= end`; if not, ask for a valid end date before duplicate checking or confirmation.
- **Amount:** Require the user’s stated amount. The iOS amount default depends on a selected budget and available balance, which this simple flow does not support, so do not default it.
- **Purpose:** Preserve the user’s stated intent. Derive it from the request text when clear; ask only when no business purpose can be identified.
- **Name:** Preserve an explicit user title. Otherwise use a returned `activityTitle` for the selected activity type when available; never substitute a category label. If none is returned, use the iOS fallback `Miscellaneous`.
- **Cost center:** When the user states a cost center, require an exact or unique semantic match against returned `costCenters` fields such as `code`, `name`, or `uiLabel`. If the stated value has no match or multiple matches, ask the user to choose from the matching or available rows; never replace it with an auto-selected or first-row default. Only when the user omits cost center, use `costCenterAutoSelected`; if absent, use the first returned `costCenters` row, matching the iOS picker default even when multiple rows exist. Treat `costCenterSelectionRequired` as requiring visible review in the final confirmation, not a separate question when a default is allowed. If no rows are returned and none was stated, omit `costCenterIds` and state that Custodia will apply its configured default.

Do not ask a separate question merely to approve defaults. The mandatory final confirmation is where the user reviews or corrects every default. Ask one compact follow-up only for required values that remain unresolved after applying this precedence.

### 3. Check for a duplicate

After category, amount, currency, and dates are resolved, call:

```json
{
  "budgetCategoryType": "<returned category code>",
  "amount": 300,
  "currency": "USD",
  "start": "2026-09-15",
  "end": "2026-09-15"
}
```

Do not pass owner or company IDs.

- If `duplicate` is false, continue.
- If `duplicate` is true, clearly warn that Custodia found a similar active or pending permission. Do not claim details the tool did not return.

The final confirmation may also confirm continuing with the duplicate if the warning is explicit.

### 4. Present final confirmation

Present:

> Submit a Custodia spend request?
> - Title: {explicit/returned activity title or Miscellaneous}
> - Spend type: {selected activityTypes code without the Other/ prefix, or Other}
> - Amount: {currency} {amount}
> - Purpose: {purpose}
> - Category: {category display label}
> - Valid: {start date} to {end date}{mark defaults}
> - Cost center: {selected display label or Custodia configured default}{mark default}
> - Duplicate warning: {None or Custodia found a similar permission}
> - Approval: Determined during Custodia validation
>
> Submit this request?

Always wait for an affirmative answer, even when every missing value was defaulted. A change to amount, currency, dates, category, purpose, or cost center invalidates the confirmation. Re-run duplicate detection and show a new summary.

### 5. Submit the composite once

After confirmation, generate a fresh stable `clientRequestId` such as a UUID. Do not show it to the user.

Call `spend_permission_request` with:

```json
{
  "clientRequestId": "<stable private UUID>",
  "activityType": "<exact selected activityTypes code, e.g. Other/Food>",
  "name": "<explicit/returned activity title or Miscellaneous>",
  "description": "<user's business purpose>",
  "purpose": "<user's business purpose>",
  "amount": 300,
  "currency": "USD",
  "start": "2026-09-15",
  "end": "2026-09-15",
  "budgetCategoryType": "<returned category code>",
  "costCenterIds": ["<selected returned id>"]
}
```

Omit `costCenterIds` when preparation returned no eligible cost center. Add `forceMultiple: true` only when the duplicate tool returned `duplicate: true` and `forceMultipleOnConfirmedSubmit: true`, and that duplicate was confirmed. Otherwise omit it.

Do not call separate draft, estimate, validation, simulation, update, or approval tools. The composite performs those operations in the correct order and returns the authoritative workflow Request.

### 6. Handle the result

On success, use `requestId`, `approvalState`, `status`, and `decision` from the response:

> Spend request submitted.
> - Request: {requestId}
> - Amount: {currency} {amount}
> - Status: {returned status}
> - Approval: {normalized approvalState}

Interpret `approvalState` as authoritative agent-facing wording: `pending`, `approved`, `rejected`, `canceled`, `failed`, or `unknown`. Preserve raw `status` and `decision` when useful. If status is `processing`, say “pending approval,” not “approved.”

If the tool returns an existing Request for the same `clientRequestId`, treat it as the authoritative idempotent result.

### 7. Handle validation and uncertain results

- **`SPEND_REQUEST_VALIDATION_FAILED`:** Report safe issue codes from `details.issues` and the preserved draft ID from `details.draftId`. Do not submit.
- **`WORKFLOW_SIMULATION_BLOCKED`:** Report `details.decision`, safe explanation/code, and `details.draftId`. Do not submit.
- **`COST_CENTER_REQUIRED`:** This failure occurs before draft creation. Re-run `spend_request_prepare`, present its current `costCenters` by `uiLabel`, obtain a selection, reconfirm, generate a fresh `clientRequestId`, and submit. Never parse an ID from the error message or call an unrelated cost-center tool.
- **`APPROVAL_STATUS_UNKNOWN`:** Read `details.allocatableId`, falling back to `details.draftId`, and pass that value as `allocatableId` to `spend_request_get_status`. The status tool performs a bounded server-side wait. Never call `spend_permission_request` again automatically.
- **`CREATED_NOT_SUBMITTED`:** A draft exists but was not submitted. Report its ID and safe reason; do not treat it as pending approval or automatically resubmit it.
- **Request found:** Return that Request as success and do not submit again.
- **`verificationState: request_not_visible`:** The draft exists but no workflow Request is visible. After `APPROVAL_STATUS_UNKNOWN`, follow `retryAfterMs` and make at most one additional read-only status call; if still absent, report “verification pending.” For any other or unknown provenance, do not imply that submission occurred—state that the draft may be unsubmitted.
- **`SPEND_REQUEST_NOT_FOUND`:** The status lookup completed and found no matching self-owned Request or draft. Report that result, but do not retry submission automatically or create a replacement.
- **No structured ID after an unknown submission result:** No status lookup is possible, so the submission result remains uncertain. Direct the user to verify in Custodia. Never claim that nothing was created, retry submission automatically, or create a replacement.

If validation or workflow simulation preserves a draft, report it and stop. This simple skill does not mutate or resubmit preserved drafts; direct the user to the Custodia UI.

## Completion checklist

- [ ] Request is for the authenticated user
- [ ] Request is a simple one-time `Other`-model activity
- [ ] Live preparation values were used
- [ ] The most specific unique `activityTypes` match was selected and passed unchanged
- [ ] Category, amount, currency, dates, purpose, and cost center were resolved
- [ ] Duplicate check ran and any warning was confirmed
- [ ] User confirmed the concrete final summary
- [ ] One private `clientRequestId` was generated after confirmation
- [ ] `spend_permission_request` was called once, except a pre-draft `COST_CENTER_REQUIRED` correction
- [ ] Any post-submit recovery reused the structured ID and only called `spend_request_get_status`
- [ ] Final wording distinguishes submitted, pending, and approved
