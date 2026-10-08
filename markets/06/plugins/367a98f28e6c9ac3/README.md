# Lifetime Core Championship — Public Plugin v1.0.4

Public, skills-only market-research build of Lifetime Core Aggressive Championship.

## v1.0.4 patch

- preserves the v1.0.2 block on personal-account sizing and security-specific capacity math;
- adds a transaction-language firewall: the plugin must not tell a user to transact **or refrain from transacting**;
- blocks negative directives such as “do not buy,” “wait to buy,” and “not yet”;
- disables public-facing legacy aliases such as “FIND WHAT IS ACTUALLY BUYABLE RIGHT NOW” and “RUN [TICKER] EXECUTION READINESS”;
- reinterprets any legacy execution-style request as a neutral **RESEARCH STATUS REVIEW**;
- removes execution states such as ARMED / FIRE / EXECUTABLE from public outputs and uses descriptive technical states instead;
- prohibits entry zones, stops, profit targets, order types, order timing, and execution plans;
- allows only neutral research references such as support/resistance, technical confirmation thresholds, invalidation, and scenario ranges;
- keeps CHAMPIONSHIP RESULT separate from the security-only Spotlight Watchlist.

The preserved canonical source remains under the skill references for lineage; `public-compliance-overlay.md` controls public behavior when the original doctrine conflicts with these boundaries.

- v1.0.4 adds a runtime canonical firewall and broker-email/account-source firewall, plus a transaction-request short circuit before tool use.
