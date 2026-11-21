---
name: oac-governance-permissions
description: Manage Oracle Analytics Cloud catalog permissions through the OAC MCP tools. Use when a user asks to grant, revoke, or otherwise change access to a catalog item, or when a permission-management workflow needs to locate the exact target item before updating its ACL. Treat ACL updates as security-sensitive, production-impacting catalog mutations. Require explicit approval immediately before execution, never infer users, groups, roles, inheritance, or permission semantics, and do not claim that current permissions were inspected unless a connected tool actually returned them.
---

# Oracle Analytics Cloud Governance and Permissions

## Configured instance

Use only the Oracle Analytics MCP connection attached to the selected configured instance. Ground requests in that instance's live tools, metadata, identifiers, and permissions. Do not fall back to the template example URL, a remembered demo account or catalog path, or another instance's connection. If no instance is configured, explain that a workspace administrator must configure one before this workflow can run.

Use this skill for catalog access-control changes. Use the runtime-exposed MCP schema as the authoritative source for supported ACL arguments, principal identifiers, permission values, and response fields.

## Workflow

1. Identify the exact catalog target.
   - If the target is not already established by an unambiguous identifier or current tool output, use `oracle_analytics-search_catalog` to locate it.
   - Do not infer a target from a similar name when multiple matches exist.

2. Establish the requested permission change.
   - Preserve the principal, permission, scope, and intended action exactly as established by the user and supported tool schema.
   - Do not invent or infer user IDs, group IDs, application roles, inheritance behavior, permission names, or ACL merge/replace semantics.

3. State the exact intended change.
   - Make clear which catalog item will be changed and what access change will be attempted.
   - If the live tool semantics indicate a replace-versus-merge distinction, surface that distinction before approval.

4. Require explicit approval.
   - `oracle_analytics-update_catalog_acl` modifies Oracle Analytics Cloud and requires `userApproved: true` or an explicit approval flow.
   - Obtain approval immediately before invoking the ACL update.
   - Do not interpret a general request to review or manage permissions as approval for a specific ACL mutation.

5. Execute the update.
   - Invoke `oracle_analytics-update_catalog_acl` only with values supported by the live schema and grounded in user intent or prior tool output.
   - Do not broaden access beyond what the user requested.

6. Report the outcome.
   - Do not claim success until the tool confirms it.
   - Report resulting permissions or status only when returned by the tool.
   - Preserve errors or uncertainty rather than filling gaps.

## MCP tools

- `oracle_analytics-search_catalog`: Locate the target catalog item when necessary. Experimental and read-only.
- `oracle_analytics-update_catalog_acl`: Update catalog permissions. Experimental; modifies OAC; approval required.

## Important limitation

The documented OAC MCP tool set does not list a dedicated read-only ACL inspection tool. Do not claim that this skill can enumerate or audit existing permissions unless the active runtime exposes additional supported functionality or the ACL update tool returns that information. If a user asks only "who has access?", state the limitation instead of fabricating a permission view.

## Security rules

- Prefer the smallest change that exactly matches the user's request.
- Never grant broader access as a convenience or workaround.
- Do not make assumptions about inherited permissions or effective access.
- Do not convert names to identities unless a connected tool explicitly resolves them.
- Do not invent MCP parameters. Follow the live runtime schema.
- The OAC MCP integration is in Preview, and both catalog search and ACL update are experimental tools.

## Example requests

- "Give the Finance Analysts group access to this workbook."
- "Remove access for this role from the Planning folder."
- "Change the permissions on the Q4 forecast workbook."
