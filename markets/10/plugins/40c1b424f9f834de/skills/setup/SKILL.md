---
name: setup
description: Sign in to OneInfer. Every tool then uses the signed-in account.
---

Help the person connect OneInfer.

1. Ask them to sign in with their own OneInfer account when ChatGPT requests access. Do not ask them to paste an API key into a tool argument.
2. Every tool then uses the signed-in account. Never ask them for a developer id, account id, API key, or password.
3. To confirm the connection, read their credits with oneinfer_get_credits, then offer to list models or their GPU machines.
4. If a tool says the sign-in is missing or expired, ask them to reconnect OneInfer in ChatGPT and try again.
