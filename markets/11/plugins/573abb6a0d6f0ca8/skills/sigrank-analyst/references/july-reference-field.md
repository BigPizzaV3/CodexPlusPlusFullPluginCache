# July 2026 reference field

## What the field is and why it matters

The [historical SignalAF board](https://signalaf.com/board/history) preserves a frozen all-time snapshot generated on **July 31, 2026 at 12:09:09.303 UTC**. The archive manifest records **1,642 profiles: 1,626 seeded public profiles and 16 recorded as real**. These labels describe the recorded source; they do not establish independent verification or current participation.

The roughly 1,600-profile field matters as a **proof-of-concept comparison cohort**. It lets a reader explore how token-flow structures differ across a substantial fixed field, inspect example rankings and compare profiles under a dated implementation. Describe that concrete purpose before its limitations. The count is not a count of paying customers, active users, individually verified humans or a representative sample proving the benchmark's validity.

The live production leaderboard is a separate product population of current public operator records, with its own window and view. The frozen July reference field, the live board, the homepage Four Degrees chart and historical field-analysis articles are distinct sources. Do not combine their populations, medians, ranks or classification versions.

## What this plugin can do today

The packaged instructions explain the archive's identity and significance. The current remote tools do **not** expose a `dataset` or archive-date selector. `get_leaderboard(window="all")`, `get_operator`, `compare_operators` and `get_field_stats` read their current live scopes; none becomes a July archive query just because the user asks for history. Do not invent parameters, a sixth tool, archive rows, archive percentiles or chart values.

When the user asks about the historical website, use available host browsing on `https://signalaf.com/board/history`, inspect the selected filters and comparison state, and cite what is actually visible. If browsing is unavailable, provide the exact link and explain the packaged facts above. Do not present a live MCP response as historical evidence. Never tell the user that the archive was queried when only this guide was read.

## Comparisons and charts

- For an archive-to-archive comparison, retain the snapshot date, archive rank, selected filters and the metrics actually available. Filtered table position is not necessarily the original archive rank.
- Show observed input/output/cache-write/cache-read counts and published metrics where available. Missing values stay unknown; do not fill gaps with zero or reverse-engineer precise counts from rounded ratios.
- Explain how reuse, generation, construction and the fresh-input denominator differ. Use the applicable dated metric/classification definitions; do not silently reclassify old rows under new archetype rules.
- A live-versus-July comparison is contextual unless measurement coverage, window boundaries, cohort and definitions are aligned. It does not establish causal improvement or a person's rank across both fields.
- One frozen all-time snapshot cannot support a historical trajectory, month-by-month trend or movement claim. Do not confuse this archive with the separate retired SIGNA-RATE profile-history endpoint.
- Only make a chart from observed numeric rows the host actually retrieved, with source/date/population labels and explicit missingness. The website's chart is not automatically available as tool output.
- Pasted token counts can support a clearly labeled hypothetical comparison under the manual-preview guide. This plugin does not upload them or publish a new rank.

## Provenance

The app's `data/history/manifest.json` names source commit `4c610df9a78a6c396e0404d6e776919ac11c40c5`, source path `public/data/board-all_time.json`, and SHA-256 `004a91aa30713d384310dbafb64745d375114d727dd7370aa2a3b2396a437ce0`. The dedicated loader is `lib/history/board-2026-07-31.ts`; the packaged guide is documentation, not an implementation of that loader in the remote tools.
