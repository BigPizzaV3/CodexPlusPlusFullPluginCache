# Enterprise integration scenario checklist

Employee lifecycle: SuccessFactors to directory/Entra ID, payroll and downstream provisioning. Map HR event timing, approval, joiner/mover/leaver, disabled creation vs activation, termination timing, duplicate prevention, PII restrictions, region/data residency, writeback and audit.

Procurement and trading: Ariba contracts, requisitions, purchase orders, acknowledgments and supplier master, partner EDI flows, mapping, sequence and state consistency, acknowledgment/audit, error reprocessing.

Salesforce–S/4HANA: customer/material data sync, pricing/ATP/simulation, order creation, credit checks, event/response correlation, duplicate prevention and status updates. Validate actual API service entities and business permissions.

Banking, finance and treasury: payment approval, encryption, signatures, SFTP/bank APIs, file-level acknowledgment, reference IDs, idempotency, reconciliation, cutoffs, audit controls and separation of duties. Never assume a retry is safe.

Intelligent document processing: invoice/PO, HR onboarding documentation, bank compliance files. Design ingestion → classification/OCR/extraction (where service exists) → validation → policy/approval → ERP API → archival/audit; label AI extraction confidence and sensitive-data risk.

For every scenario: requirements, source/target contracts, run frequency, delta handling, authentication, schema mapping, idempotency, alerts, test matrix, scaling and recovery plan.
