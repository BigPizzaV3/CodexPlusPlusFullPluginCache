---
name: ethica-compliance
description: Use Ethica to look up what workplace training, policies and notices employers in US states, cities and Canadian provinces must provide, and to read the signed-in organization's compliance records in Ethica (who is overdue, one person's record, a requirement's completion, record downloads). Read-only.
---

# Ethica

Ethica keeps employers' required workplace training, policy sign-offs and employee notices, with a dated record for each person. Every Ethica tool is read-only.

## When to use it
- The user asks what an employer in a US state, city or Canadian province must provide (training, notices, policies): use `find_requirements`. It needs no sign-in.
- The user asks about their own team's records in Ethica: overall progress (`get_compliance_overview`), finding assignments by person, role, status or due date (`search_assignments`), one person's record (`get_employee_record`), one requirement's completion (`get_requirement_status`), their list of requirements (`list_requirements`), or a link to download records (`get_records_link`). These ask the user to sign in to Ethica once.

## Behavior
- Ethica can't assign training, send reminders, add employees or change records. If asked, say so and give the Ethica link from the answer so the user can do it there.
- Report only what Ethica returns. Never say someone completed training unless the record shows a completion date.
- Requirement lookups are general information, not legal advice. Keep the official sources Ethica gives with each requirement and suggest confirming them.
- Use names, roles, requirement titles and dates as Ethica gives them. Ethica doesn't return email addresses.
