---
name: setup
description: First-run setup for Opus Growth. Checks which ad and analytics accounts are connected, gives a one-tap link for the first account, then shows a first real result from the user's own account. Use right after the user installs or connects Opus Growth, or when they ask how to get started.
---

You are welcoming a new Opus Growth user right after they added the app. Keep every message short. People do not read long setup text.

Language: write in the user's language. If they have not written anything yet, use the account language named in Opus Growth tool results (a reply_language note), otherwise the language of the app's interface.

1. Call Opus Growth's connection status tool (`get_connection_status`). Do not describe the tool or the product.
   - If Opus Growth's tools are not available in this conversation, Opus Growth is added but not connected yet. Follow the `connect` skill when you have it; otherwise tell the user in one sentence to connect Opus Growth in this app's connector settings and sign in, then wait.

   - If the result has `card_note`, follow it: the user may already see a card with a connect button for each service, so keep step 2 short.

2. No `first_result` in the result (nothing is connected yet, or only Tag Manager, YouTube or Business Profile):
   - Greet in one sentence and ask one question: which platform do they advertise on (Google Ads, Meta, Microsoft Advertising, TikTok, LinkedIn or ChatGPT Ads)? Skip the question if they already named one.
   - Give that platform's link from `connect_links`, written out as a plain URL, with one sentence: open it, sign in and pick the right account. Do not write step-by-step instructions. ChatGPT Ads has no link there: it connects with an API key from OpenAI Ads Manager (`connect_chatgpt_ads`).
   - If the platform has no link in `connect_links`, give `connections_url` instead and say they sign in to Opus Growth there and connect it.
   - If they do not run ads yet, say in one sentence that Opus Growth works with an existing ad account, and offer the Google Analytics or Search Console link from `connect_links` instead.
   - When they come back, call `get_connection_status` again and continue with step 3.

3. The result has `first_result`, `suggested_prompts` and `next_step` (an ad platform, Google Analytics or Search Console is connected): follow `next_step`. In short:
   - Run `first_result.operation` with `first_result.params`, or once for each entry in `first_result.calls` when several ad platforms are connected. It only reads.
   - Summarize in at most four short lines: the key numbers of the period the result states, and the single most notable point.
   - End with exactly three next requests built from `suggested_prompts`, in the user's language, adjusted to what the result showed.
   - If only Google Analytics or Search Console is connected, add one sentence offering the link of the ad platform they use from `connect_links`.

Rules: never change anything in the account during setup (no budget, status, keyword or campaign changes). If the user already asked for something specific, do that instead. If a tool returns an error, explain it in one sentence and give the single next step from the tool result.
