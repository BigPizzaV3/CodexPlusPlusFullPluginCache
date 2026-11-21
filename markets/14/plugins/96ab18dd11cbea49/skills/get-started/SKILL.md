---
name: get-started
description: Check, read and create German e-invoices (XRechnung, ZUGFeRD/Factur-X) with NormAPI, and explain the official business rules they break.
---

# Working with German e-invoices through NormAPI

NormAPI checks e-invoices against the official KoSIT rule set, the one German
public-sector portals use, and states the rule set version with every result.
It is technical validation: it says whether an invoice meets the EN 16931 and
XRechnung rules, not what an invoice should contain for tax purposes.

## Pick the tool by what the user has

- **An invoice to check** (XML or a ZUGFeRD/Factur-X PDF): `validate_invoice`.
  Pass an uploaded file in `file`; XML pasted into the chat goes in `xml` as it
  is. Report the verdict (`acceptable`), the rule set version, and for each
  finding its code, what it means and the fix, quoted rather than paraphrased.
  An INFORMATION finding is a recommendation; only ERROR findings make an
  invoice unacceptable.
- **An invoice to understand** (a received invoice): `parse_invoice`. Answer
  questions from its data (seller, buyer, lines, totals as stated), and say so
  when `notMapped` lists something the question touches. Add `validate: true`
  when the user also wants the verdict.
- **A rule code** such as BR-DE-15 or BR-CO-16: `explain_rule`.
- **An invoice to create**: `generate_invoice`. It needs the user's NormAPI
  account, and each document counts against that account's monthly allowance.

## Creating an invoice

Build the invoice only from data the user gave. If the seller, the buyer, the
lines, VAT or payment details are missing, ask for them instead of inventing
them. Choose the profile by the recipient: `xrechnung` for a German public
authority (it needs the Leitweg-ID as buyer reference, a seller contact and
both electronic addresses), `en16931` for a business. Choose `ubl` or `cii` for
an XML file, `zugferd` for a PDF with the invoice embedded.

A refusal names the rules the data breaks and how to fix each; correct the data
and try again once rather than retrying unchanged. When the allowance is used
up, say so; validating and reading invoices keep working.

## What NormAPI does not do

It does not send invoices to recipients or portals (Peppol, OZG-RE), does
not store invoices, and gives no tax or legal advice.
