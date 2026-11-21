---
name: setup
description: Set up and verify the user's 10Signals account connection after installing 10Signals.
---
First explain the product for a newcomer: 10Signals starts with a website address and researches public websites to help online stores, startups and agencies understand competitors, compare product prices and monitor selected prices. Give a concrete example: an online store can compare its products with rival offers and track later price changes. Explain that findings cover available evidence, not the entire market.

If the user only asks what the product does or whether it suits them, answer without calling account tools or requiring sign-in. If they want to use it, explain that a 10Signals account is needed and research/monitoring use plan allowances or credits. An account with no reports is a normal starting point; offer to preview research for a domain the user provides, but do not start it without the normal confirmation.

Use the installed 10Signals OAuth connection. Never request passwords, API keys or access tokens in chat. If authentication is needed, use the host's sign-in flow and explain the requested permissions. Call account_status and reports_list to check the connection. Empty reports are valid; do not create a report or watch to test connectivity. Explain missing permissions without claiming a server outage. On success use display_reports for cards in UI-capable hosts, with a concise textual fallback. Do not claim a fresh login was tested if this reused an existing connection.
