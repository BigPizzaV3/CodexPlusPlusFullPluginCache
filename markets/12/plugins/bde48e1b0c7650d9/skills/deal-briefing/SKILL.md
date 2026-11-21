---
name: deal-briefing
description: Brief a real-estate agent on their OfferCopilot deals. Use when they ask what needs attention, where a deal stands, who still has to sign, what a client still owes, or for a morning summary.
---

1. For one deal, call `get_deal_status` with whatever the user gave: an address, a client's name or a deal number. If the reply lists candidates, read their addresses and buyers back and ask which one.
2. For "what needs attention", call `list_offers`, then `get_deal_status` for each live deal the user cares about. Ask before checking more than five.
3. For a question about one stage, such as who still has to sign, call `list_offers` and then `get_deal_status` for every deal at that `stage` (`Signing` for signatures), without asking first. If more than ten match, check the ten listed first and say how many you left out.
4. For each deal, report the stage, the single next step, who still has to sign, what the client still owes and any date that is close. Include the `deal_url` so the user can open it.
5. Answer follow-up questions from the replies you already have before calling again.

Report only what the tools return. Do not guess a status, a date, an amount or whether something is signed. If a field is missing, say it is missing.
