---
name: mail-merge
description: Mail merge a spreadsheet (CSV, Excel .xlsx, pasted list, typed records or a list of names) into one print-ready PDF of personalized letters, certificates or #10 envelopes, using preview_mail_merge and generate_merged_documents.
---

# Mergewell Mail Merge

Use these tools when the user wants a mail merge to PDF: personalized letters from a spreadsheet, certificates for each name on a list, or envelopes from a contact list.

1. Data: pass the attached CSV/XLSX as `file` (add `sheet` for a named tab), or `csv_text` for a pasted list, `records` for rows typed in the chat, or `names` for a plain list of names. Do not retype a whole attached file into `records`.
2. Template (letters): put the text from the salutation to the last paragraph in `template`, using the user's column names: `{{First Name}}`, defaults `{{First Name|Friend}}`, formats `{{Amount:currency}}`, `{{Gift Date:date}}`, `{{Place:ordinal}}`, conditions `{{#if Company}}...{{else}}...{{/if}}`, `{{#if Seats = 1}}`. Put the sender block in `sender`, and `closing`, `signature_name`, `signature_title` separately. The recipient address block is built from the address columns automatically.
3. Certificates: set `certificate_kind` (completion, achievement, participation, appreciation, recognition, excellence), `body_template`, `organization`, up to 3 `signers`, and `style` (classic, gold, modern, deco). Award, completion and participation certificates only; no diplomas, degrees, licenses or accreditation.
4. Envelopes: `sender` is the return address; `envelope_size` "10" (default) or "a7"; `usps_style` for uppercase USPS style.
5. When columns or the template are uncertain, call `preview_mail_merge` first. It lists fields with no matching column (with the closest column), fuzzy matches to confirm, and records with empty values. Fix with `field_map`, a default, or `missing_values` (leave_blank, skip_record, placeholder).
6. `generate_merged_documents` returns ONE PDF (one document per record, up to 2,000 per call) and a merge report CSV. For longer lists call again with `start_record` = `batch.next_start`.
7. After the tool returns, give the counts, repeat warnings about empty values or fuzzy matches, and share the PDF and CSV links (they expire in about an hour).

This plugin does not send email (Outlook, Gmail, Mailchimp), print, or mail anything, and does not make mailing labels.
