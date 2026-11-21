# Exports — create, edit & rules

An **export** (data writer job) takes one or more of the organization's existing imports and writes
them out in a chosen format for a platform — the same thing Conviu's visual export wizard sets up.
For a real task, call `get_workflow` (`create_export` / `edit_export`) first and follow its
checklist; the steps below explain the same flow in more depth.

**Defaults-first:** derive everything you can, propose the complete configuration in one message,
ask only for what you can't derive (typically just the format, sometimes the source).

## Create an export

1. **Object type** — product or order export? Marketplace / price-comparison feeds (Zboží.cz,
   Heureka, Google, …) are **product** exports — don't ask for those.

2. **Source** — which existing import(s) the export draws from. Call `list_data_queries`
   (organizationUid + object type). Exactly one source → use it, don't ask. Several → if the user's
   message implies one, pick it and confirm; otherwise ask one question listing sources by name. Use
   the chosen entries' `uid` values as `add_data_writer_job`'s **`dataQueryUids`** — copied exactly.
   > These are **data query** uids, not data source (import) uids — a frequent mix-up. If the user
   > has no imports yet, an import must exist first (offer the `create_import` workflow).

3. **Format** — the one thing you must settle; never pick it silently. Call `get_data_source_formats`
   with `forDirection` EXPORT + object type. If the user named a platform, match it yourself and
   confirm — some formats are country-specific and share the same name (e.g. several "UPgates"
   entries), so pick by `country.code`. With no hint, offer the 3–5 most likely by name. Take that
   entry's exact 10-character `smallUid` — never a type code, name, or guess. Prefer a dedicated
   format over a generic **Custom** one (which needs a hand-built template in the visual wizard).

4. **Destination** — default to Conviu internal storage (`writerType` "CONVIU",
   `writerConfiguration` `{}`), which ~98% of exports use: don't ask, and don't call
   `get_data_source_writers`. Only if the user explicitly wants another destination (e.g. FTP) call
   `get_data_source_writers` and collect that writer's keys from its `configurationSchema`
   (FTP: `url`, `path`, `login`, `password`; connector-based: `connectorAccountUid`).

5. **Everything else is a default you propose:** name (e.g. the platform name); schedule (see cron
   rules in `imports.md`); no compression; full export (`dataMode` ALL); standard "block export
   when…" guards. Raise these only if the user asks.

6. **Build & create.** `add_data_writer_job` takes a **flat, friendly input** — you provide
   `dataQueryUids`, `formatSmallUid`, `schedule`, `writerType`, `dataMode`, optional `blockWhen`,
   etc., and the handler assembles the nested configuration. Read the schema; it is authoritative.
   Present the proposal in plain language and call the tool. On success it returns the new export in
   `data.dataWriterJob.uid`. Confirm briefly and offer the next step (e.g. checking the feed after
   its first run).

## Edit an export

1. **Identify** the export and its `dataWriterJobUid` (from page context if the user is on it,
   otherwise `list_data_writer_jobs` + match by name; `get_data_writer_job` for detail).

2. **Change only what was asked.** Typical changes: name; schedule; output format; compression;
   which items are exported (`dataMode`: ALL / ALL_WITH_DELETED / ONLY_INSERTED_UPDATED /
   ONLY_INSERTED_UPDATED_DELETED); the **block-export guards** (`blockWhen.exportIsEmpty` /
   `exportHasFailedImport` / `exportHasSuspiciousItemCount`); the destination; or the source imports.
   - **Format change** — `get_data_source_formats` (EXPORT + object type), exact `smallUid`, watch
     country variants.
   - **Source change** — `list_data_queries`, use the chosen `uid` values as `dataQueryUids`, and
     pass `organizationUid` so the ids can be validated. Omit `dataQueryUids` entirely if the source
     is not changing.
   - **Destination change** — only if asked; `get_data_source_writers`, pass `writerType` +
     changed keys in `writerConfiguration`.

3. **Call `edit_data_writer_job`** with `dataWriterJobUid` and **only the changed fields** (name,
   schedule, formatSmallUid, active, dataMode, compressionType, blockWhen, writerType,
   writerConfiguration, dataQueryUids). The tool fetches the current export and preserves everything
   you omit — don't rebuild the configuration.

4. **Finish** with a short plain-language confirmation.

## Export rules

An **export rule** (data writer job rule) transforms or conditions items within an export — its
`conditions` select which items it applies to, written in **FQL** (see `references/fql.md`).

Available tools: `add_data_writer_job_rule`, `edit_data_writer_job_rule`,
`list_data_writer_job_rules`, `get_data_writer_job_rule`, `clone_data_writer_job_rule`,
`set_data_writer_job_rule_active`, `delete_data_writer_job_rule`.

**Call `get_workflow` first** — `create_export_rule` or `edit_export_rule`. Those playbooks are the
authoritative checklist for which `settings` branch to use, which keys are required, and how to
write the `conditions`; this file only summarises the shape.

Two things trip agents up most often:

- **Where the text goes.** For `editElement`, inserted text lives in `value`
  (`value.rewrite: true`, `value.rewriteType: SIMPLE`, `value.value`, `value.rewriteMode` =
  `PREPEND` / `APPEND` / `REPLACE`), **not** in `transform`. `transform` only post-processes the
  result — case, diacritics, shortening, translation, AI. `PREPEND` and `APPEND` concatenate with no
  separator, so put the space inside `value.value` (`"AKCE "`). Without `value.rewrite: true` the
  rule is created successfully and does nothing.
- **Which element.** `settings` paths (`editElement.path`, `addElement.parent`,
  `hideElement.elements[].path`, `imageEdit.path`) are exact `fields` map keys from
  `get_data_writer_job`. Never invent, translate or shorten one.

`conditions` select which items the rule applies to, in FQL — the field spelling differs from a
`filter`, so read the rule-conditions section of `references/fql.md` before writing one. Pass `""`
to apply a rule to every item; `BULK_EDIT` always takes `""`.

> **There is no preview tool.** A rule takes effect on the export's next run, so state plainly what
> a rule will do before creating it, and offer to check the result afterwards. Creating a rule
> `active: false` first is a safe way to stage one for the user to inspect in Conviu.

## Value defaults & enums (quick reference)

- `writerType` default `CONVIU` (URL/internal export); FTP only on explicit request.
- `dataMode` default `ALL` (uppercase enum).
- `compressionType` — lowercase `none` / `gz` / `zip`, default `none`.
- `blockWhen` default: block when the export is empty and when a source import failed; don't block on
  a merely suspicious item count.
