---
name: cellcog-get-started
description: Connect CellCog after installing the plugin. Use when the CellCog tools are not connected yet, or the user asks how to set CellCog up.
---

# Get started with CellCog

1. The CellCog tools (`cellcog_chat_create`, `cellcog_get_result` and the rest) come from the CellCog connector at `https://cellcog.ai/mcp`. The first time one is used, the user signs in with their CellCog account and clicks Approve. No API key is needed.
2. No account yet: the user signs up free at https://cellcog.ai, then signs in from the connector.
3. Check the connection with `cellcog_account`: it returns the email, plan and credit balance.
4. Then hand CellCog a job with `cellcog_chat_create` and poll `cellcog_get_result` about once a minute. For a project the user will come back to over days or months, hire an AI employee with `cellcog_employee_hire` (read the `ai-employees-cellcog` skill first).
