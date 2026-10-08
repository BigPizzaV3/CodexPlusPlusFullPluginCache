# Research Methodology Plugin

A portable English-language plugin for evidence-led research across products, scientific literature, device failures, markets, and technology. It answers in the language of the research request. Its four skills cover the six-step research pyramid, source review, implementation/action-plan/continuation handoffs, and Karpathy-inspired working principles.

## Start

Install the package through a distribution route supported by your ChatGPT workspace, then start a new conversation and select Research Methodology. Ask a normal research question or choose the research-methodology skill. Examples:

- "Compare these two approaches against my requirements and show the evidence."
- "Shortlist robot vacuums under my budget for pets and hard floors."
- "What do PubMed trials report on intermittent fasting and HbA1c in adults with type 2 diabetes?"
- "My front-load washer stops mid-cycle after a power outage. What is the most supported cause?"

The default package is skills-only. It requires no local process, terminal, Node.js, Python, API key, or separate hosting at research runtime. It uses the host's available web/file tools and can analyze supplied material without MCP. Live research still needs network access and retrieval tools; this is not an offline search engine.

## Included capabilities

- `research-methodology`: exploratory orientation and option selection; descriptive specifications and protocols; historical experimental causal analysis — for products, literature, devices, markets, and technology.
- `evidence-review`: claim-to-source audit, applicability, contradictions, causal restraint, and domain-specific traps.
- `research-handoff`: decision records, specifications, action plans, protocols, shortlists, and continuation briefs.
- `karpathy-guidelines`: explicit assumptions, simplicity, surgical scope, and verifiable outcomes for code, documents, purchases, repairs, and decisions, plus adapted extensions.

Every research entrypoint explicitly loads the working principles. Cursor's `alwaysApply` field is not treated as a portable global rule.

## Files and distribution

The plugin root is this directory. `.codex-plugin/plugin.json` and `skills/` are the runtime package. `integrations/remote-mcp.json` supplies an optional HTTP configuration, inactive in the default package. `scripts/package.py` produces a skills-only ZIP and a separate remote-MCP ZIP under `dist/`; Python is needed only to rebuild these archives. Both archives contain the manifest at archive root.

Read [installation](docs/INSTALLATION.md) for cloud/mobile distribution, [integrations](docs/INTEGRATIONS.md) for provider choices, [provenance](docs/PROVENANCE.md) for source adaptations, and [validation](docs/VALIDATION.md) for actual checks and remaining live tests.

Cloud-ready architecture does not mean installed in an account. No cloud publication, account configuration, repository upload, or mobile test is performed by building these files. A local folder and a ZIP are not automatic cloud installation mechanisms.
