# Public submission preparation

Status, October 4, 2026: v0.5.0 is publicly hosted at `https://peptara-calculator.vercel.app/`, with MCP at `/mcp`. A genuine private ChatGPT connection has now exercised the canonical remote endpoint, five positive and three negative review cases, and explicit Share with chat delivery. The actual Peptara Labs logo was visually verified in the private plugin icon, calculator header, and decorative vial. These private tests do not establish complete directory-installed production behavior: the host displayed CSP enforcement as off. At the recorded narrow chat width, the last digit of the large 10 mg / 3 mL result wraps onto a second line; the smaller formula remains readable.

The public draft is not submitted, approved, published, or listed. Latest user screenshots show MCP Configured, Metadata No Issues, and skill Checks passed. The only visible issue is incomplete review information, with supporting content identifying the missing `demo_recording_url`. Ken clarified that this draft and business-verification work belong to the original PeptaraLabs organization on another account. The current ChatGPT account is only for private walkthrough testing. Ken will upload the final ZIP himself from the original account. Registered PeptaraLabs LLC is user-reported; the official OpenAI publisher-verification result has not been independently confirmed. No organization, account-setting change, submission, or publication is authorized by this handoff.

## Review payload and commercial purpose

`REVIEW-CASES.json` contains exactly five positive and three negative cases using the documented review field names. These cases and the commerce disclosure are included in `extensions.com.openai.review` in the portable `plugin.json`. The file in `docs/` is a readable source copy; the portal imports the manifest declarations. Positive cases include `description`, `prompt`, `tools_triggered`, and `expected_behavior`; negative cases include the first two and their expected safe outcome. `publication.release_notes` is populated.

The `commerce: true` declaration discloses the commercial brand-discovery purpose. There is no in-plugin checkout, payment, account requirement, cart, or product search. Optional CTAs link to the Peptara Labs homepage and COA page. The calculator works without visiting either link. Do not describe it as having no commercial purpose, hide the CTAs, or claim the linked catalog is approved. Directory eligibility of the brand links remains unresolved.

## Live private ChatGPT evidence

The private connection is named **Peptide Reconstitution Calculator by Peptara Labs**. It connects without application authentication to `https://peptara-calculator.vercel.app/mcp`. Its private connection package version is separate from the public portable package's v0.5.0. The Peptara Labs PNG was selected during connection creation; screenshots verified the actual icon in the plugin header and app row. This connection is for walkthrough testing, not the public directory draft.

| Check | Observed result | Limit |
| --- | --- | --- |
| Review cases | Five positive and three negative cases executed against the remote endpoint; model responses were correct | The portal's earlier completion ticks alone did not establish execution. This later walkthrough supplies private-host evidence. |
| 10 mg / 3 mL | Correct model response for final total solution volume | Verified approximately 3.33333333333 mg/mL and 3333.33333333 mcg/mL. The large value wraps its last digit at the recorded narrow width; the formula remains readable. |
| Unit conversion | 750 mcg / 150 microliters returned 5 mg/mL | Synthetic arithmetic fixture, not suggested quantities. |
| Decimal arithmetic | 13.7 mg / 2.5 mL returned 5.48 mg/mL | Synthetic arithmetic fixture, not preparation validation. |
| Equipment references | Changing from a 0.5 mL U-100 reference to a 3 mL marked reference left concentration unchanged | Capacity references do not calculate syringe markings or recommend a device. |
| Reset | Cleared the calculator form | Does not erase information already shared with ChatGPT. |
| Share with chat | A unique fixture entered only in the component, 17.2 mg / 4 mL = 4.3 mg/mL, was explicitly shared through `updateModelContext`; ChatGPT then correctly repeated the fixture, which had been absent from the chat | This establishes delivery after explicit sharing. Values supplied directly in chat are already conversation data. |
| Automatic sharing | Source inspection found no automatic sharing call before the explicit Share action | This is source evidence, not a claim about every provider's operational processing. |
| Brand rendering | Actual Peptara Labs logo verified in plugin icon, calculator header, and decorative vial | Public listing rendering is still separate. |
| Host CSP | Host badge showed CSP enforcement off | Production directory CSP enforcement remains unverified. |

All quantities above are test fixtures. They verify concentration arithmetic and interface behavior, not source quantities, preparation suitability, doses, or administration. The earlier real-user screenshot with 10 mg and 3 mL was also checked for arithmetic with 3 mL explicitly treated as final total solution volume.

The genuine walkthrough is deployed at `https://peptara-calculator.vercel.app/review/demo-20261004.mp4`, also included at `public/review/demo-20261004.mp4`. It is 306.833 seconds, 7,134,157 bytes, H.264/yuv420p, 1366 by 1000 pixels, with 17 chapters and no audio. Full decoding, all eight review cases, corrected Reset before/after, explicit sharing, and actual-logo rendering were checked. Anonymous GET returns HTTP 200 with video/mp4 and byte-exact content; a byte-range request returns 206. Neo browser playback and seeking to 150 seconds passed without a video error. The final manifest contains this URL. Import into the original public draft remains for Ken to complete. The video contains only actual captured UI, with no fabricated tool responses.

## Hosting, audit, and privacy evidence

- Final video deployment `dpl_Cj7RsrTAC23PshvmrfwDVutgtcq2` is READY and aliased to the canonical hostname. All eight anonymous public calculator checks passed again after this deployment. Video SHA-256: `77281ef4c2d33d046e7de131778665a1bddb1bf4f7b0871d9a6000078912cfaf`. Workspace evidence: `work/review-video-qa/hosting-verification.json`, `final-provenance.json`, and `browser-playback.json`. The final source passed 40 automated tests with zero failures.

- Version 0.5.0 passed 40 tests with zero failures and `vercel build --prod`. Eight anonymous public checks passed without authentication or a bypass: root UI exact hash, health reporting 0.5.0, privacy with verified retention text, support, MCP initialize, discovery of two tools, 13.7 / 2.5 = 5.48, and byte-exact embedded UI of 708,404 bytes. Workspace evidence: `work/public-release-audit/public-checks.json`.
- Eight earlier authenticated checks established the protected deployment's behavior. They are historical and separate from the eight anonymous checks. Deployment `dpl_4RP3UJxMZ42dAijquLfpu6sM4Lx8` included the verified privacy corrections; its served content and anonymous browser access were checked.
- Domain-challenge deployment `dpl_3u1c6D1TAygnXEYydGzoi8WnMkho` passed three anonymous checks: HTTP 200 with the exact supplied 43-character challenge and no newline, health reporting 0.5.0, and discovery of both tools. Workspace evidence: `work/public-release-audit/domain-challenge-checks.json`. The challenge is not reproduced here. Later user screenshots show MCP Configured and supersede the earlier pending Connect and domain-setup state.
- The initial deployment was automatically assigned to production and briefly exposed the canonical URL before protection was applied and verified. After the Opus hosting gate and privacy corrections, only the `peptara-calculator` project's SSO setting changed from `all` to `all_except_custom_domains` under Ken's publication authorization. Canonical anonymous access was then verified.
- Ken waived GLM for this release. The earlier GLM invocation timed out without a report, and Robin Opus was quota-blocked. The local claude-opus-5 review completed October 4, 2026 with HOSTING GO. It found no high-severity exploitable runtime or security defect in the hosting changes. Four non-blocking findings remain: repeated HTML validation on MCP requests, loopback Host/Origin acceptance for non-loopback peers, unnecessary stateless GET event streams, and the canonical UI domain on previews. No remediation is claimed by this status update. See [the Opus release review](OPUS-RELEASE-REVIEW.md) and [verification record](VERIFICATION.md). Hosting approval does not establish directory eligibility or approval.
- Calculator-specific `/privacy` and `/support` pages are deployed. Vercel CLI API evidence established an active Pro team with Observability Plus, no disabled observability projects, and no log drains. Vercel's runtime-log documentation, updated August 28, 2026, specifies 30-day retention for this configuration. The served privacy notice states that period. It does not promise the same expiry for every provider security, service-operation, or legal record.
- Peptara Labs' [existing privacy policy](https://www.peptaralabs.io/privacy) was live-read. Support is a stated purpose; information is retained as long as needed for stated purposes or required by law, then deleted or anonymized. The calculator notice applies those existing criteria to support correspondence. No fixed numeric support-mailbox period or separately audited mailbox-deletion process is claimed.

## Public draft and remaining work

| Item | Current evidence | Remaining action |
| --- | --- | --- |
| Account and organization | Ken says the PeptaraLabs public draft and business-verification work are on another account; current account is private testing only | Ken uploads the final ZIP using the original account and intended PeptaraLabs organization. Do not create a replacement organization. |
| Developer identity | Ken reports registered PeptaraLabs LLC; manifest publisher is Peptara Labs | Confirm the official verification result and selected publisher identity in the original account. Registration alone does not establish OpenAI verification. |
| Portal status | User screenshots show MCP Configured, Metadata No Issues, skill Checks passed, and incomplete review information | Preserve the accepted metadata and connection. Review submission and approval are still pending. |
| Remote MCP and UI | Private ChatGPT tests now exercise the canonical endpoint and embedded component; sharing delivery passed | Complete directory-installed host checks, including production CSP enforcement. Private testing does not prove this enforcement. |
| Presentation and interactions | Arithmetic, equipment references, Reset, logo rendering, and explicit Share tested | The large repeating-decimal value wraps at narrow width. Additional directory-host mobile, motion-control, and fixed-CTA checks remain separate. |
| Authentication and domain | No application authentication; public website and MCP available; domain challenge exact-match checked; portal MCP Configured | Preserve the intended configuration and challenge. No repeat Connect/domain action is identified by current evidence. |
| Review cases | Exactly five positive and three negative cases in the manifest, executed in the private remote ChatGPT walkthrough | Keep actual outcomes and any residual limitations in the final reviewer materials. |
| `review.demo_recording_url` | Present in final manifest; genuine video deployed and anonymous playback, seeking, byte range, and content hash verified | Upload the final ZIP into the existing public draft and check that Supporting content imports the URL. |
| Website and support | Portal imported `https://www.peptaralabs.io/` and `https://www.peptaralabs.io/contact`; destinations live-verified | Retain these listing URLs. The calculator also has its own `/support` help page. |
| Privacy and terms | Calculator-specific `/privacy` deployed with verified retention wording; existing Peptara Labs terms URL supplied | Confirm final imported URLs and terms applicability at submission. Keep runtime-log and support-retention claims distinct. |
| Name, description, and category | `Peptide Reconstitution Calc`, public-release wording, and Education & Research imported; Metadata reports No Issues | Preserve accepted values. The earlier Education-category rejection is resolved. |
| Commerce | `commerce: true` and explicit homepage/COA CTA disclosure included | Keep the imported disclosure accurate; directory acceptance of linked destinations remains for review. |
| Release notes | Initial notes included under `publication.release_notes` | Match the final package and demo URL to the actual deployed behavior. |
| Countries and translations | No publication targeting supplied | Confirm intended availability in the original portal account. Translations are optional. No restricted-country approval is inferred. |
| Submission and publication | Draft uploaded, not submitted or published; no review approval | Ken completes remaining review information and actual attestations, submits from the original account, and publishes only after approval. |

Display name, subtitle, and developer name fit their documented limits: 27, 26, and 12 characters respectively. Build and validate the final v0.5.0 ZIP after release edits; earlier archive checks do not establish that a later package is current. Keep the stable public package name when uploading updates. The current private connection and its generated package must not replace the public draft's identity.

## Tool annotations

Both tools explicitly declare `readOnlyHint: true`, `destructiveHint: false`, `openWorldHint: false`, and `idempotentHint: true`. They compute or open a bounded calculator; they do not fetch arbitrary external content or mutate external state. Fixed, user-activated CTA navigation is separate from calculation tools.

The current Plugin Guidelines say annotation justifications are no longer required. The submission-error reference still contains `justification_required`, so those pages are inconsistent. Keep accurate explicit boolean annotations; do not invent justification fields. If a real portal scan flags an issue, examine it and provide clarification or appeal as the guidelines permit. External iframe-domain explanations are separate where external frames are used; the current UI is self-contained and declares no external frame origins.

## Official references

- [Submission fields, review materials, verification, and publication](https://developers.openai.com/plugins/deploy/submission)
- [Portable package layout and remote MCP configuration](https://developers.openai.com/plugins/build/plugins)
- [Plugin guidelines, annotations, privacy, advertising, and commerce](https://developers.openai.com/plugins/plugin-guidelines)
- [Submission errors and the inconsistent annotation-justification entry](https://developers.openai.com/plugins/deploy/submission-errors)
- [Remote MCP review and production endpoint requirements](https://developers.openai.com/plugins/deploy/app-review)
- [Vercel runtime-log retention, updated August 28, 2026](https://vercel.com/docs/logs/runtime)
- [Peptara Labs privacy policy and support-retention criteria](https://www.peptaralabs.io/privacy)

The walkthrough deployment is complete. The final package is prepared for the original public draft. No account switch, organization change, review submission, directory approval, or directory publication is claimed.
