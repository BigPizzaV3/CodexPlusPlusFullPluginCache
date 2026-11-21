    ---
    name: booking-attendance-review
    description: Analyze 33CRM booking volume, attendance, no-shows, cancellations, status mix, branches, owners, and upcoming booking records. Use for appointment operations, attendance reviews, no-show analysis, and branch booking workload.
    ---

    Use this skill for booking and attendance operations.

Workflow:
1. Resolve the requested date range.
2. Call `get_booking_report` for total bookings, attended count/share, status breakdown, and branch breakdown.
3. Call `list_bookings` when the user requests the actual booking records, upcoming appointments, a status filter, branch, sales rep, or lead.
4. Call `get_booking` only for one identified booking.
5. Call `list_branches` or `list_sales_reps` when IDs/names are needed for filters.

Output:
- Booking volume
- Attendance and status mix
- Branch distribution
- Upcoming / filtered booking list when requested
- Operational attention items
- Data caveats

Rules:
- `attended_share_of_all_bookings` uses all bookings in the period as the denominator; it is not necessarily a completed-appointment show-up rate.
- Do not infer treatment type, diagnosis, clinical status, or patient outcome.
- Appointment notes and clinical fields are not available and must not be invented.
- Reply in the user's language.
- Read-only only.
