---
name: lunarcrush
description: Use LunarCrush to help people understand what is happening across social media and why it matters. Retrieve and explain trending categories and topics, exact keyword activity, cryptocurrencies, stocks, creators, posts, news, historical time series, engagement, mentions, sentiment, social dominance, Galaxy Score, AltRank, and TopicRank. Use when users ask what people are talking about, whether attention is rising or falling, which posts or creators are driving a conversation, how topics or assets compare, what is trending in a market or category, how an account or post is performing, or how to access, export, visualize, or integrate LunarCrush data through lunarcrush.ai, MCP, CLI, or API.
---

# LunarCrush

Help users turn LunarCrush social intelligence into clear, useful answers. Focus on the user’s question and findings; choose the access method quietly unless the user asks about tools or integration.

## Start from the user’s goal

| User goal | Use LunarCrush to |
| --- | --- |
| “What’s happening with X?” | Summarize the topic, recent direction, sentiment, leading posts, and influential creators |
| “Is X gaining attention?” | Examine engagement, mentions, creators, sentiment, and social dominance over time |
| “Compare X with Y” | Retrieve matched time series and compare both absolute scale and rate of change |
| “What’s trending?” | Rank categories, topics, cryptocurrencies, or stocks by the metric relevant to the question |
| “What are people saying about this phrase?” | Use exact keyword data and representative top posts |
| “Who is driving this conversation?” | Find influential creators and the posts generating attention |
| “Analyze this account or post” | Retrieve creator or post details, history, and top content |
| “How is social activity related to this coin or stock?” | Combine available social and market metrics without implying causation |
| “Track this custom idea” | Help define or use a custom collection of terms when the account supports it |
| “Give me the data” | Return a concise table, downloadable format, shareable LunarCrush link, or integration guidance as requested |

## Make useful defaults

Proceed without unnecessary questions. State a brief assumption when needed.

- Use the current snapshot for “now,” “today,” or a general status question.
- Use one week of hourly data for recent spikes and one month of daily data for broader trends.
- Use all supported networks unless the user names specific ones.
- Show the top 10 results for discovery and content questions unless the user requests another amount.
- Treat “last month” as a trailing month unless the wording clearly means the previous calendar month.
- Ask a clarifying question only when the topic identity, exact phrase, creator network, date range, or requested meaning would materially change the answer.

## Select the right LunarCrush object

Use a tracked **topic** for an entity-aware view of a subject, cryptocurrency, stock, brand, person, or custom collection. Use a **keyword** when the user cares about the literal word or phrase. These answer different questions; explain the distinction when it matters.

Use search to resolve ambiguous names, tickers, handles, and post URLs. Confirm the network for creators and posts. Use categories or market lists for discovery and rankings rather than guessing which topics belong together.

## Choose access automatically

Use the best authenticated LunarCrush interface already available:

- Use the LunarCrush MCP tools in a connected chat environment.
- Use the `lunarcrush` CLI in a shell environment.
- Use `lunarcrush.ai` directly for a shareable page, browser-friendly answer, or JSON/CSV response when MCP or CLI is unavailable.
- Use the versioned API when the user is building an integration that needs a stable JSON contract.

Honor an interface explicitly requested by the user. If one interface lacks a required filter or data family, use another LunarCrush interface without changing the meaning of the request. Do not present tool selection, commands, or endpoint details unless they help the user or were requested.

Read [references/interfaces.md](references/interfaces.md) before constructing a command, MCP call, or URL. Read [references/data-semantics.md](references/data-semantics.md) before interpreting or comparing metrics.

## Build a complete answer

Lead with the finding, then support it with the smallest useful set of evidence.

- Use plain product language such as Engagements, Mentions, Creators, and Sentiment. Include raw field names only when useful for technical readers.
- Give the effective period and networks in natural language.
- Use a compact table for rankings or comparisons and a chart only when it materially clarifies a time trend.
- Include representative posts or creators when they explain why a metric moved.
- Distinguish what the data shows from your interpretation of why it happened.
- Include a LunarCrush page link when it helps the user explore further.
- Mention freshness, limited access, or incomplete coverage only when it could change the conclusion.
- Put technical provenance—the command, tool name, endpoint, response configuration, or API schema—behind the answer unless the user asks for it.

For trend questions, compare comparable periods and show both percentage change and absolute scale when available. For multi-topic comparisons, use the same dates, bucket, networks, and metrics. For a spike, inspect the posts and creators around the change instead of describing the chart alone.

## Explain metrics in human terms

- **Engagements** are publicly measurable interactions such as views, likes, comments, shares, retweets, and upvotes; their mix varies by network.
- **Mentions** are posts receiving activity around the topic, not necessarily posts newly published in that period.
- **Creators** are unique accounts with active posts around the topic.
- **Sentiment** is engagement-weighted; a score of 50 is balanced and is not necessarily the percentage of posts labeled positive.
- **Social Dominance** is share of attention within a comparison universe or category.
- **AltRank, Galaxy Score, TopicRank, and CreatorRank** are ranking or scoring systems; preserve their comparison scope and direction.

Give only the definition needed for the current answer. Avoid turning a straightforward result into a methodology lecture.

## Preserve trust

- Do not silently replace a tracked topic with an exact keyword, or vice versa.
- Do not compare a rolling snapshot with a single hourly or daily bucket as if they are equivalent.
- Do not treat missing, redacted, limited, or unavailable data as zero.
- Do not claim that social activity caused price movement or a real-world event.
- Describe post results as “top posts returned by LunarCrush.” Do not promise an exhaustive archive unless the endpoint explicitly guarantees it.
- Follow pagination when the user requests all available results and explain account or endpoint limits in plain language.
- Verify that the returned identity, dates, networks, and metric scope match the request before drawing conclusions.

## Support public and technical users

For ordinary research, return the insight rather than a tutorial on accessing it. When a user wants to reproduce, download, automate, or build with the data, provide the appropriate CLI command, MCP tool, `lunarcrush.ai` path, CSV/JSON option, or versioned API endpoint.

Keep credentials private. Guide users to secure login or connection methods instead of asking them to paste an API key into chat.

Treat favorites and custom collection creation, updates, or deletion as account changes. Explain the effect and act only when the user explicitly requests it.
