# Public submission draft

Updated on 2026-10-24 Eastern for the version 1.0.1 icon update. OpenAI approved version 1.0.0; its saved submission uses the previous flat icon. This candidate replaces the listing and composer icon with the current 3D glass artwork and updates the version and release notes. Tools, authentication, permissions, review cases, and listing URLs are unchanged. These are separate public-submission sources; the private plugin is unchanged. Version 1.0.1 has not yet been uploaded or submitted, and publication is not claimed.

## Included

- `plugin.json`: portable Agent Plugins 1.0 manifest, English OpenAI listing, five positive and three negative review cases, verified public demo link, and release notes.
- `mcp.json`: the live HTTPS Streamable HTTP endpoint. Compatible clients discover OAuth and ask the user to approve access; no credentials are embedded.
- `assets/icon.png`: byte-identical to the current `public/brand/church-planner-icon-512.png` and `mobile/store-assets/google-play/icon-512.png`, a square 512 × 512 opaque PNG (277,009 bytes). The green glass church outline and cross, three coral/champagne/green spheres, and cream background match the artwork committed on 2026-10-10. SHA-256: `f80da840c4b689a780391965fa7c6332a1fbcd521ae5844e55006880cca474a3`.
- `claude-listing.draft.json`: a local worksheet for Claude's listing fields, not an official import format. Category, permanent slug, verified publisher details, and attestations remain unset.
- `review-fixtures.json`: synthetic ministry inputs and the isolated reviewer setup. No reviewer credentials are included.

The user confirmed the public developer name **Hapibit**, availability in **all countries supported by the destination platform**, and **free MCP access without purchases**. These values are recorded in the manifest, including the intentional empty `publication.countries` list. The intended name does not establish that a matching portal identity has been verified.

## Verified public destinations

The following public pages returned HTTP 200 after deployment on 2026-10-02 Eastern, with their content accessible without private login.

| Field | Destination | Observed content |
| --- | --- | --- |
| Website / documentation | https://churchplan.hapibit.com/mcp | Account prerequisites, OAuth connection instructions, six supported workflows, permissions, expiry and revocation guidance. |
| Support | https://churchplan.hapibit.com/support | Product help, account and role guidance, and contact link to `daniel@hapibit.com`. |
| Privacy | https://churchplan.hapibit.com/privacy | Product data handling, third-party AI/MCP sharing, personal-key and OAuth handling, retention, deletion, and contact details. |
| Terms | https://churchplan.hapibit.com/terms | User-approved MCP terms identifying Ziklag Holdings LLC, free access, permissions, data handling and an effective date of 2026-10-02. |
| Demo | https://churchplan.hapibit.com/review/index.html | Public HTML player with the verified 6:56 recording of a ChatGPT development connection using synthetic data. |

Live OAuth authorization-server and protected-resource metadata returned HTTP 200 with the MCP resource, public-client registration, S256 PKCE, and the documentation/policy links. An unauthenticated MCP initialization returned HTTP 401 with the protected-resource metadata challenge. These checks verify deployment and discovery; they do not establish authenticated operation inside ChatGPT or Claude.

The independent security review verified PKCE and client/redirect/resource binding, scope restrictions, token rotation and reuse handling, revocation, deletion, and consent boundaries. It found and resolved an authorization-code claim race and strengthened token audience isolation. All 13 focused server OAuth tests passed in the local fixture environment. These tests are separate from the cases against the saved submission version, which remain **Not run**.

The dedicated reviewer account and synthetic workspace were verified on 2026-10-02 at 22:10 Eastern. Normal password sign-in, sole ADMIN membership, accepted community rules and exactly three fixtures passed. The official MCP SDK discovered all six tools and verified P1-equivalent context, P2-equivalent pagination/detail reads, read-only write denial, write-scope context, refresh rotation and revocation. Those SDK checks left the fixtures unchanged and no active verification grants; they did not exercise P3–P5 mutations.

The reviewer subsequently completed ChatGPT development sign-in and consent, and the review app is installed. The published demo shows context, ministry details, a confirmed draft creation, a confirmed location-only update and confirmed rollover. Workspace snapshots corroborate the saved results and preservation of the original records. After recording, authorized administration removed only the two new synthetic records and verified that the original three-record baseline was restored, preserving the development connection. Exact tool arguments are not exposed by the observed UI, and P2's list output required an extra prompt. Development observations do not mark any saved-submission case as passed. No authenticated Claude host case has been reported.

## Remaining preparation

1. Supply the verified dedicated reviewer account's access instructions only in secure portal fields. Provisioning and SDK checks are complete; do not include the account details or credentials in this package. Preserve account access throughout review and restore the isolated three-record baseline between host runs.
2. Verify the saved submission version's connection in ChatGPT and Claude. Run the five positive and three negative review cases against that version, compare actual tool calls and visible results, and record results. Check both read-only and write-approved access. No saved-submission case is claimed as passed yet.
3. Select available categories and Claude's permanent listing slug in the target portals. Complete the intended Hapibit publisher/domain verification and required scans and policy acknowledgments. Authenticated portal access alone does not establish these requirements are complete.
4. Verify imported metadata and the saved version in the target portal. Rebuild and inspect a new ZIP if package fields change. A structurally valid draft ZIP is not a submitted or approved listing.

Optional dark-mode assets and brand colors are omitted and do not block preparation. The published terms are linked in the manifest; their source approval record remains outside this package at repository path `docs/release/mcp-terms-draft.md`.

## Package checks

From the repository root, `node integrations/submission/prepare.mjs --check` validates without writing an archive. Omit `--check` to create a uniquely named draft ZIP and an inspection report under `artifacts/submission/`. Workflow documentation and pinned schemas live beside this source directory and are excluded from the upload.

The builder validates both portable schemas, listing lengths, prompt uniqueness, review-case fields and counts, contained PNG paths and dimensions, an explicit inventory, forbidden app bindings, and known credential patterns. It reads the completed ZIP and verifies entries, CRCs, sizes and SHA-256 hashes against the checked source. The three sample ministry inputs separately passed the repository's actual ministry schema. The copied icon's SHA-256 matches its original source. These checks do not validate client-specific portal metadata or prove arbitrary content contains no sensitive data; review the inventory before sharing.

## Published demo

[Watch the demo](https://churchplan.hapibit.com/review/index.html) or [open the MP4](https://churchplan.hapibit.com/review/hapibit-mcp-demo-v1.mp4). The 6:56 recording is silent, 1600 × 880, H.264 at 10 fps, and contains actual ChatGPT development interactions with synthetic records. Idle intervals were removed and recording segments joined; the prompts and results are real.

The final file passed full decoding and visual contact-sheet review, which found synthetic data and no credentials. Local and public browser playback advanced normally with no media error. The public MP4 returned HTTP 200 with `video/mp4`; a byte-range request returned HTTP 206. The verified player link is included in the manifest. This demonstration is separate from the saved-submission case runs and does not imply directory approval.

## Sources

- [Agent Plugins manifest schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)
- [Agent Plugins MCP schema](https://agent-plugins.org/schemas/1.0.0/mcp.schema.json)
- [Claude connector submission](https://claude.com/docs/connectors/building/submission)
- Implemented behavior: `lib/integrations/operations.ts`, `lib/integrations/mcp.ts`, `lib/server/integrations.ts`, `lib/server/ministries.ts`, and `lib/server/validation.ts` in the repository root.
