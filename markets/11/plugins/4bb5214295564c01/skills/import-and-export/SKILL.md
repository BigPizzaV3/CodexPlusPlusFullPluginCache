---
name: import-and-export
description: Move lists in and out of Oneprofile. Bring rows pasted into the chat, a CSV or spreadsheet, or contacts and companies from a connected tool such as a CRM (HubSpot, Salesforce, Pipedrive, Attio and others) into a Oneprofile table, and send a table's rows back to a CRM or out as CSV. Use when the user says import, upload, paste this list, bring in my contacts or accounts, sync from their CRM, push or export to their CRM, or download a table.
---

# Import and export

Get an existing list into a Oneprofile table so it can be researched and reached, and send the results back to where the team works. Importing costs no credits. Exporting to a CRM writes into the user's CRM, so preview it and confirm before running.

## Reaching the tools

`create_table` and `read_table_rows` are listed by name. The import and export tools below are listed by `list_table_sync_tools`, and connection tools by `list_integration_tools`. Reach any of them through one of three runner tools, passing `{"name": "<tool>", "arguments": {...}}`:

- `run_read_tool` for a call that only reads
- `run_change_tool` for a call that changes the workspace
- `run_send_or_remove_tool` for a call that sends to people, removes something, changes where a payout goes or loosens what waits for a person's approval

Read exact arguments with `describe_tool` (up to 8 names per call). When a runner refuses a call, it names the runner to use.

## Bring in rows from the chat or a file

`create_table` takes `name` and `csv_text`, up to **200 rows and 25 columns**. The first line holds the column names, and every column comes in as text.

1. Get the rows as CSV. If the user pasted a list, use it. If they attached a spreadsheet or CSV, read it yourself and turn the rows you need into CSV text.
2. Tidy without changing meaning: trim spaces, drop fully empty rows, keep the user's own column names, and put quotes around any value that contains a comma.
3. Keep the columns that later steps need: name, job title, company, company domain or website, email, LinkedIn URL. If the file has more than 25 columns, keep those and tell the user what you left out.
4. Call `create_table` with a name in the user's words.
5. Check it with `get_table` and a few rows from `read_table_rows`, then say how many rows and columns landed.

**More than 200 rows**: `create_table` refuses them. Point the user to **Import from file** on the [Tables page](https://app.getoneprofile.ai/tables). It takes CSV and `.xlsx` up to 50 MB, with as many rows as your plan holds, and types each column. Offer to load the first 200 rows now if they want to try the workflow first. Don't split a list across several tables unless they ask.

`import_file_as_table` and `read_file` only work with files attached inside Oneprofile's own assistant chat. Don't use them here.

## Bring in records from a connected tool

1. `list_connected_sources`: the tools this workspace has connected, and the objects each can import, such as contacts or companies.
2. If the tool the user means isn't connected, look it up with `browse_integration_directory`. `connect_app_by_oauth` returns a sign-in link: give it to the user to open, then continue once they say they have connected.
3. `preview_connected_records`: a few real rows from that object. Show them, because every tool means something different by "contact".
4. `create_table_from_connected_tool`, through `run_change_tool`. It costs no credits.
   - Match rows on the tool's own record ID. It never changes, so later refreshes update the right row. Matching on email adds a new row whenever someone edits the email in the tool.
   - Bring in everything, or set a row limit when the user only wants a sample.
   - Fields not given a column stay on each row and can become columns later with `promote_source_field_to_column`.
5. Keep the table current with `refresh_table_from_source` or `set_table_refresh_schedule`. Either can remove rows that left the source, so the runner depends on the call.

## Send rows to a CRM

The export column alone sends nothing. Running it is what writes into the CRM.

1. `list_export_destinations`: the connected tools and objects a table can push to.
2. `add_export_column` with `match_on` and `field_mappings`. Say which object it writes, which fields, and whether it creates new records, updates matching ones, or both.
3. `preview_export_column`: a dry run that writes nothing. Show the user what would be created and what would be updated.
4. Only after the user agrees, run that column with `run_table_column` through `run_change_tool`. Start with `scope: "first_n"` on a few rows, check them, then run the rest.
5. `get_export_column_summary`: report how many records were created, updated or failed.

To bring CRM fields into a table without importing the whole object, use `add_lookup_column` (from `list_table_sync_tools`).

## Download a table

`export_table_to_csv` returns the table as CSV text. Give it to the user as a file, or as a short table when it's small.

## Next steps

- Research or fill in the imported rows: the `enrich-a-table` skill
- Write to them: the `launch-a-sequence` skill
