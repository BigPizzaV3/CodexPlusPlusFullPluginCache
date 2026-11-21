---
name: google-serp-research
description: Compare current Google organic results, examine search intent, or find a supplied domain in a bounded result set with HasData. Use when the user asks for SEO research backed by live SERPs.
---

# Compare current Google results

Read `../hasdata-research/SKILL.md` and `../hasdata-research/references/tool-contract.md` before tool calls. Their scope, security and credit limits apply.

1. Identify the supplied keywords and requested location. For up to three queries, fetch one page per query. For larger keyword lists, agree a bounded request count before starting. Use Light for organic research, or the full SERP tool for explicitly requested device settings or additional features. Do not switch APIs after a paid response merely to make the output look fuller.
2. Preserve exact query wording. Set a canonical location only if supplied or unambiguous. Leave other search options unset unless requested. Omit `start` on the first page.
3. Check the response envelope. Record query, requested location, applied location if returned, tool used, observation time, request ID and organic count. Read returned position values rather than renumbering results into a different rank.
4. If checking a domain, parse each URL's hostname. Match the exact hostname or its subdomains only, not strings found in the path or an unrelated hostname. Distinguish domain matches from an exact requested page URL. If absent, say it was not found in the fetched results, not that it has no ranking anywhere.
5. For comparison, normalize URLs by removing only fragments and obvious tracking parameters. Preserve meaningful path and query differences. Show shared ranking pages across queries and separate different apparent intents. Similar results suggest overlap but do not prove cannibalization or that pages should be merged.
6. Return the relevant observed URLs, positions and brief snippet-based intent summary. If recommending content changes, label them as research hypotheses. Reading owned pages requires additional calls within the agreed budget. Snippets alone cannot establish a content gap or justify rewriting an article.

If the user provides an earlier snapshot, compare compatible observations using the same query, location and API/device context. Without an earlier snapshot, do not invent movement or a ranking trend. Report incomplete/failed results separately from successful observations.
