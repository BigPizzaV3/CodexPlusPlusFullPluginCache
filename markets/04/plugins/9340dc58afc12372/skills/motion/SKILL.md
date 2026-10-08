---
name: motion
description: Camera-driven and cinematic video — dolly, orbit, crane, FPV, drone and aerial shots, plus food and recipe video. Use when the user describes how the camera moves or wants a cinematic clip of a subject. Not for preset viral looks on an uploaded photo (use Effects) and not for fashion motion (use Fashion).
---

# Motion

Read `references/recipes.md` for the move library and `references/models.md` before any
call — model choice here is a quality choice.

## Tokens

| Token | What it does |
|---|---|
| `/dolly` `/crane` `/push` `/track` | Camera moves |
| `/fpv` `/drone` `/aerial` | Drone and FPV footage |
| `/recipe` `/cooking` `/food` | Food and recipe video |
| `/cinematic` | General cinematic treatment |

## Overlap with Effects

**`/orbit` belongs to Effects**, which owns preset looks applied to an uploaded photo. Use
Motion when the user describes a camera move for a scene being generated, or supplies a
still to move *through* rather than a subject to orbit. When both could apply and the user
uploaded a photo, Effects wins.

## Resolving the move

`list_camera_movements` and `list_camera_angles` hold the valid values. **Never invent
one** — match the user's words to a real entry.

**Do not use `list_durations` or `list_resolutions` here** — those describe ad generation.
Video durations and resolutions are per-model allow-lists in `references/models.md`.

| Request | Tool |
|---|---|
| Aerial / drone footage | `generate_drone_video` |
| Food and recipe | `generate_cooking_video` |
| Everything else | `generate_video` with the movement written into the prompt |

If the user supplied a still to move through, pass it as `image_url` with **exactly one**
URL — that switches the call to image-to-video.

## Model choice is the quality decision

Camera control and resolution ceiling vary sharply. From `references/models.md`:

- **Controlled, specific moves** → `seedance-2.5` has the strongest adherence, but caps at
  **720p** and **refuses people**.
- **Quality first** → `ltx-2.3` at 1080p+ (durations 6/8/10 only) or `seedance-2.0` at 1080p.
- **People in frame** → never `seedance-2.5`. Open on `seedance-2.0` at 1080p.

Say which model you picked in one line so the user can ask for something else.

**Never omit `resolution`** — it defaults to the model's lowest tier.

## Food

`generate_cooking_video`. This category reads through **steam, texture and motion** — a
pour, a cut, rising steam. Warm directional light; flat light makes food look dead. Don't
inflate portions beyond what the recipe produces.

## Defaults

`16:9` — these are cinematic shots, not feed content, unless the user says otherwise.
`9:16` for food headed to social.

## Conventions

Never print `org_id`, `folder_id`, or raw asset uuids.

## When something fails

Read `references/errors.md`. Identify the kind of failure before responding: pending jobs
are waited on, technical errors retried at most twice, unsupported capabilities stated
plainly, safety refusals never routed around, and every material change disclosed.

## QA before delivery

Run `references/qa.md` before calling this finished. Inspect the actual output — never
claim quality you have not observed, and say plainly what you could not verify.
