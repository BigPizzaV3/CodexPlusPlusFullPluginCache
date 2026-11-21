---
name: zatca-auditor
description: Audit, inspect, and verify Saudi ZATCA e-invoices (XML and PDF) for Phase 2 compliance, VAT calculations, and QR codes.
---

# ZATCA E-Invoice Auditor

When the user asks to inspect, audit, or check a Saudi Arabian e-invoice, use the Qeemah extension tools.

## Key Capabilities

1. **File Inspector (`qeemah.zatca_viewer`)**:
   - Opens when the user clicks or views a `.xml` or `.pdf` e-invoice.
   - Decodes Base64 TLV QR codes into human-readable data (Seller, VAT, Timestamp, Invoice Total, VAT Amount, Hash, Signature, ECDSA Public Key).
   - Verifies UBL 2.1 elements according to KSA Phase 2 rules.

2. **Validation Rules to Check**:
   - **Seller VAT Number**: Must be 15 digits, starting with 3 and ending with 3 (`^3\\d{13}3$`).
   - **Invoice Type Code**:
     - `388`: Tax Invoice
     - `381`: Credit Note
     - `383`: Debit Note
   - **Invoice Subtype**:
     - `0100000`: Standard Tax Invoice (B2B) - requires buyer VAT number and address.
     - `0200000`: Simplified Tax Invoice (B2C) - requires TLV QR code.
   - **Currency**: Must be `SAR` for domestic transactions.
   - **Standard VAT Rate**: Must be `15%` unless zero-rated (`Z`), exempt (`E`), or out-of-scope (`O`).
   - **Math Integrity**:
     - Tax Exclusive Amount = Sum of Line Extension Amounts - Allowances + Charges.
     - Tax Inclusive Amount = Tax Exclusive Amount + Tax Amount.
     - Payable Amount = Tax Inclusive Amount - Prepaid Amount.
     - QR Code Total and VAT must exactly match the Invoice Payable Amount and Tax Amount.

3. **Guidance for the Assistant**:
   - Provide responses in the user's preferred language (Arabic or English).
   - If the user asks about tax deductibility, clarify that only Standard Invoices (B2B) addressed to the taxable person's VAT registration number can be used for input VAT deduction.
