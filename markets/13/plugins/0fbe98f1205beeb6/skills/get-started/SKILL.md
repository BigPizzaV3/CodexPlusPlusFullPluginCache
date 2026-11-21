---
name: get-started
description: Set up a default QRsome brand look on first use, then make, find, change and measure QR codes.
---

# Getting started with QRsome

QRsome makes QR codes in the chat. The user connects their QRsome account by signing in with email.
The first saved look becomes the default for new codes. A look contains a shape, color and optional
logo; each code can use another saved look by name, use no saved look with `look: "none"`, or override
individual fields.

## First-use brand setup

When the user starts using QRsome, call `list_looks`. If a default look exists, use it and do not
repeat setup. If no look exists, help the user create one:

1. Ask in one short message for their preferred shape (classic, rounded, dots or elegant), color,
   optional logo (attached image, image URL or website), and optional brand/look name. Accept any
   details they have already given instead of asking again. In Spanish, use **Mi marca** as the name
   when they give none; in English use **My brand** and in Portuguese **Minha marca**.
2. If they attach an image, call `upload_logo` with its file parameter, then use the returned
   `logo_url` in `save_look`. An image URL can go straight into `save_look`. For a website, call
   `logo_from_website` and use its returned `logo_url`. File attachments work only when the chat host
   supplies the image as a file parameter. If it does not, ask for an image URL or website. Never
   ask the QRsome widget to call `upload_logo`: widget calls cannot use tools with file parameters.
3. Call `save_look` with the chosen name, shape, color and optional logo, and `default: true`. If
   the user skips customization, save the named look with `shape: "classic"` and `fg: "#1F2A4D"`.
   QRsome checks color contrast and reports colors that cannot scan reliably.
4. Tell the user that this look will be applied to new codes, and show its sample. Do not create a
   QR code until the user asks for one or has already supplied its content.

If the user asks for a QR immediately, make it. Use their supplied brand details for its look. Then
offer the setup in one short follow-up; when they agree, save that code's look with `save_look` and
`from_code`. Do not make setup a requirement for creating a QR.

## QR tools

| Task | Tool |
| --- | --- |
| One code | `create_qr` (`dynamic: true` for a link that may change later) |
| Many codes at once, with a ZIP | `create_qr_batch` |
| Find by words or list recent codes | `search_qr_codes`, `list_qr_codes` |
| Open or change a code | `get_qr_code`, `update_qr` |
| Restore its previous appearance | `undo_qr_look` |
| Scan counts for a dynamic code | `get_qr_stats` |
| Save, list or delete looks | `save_look`, `list_looks`, `delete_look` |
| Find a website logo or store an attached image | `logo_from_website`, `upload_logo` |

For a new code, omit `look` to use the default. Set `look` to a saved name to use that look, or to
`"none"` when the user requests no saved look. A shape, color or logo passed with `create_qr`
overrides that part of the chosen look. `update_qr` can change an existing code's look. Saving or
changing a look does not redraw codes already made with it.

Static codes hold their content directly. Dynamic codes point through a short qrsome.com link, so
their destination can change after printing and their scans can be counted. Image download links
keep serving a code's current appearance after `update_qr`.

QRsome makes QR codes only, not barcodes. Colors need at least 3:1 contrast against the background.
Codes do not expire; deleting a dynamic code stops its short link. Support: support@qrsome.com.

Free includes 10 active dynamic codes and 100 new static codes per calendar month (UTC). Deleting a dynamic code frees a place; deleting static codes does not refund creations. Existing codes keep working. An account can save 5 brand looks. Requests remain rate limited.
