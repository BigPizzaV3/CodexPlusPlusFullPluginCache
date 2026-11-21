# Gotchas & things the tools can't do

Quirks, casing traps, and hard boundaries worth knowing. Skim it before a create/edit task and come
back to it when something behaves unexpectedly. The tool's own schema and `get_workflow` always win
over this file — treat it as a fast lookup, not the source of truth.

## Identifiers

- A Conviu uid is **32 lowercase alphanumerics with at least one digit** — not hex. A `[a-f0-9]{32}`
  check will reject real ids. Copy ids verbatim from tool results; never hand-build one.
- Two id kinds coexist: **UID32** for entities, **UID10 (smallUid)** for formats and org URLs. A
  `formatSmallUid` is always the 10-character `smallUid` from `get_data_source_formats` /
  `detect_feed_format` — never a format's type code or human name.

## Formats

- **Country variants share a name.** Several formats can have the identical display name and differ
  only by country (e.g. multiple "UPgates" entries, Heureka CZ vs SK). Always pick by `country.code`,
  not by name alone, or you'll wire up the wrong country's feed.
- **Custom formats need a mapping.** Custom XML / CSV / XLSX formats require a feed-structure mapping
  that's built in Conviu's visual wizard — the MCP can't assemble that mapping. Prefer a dedicated
  format; use Custom only when the user confirms and is ready to map in the app. Detection returns a
  Custom candidate only as a last-resort fallback.
- `get_data_source_formats` returns the **whole** compatible list (name-ordered) — filter your
  presentation to the 3–5 most relevant; don't dump it all on the user.

## Imports (data sources)

- **`configuration` is composite:** `{ reader, formatter, import }` — not a flat reader config. A URL
  reader MUST carry `url`; sending an empty reader creates a broken import.
- **Verify reachability with the real config.** `get_data_source_readable` must receive the actual
  reader configuration, never an empty one.
- **Edits are deltas.** `update_data_source` fetches the current import and overlays only the fields
  you send, preserving everything else (including custom field mappings). Never resend the full
  configuration to "be safe" — you risk wiping the mapping.

## Exports (data writer jobs)

- **`dataQueryUids` are data-query ids, not import ids.** The export's source is a *data query* — copy
  its `uid` from `list_data_queries`, not the data source's uid. The server validates them and returns
  `availableSources` on a mismatch, so read that if a create/edit is rejected.
- **`add_data_writer_job` takes flat input; the handler builds the nested structure.** Don't try to
  hand-write the composite `configuration` — provide the flat fields the schema lists.
- **Enum casing is inconsistent:** `dataMode` is UPPERCASE (`ALL`, …); `compressionType` is lowercase
  (`none` / `gz` / `zip`); approval is `approved` / `pending`. Follow the schema exactly.
- **Rules can be created and edited, but there is no preview.** `add_data_writer_job_rule` and
  `edit_data_writer_job_rule` exist — call `get_workflow` (`create_export_rule` / `edit_export_rule`)
  first. Nothing shows which items a rule would hit before it runs, so describe the effect plainly
  up front, or create the rule `active: false` and let the user check it in Conviu.
- **A rule's `conditions` name fields differently than a `filter`.** Only `%variable%` and
  `'Full > path'` resolve; a bare field name is stored without complaint and then matches nothing.
  See `references/fql.md`.

## Validation

- **Counts only, no issue list.** The validation tools return `errorCount` / `warningCount` /
  `infoCount` plus status — **never** the individual problems. You cannot say which product broke
  which rule; point the user to the validation detail in the Conviu app for that, and never invent
  error messages.
- **`uid` means different things.** `trigger_data_writer_job_validation` takes the **export's** uid;
  `get_data_writer_job_validation` takes the **validation's** uid (obtained from
  `get_data_writer_job_latest_validation`); `get_data_writer_job_latest_validation` and
  `get_data_writer_job_latest_download_logs` take `dataWriterJobUid`. Mixing them up silently targets
  the wrong thing.
- **A stale validation proves nothing** — check `completedAt` before quoting its numbers.

## Modules

- `get_organization_modules` **requires a locale** in `language-country` form (`cs-cz`, `en-us`) — it
  localises module titles and status messages. `whoami` returns the user's locale; pass it, or they
  get English.
- `status` is lowercase: `error` / `warning` / `success` / `info`.

## Schedules (cron)

- Only a **restricted crontab** is valid: the minute is a single number 0–59 (never `*`/list); the
  other four fields are `*` or comma-lists of numbers — **no ranges, no `*/n` steps**; day-of-week
  0–6. Shortest interval is **once per hour**. Shapes: hourly / daily / weekly / monthly / yearly.
- "Every N minutes" (N < 60) is not expressible — offer an explicit minute list or an hourly run.

## Data queries

- Every import has one data query (with a linked data source). A synthetic "all products" query
  (no linked data source) exists but is hidden by `list_data_queries` — so the list shows only
  real, import-backed sources you can export from.

## Filters (FQL)

- FQL is **not SQL** — see `references/fql.md`. Values are always double-quoted; sets separate with
  `;`; ranges use mixed inclusive/exclusive brackets. Verify field names against real items first — a
  filter over a non-existent field silently matches nothing.

## Working style

- **Read before write; confirm before destructive.** `delete_*`, `trigger_*`, and deactivations act
  on live data — get explicit consent. A `trigger_*` run also consumes processing resources.
- **Don't force reruns to "refresh".** Imports and exports run on their own schedules; trigger a run
  only when the user actually wants one now, not as a reflex.
