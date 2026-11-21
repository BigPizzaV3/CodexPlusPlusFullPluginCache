# Example — business description to approved CRM structure

Illustrative workflow, not evidence of an executed test. Use the tools and schemas exposed in the current session.

**User:** Build a new Deals board for a software business with three salespeople and around 80 opportunities. Use Sales Ops; show the full plan before creating anything.

1. Run `get_user_context`, resolve the accessible workspace and search for an existing same-named board.
2. Propose Discovery, Proposal, Negotiation, Won and Lost groups; Stage, Owner, Deal Value, Probability, Expected Close, Last Touch and Source columns. Show workspace, visibility and setup-document content in the approval batch. Seed items are a separate opt-in.
3. Wait for approval of that exact batch.
4. Use `create_board` with its current schema and group names in `creationPrompt`. Read the board back before adding missing groups or columns.
5. Before configured columns, obtain `get_column_type_info` schemas. `create_column` uses numeric `boardId`, `columnType`, `columnTitle` and optional `columnSettings` as a JSON string. Build type-specific configuration from the returned schema, not legacy `labels`, `defaults` or `settings` arguments.
6. Read the completed board back; disclose missing groups/columns and actual done-label settings.
7. Search/read possible setup-document duplicates. Create only the approved summary, with the visible `monday-crm-skill-id: workspace-builder` marker and generated-by footer, and read it back.
8. Report actual counts and the board/doc links. If creation was partial, list the failures.

No seed items are included here. Amount fields are never written, including on new items. Last-touch dates require an actual fictional interaction confirmed by the user.
