# URL prioritization for rebuilds

Criteria and order for choosing which pages to rebuild first, when the user has
many.

## Pre-filter: technical blockers

URLs with blocked crawler access (robots.txt, firewall, pure client rendering)
are not rebuilt editorially until access is fixed. Editorial effort on an
invisible page is wasted (see `crawler-access.md`).

## Prioritization criteria

Score four criteria per URL or cluster:

1. **Prompt demand.** How many of the client's tracked prompts target the
   cluster's topic? High demand first.

2. **Competitor gap.** Is a competitor mentioned in answers where the brand is
   not? These clusters have the biggest short-term payoff (see
   `measurement.md`).

3. **Business value.** Proximity of the cluster to a transaction or lead.
   Information-only topics rank lower.

4. **Rebuild effort.** Rough estimate: number of paragraphs, availability of
   proprietary data for citation-worthiness, dependency on IT changes.

## Building the order

High demand plus a competitor gap at low effort forms the first wave. Clusters
with high business value but IT dependency run in parallel as technical tickets.
Re-check the order after each measurement window against actual SoM movement, do
not fix it once.
