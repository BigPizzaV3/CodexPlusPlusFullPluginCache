---
name: competitor-benchmark
description: Benchmark a site's AI search readiness against named competitors with Glippy, find the categories where it trails, and rank the gaps worth closing first.
---

# Benchmarking against competitors

Use this when the user wants to know how their site compares with competitors for AI search, or asks "who is doing GEO best in my market".

## Get the list of sites

- Ask the user for their own domain and the competitors to include. Use only domains the user named. If they ask you to suggest competitors, you may propose some, but confirm the list before running anything.
- `compare_domains` takes 2 to 8 domains. If the user names more, ask which 8 matter most.
- Decide each homepage's page type before the call and pass it as `page_type`, as a map when the sites differ (for example a one-page local business is "service"). A re-run with another page type is a new analysis.

## Run one comparison

Call `compare_domains` once with all the sites. Do not also run `analyze_domain` on each site unless the user asks for one site's full report. If a site could not be analysed (robots.txt, unreachable, rate limit), say so and benchmark the rest. Do not retry.

## Read the result

Lead with the ranking: the user's site position, its score, and the leader's score. Then:

1. **Gaps.** Categories where the user's site trails the best competitor by about 15 points or more. These are where competitors are visibly ahead.
2. **Strengths.** Categories where the user's site leads. Tell them to keep these.
3. **Shared weaknesses.** Categories where every site scores low. Fixing these is a chance to lead the whole market, not just catch up.

## Rank what to do first

Order the gaps by what AI answer engines depend on most: Machine Readability first (it includes whether robots.txt lets AI crawlers in at all), then Structured Data & Schema, Entity & Authority and Citability & Answer-Readiness, then the rest. Within that, prefer fixes that are cheap to ship, such as adding JSON-LD or meta tags, over large content projects. Give three to five steps, each tied to a category and a competitor that does it better.

Offer to draft the fixes (see the draft-fixes skill) or to run the full report on the user's own site.

## Limits to state

- Each site is judged on its homepage only, so this compares homepages, not whole sites.
- Scores measure readiness signals on the page. They do not measure how often AI engines actually cite each site.
