---
name: translate-document
description: Use when the user wants a PDF, scanned PDF, DOCX, EPUB or image translated into another language and returned as the same kind of file with its layout kept. Sends the file to the user's PageTranslate account, starts the translation on the account's word balance and returns a download link.
---

# Translate a document with PageTranslate

PageTranslate translates the file itself, so pages, tables, fonts and images stay in place, and
returns the same kind of file. For a sentence or a paragraph of pasted text, translate it yourself
and do not use these tools.

## Before you start

- **Target language:** a code such as `es`, `fr`, `de`, `it`, `ja`, `ko`, `ar`, `hi`, `ru`. Use
  `pt-BR` for Brazilian Portuguese, `zh` for Simplified and `zh-TW` for Traditional Chinese. The
  source language is detected. If the user did not name a target language, ask.
- **Formats:** PDF (text or scanned), DOCX, EPUB, PNG, JPG, WEBP, TIFF, BMP, GIF. Up to 100 MB and
  1,000 PDF pages. Spreadsheets, slides and subtitles are not supported: say so instead of uploading.

## Steps

1. **Upload:** `upload_document` with the attached file, or `file_url` when the user gives a link,
   and the target language. It returns `job_id`, `word_count` and `covered_by_balance`.
2. **Covered:** when `covered_by_balance` is true, tell the user the word count and ask before
   starting. Starting spends words from their balance and cannot be undone. Then call
   `start_translation`.
3. **Not covered:** when `covered_by_balance` is false, the translation cannot be started here. Say
   that the account's word balance does not cover the document and that plans are described at
   https://pagetranslate.ai/pricing. Do not quote prices and do not offer to sell anything.
4. **Wait:** call `get_translation` about every 30 seconds until `status` is `completed`. If it is
   `failed`, give the reason returned.
5. **Deliver:** call `get_download_link` and give the user the link exactly as returned. It works
   for one hour. Call the tool again for a fresh one.

`list_translations` shows earlier jobs, including documents uploaded on the PageTranslate website.
