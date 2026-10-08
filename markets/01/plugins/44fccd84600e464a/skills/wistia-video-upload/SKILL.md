---
name: wistia-video-upload
description: >
  Runs the standard set of setup steps for a new Wistia video: folder placement, tagging,
  metadata (title/description), and player customizations (captions/branding). Use this
  skill whenever the user asks to upload a video to Wistia via Claude, or references a
  video they just uploaded and wants it set up/organized/finished/published. Trigger on
  phrases like "upload this to Wistia", "set up this video", "finish setting up the video
  I just uploaded", "organize this video", "run the upload checklist", or when a Wistia
  hashed_id/URL is shared right after an upload. Do NOT trigger for general Wistia
  analytics, editing, or remix requests that aren't about onboarding a newly uploaded video.
---

# Wistia Video Upload Workflow

## Welcome message

Show this to the user before starting the workflow:

> Let's finish setting up your new video: folder, tags, title, description, captions, and branding.
>
> Have the video file or URL ready if it's not uploaded yet. Know which folder it belongs in? Even better, though not required.
>
> When we're done, it'll be fully organized and ready to publish.

---

Runs Wistia's standard new-video setup: folder placement, tagging, metadata, and player
customizations. Works whether the user is uploading a video through Claude right now or
pointing at a video they just uploaded some other way.

All Wistia actions use the Wistia MCP tools — call `tool_search` for the relevant tool name
(e.g. "wistia folders", "wistia tags", "wistia update media") before each new tool family,
since these are deferred tools and their exact parameters aren't in context by default.

---

## Step 0: Identify the video

- **New upload**: if the user is providing a file or URL to upload, hold off on calling
  `upload-media-to-folder` / `import-media-from-url` until Step 1 (folder) is resolved —
  folder is required at upload time for `upload-media-to-folder`.
- **Existing/recent upload**: if the user references a video without a hashed_id (e.g. "the
  video I just uploaded"), use `get-medias` (sorted by most recent) to find the likely match
  and confirm the title with the user before proceeding. If a hashed_id or Wistia URL is
  given directly, use `get-medias` to pull its current details as a baseline.

Never guess a hashed_id. If there's any ambiguity about which video, ask.

---

## Step 1: Folder placement (always ask)

Folder is never inferred — always ask the user which folder/project this belongs in, every
time, even if a recent chat used the same folder.

1. Call `get-folders` to list current folders so you can offer real options rather than
   guessing names.
2. Ask the user which folder to use (or whether to create a new one).
3. If new upload: pass the folder into `upload-media-to-folder` directly. If existing video:
   use `move-media` to relocate it.
4. If the user wants a new folder, use `create-folder` first, then place the video there.

---

## Step 2: Metadata (title & description)

Write clean, sensible title and description copy from context — the video's existing title,
any source material discussed in the conversation, and the folder/purpose. There's no fixed
naming convention to follow, so use good judgment: clear, specific, human-readable.

- Apply directly via `update-media` (no need to ask for approval first).
- Always show the user what title/description was set as part of your final summary, so
  they can ask for edits if it's off.

---

## Step 3: Tagging (confirm before applying)

Unlike metadata, tags are **not** applied without confirmation.

1. Call `get-tags` to pull the account's existing tag list.
2. Suggest tags for this video by matching against the existing taxonomy first — reuse
   existing tags wherever they reasonably fit rather than inventing near-duplicates (e.g.
   don't create "onboarding-video" if "Onboarding" already exists).
3. Only propose a brand-new tag if nothing in the existing list fits.
4. Present the proposed tag list to the user and wait for confirmation (or edits) before
   applying anything.
5. Once confirmed: use `create-tags` for any genuinely new tags, then `bulk-tag-media` (or
   the single-media tagging path) to apply the final set.

---

## Step 4: Player customizations (standard preset — apply directly)

The standard preset is: **use Wistia's account-level defaults, and make sure captions and
branding are turned on.** No per-video customization, no need to ask — just verify and fix
these two things:

1. **Captions**: check `get-captions` / `show-accessibility-customizations` for this media.
   - If captions already exist and are enabled, leave as-is.
   - If captions exist but are disabled, enable them via
     `update-accessibility-customizations`.
   - If no captions exist, note it in your summary and point the user to caption
     generation in the Wistia app — don't generate captions from here.
   - Note in your summary if caption generation is still processing (it's async — use
     `get-background-job-status` if you need to check on it), since it won't be instant.
2. **Branding**: check `show-sharing-customizations` and/or `show-appearance-customizations`
   for this media to see whether Wistia branding is currently shown or hidden.
   - If branding is off, turn it back on (account default) via the corresponding
     `update-*-customizations` call.
   - If branding is already on (the default), leave everything else untouched — don't apply
     any other appearance changes.

Do not touch thumbnail, colors, CTAs, or other appearance settings beyond this — those stay
at whatever the account default already is.

---

## Step 5: Summary

End with a short, concrete recap of what was actually done, e.g.:

```
✅ Video: [title] ([hashed_id])
📁 Folder: [folder name]
🏷️ Tags: [tag1, tag2, ...]
📝 Title: [title set]
📝 Description: [description set]
🎬 Captions: [on / processing / already present / missing — add in Wistia]
🎨 Branding: [on (default) / re-enabled]
```

If anything is still pending (e.g. captions processing), say so explicitly rather than
implying the checklist is fully done.

---

## Handling gaps and edge cases

- **Can't find the video** → ask for the hashed_id or Wistia share URL directly rather than
  guessing from `get-medias`.
- **No folders exist yet** → offer to create one before proceeding; don't default to "no
  folder" silently.
- **Ambiguous tag match** (e.g. both "Webinar" and "Webinars" exist) → surface the ambiguity
  to the user in the confirmation step rather than picking one.
- **Caption generation still processing** → just note the pending status in the summary.
- **User only wants part of the checklist** (e.g. "just tag this one") → run only the
  requested step(s), skip the rest, and don't ask about folder/customizations unless they
  bring it up.
