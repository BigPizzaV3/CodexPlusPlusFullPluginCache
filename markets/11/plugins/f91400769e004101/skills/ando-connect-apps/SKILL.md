---
name: ando-connect-apps
description: Connect the apps an Ando team uses, choose account ownership and agent access, and verify permissions with a real read. Use for first app setup or adding a required account.
---

# Connect your apps

Read [Ando basics](../../references/ando-basics.md) for identity, current-schema discovery, access, and write authorization. Establish the app, account, resource, and team outcome the connection should support. Connect the apps needed for that outcome rather than everything available.

## Choose ownership and access

Follow the current [Connecting apps guide](https://docs.ando.so/docs/connecting-apps-to-ando). Choose who owns each connection, who may use it, and which resources and actions it should allow. Workspace and personal connections belong to different audiences; an app can have both.

For a personal connection, determine whether an enabled agent should use the account only for the owner's requests or for others allowed to ask. Keep the supported restrictive default unless broader use is explicitly intended. A personal connection acts through its owner's provider account; Ando agent identity does not change that provider identity.

## Discover and connect

Read current connection state and reuse the intended account when already connected. Verify its actual provider/account identity; connection labels alone are insufficient. Use the exposed discovery path and exact schemas: compact catalogs may expose `list_connections`, `search_app_tools`, and `get_app_tool_schemas` (older compact servers use `list_app_tools`), while legacy catalogs may use `list_tools` and `get_tool_schemas`.

Use the returned supported connection or reconnect flow within the user's scope. If consent or administration requires the owner, prepare the configuration and provide the exact handoff. Never collect provider passwords, tokens, or verification codes in chat. See [optional capabilities](../../references/optional-capabilities.md) for shared app-tool boundaries.

Grant the intended members or agent only the required account, resources, and actions through supported controls. A successful OAuth callback does not establish that the agent can use the requested provider resource.

## Verify practical access

From the intended acting identity, perform a narrow read of a known permitted resource using its current tool schema. Confirm the provider account, returned resource, and relevant access. A read verifies reading only; do not use a provider mutation as a permission test without authorization.

Report the configured account, audience, verified operation, and remaining permissions or consent. Record where to disable access. For inbound provider events use [Set up an alert channel](../ando-alert-channel/SKILL.md); connecting an account alone does not create an alert feed or ongoing agent worker.
