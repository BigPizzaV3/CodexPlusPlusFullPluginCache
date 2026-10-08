# LunarCrush interfaces

Use this reference only when selecting or operating a LunarCrush interface. Keep these implementation details behind the user-facing answer unless the user asks how to reproduce, export, or integrate the data. Confirm live help and tool schemas when available.

## CLI

Prefer CLI output as JSON for analysis and Markdown/default output for quick human inspection.

```bash
lunarcrush categories --json
lunarcrush category cryptocurrencies --filter meme --sort market_cap --limit 100 --json
lunarcrush topic bitcoin --json
lunarcrush topic bitcoin time-series --interval 1m --bucket day --metrics interactions,posts_active,contributors_active --json
lunarcrush topic bitcoin posts --start 2026-08-01 --end 2026-08-07 --network twitter,youtube --limit 100 --json
lunarcrush keyword "artificial intelligence" --json
lunarcrush keyword "artificial intelligence" time-series --interval 1m --bucket day --network reddit --json
lunarcrush keyword "artificial intelligence" posts --interval 1w --limit 100 --json
lunarcrush creators bitcoin --limit 100 --json
lunarcrush creator youtube mrbeast --json
lunarcrush creator youtube mrbeast time-series --interval 1m --bucket day --json
lunarcrush creator youtube mrbeast posts --interval 1m --limit 100 --json
lunarcrush post tweet 1973189127144349980 --json
lunarcrush search "bitcoin etf" --json
lunarcrush /topic/bitcoin/time-series --json
lunarcrush whoami --json
```

Quote every topic, keyword, handle, or query containing whitespace, `#`, `$`, or shell metacharacters. Never interpolate untrusted text into a shell command without argument-safe quoting.

Common flags:

- `--json`, `--csv`, `--tsv`, or `--format <json,csv>`: choose output format.
- `--interval <1d|1w|1m|3m|6m|1y|all>`: choose a relative range.
- `--start <YYYY-MM-DD|unix>` and `--end <YYYY-MM-DD|unix>`: choose an exact range.
- `--bucket <hour|day>`: choose historical granularity.
- `--network <comma-separated networks>`: filter posts or time series.
- `--metrics <comma-separated keys>`: limit time-series columns.
- `--sort`, `--filter`, `--limit`, and `--page`: rank and paginate lists.
- `--url`: inspect the resolved URL and detect dropped/unsupported flags; do not assume its host because CLI configuration can override it.
- `--ui`: open the corresponding visual interface only when the user requests it.

Run `lunarcrush --help` because installed CLI versions can lag hosted documentation. Hosted CLI documentation may include `favorites` and `collections`; do not assume they exist locally. Use `lunarcrush update` only with user approval.

## MCP

Connect to the Streamable HTTP server at `https://lunarcrush.ai/mcp`. Prefer a specialized read-only tool when present. The observed tool set includes:

| Need | Specialized tool |
| --- | --- |
| Categories or category topics | `list` |
| Topic snapshot | `topic` |
| Topic history | `topic_time_series` |
| Topic top posts | `topic_posts` |
| Exact keyword history | `keyword_time_series` |
| Exact keyword top posts | `keyword_posts` |
| Creator snapshot/history/posts | `creator`, `creator_time_series`, `creator_posts` |
| Single post | `post` |
| Ranked crypto or stock lists | `cryptocurrencies`, `stocks` |
| Entity discovery | `search` |
| Valid path without a specialized tool | `fetch` |
| Subscription and rate limits | `auth` |

Use the connected tool schema, not this snapshot, for accepted enums and field names. Current specialized tools generally accept limits up to 1000; topic/keyword/creator history accepts interval and metric selection; posts accepts interval or date range and network filters.

Use `fetch` for paths such as `/creators/bitcoin` or `/list/cryptocurrencies/alt_rank/100` when no specialized tool covers the request. Do not handcraft MCP JSON-RPC when a connected MCP tool is available.

Map exact post dates carefully: current MCP post tools use `from_date` and `to_date`, while CLI and HTTP use `start` and `end`. Current MCP `topic_time_series` does not expose a network filter; if network-filtered topic history is required, use MCP `fetch`, the CLI, or HTTP rather than silently dropping the filter.

## AI-ready HTTP at lunarcrush.ai

Base URL: `https://lunarcrush.ai`

Authenticate with `Authorization: Bearer <API_KEY>` through a secure client configuration. Responses are Markdown by default; request `?format=json` for computation or `?format=csv` for tabular transfer. URL-encode each dynamic path segment and query value.

| Data | Path pattern |
| --- | --- |
| Categories | `/categories` |
| Topics in a category | `/category/{category}` |
| Topic snapshot/history/posts | `/topic/{topic}`, `/topic/{topic}/time-series`, `/topic/{topic}/posts` |
| Exact keyword snapshot/history/posts | `/keyword/{keyword}`, `/keyword/{keyword}/time-series`, `/keyword/{keyword}/posts` |
| Influential creators for a topic | `/creators/{topic}` |
| Creator snapshot/history/posts | `/creator/{network}/{id}`, `/creator/{network}/{id}/time-series`, `/creator/{network}/{id}/posts` |
| Single post | `/post/{network-or-post-type}/{id}` |
| Search | `/search/{query}` |
| Ranked market lists | `/list/cryptocurrencies/{sort}/{limit}`, `/list/stocks/{sort}/{limit}` |

Use the query parameters represented by the CLI flags when supported: `interval`, `start`, `end`, `bucket`, `network`, `metrics`, `sort`, `filter`, `limit`, and `page`. Read returned `config` to confirm which parameters took effect.

## Versioned JSON API v4

Use API v4 only when an application needs a documented versioned JSON schema or the AI-ready interfaces do not expose the required family. Base URL: `https://lunarcrush.com/api4/public`. Read the current contract at `https://lunarcrush.ai/api` before implementation.

Documented families include:

- Topic list, topic snapshot, AI “whatsup,” time series, posts, news, and creators.
- Category list, category snapshot, topics, time series, posts, news, and creators.
- Creator list, creator snapshot, time series, and posts.
- Post details and post time series.
- Coin list, coin detail, time series, and metadata.
- Stock list, stock detail, and time series.
- Custom search test, list, detail, create, update, and delete.
- System changes.

Endpoint versions differ by family and can change when schemas change; never invent a version suffix. Use the exact current path from the API documentation. Treat search create/update/delete as mutations.

## Fallback rules

1. Honor the interface requested by the user.
2. In a connected chat, use a specialized MCP tool, then `fetch` for gaps.
3. In a shell environment, use the named CLI command; if it lacks a named command, use `lunarcrush /<path>`.
4. Use AI-ready HTTP when MCP/CLI is unavailable or the user wants a shareable page or direct response format.
5. Use API v4 for stable application contracts or data families available only there.
6. If access is limited, explain the practical limitation in plain language; do not replace censored or absent values with estimates.
