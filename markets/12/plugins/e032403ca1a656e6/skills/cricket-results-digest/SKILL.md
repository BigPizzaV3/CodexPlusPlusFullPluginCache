---
name: cricket-results-digest
description: Produce a concise roundup of reported completed Cricket Explorer matches when the user asks for a series results digest, a recap of selected matches, or a shareable catch-up. Aggregate only returned match records; do not invent ball-by-ball narratives, standings, player performances, or complete tournament coverage.
---

# Cricket Results Digest

Organize the reported outcomes of a defined set of matches into a readable catch-up.

## Inputs and retrieval

1. Resolve the requested scope: one series, selected matches, or a stated date/team subset of returned rows. Reuse matches already present in model-visible tool results or `widgetState.modelContent.selectedMatch`.
2. For a series, use `structuredContent.selectedSeries.matches`. If only its summary or ID is visible, call `open-cricket-explorer` with `reason`, `initialPanel: "series"`, and the supplied or observed `seriesId`. Widget state alone does not contain that fixture list.
3. For missing individual details with known IDs, call `open-cricket-explorer` with `reason`, `initialPanel: "matches"`, and `matchId`. Check each returned `selectedMatch`; a null selection is an unresolved lookup.
4. If no entity ID is known, open the relevant panel with `reason` and `initialPanel`, then ask the user to select the series or match. Use its next model-visible selection. Do not invent search, date-filter, team-filter, or pagination arguments.
5. Keep `get-cricket-data` and Load more actions in the widget. Do not assume its local lists, filters, or cache are accessible to the model. Label a digest from a first-page list as covering returned rows only, including incomplete pagination when reported.

## Assemble the roundup

1. Deduplicate by match ID and keep a single coherent snapshot per match. Apply requested filters only where the returned fields support them. Disclose gaps or unresolved lookups.
2. Use `matchEnded` to identify records reported as completed, and read their `status` and `matchWinner`. Separate ongoing, upcoming, or contradictory records from confirmed entries in the digest. Treat `state` as derived context rather than proof of a final result.
3. Preserve draws, ties, abandonments, and no-results as stated. A missing winner does not mean a draw, and lower or higher innings totals alone do not establish an outcome or victory margin.
4. Summarize the reported status and relevant innings totals. Preserve innings labels, null scores, and `matchType: "unknown"`. Prefer `runs`, `wickets`, and `overs` over the derived score summary, which can render missing wickets as zero.
5. Sort by trustworthy match dates when useful, without inventing dates or years. If the ordering cannot be established, use a labeled source order.
6. Add only supported aggregate observations. A tally may count reported wins within this returned set; label it that way and keep unknown outcomes separate. Do not call it a series score, standings table, or complete tournament tally without evidence of coverage and the applicable competition rules.

## Deliverable

Provide a compact table of match, format, reported result, and relevant scores, followed by a short shareable recap if requested. Include a brief coverage note and identify omitted or unresolved records.

Describe the digest as a snapshot of CricketData records potentially cached for up to 24 hours. Tool response timestamps do not establish when upstream results were last updated. Keep player contributions, turning points, tactical causes, and ball-by-ball narratives outside the recap unless separately supplied by the user.
