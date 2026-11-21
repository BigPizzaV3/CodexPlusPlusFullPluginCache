---
name: get-started
description: Use Mitratech Legal (powered by ARIES) to find, summarize and update the signed-in user's TeamConnect matters, contacts, tasks, appointments and invoices. Runs with the user's own TeamConnect permissions; confirm every change with the user first.
---

# Using Mitratech Legal with TeamConnect

Mitratech Legal connects ChatGPT to the user's own TeamConnect instance. It can find and read records, and,
when the user asks, create, update, close or delete them. Every request runs with the user's TeamConnect
permissions.

## Before the first question

The user signs in with their TeamConnect account when they connect Mitratech Legal. If a tool reports that the
user isn't signed in or the sign-in expired, ask them to reconnect Mitratech Legal. Use `teamconnect_auth_status`
to check who is signed in.

## Finding records

1. Matters are TeamConnect projects. Their type codes differ between instances, so call
   `list_project_types` before reading or searching matters. Use `list_object_types` for the standard
   types (contacts, tasks, appointments, accounts, users).
2. To find a record by name, number or another field, use `search_records` (or `search_custom_field`
   for a custom field). To use a list the user already has in TeamConnect, use `list_search_views`
   and pass the view's key to `list_records`, but only when the user names that list. "My matters" (or
   "my tasks") means every record the user can access, so list or search the records themselves; a
   saved view such as "My Matters" can be empty.
3. To find matters by phase or stage, list or search the matters and read each one's
   `currentPhase.displayString` (for example "Intake" or "Open"). Phase codes don't always match the
   names, so compare the display names, not the codes.
4. Read one record with `get_record`. Read its tasks, appointments, involved parties or related records
   with `get_record_subresource`. Read custom field values with `get_record_categories` or
   `get_custom_fields`.
5. For invoices and spend, use `get_invoice_line_items` or `invoice_review_bundle`. Spend totals you
   calculate are sums of the invoices you read; say which invoices and period they cover.
6. Ask for small pages first and say when results were truncated.

## Making changes

1. Change something only when the user asks for it. If more than one record matches, ask which one.
2. Before any write, tell the user exactly what will change: the record, the fields and the new values.
   Preview where the tool supports it: `update_record` and `update_record_category` with `preview=true`,
   `change_project_phase` with `dry_run=true`, and `create_matter_involved`, which previews by default.
3. Make the change only after the user confirms. `create_record` has no preview, so confirm the full set
   of fields first.
4. Before creating a matter or contact, check for duplicates with `prepare_matter_intake` or
   `find_contact_identity`, and tell the user what you found.
5. Delete a record only when the user asks to delete that specific record and confirms it by name.
6. After a change, read the record again and report what TeamConnect saved.

## What to tell the user

- Answer only from what the tools returned. Name the matter or record you used. Don't infer legal
  deadlines from dates; report the dates TeamConnect has recorded.
- If TeamConnect says the user doesn't have access to a record, or rejects a change, say so. Don't look
  for another way to reach it.
- Don't send emails or messages; Mitratech Legal can't. Offer a summary the user can send themselves.
