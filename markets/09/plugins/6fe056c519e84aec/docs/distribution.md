# Distribution status

Updated 2026-10-08. A valid package is not a directory approval or a complete host acceptance test.

| Route | Current state | Next requirement |
| --- | --- | --- |
| Claude Code repository marketplace | Published; Claude Code 2.1.284 installed from GitHub; strict validation passes | Interactive OAuth and publish/update/revoke acceptance |
| Codex repository marketplace | Published; install check and full hosted API-key workflow passed in Codex 0.155.1 | Interactive OAuth and recorded browser/host demonstration |
| skills.sh / Skills CLI | Public Shareout detail page verified 2026-10-06; remote skill installation passed | Ranking and install counts are not yet populated |
| OpenCode | Configuration published; OpenCode 1.17.11 connected to production with a disposable API key | Interactive OAuth and publish/update/revoke acceptance |
| Gemini CLI | Extension 0.1.6 published; isolated install and skill discovery passed; required gallery topic verified | Daily gallery crawler listing unconfirmed; authenticated host acceptance remains separate |
| Cline Marketplace | Skill [PR #179](https://github.com/cline/marketplace/pull/179) submitted; installation and marketplace validator passed | Await maintainer review; authenticated publishing not yet verified |
| Cursor Marketplace | Declined at this time; owner shared response 2026-10-08 | Team recommends cursor.directory; no reason provided |
| Cursor Directory | [Community submission accepted](https://cursor.directory/plugins/shareout) 2026-10-08; one MCP, one skill and brand icon | Security scan pending; unpublished and hidden until it completes |
| VS Code / GitHub Copilot | MCP configuration prepared | Host acceptance |
| Official MCP Registry | Published and independently verified: `io.shareout/shareout` version `0.6.2` | Keep metadata aligned with releases |
| ChatGPT / Codex public directory | Submitted by owner 2026-10-05; portal independently shows In review and Not published; package 0.1.5 | Await review decision; approval and publication remain separate |
| Claude directory | Deferred by the owner on 2026-10-02; existing repository package remains available | Revisit if a paid publisher account and product fit justify it |
| Smithery | [Published](https://smithery.ai/servers/gregaeland/shareout) 2026-10-05; production 0.6.2 and all eight tools discovered | Full publish/update/revoke through Smithery remains a separate host acceptance test |
| Glama | [Live, ownership verified, Healthy](https://glama.ai/mcp/connectors/io.shareout/shareout); all eight tools discovered | OAuth health-check profile uses isolated demo workspace; renew when grant expires |
| PulseMCP | Submission pause rechecked 2026-10-05 | Wait for submissions to reopen |
| Docker MCP Catalog | Withdrawn at owner request; PR #5462 closed without merge | Do not reopen without explicit request |
| Awesome MCP Servers | Free submission accepted 2026-10-05; awaiting review | Directory says review within two weeks; contact email receives approval notice |
| Vercel Connect | API-key service submitted 2026-10-05; configuration valid | Await review; OAuth dashboard test remains incompatible with required token resource parameter |
| mcp.so | Current intake requires a $39 payment | No paid submission authorized or purchased |
| GitHub public MCP directory | Curated surface investigated; no submission made | Establish the current intake route; registry publication alone does not establish a GitHub listing |

## Additional distribution pass — 2026-10-05

Official MCP Registry 0.6.2 was published through the existing domain-owned identity and independently read back as active and latest. Official plugin, MCP and registry schemas all pass. The submitted OpenAI 0.1.5 release assets were not replaced.

Awesome MCP Servers accepted the free Shareout submission with the hosted endpoint, OAuth authentication, registry name, documentation URL and hello@gregeland.com contact. The page explicitly confirmed successful submission and review within two weeks; this is not yet an approved listing.

The owner completed sign-ins. Smithery successfully scanned production 0.6.2 and discovered all eight tools; its public listing shows Published Oct 5, 2026. Optional resource/prompt discovery returned method-not-found warnings without blocking publication. Cursor publisher application submitted after owner approval; portal confirms receipt with “Thanks for applying”. Glama session expired during the follow-up; fresh sign-in requested before completing profile and connector submission. Vercel Connect has a locally saved service draft, SVG icon, hosted target, successful OAuth discovery and automatic registration, and a test connector in the Elandry team. Chrome resolved the built-in-browser redirect block and completed isolated demo consent. The OAuth token exchange still failed because the required MCP resource was absent; Vercel documents resource indicators as SDK-only. Shareout validation remains unchanged. A separate API-key-only service submission succeeded in Chrome (571fbf94-d02b-447d-9592-ebd5ce7039e3); Vercel confirmed Service Submitted and API Key Configuration Valid. This is review intake, not publication. The optional SVG was omitted because Chrome extension file access was disabled. OAuth remains an unverified follow-up, and no private API key was submitted. The owner explicitly approved isolated demo read/write OAuth tests for Smithery and Vercel. PulseMCP remains paused. No paid aggregator placement has been purchased.

Docker catalog draft [PR #5462](https://github.com/docker/mcp-registry/pull/5462) contains the three required remote-server files. The official validator and catalog generator passed. Docker MCP 0.42.2 loaded the isolated catalog and reached a 401 without OAuth credentials, as expected; authenticated host acceptance remains pending. No checks were reported immediately after opening the draft.

## Current OpenAI submission

2026-10-20: package 0.1.5 is Approved, Ready to publish, Not published (verified in portal). A fresh scan flags catalog, links, reviews and versions for grouped operations. MCP/CLI 0.7.0 and plugin 0.2.0 are being prepared to expose independent operations; they are not yet deployed, uploaded, reviewed or published. The older submission narrative below is historical.


The owner completed final attestations and submission on 2026-10-05. The publisher portal independently shows Shareout “Version 1.0.0 · In review”, “Not published”, and “Configured”. The uploaded portable package is 0.1.5; the portal uses a separate associated-app version label. The final ZIP includes the accessible 6:01 labeled walkthrough URL, verified by anonymous HTTP 200 and SHA-256 match. Reviewer credentials were saved privately. Non-blocking MCP findings remain for reviewers. Earlier dated notes below describe the path to submission and are superseded by this status.

## Verified evidence

- Public source: [geland/shareout-integrations](https://github.com/geland/shareout-integrations). Initial package CI [37078527842](https://github.com/geland/shareout-integrations/actions/runs/37078527842) passed.
- [Official Registry version 0.6.2](https://registry.modelcontextprotocol.io/v0.1/servers/io.shareout%2Fshareout/versions/0.6.2): published through shareout.io domain verification, then independently read back. This is not endorsement by the registry or an automatic curated listing elsewhere.
- Claude Code and Codex installation checks used isolated/local test scopes. The temporary Codex installation was removed afterward. Claude Code's separate MCP health check stopped at its project trust approval; it did not establish a connected session.
- Skills CLI discovery and project-scoped OpenCode installation passed with test telemetry disabled. No claim of skills.sh indexing or ranking.
- OpenCode's actual MCP connection returned `connected`. Its disposable empty workspace was deleted and key revoked. This check used API-key authentication, not the OAuth sign-in UI.
- Production policy/support pages, connection guide and agent discovery file verified live. Worker `908eb9e8-3bf0-4688-bb33-4d637dbcca27` serves source `1b26a08` at 100%. HTML matches source after excluding Cloudflare’s injected analytics beacon; the privacy policy explicitly discloses it. Typecheck, 82 Worker tests and exact-source CI passed; post-deploy MCP initialization and all eight tool definitions returned successfully.
- OpenAI and Claude publisher sign-ins completed. OpenAI confirmed the individual developer identity and accepted package 0.1.3 as a draft on 2026-10-03. The replacement 0.1.4 draft passes metadata and skill checks, its domain is verified, and all five positive/three negative cases imported. The live OAuth flow now reaches Shareout account consent; the discovered relay-state length incompatibility was fixed and deployed with 85 passing Worker tests. The owner approved consent. Manual clicks exposed native-form origin and callback CSP defects. A three-origin fixture reproduced the remaining client relay failure in both regular Chrome and the built-in browser. The production correction passes 87 Worker tests and both browser fixtures; one consent click now reaches OpenAI's callback. The owner completed OpenAI's human-verification check; the portal now shows Authorized, Domain verified, and all eight tools. Three tools have generic further-review findings. Reviewer access, running and recording the scenarios, and final submission remain incomplete. Claude directory submission is deferred at the owner’s request; the signed-in account is Free and the portal requires a paid plan. Cursor, Smithery and Glama still need their publisher account flows. The OpenAI draft is not a submitted or approved listing.

## Host acceptance procedure

Use a disposable Shareout workspace and fictional HTML, never a customer's document. In each host: connect using its normal UI, list tools, publish via file upload, open the recipient link, update with the starting base version, verify the same link shows the revision, revoke the test link, and remove the test data. Record the host version and outcome. Validate error handling when the host has no file-transfer capability. Existing service-level OAuth/tool tests do not replace these host checks.

## Listing copy

**Name:** Shareout

**Publisher:** Greg Eland

**Support email:** hello@gregeland.com

**Support:** https://shareout.io/support

**Privacy:** https://shareout.io/privacy

**Terms:** https://shareout.io/terms

**Short description:** Share what your agent makes

**Description:** Publish HTML reports, proposals, walkthroughs, and interactive pages. Share a link, collect feedback, and publish revisions at the same address. Named links can expire or be revoked. A Shareout account is required. Hosted publishing accepts native ChatGPT HTML attachments or direct HTTP transfer; local MCP and the standalone CLI read files directly from disk.

**Endpoint:** https://shareout.io/mcp

**Website:** https://shareout.io

**Docs:** https://shareout.io/agents

**Live example:** https://shareout.io/d/cujufgdheurd

The publisher and support contact were confirmed on 2026-10-02. Cloudflare confirms the support address has an enabled forwarding rule and a verified destination. Public policies are live. Publisher verification is confirmed; MCP authorization/discovery and private reviewer credentials are now complete. The host walkthrough and recording are complete and OpenAI review is pending; generic tool findings were non-blocking. Do not place private review credentials in this repository or ZIP. The live example is not a substitute for a recorded host demo.

The 0.1.3 package adds the public policy URLs and five positive/three negative scenarios. Fictional first/revised HTML files live in `examples/review/`; see [submission kit](submission-kit.md) for data-handling answers and remaining gates. Public policy URLs were verified after deployment. Cases are prepared, not a claim that every host has passed them.

## Sources

- [OpenAI packaging](https://developers.openai.com/plugins/build/plugins) and [submission](https://developers.openai.com/plugins/deploy/submission)
- [Claude plugin submission](https://claude.com/docs/plugins/submit) and [manifest reference](https://code.claude.com/docs/en/plugins-reference)
- [Skills CLI](https://skills.sh/docs/cli) and [directory discovery](https://skills.sh/docs/faq)
- [OpenCode MCP](https://opencode.ai/docs/mcp-servers/)
- [Cursor plugins](https://prod.cursor.com/docs/plugins)
- [Official MCP Registry](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/quickstart.mdx)
- [Smithery publishing](https://smithery.ai/docs/build/publish)
- [Glama connector submissions](https://glama.ai/mcp/faq)
- [PulseMCP submission notice](https://www.pulsemcp.com/)
- [Awesome MCP Servers submission](https://mcpservers.org/submit)
- [Vercel Connect submission launch](https://vercel.com/changelog/vercel-connect-service-submissions) and [provider requirements](https://vercel.com/docs/connect/providers)
- [mcp.so paid intake](https://mcp.so/submit?type=server)


### Review readiness update — 2026-10-03

Service MCP 0.6.1 and isolated reviewer demo access are live. OpenAI's private reviewer fields were saved successfully, and the new tool definitions were rescanned. Three generic further-review notices remain. ChatGPT host sign-in and the actual recorded review workflow are still needed; no final submission or approval is claimed. The integration package remains 0.1.4 and the official MCP Registry listing remains 0.6.0 until a separate registry update.

Package 0.1.5 prepares native ChatGPT file-input guidance for deployed MCP 0.6.2. Native attachment publication and anonymous exact-byte recipient access passed; see [host acceptance](host-acceptance.md). The portal remains on draft 0.1.4 until a replacement package is uploaded; no directory approval is implied.

Follow-up: Docker Desktop 29.5.3 is running. PR #5462 remains open/draft, review required, with no CI checks reported. Starting Docker OAuth awaits explicit approval for isolated demo workspace read/write access; the prior approval named only Smithery and Vercel.

Glama follow-up: Google-backed account onboarding completed. Submission identified an existing registry-imported io.shareout/shareout connector, avoiding a duplicate. Public listing reports Unhealthy and OAuth Works in Glama; this badge does not establish our own authenticated test. Domain ownership can be verified using /.well-known/glama.json or a TXT record. Claim and isolated health-check access await explicit approval; no verification file or test credentials have been published.

Glama completion: owner approved namespace claim and isolated health checks. Public domain proof deployed from afad9b4 as Worker 51f37724-ee37-408a-938d-7d6593c233d4 at 100%; exact live JSON bytes verified. Ownership verified in Glama, OAuth health check passed, public listing shows Healthy and eight tools. Read-only grant metadata confirmed reviewer workspace ws_demo_9081c380d08e with read/write scopes. Support contact saved as hello@gregeland.com and thumbnail uploaded. The proof stays public for daily ownership checks. Full publishing acceptance through Glama remains separate from discovery/health checks.

MCP 0.6.3 follow-up (2026-10-05): concise catalog/publish/link parameter descriptions are deployed; eight tools and security behavior unchanged. Discovery remains under existing budgets at 7,364 bytes. Glama authenticated health passed after deployment, but indexed descriptions and TDQS have not yet refreshed (admin average 3.1/5). Official Registry metadata still lists 0.6.2 at the same hosted endpoint.

Docker follow-up: isolated reviewer read/write tests are now approved. Docker MCP CLI 0.42.2 returns HTTP 500, provider `shareout`: not found before OAuth begins. PR #5462 now documents this provider-onboarding blocker; authenticated publish/revise/revoke acceptance remains incomplete. PR remains draft pending approval to request maintainer review with the blocker disclosed.

Docker review update (2026-10-05): owner explicitly approved requesting maintainer review before authenticated acceptance. PR #5462 is now open and ready for review (isDraft=false verified). The body discloses the missing OAuth provider and requests onboarding guidance; publish/revise/revoke tests remain blocked.

Docker withdrawal (2026-10-05): owner requested closing the upstream submission. PR #5462 is CLOSED and mergedAt is null, independently verified. Do not reopen or pursue this upstream submission without a new explicit request.

## Gemini, Skills and Cline release — 2026-10-06

Package 0.1.6 adds a Gemini extension manifest with the existing hosted MCP and on-demand skill, plus Gemini and Cline installation instructions. Official portable schemas and Claude strict validation passed. Gemini installed the local extension into isolated settings and listed both the MCP server and skill. Cline installed the skill into a temporary project. The Cline marketplace validator passed with the proposed skill entry (204 entries total). These installation checks do not establish authenticated publishing acceptance in either host. The OpenAI submission remains on 0.1.5 and is not replaced by this release.

Completion: public source 67786c2 publishes package 0.1.6; the `gemini-cli-extension` repository topic was independently verified. Gemini CLI 0.62.0 installed the extension in isolated settings, listed the Shareout skill and MCP server, and reached the expected authentication prompt. No gallery listing or authenticated workflow is claimed. Cline 3.0.68 installed the skill locally; Skills CLI 1.7.0 installed it from the public repository with normal telemetry once. The skills.sh detail page subsequently displayed the real SKILL.md and installation command (previously unavailable); counts and ranking remain unconfirmed. Cline PR #179 is open, not draft, and awaiting review, with full host-test limits disclosed. No Docker submission was reopened.

External-collaboration positioning (2026-10-06): package 0.1.7 and the Cline entry now lead with sharing to clients outside the publisher's AI team, including non-AI users. Viewing and commenting access remain explicitly separate. Cline device login succeeded, but the first inference run returned upstream HTTP 429 for the selected free model after three attempts. No recorded Cline publish/review/revision workflow is claimed. The fictional external-client demo plan is in docs/external-review-demo.md.

Cursor update (2026-10-08): owner shared the Marketplace team's decision declining the submission at this time and recommending cursor.directory. No reason was stated. Cursor Directory explicitly accepts community plugins through its website and detects `.mcp.json` plus `skills/*/SKILL.md` from GitHub. The repository is compatible with those paths; normal sign-in is pending. No directory submission or publication is claimed.

Community scope clarified (2026-10-08): Greg wants community contribution routes. See [the route audit](distribution-community-audit.md). Default to independent directories, ecosystem galleries, open metadata registries and our own repository marketplaces. Cline is an explicitly invited catalog metadata PR, not a core-source change; PR #179 remains open and touches only the skill entry and icon. Docker PR #5462 remains closed and unmerged. Cursor Directory accepted the website submission with MCP, skill and icon, and currently reports a pending security scan with the listing unpublished/hidden. Greg confirmed on 2026-10-08 that the existing OpenAI and Vercel Connect applications should be retained; do not withdraw them. New effort focuses on community discovery. No new curated first-party application or core-repository contribution is in scope.
