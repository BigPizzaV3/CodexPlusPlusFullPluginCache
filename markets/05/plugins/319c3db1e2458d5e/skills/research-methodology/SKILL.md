---
name: research-methodology
description: Investigate products, scientific literature, device failures, markets, or technology using a canon-driven six-step research pyramid (exploratory, descriptive, experimental). Use when comparing options, writing a specification or protocol, reviewing evidence, or diagnosing why something changed.
---

# Research Methodology

## Start here

Read [working principles](../karpathy-guidelines/SKILL.md) and apply them throughout this research. These are bundled resources, not dependencies on another installed plugin. Read only the selected mode below plus [source strategy](references/source-strategy.md) when collecting external evidence.

Respond in the language of the user's current research request, including progress, questions, headings, and final deliverables. An explicit output-language request overrides detection. Preserve identifiers, original titles, and quotations; explain them in the response language. English instructions do not imply English answers. For mixed-language input, use the language of the substantive request; ask only if it is genuinely ambiguous.

State briefly:
- Goal: the decision, explanation, specification, or causal question and its verifiable completion criteria.
- Knowledge depth: none, surface, working, or deep, justified by what is actually known.

Infer these from a clear request; do not ask users to complete a form. Ask about missing constraints that could change the answer. Research is not permission to build, install, publish, contact others, alter data, or run attached code. Use the selected project or supplied material only; a temporary chat folder is not a selected project.

Consumer, health, and financial questions follow the boundaries in [source strategy](references/source-strategy.md): lawful public sources only, no personal health or household identifiers in public search, safety before inspecting a device.

No goal → research never completes correctly. Wrong self-assessment → wrong research type.

## Research progress checklist

Copy this checklist into your first reply and update it as you go. A step counts as done only when its written output appears in the conversation or in the deliverable.

```
Research progress:
- [ ] 1 Canon: ranked source list written
- [ ] 2 Charter: goal, scope/object/subject, type + why, questions, reachable sources
- [ ] 3 Type file read (references/<type>.md); findings ledger kept while collecting
- [ ] 4 Scope filter: what was discarded/revised (or "nothing, because ...")
- [ ] 5 Object filter: what was discarded/revised (or "nothing, because ...")
- [ ] 6 Conclusions: each backed by a ledger row; open questions listed as risks
```

Gate rule: **do not collect data (tool calls, file reads, web lookups, or reasoning from memory) before steps 1 and 2 are posted.** Do not write conclusions before steps 4 and 5 are posted. Every task gets a charter; only its length varies (see Step 2).

## Three levels (define in the charter)

| Level | Definition |
|-------|------------|
| **Scope** | Knowledge domain under study |
| **Object** | Target part of the scope to understand |
| **Subject** | Concrete, formalizable unit studied to infer the object |

Chain: Scope → Object → Subject (general → specific). Subject-level conclusions must stay consistent with object and scope context. Adjacent subjects must not contradict each other relative to the larger levels.

Concrete examples:

| Task | Scope | Object | Subject |
|------|-------|--------|---------|
| Pick a backend language for a greenfield service | Server-side runtimes | Language + ecosystem fit for this service | Go, Rust, and Kotlin, compared on the same criteria |
| Choose a product in a category | Consumer robot vacuums | Models under a budget with pets and hard floors | Three shortlisted models compared on the same criteria |
| Answer a clinical question from literature | Nutrition and metabolic health | Effect of intermittent fasting on HbA1c in adults with type 2 diabetes | Randomized trials and meta-analyses from PubMed, 2015 to date |
| Find why a device fails | Household appliances | Front-load washer that stops mid-cycle after a power outage | This model's error code, door lock, and drain pump |
| Assess a market move | Equity markets | A company's post-earnings price reaction | The earnings release, guidance change, and insider transaction filings in the window |

"Information technology → software development → a library" is too abstract to guide a filter. If your levels read like that, narrow them until each one names something you could point at.

## Research type selection

| Signal | Type | Detail file | Orientation |
|--------|------|-------------|-------------|
| Near-zero knowledge of a domain, market, product category, body of literature, or technology; need orientation or option selection | **Exploratory** | [exploratory](references/exploratory.md) | Forward-looking / theoretical |
| Object understood; need a plan, protocol, purchase or requirements spec, acceptance criteria, or estimates | **Descriptive** | [descriptive](references/descriptive.md) | Forward-looking / theoretical |
| Object understood; need the cause of an observed change or failure from recorded evidence (logs, symptoms, price history, trial data) | **Experimental** | [experimental](references/experimental.md) | Backward-looking / practical |

Rules:

- Exploratory + descriptive = theoretical (understand future application; no working artifact required).
- Experimental = practical (learn from historical/recorded data of a working system).
- **Never** use experimental when the object is not yet understood; conclusions will be wrong at a fundamental level.
- Poor exploratory work surfaces as surprises during descriptive work. Good exploratory work makes descriptive work precise.

Typical chaining: Exploratory (pick a category or method) → Descriptive (spec or protocol) → Experimental (diagnose after it goes wrong).

The historical experimental label is this plugin's convention, not a definition of all scientific experimentation. Do not force a broad literature review or prospective study into a regression workflow. First explore unfamiliar fundamentals, then use the appropriate domain method. If several modes are needed, finish each bounded phase before the next.

## Research pyramid — execute in order

### Step 1 — Establish canon

Identify sources closest to the claim. Rank every source you intend to use:

| Rank | Source class | How to reach it (default → fallback) |
|------|--------------|--------------------------------------|
| 1 | **Originating source** — the party that created the thing or the data | Software: maintainer changelog, RFC, commit history. Product: manufacturer spec sheet, manual, recall notice. Science: the original study and its dataset or registry entry. Appliance: service manual and error-code table for the exact model. Market: the company's own filings, transcripts, insider transaction reports, official statistics |
| 2 | **Authoritative reference** | Official documentation, standards bodies, regulators, systematic reviews and guidelines, consumer-safety databases, exchange or central-bank publications. A docs MCP (for example Context7) when the subject is a library; otherwise the official site via web fetch/search |
| 3 | **Direct inspection** | Source code, raw data, the physical device (model plate, symptoms, measurements), live listings captured with date and price, price and volume history |
| 4 | **Secondary sources** | Blogs, tutorials, reviews, forums, analyst commentary, retailer summaries; always mark as rank 4 |

For intended behavior, prioritize the originating source, versioned official documentation, and direct inspection; use secondary explanations for context. Do not infer private author intent. For actual behavior, exact-version observations and reproducible evidence can establish a defect or discrepancy with the intended contract. Record both rather than declaring one nonexistent.

A research method is not a guarantee that a vendor, author, or single study is correct. Record the ranked source list and why each source fits this question.

If the subject is a third-party product, study, device, market, library, or platform, at least one rank 1–2 source is mandatory. Reading only listings, reviews, abstracts, headlines, or a local copy of code is not enough to establish canon.

If a source class is unreachable in the current environment (no web access, no repository, no docs tool), write `unavailable` next to it in the charter. Conclusions that would depend on it are reported as **unverified**, not as facts.

Output: the ranked list, posted before collection starts.

### Step 2 — Define interpretation rules (the charter)

Post the charter as a message **before the first data-collection action**. Format:

```
Charter
- Goal: <verifiable outcome>
- Scope / Object / Subject: <...> / <...> / <...>
- Type: <exploratory | descriptive | experimental> — because <one sentence>
- Questions: Q1 <...>; Q2 <...>; ...
- Sources: <ranked list from Step 1, with `unavailable` marks>
```

Length rule:

- **Small task** (single subject, expected ≤5 sources, no third-party unknowns): the five lines above are the whole charter. Still post them.
- Anything else: full charter, and each question gets its own line so the ledger can reference it.

Most common failure: treating personal knowledge as canon and skipping this step. A charter written after collection is not a charter; it is a rationalization.

### Step 3 — Execute research and record findings

1. **Read the bundled type file** for the chosen mode: [exploratory](references/exploratory.md), [descriptive](references/descriptive.md), or [experimental](references/experimental.md). An inlined `SKILL.md` does not include them. If the file cannot be read in the current environment, say so and follow the type's steps as summarized in the selection table. Keep the conversation [research record](references/research-record.md) for the required ledger and any optional expansion. Prefer structured notes in the current conversation unless an artifact was requested. Do not require a local filesystem, shell, background daemon, or persistent database.
2. **Keep a findings ledger** and append to it after every batch of reads, lookups, or observations. One row per claim:

```
| # | Claim | Evidence (file:line / URL / version / commit / PMID / model+date) | Rank | Answers |
|---|-------|-----------------------------------------------|------|---------|
| F1 | Plugin rejects ids > Int.MAX_VALUE | LocalNotification.kt:131, @capacitor/local-notifications 8.3.1 | 3 | Q1 |
| F2 | One 12-week RCT reported HbA1c change of −0.5% vs control | PMID 12345678, parallel-group RCT, n=74 | 1 | Q1 |
| F3 | Model X lists 180-minute runtime on hard floors | manufacturer spec sheet, model X, captured 2026-09-18 | 1 | Q2 |
```

   A finding without evidence is a hypothesis; put it in a separate `Open` list, not in the ledger. Re-reading a source you already have a ledger row for is a signal that the ledger is incomplete: fix the row, do not re-read.
3. **Stop collecting** when every charter question has at least one rank 1–3 row, or is explicitly marked *unanswered*. Unanswered questions go to Step 6 as risks, never as guesses.

Distinguish retrieved facts, observations, inferences, assumptions, and unknowns. Search snippets locate evidence; open the source before treating it as verified. Track inaccessible sources. Use timestamps and exact versions when relevant. Seek evidence that could overturn the leading answer.

Output: the ledger (table) plus the `Open` list. No conclusions yet.

### Step 4 — Filter by scope context

Review every ledger row against the **scope**. Discard or revise rows that ignore domain constraints, history, or cross-cutting principles valid at this level.

Ask: "Does this hold within the broader domain, not just in this narrow case?"

Output, always posted even when nothing changes:

```
Scope filter: discarded F<...> because <...>; revised F<...> to <...>.
```
or
```
Scope filter: nothing discarded — <one sentence why the rows already respect the domain>.
```

### Step 5 — Filter by object context

Review surviving rows against the **object**. Discard or revise rows distorted by imperfect research conditions or over-generalized from the subject.

Ask: "Does this apply to the target system/component, not just the specific artifact I studied?"

Output, same format as Step 4, always posted. Record where a conclusion stops applying. Resolve cross-subject contradictions or retain them explicitly as unresolved.

### Step 6 — Formalize and hand off

Produce final, verifiable conclusions. Every conclusion cites the ledger rows it rests on. Every unanswered charter question appears as a risk with a proposed way to close it.

Before delivering, apply the review procedure in [evidence review](../evidence-review/SKILL.md). Lead with the answer, then the evidence needed to assess it. Include decision-relevant uncertainty, alternatives, acceptance criteria, and next steps. Cite the page or supplied artifact supporting each material claim. Never fabricate references, test runs, estimates, or numerical confidence.

The deliverable must contain these sections in this order, regardless of where it lives (chat reply, plan document, spec file, issue comment):

```
## Charter
## Canonical sources
## Findings ledger
## Scope filter
## Object filter
## Conclusions            <- each item: statement + ledger refs
## Next steps / Risks     <- or Implementation steps + Acceptance criteria for a plan
```

When the deliverable is an implementation plan, the research sections above go **first**, then the implementation steps. Use the output template of the chosen type file for the type-specific content (comparison table, acceptance criteria, classification table).

Use [research handoff](../research-handoff/SKILL.md) when the user wants implementation-ready output or a continuation record. Applying a recommendation requires authorization for the actual change; do not silently turn research into implementation.

## Anti-patterns

| Anti-pattern | Effect |
|--------------|--------|
| Collecting before the charter is posted | Charter becomes a post-hoc story; research type is chosen to fit what was found |
| "This task is small, I'll keep the charter in my head" | Steps 4–6 become unverifiable; the most common way the pyramid collapses |
| Skipping steps 4 or 5 or posting them as an empty heading | Narrow-case conclusions ship as general truths |
| Listings, reviews, abstracts, headlines, or local code as the only canon | Version, population, and originating intent are invisible; fixes target symptoms |
| Treating a price move after news as its cause | Association reported as mechanism |
| Findings held in memory instead of the ledger | Repeated reads of the same files; conclusions cannot be traced to evidence |
| Wrong research type | Micromanagement or endless unfocused reading |
| Fit results to a predetermined answer | Wasted effort; false confidence |
| "My knowledge is canon" | Skips interpretation rules; no external verification |

Research exists to produce **repeatable, checkable outcomes**, not activity for its own sake.

## Completion and efficiency

Stop when each material question is supported or explicitly unresolved and the stated acceptance criteria are met, or when an identified access/data limitation prevents further progress. A second search that adds no decision-relevant evidence is a reason to reassess, not repeat indefinitely. Do not claim exhaustive coverage without a documented search boundary.

Scale depth to consequence and user constraints. Batch independent retrievals when the host supports it; reuse sources only within their date/version scope. Do not require subagents. Give short updates at meaningful milestones. Honor explicit time or token budgets; if exact usage is unavailable, say so and use bounded research phases, never invented counters. Keep concise continuation notes when interrupted; do not automatically create a new chat or schedule monitoring.

## Capability fallback

Use only tools actually exposed by the host. If an optional MCP is absent, use official web sources. If browsing is absent, analyze available files and clearly limit claims to them. If an experiment cannot run, supply a protocol or analyze historical records and label it unexecuted. Never report cloud/mobile installation, persistent storage, or tool availability merely because a configuration file exists.
