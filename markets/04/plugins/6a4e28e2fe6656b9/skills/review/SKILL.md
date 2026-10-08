---
name: review
description: Review the current working branch with the bundled Greptile CLI, optionally against a specified base branch or with review instructions.
---

Run a Greptile review from the user's repository. No open pull request is needed.

Resolve `<skill-root>` as the directory containing this `SKILL.md`.
Substitute that absolute path in the command; use the bundled script rather
than a separately installed `greptile` executable.
Keep the working directory in the repository being reviewed.

```sh
GREPTILE_NO_AUTO_INSTALL=1 GREPTILE_NO_UPDATE_CHECK=1 node "<skill-root>/scripts/greptile.mjs" review --agent
```

If the user specifies a base branch, append `--branch` with that branch. Pass
any focus instructions verbatim with `--instructions`. Shell-quote both
values as literal arguments so dollar signs, backticks, quotes, and command
substitutions in user text cannot execute or change the text.

Always pass `--agent`. The environment variables suppress the Mermaid renderer
download and standalone update notices; the bundled CLI updates with the plugin.

Reviews can take longer than two minutes. If the shell tool returns a running
session, keep polling that session until it completes rather than starting a
second review.

If authentication is missing, direct the user to the plugin's `login` skill.
Do not start browser sign-in as a side effect of this review command.

The CLI stores the review on the user's Greptile account. The MCP tools
`list_code_reviews` and `get_code_review` can read it with `source: "headless"`;
MCP authentication is separate from CLI login.

Summarize the findings and offer to fix them. Use `get_code_review` when more
finding detail is needed. If the command fails, report the failure and the
next action rather than presenting it as a successful review.
