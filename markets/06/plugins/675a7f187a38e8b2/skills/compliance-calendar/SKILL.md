---
name: compliance-calendar
description: Build a forward calendar of dated regulatory obligations from scan findings or a compliance profile — comment deadlines, entry-into-force dates, applies-from dates, staged transition milestones, and first reporting dates — each carrying the source link and the quote that establishes it. Use when the user asks what is coming up, what deadlines they face, what to diarise, or wants a compliance calendar or timeline for a quarter, year, or specific regulation.
---

Read `../../references/runtime-safety.md` before using this workflow. Resolve relative paths from this skill directory. To use a sibling skill, read its `../<skill-name>/SKILL.md`; no special invocation tool is required.


Turn findings into dates the user can diarise, each traceable to the provision that sets it.

**Read `../../references/citation-discipline.md` first.** This skill carries the highest fabrication
risk in the plugin: an unsourced date here gets entered in a diary, relied on, and either missed or
acted on early. **A date with no quotable source is omitted and listed as a gap — never estimated,
never interpolated, never carried over from a similar instrument.**

---

## 1. Get the input

Either the findings from a `horizon-scan` run, a specific instrument, or a compliance profile (in
which case run a scan first, or work from the domains in scope).

## 2. Extract every dated obligation

For each finding, pull out **every** date, not just the headline one. A single instrument commonly
carries several, and the one that matters to this user may not be the first:

- consultation or comment deadline
- adoption date
- entry into force
- applies-from / application date
- staged milestones — by obligation, entity class, or product category
- first reporting date, and the reporting period it covers
- transitional or grandfathering cut-offs
- review or sunset dates

**Each becomes its own calendar entry.** Do not collapse a staged regime into a single date — the
staging is usually the operationally important part, and a business may be in scope for one stage
and not another.

## 3. Source every date individually

Each entry carries the link and the verbatim quote from the provision that sets it. Different dates
in one instrument usually come from different provisions; cite each to its own.

**Derived dates.** Where a date must be computed — an EU act's "twentieth day following that of its
publication," a UK SI's "the day after the day on which these Regulations are made" — show the
arithmetic, quote the provision, and label it derived:

> **28 September 2026** — entry into force *(derived: 20th day after OJ publication 8 September
> 2026)* · "shall enter into force on the twentieth day following that of its publication in the
> *Official Journal of the European Union*" · [CELEX 32026R1975](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026R1975)

**Undated obligations.** These are common and must be represented honestly, not dropped and not
guessed:

- A proposed US rule has no effective date — `effective_on` is `null`. The comment deadline is the
  one possible fixed date; hearing, registration, and other procedural dates may also be set.
- A UK SI may commence "on such day as the Secretary of State may by regulations appoint," which
  means **no date exists yet**.
- An EU directive's transposition deadline binds member states, not businesses; the business date
  comes from national law, which is outside v1 coverage.

Put all of these in an **Undated / pending** section with the reason and what will fix it. This
section is often the most useful part of the calendar, because it tells the user what to keep
watching rather than implying nothing is coming.

## 4. Flag lead-time mismatches

Compare each entry's `effort` score to the time available. Where effort exceeds lead time, flag it —
this is frequently the single most valuable output of the whole plugin:

> ⚠️ **Lead-time risk** — `program_change` due in 41 days. Cross-functional work with under six
> weeks of runway.

Rough guide, to be applied with judgement rather than mechanically: `program_change` needs quarters,
`policy_change` needs weeks, `documentation_only` needs days.

## 5. Output

Group by time bucket, soonest first, and make every date checkable:

```
## Compliance calendar · <profile_name>
Built <date> from a horizon scan covering <window>. Dates are as published; verify before diarising.

### Next 30 days
| Date | What | Instrument | Effort | Source |
|---|---|---|---|---|
| 2026-09-30 | Comment deadline | DOL proposed rule 2026-15717 | — | "<quote>" [link] |

### 30–90 days
### 90–365 days
### Beyond 12 months
### Undated / pending
| What | Why undated | What will fix it |
|---|---|---|
| Effective date, DOL 2026-15717 | Proposed rule; no effective date published | Final rule publication — re-scan `labor-department` monthly |

### Lead-time risks
<entries where effort exceeds available runway>

**Provenance:** N dated entries, N sourced to a quoted provision · N derived (arithmetic shown) ·
N undated and listed as pending · N coverage gaps

---
Regulatory intelligence, not legal advice. Verify each date against the cited source before relying
on it or entering it in a diary.
```

## 6. Self-check — strictly

Before returning, walk every entry:

- [ ] every date traces to a verbatim quote from a document fetched this session
- [ ] every derived date shows its arithmetic and the provision it rests on
- [ ] no date is inferred from a similar instrument, from a typical pattern, or from recall
- [ ] undated obligations appear in the pending section rather than being dropped or filled
- [ ] the provenance tally is stated

Then state the tally. If a date failed the check, it is not in the calendar — say so in the gaps
line rather than including it with a caveat. A caveated date in a table still gets diarised.

---

## Offering it as a file

Users usually want this in their own calendar or tracker. Offer a CSV they can import, with columns
`date,what,instrument,official_id,effort,source_url,supporting_quote`.

**Keep `source_url` and `supporting_quote` as columns in the export.** They are what make an entry
checkable six months later, when whoever reads the row has forgotten where it came from and is
deciding whether to act on it. Stripping them for tidiness defeats the purpose of the calendar.
