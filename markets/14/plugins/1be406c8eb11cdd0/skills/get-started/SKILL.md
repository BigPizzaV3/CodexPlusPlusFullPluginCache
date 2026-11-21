---
name: get-started
description: Get started with Pledge. Use when the user asks what Pledge can do, how to connect it, which workspace they're in, or wants to try it for the first time.
---

# Get started with Pledge

Pledge stores a company's contracts, clients and templates, and sends contracts for e-signature. Through the `pledge` MCP tools you act as the user, in the workspace they picked when they connected.

1. Call `whoami` and tell the user which workspace you're in and whether the connection can only read or can also write. If the tools aren't connected, tell them to connect Pledge (they sign in with their Pledge account at https://www.pledge.no) and stop.
2. Offer two or three things to try, picked from what the workspace has (`list_templates`, `list_contracts`):
   - "Draft an NDA for a new client and show it to me"
   - "Which contracts end in the next three months?"
   - "Find the contract with Acme and summarise what we agreed"
3. To write a contract, follow the `new-contract` skill: ask a few questions at a time, draft early, show it with `preview_contract`, and send only after the user says so.

Pledge has no delete tools, and nothing is sent for signing unless the user presses Send or tells you to. Help and setup: https://www.pledge.no/agents.
