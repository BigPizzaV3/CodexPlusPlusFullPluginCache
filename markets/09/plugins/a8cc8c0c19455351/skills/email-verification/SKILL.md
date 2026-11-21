---
name: email-verification
description: Use when the user asks to verify, validate, or check whether an email address is deliverable or valid with Fraud Blocker, or asks to interpret a Fraud Blocker email verification result.
---

# Fraud Blocker email verification

Use the `verify_email` MCP tool when the user explicitly asks to verify or validate an email address.

- Pass only the email address the user asked to verify.
- Never invent or infer a verification result.
- Explain the returned `status` and `sub_status` in plain language when useful.
- Surface `did_you_mean` when present.
- Mention `free_email`, `domain`, and `mx_found` only when they help answer the user's question.
- If the response includes `usage`, report it when the user asks about remaining verification capacity or when a monthly-limit error occurs.
- If the service returns `monthly_limit_reached`, explain that the connected Fraud Blocker account has reached its monthly email verification limit.
- If authentication is required, ask the user to connect their Fraud Blocker account through the plugin's sign-in flow; never ask them to paste passwords, API keys, access tokens, refresh tokens, or Firebase tokens into chat.
- Do not call verification merely to illustrate an example. A verification consumes the connected account's allowance.
