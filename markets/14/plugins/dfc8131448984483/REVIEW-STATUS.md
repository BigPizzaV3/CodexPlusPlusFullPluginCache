# BudgetSyncer public listing draft — review status

This is a preparation draft, not a submitted or published listing. It is separate from the existing private plugin.

## Listing and package
- Display name: BudgetSyncer
- Publisher intended for listing: Dawnode Oy (verify selected publisher identity in the submission portal)
- Category: Finance
- MCP endpoint: https://budgetsyncer.com/api/mcp
- OAuth client ID: chatgpt; scope: mcp:read
- Icons included: 512x512 PNG logo and 48x48 PNG composer icon
- Release draft version: 0.1.1

## Must resolve before submission
1. Verify that `https://budgetsyncer.com/support` and `https://budgetsyncer.com/terms` are publicly accessible and contain the promised support and plugin terms.
2. The currently indexed privacy policy appears to describe data handling differently from the updated policy text supplied by the publisher. Publish and verify a policy that accurately reflects actual MCP behavior, retention, logging, transaction previews, account deletion, and sharing with connected assistants before submitting.
3. Run the five positive and three negative review cases in `plugin.json` against the exact saved ChatGPT/MCP version and record actual results. The cases are packaged, but they have not been executed.
4. Confirm that the supplied YouTube demo is publicly viewable and shows the actual ChatGPT-MCP integration and representative behavior: https://youtu.be/SBa65rLfk3I
5. In the submission portal, verify the publisher identity, OAuth connection, required scans, legal attestations, reviewer access, release notes, and country targeting. These cannot be attested or verified by packaging alone.

## Review cases in plugin.json (not yet executed)
Positive prompts:
1. When did BudgetSyncer last sync my banks, and were there any errors?
2. Which banks and accounts are linked in my BudgetSyncer account?
3. What booked and pending transactions does my linked bank account show?
4. What YNAB budgets, accounts, and categories are on my connected YNAB account?
5. Show recent transactions in my YNAB budget.

Negative prompts, where the plugin should not be called:
1. How does YNAB zero-based budgeting work?
2. Add a 20 euro grocery transaction to my YNAB budget.
3. Transfer 100 euros from my bank account to another account.
