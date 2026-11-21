---
name: explore-oracle-hdi
description: Show the Oracle Health Data Intelligence overview once per conversation, then answer HDI product and getting-started questions using web sources. Use for Oracle HDI overview and public product questions, not for patient analysis or live data queries.
---

# Explore Oracle HDI

## Choose the response for this turn

Check the current conversation before acting. The overview is an introduction, not the answer to every message.

- On the first HDI interaction, present the overview once using the existing display tool or bundled fallback below. If the host has already displayed it when starting the chat, do not display it again.
- Once the conversation already contains the hosted widget, bundled overview image, or interactive HTML link, answer subsequent questions using the web-search workflow below. Do not call `explain_app`, embed the image, attach the HTML, or repeat the page link as part of an ordinary follow-up answer. The same applies when the earlier overview attempt failed and that limitation was already explained.
- Reopen the page only when the user explicitly asks to show/open the overview again or to test the hosted page. A question about a capability, access, or getting started is not a request to reopen it.
- A new conversation starts a new introduction. Use this conversation's visible history; do not write a shared flag or infer state from another chat. Explicit user instructions, including a request for text only, take precedence.

## Present the initial overview

For the first HDI interaction or an explicit request to reopen the page:

1. When the existing `oracle-hdi-marketing` MCP connection is available, call its existing `explain_app` tool once with `{}`. Its UI resource is `ui://widget/oracle-health-population-health.html`. Do not invent parameters or add a tool. Let the host display that resource; do not also attach the bundled page when the widget is displayed.
2. If that connection is unavailable, the call fails, or the client cannot display the widget, use the bundled [overview screenshot](assets/overview.png) and self-contained [interactive page](assets/overview.html). Resolve both paths relative to this loaded `SKILL.md` and confirm they exist. Embed the screenshot inline first, followed by a link labeled **Open interactive overview**. In Codex desktop use actual absolute paths; where attachments are required, use the URLs returned by the client. Do not emit relative `assets/` paths or substitute a tool-only image preview for the final inline image.
3. Keep the introduction brief. If neither visual output can be shown, explain the specific limitation and provide a short text overview from [capabilities reference](references/capabilities.md). Do not retry the page automatically on each later message. If the initial message also asks a substantive question, answer that question using web search after the introduction.

For deployment or hosted-connection questions, read the [connection guide](references/connection.md). A successful tool result alone does not prove that the widget rendered, and a bundled fallback is not a hosted display. Packaging the HTML does not deploy it to the server.

## Answer follow-up questions with web search

For a substantive follow-up question about HDI, its capabilities, or getting started:

1. Use the host's existing web-search capability to research the user's actual question. Prefer official Oracle product pages and documentation, and open the relevant sources before answering. Use public product terms in queries; do not send patient data, credentials, or confidential customer details to web search.
2. Give a direct, concise text answer with links to the sources supporting factual claims. Use the bundled [capabilities reference](references/capabilities.md) for what the marketing page says. For intended-use, eligibility, or legal questions, read the relevant section of the [intended-use statement](references/ifu.md), preserving its wording when reproducing it. Do not infer customer-specific access, enabled features, or availability from general public pages.
3. Do not display the overview again. Do not use `explain_app` as a research tool: it returns the same static page. If web search is disabled or unavailable, say so briefly and answer only what the supplied references support, without inventing sources or replaying the page.

Brief acknowledgements and requests to rephrase an earlier answer do not require a new search. The server also advertises `contact_oracle`, but an overview or product question does not authorize submitting a contact request. This skill provides public product information; it does not execute, simulate, or promise clinical or data workflows. No customer account or data access is provisioned by viewing the page.

## Contact and access

Share the published contact and demo destinations recorded in the reference. Both currently lead to the Oracle Health Population Health website; do not describe opening the link as submitting a request. Keep the reference and browser page configuration aligned when these details change.

Availability depends on enabled tools, entitlements, data rights, access controls, and applicable approvals. Installing this information skill does not provision an HDI account or grant data access.

## Sources

- [Capabilities reference](references/capabilities.md), describing the bundled overview.
- [intended-use statement](references/ifu.md).
- [Current page screenshot](assets/overview.png).
