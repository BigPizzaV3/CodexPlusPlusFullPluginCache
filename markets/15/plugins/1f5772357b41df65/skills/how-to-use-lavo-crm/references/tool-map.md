# Lavo CRM MCP tool map

LavoLink server v2.6.5, 71 tools. Every tool sets readOnlyHint, openWorldHint, and destructiveHint explicitly.

Prefer typed list/get when the record type is known. Generics (`list_records`, `get_record`, `search`, `fetch`) remain supported.

## Read (readOnly true, openWorld false, destructive false)

`fetch`, `get_account_plan`, `get_company_branding`, `get_customer`, `get_customer_summary`, `get_dashboard_snapshot`, `get_invoice`, `get_job`, `get_property`, `get_quote`, `get_quote_funnel`, `get_record`, `get_request`, `get_revenue_summary`, `get_schedule`, `get_service_pricing`, `list_campaigns`, `list_customers`, `list_invoices`, `list_jobs`, `list_messages`, `list_my_accounts`, `list_payments`, `list_photos`, `list_properties`, `list_quotes`, `list_records`, `list_requests`, `list_staff`, `list_tags`, `list_visits`, `search`

## Write inside Lavo CRM, additive (readOnly false, openWorld false, destructive false)

`add_customer_note`, `add_invoice_line_item`, `add_line_item`, `add_line_item_to_quote`, `add_tag_to_customer`, `bulk_tag_customers`, `convert_quote_to_job`, `create_calendar_item`, `create_campaign_draft`, `create_invoice_from_job`, `create_property`, `create_quote_draft`, `create_request`

## Write inside Lavo CRM, overwrites or removes (readOnly false, openWorld false, destructive true)

`apply_discount_to_quote`, `bulk_untag_customers`, `cancel_visit`, `complete_calendar_item`, `delete_calendar_item`, `record_offline_payment`, `remove_quote_line_item`, `remove_tag_from_customer`, `update_calendar_item`, `update_customer`, `update_customer_meta`, `update_quote_draft`, `update_quote_line_item`, `update_visit`

## Additive, may start account automations (readOnly false, openWorld true, destructive false)

`convert_request_to_customer`, `create_customer`, `schedule_visit`

## Overwrites, reaches the customer or an outside service (readOnly false, openWorld true, destructive true)

`complete_visit`, `quote_house_washing_price`, `reschedule_visit`, `send_customer_message`, `send_invoice`, `send_quote`, `send_to_customer`, `send_visit_confirmation`, `update_job_status`

## Send rules

- `send_customer_message`, `send_invoice`, `send_quote`, `send_to_customer`, and `send_visit_confirmation` need a preview and the user's explicit confirmation before anything is sent.
- `create_customer` and `convert_request_to_customer` may trigger the account's welcome message. `schedule_visit` and `reschedule_visit` may trigger visit reminders. `complete_visit` and `update_job_status` (completed) may trigger review request, thank-you, and follow-up messages. Each only happens if that automation is on in the account's settings.
- `schedule_visit` sends no confirmation itself; it returns a preview and confirm_token for `send_visit_confirmation`.
- `delete_calendar_item` is two-phase: preview, then confirm_token.

## Quote services and terms

- `get_service_pricing` returns `services`, `custom_services`, and active `quote_terms_templates`.
- `create_quote_draft`: `line_items[]` (not `items`) with required `name`, `unit_price`; optional `service_id` (UUID), `description`, `quantity`. Optional `terms_template_id` (UUID) and `terms_type` (`general` | `commercial`).
- `update_quote_draft`: optional `terms_template_id`, `terms_type`; notes-only or expiry-only edits leave terms unchanged.
- `add_line_item`, `add_line_item_to_quote`, `add_invoice_line_item`, `update_quote_line_item`: optional `service_id` (UUID). Quote lines may use `services` or `custom_services` ids; invoice lines must use `services` ids.
- Ids must belong to the same account. Name-only lines link only on a unique exact name match (case and spacing ignored).

## Notes

- Responses omit lat/lng, portal tokens, signatures, auto-charge card ids, staff emails/phones, and inline image bytes (unless `list_photos` is asked for image data).
- `quote_house_washing_price` may call an external property-data lookup (RentCast).
- Marketing campaigns cannot be delivered from MCP. `create_campaign_draft` only drafts.
- Card and ACH payments stay in the Lavo CRM app. `record_offline_payment` is cash or check only.
