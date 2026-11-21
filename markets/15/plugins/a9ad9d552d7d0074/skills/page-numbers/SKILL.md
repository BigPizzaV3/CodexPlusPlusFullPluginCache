---
name: page-numbers
description: Stamp page numbers (stamp_page_numbers), Bates numbers with a CSV log (stamp_bates_numbers), or a text watermark such as DRAFT (stamp_watermark) on an attached PDF, upright on rotated and cropped pages, with each stamp found again in the new file.
---

# Zovo Page Numbers

1. Page numbers: call `stamp_page_numbers` with the attached PDF. `format` uses `{n}` (this page's number) and optional `{total}` (the last number), e.g. "Page {n} of {total}" (default), "{n}", "{n}/{total}". `position` is one of top-left, top-center, top-right, bottom-left, bottom-center (default), bottom-right, as the reader sees the page. Use `skip_first` for a cover page and `start_number` to continue from an earlier file.
2. Bates numbers: call `stamp_bates_numbers` with `prefix`, `start`, `digits` (zero padding, default 6) and optional `suffix`. For a set of files, call once per file and use the "next file starts at" number from the previous result.
3. Watermark: call `stamp_watermark` with `text` (e.g. DRAFT), optional `opacity` (0.05 to 0.5), `angle` (-90 to 90) and `pages` (e.g. "1-3, 8").
4. After a result, give the first and last stamp, the check result, any notes as they are, and the download link (kept for 1 hour). For Bates, also give the CSV log link.

Text uses the standard PDF font: Latin letters, digits and common punctuation. If the tool refuses characters, ask the user for a Latin version. Password-protected PDFs are refused; do not ask for the password. Do not use this skill to sign PDFs, remove watermarks, or edit the page text.
