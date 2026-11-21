---
name: review-insights
description: Summarize recurring themes in sampled public Google Maps, Yelp, Amazon or Walmart reviews with HasData. Use for business or product review comparisons, not posting, removing or verifying reviewers.
---

# Summarize customer review evidence

Read `../hasdata-research/SKILL.md` and `../hasdata-research/references/tool-contract.md` before tool calls. Their scope, security and credit limits apply.

Honor the requested review source. For Maps, reuse a known placeId or search by business name and city. For Yelp, resolve the directory's own placeId. For Amazon or Walmart, use a returned product identifier or an unambiguous supplied product URL. Read the relevant section of `../hasdata-research/references/tool-catalog.md`. Never reuse IDs between platforms. Ask when several branches or product variants are plausible rather than charging for a guessed target.

Fetch one page. For recent Maps feedback use sortBy:newestFirst unless another order was requested. Other platforms have different sort enums, filters and pagination fields. Use the chosen tool's actual schema and do not pass Maps options to a product or Yelp review tool. Do not invent topic or aspect IDs. Further pages use the source's supported page field or returned token within an agreed budget.

Read actual review fields from the payload. Separate review text, star rating, returned publication date and available source URL. State the number of reviews with readable text, the returned sample size and sort order. Relative dates are approximate. Do not claim a calendar cutoff was enforced unless the tool supports it and the returned dates justify it.

Group recurring themes with supporting examples. Count each review once per theme. Give concise faithful quotes and available review links; if individual URLs are absent, link the place or returned snapshot and say individual links were not returned. Do not copy unnecessary reviewer profile details. Distinguish recurring issues from an isolated complaint, and evidence from your interpretation.

Return a short findings summary with theme counts and practical follow-up suggestions. Label the suggestions as analysis, not claims from the reviews. Do not infer motivations or sensitive traits, exaggerate the prevalence of an issue, or turn a sampled sentiment count into the business's overall customer satisfaction rate. A business rating is not an average you calculated from this sample.

For comparing two businesses, use the same sort order and a bounded page count for each. Flag differing sample sizes and missing text. Without earlier saved review observations, do not claim that sentiment improved or deteriorated.
