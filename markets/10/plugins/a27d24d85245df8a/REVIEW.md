# Google Review Link & QR — submission preparation

Updated 7 October 2026. Production commit `4d117019c` passed validation and deployment. Public submission and approval are not complete. This ZIP is a preparation copy; do not replace the existing private plugin or its saved app bindings with it.

## Release

MCP: https://productmate.com/api/plugins/google-reviews/mcp
No sign-in or OAuth is required. Offers and purchase links are disabled.
The private Productmate plugin is `Plugin_810ce21da1f081918fc2b30a8292e917`; its development app is `asdk_app_6ac6048732f88191a1ec7daaabecdb0b`.

Refresh the development connection after a server update. The old cached widget failed until Settings → Plugins → Google Review Link & QR → Refresh fetched the current resource, including clipboard-write permission.

## Live ChatGPT evidence

Chat: https://chatgpt.com/c/6ac6194d-d4d4-83eb-9b6f-328f55fa4e68
This is a private evidence reference, not a public reviewer-access link.

| Case | Observed result | Status |
| --- | --- | --- |
| Business search: PRODUCTMATE, Hamburg | App response, matching business, review URL and visible QR card | Passed |
| Ambiguous Cafe Central review-link request | App response, three locations, asks user to choose; no link created | Passed |
| Direct Google Maps URL | Card URL preserves Place ID ChIJN1t_tDeuEmsRUsoyG83frY4 | Passed |
| German Place ID request | German labels and download buttons; correct review URL | Passed |
| Direct Place ID without offers | Review link and PNG/SVG controls, no product or purchase offer | Passed |
| Post five positive reviews | Refused fabricated reviews; no app call shown | Passed |
| Local admin URL | Rejected as unsupported and requested Maps URL or Place ID; no app call shown | Passed |
| Ownership verification and paid kit | Declined verification and paid access; general Google help links, no plugin call or purchase | Passed |

**October 2026:** business search changed to the free IDs-only flow. Results no longer include names; the card shows candidates in a Google Maps embed and the user confirms one there. The two search cases above must be re-run in ChatGPT developer mode before submission.

These are user-visible workflow checks. Full tool arguments were not separately audited for each conversation turn. The original generic prompt “Find Cafe Central in Berlin” used ChatGPT's general search instead of the plugin. The revised case explicitly requests the review-link app and its supported task.

PNG and SVG files saved by actual widget button clicks were decoded with sharp/jsQR in Docker. Both contained the exact PRODUCTMATE review URL. Copy displayed “Copied!” after the clipboard API resolved, but the automation's virtual clipboard could not read the OS clipboard; the user independently verified clipboard paste on 7 October 2026.

## Demo

A real 27-second ChatGPT recording is saved locally at `tmp/review-plugin/productmate-chatgpt-demo.mp4`. It shows generation and the Copy/download actions. Two recorded segments were joined, removing the idle gap between them. No fabricated UI is included. Public demo: https://productmate.com/public-assets/53809af2-0414-4c82-ae02-88cc7ccc19c4 . Anonymous HTTP access returned the exact original MP4 (SHA-256 matched). The manifest includes this URL.

## Listing URL review

- Website: https://productmate.com/google-review-link-generator — reachable, describes the tool.
- Support: https://productmate.com/impressum — reachable, names PRODUCTMATE GmbH and gives email/phone contact. Publisher confirmed PRODUCTMATE GmbH on 7 October 2026.
- Privacy: https://productmate.com/plugins/google-reviews/privacy — reachable, names PRODUCTMATE GmbH and describes generation records and 90-day retention.
- Terms: https://productmate.com/plugins/google-reviews/terms — publisher approved on 7 October 2026. Deployed in commit 1805c20e1; anonymous HTTP 200 and approved text verified. Replaces the unsuitable /agb URL.

## Remaining requirements

- Publisher selected: PRODUCTMATE GmbH; all supported countries confirmed on 7 October 2026. Portal identity verification remains to be checked.
- Publisher/domain verification and legal declarations in the submission portal.
- Validate the completed metadata and preserve the portal's existing app bindings.
- Submit for review only after preparation; approval and publication are separate steps.

## Data

Business queries go to Google Places. QR files are rendered on Productmate. Short download codes refer to encrypted context in shared cache for up to seven days, and can expire sooner on cache eviction. The original signed expiry remains enforced. Generation records use source `chatgpt` and are removed after 90 days. Preview/download requests do not create new generation records. The widget sends no optional analytics events.
