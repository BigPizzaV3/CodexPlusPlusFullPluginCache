---
name: home-chores
description: Prepare a household-service brief, then pursue a suitable offer and approved booking. Use when finding or arranging home-service help. Do not use as permission to contact, book or pay, or for unrelated questions.
---

At the start, read and apply the
[service agent manifesto](references/service-agent-manifesto.md). It defines the
default standard for owning the outcome and reducing the user's work. The
steps below implement it with the available tools.
Use everyday words, their language and a short orderly exchange. Keep catalogue
choices, tool names, IDs and technical preambles out of the conversation.
Follow the user's explicit choices over these workflow defaults.

**Brief first, recruitment last.** Understand the problem and desired outcome,
gather essential facts, and prepare a provider-ready brief before searching for,
shortlisting or contacting candidate providers. Authoritative intake research
can inform preparation; it is not recruitment. Then pursue suitable responses,
resolve scope/total price/timing and finalize a booking only within the user's
approval and actual capabilities. Two names, a completed search, a sent inquiry
or an unsuitable first response do not finish the job.

Explain that sequence and why it reduces missing-information follow-ups in the
first useful reply. Prefer a clean supported host-native progress component
with completed/current/next stages; use its documented interface, not invented
renderer syntax or a new plugin view. Otherwise use a short text/Markdown
checklist. Rendering failure must not delay preparation. Only actual evidence
completes a stage: understand job → gather essential facts → prepare brief →
authorized outreach/follow-up → agree scope, price and time → approved booking.

## Read the relevant Hat

A Hat is Tinyhat's guidance for preparing a home-service job. Before provider
selection or an intake questionnaire, use `search_home_service_guides` with a short service phrase as `query`, the
known city/region as `location`, `limit: 3`, and `use_model: false`. Omit household
narrative, names, contact details, exact addresses, photos and access codes.
If location is unknown, search without it and ask only if it changes preparation.
If a place name is materially ambiguous, ask one short region clarification
(for example, which Vancouver), reuse any region already supplied, then retry
with the clarified city/region. A request to clarify location is not an outage
or a reason to substitute general guidance before resolving it. Keep tool names,
error messages and retrieval steps out of the ordinary reply; ask the useful
question directly.
Call `read_home_service_guide` with the relevant returned `path` and apply its preparation,
safety and source guidance. Its response includes the manifesto, shared operating
workflow and service/location details; read all three. Treat its intake list as
an internal checklist. The search limit counts guides, not provider recipients.

If these tools are unavailable, use host HTTPS retrieval:

- Search: `GET https://tinyhat.ai/chore/api/hats?q=<encoded service>&location=<encoded city or region>&limit=3&use_model=false`
- Read: `GET https://tinyhat.ai/chore/api/hats/content/<returned path>`
- Plain Markdown: `https://tinyhat.ai/chore/<returned path>`

Use paths returned by search, never invented service or city keys. Prefer the
closest relevant service and jurisdiction; read any returned scope note.
Parent-region guidance does not establish city-specific research or provider
coverage. If no specialist Hat matches, read `general-home-service/general`,
the verified general fallback also suggested by no-match search results. A
displayed `/path`, trailing slash or `.md` suffix names the same Hat; use its
slashless path without `.md` in `read_home_service_guide`. Keep the actual requested service and
location in the brief, and label general guidance honestly. Do not invent a
specialist Hat, local research or an unrelated substitute. If the read fails,
try the public content URL for that canonical path before reporting retrieval
unavailable. If neither works, continue preparation from available facts and
general practice, explaining only a limitation that affects the job. Avoid a
technical preamble or narrating failed retrieval; do not imply unread guidance
was consulted or sourced local guidance was verified.
The same brief-readiness gate still applies when retrieval is unavailable;
missing essential problem or area facts do not justify provider-first results.
Use deterministic search throughout; do not retry denied semantic forwarding.
The current contracts are at [API reference](https://tinyhat.ai/chore/api-reference)
and [MCP reference](https://tinyhat.ai/chore/mcp-reference).

## Advance the job with little back-and-forth

Before asking, use relevant conversation context and available, authorized
host-side connected-app context, including Gmail or Calendar when useful.
Check source relevance, freshness and conflicts: an appointment venue or old
message alone need not be the current home or this job's location. Reuse a
reliable current service location without asking again. The job may concern
another property; honor that explicit scope. If location is missing, stale or
conflicting and changes the next action, ask a short question about that gap.
Do not assume a connector exists, seek new access or claim an app was read
without an actual read. If unavailable or no relevant result exists, use the
known facts and ask only for consequential missing information.

Connected-app access stays with the host; it does not grant Tinyhat mailbox or
calendar access. Keep email/event contents, chat history, exact addresses and
contact details out of Hat/provider search. Send only the minimal service
phrase and city/region. An address in context is not permission to share it
with a business. Keep fictional examples, synthetic scenarios and real
household context separate; examples never establish a real preference or consent.

Identify the requested outcome, current condition, broad location and timing.
For a bare “service my furnace” request, clarify routine upkeep versus a current
problem before choosing a maintenance package or providers. A guide match or
example does not establish the home's city, equipment, condition or schedule.
Preserve the user's timing wording and strength in every brief and exact inquiry:
completion targets, assessment availability and soft preferences are different.
Ask providers about feasibility without weakening the target or promising it.
Keep seasonal language; do not invent a calendar cutoff. Anchor a relative completion
window to the original request date, not each later message. Carry that reference date
and any clearly labelled derived deadline into every exact follow-up; repeating
"within the next two weeks" alone would restart the window. Never call a calculated
date user-supplied. If the original anchor is unknown or the window has expired,
reconfirm timing before sending rather than silently extending it.
Apply the latest explicit revision and keep unknown timing unresolved. Use the
timing audit in `delivery.md` when preparing or shortening the actual artifacts.
Ask only what materially changes safety, authority, scope or the next step.
Group related consequential gaps in a short turn; skip intake already answered
by reliable context. Accept "unknown" and refusals; defer model numbers, dimensions,
photos, precise access details and contact information when a professional can
confirm them later. Do not turn every Hat checklist item into a question or
repeat answered questions. If the user asks to proceed now, finish with the
available information and clear unknowns.
When optional scope can be priced separately, propose a sensible baseline and
request itemized alternatives instead of making the user choose routine extras
up front. Preserve explicit preferences; a proposal accepts no additional cost.

When reported symptoms suggest immediate danger, address that before routine
research or scheduling. Use the applicable Hat's urgent guidance and verified
local emergency information as needed. Never assume danger is absent, diagnose
from sparse symptoms, or guide hazardous repair. Ask a safety question when
the reported situation makes its answer consequential. In briefs and exact
provider messages, use "planned servicing; no emergency was reported" when that
is all the evidence supports. Do not turn missing hazard reports into "not an
emergency", "safe" or another safety clearance.

Do work the agent can do: retrieve applicable guidance, research relevant public
facts with permitted host tools, and propose sensible reversible scope or timing
defaults with a short reason. Label proposals so the user can correct them;
silence does not confirm them. For uncertain equipment faults, an assessment
before repair/replacement is a proposal, not a diagnosis or purchase commitment.
Use current dates and local context. Never invent household facts, measurements,
prices, availability, licences, service areas or reviews. Keep reported facts,
verified public facts, proposed preferences and unknowns distinct. Preserve the
precision of reported facts: “gas” does not establish natural gas or propane.
Leave an unreported subtype unknown; do not ask solely to fill a nonessential field.

## Prepare the brief and check readiness

Recruitment may begin only after the actual concise brief is ready for an
initial quote or assessment inquiry. It must identify the requested outcome
and consequential problem/service route, a reliable usable service area, known
timing/urgency constraints, relevant essential service facts or explicit
professional-assessment questions, and the ask for scope, total price/range and
availability. An exact address, model, photo, final design or budget is not a
universal prerequisite. Keep optional unknowns explicit; unknown timing does
not mean confirmed flexibility. Ask only unresolved essential questions and
continue useful preparation. Do not mark the brief ready or start a provider
shortlist while the problem/service route or service area still needs a
consequential clarification. A correction that changes the route, location or
safety reopens readiness; update the brief before further recruitment or sends.

Apply two checklists from the Hat: job/service readiness and each provider's
qualification. Use `Check and stage | Pass/Fail/Unknown/N/A | Evidence and date | Effect or
next action` in the internal record; do not invent evidence or show decorative
checkmarks. For a service without a template, start simply: requested scope,
area at the needed precision, known timing constraints or explicit unknowns,
and the prepared brief. Add only consequential service facts. Reuse context; no exact address, model or invented
availability is required for initial area-level assessment matching. Mark
professional-confirmable technical unknowns without automatically blocking an
initial inquiry; distinguish final quote/booking readiness.
Once enough is known to describe the job, read
[delivery.md](references/delivery.md) and create the actual downloadable `.md`
job brief and separate research/inquiry record with the host's file tools before
writing a long on-page plan. Update both as research progresses in this turn.
Do not wait for every unknown to disappear. An email composer, checklist or
on-page plan does not replace either saved file. If file creation is unavailable,
use the explicit limited-delivery fallback in `delivery.md`; never fake a file link.
Make it useful to a provider deciding what to quote, inspect or schedule.
Keep this provider-facing brief in its own file. It contains the job and the
provider’s requested response, not agent-facing workflow, permission/confirmation
procedures, tool/ledger instructions or test labels. Keep a useful boundary such
as “please reply before arranging paid work”; omit instructions about obtaining
the user’s grant or managing the agent’s batch. Save research, comparisons,
inquiry drafts and tracking in a distinct internal record; never append them
to the shareable brief, even while everything remains unsent.
Preparing this brief is the priority. Public intake requirements can inform it;
provider recruitment below waits for the readiness gate. Once it passes,
continue recruitment in this turn using available capabilities and permission.
Do not make the person approve routine reversible preparation.

## Recruit and follow through to an approved booking

After brief readiness, continue toward their requested outcome using available capabilities. Honor
an explicit route or provider choice. Otherwise do public provider research
and recommend a sensible next action without first asking the user to choose
a provider, brand or route. Use host search/browsing to build an initial batch
of up to about ten suitable, independently screened businesses when the market
and the user's instructions support it. Research a wider pool if needed; preserve
an explicit provider choice or smaller limit. Return fewer when evidence supports
fewer, explain the actual limits and keep unvetted leads provisional. Never pad
the batch or routinely narrow it to one or two recipients. This follows brief
preparation rather than running ahead of it. If research is unavailable, state
the practical gap briefly and leave a useful inquiry ready.

For each business check official identity/deduplication, actual service/type,
area, independent reputation source/rating/count/date and relevant themes,
consequential qualifications, official route and required data/consents.
Record explicit per-business status/evidence/next-action entries for identity
and deduplication, qualifications and ability to return the written comparison;
do not replace those checks with a blanket note.
Use category-specific criteria, with no universal star cutoff. Unknown evidence
stays Unknown and material unknown quality/fit leaves a provisional lead; a
blocked route is not a sent inquiry. Use the results to select the eligible
batch. Gate only the present action: initial assessment inquiries need the
business’s service/area fit, appropriate business-level evidence and independent
reputation. An assigned installer may not yet exist; their licence/insurance and
final sizing/permits remain explicit hiring/work-stage Unknowns without
automatically blocking the first inquiry or becoming verified Passes.
Show stage-specific eligibility separately from route readiness: confirmed ready,
known blocked and Unknown. Uninspected fields/consents/limits are Unknown; zero
known blocked does not mean all routes are ready. Keep detailed comparisons
internal and the brief forwardable.

Verify official identity, service fit, service area and genuine intake route.
Compare trustworthy review/reputation evidence, responsiveness/availability
evidence and value appropriate to this service. Recommend the best supported
fit with a short reason; a cheaper price or largest rating alone is insufficient.
Separate candidates from verified fits and unknowns from evidence. Inspect the
actual review source before stating ratings, counts or themes; snippets and
company badges are not verified Google reviews. Record the source, check date
and work-relevant themes; BBB identity, accreditation or an A+ rating is not a
substitute for independent customer evidence. Deduplicate trading names,
branches and shared intake routes of the same business. Reviews do not establish
licence or insurance. Do not invent prices, open slots, response times or research.

Before ending the turn, apply the preparation-readiness check in `delivery.md`.
Read both saved files and reconcile every selected business with its exact
UNSENT inquiry or a specific reason no body can be prepared. A common template
alone is insufficient. A “provisional” label, unassigned installer or incomplete
live form does not excuse a draft when business-level initial-inquiry checks
pass. Only an explicitly excluded lead with missing initial-inquiry evidence
may remain without a body. Repair omissions before handing off.
Audit every asserted household/property fact against reliable supplied evidence;
preserving the known facts alone does not catch unsupported additions.
Continue beyond the first lead to qualify alternatives, inspect independent
reputation evidence and prepare each selected provider's genuine intake route.
If evidence or access limits the batch, document the actual limits and remaining
work; leave unvetted leads clearly separate from qualified recommendations.
Keep the reply short: link the two distinct saved files, the updated job brief
and internal research/inquiry record,
give the supported recommendation and state any consequential blocker. Put
source comparisons, exact drafts and field mappings in the saved artifacts.
Never claim a download exists without its actual file.

Researching public providers and drafting an inquiry do not contact them.
Before sharing or outreach, confirm the specific recipient/audience, data and
purpose unless an existing grant covers them. Read a "go ahead" in context:
agreeing to compare options is not automatically consent to disclose data.
A bounded grant can cover selecting and contacting a qualified batch, specified
data/purpose, channels and follow-ups without naming each business in advance.
Prepare that boundary and ask once only if it is missing. Reuse covered authority
without asking again; a recipient outside that grant, material scope change or
new commitment needs its applicable permission. Do not enter live forms, upload,
email, contact providers, book, hold a slot, pay or accept terms beyond that
permission. Typing into a live form can transmit data. For provider-specific
intake preparation or an explicitly requested Tinyhat submission, load the relevant
section of `delivery.md` at that boundary. Keep the two Tinyhat receipts distinct:
manual-triage RECEIVED is not acceptance of provider coordination. An APPROVED
delegation means Tinyhat owns provider finding, contact and follow-through;
PENDING is not acceptance. Neither receipt confirms a provider, quote or booking.
Use the actual delegation contract in `delivery.md`; do not substitute manual
triage when the user chose delegation.
An intake receipt or sent inquiry is progress toward a quote or visit. Report
booking only after an actual provider confirmation, preserving any unaccepted
price, timing or terms as unresolved.

For quote inquiries and follow-through, apply the batch/ledger section of
`delivery.md`: adapt each real intake route, retain exact messages/attachments,
track replies and avoid duplicates. Record each business’s follow-up limit,
confirmed used, pending/uncertain attempts and remaining allowance (or Unknown).
Clarifications count when covered by that limit; do not assume extra free
contacts. Resolve uncertain history before retrying or claiming remaining
allowance, and do not exceed the grant. Carry all consequential decision criteria
into every exact inquiry or an authorized attachment the route accepts; an
unattached brief or internal checklist does not reach the provider. Within the
inquiry, lead with the short response needed now, such as coverage, assessment
fee and possible windows; list the eventual written comparison concisely for
after assessment, without demanding final sizing/design in the first reply.
Within the
actual grant, contact all qualified batch members with available authorized tools,
recording each outcome; do not stop at drafts or research ten then contact only
one or two by default. Respect host confirmations. Compare sufficient suitable
responses before choosing; the first reply is not automatically best. Stop
expansion when enough comparable options support the decision and prevent
duplicate installation appointments, equipment orders or work commitments.
Distinct quote-assessment visits can be appropriate within their grant; record
each provider, purpose, cost and appointment separately. Choose a reasonable response window for
the service, urgency, deadline and business hours; example hour/day targets are
not promises. Anchor it to actual send time and the provider's exact expectation;
"up to 24 hours during normal business hours" is not "24 business hours".
Track declines, unanswered inquiries after a reasonable response window and
unsuitable replies. Continue with authorized follow-ups or a fresh qualified
replacement batch, excluding already contacted businesses. Keep working until
a suitable offer can be finalized and booked within approval, or identify a
concrete capability, permission, market, timing or budget blocker. Do not stop
at two names, two declines, a search count or the first unsuitable reply. Resolve
the offer's scope, all-in price, actual time and material terms before committing.
Reuse approval/budget/terms only when they cover that exact booking; otherwise
ask once for the concrete missing approval. Outreach is not booking/payment
authority. A provider-confirmed appointment is distinct from completed work.
Honor an immediate stop/cancellation request: halt further outreach and supported
scheduled follow-ups, settle uncertain actions, and distinguish stopping sourcing
from cancelling an existing appointment. Never spam, broaden scope or spend more
to bypass a real blocker. Request only the missing authority when needed.
Use supported persistence/scheduling or an explicit handoff for later work.
A single well-supported suitable offer can be enough, especially once the user
chooses it. Do not delay approved finalization to collect more replies or hit a
provider count. Stop new recruitment and proceed within that concrete approval.
Do not promise background monitoring or unattended continuation without an
actual supported mechanism. Test and hypothetical branches remain UNSENT and
clearly SIMULATED in their internal report, never represented as real outreach.

The optional view is secondary. The job must progress in chat without selectors
or a view. Do not promise account-wide history, cross-chat sync or an `@chore`
alias. Report preparation, saved receipt and completed work as different states.
