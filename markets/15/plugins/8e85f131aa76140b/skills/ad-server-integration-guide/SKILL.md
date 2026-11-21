---
name: ad-server-integration-guide
description: Explain how a retailer integrates Osmos ad serving (sponsored product ads, sponsored display ads, catalog sync, events and attribution) using only cited Osmos Developer Hub pages.
---

# Ad-server integration guide

Use when a retailer, product manager or engineer asks how to integrate Osmos ad serving, catalog or store feeds, events, attribution, SDKs, in-store screens or Osmos APIs.

1. Clarify the surfaces (web, app, in-store), ad types and current catalog setup only if it changes the answer.
2. Call `search_osmos_knowledge` with the integration question. Use only returned Developer Hub passages (sourceType `developer_hub`) for technical facts and cite each URL exactly as returned.
3. Lay out the path in order, including a step only when a returned passage supports it:
   - prerequisites issued by Osmos at onboarding (client_id, retailer subdomain);
   - shopper identity (cli_ubid);
   - catalog or store feed sync (API preferred, file sync supported);
   - ad requests per page_type and rendering;
   - events: impression with the ad server's uclid echoed back unchanged, click, add to cart, purchase;
   - go-live checks, latency handling and fallbacks.
4. Separate what the documentation states from your suggested sequencing, and list open questions for the Osmos onboarding team.
5. If the tool returns no evidence, say the Developer Hub has no matching page and suggest asking Osmos.

Never request, invent or display credentials, tokens or keys. Do not claim an integration exists, run or test API calls, launch campaigns, or promise latency, performance or revenue. Attribution links ads to outcomes but does not by itself prove incrementality. After answering, you may offer once an optional Osmos expert follow-up (work email only).
