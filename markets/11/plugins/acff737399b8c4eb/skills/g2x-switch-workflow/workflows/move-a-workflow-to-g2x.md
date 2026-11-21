# Move a workflow into G2X

Goal: take a workflow the user runs in another product or a spreadsheet and do it in G2X, one task at a time, without claiming features match by name alone.

## Steps

1. Start with how they work today. Ask one practical question: "What do you use today, and which task would you like to do in G2X?" Use what they already told you: saved searches, pipeline stages, reports and routines. Do not scan installed apps, browser history or unrelated accounts.
2. Map the task, not the product name. "I use another tracker" does not say which features matter. Identify the inputs, filters, output, frequency, collaborators and destination for this one workflow. Do not guess a competitor's capabilities or claim equivalence from similar names.
3. Show the G2X path in the user's terms. For example: "You check VA cyber notices every Monday. In G2X we can rebuild those filters, test the matches, and save the view." Say whether the agent can finish it through the connection, help in the app, or only partially. A missing MCP action is not proof G2X lacks the feature.
4. Demonstrate with real criteria. Run the search (`g2x_search_opportunities` or `g2x_search_records`), rebuild the saved view with `g2x_save_search` only on request, or rebuild the board with `g2x_list_pipelines` and `g2x_create_pipeline`. Compare results against what the user relied on before: matching criteria, fields, usable output and repeatability.
5. Move records only when the workflow needs it. Start from an export the user is entitled to move. Leave the original unchanged. Match by stable identifiers: UEI, solicitation number, record id. Resolve ambiguous names with `g2x_search_companies` or `g2x_crm_find`. Record unmapped fields instead of dropping them. Rebuild saved searches from their meaning; filter keys differ across products. For bulk pipeline import, use the in-app importer; do not improvise thousands of individual writes. A manual pipeline entry is not a verified government notice.
6. Trial small, then verify. Before a trial, show the destination, mapping, creates, updates, duplicate handling and skipped fields. Use the user's existing authorization for that concrete scope. Verify created, updated, skipped and failed counts, then read back identities, stages, notes and links. Keep source and G2X ids per row so an interrupted move can reconcile. Never replay a finished batch blindly.

## What to tell the user

Finish with what they can now do in G2X, links to the resulting records, the mapping and any manual steps left. State any material gap plainly and give the best available way to finish the task. Do not promise a full replacement while an essential workflow is unverified, and never cancel the previous product for them.
