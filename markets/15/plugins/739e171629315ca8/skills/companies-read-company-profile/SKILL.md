---
name: companies-read-company-profile
description: Read one PropBot company profile the person is a member of.
---

Use this skill for that request.

Permission: propbot.companies.read.

1. Take one company id from companies_private_membership_list. Call companies_private_company_get for that company only. This is not a public company directory.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
