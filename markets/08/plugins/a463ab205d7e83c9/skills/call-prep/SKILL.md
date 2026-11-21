---
name: call-prep
description: Prepare a brief before a call or meeting with a customer or prospect, using Minz.ai CRM data (company, contacts, open deals, deal history, recent activities, related tasks). Use when the user asks to prepare for, get ready for, or get background on a call, meeting or visit with a named company or person.
---

# Call prep

Produce a brief the user can read in two minutes before talking to a customer. Everything comes from the Minz.ai connector, and this skill only reads. It returns only what the user's account can see. To change anything in Minz, use the `actions` skill.

## What to gather

Start from the name the user gives. It may be a company, a person or a deal.

- **Company:** `crm_accounts_search` with the company name. It matches the whole phrase against name or industry and returns at most 8 accounts, so if several come back, say which one you used or ask.
- **People:** `crm_contacts_search`, filtered by `crmAccountId` once you know the account. It returns name, job title, email and phone, at most 8 rows.
- **Deals:** `crm_deals_search` with the company name as `query`. Every word must match the title, account, contact or owner. It returns up to 20 deals with stage, value, currency and close date.
- **History:** `crm_deals_history` for the one or two deals that matter most, by `deal_id`. History is recent and bounded, not a full audit trail.
- **Recent contact:** `general_activities_search` by `dealId` or `contactId`, which gives type, title and date. Activity notes are never returned.
- **Open follow-ups:** `general_tasks_search` gives tasks with due date and status. Keep only those linked to these deals or contacts.

Leads only expose company and status, never a person's name or contact details, so use them only to say that an open lead exists.

## The brief

Lead with what the user most needs walking in: who they are meeting, where the relationship stands, and the open deal's stage, value and close date. Then list recent touchpoints, open follow-ups, and two or three questions or goals for the call that follow from the data.

Keep facts and suggestions apart. Say plainly when something is missing, for example "no activities logged in the last 90 days". If a search returned its maximum number of rows, say the list may be incomplete. Reply in the user's language.
