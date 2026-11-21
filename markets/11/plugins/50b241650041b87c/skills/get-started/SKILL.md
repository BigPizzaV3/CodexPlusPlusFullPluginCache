---
name: get-started
description: Explain what Eskopia is, what it monitors, what you can ask after connecting, and what's needed to use it (an Eskopia account with a store set up in Eskopia). Use for "what is Eskopia", "what can it do", "do I need an account", "how do I connect my Shopify store", "how do I get started", and when a tool reports that the store isn't ready.
---

# Getting started with Eskopia

Answer from the facts below only. Don't promote plans, prices, trials or sign-up offers, and don't start or walk through account creation in ChatGPT. You may point to the informational page https://eskopia.com/chatgpt.

## What Eskopia is

A store monitoring and insights platform for Shopify merchants, built by AMNYA Technology, founded by Adel Ammari. It watches storefront activity and orders as they happen and flags when something looks wrong.

## What it monitors

- Live activity: who is on the store now and what they're doing (browsing, viewing products, cart, checkout)
- Orders and revenue from the store's Shopify order webhook, including individual orders and checkouts (without customer details)
- Where visitors and orders come from: country, city, traffic source, device, landing page, and how that changes over time
- The shopper funnel and checkout steps, and where people drop out
- Products: views and add-to-carts per product, and units sold and revenue per product from order data
- Store health, including whether the Eskopia pixel and order webhook are still sending data
- Anomalies, using seven fixed rules checked every 15 minutes: no orders, revenue drop, traffic drop, checkout completion drop, abandoned checkout spike, tracking gap, order webhook gap
- Alerts Eskopia has sent

## What you can ask after connecting

"Is everything okay with my store?", "What's happening right now?", "How are sales today vs last week?", "How many visitors from Saudi Arabia today?", "Which traffic sources convert best?", "Show me today's biggest orders", "What are my best sellers?", "How much is sitting in abandoned checkouts?", "When are my peak hours?", "Why are sales down?", "Where are customers dropping out?", "Which products get views but no add-to-carts?", "Has Eskopia detected anything unusual?", "Explain my latest alert."

## What's needed

- An Eskopia account, and a store set up in Eskopia. Account creation and store setup happen in the Eskopia web app at eskopia.com, not in ChatGPT.
- Store setup (done by a store admin in Eskopia): enter the Shopify domain and order webhook signing secret in Settings, create the order webhook in Shopify pointing at Eskopia, and install the Eskopia custom pixel in Shopify's Customer events. ChatGPT never connects to Shopify and never sees Shopify credentials.
- Connecting: when the merchant uses Eskopia in ChatGPT, they sign in on eskopia.com and approve read-only access. Disconnect any time in Eskopia under My Settings, Connected apps.

## When a tool says the store isn't ready

Read `readiness.state` from `list_stores`:
- `not_configured`: a store admin needs to finish Settings and Shopify Setup in Eskopia.
- `awaiting_data`: set up, but no activity has arrived yet; check the pixel and order webhook on Eskopia's Shopify Setup page.
- `pending_subscription`: the Eskopia signup wasn't completed; finish it in the Eskopia web app.
- `suspended` or `cancelled`: an admin can review the account under Billing in Eskopia.

## Limits to state honestly

Read-only (no changes to Eskopia or Shopify). Product sales cover only orders whose product lines Eskopia stored, and refunds aren't subtracted. Can't see site speed, payment failures, inventory or ad campaigns. Never returns shoppers' names, emails, order numbers or IP addresses.
