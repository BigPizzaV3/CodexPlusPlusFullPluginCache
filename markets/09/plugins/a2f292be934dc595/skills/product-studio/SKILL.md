---
name: product-studio
description: Create 1–4 product shots from an attached product image and scene instructions, then animate a selected shot. Exact product and label fidelity is not guaranteed.
---

# Firemoon Product Studio

Use product_shots and product_animate. Create 1–4 product shots from an attached product image and scene instructions, then animate a selected shot. Exact product and label fidelity is not guaranteed.

Use the image attached to the user message as image. Ask for a product image if required and missing. Supply explicit scene descriptions in order. Show the returned inline canvas rather than just a URL. Animate only when requested. Use actual returned media URLs as inputs for subsequent tools. Do not automatically retry uncertain image or animation requests; inspect existing outputs first. Media is processed by Firemoon and its providers; links can be viewed by recipients who have them. Never execute downloaded code or silently substitute another generator.

Use product_preview with a saved generation_id to reopen an existing result in the inline canvas without generating it again.

## Guest access and optional account linking

Start by calling the workflow tools directly. Do not request account linking before using the anonymous daily image/video allowance. Guests share 100 image/video outputs per host guest identity per UTC day; each image variation counts separately. Only offer account linking when the tool returns an authentication challenge or the user explicitly wants to use account credits. Never invent a guest identifier or bypass a quota response. Preserve existing attachment requirements and uncertain-job retry safeguards. Account linking accesses existing account entitlements. Do not list plans or credit packs, promote digital upgrades, or create checkout links in the plugin.
