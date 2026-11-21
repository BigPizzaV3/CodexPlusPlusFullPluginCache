---
name: channels-search
description: Find channels that focus on a specific topic or niche
---
Find channels that focus on this topic or niche: $ARGUMENTS

Use the `discover_channels` tool with `query` set to `$ARGUMENTS`. This triggers smart mode, which searches for channels matching the topic rather than recommending based on my existing watchlist. If the results appear as interactive cards, don't list the channels again; otherwise present them as a list. Either way, organize them by category if there's natural grouping, and use channel descriptions intelligently to explain why each fits the topic. If `$ARGUMENTS` is empty, ask the user what topic or niche they want to search for.
