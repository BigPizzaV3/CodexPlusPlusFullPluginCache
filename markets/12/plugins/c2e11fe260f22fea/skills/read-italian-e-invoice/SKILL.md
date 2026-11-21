---
name: read-italian-e-invoice
description: Read the files of Italian electronic invoicing that the user attached (FatturaPA invoices as .xml, signed .xml.p7m or a zip, and receipts of the Sistema di Interscambio SdI such as a notifica di scarto, an _NS_ file) with the read_e_invoice_files tool of e-invoices.it. Explain an invoice - parties, amounts, VAT, due dates, payment details, withholding tax - or why the SdI rejected an invoice the user sent and how to correct it, or sum up several invoices (a download massivo) - revenue, costs, VAT, top customers and suppliers, imposta di bollo, ritenute and anomalies to check for the accountant. Use it whenever the user attaches such a file, asks about an attached Italian e-invoice, or says their e-invoice was rejected ("scartata").
---

# Read Italian e-invoice files

The `read_e_invoice_files` tool of e-invoices.it reads the files of Italian
electronic invoicing (FatturaPA, the XML exchanged through the Sistema di
Interscambio, SdI). What it returns depends on the files:

- **one invoice**: its data, and the invoice is shown as a readable document next to
  the answer;
- **a notifica di scarto** (the SdI rejected an invoice the user sent: an XML file
  with `_NS_` in its name and one or more five-digit error codes, e.g. `00404`),
  with the rejected invoice if attached: each error explained, with the current
  values of the fields it concerns;
- **another SdI receipt** (delivery receipt, mancata consegna, esito, decorrenza
  termini): what it means;
- **several invoices** (more files, a zip or a download massivo from Fatture e
  Corrispettivi): aggregates for the business and its accountant, not the single
  invoices.

## When to use it

- The user attached a `.xml`, `.xml.p7m` or `.zip` file that is, or may be, an
  Italian e-invoice or an SdI receipt. Pass **all** attached files in one call: a
  notifica di scarto together with its invoice gives the best answer.
- Call `read_e_invoice_files` with the attached files. Do not ask the user to paste
  the XML as text, and do not try to read the file yourself first.
- The user says an invoice was rejected but attached only the invoice: read it, and
  ask for the `_NS_` file they received (by PEC, from their invoicing software or
  from the Fatture e Corrispettivi portal) to explain the rejection.
- Do not call it without an attached file, or to create, check in advance, change
  or send an invoice: it only reads.

## How to answer about an invoice

1. Answer only from the tool result (`structuredContent`). Never invent or estimate a
   value; if a field is missing, say that the invoice does not contain it.
2. Unless the user asks something specific, give a short summary:
   - document type, number and date
   - supplier and customer, with their VAT numbers
   - total amount and currency; the net amount to pay if there is withholding tax
   - due dates, payment method and IBAN
   - names of the attachments, if any
3. The invoice is shown in full next to your answer: do not repeat every line item
   unless the user asks for them.
4. Codes: the result has a description next to each code (document type `TD..`, VAT
   nature `N..`, VAT due `I`/`D`/`S`, payment method `MP..`). Use the descriptions and
   explain them briefly when they matter, e.g. `S` is split payment.
5. Amounts with two decimals and their currency; dates in the user's usual format.

## How to answer about a rejection (notifica di scarto)

1. Answer only from the tool result (`structuredContent`). For each error in
   `Errori`:
   - the code and, in one sentence, what is wrong (`Spiegazione`; else the SdI's
     `Descrizione`);
   - where: the field (`Campi`) and, if the invoice was attached, the value it has
     now (`ValoriNellaFattura`);
   - the correction: start from `Correzione` and the SdI's `Suggerimento`, and make
     it concrete with the values, e.g. "line 3: 8 × 18.40 = 147.20, not 147.00".
2. The SdI's `Descrizione` often names the exact field, line or value: use it.
3. Keep the correction a **proposal**. Say what to change and in which field; the
   user changes it in their invoicing software. Do not write a corrected XML file
   unless the user asks for it, and if you do, say that their software has to
   produce and sign the file it sends.
4. When you cannot tell the right value (a VAT number, the recipient code, the
   correct VAT nature), say what to check and with whom (the customer, their
   accountant), and do not guess.
5. End with what to do now (`DopoLoScarto`): the rejected invoice counts as not
   issued and is sent again, corrected.
6. `NotaFattura`: if present, mention it. The attached invoice may not be the one
   that was rejected.

## How to answer about several invoices

1. Answer only from the tool result (`structuredContent`): aggregates, not the single
   invoices. `company` is the business the invoices are about (the party of most of
   them); if `tied_with` is set, another party has as many, so say which one was
   taken and ask if it is the right one.
2. Unless the user asks something specific, give a short overview:
   - the company and the period;
   - issued (`sales`) and received (`purchases`) invoices: number, taxable amount,
     VAT, total; the largest customers and suppliers;
   - the VAT position (`vat_position`) and, if useful, the trend by period
     (`by_period`) and the expected cash flow from the due dates (`cash_flow`);
   - what an accountant (commercialista) looks at, when present: imposta di bollo per
     quarter with its F24 code (`bollo`, and `to_check`: invoices without bollo that
     may need it), ritenute d'acconto operated and suffered per month and supplier
     (`ritenute`), and the anomalies to check (`controlli`, each with the invoices
     concerned).
3. `remarks` point out what stands out (a customer or supplier with a large share,
   a weak period, a possible cash shortfall): mention them.
4. Everything is an aid to be checked, not a tax return or a verification of the
   invoices: say so when the user may act on it.
5. For one Excel file, readable PDFs or the full dashboard of the same invoices,
   point to https://e-invoices.it.

## In every answer

- Answer in the user's language. Keep the Italian terms and field names the user
  sees on the invoice or in their software (imponibile, ritenuta d'acconto, imposta
  di bollo, PrezzoTotale) and translate them once.

## When the tool cannot read the files

- **Too many invoices**, or **the analyses of several invoices are used up** for
  now: the chat has a limit of invoices per call and of analyses per user. Relay the
  note: e-invoices.it handles many invoices at once (one Excel file, PDFs, a
  dashboard) at https://e-invoices.it; or offer to look at fewer invoices here.
- **Several notifiche di scarto**: the tool explains one at a time; ask which one.
- **Another SdI receipt**: relay what the tool says. These are not rejections.
- **Not an e-invoice** or an unreadable file: say so, and suggest the XML or
  `.xml.p7m` from the Agenzia delle Entrate portal (Fatture e Corrispettivi) or from
  the supplier. A PDF is only a copy of the invoice and cannot be read by the tool.
- **The service is busy**: say so and suggest trying again in a minute.

## Limits

- This is no tax or legal advice, and e-invoices.it does not check invoices before
  they are sent: a corrected invoice may still be rejected for another reason. For
  decisions and doubts about VAT, refer the user to their accountant
  (commercialista).
- The legally valid invoice is the XML file; a PDF attached to it is only a copy.
- e-invoices.it processes the files only in memory: it does not store them and
  does not log anything about them. Say only this about e-invoices.it, and make no
  statement about how ChatGPT or OpenAI handle the user's data.
