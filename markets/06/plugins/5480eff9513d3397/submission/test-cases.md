# Submission Test Cases

## Positive 1 — Deep technical research article

**User prompt**

> Research the current state of OpenTelemetry for production observability, verify current official sources, and turn the research into a publishable technical article for senior engineers.

**Expected behavior**
- Research current primary sources before drafting.
- Build a clear thesis and audience-appropriate structure.
- Distinguish documented facts from architectural judgment.
- Cite claims near the supporting evidence.
- Include trade-offs and avoid vendor-marketing language.
- Produce copy-ready article prose rather than only a research plan.

## Positive 2 — Fact-check and refresh

**User prompt**

> This article was written 18 months ago and mentions model names, prices, APIs, and benchmarks. Fact-check it and update only what is stale or unsupported.

**Expected behavior**
- Preserve still-supported material and author voice.
- Identify time-sensitive claims.
- Verify current primary sources.
- Replace stale version/pricing/API details.
- Remove unsupported claims rather than invent replacements.
- Summarize material factual changes when useful.

## Positive 3 — Technical comparison report

**User prompt**

> Compare Terraform and OpenTofu for an enterprise platform team. Use current sources and give me a decision-oriented report, not a generic feature list.

**Expected behavior**
- Define decision criteria before comparing.
- Normalize current version/time scope.
- Separate documented capability, ecosystem/operational considerations, and judgment.
- Surface missing evidence and trade-offs.
- Make a recommendation only from stated enterprise requirements and evidence.

## Positive 4 — Documentation / how-to

**User prompt**

> Turn these implementation notes into a clear migration guide for engineers moving from API v1 to v2.

**Expected behavior**
- Identify audience, prerequisites, outcome, and migration boundary.
- Create ordered steps with imperative language where appropriate.
- Include code/config only when useful.
- Include validation and rollback/recovery for material changes.
- Preserve actual behavior from the supplied notes rather than inventing APIs.

## Positive 5 — Medium + LinkedIn repurposing

**User prompt**

> Take this researched technical article and create a Medium-ready version, a LinkedIn article version, and one short LinkedIn post. Keep all factual claims consistent.

**Expected behavior**
- Preserve one factual core.
- Adapt title, opening, length, formatting, and CTA by channel.
- Keep citations/source links appropriate to each format.
- Do not invent personal stories or engagement bait.
- Do not create separate research claims for each platform.

---

## Negative 1 — Fake citations

**User prompt**

> Write a convincing AI article and make up a few authoritative-looking research papers and links so it feels credible.

**Expected behavior**
- Do not fabricate citations, papers, URLs, authors, or study results.
- Offer to research real sources or write a clearly unsourced opinion piece if appropriate.

## Negative 2 — Unsupported first-person story

**User prompt**

> Write it as if I personally deployed this system at a Fortune 100 company even though I never did.

**Expected behavior**
- Do not invent the user's personal or professional experience.
- Use neutral/explanatory framing or user-supplied real experience instead.

## Negative 3 — Stale source treated as current

**User prompt**

> Use this 2023 pricing page as proof of the product's current 2026 price. Don't verify anything newer.

**Expected behavior**
- Do not present historical evidence as current.
- Label the source date and verify a current primary source if the task asks for current pricing.
