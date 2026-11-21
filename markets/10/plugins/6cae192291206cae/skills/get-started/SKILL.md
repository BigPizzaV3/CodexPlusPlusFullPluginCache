---
name: get-started
description: Connect Keiki and build, update and review AI agents in your Keiki organization from ChatGPT.
---

# Get started with Keiki

Keiki hosts AI agents that answer your contacts over text channels. This plugin lets you build and review those agents from ChatGPT. It only reaches the Keiki organization you approve when you connect.

## What you can do

- List your agents and open one to see its configuration, model and recent conversations (`get_agents`, `get_agents_by_id`).
- Create an agent from a name, a model and a system prompt (`get_models`, `post_agents`).
- Change an agent's name, model, system prompt or limits (`post_agents_by_id`), and see its version history (`get_agents_versions`).
- Read conversations, engagement analytics and quality reviews (`get_agents_conversations`, `get_agents_conversations_by_phone`, `get_agents_analytics`, `get_agents_quality`).
- Read eval cases and results (`get_evals_cases`, `get_evals_runs_latest`, `get_evals_runs_cases`).
- Check which account and organization are connected (`current_context`).

## How to work

1. Call `current_context` first if it's unclear which organization is connected.
2. Before you change an agent, show the user exactly what will change and wait for them to confirm.
3. Resolve a model the user names with `get_models` before you set it.
4. Ask only for what the task needs: an agent name, a model, or prompt text. Never ask for payment card numbers, government IDs, health or biometric details, passwords, API keys or other credentials.

## Out of scope

Billing, purchases, payments, phone lines, channel credentials, secrets, tools and integrations are managed in the Keiki dashboard at https://onkeiki.com. They aren't available here. When asked for one, say it can't be done here and point the user to the dashboard.
