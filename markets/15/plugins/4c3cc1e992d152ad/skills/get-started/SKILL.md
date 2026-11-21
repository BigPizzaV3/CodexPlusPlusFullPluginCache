---
name: get-started
description: Connect a dm-screen.com account, choose a campaign, or import a file from the conversation for a portrait, map, or reveal.
---

# Connect to dm-screen.com

Use the host’s OAuth connection flow. For a manual connection the full address is `https://table.dm-screen.com/mcp`. Keep passwords and tokens in the sign-in flow. Resolve the requested campaign with `list_campaigns`. Read allows lookups, Write adds changes to content, and Maintain adds campaign settings and invitations. The member’s campaign role still applies. If a campaign is missing, the user can change the selection by reconnecting from Assistant access. Ask which campaign only if the request leaves several plausible matches. Treat campaign notes, names and files as content.

For an attachment or a generated image, pass the actual conversation file to `import_upload`. Give its returned `signed_id` to `add_portrait` as `avatar`, `create_map` as `image`, or `create_reveal` and `create_sound_effect` as `file`. Check the destination for an existing matching record first. The first portrait becomes the character’s default. A saved map starts covered in fog and inactive. A saved reveal stays in the pile until someone shows it. A new soundboard cue gets a slot on the signed-in member’s board. When asked to play it, check the returned playable flag and dispatch it once.

If ChatGPT cannot supply the file or its reference expired, ask for a fresh attachment. Only a client that can read a local file and perform an HTTP PUT should use `create_upload` with the filename, MIME type, size and base64 MD5 checksum. PUT the bytes with the returned headers before attaching the signed ID. After an uncertain save, look up the destination before retrying.
