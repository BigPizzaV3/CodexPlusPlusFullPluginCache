---
name: get-file-summary
description: Retrieve an existing summary for a single file accessible to the authenticated HiNoter user. Use when the user asks to view or read a HiNoter file summary and provides a file_id or a clear file_id exists in context; do not use for generating, updating, or deleting summaries.
---

# Get File Summary

Use the `get_user_file_summary` tool provided by the plugin MCP service to read an existing summary.

1. Obtain a unique, explicit `file_id` from the user message or a trusted previous tool result. If there is no `file_id`, ask first; if the user only provides a file name, use `$browse-hinoter-files` to get a list first, then ask the user to confirm the single match. Never guess identifiers.
2. Call `get_user_file_summary` exactly once using the `file_id`; do not pass `user_id`, access tokens, or any other identity information. The server determines the current user from the OAuth context and validates read permission on the personal or team workspace.
3. 当 `has_summary` 为 `true` 时，保留 Markdown 结构展示返回的总结；可以提及文件名称。不要编造工具未返回的事实或更新时间。
4. When `has_summary` is `false`, clearly state that the file has no existing summary. Never generate or fabricate a summary.
5. If the tool returns `isError`, briefly restate the error and stop. Do not try other file IDs and do not bypass permission checks by calling regular business APIs.
6. When `get_user_file_summary` is not available in the current task, do not interpret it as "the file has no summary". Explain that the HiNoter MCP is not loaded in the current task, then advise: confirm HiNoter is enabled in the Codex plugin settings (from the command line, check `codex plugin list`), and start a new task or restart Codex after installing or updating the plugin. If a new task still has no tools, check that the MCP URL in the plugin `mcp.json` is reachable and that the protected resource metadata and authorization server metadata return JSON, and confirm the server has `mcp.issuer`, `mcp.resource_uri`, and `mcp.token_hmac_key` configured — production also requires `mcp.web_login_url` with test authorization disabled. Do not fall back to unauthorized network requests.

This skill only reads existing summaries. It never triggers regeneration, never reads transcriptions, images, todos, or storage paths, and never performs any write operation.
