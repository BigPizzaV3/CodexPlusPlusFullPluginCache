# Platform lift studies

Ad platforms can randomize at user level: a holdout group is eligible to see the ads but does not, and the platform compares conversions between groups. This is the strongest design available for a single platform, and it is usually cheaper than a geo test. Recommend it first when the question is about one platform and the account qualifies.

Requirements change often. Figures below were checked on 2026-10-02 in the platforms' help pages. Tell the user to confirm eligibility in their account or with their platform representative before planning around it.

## Google Ads Conversion Lift

Two variants:

| | Based on users | Based on geography |
|---|---|---|
| Randomization | Users held out from seeing ads | Regions, within one country |
| Campaign types | Display, Search, Video, Demand Gen, App, Performance Max | App, Demand Gen, Display, Video, Search, Shopping, Performance Max |
| Minimum | 1,000 observed conversions; minimum campaign budget of $5,000 USD | Budget "tends to be higher" than user-based; no public figure |
| Holdback | 1% to 50% | Regions |
| Other | Not for iOS-targeted App campaigns or Travel Ads | Campaigns must target a single country; supports offline conversions at ZIP or city level |

- Access: not available to all accounts. The user asks their Google account representative.
- Google lowered the cost of a study from "upwards of $100,000" to "$5,000" (announcement of November 11, 2025).
- Duration: studies can run 7 days, but Google recommends more than 14. It reports up to a 17% drop in absolute lift for studies under 14 days with long conversion lags.
- Reading: certainty is shown from 50% to 95%. Google recommends aiming for 90%; 50% to 90% is directional.
- API: Google Ads API v25.1 (August 2026) exposes lift studies and Conversion Lift metrics read-only. Studies are not created through the API.

Sources: support.google.com/google-ads/answer/12005564, /14097193, /14097991, /16719772; Google Ads API release notes.

## Meta Conversion Lift and Brand Lift

- Conversion Lift on web events requires the Conversions API (CAPI), not only the pixel.
- Minimum spend is shown in Experiments when creating the test, and depends on the account; Meta does not publish a single figure. Ask the Meta representative.
- Brand Lift minimums as of September 15, 2026 include United States $175,000, United Kingdom $64,000, Germany $110,000, France $79,000, Spain $39,000, Italy $55,000. The default for unlisted countries is $15,000.
- Meta's guidance: aim for 80% estimated power; "a 90 percent or higher confidence percentage represents a statistically reliable result" for lift tests.
- Brand Lift should not run while other campaigns for the same brand run on Meta.
- API: lift studies can be read through the Marketing API (`ad_study`, types LIFT and GEO_LIFT, among others). Meta's Ads MCP server documentation lists creating and managing conversion lift studies among its tools.

Sources: facebook.com/business/help/453968412201452, /2420136524735942, /417527072254206, /1693381447650068, /239549606692303; developers.facebook.com Marketing API and Ads MCP Server docs.

## Other platforms

TikTok, Snap, Pinterest, LinkedIn, Reddit and Amazon offer lift or holdout studies of their own, with eligibility set by spend and account status. Their terms were not verified for this plugin: tell the user to check in the platform's experiments or measurement section, or with their representative.

## How to recommend one

1. Confirm the question is about one platform. If it compares channels or needs the business KPI across channels, a geo experiment is the right tool, and the platform study can run before or after it, not during.
2. Check the conversion signal: the study only sees conversions the platform receives. Recommend server-side events (CAPI, offline conversion import, enhanced conversions) so offline and cross-device outcomes count.
3. Choose holdback size with the user: larger holdback, more power, more lost conversions during the test.
4. Plan at least 2 weeks, plus the purchase cycle.
5. Set the decision rule before launch, as for any test (`assets/test-plan-template.md`).

## Limits to state

- Platform studies measure that platform only, with its own conversion data. Results from different platforms cannot be added together.
- Search ads mostly capture existing demand. A user-level study answers whether showing the ad changes behavior, which is the right question, but brand search also depends on whether competitors bid on the brand during the test.
- During a geo experiment, deactivate user-level lift studies on the campaigns under test (Meridian GeoX guidance), since both change who sees the ads.
