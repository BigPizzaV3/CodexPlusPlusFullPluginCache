---
name: empire-handoff
description: Route one bounded planning checklist or single-file implementation proposal to an external model, quarantine and validate it outside the repository, and let Codex preview, download, adversarially review, approve for consideration, or reject it without automatic application. Use when the user asks for an Empire handoff, external-model implementation proposal, downloadable model artifact, project checklist, single-file frontend, partner plan, or worker file while Codex remains the only repository writer.
---

# Empire Handoff

Keep Codex as the sole implementation authority. External `partner` and `worker` labels describe output type only; neither receives tools, filesystem access, approval authority, or repository-write access.

## Resolve the runner

Resolve this skill directory as `EMPIRE_HANDOFF_ROOT`, then run:

```bash
python3 "$EMPIRE_HANDOFF_ROOT/scripts/empire_handoff.py" --help
```

Use `$empire-settings` when credentials or budgets need configuration. Never put credential values in chat or command arguments.

The CLI's default JSON remains the machine-readable source of truth. For direct
human-readable output, add `--view compact` or `--view detailed` before or after
the lifecycle command. Present the returned result with status first, then
identity, cost, delivery, validation, and one safe next action. Never rerun a
paid generation merely to change its presentation; format the existing result
instead.

## Generate one handoff

Choose only one supported pairing:

- `partner` + `checklist` for specifications, plans, risk registers, test strategies, or adversarial thinking.
- `worker` + `single-file` for exactly one textual source-file proposal.

Checklist example:

```bash
python3 "$EMPIRE_HANDOFF_ROOT/scripts/empire_handoff.py" generate \
  --repo /absolute/path/to/repository \
  --task "Turn the supplied project specification into an implementation checklist" \
  --role partner \
  --format checklist \
  --suggested-path docs/implementation-checklist.md \
  --media-type text/markdown \
  --file PROJECT_SPEC.md \
  --mode balanced
```

Single-file example:

```bash
python3 "$EMPIRE_HANDOFF_ROOT/scripts/empire_handoff.py" generate \
  --repo /absolute/path/to/repository \
  --task "Propose one accessible responsive HTML5 landing page" \
  --role worker \
  --format single-file \
  --suggested-path proposals/index.html \
  --media-type text/html \
  --file docs/frontend-spec.md \
  --mode balanced
```

Send only the minimum bounded evidence needed. Do not route secrets, credential files, unrelated repository content, or private material that is ineligible under the selected provider's data policy. Let catalog metadata, benchmark evidence, task fit, availability, and any configured accumulated project budget control selection. Use `--model provider/model` only when the user explicitly requests that canonical model. Do not add `--max-authorized-cost` unless the user explicitly requests a per-call dollar ceiling. Add `--require-zdr` only when the user explicitly requires Zero Data Retention; data-collecting providers remain denied by default.

Handoff shares Review's invocation-time catalog policy. Exact-model cache misses and requests for the latest, newest, or currently available model force a live refresh before route selection. Use `--require-live-catalog` when a fresh authenticated OpenRouter scan must be explicit.

Handoff results include the same measurement-only `context_preflight` contract
as Review. Supply both `--codex-context-limit-tokens` and
`--codex-context-used-tokens` only when the active host exposes them. Unknown
context recommends artifact delivery because Handoff is already a persistent,
quarantined workflow. `--response-class` records a recommendation but does not
change the provider request in this phase; `applied_to_dispatch: false` prevents
the receipt from implying enforcement.

## Inspect and act

Treat the generated artifact as quarantined source, not as an implementation.

```bash
python3 "$EMPIRE_HANDOFF_ROOT/scripts/empire_handoff.py" show HANDOFF_ID
python3 "$EMPIRE_HANDOFF_ROOT/scripts/empire_handoff.py" continuation-plan HANDOFF_ID \
  --repo /absolute/path/to/repository \
  --task "Finish only the missing risks and acceptance checks" \
  --file PROJECT_SPEC.md \
  --completed-id scope \
  --completed-id implementation
python3 "$EMPIRE_HANDOFF_ROOT/scripts/empire_handoff.py" adversarial-review HANDOFF_ID
python3 "$EMPIRE_HANDOFF_ROOT/scripts/empire_handoff.py" approve HANDOFF_ID
python3 "$EMPIRE_HANDOFF_ROOT/scripts/empire_handoff.py" reject HANDOFF_ID
python3 "$EMPIRE_HANDOFF_ROOT/scripts/empire_handoff.py" download HANDOFF_ID \
  --repo /absolute/path/to/repository \
  --destination /path/outside/repository/proposal.html
```

Render `show` output as source text. Never execute generated HTML, JavaScript, or other executable content. A download destination must remain outside the active repository.

If generation returns `partial_recoverable` or `completed_degraded`, do not reject or rerun it. The assistant response was already saved to `research_artifact.content_path` before validation. Read it through repeated `show HANDOFF_ID --offset N --max-chars 12000` calls until `chunk.has_more` is false, synthesize the usable partial research, and clearly label incomplete sections. An in-band provider error with usable bytes is partial, never complete. Never start a paid retry or continuation automatically. Request explicit authorization and show incremental plus cumulative cost before a same-model continuation of only the missing work. A `failed_empty` result with observed cost must remain visible as `compensation_pending`; an unknown billing outcome must remain `pending_reconciliation`. Do not represent either as delivered or as zero cost.

Use `continuation-plan` only for `partial_recoverable` handoffs. It is a
non-billable preflight: it revalidates the original project and evidence hash,
hashes the missing-work request, records completed IDs, bounds the recovered
tail used by a future continuation prompt, and reports the parent-based
incremental and cumulative estimate. It never reserves budget or dispatches a
provider request. Treat `continuation_plan_blocked` as fail-closed. In
particular, a display provider name is not an exact OpenRouter provider slug;
same-provider continuation requires a proven slug plus a current pricing
refresh and explicit incremental and cumulative cost authorization. The paid
continuation transport remains unavailable in this slice.

A provider `content_filter` or `safety` terminal is
`blocked_provider_safety`, even when readable bytes arrived or an in-band error
is also present. Preserve those bytes privately but never preview, synthesize,
approve, download, or export them through the ordinary handoff lifecycle.

For a paid `failed_empty` result, the review runtime automatically creates a
local compensation record in state `needed`. Inspect or advance it through the
review CLI's `compensation list`, cross-project `compensation report`, and
`compensation update` commands. New OpenRouter handoffs preserve the generation
ID in both the route receipt and local ledger so the empty delivery can be
matched to provider activity without relying only on timestamp/model/cost. A
local record is not proof that a provider claim was submitted.

For adversarial review, create the separate review record, inspect the unchanged source through `show`, then have Codex independently report correctness, security, accessibility, assumptions, and missing-test findings. Do not mutate the original artifact while reviewing it.

`approve` means approved for Codex consideration. It never means apply directly. After approval, Codex may revise, partially use, relocate, or reject the proposal; Codex must make repository edits itself and run appropriate validation before reporting completion.

## Report provenance

Present:

- Codex as lead and the selected external model as Partner or Worker.
- End any handoff synthesis or conclusion with `synthesis_footnote.markdown`. It contains only the external model icon and base model name in one atomic SVG; never rebuild it from a standalone image and adjacent text.
- A quiet footer after a horizontal rule using `response_footnote.markdown`; keep it on one physical line and use its text fallback when local images do not render. Each visible chip must be one transparent SVG image containing an internally aligned 14px logo and vector label; never place a standalone Markdown image beside separate Markdown text. Never emit raw HTML.
- Requested, selected, and proven served model/provider identities.
- `unavailable` whenever upstream metadata does not prove served identity.
- Artificial Analysis as a chip only when matched benchmark evidence affected route selection. Keep Codex web-tool citations native beside their claims; include only provider-returned external URLs from `web_research.sources` in the Empire footer.
- Route profile, benchmark availability, projected and observed cost, artifact hash, validation state, and warnings.
- A clickable local file link only after a successful download.

Do not expose the raw provider response, raw repository evidence, credentials, quarantine internals beyond the returned path, or unverified identity claims.
