# ActiveCampaign submission preparation

## Package and confirmed access details

- Internal name: `app-6aa3b70df09481919a89339083735c48`; version: **1.0.0**.
- Display name: **Adzviser ActiveCampaign**. Publisher: Adzviser LLC.
- Verified reachable MCP endpoint with an OAuth challenge:
  `https://activecampaign.mcp.adzviser.com/widgets/http`.
- Connected workspace and account: **ActiveCampaign Demo**.
- The user confirmed the existing entry is unpublished/rejected, the registered
  endpoint is exactly the URL above, and the reviewer login has access to
  **ActiveCampaign Demo**. Fresh reviewer OAuth still needs to be tested;
  confirmation of access is not an end-to-end sign-in test.
- All supported countries. Subscriptions are purchased separately on Adzviser's
  website; this plugin does not provide purchases or checkout.
- Reviewer credentials belong only in secure portal fields, never this ZIP.

The original package ID, version, display name and subtitle are preserved. The
package includes the Adzviser icon, concrete MCP configuration, source-specific
skills, five positive Data Mode cases, three negative cases, the supplied demo
URL, annotation explanations and user-facing release notes. The original
downloaded ZIP is intact. The listing describes supported email reporting
without promising list-level breakdowns or historical contact growth.

## Five positive cases

1. Overall sends, unique opens, unique subscriber clicks, open rate and click rate.
2. Sends, unique opens and unique subscriber clicks by campaign ID and name.
3. Hard bounces, soft bounces, total bounces, unsubscribes and unsubscribe rate.
4. Up to five campaigns ranked by click rate, with sends and subscriber clicks.
5. Performance compared with campaigns sent in the preceding 30-day window.

Use a fresh Data Mode conversation for each. Let D be today's date in the user's
timezone. Recent 30 days are [D-31,D-2], and the preceding 30 days are [D-61,D-32],
inclusive. Recalculate at review time. Numerical answers and calendar dates are
not hardcoded into the review cases. No UI-widget review case is included.

Dates select campaigns using the send-date field's calendar date returned by
ActiveCampaign. Metrics are the selected campaigns' current cumulative counters,
not engagement events restricted to the calendar window. Unique counts are
unique within each campaign, not globally deduplicated people across campaigns.
Rates must be recomputed from count totals rather than averaged across campaigns.
If Sends is zero, rates are undefined even if the tool formats them as 0.00%.

Three negative cases cover sending a promotional email, deleting contacts and
disabling automations, and accessing an unconnected competitor's private data.
Explain these limits without invoking reporting tools to simulate changes.

## Direct-query evidence

Checked on **October 26, 2026, America/Los_Angeles**. Workspace and field-catalog
discovery succeeded. All five report calls returned model-visible data with
`directData=true`, `reportingMode=data` and no field assumptions. Recent dates
were **September 25–October 24, 2026**; earlier dates were **August 26–September 24**.

| Case | Observed response and consistency check | Result |
| --- | --- | --- |
| Overall engagement | 17,315 sends, 8,400 unique opens, 448 unique subscriber clicks; open rate 48.51% and click rate 2.59% match their count ratios after rounding. | Passed direct-query checks |
| Campaign breakdown | Two distinct campaign IDs; their sends, opens and clicks sum to the overall values. | Passed direct-query checks |
| Bounces and unsubscribes | 529 hard and 81 soft bounces sum to 610 total; 392 unsubscribes divided by 17,315 sends rounds to 2.26%. | Passed direct-query checks |
| Click-rate ranking | Two eligible campaigns, with reported click rates 2.74% and 2.16%; both reconcile with counts. Returning only two is correct. | Passed direct-query checks |
| Period comparison | Recent row matches overall engagement. Earlier counts are zero; percentage growth and earlier rates are undefined. | Passed direct-query checks |

These are dated observations, not fixed expected answers. They verify direct
tool execution and internal consistency, not an independent audit against the
ActiveCampaign administration console. Fresh conversations against the saved
submission, including the three negative cases, have **not been run**.
No ActiveCampaign backend change was needed for these five report requests.

Current count-only contact, deal, account and campaign paths return account-wide
counts rather than applying the date range. The selected campaign cases request
performance measures that fetch and filter campaigns; they do not rely on those
count-only paths. The bundled skill explains the distinction for other questions.

## Annotations and deployment

The shared local MCP correction from preceding connector work sets
`openWorldHint=false` for account-bound reporting and workspace discovery.
ActiveCampaign uses that shared profile. Public-source reporting retains true.
See [tool annotations](tool-annotations.md) for explicit values and explanations
for all five tools.

The shared correction has **not been deployed as part of this preparation**.
The ZIP does not deploy the server or override its annotations. If deployment
is still pending, deploy that correction, rescan the existing MCP connection,
and compare its scanned definitions with these documented values. Enter any
required justification in the portal. This is separate from the successful
reporting queries; no ActiveCampaign-specific Copter deployment is needed for them.

## Listing links and demo

The four Adzviser listing destinations were inspected anonymously earlier on
October 26: website, support contact form, privacy policy and terms. The checks
confirmed the intended accessible destinations, not legal compliance. The
supplied 256×256 PNG logo is included.

Demo: https://youtu.be/sFDedbJiF-8

YouTube identifies this as **Adzviser ActiveCampaign ChatGPT Plugin Demo** by
Adzviser, approximately 208 seconds long and accessible without signing in.
An isolated browser played sampled segments through the final reporting result.
Inspected frames show the source-specific endpoint, an open-rate question, an
empty-period response and a later response with sends, unique opens and an open
rate. The recording demonstrates reporting but not all five packaged cases.
Uninterrupted playback hit a YouTube player error, so continuous full playback
was not verified. No credentials were observed in the sampled frames; this was
not a frame-by-frame secrets audit.

Around **1:54**, the recording shows a warning that not all requested permissions
were granted and some actions may require reconnecting. Later report queries
complete. This historical warning does not establish a current authentication
failure. Rehearse fresh reviewer sign-in and resolve the warning if it persists;
update the recording to show a clean connection and the review cases before
final review.

## Remaining portal checks

The registered URL, submission status and reviewer workspace are user-confirmed.
Preserve the original entry and MCP binding; do not delete or duplicate the
plugin to work around a connection error. Check imported review metadata and
the final MCP scan on the exact saved version.

Successful calls through the existing authenticated connection do not verify
a new reviewer's sign-in, consent or callback flow. Test the complete flow with
the credentials entered in secure portal fields, ensuring access to the stated
workspace without additional registration, verification or account setup.

Fresh reviewer OAuth, saved-version positive/negative conversations, imported
review metadata, final scan and required attestations: **Not run / incomplete**.
No portal upload, submission, publication, account mutation or deletion was performed.
