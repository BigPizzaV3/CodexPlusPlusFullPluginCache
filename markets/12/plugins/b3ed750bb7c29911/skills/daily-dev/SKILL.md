---
name: daily-dev
description: Use the daily.dev Public API to explore a user's personalized feed, trending posts, bookmarks, custom feeds, filters, notifications, and profile, or make requested changes to those resources.
---

# daily.dev

Use this skill when the user asks about their daily.dev account or developer reading feed. The canonical API reference is https://docs.daily.dev/public-api/ and its OpenAPI specification is https://api.daily.dev/public/v1/docs/json. Use of the API is subject to https://r.daily.dev/tos. Check the live specification for endpoint parameters and request bodies before an unfamiliar operation; do not guess fields.

## Connect and choose tools

In ChatGPT Work, use the daily.dev MCP connection bundled with this plugin. When it is not linked, guide the user through the connection's OAuth sign-in; do not ask for a personal access token in chat. Once linked, inspect the connected MCP tool names, descriptions, and input schemas and select the tool matching the task. Do not invent a tool name or call the REST API from a hosted environment in place of the connected tool. Report a connection or scope error as such.

The endpoint map below helps choose a workflow and supports local environments. MCP tool names and input schemas are authoritative for MCP calls; the OpenAPI spec is authoritative for direct REST calls. Do not assume one-to-one tool names or arguments from REST paths.

## Local REST fallback and token

Only if a local agent has no MCP connection and can access `api.daily.dev`, the Public REST API uses `https://api.daily.dev/public/v1` and `Authorization: Bearer <token>`. The user can generate a personal access token at https://daily.dev/settings/api. Use `DAILY_DEV_TOKEN` from the local environment or an existing secure credential store if available. If absent, explain setup in their own environment; never request a token in chat. Do not print, log, commit, include in a URL, or transmit it to any host other than `api.daily.dev`. Treat a token beginning `dda_` as secret.

Use an HTTP-capable tool or terminal for the fallback only when network access is permitted. If neither a connected MCP tool nor local REST access is available, describe the concrete setup needed and avoid implying account data was fetched.

## Find the right endpoint

Paths below are relative to the REST base URL. They are a practical map, not MCP tool names or a substitute for the live OpenAPI request and response schemas.

| Task | Endpoint and useful parameters |
| --- | --- |
| Personalized reading | `GET /feeds/foryou?limit=10`; use `cursor` for later pages. |
| Trending or active discussion | `GET /feeds/popular` (`tags` is a comma-separated list); `GET /feeds/discussed` (`period` is 1–30 days, with optional `tag` or `source`). |
| Topic or publisher feed | `GET /feeds/tag/{tag}` or `/feeds/source/{source}`. Search names first if needed. |
| Search content | `GET /search/posts?q=...` with optional `time=day|week|month|year|all`; `GET /search/tags?q=...`; `GET /search/sources?q=...`. |
| Post and discussion | `GET /posts/{id}` and `GET /posts/{id}/comments` (optional `sort`, `limit`, `cursor`). |
| Saved reading | `GET /bookmarks/` (optional `unreadOnly`, `listId`); `GET /bookmarks/search?q=...`; `GET /bookmarks/lists`. |
| Custom feeds | `GET /feeds/custom/`, `/feeds/custom/{feedId}`, and `/feeds/custom/{feedId}/info`; `GET /feeds/custom/advanced-settings` lists available advanced settings. |
| Personal settings | `GET /feeds/filters/` for global filters or `/feeds/filters/{feedId}` for one custom feed; `GET /profile/`, `/profile/experiences/`, `/profile/stack/`. |
| Notifications and catalog | `GET /notifications/`, `/notifications/unread/count`, and `/tags/`. |

Most list routes accept `limit` and `cursor`; the OpenAPI spec supplies the exact range for each route. Use `GET /profile/stack/search?query=...` to find a tool before adding it to the profile.

## Common changes

For MCP changes, inspect the selected tool's schema and annotations before calling it. For direct REST changes, look up the current request schema. `POST /bookmarks/` accepts `postIds` and optionally `listId`; `DELETE /bookmarks/{id}` removes a bookmark, and `POST /bookmarks/lists` creates a folder with `name` and optional `icon`. Bookmark folders are not enabled on every account; the move route is `PATCH /bookmarks/{id}` and it returns an error when the account cannot use folders.

`POST /feeds/custom/` creates a custom feed; `PATCH /feeds/custom/{feedId}` changes it; `DELETE /feeds/custom/{feedId}` removes it. Settings include `name`, `icon`, sorting, time range, engagement thresholds, and filters. For advanced settings, read `/feeds/custom/advanced-settings` before `PATCH /feeds/custom/{feedId}/advanced`. Global tag/source follow and block operations use `POST /feeds/filters/{tags|sources}/{follow|unfollow|block|unblock}`; for a custom feed, insert `{feedId}` after `/feeds/filters/`. Their bodies use `tags` or `sources` respectively.

Profile updates use `PATCH /profile/`; experiences use `/profile/experiences/`; tech stack items use `/profile/stack/`. Inspect the live schema for required fields and valid enum values. Do not create an account via the signup endpoint unless the user expressly asks to do so.

## Request and response workflow

1. Choose the smallest read or requested change. Prefer the connected MCP tool and its declared schema in ChatGPT Work. For local REST, check the exact route, parameters, and JSON body in the OpenAPI spec when unfamiliar. For example, inspect `.paths["/feeds/foryou"].get` and follow any `$ref` into `.components.schemas`.
2. Use the connected tool when present. For a local REST fallback with `DAILY_DEV_TOKEN` already set, a simple read is:

   ```bash
   curl --fail-with-body --silent --show-error \
     -H "Authorization: Bearer $DAILY_DEV_TOKEN" \
     'https://api.daily.dev/public/v1/feeds/foryou?limit=10'
   ```

   For user-supplied queries, use an HTTP client's parameter encoder or `curl --get --data-urlencode 'q=your topic'` rather than constructing a raw URL. Encode path segments too. Never use shell tracing while a token is loaded or interpolate untrusted text into a shell command.
3. Paginated results return `data` plus `pagination.hasNextPage` and `pagination.endCursor`. Pass that end cursor as `cursor` only when another page is useful. Avoid fetching an entire account by default.
4. For a briefing, select relevant posts and link their original article or daily.dev post URLs. An API summary or engagement count does not establish an article's full claims or accuracy; read original sources when a detailed synthesis depends on them.
5. For mutations, resolve IDs, inspect the intended target, and confirm destructive deletion or broad changes. Report the actual API result. Do not expose private account data beyond the user's request.

Check rate limit headers and honor `Retry-After` on HTTP 429. For local REST, a 401 indicates a missing or invalid token. For MCP, guide the user through reconnecting OAuth when authorization fails. A 403 can indicate a missing scope, a capability the account does not have, or an unconfirmed account; explain the returned error rather than assuming which.
