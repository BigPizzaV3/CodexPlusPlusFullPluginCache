---
name: pdf-merge
description: Merge attached PDFs with page ranges, page order, pages to leave out and rotation (merge_pdfs), split one PDF into several files (split_pdf), and report page count, paper sizes, rotation, encryption, form fields and text (inspect_pdf).
---

# Zovo PDF Merge

1. Merge or edit pages: call `merge_pdfs` with the attached PDFs in `files` (attach order = file 1, 2, ...). With no `parts`, all pages of all files is used in attach order.
2. For page ranges, a new order, pages to leave out or rotation, pass `parts` in output order: `{ "file": 2, "pages": "1-3, 7, 10-end", "skip": "5", "rotate": 90 }`. Pages are 1-based; `end` means the last page; rotation is 0, 90, 180 or 270 degrees clockwise and adds to the page's own rotation. To delete pages from one PDF, pass one file with `skip`.
3. Split: call `split_pdf` with one file and one of `ranges` (one item per output file, e.g. `["1-4", "5-12", "13-end"]`), `every_n_pages`, or `each_page: true`. Up to 50 output files.
4. Inspect: call `inspect_pdf` when the user asks how many pages a PDF has, which pages are rotated, the paper size, whether it is password-protected, or whether it has form fields or selectable text.
5. After a result, give the page count, the plan in one or two lines, the check result, any notes as they are, and the download link. Say the link is kept for 1 hour.

If a range is refused, the message names the bad item: ask the user for a corrected range. Password-protected PDFs are refused; do not ask the user for the password. Do not use this skill to remove passwords, convert PDFs to other formats, compress files, or read and summarize the text.
