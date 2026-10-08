<!-- Samples demonstrate output structure, not verified facts or reusable scores.
Re-fetch legal claims; score against the current profile. Never copy a sample score. -->
# Output templates

Four formats. Every one carries citations to the reader, a coverage-gap list, a provenance tally,
the scan window, and the disclaimer. Those five elements are structural — do not drop them to make
a document look cleaner.

Placeholders in `<angle brackets>`. Examples below use verified real sources so the shape of a
correct citation is unambiguous.

---

## 1. `exec-memo` — in-house executive or board

```markdown
# Regulatory horizon — <period>
**To:** <audience> · **From:** <author> · **Date:** <date>
**Scan window:** <start> → <end> · **Scope:** <jurisdictions> · <N> items above <threshold>

## What we need from you
<The decision or approval sought, and by when. If nothing, say "No decisions required this period.">

## Bottom line
<Three or four sentences. What changed, what binds us, what the tightest deadline is.>

## Items requiring action

### 1. <Instrument name> — <impact>, <timeline>
**What it is.** <One or two sentences.>
**Why it binds us.** <Profile field and threshold, quoted and linked.>
**Key dates.** <Each date, quoted and linked.>
**What it takes.** <Operational change, tied to provisions.>
**Owner / next step.** <Who, what, by when.>

## Monitoring only
<One line each: instrument, why not yet applicable, what would change that.>

## Not covered by this scan
<Uncovered jurisdictions and failed sources, in plain terms.>

## Sources
| Instrument | Identifier | Publisher | Retrieved | Link |
|---|---|---|---|---|

---
*Regulatory intelligence, not legal advice. Verify against the cited sources before acting.*
*Provenance: <N> items, <N> fully sourced, <N> coverage gaps.*
```

**Notes.** "What we need from you" goes first because an executive reader is scanning for their own
decision. If the honest answer is that nothing is needed, say so plainly — it is a useful result and
it builds trust in the periods when something *is* needed.

---

## 2. `client-alert` — law firm

```markdown
# <Headline: what changed, plainly>
**<Firm>** · <date> · <practice area>

## Who this affects
<Specific. Sector, size, jurisdiction, activity. Say who it does NOT affect.>

## What has changed
<What was published, by whom, when, and its current lifecycle stage — quoted and linked.>

## Key dates
| What | Date | Source |
|---|---|---|

## What it requires
<Obligations, each tied to a provision.>

## What to do now
<Concrete steps, in priority order.>

## How we can help
<Brief.>

## Scope of this alert
<Jurisdictions and period covered; what was not searched.>

## Sources
<Full list with identifiers and retrieval dates.>

---
*This alert is general information, not legal advice, and does not create a solicitor–client (or
attorney–client) relationship. Whether and how these developments apply depends on your specific
circumstances.*
```

**Notes.** "Who this affects" — including who it doesn't — is what makes an alert series worth
opening. The disclaimer here is heavier than the internal formats deliberately: an alert goes to
people who are not your client and may act on it.

---

## 3. `register` — obligation register rows

CSV-ready. Columns, in order:

```csv
date_identified,instrument_name,official_id,publisher,jurisdiction,domain,lifecycle_stage,applicability,impact,effort,timeline_bucket,next_action_date,next_action_type,confidence,source_url,supporting_quote,owner,status
```

Example row, from a verified live source:

Example row — real document, real identifier, real verbatim quote, verified 2026-09-09:

```csv
2026-09-09,"Ventilation Plan Approval Criteria","2026-15717","Federal Register",US-Federal,employment,proposed,monitor_only,medium,policy_change,30-90,2026-09-30,comment_deadline,high,"https://www.federalregister.gov/documents/2026/08/03/2026-15717/ventilation-plan-approval-criteria","All new comments must be received or postmarked by 11:59 p.m. Eastern Time on September 30, 2026",,open
```

**Rules.**
- `source_url` and `supporting_quote` are **mandatory**. A row without both is not written.
- One obligation per row. A staged regime becomes several rows, one per milestone.
- ISO dates throughout. Empty string for undated, never a guess.
- `owner` and `status` are left for the user's own workflow.
- Quote the deadline provision in `supporting_quote`, not an editorial summary — this is the field
  someone checks in six months when deciding whether the row is still right.

---

## 4. `digest` — email or Slack

```markdown
**Regulatory horizon · <period>** — <N> items, <N> needing attention

🔴 **<Instrument>** — <what, in one line>. <Date type> <date>. [source](<url>)
🟡 **<Instrument>** — <one line>. <Date type> <date>. [source](<url>)
⚪ **<Instrument>** — monitoring only. [source](<url>)

**Not covered:** <uncovered jurisdictions / failed sources>
<N> items, <N> sourced, <N> gaps · window <start>–<end> · not legal advice
```

Markers: 🔴 critical/high · 🟡 medium · ⚪ monitor only.

**Notes.** One line per item, hard limit. If it doesn't fit on a screen, cut items rather than
shortening the footer — the window, gap line, and disclaimer are what stop a forwarded digest from
being read as current and complete months later.

---

## Citation forms

Get these right; they are how a reader finds the document.

| Source | Cite as | Identifier | Link form |
|---|---|---|---|
| US Federal Register | Document title, agency | FR document number, e.g. `2026-15717` | the API's `html_url` |
| US CFR | `<title> CFR <part>` | e.g. title 45 part 164 | eCFR API |
| EU, 2015 onward | Regulation/Directive (EU) YYYY/N | CELEX, e.g. `32024R1689` | `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:<celex>` |
| EU, pre-2015 | Directive YYYY/N/EU | CELEX, e.g. `32011L0083` | same |
| UK Act | Name + year | `ukpga/<year>/<number>` | `https://www.legislation.gov.uk/ukpga/<year>/<number>` |
| UK SI | Name + year | `<year>/<number>` | `https://www.legislation.gov.uk/uksi/<year>/<number>` |

Never cite an API query URL, a search-results page, or a feed root as a source. Cite the document.

## Derived dates, in any format

Show the arithmetic and mark it derived. Never present a computed date as one the instrument states:

> **28 September 2026** — entry into force *(derived: 20th day after OJ publication 8 September
> 2026)* · "shall enter into force on the twentieth day following that of its publication in the
> *Official Journal of the European Union*" · [CELEX 32026R1975](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026R1975)
