---
name: get-started
description: Run a home service shop (HVAC, plumbing or electrical) in EstimateKit from ChatGPT - the day's to-do list, customers and their equipment, quotes, jobs, invoices, and good-better-best draft quotes.
---

EstimateKit is quoting and job software for small home service shops: HVAC, plumbing and electrical. The connected account belongs to one shop; everything returned is that shop's own data, limited to what the signed-in person's role can see.

Good starting points:
- "What needs my attention today?" uses business_snapshot: overdue invoices, finished jobs not invoiced, approved quotes waiting for a date, quotes opened but unanswered, drafts, maintenance visits to book, today's jobs and jobs with no technician.
- Customer questions: search_customers, then get_customer for equipment, maintenance plan, quotes, jobs and invoices.
- Money: list_invoices (unpaid, overdue, paid this month).

Drafting a quote:
1. Find the customer with search_customers. Use new_customer on create_draft_estimate only when no match exists.
2. Prefer a saved template (list_templates). Otherwise build options from price book items (search_price_book) so the shop's own prices are used; custom lines need a price the user gave.
3. create_draft_estimate saves a draft and returns every line, the tax rates and totals, plus any items to check before sending.

Drafts are never sent from here. The shop reviews and sends them in EstimateKit, using the review link in the result. Nothing here can send messages, delete records, record payments or change settings.
