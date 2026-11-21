# Matomo submission preparation

Prepared on October 26, 2026. Original package identity
`app-6aa3b88a88448191aa62347ff93cc15e`, version `1.0.0`, public name
`Adzviser Matomo`, subtitle, and starter prompts are preserved. The original
downloaded ZIP remains in Downloads. No submission was created, uploaded,
submitted, published, or deleted during this preparation.

The owner confirmed that the existing entry is unpublished/rejected and that
its registered MCP URL is https://matomo.mcp.adzviser.com/widgets/http. The owner
also confirmed reviewer access to `Matomo Demo Good`, containing `docusnap.com`.

## Package contents

The portable root manifest and compatibility manifest have matching identity,
version, listing, publication, and review metadata. The concrete MCP endpoint
is declared in `mcp.json` and both skill dependencies. The generic skills are
specialized to Matomo with exact field discovery, report-family selection,
segmented response parsing, date handling, and interpretation limits.

The package contains the supplied 256-pixel Adzviser icon, five positive Data
Mode cases, three negative cases, the demo URL, all supported countries,
website-only subscription information, and user-facing release notes. Preview
UI remains available on explicit request; no review case requires a widget.
No credentials, private app bindings, or unrelated files are included.

## Five positive prompts

1. Show Matomo visits, actions, and bounce rate for the 30 days ending two days ago in Matomo Demo Good.
2. Show Matomo visits by device type for the 30 days ending two days ago in Matomo Demo Good. Include only devices with visits.
3. Which channels brought visits to our site in the 30 days ending two days ago in Matomo Demo Good?
4. Compare Matomo visits and actions for the 30 days ending two days ago with the preceding 30 days in Matomo Demo Good.
5. Show daily Matomo visits and actions for the 30 days ending two days ago in Matomo Demo Good.

Let D be the current date in the user's timezone. Recent means [D-31, D-2],
inclusive; preceding means [D-61, D-32]. Recalculate dates at review time. Cases
contain no fixed dates or numeric answers. The local preparation date was
October 26 in America/Los_Angeles; discovery reported October 27 UTC. The local
date was used consistently for these checks.

## Direct-tool verification

Workspace and field discovery succeeded. All five selected underlying queries
passed through the authenticated Matomo connection available in this session.
Recent dates were September 25–October 24, 2026. Comparison dates were
August 26–September 24. Responses had `isError=false`, `directData=true`,
`reportingMode=data`, and empty `note_of_assumption`.

| Case | Status | Observed evidence |
| --- | --- | --- |
| Overall traffic and bounce rate | Passed | 19,655 Visits, 44,471 Actions, and 13,385 Bounces. Bounces divided by Visits gives approximately 68.10%. Actions were not relabeled as pageviews. |
| Devices | Passed | Fifteen returned categories, five with visits: Desktop 15,092; Smartphone 4,191; Phablet 199; Tablet 159; unknown 14. All categories summed to 19,655 visits. The prompt asks to display only categories with visits. |
| Channels | Passed | Six nonzero categories: direct 9,260; search engines 5,008; campaigns 4,458; referring websites 821; AI assistants 74; social networks 34. They summed exactly to 19,655 visits. Original source labels were in German. |
| Period comparison | Passed | Previous: 18,034 Visits and 37,383 Actions. Recent increases: 1,621 Visits (+8.99%) and 7,088 Actions (+18.96%). The recent row matched the standalone report. |
| Daily activity | Passed | All 30 requested dates returned rows. Daily Visits summed to 19,655 and daily Actions to 44,471, exactly matching the overall report. |

These numbers are observations from one verification, not expected future
answers. Keep the connected review site available and populated during review.
Source completeness against the Matomo console was not independently audited.
The returned report structure contains named tables (Combined, Device, Channel,
VisitorOverview); the skills explicitly handle this structure.

Fresh natural-language conversations through the saved submission: **Not run**.
Direct queries establish execution and numerical consistency, not every step
of a fresh saved-plugin conversation. No widget was opened during these checks.

The three negative conversations are **Not run**. They cover installing tracking
code, deleting recorded visits, and identifying visitors by name/email. Each
expects a clear explanation of the unsupported action without unnecessary tool
calls or claims of completion.

## Additional country-report limitation

A separate probe requested Location visits with Country for the same recent
interval. It returned 100 country rows totaling 19,612 visits, which is 43 fewer
than the overview, device, channel, and daily total of 19,655. This is not a
verified complete country distribution. A row limit is a possible explanation;
the exact cause was not established against the source account.

The five review cases use the verified complete device distribution instead.
This does not fix or hide the country-report limitation: the skills instruct the
model to disclose incomplete dimension coverage and never invent missing rows or
claim a partial subtotal is the site total. No connector implementation change
was made. Do not describe the country report as fully reconciled.

## Tool annotations and deployment

The local scoped connector sets explicit boolean annotations:

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| list_metrics_and_breakdowns_matomo | true | false | true | false |
| retrieve_reporting_data | false | false | false | false |
| preview_and_retrieve_reporting_data | false | false | false | false |
| list_workspace | false | false | true | false |
| set_reporting_mode | false | false | true | false |

The catalog reads static field definitions. Retrieval reads the authorized
Matomo site's reporting APIs and records Adzviser usage. Repeating retrieval
can record additional usage, explaining the false read-only and idempotent
hints; it does not edit tracking or delete analytics. Preview compatibility
paths can run reporting or save presentation preferences. Workspace resolution
can clear a stale account preference, and mode selection saves a presentation
preference. Repeating the same preference operation is idempotent. These tools
operate within authorized accounts or local definitions, so scoped open-world
hints are false. External hosting alone does not make that scope open-ended.

**The shared annotation correction still needs deployment and a portal rescan.**
The public Matomo endpoint reported build `6bf20c8d-20261002201522` on October 26.
Earlier inspection of that deployed build's source established that it predates
the local scoped open-world correction; its reporting and workspace definitions
still use true. The ZIP cannot change server annotations. No deployment was
performed. The two existing connector suites passed all 113 Matomo-specific
checks locally; that does not establish production deployment or a saved scan.

The public endpoint and OAuth discovery responded successfully. Anonymous MCP
initialization returned an expected 401 challenge for the same resource.
Fresh reviewer sign-in and the saved submission scan: **Not run**. Working
authenticated queries do not verify the credentials saved for a reviewer.

## Demo and listing checks

Demo: [Adzviser Matomo ChatGPT Plugin Demo](https://youtu.be/4laL_BwtqQc).
YouTube identified a non-private recording by Adzviser, approximately 169 seconds.
An isolated signed-out browser played the beginning, middle, and ending in
separate runs. Inspected frames show plugin setup, an OAuth return, a natural
language reporting prompt, and a numerical response at about 2:40 for
`docusnap.com` in `Matomo Demo Good`. The recorded response describes page visits
summed across reported pages, which is distinct from overall site Visits in the
new cases. The final playback run reached the video's end.

The recording demonstrates an existing reporting workflow, not all five new
cases or their negative cases. The first two playback runs encountered YouTube
player errors after approximately one minute; timestamped restarts verified the
middle and ending. Uninterrupted playback and every frame were not verified.
The browser address bar briefly shows OAuth callback query parameters. The
recording's historic authentication flow does not prove current reviewer login.

The icon was visually checked earlier in this session and reused
unchanged. The four unchanged listing URLs were opened anonymously and inspected
earlier in this session: [website](https://adzviser.com),
[support](https://adzviser.com/contact-us),
[privacy](https://docs.adzviser.com/privacy), and
[terms](https://docs.adzviser.com/terms). They identify Adzviser and provide the
expected public content. Publication countries and website-only billing reuse
the owner's confirmed preferences.

## Portal handoff

Use the archive for the existing Matomo entry. Its package identity, version,
and confirmed endpoint are preserved. Do not create another plugin or change
its identity to work around an upload error without inspecting that error.

After an accepted upload and deployment of the shared annotation correction,
rescan tools, inspect saved boolean annotations, and verify imported review
metadata. Supply working reviewer credentials and detailed sign-in instructions
only through the secure dashboard fields. Verify a fresh login reaches the
intended workspace without additional setup or verification, then run the cases
through the saved version and complete the required attestations.

No specific Matomo rejection details were provided. A valid ZIP cannot guarantee
approval or complete reviewer authentication, domain/developer verification,
tool scans, or attestations.
