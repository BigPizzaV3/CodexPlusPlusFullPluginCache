---
name: avatar-from-photo
description: Turn a photo into a custom Anam avatar, a real-time talking video face, and use it for a persona. Use when the user wants an AI avatar of themselves, a team member or a brand character from an image they have the rights to.
compatibility: Needs the Anam MCP server connected to an Anam account (the Anam plugin in ChatGPT, or https://lab.anam.ai/mcp elsewhere). Attaching a photo works in ChatGPT; other apps need a public image URL.
---

# Create an avatar from a photo

Anam makes a one-shot avatar from a single image: a face that can talk in
real time. Creating one is paid work, so it needs the user's confirmation.

## 1. Check rights and consent

Before anything else, ask:

- Is the person in the photo the user, or someone who has agreed to have an
  avatar made of them?
- For a drawn or generated character, does the user have the rights to the
  image?

If the answer is no or unclear, don't create the avatar. Never make an avatar
of a public figure or anyone who hasn't consented. Offer a stock avatar
instead (`pick-voice-and-avatar`).

Call `anam_connection_info`; creating an avatar needs full access.

## 2. Get the image

- In ChatGPT, the user can attach the photo to the chat; pass it as `image`.
- Otherwise, a public `https` URL as `imageUrl`: JPEG, PNG or WebP, up to
  4.5MB. Local file paths don't work.

A photo of one front-facing adult looking into the camera, mouth closed,
hands away from the face and in even light works best. Anam crops the image
and, where needed, extends it past the edges (`imageProcessing: "auto"`, the
default).

## 3. Confirm the paid work

Tell the user, before calling the tool:

- creating the avatar is paid work: it counts towards the organization's
  avatar creation limits;
- the image goes through moderation, and is stored with the avatar;
- each call creates a new avatar, so a retry needs their yes too.

Wait for their yes. Their app may also ask them to approve the call.

## 4. Create it

Call `anam_avatar_create` with `displayName` (3 to 50 characters) and either
`image` or `imageUrl`, not both. If ChatGPT didn't pass the attachment, the
tool says so: ask the user to attach the image again or give a URL.

The avatar starts in `processing`. Call `anam_avatar_get` with its `id`
about 10 seconds later, and again until `status` is `ready`. If creation is
refused, tell the user the reason it gives, such as moderation or creation
capacity (by default an organization can create two avatars at once).

## 5. Use it

- For an existing persona: find it with `anam_persona_list`, then call
  `anam_persona_update` with `id` and the new `avatarId`. The change is
  published at once.
- For a new persona: call `anam_quickstart` with `avatarId` (see
  `create-persona`).

Finish with a share link so the user can see and talk to the avatar: the one
`anam_quickstart` returns, one from `anam_share_link_list` (`personaId`), or a
new one from `anam_share_link_create`.

## Rules

- Only use images of people who have consented, and images the user has the
  rights to.
- Don't create an avatar to impersonate someone or to deceive the people who
  talk to it.
