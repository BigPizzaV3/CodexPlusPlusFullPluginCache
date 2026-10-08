---
name: pl-partner-ecosystem-scan
description: Scan Partnership Leaders research for companies, partner motions, AI partner programs, marketplaces, announcements, M&A, awards, financial disclosures, industries, and recurring partner ecosystem patterns.
---

# Partnership Leaders Partner Ecosystem Scan

Use this skill when a user wants a market scan, trend pass, competitor readout, or account-specific research pass across Partnership Leaders research. Assume the reader is a senior partnership leader who needs slide-ready judgment backed by named companies, dates, and figures.

Recommended workflow:

1. Identify the likely dataset filter from the request.
2. If the user names a company, product, partner program, topic, or motion, search that term first.
3. If the user asks for a market view, list relevant tags, events, or companies before selecting evidence findings.
4. Lead with the most significant companies, tightened rules, changed incentives, or cross-market patterns.
5. If no company is named, surface notable companies plus competitors or adjacent ecosystem players rather than generic long-tail mentions.
6. If a company is named, center that company first, then compare with one or two named peers when evidence supports it.
7. Compare across datasets only when useful; otherwise keep the scan focused.
8. Ground the scan in returned evidence and verify source URLs before using them.

Dataset guidance:

- Use `aip` for AI partner programs, partner-facing AI, AI marketplaces, frontier AI partnerships, partner AI upskilling, and partner org AI usage.
- Use `ec75` for ecosystem companies, partner-tech, marketplaces, resell/co-sell motions, and technology partner programs.
- Use `insight_si` for systems integrators, consulting partners, managed services, hyperscaler SI motions, and service capability signals.
- Treat dataset names as internal routing only. Do not expose dataset names, project names, significance labels, coverage notes, cadence, or provenance footers in the final answer unless the user asks an admin/testing question.

Executive lens:

- Emphasize why each signal matters to a partnerships, alliances, channel, or ecosystem leader.
- Look for implications around partner program design, partner incentives, marketplace routes, co-sell/resell motion, certification or enablement requirements, competitive positioning, partner selection, and customer access.
- Separate observed facts from strategic interpretation.
- Include at least one cross-company synthesis when the evidence supports it, such as concentration, outliers, or counts across named companies.
- Counts must come from named items in the answer. Count vendors and programs separately, and do not include announced future programs in counts of completed changes.
- Cover what got harder or was tightened, not only what launched.
- Use day-level dates only when the returned records carry day-level dates.
- Use at most one superlative per answer, and only when the evidence names what it beats.

What to avoid:

- Do not infer partner access, tenant, tier, or entitlements from user text.
- Do not expose raw internal data beyond what the MCP server returns.
- Do not overstate a sparse tag as a market-wide trend.
- Do not merge companies with similar names unless the evidence clearly supports it.
- Do not invent prior rules or prior regimes just to make a change look bigger.
- Do not use formula closers, bold-fronted label ladders, or generic consulting language such as "robust", "seamless", "landscape", "leverage", and "game-changing".
