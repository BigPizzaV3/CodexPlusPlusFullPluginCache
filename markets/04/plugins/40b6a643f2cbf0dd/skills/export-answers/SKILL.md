---
name: export-answers
description: Export the AI answers, sources, competitors, rankings or search queries a Radarkit project tracks as a downloadable CSV or NDJSON file for a date range, with every answer rendered as Markdown. Use when the user wants a spreadsheet, a file, a bulk download, "all answers", or more than a few pages of data.
---

Use this skill when the user asks for a file, a spreadsheet, a full export, or more rows than a couple of pages would return.

1. Call `list_projects` and pick the project (ask if there are several and none was named).
2. Decide the export `type` from the request: `responses` for the answers themselves,
   `sources` for cited pages, `competitors`, `rankings`, or `query_fanout` for the searches the
   models ran. Default to `responses`. Default `format` to `csv`; use `ndjson` only if asked.
3. Set the window. Exports accept up to 365 days. Narrow to specific topics with `topic_ids`
   (from `list_topics`) or specific prompts with `prompt_ids` when the user names them.
4. Call `estimate_export` first. It is free. Tell the user the row count and how many Export
   rows they have left, and ask for a go-ahead before creating the export. Never create an
   export without that confirmation.
5. Call `create_export`. It spends Export rows equal to the row count. Then call `get_export`
   with the returned id every few seconds until `status` is `ready` (usually under a minute).
   `get_export` is free.
6. Hand the user `download_url` and the file name. The link is valid for 30 minutes; the file
   stays for 7 days. Say what the columns are: prompt, topic, model, date, brand mentioned,
   position, sentiment, competitors, sources cited and the answer as Markdown.

Do not page through `list_responses` to build a spreadsheet yourself. Do not create an export
when the estimate says the account lacks Export rows; tell the user how many are needed.
If `get_export` reports `failed`, tell the user the rows were refunded and offer to retry.
