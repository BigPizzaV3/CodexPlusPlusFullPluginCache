# Verification and public submission

## Verified on 13 October 2026

- The supplied HTTPS endpoint accepted an unauthenticated MCP initialize request using protocol 2025-03-26.
- Server identity: `hg-mcp-filinvest`, version `0.1.0`, title `Filinvest`.
- Streamable HTTP session establishment and read-only `tools/list` succeeded.
- Two tools were exposed: `search_hotels` and `check_availability`.
- Both tools expose boolean readOnlyHint, destructiveHint and openWorldHint annotations. The values were preserved in the discovery snapshot, not independently certified for all downstream behavior.
- Tool responses advertise hosted hotel and availability UI resources.

Hotel search, dated availability, UI rendering and checkout were not executed for this packaging task. All five positive and three negative review cases in plugin.json remain Not run. No real booking or payment action was attempted.

## Public submission materials still needed

This is a connection/source ZIP, not a complete public-submission bundle.

1. Supply four verified public pages for this app: website, support, privacy policy and terms of service. They must cover the app and hotel booking flow, not merely an unrelated brand website. Set the actual verified URLs under extensions.com.openai.interface. No guessed URLs are included.
2. Supply an approved square Filinvest app icon and add contained assets/logo.png and the interface logo/composerIcon references. No unofficial logo is included.
3. Confirm the commerce declaration supported by the target portal. Prior owner instructions describe hotel reservations within the app, card details supplied as a guarantee through the secure provider view, and payment at the hotel. These practices require provider confirmation and policy coverage; no security certification is implied.
4. Record a real demo and host it at a reviewer-accessible URL. Add review.demo_recording_url only after verifying access and playback.
5. Run the draft review cases in the intended host, using future dates and test checkout data. Update case expectations if the actual provider behavior differs. The package does not invent hotel IDs or availability.
6. Complete business/domain verification, connection checks and required legal declarations in the publisher portal. Publisher name in this ZIP does not establish verified ownership.

The owner's previously specified audience is all available countries, represented by publication.countries=[]. Confirm the imported country targeting in the target portal.

## Suggested demo sequence

Connect the endpoint in an authorized development setup. Search for a family resort in Boracay and show actual results. Select a returned hotel, enter future dates for two adults and show live rates and policies. Open the returned checkout view without completing a production booking. Show a flight-booking request as an unsupported-task example. Keep card details, credentials and unrelated account content off screen. Record the actual interaction, then verify playback and reviewer access.

Installation and ZIP validation do not guarantee public-directory approval.
