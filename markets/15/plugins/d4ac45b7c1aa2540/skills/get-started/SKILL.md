---
name: get-started
description: Set up the Baseline plugin after installation and confirm access to its research catalog. Use for Baseline setup or connection help.
---

# Get started with Baseline

Baseline provides dated qualitative company research, stock screening, and personal watchlists. An existing Baseline account with research access is required.

If the Baseline tools are unavailable or request authentication, direct the user to the host's connection or reconnect flow. Sign-in and consent happen in Baseline's browser OAuth flow. Never ask for passwords, tokens, or verification codes in the conversation.

Once connected, call `baseline_catalog` to confirm research access. Tool names may have a host-specific namespace. If access is denied, explain the returned restriction and stop setup; do not claim setup succeeded, initiate a subscription, or surface checkout links.

After a successful catalog response, describe the available research using the returned fields. Offer a relevant next step: screen stocks, read research for a ticker such as `MSFT.US`, or view the user's watchlists. Setup itself does not create or change a watchlist.

Use the packaged [equity research workflow](../equity-research/SKILL.md) for subsequent research and watchlist requests. Include research dates and explain that Baseline provides neither live quotes nor trade execution.

Connection help: https://baseline.a5labs.com/mcp-docs#troubleshooting
