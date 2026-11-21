---
name: compare-audiences
description: Compare how different groups answered an Attest Measure question, such as age groups, saved audience segments, or markets like the UK and US.
---

Use this when the user wants results split by group: two or more audiences, saved segments, demographic bands, or markets.

1. Find the study and read its structure to find the question and the surveys it ran in.
2. Work out how each group is defined:
   - A group the user names may be one of their saved segments. Check those first and use a matching segment's own filter as it is.
   - Build a filter yourself only when no saved segment matches, using the fields and values the connection reports as valid for that market.
   - Markets are usually separate surveys rather than filters. Compare them by reading each market's survey.
3. Read results once per group, one survey at a time, each with that group's filter. Never read the whole sample once and estimate the groups from it. If two groups come back with identical figures, check that each request carried its own group's filter before reporting. Identical results can be genuine, but they're also how a dropped filter shows up.
4. When comparing markets, compare like with like. A question or option hidden from one market means it wasn't shown there, not that nobody chose it.
5. Present the groups side by side for each answer, with every group's base, and point out the biggest differences. Treat any group below the reliable base the results flag as indicative only, and say when a difference is too small to read much into.

If the user names a group you can't define from their segments or the available fields, say so rather than substituting a near match.
