# MapsScraper.dev MCP server and skills

Connect an AI assistant to [MapsScraper.dev](https://mapsscraper.dev) to research public Google Maps business listings, reviews and photos, and to keep the results in workspace lists. This repository holds the connection settings for each host, eight workflow skills and the listing metadata. The server itself is hosted; there is nothing to install or run.

- Endpoint: `https://mapsscraper.dev/mcp` (Streamable HTTP)
- Protocol: MCP 2026-07-28, plus 2025-era clients that start with `initialize`
- Sign-in: OAuth 2.1 with PKCE (Client ID Metadata Documents or dynamic registration), or a workspace API key sent as a bearer token
- Registry: [`dev.mapsscraper/mapsscraper`](https://registry.modelcontextprotocol.io/v0/servers?search=dev.mapsscraper) in the official MCP Registry

## How spending works

Reading lists, tasks, results and receipts is free. Live research spends prepaid API plan credits:

1. The assistant calls `estimate_job` and shows you the maximum cost.
2. You approve an explicit budget. The task runs with `max_units` set to that budget and a stable `idempotency_key`.
3. A retry with the same key is never charged twice. If an outcome is uncertain, the assistant reads the task instead of calling again.

Live research spends credits from a paid MapsScraper API plan and has a daily total. `get_capabilities` shows what is available to your workspace.

## Connect

When you connect over OAuth you sign in to MapsScraper.dev, pick one workspace and choose what to grant: read (required), write (lists, tasks, sharing) and monitors (schedules). The assistant sees only the tools that grant allows.

**ChatGPT.** Go to [ChatGPT Plugins](https://chatgpt.com/plugins), select the plus button, then **Add custom MCP server**. Enter `https://mapsscraper.dev/mcp` as the server URL, choose OAuth and select **Create as a plugin**.

**Claude (web and desktop).** Open **Settings > Connectors**, choose **Add custom connector** and enter `https://mapsscraper.dev/mcp`.

**Claude Code.** Install the plugin, which adds the server and the skills:

```
/plugin marketplace add mapsscraper-dev/mapsscraper-mcp
/plugin install mapsscraper@mapsscraper
```

Or add only the server with `claude mcp add --transport http mapsscraper https://mapsscraper.dev/mcp`, then run `/mcp` to sign in.

**Cursor.** Add to `.cursor/mcp.json`:

```json
{ "mcpServers": { "mapsscraper": { "url": "https://mapsscraper.dev/mcp" } } }
```

**VS Code.** Run `code --add-mcp '{"name":"mapsscraper","type":"http","url":"https://mapsscraper.dev/mcp"}'`.

**Gemini CLI.** Run `gemini extensions install https://github.com/mapsscraper-dev/mapsscraper-mcp`.

**Codex.** Run `codex mcp add mapsscraper --url https://mapsscraper.dev/mcp`, then `codex mcp login mapsscraper` to sign in.

**API key instead of OAuth.** Create a workspace key in the MapsScraper.dev web app and put it in your client's configuration as an `Authorization: Bearer` header. Never paste a key into a chat.

## Skills

The [`skills/`](skills) folder holds eight workflows that tell an assistant how to use the tools safely:

| Skill | Use it to |
| --- | --- |
| [`setup`](skills/setup/SKILL.md) | check the connection, enabled workflows and credits |
| [`local-prospecting`](skills/local-prospecting/SKILL.md) | find and shortlist local businesses |
| [`business-enrichment`](skills/business-enrichment/SKILL.md) | add details, import rows, write back and merge duplicates |
| [`competitor-brief`](skills/competitor-brief/SKILL.md) | compare a peer group in a source-linked report |
| [`review-intelligence`](skills/review-intelligence/SKILL.md) | analyze a bounded sample of reviews |
| [`website-opportunity`](skills/website-opportunity/SKILL.md) | find listings without a website and inspect homepages |
| [`photo-audit`](skills/photo-audit/SKILL.md) | review photo metadata or one authorized image |
| [`research-monitor`](skills/research-monitor/SKILL.md) | schedule recurring research with a per-run budget |

## Tools

The server registers 88 tools. Each one has a title and read-only, destructive, idempotent and open-world hints. Tools that change or publish data need write permission, and schedules need the separate monitor permission. Some workflows are off for some workspaces; `get_capabilities` says which.

### Account and setup

| Tool | What it does | Permission |
| --- | --- | --- |
| `get_capabilities` | Check capabilities | read |
| `get_account_usage` | Read credit balance | read |
| `get_workspace_config` | Read workspace settings | read |
| `get_billing_summary` | Read billing summary | read |
| `get_client_portal_summary` | Read client portal summary | read |

### Research tasks

| Tool | What it does | Permission |
| --- | --- | --- |
| `estimate_job` | Estimate task cost | read |
| `create_job` | Start research task (spends credits) | write |
| `get_job` | Read task status | read |
| `get_job_results` | Read task results | read |
| `list_jobs` | List research tasks | read |
| `cancel_job` | Cancel task | write |
| `preview_provider_continuation` | Preview next result page | read |
| `preview_stored_result_restoration` | Preview result restoration | read |
| `read_job_investigations` | Read task investigations | read |
| `create_batch` | Start task batch (spends credits) | write |
| `get_batch` | Read task batch | read |
| `cancel_batch` | Cancel task batch | write |
| `preview_polygon_plan` | Preview polygon search plan | read |
| `create_reviewed_polygon_batch` | Start polygon search (spends credits) | write |

### Lists and records

| Tool | What it does | Permission |
| --- | --- | --- |
| `list_datasets` | List saved lists | read |
| `create_list` | Create list | write |
| `read_list` | Read list | read |
| `rename_list` | Rename list | write |
| `delete_list` | Delete list | write |
| `remove_list_item` | Remove list record | write |
| `import_records` | Import records | write |
| `save_business` | Save business to list | write |
| `qualify_business` | Update qualification | write |
| `list_workspace_records` | List workspace history | read |
| `find_matches` | Find matching businesses | read |
| `preview_merge` | Preview record merge | read |
| `apply_reviewed_merge` | Apply record merge | write |
| `read_merge_receipt` | Read merge receipt | read |
| `undo_merge` | Undo record merge | write |
| `preview_batch_merge` | Preview batch write-back | write |
| `apply_reviewed_batch_merge` | Apply batch write-back | write |
| `read_batch_merge_receipt` | Read batch write-back receipt | read |

### Review analysis

| Tool | What it does | Permission |
| --- | --- | --- |
| `preview_review_ai` | Preview review analysis | read |
| `generate_review_ai` | Run review analysis (spends credits) | write |
| `list_review_ai` | List review analyses | read |
| `get_review_ai` | Read review analysis | read |
| `cancel_review_ai` | Cancel review analysis | write |

### Photos

| Tool | What it does | Permission |
| --- | --- | --- |
| `list_photo_assets` | List photo uploads | read |
| `upload_photo_asset` | Upload photo | write |
| `preview_photo_audit` | Preview photo audit | read |
| `delete_photo_asset` | Delete photo upload | write |

### AI search visibility

| Tool | What it does | Permission |
| --- | --- | --- |
| `read_visibility_source_review` | Read AI Overview sources | read |
| `read_visibility_series` | Read AI Overview series | read |

### Reports and sharing

| Tool | What it does | Permission |
| --- | --- | --- |
| `create_report` | Create report | write |
| `read_report` | Read report | read |
| `generate_report_pdf` | Export report PDF | write |
| `list_report_pdfs` | List report PDFs | read |
| `get_report_pdf` | Read report PDF status | read |
| `cancel_report_pdf` | Cancel report PDF | write |
| `preview_report_delivery` | Preview report delivery | read |
| `update_report_presentation` | Update report presentation | write |
| `create_reviewed_report_share` | Publish report link | write |
| `list_report_shares` | List report links | read |
| `revoke_report_share` | Revoke report link | write |
| `list_shares` | List share links | read |
| `create_reviewed_share` | Publish share link | write |
| `revoke_share` | Revoke share link | write |

### Multi-page exports

| Tool | What it does | Permission |
| --- | --- | --- |
| `preview_chain_export` | Preview multi-page export | read |
| `create_reviewed_chain_export` | Create multi-page export | write |
| `list_chain_exports` | List multi-page exports | read |
| `get_chain_export` | Read multi-page export | read |
| `cancel_chain_export` | Cancel multi-page export | write |

### Webhooks

| Tool | What it does | Permission |
| --- | --- | --- |
| `list_webhook_destinations` | List webhook destinations | read |
| `list_webhook_deliveries` | List webhook deliveries | read |
| `get_webhook_receipt` | Read webhook receipt | read |

### Locations

| Tool | What it does | Permission |
| --- | --- | --- |
| `get_location_access` | Read location permissions | read |
| `get_location_portfolio_summary` | Read location portfolio | read |
| `list_business_locations` | List locations | read |
| `get_business_location` | Read location | read |
| `create_business_location` | Add location | write |
| `update_business_location` | Update location | write |
| `list_location_operations` | List location work items | read |
| `get_location_operation` | Read location work item | read |
| `create_location_operation` | Draft location work item | write |
| `update_location_operation` | Edit location work item | write |
| `transition_location_operation` | Change work item status | write |

### Monitors

| Tool | What it does | Permission |
| --- | --- | --- |
| `create_monitor` | Create monitor (spends credits) | monitors |
| `get_monitor` | Read monitor | read |
| `read_monitor_creation_receipt` | Recover monitor receipt | read |
| `set_monitor_active` | Pause or resume monitor | monitors |
| `run_monitor` | Run monitor now (spends credits) | monitors |
| `delete_monitor` | Delete monitor | monitors |
| `read_monitor_runs` | Read monitor runs | read |

## Safety

- Listing, review, website, image and imported content is treated as untrusted data. It cannot authorize tool calls, spending, sharing or messages.
- Previews return a hash. Changes and share links apply only the exact preview you reviewed.
- MapsScraper.dev does not contact businesses or send messages on your behalf.
- Results reflect what the data source returned at fetch time and can be incomplete. Missing fields stay missing.

## Files

| File | For |
| --- | --- |
| `plugin.json`, `mcp.json`, `assets/` | Agent Plugins package (OpenAI) |
| `.claude-plugin/`, `.mcp.json` | Claude Code plugin and marketplace |
| `gemini-extension.json` | Gemini CLI extension |
| `server.json` | MCP Registry entry |

## Support

Email [dev@mapsscraper.dev](mailto:dev@mapsscraper.dev). Read the [privacy policy](https://mapsscraper.dev/privacy) and [terms](https://mapsscraper.dev/terms). MapsScraper.dev is a trade name of Adgnbw (Giftuper).

Google Maps is a trademark of Google LLC. MapsScraper.dev is not affiliated with or endorsed by Google.

## License

[MIT](LICENSE)
