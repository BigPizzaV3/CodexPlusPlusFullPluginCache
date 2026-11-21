---
name: prepare-remittance
description: Prepare a sanitized vendor payment-summary PDF and reply draft for a verified original invoice thread using existing Grid invoice, PO and payment evidence. Drafting does not authorize sending or prove settlement.
---

# Prepare vendor remittance

Use existing project, vendor, invoice/document, PO and payment IDs. Inspect current schemas and read canonical records, including active applications and remaining balance via `grid.get_payable` and `grid.get_payment`. Use [record-and-reconcile-payment](../record-and-reconcile-payment/SKILL.md) when bookkeeping is requested. Never initiate a payment. A payment summary describes the evidence actually available; do not turn a user-reported sent payment into bank-confirmed sent, vendor receipt or settled AP.

## Verify thread and recipients

Discover the connected Grid vendor-thread read/link capability and inspect its actual callable schema. Vendor email relationships are a separate API dependency being developed in PR #6511; skill installation, a PR or a newer server version does not establish deployment or callable access. Do not invent a tool name, thread association or API result. When available, read the relationship and actual original invoice messages; verify project, vendor, invoice revision, sender/reply-to, thread identity and intended recipients. Do not choose the newest unrelated vendor email or assume any company contact is the invoice recipient. Resolve ambiguous people using available recipient-resolution tools/history before addressing a reply.

If the relationship is missing, link only through a supported reviewed workflow within the user's authorization; do not use notes or arbitrary metadata as a substitute. If reads/linking or authorized message access are unavailable, checkpoint `original_thread_unverified` and state exactly which capability is missing. Continue a standalone payment-summary PDF and unaddressed draft when enough verified financial facts exist. Do not claim it is saved to or addressed in the original thread. Resume after capability and relationship readback.

## Generate and inspect the summary

Use an available PDF authoring workflow; this plugin does not add a PDF renderer or remittance endpoint. If none is available, return reviewable summary text and mark PDF generation pending, not completed. Read [the sanitized field contract](references/summary-fields.md) before generating. Preserve unknowns explicitly; a missing PO number is not permission to issue one or invent its number.

Create a new document from the allowlisted facts, never a bank statement screenshot or a redacted copy with hidden source data. Render and inspect every page and extracted text before attaching. Verify invoice/PO identity, amount, currency, payment date, actual method, safe reference, evidence-qualified status and remaining balance against fresh reads. Exclude account balances, full account/routing/card details, credentials, unrelated transactions, internal notes and bank data. Avoid source PDFs or statements as attachments merely because they supported the research. The payment summary is not a bank-generated confirmation.

## Draft and checkpoint

Draft a concise reply referring to the original invoice and internal PO, stating payment amount, currency, method, date, safe reference and remaining balance as verified. Attribute user-reported information and leave missing facts visibly unresolved. Do not claim vendor receipt. Show final recipients, subject/thread, body and exact sanitized PDF for review. If an authorized draft-save capability exists, save and read back its draft/thread/attachment IDs; otherwise deliver the draft locally and mark host draft persistence unavailable.

Generic vendor templates do not prove payment-specific merge fields or triggers. Discover the supported template catalog and resolved values before using one; if unavailable or incomplete, draft literal verified text without inventing fields or enabling triggers.

Require explicit user approval before every email send, covering the final recipients, thread, body and attachment. Import/payment approval or an old draft approval is not send approval. On resumed work, request fresh send approval; never persist permission as a checkpoint flag. If the user forbids sends, stop at the draft. If a send is separately authorized, use only the verified supported send capability and read back its sent message ID. After an uncertain send response, inspect sent/draft state before any retry; do not send again while the result is unknown. Changed content or recipients require renewed approval. Return draft/PDF IDs or paths, verified thread ID, actual send outcome and remaining blockers using the [checkpoint contract](../process-vendor-invoice/references/checkpoints.md).
