---
name: daily-dev-ask
description: Research a technical question using daily.dev's community-curated article recommendations, then answer with links and clear limits of the retrieved evidence.
---

# daily.dev Ask

Use this skill for technical questions when the user asks for daily.dev sourced research or community-vetted developer articles. This skill uses the Public API, subject to https://r.daily.dev/tos. The recommendations endpoints are experimental and can change. Check https://api.daily.dev/public/v1/docs/json for current parameters and availability.

## Access

In ChatGPT Work, use the bundled daily.dev MCP connection and its OAuth sign-in. Inspect the available search or recommendation tools and their schemas; do not invent names or assume REST parameters are MCP parameters. Follow the token handling instructions in `daily-dev` only for a local REST fallback. Never ask the user to paste a token in chat. These recommendation capabilities are not available to every account; report access errors accurately. If neither a connected MCP tool nor local REST access is available, say that live daily.dev research could not run.

## Research

The experimental REST recommendation endpoints differ from ordinary `GET /search/posts`: they return compact article metadata and community engagement signals intended for research. Verify current availability in the MCP tool list or, for local REST, the OpenAPI spec.

| Search | Endpoint | Best use |
| --- | --- | --- |
| Keyword | `GET /recommend/keyword?q=...&limit=20` | Specific technologies, names, and technical terms. Supports `cursor` for another page. |
| Full text | `GET /search/posts?q=...` | Natural-language questions, and a fallback whenever keyword recommendations return little. |

For direct REST, both accept a `time` filter such as `month`, `year`, or `all`; `limit` is 1–20 for recommendations and 1–50 for search. URL-encode the query. With `DAILY_DEV_TOKEN` set locally, one shell pattern is:

```bash
curl --fail-with-body --silent --show-error --get \
  -H "Authorization: Bearer $DAILY_DEV_TOKEN" \
  --data-urlencode 'q=RAG vs fine-tuning' \
  --data-urlencode 'limit=20' \
  'https://api.daily.dev/public/v1/recommend/keyword'
```

1. Start with a focused keyword query, then widen with a full-text search using the user's own wording. Use a recent time window for current topics; broaden when results are sparse. Follow up on relevant terms, frameworks, or gaps; stop when searches cease adding useful articles.
2. Merge results by post `id`. Inspect `title`, `url`, `summary`, `tags`, `source`, `readTime`, `numUpvotes`, and `numComments` when returned. Upvotes and comments help prioritize reading, but do not prove technical correctness. A short summary may omit crucial caveats.
3. Open the most relevant original articles for precise claims and, when the question concerns current software behavior, check official documentation too. Note publication dates and conflicting perspectives. If only titles and summaries are available, limit the answer to what those fields support.
4. Answer directly with links near the supported claims. Include a compact list of the most useful articles with title, publisher, and relevant engagement data when helpful. Say what the available material does not answer. If no results appear, report the gap instead of inventing sources.

For MCP authorization errors, guide the user through reconnecting OAuth. For local REST 401, guide the user to regenerate a token at https://daily.dev/settings/api. A 403 may mean a missing scope, a capability the account does not have, or that account confirmation is required. On 429, respect `Retry-After` and retry only as needed; do not run unlimited queries.
