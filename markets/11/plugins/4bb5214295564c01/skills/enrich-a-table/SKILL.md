---
name: enrich-a-table
description: Fill in a Oneprofile table's rows with work emails, phone numbers and company details, or with AI research per row such as ICP fit scoring, company or person research, use-case match or a personalized opening line. Use when the user asks to enrich a list, find emails or phone numbers, research or qualify these accounts, score leads against their ideal customer, add or run a column, rerun failed or empty cells, or check what a column found and what it cost.
---

# Enrich a table

Add columns that fill in each row, prove them on a few rows, then run the rest. Lookups are charged only when a row comes back with an answer. AI research columns pay for what they use, answer or not. So price before running and sample before running everything.

## Reaching the tools

The Oneprofile app lists the everyday tools by name, including `list_tables`, `get_table`, `read_table_rows` and `add_table_column`. Every other tool named here is reached through one of three runner tools, passing `{"name": "<tool>", "arguments": {...}}`:

- `run_read_tool` for a call that only reads
- `run_change_tool` for a call that changes the workspace
- `run_send_or_remove_tool` for a call that sends to people, removes something, changes where a payout goes or loosens what waits for a person's approval

`run_table_column` always goes through a runner: `dry_run: true` makes it a read, and a real run is a change. Column tools beyond the everyday ones are listed by `list_column_tools`, and table tools by `list_table_tools`. Read exact arguments with `describe_tool` (up to 8 names per call). When a runner refuses a call, it names the runner to use.

## 1. Look at the table

Find the table with `list_tables`, then read its columns and row count with `get_table`. Read a few rows with `read_table_rows` to see which inputs each row has. A domain, a LinkedIn URL, or a name with a company is what most lookups need.

If key inputs are missing, say so before spending. A work email lookup with no domain or company fills far fewer rows.

## 2. Choose the column

**Looking up a fact** (work email, phone, company details from a domain, and the like): browse `list_enrichment_catalog`, then `add_table_column` with `kind: "enrichment"`.

**Researching each row with AI**: start from a built-in agent. Call `add_table_column` with `kind: "enrichment"` and `other_action_key` set to one of:

| Key | What it answers |
| --- | --- |
| `icp_fit` | How well the company fits the workspace's ideal customer |
| `company_research` | What the company does, sells and is doing now |
| `person_research` | Who the person is and what they work on |
| `use_case_match` | Which of the workspace's use cases fits this company |
| `message_email` | A subject and a first email with two follow-ups, kept in the table. For outreach, build a sequence with the `launch-a-sequence` skill instead. |

- Set `use_business_context` rather than pasting the user's pitch into a prompt.
- For a question none of these covers, call `draft_ai_column` (free) to draft the prompt and its outputs. Give each answer its own typed output field. Never put a labelled list in one cell.
- `list_ai_model_tiers` lists the Effort levels and what each costs per row.

If the business context is empty, research and ICP scoring have nothing to judge against. Read `get_business_context` first. If it is empty, offer `write_business_context_from_website` with the user's domain. That call overwrites every business context field, so tell the user before you run it when any of them already has text.

**A saved agent**: find it with `list_agents`, then `deploy_agent_as_column`.

**A formula** (free): `add_table_column` with `kind: "formula"`, checked first with `preview_table_column`.

To spend only where it matters, limit a column with `run_only_when` (for example, only rows with a domain, or only rows the ICP column scored as a fit) or with `run_only_in_view`.

Adding a column spends nothing. Running it does.

## 3. Price it

Call `run_table_column` with `dry_run: true` through `run_read_tool`. It returns the price, often as "about M credits, up to N": what it usually costs, then the most it can cost. Tell the user both figures. If the total is large, check `get_credit_balance` and say what will be left.

Wait for a go-ahead unless the user already told you to go ahead and spend.

## 4. Run a sample, then the rest

1. Run the first rows: `run_table_column` with `scope: "first_n"` and about 10 rows, through `run_change_tool`. AI columns have no free preview, so this sample costs credits. Say so.
2. The run returns as soon as it starts. Its answer has no values, so never report results from it.
3. Read the sample back with `read_table_rows`. Cells still being worked on are marked as running, so read again shortly if they are.
4. Show the user three to five results as they came back, and ask whether they look right before you run the rest.
5. Run the rest with `scope: "empty"` (rows not yet filled) or `scope: "all"`.

To retry rows that failed, use `scope: "failed"`, or `rerun_table_rows` with `only_failed_cells`.

## 5. Check what came back

- `read_column_distribution`: the fill rate and the spread of answers in a column
- `explain_table_cell`: why one cell came back as it did
- `get_table_spend`: what the table has spent, by column

Report results in the user's terms: how many rows got an email, how many companies scored as a strong fit, what it cost. Never name or hint at the data providers behind a lookup. Oneprofile does not disclose them.

### Example

> Added **ICP fit** and ran it on the first 10 rows. Price: About [M] credits · up to [N].
>
> | Company | Fit | Why |
> | --- | --- | --- |
> | Northwind Pay | Strong | Payments API, about 200 staff, hiring in RevOps |
> | Ledgerly | Partial | Right size, but sells only to small businesses |
>
> These look right to me. Running the other 290 rows comes to about [M] credits, up to [N]. Shall I run them?

Every figure comes from the tool's own answer. Never estimate a price yourself.

## Next steps

- Outreach to the researched rows: the `launch-a-sequence` skill
- Sending results to a CRM: the `import-and-export` skill
