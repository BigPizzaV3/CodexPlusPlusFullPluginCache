# Library organization plan

Before a bulk action, provide a compact table:

| Reference / DOI | Current folders | Proposed folder(s) | Action: add vs move | Evidence for classification | Needs review? |
|---|---|---|---|---|---|

- **Add** (`add_references_to_folder`) retains all existing folder memberships.
- **Move** (`move_references`) removes *all* existing folder memberships and assigns exactly the specified destination folders; use only with clear intent.
- `Unorganised` is the default state for papers in no other folder; its folder cannot be renamed. Papers can belong to several folders without duplication.
- For unresolved titles, duplicate DOI records or low-confidence topic assignments, request review or put them in a clearly labeled pending group if the user approved such a folder.
- Show a post-action count from the service result, not from planned operations. Explain partial success and permission errors.
