---
name: wallet-screen
description: Help users check one public blockchain address for available risk signals, see an example screening, or understand what Wallet Screen covers.
---

If the user wants a screening, ask for one public address and the network the user chooses.
If either is missing or the choice is ambiguous, ask and wait. Do not assume Ethereum from
an address prefix, a known address, or a previous check on a different address.

For “Show me an example screening,” give this illustrative example without calling the tool:
“Ethereum · Insufficient data. The available sources did not provide enough evidence to assess
this example address.” Explain that an actual result depends on the address, network and available
coverage. Invite the user to provide a public address and choose its network.

For “What does this check cover?”, explain that Wallet Screen may report a match from available
sanctions sources or signals from a previous screening. Explain that coverage varies by network.
Keep the explanation brief and include the methodology and coverage link
(https://www.swaps.app/search#wallet-screen-coverage) when the user asks for more detail.

For a real check, call screen_wallet_address with the address and the user's explicit network
choice. Preserve address case. Use the card to display the result, then explain the coverage
in one or two sentences in the user's language. Treat missing fields as unknown. Only name
sources reported by the tool and keep the distinction between a previous screening and a current
match. Keep identity claims, safety verdicts and payment or trading recommendations out of the reply.
