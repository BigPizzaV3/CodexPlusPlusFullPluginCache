# Zoho CRM submission preparation

## Package and pending access confirmation

- Internal name: `app-6aa3b9ffa72c81919c22315dc53856a1`; version: **1.0.0**.
- Display name: **Adzviser Zoho CRM**. Publisher: Adzviser LLC.
- MCP endpoint verified reachable with an OAuth challenge:
  `https://zoho-crm.mcp.adzviser.com/widgets/http`.
- Connected workspace: **Zoho CRM**, containing the **Adzviser LLC** account.
- We are awaiting the user to confirm that the existing submission is
  unpublished/rejected, this is its registered endpoint, and the intended
  reviewer login has access to this test workspace. Do not infer these portal
  facts from the existing authenticated tool connection.
- All supported countries. Subscriptions are purchased separately on Adzviser's
  website. The plugin has no purchase or checkout feature.
- Supply reviewer credentials only through secure portal fields, never this ZIP.

The original package ID, version, display name and subtitle are preserved. The
ZIP includes the Adzviser icon, concrete MCP configuration, source-specific
skills, five positive Data Mode cases, three negative cases, the supplied demo
link and user-facing release notes. The original downloaded ZIP is unchanged.
The listing now describes creation-date filtering and current field values;
it does not promise historical stage changes or closing-date reporting.

## Five positive cases

1. Counts of accounts, contacts, deals and leads created in the period.
2. Leads created in the period grouped by their current lead status.
3. Deals created in the period grouped by their current stage.
4. Contacts created in the period grouped by recorded lead source.
5. Accounts created in the period grouped by industry.

Each uses a fresh Data Mode conversation and a two-calendar-year window ending
two days before the current date. Let D be today's date in the user's timezone,
E=D-2 days, and S=the day after E shifted back two years (clamp February 29 to
February 28 if necessary). Request [S,E], inclusive. Recalculate at review time.
No numerical answer or fixed calendar date is hardcoded in the review cases.

The connected records were created in 2025; the checked 2026 windows returned
zero counts. The longer window deliberately exercises existing test records.
It must not be silently replaced with a recent window. As these records age,
maintain suitable test data or revise the review setup.

Dates select records by the calendar date in Zoho's `Created_Time`. Statuses,
stages and other fields are current values, not historical values as of E.
Accounts means CRM company records. Keep module counts separate; the connector
does not join modules or establish funnel conversion rates. No names, emails,
phone numbers, addresses, monetary values or currency assumptions are needed.

Three negative cases cover creating a lead, changing deal stages/amounts, and
accessing an unconnected competitor's private CRM. Explain those limits without
calling reporting tools to simulate writes or inventing private data.
No UI-widget review case is included.

## Direct-query evidence

Checked on **October 26, 2026, America/Los_Angeles**. Workspace and field-catalog
discovery succeeded. All five report calls returned model-visible data with
`directData=true`, `reportingMode=data` and no field assumptions. The requested
inclusive dates were **October 25, 2024–October 24, 2026**.

| Case | Observed response and consistency check | Result |
| --- | --- | --- |
| Module totals | 10 accounts, 10 contacts, 10 deals and 10 leads, kept as separate counts. | Passed direct-query checks |
| Lead statuses | Six status groups; counts sum to the overall 10 leads. | Passed direct-query checks |
| Deal stages | Eight stage groups; counts sum to the overall 10 deals. | Passed direct-query checks |
| Contact lead sources | Nine source groups; counts sum to the overall 10 contacts. | Passed direct-query checks |
| Account industries | Eight industry groups; counts sum to the overall 10 accounts. | Passed direct-query checks |

These are dated preparation observations, not fixed expected answers. They
verify direct tool execution and internal consistency, not an independent audit
against the Zoho administration console. Fresh conversations against the saved
submission, including the three negative cases, have **not been run**.
No Zoho CRM backend change was needed for these five report requests.

## MCP annotations and deployment

The shared local MCP correction prepared during preceding connector work sets
`openWorldHint=false` for account-bound reporting and workspace discovery.
Zoho CRM uses that shared profile. Public-source reporting retains true.
See [tool annotations](tool-annotations.md) for all five tools' explicit flags
and behavior-based explanations.

The shared correction has **not been deployed as part of this preparation**.
The ZIP does not deploy the MCP server, and packaged explanations do not override
tool definitions. Deploy the shared annotation correction if it is still pending,
then rescan and compare the actual scanned flags with the documented values.
Supply any required portal justifications. This is separate from the five
successful reporting queries; no Zoho-specific Copter deployment is required
for those queries.

## Listing links and demo

The package reuses the four Adzviser listing destinations inspected anonymously
earlier on October 26: the service website, support contact form, privacy policy
and terms. Those checks verified the intended destinations, not legal compliance.
The supplied 256×256 PNG logo is included.

Demo: https://youtu.be/wGPiXuxj10A

YouTube identifies this as **Adzviser Zoho CRM ChatGPT Plugin Demo** by Adzviser,
approximately 146 seconds long and accessible without signing in. An isolated
browser played sampled segments through the end. Inspected frames show the
source-specific MCP connection, a lead-count prompt and a completed response
reporting 10 leads for 2025 in the Zoho CRM workspace. The video demonstrates
basic Data Mode reporting; it does not demonstrate all five packaged cases.
An uninterrupted playback attempt hit a YouTube player error, so continuous
full playback was not verified. No credentials were observed in sampled frames;
this was not a frame-by-frame secrets audit.

Around **1:33**, the recording shows a warning that not all requested permissions
were granted and some actions may require reconnecting. The later lead query
does complete. This does not prove the current service is broken, but it is not
clean evidence of complete reviewer access. Rehearse a fresh reviewer sign-in;
resolve any warning that still appears and update the recording to show a clean
connection and the review cases before final review.

## Remaining portal checks

After registration and reviewer-workspace confirmation, verify the exact saved
draft's imported metadata and original MCP binding. Do not delete or duplicate
the existing entry to work around a connection error.

The endpoint challenges anonymous calls with OAuth, and reports through the
existing authenticated connection succeeded. Neither proves a fresh reviewer's
sign-in, consent and callback flow. Test that complete flow with the credentials
entered in secure portal fields, with access to the stated workspace and no
additional registration, verification or account setup.

Fresh reviewer OAuth, saved-version positive/negative conversations, imported
review metadata, final MCP scan and required attestations: **Not run / incomplete**.
No portal upload, submission, publication, account mutation or deletion was performed.
