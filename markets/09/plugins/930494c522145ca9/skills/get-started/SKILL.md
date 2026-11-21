---
name: aya-web-extract-guide
description: Use Aya Web Extract to turn permitted public HTML listing pages into source-linked datasets, filter them, and export them.
---

# Aya Web Extract

Use this plugin when the user supplies a public web page and asks to collect products, jobs, directory entries, or similar repeated records. Ask for the public URL when missing. Never invent source data or claim to have extracted fields that are blank.

1. Call `extract_url` with the URL, a concise request naming record type and fields, and bounded `max_pages` and `max_records` values. The service supports at most 10 pages and 250 records.
2. Call `get_job_status` until the job is completed or failed. Report an error plainly if it fails.
3. Call `get_dataset` or `query_dataset` to inspect actual records. Read additional pages by increasing `offset` when needed.
4. Cite each record's `source_url` or item `url` when presenting results. Use `export_dataset` for CSV or JSON when the user asks for an export.

The service handles public HTML pages and checks robots.txt. It cannot access sign-in pages, paywalls, CAPTCHAs, or JavaScript-only listings. Missing values stay blank. Datasets expire after 7 days and anyone with a dataset link can access it, so do not submit private or sensitive URLs.
