---
name: manage-my-listings
description: Post, check, edit, hide, mark as sold or delete the user's own ads on ALAL.AZ. Use when the user wants to sell something or asks about the status of their listings.
---

# Posting and managing listings on ALAL.AZ

These actions need the user's ALAL.AZ account to be linked. If a tool asks for linking, tell the
user that they need to connect their ALAL.AZ account, then continue once it is linked.

## Every change needs explicit confirmation

Before `create_listing`, `update_listing`, `change_listing_status` or `delete_listing`:

1. Show exactly what will happen: the listing preview, the changed fields with old and new
   values, or the action.
2. Wait for a clear "yes" from the user. Only then call the tool with `confirmed: true`.

Never set `confirmed: true` on your own. Never set `termsAccepted: true` unless the user has
accepted the ALAL.AZ rules.

## Posting a new listing

1. Photos are required. Upload each image with `upload_listing_file`. If an image was generated
   by ChatGPT rather than photographed, add «Şəkil illüstrasiyadır» to the description.
2. Find the category with `list_categories`, the required fields with `get_category_fields`,
   and the city with `list_locations`.
3. Take the seller name and phone from `get_my_profile`. Ask for a phone number only if the
   profile has none.
4. Write a clear title and an honest description. Do not add claims the user did not make.
5. Preview, confirm, then call `create_listing`. Tell the user that the listing goes through
   moderation before it appears on the site.

## Checking status

- Use `list_my_listings`. Explain each status in plain words:
  - **Aktiv**: live on the site.
  - **Yoxlamada**: in moderation.
  - **Dərc olunmayıb**: rejected. Explain the `rejectionReason` and offer to fix it.
  - **Deaktiv**: hidden by the user.
  - **Satılıb**: marked as sold.
  - **Müddəti bitib**: expired. It can be renewed.
- Offer only the actions listed in the listing's `actions`.

## Editing

1. Call `get_my_listing` first to read the current values and `editQuota`. There is a daily edit
   limit, so tell the user how many edits are left.
2. Send only the fields that change. To add photos, upload them first, then send `imageAssetIds`
   with the old and the new IDs together.
3. After an edit, the listing goes through moderation again.

## Hiding, sold, deleting

- "I sold it" → `change_listing_status` with `mark_sold`.
- "Hide it for now" → `deactivate`, and later `reactivate`.
- Deleting is permanent. Suggest `deactivate` first, and delete only after the user explicitly
  confirms that they want the listing gone for good.
