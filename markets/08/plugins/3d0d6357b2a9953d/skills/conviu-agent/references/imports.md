# Imports — create & edit

An **import** (data source) pulls product or order data into Conviu on a schedule — the same thing
Conviu's visual import wizard sets up. For a real task, call `get_workflow` (`create_import` /
`edit_import`) first and follow its checklist; the steps below explain the same flow in more depth.

**Defaults-first:** derive everything you can from the context and the user's message, propose the
**complete** configuration in one message, and ask only for what you genuinely cannot derive
(usually just the format). Don't ask permission to proceed — propose, then act on agreement.

## Create an import

1. **Object type** — product or order import? Infer from context; ask only if unclear.

2. **Connection (reader)** — how the data is fetched. Call `get_data_source_readers`
   (organizationUid + object type). If the user gave a URL, it's the URL reader — don't ask.
   Otherwise present the methods by name (URL download, FTP/SFTP, Google Sheet, file upload, web
   service, or a marketplace API such as Allegro / Heureka / Kaufland). Build that reader's keys
   from its `configurationSchema`: URL/FTP need the address and whether it's login-protected;
   marketplace/API readers are order-only and need a connected account (`connectorAccountUid`, from
   `list_data_connector_accounts`). To verify the source is reachable, call
   `get_data_source_readable` with the **real** configuration — never an empty one.

3. **Format** — settle it with the user, but let detection do the work; never pick it silently.
   - **With a feed URL:** call `detect_feed_format` first (organizationUid + url + object type; pass
     login/password if the feed is protected).
     - One high-confidence candidate → treat it as the match and just confirm it.
     - Several similar candidates (often the same format differing only by country) → ask one
       question offering those 2–4 by name.
     - Empty / low-confidence → fall back to the format list.
   - **Without a URL** (upload, Google Sheet, marketplace API) or when detection fails: call
     `get_data_source_formats` filtered to the reader (`dataSourceReaderType` + `forDirection` IMPORT
     + object type). If the user named a platform, match it yourself and confirm; watch for
     country-specific formats sharing a name (pick by `country.code`). With no hint, offer the 3–5
     most likely formats by name — never dump the whole list.
   - `formatSmallUid` MUST be the exact 10-character `smallUid` from the detect/format result — never
     a type code, a name, or a guess. Prefer a dedicated format over a generic **Custom** one (Custom
     XML/CSV/XLSX needs a feed-structure mapping best built in Conviu's visual wizard; detection
     returns it only as the fallback when nothing dedicated matches).

4. **Everything else is a default you propose, not a question:**
   - **Name** — propose it (e.g. platform or shop name + what it is).
   - **Schedule** — a sensible default: products roughly once a day, orders hourly. See the cron
     rules below.
   - New products arrive **auto-approved** by default (mention the "for review" option only if the
     user raises quality control). Leave automatic child-source importing on; create the import
     active.

5. **Build & create.** Present the full proposal in plain language and call `create_data_source`.
   The `configuration` is the **composite** `{ reader, formatter, import }`:
   - `reader` — the reader's keys (a URL reader MUST include `url`; never send an empty reader).
   - `formatter` — `{}` for a dedicated format.
   - `import` — import-level settings like `defaultApprovalState` (`approved` / `pending`) and
     `incrementalOutput`.
   Read the tool's schema for exact field names; it is authoritative.

6. **Finish.** `create_data_source` returns the new import in `data.dataSource.uid`. Confirm briefly
   in plain words and offer the logical next step (typically creating a matching export from this
   import). To point at the new import, describe where it is in the Conviu app — don't hardcode a URL.

## Edit an import

1. **Identify** which import and get its `dataSourceUid`. If the user is on the import's page, the
   uid is already in context — use it. Otherwise `list_data_sources` (optionally `get_data_source`
   for detail) and match by name. If unclear, ask.

2. **Change only what the user asked**, nothing else. Typical changes:
   - **Name** or **schedule** (convert to a crontab string and confirm its plain meaning).
   - **Feed URL / login** — these live under the `reader` object, e.g. `{ "url": "https://…/new.xml" }`.
   - **Format** — call `get_data_source_formats` (reader + IMPORT + object type), use the exact
     `smallUid`; prefer a dedicated format.
   - **Auto-approval** — under the `import` object (`defaultApprovalState`).

3. **Call `update_data_source`** with `organizationUid`, `dataSourceUid`, and **only the changed
   fields** (name, schedule, formatSmallUid, active, childrenAutoImport, reader, import). Do NOT
   resend unchanged fields or rebuild the whole configuration — the tool fetches the current import
   and preserves everything you omit, including any custom field mapping.

4. **Finish** with a short plain-language confirmation of what changed.

## Cron schedule rules (strict)

Conviu accepts only a restricted crontab shape — validate before sending:
- The **minute** is a single number 0–59 (never `*`, never a list).
- The other four fields are `*` or a comma-separated list of numbers — **no ranges** (`1-5`),
  **no steps** (`*/10`). The shortest interval is once per hour.
- Allowed shapes: hourly `M * * * *`, daily `M H * * *`, weekly `M H * * D`, monthly `M H Dom * *`,
  yearly `M H Dom Mon *`. Day-of-week is 0–6.
- "Every 10 minutes" is not expressible — offer an explicit minute list or hourly instead.
