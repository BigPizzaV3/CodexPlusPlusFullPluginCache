---
name: print-production
description: Prepare a 3DJ model for operator print quote review by Neural Deep Network Ltd; establish manufacturing requirements and explain quote, checkout, and shipping boundaries accurately.
---

# Print and deliver

Discover the actual MCP catalogue before proceeding. Read `../create-model/references/capabilities.md` for the 32 deployed tools and their required OAuth scopes. Never claim an order, charge, print booking, printer dispatch, or shipment happened without its own supported action and confirmed result.

Collect or derive: exact model/version, units, target dimensions in millimetres, material preference, colour, quantity, intended use, tolerances, finish, and delivery country/postal region. State unknowns explicitly. Do not collect a full street delivery address or payment card data in chat.

When `openscad_compile_model` is used, include its measured bounding box, closed-manifold status, and printer build-volume fit as supporting evidence for the design brief. Remember that `openscad_compile_model` does not create an exported STL asset URL or saved gallery model; a saved completed model in the user's gallery is required before calling `request_print_quote`. For a Replicad script, `cad_save_model` creates exactly such a saved model (with its measured STL) and returns the `modelId` to reference. Never turn `manufacturingApproved: false` into a manufacturing certification.

Separate three gates:

- **Design:** functional dimensions and model revision approved by the user.
- **Manufacturing:** a real exported mesh/solid inspected for watertightness, topology, thin walls, build volume, supports, and assembly clearance; printer/material-specific checks and an operator review. The schema (`cad_get_evidence_schema`), build-validation (`cad_validate_script`), export (`cad_export_model`) and save (`cad_save_model`) tools report kernel diagnostics and do not pass this gate on their own.
- **Commercial:** an operator-issued, expiring EUR quote tied to the inspected file hash, quantity, material/finish, destination region, currency, taxes, and shipping. Never estimate prices or delivery promises as if they are a live operator quote.

## Print Quote Request & Acceptance Workflow

1. Call `get_account_status` (`account:read`) to check account connection and `printQuoteRequestsOpen`.
2. When `printQuoteRequestsOpen` is `true` and the user asks to submit a saved completed model (`list_my_models` / `cad_list_models`), collect the required fields (`requestKey`, `modelId`, `dimensionsMm`, `material`, `colour`, `quantity`, `destinationCountry`, `destinationRegion`, `intendedUse`, optional `notes`) and call `request_print_quote` (`quotes:write`).
   - Use one unique `requestKey` per brief, reuse it for identical retries, and generate a new `requestKey` if any field or model changes.
   - Report the returned request ID, status (`pending_review`), and that `paymentRequiredNow` is `false`.
   - If `printQuoteRequestsOpen` is `false` (default operator gate when review queue is closed), explain that live quote submissions are currently closed and provide a structured manufacturing brief the user can keep or email to `3d@neuraldeep.net`.
3. Use `list_print_requests` (`quotes:read`) to check status and operator review notes. Use `cancel_print_request` (`quotes:write`) only when the user explicitly asks to cancel a request.
4. Use `list_print_quotes` (`quotes:read`) to show operator-issued EUR quotes, including confirmed material, colour, quantity, dimensions, delivery region, unit price, shipping, tax, EUR total, expiry, lead time, and the operator's inspection note and file SHA-256 reference. Explain that the inspection note is an operator attestation.
5. When the user explicitly accepts the exact displayed quote terms, call `accept_print_quote` (`quotes:write`) with the returned `quoteId` and `quoteHash`. Report the recorded acceptance clearly and state that payment checkout, print booking, and shipping are not connected in this release.
