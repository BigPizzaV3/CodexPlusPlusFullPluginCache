---
name: print-and-mail
description: Print a PDF and send a physical letter or paper copies by ordinary post, worldwide, to the user or other recipients. Use when the user wants a printout, hard copy or paper copy, a letter mailed, help printing without their own printer, help mailing a document they have a picture of, or a price for printing and posting a document.
---

Keep the normal flow in chat. Where available, proactively use relevant addresses and preferences already in your context, and present them for review in the order summary. Ask only for missing details. If warranted, distinguish paid postal printing from using a local printer or creating a printable file. Decline using this skill for emailing.

Use `draft_printout` to prepare an order or answer a price enquiry. If the user has not supplied a document or an address yet, ask for them. If the document is not a PDF, proactively convert it to PDF. If the user only has pictures of pages, crop, rotate and assemble them into a single PDF. Visually inspect any PDF you create before submitting it. If the user has not specified the colour option, inspect the document to choose black-and-white or colour.

Preview is optional: use `show_print_preview` only on request or for an issue that warrants visual inspection by the user.

Present the draft in the concise table format below, replacing the illustrative values with the selected document's name and the tool's actual results:

| Detail | Selected |
|---|---|
| Document | file-name.pdf · 2 pages |
| Settings | US Letter · Colour · Single-sided |
| Layout | Pages scaled to 89.8% |
| Printouts | 2 copies → Name, address |
| | 1 copy → Name, address |
| Sheets | 8 sheets, including address sheets |
| Price | **$Z.ZZ** |

Use one Printouts row per delivery, leaving its label blank after the first. Take counts, layout details and prices from the tool output; Sheets is the sum of its per-delivery sheet counts, and Price is its combined total with the applicable currency symbol. Omit Layout unless there is a meaningful change, and round scaling percentages to one decimal place. If paper size, layout, print origin or postal service differs between deliveries, place those details alongside the relevant delivery between copies and the arrow. Show a return address only when the user supplied one, and omit it when it matches the delivery address. Include a delivery date estimate if the tool returns one. Keep draft/quote IDs, hashes and terms-version identifiers out of the summary.

Include the order summary and the checkout link together in the same reply, with the exact combined amount in the link text (for example, "Checkout $Z.ZZ"). The checkout page links to the service terms, so omit a separate terms link from the chat summary. The user confirms the order by completing the checkout; opening the link alone does not charge, print or send anything. Do not ask for a separate chat confirmation and never request card details in chat.

Before payment, a change to the document, addresses, copies, print settings or contact email warrants a new draft. Use `cancel_order` to cancel the previous draft at the user's request or when replacing it. Confirm that cancellation succeeded before showing only the new draft's payment link. If cancellation is not possible, explain the result and do not create a replacement as a retry.

After payment, use `cancel_order` only at the user's request; a paid order can be cancelled on a best-effort basis until processing starts.

Use `get_status` if the user asks about their order's status, receipt or cancellation. Report the returned stage and receipt code; "posted" means handed to the postal service, not delivered. If the user asks for an expected delivery date and no date was returned, search online for average delivery times for the route and present the results as your estimate.

Use `report_issue` once for each distinct tool error, blocked tool call or upload, and tell the user whether it was recorded. Keep reports free of private material: do not include document content, postal addresses, email addresses, payment details, credentials or file URLs. If submission status is uncertain, call `get_status` and explain what remains unknown. Do not create another order as a retry.
