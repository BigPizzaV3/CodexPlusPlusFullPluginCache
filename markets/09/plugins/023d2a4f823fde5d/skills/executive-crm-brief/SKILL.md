    ---
    name: executive-crm-brief
    description: Create a management-level 33CRM brief across sales, pipeline, bookings, marketing, and conversation operations. Use when an owner, CEO, or company admin asks for an executive overview, business pulse, management summary, or cross-functional CRM performance brief.
    ---

    Use this skill for a cross-functional executive view of the authenticated company.

Core workflow:
1. Resolve the requested period. If the user gives no period, use the most recent 30 days for period reports and clearly label `pipeline_summary` as a current snapshot.
2. Call `sales_summary` for lead-cohort performance.
3. Call `get_sales_report` for deal count, booked value, amount paid to date, stage, and owner breakdowns.
4. Call `pipeline_summary` for the current pipeline snapshot.
5. Call `get_booking_report` for booking volume and attendance.
6. Call `get_marketing_report` for stored Meta delivery/spend by ad account.
7. Call `get_conversation_report` for conversation volume by channel/status.
8. Use pagination or narrower filters if a tool says results are incomplete.

Output:
- Executive summary
- Key commercial metrics
- Pipeline position
- Booking/attendance position
- Marketing delivery
- Conversation workload
- Items needing management attention
- Data caveats

Rules:
- Reply in the user's language.
- Keep lead metrics and deal metrics separate; they are different populations.
- `booked_value` is agreed deal value, not recognized revenue.
- `amount_paid_to_date` is the current collected amount on deals in the selected deal cohort, not cash received during the period.
- Meta provider leads are not CRM leads and must not be treated as directly attributed conversions.
- Stored Meta data may be stale; do not imply a live provider refresh.
- Conversation tools return operational metadata and counters, not message bodies.
- Do not infer clinical, medical, treatment, or patient outcomes.
- Do not invent benchmarks, targets, trends, or causes that are not supported by the returned data.
- This workflow is read-only. Never imply that CRM records were changed.
