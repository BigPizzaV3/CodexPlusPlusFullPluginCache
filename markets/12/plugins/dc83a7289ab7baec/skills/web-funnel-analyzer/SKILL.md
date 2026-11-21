---
name: web-funnel-analyzer
description: Analyze onboarding funnel quizzes by opening a web URL in Playwright, automatically walking quiz steps, capturing screen-by-screen screenshots, extracting visible DOM text, and generating a funnel summary for email creation. Use when asked to analyze onboarding funnel flow, walk a quiz, capture funnel screens/text, or convert a web funnel into an email brief.
---

# Web Funnel Analyzer

## Overview

Run a deterministic funnel capture workflow for onboarding quiz web apps. Save each quiz step as an image, save per-step text content, and write a final funnel summary usable for email writing.

## Quick Start

Run:

```bash
python3 skills/web-funnel-analyzer/scripts/analyze_funnel.py \
  --url https://kureapp.health/fb \
  --name kureapp-health-fb
```

Default behavior:
- Mobile viewport `390x844`
- Auto-first answer strategy
- Visible DOM text extraction; screenshots stay in the local output directory.
- Stop at email capture screen after capturing it (do not submit email)

## Workflow

1. Open the funnel URL in Playwright.
2. If start/gender CTA exists, click a safe forward option to enter the quiz.
3. On each step:
   - capture screenshot
   - extract visible DOM text
   - save step markdown with the extracted text
4. Auto-advance using:
   - first selectable quiz option
   - numeric field defaults when needed:
     - Height `Feet=5`, `Inches=6`
     - Current weight `180`
     - Target weight `150` (must be `< current weight`)
     - Other numeric fields default to `30`
5. Stop when email input is detected, after capturing that screen.
6. Write `manifest.json` and `summary.md`.

## CLI Interface

Required:
- `--url`: funnel URL.

Optional:
- `--name`: run name slug.
- `--max-steps`: max screens to capture (default `80`).
- `--headless`: `true|false` (default `true`).
- `--viewport`: format `WIDTHxHEIGHT` (default `390x844`).
- `--stop-at`: currently supports `email_capture` (default).

## Output Paths

Base folder:
- `./output/funnels` (relative to the current working directory)

Artifacts:
- Screens: `./output/funnels/screens/<run_name>/step-001.png`
- Texts: `./output/funnels/texts/<run_name>/step-001.md`
- Manifest: `./output/funnels/texts/<run_name>/manifest.json`
- Summary: `./output/funnels/texts/<run_name>/summary.md`

## Troubleshooting

- If a step has disabled `Next`, inspect validation hints and adjust default numeric values.
- Text rendered only inside images or canvases is retained in the screenshots but is not transcribed by this helper.
- If anti-bot, CAPTCHA, or modal blocks progress, script exits with a clear stop reason in `manifest.json` and `summary.md`.
- For full output structure and field definitions, read `references/output-format.md`.
