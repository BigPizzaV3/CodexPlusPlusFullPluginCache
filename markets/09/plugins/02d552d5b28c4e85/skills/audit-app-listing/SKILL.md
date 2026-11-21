---
name: audit-app-listing
description: Audit an app's App Store or Google Play listing against its competitors with Clonerrr's App audit and turn the findings into a prioritised plan. Use when the user asks for an app store optimisation (ASO) review, why their listing is not converting, feedback on their title, keywords or screenshots, or what their recent reviews say.
---

# Audit an app's store listing

Clonerrr's App audit reads a public App Store or Google Play listing, finds the apps it competes with, and grades the listing, keywords, screenshots, recent reviews and paid ads against them.

What the user asks for comes first. If they only want one section, or a shorter answer, give that.

## Steps

1. **Get the store link.** The audit needs the app's App Store or Google Play link. If the user gave only a name, ask for the link; do not guess one.
2. **Run it.** Call `run_app_audit` with `store_url`. A new audit takes a minute or two and is worked through a few steps per call:
   - While `status` is `running`, call `run_app_audit` again with the same `store_url`. Tell the user once that it takes a minute or two.
   - If it is still running after eight calls, stop, give the user `report_url` and say the report finishes filling in on its page.
   - An audit finished in the last three days comes back at once; `audited_on` says when the listing was read.
3. **Answer from the findings** once `status` is `done`:
   - The store score and each section's score, then the `headline`.
   - The `priorities`, in the order given, each with what to change and why.
   - A link to `report_url`, where every section is laid out in full with the competitors side by side.
4. **Go deeper on request.** Each entry under `sections` has the detail: the listing's checks with a grade and a fix, the searches with today's rank, the screenshots' first three to test, the complaints in recent reviews, and ad ideas. Useful follow-ups you can write yourself: a new title and subtitle from `title_to_test` and `subtitle_to_test` (30 characters each on the App Store), a rewritten description opening, screenshot captions. For an ad idea, call `get_ad_template` with its `built_on.id` and write the script.

## What not to infer

- Ranks come only from `searches`. A search with no `rank` means the app was not in the results read (`looked_at_top`), not that it can never rank.
- Use only the numbers in the result. Do not estimate downloads, revenue or conversion rates.
- The paid ads section reads Clonerrr's library, which is a sample. Never say a competitor does not advertise; say none of its ads are in the library.
- A score is a comparison with the competitors found for this audit, not an absolute grade.

## When it cannot run

- The link is not an App Store or Google Play listing: say the audit covers those two stores only.
- The tool says the day's limit is reached: tell the user and suggest trying tomorrow. Do not retry in a loop.
