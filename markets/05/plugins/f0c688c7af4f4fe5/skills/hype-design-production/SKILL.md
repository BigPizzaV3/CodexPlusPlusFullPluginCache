---
name: hype-design-production
description: Generate one-page fixed-template Hype Events PDF files from direct or email-derived requirements. Use for CTFS, STC, Hype featured awards, and Hype promotion certificates. This workflow never generates images and never redesigns the template.
---

# Hype Design Production

## Non-negotiable output contract

- The only successful deliverable is a `.pdf` created by the bundled deterministic generator from the bundled HTML template and logo assets.
- Never call image generation or image editing. Never use Canva. Never return PNG, JPG, WebP, a newly designed poster, or a text substitute.
- Do not recreate or reinterpret the visual design. The files in `assets/` are the product template, not inspiration.
- If the bundled generator cannot run or cannot produce exactly one PDF page, stop and report the precise blocker. A different-looking image is never an acceptable fallback.

## Workflow

1. Read [references/production-rules.md](references/production-rules.md).
2. Parse the request into structured fields. Preserve the user's spelling, capitalization intent, value symbols, and date wording unless the user explicitly corrects them.
3. Choose one mode:
   - `record`: normal CTFS/STC record poster.
   - `featured`: Hype-only `Best Leader of the Week` or `New Kids on the Block This Week` poster.
   - `promotion`: Hype promotion certificate.
4. Resolve this skill's own directory first, then run its bundled [scripts/generate.py](scripts/generate.py) by absolute path. Do not assume the process starts inside the skill folder. Always pass arguments as a list; never construct a shell command from user text.
5. Let the script copy the fixed template, export with Google Chrome, verify that the PDF is one page, save it to `result`, and remove temporary files.
6. Confirm that the returned path ends in `.pdf`. If it does not, treat the run as failed.
7. Return only completion status and a clickable path to the PDF. Do not narrate background operations unless the user starts the request with `/详细`.

## Commands

Normal record:

```bash
python3 "/absolute/path/to/hype-design-production/scripts/generate.py" record \
  --brand ctfs \
  --title "Most Profit" \
  --subtitle "In a Day" \
  --value '$300' \
  --name "Cameron" \
  --date "Aug 11th"
```

Hype featured award:

```bash
python3 "/absolute/path/to/hype-design-production/scripts/generate.py" featured \
  --title "Best Leader of the Week" \
  --name "Helia" \
  --date "July 20th - 26th"
```

Promotion certificate:

```bash
python3 "/absolute/path/to/hype-design-production/scripts/generate.py" promotion \
  --name "Sriya Indrakanti" \
  --date "August 7 2026" \
  --role "Corporate Trainer"
```

The repository-local skill defaults to the Project 2 `result` directory. If installed outside Project 2, pass `--output-dir /absolute/path/to/result`.

## Failure handling

- Do not silently switch templates, invoke image generation, use Canva, create a bitmap, or create a text-only substitute.
- If Chrome is unavailable, output cannot be written, or a PDF is not exactly one page, stop and report the precise blocker.
- On failure, preserve the temporary HTML path printed by the generator. On success, do not leave temporary HTML files.
- Ask the user only when an essential field cannot be inferred safely. Otherwise complete the full flow without confirmation.

For installation and handoff, read [references/handoff.md](references/handoff.md).
