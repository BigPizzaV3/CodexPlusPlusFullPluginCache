---
name: unblocked-context-get-urls-mcp
description: >
  Loads full content for known pull request, issue, document, message, and public
  web URLs with the context_get_urls MCP tool. Use when the user supplies URLs or
  a prior search returns URLs that need full-text review. Use context_research
  when the URL is not known. Do not use for local files or private network URLs.
---

# Unblocked URL retrieval for MCP

Use `context_get_urls` when you already know which documents to load. The tool
can resolve content through configured private connectors and public web pages.

## Tool use

Call the `context_get_urls` MCP tool directly. Pass `urls` as an array.

If the tool is not available, tell the user that Unblocked is not configured in
this environment. Do not use a generic web fetch for private GitHub, Jira,
Linear, Slack, Notion, or other connector content.

## When to use it

Use this skill when:

- The user provides one or more URLs to summarize or analyze.
- `context_research` returns URLs and the snippets are not enough.
- A known pull request, issue, document, or message must be checked again.
- Several related source URLs need one combined review.

Use `context_research` when you must find the URL first.

## Input

| Parameter | Required | Use |
|:---|:---|:---|
| `urls` | Yes | An array of complete `http://` or `https://` URLs. |

Good inputs include direct links to pull requests, issues, Slack threads,
Confluence or Notion pages, and public web pages.

Do not pass:

- `localhost` or `127.0.0.1`
- Private network addresses
- `file://` URLs
- URLs without an `http://` or `https://` scheme
- Session URLs that depend on browser cookies

## Check support

Connector support differs by organization. Inspect the live
`context_get_urls` tool description when you need to confirm supported URL
patterns. If a URL does not match a listed pattern, tell the user that its
connector or organization might not be configured.

## Batch related URLs

Send a related set of URLs in one call. A batch of about 5 to 10 URLs is a good
default. Split larger or unrelated sets to reduce timeouts and oversized output.

Keep the original URL with each finding. This makes the source easy to check and
cites the correct item when a batch contains similar documents.

## Work with results

- Check for empty content, login pages, and authorization errors before you use
  the result as evidence.
- Treat issue and pull request status as live at retrieval time.
- Do not assume pull request content includes the full diff.
- Use local repository tools when the task needs code changes or exact diff
  inspection.
- State which URL failed and why when only part of a batch resolves.

## Limits

- Skip retrieval when the available snippet already answers the question.
- Do not use this tool for local files or private network resources.
- Do not guess at content when a connector is missing or authorization fails.
