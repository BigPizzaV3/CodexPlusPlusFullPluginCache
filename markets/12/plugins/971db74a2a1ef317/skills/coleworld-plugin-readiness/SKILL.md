---
name: coleworld-plugin-readiness
description: Assess plugin and MCP release readiness using verifiable evidence. Use for submission preparation, OAuth or discovery troubleshooting, reviewer access checks, positive and negative test plans, release reviews, and preserving shared voice or shortcut memory during updates.
---
# ColeWorld Plugin Readiness

Produce a concise release decision with evidence and prioritized fixes. This skill guides assessment; it does not supply hosting, authentication, publication authority, or an approval guarantee.

## Connected assessment tools

For requests to create, save, list, read, update observations, export or delete an
assessment, read [workspace-tools.md](references/workspace-tools.md) first and use
the connected workspace tools. Follow its exact required fields, methodology and
status mappings, provenance, retry rules and confirmation requirements. Verify
saved state before reporting success. If tools are unavailable, label the result
unsaved and state the blocker.

## Establish the target

1. Classify the package as skills-only, MCP/backend, or mixed. Apply only the gates relevant to that architecture. For a skills-only package, mark server discovery, OAuth, reviewer credentials, and video requirements NOT APPLICABLE when current official rules exempt them; do not invent a backend requirement. General privacy, originality, accuracy, and publication requirements still apply.
2. Identify the exact plugin, organization, environment, endpoint, package version or commit, supported surfaces, and intended audience. Keep similarly named products and staging/production separate.
3. Read current configuration and any existing submission record before proposing a replacement. Do not duplicate, withdraw, or overwrite an in-review submission merely because a newer build exists.
4. Ask only for missing information that changes the assessment. Never request secrets in chat; inspect secret names and configuration presence without exposing values.
5. Consult the official sources in references/sources.md for current requirements. Record the check date. If a source or portal is unavailable, mark that requirement unverified rather than guessing.

## Build the evidence ledger

For each check record: check ID, environment/version, expected behavior, observed behavior, timestamp, redacted evidence location, and status. Use PASS only with observed matching evidence; FAIL for observed mismatch; BLOCKED for an unmet dependency; NOT RUN for unexecuted checks; and NOT APPLICABLE with a reason. A written test plan is not a passing test. Distinguish user-reported results from independently observed results.

Assess these gates:

- Package: valid manifest and referenced paths, accurate description and tool schemas, correct audience, working policy/support links, no embedded credentials or private fixtures.
- Discovery: externally reachable endpoint, valid transport and TLS, initialization and tool listing, schemas matching actual tool behavior, useful errors and bounded retries.
- Authentication: correct authorization-server/resource metadata, registered redirect behavior, applicable PKCE/state protections, token issuer/audience/scope validation, expiry and revocation behavior. Distinguish sign-in identity from API or conversation-data access.
- Authorization: enforce resource ownership server-side. Test another user's object ID, missing privileges, expired/revoked credentials, and missing authentication against protected operations. A successful login or tool annotation does not establish resource authorization.
- Data boundaries: use synthetic reviewer records. Keep personal memory, voice transcripts, shortcut data, other tenants, secrets, and internal logs out of reviewer responses and shared packages. Test both allowed owner access and denied cross-account access.
- Reviewer journey: fresh-session sign-in, authorized demo fixtures, readable results, useful empty/error states, access validity and revocation. Check the current reviewer-access rules without weakening the owner's account security.
- Regression: exercise existing supported workflows before and after the candidate update. For shared memory, verify expected persistence and isolation with disposable fixtures. Preserve production data, existing secret bindings, and working shortcut contracts.
- Presentation: demo video, release notes, screenshots, claims, and reviewer instructions must describe the actual build. Do not present planned features as implemented.

## Test without collateral changes

Begin with static inspection and existing evidence. Propose bounded synthetic tests in an isolated environment. Before any write, credential change, deployment, data migration, paid call, or submission, verify authorization for that exact operation and destination. Respect the current total budget and account for uncertain earlier charges; do not treat a budget setting as a proven hard cap. Never bypass access denials or security warnings.

Include at least one happy path and relevant negative cases for each privileged workflow. Capture the actual response and verify absence of unintended side effects. If a request times out, reconcile its outcome before retrying. Preserve a tested rollback route before proposing a release.

## Return a decision

Deliver:
1. Target and overall state: ready for the next review step, not ready, or blocked. Do not equate technical readiness with platform approval.
2. A short ledger of observed results, including untested or unavailable checks.
3. Blocking issues ranked by user impact, each with the smallest fix and retest.
4. Reviewer prerequisites and exact remaining actions, owners, and required approvals.
5. State changes actually performed, or explicitly state assessment only.

Use submission states precisely: drafted, uploaded, submitted, in review, approved, and published are different. Claim each only from a current portal receipt or equivalent verified evidence. Installation and organization sharing do not prove public availability.

## Attribution

Prepared for Sophia Cole / ColeWorld™ with AI assistance. © 2026 Sophia Cole. These notices do not claim trademark or copyright registration, platform endorsement, or third-party ownership.
