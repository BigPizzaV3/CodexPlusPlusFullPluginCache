---
name: email-images
description: Put images into an Apsis Vega email, whether they come from the web, from the user's computer, or were generated. Use when the user wants images in an email, or attaches images for one.
---

Apsis Vega works on the user's Apsis account. The company is Apsis, with a capital A and the rest in lower case, never in all capitals, and the product is Apsis Vega. Once the user has picked an account and a section, pass the same `account` and `section` to every later call. When a tool result asks for the user's go-ahead, say what the next call would do and wait for their answer in a new message. The user's explicit instructions take priority over this skill, and a tool's own refusals and notes always apply.

## Images from the web

An image already on the web works as it stands: put its URL in the email and the user gets a finished, previewable email at once. Hosting it at Apsis is an improvement, not a precondition, because another site may block or change the image after the send, and every open tells that site who opened it. Offer it, and if the user agrees, pass the whole set to `host_email_images_from_url` in one call; Apsis fetches them itself and needs nothing from the user. An image on plain http is worth hosting rather than just offering, since many mail clients block it.

## Images from the user's computer

The upload is the user's to do: they open a link, pick the files, and their browser sends them straight to storage. Nothing passes through the chat.

1. Settle each file's format first. Only PNG, JPEG and GIF can be hosted, and each slot is signed for one type that can't change later. WebP, AVIF, HEIC, BMP, TIFF and SVG have to be converted first. A picture attached to the chat shows what the image looks like, not what format the file is, and a file named .jpg is often WebP inside.
2. Files over 5 MB can't be uploaded; a phone photo usually is. Around 1200 px wide is a good size for email.
3. For several images, `create_email_image_uploads` gives one link for the whole set. List the images in `images` in the order the user should pick them, each with a short `label`. Where the image was your choice, found on the web or generated, add its `source_url` so the user knows where to get it.
4. Relay the link message as it stands. It already lists the slots in order with their formats. Add beside the link only what it can't know, such as which converted file goes in which slot, and any question still open: an earlier message in the same turn is often never read.
5. Once the user says the upload is done, call `finalize_email_image_uploads` once with every `upload_id`. Don't create a second link for the same files.
6. Retry a finalize only on not-found, once. A format or size refusal fails the same way again. An expired link needs a new create.

## Generated images

You can't upload a generated image yourself. It has to reach somewhere the user can get at first, then go through an upload link like any other file. A sandbox path, a file URL or a data URI renders broken for every recipient.

## Into the email

Put each finalized `imageUrl`, or each `hostedUrl`, into an img tag's src in the HTML for `create_email_activity` or `edit_email_activity`. An edit makes the last preview stale, so preview again before a send.
