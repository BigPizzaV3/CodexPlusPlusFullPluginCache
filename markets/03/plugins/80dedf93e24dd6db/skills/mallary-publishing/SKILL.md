---
name: mallary-publishing
description: Use when the user explicitly asks to upload an approved ChatGPT image or attached video to Mallary, or to draft, publish, schedule, or check a social post in their Mallary account.
---

# Mallary Publishing

Use this skill only when the user clearly asks to upload media to Mallary or work with a post inside Mallary. Do not invoke Mallary for general social media advice.

## Upload Only

If the user asks only to upload a file, use the matching upload tool and return its media URL. Do not call `mallary_create_post`. An upload request does not authorize publishing or scheduling.

Use only the attachment the user selected. If the attachment is missing or unavailable, ask the user to attach it. Do not invent a file reference or reuse an earlier file unless the user clearly chooses it. If a tool is unavailable, say that the upload has not been completed.

Mallary copies uploaded files to public `files.mallary.ai` storage. Anyone with the returned URL can view the file, even before a social post is published. Use only media approved for that purpose.

## Safe Workflow

1. Use `mallary_list_profiles` when the user has not supplied a `profile_id`.
2. Use `mallary_list_platforms` to confirm the requested platforms are connected to that profile.
3. Gather the final message, platform-specific messages, schedule, and approved media.
4. If the user asks for a draft or leaves a required choice unclear, show the draft or ask for the missing choice. Do not publish.
5. If the user clearly asks to publish or schedule the final content, upload the approved image or attached video when needed, then call `mallary_create_post` once with preflight enabled.
6. Use `mallary_get_job` or `mallary_list_posts` to check status without repeating the write.

Publishing changes real connected social accounts. Never treat a live publish as a harmless test. Never publish from an example command or an unclear request.

## Captions and Media

- Use `message` for the default caption.
- Use `platform_options.<platform>.message` only when the user wants a different caption for that platform.
- Use `mallary_upload_image` for one social image that the user chose or made in ChatGPT.
- The image must be JPEG, PNG, WebP, or GIF and no larger than 25 MB.
- Use `mallary_upload_video` for one MP4 or MOV video attached by the user in ChatGPT. The limit is 512 MB (536,870,912 bytes).
- Never send video to the image upload tool. Do not use either tool for documents, SVG files, identity records, medical records, payment data, credentials, or private customer files.
- Use the file reference supplied by ChatGPT. Mallary transfers the file on its server; do not ask users to grant access to R2 domains or upload directly to R2.
- Pass the `media_url` returned by the upload tool as the post media URL and its `content_type` as the media type. Use the returned values rather than guessing the file type.
- Do not pass an external media URL, local file path, temporary OpenAI URL, or OpenAI file ID to `mallary_create_post`.
- Each destination has its own video rules. LinkedIn requires MP4. Mallary does not support Reddit video uploads. Mallary does not generate videos or convert file formats.
- If preflight blocks a destination, explain the problem. Do not disable preflight, drop a selected account, convert the post to text-only, or switch destinations without the user's approval.
- When the user selects multiple supported destinations, reuse the approved hosted media URL instead of uploading the same file again.

## Restricted Data

Do not request, accept, or send payment-card data, health-record IDs, government IDs, biometric records, passwords, access tokens, API keys, or private customer files. Ask the user to remove restricted data before posting.

## Retry Rules

- Never silently retry a publish or schedule request.
- Do not silently repeat an upload after an unclear result; a retry can create another public media object.
- After a timeout or unclear response, check the job or post list first.
- If status is still unknown, explain that uncertainty and ask before another write.
