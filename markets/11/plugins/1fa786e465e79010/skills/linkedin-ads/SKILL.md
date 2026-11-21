---
name: linkedin-ads
description: LinkedIn Ads with Opus Growth - campaign groups, campaigns (ad sets), sponsored content from Company Page posts, text ads, targeting by job title, function, seniority, industry and company, audience forecasts, bids, conversions, lead gen forms and analytics. Use for any LinkedIn Campaign Manager question or change. Covers LinkedIn's renamed levels, what "active" means, image ads without upload, and lead access requirements.
---

# LinkedIn Ads

Follow the `opus-growth` skill for preview, confirm, dates and budgets.

## Names: the screen and the API differ

LinkedIn renamed Campaign Manager levels in October 2025 but not its API:

| User's screen | API / tool name |
|---|---|
| Campaign | campaign group (`list_linkedin_campaign_groups`) |
| Ad set | campaign (`list_linkedin_campaigns`) |
| Ad | creative (`list_linkedin_creatives`) |

Answer at the level the user sees. When they say "my campaigns", they usually mean campaign
groups; `list_linkedin_campaigns` also returns `ui_campaigns` for that reason.

## What is really running

Creatives list `serving_hold_reasons` when they do not serve (for example UNDER_REVIEW,
CAMPAIGN_END_DATE_HOLD, ACCOUNT_TOTAL_BUDGET_HOLD, CAMPAIGN_AUDIENCE_COUNT_HOLD) and
`rejection_reasons` for a rejected ad; quote them instead of guessing.

LinkedIn's API has no change log. `created_time` and `updated_time` are the only clocks. Do not
invent who edited a campaign.

A campaign serves only when its status is ACTIVE **and** its serving statuses include RUNNABLE.
A campaign in a paused or on-hold group stays ACTIVE but does not serve. A creative in DRAFT
never serves, even under an active campaign; activate it with `update_linkedin_creative_status`.

## Building

1. `create_linkedin_campaign_group` (the user's "campaign") with its budget and dates if needed.
2. `create_linkedin_campaign` (the user's "ad set"): objective (cannot be changed later),
   campaign type (SPONSORED_UPDATES for feed ads, TEXT_AD for right-rail text ads), cost type,
   targeting and budget. Find targeting values with `linkedin_targeting_search`; check the size
   with `linkedin_audience_forecast` (LinkedIn will not run very small audiences, at least about
   300 members) and the bid range with `linkedin_bid_recommendations`.
   A total budget without an end date paces over LinkedIn's 90-day default; set an end date for
   short campaigns. Created as a draft unless the user asks to launch.
3. Ads:
   - **Image ads**: there is no direct image upload in this connection (LinkedIn needs an
     organization permission it does not grant here). Post the image on the Company Page
     first, then sponsor that post with `create_linkedin_post_ad` (post URN from the post URL).
   - Text ads: `create_linkedin_text_ad` (headline ≤25, description ≤75 characters).
   - The actual text of ads that already ran (to compare messaging): `linkedin_ad_copy`.
4. Read back with `list_linkedin_campaigns` / `list_linkedin_creatives`; activate on request.

## Targeting rules that matter

- B2B precision: check `audience_expansion` and `offsite_delivery` (LinkedIn Audience Network)
  in the campaign row. Both widen delivery beyond the chosen professionals; turn them off when
  the audience must be exact.
- Exclusions exist for every facet (industries, employers, titles, functions, seniorities,
  skills, company sizes, locations) in `update_linkedin_campaign_targeting`. Read the current
  targeting first (`list_linkedin_campaigns` returns it) and compare it with the preview, which
  shows what will be set, not what is set now. `location_mode='permanent'` limits geography to
  members whose profile location matches (LinkedIn's default also includes recent locations).
- Job titles are narrow and expensive; function + seniority usually reaches more of the right
  people at a lower cost.

## Conversions and leads

- Website conversions come from the Insight Tag; attach them to campaigns with
  `attach_linkedin_conversion` (`list_linkedin_conversions` shows them).
- No Insight Tag yet: `create_linkedin_insight_tag` creates it. An ad account has only one; if it
  already exists, the existing tag and its code come back. The code goes on every page of the
  site. `create_linkedin_conversion` then adds a website conversion rule: a page URL rule
  (EXACT, STARTS_WITH or CONTAINS), or no URL for an event-specific conversion. A new rule is
  attached to no campaign; attach it with `attach_linkedin_conversion`. Creating either needs a
  role above VIEWER on the ad account.
- Lead gen form answers: `download_linkedin_leads`. It needs LinkedIn's Lead Sync access and a
  role on the Company Page (administrator, lead gen forms manager, content admin, curator or
  analyst) for the person who connected; without the page role LinkedIn refuses even with the
  permission. If the tool says to reconnect, the permission arrived after the last connection.

## Reporting

`linkedin_campaign_analytics` (and `get_report`) report spend, impressions, clicks, leads and
conversions. LinkedIn CPCs are typically several times Google's or Meta's; judge on cost per
qualified lead, not CPC. Reporting can lag by up to a day.

## Every operation

The complete list of this area's operations, what each is for and the tool that runs it: `references/operations.md`.
