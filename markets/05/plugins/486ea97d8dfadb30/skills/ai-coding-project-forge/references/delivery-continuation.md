# Codex continuation, delivery, and value verification

Read this reference only when the user wants to continue after the five-file handoff, reports that Codex has finished or stopped, provides a repository or build, asks for testing or preview, wants acceptance fixes, requests publication, or wants to verify practical value.

Use the user's selected language. Keep the interaction simple: report what is known, what evidence is missing, the current lifecycle stage, and one next action. Do not restart the original product interview unless implementation evidence reveals a product-changing conflict.

## 1. Recover the project

Use the strongest available source of truth in this order:

1. accessible project folder or connected GitHub repository;
2. ZIP or complete source package;
3. Codex completion summary plus test/build output;
4. preview URL, screenshots, or user description.

Read the five specifications, repository status, latest relevant commit, build instructions, and existing test evidence. Never infer missing code or test results from a verbal claim alone. If the wrong or ambiguous repository may be selected, resolve it before any write.

Create or update `PROJECT_STATUS.md` when file access is available. Include:

- project and target artifact;
- current lifecycle stage;
- completed milestones and evidence;
- failing or untested acceptance cases;
- blockers and decisions needed;
- next action;
- latest known commit, build, preview, or release identifier;
- last updated timestamp.

## 2. Establish the GitHub record

If no repository exists, explain in one sentence that GitHub preserves recoverable development history. With explicit authorization and an available GitHub connection, create or select the repository and save the specification baseline. Default to private for confidential, client, enterprise, or unpublished projects. Never expose secrets, API keys, credentials, customer data, or generated build secrets in the repository.

If GitHub is unavailable or declined, continue through a local project package and clearly state that recovery across conversations and devices is weaker. Do not block a personal project merely because GitHub is absent.

## 3. Inspect Codex output

Classify the returned state without relying on elapsed time:

- `blocked`: missing decision, credential, dependency, service, data, permission, or target environment;
- `implementation incomplete`: required module or artifact is absent;
- `build failed`: the required artifact cannot be produced;
- `tests failing`: tests ran and one or more required cases failed;
- `ready for preview`: the application runs and required automated checks pass sufficiently for user review;
- `acceptance fixes required`: the user or acceptance evidence found a mismatch;
- `ready for release approval`: required acceptance is complete and release preparation is verified;
- `released, value unverified`: delivery occurred but real-use outcomes are not yet measured;
- `complete`: release or agreed delivery is complete and value evidence or a measurement plan is recorded.

Summarize the state in plain language. Do not overwhelm a beginner with raw logs unless a specific line requires their action.

## 4. Run automated checks

Use commands documented by the project. Inspect before running commands when they are missing or unverified. Run the smallest relevant sequence: dependency check, static/type check, build, automated tests, packaging check, and security or privacy checks only when required by the project.

Record actual results and evidence. A successful build does not prove functional acceptance. A skipped, unavailable, or flaky test is not a pass. Ask Codex to fix ordinary implementation defects and retest within the approved scope; pause when the fix changes the product, architecture, cost, security, or delivery target.

## 5. Arrange user preview

Provide the simplest preview supported by the target:

- Web: local or hosted preview URL;
- desktop: runnable development build or test installer;
- mobile: simulator, test device build, or approved distribution test channel;
- Linux/service: staging endpoint, container, or controlled test service;
- non-visual automation: representative input, execution record, and output.

Guide the user through the primary workflow in a few observable steps. Ask whether the result matches real use, not whether the implementation is technically elegant. Record feedback as passed acceptance, defect, change request, or later-phase idea. Do not silently turn later ideas into current scope.

## 6. Acceptance and fixes

Evaluate every required case in `ACCEPTANCE.md` as `Passed`, `Failed`, `Blocked`, `Not tested`, or `Waived`. A waiver requires an authorized person and a reason; it must not conceal a safety, legal, financial, privacy, or physical-control risk.

For failures:

1. state the mismatch and evidence;
2. ask Codex for the smallest in-scope correction;
3. rerun affected tests plus regression checks;
4. update the result and project status;
5. save a recoverable milestone when GitHub is authorized.

Do not declare completion while a required case remains failed, blocked, or untested.

## 7. Release authorization

Separate “ready to release” from “released.” Before a public or production release, present a short release summary:

- artifact and version;
- target environment and audience;
- acceptance status;
- known limitations;
- data, cost, domain, and rollback implications;
- exact action that will make it public or operational.

Obtain explicit authorization immediately before production deployment, public access, app-store submission, package signing with real credentials, or another consequential release action. Authorization for planning, coding, testing, or preview is not release authorization.

After release, verify the actual destination and record the URL, package, version, commit, or deployment identifier. Do not claim publication from a successful local build.

## 8. Verify value

The goal is to determine whether the application became a useful production asset rather than merely a completed coding exercise. Ask only for metrics that fit the original goal. Compare a baseline with actual use where possible:

- time per task and task frequency;
- error, rework, or omission rate;
- throughput or response time;
- manual handoffs removed;
- adoption or repeat use;
- cost avoided;
- revenue or paid delivery enabled;
- knowledge preserved or work delegated.

Distinguish measured, user-reported, estimated, and unverified values. Do not invent savings or revenue. If the application has not been used long enough, define the metric, baseline, observation period, owner, and review date, then mark value as pending.

When file creation is useful, create `VALUE_REPORT.md` with the original problem, baseline, current evidence, calculation method, confirmed result, limitations, and next measurement date. This is an operational outcome record, not one of the five implementation specifications.

## Completion handoff

At the end, state:

- what was delivered and where;
- which acceptance cases passed or remain open;
- whether release was authorized and verified;
- whether value is measured, estimated, or pending;
- the next maintenance or measurement action, if any.

Only use “complete” when the agreed delivery exists and every required acceptance condition has evidence or an authorized, documented waiver.
