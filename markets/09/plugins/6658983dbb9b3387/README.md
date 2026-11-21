# MakeBox for Etsy

Version **0.3.12** provides an Etsy SEO strategist and eight guided workflows. It is useful without an MCP connection: supply product facts, a photo, pasted listing or CSV, and receive complete copy-ready fields, a settings worksheet and clearly marked unresolved facts. The same knowledge supports connected execution through the seller's authorized MakeBox workspace.

The manager combines SEO, product positioning, conversion copy, options, delivery and careful shop operations. It does not guess material, package size, search volume, delivery promises or ranking outcomes. Long descriptions are returned in full with their factual sections preserved. [Worked examples](references/worked-examples.md) and [fillable templates](templates/product-brief.md) demonstrate the result.

## Use without a connector

Ask “create a complete listing from these product details,” “improve this pasted description without losing specifications,” or “analyze my keyword CSV.” The plugin prepares title, complete description, tags, applicable attributes/materials, personalization, options and shipping/digital settings. Missing facts are listed outside buyer-facing copy. Manual handoff tells the seller what to paste/select in Etsy and inspect before publication. No account, token or subscription is needed to use the instruction content; the host's own model/access rules still apply.

The standalone package contains the same skills, role, guides, examples and optional QA with an empty MCP configuration. The connected package adds the remote MakeBox declaration; its editorial work still works when tools are not connected. An agent definition does not force every client to launch a separate agent. The coordinating skill carries the role in clients that support skills but not agent files.

## Optional live Etsy operations

The server exposes adapters for all 105 operations in the official Etsy API snapshot dated October 1, 2026, alongside MakeBox workflows. The bundled operation index/input schemas were checked against the local runtime on October 4. Live tool schemas remain authoritative. This covers published API operations, not every Etsy website feature. Availability depends on scopes, app access, valid product data and MakeBox access. Direct Etsy transport does not invoke another model or debit MakeBox AI allowances; Etsy fees can still apply.

## Connect and use

Install the connected variant, then connect **MakeBox** through OAuth when you need live operations. Use `list_shops` and `get_account_status` to identify workspace/access. Private actions bind the seller's shop; public research may read other shops. Connection is not required for copy preparation.

When the connected server exposes `open_makebox_workspace` and the client supports MCP Apps, you can open a read-only visual catalogue, inspect listings and photos, and bring a selected listing into the conversation. Optional buttons start a conversation about creating, improving or researching a listing; they do not themselves generate content or change Etsy. The server and host determine availability. Existing text tools remain the fallback.

Try “change this listing's shipping profile,” “create an Etsy draft from this finished copy,” “show my latest orders and payment ledger,” or “research relevant keywords.” Claude uses the live tool schemas rather than a fixed list embedded in the plugin. If an existing conversation lacks newly added tools, refresh the connector or start a new conversation; discovery and caching depend on the client.

A direct `etsy_*` action uses Etsy IDs and does not require a MakeBox import first. Writes need authorization for the exact target and values. A successful HTTP response is separate from a fresh readback proving the final state. Existing MakeBox draft, research, optimization and bulk-job tools remain available when those workflows are requested. Image and video generation are not provided by this MCP connector; existing files can be uploaded and managed.

## Data and support

The connector sends the selected tool request to MakeBox at `https://mcp.makebox.ai/mcp`, which calls Etsy with the seller's OAuth authorization. Direct operations may include listing content, order and buyer details, shipping information, payment records and shop policies. Display only the data needed for the seller's task. Optional personal Etsy email/address methods require additional Etsy consent; the ordinary connection does not gain these permissions automatically.

The plugin contains no credentials or autonomous background worker. Seller-owned files are uploaded only within authorization through `get_upload_link` or the Asset Library; direct multipart fields use `asset_id`. Never share tokens or arbitrary paths.

See the [MakeBox homepage](https://www.makebox.ai/), [plugin documentation](https://github.com/russol07/makebox-etsy-plugin#readme), [privacy policy](https://www.makebox.ai/privacy), [terms of service](https://www.makebox.ai/terms), and [support/contact page](https://www.makebox.ai/contact). Plugin use is governed by the bundled [proprietary license](LICENSE).

## Components

- `agents/makebox-etsy-manager.md`: coordinates work in Cowork and Claude Code.
- `skills/makebox-shop-manager/SKILL.md`: the coordinating role in ordinary Claude chat.
- `skills/use-etsy-api/SKILL.md`: direct API discovery, authorization, transport and readback.
- `skills/visual-etsy-workspace/SKILL.md`: safe visual catalogue access when available.
- `skills/create-etsy-listing/SKILL.md`: complete listing drafts, options, policies and media.
- `skills/optimize-etsy-listing/SKILL.md`: chat-authored improvements or explicitly requested MakeBox AI jobs.
- `skills/manage-etsy-orders/SKILL.md`: current orders, transactions, payment records and authorized fulfillment.
- `skills/research-etsy-market/SKILL.md`: public Etsy observations and MakeBox keyword evidence.
- `skills/manage-etsy-shop/SKILL.md`: shipping, returns, sections, processing and shop settings.
- `references/direct-etsy-api-guide.md`: the direct connector contract and examples.
- `.mcp.json`: the remote server URL; server code and credentials are not bundled.

## Knowledge and checks

The [plugin map](references/plugin-map.md) routes the agent/skills to facts, copy, keyword evidence, variants, personalization, delivery/packaging, media/digital, orders, API recipes and 105 schemas. Load task-specific guides progressively, not the whole catalogue into every copy request.

Use the [listing release checklist](checklists/listing-release.md) to review product facts, listing structure and operational details. Recipes contain illustrative IDs and must never be executed unchanged.

Claude chat uses the coordinating skill where agent files are not loaded; compatible Cowork/Code runtimes can load the manager agent. Codex packaging exposes the same role through its onboarding skill, without claiming an unsupported agent loader. Muse connector installation alone does not install these Markdown instructions; import them only through capabilities Muse actually provides or use them as project instructions. Remote tool changes come from MCP; knowledge changes require a plugin update. Prepared archives or an updated GitHub package do not mean a marketplace review is approved. See [CHANGELOG.md](CHANGELOG.md).
