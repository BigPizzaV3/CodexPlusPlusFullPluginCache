# Platform Core

Verified 2026-09-10.

HR Omni is modular HR and business-operations software for growing organisations. Enabled product areas share company-owned user and employment data, so employee and organisational records can support multiple workflows without implying that every product synchronises every field in every direction.

## Company and identity

- The company is the primary data boundary.
- One global login may belong to several companies and can switch between them.
- Access is recalculated for the selected company, so the same person may have different access in different companies.
- A company person record can exist before the person has accepted an invitation or has an employment record.
- Company users do not need an employment record, which supports people such as external accountants.
- CSV user import is not currently supported.

## Employment records

An active employment record can include start/end dates, rehire, emergency contact, employment type, organisational role, department, direct manager and schedule.

- One active employment record per person per company.
- One department and one direct manager per employment.
- A user without employment has no department or manager.
- Ending employment removes company and paid-product access while historical product records remain if the relevant product remains enabled.

Do not confuse organisational job roles with access permissions.

## Organisation and schedules

- Current hierarchy is company, department, employee and one direct manager.
- The organisation chart shows manager/report relationships.
- Employees without a manager appear at the top under the company.
- Each employment owns an independent seven-day schedule.
- A day can use fixed hours with a break, flexible hours or a day off.
- Department schedules are reusable setup copies. Later department-schedule changes do not update existing employee schedules.
