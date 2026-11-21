# Apple Ads submission notes

## Package and reviewer access

- Internal name: `app-6aa605ef1b7c81918376ffde14e66296`.
- Display name: Adzviser Apple Ads. Version: 1.0.0.
- The user confirmed this is an unpublished/rejected submission registered at
  `https://apple-ads.mcp.adzviser.com/widgets/http`.
- The user confirmed reviewer access to **Apple Ads Demo**, containing
  **goPuff - UK**. Reports returned account ID **3069930** and currency **GBP**.
- All supported countries. Subscriptions are purchased on Adzviser's website;
  this plugin does not provide purchases or checkout.
- Reviewer credentials belong only in secure portal fields, never in this ZIP.

The original package identity, version, public name, descriptions and starter
prompts are preserved. The package adds the supplied icon, concrete Apple Ads
MCP declaration, source-specific skills, review cases, demo URL and release notes.
The original downloaded archive was not changed. There is one prepared ZIP.

## Review cases and dynamic dates

Structured review metadata contains five positive Data Mode cases:

1. Total spend.
2. Campaign spend, impressions, taps and tap-through installs.
3. Total installs split into new downloads and redownloads, with attribution checks.
4. Top five keywords by tap-through installs, including spend and taps.
5. Spend and total-install comparison against the preceding period.

Three negative cases cover campaign/budget changes, keyword/bid creation, and
unconnected competitor-account access. The expected response explains the tool
boundary without fabricating actions or querying unrelated private data.
No UI-widget case is required.

Use current local date D: recent 30 days are [D-31, D-2]; preceding 30 days
are [D-61, D-32], inclusive. Resolve these dates anew at review time. All numerical
answers must come from live rows; historical observations below are not fixed
expected answers. The current local date was **2026-10-26 in America/Los_Angeles**
during preparation, although discovery had already advanced to October 27 UTC.

## Direct-query evidence

Workspace and field discovery succeeded. All five requests used supported
catalog fields and returned model-visible AppleAds rows with directData=true,
reportingMode=data and an empty note_of_assumption. No preview or preference
control was invoked. Recent dates were **2026-09-25 through 2026-10-24**;
preceding dates were **2026-08-26 through 2026-09-24**.

| Case | Direct-query result | Checks |
| --- | --- | --- |
| Spend | Passed | Account returned GBP 9,367.9486; display GBP 9,367.95. |
| Campaign performance | Passed | 26 campaign rows, 3 with activity. Totals: GBP 9,367.9486, 27,610 impressions, 6,209 taps, 4,790 tap-through installs. Spend matches Account. |
| Install breakdown | Passed | 15,160 total installs = 4,790 tap-through + 10,370 view-through = 7,623 new downloads + 7,537 redownloads. |
| Keyword ranking | Passed | 1,211 keyword rows. Totals: 6,209 taps and 4,790 tap-through installs, matching Campaigns; spend GBP 9,367.9487, within GBP 0.01 of the account total. |
| Period comparison | Passed | Recent GBP 9,367.9486 / 15,160 total installs; preceding GBP 6,937.6887 / 11,829. Spend +35.03%; total installs +28.16%. |

The five leading keyword rows by tap-through installs were: go puff (4,466),
zapp (92), gopuff (68), food delivery (43), and getir (41). Rank by the actual
returned data at review time, preserving campaign, ad-group and keyword IDs.
Names alone are not identity. The GBP 0.0001 difference between keyword and
account spend is below displayed currency precision; its precise cause was not
independently established and the reports were not altered to force equality.

Validation checked table shape, date segments, field support, nonnegative finite
metrics, stable keyword identities, spend reconciliation and install identities.
It did not compare every value with Apple's dashboard or directly audit Apple's
attribution pipeline. These are direct request checks through the connected
Apple Ads service, not saved-version ChatGPT conversations or reviewer-login tests.

Saved-plugin positive conversations, the three negative conversations, imported
portal metadata, final scan and reviewer sign-in: **Not run**. Do not present
these remaining checks as passed merely because direct reporting succeeded.

## Reporting semantics and tool annotations

The connector maps Installs to tapInstalls and Total installs to totalInstalls.
Total new downloads and Total re-downloads use the corresponding total fields.
[Apple's dashboard documentation](https://ads.apple.com/app-store/help/reporting/0024-view-campaigns-dashboard-metrics)
separates tap-through, view-through and total install reporting. The skills keep
those definitions distinct and avoid adding overlapping attribution components.
Cost is already in account currency units. Aggregated rates require their
component metrics; the skill requests those counts and avoids averaging rates.

Inspected local tool definitions contain explicit boolean annotations:

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| list_metrics_and_breakdowns_apple_ads | true | false | true | false |
| retrieve_reporting_data | false | false | false | true |
| preview_and_retrieve_reporting_data | false | false | false | true |
| list_workspace | false | false | true | true |
| set_reporting_mode | false | false | true | false |

Catalog discovery reads static definitions without external effects. Retrieval
reads authorized Apple Ads reports and records usage; the connector may also
refresh its authorization cache. It does not edit campaigns or bids. Repeated
report calls can record more usage, so reporting is not annotated idempotent.
Preview compatibility paths can run reports or save presentation preferences.
Workspace lookup can clear stale account preferences; mode selection saves a
presentation preference. Those operations are non-destructive. External report
and account access use openWorldHint=true with authorization still limiting
accounts. The local preference control uses openWorldHint=false. Static catalog
reads, workspace normalization and setting the same preference are idempotent.

Anonymous initialize and tools/list checks returned expected OAuth 401 challenges
with the Apple Ads resource metadata URL. Saved portal tool descriptors were not
captured or compared. Packaged notes do not override deployed annotations, and
no MCP or Copter server code, configuration or deployment was changed.

## Demo and handoff

Demo: https://youtu.be/xn-d2xBmwSg

Anonymous metadata identified “Adzviser Apple Ads ChatGPT Plugin Demo” by Adzviser,
approximately 163 seconds, non-private with player status OK. An isolated signed-out
browser played the opening; an inspected frame around 48 seconds showed ChatGPT's
plugin directory. Playback stopped around 60 seconds with a YouTube player error.
Full playback, coverage of the cases and absence of sensitive content throughout
remain unverified. Check the full recording before review. This browser failure
alone does not establish that the hosted video is broken.

The unchanged website, support, privacy and terms URLs were opened anonymously
and inspected earlier on October 26 during Salesforce preparation. The supplied
256-pixel Adzviser PNG was inspected and reused. Release notes describe reporting
features users can use, rather than submission mechanics.

After uploading to the intended original entry, inspect imported review information,
connect and scan the MCP, verify reviewer sign-in, and run the cases through the
saved version. Complete the full-video check and required portal attestations
before submission. No portal upload, submission, publication or deletion was performed.
