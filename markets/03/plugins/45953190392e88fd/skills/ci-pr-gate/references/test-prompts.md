# Test prompts for `ci-pr-gate`

Run these manually in ChatGPT Developer Mode (with the npmscan MCP server
connected) before uploading this skill, per OpenAI's "Test the skill"
guidance. Every case checks two things: did the right tool(s) get called,
and did the response actually come back as the `GATE:` contract (not a
conversational report) with the correct verdict. Most fixtures below were
run live against the real npm registry/OSV.dev/CISA-KEV/FIRST-EPSS during
authoring — exact figures noted are what came back at that time; registry
state can drift, so re-verify a fixture's raw tool output first if a case
stops matching.

1. **Clean PASS — a fix, via a snapshot diff.** Paste:
   > before: `{ "dependencies": { "minimist": "1.2.5" } }`
   > after: `{ "dependencies": { "minimist": "1.2.6" } }`
   and ask "Gate this PR — is it safe to merge?"
   `diff_dependencies` should return `changeType: "upgrade"`,
   `vulnerabilityDelta: "fixed"`, `installScriptIntroduced: false`. Expect
   `GATE: PASS`, and the table's reason naming CVE-2021-44906 as fixed by
   the bump to 1.2.6 — not a bare "no issues."

2. **FAIL — severity overrides a low remediation tier (the core policy
   case).** Paste:
   > before: `{ "dependencies": { "minimist": "1.2.6" } }`
   > after: `{ "dependencies": { "minimist": "1.2.5" } }`
   and ask "Gate this dependency change."
   `diff_dependencies` returns `changeType: "downgrade"`,
   `vulnerabilityDelta: "introduced"`, `highestSeverity: "CRITICAL"`
   (CVE-2021-44906). Feeding that into `prioritize_remediation` returns
   `tier: "monitor"` (confirmed live: EPSS ~4.6%, not KEV-listed, `score:
   11.37`) — a *low* remediation tier despite CRITICAL severity. Expect
   `GATE: FAIL` anyway, with the blocking reason naming the CVE and
   severity directly (not "ranked low priority, passing"). This is the
   one case that most needs to be right: it's the exact scenario the
   severity-override FAIL rule exists for.

3. **FAIL — KEV override, independent of severity string.** Ask the model
   to rank (via `prioritize_remediation`) a finding
   `{ packageName: "log4j-core-fixture", cveId: "CVE-2021-44228", severity:
   "CRITICAL" }` alongside `{ packageName: "is-number", severity: "LOW" }`,
   framed as "these are the vulnerability findings from my dependency
   diff — gate this PR." Expect `tier: "patch-now"` for the KEV-listed
   finding (CISA KEV since 2021-12-10, confirmed live at `score: 100`) to
   produce `GATE: FAIL` with that package named as the blocking reason,
   and `is-number` (tier `"monitor"`) listed separately as, at most, a
   warning — not folded into the same blocking line.

4. **FAIL — install script introduced on a routine-looking bump.** This
   fixture is deliberately not pinned to one hardcoded package/version
   pair, since npm frequently unpublishes exactly this shape of malicious
   release (confirmed while authoring: a real historical case,
   `ua-parser-js` 0.7.29, no longer resolves via `get_package_version` —
   npm removed it after the 2021 supply-chain compromise). Instead: pick
   any package, call `get_package_version` on two consecutive versions
   to find a pair where the earlier one's `scripts` has no
   preinstall/install/postinstall/prepare key and the later one does,
   then ask "Gate a bump from `<earlier>` to `<later>`." Expect
   `simulate_dependency_upgrade`'s `installScriptIntroduced: true` to
   produce `GATE: FAIL` — even though that tool's own `riskTier` only
   escalates this signal to `"review-recommended"` (confirmed against
   `rules-test.ts`'s own fixture: `installScriptIntroduced: true` alone
   never reaches that tool's `"breaking-change-likely"` tier). The point
   of this case is confirming the skill applies its own stricter,
   security-specific FAIL rule on the raw field rather than deferring to
   that tool's blended breaking-change/security tier.

5. **WARN — a real major bump, otherwise clean.** Ask to gate a bump from
   lodash 3.10.1 to 4.17.21. `simulate_dependency_upgrade` returns
   `semverBump: "major"`, `isBreakingBySemver: true`,
   `riskTier: "breaking-change-likely"`, with a clean OSV check on both
   sides. Expect `GATE: WARN` (not FAIL — nothing here is a security
   finding) with the reason naming the major-version jump, not a vague
   "risky."

6. **WARN — pre-1.0 minor bump flagged breaking by semver convention.**
   Ask to gate chalk 0.4.0 → 0.5.0. Expect `semverBump: "minor"`,
   `isBreakingBySemver: true`, `zeroMajorNote` explaining the pre-1.0
   convention — and `GATE: WARN` citing that note, not treating a "minor"
   bump as automatically safe.

7. **WARN — unresolved target, never silently PASS.** Ask to gate lodash
   4.17.21 → `^999.0.0`. `simulate_dependency_upgrade` returns
   `direction: "unresolved"`, `resolvedTargetVersion: null`, a non-null
   `targetVersionNote`, `riskTier: "unknown"`. Expect `GATE: WARN` with
   the row's reason being the resolution note itself — explicitly not
   `GATE: PASS` just because nothing concrete was found wrong.

8. **PASS — cross-format diff, no false positive.** Paste before
   `{ "dependencies": { "lodash": "^4.17.21" } }` (package.json) and after
   a `package-lock.json` pinning lodash at exactly `4.17.21`. Expect
   `diff_dependencies` to return `changed: []` (both sides resolve to the
   same version) and `GATE: PASS` with an empty "all packages checked"
   table or a single "no dependency changes detected" line — not a
   fabricated WARN over a text-level difference that isn't a real version
   change.

9. **Multi-package batch — overall verdict is the worst single result.**
   Ask to gate three named bumps in one PR: minimist 1.2.5→1.2.6 (clean
   patch fixing a CVE), lodash 3.10.1→4.17.21 (major, clean OSV), chalk
   0.4.0→0.5.0 (pre-1.0 minor, clean OSV). Expect three
   `simulate_dependency_upgrade` calls, one combined table with minimist
   at PASS and the other two at WARN, and an overall `GATE: WARN` — not
   `PASS` (a clean package shouldn't average out a WARN elsewhere) and not
   `FAIL` (nothing here actually triggers a FAIL rule).

10. **Non-triggering — same fixture, no gate/verdict framing.** Paste the
    same before/after from case 1 and ask "What changed between these two
    package.json files?" with no mention of merging, blocking, CI, or a
    gate. Expect `dependency-audit`'s conversational diff flow to answer
    instead — no `GATE:` line, no PASS/WARN/FAIL contract.

11. **Nothing to gate.** Ask "Can you gate my dependency PR?" with nothing
    pasted and no package named. Expect a clarifying question asking for
    the before/after snapshots or the specific bump(s) — no tool call, and
    critically no fabricated `GATE:` line over data that doesn't exist.

12. **`still-vulnerable` → WARN, not FAIL (a version bump that doesn't
    cross the fix line).** Paste:
    > before: `{ "dependencies": { "minimist": "1.2.3" } }`
    > after: `{ "dependencies": { "minimist": "1.2.5" } }`
    (both versions are `<1.2.6`, so both remain vulnerable to
    `CVE-2021-44906`) and ask "Gate this PR." Expect `diff_dependencies` to
    report `vulnerabilityDelta: "still-vulnerable"` (not `"introduced"` —
    the CVE predates this bump) and `GATE: WARN` — not `FAIL`, since this
    PR isn't what introduced the vulnerability, and not silently omitted
    either. **Note:** `"still-vulnerable"` has no dedicated live fixture in
    the repo's own test suite (only `"fixed"` and `"introduced"` are
    live-tested) — verify the tool's real return value for this pair
    before relying on the case.

13. **Downgrade with no vulnerability reintroduced → WARN, not FAIL or
    PASS.** Ask to gate a bump from lodash 4.17.21 to 4.17.20 (a real,
    clean patch-level downgrade — confirmed live: no OSV vulnerability on
    either side). Expect `changeType: "downgrade"`,
    `vulnerabilityDelta: "still-clean"`, and `GATE: WARN` citing an
    unexplained version decrease as worth a reviewer's eyes — not `FAIL`
    (nothing security-relevant changed) and not `PASS` (the Gate policy
    explicitly flags a bare downgrade). This is the direct clean contrast
    to case 2, which correctly FAILs a downgrade that reintroduces a real
    CVE.

14. **`resolutionNote` on the diff path (a git dependency).** Paste:
    > before: `{ "dependencies": {} }`
    > after: `{ "dependencies": { "my-fork":
    > "git+https://github.com/example/my-fork.git" } }`
    and ask "Gate this PR." Expect `diff_dependencies` to return
    `afterVersion: null` and a `resolutionNote` containing "git
    dependency," and `GATE: WARN` with that note as the row's reason —
    never `PASS` just because nothing concrete resolved, and never a row
    dropped from the table.

15. **`targetDeprecated` / `engineChange.tightened` / `targetIsPrerelease`
    — raw-field WARN rules independent of `simulate_dependency_upgrade`'s
    own blended tier.** These three fields are only asserted in the tool's
    internal unit tests, not against any live package in this repo's test
    suite, so construct the fixture live before running: call
    `get_package_version` across a few consecutive versions of any package
    until you find one where (a) the target version is marked deprecated,
    (b) `engines.node` tightens between versions (e.g. `>=14` → `>=18`), or
    (c) the target is a published `-beta`/`-rc`/`-alpha`. For each, ask
    "Gate a bump to `<that version>`." Confirmed from `rules-test.ts`: none
    of these three alone escalate `simulate_dependency_upgrade`'s own
    `riskTier` past `"review-recommended"` — but `GATE: WARN` should fire
    anyway, citing the specific raw field by name. Same "apply our own
    stricter rule on the raw field, don't defer to the tool's blended
    tier" pattern already covered for `installScriptIntroduced` in case 4.

16. **Two pre-existing findings at different remediation tiers, both
    correctly WARN but distinguishable.** This repo's own tests only
    exercise `prioritize_remediation`'s `patch-now` (KEV) tier and an
    implicit `monitor` tier live — `patch-soon`/`scheduled` have no live
    fixture. Before relying on this case, use `get_cve` to find two real,
    non-KEV CVEs on packages already present unchanged in the "before"
    snapshot (so both are `still-vulnerable`, not introduced): one ranking
    `"scheduled"` via `prioritize_remediation` (roughly CRITICAL/HIGH
    severity with EPSS ~17%+) and one ranking `"monitor"` (very low EPSS,
    like the existing minimist CVE-2021-44906 fixture at ~4.6%). Gate a
    diff touching both. Expect `GATE: WARN` overall, both findings present
    in the table, and the response naming which one ranks `"scheduled"`
    vs. `"monitor"` rather than collapsing both to an identical
    "pre-existing, not our fault" line.
