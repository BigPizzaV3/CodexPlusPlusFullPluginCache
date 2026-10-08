# Sector Brief — Report Authoring Spec

Detailed authoring rules for the Sector Brief report body. Read this before emitting the
HTML artifact. It is authoritative for the per-section content specs (Executive Summary and
Sections 1–6) and the inline SVG charts; the section content **targets** (`#sa-*` element
mapping), cover/footer fields, and HTML conventions remain in `SKILL.md`.

## Section content specs

Per-section content requirements for the report body. The synthesis hierarchy (Moody's
internal research is the primary foundation, web supplements) and the inline-citation rules
are in `SKILL.md` Step 3.

### Executive Summary

Write after all other sections are complete. Half-page maximum. Highlight the most relevant
data from each section. No bullet points — flowing paragraphs only.

### Section 1: Sector Overview

Four subsections:
1. **Description of the Sector** — Define the industry, key activities, product/service
   categories, and business-model differences
2. **Market Size and Growth Trends** — Current market size (revenue, volume), historical
   growth rates, regional growth data
3. **Key Players** — Major companies, market share, roles within the sector
4. **Geographic Scope** — Key regions of activity, potential growth markets,
   region-specific trends

### Section 2: Macro-Economic Context

Three subsections:
1. **Economic Indicators** — How GDP growth, inflation, interest rates, consumer
   spending/confidence impact the sector
2. **Regulatory Environment** — Laws, regulations, compliance risks, tariff/trade policy
3. **Global Trends and External Factors** — Geopolitical issues, trade policies,
   technological disruptions, channel evolution

### Section 3: Financial Performance Analysis

Three subsections with **mandatory quantitative data**:
1. **Sector-Level Financial Metrics** — Aggregate revenue, profit margins, return on
   equity, other key metrics. Every metric must include the actual number (e.g., "Aggregate
   revenue of $35.2 trillion in 2025") followed by analytical commentary
2. **Historical Trends** — Past performance trends, demand/earnings trajectories,
   recent growth rates
3. **Projected Financial Outlook** — Forecast key metrics, earnings outlook, key drivers
   shaping the near-term, structural offsets and strategic responses

### Section 4: Industry Structure and Dynamics

Four subsections:
1. **Main Participants** — Benchmark major companies, roles, market share, significance
2. **Supply Chain Analysis** — Suppliers, manufacturers, distributors, customers,
   key pressure points
3. **Competitive Landscape** — Porter's Five Forces analysis with Moody's-grounded
   commentary for each force (use ratings High / Moderate / Low for each force)
4. **Barriers to Entry** — Capital requirements, regulatory hurdles, technology
   requirements, market saturation

### Section 5: Risks and Challenges

Five subsections:
1. **Operational Risks** — Supply chain disruptions, labor shortages, working capital
2. **Regulatory Risks** — Compliance requirements, policy changes, tariff exposure
3. **Market Risks** — Demand volatility, competition, pricing, category weakness
4. **Financial Performance and Capital Structure** — Refinancing risk, default outlook,
   margin pressure, deleveraging
5. **Environmental and Social Risks** — ESG considerations, climate risk, social/governance
   pressures

### Section 6: Sector Outlook

State the Moody's outlook (Positive, Stable, Negative) and date. Then provide 2-3
well-developed paragraphs explaining the rationale — primary drivers, regional nuances,
key factors and considerations. All paragraph form, no bullet points.

## Inline SVG Charts — Section Instructions

After synthesizing each of the following sections, embed one inline SVG chart directly in the section content at the position indicated. All charts must be self-contained (no external scripts or stylesheets), include a `<title>` element for accessibility, and use `font-family: 'Source Sans Pro', Arial, sans-serif` inside an embedded `<style>` block.

### Section 3 — Financial Performance Analysis

Insert **Chart A** immediately after the Historical Trends subsection prose:

- Type: grouped bar chart (revenue) with a right-axis line series (EBITDA margin %)
- X-axis: fiscal years (last 3–5 years); left Y-axis: revenue ($B or $T); right Y-axis: margin (%)
- Bar color: `#003087`; line color: `#0073CF`
- `viewBox="0 0 700 320"`

### Section 4 — Industry Structure and Dynamics

Insert **Chart C** immediately after the Porter's Five Forces prose:

- Type: horizontal scored bar chart, one bar per force (5 bars)
- Map ratings to scores: High = 3, Moderate = 2, Low = 1; scale bar lengths to a 1–3 axis
- Bar colors: High = `#C0392B`, Moderate = `#E67E22`, Low = `#27AE60`
- `viewBox="0 0 700 220"`

### Section 6 — Sector Outlook

Insert **Chart D** immediately after the outlook paragraphs:

- Type: horizontal three-zone sentiment track (Negative | Stable | Positive) with a triangular marker at the current outlook position
- Zone colors: Negative = `#C0392B`, Stable = `#2980B9`, Positive = `#27AE60`; marker color matches active zone
- Label the current outlook and date below the track
- `viewBox="0 0 700 120"`

### Pre-computation requirement — mandatory, no exceptions

Before writing any SVG `x`, `y`, `width`, `height`, or `points` attribute that depends on a calculated value (bar lengths, axis tick positions, scale factors, percentage-to-pixel conversions, label offsets, marker positions), compute every value programmatically. **If you do not have a calculator tool, use bash or Python to compute all of the above values before emitting any SVG — do not attempt to calculate them mentally.** Record the computed values, verify them, then substitute the confirmed numbers into the SVG markup.

If source data for any chart is unavailable, emit a `<p>Chart data unavailable</p>` placeholder in its place — never omit it silently.
