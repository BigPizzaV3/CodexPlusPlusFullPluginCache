---
name: ai-generation
description: "Find stock media and generate images, voiceover, music and stickers in Donkey Cut with the account's credits. Use when the user needs media the project does not have."
---

# Finding and creating media
Start with the user's project assets, attached files and links. import_media imports ChatGPT attachments or URLs into the cloud project. Poll a returned job with get_job_status, then use the asset ids in the completed result. Ask for missing footage or a reference when it is needed to fulfill the request.
stock_search finds existing footage, images and sounds; stock_add imports a chosen result. Inspect the media before placing it. ChatGPT can plan a sequence from the supplied footage and use add_clip with blocks to mark missing shots for the user.
Available generation commands include generate_image, voiceover_generate, generate_music and create_sticker. Use them when the user requests generated media; they spend account credits. Each tool's schema lists current options. Inspect returned asset ids and placement, and place an unplaced asset with add_clip or add_overlay_video when the user asked for it in the cut.
When a requested operation is unavailable, explain the limit and ask the user to supply the required media or complete that step in Donkey Cut.
