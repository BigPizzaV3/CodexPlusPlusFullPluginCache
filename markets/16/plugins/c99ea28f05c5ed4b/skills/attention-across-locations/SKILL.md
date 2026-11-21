---
name: attention-across-locations
description: Use when someone asks what needs attention in their business right now, what is overdue or expiring, or what is coming up across their Locations in Binto.
---

# What needs attention across Locations

Answer from Binto records only. Everything here is read-only.

1. If you do not know which Organization the person means, call `organizations_list`. With one Organization, use it. With several, ask which one, then pass its `id` as `organizationId` on every call.
2. Call `overview_attention` for what needs attention now: expired documents, documents expiring within 30 days, dates waiting to be confirmed and draft inspections. For overdue tasks, call `task_find` as well.
3. If they ask about a period ahead ("this month", "next 60 days"), call `upcoming_find` with `days`.
4. If they name one Location by name, code or address, call `location_resolve` first and use the Location it returns to narrow what you report.

When you answer:

- Group by Location, most urgent first. Say the date and how late or how soon.
- Cite each record by its title from `sources`, and include its link from `links` when there is one. Links open in Binto and need the person to be signed in.
- Report only what the results contain. Do not guess a date, a count or a name, and do not say how many records exist beyond what was returned.
- If a tool says something is not available, say so plainly. The person may not have access to that module or Location.
