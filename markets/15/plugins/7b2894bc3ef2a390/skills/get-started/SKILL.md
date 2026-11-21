---
name: get-started
description: How to look up a company's Struct construction data (projects, site reports, sales, purchasing, accounts and HR) with the Struct tools, and how to present the answers.
---

# Using Struct

Struct is the company's construction management system. The Struct tools read live data exactly as the signed-in person may see it in Struct.

## Rules

- Look up only. Nothing can be created, changed, approved or deleted from ChatGPT. If the person asks for that, say it is done in Struct itself.
- All money is in AED (UAE dirham). Write amounts as AED 12,450.00, never $, USD or dollars.
- When a tool answers `permission_denied`, say the person has no access to that in Struct. Never guess the data.
- PDFs cannot be shown here. Tell the person to open the document in Struct.

## Finding things

- Projects: by number (for example P12) or by name. For the newest projects, use `get_projects_list`.
- Quotes: Q and the number (for example Q24), or the client, project or enquiry name.
- Invoices: by invoice number. Money a client owes the company is `get_overdue_invoices_ar`; money the company owes its suppliers is `get_overdue_invoices_ap`. If it is not clear which one the person means, ask.
- Site: daily progress reports (DPRs), snags, work inspections, samples and general requests, per project.

## Answers

- Keep answers short and plain. Use a small table when there are several rows.
- Name a project by its number and name, for example "P12 Warehouse fit-out".
