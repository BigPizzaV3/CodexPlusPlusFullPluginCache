# RICS "Responsible Use of AI" — Compliance Support Guide

**The standard:** *Responsible use of artificial intelligence in surveying practice*, RICS
professional standard (global), 1st edition, published September 2025, **in force since
9 March 2026**. It is mandatory for all RICS members and RICS-regulated firms, in all
jurisdictions. Where local legislation (e.g. the EU AI Act) conflicts, legislation prevails —
but the firm must record the conflict and report it to RICS (§1.2).

**Why it applies to this plugin's users:** the standard bites on AI outputs with a **material
impact** on the delivery of a surveying service. Its own examples — outputs summarising
documents later relied on in a report, composing all or significant parts of an opinion,
recommending what to investigate — map directly onto what this plugin produces: valuations,
CVRs, delay registers, CE notifications and quotations, claims narratives, contract guidance.
**Assume material impact.** If a firm judges a particular use non-material, §1.2 still
requires that determination and its reasoning to be recorded in writing.

**What this document is:** a map from each of the standard's requirements to (a) what the
plugin already does to support it, (b) what Gather supplies on request, and (c) what remains
the firm's own obligation — because RICS obligations sit with the member/firm, not the tool.
No tool can make a firm compliant. This document is compliance support, not legal advice.

---

## Who does what

| Party | Role under the standard |
|---|---|
| **The RICS member/firm** | Owns every obligation: governance policies, AI-use register, risk register, reliability decisions, client disclosure, training. |
| **Gather** (this plugin + the Gather MCP server) | The procured third-party tool. Answers §4.1 due-diligence requests for the plugin and MCP layers; designs outputs so §4.2 reliability decisions are easy to make and evidence. |
| **Anthropic** (the assistant, via ChatGPT Work) | The underlying AI system. Model-level due-diligence items (training data, safety, data handling, environmental reporting) come from Anthropic's published documentation — see §4.1 below. |

A useful framing for the firm's records: the **AI system** is the assistant as deployed through
ChatGPT Work; the **Gather plugin** is methodology that constrains and directs it (skills,
agents, guardrails, verification patterns); the **Gather MCP server** is a read-only data
connection to the firm's own project records. All three belong in the §3.2 register entry.

---

## Section-by-section

### §2 — Baseline knowledge

Members must maintain a basic understanding of how the AI works, its limitations and failure
modes, erroneous-output risk, bias risk, and data risks. **Plugin support:** the README's
Current Limitations section, `docs/SKILL_REFERENCE.md`, and the standing caveats on every
output state limitations explicitly and honestly (no cost/value data via the API, no CPM
recomputation, records-gap-vs-absence discipline, fabrication guards). These are suitable
source material for the firm's own training. **Firm's obligation:** actually run the training,
at least annually for staff involved (§3.2).

### §3.1 — Data governance

The must-nots here are the firm's: secure storage, restricted access, annual training, and
**no uploading of private/confidential data to AI systems without express written consent in
advance from affected stakeholders plus a reasonableness assessment**. Points the firm's
assessment should cover, and what the plugin does to help:

- The Gather MCP connection is **read-only** and OAuth-authenticated — the plugin analyses
  records; it cannot create, modify, or delete them.
- Commercially sensitive local files (`commercial-profile.md`, `commercial/cost-ledger.md`)
  stay on the firm's own machine; the creating skills remind users to keep them out of shared
  repositories, and outputs destined for the other party never include them (Patterns 14/16).
- Site diary data routinely contains **personal data** (names and recorded hours). The
  firm's §3.1 assessment should cover both the Gather platform's own processing and
  Anthropic's processing of conversation content — Anthropic's commercial terms and trust
  documentation (trust.anthropic.com) address retention and training use; verify the position
  for the firm's specific plan rather than assuming it.

### §3.2 — System governance (appropriateness assessment, AI-use register, policies)

All firm-side. A ready-to-adapt register entry:

> **System:** the assistant (Anthropic), deployed via ChatGPT Work with the Gather plugin v[X.Y.Z] and
> the read-only Gather MCP server. **Purpose:** analysis of site diary records for commercial
> management — valuations, CVRs, delay/claims evidence packs, contract procedure guidance —
> all outputs drafts for named-surveyor review. **First used:** [date]. **Next review:**
> [date — the standard expects a stated review date].

The plugin's version discipline helps here: `plugin.json` is the single version authority and
the CHANGELOG records what changed in each release, so the register can pin and review a
specific version.

### §3.3 — Risk register (quarterly review)

Firm-side, but these starter rows reflect how the plugin's design maps to the overarching
risks the standard names:

| Risk | Plugin-level mitigation (cite in the register) | Residual firm action |
|---|---|---|
| Erroneous output | Fabrication guards (no invented rates, costs, dates, mappings, accruals); every figure record-cited or labelled user-supplied; four-verdict verification discipline; cross-register reconciliation with stated tolerances | Named-surveyor review of every relied-on output (§4.2) |
| Recording gap read as fact | "Records do not support" / "recording gap ≠ absence" language enforced across skills | Check gaps against non-Gather sources before relying |
| Bias | Outputs are grounded in the firm's own project records, not population-level training generalisations; contract clauses are source-verified | Dip-sample for systematic skew (e.g. always-favourable variance framing) |
| Input-data retention | Read-only MCP; local sensitive files; provider retention terms | Confirm Anthropic/Gather retention positions for the firm's plan |
| Tool drift between versions | Semver + CHANGELOG + pinned register entry | Re-review on version change |

### §4.1 — Procurement due diligence

The standard requires written requests to the supplier covering six items. Where the answers
live:

| Mandatory request | Answer source |
|---|---|
| Environmental impact | Anthropic's published environmental/sustainability reporting (model layer); the plugin itself adds no compute beyond the assistant usage |
| Stakeholders involved in development | Gather Insights (plugin + MCP server); Anthropic (model) |
| Compliance with data/confidentiality laws | Gather's data-processing documentation for the MCP server; Anthropic's trust centre and commercial terms for the model layer |
| Permissions for individuals' data/content | **The plugin contains no trained model and trains nothing on customer data** — it is prompt-layer methodology. Model-layer training-data questions are Anthropic's to answer via published documentation |
| Training-dataset accuracy/diversity/bias | As above — model layer. Plugin layer: contract knowledge is source-verified (e.g. against the GMH Planning/CECA NEC library) and the verification record is in the repo (`internal/nec4-source-review.md`) |
| Supplier liability | The plugin LICENSE (proprietary Gather customer licence); Gather's customer agreement; Anthropic's commercial terms |

Firms should send the requests in writing and keep the responses (§4.1 requires the record,
and unanswered items go on the risk register). Gather's practical fitness-for-purpose evidence
worth recording: the live model-in-the-loop fixture suite in `tests/` (graded transcripts with
must-not regression checks) — this is exactly the "extent of practical testing" record §4.1
asks firms to keep.

### §4.2 — Output reliability decisions (the core operational duty)

Every material-impact output needs professional judgement applied and a **written reliability
decision by, or supervised by, a named qualified surveyor who accepts responsibility** —
covering assumptions, concerns, and a conclusion on fitness for purpose. The plugin's output
contract is designed to make that decision fast to write:

- **Assumptions are stated in-line** (date parsing, rate sources, column semantics, first-CVR
  positions, non-interactive assumptions) — the decision's "assumptions" section can quote them.
- **Every figure is traceable** — record IDs per line, "per commercial profile" /
  "user-supplied this session" / "per the imported cost ledger" citations, and session-local
  Ref numbers (`AP-001`, `CV-001`, …) for cross-referencing the decision to the output.
- **Gaps & caveats sections are mandatory**, not optional — the "key areas of concern" section
  of the reliability decision can be lifted from them.
- **HTML deliverables carry `Prepared by` / `Reviewed by` signature lines** and an explicit
  "Prepared with AI assistance" footer — the named-surveyor adoption is visible on the face of
  the document.
- **Dip-sampling** (the §4.2 route for high-volume/automated use, e.g. scheduled routines):
  session transcripts plus Ref numbers give a sampling frame; the graded-fixture method in
  `tests/harness/` is a ready-made template for scrutinising a sampled output against a
  written expectation.

**Firm's obligation:** the decision itself, the named surveyor, and — where an output is found
not fit for purpose — telling the client in writing.

### §4.3 — Terms of engagement and client disclosure

Firm-side and unavoidable: clients must be told **in writing, in advance**, when and for what
purpose AI is used, and engagement terms must cover PI position, contest and redress routes,
and any opt-out. Suggested disclosure wording to adapt:

> In delivering commercial management services we use AI assistance (the assistant, via the Gather
> plugin) to analyse our contemporaneous site records and draft commercial documents —
> valuations, reconciliations, delay and event registers, and contract-procedure checks. Every
> AI-assisted output is reviewed and adopted by a named surveyor before it is relied on or
> issued. [PI position]. [Contest/redress route]. [Opt-out position].

The plugin supports the disclosure with the always-on document footer ("Prepared with AI
assistance") — a client can see on the face of a deliverable that the disclosure applied to it.

### §4.4 — Explainability

Firms must be able to provide written information on request: system type, ways of working and
limitations, due diligence done, risk management, reliability decisions. The plugin's standing
written material covers the first two (`README`, `docs/SKILL_REFERENCE.md`,
`../shared/patterns/README.md` — the methodology is inspectable, not a black box); the firm's
§3.2/3.3/4.1/4.2 records cover the rest.

### §5 — Development of AI

Applies to firms **building or training** AI systems. A firm using this plugin as shipped is
not developing AI; §5 is out of scope. (It would be engaged if a firm fine-tuned a model on
its own data — not something this plugin does or requires.)

---

## The firm's own checklist (nothing the tool can do for you)

1. Record the materiality determination for each use (§1.2).
2. Written appropriateness assessment before use (§3.2).
3. AI-use register entry (template above) with a review date (§3.2).
4. Responsible-AI policy: roles, annual training, human-control statement, risk guidance (§3.2).
5. Risk register, reviewed at least quarterly (§3.3).
6. Written due-diligence requests to Gather and reliance on Anthropic's published documentation; file the responses (§4.1).
7. Named-surveyor written reliability decision per relied-on output, or documented dip-sampling for routine/scheduled outputs (§4.2).
8. Terms-of-engagement disclosure before AI-assisted work starts (§4.3).
9. Be ready to answer an explainability request in writing (§4.4).

---

## Sources

- RICS, *Responsible use of artificial intelligence in surveying practice*, 1st ed., September
  2025 (rics.org — professional standards) — the primary text; section references above follow
  its own numbering (it numbers sections, not individual sentences).
- RICS standard landing page: rics.org/profession-standards → conduct & competence →
  responsible use of AI.
- Commentary consulted: CMS Law, Beale & Co, and 4 New Square briefings on the standard
  (consistent with the primary text; they add the professional-negligence framing — courts and
  adjudicators can be expected to treat the standard as the benchmark of reasonable competence
  for AI-assisted surveying work).

*This guide reflects the standard as published and the plugin as at the version in
`plugin.json`. It is not legal advice; firms should take their own advice on regulatory
obligations.*
