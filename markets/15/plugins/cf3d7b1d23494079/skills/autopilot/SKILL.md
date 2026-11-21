---
name: autopilot
description: Run Cituna Autopilot, the weekly plan built only from evidence (Search Console queries, tracked prompts the brand is not named on, verified source gaps). It holds pages inside their 28-day window and proposes enrich, publish, title, pitch, fix or skip; nothing is written until the user picks rows. Use for "run the autopilot", "weekly SEO or AEO plan", "what should we work on this week", "get us cited".
---

# Cituna Autopilot: plan the week from evidence

Read [connection and evidence rules](../../references/connection-and-evidence.md) and
[autopilot rules](../../references/autopilot-rules.md). Writing goes to the sibling
`autopilot-write` skill; logging and the 28-day re-check to `autopilot-measure`.

One rule decides everything: **no evidence, no work.** Evidence is a Search Console query
with impressions, a tracked prompt the brand is not named on, or a verified source gap.
Everything else is enriched into an existing page or skipped. Building the plan costs only
reads (stored Cituna data is free; Search Console reads are metered but cheap). Model
writing happens only for the rows the user picks.

Options the user may add: `dry` (show the plan and stop, no question), `write N` (new pages
this week, default 2), `enrich N` (default 2), a brand or domain.

## 1 · Connect and load last week

1. `whoami`, `list_brands`, `gsc_status`, once per conversation. Use the named brand, the
   only brand, or ask. On Starter, say once that the plan and drafts work but applying needs
   Pro. If Search Console is not connected for the domain, drop the Search Console lanes, say
   the plan covers AI answers and sources only, and point to https://cituna.com/integrations.
2. Read the change log and last plan if they exist (see autopilot-measure): pages whose
   `hold_until` has not passed are held; open rows from last week come back first. If
   re-checks are due, run autopilot-measure first so this week's plan learns from them.

## 2 · Read (about ten calls)

| Call | Arguments | Keep |
| --- | --- | --- |
| `gsc_striking_distance` | `domain`, `days: 28`, `minPosition: 4`, `maxPosition: 60`, `limit: 40` | query, page, position, impressions |
| `gsc_zero_click_pages` | `domain`, `days: 28`, `limit: 20` | `snippet` and `page-two` rows with top queries |
| `gsc_cannibalisation` | `domain`, `days: 28`, `limit: 20` | non-brand queries split across pages |
| `gsc_coverage_gap` | `domain`, `days: 90`, `limit: 50` | silent URLs: page inventory, not work by itself |
| `get_visibility` | `brand` | prompts answered and not cited, per engine |
| `list_citation_sources` | `domain`, `range: "30d"`, `gapsOnly: true`, `limit: 15` | verified gaps, `yourPagesEnginesCite`, `whatEachEngineReads` |
| `list_keywords` | `domain`, `stage: "none"` | `content.existingUrl`: the page that already serves a keyword |
| `list_content_queue` | `domain`, `limit: 5` | `enabled`, `destination`, the `queued` topics |
| `list_articles` | `domain`, `status: "live"` | AutoSEO pages: `url`, `lastSentAt`, `editsNotSent`, `enrich.eligible` |
| `list_gaps` | `domain` | Cituna's own fix list |

Read every `history` block first. `windowTruncated: true` means a young property: deep
positions there mean Google barely knows the site, not that the content is weak. Do not page
through `list_content_queue` articles for the plan; they are large. `list_articles` gives the
AutoSEO pages as short rows, 50 a call; pass `nextCursor` as `before` only when an older page
is a candidate.

## 3 · Candidates

Sort every signal into the lanes in the rules:

- **Near page one:** striking rows at 4 to 20 with 20+ impressions, grouped by page. The
  page's searches are the evidence; what they ask that the page does not answer is the work.
- **Seen, not clicked:** zero-click rows with cause `snippet`. `page-two` rows go to
  enrichment, `ranking` rows are not title work, `branded` rows are skipped.
- **Unserved demand:** striking rows at 20 to 60 with 50+ impressions. If the page Google
  shows fits the intent, enrich it; if it is off-intent and no page fits, a new page.
- **Source only:** for each page in `yourPagesEnginesCite`, its `queries` are tracked prompts.
  Where today's grid shows the brand not cited by the engines in that page's `byEngine`, the
  engines read the page and recommend others.
- **Absent:** prompts answered by 3+ engines with no cell cited and no page in
  `yourPagesEnginesCite`. Find the brand's page for the intent (`list_keywords.existingUrl`,
  the striking and coverage URLs, or one fetch of the sitemap). Found: enrich. None: new page.
- **Verified source gaps:** targets with `outreachStatus` `none` or `planned`, ranked by
  engines citing them, then citations; publisher, directory and roundup roles first.
- **Twins:** cannibalisation rows on non-brand queries.
- **Not evidence:** queued topics whose `source` is a planner or manual idea with no query or
  prompt behind it, queued topics a page already serves, and silent pages with no query or
  prompt pointing at them. List them as skipped and never write more like them. The queued
  topics among them are `skip` rows the user can pick.

## 4 · Gates and cheap confirmation

Apply the gates in the rules in order: 28-day hold, already owned or in flight, twins
first, doorway test, plan and permission, weekly budget. A page's change date comes from the
log, the repository's git history for its source when Claude Code works in it, the page's
`dateModified`, or Cituna's article record (`list_articles.lastSentAt`), in that order.

Only for candidates that pass, confirm cheaply:

- Up to 3 AI candidates: `get_engine_answers` with `brand`, the exact `prompt` and one
  `engine` that answered without the brand. Note who is named and whether the brand's URL is
  in `cited_urls` (source only) or not (absent).
- Each twin: fetch the weaker URL once. If it already redirects to the other, mark it
  resolved and waiting for Search Console.
- Each title candidate: fetch the page once for its live title, H1, description and
  `dateModified`.

## 5 · The weekly plan

Order, as in the founder's loop: twins first, then source-only enrichments (the cheapest AI
fix), enrichments near page one, titles, new pages, with pitches alongside. Cap new pages and
enrichments at the budget; the rest goes to next week with its reason.

Present:

1. One line: brand, data window, Search Console state, plan tier.
2. **This week:** a table of `# | lane | target | evidence (numbers and window) | outcome |
   model writing | re-check on`.
3. **Held:** each page inside its window with its change date and re-check date (group by
   date when there are many).
4. **Skipped:** counts by reason (no evidence, already owned, doorway, planner topics).
5. **Learned since last run:** results and early reads from autopilot-measure, if any. Early
   reads are directions, never evidence.

With a filesystem, save the plan to `~/.cituna/autopilot/<domain>/plan-<YYYY-MM-DD>.md`.
An empty week is a valid result: say so, name the next re-check dates, and stop.

## 6 · Ask once, then apply only what was picked

Unless `dry`, ask one multi-select question (a picker where the host has one, otherwise a
numbered list): which rows to apply now. Then, per picked row:

| Outcome | What happens |
| --- | --- |
| enrich, publish | autopilot-write, one row at a time; the claims ledger and fact check are not optional |
| title | Propose a title and description from the page's own queries (`gsc_query` with a `page` equals filter) and its live title, under the page rules; apply in the repository or tell the user where; log it |
| title, on an AutoSEO page that is due | `enrich_article` with the article `id` from `list_articles` (`enrich.eligible: true`): Cituna writes the title, description and up to two FAQ answers from the page's own queries and updates the live page. It uses one AutoSEO generation; a refusal spends nothing. Log it as a `refresh` with the returned `before` |
| pitch | Draft a short ask: what the cited page covers, the fact that earns the brand a place, the link. Never send it. On the user's word, `set_outreach_status` with `status: "planned"`; `pitched` only after they send it |
| fix | Recommend the owner page by clicks, then position, and what happens to the other (301 or a different intent); a pull request in the repository or written steps; log it |
| queue | `queue_article` with `domain`, `keyword`, `impressions`, `position` only when AutoSEO is `enabled` and the user wants Cituna to write it. Never also draft it here |
| Cituna fix | `set_gap_status` to `doing` or `done` on the user's word |
| skip a queued topic | `skip_queued_topics` with the picked `queued[].id` values; queueing the same text again brings one back |

Every applied change goes into the change log the day it goes live. Never call `run_scan`
or `set_prompts` from the autopilot, and never `enrich_article` for a row the user did not
pick.

## Relevant tools

`whoami`, `list_brands`, `gsc_status`, `gsc_striking_distance`, `gsc_zero_click_pages`,
`gsc_cannibalisation`, `gsc_coverage_gap`, `gsc_query`, `get_visibility`,
`get_engine_answers`, `list_citation_sources`, `list_keywords`, `list_content_queue`,
`list_articles`, `list_gaps`, `queue_article`, `enrich_article`, `skip_queued_topics`,
`set_outreach_status`, `set_gap_status`.
