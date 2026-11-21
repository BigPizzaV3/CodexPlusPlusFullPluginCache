---
name: submit-claim
description: Prepare and submit a supported Delos Claim Sale, Collections, Factoring, Payment Protection or portfolio enquiry, with optional selected documents. Review the completed details and exact file plan and obtain approval before sending. Lien intake remains paused.
---

# Prepare a Delos enquiry

Read the generated [shared procedure](references/procedure.md) before intake.
Use its normal-chat response style and service-specific party labels while keeping
the completed review summary complete. Native host approval controls still apply.
The procedure also supplies standalone MCP instructions and guidance hints.
Before constructing submission arguments, read the
[submission field reference](references/submission-contract.md) and check the
selected host tool's actual schema, even when a complete draft is already supplied.
Map the reviewed facts to its exact nested keys; conversational labels are not API
aliases. For a single enquiry, use `creditor.name`, `creditor.address`,
`creditor.contact_person`, `creditor.type_of_service_interested_in`, `debtor.address`
and `financials.original_claim_balance`. Do not use `creditor.legal_name` or
`financials.amount`; `debtor.legal_name` is correct for a business debtor.
No Delos account or user-supplied API key is needed.

## Preserve the person's intent

If the user asks about suitability or terms, use `get_product_guidance` when exposed.
Use it even if packaged product facts are already in context; their presence does
not make the live tool absent or optional.
When it is not exposed, use the generated [product snapshot](references/products.md)
and identify its revision/date on first use. A visible guidance failure follows the
shared error procedure, not a silent fallback. Do not switch to a different Delos
connection to obtain an absent tool.

Check the chosen product's availability. Keep the existing four entry points:

| Enquiry | No files selected | Selected files supported by this host |
| --- | --- | --- |
| One Claim Sale, Collections, Factoring or Payment Protection enquiry | `submit_claim` | `submit_claim_with_documents` |
| Portfolio Sale or Portfolio Collections overview | `submit_portfolio` | `submit_portfolio_with_documents` |

Tool names can have a host prefix. Match the tools in this Delos connection.
Dedicated lien intake and files remain paused; use general contact instead.
Do not infer additional portfolio services from legacy accepted enums.

Ask one invoice or several, or which service, only if the request is unclear.
Do not restart the questionnaire after the person has supplied a complete draft.
Use planned payment/payer for PP, invoice recipient for Factoring, and debtor for
Claim Sale/Collections. Keep the existing backend field mapping. Dates and terms
go in the description where appropriate; never invent an invoice number/object.

## Prepare and review

Ask one related group of at most three missing questions at a time. Keep optional
fields optional. Resolve contradictions rather than inventing identities, countries,
amounts or dates. A portfolio overview needs no individual-debtor questionnaire.

Use the shared review procedure: show the service, details, amount/currency,
description and exact file list, including any files agreed for later upload.
Explain that they go to Delos for review and obtain approval of that completed
summary. Reuse approval for an unchanged summary; show and approve changes before
sending. Cancellation stops the send.

## Use one document transport

Prefer the matching with-documents MCP tool when the host supports its file input.
Follow the actual advertised shape: a host may expose attached files as absolute
local paths and bind them to remote descriptors itself. The remote MCP wire does
not read arbitrary paths. Do not fabricate IDs/URLs, pass Base64 or silently drop files.

If only readable selected local files are available, and this installed package
includes its uploader, follow [the local-file procedure](references/local-files.md).
The uploader is preserved from the published package. A URL-only MCP connection
does not install it. Do not call a real send merely to test it.

For unsupported or oversized selected files, explain the relevant direct limit:
10 files and a complete multipart request below 4 MiB. Offer submission of the
details first and later upload through the expected emailed secure link, supporting
up to 500 MB per file. Obtain explicit approval of any omitted/changed files before
using the no-document tool. This fallback does not apply to paused lien intake.

Read [optional portfolio financials](references/portfolio-financials.md) only when
the user supplies or asks to include those amounts. Do not require them.

## Send once and report the actual result

Check the required fields and selected-file input against that schema before the
call; do not use a real submission call as a payload validator.
After approval, use one matching transport once, with `confirmed: true` for an MCP
submission. Host confirmation controls also apply. Report the actual returned
public reference and status. Accepted means queued for review; it does not prove
completed processing or email delivery. Explain that next steps and the secure
upload link should follow after processing; never invent the link or reference.

After an uncertain send, preserve the receipt and stop. Do not automatically retry
or switch transports. The local uploader's documented, deliberate retry after a
proven pre-connection failure is a narrow exception, not an uncertain-send retry.
Use witold@delos.international with the actual reference for follow-up, and
hello@delos.international for technical help. There is no status-lookup tool.

For validation failures, report the exact field paths and returned messages. For
a host safety block, quote the reason provided and stop; distinguish it from a
Delos API error. Do not switch connections or transports, or change the approved
facts or files to get around the block. If no detailed reason is supplied, say so.

