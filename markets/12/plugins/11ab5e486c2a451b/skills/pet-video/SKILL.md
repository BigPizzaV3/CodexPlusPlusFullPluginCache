---
name: pet-video
description: Use when the user wants their dog, cat or other animal animated from a photo ('make my dog do a happy dance from this photo'). Turns the pet photo into a 5-second video clip.
---

Boopreel turns a photo of a pet or other animal into a 5-second video clip: the same animal, from the user's own photo, moving in one of Boopreel's effects (for example a happy dance, a boop on the nose or the zoomies). The clip plays in the card in the chat and can be saved as an MP4 from the clip's own page. This skill covers making a clip, checking it, trying another effect and deleting clips. The user's own instructions come first.

## Inputs

- **A new clip** (`make_pet_clip`): the photo the user attached in the chat (`photo`), what the animal is as seen in the photo (`pet`, for example "corgi puppy" or "orange tabby cat") and its kind (`pet_kind`). Optional: the effect id (`effect`, for example happy-dance, boop or zoomies; this week's new effect when omitted) and the pet's name if the user said it (`pet_name`).
- **Another effect on the same photo**: the earlier clip's id in `from_clip_id` instead of `photo`, so the photo isn't attached again.
- **Another take** of the same photo and effect: `new_take` set to true.

## Flow

1. `make_pet_clip` starts the clip and returns at once with `clip` (its `clip_id`, `status`, `effect_name` and, once ready, `watch_url`) and `clips_left_today`. The card shows progress and plays the clip when it's ready: about a minute, or a few minutes when the video machine has to start first. One call per request is enough.
2. `get_pet_clip` returns a clip's `status` and, once it is ready, its `watch_url`, the page where the clip is saved or shared.
3. `list_effects` returns `this_week` and the current `effects`, each with its `name`, `blurb` and whether it `is_new`. It makes nothing and uses up nothing.
4. `list_my_clips` returns the user's recent `clips` from the last 30 days, and `delete_pet_clips` deletes one clip (`clip_id`) or all of them (`all`), with their photos and pages.

## Scope

- Animals only. A photo of a person, or of a pet with a person's face in view, is refused; a person far from the pet is cropped out. Boopreel never animates people.
- Each person can make up to 3 clips a day. A refused photo or a failed clip doesn't count.
- Clips are AI-generated, carry a small "Boopreel · AI" mark and are deleted after 30 days.
- Boopreel makes videos only. Drawing, editing or restyling a still picture is outside it.
