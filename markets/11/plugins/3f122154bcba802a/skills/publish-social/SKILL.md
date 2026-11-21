---
name: publish-social
description: Prepare and schedule approved Postroom posts. Use for multi-channel publishing, Pinterest Pins, attachment imports and scheduling requests.
---
Call yet_accounts first. Read yet_brand for saved voice and rules. Import attachments with yet_import_file; use returned workspace media URLs.
Ask for missing date and timezone; pass a future ISO time with an explicit offset.
For Pinterest, call yet_pinterest_boards for every selected account. Ask the user to choose a board unless an explicitly named board matches exactly one result. Never guess the first board. Pass board_ids keyed by account ID.
Prepare a title of up to 100 characters and description of up to 800 characters. Use caption/captions for descriptions, preserving other channels' captions. Suggest a title and show it before approval. Ask whether to add a destination HTTPS URL or omit it; never invent a URL or unsupported tags.
Call yet_preview. Show the exact accounts, board names, Pin title, descriptions, URL and time. A preview does not schedule.
Call yet_approve with the existing draft_id and confirmation approve_exact_preview only after explicit approval of that exact preview. If details change, create a new preview and obtain approval again. Never duplicate scheduling to recover a lost response.
Report queue receipts as scheduled, not published. Verify delivery with yet_post_status. TikTok through this MCP uses inbox upload and needs completion in TikTok.
