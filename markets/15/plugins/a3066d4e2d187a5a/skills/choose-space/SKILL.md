---
name: choose-space
description: Choose the approved Futoroku Space, ledger and account for a financial task, or check this connection's permissions and usage.
---

Use this workflow for Futoroku setup and whenever a financial destination is unclear. Read [the shared MCP contract](references/mcp-safety.md).

1. Call `list_spaces`. It returns only currently approved Spaces and effective permissions. Match the user's intended Space to its returned `space_id`. If several choices fit, ask a short question showing their names. Do not choose from browser state or infer a Space from an account name.
2. Call `get_finance_context` with that explicit `space_id` when role, available capabilities or allowance matters. A Viewer or read-only grant cannot write. Do not ask for broader access to finish a read task.
3. Discover only the needed catalogs with `list_ledger_catalog`, `list_account_catalog` and `list_category_catalog`; follow continuation metadata. Use authoritative IDs from this Space, including the account's exact denomination. Resolve duplicate names by asking the user. Reuse verified IDs within this task while their scope remains valid.
4. For a requested payer other than the user, use `list_transaction_members`; never infer a member ID from email. Omit attribution to use the authenticated creator. Do not set `recorded_by_user_id`.
5. Retain the chosen Space and object IDs for subsequent calls and any uncertain retry. Give a concise scope summary when it helps the user check a write.

Setup is read-only. Do not create a Space, ledger, account, category, grant or subscription as a setup shortcut. If access is missing, explain the specific missing permission and let the user manage it in Futoroku.
