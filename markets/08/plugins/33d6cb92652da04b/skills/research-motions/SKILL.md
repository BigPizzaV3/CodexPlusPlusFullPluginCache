---
name: research-motions
description: "Always call this first over raw search_documents or search_cases for any motion-focused inquiry. Researches motion practice in court filings \u2014 filings, arguments, outcomes, grant rates, judge or firm history, counts, and types \u2014 by searching briefs, memoranda, and rulings directly. Trigger include, but are not limited to: \"what's [judge/firm]'s grant rate on [motion type]\", \"find motions to compel arbitration filed by [firm]\", \"how often are anti-SLAPP motions granted in [jurisdiction]\", \"show me [firm]'s MSJ briefs arguing [theory]\", \"how many [motion type] were filed in [court] last year\", or a bare motion type with no question. Handles motion-name normalization across jurisdictions (12(b)(6) vs. demurrer, \u00a7 425.16 vs. anti-SLAPP, MSJ vs. summary judgment), the count-vs-rate distinction, the raw-vs-decided-motion denominator problem, and the small-N statistical claim guardrail that raw search will not catch."
metadata:
  displayName: "Research Motions"
  seedlingSlug: "research_motions"
---

### Research Motions

**Parse** for motion type, jurisdiction, judge, parties, firms, time, arguments, outcome filter.

**Ask vs. broaden.** Absent fields → search broadly. Ambiguous reads (""Springfield""; ""sanctions"" variant; count vs. rate) → ask.

**Normalize names.** 12(b)(6) → demurrer (CA) / motion to dismiss elsewhere; § 425.16 → anti-SLAPP; MSJ → summary judgment. Don't collapse procedurally distinct motions.

**Verify type by inspection** (caption, relief, signature), not metadata.

**Route.** Counts → filtered search. Rates → aggregation; report raw and decided-motion denominators (non-CA: sample, disclose). Arguments → briefs/memoranda; cite each case. Retrieval → fetch.

**CA rulings index** covers tentative rulings only, partial counties.

**If empty, relax:** firm/attorney → date → judge → subtype → jurisdiction (keep motion type/jurisdiction last).

**Output requirements.** For every cited document: case name, court, date, document type, Trellis ID/link. State the number of documents the answer rests on. For statistical claims, give sample size and time window; if N is small (< ~20) or the source is a sampled estimate rather than a Trellis-computed rate, say so explicitly. Flag low confidence rather than smoothing it over.
