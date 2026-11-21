---
name: get-started
description: Create PDF documents from the user's Papely templates. Use when the user asks to list their Papely templates, see the fields of a template, generate one or more PDFs from a template, get a download link, register an image for a template, or email generated PDFs.
---

# Create PDFs with Papely

Use the Papely tools to fill the user's PDF templates with data. Explicit instructions from the user take priority over this guide.

## Workflow

1. Call `list_templates` to find the template the user means. If more than one template could match, ask which one.
2. Call `get_template` to read its fields and the value each field expects:
   - `text`, `date` and `qr`: a string.
   - `image`: an `img_<id>` reference from `register_image_from_url`, or `""`.
   - `table`: an array of rows. Each row has exactly one string (or `null`) cell per entry of the field's `columns`, in the same order.
3. Build `data` with the field keys from `get_template`. Use only values the user gave you; do not invent names, codes or other values. Ask for any value you need. A field you leave out renders blank or with its default.
4. Call `generate_document` for one PDF, or `generate_batch` for up to 100 PDFs from the same template in one job (the batch downloads as a ZIP file). Each document counts toward the generation limit of the workspace. Pass an `idempotencyKey` if you may need to retry the same call.
5. Call `get_generation_status` every few seconds until the status is `completed` or `failed`. If it failed, tell the user the error message.
6. When it is completed, call `get_generation_document` and give the user the download link. The link expires after a short time; call the tool again for a new link.

## Images

For an image field, call `register_image_from_url` with a public HTTPS URL to a PNG or JPEG image. Use the returned `img_<id>` as the value of the field. A registered image can be reused in later generations.

## Email delivery

Only email documents when the user asks for it. An email cannot be undone, so confirm the recipients with the user before you generate. Put each recipient's address in `data.email` (and optionally their name in `data.name`) and pass the `email` template block. Documents without an email address are generated but not sent. Use `get_generation_emails` to report the delivery status of each recipient.

## When not to use Papely

Do not use these tools to read, summarize or convert existing files, or to write free-form text. Papely only creates PDFs from the templates in the user's workspace; templates are created and edited in the Papely web app.
