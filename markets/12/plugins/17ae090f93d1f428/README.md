# Stock Reservation Reconcile

Reconciles supplied on-hand stock against active and released reservations. Flags negative available quantities and reservations for unknown SKUs. Does not update stock or decide order priority.

Standalone worksheet: https://duopore-public-tools.ch-kae88.workers.dev/tools/stock-reservation-reconcile

MCP exposes only `stock_reservation_reconcile` at the scoped endpoint. Input schema and output are independently tested. Aggregate MCP requests are limited to 128 KiB and results to 256 KiB, in addition to individual schema bounds. Use smaller batches when needed. Install/login through the host platform as required; no credentials are bundled.

Prepared ZIP is not an uploaded or approved Directory listing. Publisher verification, real connected ChatGPT tests, a demo recording, exact domain challenge and review still apply. Multiple separate Directory plugins cannot assume independent domain verification on one shared host; each may need an eligible separate origin before public submission. No fake challenge tokens are included. The 95 utilities share one hosting runtime and workbench; this is not 95 independently deployed Sites.

The standalone worksheet has reviewed CSV/JSON exports; the MCP tool returns structured rows. It does not include an embedded UI or transfer result data to the website.
