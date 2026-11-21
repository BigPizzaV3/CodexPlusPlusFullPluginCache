---
name: get-started
description: Get a new Hustle Got Real user oriented in ChatGPT. Use when the user first connects Hustle Got Real, asks what it can do, or asks to see their stores or store overview.
---

Use this skill to orient the user in their Hustle Got Real (HGR) account. Explicit user instructions always take priority over these steps.

1. Call `hgr_list_stores` to read the user's stores. If the call asks to connect or reconnect, tell the user to connect Hustle Got Real in ChatGPT and stop.
2. If the user has no stores, explain that they need to connect a marketplace store in Hustle Got Real first (https://app.hustlegotreal.com) and stop.
3. Call `hgr_open_store_manager` so the user can see their store overview in the app.
4. Summarize in a few lines:
   - How many stores they have, and each store's marketplace and country when there are only a few.
   - Stores whose `connectionStatus` is "needs reconnecting". Say they must be reconnected in Hustle Got Real; ChatGPT cannot reconnect them.
5. Offer three next steps the plugin supports: review or edit listings, find products to sell, or check orders and sales.

Rules:
- Report only what the tools return. Do not guess listing counts, sales or connection states.
- Do not change anything in this workflow; it is read-only.
- Do not ask for passwords, API keys or marketplace credentials.
