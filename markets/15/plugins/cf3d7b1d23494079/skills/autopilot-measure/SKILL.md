---
name: autopilot-measure
description: Keep Cituna Autopilot's change log and re-check each change after its 28-day window, comparing Search Console clicks with the site's own trend and AI citations with the 30-day record, without claiming causes the data cannot show. Use for "log this change", "did our changes work", "28-day re-check", "what have we learned".
---

# Log every change, re-check it after 28 days

Read [connection and evidence rules](../../references/connection-and-evidence.md) and
[autopilot rules](../../references/autopilot-rules.md), which define the log line. A change
nobody logged cannot be learned from, so log on the day it goes live, not the day it merges.

## Log a change

1. Take the live date (deploy day), the URL, the type and the evidence from the plan row.
   For an AutoSEO page the live date is its new `lastSentAt` in `list_articles`.
2. Read the `before` numbers now, while they are easy to get:
   - The page: `gsc_query` with `domain`, `dimensions: ["page"]`, `startDate` = live date
     minus 28 days, `endDate` = live date minus 1, and a filter `{dimension: "page",
     operator: "equals", expression: <url>}`. Keep clicks, impressions, CTR, position.
   - The site, same window: `gsc_query` with `dimensions: ["date"]`, `rowLimit: 40`; sum the
     clicks and impressions.
   - Each evidence prompt: today's `get_visibility` cells (engines that answered, engines
     naming the brand) and the page's entry in `list_citation_sources.yourPagesEnginesCite`
     (30-day `count` and `byEngine`), if it has one.
   - A pitch: the host's `youOnThisSite` and `outreachStatus` from `list_citation_sources`
     with `search` set to the host.
   - A refresh: the title and description it replaced, from the `before` that
     `enrich_article` returned.
3. Set `hold_until` to the live date plus 30 days and `recheck_on` to the live date plus 33:
   the after-window runs from day 3 to day 30, and Search Console reports about 3 days late.
4. Append the line to the log (with a filesystem,
   `~/.cituna/autopilot/<domain>/changes.jsonl`; otherwise print it in a fenced block titled
   "Cituna change log" and ask the user to keep it for the next run).

## Re-check what is due

Read the log (or ask the user to paste it). Due: `recheck_on` on or before today. Early: at
least 14 days of after-data; report those as "so far", never as a result.

For each due change:

1. **Windows.** Before: the 28 days before the live date. After: day 3 to day 30. Read the
   page and the site for the after window exactly as for `before`. Check the `history` block:
   a window the property does not fully cover is reported as such.
2. **Search Console verdict.**
   - `title`, `description` or `refresh`: if the average position moved more than 3, the change is
     confounded (report it as a ranking move). Otherwise expected clicks = after impressions x
     before CTR.
   - `enrich` or `fix`: expected clicks = before clicks x (site clicks after / site clicks
     before), so a seasonal rise or fall does not count.
   - Win or loss only when actual and expected clicks differ by more than 2 x the square root
     of expected and by at least 5 clicks; otherwise flat. Under 100 impressions in the after
     window: too few impressions to judge, report the movement only.
   - `new-page`: no before. Report the impressions, clicks, position and top queries it
     earned in the after window (`gsc_query` with `dimensions: ["query"]` and the page filter).
3. **AI verdict.** Compare with the `before` snapshot. The 30-day record is the measure: read
   at the re-check, the page's `yourPagesEnginesCite` entry (`count`, `byEngine`, `queries`)
   covers about the after window. Missing before and listed now means engines started reading
   the page; more engines or citations means they read it more. Today's `get_visibility` cells
   for each evidence prompt say whether engines name the brand: absent to cited, and source
   only to named, are the movements that matter, and the reverse counts the same way. Daily
   answers flip, so a one-day difference is noise. With no `before`, the audit nearest before
   the live date (`list_audits`, then `get_audit`) is the fallback; say it is one snapshot.
4. **Pitch.** `list_citation_sources` with `search` set to the host: `absent` turning
   `mentioned` or `linked` means it landed. `set_outreach_status` to `placed` only on the
   user's word.
5. Write the result back into the log line: `read_on`, `after`, `verdict`, `ai`.

## Report

One row per change: change, live date, type, clicks before and after (with the expected
figure), verdict, AI before and after, note. Then:

- **Wins and losses** with their numbers; **flat** and **too early** in one line each.
- **What repeats:** a pattern only when 4 or more decided changes of one type go at least 75%
  one way. Fewer: "not enough cases yet". With a filesystem, keep confirmed patterns in
  `~/.cituna/autopilot/<domain>/lessons.md`; the autopilot reads it before planning.
- **Limits, plainly:** a before-and-after read is not proof of cause. Seasons, Google
  updates, rival moves and engine changes move these numbers too.

Never change a page inside its window to rescue a result, never run a scan to re-measure,
and never report a single day's answer as a trend.

## Relevant tools

`gsc_query`, `get_visibility`, `list_citation_sources`, `list_articles`, `list_audits`,
`get_audit`, `set_outreach_status`.
