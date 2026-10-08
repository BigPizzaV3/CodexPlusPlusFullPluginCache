---
name: redline-issues-list
description: "Turn a Word document's tracked changes (redline, markup, blackline) into a structured issues list for lawyers. Use this whenever someone uploads or refers to a redlined .docx and wants the changes reviewed, summarised, risk-assessed, or turned into an issues list or change log -- including casual phrasings like 'review this redline', 'what did they change', 'go through the counterparty's markup', 'summarise the blackline', or 'is there anything nasty in here'. Reads w:ins/w:del revisions straight from the OOXML in document order with real clause numbers, separates out formatting-only edits, picks up Word comments and counter-edits, and builds a change / comments / impact table -- then asks which side of the deal the user is on and re-weights the impact ratings from that position."
---

# Redline Issues List

Produces a lawyer-facing issues list from a redlined `.docx`: every substantive
tracked change, in document order, with a plain description, an analysis of
what it does in practice, and a 1-10 impact score -- then revised once you know
which side of the deal the user is on.

The value here is not in listing the edits (the script does that). It's in the
comments column: what the change actually does given *this document's*
definitions and cross-references. A reviewer who could only get a list of
diffs would open Word and read the redline themselves.

Background you need: a `.docx` is a zip; the body is `word/document.xml`;
tracked insertions are `w:ins` elements, deletions are `w:del` elements whose
text sits in `w:delText`; comments live in `word/comments.xml` and list
numbering in `word/numbering.xml`. The script below handles all of that.

## Extraction

`scripts/extract_changes.py` walks the document once and classifies every
revision. Use it rather than reading `document.xml` yourself: Word tags
formatting-only edits with `*Change` elements that read like content edits;
revisions nest (an `<w:ins>` wrapping a `<w:del>` is a counter-edit across
markup rounds, not a plain deletion); a substitution is routinely split by a
stray space into what looks like two unrelated edits; clause numbers usually
live in `numbering.xml` rather than in the paragraph text; and changes hide in
table cells, footnotes, and deleted paragraph marks.

```bash
python scripts/extract_changes.py redline.docx > changes.json      # full detail
python scripts/extract_changes.py redline.docx --markdown          # starter table
python scripts/extract_changes.py redline.docx --all-parts         # + headers/footers
python scripts/extract_changes.py redline.docx --seq 20-40         # one batch, full context
python scripts/extract_changes.py redline.docx --brief             # compact index
python scripts/extract_changes.py redline.docx --text              # greppable plain text
```

Accepts a `.docx`, an unzipped folder, or a bare `document.xml` (clause numbers
and comments need the full package). Body, footnotes, and endnotes are scanned
by default. Read the script's docstring for its limitations before trusting a
clause number in an unusually numbered document.

**What comes back:** `content_changes` (the table's raw material),
`formatting_changes` (excluded, but see below), `comments`, and
`unanchored_comments`. Each content change carries `sequence` (document order),
`type`, `old_text` / `new_text`, `inserted_then_deleted` for counter-edits,
`location` (heading path plus clause number), `paragraph_context` with the edit
marked inline as `⟦DELETED: …⟧` / `⟦INSERTED: …⟧`, plus author and date.

## Workflow

### 1-2. Extract, with formatting changes set aside

Running the script covers both steps: every revision is picked up, and
formatting-only ones are already separated. Two things to do before moving on:

**Check `summary.formatting_changes_needing_review`.** A `pPrChange` that also
shifted numbering or list level is flagged there. Promoting or demoting a
clause changes what it is subordinate to, and renumbering can silently break
cross-references elsewhere in the document -- that is substantive even though
Word records it as formatting. Pull anything real into the content list.

**Read the `comments` list now, not later.** Word comments in a counterparty
markup usually carry the negotiating rationale ("client can't accept this
without a carve-out"), which is often the most useful thing in the file. They
aren't revisions so they don't get their own table rows, but they should inform
the comments column of the rows they anchor to, and any comment that raises an
issue with no corresponding edit deserves a row of its own.

### 3. The "change" column

**One row per issue, not per revision.** A comparison tool emits a revision
every time the text diverges, so a single negotiated change routinely arrives
as three or four. Twenty-nine revisions in a nine-clause agreement is normally
about twelve issues. Merge revisions that a lawyer would discuss as one point
-- usually meaning they sit in the same clause and pull in the same direction
-- and note the count in the row so nothing looks dropped ("3 revisions").
Keep issues in document order.

Three patterns come up constantly and each collapses to one row:

- **Several edits within one clause.** A definition narrowed by adding "clearly
  marked as confidential", then having "customer lists" struck from its
  examples, is one issue: the definition was narrowed. Describe the net effect,
  not each edit.
- **A replaced table.** When `summary.replaced_tables` is non-zero, or rows
  carry `table_status` of `wholly-inserted` / `wholly-deleted`, the tool tore
  the table down and rebuilt it rather than editing cells. Diff the deleted row
  set against the inserted set and report only the rows that actually differ.
  Four inserted plus three deleted rows usually means one figure changed and
  one row was added.
- **A deleted clause and its renumbering wake.** Removing a clause makes the
  headings below it shift, which surfaces as heading substitutions ("Audit" →
  "Termination", "9." → "8.") scattered across later clauses. That's one issue:
  the clause was deleted and everything after it renumbered. Say so once, and
  flag it as a cross-reference risk -- any provision that referred to the old
  numbers now points somewhere else.

Lead each row with the location so it can be found in Word:

| change |
|---|
| §1 (Definitions): "Confidential Information" narrowed — now requires clear marking at disclosure, and customer lists removed from the examples (3 revisions) |
| §2.1 (Initial Term): term extended from three years to five |
| §2.2 (Renewal): non-renewal notice cut from 90 to 30 days, and a new termination-for-convenience right added on 60 days' notice (2 revisions) |
| §3 (Fees) — fee table: monthly fee raised from $10,000 to $12,500 and a new late payment fee of 1.5% per month added (table rebuilt, 7 revisions) |
| §7: Audit clause deleted in full; clauses 8 and 9 renumbered to 7 and 8 (6 revisions) |

Summarise long insertions rather than reproducing them; the exact wording is in
the JSON. Keep the "so what" out of this column -- that's the next one.

### 4. The "comments" column

This is where the work is. For each row, explain the practical consequence,
grounded in the document rather than in what a clause of that kind usually
says. Get a clean searchable copy of the text first:

```bash
python scripts/extract_changes.py redline.docx --text > plain.txt   # then grep it
```

That prints the document with changes accepted, one paragraph per line prefixed
by its clause number, so a hit tells you where the definition lives. It uses
the same parser as the extraction, so it works on any file the extraction
worked on -- `pandoc -t plain` is fine too but refuses some valid `.docx`
files, and finding that out mid-analysis wastes a step.

For each row, check the things that change the answer:

- **Defined terms.** If the changed text or its surrounding context uses a
  capitalised term, find its actual definition in this document before
  commenting. A one-word change to a heavily cross-referenced term can be the
  highest-impact row in the table precisely because of its reach -- but only
  checking tells you that. Grep the plain text for how many times the term
  appears; a term used forty times is a different proposition from one used
  twice.
- **Cross-references.** "Subject to Section 8" or "as defined in Clause 1.1"
  means you need to read that provision as it now stands. Note that if a
  paragraph-mark insertion or a numbering shift appears in the list, the
  numbers referred to elsewhere in the document may no longer point where the
  drafter intended -- worth checking whether any cross-reference has been
  orphaned.
- **Interaction between changes.** Edits are rarely independent. A deleted
  liability cap plus an expanded indemnity is a different story than either
  alone. Where two rows combine, say so in both.
- **Counter-edits.** For a `counter-edit` row, the negotiating history matters:
  who proposed what, who struck it, and whether the net position is the
  original wording or something new. Name the authors.

Write these as a lawyer would annotate a markup for a colleague: what's
different in practice, what it exposes or protects, what to check. Where a
change plainly favours one party, say which -- but keep the framing neutral
until step 7, since the user's side isn't known yet.

If a check comes up empty (a defined term you can't locate, a cross-reference
to a schedule that isn't in the file), say so in the row rather than
substituting a plausible-sounding generality. "Refers to Schedule 3, not
included in this file" is useful; a confident guess about what Schedule 3 says
is worse than nothing.

### 5. Review before scoring

The script won't miscount rows, so checking the count against the JSON proves
little. The real risk is a wrong or shallow comment. So:

- **Account for every revision.** Since rows group multiple revisions, the row
  count won't match `content_change_count` -- so check that the revisions you
  merged into each row add up to the total. A revision that belongs to no row
  is one you've silently dropped.
- **Re-read the full clause** for every row you're about to score 7 or above,
  using `paragraph_context` or the plain text. High-impact rows are the ones
  where an error costs the most, and a change often reads differently in the
  context of the whole clause than as an isolated diff.
- **Distrust `move` classifications.** Comparison tools tag text as moved when
  it merely also appears elsewhere. If a row reads as a move, confirm the text
  really is the same in both places before describing it as relocated.
- **Sanity-check clause numbers** on a few rows against the rendered document.
  Inserted and deleted paragraphs shift Word's displayed numbering, so a
  computed number is a locator to verify, not a citation:

  ```bash
  soffice --headless --convert-to pdf redline.docx   # LibreOffice, if available
  pdftoppm -jpeg -r 100 redline.pdf page              # then read the images
  ```

  If no converter is available, skip the visual check and say so in the
  output rather than presenting computed numbers as verified.

- **Look at the densest pages** in that render if the markup is heavy. Adjacent
  unrelated edits can group into one row, and one edit a person reads as a
  single substitution can split across rows.
- **Ask what's conspicuously absent.** If the counterparty rewrote the
  indemnity but left the liability cap untouched, or accepted a clause you'd
  expect them to fight, that's worth a line under the table. Silence in a
  redline is information.

### 6. The "impact" column, 1-10

Score the commercial and legal significance of each change on its own terms,
before accounting for the user's side. Consistency matters more than
precision, so use these anchors:

- **9-10** — changes the deal's basic economics or risk allocation: liability
  caps removed or multiplied, indemnity scope reversed, IP ownership moved,
  price or payment mechanics rewritten, exclusivity granted or lost,
  termination-for-convenience added, a condition precedent deleted.
- **7-8** — materially shifts a party's position without redefining the deal:
  a cap resized, an indemnity carve-out added, notice or cure periods that
  change whether a remedy is usable, governing law or forum changed, a defined
  term with wide reach narrowed or broadened, a numbering shift that orphans
  cross-references.
- **4-6** — real but bounded: term length, a specific notice period, an
  assignment or subcontracting consent, reporting and audit obligations, a
  single figure in a fee table.
- **2-3** — tightening rather than substance: clarifying wording, a
  belt-and-braces addition that restates an existing obligation, a
  cross-reference corrected.
- **1** — housekeeping with no legal effect: party name spelling, a date
  correction, defined-term capitalisation made consistent.

Don't compress the range. If a redline of thirty changes produces thirty scores
between 4 and 6, the column isn't doing its job -- most markups contain a
handful of things that matter and a long tail that doesn't, and the point of
the score is to surface that difference. Say so explicitly if the redline
genuinely is all housekeeping.

Present the full table -- change / comments / impact -- as the draft.

### 7. Ask the user's position, then revise

The table so far is deliberately side-agnostic, and impact isn't symmetric: a
higher liability cap is bad for the party bearing the liability and good for
the counterparty; a client focused on IP weights an ownership clause above
payment terms. So ask:

- Which side they're on (buyer/seller, licensor/licensee, borrower/lender,
  landlord/tenant -- whatever fits), unless it's already clear from context.
- Their key concerns, if any.

Ask in plain language and offer the likely options as a short list so the
answer is one tap or one word. Don't stall the draft waiting for it: produce
the neutral table first, then ask.

Then revise: re-score `impact` as risk *to them*, and rewrite comments where
perspective changes the meaning ("favours the Company" becoming concretely good
or bad news). Keep both numbers visible -- a `neutral → adjusted` column, or
the original in brackets -- so the user can see what their position changed,
and reorder or flag the top few rows as the ones to negotiate. If a change is
strictly good for them, say so; an issues list that treats every edit as a
problem is not useful.

## Using the Syntheia workspace

The comments column depends on reading definitions and cross-referenced
clauses as they stand in the full agreement. When the agreement (or the
version it was marked up from) is indexed in the user's Syntheia workspace,
use the Syntheia tools for that instead of grepping the plain text:

- `list-syntheia-documents` to confirm the document is there and resolve its
  `doc_id`; `list-syntheia-documents-by-tag` if the user names a matter,
  party, or jurisdiction rather than a title.
- `get-syntheia-index-json` on that `doc_id`, then one
  `get-syntheia-index-provisions` call for the definitions and every clause
  a changed provision points to. It returns verbatim text with one level of
  cross-references already expanded and a link to each source clause, which
  is exactly what a row's comment should cite.
- `search-syntheia-provisions` when the user asks how the changed clause
  compares to the firm's other agreements: search the workspace for the
  clause as it now reads and report where the redlined position sits against
  the precedents that come back.

Quote provision text from these tools verbatim in the comments column and
keep the source links; never paraphrase a definition you retrieved. If the
document is not in the workspace, fall back to the plain-text extraction
above and say which source you used.

## Large redlines

A 200-change markup won't fit in one readable table or one context window.
Don't truncate silently or drift into shorter comments as the table goes on --
either would leave the user unsure whether the tail was reviewed.

Instead: start with `--markdown` for the index of every change with its
location, tell the user the count, and work in batches of roughly 20-30 with
`--seq 1-25`, `--seq 26-50`, filling comments and scores per batch. Then
consolidate. Two things help keep it manageable:

- **Group conforming changes.** Eight instances of the same defined term being
  replaced throughout is one issue, not eight rows -- one row, noting where it
  recurs.
- **Offer a materiality floor.** For very large markups, ask whether the user
  wants everything or only rows scoring above a threshold, with the rest listed
  in a short appendix. Let them choose rather than deciding for them.

## Output

Default to the table inline in the conversation -- that's where the review
happens. Offer a `.docx` or `.xlsx` export for circulating to the deal team
rather than assuming one is wanted.

One caution worth stating in the output: this is a review aid, not advice. It
flags what changed and what it appears to do, for a lawyer to verify against
the document and the deal.
