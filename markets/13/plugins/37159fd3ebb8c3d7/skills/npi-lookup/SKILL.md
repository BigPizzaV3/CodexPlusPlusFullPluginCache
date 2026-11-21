---
name: npi-lookup
description: Look up public NPI Registry records in a provider roster or search by name and state, with credentialing XLSX and CSV downloads.
---
Use `verify_npi_numbers` for npi lookup, verify npi number, bulk npi lookup, check npi number, or npi taxonomy code lookup. Give 1–40 provider objects with `npi` and optional `expected_name`, `expected_state`, `expected_taxonomy`. Example: {"providers":[{"npi":"1245319599","expected_state":"VA","expected_taxonomy":"207Q00000X"}]}.

Use `search_npi_providers` for npi registry search, npi search, or provider npi lookup by name. Give 1–10 searches with state and last_name or organization_name; optionally first_name, city, postal_code, taxonomy_description, entity_type. Example: {"searches":[{"last_name":"Smith","first_name":"John","state":"MA"}]}.

Report the counts, per-item errors, mismatches, source retrieval time and download links. Links expire in about one hour. Invalid numbers are checked locally. Results can be cached: roster records up to 24 hours, searches up to 6 hours. Search returns up to 10 matches; narrow a broad query. Do not enter patient information or use these enumeration records as proof of licensure, board certification, sanctions or payer enrolment. Deactivated NPIs may appear as Not found.
