# Capability coverage

Checked 2026-11-04 against Landit commit `9368236d`, `app/services/mcp/server_factory.rb`, its tool implementations/entities, and the connected host's 16 exposed tool names. A successful list_templates read is separate from fresh ChatGPT OAuth and end-to-end write testing. Live schemas govern calls.

| Tool | Inputs / purpose | Effects and completion |
| --- | --- | --- |
| list_templates | Optional page; accessible template summaries and variables | Read; follow next_page until null for a complete list |
| get_template | slug; current HTML, invitation, revision, manifests, preview_url | Read; template preview browsing permitted under shared policy |
| get_template_authoring_context | Optional owned template_slug; account facts, Liquid paths, assets, preview samples | Read; contains private context; no prompt execution |
| create_template | source_url, user_prompt; ask Landit's AI to build a template | Starts new hosted work; may publish accepted output automatically; save creation id |
| get_template_creation | id; creation status, messages, can_continue, result | Read; preparing/working, awaiting_input, ready, failed, cancelled |
| send_template_creation_message | id, content; answer/correct unfinished creation | Write; same captured context and creation; only when can_continue |
| create_template_html | name, content, optional og_preview_content | Immediately publishes new private template; non-idempotent |
| update_template_html | slug, content, expected_revision_number, optional og_preview_content | Immediately publishes owned template revision; stale revision rejected |
| get_template_generation | run_id; individual generation attempt | Read; succeeded/failed/cancel; not the creation id |
| enrich_prospects | template_slug, enrichment_name, prospects | Creates new Enrichment and PageRuns; consumes credits; optional HubSpot writeback |
| get_enrichment | enrichment_uuid; batch and associated runs | Read; inspect every run; batch settlement may lag 30 minutes |
| get_page_run | run_id; one PageRun and component outcomes | Read; distinguish overall success and crm_writeback_state |
| search_pages | Optional page, date bounds, slug, template_slug, enrichment_name, source, status, paired integration/prospect_id | Read; combined exact filters; fixed 25-item pages; not general name/LinkedIn search |
| get_page_analytics | slug; stored tracking snapshots and context | Read; no named-visitor or confirmed-reading inference; never open Page URLs |
| get_image_upload_instructions | Empty arguments; separate asset API workflow | Instructions only; no file upload or key issuance |
| update_asset_sharing | slug, shared boolean; owned asset | Changes workspace-library visibility; returns canonical asset fields |

## Contract details

For Page creation each prospect needs linkedin_url. Put template values directly on the prospect alongside it; do not wrap them in an invented template_variables object. Optional crm_provider is hubspot and must be paired with crm_contact_id. Send the complete requested list in one batch within actual host/server request limits. The current schema has no maxItems cap; do not carry forward the obsolete 20-prospect limit. Every submission creates a new batch; no in-place correction or expansion is exposed.

HTML creation/update requests share the server's 8 MiB encoded-request limit. Normally include a matching personalized 1200 × 630 invitation in og_preview_content. Creation omission/null means absent. Update omission preserves the invitation, null clears it, and nonblank HTML replaces it. Never replace omitted values with null automatically.

The current server offers tools only, with no MCP resources, prompt catalog, embedded UI, account profile tool, arbitrary Page content editor, CRM contact manager, or upload-bytes tool. Skills supply the conversational workflows. No extra backend is bundled.

OAuth is declared with mcp:connect and CIMD preference. Current Landit source advertises CIMD plus DCR compatibility; OpenAI's documented CIMD preference retains DCR fallback. Fresh ChatGPT client selection, callback handling, refresh, and reconnection remain runtime test requirements.
