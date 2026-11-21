# Counterparty Modes: a design exploration

This is a design feasibility paper, not a committed roadmap. It asks what would have to change,
technically, if the plugin served a different party to the same contract than it does today —
and sets out what would need deciding before any of it went into the backlog. The commercial
decision that follows from this — which market to sell into, at what price, through what channel,
and how to position around conflict of interest — stays with Gather. Nothing here recommends an
answer to those questions; Section 5 lists them as a checklist.

## Why this question, now

Every skill in this plugin is written from one seat: the main contractor's QS. It verifies
subcontractor applications (`$subcontractor-check`), builds the contractor's own
application to the client (`$valuation`), and frames claims and events as things the main
contractor submits upward. That seat is not accidental — it is the buyer today. But the plugin's
real asset is the methodology (evidence discipline, contract-aware framing, the shared patterns
library) sitting on top of Gather's site records, and none of that methodology is intrinsically
tied to being the main contractor. This paper works through what changes, and what doesn't, if the
same machinery is pointed at a subcontractor's own records, or at a client/PM reviewing what a
contractor submits to them.

## 1. The three personas

### (a) Main-contractor QS — today's product, baseline

- **Who:** the main contractor's commercial team, running Gather against their own project
  records.
- **Submits/receives:** submits applications for payment and claims upward to the
  client/PM/Engineer; receives and checks subcontractor applications from below.
- **Faces both ways today:** `$valuation` and `$ce-builder` face up (to the
  client); `$subcontractor-check` and `$timesheet-check` face down (to
  subcontractors and labour-only suppliers). This is the persona every skill, agent, and
  worked example in the repo currently assumes.

### (b) Subcontractor-up — the subbie's own QS

- **Who:** the subcontractor's own commercial team, running Gather against their own site
  records (their own diaries, their own labour, their own plant) for their package.
- **Submits/receives:** submits applications, dayworks, delay notices and claims **to** the
  main contractor, from the subcontractor's own Gather records — the mirror image of (a)'s
  downward-facing skills.
- **Maps across unchanged:** `$valuation` (the subbie's own application, priced at
  their own commercial profile), `$dayworks`, `$ce-builder` (a claim against
  the main contractor rather than the client), `$delay-analysis`, `$events`,
  `$nec-deadlines`, all site-records skills (`diary`, `labour`, `progress`, `access`,
  `weather-impact`). These skills already only look at "our own records" — they don't care
  whose records those are.
- **Inverts:** `$subcontractor-check` and the paid-hours side of `$timesheet-check`
  invert from "verify what's coming in" to "defend what we're sending out" — see Section 2(b).
  Contract terminology also inverts: the subcontractor's contract is the subcontract (NEC's ECS,
  or a JCT/FIDIC domestic subcontract), not the main contract, and its own notice and reply
  periods apply, not the main contract's.

### (c) PM/client-side — reviewing incoming contractor submissions

- **Who:** the employer's or PM's/Engineer's own team, holding the employer's own records
  (possession dates given, instructions issued, information released, its own site
  supervision diary where one exists) and reviewing what the contractor submits against them.
- **Submits/receives:** receives applications and claims from the contractor; issues
  certificates, payment notices, and replies to notifications against its own record set.
- **Maps across unchanged:** the site-records and analytical skills again — `narrative-search`,
  `progress`, `delay-analysis`, `access` — run the same way over the employer's own records if
  the employer holds any (this is the persona's biggest practical gap: the employer typically
  holds far thinner site records than the parties actually doing the work — see Section 4).
  `$nec-deadlines` maps across directly: a PM reply clock is a clock either way.
- **Inverts:** `$subcontractor-check`'s verification pattern (claim vs records, four
  verdicts, draft response) becomes "verify the contractor's application/claim against the
  employer's records" rather than "verify the subbie's application against ours."
  `$valuation` inverts from "build our application" to "check the contractor's
  application" — the employer doesn't build a valuation, it certifies or corrects one.
  Duties that are opportunities for the main contractor (the 61.4 reply period, certifying a
  payment) become obligations to track and not miss for the PM — see Section 4.

## 2. What technically changes

Surprisingly little, and it is worth being specific about why.

### (a) A persona field in the contract profile

`contract-profile.md` (Pattern 13) already captures `contract_family`, `main_option`, and
Z-clause amendments per project. A `persona` field (`main_contractor` / `subcontractor` /
`client_pm`) alongside it would do most of the work: it switches which party's obligations are
"ours" and which are "theirs" for output framing, and which contract instrument governs — under
NEC, a subcontractor's contract is the subcontract (ECS, or the short forms ECSC/ECSS), not the
ECC the main contractor holds, and the short-form timescales already captured in the contract
skills apply (Pattern 6 and `skills/nec-contracts/references/short-forms.md` already state the
ECS/ECSC/ECSS notification and reply periods and the ECSC/ECSS instant-deemed-acceptance rule —
this paper doesn't restate them here beyond noting they already exist in the codebase and would
simply become the governing clock for a subcontractor-up persona rather than an edge case to
flag). For JCT and FIDIC, the persona field would similarly point at the subcontract terms rather
than the main contract's Relevant Events/clause 20.2 regime.

### (b) Guardrail inversions — same machinery, opposite beneficiary

| Today (main-contractor persona) | Inverted (subcontractor-up) |
|---|---|
| `$subcontractor-check` verifies a subbie's incoming application against our records, produces a draft response we send **to** them | Same four-verdict, evidence-cited discipline, run against **our own** records to pre-check **our own** application before we send it **to** the main contractor — a "defend our application" mode |
| `$timesheet-check`'s reverse sweep already finds days worked-but-not-claimed, cutting the check both ways in one run | No change needed — the reverse sweep is already symmetric; a subcontractor running it against their own paid timesheets gets the same underclaim-protection today's main-contractor user gets |
| `$valuation` builds the main contractor's monthly application to the client | Same skill, same steps, run at the subcontractor's own commercial profile rates — it becomes the subbie's application to the main contractor |
| `$events`, `$ce-builder`, `$nec-deadlines` sweep for CEs and time bars against the main contract's notice periods | Same sweep, pointed at the subcontract's notice periods (ECS 7 weeks vs ECC 8 weeks, per Pattern 6) — the event-detection keyword list (Pattern 10) and the four-verdict/evidence machinery are unchanged, only the governing clock differs |

The pattern across every row: the plugin's evidence engine has no directional assumption built
into it. `$subcontractor-check` verifies "a claim against records"; it does not verify
"a claim against records I own and someone else made." Nothing stops the same claim-vs-records
comparison running the other way round — the "defend our application" mode is really the same
skill invoked with the roles of claimant and verifier swapped, which is exactly what the
timesheet-check reverse sweep already demonstrates works today.

### (c) What does not change

- **Evidence discipline and fabrication guards** — every figure still traces to a dated record
  or a stated user-supplied rate, regardless of whose records they are.
- **The four-verdict verification language** (SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED
  BY RECORDS / NO RECORDS) and the rule that absence of a record is a recording gap, never
  evidence work wasn't done.
- **Pattern 8 report numbering**, Pattern 9's commercial QA gate, Pattern 12's schema
  degradation, and Pattern 14/16's "priced where rates exist, quantities-only otherwise, never
  block" rule — all persona-agnostic.
- **RICS alignment** (`docs/rics-ai-standard.md`) — the "material impact" test and the
  AI-use-register/reliability-decision duties apply to whichever regulated firm is using the
  plugin.
- **The read-only, no-CE/EWN-register, no-financial-data-via-API limitations** — properties of
  the Gather API, not of the persona consuming it.

In short: the records don't care who reads them — the main-contractor framing is terminology and
direction layered on top of an evidence-vs-claim engine, not something baked into it.

## 3. The conflict question

Both parties to the same contract could, in principle, run Gather against the same underlying
events — a main contractor checking a subbie's application while that subbie runs a
subcontractor-up session defending the same application, or an employer reviewing a contractor's
claim while the contractor builds it. This needs stating plainly rather than glossed over.

- **The plugin only ever reads its own party's records.** A main-contractor session sees the
  main contractor's Gather workspace; a subcontractor-up session would see the subcontractor's.
  Neither session claims to know, or fabricates, what the other side's records show. There is no
  shared or arbitration view.
- **Simultaneous use by both sides is symmetrical, and arguably a good outcome for dispute
  avoidance.** If both parties are working from contemporaneous, evidence-cited positions rather
  than assertions, the space of things left to actually dispute narrows — that is the same logic
  behind the timesheet-check reverse sweep already being "usable with the other party." Two
  parties each producing a factual, records-backed position is not a conflict; it's what a
  well-run commercial relationship looks like today, just automated on both sides instead of one.
- **That said, Gather should take a positioning decision — and possibly write an
  engagement-rules paragraph into the licence — before marketing both sides of one project.**
  Questions like whether Gather (or a reseller) can knowingly sell and support both a main
  contractor and its subcontractor on the same live project, what if anything the licence should
  say about that, and how support queries from opposing parties on the same dispute are handled,
  are business and professional-conduct questions, not technical ones. This paper flags the
  question; it does not answer it.

## 4. Effort estimate by persona

| Persona | Estimate | What's involved |
|---|---|---|
| **Subcontractor-up** | Small | Add the `persona` field to `contract-profile.md` (Pattern 13); a terminology sweep so outputs say "main contractor" where they currently say "client/PM" and vice versa where the persona is set; a "defend our application" mode added to `$subcontractor-check` and `$timesheet-check` (largely re-pointing existing verdict logic, not new logic — see 2(b)); point `$events`/`$ce-builder`/`$nec-deadlines` at the subcontract's notice periods when the persona is set; fixture coverage in `tests/fixtures/` for the new mode. No new skills required. |
| **PM/client-side** | Medium | New review-mode skills mirroring `$ce-builder` and `$valuation` from the receiving end (certify/query rather than build); PM-specific duties reframed as obligations-to-track rather than opportunities — most notably the 61.4 PM reply clock, which `$nec-deadlines` already tracks but currently frames as "have we missed it" from the contractor's side, needing a "have we (the PM) got X days left to reply" framing instead; and, materially, the employer/PM persona typically has far thinner site records than the party actually on site, so several skills would need to degrade gracefully (Pattern 12-style) when the employer's own records don't cover what the contractor's do, rather than assuming records of similar richness exist on both sides. |

**Sequencing recommendation:** subcontractor-up first, PM/client-side second. Subcontractor-up
is the same buyer motion Gather already runs (a contracting business tracking its own site
records against a counterparty), reuses the same skills with only a terminology and direction
flip, and — per Section 3's framing — most plausibly to a larger addressable set of firms
(subcontractors outnumber main contractors on most supply chains). PM/client-side is a genuinely
different motion (an employer/consultant organisation, often without comparable site records of
its own) and needs new review-mode skills rather than a relabelling of existing ones.

## 5. Decision checklist for Gather

Before any of this becomes build work, these need answers — none of them are technical, and none
are answered here:

1. **Target segment.** Is subcontractor-up aimed at the same tier of subcontractor already
   using main-contractor Gather (i.e. expansion within existing accounts), or a new segment of
   subcontractors who aren't Gather customers today?
2. **Pricing tier.** Does a subcontractor-up licence sit at the same price point as the
   main-contractor product, a reduced tier, or a different packaging altogether (e.g. bundled
   with an existing site-diary subscription)?
3. **Both-sides-of-one-project policy.** Will Gather (directly or through partners) knowingly
   sell to both the main contractor and a subcontractor on the same live project? If so, does
   the licence need an engagement-rules paragraph addressing it (Section 3)?
4. **Channel.** Does subcontractor-up sell through the same channel as today (direct, or via
   main contractors who mandate Gather down their supply chain), or does it need its own route
   to market given the different buyer?
5. **Support load.** Reviewing incoming submissions (PM/client-side) and defending outgoing ones
   (subcontractor-up) both surface disputes to Gather's support desk in a way the current
   one-persona product doesn't — what's the support model if two parties to the same dispute are
   both Gather customers?
6. **Licence wording.** Does the current proprietary licence need amendment to state which party
   role(s) a given customer is licensed for, and any restriction (or explicit permission) on
   multi-party use on one project?

None of these questions has a right answer supplied by this paper — they are listed so the
technical feasibility work in Sections 1–4 isn't mistaken for a green light on the commercial
question.
