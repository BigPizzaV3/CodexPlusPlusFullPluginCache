# Box Search

Box permissions are the access boundary. Scope searches for relevance and performance when the user identifies a folder or project area, but broaden autonomously when the task requires it.

## Choose a search tool

- Use `search_folders_by_name` to resolve a named folder, workspace, client, project, or department. It returns basic fields; when matches are ambiguous, call `get_folder_details` for the candidates before distinguishing them by path, owner, or date.
- Use `search_files_keyword` for filename, extension, keyword, or content searches. Apply `ancestor_folder_id` when the user supplied a folder scope, and add extension or date filters when useful.
- Use `search_files_metadata` when the criteria map to structured metadata fields.

## Metadata search

1. Use `list_metadata_templates` to resolve the template scope and key.
2. Use `get_metadata_template_schema` to obtain its field keys.
3. Call `search_files_metadata` with the resulting `from` value and fields.
4. Pass user-provided values through `query_params` rather than embedding them in the query.

### Error handling

- If search returns no results, broaden one dimension at a time: remove date filters, remove file extension filters, search by partial folder name, or try keyword search instead of metadata search.
- If search returns too many results, narrow with folder scope, file extension, date range, metadata filters, or requested fields.
- If metadata search fails, verify the template scope, template key, field keys, and `from` value using `list_metadata_templates` and `get_metadata_template_schema`.
- If results are ambiguous, do not assume the intended file. Present the top candidates with stable identifiers such as name, type, path, modified date, and owner.