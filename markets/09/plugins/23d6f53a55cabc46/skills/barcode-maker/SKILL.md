---
name: barcode-maker
description: Make print-ready EAN-13, EAN-8, UPC-A, UPC-E, Code 128, GS1-128, Code 39, ITF-14, ISBN and ISSN barcodes with SVG/PNG downloads and GS1 size guidance, and validate UPC/EAN/GTIN/SSCC/ISBN/ISSN check digits.
---

# Zovo Barcode Maker

Use `generate_barcode` when the user wants a barcode drawn, and `validate_barcode_number` when they only want to know whether a number (and its check digit) is valid or want a conversion (ISBN-10 to ISBN-13, UPC-E to UPC-A, UPC-A to GTIN-13/14).

1. Pick the symbology: retail products `ean13` (12-13 digits) or `upca` (11-12 digits, US/Canada); small packs `ean8` or `upce`; SKUs, bin and shelf labels `code128` (or `code39` if the user's system needs it); cartons `itf14`; logistics labels with AIs `gs1_128`; books `isbn`; magazines `issn`.
2. Pass the number as given. Leave the check digit off to have it computed; if the user gives one, it is verified. A wrong check digit returns an explanation: show it and ask before using `fix_check_digit: true`.
3. GS1-128 data uses parentheses: `(01)` 14-digit GTIN, `(17)` expiry as YYMMDD (convert 2026-12-31 to 261231), `(10)` lot, `(21)` serial, `(00)` SSCC.
4. Size: `magnification_percent` for EAN/UPC/ISBN (GS1 retail range 80-200), `x_dimension_mm` for other types, `bar_height_mm` only if asked. If the user mentions a label printer resolution, pass `printer_dpi` (203, 300, 600).
5. After the tool returns, give the encoded number, the check digit result, the print size in mm, any warnings verbatim, and both download links.

Always make clear that this tool does not issue GS1 numbers: real retail UPC/EAN numbers must be licensed from GS1 (ISBNs from the national ISBN agency). Do not use this skill for QR codes, scanning or reading barcode images, or looking up products, prices or owners of a barcode.
