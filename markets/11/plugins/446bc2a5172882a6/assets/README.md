# Floyd by The F Suite bundle assets

Visual assets referenced from [`../plugin.json`](../plugin.json)
(`extensions.com.openai.interface.composerIcon` and `.logo`).

**Status: placeholder, pending Design.** `icon.png` and `logo.png` are the production CFO favicon
(`frontend/packages/app/public/favicon/cfo/android-icon-192x192.png`) padded from 135×192 to a
square 192×192, because OpenAI requires square icons of at least 48×48. The padding is mechanical,
not designed — replace both with real square artwork before submission.

| File | `plugin.json` field | Requirement |
|---|---|---|
| `icon.png` | `interface.composerIcon` | Square, 48×48 to 4096×4096, ≤5 MiB |
| `logo.png` | `interface.logo` | Square, 48×48 to 4096×4096, ≤5 MiB |

`interface.screenshots` is deliberately **absent** from `plugin.json`. OpenAI rejects a package
that references a file not present in the ZIP, so the key stays out until real screenshots exist.
(The L Suite bundle references `screenshot-1.png`, which is not committed — add the file or drop
the key there before that plugin is ever submitted.)

## Brand reference

- **Brand color:** `#E03000`, the F Suite orange from
  `frontend/packages/app/src/logos/fsuite.svg`. Contrast is 4.6:1 on white and 3.5:1 on `#212121`,
  both clearing OpenAI's 2:1 floor, so the same value serves `brandColor` and `brandColorDark`.
- **Mark:** see `frontend/packages/app/public/favicon/cfo/` and
  `frontend/packages/app/src/logos/fsuite.svg`.
