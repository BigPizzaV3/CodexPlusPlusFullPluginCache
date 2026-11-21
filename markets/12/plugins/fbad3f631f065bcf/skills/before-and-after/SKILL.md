---
name: before-and-after
description: This skill should be used when the user asks for a "before and after", "slider", "share these job photos", or gives a before photo and an after photo of finished work. It shows a slider and a share link. It does not generate images.
---

# Before and after

Use this skill when the user has two photos of a job: one before the work and one after. Show a slider. Do not generate an image.

## When the host can take files

1. Confirm which photo is the before photo and which is the after photo.
2. If a person is the subject of either photo, tell the user not to upload it. Stop if they still want that photo in the slider.
3. If the after photo is a concept the user made with the host's image tool, set `concept` to true. The slider then says "Concept, the finished work can differ". VanReceipts does not draw that image.
4. Call `create_comparison` with both photos. Pass attached files in `before` and `after`. Use `beforeBase64` and `afterBase64` only when the host cannot pass an attached file. Give the user the share link and the delete link.
5. Photos are removed when the user opens the delete link, or after 30 days, whichever comes first. The link is unguessable. No account is required.

Call `get_comparison` when the user already has a share link and wants the slider again. Call `delete_comparison` only with the delete token from the uploader's link.

## When the host cannot take files

Say that this slider needs both photos uploaded in a chat that accepts files. Do not ask the user to email the photos to a new address, and do not invent a storage account. The share link, once created, opens the same slider on the VanReceipts server.

## What not to do

Do not generate the after photo. Do not collect a precise location from the photo. VanReceipts strips location data on upload. Do not ask the user to pay, and do not pitch a plan. The only site link is https://vanreceipts.app
