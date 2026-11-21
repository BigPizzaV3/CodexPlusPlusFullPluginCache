---
name: vat-check
description: Check EU and Northern Ireland business VAT numbers live in VIES and download dated XLSX and CSV validation logs.
---

Use `check_vat_numbers` for a vat number check, vies vat validation or eu vat number lookup. Pass `numbers`, a list of 1 to 100 VAT identifiers with country prefixes. An optional `default_country` applies to numbers without a prefix. Use `EL` for Greece; a `GR` prefix is changed to `EL`. Optional `requester_vat` is the user's own business VAT identifier for VIES consultation numbers.

Report counts and each non-valid row with its reason. Share both log downloads, which expire in about an hour, and the source retrieval time. A structural match is not proof of validity. Only VIES supplies validity. An unavailable answer means retry later, not invalid. Duplicates keep their input rows and reuse the same consultation.

Use `check_vies_availability` when the user needs VIES or member-state service status, especially after unavailable answers. Status is cached for 120 seconds; VAT answers are not cached.

Coverage is the 27 EU member states and Northern Ireland (XI). No national checksum test is applied. Some states do not publish names or addresses. A VIES answer reflects the consultation time. Do not use for tax advice or to decide whether reverse charge applies.
