---
name: get-started
description: Fill an empty LeagueBoots CRM and learn the everyday moves. Use when the user first connects LeagueBoots, when their CRM has no companies yet, or when they paste or upload a list of companies, contacts or deals to import.
---

# Get started with LeagueBoots

LeagueBoots is the user's CRM. Call `describe_crm` first: it returns who the user is, their organization, and every kind of record with its fields and allowed values.

## Fill an empty CRM

If `aggregate_crm_records` on `company` counts nothing, offer to import what the user already has: a pasted list, a spreadsheet, or a CSV export from another CRM.

For LinkedIn connections, send the user to the console's [Import page](https://console.leagueboots.com/import) instead: it reads LinkedIn's Connections.csv export as it is.

1. Read the list and map its columns to the fields `describe_crm` returns. Ask about any column you can't place; leave it out rather than guessing.
2. Show the user how the first few rows will be saved, and wait for them to agree.
3. Add `companies` first, up to 50 records per `create_crm_records` call, each with its domain when the list has one. Then add `contacts` with the `company_id` values it returned, then `deals`.
4. A company or contact that's already there is refused with its ID: use `update_crm_records` instead if the list has newer details.
5. Say how many records were added, and how many were skipped and why.

## Everyday moves

- Log a call, meeting, email or note: `create_crm_records` with `activities`, each with its `type`, `occurred_at`, the company and deal it was about, and `contact_ids` for who was there.
- Add a deal: `create_crm_records` with `deals`, each with its `company_id`, `name`, `stage`, `amount_usd`, `close_date`, and its `contacts` with their roles.
- Move a stage or a close date: `update_crm_records` with only the fields that change. Earlier versions are kept, so `list_crm_changes` can show what moved.
- Pipeline totals: use `aggregate_crm_records`, never add up `search_crm_records` results yourself.
- The same person or company twice, such as a LinkedIn import and someone added from email: read both, confirm with the user, then `merge_crm_records` into the one with more history. It can't be undone.

Nothing in LeagueBoots can be deleted from here. If the user asks to delete records, explain that their organization's owner can ask LeagueBoots support to delete its data.
