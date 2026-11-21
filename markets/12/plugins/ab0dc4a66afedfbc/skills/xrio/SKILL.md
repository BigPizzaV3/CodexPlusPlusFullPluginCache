---
name: xrio
description: Check, create and read German e-invoices (XRechnung, ZUGFeRD / Factur-X) with the xrio MCP server. Use when the user wants to validate an e-invoice file, create an e-invoice from invoice data, a document or free text, turn an e-invoice XML into a readable PDF, get a download link for a file xrio created, or keep the company data, bank accounts and logo of the user's invoices.
---

# xrio — German e-invoices

xrio is a processing API with an MCP server named `xrio`. Its tools describe themselves; this
skill adds the order of the steps and the rules around them.

## Rules

- **Never handle the API key.** Do not ask for it, do not accept it in the chat, never write it
  into a file, a command or a tool argument. The user creates it in the xrio portal
  („API-Schlüssel“) and sets it themselves — as the environment variable `XRIO_API_KEY` or in
  the prompt of their client. A client that signs in to xrio through the browser (OAuth — Claude,
  ChatGPT, Claude Code without a key) needs no key at all.
- **Files never travel through the chat.** No file content and no base64 in a tool argument. A
  file to check goes to an upload link with `curl`; created files come back as download links
  on `api.xrio.de` — `curl -o <name> <downloadUrl>` fetches them. In claude.ai an attached file
  sits in your sandbox; sending it needs the user's setting „Ausgehenden Netzwerkverkehr
  erlauben“ (Einstellungen → Funktionen → Codeausführung und Dateierstellung) with `api.xrio.de`
  among the additionally allowed domains — a 403 from the sandbox proxy means it is missing: ask
  the user to add it. A chat
  without a shell, or without that setting, sends the user to the xrio portal instead: the page
  Testen checks a file or makes its PDF view, the page Firmendaten takes the logo. Never ask
  for the file's content.
- **Official sources, no tax advice.** Report findings with rule, wording and source as xrio
  returns them. Which invoice type, tax category or exemption applies is the user's decision —
  say so instead of choosing.
- **Never guess invoice values.** VAT IDs, tax numbers, IBANs, addresses, dates, amounts and the
  Leitweg-ID come from the user or their documents. Ask for anything missing.

## Check an e-invoice

1. Call `validate_invoice`. It returns `uploadLink` — single use, valid 10 minutes.
2. Send the file as the raw request body: `curl --data-binary @<file> <uploadLink>`.
3. Report the `verdict`: `valid`, `invalid` or `notEInvoice` (a PDF without embedded invoice
   XML). For `invalid`, list each finding with `rule`, `requirement` and `source`; call
   `lookup_rule` with the rule ids when the user wants the full official wording of a rule.
4. A used or expired link answers 404 — call `validate_invoice` again. Files over 10 MB are
   refused (413).

Checking costs the account's validation price from its prepaid credit (the tool description
names the default) for a verdict `valid` or `invalid`; a file xrio created for the account, a
PDF without an e-invoice and errors are free — `costCents` in the answer says what it cost. xrio
keeps nothing of the file.

## Turn an XML into a readable PDF

1. Before the paid call, tell the user the price: one document from the prepaid credit.
2. Call `render_invoice`. It returns `uploadLink` — single use, valid 10 minutes. Send the XML as
   the raw request body: `curl --data-binary @<file> <uploadLink>`.
3. A PDF view comes back in `files` — give the user its `downloadUrl` and pass on every entry
   of `notices`: the PDF view is not an e-invoice, the XML stays legally authoritative. With
   `verdict` `invalid` (the account renders invalid XML by setting) also say that the XML is no
   valid e-invoice and list its findings.
4. An invalid XML without that setting returns its `findings`, the notice `RENDER_NEEDS_CONSENT`
   and costs nothing. Report the findings like a check, then ask the user: a PDF view of the
   invalid XML costs one document and is marked invalid on every page — or the issuer corrects
   the invoice first. Only after an explicit yes call `render_invoice` again with
   `allowInvalid: true` and send the same file to the new link. Never set `allowInvalid` on your
   own. A ZUGFeRD / Factur-X PDF is readable already — check it with `validate_invoice` instead.

## Create an e-invoice

1. Call `describe_invoice_fields` for every field and its requirement. Call
   `describe_invoice_types` when it is unclear whether an invoice, a corrected invoice, a credit
   note or a self-billed invoice is wanted.
2. Collect the values and ask for every required one that is missing. `format` is `zugferd`
   (PDF with embedded XML), `xrechnung` (XML; needs `buyerReference`) or `both`.
3. Before the first paid call, tell the user the price: each e-invoice produced costs the
   account's price per document from its prepaid credit (the tool description names the
   default) — format `both` makes two; rejected calls are free.
4. Call `generate_invoice` with `idempotencyKey` set to the invoice number. The account's
   company data (portal: „Firmendaten“) are the issuer: without `seller`, xrio takes the seller
   from them; for a self-billed invoice (389) the buyer issues, so leave out `buyer` and send
   the supplier as `seller`. Without an
   IBAN, a credit transfer takes the account's default bank account; when the user names another
   one, call `list_bank_accounts` and send its id as `payment.bankAccountId`. `withLogo` puts the
   account's logo on the ZUGFeRD PDF (`true`) or leaves it off (`false`); leave it out to follow
   the account's setting.
5. A rejection is an error result with every finding at once; each names the field
   (`location`, a JSON pointer such as `/lines/1/price` — or the XML path in `xpath` when no
   field fits), the rule, its wording and the `businessTerm`. Correct exactly those values — ask
   the user where the source does not hold them — and call again with the same `idempotencyKey`.
6. On success, pass on every entry of `notices` and give the user the `downloadUrl` of each file
   in `files`.

## Company data, bank accounts and logo

The account keeps its company data (the issuer — the seller, or the buyer of a self-billed invoice), up to 5 bank accounts with one default, and a
logo for its ZUGFeRD PDFs. Every change shows in the account's change log with this key's name.

- **Read freely:** `get_company_data`, `list_bank_accounts`.
- **Change only on the user's explicit request** — never because an invoice or a document holds
  other values: `update_company_data` (send only the fields to change), `save_bank_account`
  (without `bankAccountId` it adds one, with it it changes one; `isDefault: true` makes it the
  default), `delete_bank_account`, `set_company_logo`, `delete_company_logo`. Repeat the change
  to the user before the call.
- The default bank account can only be deleted as the last one. Ask the user which account
  becomes the default, make it the default with `save_bank_account`, then delete.
- `set_company_logo` returns an upload link like `validate_invoice`: send the PNG or JPEG
  (at most 2 MB) with `curl --data-binary @<file> <uploadLink>`.

## Account settings

The account's settings decide the layout of its PDF views (`pdfViewLayout`: `xrio` or `kosit`),
whether its logo is printed on its ZUGFeRD PDFs (`logoOnZugferd`, needs a kept logo) and whether
an invalid XML is rendered as a charged, marked PDF view on every channel (`renderInvalid`).

- **Read freely:** `get_account_settings`.
- **Change only on the user's explicit request:** `update_account_settings`, sending only the
  fields to change. Every change shows in the change log with this key's name.
- **Switching `renderInvalid` on charges money on every channel, the API included.** Tell the user
  what it costs and ask; send `confirm: true` only after a clear yes. Without it the result is
  `CONFIRMATION_REQUIRED` and nothing changes. A client with its own confirmation dialog shows it
  as well — the change needs both yeses. Switching it off needs no confirmation.

## Download links and earlier results

A download link opens without login for 24 hours; the file is deleted 7 days after it was
created. For a fresh link call `get_download_link` with the `fileId` from `files`.

To find a result of the last 7 days again — a new chat, a lost `fileId` — call
`list_history_entries`, best with `idempotencyKey` set to the invoice number; each entry carries
its files with fresh links. It lists metadata only: there is no search by invoice content.

## Calls that take longer

`generate_invoice` and a PDF view run as jobs. Normally the answer comes within seconds as
always. When many calls wait, a call can outlive its wait and answers with `isError`, a
`jobId` and status `queued` or `running` — it is not lost. Do not send it again: call `get_job`
with that `jobId` after a few seconds until the status is `done` (the result is in
`generateResult` or `renderResult`, a rejection in `problem`) or `failed` (nothing was
charged; then send the call again).

## Errors

A failed call is a tool result with `isError`, an `errorCode`, a `detail` and a `traceId`. Give
the user the `traceId` for questions to xrio.

- `INSUFFICIENT_CREDIT` — nothing was created or charged. Ask the user to top up their credit in
  the xrio portal („Guthaben“).
- `VALIDATION_FAILED` — the values break a rule; the `findings` say which.
- `CONFLICT` — the `idempotencyKey` was used with other values (a different invoice needs its
  own key).
- `TIMEOUT`, `UNAVAILABLE` — a service did not answer in time. Nothing was charged; retry the
  same call with the same `idempotencyKey`.
- `NOT_FOUND` — the file or link is unknown or expired.
- The server refuses the connection (HTTP 401) — the API key is missing, expired or revoked. The
  user creates a new one in the portal and sets it themselves.
