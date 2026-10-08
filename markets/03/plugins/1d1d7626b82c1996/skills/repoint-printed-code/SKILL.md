---
name: repoint-printed-code
description: Change where an already printed, posted, or distributed CodeQR code leads, without reprinting or resending anything. Triggers when a destination moved, a landing page changed, a campaign was redirected, or the user asks to fix a QR code or short link that is already out in the world. Not for creating a new code, not for bulk creation across a list, and not for deleting a code.
---

# Re-point a code that is already out in the world

The user has a QR code on paper, or a short link already sent, and the
destination behind it needs to change. The code itself stays exactly as it is.

Work only through the CodeQR MCP tools. Do not generate a replacement QR image:
producing a new image is the failure this workflow exists to avoid.

## 1. Find the code

- **Short links** — `list_links` accepts `search`, `domain` and `tagId`. Search
  by the slug or by words from the destination.
- **QR codes** — `list_qrcodes` accepts only `page`. There is no server-side
  search, so page through the results and match on key or current destination
  yourself. Do not claim a code does not exist until you have reached the last
  page.

Show the user the candidate you found — key, current destination, scan or click
count — and confirm it is the right one before changing anything.

## 2. Check whether the QR code is static before promising anything

Every QR code record carries a `static` boolean. Read it.

- **`static: false` (dynamic)** — the printed pattern encodes a short link, so
  changing the destination re-points every copy already printed. This is the
  case the user is hoping for.

- **`static: true`** — the printed pattern encodes the destination itself.
  Updating the record changes the dashboard entry and nothing else: every sheet,
  label and sign already printed keeps leading to the old destination, forever.

If the code is static, say so **before** making the change, in plain terms: the
record can be updated, but the printed copies cannot be redirected and the only
fix is a new code on new material. Do not report a static update as a success —
that is the one outcome that would leave the user believing a problem is solved
when it is not.

## 3. Make the change

- `update_qrcode` — pass `qrcodeId` and the new `url`.
- `update_link` — pass `linkId` and the new `url`.

**Change `url` only.** `update_link` also accepts `key`, and changing it rewrites
the short link itself, so every copy already printed or sent stops working. Never
change `key` while re-pointing. (`update_qrcode` cannot change the key at all.)

Both tools are annotated as destructive, so the client will ask the user to
confirm. That prompt is correct and expected — let it happen and do not look for
a way around it.

## 4. Confirm the result

Report back three things, explicitly:

- the key and short link, unchanged
- the old destination and the new one
- for a QR code, whether printed copies now follow the change (dynamic) or do
  not (static)

Scan and click history stays attached to the code across a re-point, so the
user's existing numbers are not reset. Say so if they ask.
