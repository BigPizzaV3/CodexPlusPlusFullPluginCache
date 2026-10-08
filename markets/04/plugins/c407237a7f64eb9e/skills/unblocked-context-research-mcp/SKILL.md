---
name: unblocked-context-research-mcp
description: >
  Searches connected code, pull requests, documentation, messages, and issue
  trackers with the context_research MCP tool. Use for decision history, prior
  work, team conventions, planning, incident investigation, cross-system
  questions, or code that is not available in the local workspace. Use local
  file search when the current implementation alone can answer the question.
---

# Unblocked context research for MCP

Use `context_research` to retrieve engineering context from connected systems.
It can find current records, decision history, earlier attempts, and related work.

## Tool use

Call the `context_research` MCP tool directly.

If the tool is not available, stop and tell the user that Unblocked is not
configured in this environment. Do not replace it with web search. Web search
cannot access private repositories, issue trackers, documents, or messages.

## When to use it

Use this skill when the request needs one or more of these:

- The reason behind a code or product decision
- Earlier implementations or rejected approaches
- Pull request, issue, document, or message history
- Work across repositories or systems
- Filtered activity for a person, project, status, or date range
- Planning or investigation that needs evidence outside the local workspace

Use local file search first when the user only needs the current implementation.
If the named code is not in the workspace, use `context_research`.

## Input

| Parameter | Required | Use |
|:---|:---|:---|
| `query` | Yes | A complete question or directive with the topic, named entities, and hard filters. |
| `effort` | No | `low`, `medium`, or `high`. Use `low` for a focused lookup, `medium` for exploration, and `high` for plans, migrations, incidents, or broad investigations. |
| `include_content` | No | Set to `"true"` when the response must include document content. Omit it for an initial discovery pass. |
| `instruction` | No | Relevance and ranking guidance. It must not change the requested search scope. |
| `max_results` | No | A string that limits the number of returned documents. |

## Write focused queries

Use a complete question. Include the most concrete identifiers available:

- Repository, service, module, class, method, file, or endpoint
- Pull request or issue number
- Project key, channel, board, sprint, or label
- Person, status, and exact date range
- Decision, incident, migration, or feature name

Avoid bare keywords such as `auth` or `rate limiting`.

Keep one objective per call. Split independent unknowns into separate calls and
run those calls in parallel when the environment supports parallel tool use.

Example:

```text
How does AuthService.validateToken handle expired JWTs, and what prior pull
request or team discussion explains the current behavior?
```

For a complex investigation, write a short directive that names the systems,
constraints, and questions that the result must answer.

## Choose content depth

Start without `include_content` when titles, URLs, and snippets can identify the
best sources. Then either:

- Repeat the focused query with `include_content: "true"`.
- Use `context_get_urls` to load the strongest known URLs.

Set `include_content: "true"` on the first call when the task needs source text
immediately and the search scope is already narrow.

## Work with results

1. Extract file paths, symbols, pull request numbers, issue keys, people, and
   channel names from the first useful results.
2. Make one focused follow-up call if an important gap remains.
3. Check important code claims against local files before you edit them.
4. Use the returned source URLs when you report evidence.
5. State when results are thin, stale, or in conflict.

Code results normally represent the connected repository state. They might not
match local changes or the current branch.

## Filter semantics

- Use `me` when the user asks about their own work.
- Use status filters for current work. Do not add a date range unless the user
  asks about activity during a period.
- Treat completed issues as resolved during the requested period.
- Treat completed pull requests as merged during the requested period.
- Include exact dates when relative dates could be unclear.

## Limits

- Do not use this skill for a syntax question that has no company context.
- Do not treat a ranked search result as a complete list unless the tool states
  that the result is complete.
- Do not assume that returned code matches the local working tree.
- Do not invent missing history or conclusions.
