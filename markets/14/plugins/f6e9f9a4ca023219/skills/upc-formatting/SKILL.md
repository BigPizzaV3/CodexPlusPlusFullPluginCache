---
name: upc-formatting
description: Mandatory UPC and barcode digit formatting validation for every BRUCE eBay listing. Apply in conjunction with the existing ebay-listings skill whenever creating or reviewing a listing, whether or not the item has a UPC.
---

# UPC formatting: mandatory listing-wide validation

Before sending each BRUCE eBay listing, check every occurrence of a UPC in the Description paragraph, Description bullets, Item Specifics, and all other sections. A confirmed UPC must be reproduced as the exact original digit string, consisting only of ASCII digits 0-9. Never add a trailing period, decimal point, comma, hyphen, space, separator, suffix, or any non-digit character to a UPC value. Do not treat a UPC as a number: do not round it, insert decimal .0, use scientific notation, or remove its leading zeros. Do not invent or append digits, including check digits. If a UPC is unclear, do not guess; omit an unsupported identifier. A period that would ordinarily end a sentence must not directly follow the UPC value. Example of the intended text content: UPC: 012345678905 (the UPC digits have no trailing punctuation).


UPC DISPLAY STYLE (MANDATORY)
Present every UPC value as ordinary plain text in the same font, size, color, and weight as the surrounding bullet text. Never wrap a UPC or the UPC line in Markdown inline-code backticks, fenced code blocks, code styling, quotes, HTML code tags, or any other formatting that makes it appear gray, shaded, highlighted, boxed, or monospaced. Do not use bold or italics solely for the UPC. For example, render the bullet as plain text: - UPC: 881934621420. The UPC digits themselves must still have no trailing period; the example sentence punctuation is not part of the bullet.

Retain all other BRUCE ebay-listings instructions, sections and output rules unchanged.
