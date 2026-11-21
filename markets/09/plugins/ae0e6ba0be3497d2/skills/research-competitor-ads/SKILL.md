---
name: research-competitor-ads
description: Research the ads other brands are running and turn them into ideas. Use when the user asks what ads a named brand is running, who their competitors are, what is working in their market, how a competitor's ad strategy is built, or which angles and hooks to use based on what customers say.
---

# Research competitor ads

Use this skill to answer questions about other brands' advertising with real ads from public ad libraries, then
turn what you found into something the user can act on. Explicit instructions from the user always take priority
over this skill (for example a country, a platform or how many ads to show).

## Pick the right tool for the question
- **One named brand's ads** ("show me Liquid Death's ads"): call `pull_competitor_ads` with the brand name, and its
  website if you know it. It returns that brand's live Meta (Facebook and Instagram) ads in a few seconds. This is
  the default for any request that names a brand.
- **Who the competitors are** ("who competes with oatly.com?"): call `find_competitors` with the domain. Ask for the
  website if the user only gave a name and it is ambiguous.
- **How a competitor's strategy works** ("break down Athletic Greens' ads", "where is the white space?"): call
  `competitor_teardown` with the competitor's name and website. If you already pulled their ads in this
  conversation, pass those ads so they are not fetched again.
- **An open question across the market** ("what angles are working for oat milk brands?", "who else advertises
  like this?"): call `research_ads` with the question. It runs several searches and writes a synthesis, so it takes
  30 to 60 seconds. Do not use it when the user named one brand.
- **Angles from real customer language** ("what do customers actually say about us?", "give me hooks from our
  reviews"): call `mine_angles`. If the user pastes reviews or gives a file or review page, pass them.

## Steps
1. Work out which of the questions above the user is asking. If they named nothing (no brand, no domain, no
   market), ask one question to find out whose ads they want to see.
2. Call the one tool that answers it. Do not chain every research tool by default.
3. Summarise what came back in plain language: the recurring hooks, offers, formats and how long the ads have been
   running (long-running ads are the ones the advertiser keeps paying for). Name specific ads when you point at a
   pattern.
4. Offer one next step that fits: break the strategy down (`competitor_teardown`), mine angles for their own brand
   (`mine_angles`), or make an ad that uses what they learned (the make-an-ad skill).

## Output
Lead with the answer to the question, then the evidence. Keep the ads in the cards the tool returns rather than
re-listing every field. Close with the one suggested next step.

## Handle thin or missing results
- An advertiser can have no ads in a library, or run them under a different page name. If a pull returns nothing,
  say so plainly, suggest checking the exact brand name or website, and offer `research_ads` for the category.
- Never invent ads, dates, spend or results. Ad libraries do not publish spend or conversions, so do not estimate
  them.

## Do not
- Do not claim you can see a competitor's private ad account, targeting or budgets. Only public library data is
  available.
- Research uses credits from the user's Hermoso account, so run a search when the user asks for one, not
  speculatively.
