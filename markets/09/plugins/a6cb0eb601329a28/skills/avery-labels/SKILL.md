---
name: avery-labels
description: Print address labels, return address labels, shipping labels, name badges, place cards and file folder labels from a typed list or an uploaded CSV/Excel file, as a PDF that lines up with standard US Letter label sheets (5160/8160, 5161, 5162, 5163, 5164, 5167, 5195, 5366, 5395, 22805 and more).
---

# Sheetwise Label Maker

Tools: `generate_label_sheet` (the PDF), `find_label_template` (sheet sizes and margins), `check_mailing_list` (review a list before printing).

1. When the user gives names and addresses, call `generate_label_sheet` right away. Put each address in `labels` as an object
   (`name`, `company`, `address1`, `address2`, `city`, `state`, `zip`, `country`) or as text with lines separated by `\n`.
   When they attach a CSV or Excel file, pass it in `file`; columns are detected. Pass `columns` only if the user names unusual headings.
2. Pick `kind` from the request: address (default), return_address, shipping, name_badge, place_card, file_folder, general.
   Pass the product number the user mentions in `template` (8160, 18160 and 5260 all mean the 5160 layout). Without one, the kind picks a default.
3. Partly used sheet: "start at label 7" means `start_at: 7`. "Two of each" means `copies: 2`. One return address for a whole sheet:
   `kind: "return_address"` with one label (it fills the sheet; `sheets` sets how many).
4. USPS all-caps style only if asked (`uppercase: true`). Sort by ZIP only if asked.
5. After the call, share the label count, the sheet, any problems found (missing ZIP, unknown state), and the PDF and CSV links.
   Remind the user to print at 100% / Actual size. Suggest `alignment_test: true` if they worry about alignment.

Do not use for buying postage or carrier shipping labels, label-maker tape printers, barcodes, or nutrition labels.
