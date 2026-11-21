---
name: plan-an-integration
description: Turn an integration someone describes into a CRM Connector plan with a prefilled setup link. Use it when a person wants two business systems connected, for example "when a deal is won in HubSpot, make a draft invoice in QuickBooks Online" or "keep my Xero contacts in Pipedrive".
---

# Set up a sync with CRM Connector

This belongs to part 2 of the plugin, **Integrations between two systems**: an integration set up once that then keeps two systems in sync by itself. Work inside one system (reading, changing or automating its records) is part 1, AI Agents: `get_ai_agent_options` explains it.

CRM Connector keeps business systems in sync: contacts, invoices, quotes, deals, jobs and appointments travel between systems such as QuickBooks Online, Xero, Jobber, HubSpot, Pipedrive and Salesforce. This skill turns a wish into a plan; the CRM Connector tools hold the facts.

## Steps

1. **Know the two systems and what should travel.** If either is unclear, ask one short question, for example "Which system do the deals start in, and where should the invoices end up?" Never guess a system.
2. **Check what is possible.** Call `get_integration_options` with both systems. Use what it returns: the record types, the direction (one way, or both ways for the record types it marks), the moments a record can wait for (such as when paid or when accepted) and the filters.
3. **Make the plan.** Call `plan_integration` with:
   - the source system and the target system
   - the record type keys `get_integration_options` returned
   - the trigger, when the person asked for one
   - `direction` `both_ways` when changes made in either system should reach the other; leave it out for one way
   When they change their mind, call `plan_integration` again: that saves a new concept with its own link and leaves the earlier one as it is, so share the newest link.
4. **Share the link and what happens next.**
   - Share the setup link from the plan as a link.
   - Say the plan is saved as a concept: nothing syncs yet, and they find it again under Integrations in CRM Connector.
   - They open it, sign in or create a CRM Connector account, connect both systems and review every choice before anything syncs.
   - Pass on the plan's notes, for example that contacts travel along, that a sync from date is needed, or which record types stay one way when both ways was asked.

## Spreadsheets (Google Sheets, an Excel or CSV file)

- A spreadsheet only sends: records go from the sheet into the other system and nothing is written back.
- Only our template is ever used, so nothing is matched. Call `get_integration_options` with the spreadsheet and the other system, or `get_connection_guide` with `other_system`: its `sheet` part names the template's tabs and columns and holds its download link.
- Then `plan_integration`. Its link asks only to connect: Google and the other system for Google Sheets, only the other system for an Excel or CSV file. The integration is saved at once, with our template made in their Google Drive or waiting to be uploaded. On the page it lands on they paste their rows (or upload the filled file), test it (nothing is written) and switch it on.
- With a sheet of their own, offer to copy its rows into the template here first: ask them to share it, and hand back an .xlsx with the template's tabs and exact headers, one row per record. They paste those rows into the Google sheet, or upload the file. A sheet that is not our template is refused.
- For a spreadsheet, `get_integration_fields` names each field by the column of our template.

## When something is not offered

- Say so plainly and share the request an integration link the tool gives.
- When a tool says the other direction is possible, offer that instead.

## Rules

- Only describe what the tools return. Never promise a record type, a direction, a trigger or a system the tools did not confirm.
- No tool creates the integration itself: the person creates it in CRM Connector from the setup link, after reviewing every choice. No tool deletes an integration or a connection.
- Do not discuss prices, plans, trials or discounts. If a tool says the account has no active plan, pass on its sentence and link exactly as given.
- Never ask for passwords, API keys or tokens. Systems are connected inside the CRM Connector app, never in the conversation.

## Test before committing

Offer a test whenever somebody is deciding, without waiting to be asked:

- **An integration:** Test with sample records, on the last step of the setup, shows what a first sync would do with their own records. It writes nothing and needs no plan.
- **An AI agent:** once the setup is saved, it can be tried here in the chat before it is switched on: it reads up to 100 records of that system with every read tool (search, filters, counting, reports, lists) and makes up to 25 changes the person agrees to; sending messages, recording payments and voiding wait until it is switched on. Answers say how much of the test is left. A first automation can be written and approved before it is switched on, and starts with it. When the person wants it to work for real, share the Switch it on link the tool answer gives: one step there switches on every agent that waits.
