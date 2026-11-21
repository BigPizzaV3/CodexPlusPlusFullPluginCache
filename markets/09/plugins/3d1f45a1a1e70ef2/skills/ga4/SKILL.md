---
name: ga4
description: Read Google Analytics traffic for a CreceRank brand that is already connected, choose a GA4 property, or disconnect Analytics. Use when the user asks about AI referral traffic or their GA4 property.
---

Use this skill only for Google Analytics that is already connected in the CreceRank dashboard.

If the user gives a different instruction, follow that instruction.

1. Call `crecerank_get_ga4_summary`. Pass `days`, or `start_date` and `end_date`, when they name a range.
2. If the result says Analytics is not connected, tell them to connect GA4 in the CreceRank dashboard. Do not invent an OAuth URL and do not start Google sign-in.
3. When it is connected and they need to choose a property, call `crecerank_list_ga4_properties`, then `crecerank_select_ga4_property` with the `property_id` they pick.
4. Call `crecerank_disconnect_ga4` only after they explicitly ask to unlink Analytics. This clears the connection on the brand. It does not delete data in Google.

Report the sessions and sources the summary returns. Do not estimate traffic when the tool says Analytics is disconnected.
