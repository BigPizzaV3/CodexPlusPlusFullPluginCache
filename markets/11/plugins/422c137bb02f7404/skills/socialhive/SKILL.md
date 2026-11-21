---
name: socialhive
description: Draft and manage social content through the connected SocialHive MCP server.
---

# SocialHive

Use this skill to draft, adapt, schedule, publish, and analyze social content through the SocialHive MCP server.

## Instructions
1. **Channels first**: Before creating or scheduling anything, call `list_channels` and use the real channel ids it returns. Never invent channel or post ids.
2. **Drafting**: Use `generate_text` for new copy and `adapt_post` to tailor one message for several platforms. Use `generate_image` or `list_media` / `upload_media` / `import_media` for visuals.
3. **Creating posts**: Use `create_post`. Without `publishNow` or `scheduledAt` it saves a draft. Prefer drafts unless the user clearly asks to publish.
4. **Scheduling**: To schedule an existing post, find it with `list_posts` or `get_post`, convert the requested time to an ISO 8601 UTC timestamp, then call `schedule_post`. Tell the user the exact scheduled time.
5. **Publishing**: `publish_post`, `publish_article`, and `create_post` with `publishNow` post publicly. Confirm with the user before calling them.
6. **Approvals**: Posts may return `pending_approval` when the workspace requires approval. Report this instead of retrying.
7. **Analytics**: Use `get_analytics` for impressions, engagement, and top posts.
8. **Articles and sources**: Use `list_articles`, `get_article`, `create_article`, and `list_connected_sites` for long-form content, and `list_sources` / `search_source_items` for content ideas.
9. **Workflows**: `propose_workflow` only saves a draft that a person must activate in Workflow Studio. Say so when you use it. Use `list_workflows` and `list_node_types` to inspect existing automation.
10. **Out of scope**: Do not expose credentials or tokens, and decline requests unrelated to social content management.
