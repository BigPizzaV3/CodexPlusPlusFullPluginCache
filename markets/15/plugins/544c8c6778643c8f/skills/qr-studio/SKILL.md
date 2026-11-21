---
name: qr-studio
description: Use when the user wants to create, restyle, save, open, or export a QR code — a link, Wi-Fi network, contact card, email, SMS, phone number, location, calendar event, or plain text — especially when they want a designed QR with colors, shapes, or a center logo.
---

# QR Studio

QR Studio is a design studio for styled QR codes. The hosted MCP server runs at `https://iplugin.dev/qr/mcp`; a self-hosted copy can run at `http://127.0.0.1:8801/mcp`. The preview and editor are an MCP App, and saved designs and exports stay in the current MCP session (the local copy uses `~/.iplugin-qr`). There is no account, analytics, or separate model call.

The code is rendered by the vendored [qr-code-styling](https://github.com/kozakdenys/qr-code-styling) library, so the encoded payload is a real QR code, not a picture of one.

## Opening the studio

Call `qr_home` when the user wants to design, preview, or manage QR codes interactively. It opens the fullscreen studio, resumes the active design, and returns `{ design, designs }`. It is the main render tool. Do not call it in a loop.

`qr_state` is the same data without opening another view; the studio uses it while booting. `qr_list` returns only the library summaries.

## Creating and changing

- `qr_create` — build, save, and open a new design. Provide either `data` (the exact payload) or `content` (a structured object such as `{ "type": "wifi", "ssid": "Home", "password": "secret", "encryption": "WPA" }`).
- `qr_update` — change a saved design by `id`. Only the supplied fields change.
- `qr_open` — open a saved design by `id`.
- `qr_delete` — permanently delete a design.
- `qr_save` — internal tool for the studio editor. Models should not call it.

Structured content types and their fields:

| Type | Fields |
| --- | --- |
| `url` | `url` |
| `text` | `text` |
| `wifi` | `ssid`, `password`, `encryption` (`WPA`/`WEP`/`nopass`), `hidden` |
| `vcard` | `firstName`, `lastName`, `org`, `title`, `phone`, `email`, `url`, `address`, `note` |
| `email` | `to`, `subject`, `body` |
| `sms` | `phone`, `message` |
| `phone` | `phone` |
| `geo` | `lat`, `lng`, `label` |
| `event` | `title`, `location`, `start`, `end`, `description` (datetime-local values) |

Use `data` when the user already has a payload. The server builds the correct escaping for Wi-Fi and vCard; do not hand-assemble those strings when `content` will do it. Never invent a URL, password, phone number, or contact detail the user did not give you.

## Choosing a look

Call `qr_presets` before choosing a style; do not invent preset ids. Presets: `violet`, `ink`, `ocean`, `sunset`, `forest`, `candy`, `gold`, `midnight`, `mono`.

A style is `preset` plus optional overrides: `dotType` (`square`, `rounded`, `dots`, `classy`, `classy-rounded`, `extra-rounded`), `cornerSquareType`, `cornerDotType`, `fg`, `accent`, `bg` (hex or `transparent`), `gradient`, `gradientType`, `gradientRotation`, `shape` (`square`/`circle`), `margin` (quiet zone px at 1024 reference), and `ecc` (`L`/`M`/`Q`/`H`).

Keep the QR scannable:

- Use dark dots on a light background, or the `midnight` preset for light-on-dark. Avoid low-contrast palettes.
- Keep a logo at or below 35% (`logo.size` ≤ 0.35) and leave `ecc` at `H` when a logo is present.
- Do not set `margin` to 0 for print use. The default is 36 px at 1024, about 3.5%.
- If the user asks for a tiny QR, prefer the `ink` or `mono` preset and a larger export size.

## Logos

`logo` accepts `{ enabled, kind: "mark" | "monogram" | "custom", initials, size, margin, hideDots, plate }`. `mark` is the QR Studio glyph, `monogram` draws the user's 1–3 initials on a gradient tile, and `custom` needs an image. For a custom image, use the studio's upload control. Do not claim an upload succeeded unless the tool returned a saved design.

## Exporting

`qr_export` renders a saved design to `png` or `svg` at 256–4096 px and returns a download URL and filename. The hosted service stores the export on the server; a self-hosted copy uses `~/.iplugin-qr/exports`. PNG rendering can use headless Chrome or the server's resvg fallback. Report the URL and file name from the result; do not invent local paths such as `~/Desktop`.

## Data boundary

The hosted service receives the content and logos needed for the user's requested operations and keeps each MCP session isolated; a self-hosted local copy stores design JSON in `~/.iplugin-qr/designs.json` and exports in `~/.iplugin-qr/exports/`. Do not share designs, logos, or payloads with unrelated services. Do not ask for an account.
