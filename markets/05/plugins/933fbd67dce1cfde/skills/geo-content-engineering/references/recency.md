# Recency and freshness

Visible date markers and real content updates as a precondition for being chosen
by generative systems.

## The mechanic

Current LLM systems favor fresh content, sometimes strongly enough that a weaker
but newer text displaces a better older one. Freshness has to be both visible and
real.

## Rules

1. **Visible date markers in the text.** Write the date into the content itself,
   for example "As of 01/2026: currently ...". A CMS timestamp alone is not
   enough.

2. **Update boxes.** Keep a "What changed" section with two to four points from
   the most recent real content changes. Template in `../assets/update-box.md`.

3. **Real updates.** Actually refresh facts, prices, links, and figures on a
   schedule. Do not just move the date.

## Risk: timestamp gaming

Changing the publish date with no substantial change is detectable and likely to
be penalized more over time. Substantial means new facts, new sources, or changed
recommendations, not cosmetic rewording.
