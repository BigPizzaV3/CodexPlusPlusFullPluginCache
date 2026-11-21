# Thissa Store

Developed by **Thissa Digital SAS**. Category: **Business & Operations**.

Website: https://thissa.store
Remote MCP endpoint: https://thissa.store/mcp

Connect your Thissa Store account to manage digital menus, catalogs and suppliers, inspect native inventory and movement history, read merchandise purchases and supplier balances, upload images and read aggregated analytics. Existing moderator accounts retain their authorized business management tools.

Ordering, purchase, stock, payment, reservation and loyalty writes are outside this integration. Supplier changes never contact suppliers or alter stock, cash or historical purchase snapshots. Available operations depend on the authenticated account, its permissions and the installed modules.

## Connection

The MCP server runs remotely. This package contains its connection configuration and public branding, including the original Thissa Store SVG isotype and a transparent PNG alternative. Keep the server deployed and reachable over HTTPS. No local server, API key or WordPress installation is included or required on the client's computer.

Sign in as a Thissa Store owner or an authorized moderator with the AI Assistant add-on enabled. Approve the requested permissions on the Thissa Store consent screen. Customer accounts cannot authorize this integration. OAuth uses S256 PKCE and client metadata discovery for ChatGPT and Claude's supported web clients.

Store owners use their connected store automatically. Shared store tools accept an optional `store_id` only when it matches that account. Moderators must send the intended store ID on every store operation. Store owners query their catalog and branches directly; moderator-only tools cannot be enabled by reconnecting an owner account.

Moderator accounts may be restricted to particular stores. Search results, totals, pagination, alerts and direct operations all enforce that restriction. The review moderator account is limited to the demo store and cannot access registration leads. Provide separate owner and moderator demo credentials in the portal's private review details when testing both workflows.

Tool discovery exposes the same 20 definitions for every account so that switching between an owner and a moderator does not lose moderator tools. Every call validates the authenticated role and approved scopes. Moderators use `search_stores` with `plan="pro"` to find Pro stores. Refresh the connection's tool metadata and start a new conversation after updating the server.

Moderators use `get_attention` with `group="pending_invoices"` to list pending plan invoices for stores that are still enabled, ordered by earliest deadline, with payment links and days remaining. `due_date` indicates eligibility for store deactivation under the Payments grace period; transaction reconciliation and cron execution determine actual suspension. Read all pages for a complete list and preserve unknown deadlines. `group="unpaid_disabled"` lists disabled stores with pending invoices; `group="all"` includes every attention group.

## Suppliers, inventory and purchases

Release 1.19.0 adds eight tools, each with an explicit `branch_id`:

| Tools | Permission | Requirement |
| --- | --- | --- |
| `search_suppliers`, `get_supplier` | `suppliers:read` | POS Plus |
| `create_supplier`, `update_supplier` | `suppliers:write` | POS Plus |
| `search_inventory`, `get_inventory_history` | `inventory:read` | POS with native inventory enabled |
| `search_purchases`, `get_purchase` | `purchases:read` | POS Plus |

POS and POS Plus are add-ons distinct from the store subscription. Suppliers share one business directory; their purchase histories and balances belong to the selected authorized branch. Keep unpaid balances separate from supplier credits and refunds due, and keep currencies separate. Search operations use server pagination; follow `has_more` for complete lists. Physical stock, reserved stock and sellable stock are different quantities. External or disabled inventory is not represented as native availability.

Supplier creation and updates default to `dry_run=true`. Preview before applying with `dry_run=false` and a unique `request_id`; updates require `expected_version` from a fresh supplier read. Partial updates preserve omitted contacts. Identical retries reuse the native operation. Deactivation preserves history and excludes the supplier from new receipt selections. Moderator mutations retain the original authenticated moderator as their audit actor.

New permissions require reconnection and explicit OAuth consent. Existing tokens and refresh grants never gain these scopes automatically. Deploy both the MCP and matching POS changes before refreshing tool discovery; this ZIP only configures the remote client.

## Tool annotation justifications

All 20 tool definitions explicitly set boolean `readOnlyHint`, `destructiveHint` and `openWorldHint` values for the server's `tools/list` response. None of these required values is `null`. Deploy server changes before checking the remote values. The table explains each value for review; it does not add custom fields to the MCP annotations. Optional `idempotentHint` is listed only where the server advertises it.

| Tool | `readOnlyHint` | `destructiveHint` | `openWorldHint` | `idempotentHint` |
| --- | --- | --- | --- | --- |
| `search` | `true`: retrieves authorized catalog records and editable fields. | `false`: does not delete or overwrite catalog records. | `false`: queries the selected store's bounded catalog; accepts no arbitrary search destination. | Not advertised. |
| `get_profile` | `true`: retrieves the connected account identity and available entities. | `false`: does not modify the account or its permissions. | `false`: resolves only the authenticated account; accepts no external destination. | Not advertised. |
| `get_analytics` | `true`: computes and retrieves aggregated store metrics. | `false`: does not modify orders, customer records or catalog data. | `false`: uses authorized store analytics and owned branch filters, without public web search. | Not advertised. |
| `read_image` | `true`: reads an owned library image and returns its bytes and metadata. | `false`: does not upload, replace or delete images. | `false`: reads a validated local attachment belonging to the selected store, without arbitrary URL input. | `true`: repeating the read does not create or modify an image. |
| `prepare_image_reference` | `true`: reads an owned image and prepares a selection preview. | `false`: the tool does not upload, replace or delete an image. | `false`: accesses only the selected store's existing image; accepts no external destination. | Not advertised. |
| `search_stores` | `true`: retrieves stores matching authorized moderator filters. | `false`: does not modify stores or subscriptions. | `false`: searches Thissa Store's bounded business directory, without public web search. | Not advertised. |
| `get_store` | `true`: retrieves the selected store's details, plan and branches. | `false`: does not change the store, add-ons or connected identity. | `false`: reads an existing store within the moderator's authorized service. | Not advertised. |
| `get_store_contact` | `true`: retrieves contact fields for the selected store. | `false`: does not edit contacts or send messages. | `false`: reads contact data within the authorized service; does not contact external recipients. | Not advertised. |
| `get_attention` | `true`: retrieves store alerts and existing pending invoice details. | `false`: does not change invoices, charge payments or suspend stores. | `false`: reads authorized service records; returning an existing payment link does not submit a payment or fetch an arbitrary destination. | Not advertised. |
| `create` | `false`: persists new catalog items when `dry_run=false`. | `false`: adds new items; does not overwrite or delete existing catalog records. | `true`: can publish new items in the customer-facing catalog, including button and banner links to external destinations. | `true`: retries with the same `request_id` and identical payload reuse the recorded result instead of creating duplicates. |
| `update` | `false`: persists catalog and profile-button changes when `dry_run=false`. | `true`: can overwrite existing text, prices, images, visibility, schedules and relationships. | `true`: changes the customer-facing catalog and can publish button or banner links to external destinations. | `true`: retries with the same `request_id` and identical payload reuse the recorded result instead of applying the changes again. |
| `upload_image` | `false`: adds an image attachment to the selected store's library. | `false`: adds or reuses an attachment; does not replace or delete an existing image or assign it to a catalog item. | `true`: can download an image from a caller-supplied HTTPS URL or a client-provided file URL. | `false`: there is no operation-level request ledger guaranteeing deduplication for every supported input. |
| `search_suppliers`, `get_supplier` | `true`: read suppliers and authorized branch accounts. | `false`: preserve directory and purchase data. | `false`: use business records without contacting suppliers. | `true`: repeated reads do not mutate records. |
| `search_inventory`, `get_inventory_history` | `true`: read physical inventory and its ledger. | `false`: never change quantities or reservations. | `false`: use native authorized branch records. | `true`: repeated reads do not mutate inventory. |
| `search_purchases`, `get_purchase` | `true`: read effective documents and settlements. | `false`: never receive goods, allocate payments or record refunds. | `false`: query authorized business records. | `true`: repeated reads do not mutate purchases. |
| `create_supplier` | `false`: persists a supplier when `dry_run=false`. | `false`: creates a directory record. | `false`: does not publish the contact or contact recipients. | `true`: identical retries recover the accepted operation. |
| `update_supplier` | `false`: persists supplier fields when `dry_run=false`. | `true`: overwrites selected fields or deactivates the supplier. | `false`: does not publish contacts or alter purchases. | `true`: identical retries recover the accepted operation. |

Annotations describe the full tool, including its write-capable modes. A `dry_run=true` preview does not make `create` or `update` read-only. Writes still enforce authorization, ownership, validation and their applicable preview, version and request-ID checks. Publishing a new item is additive; overwriting an existing value is classified as destructive even when another authorized edit could restore it.

`prepare_image_reference` returns an `awaiting_selection` preview. Uploading the original into ChatGPT occurs only after the user clicks **Use as reference** in the UI; it is a separate user-triggered host action, not a side effect of the MCP tool call.

For this resubmission, deploy the complete MCP module and matching POS service changes before selecting **Scan Tools** in the OpenAI portal. Verify the scanned 20 tools and their boolean values, then enter the requested justifications using the explanations above. The ZIP contains the remote connection and public documentation, not the server implementation or a frozen tool inventory. Justifications explain the advertised values; they do not override them. See [OpenAI's MCP review requirements](https://developers.openai.com/plugins/deploy/app-review).

## ChatGPT package

The manifest includes five positive and three negative cases under `extensions.com.openai.review.test_cases`, plus publication release notes. Upload this complete ZIP to import them into **Metadata & Skills → Review information → Review details**. The positive cases cover owner catalog search, authorized category creation, analytics, operational reads and supplier writes. Negative cases cover access outside demo, unsupported permanent deletion and unsupported financial mutations.

Use the owner demo connection for owner cases and the restricted moderator connection for moderator cases. Operational owner cases require POS Plus, an authorized branch, native inventory and representative supplier/purchase fixtures. Provide their credentials only in the portal's private form. Prepare a published branch, category and product in the demo store and run the cases in the supported clients before submission. Packaged expected results are review scenarios, not a claim that conversational tests have already been executed. Keep the accessible demo recording URL in the portal; this package omits that field so an existing saved recording is preserved.

Upload the ZIP containing root `plugin.json` and `mcp.json` at https://platform.openai.com/plugins. Select the verified **Thissa Digital SAS** developer identity, verify the server domain, complete OAuth/MCP setup and inspect the scanned tools. Complete review materials and publish after approval. For a development connection, configure the MCP URL with OAuth and CIMD in ChatGPT's custom connection settings.

Official instructions: https://developers.openai.com/plugins/deploy/submission

## Claude package

The Claude ZIP contains `.claude-plugin/plugin.json` and root `.mcp.json`. Extract it into a dedicated plugin repository, preserving hidden files. Submit the repository through the Claude directory portal, or submit the remote MCP URL directly as a single connector. The portal's repository and connector routes do not use OpenAI's ZIP-upload flow.

For immediate private use, open Claude Settings > Connectors > Add custom connector, enter the MCP URL and complete OAuth. Authentication in Claude Code or other local clients may require separate client registration by the server administrator; the server's built-in client metadata trust covers ChatGPT and Claude web identities.

Official instructions: https://claude.com/resources/articles/build-plugins-for-claude

## Support and policies

- Support: https://thissa.store/support
- Privacy: https://thissa.store/politica-de-privacidad
- Terms: https://thissa.store/terminos-y-condiciones

The public directory controls the final category, publisher identity and icon presentation. Package validation does not constitute directory approval or a complete authenticated client test. Keep reviewer credentials, OAuth tokens and production customer data outside the package.
