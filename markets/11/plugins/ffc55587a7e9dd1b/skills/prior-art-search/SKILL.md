---
name: prior-art-search
description: Run a prior-art search with Patenta and report which published patents overlap an invention. Use when someone asks whether an idea is new, whether it is already patented, or which existing patents are close to it.
---

# Prior-art search

## 1. Get a searchable description

A good description says what the invention is, how it works and what is distinctive about it. If the user's message already covers that, use it. If it is only a product name or a goal ("a better bike lock"), ask one short question about how it works before searching.

Leave names, companies and contact details out of the search.

## 2. Search once

Call `search_patents` with:

- `query`: two to six plain sentences of technical substance. Use the user's own terms and add the standard technical terms for the same things. No marketing language.
- `country`: only when the user names a patent office. Otherwise leave the default.

Every search covers the full history. There is no period to set.

Each call runs a search on the user's Patenta account and uses its credits. Do not repeat a search with the same description. Search a second time only when the first results are clearly from the wrong field or the user asks for it, and say why you are searching again.

## 3. Report

- Start with a one or two sentence answer: how close is the closest existing patent?
- List the three to five most relevant results. For each give the publication number as a link, the title, the assignee and the year, then one sentence on what overlaps with the user's idea and one on what differs. Base both on the abstract. Do not describe claims you have not seen.
- If the user asked about a period ("the last five years", "before 2010"), pick the patents from the results by their publication dates. If none fall in it, say so and name the closest ones outside it.
- State what was searched (offices and period), taken from `searched` in the result.
- If nothing close was found, say so, and add that this does not prove the idea is new: the search covers published patents only, not unpublished applications, products or papers.

## Limits to state plainly

- This is a screening search. It is not a legal opinion on patentability or freedom to operate. For a filing decision, point the user to a patent attorney.
- Results come most relevant first. Relevance (0 to 100) says how closely a patent discloses the same technical solution. Similarity says how close its text is in topic, so it need not follow the order. A high score is a reason to read the patent, not proof of a conflict.
- If the tool reports that the account has no search access or has run out of credits, pass that message on as it is.
