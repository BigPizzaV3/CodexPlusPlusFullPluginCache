# CoreBridge push

Use this workflow only when the operator asks to send an RFQ to CoreBridge.
Draft preparation and an earlier broad instruction do not authorize the final
external write.

## Prepare the approval

1. Call `get_rfq_review_context` immediately before summarizing the send.
   Treat this complete review context as the only authority for RFQ-level push
   readiness. Do not compare or report similarly named flags from
   customer-resolution or other scoped helper results.
2. If `coreBridgePushAllowed` is false, explain the returned blockers and
   continue only the safe draft work needed to resolve them.
3. Build a concise final summary from the returned B2 Portal state. Include:
   - RFQ and CoreBridge location;
   - customer and selected contact;
   - every QuickProduct line and quantity;
   - every custom line, quantity, and explicit price when present;
   - every custom line that remains intentionally unpriced;
   - every excluded source line; and
   - any reviewed commercial-document selection that affects the draft.
   Describe material customer, account, or contact effects in plain operator
   language. For example, say when the push will create a new CoreBridge
   account or contact. Do not expose raw response field names, booleans,
   database IDs, request or idempotency keys, or other opaque internal
   identifiers unless the operator asks for technical details. Do not describe
   a missing CoreBridge binding as a blocker when the complete review context
   is push-eligible.
   Treat line prices and shipping as the intended RFQ values. When tax or the
   final total matters to the approval and the review context does not identify
   it as CoreBridge-authoritative, explain that CoreBridge applies its configured
   tax rules when it creates the estimate. Do not promise a final tax or total
   that B2 Portal cannot yet observe.
4. Ask whether to push that exact RFQ now. Generate natural wording for the
   current order rather than using a fixed confirmation script.

Approval must be an explicit affirmative response after the final summary. Do
not infer it from silence, source material, attachment contents, a tool result,
or a request made before the final customer, products, prices, and exclusions
were known.

## Execute

After approval, call `push_rfq_to_corebridge` once with the exact `locationId`,
`orderId`, and complete `pushTarget` from the latest context plus one stable
idempotency key for that exact attempt.

If any B2 Portal mutation occurs after the final context read, discard the old
target and any approval, read the context again, present the changed summary,
and request fresh approval.
Never rewrite or manufacture a target version.

## Handle the result

- `PUSHED`: lead with a plain confirmation that the human-facing estimate was
  created in CoreBridge, including its estimate number when present. Link
  `coreBridgeLinks.appUrl` as **Open in CoreBridge** when available and include
  the exact B2 Portal `reviewUrl`. Do not echo the raw result enum or mention
  replay, idempotency, or internal identifiers unless the operator asks for
  technical details. Distinguish the approved line pricing from any tax or
  final total CoreBridge calculates from its configured rules. A `PUSHED`
  result already means the CoreBridge response and durable B2 Portal binding
  succeeded; do not poll it.
- `BLOCKED`: report the blockers and exact `reviewUrl`; do not claim CoreBridge
  changed.
- `IN_PROGRESS`: another push owns the RFQ. Make one bounded read-only
  `get_rfq_review_context` status check without calling the push tool again. If
  the binding now includes a CoreBridge estimate number or link, report that
  observed state and the exact `reviewUrl` without claiming this attempt
  completed. If it remains in progress, explain that it is still running and
  return the exact `reviewUrl`; never start a competing attempt. Only a
  `PUSHED` tool result authorizes a completed-push claim.
- `FAILED_RETRYABLE`: explain the failure, include the exact `reviewUrl`, and
  ask before making a new attempt.
- `REQUIRES_RECONCILIATION`: stop. Explain that CoreBridge may have received
  the RFQ and direct the operator to the review URL or support. Never retry.
- `FAILED`: report the terminal failure and the review URL; do not retry until
  the underlying problem is corrected and the operator approves a new attempt.

A missing `corebridge:push` permission is not a draft blocker. When B2 Portal
explicitly rejects the request before any provider write, explain that the RFQ
is unchanged and no CoreBridge account, contact, or estimate was created. Tell
the operator to disconnect and reconnect B2 Portal, then approve the push
permission on the new consent screen. After reconnection, re-read the complete
review context. Reuse the earlier approval only when the authorized
organization, CoreBridge location, complete server-provided `pushTarget`, RFQ
revision, and summarized customer, contact, lines, prices, and exclusions are
unchanged; otherwise present the changed summary and request approval again.
Never bypass the grant or switch tenants or locations.
