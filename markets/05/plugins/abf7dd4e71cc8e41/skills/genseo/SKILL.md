---
name: genseo
description: Use Genseo through its remote MCP server to inspect AI visibility, tracked prompts, cited sources, competitors, projects, keywords, SEO drafts, audits, publishing integrations, and webhooks.
---

# Genseo

Use the connected Genseo MCP tools instead of calling internal application routes or the database.

## Workflow

1. Call `genseo_me` and `genseo_projects_list` before any project operation.
2. Ask the user to select exactly one accessible project when the intended project is not already explicit. Never guess a project ID or silently switch projects.
3. Include the selected `project_id` with every project operation.
4. Read an existing post before updating it and send only intentional changes.
5. For AI visibility questions, start with `genseo_visibility_overview`; use the prompt-list and prompt-detail tools only when the user asks for prompt-level evidence.
6. Prefer creating a draft before generating or publishing content.
7. Check `genseo_integrations_list` before publishing.
8. Ask for confirmation before `genseo_posts_publish` unless autonomous publishing was explicitly requested.

Treat authorization and project-boundary errors as final. OAuth access never includes billing, team management, credentials, or project deletion. Viewer roles stay read-only, and writes require Agent Autonomy. Back off on rate limits, and treat `202 Accepted` as successful queueing.

For endpoint details and error codes, use [the Genseo developer documentation](https://docs.genseo.co/developers/overview).
