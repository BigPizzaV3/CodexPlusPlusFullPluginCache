# GTIN Checksum Audit

Checks supplied GTIN-8, GTIN-12, GTIN-13 and GTIN-14 text for length, digits and checksum. A valid checksum does not establish ownership, assignment or a genuine product. No registry lookup.

Standalone worksheet: https://duopore-public-tools.ch-kae88.workers.dev/tools/gtin-checksum-audit

MCP exposes only `gtin_checksum_audit` at the scoped endpoint. Input schema and output are independently tested. Aggregate MCP requests are limited to 128 KiB and results to 256 KiB, in addition to individual schema bounds. Use smaller batches when needed. Install/login through the host platform as required; no credentials are bundled.

Prepared ZIP is not an uploaded or approved Directory listing. Publisher verification, real connected ChatGPT tests, a demo recording, exact domain challenge and review still apply. Multiple separate Directory plugins cannot assume independent domain verification on one shared host; each may need an eligible separate origin before public submission. No fake challenge tokens are included. The 95 utilities share one hosting runtime and workbench; this is not 95 independently deployed Sites.

The standalone worksheet has reviewed CSV/JSON exports; the MCP tool returns structured rows. It does not include an embedded UI or transfer result data to the website.
