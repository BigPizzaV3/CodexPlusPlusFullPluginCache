---
name: content-and-fixes
description: Use Cituna to prioritize visibility fixes and content opportunities, manage gap statuses, inspect keyword and article queues, queue requested articles, edit or refresh AutoSEO articles, skip queued topics, and record pages already published.
---

# Manage content opportunities and visibility fixes

Read [connection and evidence rules](../../references/connection-and-evidence.md).
For a weekly plan built from evidence, with drafting and 28-day re-checks, use the
`autopilot` skill.

## Prioritize existing work

1. Read `list_gaps` for an explicit scan ID or the domain's latest audit. Preserve
   gap keys, category, impact, effort and existing status.
2. Use `list_keywords` for keyword evidence and article stages. Filter
   `stage: "none"` for keywords with no content yet. The optional Search Console
   join is enabled by default and metered; `includeSearchConsole: false` skips
   that join. It does not make all MCP usage unmetered.
3. Inspect `list_content_queue` before proposing or queueing an article. Match
   the requested `status` (`all`, `live`, `review`, `rejected`, `attention`).
   For a complete article inventory, pass each returned `nextCursor` as `before`
   until there is no next cursor; `limit` accepts 1 to 50. Later pages contain
   articles only, so keep the first page's pipeline context. Disclose partial
   coverage if you stop early. Existing
   queued, drafted or published work should not be duplicated. Distinguish a
   live rank-check result from a period-average GSC position; missing rank-check
   results outside its range are not evidence of zero search visibility. For the
   articles alone, `list_articles` returns one short row per AutoSEO article with its live
   URL and when it was published, last sent to the site, edited and refreshed.
4. Rank actions using actual impressions, observed citation gaps, relevance and
   effort. Keep estimates labeled. Use the search-console and citation-sources
   workflows for supporting evidence without automatically changing state.

## Apply requested actions

| Intent | Tool and inputs | Verification |
| --- | --- | --- |
| Change a fix's status | `set_gap_status` with returned domain, `gapKey`, and `todo` / `doing` / `done` | Read `list_gaps` |
| Queue an article | `queue_article` with domain and exact keyword from `list_keywords`; include supported evidence when available | Read `list_content_queue` and keyword state |
| Record an already-live page | `mark_article_published` with domain, exact keyword, full HTTPS URL, optional title | Read content queue or keyword state |
| Edit an AutoSEO article's text | `get_article` with the `id` from `list_articles`, then `update_article` with only the fields to change (`sections`, `faqs` and `tags` replace whole lists) | Read back with `get_article` |
| Refresh a live AutoSEO article | `enrich_article` with the `id`, only when `list_articles` shows `enrich.eligible: true` | The returned `before` and `after` |
| Remove queued topics | `skip_queued_topics` with ids from `list_content_queue` (`queued[].id`) | Read `list_content_queue`; `notQueued` ids were not open |

Queueing schedules an AutoSEO draft on its next run and may have downstream
effects under the user's existing automation settings. It does not guarantee an
immediate draft or publication. Explain that effect when preparing the change.
Handle duplicate notices as existing work, not a new queued article.

`mark_article_published` records a page that is already live; it does not publish
or edit a CMS page. Use it only when the user has supplied/confirmed the actual
published page or the publication has otherwise been verified. It should not
be called merely because text was drafted in chat.

`update_article` changes Cituna's stored copy only: a page already on the site
changes when the user sends the article again from the Cituna app. `enrich_article`
does change the live page (its title, description and up to two FAQ answers) and
uses one AutoSEO generation; call it only on a clear instruction for that article.
A refusal returns `refreshed: false` with a `reason` and spends nothing.

Do not invent CMS publishing, billing or automation-setting tools. For actions
absent from the current MCP tool list, explain the limitation and link to Cituna
for the specific app step.

## Relevant tools

`list_gaps`, `set_gap_status`, `list_keywords`, `list_content_queue`,
`list_articles`, `get_article`, `queue_article`, `mark_article_published`,
`update_article`, `enrich_article`, `skip_queued_topics`.
