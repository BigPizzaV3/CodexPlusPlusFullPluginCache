# Diagnose — why an import or export isn't working

For "why doesn't my feed work?", a feed that's old / empty / blocked, missing products, or a failed
run. Call `get_workflow` (`diagnose`) first and follow its checklist; the steps below explain the
same investigation in more depth.

**Gather the facts below IN ORDER before concluding anything.** Run each lookup once. Translate
every state, code, log line, and timestamp into plain, everyday words when you report back — don't
show raw dumps.

## 1. Identify the item

If the user is on its page, the uid is in context — use it. Otherwise match by name via
`list_data_sources` (import) or `list_data_writer_jobs` (export). If you can't tell which item — or
whether they mean an import or an export — ask one clarifying question offering the candidates.

## 2. Export diagnosis (data writer job)

a. **`get_data_writer_job`** — check `state`, `active` (an inactive export never runs), `schedule`,
   `lastWrittenAt` (compare with the current date/time: is the last run suspiciously old?), and
   `itemCount` (zero → likely an empty or blocked feed).

b. **`get_data_writer_job_logs`** (a few latest) — read the actual error, and whether a run was
   **blocked** by a "block export when…" guard (empty feed, failed source import, suspicious item
   count).

c. **`get_data_writer_job_latest_validation`** — `errorCount` / `warningCount` reveal problems with
   the feed's content. (`get_data_writer_job_latest_download_logs` shows delivery attempts.)

d. **Check the source imports.** An export depends on the imports feeding it — a failed or stale
   source import is the most common root cause of an empty or outdated export. Use `list_data_queries`
   to see which imports feed it, then `get_data_source` on the suspicious one.

## 3. Import diagnosis (data source)

a. **`get_data_source`** — check `state`, `active`, `schedule`, `lastImportedAt` (suspiciously old?),
   `itemCount` vs `totalItemCount`, and the children states.

b. **`get_data_source_job_logs`** (a few latest) — read the actual error (unreachable feed, wrong
   login, parse failure, …).

c. If the feed looks unreachable, verify with **`get_data_source_readable`** using the source's real
   current configuration.

d. If the complaint is about downstream data ("my export is empty"), see what the import feeds via
   **`get_module_jobs_by_data_source`**.

## 4. Conclude

One plain-language summary: **what is broken, why, and what will fix it.** No log dumps, no state
codes; describe times in words ("the last successful run was yesterday morning"). Don't speculate
beyond the facts you gathered — if the cause is really a product-behaviour question, verify it with
`search_documentation` instead of guessing.

## 5. Offer the fix — and, when a tool can do it, do it (after consent)

- **Reactivate** — `set_data_source_active` / `set_data_writer_job_active`.
- **Fix the feed URL / login** — `update_data_source`.
- **Adjust the schedule** — `update_data_source` / `edit_data_writer_job`.
- **Run it now** — `trigger_data_source` / `trigger_data_writer_job` (a run consumes resources —
  confirm first).
- **Re-validate an export** — `trigger_data_writer_job_validation`.

If no tool fits, give concrete steps and point the user to the right page in the Conviu app (describe
it — don't hardcode a URL).

## Common root causes (pattern → likely cause)

- **Export empty** → a source import failed or returned nothing; or a `blockWhen.exportIsEmpty` guard
  blocked the run.
- **Export old / not updating** → export is inactive, its schedule is wrong, or the source import is stale.
- **Products missing from the feed** → they're filtered out, unapproved (`approval:"pending"`), or the
  source import didn't bring them in. Confirm with `list_items` + an FQL filter.
- **Import failing** → unreachable feed URL, wrong login, or a format/parse mismatch — the job logs
  say which.
