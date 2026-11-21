---
name: wignet
description: Drive a Écran Papier framed e-paper display for its owner — show a message, a photo or a generated picture, switch what the frame displays (weather, surf, transit, bikes, a custom image), schedule it, save its battery, and check the result. Also answers price and stock questions about the frames sold on ecranpapier.com. Use whenever the user mentions their Écran Papier or e-paper frame, pastes a app.ecranpapier.com/w/… link, or wants something shown on the frame.
---

# Écran Papier e-paper frame

A Écran Papier is a framed e-paper panel (black and white, some units six-colour
Spectra 6; 800×480 or smaller) that wakes up every few minutes, fetches one
image from the platform and sleeps again. You change what it shows through
the platform; you never talk to the frame itself.

## 1. One frame, one link

Each frame has a personal link, `https://app.ecranpapier.com/w/<id>` (`<id>` = the
frame's unique identifier, the last part of the link). **The link is the key**: whoever holds it
controls that frame and no other. No account, no token, no OAuth.

- No link in the conversation? Ask for it (it is behind the QR code the frame
  shows at first boot). Never guess or reuse one from elsewhere.
- Don't write the link into anything public or shared (a document, a
  public image host, a commit).
- With the installed plugin's shared MCP server `https://mcp.ecranpapier.com/`, pass the
  supplied link in `device` on every screen tool call. Use `describe_device`
  when a screen is first introduced, then `get_state`. Keep the name and link
  together in this conversation; ask which screen if the target is ambiguous.
  Ask for the link again in a new conversation when it is unavailable.

## 2. How to act — pick the first that exists

1. **Device connector (MCP)** — tools named `get_state`, `push_content`,
   `set_service`… The plugin uses `https://mcp.ecranpapier.com/` for all screens; a standalone
   connector can also use `https://mcp.ecranpapier.com/<id>` for one screen. If those
   tools are missing and the user wants you to act, walk them through adding
   it: `references/connecting.md`.
2. **HTTP**, if you can make requests (Claude Code, Codex, an agent): the
   same actions as REST, described per frame at
   `https://app.ecranpapier.com/api/owner/<id>/openapi.json`, and in prose at
   `https://app.ecranpapier.com/api/owner/<id>/guide`. Read the guide once: it lists the
   services, their settings and this frame's current state.
3. Neither: explain what you would do and give the owner the steps.

## 3. The loop, every time

1. `get_state` first. It tells you the service on screen, its settings, the
   schedule rules, `interval_seconds` (how often the frame wakes) and health.
2. Before composing any picture: `get_orientation`
   (its `orientation` and logical width × height) and `get_capabilities`
   (`screen.display_profile`: `mono1`, or `spectra6` for six colours).
3. Act (table below).
4. **Verify.** The frame never shows an error: when a render fails, it just
   keeps the previous image, so a refused change looks exactly like one that
   worked. Call `get_state` again: `health.image_status` = `error` and
   `last_run.error` give the cause.
5. Tell the owner **when** it will appear: at the next wake-up, i.e. within
   `interval_seconds`, not instantly (unless `params.active_watch_enabled`).

## 4. Which action

| The owner wants… | Do |
|---|---|
| A message now, then back to normal | `push_content` with `text` |
| A lasting note on the frame | `set_message` |
| A photo / picture now, then back | `push_content` with an image (§5) |
| A picture that stays or refreshes | host it, then `set_service` `custom` with its `url` |
| Weather, surf, transit, bikes… | `set_service` — the live list of services and their settings is in that tool's description and in the guide |
| Different things at different hours | `get_schedule`, then `set_schedule` with the full list (it replaces every rule; hours are Paris time) |
| Stop a push early | `cancel_push` |
| Save battery (away, holidays) | `sleep`, later `wake` |
| Rotate the content | `set_orientation` (global to the frame) |

Text is rendered by the platform: prefer `push_content` `text` to composing
an image of text. Keep it short (it is read from 2–3 m; the font shrinks as
text grows). Supported markup: a line starting with `# ` is a title, `---`
draws a rule, `**bold**`, blank line = paragraph. Max 2000 characters.

Temporary describes the display override, not a content revision: a text push
overwrites the saved `message_board` text. Expiry restores the usual service,
not the previous message text. Explain this when describing what is preserved;
do not claim that all saved content or permanent settings remain unchanged.

Never send `width`/`height` (admin only, refused) and never pass the whole
`params` object back to `set_service`: only that service's keys.

## 5. Showing a picture

Choose the first route that works where you are:

0. **ChatGPT with a file attached or generated in the conversation** →
   `push_content` with `image_file`; ChatGPT supplies the file object through
   the tool's file parameter. Check orientation and capabilities first and
   pass the orientation. Use this before copying base64 or hosting a photo.
1. **You have a public URL** of the image → `push_content` `image_url`. The
   platform downloads it once, at push time, so a temporary URL is fine.
2. **You can make HTTP requests** → `scripts/compose.py image <file>
   --upload <frame link> --orientation <o>`, which prepares and POSTs it.
3. **You are in a code sandbox without network** (ChatGPT, claude.ai by
   default) → `scripts/compose.py image <file> --base64 --print-base64`,
   then `push_content` with `image_base64` = the printed string, verbatim,
   `image_sha256` = the `sha256` it printed, plus `mode` and `orientation`.
   The string travels inside the tool call: a photo is about 20 000
   characters (sent as a compact JPEG the platform dithers), a line drawing
   a few thousand. With the digest, a copy that changed by one character is
   refused and the frame is left alone; retry the copy.

`compose.py` needs only Pillow. Give it the frame's logical size
(`--width` = `logical_width`, `--height` = `logical_height` from
`get_orientation`) and `--profile spectra6` for a
colour frame. Composition rules for a readable panel:
`references/eink-design.md`.

Always pass `orientation` = the value `get_orientation` returns when it is
not `paysage`: a picture pushed without it on a portrait frame shows up
lying on its side. `mode`: `dither` for photos,
`threshold` for text, logos, QR codes, charts.

The push store is temporary: one image per frame, kept at most 24 h,
replaced by the next. For anything meant to stay, rotate or refresh, host
the image elsewhere and use the `custom` service with its URL.

## 6. Prices, stock, buying

Frames on sale, live prices (VAT and shipping included) and remaining stock:
the shop connector `https://ecranpapier.com/api/shop/mcp` (tools `list_products`,
`get_product`), or `https://ecranpapier.com/api/shop/products` as JSON. Never quote a price
or say what is left from memory — stock is a handful of units and changes
with every sale. Ordering is done by the person on https://ecranpapier.com/boutique.html; you
cannot order for them. A product's `page_url` shows it in full (photos,
characteristics): link that one when discussing a single frame. Anything else (sizes, custom frames, lead times,
a fault that survives the checks above): contact@ecranpapier.com — offer to draft the
email.

## 7. When something is off

- `last_run.error` names the cause; fix and verify again.
- A `set_service` accepted but nothing changed: a schedule rule may be
  overriding it (`get_state` → `schedule_rules`). `push_content` outranks
  rules; `set_service` does not.
- Asleep (`sleep`): changes wait for the next wake. A sleep in progress
  cannot be interrupted.
- More recipes, step by step: `references/recipes.md`.
