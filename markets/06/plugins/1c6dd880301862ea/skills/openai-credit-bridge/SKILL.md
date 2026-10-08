---
name: openai-credit-bridge
description: Use when the user wants a ChatGPT or Codex workflow to invoke an OpenAI API project through a separately deployed gateway, or wants Claude to call that OpenAI-backed gateway as an external MCP tool. Do not claim that native ChatGPT or Claude model usage can be rebilled to another provider.
---

# OpenAI Credit Bridge

Use this workflow only when the user explicitly asks to call an OpenAI-backed gateway or inspect its configuration.

## Required behaviour

1. Explain that native ChatGPT usage, OpenAI API usage, and Anthropic Claude usage have separate billing boundaries.
2. Never claim that installing this skill changes iOS ChatGPT model billing.
3. Never claim that OpenAI credits pay for native Claude inference.
4. If a configured MCP tool named `openai_create_response` is available and the user explicitly asks to use their OpenAI API credits, call that tool.
5. If the tool is unavailable, state that the remote MCP gateway must be deployed and connected first.
6. Keep provider API keys on the gateway in a secret store. Never request that a provider key be embedded in this skill, a plugin manifest, a mobile app, or a client-side JSON file.
7. Require explicit user approval before sending sensitive or confidential content to the external gateway.

## Expected gateway contract

The connected MCP server should expose:

- `openai_create_response`: Send input to an allowed OpenAI model through the gateway.
- `openai_list_models`: Return the gateway's permitted model identifiers.
- `openai_usage_summary`: Return usage metadata available to the authenticated gateway user.

## Response format

When the gateway is used, report:

1. Selected gateway tool
2. Selected model identifier
3. Result
4. Billing note: the gateway's OpenAI API project is charged for the gateway call; ChatGPT or Claude client usage remains separately governed

## Claude interoperability

Claude may connect to the same publicly reachable HTTPS MCP gateway as a custom connector. Treat OpenAI output as external tool output inside Claude. Do not describe this as Claude being powered or billed by OpenAI credits.
