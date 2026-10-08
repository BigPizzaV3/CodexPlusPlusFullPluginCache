# Scoped frontend code-hygiene gate

Use this gate for implementation, repair, refactor, and completion verification. Its purpose is to leave the affected frontend simpler and more canonical without converting a UI lane into an unsafe repository-wide rewrite.

## Set the boundary

Cover:

- files changed by the lane;
- components, hooks, utilities, styles, tokens, fixtures, and tests they directly depend on;
- existing alternatives that perform the same affected responsibility;
- shared code changed to fix the root cause.

Inspect wider code only far enough to establish reuse, references, ownership, and regression risk. Record unrelated debt rather than editing it. Respect lane ownership and active parallel work.

Before coding, identify the current canonical implementation and search for existing components, hooks, utilities, styles, tokens, tests, and APIs that already solve the need. Establish a focused baseline from the repository's available type, lint, test, build, browser, bundle, or dependency checks. Do not introduce a second implementation merely because discovery was incomplete.

## Prefer one canonical path

Within scope:

- extend or repair a sound shared implementation instead of copying it;
- consolidate materially equivalent logic, markup, styling, state, or transformations when doing so preserves behavior and makes ownership clearer;
- remove the superseded implementation, obsolete compatibility path, unused import or export, abandoned style rule, stale fixture, and invalidated test once the replacement is verified;
- keep deliberate variants when they serve different product behavior, accessibility semantics, performance needs, or lane ownership, and state why they are not duplicates;
- avoid speculative abstractions: a small repeated fragment is not automatically a reusable component.

Do not mix mechanical cleanup with behavioral change when separating them would make review or rollback safer.

## Check for stale, duplicate, and overridden code

Use repository-aware searches and the project's own tooling where available. Examine the affected scope for:

- duplicate or near-duplicate components, hooks, utilities, formatters, constants, and state derivations;
- copied JSX or CSS that should use an existing primitive or token;
- unused imports, exports, props, state, effects, branches, files, dependencies, fixtures, mocks, tests, and feature flags;
- old code paths that remain reachable after a replacement;
- selectors, declarations, tokens, media queries, or utility classes that override one another accidentally or can no longer win;
- multiple sources of truth, shadowed values, repeated transformations, and state that can be derived safely;
- unnecessary effects, render-triggering state, repeated expensive work, unstable identities, avoidable client code, and oversized imports when they have a measurable or well-supported cost;
- comments, names, tests, stories, and documentation that describe behavior the lane changed.

Treat tool output as evidence, not proof. Static analysis may miss dynamic imports, framework conventions, CSS reachability, runtime registration, reflection, generated references, or externally consumed exports.

## Delete safely

Before deleting or consolidating code:

1. Search all relevant references, including tests, stories, dynamic registration, route configuration, exports, CSS usage, and framework conventions.
2. Check git history or active authority when the code's purpose is unclear.
3. Confirm that another active lane does not own or depend on it.
4. Run the most focused check that would fail if the removal were wrong.
5. Re-run the affected rendered journey and relevant wider gates after removal.

If use cannot be disproved confidently, do not delete. Mark it as suspected stale code with the exact uncertainty and the check needed to resolve it. Never claim that the repository contains no duplicate, stale, overridden, or inefficient code unless the inspected coverage supports that claim.

## Efficiency standard

Optimize for understandable behavior, fewer sources of truth, and work avoided on real user paths. Do not apply memoization, code splitting, virtualization, caching, or abstraction by reflex. Require a supported bottleneck, meaningful scale risk, or clear simplification benefit. Preserve correctness, accessibility, and server-authoritative behavior ahead of micro-optimizations.

When performance is material, compare an appropriate before and after signal such as render count, interaction latency, network requests, bundle contribution, layout shift, or browser profile. If measurement is unavailable, label the improvement as an inference rather than a measured result.

## Dependency gate

Apply this gate when the lane would add, replace, or materially upgrade a runtime or development dependency. Prefer the platform, browser, framework, and packages already accepted by the repository when they meet the need. Treat a new dependency as a planned lane decision, not incidental implementation detail. If the accepted lane did not name it, pause before installation and present the need, alternatives, costs, and removal route.

Before accepting a dependency, establish from the package's authoritative source and repository evidence:

- the exact package identity, owner, licence, version, release and maintenance status, and compatibility with the current framework and runtime;
- whether an existing dependency or small local implementation safely solves the same problem;
- known relevant advisories, risky install scripts, transitive dependency growth, and lockfile changes;
- browser versus server execution, data egress, telemetry, permissions, and any effect on client data;
- client bundle and runtime cost where the dependency can reach the browser;
- version-pinning, update ownership, rollback, replacement, and clean removal.

Use current official documentation or package metadata for time-sensitive claims. Treat audit tools and popularity as signals, not proof of safety. Do not suppress an advisory, waive an incompatible licence, or accept unexplained lockfile churn merely to make the build pass.

After an approved change, inspect the manifest and lockfile diff, run the relevant install, type, test, build, browser, and bundle checks, and confirm that removal remains possible. Report the dependency decision and continuing maintenance owner.

## Completion evidence

Report:

- the canonical implementation retained;
- duplicate, stale, overridden, or inefficient code found;
- files, exports, rules, dependencies, flags, fixtures, or tests removed or consolidated;
- searches, static checks, focused tests, rendered checks, and wider gates run with their results;
- deliberate duplication retained and why;
- suspected debt not changed, including ownership or evidence gaps;
- whether efficiency claims are measured, directly inferred, or still unknown.

A green lint, typecheck, or build is necessary when relevant but does not by itself prove that the code is clean, efficient, or free of stale paths.
