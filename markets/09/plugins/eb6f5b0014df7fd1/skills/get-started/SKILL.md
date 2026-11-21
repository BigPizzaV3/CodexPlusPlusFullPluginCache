---
name: get-started
description: Introduce FLUF Connect and check the user's account is ready. Use the first time FLUF is used in a conversation, or when the user asks what FLUF can do or how to set it up.
---

# Getting started with FLUF Connect

FLUF Connect lists one inventory on many marketplaces (Vinted, eBay, Depop, Etsy, Shopify, Facebook
Marketplace and more) and keeps stock in sync across them.

1. Call `list_channels` to see which marketplaces this account has connected and which its plan can
   list to. Say in one line what you found.
2. If nothing is connected, tell the user to connect a marketplace at https://fluf.io/connect/channels.
   You can't connect one from ChatGPT.
3. If a call says a feature isn't on the account's plan, say so plainly. Don't file a bug, and don't
   suggest plans, prices or upgrades.
4. FLUF lists physical items only through ChatGPT. Digital goods, gift cards, tickets, services and
   prohibited categories (weapons, drugs, medicines, tobacco, adult) come back under
   `not_listable_here`; tell the user and don't retry them.
5. Offer the three common next steps: find items not yet on a marketplace and crosslist them, fix
   listings a marketplace rejected, or review recent orders.
