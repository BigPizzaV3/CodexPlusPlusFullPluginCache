---
name: check-addresses
description: Find stored Grid addresses or validate a supplied postal address with Google, review ambiguous candidates and corrections, and distinguish verification from saving or ownership.
---

# Check an address

1. For a request to find an existing Grid address, call `grid.search_addresses` with supplied terms and optional entity scope. Explain that a stored match is not a new Google validation. Respect `has_more` and do not reassign an address's owner.
2. For an explicit validation or lookup request, call `grid.resolve_address` with the supplied address, venue or area and optional context. A line that starts with a street number goes to Google address validation; a name, neighborhood or city goes to Google Places. Pass `mode: "postal"` or `"place"` only to override that choice. Preserve apartment, suite, stage, or unit information. Explain that external validation sends the address to Google; if the user disallows external processing, limit the workflow to stored records.
3. For a street address, present the returned accept, confirm, or fix verdict and supporting reasons. For confirm, show the proposed correction and obtain the user's choice. For fix, request corrected input before validating again. Neither acceptance nor a candidate proves ownership, deliverability guarantees, or authorization to overwrite a Grid record.
4. If alternatives are needed, call `grid.resolve_address` with `mode: "place"`. These Google Places results (status `choose`) are explicitly not validated. Show the options, let the user select, then resolve the chosen street address with `mode: "postal"` while preserving supplied unit information.
5. Treat unavailable configuration, rate limits, and provider failures as service failures, never as evidence the address is invalid. Stop repeated failed calls and explain the retry or missing-input path.

Return the selected address, its actual verification status, and unresolved differences. These lookup tools update operational rate-limit counters but do not save entity/address records. If saving is requested, use the appropriate company's, contact's, or location import's own preview workflow so any signed verification evidence is bound to the exact fields being saved.

For contacts, `grid.preview_create_contact` accepts `contact.addresses`. Existing-contact edits use `grid.get_contact_notes` to read authorized saved address IDs, then `grid.preview_contact_update` with `changes.addresses` operations (`add`, `update`, `remove`). Add uses a fresh stable UUID; update/remove use the exact owned row ID. Confirm the complete preview before apply, then read current data again. Copy permitted fields to a new owned row; never reassign another entity's address. Contact edits retain provider provenance without claiming durable postal validation.

Use `label: "Home City"` for the person's explicitly supplied home geography only. City/state/country and region-only rows require no street or ZIP. Keep area precision and Google coordinate expiry; area centers are browsing pins, never routing destinations. Preserve full structured addresses when supplied. Omission preserves billing, agency, ordering, and unrelated channels. Text edits clear stale coordinates and invalidate the applicability of earlier confirmation; confirmation history is retained. Never infer Home City from an agency office or production location.
