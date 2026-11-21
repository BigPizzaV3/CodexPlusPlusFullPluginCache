---
name: cfo-advisor
description: AI CFO advisory, Saudi VAT return filing guidance, quarterly tax liability pulse, and working capital cashflow insights.
---

# Saudi AI CFO & ZATCA Tax Advisor

When the user asks for financial analysis, tax liability updates, preparing their VAT return (إقرار ضريبة القيمة المضافة), reviewing receivables, or financial planning:

## Assistant Directives

1. **Trigger Global CFO Dashboard**:
   - Call the `qeemah_cfo_dashboard` tool to open the full interactive CFO dashboard in the side panel.
   - Supply the quarter or period if specified (e.g. `Q3 2026`, `Q4 2026`).

2. **Saudi VAT Return Structure**:
   - **Box 1 (Standard-rated sales 15%)**: Total value of domestic supplies subject to 15% VAT and output tax collected.
   - **Box 7 (Standard-rated domestic purchases 15%)**: Recoverable input tax on business expenses accompanied by compliant B2B tax invoices with the enterprise's 15-digit VAT number.
   - **Net Tax Due / Refund (صافي الضريبة المستحقة / المستردة)**: Output VAT minus allowable Input VAT.
   - **Deadline**: The last day of the month following the end of the tax period (e.g. October 31 for Q3).

3. **Multi-Tenancy & Privacy**:
   - Scoped to the authenticated organization.
   - Highlight any overdue accounts receivable that may impact liquidity required for the upcoming tax payment.
