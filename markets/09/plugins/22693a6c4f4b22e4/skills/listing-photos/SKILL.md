---
name: listing-photos
description: Virtually stage or enhance real estate photos through ListingScene, check ListingScene credits, and retrieve previously generated listing photos.
---

Use the ListingScene MCP tools with the connected account.
If a tool requests authentication, let the host's account-linking flow connect the user; do not ask for passwords, session cookies, or API keys.

For a first edit, use the attached photo through the tool's `photo` file parameter.
For a follow-up edit, pass the actual preceding result URL as `sourceUrl` instead.
Supply exactly one of `photo` or `sourceUrl`.
Do not download or reupload a ListingScene result to continue editing it.
The host supplies `download_url` and `file_id`, with optional `mime_type` and `file_name`.
Do not invent file identifiers or temporary download URLs.
Accept JPEG, PNG, or WebP photos under 25 MB.

Read `get_account` before generation and explain that each successful image uses one credit.
An explicit request to stage or enhance a photo authorizes the requested generation.
When inputs are sufficient, proceed using the requested style or correction.
Ask for a missing photo or room type when staging cannot proceed.
Stage one photo per call; for multiple photos, check that credits cover the requested count before starting.

Use `stage_photo` for furnishing and decor.
Supported room types are Living Room, Bedroom, Kitchen, Bathroom, Dining Room, Office, Basement, and Patio.
Styles are standard, modern, minimalist, scandinavian, mid-century modern, farmhouse, industrial, coastal, and luxury.
Set `replaceFurniture` to false when the user wants to preserve existing furniture.
Preserve the existing architecture, camera angle, and structural features.

Use `enhance_photo` for general-enhancement, general-and-sky, brighten-and-balance-lighting, fix-color-cast, blue-sky-and-window-view, straighten-walls-and-perspective, or declutter-small-items.
Choose the enhancement that matches the user's request.
Use `general-and-sky` for overall enhancement plus sky correction in one pass and one credit.
Sky replacement and decluttering change visible details; describe the actual chosen correction.

When the user asks for editing options or has not chosen an edit, call `show_photo_editor` with the attached photo.
It shows Stage + Enhance, Virtual stage, and Enhance choices, style examples, corrections, remaining credits, and the exact Generate cost without spending credits.
Stage + Enhance costs two credits and supports `stage-first` and `enhance-first` orders.
For a requested sequence, check credits cover both edits, run the tools in the requested order, and pass the first returned URL as `sourceUrl` for the second call.
If the second step fails, stop and show the completed first result; check history before retrying.
Infer `roomType` from the attached photo and current conversation when clear, such as Kitchen or Living Room.
Pass it to the editor even in choose or enhance mode, and to `enhance_photo` and `show_photo_result` so later staging is prefilled.
Preserve an explicit user room choice and leave it unset when uncertain.
Do not request the user's full ChatGPT history.
Keep explicit generation requests direct rather than requiring a menu.

After generation, call `show_photo_result` with the actual returned `url` and original attached `photo` and identified `roomType` to display the before/after slider, download, and actions to enhance or stage the finished result.
For an existing result, use its actual history URL; the result must belong to the connected account.
If the host does not support the interactive view, display the actual image URL and include a usable download link.
Label staged images as virtually staged and enhanced images as edited.
Do not promise MLS compliance, exact image fidelity, or a successful result when the tool reports an error.
Do not automatically retry generation after a timeout, transport error, or uncertain result because the first request may have completed and spent a credit.
Use `list_history` to check for the result first and let the user decide whether to retry.

Use `get_profile` to identify the connected account and `list_history` to retrieve existing results.
The plugin does not publish listings, contact prospects, change subscriptions, or charge payments.
