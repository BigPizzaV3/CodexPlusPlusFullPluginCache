---
name: lueira-customer-management
description: Find, create or update customer records in the connected Lueira business, resolving duplicates and ambiguous identities before writing.
---

Use Lueira's current customer-tool schemas and the tenant connection already selected by the user. Permissions come from that connection, not from a tenant ID supplied in conversation.

For an existing customer, search using the identifying information the user supplied (`q` matches name, email, phone, legal name and VAT number), then fetch the matching record. Names may not be unique: use returned email, phone or other relevant details to distinguish candidates. `get_customer` returns only names, email, phone, type and created date; address, tax data, birth date and comments need `get_customer_pii` (`pii:read`). Ask about an unresolved identity before making a change.

Before creating a customer, check for an existing matching email or other strong identifier: `create_customer` does not de-duplicate. If the match is uncertain, explain it rather than silently creating a duplicate or modifying a different person. Use the user's supplied values; do not fabricate contact details, fiscal data or birth dates. For more than a handful of customers, run `import_customers_dry_run` first (it matches by email, VAT number, or phone plus name), then `import_customers`.

For updates, inspect the current record and current tool schema. Send only the requested changes: leave a field out to keep it. An empty string is ignored, and `update_customer` cannot clear a saved value. Creation validates country, language, VAT and birth date but update does not, so check those values yourself. These tools never read or set newsletter or other marketing consent, so a requested email correction does not change consent.

For deletion, identify the exact customer and follow the host's applicable confirmation flow. Do not delete records as a way to resolve a search or permission error. Deletion is a soft delete and the tool does not check orders, so do not expect it to refuse. Report only the effect confirmed by the tool; deletion does not establish that related bookings, invoices or legal records have also been removed. On Lueira's admin MCP, deletion only creates a pending action: say it is waiting for the member's confirmation.

After a successful write, report the returned customer ID and the actual changes. If the response is uncertain or times out, check the record before retrying a creation. Do not declare success on an error or repeat a write blindly. If the account lacks the required customer scope, explain the permission gap without changing the connection's permissions yourself.
