---
name: getting-started
description: Set up and orient a person in CitationLab Marketing Manager. Use when they first install the plugin, ask what CitationLab can do, or you do not yet know which project to work in.
---

# Getting started with CitationLab

1. Call `list_projects`. It returns the projects the person can access, each with its `id` (a project token).
2. For the project they pick, call `get_integration_status` with `projectId` to see which data sources are connected (Search Console, GA4, Google Ads, Meta Ads and so on), and `get_project_summary` for an overview.
3. Summarise briefly in the person's own language: which projects they have, what is connected, and three things they can ask right now. Do not paste the raw result.
4. Ask which project and which goal they want to start with.

## Rules that apply to every CitationLab task

- **Projects are addressed by token.** Pass the project's `id` from `list_projects` or `get_project` as `projectId`, never its name.
- **Name things by their name.** Campaigns, keywords, pages and actions are shown to the person by name (and actions by their key, such as `ELNO-142`), never by an internal numeric id.
- **Almost everything only reads.** `create_action`, `update_action` and `add_action_comment` are the only tools that change anything, and only in the person's CitationLab workspace (and a paired Jira issue). Say what you will write and get a yes first.
- **A missing integration is not an error.** If a tool says a data source is not connected, say which one and that it is connected in the CitationLab app under the project's integrations.
