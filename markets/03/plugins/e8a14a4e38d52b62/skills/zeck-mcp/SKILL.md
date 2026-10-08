---
name: zeck-mcp
description: Query the authenticated Zeck MCP server for the current user, company memberships, company Zecks, unpublished section outlines, and published markdown content. Use when a user asks who they are in Zeck, which companies or Zecks they can access, wants to find, inspect, summarize, compare, or answer questions about Zeck documents, asks for unpublished section metadata, says to use or re-check Zeck MCP, or needs a Zeck MCP authentication, authorization, scope, or tool-availability failure classified.
---

# Zeck MCP

Use the connected Zeck MCP tools as the authoritative source for live Zeck data. Never substitute remembered identities, memberships, document metadata, or contents for a current tool result.

## Choose the shortest tool path

- Call `get_current_user` for the authenticated user's ID and name.
- Call `get_current_user_companies` to list accessible companies or discover a `companyId`.
- Call `get_company_zecks` with a known `companyId` to discover Zecks and their publication, archive, and unpublished-editability state.
- Call `get_unpublished_zeck_section_list` with 1-10 Zeck IDs for editable unpublished section IDs, titles, and appendix flags. This tool does not return section bodies.
- Call `get_published_zeck_contents` with 1-10 Zeck IDs for published markdown section bodies.

Read [references/tool-contracts.md](references/tool-contracts.md) when exact inputs, output variants, scopes, or failure boundaries matter.

## Resolve ambiguous requests

Build only as much context as the request requires:

1. Identify the user only when identity affects the answer.
2. Discover companies when no company ID or unambiguous company name is available.
3. Discover Zecks when no Zeck ID or unambiguous Zeck selection is available.
4. Prefer published contents for requests to read, summarize, compare, extract, or answer questions about document content.
5. Use unpublished section list only for requests about the current editable outline, section IDs, section titles, or appendix status.

If a name matches multiple companies or Zecks, present the minimal disambiguating details and ask the user to choose. Do not guess.

## Use live results carefully

- Treat user display names, company memberships, Zeck names, timestamps, permissions, and contents as mutable.
- When the user says "check again", rerun the relevant live tool.
- Treat returned UUIDs as opaque identifiers and copy them exactly.
- Respect the 1-10 ID limit on both content tools. Chunk larger requests into groups of at most 10 while preserving the requested order.
- Do not claim unpublished content was retrieved: unpublished lites expose metadata only.
- Treat `canEditUnpublished: false` as inaccessible unpublished content for your user. Zecks can be both published and unpublished. A user might only have access to one, not both.
- Do not infer access to one Zeck from access to another Zeck in the same company.
- Summarize only the documents actually returned. Identify missing or failed Zeck IDs separately.

## Classify failures before suggesting remediation

Separate these states:

- **Tool unavailable:** The Zeck MCP connection or expected tool is not callable in the current environment.
- **Authentication required or invalid:** The server has no usable bearer token or rejects its claims, audience, expiry, or user binding.
- **Insufficient scope:** Authentication succeeded but the token lacks a required MCP scope.
- **Downstream authorization or lookup failure:** An MCP tool ran, but the backing Zeck service rejected or could not find the requested resource.
- **Input validation failure:** An ID is malformed, required input is absent, or a content request has fewer than 1 or more than 10 IDs.

Report the observed state and the exact failing operation. Do not report a prior cached result as if the failed call succeeded. Request reconnection or authorization only when the environment supports that action; otherwise state what capability is missing.

## Produce focused answers

- Lead with the requested identity, list, summary, comparison, or answer.
- Include company or Zeck names when they are useful for a follow-up operation (but a user rarely would want IDs).
- Mention publication, archive, or editability state only when relevant.
- Avoid narrating discovery calls that merely supported the answer.
- State content limitations or partial failures that materially affect confidence.

## Maintain portability

Use MCP tool capabilities rather than assuming a particular connector namespace, CLI, host, or deployment URL. Tool namespaces and endpoints may differ between local development, Codex, and the OpenAI Platform.
