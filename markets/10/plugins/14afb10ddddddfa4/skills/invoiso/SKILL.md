---
name: invoiso
description: Use when the user wants to read or manage invoices, expenses, contacts, inventory, documents, accounting workflows, or settings in their invoiso workspace.
---

# invoiso

Use the connected invoiso MCP tools for the user's current workspace. Let the
server's tool descriptions and annotations guide tool choice and required
inputs; do not invent tool names or fields.

## Connection and access

- Prefer the browser sign-in flow. The workspace is selected by the signed-in
  account, so do not ask the user to paste credentials into chat or store them
  in plugin files.
- Some workspaces can read but not change records through this connection,
  and some people's access is limited. When a tool refuses, pass on the reason
  it gives rather than guessing at another.
- Values omitted when creating an invoice may inherit the workspace's saved
  issuer, numbering, currency, tax, language, and notes defaults. Check the
  available workspace settings when a missing value could change the result.

## Work carefully

- Resolve customer, supplier, invoice, expense, and product references from
  workspace results before using their identifiers in a change.
- Check the tool annotations and confirm material details before destructive,
  external, or money-moving actions such as deletion, sending, publishing, or
  payment-related actions.
- Do not claim an action succeeded unless the tool result confirms it. Report
  plan limits, validation errors, and partial results plainly.
