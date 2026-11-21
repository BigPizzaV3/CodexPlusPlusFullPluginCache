# Kaebox public-submission candidate — 2026-10-15

Status: portable package prepared for approval; NOT ready for public submission until the gaps below are resolved. No existing plugin was read or modified, no server deployed, and no submission draft was created or uploaded.

## Listing
Name: Kaebox
Subtitle: Compare Live Shipping Rates (27 characters)
Publisher requested: Kaebox, verified business identity. author.name and developerName match; identity verification and selection were not inspected and cannot be established by ZIP metadata.
Description and three starter prompts are embedded in plugin.json.
Category: Small Business intended based on prior user direction; omitted from manifest because the target dashboard's exact supported category title has not been verified.

## Connection and capabilities
Endpoint: https://mcp.kaebox.com/mcp
Transport: streamable-http. Direct initialize and tools/list succeeded without credentials; server kaebox-mcp 1.1.0, negotiated protocol 2025-03-26. No authentication headers or credentials are packaged; anonymous discovery succeeded. OpenAI auth extension omitted to conform to the published portable MCP schema, which rejects server extensions. Reconfirm anonymous access in the portal.
Exactly two tools discovered: get_shipping_options and get_shipping_rates. Full descriptions, schemas, and annotations appear in evidence/tools-list.json.
get_shipping_options: parcel catalog, optionally filtered by parcel type.
get_shipping_rates: live estimates from postal codes and selected parcel category codes; optional carrier filter, destination country, and ship timestamp. No purchase or shipment creation.
Both tools declare readOnlyHint=true and destructiveHint=false. openWorldHint is false for options and true for rates. Required boolean annotations are present and consistent with observed behavior.
No label generation, tracking, pickup scheduling, or purchase tool exists. A returned trackable flag is service metadata, not a tracking capability. Quotes do not establish eligibility for particular contents or restricted goods.

## Verification
Direct MCP initialization and discovery: Passed.
Catalog call: Passed; three parcel types and their categories returned.
Live box rate smoke test: Passed; 27127 to 22046, parcelType=3, parcelWeight=0, parcelSize=0 returned UPS, USPS, and FedEx service estimates. This is tool connectivity evidence, not a completed host review suite.
Five positive and three negative cases are embedded under extensions.com.openai.review.test_cases. All complete conversational review cases: Not run in a saved submission version. No fabricated pass results are asserted.

## URLs inspected
Website https://kaebox.com — accessible using direct HTTP fetch; identifies Kaebox shipping services and links its AI assistant. Existing assistant wording mentions labels beyond this MCP's capability; align that public wording before review.
Support https://www.kaebox.com/contact — accessible public contact page with Help@kaebox.com, text number, and contact form. Form submission was not tested.
Terms https://www.kaebox.com/privacy — accessible Kaebox Terms of Service; unusually named URL is the real footer link. Text refers to associated applications/APIs and the broader platform.
Privacy https://www.kaebox.com/privacy-1 — accessible Kaebox Privacy Policy describing service information, package details, device data, sharing and other practices.
No missing support/legal URL was found. Coverage of this exact MCP integration remains unconfirmed. Business owner must confirm or update coverage for postal codes, parcel categories, carrier requests, logging, retention/deletion, and any third parties. No policies or commitments have been invented.

## Remaining preparation
1. Confirm actual supported countries (specific country codes or explicit all available countries). Destination schema accepting country codes does not establish availability in those countries; publication.countries omitted.
2. Confirm commerce declaration: tools do not transact, but the business must confirm whether the plugin involves paid access or off-platform purchases and where payment occurs. review.commerce and commerce_description omitted pending the answer.
3. Supply/record and host a real demo video; demo_recording_url omitted until verified. No recording was created.
4. Confirm legal pages cover this MCP integration and align website capability wording.
5. Confirm Small Business is a supported category title in the intended portal and select the verified Kaebox business publisher. Package text cannot verify or override publisher identity.
6. Verify saved-version test cases, server connection, domain/developer verification, required scans and legal attestations in the portal only after approval. No reviewer credentials appear in the ZIP. Anonymous endpoint worked during inspection; reconfirm reviewer access at submission time.

## Demo walkthrough to record
Use the existing working Kaebox installation; do not create another private plugin. Start a screen recording with a tool such as the operating system screen recorder. Show (1) parcel choices, (2) the complete box quote prompt from positive case 3 with real carrier results readable on screen, (3) envelope-specific choices, (4) the exactly-1-lb boundary clarification, and (5) a tracking or label request correctly declined. Keep credentials and private data off screen. Stop, play back, and host the actual recording at a reviewer-accessible URL on a destination you control. Verify playback without private access before adding its URL to the manifest. A script is not recording evidence.

## Assets and package checks
Reused the 600 x 600 PNG icon publicly served as Kaebox's website favicon; inspected the actual image and checked legibility. Logo and composerIcon point to the included asset. Optional dark assets and brand colors omitted; they can be added if desired and are not blockers.
The ZIP contains one kaebox directory, required schema declarations, explicit SemVer, and portable mcp.json; no .app.json, apps bindings, secrets, credentials, dependencies or symlinks. JSON schema validation and ZIP inventory checks are recorded in VALIDATION.txt.
