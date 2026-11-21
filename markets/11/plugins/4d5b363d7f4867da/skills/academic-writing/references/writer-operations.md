# Writer operation notes

- Workspace: the same `workspace_id` selected from `list_reference_managers` is also used for Writer documents; required for organization-billed connections with multiple workspaces.
- `generate_document`: full research-and-writing workflow; 200–20,000 words, free plans capped at 3,000; `reference_ids` max 50 and only for sources `library` or `both`; returns `status: generating` and link rather than final content. Credit-billed. A folder restriction must be translated into explicit IDs; do not claim "only this folder" if the selected folder exceeds the supported reference ID limit or the selection isn't enforceable.
- `create_document` and `update_document`: source-citation markdown `[Label](cite:<paper-id>)` or `[Label](cite:doi:<DOI>)`; use only real IDs or verified DOI strings. Save operations may remove unmatched citations and return those targets in `citations.unmatched`.
- `get_document`: includes `sections`, `sources`, `generating`, `truncated`, `unknown_sources`. Read sections when truncated, and do not rewrite links into ordinary bracket-text citations.
- `update_document` modes: `replace_section` requires exact heading in `section`; `append` adds content; `replace` swaps all content. Previous version saved; pinned comments may be unanchored.
- `export_document`: DOCX or PDF, URL expires 24 hours later; disclose exact `link_expires_at` returned. Exports automatically format citations.
- `check_plagiarism`: separate opt-in request; <=200 words per call, monthly word quota, may not capture all sources; similarity is not a legal or institutional plagiarism determination.
