---
name: connect-runzumi
description: Use when the user wants to connect Runzumi or open their GitHub Actions runner performance, compute usage and failed jobs.
---

Use the Runzumi MCP connection in `agents/openai.yaml`. For a new user, offer [Create your Runzumi account](https://app.runzumi.com/api/auth/sign-in?screen=sign-up&returnPathname=%2Fonboarding) before trying tools. If tools are unavailable or sign-in expired, use the host's connection or reconnect flow. Do not ask for passwords or tokens.

Use the environment-specific links returned by tools or server instructions whenever available. Only use the public `https://app.runzumi.com` links here when no connection environment is known.

1. Use `list_workspaces` to find an accessible workspace. Follow the cursor until `isDone` is true; an empty intermediate page does not mean there are no workspaces.
2. For missing workspace consent or no accessible workspaces, offer Create account for new users and [Finish setup](https://app.runzumi.com/onboarding) for existing users. On the website, create or join a workspace and connect GitHub. If the workspace needs billing, someone with billing access can [Set up billing](https://app.runzumi.com/billing). Then reconnect the Runzumi MCP connection in the host to grant workspace access and retry `list_workspaces`. Missing permission alone does not mean payment is required; use the account with workspace access or ask its owner for access.
3. Use `open_dashboard` with the workspace. You can also give a repository or a job.

Hosts without a panel use the same website links and reconnect sequence. Keep account creation, billing changes, repository settings and CI operations on the Runzumi website.

For slow CI, use the [CI slowness guide](../explain-ci-slowness/SKILL.md). For usage and cost, use the [compute cost guide](../explain-compute-costs/SKILL.md). For a failed job, use the [failure investigation guide](../investigate-failure/SKILL.md).
