---
name: centralize-persona-functions-creation
description: "Define buyer functions and personas for a named account in the connected Centralize workspace. Use when the user asks to configure who that account's sales team sells to."
---

# Configure buyer functions and personas

Read [workspace and write boundaries](../../references/workspace-safety.md) first.
Model the external buyers that the named company's sales team serves, not the plugin developer's own buyers.

## Establish scope and existing definitions

Resolve the company with `searchCustomers`. Read `getAccountContext`, `listFunctions`, `listPersonas`, and `listSeniorities`.
If the account does not exist, stop and ask whether the user wants to add it. Do not create an unrelated default function.
If account context does not establish the company's buyers, ask for its target roles and sales motion.
Do not require external enrichment, private call notes, or another plugin to complete this workflow.

Reuse matching functions and persona concepts. Flag duplicates and prospect-specific text on workspace defaults without editing them.
Do not assume that the connected workspace contains a fixed set of functions or seniority names.

## Present the plan

For each new function, give its name, responsibilities, four to eight example job titles, and five to eight related keywords.
Use generic responsibilities so the function does not contain another prospect's sales pitch.
Mark each definition as reuse or create. New account-specific functions require `isDefault: false` and `accountIds` for the selected account.

For each persona, give its name, function, discovered seniorities, and business context of no more than 1,000 characters.
Explain the buyer's responsibilities, relevant problem, buying triggers, role in the decision, and common objections.
State which claims come from account context and which require user confirmation.

Personas are workspace-wide definitions even when they include `customerOverrides`. Explain this scope before approval.
Reuse an existing persona when it fits. The plugin has no persona-update operation, so do not create duplicates to emulate an update.
When an existing persona needs a new override, report the required edit for the user to make in Centralize.
Obtain confirmation of the exact definitions, account bindings, and workspace-wide effects before creation.

## Create and verify

Create approved functions with `createFunction` before the personas that depend on them.
Trim names, keep them within 200 characters, and exclude colons from function names.
Keep function descriptions within 1,000 characters.

Use `createPersona` with either `customFunctionName` or `function`, following the current schema.
Use discovered `customSeniorityNames` or supported base `seniorities` without inventing names.
Use `customerOverrides` only when creating an approved new persona that requires account-specific mappings.
Never imply that `createPersona` edits an existing persona.

Read `listFunctions` and `listPersonas` again. Report stored names, account bindings, created definitions, and unsupported edits.
After a partial failure, re-read existing definitions before retrying to prevent duplicate creation.
