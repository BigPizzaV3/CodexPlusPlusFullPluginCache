---
name: review-broadcast-campaigns
description: Plan Tap campaigns, manage public and private RFPs, compare supplier responses, and prepare unsent direct-buy drafts and track existing Orders. Use for buyer media sourcing, supplier Deals, DOOH planning, correspondence, and creative fulfillment in Tap.
---

# Buyer media planning in Tap

Use connected Tap tools for the authenticated buyer workspace. Match the named
campaign before editing; clarify only if multiple matches remain. The skill
identifier and tool names retain Plan, Broadcast and Avail for compatibility.
Call these campaigns, private TV/radio RFPs, and supplier responses in answers.

## Select the buying method

- Public RFPs: open sourcing briefs for TV, radio, static out-of-home, CTV,
  cinema, podcasts, digital display, digital video, digital audio, print,
  social, search, or Any media. A draft is private until explicitly published.
- Private RFPs: TV/radio requirements sent to specifically selected supplier
  recipients. Staging recipients does not send the request.
- Direct-buy planning: compare supplier Deals and DOOH inventory and prepare
  unsent drafts. This plugin cannot place Orders or record bookings. Existing
  Order status, correspondence, withdrawals and creative fulfillment are supported.

Campaign mediaTypes supports TV, radio and out-of-home at campaign level.
Other categories belong to the public RFP brief; do not invent campaign enum
values. Use the canonical tool schemas and exact directory/catalog identities.

## Campaign and RFP preparation

Use listMyPlans to identify campaigns, then getPlanContext for each campaign
being assessed. The list omits completion fields. Report missing budget,
objective, audience, flight, markets and requirements from detailed context;
distinguish optional fields from send blockers. Reviewing never authorizes edits.

Before creating an RFP, inspect listOpenRfps or listBroadcastRfps and matching
getOpenRfp/getBroadcastRfp details. Reuse an appropriate draft and say whether it
already existed. Preserve unchanged requirements and issued requests. Public
TV/radio RFPs use getOpenRfpDraftContext for exact market, audience, weeks,
dayparts, lengths and goals. Private station choices use
listBroadcastRecipientCandidates; never invent recipients or availability.

createOpenRfpDraft and updateOpenRfpDraft prepare public briefs;
publishOpenRfp exposes the reviewed brief to eligible suppliers. closeOpenRfp
stops responses. Private RFP tools separately stage, send, revise, add recipients,
amend deadlines, close individual exchanges or withdraw the complete request.
convertRfpBuyingMethod replaces only a never-sent TV/radio draft. Re-read its
new ID and review completed fields before sending or publishing.

## Responses and supplier correspondence

For public RFPs, listOpenRfpResponses and getOpenRfpResponse expose submitted
revisions and quote options. Compare currency, pricing basis, flight, quantity,
rate, totals and validity; do not treat expired, withdrawn or superseded terms
as current. listOpenRfpResponseMessages reads correspondence;
postOpenRfpResponseMessage sends an approved message with a stable clientId UUID.
reviewOpenRfpResponse explicitly acknowledges only the reviewed revision.
Public cross-media quote-to-Order conversion is not supported by these tools.

For private RFPs, inspect getBroadcastAvailMenu/getBroadcastAvailResponse,
getBroadcastBuyingContext and assembleBroadcastBuy. Compare actual offered
weekly rates and impressions, costs, audience goals and gaps. Read current and
historical exchange conversations as needed. Sending a message and marking a
response reviewed or conversation read are separate actions from reading.

## Direct-buy drafts and existing Orders

Supplier Deals: listSupplierDeals and getSupplierDeal read eligible public and
private offers. Respond or reply only as requested: interested/reply enables the
communication relationship; passing makes existing draft Orders stale.
createSupplierDealOrder prepares exact avails/quantities from the current Deal
or quote. It leaves the Order unsent.

Broadcast responses: createBroadcastOrderDraft, addBroadcastOrderAvails and
saveBroadcastOrderQuantities prepare an unsent Order. Read getBroadcastOrder
and its current version, fees, totals and availableActions before editing.
quoteBroadcastBuyCompositionTapFees reads proposed fees for cost comparison.
Selecting a buy saves a recommendation and does not place Orders.

DOOH: use catalog overview and geography tools, then
searchDoohInventoryOptions to compare grounded catalog groups. Preserve returned
planningInput identities in configureDoohPlan. Estimates are directional and
do not reserve inventory. Read getDoohPlanningContext and
getDoohCommerceWorkspace before editing. saveDoohOrderDraft saves proposed price
and creative requirements without placing an Order. Re-read allocation and
draft versions after changes.

The plugin cannot place media Orders, materialize a buy into sent Orders or
record external bookings. Do not use messages, interested responses or another
action as a substitute purchase commitment, even when the user approves.
Available actions in a returned record describe Tap's full product; only the
currently registered plugin tools can be called. For existing Orders, report
the actual state and use withdrawal only when the current state allows it.
Do not claim booking, payment or delivery from an unsent draft or pending Order.

Creative assignments and DOOH HTTPS asset submissions are explicit supplier-
visible actions. Reading status does not approve creative. Buyer tools cannot
impersonate a supplier, confirm their Order, approve creative as them, submit
supplier post-buy reporting, make payments or execute ad-platform campaigns.

## Approval, failures and results

Before publication, outbound messages, acknowledgements, commercial actions or
destructive changes, show the exact target and consequence. Respect the host's
action permissions and confirmation prompts, and complete any additional server
approval. Model-supplied humanApproved flags are not evidence of consent.
Approval of preparation or editing does not authorize sending or publication.
If declined, cancelled or unavailable, stop that action and report no change.

Use current versions and fee quotes. On stale-version, permissions or lifecycle
errors, re-read the authorized workspace and explain the issue; never remove a
version check or use another action to bypass it. After an uncertain response,
read current state before issuing a new commercial action.

Bulk deletion of all client data, campaigns, responses or an organization is not
supported. Supported draft, brand, memory and assignment removals need specific
identifiers and approval. Do not offer unsupported actions as workarounds.

Present grounded text or tables and returned Tap links. State what changed,
what remains incomplete and whether anything was sent or published. Do not
expose credentials, diagnostic fields, unrelated tenant data or private supplier
drafts. Sign in through Tap OAuth; never request passwords, tokens or payment
credentials in the conversation.
