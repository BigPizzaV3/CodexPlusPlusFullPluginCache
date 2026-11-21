---
title: Generate and Transform Sprites
description: Request every Sprite Fusion generation operation through one API endpoint.
---

Send JSON to `POST https://www.spritefusion.com/api/v1/generate`. Every accepted request returns an SSE stream.

Read the [Agent Guide](https://www.spritefusion.com/docs/pixel-art-generator/api/agent-guide) before using these operations.

## Generate

### Before using generate

- Describe one item or subject without requesting a number of outputs. The API returns variations automatically: use "Icons of a magic potion," not "15 icons of a magic potion."
- Ask for the subject or variations, not for a grid, contact sheet, atlas, or spritesheet that packs several assets into one image. "Make multiple boats" is acceptable; instructions such as "make a grid of 24 items" or a row-and-column layout are not.

```json
{
  "operation": "generate",
  "prompt": "A clockwork fox carrying a brass lantern",
  "size": 32
}
```

`size` is `16`, `32`, or `64`. The prompt limit is 10,000 characters.

```bash
curl -N https://www.spritefusion.com/api/v1/generate \
  -H "Authorization: Bearer $SPRITE_FUSION_API_KEY" \
  -H "Content-Type: application/json" \
  --data '{"operation":"generate","prompt":"A clockwork fox","size":32}'
```

## Edit

Edits accept one to nine inputs. The first input is the primary sprite.

### Before using edit

- State the requested change and anything important that should remain unchanged.
- Use the first input as the primary sprite and later inputs as supporting visual sources.
- Do not request a spritesheet containing several poses. Create each pose as a separate asset with `edit` instead.

```json
{
  "operation": "edit",
  "prompt": "Give the hero from the first image the sword and shield from the other images",
  "size": 32,
  "inputs": [
    {"asset_id": "asset_hero"},
    {"data_url": "data:image/png;base64,..."},
    {"upload_id": "upl_large_reference"}
  ]
}
```

## Style reference

Style reference accepts one to twenty images.

### Before using style reference

- Describe the new subject and explain the role of each reference when it is not obvious.
- Use `edit`, not `style-reference`, when the goal is a targeted change that should preserve the primary image.
- Do not request a grid, contact sheet, atlas, or spritesheet that packs several assets into one image.

```json
{
  "operation": "style-reference",
  "prompt": "A small forest shrine",
  "inputs": [
    {"asset_id": "style_1"},
    {"asset_id": "style_2"}
  ]
}
```

`size` is optional for `edit` and `style-reference`; when omitted, Sprite Fusion infers an appropriate `16`, `32`, or `64` target from the inputs.

See [Edit Your Pixel Art](https://www.spritefusion.com/docs/pixel-art-generator/edit-your-pixel-art) and [Style Consistency](https://www.spritefusion.com/docs/pixel-art-generator/generate-pixel-art-with-style-consistency) for creative guidance.

## 8 directions

### Before using 8 directions

- Provide exactly one source image.
- Do not write or send a prompt; `direction-set` has no prompt field.

```json
{
  "operation": "direction-set",
  "inputs": [{"asset_id": "hero"}],
  "size": 32
}
```

This returns exactly eight directional sprites. See [Generate 8 Directions](https://www.spritefusion.com/docs/pixel-art-generator/generate-8-directions-for-your-pixel-art).

## Animate

### Before using animate

- Make sure the source sprite has a pose suited to the requested motion. For walking, running, attacking, jumping, and similar actions, first use `edit` to create an appropriate starting pose, then animate that edited asset. Idle and other subtle animations can usually use the original sprite directly.
- Describe the motion, energy, and whether it should loop.
- Set frame and color counts with `output_frames` and `colors`, not in the prompt.
- Do not request a spritesheet layout in the prompt.

```json
{
  "operation": "animate",
  "prompt": "A relaxed idle bounce, seamless loop",
  "inputs": [{"asset_id": "hero"}],
  "output_frames": 8,
  "colors": 24
}
```

`output_frames` may be any even number from 2 through 16. The animation prompt limit is 2,000 characters. The output asset includes `assetUrl` for the animation, `sourceImageUrl`, `spritesheetUrl`, frame count, and FPS.

See [Animation Tips](https://www.spritefusion.com/docs/pixel-art-generator/animation-tips) before animating a new source.

## Save generated files

Each `output` event contains a persisted Sprite Fusion asset. Download the returned `asset.assetUrl` into your project. Do not depend on hotlinking the hosted URL indefinitely; keep project-owned copies of files you ship.
