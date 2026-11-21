---
name: menu
description: "Show the Otis menu and route a user to an independent business workflow when they ask for /otis or need help choosing a task."
---

# Otis menu

Use when the user asks for /otis, the Otis menu, or help choosing an Otis task. If a task is already explicit, use its workflow without a menu detour.

Call the connected Otis otis_menu tool and show its numbered choices. Wait for a number, an action name or a natural-language task. Showing the menu does not authorize a write or invoice issuance.

If Otis is not connected, label this as a navigation preview, show the choices below, and explain how to connect the bundled remote MCP. Sign-in uses an email code in the browser; never ask for the code in chat. Do not invent business records or imply the user is authenticated.

1. Create invoice — workflow: create-invoice
2. Record work — workflow: record-work
3. Add expense — workflow: add-expense
4. Clients — workflow: clients
5. Invoices — workflow: invoices
6. Payments — workflow: payments
7. Business settings — workflow: business-settings
8. Tax settings — workflow: tax-settings
9. Export — workflow: export

After the user selects a task, use its matching workflow skill or the mapped steps returned by otis_menu. Discover the business and current permissions before accessing records. The public demo is fictional and read-only; these packaged workflow skills target the private connection.

Use the host's actual skill picker or namespace. Do not promise that /otis or a hyphenated alias is installed universally.
