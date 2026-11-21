# Common import rules

Keep an immutable reference to source file/sheet/original row and its SHA-256 fingerprint when supported. Use UTF-8; preserve leading zeros and spelling in identifiers. Reject duplicate headers and malformed rows. Unknown meaningful columns need an explicit mapping/defer decision, never silent loss.

Default operation=create. Updates require an identified target and exact approved patch. source_row_id, operation, target_id, owner_name and clear_fields are import controls, NOT domain fields. Resolve names with authorised lookups; do not invent UUIDs or use personnel IDs as users.

Blank on create omits an optional field so the actual server applies its verified default. Blank on update preserves the field. Explicit clear uses clear_fields as a JSON list, only for nullable writable fields. Literal NULL remains text, not an instruction to clear. Do not both set and clear a field.

Dates are unambiguous YYYY-MM-DD. Validate booleans using declared forms, not Python/string truthiness. Required fields must be nonblank. Map enums exactly. Record unresolved dates/owners and reject unsupported fields. Quoting, multiline cells, Unicode and CSV escaping must be preserved. Protect spreadsheet previews from formula execution without changing approved underlying values.

Classify rows as create, update, unchanged, invalid, ambiguous, duplicate or deferred. A helper's create/update classification is only an unsent candidate; it is not permission, successful matching or completion of live preflight.

Target snapshots used by the helper must be envelopes with resource, organisation_id, complete and data. complete means the caller attests all relevant pages were retrieved; the helper cannot verify access. If incomplete/unavailable, leave deduplication outstanding. Do not submit envelope keys to resources.

The descriptor/profile, protected decision rules and target context all need checking before execution. Do not fabricate defaults from nullable/optional schema types. Resource schemas may expose fields that the MCP policy prohibits; preserve the stricter boundary and report inconsistency.
