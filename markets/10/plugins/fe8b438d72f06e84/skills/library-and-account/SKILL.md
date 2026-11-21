---
name: library-and-account
description: Browse the user's RTST (rtst.ai) library and account — their generated images, videos and motion transfers, the connected account, credit balance, plan, model prices and credit spend history. Use when the user asks to see their RTST images or videos, which account is connected, how many credits they have, what something costs, or where their credits went.
---

# The RTST library and account

Tools: `list_images`, `list_videos`, `whoami`, `balance`, `transactions`, `show_models`,
`list_models`, `estimate_cost`.

- **Images:** `list_images` (newest first; `page` and `limit`).
- **Videos:** `list_videos`; `kind: "motion"` lists motion transfers instead.
- **Load more:** call the same tool with the next `page` (the card's Load more does this).
- **Which account:** `whoami`. **Credits and plan:** `balance`.
  **Where credits went:** `transactions` (optional `category`).
- **Models and prices:** when the user asks to see or compare models, `show_models`
  (the picker card in ChatGPT; once per request). A video model's rate is only a base
  rate: for a price, use `estimate_cost` with the arguments the job would use.
- **Plans and credits** are described on https://rtst.ai/pricing. Link it when the user
  asks or a job can't be afforded; nothing is bought inside the chat, and never push an
  upgrade or a purchase.

In ChatGPT these render as cards: summarize in a sentence instead of listing every
item or URL. Where no card renders (Codex, Claude Code), list items briefly with their
links.

This plugin cannot delete media, change whether an item is public, or change the plan.
Say so and point to https://rtst.ai/workspace (media) or https://rtst.ai/profile
(account); never claim to have done it.

## Messages sent by RTST card buttons

- "Estimate how many credits a 5-second 720p video costs on rtst.ai." → `estimate_cost`
  (`type: "video"`) on a suitable model's 5-second 720p settings, and say which model
  you priced.
- "Show page … of my rtst.ai …" (Load more could not run inside the card) → the matching
  list tool with that `page` (`list_videos` with `kind: "motion"` for motion transfers).
- Library buttons that animate, remix or reuse an item hand off to `create-video`,
  `create-image` or `animate-character`.
