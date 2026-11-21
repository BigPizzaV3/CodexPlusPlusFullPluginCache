# Script.it public plugin draft — 0.1.1

The listing, review cases, icon, and verified public demo URL are packaged. Portal setup, reviewer access, saved-version tests, scans, and attestations remain; this is not submitted or published.

## Confirmed publication details
Publisher display name: Script.it (selected identity still requires portal verification).
Availability: all available countries (publication.countries is deliberately empty).
Subscriptions and credits are purchased on the Script.it website. This plugin does not offer checkout.
Support email: support@script.it. The support URL uses the public website's Contact us control, which exposes that email; no unverified /support path is used.
Terms and privacy pages were read in a browser and identify Script.it and Bespo Inc.
The PNG reproduces the geometric brand asset at https://script.it/script-logo.svg.

## Connection evidence
https://api.script.it/mcp responds with an OAuth Bearer challenge.
Protected-resource metadata names Script.it and the scopes account:read, sandbox:run, terminal:connect.
Authorization-server metadata advertises S256 PKCE and client_id_metadata_document_supported=true, so the draft selects CIMD. Confirm the portal supports this mode.
The production Script.it connection exposes whoami, start_session, run_command, read_output, and connect_terminal. Fresh authenticated protocol discovery and tool annotation inspection have not been performed against this package.

## Review status
Twelve positive cases and five negative cases are embedded in plugin.json. Direct execution against the saved submission remains NOT RUN. The creator-selected video demonstrates user-visible results for positive cases 1, 2, and 4; this is recorded evidence, not independent verification of raw tool calls or all review cases.
Cases cover inventory discovery, deterministic sandbox execution, file read-back, follow-up calculations, and a reusable workflow. No real customer data or integrations are required.
Server readOnlyHint, openWorldHint, and destructiveHint annotations remain unverified. Inspect and correct them in the MCP server source before submission.
The package declares commerce=false and explains that subscriptions and credits are purchased on the website. Verify the imported declaration in the portal.
Optional dark assets and brand colors are omitted pending creator preference; their absence is not a blocker.

## Selected demo recording
The creator explicitly selected script-it-chatgpt-review-demo.mp4 as-is for this submission on 2026-11-04. No replacement recording is requested.
Duration: 224.47 seconds (3:44). Format: H.264 MP4, 1920 x 1080, silent.
The complete file decoded without reported errors; sampled frames and result screens were inspected.
The recording shows skills and app discovery, Apples/Pears revenue totaling $12, and the follow-up with Bananas totaling $16. Cases 3 and 5 and the negative cases are not shown; no claim is made that the recording demonstrates them.
Public demo page: https://bespo.notion.site/Script-it-for-ChatGPT-Review-Demo-40eec4e58f15819092dad28a4061319f
Verified on 2026-11-04 in a separate cloud browser without signing in: the page displayed the uploaded recording and playback advanced with no video error. The player reported duration 224.466667 seconds, resolution 1920 x 1080, readyState 4, and paused=false. The public page URL is stored in review.demo_recording_url; no temporary media URL is used.
SHA-256: 9900109da4d1346a953ed054cb54c4955241885ca51c843406df147550eecfa7

## Remaining before submission
- Dedicated reviewer account created by the publisher. Email/password sign-in was verified on 2026-11-04 in an independent browser; no additional verification code was requested and the account showed the Free plan. Saved-version review cases still need to be run. Save access details only in the portal’s private reviewer fields.
- Confirm selected publisher identity, commerce declaration, and all-country targeting in the portal.
- Upload this MCP package as a new submission: the existing Script.it 0.1.2 portal draft is a separate CLI-only package named scriptit, and the portal does not support adding an MCP server to an existing skills-only plugin. Preserve that draft. Connect the new saved version through OAuth and run its review cases.
- Resolve required scans and validation issues; the authorized developer completes legal/policy attestations.
- Submit for review. Publication is a separate action after approval.

## Research behind the listing
Make emphasizes creating and managing cloud automations from ChatGPT:
https://help.make.com/official-make-plugin-for-chatgpt-is-now-available
n8n emphasizes building and updating workflows from an AI app:
https://n8n.io/mcp/
Script.it's draft emphasizes inspectable, reusable cloud automations and portability across agents. It does not make comparative superiority claims.

## Listing update — 2026-11-17
Updated the long description and three starter prompts with the publisher’s supplied copy, including messaging, team workspaces, permissions, and agent portability. Connection settings, assets, review cases, and publication settings are unchanged. This package update has not been applied to the live listing.

## Onboarding update — 2026-11-17
Packaged skills/get-started/SKILL.md and its MCP dependency metadata, and selected it through extensions.com.openai.onboardingSkill. Setup opens or reuses a Script.it session, reads the real workspace context, continues an existing task or asks for a task with three concrete choices, then saves and tests the chosen workflow and reports the verified result.

The documented activation is the user running setup after installation; completing OAuth alone is not a guaranteed trigger. Two additional review cases cover setup with and without a chosen task. Package structure, JSON/YAML, dependency references, and preservation checks were validated locally. Installed-plugin setup activation and end-to-end execution remain NOT RUN. Upload this version through the existing submission's update flow, then test both onboarding paths with the reviewer account before publication.

## Automation intent update — 2026-11-17
Added a regular build-automation skill for two equal entry points: continuing a task automatically, and creating a new event-and-action rule. Its metadata includes natural prompts without the product name. The package summary, listing introduction, discovery keywords, and release notes now reflect schedules, events, and monitored changes. The existing starter prompts are retained because they already cover invoice events, a Monday schedule, and ongoing monitoring.

Onboarding hands a chosen task to the regular automation skill. Trigger setup now distinguishes active schedules, registered webhooks awaiting an external sender, processing tests, verified event delivery, and polling-based detection. Runtime commands and supported trigger types must come from live session context. This package does not modify hosted MCP tool descriptions or server behavior.

Two additional positive review cases cover unbranded schedule and incoming-event requests. Two negative cases cover one-off calculation and conceptual explanation. All new behavioral cases are NOT RUN. Local checks cover archive integrity, metadata types, packaged skill references, MCP dependencies, text limits, and preservation of unrelated package content. No installed-plugin recommendation, selection, or end-to-end activation result is claimed.

For discovery evaluation, use fresh conversations with the public plugin available but uninstalled and record whether it is recommended. Separately use fresh conversations with it installed and connected and record selection, tool calls, and successful results. Keep other available tools comparable, use paraphrases, and include the negative cases. Explicit plugin mentions are useful execution checks but do not establish unbranded discovery or selection.

## Full use-case coverage — 2026-11-17
All twelve original listing examples and the integrations paragraph remain intact. The package summary, discovery keywords, and the build-automation skill description now expose the concrete task categories as direct entry points. The skill's display name is Automate a task; its stable folder/name remain build-automation. Schedules and events are optional execution modes rather than prerequisites. One-off operational work and interactive agent creation are explicitly supported by the instructions, subject to live runtime capabilities.

Onboarding now preserves the requested mode and does not turn every job into recurring work. A twelve-row use-case guide maps each original example to the work requested. Three additional review cases cover one-off browser data extraction, one-off enrichment with CRM export, and an internal knowledge agent draft. These cases require the stated reviewer fixtures and have NOT RUN. Package checks validate coverage, references, syntax, length limits, and preservation; they do not establish recommendation or tool-selection rates. Hosted MCP metadata is not changed by this ZIP.
