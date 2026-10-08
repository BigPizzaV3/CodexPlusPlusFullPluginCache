---
name: google-analytics-report
description: Report Google Analytics 4 data for a brand. Use for sessions, users, engagement, traffic sources and channels, GA4 events, conversions, or audience breakdowns. Do not use for Google search impressions, clicks or ranking position, which belong to google-search-console-report.
---

# Google Analytics 4 report

Report what people did once they arrived: where they came from, how many, and what they did.

Every tool here is scoped to one brand and takes `brand_id`.

## Step 1: resolve the brand

Call `list_brands`. If more than one, ask which. Keep `brand_id` for every later call.

## Step 2: confirm the property

1. `list_connectors` to check Google is connected. If not, say so and stop.
2. `list_ga4_properties` to see the available properties.
3. If several exist, ask which one. Reporting the wrong property is worse than reporting nothing, because the numbers look plausible and are simply about a different site.
4. `set_ga4_property` selects it. This changes what every later report measures, so confirm before calling it.

## Step 3: refresh only if asked

`sync_ga4` pulls fresh data and takes time. Otherwise report what is stored and say when it was last synced.

## Step 4: pull the numbers

- `get_ga4_metrics` for the headline: users, sessions, engagement.
- `get_ga4_traffic_breakdown` for channels and sources.
- `get_ga4_events` for tracked events and conversions.
- `get_audience_breakdown` for who they were.

## Step 5: report

State the property and the date range for every number.

Rules that keep the report honest:

- **Segment before concluding.** A rise in sessions driven by one referral is a different story from a rise in organic search. Give the channel breakdown alongside the total, never the total alone.
- **Sessions are not people.** Report users and sessions distinctly and do not use them interchangeably.
- **Check the window is complete.** GA4 data for the current day is partial. Exclude today, or say it is partial.
- **Compare equal windows,** and prefer like for like periods. Month against month is cleaner than an arbitrary range against another.
- **An event is only a conversion if it is configured as one.** Do not promote an ordinary event into a conversion in the write up.
- Never estimate a missing figure. If it returned nothing, say so.

## Step 6: connect it to the work

The useful question is not how many sessions there were, but whether the work moved them:

- Organic sessions rising while search impressions are flat suggests better CTR rather than better reach. Confirm with the google-search-console-report skill before claiming either.
- A traffic rise concentrated on a small number of pages is worth naming. Say which pages.
- If a channel collapsed, check whether tracking changed before treating it as a real loss. A tag change and a traffic drop look identical in the data.

## Boundaries

- GA4 measures people on the site. It cannot tell you what someone searched to get there, which is Search Console's job.
- For visibility inside AI assistant answers, use the ai-visibility-report skill.
- For a combined client or monthly report, use the performance-report skill.
