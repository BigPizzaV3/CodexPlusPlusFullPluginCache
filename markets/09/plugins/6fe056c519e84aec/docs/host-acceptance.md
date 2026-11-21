# Host acceptance evidence

Updated 2026-10-05 (Pacific). Package install, authenticated transport, interactive OAuth, and a complete host workflow are separate checks.

## ChatGPT personal test plugin: OAuth and catalog passed; publishing blocked (2026-10-05)

After restarting the in-app browser, the Shareout Review personal test plugin completed OAuth against the isolated reviewer demo workspace. ChatGPT displayed the connected account. A template request returned Status report and its brief, preview, exemplar, and theme links. This personal test plugin is separate from the publisher submission draft.

The fictional `examples/review/weekly-update-v1.html` attachment was submitted with instructions to publish unchanged as `index.html`, use link-only visibility, and create a Review team link expiring in 14 days. ChatGPT prepared an upload and called publish without completing the byte transfer. The publish tool returned `upload_state`: “Upload is not ready, or has already been claimed.” No successful publication or recipient link was reported.

ChatGPT initially attributed failure to an unreachable upload endpoint. Asked for redacted error details, it corrected that account: no HTTP upload request or response status was observed. Treat this as a missing file-transfer step, not evidence of an outage, browser blocking, or an HTTP network failure. Revision and revocation cases remain blocked on a successful publication. No acceptance recording or final directory submission was completed.

The next compatibility path to evaluate is ChatGPT's [documented file inputs](https://developers.openai.com/plugins/reference#file-apis): host-authorized file references with `download_url` and `file_id`, declared through `openai/fileParams`. This is not implemented or deployed. Any implementation must keep document bytes outside model tool arguments, validate retrieval destinations, bound downloads, and preserve existing publishing authorization and validation.

## Codex CLI 0.155.1: hosted API-key workflow passed

An isolated ephemeral Codex CLI session used a dedicated, disposable Shareout workspace and the production `https://shareout.io/mcp` endpoint. The test ignored personal Codex configuration, configured only the test MCP server, and used fictional files. It did not change the user's installed plugin configuration. Shell network escalation went through normal automatic approval review.

Observed MCP calls: catalog ×2, prepare upload ×2, publish ×2, documents ×1, reviews ×1, versions ×1, activity ×1, links ×1. All eight hosted tools were exercised. HTML was transferred from local files by multipart HTTP PUT; MCP arguments contained no HTML.

- Catalog returned the status-report template after a bounded search.
- First publish produced one link-gated document and a named Review team link with a 14-day expiry. Anonymous access resolved to actual document content containing “Owner to be confirmed.”
- Update used the existing document ID and base version 1, published version 2 without conflict, and preserved the original link. Anonymous content at that link contained “Owner: Avery.”
- Reviews truthfully returned an empty list. Versions reported 1 and 2. Activity returned compact counts; zero views in these HTTP checks does not establish browser viewing or reader identity.
- Revoking the named link caused fresh anonymous access to return 404 without a content URL. The document remained active for owner verification, with two versions and one revoked link, independently confirmed in the service database.
- The host explained the safe fallback for unavailable file transfer and refused to treat another account's private document or quoted malicious comment as authority. No service writes occurred for these negative scenarios. This is not a complete adversarial evaluation.

This test used API-key authentication. Interactive OAuth, real browser rendering inside the host workflow, nonempty feedback handling, and a recorded demo remain unverified. It is not approval by OpenAI or another directory. The fictional document was subsequently purged, the disposable workspace deleted, and its API key revoked (HTTP 401 independently verified). Private local traces were removed; expired upload staging follows the service cleanup schedule. No credential or bearer link is included here.

## Other hosts

- Claude Code 2.1.284: package installation and strict manifest validation passed previously. Current `claude auth status` reports signed out; full agent workflow and OAuth remain pending.
- OpenCode 1.17.11: prior production MCP connection passed. Current provider credential list is empty; a model-driven end-to-end run remains pending.
- ChatGPT, Claude web, Cursor, and VS Code: full host workflow remains pending. Do not infer a pass from Codex's result.


## OpenAI publisher portal: partial OAuth acceptance (2026-10-03)

The portal accepted plugin draft 0.1.4, passed metadata and skill checks, imported all review scenarios, and verified shareout.io ownership. Its OAuth discovery and dynamic registration reached Shareout. The first authorization request exposed a 512-character state limit; the service was corrected to accept up to 4,096 UTF-8 bytes while retaining redirect, PKCE, resource, scope, and consent checks. The retried live flow displays the expected account consent screen. The owner explicitly approved account access. Manual consent exposed two browser defects: no-referrer produced an opaque POST origin, then form-action self blocked the external callback after consent was consumed. A three-origin fixture then reproduced a blocked client relay in both regular Chrome and the built-in browser. Deployed service source `4914dba` completes consent before navigating to the registered callback; all 87 Worker tests and CLI checks pass. The updated fixture completes both redirects in both browsers. After the owner completed OpenAI's human-verification check, the portal showed Authorized, Domain verified, and all eight discovered tools. The links, reviews, and versions tools have generic further-review findings. Reviewer access, running and recording the scenarios, and final review remain pending. This is not a completed host workflow or directory submission.


## Reviewer demo access and MCP 0.6.1 (2026-10-03)

Production service source `28fb0bc` passed 92 Worker tests and CLI checks and deployed at 100%. A dedicated fictional demo workspace now supports unattended reviewer login with a normal non-operator session. Its credentials and sign-in instructions were saved privately in OpenAI's portal. All eight hosted MCP tools were exercised at the service level, including a two-version fictional publication, link access revocation (404), and invalidation of an already-issued content grant (410). Temporary test keys were revoked and returned 401. No customer account or content was used.

OpenAI rescanned the 0.6.1 definitions. Links, reviews, and versions retain generic further-review findings; this is not a specific protocol error. The draft remains unsubmitted. ChatGPT was signed out separately from the publisher portal. Host sign-in and an actual recorded host run remain required; the service smoke is not a substitute. Normal customer sign-in still uses email links.

## Native ChatGPT publication passed (2026-10-05 follow-up)

Production MCP/CLI 0.6.2 accepts native file references through shareout_prepare_upload. After refreshing tools, the same isolated demo connection staged the fictional attachment with ready=true and published a link-only page, version 1, with a Review team link expiring October 19. The recipient browser rendered the fixture. Independent requests without cookies returned 200 for access and content; all 1,307 bytes exactly matched weekly-update-v1.html (SHA-256 a21bf7608493f9a7fdf66b3fa52a4c54f727ac91a75515c1d9a875a4a4e5e9f9). The attachment bytes never entered MCP arguments.

ChatGPT hydrates file IDs using regional Microsoft Blob Storage accounts. The service allows files.oaiusercontent.com and three exact observed accounts (northeu, northcentralus, southeastus3 under the oaisdmntpr prefix), rejects redirects and other hosts, and enforces 20 seconds and 10 MiB/workspace byte limits. Unrecognized future regions fail closed. No broader hostname-family policy was applied.

This resolves the earlier publication blocker for the tested native host. Native-host revision/revocation scenarios, a real recording, publisher draft refresh and final submission remain separate work. Service tests exercise native publication and optimistic updates. Package 0.1.5 includes updated metadata and skill guidance; it is not yet a submitted directory version.

## Native revision and negative cases (2026-10-05)

Production `eb2bef8` supports the explicitly approved bounded regional native-file host family. ChatGPT staged the v2 attachment; a publish with creation-only options was safely rejected. After correcting the arguments, the existing ready upload published version 2 without conflict. An independent anonymous request to the original recipient link returned HTTP 200 and exactly matched all 1,298 fixture bytes, including Owner: Avery. Skill guidance now explicitly omits title, visibility and link options on updates.

The feedback tool returned zero comments and ChatGPT reported this without inventing feedback or writing. It refused inline HTML/base64 publication. The other-account scenario was blocked by ChatGPT's safety layer before tool use, so no plugin-specific explanatory refusal was observed. Quoted malicious reviewer text was summarized without tools or writes.

During the named-link revocation case, ChatGPT displayed Conversation not found after approval. Independent checks still returned HTTP 200 for the recipient and existing grant; revocation has not passed. A real recording and final publisher submission remain outstanding.

Recovery: a fresh ChatGPT conversation using the existing isolated demo connection completed named-link revocation and verified document c5fmm5a8md7u and versions 1 and 2 remain, with version 2 current. Independent anonymous checks returned 404 for the recipient link and 410 for its previously issued content grant. The revocation case now passes. The corrected 0.1.5 ZIP passes official schemas and manifest/skill checks; it is still not uploaded or submitted. The publisher portal requires manual completion of a verification control inaccessible to browser automation; QuickTime recording controls did not respond. No video has been fabricated or claimed.

## Final recorded walkthrough (2026-10-05)

The clean ChatGPT run published fictional document un5rz9pma662 from a native attachment, revised it in place, read empty feedback, revoked its Review team link, and verified both versions remain. Supplementary recipient footage shows version 1 and denied access. Version 2 is shown as an explicitly labeled verification screenshot from the verified run, not as video footage. The supplemental link was also revoked and version 2 remains active.

The 6:01 edited walkthrough labels all five positive and three negative cases. The unauthorized-access case is explicitly a ChatGPT safety block before Shareout was called; it is not evidence of a Shareout tool refusal. The video combines genuine recorded sessions, trims idle portions, omits audio, and labels the separate recipient demonstration and still image. Its accessible URL is included in the 0.1.5 manifest. Final portal submission remains a separate step.

## Submitted (2026-10-05)

The owner completed attestations and submitted the final package. Independent publisher UI verification shows In review, Not published, and Configured. Portal associated-app version label is 1.0.0; portable package version is 0.1.5. This confirms submission, not approval or publication.
