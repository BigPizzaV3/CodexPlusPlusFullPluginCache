---
name: fix-office-accessibility
description: Fix supported accessibility issues in an attached Word (DOCX) or PowerPoint (PPTX) file with Inkable, retrieve the completed remediation, and offer the updated file with remaining issues. Use for Word/PowerPoint accessibility fixes and their status, not PDF remediation or general document editing.
---

# Fix Word and PowerPoint accessibility

Use the packaged `inkable-docs` MCP connection at `https://inkabledocs.com/mcp`. Fix the file only when requested; a check-only request belongs to `check-document-accessibility`.

## Choose the matching tools

| Original format | Start remediation              | Retrieve status and file |
| --------------- | ------------------------------ | ------------------------ |
| DOCX            | `remediate_docx_accessibility` | `get_docx_remediation`   |
| PPTX            | `remediate_pptx_accessibility` | `get_pptx_remediation`   |

Require the original DOCX or PPTX attachment. If it is missing or ambiguous, ask for the file or clarification. PDF remediation is unsupported: explain that limit and offer a check instead. Do not convert a PDF or another unsupported format to bypass the limit.

## Start or resume the job

- Pass the original attachment in `file` using ChatGPT's `openai/fileParams` flow: `download_url` and `file_id` are required; preserve the provided filename and MIME when available. Do not fabricate attachment metadata, rebuild a file from text, or use the Claude upload-token workflow.
- For an existing remediation, retain its `requestId` and format, and use the matching retrieval tool. Do not start duplicate work when the user asks whether a job is ready. Never send a remediation ID to `get_accessibility_check`.
- Report queued and running states honestly. If asked to wait or retrieve until completion, poll conservatively and honor retry guidance. Stop on a terminal result or an access/rate-limit error and explain the observed state. A failed or pending job is not a completed file.

## Deliver the completed file

- Retrieve the completed result with the dedicated DOCX or PPTX retrieval tool. Present the returned embedded binary MCP file resource as a usable download in the matching Office format. The updated file is separate; preserve the original attachment.
- If the client cannot materialize or download the resource, report the presentation problem instead of claiming delivery. Do not invent a link or substitute a reconstructed file. If a tool is missing, explain that the connection's tool set needs updating.
- Report the returned before/after scores, applied fixes, remaining active/deferred checks, and warnings without claiming all issues are resolved. Label those scores as remediation results; do not claim an independent recheck unless it actually ran. Describe an email notification only as returned by the tool.
- Explain that the output supports the user's accessibility workflow; it is not a guarantee of WCAG conformance. Keep check names/categories intact and expose neither attachment credentials nor operation capabilities in prose.

An independent post-remediation check is a separate action: run it when requested, using the actual output file and the check workflow. Do not silently add it or claim certification based on the remediation score.
