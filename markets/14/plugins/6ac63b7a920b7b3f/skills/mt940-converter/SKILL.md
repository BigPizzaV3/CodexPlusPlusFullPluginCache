---
name: mt940-converter
description: Convert SWIFT MT940 and ISO 20022 camt.053 bank statement files to Excel and CSV, and check that each statement's opening balance plus credits minus debits equals its closing balance.
---

# Zovo MT940 Converter

Use `convert_mt940_statement` when the user attaches or pastes an MT940 file (.sta, .mt940, .940, .txt) or a camt.053 / camt.052 / camt.054 XML statement and wants it in Excel or CSV, or wants to know whether it adds up.

1. Pass the attached file in `file`. If the user pasted the text, pass it unchanged in `statement_text` (keep the line breaks).
2. Call once. Report the balance check per statement (match, the difference, or why it was not checked), the number of transactions, flagged lines, and the Excel and CSV links.

Do not use for PDF or CSV bank statements, for categorizing spending, or for making MT940 files.
