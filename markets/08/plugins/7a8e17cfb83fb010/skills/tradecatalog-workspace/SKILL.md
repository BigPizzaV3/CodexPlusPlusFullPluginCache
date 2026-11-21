---
name: tradecatalog-workspace
description: Change a supplier's TradeCatalog business details, branding, order recipients or catalogue settings, invite staff, or obtain authorized export and API setup links. Use for managing an existing supplier workspace; customer access and pricing are separate workflows.
---

# TradeCatalog supplier workspace

Select the intended supplier using `list_workspaces`, then read `get_workspace` and `get_settings`. Work through the connected TradeCatalog MCP tools with the person's own membership. Settings need `branding.manage`; staff invitations and API-key controls need `staff.invite`. Owner and Admin have those permissions, while other roles can be customized. The server checks current permission and plan on every action; a role label alone does not guarantee access.

## Change supplier settings

Read `get_settings.settings` before `save_settings`. Its nested `settings` input requires `name`, `accentColour`, `currency`, `timezone`, `taxLabel` and `orderEmails`; copy current values for everything outside the request. `orderEmails` is the complete replacement list of up to three recipients, so preserve existing recipients when adding one and show the exact final list before review.

Optional fields remain unchanged when omitted: `legalName`, `registrationNumber`, `taxNumber`, `country`, `listed`, `smartSearch`, `ordersEnabled`, `priceListDownloads`, `hideProductPhotos` and `whiteLabel`. Blank legal/registration/tax fields clear their value. Choose these controls only for the person's goal:

- Business identity, colour, country and tax wording affect how the catalogue appears. A currency change relabels stored minor-unit amounts; it does not convert existing prices or agreed deals. Resolve intended currency conversion separately before changing a populated catalogue. Tax wording alone does not calculate tax.
- `ordersEnabled: false` makes customers following the supplier prices only. Customer `ordering` overrides still apply: `can_order` remains able to order and `prices_only` remains unable. Use the customer workflow when a specific account exception is requested.
- `priceListDownloads: false` blocks buyer CSV and PDF price-list downloads; it does not hide catalogue prices or stop ordering.
- `listed` opts the supplier into the public directory. Do not turn it on merely to help someone find their private trade portal.
- `smartSearch` controls natural-language catalogue search; enabling it starts indexing, so a saved setting is not proof that all products are already searchable.
- `hideProductPhotos` and enabling `whiteLabel` require Pro. Explain an unavailable setting without starting checkout or promoting an upgrade. White-label setup can require further signed-in branding/domain work; saving the toggle alone is not evidence that a branded domain is configured.

Use `open_logo_settings` when the person wants to upload a supplier logo. Return its signed-in link; that tool neither reads an image nor changes the logo. Demo workspaces do not email real recipients or appear in the directory, even when submitted settings request those outcomes.

## Invite the supplier's team

Read `list_staff` for current members and pending invitations. Distinguish staff workspace access from a customer's purchasing access. For a requested staff invitation, use `invite_staff` with the exact recipient `email` and an explicit `role`; omission defaults to Admin and must not be used to guess the required access.

Supported roles are `owner`, `admin`, `pricing_manager`, `sales_admin`, `order_handler` and `viewer`. Only an Owner can invite another Owner. Owner and Admin work on every plan; the four specialist roles require Pro. Pricing Manager focuses on catalogue/prices, Sales Admin on assigned customers, Order Handler on processing orders, and Viewer on reading. Existing members may have customized permissions, so do not promise a full set of powers from the role name alone. The legacy `staff` value is not valid for a new invitation.

The tool sends an email after review. Reread `list_staff` and report the invitation as pending until accepted. Changing an existing staff role, custom permissions, customer-region coverage, ownership or removing staff has no MCP tool: those actions finish in the signed-in **Team** page. Do not re-invite someone as a substitute for changing their existing membership.

## Export and integration handoffs

- `download_products_csv` returns a signed-in product export link and needs `data.export`. `download_workspace_export` returns a full workspace export link for an Owner or Admin. The user opens these links to download; generating one does not read, download or transfer customer data to another service.
- `open_api_key_settings` returns the signed-in API settings link for credential creation. It does not create a key. `list_api_keys` returns labels and scopes without secrets; never ask for a key in chat. OAuth is already the plugin's connection and does not need a new API key.
- For an explicitly requested integration disconnection, resolve its current `keyId` through `list_api_keys`, then use reviewed `revoke_api_key`. Revocation stops that integration immediately; it does not revoke every key or disconnect the current OAuth connection.

## Confirm and report

For mutations, show the returned confirmation card or signed-in `reviewUrl` with the exact setting, recipients or role. The person confirms there; chat text is not a substitute and the agent never calls private `decide_action`. Check `get_action_status`, then reread the relevant settings, staff invitations or API-key list after success. Stop on pending, failed or uncertain outcomes instead of repeating a write. A handoff link, saved setting, invitation sent and accepted membership are distinct states; report only what the tool and fresh read establish.
