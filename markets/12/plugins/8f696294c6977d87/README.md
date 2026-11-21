# Veridu for ChatGPT and Codex

Independent review of the change you or your coding agent just made, before you commit. Ask the agent to "verify this change with Veridu": it sends the diff and the files it changed to Veridu, two reviewers from different vendors check them, findings that cannot be grounded in the code are dropped, and the agent gets back an outcome (pass, review or block) and concrete findings with file, line, severity and evidence. The agent can fix the findings that hold up and check again; each finding keeps the same id across follow-ups, so you can see what was fixed, what persists and what a fix introduced.

Veridu reviews only what is sent. It does not read the rest of your repository, so a pass means "nothing found in what was sent", not "safe to merge". For pull-request review with repository context, use the [GitHub App](https://github.com/apps/veridu-review).

## What the plugin contains

- **An MCP server entry** for Veridu's hosted server at `https://api.veridu.io/mcp` (tools: `verify_change`, `get_change`, `veridu_review`, `veridu_review_status`).
- **A skill, `verify-before-commit`**, that tells the coding agent how to build the payload, read the result, and run the fix-and-check loop.

Nothing runs on your machine: there are no hooks, scripts or packages.

## Connect

Install Veridu from the plugin directory, connect the **veridu** MCP server, and sign in in the browser with GitHub or Google. No API keys.

## Cost

Each new change counts as one review on your Veridu account. Up to two follow-up checks of the same change do not count as new reviews, and resending an identical change returns the earlier result.

## Privacy

When the agent calls `verify_change`, it sends to `api.veridu.io` the diff of the change and the full content of the files it chose to send. Nothing else from your machine or repository is read. The check runs in an isolated sandbox in AWS us-east-1, and the reviewer prompts go to OpenAI and Anthropic, neither of which uses API traffic for training under their published policies. The diff and files are deleted 7 days after the check finishes; the result (verdict and findings, which can quote lines of your code) is kept until you delete your account. Veridu stores only a hash of the sign-in token. Full policy: https://veridu.io/data. Questions or deletion requests: hello@veridu.io.

## Support

hello@veridu.io · https://veridu.io/docs

Veridu is operated by T3 Interactive LLC.
