# GearGenius FlatRate Pro plugin package

GearGenius FlatRate Pro is developed and maintained by **Smarter Way to Apply
Technologies** ([smarterwaytoapply.com](https://smarterwaytoapply.com)).

This portable Agent Plugins package connects ChatGPT to the hosted FlatRate Pro
MCP server at `https://geargenius.ai/mcp`. OAuth discovery is served by
`https://geargenius.ai/.well-known/oauth-protected-resource`. The MCP server
implements an OAuth authorization-code flow with PKCE; this package does not
embed user credentials or use the REST `X-User-Token` header.

The public connection guide is `https://geargenius.ai/mcp-server-setup.html`.
The technician web flow is MCP-only: the earlier connection/setup URLs redirect
there, and in-app Settings/Integrations no longer create manual connection keys.
Existing backend handlers and credentials remain for internal dispatch and
legacy compatibility; older access is not automatically revoked by this UI change.

Production was deployed and anonymously probed on 2026-10-31. OAuth discovery,
MCP Apps initialization, all three report tools, and the embedded resource
passed checks. An unauthenticated protected-tool call returns HTTP 401 with
the required HTTP `WWW-Authenticate` challenge. The deployed `getUserProfile`
description is minimized and no longer includes subscription/first-call guidance.
The dedicated synthetic reviewer account subsequently passed email/password
sign-in, an OAuth authorization-code/PKCE exchange, the 18-tool listing, all
three authenticated reports, recent jobs, inventory, and exact-date search.
Actual ChatGPT/Claude rendering and portal validation still remain required;
these protocol checks do not establish OpenAI approval.

The review cases in `plugin.json` are drafts. Before submitting, run them with a
dedicated test account, add the reviewer sign-in details in the OpenAI portal,
and confirm the supplied recording demonstrates the submitted cases. Do not put credentials in
this package.

The submission listing includes job-history search by title, vehicle, and date;
read access to complete toolbox records; and updates for toolbox items and job
logs. These capabilities are served by the hosted MCP endpoint, so deploy and
verify the matching server tool definitions before portal submission.

The job/toolbox release was deployed and anonymously verified on 2026-10-31:
all 18 technician tools, expanded search/update schemas, protected read/write
OAuth challenges, REST health, and corrected OpenAPI paths passed live checks.
Array-backed toolbox updates and partial vehicle edits have local regression
coverage. These checks do not validate a connected-account ChatGPT session.

Submission also requires the publisher to verify the domain and identity,
connect the MCP server through the OpenAI portal, complete its tool scan, and
submit the required policy attestations. Those portal actions are not performed
by this repository package.

## Mobile and upload boundary

FRP and its active supporting web apps are mobile-optimized. Web uploads share
100 MB (104,857,600 bytes) per account, with a 5 MB per-file maximum and
platform-admin overrides. Uploads go through authenticated quota callables;
direct Storage writes stay denied. The owner accepted a temporary possibility
that pre-cutover sessions can bypass the limit until 2026-11-08T02:14:46.814Z.
Late finalized files are preserved and charged; over-limit accounts cannot
continue controlled uploads once accounted.

This package does not expose file-upload or quota-administration MCP tools.
Use FRP for photos and platform Admin for overrides. No manual token or direct
Storage fallback is introduced. ShopOS stays disabled. The hosted OAuth server,
18 technician tools, and existing report semantics are unchanged.

## Visual reports

The repository server adds `showEarningsReport`, `showAnalyticsReport`, and
`showPortfolioReport`. These read-scoped tools return account-backed completed
work reports and attach a self-contained MCP Apps HTML/JavaScript card. The
server serves that card over `resources/read`; it is not an HTML upload or a
separate unauthenticated report URL, and no account data is stored in this ZIP.

Reporting windows are rolling 7, 30, or 365 calendar days including today, in
UTC. Earnings use the current saved hourly rate and are estimated gross pay,
not payroll or take-home pay. Missing rates or timing remain unavailable.
Portfolios show up to 20 recent completed jobs and recorded verification flags,
not certificates. Contact fields, VINs, notes, and attachments are excluded.
See the repository's `docs/api/MCP_SERVER_SETUP.md` for the full data contract,
calculation rules, and validation commands.

The automated sandbox-browser tests use synthetic data. Version 1.2.0 packages
exactly five positive and three negative review cases in
`extensions.com.openai.review.test_cases` in [plugin.json](plugin.json).
The five positive journeys cover all 18 exposed technician tools: visual
reports; account context, history and guidance; a sample job lifecycle; a sample
toolbox lifecycle; and notes/timers. Cases include sample-data preconditions,
observable outcomes, write confirmations, and real returned IDs rather than
an assumed `job_abc123`. Run every case with the dedicated reviewer account;
local tests do not establish a successful ChatGPT run or portal approval.

## Bundled workflow skills

Version 1.2.0 includes four focused skills in the portable root `skills/`
directory, each with `SKILL.md` and an `agents/openai.yaml` dependency on the
same hosted MCP server:

- [Technician work reports](skills/technician-work-reports/SKILL.md): requested
  earnings, analytics, and completed-work portfolios with report limitations.
- [Structured job log](skills/structured-job-log/SKILL.md): scoped retrieval,
  explicit creation, and uniquely identified partial/status updates.
- [Toolbox records](skills/toolbox-records/SKILL.md): own-account inventory,
  explicit tool logging, and targeted condition/status/location edits.
- [Repair reference](skills/repair-reference/SKILL.md): tool-backed labor and
  DTC reference, without invented diagnoses or unsafe procedural advice.

Skills do not supply authentication, broaden permissions, execute purchases,
or replace backend safeguards. Their descriptions and workflow boundaries are
locally checked; test activation and output in the client, and wait for the
portal's required skill scans before submitting. The portable schema discovers
root `skills/`; do not add a Codex-only root `skills` field to `plugin.json`.

## Dedicated demo reviewer access

A separate personal-technician account was provisioned with eight synthetic
jobs, two tools, and a sample note. Six completed jobs populate current reports;
a historical front-brake fixture supports the February 10, 2025 search, and
an editable pending fixture supports write tests. No active timer, organization
membership, elevated role, real customer data, or payment access was added.

The generated login details and secure-form instructions are stored outside
the repository at `%LOCALAPPDATA%\GearGenius\reviewer-access\openai-demo-credentials.json`
in a directory restricted to the local user and SYSTEM. That file is not in
Git, Hosting, the skills, or the submission ZIP. Copy its credentials only
into OpenAI's secure reviewer access form. Keep the account available for
subsequent reviews; do not reset its password or erase reviewer-created jobs
without updating the private portal details. Report fixtures use rolling dates;
refresh sample data before a later submission if current report windows expire.

## Submission checklist (checked against OpenAI on 2026-10-31)

Canonical sources:
[submission flow and review fields](https://developers.openai.com/plugins/deploy/submission/),
[plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines/),
and [portable packaging](https://developers.openai.com/plugins/build/plugins/).
The earlier Apps SDK submission URLs redirect to these plugin docs.

| Requirement | Repository support / remaining gate |
| --- | --- |
| Complete portable ZIP with root `plugin.json`, `mcp.json`, local logo, and skills | Use [the regenerated draft ZIP](../geargenius-flatrate-pro-draft.zip), version 1.2.0; do not upload an older archive. |
| Accurate listing, three starter prompts, public website/support/privacy/terms | Declared in the manifest. Verify publisher consistency and the privacy policy's data categories, purposes, recipients, retention, and user controls before attesting. |
| Verified developer identity | Complete individual/business verification in organization settings and choose that identity in the portal. Not established by repository files. |
| Domain ownership | The clipboard challenge is served at `https://geargenius.ai/.well-known/openai-apps-challenge`. Select Verify in the portal after publishing and checking the response. Hosting the token is not itself portal acceptance. |
| One connected hosted MCP with supported authentication | HTTPS endpoint and OAuth discovery exist. Complete the connected-account OAuth flow, wait for the tool scan, and resolve required setup/validation errors. Do not embed tokens or client secrets in the ZIP. |
| Exactly five positive and three negative initial-review cases | Included in the documented import shape. Run all eight on sample data, desktop and mobile, including embedded cards. Imported cases are read-only; change the package and upload a new version to update them. |
| Immediately usable reviewer account | Dedicated sample technician account and protocol sign-in checks completed. Enter the restricted local credentials and instructions only in secure portal Review details. No MFA, email/SMS codes, magic links, or private-network dependency is configured. Maintain the account and sample data for later reviews. |
| Accessible video walkthrough | The supplied [GearGenius tutorial](https://www.youtube.com/watch?v=M_Ng7IxOGvc&t=45s) is included in `review.demo_recording_url`. Its public page and YouTube metadata are reachable. Confirm that it demonstrates the actual ChatGPT integration and all submitted cases; reachability alone does not establish coverage. |
| Release notes | Included in `publication.release_notes`; describe review-material changes, not an unverified approval. |
| Accurate tool schemas, boolean safety annotations, scoped data, explicit errors | Existing tool registry and local tests support these. Confirm the scanned production tool list matches the package and test retry/write safeguards in ChatGPT. |
| Embedded UI reliability and privacy | Test the cards in actual ChatGPT on desktop/mobile. Review CSP and any iframe-domain declarations/justifications if embeds change. Synthetic browser tests alone are insufficient. |
| Policy/commerce attestations and availability | Confirm policies in the portal; no commerce is declared. Review country availability and translations as applicable. Omitted country targeting preserves saved settings. |
| Approval and publication | Submit the selected draft only after the gates above; approval does not auto-publish. Publish the approved version explicitly. |

### Domain challenge hosting

OpenAI requires only the exact token as plain text at the challenge URL shown
in the portal, on the MCP hostname or an eligible parent HTTPS origin. Confirm
that the portal's challenge base is `https://geargenius.ai` for this draft.
Do not substitute a DNS TXT record, JSON document, or a list of tokens.

Firebase excludes hidden directories with `**/.*`. To preserve that exclusion,
an exact Hosting rewrite maps `/.well-known/openai-apps-challenge` to
[the public challenge text](../../assets/openai-apps-challenge.txt).
The route precedes the SPA fallback and sets `text/plain` and `no-store`.
This is a public ownership challenge, not an API key or login credential.
Do not replace a token used by another plugin at the same URL; choose an
eligible parent origin or distinct hostname if necessary.

Hosting was deployed on 2026-10-31 using `npm run deploy:hosting`; its release
gates, FRP type-check, 270 FRP tests, and production build passed. The live
challenge returned HTTP 200, `text/plain; charset=utf-8`, `no-store, max-age=0`,
and exactly the 43 token bytes, with no newline or SPA HTML. OpenAI's portal
Verify action still requires sign-in and has not been completed here.

### Local validation and package refresh

Run `node --test functions/__tests__/mcp-plugin-package.test.js scripts/validate-release.test.js`
from the repository root. This checks the exact counts, all advertised tool
names, import fields, and the challenge route while preserving hidden-file
exclusions. It does not execute the reviewer journeys on a connected account.

From the repository root, run `powershell -NoProfile -File scripts\package-openai-plugin.ps1`,
then run the validation command above. The builder includes root-level
`plugin.json`, `mcp.json`, `README.md`, `assets/frp-logo.svg`, and the eight skill
instruction/dependency files, excluding
credentials and the domain challenge. It explicitly uses forward slashes in
ZIP member names: Windows `Compress-Archive` can write backslashes that OpenAI
rejects as unsafe paths. The regression test reads the actual archive names
and checks every member against the current source bytes.
In the portal, select **Upload new version**,
then inspect **Metadata & Skills → Review information → Review details** to
confirm all eight imported cases. Save private access details and the recording
URL separately. The accessible browser currently requires OpenAI sign-in, so
portal imports, domain acceptance, and account testing remain unverified.

The supplied recording is titled **How to Log a Job in FlatRate Pro |
GearGenius.AI Tutorial**. Its 45-second start offset is preserved exactly as
provided. The title identifies a job-logging tutorial, not proof of the full
five-positive/three-negative MCP review walkthrough. Review its content and
supplement or replace it if it does not demonstrate those cases in ChatGPT.
