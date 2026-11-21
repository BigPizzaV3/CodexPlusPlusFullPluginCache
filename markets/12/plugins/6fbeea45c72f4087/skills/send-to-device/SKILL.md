---
name: send-to-device
description: Turn content into a PDF or EPUB laid out for the user's e-ink device and deliver it to their reMarkable, Kindle, Dropbox or Google Drive.
---

Use this for a file you produce as actual PDF or EPUB bytes: a document the user handed you, a layout you generated, a converted file.

If what you are sending is prose you wrote — a research brief, a summary, our conversation — use `send_markdown` instead and stop here; it does the render and the delivery in one call. See the research-and-send skill. If the user already has a Folio issue, call `send_file` with its `issue_id` rather than rendering it again.

1. Call `list_targets` to see the user's connected devices. Refer to devices by their label, never by type or id. If the target is ambiguous, ask which device. Kindle needs `device_id`; check the file is within the size that target accepts.
2. Read the chosen target's `render` block. Use `page_mm` as the page size and follow its e-ink guidelines: whole-pixel stroke weights, no hairlines, no pale greys, no gradients or tinted backgrounds.
3. Produce the PDF or EPUB. Name it the way Folio does: `DD.MM.YYYY - Title - Device.pdf`, using the user's local date from `get_settings` and the device label.
4. Call `create_upload` with the file name, then run the returned `curl_command` in a shell to upload it. Never paste file contents into the conversation. With no shell, give the user `drop_page_url` to upload it themselves. The link is single-use and expires in 15 minutes.
5. Call `send_file` with the stored file id and the chosen target. A temporary upload is consumed by the first delivery attempt, including a failed one, so a retry needs a fresh `create_upload`.

Confirm delivery in one sentence with the file title and device label. If a step fails, relay the plain message the tool returns and what to do next, never error codes or URLs.
