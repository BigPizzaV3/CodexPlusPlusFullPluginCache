---
name: browse-services
description: Use when the user asks what checks are available, wants to compare prices or coverage, or you need to select a compatible service before ordering.
---

# Browsing and selecting services

The user does not need an exact service name or ID. Resolve their intended check from the request and conversation, then use `list_services` to retrieve the catalogue.

## Retrieving the catalogue

Call `list_services` with `page=0` (0-based) and `size=200` by default. Check the returned total and follow pagination when needed before claiming the catalogue or price comparison is complete. A single page is sufficient when it contains every available service. There is no search parameter.

Use the returned `id`, `title`, `price`, `time`, `limit`, `allowedIdentifiers`, and `sample` fields. `sample` is an illustrative example of output fields.

## Selecting a service

- Match the user's requested outcome and selection criteria to a compatible service.
- Compare compatibility, coverage, and current price using descriptions and samples.
- Use `allowedIdentifiers` to check whether a service accepts IMEI, serial number, or MEID. Determine brand coverage from the returned service title, description, and sample where explicit. Identifier support alone does not establish brand coverage.
- Missing or empty metadata means "unknown", not "universal". Do not claim planned metadata is available before the live response includes it.
- `sample` shows possible output fields; it is not a fresh device result.

## Delegated vs ambiguous requests

- "Cheapest suitable Apple service" → choose the cheapest compatible service and explain its coverage.
- "Check this phone" → ask a short clarifying question about which check is wanted.
- Ask only when the request or compatibility remains genuinely unresolved.

## Notes

- Model, model number, warranty, GSMA Blocklist, SIM-lock, carrier, FMI, and MDM coverage vary by service and identifier. Never assume a service supports every field.
- Do not add paid services to fill missing fields without the user's authorization.
