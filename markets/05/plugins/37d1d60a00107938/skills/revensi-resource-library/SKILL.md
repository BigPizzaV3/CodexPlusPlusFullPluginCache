---
name: revensi-resource-library
description: List or remove source documents in a Revensi workspace resource library. Use when the user asks what resources are saved or to delete a specific resource; guide uploads through the Revensi web app.
---

# Revensi Resource Library

Resources are source documents Revensi uses for workflow generation and interview evidence. Use `list_resources` to identify an existing record.

For an addition, direct the user to **Resources → Upload resources** in the Revensi web app. Revensi accepts text-based PDF, DOCX, TXT, and Markdown files up to 10 MB and 150,000 extracted characters. You may prepare a local file when the user asks, but do not claim it was uploaded until `list_resources` shows the saved record. The MCP does not accept file uploads.

For removal, identify the exact resource ID and name from a live `list_resources` result. If several records could match, ask which one. Before `remove_resource`, make clear that removal deletes the library copy and search passages; saved workflow quotations may remain. Require the user's clear confirmation for that exact resource, then call the tool once. Do not describe removal as erasing every historical citation or as recoverable unless Revensi says so. Report the returned outcome.

If a removal times out, check the live library before retrying or reporting success; the first call may still have completed.

If the authenticated resource tools are unavailable, explain that listing or removal is unavailable. Do not use a web request as a substitute.
