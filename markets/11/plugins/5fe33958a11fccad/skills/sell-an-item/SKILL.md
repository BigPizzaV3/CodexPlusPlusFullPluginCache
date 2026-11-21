---
name: sell-an-item
description: Turn actual item photos and seller-provided facts into a reviewed local listing.
---

# curb · sell an item

Collect the actual item photos, title, details, faults, town/postcode, and seller-stated price. Do not invent a price, condition, brand, model, ownership, working status or accessories. Ask about missing deciding facts. A blank price is price on ask; zero means free only when the seller said so.

Pass ChatGPT attachments through save_listing_draft.photos using the documented file references. Do not generate base64 or invent download URLs. Up to six photos are supported; preserve the intended cover order. When a photo is missing or the host supplies only a local file path, preserve the seller-provided facts before handing off to the device picker. If title, details and town/postcode are available, save them as a private draft with save_listing_draft, explicitly report that the photo is still missing, and direct the user to Edit draft and its device photo picker. This retains the facts while the panel securely transfers the selected file using their curb connection. Do not route an already-described item to the empty Sell an item form. If required facts are missing, ask for them; use open_marketplace for a new blank listing only when there are no facts to preserve. Do not publish a photo-less draft when the user intended to include a photo; require the updated photo preview first. Do not ask them to reattach the same local file repeatedly. For an expired remote attachment, ask them to reattach or use the panel. Never silently omit a supplied photo or substitute a stock/generated image.

Save with a unique operation_id and reuse it for the same save after a timeout. Read the returned draft and its revision. Show price, faults, town and photo count, and use the draft UI to review the images. Saving does not publish. Call publish_listing with that draft_id and exact revision only after the user authorizes publication. A changed revision requires another review. Repeating the same publish request must not create another listing.

Report the public URL only after confirmed success and explain search may take about ten minutes. Never present unconfirmed publication as failure safe to repeat. Use list_my_listings to recover. Drafts expire after seven days; delete_listing_draft removes a private draft when requested. Use the OAuth connection for ownership; never request or expose access secrets.
