---
name: get-started
description: Check the connected ToDev account and get it ready for tasks, projects, clients and invoices.
---

Help the user start with ToDev.

1. Call `whoami` and tell the user which ToDev account is connected and which plan it is on.
2. If `hasCompany` is false, explain that clients and invoices belong to a company. Offer to set it up
   with `set_up_company`, asking for the company name first. Tasks and projects work without one.
3. Call `get_today` and summarise what is due today and what is overdue, in a few lines.
4. Suggest two or three things they can ask next, such as adding tasks to a project, moving tasks to
   another day, or recording an invoice or expense.

Never delete anything: ToDev's tools can't, and deleting stays in the ToDev app.
