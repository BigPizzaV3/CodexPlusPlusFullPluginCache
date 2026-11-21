---
name: adjudication-pack
description: Assemble a referral- or response-ready adjudication evidence bundle —
  issue chronologies, records schedules, programme evidence, quantum refs, witness
  skeletons. Document assembly support, not legal advice.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Adjudication Readiness Pack (Ref AJ-NNN)

The responding party in a UK construction adjudication typically has days, not weeks, to put a
case together once the Notice of Adjudication lands — and the referring party is usually working
to a self-imposed deadline before serving it. This skill assembles the evidence bundle from
Gather records fast: issue chronologies, records schedules, programme evidence, quantum
cross-references, and witness skeletons, indexed and ready to hand to the party's legal team.
Follow the shared patterns: `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/07-event-to-clause-mapping.md` (event-to-clause mapping).

**Scope note:** this is document assembly support for the party's legal team — **not legal
advice, not a referral notice, not a response, and no substitute for adjudication counsel**. It
never characterises the dispute, never asserts causation, fault, or entitlement, and never
states a procedural deadline as settled fact. Every deadline in this pack is indicative and
flagged for verification against the contract and statute by the party's lawyers.

**Local files this skill reads (never writes):**
- **Pattern 13 (Contract Profile)** — `contract-profile.md`, for `contract_family` and
  `secondary_options` (W1/W2/W3, or JCT/FIDIC as applicable) to identify which dispute regime
  applies. Absent → ask the user, or state the Construction Act/Scheme fallback assumption
  prominently and continue.
- **Pattern 15 (Programme Baseline)** — `programme/programme-baseline.md`, read as stored for
  Step 3(c). Never recomputed.
- **Pattern 17 (Correspondence Register)** — `correspondence/correspondence-register.md`:
  confirmed items join the Step 3 chronologies as correspondence lines, cited
  "[COR-NNN] ([date], [from] → [to], "[subject]")" with excerpts as recorded. UNCLASSIFIED
  items are "correspondence dated [date]", never characterised as a notice. Absent → the
  chronology is records-only (say so once; point to `$correspondence-import`).
- **Session refs** — any `EV`/`DA`/`AC`/`WI`/`EP`/`QT`/`AP`/`CV` report produced earlier in this
  conversation is reused and cited, never re-derived from scratch.

---

## Step 1: Mode, Dispute, and the Applicable Regime

1. **Mode** — REFERRING or RESPONDING. Take it from `the user’s request` or ask; changes framing only,
   not the assembly method below.
2. **The dispute, as the user states it** — record it verbatim. **Never characterise, narrow,
   or invent the dispute.** If the user's statement is thin, ask for more detail rather than
   assuming the merits.
3. **Project** — Pattern 1.
4. **Dispute regime** — check `contract-profile.md` (Pattern 13):
   - **NEC, `secondary_options` includes W2** (or Construction Act applies) → NEC's
     HGCRA-compliant procedure; NEC4 adds a senior-representatives negotiation step first — note
     it if the profile confirms NEC4.
   - **NEC, `secondary_options` includes W1** (or W3 with adjudication, not the standing Dispute
     Avoidance Board, confirmed in use) → NEC's standard (non-HGCRA) procedure.
   - **JCT** → clause 9.2: either party may refer any dispute at any time; decision due within
     **28 days of referral** (42 days with the referring party's consent, or longer by
     agreement) — cite as JCT clause 9.2, **indicative**.
   - **No profile, unresolved, or UK statutory construction operations with no bespoke clause**
     → state prominently: **Housing Grants, Construction and Regeneration Act 1996 (as amended)
     / the Scheme for Construction Contracts** applies by default — refer "at any time",
     referral typically within **7 days** of the Notice of Adjudication, decision typically due
     within **28 days of referral** (extendable to 42 with consent, or longer by agreement).
     Label **general Construction Act / Scheme position, indicative only**.
   - **FIDIC** → the DAB/DAAB mechanism differs from UK statutory adjudication; if UK-based, the
     Construction Act may still bite independently — flag for legal advisers, don't resolve here.
5. **Standing caveat on every regime line:** all procedural deadlines and time bars must be
   confirmed with the party's legal advisers before being relied on — timescales here are
   indicative only, never a live countdown (for that, once regime and trigger dates are settled
   with counsel, see `$nec-deadlines`).

---

## Step 2: Issue Breakdown

Decompose the stated dispute into discrete issues **with the user** — a multi-issue dispute
(e.g. "3 weeks' delay to pier works" might turn on late access, late information, and a
disputed instruction) needs separate evidence packs, not one blended narrative.

- **Interactive:** propose a candidate issue list from the dispute description and Pattern 7's
  event categories, and get the user to confirm, add, or remove issues before proceeding.
- **Non-interactive runs:** state the proposed issue list as an **assumption**, proceed, and
  flag it clearly at the top of the output so it can be corrected before the pack is relied on.

Each issue gets its own number (Issue 1, Issue 2, ...) carried through Steps 3–5.

---

## Step 3: Assemble the Evidence, Per Issue

For each issue, build all five parts below from Gather records. Apply Pattern 3 to any source
returning nothing — an empty source is a stated finding, not a silent gap.

**(a) Dated chronology** — sweep `narrative-search`-style across the issue's keywords
(Pattern 10, plus any issue-specific terms confirmed with the user) and, where relevant,
labour/access/weather data. One line per fact, strictly chronological:

> [date] — [record ID] ([source: shift diary / access register / weather record]) — "[excerpt,
> as recorded]"

**Records and timings only — no causation.** This is the same discipline as the CE Evidence
agent's incident-evidence-pull: state what the records show and when, never why, never whose
fault. Early warnings are **notified**, never "raised". Where two records coincide in time, say
"coincides with", never "caused by" or "due to".

**(b) Records schedule** — a table companion to the chronology:

| Date | Record ID | Source | What it evidences |
|---|---|---|---|

**(c) Programme evidence (Pattern 15)** — if `programme/programme-baseline.md` exists and its
project matches, cite the relevant baseline/actual dates and stored criticality/float **exactly
as stored at their data date — never recomputed**, per "per the imported programme ([revision],
exported [date])". Absent → state the standard limitation and point once to
`$programme-import`; do not fabricate a planned date from a quantity.

**(d) Quantum cross-references** — cite `QT-[NNN]` (CE quotation), `AP-[NNN]` (valuation),
`CV-[NNN]` (CVR), or `FA-[NNN]` (final account, where that skill has produced a figure) refs
already established in this conversation. No matching ref → "**not yet quantified**" — never a
guessed figure. Per Pattern 11, quantum refs are cited, never summed together across register
types.

**(e) Gaps** — state plainly, per issue, wherever the chronology, schedule, programme, or
quantum has a hole: dates with no records, an activity with no baseline mapping, an issue with
no quotation ref. **A recording gap is a gap, not absence of the underlying fact** — and in
adjudication, the other side will find it first if this pack does not surface it. Never smooth
a gap over elsewhere in the pack.

---

## Step 4: Witness Skeletons

For each supervisor or named individual appearing in the records assembled for an issue, draft a
**skeleton** — not a statement. At Step 4, read
`references/output-templates.md` for the
skeleton template.

**Hard limits on this step:**
- List **only** what that individual personally recorded — their own diary entries, narratives
  they authored, or records that name them as the recording supervisor.
- **Never** draft opinion, recollection, interpretation, or anything not present verbatim (or as
  a faithful close paraphrase clearly marked as such) in their own records.
- If a named individual has no records of their own for the issue (only appears in someone
  else's narrative), say so — do not build a skeleton from second-hand mentions.

---

## Step 5: Bundle Assembly

Present an index, then the full pack, issue by issue. At Step 5, read
`references/output-templates.md` for the
header/index template and the full-content ordering.

**Output:** offer to save the full pack to the working folder as
`adjudication-pack-[date].md`. If accepted, write it there; if declined or the run is
non-interactive, deliver the full pack as chat text instead.

Apply **Pattern 8** for the `Ref: AJ-[NNN]` line — increment on a prior `AJ` ref in this
conversation, else `001`, with the standard session-local caveat line.

---

The standing caveat, always, unmodified:

> This is document assembly support for the party's legal team — **it is not legal advice, not a
> referral notice, not a response document, and no substitute for adjudication counsel**. It does
> not characterise the dispute, and it does not assert causation, fault, or entitlement — the
> chronology and records schedule state what the records show and when, nothing more. All
> procedural deadlines and time bars in this pack are **indicative only** and must be verified
> against the contract as executed and the applicable statute by the party's legal advisers
> before any step is taken or missed on their strength. Records excerpts are reproduced as
> recorded; every gap is stated, not smoothed over. Witness skeletons are drawn solely from each
> individual's own contemporaneous records, for that individual to review, amend, and adopt or
> reject — they are not statements and must not be treated as one.
> Ref: AJ-[NNN] is a session-local sequence number for cross-referencing.

---

## Hard Rules

1. **Never characterise the dispute.** Take it exactly as the user states it; never narrow,
   reframe, or infer what it "really" is.
2. **Records and timings only — never causation, fault, or entitlement.** "Coincides with", not
   "caused by". Chronologies and schedules state what happened and when; they do not argue why or
   whose fault it was.
3. **Witness skeletons contain only that witness's own records** — no invented recollection, no
   opinion, no second-hand mentions dressed up as their evidence.
4. **Every deadline is labelled indicative and paired with "confirm with legal advisers"** — this
   skill never presents a procedural time bar as settled fact.
5. **A recording gap is a gap, not absence.** State it per issue; never let a gap read as
   evidence that nothing happened.
6. Early warnings are **notified**, never "raised" (NEC's verb).
7. UK English throughout.

---

## Related Skills

- CE Evidence agent — single-event evidence packs (this skill assembles a multi-issue dispute
  bundle; the CE Evidence agent is the single-event deep-dive it can draw on)
- The Time & Claims Advisor agent — entitlement analysis and claim-package assembly; this
  skill stops at evidence assembly and never analyses entitlement itself
- `$asbuilt-programme` — as-built timing reconstruction feeding Step 3(c) where no
  imported baseline exists
- `$narrative-search` — deeper, single-issue narrative digs beyond the per-issue sweep here
- `$final-account` — quantum reference source for Step 3(d) (being added this release)
