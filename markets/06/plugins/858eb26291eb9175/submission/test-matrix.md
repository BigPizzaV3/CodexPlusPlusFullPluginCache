# Media2URL plugin test matrix

This matrix tests the workflow instructions before the connected Media2URL App is available. App-dependent cases must be rerun after App connection with non-production test assets.

| Scenario | Expected plugin behavior | App dependency |
| --- | --- | --- |
| Publish generated HTML | Use the HTML publication workflow when a live page is requested; report only confirmed URL and expiration. | `publish_content` |
| Publish generated SVG | Publish supported generated content after explicit intent; do not claim success before confirmation. | `publish_content` |
| Request direct image URL | Return the confirmed direct media URL for code or embedding. | `get_asset_links` |
| Request share URL | Return the confirmed share page for human viewing. | `get_asset_links` |
| Request Markdown | Format structured confirmed URLs as valid Markdown without swapping URL types. | `get_asset_links` |
| Request CSS URL | Use the direct URL in `url(...)` only when delivery permits it. | `get_asset_links` |
| Request JSON output | Escape the confirmed URL in structured JSON. | `get_asset_links` |
| Update existing published page | Use update, not new publish, when the user asks to preserve the managed URL. | `update_published_content` |
| Replace asset and preserve link | Require immutable asset identity and report the new confirmed version. | `replace_asset` |
| Temporary sharing | Report actual supported expiration and controls; do not invent password or download limits. | `create_temporary_link` |
| Search existing library | Use narrow authorized search and ask the user to disambiguate similar results. | `search_assets` / `list_recent_assets` |
| Private asset handling | Keep private assets within the authorized workspace and do not publish them from a “show” request. | `get_asset` / `get_asset_links` |
| Batch success | Preserve input order and map each confirmed URL to its source filename. | repeated publish or App batch flow |
| Batch partial failure | List successes and failures separately; never label the whole batch successful. | repeated publish or App batch flow |
| Missing authentication | Ask for Media2URL account connection before any write or private-library lookup. | OAuth/App connection |
| Anonymous upload request | Reject before issuing an upload destination, creating storage, or fetching a remote file; direct the user to sign in. | `account_required` |
| Free allowance exhausted | Stop at 90 uploads per month, roughly 3 per day; return the actual quota error and pricing link. | entitlement/quota response |
| Insufficient plan or quota | Explain the structured restriction and do not silently downgrade the request. | entitlement response |
| App unavailable | State that the action could not be confirmed; do not fabricate a URL. | App availability |
| App timeout | Report that confirmation was not received and avoid duplicate claims or unsafe retries. | App timeout/idempotency |
| Link Doctor HTML wrapper | Explain that HTML is a page/viewer response rather than a direct media response. | `diagnose_url` |
| Link Doctor redirect | Report safe redirect facts and final content type only when returned. | `diagnose_url` |
| Unsupported remote content | Do not import or claim support; explain the App’s supported-content result. | `diagnose_url` / import |
| Third-party ownership unclear | Do not copy or import merely because a public URL was pasted. | rights/abuse checks |
| Delete request | Treat deletion as destructive and require explicit intent plus App authorization/confirmation. | `delete_asset` |
| Legacy artifact check | Reject `ai-plugin.json`, obsolete APIs, and deprecated connector files. | local package validation |
| App ID not yet available | Keep `.app.json` absent and document the future insertion path. | local package validation |
