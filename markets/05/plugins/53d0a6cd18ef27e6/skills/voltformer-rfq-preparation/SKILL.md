---
name: voltformer-rfq-preparation
description: Prepare a complete Voltformer electrical-equipment quotation request from member profiles, projects, catalog products, and specification PDFs. Use for RFQ drafting, validation, attachment preparation, or explicitly confirmed submission.
---

# Voltformer RFQ preparation

Prepare an accurate quotation request while keeping drafting separate from irreversible submission.

## Workflow

1. Require a connected member before accessing private data. Read available company profiles and projects only when they help fulfill the request.
2. Resolve every requested item to a known Voltformer catalog product and retrieve its details. Do not submit free-text products as if they were catalog matches.
3. Ask for missing operational details, quantity, delivery destination, requested timing, site conditions, standards, and whether a technical-specification PDF exists. Omit genuinely unknown optional fields.
4. For a PDF available in chat, use `uploadSpecificationInline` within its size limit. For larger files, use `createSpecificationUploadUrl`, have the file uploaded, then call `finalizeSpecificationUpload`.
5. Show a final summary containing customer/profile, project, products, quantities, delivery information, specification attachment, assumptions, and unresolved details.
6. Ask for explicit confirmation to submit that exact summary. Call `submitRfqQuoteRequest` only after confirmation, then return the durable request reference and optionally verify it with `listRfqs`.

## Invariants

- Never treat discussion, drafting, file upload, or a prior confirmation for different content as permission to submit.
- An RFQ requests a quotation; it is not a purchase order, payment, contract, price guarantee, or inventory reservation.
- Use business tax identifiers only when necessary for the quotation; never ask for personal government IDs, credentials, payment data, or authentication codes.
- Do not expose another member's profiles, projects, files, or RFQs.

