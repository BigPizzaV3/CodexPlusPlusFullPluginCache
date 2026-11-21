---
name: autopilot-write
description: Write one page or enrichment a Cituna Autopilot plan approved, with a claims ledger for every fact and a separate fact-check pass, then publish through the user's repository or CMS, or Cituna's copy of an AutoSEO page, and record it in Cituna. Never writes without evidence or publishes by itself. Use for "write the approved page", "draft the enrichment", "fact-check this draft".
---

# Write, check and publish one approved row

Read [connection and evidence rules](../../references/connection-and-evidence.md),
[autopilot rules](../../references/autopilot-rules.md) and
[page rules](../../references/autopilot-pages.md). Work one row at a time and finish it
before the next.

## 0 · Pick the lane before writing a word

Nothing generated may be thrown away, so the publishing route is chosen first:

- **Write here:** draft with a ledger, fact-check, the user publishes (repository or CMS),
  then `mark_article_published` records the live URL.
- **Queue for AutoSEO:** `queue_article` hands the keyword to Cituna's AutoSEO, which writes
  its own draft. Check `list_content_queue.enabled` first: when AutoSEO is off the topic only
  waits. Never draft here as well; that draft would be discarded.
- **Enrichments are written here.** For a page AutoSEO wrote (it is in `list_articles`), the
  approved blocks go into Cituna's copy with `update_article`, and the page changes when the
  user sends the article from the Cituna app. Keep its edits in Cituna: `enrich_article`
  refuses a page edited on the site since Cituna sent it.
- **A refresh is Cituna's, not a draft:** a `title` row on an AutoSEO page that
  `list_articles` shows with `enrich.eligible: true` goes to `enrich_article`, which writes the
  title, description and up to two FAQ answers from the page's own queries and updates the
  live page. Draft nothing here for it.

## 1 · Re-check the row (free)

The row must carry its evidence: the queries with impressions and position, the prompt with
the engines that answered without the brand, or the source host with its `absent` check. A
request without evidence goes back through the autopilot gates; if none applies, stop and
offer to enrich an existing page or skip.

The plan may be days old, so re-run two gates for this row: the 28-day hold on the target
page, and `list_keywords` (`content.stage`, `content.existingUrl`) for the keyword. Queued,
drafted or published means stop and report the existing work. For an AutoSEO page, read its
row again with `list_articles`: `lastSentAt` for the hold, `enrich.eligible` for a refresh.

## 2 · Brief (reads only)

- **Searches** for an enrichment: `gsc_query` with `domain`, `dimensions: ["query"]`,
  `days: 28`, `rowLimit: 25` and a filter `{dimension: "page", operator: "equals",
  expression: <url>}`. For a new page: `dimensions: ["query", "page"]` with a `query`
  `contains` filter on its core words, to see what Google shows of the brand today.
- **Prompts:** `get_engine_answers` with `brand` and the exact `prompt`, all engines, once:
  who is named, which pages are cited, whether the brand's page is among them. For more on a
  cited host, `list_citation_sources` with `search` set to it.
- **The brand's facts:** in a repository, its facts files (pricing, plans, product docs) with
  `path:line`; otherwise the brand's own pages (fetch) or the user. Never from memory.
- **Link targets:** only URLs seen in this run (Search Console page rows, the coverage list,
  the sitemap).
- **What wins:** one web search for the primary query or prompt. Note the type of the top
  results (list, guide, tool, official page), their count, table, method and FAQ. Read at
  most 3 winners, headings only. Learn the shape; never copy text.
- **The live page** for an enrichment: one fetch for title, H1, description, H2s, opening.
  For an AutoSEO page, `get_article` also gives the stored text the blocks will change.

## 3 · Draft with the ledger

Follow the page rules. A new page gets front matter (`title`, `description`, `slug`,
`author`, `primary_query`, `type`, `evidence`, `cta`). An enrichment is written as blocks
(`REPLACE: opening`, `ADD AFTER: <heading>`, `REPLACE: title`, `LINKS TO ADD`) and leaves
what works alone. A source-only row leads with the scoped verdict.

Add every fact to the claims ledger the moment it is collected. Where drafts live: with a
filesystem, outside the site repository until approved, at
`~/.cituna/autopilot/<domain>/drafts/<slug>.md` beside `<slug>.claims.md`; otherwise in the
conversation, with the ledger as a table under the draft.

Then run the mechanical check from the page rules and fix every failure.

## 4 · Fact check

Run the editor pass from the page rules as a separate pass (in Claude Code, a subagent that
gets only the draft, the ledger and the fact-check section). Exact wording fixes are applied
and listed in the ledger; fact, list and structure fixes go back for one revision and one
re-check. Report the verdict, how many claims were checked, and what the owner must confirm
(the author, any fact listed for confirmation). A rejected draft stops here.

## 5 · Publish, only on the user's go-ahead

- **Repository** (Claude Code or Codex in the brand's site repository): a branch, the
  approved draft (never the ledger) converted into the repository's own content format, a
  build, and a pull request with at most ten pages. Never push to the default branch or merge.
- **CMS without a repository:** hand over the approved draft; the user publishes it.
- **AutoSEO page:** `get_article`, then `update_article` with only the fields the approved
  blocks change (`sections`, `faqs` and `tags` replace whole lists, so send every section to
  keep). The user sends it from the Cituna app; `list_articles` then shows a new
  `lastSentAt` and `editsNotSent: false`.
- **Refresh:** `enrich_article` with the article `id`. `refreshed: true` returns the `before`
  and `after`; `refreshed: false` has a `reason` and spent nothing (not due, edited on the
  site, or the allowance is used up).
- **Once the URL is live** for a page that is not AutoSEO's (the user confirms it, or a fetch
  returns 200):
  `mark_article_published` with `domain`, `keyword` (the primary query, or the board keyword
  it serves), the full `url` and `title`, so Cituna stops suggesting a competing page.
- **Log it** with autopilot-measure, dated the day it went live, with the `before` numbers.

If write access is missing (Starter, or no write consent), stop after the approved draft:
the user publishes, and the recording waits until a Pro connection can make it.

## Relevant tools

`gsc_query`, `get_engine_answers`, `list_citation_sources`, `list_keywords`,
`list_content_queue`, `list_articles`, `get_article`, `queue_article`, `update_article`,
`enrich_article`, `mark_article_published`.
