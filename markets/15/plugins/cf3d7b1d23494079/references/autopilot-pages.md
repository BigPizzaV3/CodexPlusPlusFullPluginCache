# Cituna Autopilot page rules, claims ledger and fact check

autopilot-write follows these rules for every new page and enrichment. They apply Google's
helpful-content and scaled-content guidance and what the pages AI engines cite have in
common. The evidence and gates in [autopilot-rules.md](autopilot-rules.md) come first.

## One page per intent

- A count is wording, not an intent: "top 5" and "10 best" are the same page. Write it once,
  with the count the facts support.
- A qualifier is an intent only when the reader needs a different answer ("cheapest" can be;
  "best" and "top" never are).
- A place, engine or brand is an intent only when the page has facts of its own for it (the
  doorway test in the rules).
- An existing page that ranks or is cited for the intent is enriched, not duplicated.

## Page shape

- **Title:** 62 characters or fewer, a whole phrase, carrying the primary query's words. Take
  the shape the winning results share (one web search shows it), with the brand's own count
  and words. A number only when the page delivers it; a year only when its facts are dated.
- **H1** carries the title's promise. A title out of step with its H1 gets rewritten by Google.
- **Meta description:** 70 to 155 characters, the topic plus the specific answer or figure the
  page gives. Never cut off with an ellipsis.
- **Opening:** answer first. Name the topic, state the conclusion and name the top entries in
  the first paragraph.
- **Ranked lists** state how they were chosen (criteria, data source, date, the bar), number
  each entry, and say for each what it is, who it suits, what it costs or where it falls
  short, with its source link. A comparison table where entries share attributes.
- **FAQ** only for real sub-questions searchers or prompts ask, answered in full.
- **Links:** 2 to 4 links to existing pages of the brand where the sentence already points at
  their topic. Only URLs seen in this run (Search Console page rows, the sitemap, the site).
- **Length:** at least 700 words for a new article. Length is a floor, never a target to pad.
- **Author:** a real person who reviews it. If none is known, write `author: TO CONFIRM` and
  say so; never invent a byline.
- **Calls to action:** the brand's own actions (start a trial, run a free check, book a demo),
  right after the opening answer, at the brand's own entry in a list, and at the end. Each
  says what the reader gets. No invented offer, price, discount or urgency.
- **Facts in the HTML:** prices, names and the direct answer must be in the server HTML;
  several AI crawlers run no JavaScript.
- **Not allowed:** question headings on every section, keyword stuffing, word padding, "N+"
  without more than N behind it, copied sentences, and any page whose facts would not differ
  from a sibling's.

## The brand in its own category: named, not only used as a source

When engines read a brand's page and recommend the rivals on it (the source-only lane):

- **Scoped verdict first.** The first takeaway names the brand for a stated need, with the
  facts that make it true: "The best <rival> alternative for <need> is <brand>: <what it
  does>, from <price>." The scope words must hold for every entry on the page: a cheaper plan
  with the same coverage breaks "cheapest".
- **Other picks by need second,** one line each, with their price.
- **Nothing that discounts the brand.** No "weigh this accordingly", "treat our section as a
  pitch" or "we are not neutral": engines repeat those as reasons not to recommend it. An
  ownership line, where the owner wants one, is one plain sentence.
- **No rival crowned.** No "category leader", "the budget pick", "hard to beat". State the
  attribute and the case it fits.
- **The brand described by its work,** not only its price, once or twice a page and in the
  meta description.
- **FAQs in the buyer's words,** answered with the scoped verdict.

## Enrichment blocks

An enrichment adds to a live page; it never rewrites what works. Write one block per change:

```markdown
---
type: enrich
target: https://example.com/learn/page
queries: the searches or prompts it answers
sources: see the ledger
---
## REPLACE: opening
<new answer-first opening>

## ADD AFTER: <existing H2>
<new section>

## REPLACE: title
<new title> / <new meta description>

## LINKS TO ADD
- anchor text -> https://example.com/target, in the sentence "..."
```

## Claims ledger

Keep it beside the draft and add each fact the moment it is collected:

```markdown
| # | claim | value | source | read |
|---|---|---|---|---|
| 1 | Brand Starter price | $49 a month | https://example.com/pricing | 2026-10-21 |
| 2 | Rival entry plan | $95 a month | https://rival.com/pricing (web search "rival pricing") | 2026-10-21 |
| 3 | Engines naming the brand | 2 of 7 | Cituna get_visibility, measured 2026-10-21 | 2026-10-21 |
```

- **value** is exactly what the draft says. **source** is a repository `path:line`, a page of
  the brand, a Cituna tool with its measurement date, or the URL a web search returned with
  its query. Never a URL that was not seen.
- Every entry's existence, price, plan limit, fee, rating, review count, ranking, date, count,
  rival fact and rule gets a row.
- Facts come from the brand's own data first, then one web search per fact. Do not open
  vendor sites one by one: it is slow and adds nothing a dated search result lacks. When two
  sources disagree, use the newer dated one and list the fact for the owner to confirm.
- Never invent an entry, price, rating, quote or date. A fact without a source is left out.

## Mechanical check (before the fact check)

Title length and promise, H1, description length, count in the title equals numbered
entries, method section on a ranked list, word floor for a new article, 2 to 4 real internal
links, author or `TO CONFIRM`, a call to action, no placeholders (TODO, XX, empty links), no
figure without a ledger row, nothing copied. Fix every failure, at most three rounds; a
failure that cannot be fixed honestly (too few real entries, no page to link) is reported.

## Fact check (the editor pass)

Run it as a separate pass that starts from the draft and the ledger, not from memory of
writing them. In Claude Code, give it to a subagent with only the draft, the ledger and this
section. Elsewhere, do a second pass that re-reads each source.

1. Each ledger row against its source: repository line or brand page read again, Cituna data
   re-read, one web search per web row. Holds, contradicted or unconfirmed.
2. Claims with no row are checked like any other. Check every claim on a page with 10 or
   fewer; otherwise at least 15, including every number in the title and the table. Say how
   many were checked.
3. The list is honest: count equals entries, the method says what was done, nothing padded.
4. Rival facts carry a date and agree with a source; the scoped-verdict rules hold.
5. The title's promise is answered in the first paragraph; links read naturally and point at
   pages about what their anchor names.

The editor fixes exact wording itself (an overstatement, a crown, a length, the draft
disagreeing with its own ledger) and lists each change under `## Editor changes (wording
only)` in the ledger. Fact, list and structure problems go back for one revision, then one
re-check of those fixes only. Verdicts:

- **approve:** no fix left, every checked fact sourced; warnings listed for the owner.
- **revise:** exact fixes remain; give each one precisely.
- **reject:** the page should not exist (a doorway, too few real entries, the intent already
  owned by a live page). A rejected draft is reported, never pushed through.
