# Plugin listing assets

OpenAI requires square PNG (or JPEG/WebP/SVG) icons **at least 48×48**, max 5 MiB each.

## Source of truth (committed)

| File | Use |
|------|-----|
| `dark_db_logo.png` | Light UI surfaces (`logo`, `composerIcon`). Sync from `public/brand/dark_db_logo.png`. |
| `white_db_logo.png` | Dark UI surfaces (`logoDark`, `composerIconDark`). Sync from `public/brand/white_db_logo.png`. |

Optional listing screenshot: add `screenshot.png`, then in `plugin.json` set `"screenshots": ["./assets/screenshot.png"]`. Do not declare `screenshots` until the file exists in the ZIP (upload validation fails otherwise).

`npm run build:openai-plugin` copies missing icons from `public/brand/` when absent in this folder.
