---
name: feedback
description: Report a bug, rough edge, or feature request for Compelling or this plugin. Use when a Compelling tool call fails unexpectedly, returns wrong data, or the user says they want to report a problem or give feedback about Compelling.
---

# Send feedback about Compelling

Route feedback to the right channel and include enough context to make it actionable.

## Gather context first

Before filing anything, collect (from the conversation, not by re-running paid tools):

- What the user tried to do, and which tool call failed or misbehaved (tool name + arguments, minus anything sensitive).
- The exact error text or the unexpected output.
- The `list_id` / `question_id` involved, if any.
- Which AI client the user is working in (for example ChatGPT, Codex, Cursor).

**Never include credentials, tokens, or personal contact data (emails, phone numbers) in a report.**

## Channels

- **Plugin or MCP issues** (tool errors, schema problems, skill gaps): open a GitHub issue at
  https://github.com/seekwhens/compelling-plugin/issues — draft the title and body for the user,
  then let them review before anything is posted.
- **Product issues or account questions** (credits, billing, data quality, workspace access):
  point the user to the in-app support chat at https://app.compelling.ai (bottom-right beacon)
  or the contact options on https://compelling.ai.

## Draft format for GitHub issues

```
Title: <one-line symptom, e.g. "run_insight returns dispatch_failed for contact email columns">

**What I did:** <tool + arguments>
**What happened:** <error/output>
**Expected:** <what should have happened>
**Client:** <the AI client in use>
```
