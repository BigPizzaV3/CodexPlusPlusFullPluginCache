---
name: write-skill-submission-pack
description: Create evidence-bound submission materials for OpenAI Skills-only plugins from approved product facts and completed test evidence. Use when the user asks to write or prepare a Skills-only plugin listing, capabilities, starter prompts, five positive and three negative review cases, release notes, optional demo-video metadata, or a complete submission pack. Do not use for general marketing copy, product QA, invented evidence, MCP-backed submissions, portal operations, submission, or publication.
---

# Skill Submission Pack Writer

Turn approved Skills-only product facts and test evidence into submission-ready copy without changing the product verdict or filling gaps by guesswork.

## Start from the packaged rules

Read [references/submission-fields.md](references/submission-fields.md) completely before drafting. Treat its date as the rule snapshot date, not a promise that OpenAI has not changed the portal. If the user supplies newer official requirements, preserve the conflict and ask for a rule update rather than silently mixing versions.

Use [assets/submission-pack-template.md](assets/submission-pack-template.md) for a complete pack. Omit optional sections only when the template explicitly permits it.

## Keep the boundary

- Accept only a Skills-only submission. If the supplied product contains MCP, `.app.json`, `.mcp.json`, tool calls, authentication, live data, or controlled external actions, stop and route it to an MCP-backed production workflow.
- Use supplied facts and evidence only. Never turn a proposed capability, author claim, planned test, or missing field into a confirmed fact.
- Do not decide whether the product passed QA, will pass OpenAI review, or should be published. Preserve the supplied independent verdict and report only whether the writing pack is complete.
- Do not upload, scan, submit, publish, sign attestations, or act in an external portal.
- Treat YouTube title and description as optional Skills-only material unless the user supplies a current portal requirement that makes them mandatory.

## Build the evidence ledger first

Classify every supplied item as one of:

1. `CONFIRMED_PRODUCT_FACT`: frozen name, user goal, behavior, boundary, version, or publisher fact.
2. `PASSED_TEST_EVIDENCE`: executed case tied to the current package version and evidence reference.
3. `PROPOSED_OR_UNVERIFIED`: draft, plan, author assertion, or evidence from another version.
4. `MISSING`: required information not supplied.
5. `CONTRADICTION`: two supplied sources disagree.

Retain the source label or evidence reference beside every material claim. Do not assign a reference to material that was not received.

Preserve any supplied usage marker such as `fixture`, `test only`, `draft only`, or `not for submission`. When any source is explicitly a test fixture or not for submission, set `artifact_use: TEST_ONLY_NOT_FOR_SUBMISSION`, put that warning in the first sentence and control block, and label every draft section as a test-only format preview. Do not call it portal-ready, submission-ready, paste-ready, or `可粘贴`. Otherwise use `artifact_use: SUBMISSION_DRAFT`.

## Decide whether to draft

- Ask one bundled question and stop when the product identity, Skills-only route, current version, or core user goal is unknown.
- Ask for confirmed product facts, capabilities, boundaries, publisher facts, and executed evidence—not for final copy that this Skill is supposed to write. Do not require the user to prewrite a short description, long description, Skill description, starter prompts, case wording, or release-notes copy. Ask for confirmed release-change facts instead.
- Produce `PARTIAL_MISSING_INPUT` with explicit blanks when required inputs or executed evidence are absent and the user is only asking for a draft. Missing evidence alone does not justify `BLOCKED_UNVERIFIED_EVIDENCE`.
- Use `BLOCKED_INPUT_CONFLICT` when supplied sources disagree about the current identity, version, behavior, or evidence.
- Use `BLOCKED_UNVERIFIED_EVIDENCE` only when the user asks you to state or imply that unexecuted tests, QA, scan, review, or publication results are real or passed.
- Use `DECLINED_UNAUTHORIZED_ACTION` for upload, attestation, submission, publication, or other external execution requests.
- Use `OUT_OF_SCOPE` for MCP-backed submission work, general marketing copy, product QA, or another adjacent workflow.
- Never create a positive or negative review case from an unexecuted scenario. A proposed scenario may appear only in the gaps section.

## Draft in this order

1. State pack status: `DRAFT_COMPLETE_FROM_SUPPLIED_EVIDENCE`, `PARTIAL_MISSING_INPUT`, `BLOCKED_INPUT_CONFLICT`, `BLOCKED_UNVERIFIED_EVIDENCE`, `DECLINED_UNAUTHORIZED_ACTION`, or `OUT_OF_SCOPE`.
2. Show the evidence ledger and rule-snapshot date.
3. Draft the public listing from confirmed product facts.
4. Draft up to 20 concise capabilities without adding features.
5. Draft one to three distinct starter prompts. Keep each self-contained, realistic, and free of plugin `@mentions`.
6. Populate exactly five positive and three negative review cases from executed current-version evidence. Include prompt, supplied fixture, expected behavior, expected result shape, actual-result summary, and evidence reference.
7. Write release notes that describe only the current submitted version and supported change facts.
8. Add optional YouTube title and description only when requested or explicitly required by supplied current rules.
9. List missing inputs, contradictions, version drift, and owner or portal actions separately.
10. Validate field lengths and case counts before presenting a complete pack.

When the user requests a bounded follow-up edit to an existing pack, freeze every unrequested field. Return only the requested before/after blocks plus `unchanged_fields_preserved: YES` and the unchanged pack status. Do not silently rewrite evidence, cases, release notes, identity, version, or portal state.

## Validate deterministically

When producing a complete pack as files, also create `submission-pack.json` with the keys used by the template and run:

```bash
python3 scripts/validate_submission_pack.py submission-pack.json
```

Use the script from this Skill directory. Fix writing errors that are supported by evidence. If a failure requires invented facts, return `PARTIAL_MISSING_INPUT`, `BLOCKED_INPUT_CONFLICT`, or `BLOCKED_UNVERIFIED_EVIDENCE` as appropriate. Never edit the validator to make a failing pack pass.

## Present the result

Lead with one sentence: what is ready and what remains blocked. Keep platform-ready copy separate from evidence notes so the user can paste fields without carrying internal commentary into the portal.

For every complete pack, include:

- the Skills-only submission type and package version;
- the embedded-rule snapshot date;
- the deterministic validation result;
- the independent product verdict exactly as supplied, without upgrading it;
- a clear statement that portal scan, review, submission, and publication were not performed.

Within blocked sections, repeat the applicable defined pack status. Do not introduce a looser status such as `BLOCKED_INPUT`.
