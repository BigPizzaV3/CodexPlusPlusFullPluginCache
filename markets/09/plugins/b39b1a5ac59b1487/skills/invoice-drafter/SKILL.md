---
name: invoice-drafter
description: Draft, quote, build, and calculate Saudi ZATCA e-invoices (B2B and B2C) interactively with real-time VAT math.
---

# Saudi ZATCA Invoice Drafter & Quote Builder

When the user asks to create an invoice, draft a quote, charge a client in Saudi Arabia, or calculate VAT on services/goods:

## Instructions for Assistant

1. **Trigger Interactive Drafter**:
   - Call the `qeemah_create_invoice_draft` tool.
   - Pass any details mentioned by the user:
     - `customerName`: Name of the buyer or client.
     - `customerVat`: 15-digit VAT number (starts and ends with 3) if provided or known.
     - `isB2B`: Set to `true` for business-to-business transactions (requires full customer details), or `false` for simplified B2C consumer invoices.
     - `items`: Array of items with `name`, `quantity`, `unitPrice` (in SAR), and `taxRate` (default 15).
     - `notes`: Any payment terms (e.g., payment within 14 days, bank transfer).

2. **Advise on Saudi Tax Rules**:
   - Remind the user that for domestic B2B transactions above SAR 1,000, buyer VAT registration and full address details are required under ZATCA Phase 2.
   - For B2C retail/simplified invoices, buyer VAT is optional, but a cryptographic TLV QR code is mandatory.
   - Supply date (KSA-5) must not be in the future, and invoices should be issued within 15 days of the following month after the supply took place.

3. **Interactive Side Panel**:
   - Inform the user that the invoice draft is loaded in the Qeemah side panel, where they can adjust quantities, add lines, generate compliant UBL 2.1 XML, or sync back to the thread.
