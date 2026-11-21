---
name: create-and-send-for-signing
description: End-to-end workflow for creating a sajn document, getting its content in place, adding signing parties, and sending it for e-signature. Use when the user wants to create, prepare, or send a document, contract, or agreement for signing.
---

# Create and send a document for signing

sajn documents move draft → (optional approval) → sent → signed. This skill takes a request from "I want X signed" to a sent document.

## Workflow

1. **Pick the starting point.**
   - An existing template ("our standard NDA"): `findTemplates`, then `createDocument` with `templateId`.
   - A file the user has (PDF/Office): `createDocument` blank, then the file handoff in step 2.
   - From scratch: `createDocument` blank, then compose with `addTextField` / `addFormField` / `addTable` / `addProductTable`.
2. **File handoff.** You cannot receive file bytes and must never ask the user to paste a document's contents. Give the user the document link `createDocument` returns, ask them to drag the file onto it, and continue once they confirm.
3. **Missing facts become form fields.** Names, dates, amounts, and terms the user has not given you become FORM subfields via `addFormField` — never placeholders like "[NAME]" in text. Fill sender-side values with `listFieldValues` → `setFieldValues`. Values assigned to a party are filled by that party at signing — read them, never set them.
4. **Never write signature blocks.** No "Signature", "Ort och datum", or signature lines in text content — sajn renders signing automatically.
5. **Parties.** `addParty` per signer. Before setting `requiredSignature` or `twoStepVerification` with `updateParty`, call `listSigningMethods` — eID availability varies per account; never assume.
6. **Preflight.** `checkDocumentReadiness`; fix blockers, surface warnings to the user.
7. **Send.** Confirm recipients and expiration with the user, then `sendDocument`. If the user lacks permission to send without approval, use `submitForApproval` with the approver emails instead.

## Validation

Success = `sendDocument` (or `submitForApproval`) succeeds and the document shows PENDING (or PENDING_APPROVAL). Always end by showing the document link.
