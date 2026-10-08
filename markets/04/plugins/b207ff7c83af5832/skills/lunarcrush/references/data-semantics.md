# LunarCrush data semantics

Use these definitions before interpreting or combining LunarCrush results.

## Entity model

- **Category**: An aggregation and ranking of a curated collection of topics. Cryptocurrency and stock categories may include market fields not present for general categories.
- **Topic**: An entity-aware aggregation of social posts that impact or mention a tracked subject, asset, stock, or custom collection slug. Topic identity can differ from literal text matching.
- **Keyword**: Exact word or phrase analytics. Use this for literal language rather than a tracked entity. Never silently substitute it for a topic.
- **Custom collection/search**: A user-defined aggregation, commonly represented by an `lc...` slug. Its search definition determines inclusion; inspect it before interpreting results.
- **Creator**: A network-scoped account identified by screen name or unique ID. The same handle on two networks is not one creator.
- **Post**: A network/post-type scoped item. Preserve the returned network or post type; Twitter/X APIs may use `twitter`, `x`, or `tweet` in different positions.
- **Market asset**: A cryptocurrency or stock attached to a LunarCrush topic and market identifier. Resolve ambiguous symbols through search or numeric IDs.

Supported social sources are Twitter/X, YouTube, TikTok, Reddit, Instagram, and News. Creator endpoints generally represent social accounts and may not accept News.

## Time and aggregation

- Snapshot metrics usually represent the latest rolling 24 hours and often compare them with the previous 24 hours. A topic summary may contain roughly 48 hours of comparative context.
- Time-series rows are historical observations at the requested hour or day bucket. Read `config.start`, `config.end`, `config.bucket`, and `config.generated` when returned.
- `interval` is a convenience window. Exact `start` or `end` parameters override it on documented endpoints.
- Default history is commonly one week of hourly data; one month or longer commonly defaults to daily data. Always specify bucket when the analytical result depends on granularity.
- Timestamps are Unix seconds or UTC dates unless the response states otherwise. Report UTC and convert to local time only when useful.
- `generated` describes response/data generation time. It is not the timestamp of the latest source post or necessarily the last time-series bucket.

Do not compare a rolling snapshot to a single hourly or daily bucket as equivalent values. Do not sum `*_active` values across buckets to estimate unique totals; the same active post or creator can appear in multiple buckets.

## Core social metrics

| Key | Meaning | Interpretation guardrail |
| --- | --- | --- |
| `interactions` / `interactions_24h` | Publicly measurable engagements such as views, likes, comments, shares, retweets, and upvotes | Composition differs by network; large view-based networks can dominate |
| `posts_active` / `num_posts` | Unique posts receiving activity in the relevant rolling window | Call this Mentions in product language; it is not always newly created posts |
| `posts_created` | New posts created in the bucket/window | Use for publishing volume, not total active conversation |
| `contributors_active` / `num_contributors` | Unique creators with posts receiving activity | Do not sum across buckets for a unique-period total |
| `contributors_created` | Unique creators publishing new posts | Distinct from all creators whose older posts remain active |
| `sentiment` | Percentage positive, weighted by interactions | 50 is balanced, not “50% of posts positive” unless the endpoint explicitly returns post counts |
| `spam` | Posts classified as spam | Classification coverage and thresholds may evolve |
| `social_dominance` | Share of relevant social activity versus the comparison universe/category | State the comparison scope when available |
| `topic_rank` | Relative topic rank across LunarCrush topics | Lower rank is generally stronger; verify returned context |
| `influencer_rank` / creator rank | Relative creator influence | Preserve topic/category/network scope |

Post-level `post_sentiment` can use a 1–5 score while aggregate `sentiment` uses a 0–100 percentage. Do not combine the scales directly.

## Market metrics

Market-linked topics can return `close`, `open`, `high`, `low`, `market_cap`, `market_dominance`, `volume_24h`, `circulating_supply`, `percent_change_*`, `alt_rank`, and `galaxy_score`.

- Treat `close` as the price at a time-series point, not necessarily a final exchange close.
- Treat AltRank as relative market-plus-social performance and Galaxy Score as health relative to the asset’s own market/social history.
- Do not infer price movement from social engagement when market fields are absent.
- Do not compare rankings across differently filtered lists without preserving the list universe, sort, and time.

## Posts and completeness

Topic, keyword, category, and creator post endpoints return top posts ranked by the interface’s contract, commonly interactions. They are not a guarantee of every matching post in the archive.

When a user asks for “all posts”:

1. Use the maximum allowed limit and paginate if the response exposes pages.
2. Preserve the requested date and network filters.
3. Follow explicit next-page or total-page metadata. If none exists, continue sequentially until the endpoint’s documented terminal condition; do not assume a short page proves completion.
4. Deduplicate by stable post ID. Ranked results can move between page requests, so retain generation timestamps and disclose possible pagination drift.
5. Verify whether `start`/`end` filters post creation time, activity time, or another timestamp. If the contract is silent, check returned post timestamps and avoid claiming “published during” the range.
6. Verify whether post `interactions` is cumulative/current or accrued inside the requested range. Do not label a sum as period-only engagement unless documented.
7. State that the result is all rows returned by the public endpoint, not necessarily the full LunarCrush archive.
8. If exhaustive raw access is required, explain that it may require a higher-access export or plan feature beyond the public ranked-post endpoint.

Limited-data placeholders, redacted values, absent fields, and empty pages are unknown/limited—not zero. Network absence can mean no coverage, no matching result, endpoint exclusion, plan limits, or genuine zero; distinguish these using metadata where possible.

## Comparison checklist

Before computing change, correlation, rank movement, or cross-entity comparisons, match:

- Entity type and resolved ID/slug.
- Time range and time zone.
- Rolling versus bucketed semantics.
- Bucket size.
- Network filters.
- Metric definitions.
- Category/list universe and sort direction.
- Subscription/limited mode.
- Response generation time.

Label any unavoidable mismatch and avoid stronger precision than the source supports.
