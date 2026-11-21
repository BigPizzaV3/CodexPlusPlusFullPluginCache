---
name: ai-media
description: Generate standalone AI media with Crealix, such as images with any model, video clips (Veo, Kling, Seedance, Sora…), original songs, talking avatars, motion control, 4K upscales and saved characters. Use when the user asks for an image, a clip, a song, a talking avatar, to make a character dance, or to upscale a file.
---

# AI images, clips, music and more

Every result is saved to the user's Crealix library and can be used in any
video: as a scene, a cover, a song, a character. Each one costs credits: say
the price, and if Crealix answers `CONFIRMATION_REQUIRED`, wait for a yes before
calling again with `maxCredits`.

When the job starts, say one sentence. The card follows it. Say in one line
when it is done and what it cost.

## Images: `generate_images`

- Write a concrete prompt: subject, action, setting, framing, how the light
  falls on the subject. No lamps or beams in frame unless the scene needs one.
- Recommended model and tier unless the user names one. `show_options` with the
  image models only if they want to compare.
- Variants: one call with `count` (up to 4), shown together.
- Edit a picture or keep a subject: `referenceImageUrls` (files in Crealix).
- A visual style from the catalog (`visualStyleId`) when it should match their
  videos. Pick `aspectRatio` for where it will be used.

## Video clips: `generate_video_clip`

Clips are the most expensive thing here. Before generating, tell the user the
model, the length, the resolution, whether it has sound, and the price
(`browse_catalog('video_models')` has each model's options and an example price).
Say which of these you picked because they didn't, and ask. Generate after a
yes.
- From text, from a start image (`imageUrl`), or between two images
  (`endImageUrl`).
- The prompt describes the motion: what moves, how the camera moves, the pace.

## Music: `generate_music`

An original track of about 2–3 minutes: a prompt and style tags, and lyrics if
they have them. It can then score any video (its `trackId` as `musicId`) or
become a music video.

## More tools

- `generate_avatar_video`: a person (a ready avatar, a portrait, or a saved
  character) says a script in a Crealix voice, or lip-syncs an audio file.
- `generate_motion_control`: a character performs the movement of a reference
  video (a dance, a gesture). Both files must be in Crealix.
- `upscale_media`: an image or up to 3 minutes of video to 1080p, 2K or 4K.
- `create_character`: saves a person, mascot or creature so it looks the same
  across videos. From a picture (free) or a description (about 1 credit).

## Files and results

- The user's files must be in Crealix first: an attachment or a link with
  `import_media_from_url`, a file on their device with `upload_media`.
- To compare results side by side: `list_generations` with their `jobIds`.
- `create_share_link` shares a result. `publish_video` posts a clip, avatar or
  image (follow the publish-video skill).
- `delete_generation` only when they ask and confirm which one. It cannot be
  undone and the credits are not refunded.
