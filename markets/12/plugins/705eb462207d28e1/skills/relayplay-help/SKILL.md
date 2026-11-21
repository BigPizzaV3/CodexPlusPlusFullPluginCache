---
name: relayplay-help
description: Answer questions about how RelayPlay works, how to use a RelayPlay feature, product behavior, feature differences, accessibility, sync, settings, or troubleshooting. Always consult the RelayPlay Knowledge Base before answering, without requiring the user to mention help.
---

# RelayPlay help

Treat the confirmed RelayPlay Knowledge Base as the source of truth for product behavior.

1. Call `relayplay_search_help` with the user's complete question. Include platform and app version when known.
2. If one result answers the question, respond from that guidance.
3. If several topics are relevant, combine them and use `relayplay_get_help_topic` when exact topic content is useful.
4. Only after `no_match` or `unavailable` may general knowledge supplement the answer. Clearly label the supplement as an inference rather than documented RelayPlay behavior.

This applies to Flow ordering, Hold, Catch Up, Latest, AutoSkip, Moments, history, Find, Player, settings, sync, accessibility, troubleshooting, and interactions between RelayPlay features. Earlier chat messages and model memory never override confirmed help content.

The help tools are read-only. Do not imply that they inspected the user's library, listening history, player, devices, or settings.
