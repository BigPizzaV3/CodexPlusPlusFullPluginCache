    ---
    name: growth-performance-brief
    description: Combine 33CRM marketing delivery with CRM lead-funnel and sales outcomes in one growth brief. Use when the user wants marketing plus lead sources plus funnel conversion side by side, without assuming direct attribution between Meta and CRM outcomes.
    ---

    Use this skill for a combined growth view.

Workflow:
1. Resolve the requested period.
2. Call `get_marketing_report` for stored Meta delivery/spend by account.
3. Call `sales_summary` for CRM lead volume, source mix, qualification, attendance, won/lost outcomes, and rates.
4. Call `get_sales_report` when the user also wants deal/booked-value context.
5. Use `get_ad_insights` only when daily marketing detail is needed.
6. Use `list_leads` only when the user asks to inspect the underlying CRM leads.

Output:
- Growth summary
- Marketing delivery and spend
- CRM lead-source mix
- Lead-funnel outcomes
- Deal context when requested
- Side-by-side observations
- Attribution/data caveats

Rules:
- Present Meta provider metrics and CRM outcomes side by side unless a direct relationship is explicitly present in returned data.
- Do not claim that a campaign caused CRM leads, deals, revenue, or attendance merely because dates overlap.
- Provider leads are not the same as CRM leads.
- Booked value is not recognized revenue.
- Stored Meta figures may lag the provider.
- Reply in the user's language.
- Read-only only.
