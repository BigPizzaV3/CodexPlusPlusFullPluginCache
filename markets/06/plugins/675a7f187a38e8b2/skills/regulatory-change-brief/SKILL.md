---
name: regulatory-change-brief
description: Render horizon scan findings into a finished deliverable — an in-house executive or board memo, a law-firm client alert, obligation register rows for a compliance tracker, or a short email or Slack digest — with citations carried through to the reader. Use when the user asks to write up, summarise, or circulate regulatory findings, or asks for a memo, alert, briefing, digest, or register entries from a scan.
---

Read `../../references/runtime-safety.md` before using this workflow. Resolve relative paths from this skill directory. To use a sibling skill, read its `../<skill-name>/SKILL.md`; no special invocation tool is required.


Turn findings into something the user can send. The analysis is already done by `horizon-scan` or
`assess-materiality`; this skill is about audience and format.

**Read `../../references/citation-discipline.md` first.** Then the rule that governs this skill
specifically: **citations travel to the reader.** A brief is where sourcing is most tempting to
strip for readability and where stripping it does the most damage — the recipient is further from
the source than the user is, and often acts on it.

Templates: `../../references/output-templates.md`.

---

## 1. Ask which format, if not obvious

| Format | Audience | Shape |
|---|---|---|
| `exec-memo` | In-house: GC, exec team, board | What changed, what it means for us, what we're doing, what we need |
| `client-alert` | Law firm: clients or a client group | What changed, who it affects, what to do, how we can help |
| `register` | Compliance tracker / obligation register | Structured rows, CSV-ready |
| `digest` | Email or Slack, internal circulation | Short, scannable, links out |

Infer from context where you can — "write this up for our board" is an `exec-memo`, "send to
clients" is a `client-alert`. Ask only when genuinely ambiguous.

Also ask, or infer, **who the reader is and what decision they face**. A board paper for an
approval decision is a different document from an FYI to the same board.

## 2. Filter to what this audience needs

For a client alert, first obtain the client's saved business profile, or run `compliance-profile`
for that client before discovery. Never substitute the law firm's own profile. For a client group,
agree an explicit representative profile and disclose its limits; keep materially different clients
in separate profiles and ledgers. If findings came from another profile, run `horizon-scan` against
the client profile before drafting: filtering a firm-scoped scan cannot recover missed rules.
Existing findings may be reused only when their scope matches and sources are reverified.
Start the alert with a concise summary of the client business, jurisdictions, activities and
unresolved applicability facts that scoped the research.

A brief is not a scan with a header on it. Cut hard, and cut by relevance to the reader:

- **exec-memo / digest** — `binds_us` and `likely` only, at the profile threshold or above.
  `monitor_only` items belong in an appendix or nowhere. Put `unassessed` items in a
  separate questions section when material to the decision; never present them as duties.
- **client-alert** — items discovered against the client or agreed client-group profile.
  Be explicit about that audience and individual applicability limits.
- **register** — everything reportable, since a register is a system of record rather than a read.

## 3. Carry the citations through

Non-negotiable, per format:

- **exec-memo / client-alert** — inline linked references at each claim, plus a closing sources
  list with `official_id`, publisher, and `retrieved_on` for each item.
- **register** — mandatory `source_url` and `official_id` columns. A row without them is not
  written.
- **digest** — every item links to its primary source. A digest is the format most likely to be
  forwarded onward with no further context, which makes the link matter more, not less.

**If an item's provenance cannot be rendered in the chosen format, the item does not go in the
brief.** Do not include it unlinked. Say which items you left out and why.

**Never summarise away a date's source.** In prose, keep the link on the sentence carrying the date:

> Comments must be received or postmarked by 11:59 p.m. Eastern Time on
> [30 September 2026](https://www.federalregister.gov/documents/2026/08/03/2026-15717/ventilation-plan-approval-criteria).

Note the time and time zone survived into the prose. Compressing that to "closes 30 September" loses
eleven hours on a filing deadline, which is the kind of tidying that costs someone a submission.

## 4. Carry the gaps through too

Every brief reproduces the coverage-gap list from the scan. This is not optional and not a
formality.

A reader who receives a brief with no gap list will read it as a complete picture of the regulatory
horizon. If US state law was not searched, or the EU window was only partly covered, or a source
failed, the recipient needs to know — they are the one who will act on it, and they cannot see the
scan behind it.

Keep it short and plain:

> **Not covered by this scan:** states not selected, local law, and any selected state source
> families marked partial or failed. EU coverage for 11 July – 2 September relied on the
> OJ feed only and may be incomplete.

## 5. Write for the audience

**exec-memo.** Lead with the decision or the ask, not the chronology. An executive reader wants to
know what they must decide and by when. Put "what we need from you" high, not at the end.

**client-alert.** State up front who is affected and who is not — clients reading an alert that
doesn't apply to them stop reading the next one. Be careful with the line between information and
advice; describe the position and the general steps, and be explicit that specific advice depends
on the client's circumstances.

**register.** Consistency beats prose. Same vocabulary, same date format, one obligation per row.

**digest.** Ruthless. One line per item, the date, the link. If it runs past a screen, it won't be
read, and a digest nobody reads is worse than none.

## 6. Standard elements on every format

- **Disclaimer**, on every brief: regulatory intelligence, not legal advice; verify against cited
  sources before acting.
- **Provenance tally**: `N items, N fully sourced, N coverage gaps`.
- **Scan window and date**, so the reader knows how current it is. A brief read three months later
  with no window on it is actively misleading.

## 7. Self-check

- [ ] every claim in the brief traces to a link that reaches the reader
- [ ] every date carries its source
- [ ] no item was included without renderable provenance
- [ ] the coverage-gap list is present
- [ ] the disclaimer, window, and tally are present
- [ ] nothing from `Unverified leads` made it in — by rule, they never enter a brief

---

## On tone

Both audiences are professional readers who will lose confidence in an overstated brief faster than
in a dull one. Two habits to avoid:

**Don't manufacture urgency.** If nothing is urgent, say the horizon is quiet. A brief that makes a
`medium` item sound `critical` gets discounted, and then the real `critical` item gets discounted
too.

**Don't hedge to cover thin sourcing.** "May potentially require consideration of possible changes"
is not caution, it is an unsourced claim in a raincoat. Either the instrument requires something —
quoted and linked — or you say what is not yet established. Certainty should come from the source,
and uncertainty should be stated as a specific unknown rather than diffused through the prose.
