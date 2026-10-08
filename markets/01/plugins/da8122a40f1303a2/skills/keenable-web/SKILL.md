---
name: keenable-web
description: "Search and read the web with Keenable. Use for current information, source discovery, and extracting clean content from known URLs. Keyless by default."
---

# Keenable Web Research

Use the Keenable MCP tools provided by this plugin to retrieve current,
source-grounded web information. The tools are keyless by default — no
authentication is needed to call them.

## Choose the right tool

- `search_web_pages`: Find relevant sources when the user needs current or
  citable information from the web.
- `fetch_page_content`: Read the full, clean markdown content of a known URL.

## Workflow

1. Clarify scope, freshness, and output format when the request is ambiguous.
2. Use `search_web_pages` for focused questions and source discovery.
3. Use `fetch_page_content` when the user supplies a URL, or to read a promising
   result from search in full before relying on it.
4. Synthesize the results rather than pasting raw tool output. Preserve source
   URLs and cite factual claims.

## Search guidance

- Write concise, specific queries instead of long instructions.
- Split multi-part questions into distinct searches when that improves coverage.
- For relative dates such as "last week," calculate exact dates from today.
- Prefer primary and authoritative sources for factual or technical claims.
- Cross-check consequential claims against more than one independent source.
- Distinguish sourced facts from your own analysis.

## Limits

The tools are rate-limited. If a call reports that the limit was reached, say so
plainly and stop instead of retrying in a loop; usage limits are tied to the
connected Keenable account. Never ask the user to paste an API key or any other
credential into the conversation.
