---
name: bulk-qr-codes
description: Create a dynamic QR code or trackable short link for every row of a list, spreadsheet, or CSV in CodeQR, using predictable keys so any of them can be re-pointed later without reprinting. Triggers on bulk phrasing such as for each, every, one per, or a pasted list of destinations. Not for a single one-off code, not for reading or decoding an existing QR image, and not for offline or static QR generation.
---

# Bulk QR codes and short links

Create one CodeQR destination per row of a list, so the whole set can be measured
and re-pointed later without reprinting anything.

Do all of this through the CodeQR MCP tools. Never generate a QR image locally and
never call the CodeQR REST API directly: the connector already holds the user's
authorization, and a locally generated image cannot be re-pointed or measured,
which is the entire reason to use this workflow.

## Choose one resource type

- **Dynamic QR code** — `create_qrcode`. Use when the destination will be printed:
  signage, packaging, menus, labels, property boards.
- **Short link** — `create_link`. Use when the destination will be sent, posted,
  or clicked.

If the user has not said which, ask once. Do not create both for the same row.

## Before creating anything

1. Read the source list. Extract per row: the destination URL, and a label that
   identifies the row (property name, job title, product SKU).

2. Derive a `key` for each row from its label — lowercase, ASCII, words joined by
   hyphens, no spaces — prefixed with a short batch name shared by the whole set,
   for example `spring-menu-01`, `spring-menu-02`.

   The key is how the user finds and re-points one specific code months later.
   Omitting it gets a random 7-character slug and defeats the workflow, so always
   set it.

3. Show the row count and the **first two rows fully resolved** — label,
   destination, key — and get the user's confirmation before creating the rest.

   Confirmation is not optional here. Each call publishes a live endpoint on the
   public internet and consumes the workspace's plan quota, and a wrong prefix
   across 200 rows is 200 codes to clean up by hand.

## Creating

There is no bulk endpoint. Call the tool once per row, in list order.

- `create_qrcode` — pass `url`, `key`, and `type: "url"`.
- `create_link` — pass `url`, `key`, and `tagIds` when the user wants the batch
  tagged. Create the tag first with `create_tag` and reuse its ID for every row.

A batch does not have to be links. `create_qrcode` also encodes Wi-Fi networks,
contact cards, WhatsApp chats, email, SMS, phone numbers, plain text and crypto
requests — one per room, per branch, per sales rep. Pass `type` and the payload
named after it on every row, exactly as for a single code. The field names have
traps in them, so follow the `wifi-and-contact-qr-codes` skill for the payload
and this one for the batch mechanics.

`create_qrcode` exposes no tag parameter through this connector, so a batch of QR
codes cannot be tagged as it is created. Say that the connector cannot tag them
here — do not say CodeQR cannot tag QR codes, because the dashboard can — and
offer the shared key prefix as the way to group the batch instead.

If a row fails, record the failure and continue with the remaining rows. Report
every failure at the end. Do not stop the batch silently, and do not retry a row
that failed on a plan or quota limit — the retry fails the same way.

## Report back

Return one table, one row per input row:

| label | key | short link | destination | status |

The user pastes this back into their source sheet, so the key and short link
columns matter more than prose. Do not collapse the table into a summary.

## Re-pointing later

When the user returns to change destinations:

1. Find the codes. `list_links` accepts `search`, so filter by the batch prefix
   there. `list_qrcodes` takes only `page` — there is no server-side search, so
   page through the results and match the key prefix yourself.
2. Call `update_qrcode` or `update_link` per code with the new `url`.

Two rules for this step:

- **Never change `key` on a re-point.** `update_link` accepts a new key, and
  using it rewrites the short link itself and breaks every copy already printed
  or shared — the opposite of what this workflow exists for. Change `url` only.
  (`update_qrcode` cannot change the key at all, which is the safer default.)

- **`update_qrcode` reaches printed copies only for dynamic QR codes.** A static
  QR code encodes the destination directly in its printed pattern: the stored
  record changes, and anything already printed keeps leading to the old
  destination forever. Check before promising the change reached the paper.

## Measuring the batch

`get_analytics` with `event: "scans"` for QR codes and `event: "clicks"` for
short links. Pass `qrcodeId` or `linkId` for one code, or omit both for the whole
workspace. `groupBy` accepts time, country, city, device and browser.
