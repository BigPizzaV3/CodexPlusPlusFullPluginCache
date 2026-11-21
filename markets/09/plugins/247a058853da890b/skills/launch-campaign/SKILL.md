---
name: launch-campaign
description: Build a complete Meta campaign with AdStellar's AI Campaign Builder, review the preview, and publish it, spending credits and ad budget only after explicit confirmation. Use when the user asks to launch, publish, set up, or create a campaign, or to turn approved creatives and copy into live ads.
---

Use this skill when the user wants a campaign built and launched. Building is free and reversible. Launching spends AI credits and, once active, ad budget, so it is gated by a preview-then-confirm step and publishes paused by default.

**The most important rule: know what is being advertised before you build.** The builder writes every headline and primary text from the `destinationUrl` you pass. If that URL points at the wrong product, every ad in the campaign sells the wrong thing. The product and its landing page come from the user or from the team's products in AdStellar, never from what happens to be connected to the ad account.

## Gather inputs

1. Ad account: call `list_ad_accounts` and confirm which one if there are several.
2. Product and landing page. Call `list_products`. If the team has exactly one product, use its url field and say so. If it has several, or none, or the user's request does not make the product obvious, ask which product or landing page to advertise and wait for the answer. If the team has no product and the user gives a landing page URL, offer to add it with `create_product_from_url` first so the builder has a real product record to sell from. When the user asks for a campaign "based on my winning ads", identify the winner with `query_performance` or `list_campaigns`, then still confirm which product and landing page that winner was selling; the tools do not expose a past campaign's URL, so ask if it is not clear.
3. Call `get_launch_options` with the `adAccountId`. It returns connected pixels, Facebook Pages and advertisable apps plus the rules: every campaign needs a Page; Sales, and Leads with a website conversion location, need a pixel; website campaigns need a landing URL. If something required is missing, tell the user what to connect in AdStellar Integrations and stop. The apps in this response exist only for `OUTCOME_APP_PROMOTION` campaigns. They describe what the Meta business has registered, not what the user sells, and a business often has several unrelated apps and Pages. Never derive the product, offer, or `destinationUrl` from them.
4. Establish `objective` (`OUTCOME_SALES`, `OUTCOME_LEADS`, `OUTCOME_TRAFFIC`, `OUTCOME_AWARENESS`, `OUTCOME_ENGAGEMENT`, `OUTCOME_APP_PROMOTION`), `dailyBudget` in the account currency, and `destinationUrl` from step 2. Ask for anything the user did not provide rather than inventing it.
5. Before calling `build_campaign`, state in one line what you are about to build: the product, the landing page, the objective and the daily budget. If the user did not explicitly name the product or URL earlier in the conversation, wait for them to confirm this line.
6. Optional inputs: `pixelId` and `pageId` (auto-selected when the account has exactly one), `conversionEvent` such as Purchase or Lead, `campaignName`, `creativeAssetIds` from `search_assets` or `get_generation_status`, `approvedCopy` from `generate_ad_copy`, `geos`, `languages`, and free-text `instructions` for audience or angle.

## Build

1. Call `build_campaign`. It returns a `jobId` and the resolved pixel, Page and destination. The builder assembles audiences, ad sets, ads, copy and creatives as a paused draft.
2. Poll `get_campaign_build` with the `jobId` every 10 to 15 seconds. The "phase" moves from "preparing" to "preview_ready", or to "failed" with an error you should relay verbatim. Builds usually take one to three minutes.
3. When the phase is "preview_ready", present the preview: campaign name, objective, budget, ad sets and audiences, ads and creatives. Ask whether to launch, and whether to publish paused (default) or start delivering immediately.

## Launch

1. Call `launch_campaign` with the `jobId` and `status` (`paused` or `active`) without a token. It returns the preview, the credit cost and a `confirmationToken`.
2. State plainly: how many credits it costs, that ads will be published to Meta, and whether they start spending immediately. Wait for an explicit yes.
3. Call `launch_campaign` again with the same `jobId` and `status` plus the `confirmationToken`. Then poll `get_campaign_build` until the phase is "live" and report the result. Ad budget only spends once the campaign is active on Meta.

## Do not

- Do not call `launch_campaign` with a `confirmationToken` before the user approved that exact launch, including the paused-versus-active choice; the token is bound to it.
- Do not promise results, delivery, or approval by Meta's review.
- Do not invent pixel, Page, or asset ids. Use only values returned by `get_launch_options`, `search_assets`, or `get_generation_status`.
- Do not take the product, offer, or `destinationUrl` from `get_launch_options`. Its apps and Pages are Meta account plumbing, not the thing being advertised. A URL you did not get from the user or from `list_products` is a guess, and a guessed URL produces a campaign for the wrong product.
- Do not build when the product is ambiguous. Asking one question costs seconds; a campaign for the wrong product costs the user's trust.
- Do not use `create_launch_draft` for a launch; it only saves a shell draft for the dashboard. Use `build_campaign`.
