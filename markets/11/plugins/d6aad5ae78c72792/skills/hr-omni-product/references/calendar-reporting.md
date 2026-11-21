# Calendar Feeds and Reporting

Verified 2026-09-10.

## Calendar feeds

Calendar Feeds are read-only ICS subscription URLs, not direct calendar integrations.

Two feed families exist:
- Leave feeds: personal, department and company-wide approved leave.
- Employment feeds: birthdays and work anniversaries by department or company.

Users can subscribe through calendar applications such as Google Calendar, Apple Calendar or Microsoft Outlook. The URL is a bearer secret once shared and should be treated as sensitive.

Pending and hidden leave do not appear in leave feeds. Feeds cannot modify HR Omni.

## Reporting

Reporting is embedded inside relevant product areas rather than provided as a universal custom report builder.

- The underlying product must be enabled.
- Company and access boundaries apply to reports, lists, filters and exports.
- Data is generated from current records.
- Excel and CSV exports are supported where the relevant product reference says so.
- Native PDF report export is not supported.
- Do not claim scheduled reports, saved templates, arbitrary custom columns, API or BI integrations unless current official sources verify them.

## Form 76

The Bulgarian attendance report commonly called Form 76 requires Leave Management and can incorporate approved leave, public/non-working days, employee schedules and Worklogs hours when Worklogs is enabled.

It can support payroll preparation but does not process payroll or guarantee legal compliance.
