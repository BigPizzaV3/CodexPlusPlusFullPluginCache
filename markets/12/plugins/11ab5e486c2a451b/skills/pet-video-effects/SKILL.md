---
name: pet-video-effects
description: Use when the user asks which pet video effects there are, what is new this week, or wants another effect on a photo they already used ('what's this week's new effect?', 'now make it do the zoomies'). Lists Boopreel's effects and remakes a clip in another one.
---

Boopreel animates a pet photo in one of its effects, such as a happy dance, a boop on the nose or the zoomies, and a new effect arrives every Monday. The user's own instructions come first.

## Flow

1. `list_effects` returns `this_week` and the current `effects`, each with its `name`, `blurb` and whether it `is_new`. It makes nothing and uses up nothing.
2. For another effect on a photo already used, `make_pet_clip` takes the earlier clip's id in `from_clip_id` and the new `effect`, so the photo is not attached again. `new_take` set to true makes another take of the same photo and effect.
3. The card shows progress and plays the new clip when it is ready, usually in about a minute.

## Scope

- Animals only; a photo with a person's face in view is refused.
- Each new clip counts toward the 3 clips a person can make each day; a refused photo or a failed clip does not.
