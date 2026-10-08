# Plugin assets

Copy branding images here before running `node scripts/validate-and-zip.mjs`.

| File | Role | Constraints |
|------|------|-------------|
| `icon.png` | `composerIcon` in `plugin.json` | Square, ≥48×48, ≤5 MiB |
| `logo.png` | `logo` (primary listing icon) | Square, ≥48×48, ≤5 MiB |
| `screenshot-carousel.png` | Listing screenshot | Optional format rules; ≤5 MiB |

Optional dark variants if you add them to `plugin.json`:

- `icon-dark.png` → `composerIconDark`
- `logo-dark.png` → `logoDark`

Supported formats: PNG, JPEG, WebP, SVG.
