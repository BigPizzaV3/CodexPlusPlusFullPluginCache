# AdRoll review preparation

Publication settings, the demo URL, and the five positive and three negative
review cases are imported from `.codex-plugin/plugin.json`. This supporting
file records preparation evidence; it is not a substitute for portal fields.
All positive cases use Data Mode. No widget interaction is required.

## Inclusive end-date fix: deployed and verified

The AdRoll date correction is live on the production reporting backend as of
2026-10-01 UTC, revision `copter-02183-lof`. It was built from the preceding
production image with only `connectors/adroll/adroll_utils.py` replaced. Cloud
Build verified that the preceding file matched the reviewed baseline and ran
the regression test against the patched production image before deployment.
The prior revision remains available for rollback.

The original bug excluded the final day of multi-day requests even though
Adzviser accepts inclusive dates. June 1-30 returned only June 1-29, omitting
June 30's USD 1,522.142213, 76,007 impressions and 60 clicks. The fix converts
every inclusive end date to AdRoll's exclusive end date. Single-day behavior
is preserved.

Local source: `copter/connectors/adroll/adroll_utils.py`.
Regression coverage: `copter/connectors/test_adroll_utils.py`.
All eight summary/daily scenarios pass for multi-day, single-day, year-end,
and leap-day ranges. The six multi-day scenarios failed before the correction.
The isolated regression test mocks the provider and unrelated ORM import.
Production verification below uses actual reporting responses.

Deployment evidence:
- Cloud Build: `edc96d94-41c4-49d2-a3af-19ec94daca1c` (SUCCESS).
- Image: `gcr.io/adzviser-doraemon/copter@sha256:ae5814752de5730c48778f5087f9b66611c7cdd6fa62ebf9bef932c072667bb4`.
- Production traffic: 100% to `copter-02183-lof` at verification.

## Workspace and verification evidence

Use AdRoll Demo, which returned the advertiser WeWork and account currency USD.
The reviewer account must have access to that workspace and its historical
data. No dedicated reviewer credentials or saved portal draft were exercised.
All monetary review metrics explicitly request Cost (USD).

| Check | Status | Evidence and limits |
| --- | --- | --- |
| Workspace and field discovery | Passed | The session connection listed AdRoll Demo and the exact metric and breakdown labels used in the cases. |
| Monthly report data | Passed | June 1-30 returned Cost (USD) 9,945.289656, 396,231 impressions, 459 clicks and 5 conversions. The increase from the preceding response exactly matches the previously missing June 30 contributions. |
| Month comparison data | Passed | One request returned June and July. July returned Cost (USD) 27,899.780713, 1,552,057 impressions, 1,909 clicks and 60 conversions. June matches the independent monthly summary. |
| Campaign report data | Passed | Ten distinct campaign EIDs returned. Spend, impressions, clicks and conversions sum to the corrected June summary. Repeated names are kept separate by EID. |
| Daily trend data | Passed | All 30 dates from June 1 through June 30 returned exactly once, with no July 1 row. All four metric totals match the monthly summary. |
| Ad group report data | Passed | Ten distinct ad group EIDs returned with campaign associations. All four metric totals match the corrected June summary. |
| Single-day regression, live | Passed | June 30 still returns Cost (USD) 1,522.142213, 76,007 impressions, 60 clicks and zero conversions; these match the June 30 daily row. |
| Date regression in production image | Passed | Eight mocked scenarios include the final day and exclude observations outside the requested window. |
| Existing local connector checks | Passed | 113 AdRoll profile/UI tests passed with authentication, reports and widget loading mocked. UI tests are implementation checks, not review cases. |
| Public endpoint | Passed for discovery | Root status and OAuth protected-resource metadata responded with the expected AdRoll endpoint and tools. |
| Full conversational review suite | Not run | Direct data requests do not establish fresh-chat routing, calculations, explanations, or the three negative cases. |
| Portal upload, scan and reviewer sign-in | Not run | These require checks on the saved version and the actual reviewer account. |

An earlier query combining account-currency cost and account-currency revenue
returned headers without data rows. Its cause was not established; that result
does not establish zero activity. The cases use the USD fields that returned rows and passed the corrected
live report checks above.

Live queries used the AdRoll connection exposed to this session. Its runtime
label does not establish a particular installed plugin or portal draft. Recorded
numbers are evidence from those responses, not immutable expected outputs.
All five reporting requests have now been rerun after deployment. The daily
report includes June 30, excludes July 1, and reconciles to the advertiser
summary. The actual five positive and three negative prompts still need to be
run in fresh chats against the saved submission version.

## Demo and publication details

Demo: https://youtu.be/TC-gnBVuStk

Anonymous YouTube checks returned “Adzviser AdRoll ChatGPT Plugin Demo” by
Adzviser, player status OK, a non-private flag, and a 187-second duration. The
video's visual quality and case coverage were not independently watched.

The package uses the supplied 256 x 256 Adzviser icon, existing listing links,
all supported countries, website-only subscription billing, and user-facing
release notes. It contains no reviewer passwords or account email addresses.

## Upload and review

The original ZIP remains in Downloads. This package is named `adzviser-adroll`
and declares the `adroll` server at
`https://adroll.mcp.adzviser.com/widgets/http`. The initial new-entry preparation
has already happened; update that existing AdRoll entry for resubmission.
Preserve its package name and MCP identity. Do not create a duplicate entry to
address the sign-in rejection.

Connect and verify the server, inspect the imported review fields and scan
findings, and provide reviewer access through the portal's secure fields.
The end-date deployment blocker is resolved. Complete the conversational
cases and reviewer-access checks before submitting. Hosted tool annotations
are not controlled by this ZIP; local and live data checks do not establish
OpenAI scan approval.

## Sign-in rejection follow-up: October 26

The later rejection says the reviewer could not complete sign-in/OAuth. The
prior reporting tests and inclusive-date fix do not resolve that finding. The
actual reviewer account, supplied credentials and fresh OAuth completion have
not been verified, so this rejection remains unresolved.

Both public OAuth discovery endpoints currently respond successfully. That only
checks public metadata; it does not test credentials, account activation,
subscription or workspace access, or completion of authorization. Existing
authenticated tool connections also do not establish a fresh reviewer login.

The owner needs to confirm or replace the saved reviewer credentials using a
dedicated, already provisioned demo account, then verify the complete connection
flow in a fresh browser session. The account must access AdRoll Demo and the
historical periods used by the cases without requiring mailbox/phone verification,
a purchase, an account invitation, or data-source setup by the reviewer.
Detailed login instructions and credentials belong in the portal's secure
reviewer-access fields, not in this package. No account or credential changes
were made during this audit.

The shared MCP annotation correction also applies to AdRoll. Production still
serves build `6bf20c8d-20261002201522`, whose inspected build source lacks the
bounded-account openWorldHint correction. Deploy that prepared correction and
rescan as a separate step; it is not a demonstrated fix for the sign-in failure.
