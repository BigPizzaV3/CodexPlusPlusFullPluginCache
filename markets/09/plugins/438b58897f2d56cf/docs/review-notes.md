# MNTN review preparation

The imported cases and publication details are in `.codex-plugin/plugin.json`.
This file records preparation evidence and is not automatically imported into
the portal review form. All five positive cases use Data Mode; no widget
interaction is required by these cases.

## Selected workspace and dates

The available MNTN connection listed MNTN Demo, connected to LeapXpert. June 2026
returned advertising delivery, so the cases use that month, with July 2026 as
the comparison. The reviewer account must have access to MNTN Demo and its
historical data. No dedicated reviewer login has been exercised here.

| Check | Status | Evidence and limits |
| --- | --- | --- |
| Monthly report data | Passed | June returned Total spend 14,040.16, 470,540 impressions, 460,594 completed views, 165 verified visits, 116 conversions, and Cost per visit 85.09. No currency code was returned. |
| Month comparison data | Passed | One request returned June and July. July had zero spend and impressions but 96 verified visits and 67 conversions; the case preserves those outcomes without inventing a cause. |
| Campaign report data | Passed | One campaign row returned with an ID and name; spend, impressions, visits, and conversions matched the advertiser summary. |
| Weekly report data | Passed | Five periods returned, including June 29-30 as a partial week. Spend, impressions, and visits summed to the June summary. |
| Creative report data | Passed | Three distinct creative IDs shared the same name. Spend, impressions, and visits matched the advertiser summary; completed-view totals differed as described below. |
| Full conversational cases | Not run | Direct reporting calls do not establish the model's routing, calculations, explanations, or handling of the three negative prompts in fresh conversations. |
| Local connector tests | Passed | 113 existing MNTN profile/UI tests passed with authentication, reports, and widget loading mocked. These are separate from the Data Mode-only review cases. |
| Public endpoint | Passed for discovery | Root status and OAuth protected-resource metadata were reachable, with the expected MNTN endpoint and tool names. |
| Saved draft and reviewer sign-in | Not run | No portal draft was uploaded and no dedicated reviewer credentials were tested. |

A daily-granularity request failed with an upstream MNTN HTTP 429 rate limit.
After independent package work, a weekly-granularity request succeeded. The
submitted trend case uses Week to reduce the number of report periods. The
server's handling of daily-report rate limits was not changed during packaging.

Creative-level completed views summed to 460,600, versus 460,594 in the
advertiser-level summary. The cause was not established. Returned creative
values are preserved; the case requires disclosure if comparing aggregation
levels, not changing rows to force equality. Monetary values had no currency
code, so the cases do not invent one.

Live queries used the MNTN connection exposed to this session. Its runtime label
does not establish a particular installed plugin or saved portal draft. The
recorded values are evidence from those responses, not immutable expected
outputs. The complete conversational review suite is not marked passed.

## Demo and publication details

The supplied demo is https://youtu.be/WtrdIW8qXto. Anonymous YouTube checks
returned “Adzviser MNTN ChatGPT Plugin Demo” by Adzviser, player status OK,
a non-private flag, and a 192-second duration. Visual quality and case coverage
were not independently watched.

The package reuses the supplied 256 x 256 Adzviser icon and existing website,
support form, privacy notice, and terms. All supported countries and website-only
Adzviser subscription billing carry forward the publisher's previous choices.
Reviewer credentials and account email addresses are not in the ZIP.

## Upload and review

The original download remains in Downloads. The package is named `adzviser-mntn`
and declares the `mntn` server at `https://mntn.mcp.adzviser.com/widgets/http`
from the first upload. Create the new submission from the main Plugins page;
an existing skills-only draft cannot accept an added server through reupload.
Subsequent ZIP revisions retaining this server can be reuploaded to that draft.

Connect and verify the server, inspect the imported review fields and scan
findings, and provide reviewer access in the portal's secure fields. Run the five
Data Mode prompts and three negative prompts against the saved version before
completing review attestations. Hosted tool annotations are not controlled by
this ZIP, and local test success does not establish OpenAI scan approval.
