---
name: manage-brand
description: Create or edit a CreceRank brand, its country, name variations, and analysis prompts. Use when the user wants to add a site, switch brands, rename the brand, or change the questions used in scans.
---

Use this skill when the user is changing brand setup or prompts, not when they only want the latest score.

If the user gives a different instruction, follow that instruction.

1. Call `crecerank_whoami`, then `crecerank_list_brands`.
2. If they name a brand that is not active, call `crecerank_set_active_brand`.
3. Call `crecerank_get_brand` before editing so you show the current URL, country, variations, and prompts.
4. For a new or replacement site, call `crecerank_list_countries` when the country is unclear, `crecerank_validate_brand_url`, then `crecerank_setup_brand`. Use `crecerank_create_brand` only when they want an extra brand that should not become active yet. Trial plans cannot create extra brands.
5. Call `crecerank_url_brand_hints` before saving generated names. Call `crecerank_update_variations` to save the name list. Call `crecerank_patch_official_name` to set the display name. An empty official name clears the override.
6. To replace prompts, call `crecerank_update_prompts` with `text` and `included_in_scan`. Each text must be 10–300 characters. To generate and save a new set, call `crecerank_suggest_prompts` for prompts only, or `crecerank_suggest_setup` when they also want new name variations. Both writes replace saved rows. Say that before calling them.
7. Call `crecerank_list_deleted_prompts` when they ask what was removed. MCP cannot restore those prompts.
8. Call `crecerank_delete_brand` only after they name the exact URL and confirm a permanent delete. It requires `mcp.destructive`. If the tool returns a scope error, ask them to reconnect and allow deletes.

Do not start a scan from this skill unless they also asked to measure visibility.
