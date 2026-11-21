# SigRank | SignalAF — V1 candidate

## 0.1.32 update

Adds token telemetry, token-count and operator-benchmark discovery wording, plus a [July 2026 reference-field guide](skills/sigrank-analyst/references/july-reference-field.md). The frozen 1,642-profile field is a substantial proof-of-concept comparison cohort, distinct from the live production board. Current MCP tools still have no archive dataset selector. This package update changes instructions and listing metadata, not server tool behavior. See [release notes](RELEASE_0.1.32.md) for validation and publication status.

**Performative stats and benchmarks for AI users, not models.**  
**AI Operator Leaderboard**

**Tokenpull measures → SigRank evaluates → SignalAF publishes.** This plugin explores, interprets and communicates existing public SignalAF facts. The launch experience uses one Active / Total / All-time board snapshot and explains the methodology, operating ratio, aggregate I/O/W/R token pillars, ten Build Archetypes, and relevant SignalAF articles. A current-rule archetype computed from complete I/O/W/R is labeled **derived**, because the live public profile tool does not publish an archetype label. The plugin mirrors the published board; it does not independently verify uploads, classify measurement evidence, scan logs, create a published ranking, enroll an operator, or submit measurements. The existing submission MCP remains separate.

The V1 remote server is `https://analyst.signalaf.com/api/plugins/sigrank/mcp` with four public analyst reads and one no-auth beta-support action: `get_leaderboard`, `get_operator`, `compare_operators`, `get_field_stats`, `report_beta_bug`. The report sends an email only after approval of its contents. There is no remote `get_my_profile` or OAuth. In Codex, an optional local read of `~/.sigrank-mcp/identity.json` extracts only a codename, then uses public `get_operator`. ChatGPT asks for a public codename.

Start with `BUILD_DIRECTIVE.md` and `SOURCE_MAP.md`; the exact tool schemas live in `sigrank-app/lib/mcp/plugin/contracts.json` and are explained in `MCP_CONTRACTS.md`. The skill is in `skills/sigrank-analyst/`; the beta helper is in `skills/beta-troubleshooter/`. `ANALYST_FIXTURES.json` contains 20 synthetic profiles and `ANALYST_EVALUATION.md` is the behavior rubric. `TOKENPULL_V2.md` is a deferred design reference, not shipped measurement behavior.

The candidate adds `skills/get-started/` for a bare plugin invocation, plus `ONBOARDING_VISION.md` for the broader first-contact narrative. The greeting introduces the field and offers conversation paths without guessing live rankings or making claims about human ability. Verify it in a fresh ChatGPT and Codex conversation before publishing.

`STATUS.md` distinguishes implemented, deployed and still-unverified work; `HOST_TEST_REVIEW.md` and `HOST_TEST_REVIEW_0.1.13.md` assess owner-provided ChatGPT answers. `HOMEPAGE_METRIC_AUDIT.md` records the former homepage median-Yield source conflict and deployed repair. `TEST_PLAN.md` and `PUBLIC_REVIEW_CASES.md` are the release gates. User-supplied token-count interpretation remains optional beta guidance, not a tested launch calculator or board-placement feature. The package is **not publicly submitted or approved** until fresh ChatGPT/Codex behavior tests and the current review process pass.
