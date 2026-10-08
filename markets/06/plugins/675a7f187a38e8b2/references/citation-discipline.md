# Citation discipline

**This file governs every output of this plugin. Read it before producing any finding, brief, or
calendar entry. Within this plugin, this file resolves conflicting citation guidance; user and host instructions take precedence.**

The core rule: **every compliance statement must be traceable to a source link that was fetched in
this session. Nothing is produced from recall.**

In a compliance context, a wrong effective date or an invented obligation is a real harm to whoever
relies on it, and a claim with no citation is indistinguishable from a fabricated one. So an uncited
claim is not "a finding with a missing field" — it is not a finding at all.

---

## 1. The provenance record

Every finding carries this block. A finding whose block is incomplete is **not reportable**: move it
to Coverage gaps or Unverified leads. There is no "probably correct" pass-through, and no exception
for findings that seem obvious or well known.

Historical author example, not reverified by the compatibility review. Fetch and check the
document before reusing any claim or quote:

```yaml
provenance:
  source_url: https://www.federalregister.gov/documents/2026/08/03/2026-15717/ventilation-plan-approval-criteria
  official_id: "2026-15717"
  source_tier: primary
  publisher: "Federal Register (Labor Department)"
  retrieved_on: 2026-09-09
  supporting_quote: "All new comments must be received or postmarked by 11:59 p.m. Eastern Time on September 30, 2026."
```

Note that the quote is the document's own sentence, not a tidied version of it. "Comments close
30 September 2026" would be a paraphrase, and a paraphrase is not a quote — it drops the time and
the time zone, both of which matter on a filing deadline.

| Field | Requirement |
|---|---|
| `source_url` | Must resolve, and must point at the document itself — not a search page, homepage, or feed root. |
| `official_id` | The publisher's own identifier: Federal Register document number, CELEX number, UK SI `year/number`, ELI, docket number. If the publisher issues no identifier, write `none` and explain in one clause. |
| `source_tier` | `primary` (official publisher of the instrument) / `regulator` (the regulator's own site, guidance, or press release) / `secondary` (anything else). |
| `publisher` | The body that published this document. |
| `retrieved_on` | The date you actually fetched it, in ISO form. Not the document's date. |
| `supporting_quote` | Verbatim text from the fetched document that establishes the claim. Quote, don't paraphrase. Ellipses to trim are fine; changing words is not. |

### Verbatim means verbatim

`supporting_quote` must appear in the fetched document character-for-character within the quoted
span. If you cannot reproduce it exactly, you did not fetch the document — fetch it, or move the
item to Coverage gaps. Do not reconstruct a quote from memory of what such a document usually says.

---

## 2. Source each claim, not each item

One link at the end of a paragraph is not provenance. These fields are what people act on, and they
are where recall drifts most, so **each one needs its own citation and its own supporting quote**:

- effective dates, entry-into-force dates, applies-from dates, transition milestones
- consultation and comment deadlines
- scope thresholds — headcount, revenue, data volume, product class, turnover
- penalty and liability exposure
- who the obligation binds

Two consequences worth internalising:

- **A single document may not source all of them.** A proposed rule states its comment deadline but
  usually not its final effective date. Cite each field to the document that actually establishes
  it, and if no document establishes it, say so rather than filling it in.
- **An unsourced date is worse than no date.** Omit it and note the omission. "Effective date not
  yet published" is useful and honest. A guessed date gets diarised, relied on, and missed.

---

## 3. Operating rules

1. **No link, no claim.** If it was not fetched in this session, it is not stated as fact. Anything
   you merely suspect exists goes under `Unverified leads`, clearly separated from findings, and
   never enters a brief, a register, or the calendar.
2. **Cite the document, not the search.** A results page, a homepage, or an RSS feed root is not an
   acceptable citation for a finding. Follow through to the instrument and cite that.
3. **Label lifecycle stage** — `proposed` / `consultation` / `adopted` / `in force` / `applies from`
   — each backed by the source that establishes it. Never carry a proposal's date forward as if it
   were adopted, and never describe a proposal in the language of binding obligation.
4. **Report coverage gaps; never bridge them.** A source that fails to fetch produces a named gap:
   "EU Have Your Say — fetch failed, 2026-09-09, consultations may be missing from this scan." The
   reader must be able to see what was *not* looked at. Never fill silence with recall.
5. **Secondary sources are leads, never conclusions.** Law-firm commentary, trade press, and
   newsletters may point you at something real, but the finding only becomes reportable once you
   reach the primary instrument and cite that. Until then it stays an unverified lead, labelled with
   where the lead came from.
6. **"Made" is not "in force."** For UK statutory instruments, EU acts with deferred application,
   and US rules with delayed effective dates, the publication date and the date obligations bite are
   different. Cite the commencement or application provision specifically.
7. **The disclaimer travels with the output.** Every brief, memo, alert, and calendar states that it
   is regulatory intelligence and not legal advice. Not just the README.

---

## 4. Mandatory self-check before returning anything

Walk the findings and verify each one. This is not optional and not a formality:

- [ ] `source_url` present, and fetched in this session
- [ ] `source_url` points at the document, not a search or index page
- [ ] `official_id` present (or explicitly `none` with a reason)
- [ ] `supporting_quote` present and verbatim
- [ ] every date, deadline, threshold, and penalty asserted anywhere in the output traces to a quote
- [ ] lifecycle stage matches what the cited source actually says
- [ ] no secondary-tier item is presented as a finding

Move every failure to Coverage gaps or Unverified leads. Then **state the tally in the output**:

```
Provenance: 14 findings, 14 fully sourced. 2 coverage gaps. 3 unverified leads.
```

State it even when nothing failed. The reader needs to see that the gate ran, not assume it did.

---

## 5. What good and bad look like

**Illustrative format, requiring fresh verification.** Every acted-on field carries its own quote, and the missing field is named as
missing rather than estimated:

> **EU — Commission Implementing Regulation (EU) 2026/1975** · `adopted` · confidence `high`
> Exempts certain fluorinated greenhouse gases in compressed-air drying equipment.
> - Adopted 8 September 2026 — "Done at Brussels, 8 September 2026." [CELEX 32026R1975](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026R1975) (EUR-Lex, primary, retrieved 2026-09-09)
> - Entry into force: "shall enter into force on the twentieth day following that of its publication in the *Official Journal of the European Union*." Publication 8 September 2026 → 28 September 2026. *Derived from the quoted provision and the publication date; not stated as a date in the act.*
> - Applies-from date: not separately specified in the act.

Note what that last bullet does: the arithmetic is shown, its basis is quoted, and it is flagged as
derived rather than dressed up as a date the act contains.

**Not reportable — this is the failure mode to refuse.** No link, no identifier, no quote, and a
confident date that came from nowhere:

> ~~The EU is expected to tighten f-gas rules in late 2026, with compliance required by Q1 2027.~~

Correct handling: either fetch the instrument and cite it, or write
`Unverified lead: possible f-gas amendment — no primary source located, 2026-09-09.`

---

## 6. When the user pushes for an unsourced answer

Users will sometimes ask for a best guess, a "rough sense," or a date "just approximately." Give
what you can defend and be plain about the rest:

- Report what is sourced.
- Name the gap and say what it would take to close it — which register, feed, or regulator page
  would carry the answer.
- Offer the shape of the answer without inventing its content: "final rules from this agency have
  typically taken 6–18 months after the comment close, but no date is published for this one" is
  fine **only** if you are not asserting a specific date and you label it as pattern, not fact.

Never resolve pressure for specificity by supplying an uncited date, threshold, or penalty. Saying
"I don't have a sourced answer for that" is a correct and complete response.
