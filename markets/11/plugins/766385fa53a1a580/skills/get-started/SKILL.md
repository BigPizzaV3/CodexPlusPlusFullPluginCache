---
name: get-started
description: Onboarding for the AnySchool connector. Use when the user first connects AnySchool or asks what it can do, to explain the tools for their account type and start with a sensible first question.
---

# Getting started with AnySchool

AnySchool answers questions about 126k+ schools in 216 countries, using the signed-in user's own plan, filters and credits.

## First steps

1. Call `get_account` to see whether this is a **supplier** or a **school** account, the plan, and the remaining unlock credits and Brief quota. Which tools exist depends on that.
2. Call `list_filters` before building any filter. It returns the columns and exact values available on this plan. Use only those.
3. Use `find_schools` to filter, and read the step counts to explain how the set narrows. Use `school_brief` for medians and spread (this counts against the plan's Brief quota, so use it once per question).

## School accounts

Competitor and peer analysis: `find_peers` (closest schools by size and fees, compared with the user's school) plus `school_brief` for the wider market. School accounts never have contacts; if asked, say so and stop.

## Supplier accounts

Qualify the market first (`find_schools`, `school_brief`), then `find_contacts` for named schools. Contacts come back masked. `unmask_contact` unlocks exactly one contact and costs 1 credit: say so and get a yes first. `start_lead_finder` runs an AI ranking that takes minutes; poll `get_lead_finder_run`.

## What AnySchool will not do

No export, bulk reveal, CRM push or mass unlock in chat. Do not promise lists of contacts. Fees are in local currency, so never mix currencies in a median.

## Good first questions

- "Find UK boarding schools with STEM investment and give me the median fee."
- "Who are our closest peer schools, and how do our fees compare?"
- "What filters can I use on my plan?"
