---
name: envelope-printer
description: Print addresses on envelopes as a PDF with one page per envelope at the real envelope size (#10, A7, DL, C5 and more) from a pasted list, typed names or a CSV/Excel file, and find which envelope fits a card or folded letter.
---

# Zovo Envelope Printer

Use `generate_envelope_pdf` when the user wants addresses printed on envelopes.

1. Convert the addresses the user pasted, typed or showed in an image into `recipients` objects (`name`, `company`, `address1`, `address2`, `city`, `state`, `zip`, `country`). Keep every address; do not merge or drop any. If converting is hard, pass the pasted text as one string.
2. Pass an attached CSV or Excel list in `file`.
3. Put the sender in `return_address` when the user gives one.
4. Set `envelope_size` from the request (#10 is the default, "5x7" or "invitation" is A7, "RSVP" is A2, DL/C5/C6 for A4 countries). Call once without asking about optional settings.
5. Share the PDF link, the list of envelopes to check, and the printing note (print at 100%, test page first).

Use `find_envelope_size` when the user asks which envelope fits a card, photo or folded sheet, or how big an envelope is.

Do not use for postage, shipping labels, label sheets, or checking that an address exists.
