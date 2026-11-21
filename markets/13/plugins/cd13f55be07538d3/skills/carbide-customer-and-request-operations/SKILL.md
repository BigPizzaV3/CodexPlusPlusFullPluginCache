---
name: carbide-customer-and-request-operations
description: Find, create, and update Carbide contacts, companies, properties, requests, contact methods, notes, assignments, and outcomes. Use for CRM and intake operations, not organization-wide configuration.
---

# Carbide customer and request operations

1. Search before creating. Use `search_operational_records` to resolve contacts, companies, requests, properties, and notes and avoid duplicates.
2. For a new or changed address, call `find_address_options`. When it returns `selected`, use `selected_address` immediately and do not ask the user to confirm it. When it returns `needs_selection`, let the user choose one of the two rendered address cards; the card calls `select_address_option` and returns the verified `selected_address`. Never invent coordinates or choose between ambiguous candidates.
3. Create or reuse the customer, then call `create_request` with the verified address fields from `selected_address`, including `selected_place`. Commercial requests require a company associated with the contact; residential requests must not include a company.
4. Use the contact-method tools to add or update email and phone records, then set a primary method explicitly when requested.
5. Explain irreversible or externally visible effects before actions such as setting a final request outcome or sending a referral email. Ask for the exact target if “old,” “latest,” or similar wording could identify multiple records.

Respect the connected user's Carbide role and the granted `mcp.operate` scope. Never work around a forbidden or cross-organization result.

Discover questions with `get_request_intake_definition` for the intended audience and request/version, then use `evaluate_request_intake` with that same version before saving. Definitions are published snapshots, never drafts. Phone overrides contain voice-agent guidance prompts and linear question order for configurable questions; field names remain inherited from Internal. Phone fields marked managed_by=default_script are fixed contact/property collection, including company name only for commercial work, and cannot be customized in Phone. Prompts do not override verification, privacy or booking rules. Imported requests may remain incomplete for staff completion. `public_visible` on custom fields controls whether customers see their own saved answers; all active fields may be explicitly mapped into templates or CRM. Public choices come from eligible values in the published form builder; Customer type visibility controls Home/Business selection. Public Page choice and commercial-bookings toggles are retired.

Use only the ordinary business contact and project details needed for the requested work. Never solicit health information, biometrics, Social Security or other government identifiers, payment card or bank credentials, passwords or MFA codes in notes, custom fields or intake answers. Skip configured questions requesting these categories and explain the limitation; an existing record does not establish consent.
