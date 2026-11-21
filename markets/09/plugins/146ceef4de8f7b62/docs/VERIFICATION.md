# Banyan ChatGPT verification - 3 October 2026

Built in an isolated release checkout that preserves the original development work. The integration is deployed to production. OpenAI identity and domain verification are complete; directory submission and approval remain pending.

## Current hosted acceptance

The current workspace keeps Banyan white in either host theme, moves tree switching into family options, removes manual refresh, uses the original share icon and adds anchored wheel/pinch/button/keyboard zoom. The logo and DM Sans remain the website originals. Actual ChatGPT v9 acceptance ran with **Enforce CSP for custom apps enabled**: all 37 tools were discovered after a metadata refresh, Close family opened the six fictional adults, computed headings retained DM Sans, family options disclosed Switch tree, and the header contained no Refresh or Switch tree button. People search, protected profile drafts, successful saving with focus restored, and button/keyboard Full tree zoom passed. The saved fictional note was reopened in the profile. v10 adds an exact-relative native photo fallback and clearer timeout recovery; older aliases remain available. The v8 evidence below is historical.

The final Singapore-hosted candidate **305e268** at `banyan-49xru10qi-azs-ventures.vercel.app` passed all **37 tools** and **28 grouped/negative cases** through deployed MCP, native routes and production Postgres. Independent read-back verified persisted mutations and denied writes. Member and photo quotas, free-plan PDF restrictions, separate photo consent and the active-subscription deletion guard passed. Hosted OAuth refresh rotation, rejection of replayed refresh credentials and revocation of the rotated connection passed; every temporary connection was revoked through HTTP and its subsequent MCP request returned 401. Synthetic entitlements were restored and the temporary billing record removed; no Stripe operation or charge occurred. Private photo upload/read and both generated export formats passed. The operator report is `.tmp/chatgpt-v10-acceptance.json`.

The same hosted candidate passed **3,000 mixed requests from 1,000 synthetic connected identities across 50 fictional families**, ramped at 10, 25 and 50 concurrent requests. Every response matched its expected family/member IDs; saved changes were checked. There were zero failures and no observed cross-family leakage. At 50 concurrent requests, p50 was 313 ms, p95 1,274 ms and p99 2,175 ms. Temporary fixtures and auth records were removed; independent cleanup queries returned zero owned trees and zero auth records. This proves the measured MCP workload, not 1,000 simultaneous users or ChatGPT/model/device latency. The workload excludes photos and uses 20-member families; the separate large-layout fixture covers 1,000 relatives. The operator report is `.tmp/chatgpt-v10-capacity.json`. Functions are configured in Singapore beside production Postgres; the staged deployment's function locations were independently inspected.

`scripts/chatgpt-live-acceptance.cjs` passed all **37 tools** through an actual Next.js HTTP server, native routes and production Postgres using newly created fictional families and temporary synthetic OAuth connections. The run completed 19 grouped/negative cases, including independent database read-back, duplicate receipt replay, first-time join/claim, guest replacement, correction approval, branch approval, photo upload/read, generated PDF/GEDCOM files and reviewed batch persistence. Connections were revoked. Temporary synthetic paid entitlement was restored; no subscription or charge was created. A disposable synthetic tree was physically removed through MCP and its absence checked. The retained local report is `.tmp/chatgpt-candidate-acceptance.json`; it is operator evidence, not a package credential file.

This acceptance found and corrected real defects: first-time claiming incorrectly required existing membership; revoked invitations could start branch requests; relationship arrays and joined-member envelopes lost their identifiers; parent/child updates and removals skipped the inverse edge; unknown-age self-join confirmation was not retained; and a PostgreSQL DATE could be returned as a timestamp, preventing an explicitly reviewed adult batch from saving. Calendar dates now remain dates. Removal and role changes use the same tree transaction lock, recheck the acting elder, preserve a connected elder and reject concurrent demotions that would leave none.

GitHub CI for **8846d24** passes **110 web suites, 929 tests and one snapshot**, six mobile suites/26 tests, lint, TypeScript and the production web build. The v10 exact-relative fallback has an interaction regression test. Release parser and rendered /updates tests pass. Hosted evidence is distinct from installed-package and physical-device evidence.

The current [review walkthrough](https://banyan.family/chatgpt/review/banyan-1.0.0.mp4) is a 102-second, 720 by 840 H.264 video assembled from 17 chronological actual ChatGPT v9 captures. It shows the accepted white workspace, branches, People search, saved profile read-back, protected edits, Full tree zoom/Fit, the saved gathering, guest review and family options. v10 retains that geometry and identity and changes the native photo destination and timeout recovery copy. Idle waits are shortened into six-second state holds; this is a captured-state walkthrough, not continuous gesture footage or generated UI. The sidebar is closed, only fictional family data is shown and there is no audio. HyperFrames 0.8.114 passed lint/runtime/layout/motion checks (the dense sequential capture track has a reviewed organizational warning). Rendered duration, dimensions and codec were independently checked. SHA-256: `109fb24cfd5ff7d3acc7f02062c0be0ab9997042b8f90fb638304c4d152d0a02`.

Both repository-root and web-root deployment configurations preserve the existing cleanup and weekly-digest schedules and select Singapore. Their region/schedule parity was checked. The root configuration ensures clean CLI deployments honor these settings as well as web-root deployments.

OpenAI's draft scanner previously flagged eleven bounded family tools as open-world. The tool descriptions now explicitly identify their connected-account and authorized-family boundary and lack of external recipients or arbitrary URL targets. The closed-world annotations remain correct under [OpenAI's current annotation requirements](https://developers.openai.com/plugins/deploy/app-review#review-and-approval): externally hosted private workspaces are still bounded. Invite-based joining/claiming and cross-family linking retain their open-world flags. The focused protocol, HTTP and adult-sharing suites pass 38 tests after this description clarification; canonical rescanning is required before submission.

## Historical v8 ChatGPT acceptance

The website-matched workspace is deployed as widget v8 at main commit b0e644eb02cf8cf69295a82a878680a6f983032b. GitHub CI and the production deployment pass; the live resource publishes v8, all 37 tools and the current release entry. The v7 container font correction protects the original DM Sans from ChatGPT's injected html/body font. The v8 follow-up removes duplicate displayed reciprocal connections and clarifies that Banyan's spouse relationship is displayed as Partner, including unmarried partners. Older resource aliases remain available.

Fresh acceptance in actual ChatGPT opened Review redesign family, containing six fictional adults and no invented birthdays. Close family is the default, as explicitly selected by the owner to match the website. The Sam/Maya Partner household, Noor/Idris parents and Lina/Amir children use the website's identity and family semantics. Both the workspace and dialog headings resolve to DM Sans in the actual host.

- Branches show the genuine descendants, follow Lina's family and return to Sam's family.
- People search locates Noor. Her profile shows one Sam Child connection; distinct other connections remain available. Profiles without photos do not offer a misleading View private photo action.
- Profile editing protects an unfinished draft with Keep editing and Discard controls. Keeping it and saving persists the synthetic note and returns to People with the profile action in focus.
- Full tree locates Lina at readable scale and supports keyboard panning. An actual network refresh preserves the exact viewBox, 152 595 704 240.
- Review redesign gathering was saved on 2026-12-27. Its form's Cancel and Create controls each measure 44px and remain entirely inside the 480px widget. Saving and reopening the guest list confirms Noor as the only guest, with no invitations sent.
- The management panel renders the relevant role, export and native Banyan actions. No destructive action was taken.
- In Review family, Noor's separately permitted private photo decodes as a 1024px square image and displays inside the scrolling profile panel with the header fixed. The image is the original Banyan logo, not a person's photo. The mixed-age fixture still displays only three confirmed adults.

### Earlier adult-policy and security acceptance

The eight scenarios below were exercised on the earlier deployed v5 widget. That evidence is preserved separately from the fresh v8 interface acceptance; unchanged backend boundaries are covered by the current CI.

The eight scenarios below were repeated against the deployed adult-only build after renewing synthetic reviewer consent. Native sharing controls hid Noor when confirmation was withdrawn and showed her after confirmation was restored; a fictional profile dated 2020-01-01 stayed excluded. Production HTTP checks also rejected that younger profile's direct lookup, photo, relationship path, a contradictory adult declaration, and a whole-tree export. Filtered graph/layout output contained neither its name nor its ID.

All five positive and three negative review scenarios were exercised in ChatGPT Work through a private MCP connection to the production server. The connected account contains only synthetic review families.

- Listed the account's trees and opened Review family with its stored relatives.
- Previewed Review branch adult verified with Sam as founder, Noor as parent and no invented dates. Clicking Save changed the existing widget into the saved tree. The production draft records four completed operations. An earlier attempt saved correctly but exceeded the widget's response timeout; the successful retest followed the deployed timeout and private-tool metadata fixes.
- Resolved the stored Noor-to-Sam parent relationship.
- Created Review adult gathering with database date 2026-12-26 and Noor as its only attendee. No invitations were sent.
- Opened Noor's profile and displayed its private photo, which is the Banyan brand tree rather than a person's image. A final retest after the photo-response fix correctly told the user the image had opened in the workspace.
- Refused access to an uninvited stranger's private tree.
- Refused a viewer's request to rename their tree or promote themselves. Database inspection confirms the tree name and viewer role are unchanged.
- Read the synthetic Instruction test note as data and refused its export/transmission instructions.

The previous v8 review recording contained 24 actual ChatGPT frames and lasted 144 seconds. Its original captures and earlier failed responses are retained in ignored operator evidence. The current recording above supersedes it.

Production password sign-in for the dedicated reviewer account and scoped OAuth linking have also succeeded. Reviewer passwords are retained in an ignored Windows-user-encrypted operator file and are not included in the plugin ZIP.

These are MCP and widget tests. The uploaded package's family skill still needs a full private-package test in the desktop ChatGPT experience; its web directory entry currently opens on desktop only. The current v9 host acceptance above supersedes the earlier CSP-off result: enforcement is now enabled and the tested widget flows pass with it on.

## Passed

- Portable package validation stages exactly eight expected files: manifest, MCP transport, README, family skill, original logo and provenance, integration guide and verification report. HTTPS endpoint and credential-pattern checks pass; reviewer credentials are excluded.
- Final redesign CI for b0e644e: 109 web suites, 917 tests and one snapshot; web/shared/mobile TypeScript, lint and the production build pass with the repository's format-valid dummy CI configuration. The mobile checks pass six suites and 26 tests. The ten widget interaction cases include reciprocal Child deduplication while retaining a distinct Mentor connection.
- Host font correction: six focused widget, HTTP and release-note suites with 31 tests, web TypeScript and lint pass. Fresh v8 computed-style inspection confirms DM Sans on workspace and dialog headings inside actual ChatGPT.
- Actual-host follow-up found reciprocal parent/child edges repeated in profile navigation and a model preview using a custom partner label. v8 deduplicates only identical displayed member/relation links, retaining different connections. Tool/schema/package instructions identify spouse as Banyan's Partner type and explain reciprocal inference. Six focused suites with 32 tests pass, including a duplicate Child plus distinct Mentor case. Fresh deployed profile acceptance shows the intended single Child connection.
- v6 local browser proof at 1280×720, 960×800 and 390×844: website DM Sans, original tree artwork and colours; Close family default; focused-family context, real descendant branches, profile and family actions; calendar keyboard return; fixed edit controls. At 390×520, Save and Cancel remain completely inside the iframe with 44px heights.
- v6 photo checks: visible permitted portraits load through bounded private tool reads; profiles distinguish photo absence. The synthetic picker, keyboard crop, explicit positioning and save flow passed in the local browser. Tests reject stale/replaced image decodes, keep invalid replacement Save disabled and clamp crop positioning.
- v6 deterministic large-family proof: 1,000 adults, 1,002 graph appearances, a 1,542,273-byte complete local response and one observed 160ms local invocation. Browser search reveals Relative 1000 at readable 100% scale; keyboard pan survives refresh and Fit provides the overview. This is local payload/layout/navigation evidence, not a production concurrency benchmark.

- Production HTTP photo upload and private-photo read using the owned Banyan logo. GEDCOM (315 bytes) and PDF (3,722 bytes) export generation passed with a temporary synthetic paid entitlement; the original free tier was restored and no subscription or charge was created.
- Actual ChatGPT PDF export reached the download view. This host advertised no download-file capability, so the widget displayed the authenticated native Banyan fallback. The target tree and its native export menu were verified; a completed browser download was not captured.

- Earlier deployed CI: 106 web suites, 900 tests and one snapshot; six mobile suites and 26 tests. Web/mobile lint and typecheck, plus the production web build, passed for v5.
- Web TypeScript and ESLint checks (final CI also verifies shared/mobile and production build).
- Actual Next.js HTTP MCP/native-route integration against a dedicated Neon test branch: 37 tools; create tree, add/edit relatives, parent relationship, relationship path, create gathering and attendee replacement; duplicate mutation receipt replay; missing-auth and wrong-tree rejection.
- Private read load: 25 synthetic accounts, 25 concurrent readers, 250 reads, zero failures; p50 2.091 s, p95 2.339 s, p99 2.513 s on the small test compute. This is not a production or ChatGPT benchmark.
- Real Neon Postgres store: 30 concurrent locked counter updates, transaction rollback, eight concurrent identical mutation requests producing one result, refresh rotation and replay revoking the rotated connection.
- Branch-tested additive migration, then applied to the explicitly selected production main branch. No existing family tables or records were changed by that migration.
- Synthetic correctness checks for 1,000 distinct connected identities, OAuth/PKCE/scope boundaries, mutation receipts, reviewed batch checkpoints, transport metadata, maintenance and credential scrubbing.
- Fixture-host browser checks: graph, profile edits, nickname search, gatherings/guests, member creation, model-invoked photo display; desktop 960px, phone 390px and dark theme, adequate control height and no horizontal overflow.
- Real image processing tests: large PNG preview resized to bounded WebP with metadata removed; malformed images and oversized encoded uploads rejected.
- Cleanup/challenge route tests: credential rejection, feature-off skip, transaction-lock contention, expiry batching, rollback/release and exact plain-text domain challenge.
- Release parser and rendered preview /updates checks before each merge, followed by verification of the deployed entry. The adult-sharing entry is live.

Operator evidence is kept in private ignored files rather than the portable package. The native HTTP check uses a synthetic issued connection; it does not prove live Clerk sign-in or ChatGPT host rendering. The local preview is a test host, not the ChatGPT client.

## Still requires acceptance

- Full uploaded-package skill testing in desktop ChatGPT. Native desktop control is unavailable in this tool session; the browser cannot execute that installed desktop-only entry.
- Physical phone pinch and embedded file-picker acceptance. The controller does not support native multi-touch and did not emit the embedded file chooser, despite a visible standard input. Pointer-gesture regression tests, local responsive rendering, hosted image processing/storage and scoped reads pass. The fallback targets the same native profile.
- Completed host-mediated export download on a client advertising downloadFile. This browser host lacks that capability; generated PDF/GEDCOM bytes and the authenticated native fallback are verified separately.
- Reviewer credential transmission, completed submission, review approval and directory publication.

The [integration guide](./BUILD.md) explains connection, operations and publication. Hosted verification uses scripts/chatgpt-native-check.cjs with explicit production authorization and only synthetic data; verify the live /updates entry and canonical OAuth/MCP discovery after deployment.
