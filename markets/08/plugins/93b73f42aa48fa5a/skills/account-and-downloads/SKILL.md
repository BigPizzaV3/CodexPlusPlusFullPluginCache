---
name: account-and-downloads
description: Check UGCBuilder account status, inspect generation status, and retrieve existing image or video download links without creating new generations.
---

Use get_account for current credits and generation prices. Report returned values accurately; do not rely on remembered balances or pricing.

For a known prepared request ID, call get_landing_page_request. For a known job ID, use get_generation or display_generation. If the user requests recent outputs without an ID, use list_generations and match the requested product or generation. Ask a concise clarification only if multiple results remain ambiguous.

List results are temporary in-memory jobs, not durable account history. Download links expire after 15 minutes. Jobs and links may disappear after server restarts. Share the exact returned downloadMarkdown or download URLs promptly, along with expiry when supplied. Never invent links or call a paid generation tool to replace expired results without a new user request and the required credit authorization.

Saving to Google Drive or another destination requires its available integration and an authorized destination. Do not claim files were saved because a download link was displayed.
