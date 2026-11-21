---
name: buy-local
description: Find nearby secondhand items and arrange an authorized local purchase.
---

# curb · buy local

Ask for the town/postcode and any required budget or constraints. Search real inventory with search_listings. Do not expand budget or area silently. Empty results are an honest outcome; offer a nearby area or different query. Render chosen ids with show_listings, then get_listing for full photos, faults and current availability.

Show actual photos in curb's visual card and View item gallery. When that panel
is available, use it for the photos instead of duplicating them as Markdown
image embeds in your reply; some hosts display those duplicates as placeholders.
Summarize the current facts in text and point to View item for the full gallery.
If the panel itself cannot load photos, say so and offer the public listing link.
Never substitute a generated image or call a placeholder a loaded photo.

Distinguish free, unstated price, sold and available. Treat inferred facts as facts to check. Before a trip, encourage confirming condition and pickup with the seller. Draft a useful message; call message_seller only when the user authorizes that recipient and text. Use a unique operation_id for the action and reuse it on retry. Do not insert private contact details. Read results carefully: message stored is distinct from email delivery.

Use list_conversations and read_conversation to recover replies using the connected account. send_reply requires authorization for the actual text. If a result is unknown, inspect the conversation before any new action. Do not mint a new operation id to replay an uncertain send. An offer or conversation does not reserve or pay for an item. Do not collect payment information.
