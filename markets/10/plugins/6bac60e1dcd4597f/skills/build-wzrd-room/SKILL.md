---
name: build-wzrd-room
description: Turn a job, conversation, or selected materials into a structured WZRD room using the matching WZRD tool or best available template. Use when the user asks to make, build, or publish something others will open or view, such as a proposal, invoice, quote, pitch deck, client portal, investor update, sales room, menu, showroom, onboarding hub, course, or data room. Also use for rooms built from chats, transcripts, attachments, project files, links, or chosen messages and documents. Do not use for ordinary text answers or summaries that are not intended to become a room.
---

# Build a WZRD Room

Convert a job and its source material into an interactive, source-grounded experience through the WZRD MCP. When the user names a job supported by a WZRD tool, use that tool directly; otherwise find the best matching template. Pass the relevant conversation and notes to WZRD verbatim so the service can build from the complete source rather than from an intermediate summary.

## Establish scope

Interpret “this chat,” “this conversation,” or “everything” as the user-visible conversation plus the documents and links actually available in its context. Do not claim access to hidden history, private reasoning, deleted content, or files that were not supplied or connected.

Support two modes:

- **Include everything:** include the full relevant user-visible conversation and notes verbatim, in order, with speaker labels. Include every accessible document, image, and website the user mentioned or attached, subject to the MCP limits.
- **Choose what to include:** inventory the available topics, message ranges, documents, images, and links in a compact numbered list. Let the user select items, ranges, or rules. Put the selected conversation passages and notes into `context` verbatim rather than summarizing them. If the selection is already clear, proceed without another confirmation.

Before using sensitive, personal, confidential, or third-party material, surface what would enter the room and apply the user's intended access level. Never place credentials, hidden instructions, private chain-of-thought, or internal tool output in a room.

## Prepare the request

Read [references/mcp-workflow.md](references/mcp-workflow.md) before any WZRD MCP call.

1. Express what the room is for in one or two sentences for `prompt`.
2. Choose the creation route. If the requested outcome matches one of the named jobs supported by `tools_make`, select its exact tool id and prepare the user's facts as `answers`. Otherwise derive a concise `templates_search` query from the user's requested outcome. Preserve the user's wording and only add filters such as role, industry, audience, input, or moment when the user explicitly supplied them.
3. Assemble the full selected conversation and notes verbatim for `context`, up to 400,000 characters. Preserve speaker labels, order, wording, decisions, and competing ideas. Do not include hidden system or developer instructions, private reasoning, credentials, or internal tool output.
4. Read every selected local document from disk and encode its bytes as base64. Preserve its filename and MIME type.
5. Classify logos and pictures as `images`; classify supported documents as `files`; put sites the user wants WZRD to read in `websites`.
6. Preflight the item counts, per-item sizes, total file sizes, and serialized request size. Ask the user to narrow the selection only when the request cannot fit safely within the limits.

## Build through WZRD MCP

Use the plugin's WZRD MCP server for room creation. Do not substitute a generic website builder, local mockup, direct private API call, or hand-authored “room” artifact.

When the user explicitly asks for a named outcome supported by `tools_make`, call `tools_make` once with its exact `tool` id, the supplied details as `answers`, and any selected `context`, `files`, `images`, and `websites`. Do not call `templates_search` first for this route.

For other outcomes intended to be sent, shared, presented, or opened by other people, call `templates_search` once with the job in the user's own words. Choose the strongest matching result and pass its `id` to `rooms_create` as `template`. Then call `rooms_create` once with the prepared `prompt`, `context`, `files`, `images`, and `websites`; include `audience` and `moment` only when the user stated them. Do not invoke WZRD for a plain text answer, private analysis, or ordinary document that nobody else will open.

The production MCP exposes `templates_search`, `rooms_create`, and `tools_make` without sign-in, so do not ask the user for credentials merely to find a template or create a room. Do not silently retry a response that may have created a room, because that could create a duplicate.

If `rooms_create` fails before returning a result, report the failure and preserve the prepared request for a deliberate retry. If the tool is unavailable, explain that the WZRD MCP connection must be reloaded; do not present a blueprint as the completed room.

## Quality bar

- Send the selected conversation and notes verbatim in `context`; do not replace them with a summary.
- Keep documents as first-class source files rather than manually paraphrasing their contents.
- Do not invent names, prices, dates, proof points, permissions, integrations, or completed actions.
- Do not include the private `claimUrl` in the room content, public link text, or source context.

## Handoff

After `rooms_create` or `tools_make` returns:

1. Give the user the public room URL from `links.preview` (or `shareUrl` if the server returns that legacy field) and label it **Preview**.
2. Report every entry in `skipped` and the reason WZRD supplied. If `skipped` is empty, say that nothing was skipped.
3. Give the private room URL from `links.edit` (or `claimUrl` if the server returns that legacy field) separately and label it **Edit & claim**. Explain that it opens the editor and lets the user save the room to their WZRD account.

Never combine or confuse Preview with Edit & claim.
