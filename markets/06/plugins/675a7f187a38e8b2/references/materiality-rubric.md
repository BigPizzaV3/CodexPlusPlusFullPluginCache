# Materiality rubric

A fixed scoring model, so results are comparable between scans, between businesses, and between
whoever is reading. Score every finding on all five axes and show the scores — a score the reader
can't see is a score they can't challenge.

**The provenance gate in `citation-discipline.md` runs first.** Materiality never overrides it: a
`critical` finding with no resolvable source is a coverage gap, not a headline.

---

## 1. Applicability

Does this bind *this* business, per the profile?

| Value | Meaning |
|---|---|
| `binds_us` | The business is within scope on the face of the instrument. |
| `likely` | Evidence supports probable scope, but a remaining fact needs confirmation. Name both the evidence and missing fact. |
| `unassessed` | Available facts do not establish whether the business is in scope. Name the missing facts without guessing probability. |
| `monitor_only` | Not in scope now; a plausible business change or a pending extension would bring it in. |
| `not_applicable` | Confirmed out of scope. Exclude from scan findings even if an `always_report` keyword matches. |

**Always name the profile field that triggered it.** "Applies because
`headcount_by_jurisdiction.UK = 120` exceeds the 50-employee threshold" is auditable;
"applies to your business" is not. Where a threshold decides applicability, that threshold needs its
own citation and quote — it is one of the per-claim sourcing fields.

Where missing facts prevent assessing scope, score `unassessed` and ask. Use `likely` only
when affirmative evidence supports it, not merely because a fact is missing. Do not assume
the answer that makes the finding more interesting.

## 2. Impact

What happens to the business if this applies?

| Value | Anchors |
|---|---|
| `critical` | Criminal liability; personal liability for directors or officers; licence or authorisation condition; ability to operate or sell in a market is at stake. |
| `high` | Significant financial penalty exposure; mandatory product, contract, or system change; new external reporting obligation; new regulator notification duty. |
| `medium` | Policy, notice, or documentation changes; internal process change; new record-keeping duty. |
| `low` | Clarification, guidance, or codification of existing practice; procedural or definitional change with no operational consequence. |

Criminal liability, personal liability, and licence conditions are **always** `critical`, regardless
of how remote the risk appears. That judgement belongs to counsel, not to this tool.

## 3. Effort

What would compliance actually take?

- `program_change` — cross-functional work: engineering, new controls, new systems, external audit.
- `policy_change` — policies, contracts, notices, training.
- `documentation_only` — record-keeping or evidence-gathering against existing practice.
- `not_applicable` — no compliance work established for an out-of-scope business.
- `unassessed` — scope or obligations are not sufficiently established to estimate effort.

## 4. Timeline

Days from today to the **next dated action** — comment deadline, entry into force, applies-from
date, or first reporting date, whichever comes first.

Buckets: `<30` · `30-90` · `90-365` · `>365` · `undated`

`undated` is a legitimate and common value. Use it whenever no date is published, and never
substitute an estimate — see the per-claim sourcing rules. Say which date the bucket is measured to,
because "60 days" means something very different for a comment deadline than for entry into force.

## 5. Confidence

**Derived from `provenance.source_tier`. Never asserted independently.**

| Value | Basis |
|---|---|
| `high` | Primary instrument fetched this session. |
| `medium` | Regulator's own site or guidance fetched this session, primary instrument not reached. |
| `low` | Secondary only — press, commentary, newsletter. |

`low` confidence items are **not findings**. By rule 5 of the citation discipline they stay in
`Unverified leads` until the primary instrument is reached. There is no path by which a `low`
confidence item enters a brief, a register, or the calendar.

---

## Reporting rule

Report a finding when **both** hold:

1. The provenance gate passes — complete record, verbatim quote, per-claim sourcing.
2. Either `impact >= profile.materiality_thresholds.report_at_or_above`, **or** any
   `profile.materiality_thresholds.always_report` tag matches.

And `applicability` is not `not_applicable`. `always_report` overrides the impact threshold
and keyword exclusions only for a potentially relevant development; it never overrides
confirmed non-applicability or provenance. Match liability tags to the development's
relevant provisions, not an incidental mention of liability in unrelated historical text.
Put `unassessed` items in a separate “Applicability questions” section, not confirmed duties.

## Ordering

Sort findings by:

1. `always_report` matches first
2. then impact: `critical` → `high` → `medium` → `low`
3. then timeline proximity: `<30` → `30-90` → `90-365` → `>365` → `undated`
4. then applicability: `binds_us` → `likely` → `monitor_only` → `unassessed`

Rationale for putting timeline behind impact: a `critical` item due in six months deserves attention
before a `medium` item due in three weeks, because the lead time it needs is longer. But do
separately flag any item where **effort exceeds the available lead time** — a `program_change` with a
`<30` or `30-90` timeline is already a problem, and that mismatch is often the single most useful
thing in a scan.

## Worked examples

### A real, fully sourced finding

Verified 2026-09-09. Scored against the test profile in `../evals/test-prompts.md`:

> **US — Ventilation Plan Approval Criteria** · FR `2026-15717` · `proposed`
> - applicability: `not_applicable` — Labor Department mine ventilation rulemaking; the profile's
>   `sector` is B2C subscription software and `regulated_products` is empty. No `always_report` tag
>   matches, so **this is not reported.**
> - confidence: `high` — [primary instrument fetched](https://www.federalregister.gov/documents/2026/08/03/2026-15717/ventilation-plan-approval-criteria)
> - comment deadline: 2026-09-30 — "All new comments must be received or postmarked by 11:59 p.m.
>   Eastern Time on September 30, 2026."

Included deliberately as a **negative** example. A high-volume register returns a great deal of
matter like this, and correctly scoring it out is most of what makes a scan usable. Note also that
the deadline is quoted in the document's own words, with its time and time zone intact.

### Scoring shape (illustrative)

The instrument below is **fictional** — identifier `SI 2099/9999`, deliberately outside any real
numbering so it cannot be mistaken for a real instrument or cited by accident. It exists only to
show the shape of a complete score:

> **UK — The Illustrative Data Protection Regulations 2099** · SI `2099/9999` *(fictional)*
> - applicability: `binds_us` — `personal_data` includes `employee` and `operating_jurisdictions`
>   includes `UK`; threshold met at `headcount_by_jurisdiction.UK = 120`
> - impact: `high` — new external reporting obligation
> - effort: `policy_change`
> - timeline: `30-90` (to applies-from date)
> - confidence: `high`
> - **flag:** none; effort is proportionate to lead time

Every line is checkable against the profile and the cited source. That is the standard: a reader who
disagrees should be able to see exactly which input to argue with.

**Never pair a real identifier with invented content**, in an example or anywhere else. A real
document number attached to a plausible-but-invented title or quote is the most dangerous artifact
this plugin could produce, because it survives a spot-check of the link.
