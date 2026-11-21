# Lukka-News - 2 Production Tools

Digital asset news intelligence. All tools exposed as `news___<tool>`.

Provides article search and daily summaries. Aggregate views (events, trends, timelines, stats) are built client-side from `getNews` / `getDailySummaries`:

## CRITICAL: Date Parameter Format (P0)

`publishDateFrom` and `publishDateTo` MUST be full ISO 8601 with timezone:
- CORRECT: `2026-04-01T00:00:00Z`
- WRONG: `2026-04-01` (bare date not accepted)

Always append `T00:00:00Z` (start of day) or `T23:59:59Z` (end of day) to bare dates. The date params require a full ISO 8601 value with a `T-hh:mm:ss` time component; always send full ISO.

## News Search

### `news___getNews`

Returns JSON array of NewsItem objects. All parameters optional - omitting all returns most recent articles.

| Param | Type | Notes |
|-------|------|-------|
| keyword | string | Free-text search across title + snippet |
| publishDateFrom | string | **Full ISO 8601 only** (`2026-04-01T00:00:00Z`) |
| publishDateTo | string | **Full ISO 8601 only**. Same constraint |
| entityCodes | string | Comma-separated publisher codes: `theblock`, `coindesk` |
| primaryCategory | string | Comma-separated. See categories below |
| sentiment | enum | `positive`, `negative`, `neutral`, `mixed` |
| technicalLevel | enum | `beginner`, `intermediate`, `advanced`, `expert`, `mixed` |
| industrySegment | string | e.g. `defi`, `trading` |
| source | string | Publisher source_name |
| qualityFrom | number | Min quality score 0-100. Recommended default: 50 |
| qualityTo | number | Max quality score 0-100 |
| relevanceFrom | number | Min relevance score 0-100. Recommended default: 50. **Warning: the relevance model assigns high scores (incl. 100) to off-topic noise (hardware, sports, etc.). Do NOT use `relevanceFrom` alone as a digital asset filter - always pair with a `keyword` or `primaryCategory` to scope to digital asset content.** |
| relevanceTo | number | Max relevance score 0-100 |
| newsID | string | Fetch single article by UUID (ignores all other filters) |
| sortBy | enum | `date`, `source`, `sentiment`, `category`, `qualityScore`, `relevanceScore` |
| sortOrder | enum | `asc`, `desc` (default: `desc`) |
| limit | integer | Max 500 per page |
| offset | integer | Zero-based pagination offset |

### Categories (valid `primaryCategory` values)

Categories are assigned by an AI tagging model, not a fixed database enum - treat this list as the model's guided taxonomy, not an exhaustive hard list. Grouped by theme:

- Markets & Trading: `price-analysis`, `market-news`, `exchange-news`, `derivatives`, `market-manipulation`
- Technology & Development: `protocol-development`, `smart-contracts`, `consensus-mechanisms`, `scaling-solutions`, `interoperability`, `developer-tools`, `open-source`
- Regulation & Legal: `regulatory-news`, `compliance`, `legal-cases`, `government-policy`, `tax-policy`, `enforcement-actions`
- DeFi & Protocols: `defi-protocols`, `lending-borrowing`, `dexes`, `yield-farming`, `staking`, `liquidity`
- NFTs & Digital Collectibles: `nft-markets`, `nft-collections`, `digital-art`, `gaming-nfts`, `nft-utility`, `metaverse`
- Institutional & Enterprise: `institutional-adoption`, `etf-news`, `corporate-treasury`, `custody-solutions`, `traditional-finance`
- Security & Privacy: `security-breaches`, `wallet-security`, `privacy-tech`, `cryptography`, `audit-reports`
- Economics & Tokenomics: `monetary-policy`, `tokenomics`, `mining-news`, `stablecoin-news`, `cbdc`
- Ecosystem & Community: `community-governance`, `ecosystem-growth`, `partnerships`, `funding-news`, `airdrops`
- Education & Analysis: `educational-content`, `research-analysis`, `opinion-editorial`, `interviews`, `case-studies`

**NOTE:** `regulatory-news` and `compliance` are distinct categories - don't conflate them. Unknown/misspelled categories return `[]` silently - confirm results are non-empty.

## Daily Summaries

### `news___getDailySummaries`

AI-generated daily digital asset news digests.

| Param | Type | Notes |
|-------|------|-------|
| date | string | YYYY-MM-DD for single-day lookup. Mutually exclusive with `limit` |
| limit | integer | Most recent N summaries. Default 14, max 90. Ignored when `date` supplied |

- `date` and `limit` are **mutually exclusive** - pass one or the other
- Monday summaries cover Saturday + Sunday as a combined weekend digest
- First summary available from **2026-04-08**. Earlier dates return empty
- Returns: summaryDate, articleCount, overallSentiment, sentimentBreakdown, summaryText, keyThemes, notableEvents, topCategories, topAssets

## Deriving composite analytics client-side

Aggregate views (events, trends, timelines, stats) are built client-side from `getNews` / `getDailySummaries`:

| Need | How |
|------|-----|
| Major events | `getNews` with `sortBy: "relevanceScore"`, `sortOrder: "desc"`, `limit: 10` |
| Trending topics | `getNews` with high `relevanceFrom: 70`, sort by `relevanceScore` |
| Sentiment timeline | Loop `getNews` day-by-day with `sentiment` filter, aggregate client-side |
| News stats | Use `getDailySummaries` for high-level overview (articleCount per day) |

## Known Issues

| Issue | Severity | Workaround |
|-------|----------|------------|
| Date not full ISO 8601 | P0 | Always full ISO 8601 with `T00:00:00Z` suffix |
| Unicode smart quotes as `???` | P1 - cosmetic | Display as-is, note corruption to user |
| No `totalCount` in response | P2 | Cannot know total matching articles; use offset pagination |
| No `detailed` flag | P2 | Hosted always returns full records |
| limit max 500 | Info | Higher than other servers' 100. Use offset for >500 results |

## Quick Examples

```
# Recent DeFi news
news___getNews({
  keyword: "uniswap",
  primaryCategory: "defi-protocols",
  sortBy: "date",
  sortOrder: "desc",
  limit: 10
})

# Negative regulatory news this week
news___getNews({
  primaryCategory: "regulatory-news",
  sentiment: "negative",
  publishDateFrom: "2026-05-12T00:00:00Z",
  publishDateTo: "2026-05-16T23:59:59Z",
  sortBy: "date",
  sortOrder: "desc"
})

# Today's daily summary
news___getDailySummaries({
  date: "2026-05-16"
})

# Last 7 days of summaries
news___getDailySummaries({
  limit: 7
})

# Single article by ID
news___getNews({
  newsID: "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
})
```
