---
name: assess-materiality
description: Assess one named regulatory development in depth against a business's compliance profile — whether it binds them, which provisions engage, what would have to change operationally, and by when. Use when the user names or pastes a specific regulation, rule, directive, statutory instrument, bill, or consultation and asks whether it applies to them, what it means for them, or what they need to do about it. Complements horizon-scan, which finds developments; this one analyses a single development.
---

Read `../../references/runtime-safety.md` before using this workflow. Resolve relative paths from this skill directory. To use a sibling skill, read its `../<skill-name>/SKILL.md`; no special invocation tool is required.


Deep-dive one development. Where `horizon-scan` triages breadth, this goes to depth on a single
instrument the user cares about.

**Read `../../references/citation-discipline.md` first. It governs everything below.** The depth
here makes provenance more important, not less — a detailed operational analysis built on an
unsourced threshold is confidently wrong in a way a one-line finding never is.

---

## 1. Identify the instrument precisely

The user may give you a name, a number, a URL, a pasted extract, or a vague description. Pin it down
to a specific instrument with an identifier before analysing anything.

- **Resolve it to a primary source and fetch it.** Federal Register document number, CELEX,
  UK SI `year/number`, or a state instrument identified by state, type, session, and official
  number. For a named state instrument read `../../references/sources-us-states.md`; an
  explicit one-off assessment does not change saved recurring state selections. Use `../../references/sources-us-federal.md`, `sources-eu.md`, `sources-uk.md`.
- **If you cannot find it, say so.** Do not analyse an instrument you could not locate. A
  plausible-sounding name may be a misremembering, a proposal that was never adopted, a measure
  under a different number, or nothing at all. The correct response is:

  > I could not locate a primary source for that. Can you share a link or the official number? I
  > searched <sources> on <date> and found nothing matching.

  Never produce an analysis from recall to be helpful. This is the single most likely way this
  skill could cause harm.
- **If several instruments could match, ask which** rather than picking the most likely. Amending
  instruments, corrigenda, and consolidations often share most of a title.

## 2. Get the profile

Ask for the compliance profile. Without it there is no "material to whom," and the answer collapses
into a generic summary the user could get anywhere.

If they don't have one, you can still analyse the instrument, but say clearly that applicability is
unassessed and ask the specific facts that decide it — usually jurisdiction, headcount, data types,
and whether they are consumer-facing.

## 3. Read the instrument and extract, with quotes

- **Scope** — who it binds, in its own words. Quote the scope provision.
- **Lifecycle stage** — proposed, in consultation, adopted, in force, or applying from a date.
- **Every date** — comment deadline, entry into force, application, staged milestones, first
  reporting date. Each quoted separately from the provision that sets it.
- **Thresholds** — headcount, turnover, data volume, product class. Quoted.
- **Substantive obligations** — what must actually be done.
- **Penalties and liability**, including whether any is criminal or personal.
- **Exemptions and derogations** — often where the answer actually lives, and commonly missed.

Where the instrument amends another, **read the amended instrument too**. An amending act's text is
often unintelligible in isolation ("in Article 4, replace 'six' with 'twelve'"), and reporting the
amendment without the underlying provision tells the user nothing.

## 4. Assess applicability against the profile

Apply `../../references/materiality-rubric.md`. Name the profile field and the threshold that
decides it:

> `binds_us` — Article 2(1) applies to "an employer with 50 or more employees";
> `headcount_by_jurisdiction.UK = 120`.

Score `unassessed` and **name the missing facts** when scope cannot be assessed. Use
`likely` only when affirmative evidence supports probable applicability. Do not resolve
ambiguity toward the more interesting answer, in either direction — neither inflating applicability
to seem useful nor dismissing it to seem reassuring.

## 5. State what would have to change

This is the part the user cannot get from reading the instrument, and the reason to run this skill.
Be concrete and tie each item to the provision that requires it:

- **Policies and documents** — which ones, and what has to change in them
- **Systems and product** — engineering work, data flows, retention, consent, logging
- **Contracts** — customer terms, supplier terms, DPAs, flow-down clauses
- **Governance** — approvals, sign-off, board or committee reporting
- **Evidence** — what a regulator would ask to see, and what would have to exist to show it

Separate **what the instrument requires** from **what would be prudent**. Both are useful; conflating
them misleads. Label the second as your assessment, not as obligation.

## 6. Output

```
## <Instrument name> · <official_id>
`<stage>` · <publisher> · retrieved <date>

**Bottom line.** <Two or three sentences: does it bind them, what is the hardest part, by when.>

**Scope** — <who it binds, quoted> [link]

**Applicability: `binds_us`** — <profile field and threshold, quoted>

**Key dates**
| What | Date | Source |
|---|---|---|
| Comment deadline | <date, or "none"> | "<verbatim quote>" [link] |
| Entry into force | <date> <if computed: "(derived: <arithmetic>)"> | "<verbatim quote>" [link] |
| Applies from | <date, or "not specified in the instrument"> | <quote, or "—"> |

**Obligations that engage** — <each with the provision and a quote>

**What would have to change** — <policies / systems / contracts / governance / evidence>

**Penalties** — <quoted, with whether any is criminal or personal>

**Exemptions worth checking** — <any that might apply, with provisions>

**Score** — impact `high` · effort `program_change` · timeline `30-90` · confidence `high`
**Flag** — <e.g. effort exceeds available lead time>

**Not established from the sources** — <anything you could not source, listed explicitly>

---
Regulatory intelligence, not legal advice. Verify against the cited primary sources before acting.
```

The **"Not established from the sources"** section is mandatory and must not be dropped when it
would be empty of interesting content — write "nothing material" rather than removing the heading.
It is where an unpublished effective date, an unresolved threshold, or an unreachable amended
instrument gets named. A detailed analysis that quietly omits what it could not establish reads as
more complete than it is, which is precisely the failure this heading prevents.

## 7. Self-check

Run the checklist in `citation-discipline.md`. Every date, threshold, and penalty in the output
traces to a verbatim quote from a document fetched this session, or it is moved to "Not established."
Then state the provenance tally.

---

## When the user pushes for a bottom line you cannot source

They will sometimes want a date, a number, or a yes/no that the sources do not give — often for a
real deadline of their own. Give the sourced part, name the gap, and say what would close it:

> The comment deadline is fixed and sourced: 11:59 p.m. Eastern Time on 30 September 2026 (quoted,
> linked). The instrument sets no effective date, and none is published — that comes with the final
> rule. I can't give you a date for it. If you need something to plan against, the comment deadline
> is the one that's certain; I'd re-scan this agency monthly for the final rule rather than plan to
> an assumed date.

That is a complete and useful answer. An invented effective date, however well hedged, is not.
