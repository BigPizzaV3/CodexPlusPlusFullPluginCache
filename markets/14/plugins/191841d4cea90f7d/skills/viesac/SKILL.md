---
name: viesac
description: Use VIESAC to validate VAT or EORI identifiers, retrieve VAT rates, create requested compliance audits, and search the connected organization's audit history.
---

Use the connected VIESAC MCP tools. If authentication is required, direct the user to Connect and the secure OAuth sign-in flow. Never ask for passwords, API keys or tokens in chat. Connections apply to the organization selected at consent. Read-only access cannot create audits; request audit permission through the host's authorization flow when needed.

When multiple VIESAC plugins or accounts are connected, retain the user's exact selected connection for every tool call and subsequent step. Never combine balances, audit history or writes from different connections. If the requested account is ambiguous or unavailable, ask the user to select it rather than falling back to another account. Before a credit-consuming operation in a multi-account context, verify the selected connection and its quota, then use that same connection for creation and retrieval.

For a quick VAT or EORI validity check, use validate_vat or validate_eori. These do not create an audit. Quick VAT validation does not provide company details. For a clearly requested formal audit or certificate, use create_audit. A VAT or EORI audit uses one existing account credit; a combined vat_eori audit uses two. If the user has not clearly requested a credit-consuming audit, explain the choice first. Check quota before bulk operations and describe expected credit use. Enable monitoring only when the user requests it and specifies the cadence; it creates additional audits on its schedule.

Use get_audit for a returned reference, list_audits for filtered history, and search_partners for counterparties in the connected organization's own historical audits. These tools cannot search every company in a country. Use get_vat_rates for a country and list_vat_rates for comparisons. Preserve source and verification dates when returned. Coverage varies by registry; refer to https://viesac.eu/countries rather than assuming all countries support every check or rate lookup.

Preserve identifiers and resolve ambiguous country prefixes with the user. Do not guess missing digits. Report registry status faithfully: unavailable, pending, unknown or a format error must not be relabeled as registry-confirmed INVALID. Never invent a company name, address, consultation number, audit reference or certificate. A consultation number exists only when the source returns it. SHA-256 evidence hashes are not digital signatures.

For global checks, inspect validation_scope, registry_checked and registration_valid when returned. A valid format or checksum alone does not confirm tax registration. If registry_checked is false or registration_valid is null, explain the narrower check instead of claiming confirmed registration, even if the top-level status says valid.

For an audit, report its actual status, reference and available certificate link. A plan-gated audit page is not a downloadable PDF. Do not claim statutory acceptance, legal advice or government endorsement. Distinguish registry facts from user-supplied invoice references and comments. VIESAC cannot file tax returns, make payments, purchase credits, delete audits or provide global company/owner contact searches. Explain unsupported requests without invoking unrelated tools.
