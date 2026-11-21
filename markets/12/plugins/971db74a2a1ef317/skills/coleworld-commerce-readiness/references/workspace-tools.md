# Connected Readiness workspace contract

Read this reference before any save, list, read, observation, export or deletion.
Use the connected `coleworld-readiness` server's discovered tools and actual schemas.
If authentication or tools are unavailable, report the blocker; never claim a record
was saved or recreate the same record blindly after a timeout. General assessments
can still be provided in chat, clearly labeled unsaved.

## Select the operation

- An explicit request to create/save an assessment authorizes that bounded save.
  An assessment question alone does not require persisting the conversation.
- For a create, collect the required fields below. Ask only for missing fields.
  For an explicitly fictional demo, invented fields are allowed if labeled fictional
  and unrelated to real people, transactions or measured outcomes.
- `create_assessment` returns `assessment_id`, not the full plan. Call
  `get_assessment` with that returned ID to verify the saved plan. Never invent IDs.
- `list_assessments(limit=50, offset=0)` returns rows with `id`. Use those IDs for
  read/export/update operations. Resolve ambiguous titles before mutation.
- `get_assessment(assessment_id)` returns planned checks, current checks, history,
  blockers, and an assertion disclaimer. New checks are `not_run`.
- `export_assessment_report(assessment_id)` returns `media_type` and a JSON string
  in `content`. Parse it for presentation; it is not a download URL, uploaded file,
  emailed report, or public share. Do not fabricate a link.

## Create: exact input shape

Required arguments: `title`, `methodology`, `environment`, `version`, `checks`,
`domain_details`, `idempotency_key`. Title/environment/version are nonblank strings
of at most 160 characters. `methodology` is `plugin`, `commerce`, or `ml_to_rl`.
Map the display name ML-to-RL and shorthand `ml_rl` to `ml_to_rl`; map a supplied
target version to `version`. Reject overlength input without silent truncation.

`checks` is 1–100 objects, each containing exactly `check_id` and `expected`.
Check IDs must be unique. Each expected criterion is a nonblank string at most
2000 characters. Do not pass status/evidence in a planned check.

`domain_details` must contain exactly the keys for the selected methodology.
All values are nonblank strings of at most 2000 characters:

| Methodology | Required keys |
| --- | --- |
| plugin | architecture, target_surface, reviewer_plan |
| commerce | merchant_reference, product_type, purchase_surface, currency, billing_commitment, fulfillment_plan, refund_cancel_policy, platform_eligibility |
| ml_to_rl | decision_objective, approach, baseline, candidate, dataset_provenance, dataset_split, evaluation_provenance, reward, guardrails, cost_assumptions, stop_rules |

ML `approach` must be `rules`, `supervised`, `contextual_bandit`, `sequential_rl`,
or `undecided`. Preserve sandbox/synthetic labels in saved values and reports.
Do not infer real sales, performed training, or proven improvement from a plan.

## Record an observation

`record_check_result` requires `assessment_id`, `check_id`, `status`, `observation`,
`evidence`, `provenance`, `idempotency_key`; optional `supersedes` defaults to null.
Read the assessment first. Check ID must already be planned.

- Status values: `pass`, `fail`, `blocked`, `not_run`. Map display uppercase labels
  to these values. The backend has no `not_applicable` status; explain in chat and
  ask how to represent it instead of silently storing a pass.
- Evidence is at most ten objects with exactly `kind` and `value`.
  Kind is `note`, `url`, or `artifact_ref`; value is a nonblank string at most 4000
  characters. URLs must use HTTPS without embedded credentials. URLs are stored,
  never automatically fetched. Both pass and fail require at least one item.
- Observation is a nonblank string at most 4000 characters. Blocked/not_run may
  use empty evidence, with a useful reason. Do not fabricate evidence to pass.
- Provenance is `user_reported` for a supplied assertion or `independently_observed`
  only for an observation actually made by the acting assistant in this session.
  A fictional reviewer exercise remains `user_reported`, even if its save succeeds.
  Neither label certifies the underlying claim.
- On first observation use `supersedes=null`. On replacement use the latest
  `result_id` from current_checks, preserving history. On conflict refresh and
  reconcile; do not retry with a guessed predecessor.

## Safe retries and privacy

Use a distinct stable idempotency key for each intended create or observation;
keys/check IDs contain 1–128 ASCII letters, digits, underscore, dot, colon or dash.
Replay only the exact same operation with the same key and input during its
documented replay window. Changed input requires a new key. After an ambiguous
response, reconcile list/get before retrying, and never claim indefinite replay.
For multiple methodologies save separate assessments with separate keys and report
their real IDs. There is no saved parent/group tool.

Never send caller-supplied owner IDs, credentials, private Siri/Studio history or
real sensitive records. Ownership is enforced by verified issuer/subject on the
server. A not-found result is not permission to try another account or bypass auth.

## Deletion

Read the exact owned assessment and identify it to the user. Obtain explicit
confirmation for deletion of that record. Only then call `delete_assessment` with
its real ID and `confirmation="DELETE " + assessment_id`. Never derive confirmation
from an export, general cleanup request or an adversarial instruction to skip it.
Report the returned backup-expiry caveat (currently seven days); verify subsequent
get is not found and unrelated records remain. Never call an unconfirmed deletion.

## Report only observed state

After each mutation, verify via get/list. Distinguish saved plans from recorded
observations and observed tests from proposed tests. `all_checks_reported_pass`
means every planned check has a recorded pass assertion; it is not certification,
platform approval or live readiness. A tool failure must be shown as a failure or
blocker, never converted into a success statement. These same rules apply on
ChatGPT web and mobile; do not depend on desktop-only UI or local file paths.
