---
name: qr-code-studio
description: Create scannable QR codes for links, text, email, phone, SMS, contact cards, and timed or all-day calendar events with the generate_qr_code and generate_text_qr_code tools, including print-size and contrast checks.
---

# Zovo QR Code Maker

Use `generate_text_qr_code` for a plain text QR image. Pass `text` and optional colours, error correction, and scanning distance. Use `generate_qr_code` for links, email, phone, SMS, contacts, and events. Plain text is limited to 1,500 characters and UTF-8 capacity also applies (1,273–2,953 bytes depending on error correction).

1. Pick the `kind` from the request: `url`, `text`, `email`, `phone`, `sms`, `contact`, or `event`.
2. Fill only the fields that kind needs. If the request already contains the content (a link, a name and number, an event date), call the tool right away. Ask one short question only if a required field is missing (for example the event date).
3. Events: pass `start`/`end` as `YYYY-MM-DDTHH:MM` local times, or `YYYY-MM-DD` dates for an all-day event (the end date is the last day, inclusive).
4. If the code will be printed, pass `scan_distance_cm` when the user mentions a distance or a format (poster across a room is about 300, a table tent about 50); use error correction `H` when the code may be scuffed or partly covered.
5. After the tool returns, share the encoded content in one line, any warnings verbatim, the recommended print width if any, and the PNG and SVG download links.

Do not use this skill for Wi-Fi password codes, barcodes (UPC, EAN, Code 128), or reading an existing QR image.
