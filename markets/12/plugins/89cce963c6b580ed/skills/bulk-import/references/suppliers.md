# Supplier import policy

Create/update the register only. Do not create evaluations, CARs, acknowledgements or document issues as side effects.

The dated schema requires name. Ordinary candidate fields are code, scope_of_supply, category, is_critical, certification, certification_expiry, contact_name, contact_email, contact_phone, next_review_date, owner_id and notes. Check the current descriptor. Criticality must be supplied explicitly, not inferred; blank does not mean false. Certificates are source claims until checked, not verified/uploaded evidence. Past expiry warns but does not change status.

Never submit status, approval_date or approval_basis in this workflow even if a REST schema exposes them. The current MCP rules reserve supplier status decisions for people. Source values such as Approved or Suspended must appear as deferred decisions in the preview. Default is hold that row. If the user approves prospective creation with deferred source decisions, the helper's --defer-protected option may prepare the ordinary fields, but still cannot verify the live initial state.

Before ANY supplier create establish from an actual supported server contract/read-only check that omission of protected fields produces the agreed safe prospective state. Optional status does NOT prove its default. If the safe default cannot be established, keep creates deferred and report the server-contract gap. Do not test a production create merely to discover the default. Existing supplier updates preserve status.

Match target_id only after authorised retrieval in the organisation. Otherwise compare supplier code using Unicode NFKC, outer trim and case-insensitive comparison; preserve original stored spelling. Multiple code matches are ambiguous. One code match with contradictory names needs review. A name-only match is a candidate for human resolution, not automatic update authority. Email/domain/contact/phone is never a sole key.

If an ID and code identify different records, block the row. Hold repeated source keys/target IDs for review; do not silently drop even identical duplicates. Do not strip company suffixes/punctuation to merge businesses. No match among visible records does not guarantee global uniqueness.

Create-only with an existing match is duplicate/deferred, not an implicit update. Updates preserve blank contacts, notes and certification. Explicit permitted clear needs preview approval. Source historical approval can be retained only as clearly labelled approved narrative, never forged system approval history.

Receipt must show source row, intended operation, actual ID, verification and deferred decisions. If a user declines prospective import of historical approved suppliers, hold those rows for the app rather than silently stripping their status.
