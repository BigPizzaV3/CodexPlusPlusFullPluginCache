---
name: contract-profile
description: Capture the contract as executed — amended timescales, secondary options,
  Contract Data, and Z clauses — so contract-touching skills use the contract as amended,
  not the standard form.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Contract Profile

Capture the contract **as executed**, once per project, so `$ce-builder`,
`$ce-quotation`, `$nec-deadlines`, `$weather-impact`, and the contract
knowledge skills (`nec-contracts`, `jct-contracts`, `fidic-contracts`) stop assuming the
unamended standard form. This skill only writes the profile file — it does not itself apply
contract timescales or produce submissions.

Follow **Pattern 13 (Contract Profile)** in `../../shared/patterns/13-contract-profile.md` for the file convention and schema. This
skill is the **producer** of that pattern; every other skill is a consumer. Follow **Pattern 19
(Interview-and-Confirm)** in `../../shared/patterns/19-interview-and-confirm.md`
for the five-step skeleton (resolve → interview → confirm as a table → write → next steps) and
Update Mode — this file holds only the question groups and schema below.

**Disclaimer:** This skill supports contract administration record-keeping. It is not legal
advice. Where entitlement or amendment interpretation is disputed, take professional legal
advice.

---

## Step 1: Resolve the Project

Resolve the project name using **Pattern 1** in `../../shared/patterns/01-project-resolution.md`. If the Gather MCP is connected, verify the
resolved name against `getMyProjects` (or `getProjects` if not in that list) so the `project`
field in the written file matches Gather exactly. If the MCP is not connected, or the project
is not a Gather-tracked project at all, proceed with the name the user gives — this skill works
without a Gather connection.

Determine the target filename:
- One project normally worked on in this directory → `contract-profile.md`
- Multiple projects worked on in this directory (existing `contract-profile-*.md` files present,
  or the user names more than one project) → `contract-profile-<project-slug>.md`, where
  `<project-slug>` is the project name lower-cased with spaces as hyphens

If a profile file for this project already exists, switch to **Update Mode** (below) instead of
running a fresh interview.

---

## Step 2: Interview — One Compact Question Set

Ask everything in one grouped message — never as twenty separate questions — under headings so
the user can answer in one pass and skip anything that doesn't apply:

> **Contract basis**
> 1. Contract family and edition (e.g., NEC4 ECC, NEC3 ECC, JCT SBC 2016, JCT DB 2016, FIDIC
>    Red Book 2017)
> 2. Main option (NEC only — A/B/C/D/E/F)
>
> **Secondary options / bespoke schedule**
> 3. Which secondary options are selected? In particular: X1 (inflation), X2 (changes in law),
>    X5 (sectional completion), X6 (bonus for early Completion), X7 (delay damages — and the
>    rate), X15 (design to reasonable skill and care), X18 (limitation of liability), X22
>    (Early Contractor Involvement), X29 (climate change), Y(UK)1–3, and dispute option
>    W1/W2/W3. (JCT/FIDIC: note bespoke amendments schedule reference instead.)
>
> **Z-clause amendments (only ones that change something)**
> 4. Any amendments to notification timescales — the 61.3 window, the PM's period for reply,
>    programme submission/review intervals, payment periods — or to risk allocation (e.g.,
>    ground conditions, design liability)? State the new value only where it differs from the
>    standard form.
>
> **Contract Data specifics**
> 5. Weather measurements list (which measurements and thresholds are recorded against 60.1(13)
>    / the equivalent clause)
> 6. Key Dates and their conditions
> 7. Delay damages / liquidated damages rate
> 8. Share percentages / gain-share ranges (Options C/D only)

If the user only wants to record one or two fields (e.g., just the amended time bar), accept
that — do not insist on a full interview. Unanswered items are simply omitted from the file.

---

## Step 3: Confirm Back as a Table

Per Pattern 19 step 3, marking unanswered fields "not provided (standard form applies)".

---

## Step 4: Write the File

Write the confirmed values into the target filename from Step 1, following the Pattern 13
schema exactly:

```yaml
project: <Gather project name>
contract_family: <e.g. NEC4 ECC>
main_option: <A-F, NEC only>
secondary_options: [<list>]
z_clause_amendments:            # only entries that CHANGE the standard form
  <field>: <value>              # e.g. ce_notification_weeks: 4  # 61.3 as amended (standard: 8)
delay_damages_rate: "<rate>"
weather_measurements: [<list>]
key_dates:
  - {condition: "<condition>", date: <YYYY-MM-DD>}
verified_against: "<source, e.g. contract as executed rev C2>"
profile_date: <YYYY-MM-DD>
```

Wrap the YAML in a short prose header (one or two sentences: project name, contract family, the
date captured) so the file reads as a human document, not just data. For every field that is
absent, add an inline YAML comment stating the standard-form default applies (e.g.
`# ce_notification_weeks not stated — standard 8-week 61.3 window applies`). Do not include a
field with an invented value — omission plus a comment is always correct where the user gave
no answer.

---

## Step 5: Explain What Happens Next

Per Pattern 19 step 5. Name the consuming skills: `$ce-builder`, `$ce-quotation`,
`$nec-deadlines`, `$weather-impact`, and the contract knowledge skills — they now
cite values as "per the contract profile (as amended)" instead of assuming the standard form.
Point to Update Mode for amendments made later or Key Date changes.

---

## Update Mode

Per Pattern 19 step 1's Update Mode trigger and rules — merge changes into the existing
structure, preserving fields not mentioned, and bump `profile_date` to today.

---

## Hard Rules

1. **Never invent a value.** Every field is user-supplied or omitted. An omitted field means the
   standard form applies — say so with a comment, not silently.
2. **Record only amendments that differ from the standard form.** `z_clause_amendments` is for
   deltas only — do not restate unamended standard-form values there.
3. **Advice-support, not legal advice.** Include the one-line disclaimer in the written file's
   header, not just in conversation.
4. **JCT and FIDIC profiles are allowed.** Omit NEC-only fields (`main_option`, NEC secondary
   options) for those forms, and note the equivalents: JCT → clause 2.27.1 notice periods and
   liquidated damages; FIDIC → clause 20.2 periods and DAAB composition.
5. **Never use "raised" for early warnings.** NEC early warnings are *notified* — use that verb
   throughout, including in file text this skill writes.
6. **A mismatched `project` field is not yours to edit.** If asked to update a profile for a
   different project, resolve that project first (Step 1) rather than editing the file in place.

---

## Worked Example

Read `references/worked-example.md` for a full
illustrative NEC4 ECC Option C profile (not a real project).

---

## Related Skills

- `$ce-builder` — reads the amended 61.3 window and secondary options when drafting a CE
- `$weather-impact` — reads `weather_measurements` and any amended threshold for 60.1(13)
- `nec-contracts` — falls back to standard-form timescales when no profile exists
- `jct-contracts` — reads notice period and liquidated damages equivalents
- `fidic-contracts` — reads clause 20.2 period and DAAB composition equivalents
