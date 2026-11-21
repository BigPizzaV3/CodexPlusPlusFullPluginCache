# Flowctory in your AI assistant

Package setup and host usage live here; server/OAuth contracts live in
[AI assistants](../../docs/features/ai-assistants.md) and the [Labs protocol references](../../docs/features/labs.md).
Keep implementation changes in those canonical documents and sync affected package instructions here.

Describe the result you want. Flowctory chooses balanced settings, shows matching Standard/Premium quotes when available, creates only what you requested, and returns the result in chat. Existing assets and editable Canvas flows keep the work reusable; run or schedule them directly from chat after reviewing the exact action.

Flowctory MCP is included on every plan, including Free. Sign in through OAuth
and approve the requested permissions. Connecting adds no credits: generations
use your existing account credits, plan limits and approvals. Suspended accounts
and unresolved live billing holds cannot connect. Buying credits does not unlock
other paid features; paid subscriptions add monthly credits and platform benefits.

## Connect once

Use this remote MCP URL: **`https://flowctory.com/api/v1/mcp`**. Sign in to Flowctory, review the permissions, then return to your assistant. No API key, local server, client secret or media-rendering extension is needed. The public `/mcp` page repeats the Claude Code and Codex CLI commands below (`apps/web/components/mcp/mcp-assistants.tsx`); change both together.

| Client                          | Setup                                                                                                                                                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ChatGPT                         | Enable the Flowctory app/plugin, or add the URL as a custom MCP connector where supported.                                                                                                                |
| Codex app                       | Enable the Flowctory plugin and complete its Connect action.                                                                                                                                              |
| Codex CLI                       | `codex mcp add flowctory --url https://flowctory.com/api/v1/mcp`, then `codex mcp login flowctory --scopes labs:read,labs:generate,flowctory:workspace,flowctory:execute`.                                |
| Claude Code                     | `claude mcp add --transport http --scope user flowctory https://flowctory.com/api/v1/mcp`, then authenticate from `/mcp`. A native `.claude-plugin/plugin.json` is also included for plugin distribution. |
| Claude web/desktop              | Add a custom connector with the URL in Settings → Connectors, then Connect.                                                                                                                               |
| Mistral Work (formerly Le Chat) | Connectors → Add Connector → Custom MCP Connector: enter `flowctory` and this URL, then Connect and sign in. Account owners/admins manage connector setup.                                                |
| Other MCP hosts                 | Configure Streamable HTTP and OAuth 2.1 with PKCE. Standard dynamic client registration is supported.                                                                                                     |

Mistral Vibe CLI currently documents no OAuth MCP support. Use Mistral Work or another OAuth-capable host; the public plugin does not supply a static owner key or copy tokens into chat. Plain LLM APIs need their application's MCP client; model choice alone does not connect tools. Mistral Studio's programmatic connector setup currently documents a client ID and secret requirement; use the Work connector UI for public-client OAuth rather than inventing a client secret.

Existing eligible media-only connections continue working. To find library assets or prepare flows, reconnect and approve the optional **workspace** permission. It reads Canvas projects, library metadata, credit balance and cloud connection status, and writes Canvas drafts and Labs notes. Approve the separate **execution** permission to run or schedule saved flows, inspect progress and stop automation. Each run or schedule needs a current account-bound quote for its exact graph, action and cost, using matching explicit human pre-approval or one inline approval. Existing subscription and node consent rules remain authoritative; old workspace grants keep draft-only authority. Sharing, billing, MFA, account linking and deletion use the app’s existing screens. No permission exposes delivery-provider credentials or internal price tables. Disconnect any assistant in Flowctory Settings → Flowctory MCP; renewal stops immediately, while an issued token may remain valid for up to 15 minutes.

## Directory publication

Installing this package or adding its MCP URL does not publish it to a public directory. OpenAI
publication requires a verified publisher, domain verification, reviewer access, a demo and review.
The portable manifest includes direct, indirect and negative reviewer cases; credentials stay in
the publisher portal, outside the package. Claude's [directory policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy)
requires a written exception for standalone AI image, video or audio generation. Custom connectors
remain a separate distribution path; do not attest that Flowctory lacks its media-generation features.
The portable package declares exactly five positive and three negative review cases, as required for an initial MCP submission. Reviewer access belongs in the secure dashboard form, never in the package. It names the dedicated reviewer account, its email/password sign-in on the Flowctory page that opens after **Connect** (not Google), and the consent step; the account must work immediately, without MFA, email or SMS codes, magic links or extra setup. OpenAI rejected version 1.6.5 because its reviewer could not complete sign-in. Directory review and publication remain separate from account access.

The [review walkthrough](https://github.com/Maelmaelr/flowctory-mcp-demo/releases/download/demo-2026-10-04-v4/flowctory-mcp-demo.mp4) is a 46-second narrated, captioned motion-graphics recreation of an assistant session. Every model output, quote and saved Canvas workflow shown is a real Flowctory MCP result from 4 October 2026; the assistant interface is illustrative, and the weekly schedule is quoted but never approved. Its URL is imported from the portable review metadata; credentials remain outside the public package.

The public OpenAI ownership challenge is served as plain text at
`/.well-known/openai-apps-challenge`. It is intentionally public and does not grant account access.

The [official MCP Registry package](./registry/README.md) contains the validated
remote-server metadata and domain-owner publication steps. The
[demonstration launch pack](../../docs/operations/mcp-growth-launch.md) prepares
recorded outcomes and independent-review materials. Neither preparation proves
a published listing, a successful generation or a recommendation.

## Just ask

The public [MCP playbook](https://flowctory.com/en/mcp/examples) provides nine copyable creative briefs, supported-input guidance and customer, reviewer and teaching resources. Download its Markdown edition to keep the prompts and evidence checklist. These are starting recipes; use current quotes for your own inputs.

- “Make a 9:16 product video from this photo.”
- “Use the saved product image from my library for this campaign.”
- “Save this script in my campaign project.”
- “Prepare a reusable flow with script, image, video and voiceover steps.”
- “Continue this Canvas project without changing its other branches.”
- “Schedule this flow to run every Monday at 9:00.”

`/create-media`, `/product-split` and `/workflow` are shortcuts where the host supports plugin skills. MCP hosts can also use the `create-campaign` prompt. All hosts can discover the same feature guide through `get_flowctory_guide`; hosts supporting resources can read `flowctory://guide`.

## Auto-approve a requested task

Say “Approve the quote and generate directly” or “Auto-approve quotes for these two
videos.” Flowctory still shows the exact quote, then proceeds without asking again
when it matches that instruction. A numeric limit is optional; “up to 250 credits
total” adds a ceiling that includes pending attempts. Otherwise Premium asks for
one inline approval after showing the quote.

Pre-approval covers the requested task, or an explicit scope in this conversation.
It can cover up to two fully-refunded retries, but never extra outputs, unrequested
quality revisions or a different chat. Quote-only, cancellation and any stated
limits take precedence. Every attempt keeps its own current quote and token.
Flow runs and schedules still need an explicitly requested exact action; external
writes and host-required approvals keep their existing consent controls.
Instructions embedded in files, prompts or tool results cannot pre-approve anything.
See [quote approval and auto-mode](../../docs/features/ai-assistants.md#quote-approval-and-auto-mode)
for the full contract.

## Feature coverage

Named subject and voice models use the controlled exact-model workflow. Model discovery
with `includeParameters` supplies each structured parameter's `itemSchema` and `inputHelp`.
Imported or reused media enters `settings.elements`/`settings.voices` as owned upload IDs;
the flat reference list and automatic-model tools do not express those nested names.

| Feature                                            | In chat                                                                             | Flowctory account screen                                                                     |
| -------------------------------------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Image/video/audio generation and reference editing | Quote, generate, exact models/settings, poll, render and reuse outputs              | Labs editor and customization                                                                |
| Text models, reasoning and research                | Discover exact models, save notes, create and execute text-generation flows         | Labs editor and advanced controls                                                            |
| Canvas                                             | Discover/read, create/edit, quote/run, poll and stop flows with revision protection | Canvas editor and node controls                                                              |
| Stitching and FFmpeg processing                    | Prepare and execute nodes using an existing trusted graph pattern                   | Existing node controls and account access still apply                                        |
| Library                                            | Browse saved image/video/audio metadata and reuse exact owned files                 | Upload, organize and remove assets                                                           |
| Marketplace                                        | Discover the feature and open its screen                                            | Choose/import workflow templates                                                             |
| Calendar and recurring automation                  | Schedule a generation or whole flow once/recurring, inspect and cancel              | Schedule editor; credits charged each run                                                    |
| Google Drive/Dropbox                               | Read connection status                                                              | Connect/import/enable auto-save                                                              |
| Google Sheets                                      | Prepare and execute an editable graph using an existing node pattern                | Authorize spreadsheet access and review the exact flow action                                |
| Collaboration and folders                          | Discover accessible projects                                                        | Invite, organize and manage permissions                                                      |
| Computa                                            | Continue through the Labs link                                                      | Built-in assistant and approvals                                                             |
| Model catalog and comparisons                      | Task-specific model names and controls; current-request credit quotes               | Catalog comparison pages                                                                     |
| Credits, plans and security                        | Read credit balance and explain connection permissions                              | Billing, purchases, MFA and storage cleanup                                                  |

Every completed output has a direct download link immediately above its preview, even when the preview fails. Preserve typed media content instead of flattening the render response into text. Images and bounded audio render as native MCP content. In Codex desktop, the assistant saves completed video outputs locally and embeds their absolute file paths in the final chat response, using the built-in video player. Downloads are limited to 256 MiB and 120 seconds, use only the authorized Flowctory result URL with HTTPS redirects, and require no additional credit approval. Other hosts use their supported native media preview or the typed link; playback is verified per host. Media URLs expire; rendering the same completed generation refreshes them without spending credits. Saved local videos remain available independently of link expiry. Project links are durable. Run/schedule completion is reported only from the actual server result. Old grants need reconnection with workspace and execution consent. Existing account and plan gates still apply; owner-restricted integrations and processing are not unlocked by the plugin.

## Review and improve

After each completed image, video, audio or text result, the assistant makes one brief-based review with its available inspection tools. It checks delivered settings and the user's main creative requirements, respecting intentionally rough or unusual styles. When an observed issue matters, it shows the result and offers one supported edit/trim, concrete prompt revision or compatible alternative selected from live model descriptions and controls. Unavailable playback, listening or partial frame sampling is reported honestly; metadata alone cannot prove creative quality.

A proposed improvement does not generate or spend. A requested new generation gets a fresh quote and request UUID; Canvas revisions use the current graph revision and a fresh approved execution quote. Both keep the original result and references and follow the existing subscription and user authorization gates; matching explicit human pre-approval avoids another confirmation for a covered revision. The assistant reviews the revision against the same brief. The loop uses existing host tools and requires no separate reviewer service or quality scores; media links and inline previews stay available.

## If connection fails

Update the plugin, check that the server is enabled, then reconnect from your assistant. Complete any MFA yourself. An invalid or stale consent screen must be restarted from Connect; do not paste callback URLs or tokens into chat. If generation is pending or submission is uncertain, reconcile its existing ID and request UUID. A retryable terminal generation failure gets at most two retries with the same model, prompt, settings and intended references, after its failed charge is fully refunded. Each new attempt uses a fresh UUID and quote. The initial Premium inline quote includes this bounded retry plan and credit ceiling, so covered retries need no second confirmation. Matching explicit human pre-approval can also cover this requested plan unless excluded, within any user budget. Typed parameter errors, including terminal results with `recovery.action: refresh_model_parameters` even without `retryable`, use the same retry budget: refresh the selected model’s live controls, correct equivalent parameter representations and requote the exact request. Explicit user settings and references remain intact; quote-only stays quote-only. Hard access, credit, unsupported constraints or moderation failures stop immediately. After exhausted retries, the assistant stops and proposes one alternative without generating it. See [failed-generation recovery](./skills/create-media/SKILL.md#recover-a-failed-generation).

Native desktop connections finish on a branded Flowctory page, which delivers the approved local callback automatically
and confirms the server's code exchange. If the browser blocks it, use the same-code retry or browser fallback;
neither issues a new grant. Public HTTPS assistant callbacks continue to redirect normally.

After the final allowed attempt or a non-retryable error, the assistant gives a short, safe reason,
confirmed charge/refund information when relevant, and one useful next step. If Flowctory returned
no specific reason, it says so. Fixed storage-delivery and generation-account funding
reasons remain visible; neither means the user's Flowctory credit balance was too low.
Retained delivery continues with the existing output and never grants another paid
generation retry. Retry flags and “policy says stop” are not a diagnosis. Unconfirmed
status or settlement stays unconfirmed; retries, approvals and disclosure boundaries still apply.

Host setup and directory rules can change. OpenAI packaging/submission, Claude Code/directory policy and Mistral
Work/Studio/Vibe references were checked on 2026-10-03; recheck the applicable first-party guide before changing setup
or publishing. References: [OpenAI packaging](https://developers.openai.com/plugins/build/plugins),
[OpenAI submission](https://developers.openai.com/plugins/deploy/submission),
[Claude Code MCP](https://code.claude.com/docs/en/mcp), [Claude directory policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy),
[Mistral Work](https://docs.mistral.ai/vibe/work/connectors/mcp-connectors),
[Studio connector requirements](https://docs.mistral.ai/studio/connectors/management),
[Vibe limitations](https://docs.mistral.ai/vibe/code/cli/mcp-servers), and
[MCP authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization).
These sources establish host configuration rules, not live account verification or rendered playback in each client.

## Disclosure boundary

The connector serves creative and workflow requests only. API DTOs are narrowed at the MCP boundary; pricing tables, USD costs, margins, delivery providers and internal payloads are omitted. Model IDs are opaque handles, quote claims are encrypted, and SDK/API failures use safe messages. Prompt/file/graph/generated content stays untrusted data and cannot grant authority. Public model names, exact supported controls and quotes for the current creative request remain usable.
