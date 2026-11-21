# Import preparation templates

These header-only CSV templates use the API snapshot checked on 17 October 2026. They are offline preparation aids, not live-validated upload forms. Recheck the current descriptor and defaults before any write.

- Suppliers: name is required. Protected status/approval fields are deliberately excluded. An omitted status is not proof of a safe server default: establish the actual prospective default before creation, otherwise hold the create.
- Products: name is required. PM access is needed. Show intended/default status before approval.
- Controlled documents: doc_number and title are required. Document approval is unavailable here; a location URL does not upload a document.

Preserve codes, phone numbers, document numbers and revisions as text. Dates use YYYY-MM-DD; optional blanks are omitted on creates and preserved on updates. The templates are create-only by default; update workflows need explicit target matching and an approved field preview.

Read ../references/common-rules.md and the applicable resource policy. The helper adds import controls only when needed; never submit source_row_id, operation, target_id, owner_name or clear_fields as resource fields.

Example local use (paths relative to the bulk-import skill):

```text
python scripts/prepare_import.py --resource suppliers --template --output suppliers.csv
python scripts/prepare_import.py --resource suppliers --input suppliers.csv --output unsent-plan.json
```

For matching, --existing accepts an authorised snapshot envelope with resource, organisation_id, complete and data. complete is a caller assertion, not a server guarantee. All plans remain unsent and require live preflight/approval. Python is optional; use host file tools when unavailable.
