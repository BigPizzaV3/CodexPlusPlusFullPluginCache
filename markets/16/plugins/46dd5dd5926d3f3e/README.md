# Timefire

Check the public record of Timefire's AI stock forecasts from your assistant.

Timefire seals each book of forecasts before outcomes are known, then grades it ten trading days later. This plugin connects your assistant to that record, so you can look up graded books, review the track record, and verify a book's seal yourself.

It's read-only and needs no account. This is not investment advice.

## Use it

Ask in plain words, and your assistant picks the tool:

- "Verify the newest graded book and tell me what the timestamp proves."
- "What is the hit rate across every graded book?"
- "Show me every graded book that included Apple."
- "Show me the equal-weighted portfolio value against RSP."

## What's inside

The plugin holds one thing: a connection to Timefire's hosted server at `https://api.timefire.ai/mcp/`. It has 12 read-only tools, listed at [timefire.ai/developers/tools](https://timefire.ai/developers/tools/). To connect without the plugin, see [client setup](https://timefire.ai/developers/mcp/).

## Data

The plugin runs nothing on your machine. When your assistant uses a tool, it sends that tool's inputs, such as a date, a ticker or search words, to `api.timefire.ai`. Graded books come back, never sealed ones. See the [privacy policy](https://timefire.ai/legal/privacy/).

## Support

Email hello@timefire.ai.
