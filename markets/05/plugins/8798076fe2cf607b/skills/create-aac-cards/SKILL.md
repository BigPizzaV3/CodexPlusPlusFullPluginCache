---
name: create-aac-cards
description: Use when creating AAC communication cards, visual schedules, choice boards, or Korean-labeled communication pictures adapted to a student's visual profile.
---

# Create AAC Cards

## Overview

Create text-free AAC images and exact labels, then package them in editable printable A4 HTML. Keep profiles pseudonymous, use uploaded or host-provided files, and preserve a complete image fallback when image generation is unavailable.

## Required references

Read both files before creating cards:

- `references/profile-schema.md` for profile fields, defaults, privacy, and storage.
- `references/aac-image-guidance.md` for prompt construction and visual constraints.

## Runtime boundaries

- Treat profiles as session- or host-local data. Do not promise that a profile persists across chats unless the host explicitly provides persistence.
- Never request a machine-specific Windows path from a public ChatGPT user. Ask for an uploaded image or use the file reference supplied by the host.
- Use the portable Python builder when the host provides portable code/file execution. Use the PowerShell builder only on Windows/Codex hosts.
- If neither builder can run, return the prepared JSON and image prompts and state exactly: `HTML was not created`.

## Workflow

1. Offer exactly these Profile paths before creating images:
   - **Existing profile**: list pseudonymous profile files and let the user choose one.
   - **New profile**: collect the six fields below and save a new file without overwriting.
   - **Default profile**: load `profiles/default.md` without asking profile questions.
2. For a New profile, ask one question at a time in this order: `alias`, `visual_style`, `visual_complexity`, `concept_range`, `sensory_constraints`, `card_size_constraints`. Accept `Unknown` or `모름` and substitute the matching default value.
3. List the requested card labels exactly as entered. If one label has multiple likely meanings, ask one question at a time until the intended meaning is clear. Do not ask extra questions for unambiguous labels.
4. Create one image-generation prompt per card using the selected profile and the image guidance. Keep all text, labels, letters, captions, and watermarks out of the image.
5. If image generation is available, generate one image per card. If image generation is unavailable or fails, return the prompts and ask for one uploaded image per card; continue the workflow instead of stopping.
6. Create UTF-8 JSON with `title`, `profile_alias`, `cards_per_page`, and `cards`. Each card contains `id`, exact `label`, and local `image_path`.
7. Run the deterministic builder through the host's available portable file/code execution tool:

```text
python <plugin-root>/scripts/build-aac-html.py --InputJson <cards.json> --OutputHtml <result.html>
```

On a Windows/Codex host where portable execution is unavailable, use:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File <plugin-root>/scripts/build-aac-html.ps1 -InputJson <cards.json> -OutputHtml <result.html>
```

8. Report the JSON, image, and HTML file references. If neither builder ran, report the JSON and prompts and state `HTML was not created`. Never overwrite an existing profile or HTML file automatically.

## Quick reference

| Situation | Action |
|---|---|
| No profile selected | Offer Existing profile, New profile, and Default profile |
| New profile field is unknown | Record `Unknown` and use the default for generation |
| Card meaning is ambiguous | Ask one meaning question at a time |
| Image generation works | Generate text-free images |
| Image generation is unavailable | Return prompts and collect uploaded images |
| Portable code execution is available | Run `build-aac-html.py` |
| No builder is available | Return inputs and state `HTML was not created` |
| Output path exists | Choose a new path |

## Builder input example

```json
{
  "title": "생활 AAC 카드",
  "profile_alias": "sample-student",
  "cards_per_page": 4,
  "cards": [
    {
      "id": "drink-water",
      "label": "물 마시기",
      "image_path": "images/drink-water.png"
    }
  ]
}
```

## Common mistakes

- Do not put labels inside generated images; render exact labels in HTML.
- Do not collect real names, diagnoses, or medical history by default.
- Do not silently choose a profile when no profile is selected.
- Do not stop merely because image generation is unavailable.
- Do not ask public ChatGPT users for machine-specific Windows paths.
- Do not claim that HTML was created when no builder actually ran.
- Do not crop replacement images or overwrite existing outputs.
