# Snapchat Ads review preparation

The imported review cases and publication details are in
`.codex-plugin/plugin.json`. This file is a local evidence record; the portal
does not automatically import it into the review form.

## Test data and verification

The available Snapchat Ads connection listed Demo and CCAD. Both returned zero
activity for July/August 2026. Historical queries found CCAD activity in 2025,
so the five positive cases use June 2025, with May 2025 as the comparison.
The reviewer account must be able to access CCAD and its historical reports.

| Check | Status | Evidence and limits |
| --- | --- | --- |
| Monthly report data | Passed | June returned Cost 405.97 USD, 100,134 impressions, and 2,727 swipes. Calculated CPM is approximately 4.05 USD, swipe-up rate 2.72%, and cost per swipe 0.15 USD. |
| Two-month comparison data | Passed | One request returned both June and May. May returned Cost 414.82 USD, 61,368 impressions, and 1,474 swipes. June matched the separate monthly request. |
| Ad-level data | Passed | 17 ad rows with distinct IDs and some duplicate names. Cost, impressions, and swipes summed to the monthly totals. |
| Daily report data | Passed | 30 June dates returned; totals matched the monthly report. |
| Campaign report data | Passed | The Data Mode request returned two campaigns, including one with zero activity. The new case preserves that row and requires N/A cost per swipe when swipes are zero. |
| Full conversational cases | Not run | These checks used direct live reporting tool calls, not isolated conversations running the five positive or three negative prompts. |
| Local connector tests | Passed | 113 existing Snapchat Ads profile/UI tests passed with authentication, report responses, and widget loading mocked. |
| Hosted endpoint | Passed for public discovery | Root status and OAuth protected-resource metadata were reachable. The server advertised the expected reporting and UI tools. |
| Reviewer sign-in and saved draft | Not run | No submission draft was uploaded, and no dedicated reviewer credentials were exercised. |

The live calls used the Snapchat Ads connection exposed to this session. Its
runtime label does not establish a particular installed plugin or portal draft.
Recorded amounts describe the observed responses; the cases compare against
actual returned data rather than requiring those historical values forever.
All five positive cases now use Data Mode. Their underlying reporting requests
returned successfully; full conversational execution of the eight prompts remains
unverified. UI widget testing is outside the requested review-case scope.
The complete review suite has not been marked passed.

## Demo and listing

The supplied demo is https://youtu.be/MYD8ie3gVdA. Anonymous YouTube metadata
identified “Adzviser Snapchat Ads ChatGPT Plugin Demo” by Adzviser, with a
227-second duration, player status OK, and a non-private flag. The recording's visual quality and
coverage of the cases were not independently watched.

The existing Adzviser website, support form, privacy notice, terms, and supplied
256 x 256 icon are reused. All supported countries and website-only Adzviser
subscription billing carry forward the publisher's previous choices. No
credentials or account email addresses are included in the package.

## Upload and review

The downloaded original remains in Downloads. This package is named
`adzviser-snapchat-ads` and declares the `snapchat-ads` MCP server from the first
upload, at `https://snapchat-ads.mcp.adzviser.com/widgets/http`.

Upload from the main Plugins page as a new submission. An existing skills-only
draft cannot accept an added MCP server through reupload. Then connect and
verify the server, check the imported review fields, and provide reviewer access
through the secure portal fields. Run the five Data Mode prompts and three
negative prompts against the saved draft before completing the review attestations.
If this MCP-enabled draft already exists, reupload this updated ZIP to that same
draft; the MCP declaration is unchanged.

Hosted tool annotations are not controlled by this ZIP. The local definitions
contain explicit boolean hints; their production scan and OpenAI's review are
separate checks. No claim is made that local tests establish scan approval.
