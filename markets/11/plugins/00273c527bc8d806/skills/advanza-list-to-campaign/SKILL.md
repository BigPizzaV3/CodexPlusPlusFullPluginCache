---
name: advanza-list-to-campaign
description: Turn a messy contact list the user pastes or uploads into clean Advanza contacts in a group, then an email to them. Use when they have a list of people to market to.
---

# From a messy list to an email

The user has a list - pasted text, a spreadsheet export, a sign-up sheet - and wants to reach the
people on it. Clean it, import it into a group, and prepare the email.

Explicit instructions from the user always take priority over this skill, with one exception: the
rule on restricted data in step 1 always applies. Answer in the user's language.

## 1. Clean the list

- **Leave out restricted data**, whatever the user asks: national ID or social security numbers, card
  or bank numbers, health information, passwords and other credentials. Say which columns were left
  out and why.
- Map the other columns to contact fields: first name, last name, email, phone, job title. Company
  names go in the import's `companies` section, each contact linked with `companyRef` (or `companyId`
  for a company that already exists). The workspace's own fields go under `custom`, by the keys from
  `custom-fields.list`.
- Fix the obvious: trim spaces, split full names, lower-case emails. Drop rows with no email: Advanza
  needs an email for each contact; list them as left out. Keep one row per email.
- Show a short summary: rows in, rows to import, rows left out and why. Do not show the whole list
  back unless asked.

## 2. Confirm the basis

Before importing people to market to, ask the user to confirm they have a lawful basis to send them
marketing (for example consent, or an existing customer relationship). If they cannot confirm it,
import without the email step and say why.

## 3. Import into a group

- Create a group for the list with `contact-groups.create`, named after its source and date.
- Import with `contacts.bulk-upsert`, at most 500 rows per call, with the group's id in each row's
  `groupIds`. Give every row an `externalSource` (the list's name) and `externalId` (its row number),
  so sending the same rows again never duplicates them.
- Contacts are matched on email only; never merge or update a contact because the name matches. Rows
  whose name matches an existing contact with another email come back as `possible_duplicate` and are
  skipped: show them, and send them again with `includeRows` only for the ones the user says are new
  people.
- If the result is `Accepted` with a `jobId`, follow it with `wait_for_jobs`. Report what was created,
  updated and skipped, with the reasons.

## 4. Prepare the email

- For one email to the list: let the user pick a template in `open_email_template_picker` unless they
  asked for a plain email, create it with `email-campaigns.create-draft` (no `campaignId`), set its
  recipients with `email-campaigns.set-audience` (`contactGroupIds` with the group), run
  `brand.check-text` on it, and show it with its link.
- Check `mailbox-senders.list` and say which mailbox it will go from, or how to connect one.
- Sending is the user's call: offer `email-campaigns.schedule` at the time they want; the person
  approves it on the card.

When the user wants more than one item (several emails, or posts too), use a campaign instead:
`campaigns.create`, `campaigns.set-audience` with the group, the drafts in the campaign, and
`campaigns.activate` when everything is ready.
