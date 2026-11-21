# Buyer-Knowledge Update Methodology (BuyerTwin)

This reference defines safe canonical BuyerTwin mutation behavior using existing proposal/apply MCP tools.

## 1) Activation and boundaries

Use update-buyer-knowledge only when the user explicitly asks to add, correct, or update canonical BuyerTwin knowledge.

Do not mutate for:
- casual statements
- hypothetical brainstorming
- ask_buyer simulation output without explicit save instruction
- AI synthesis unless user explicitly asks to save/update
- requests that belong to ask-buyers, compare-buyers, evaluate-messaging, create-buyer-content, or prepare-sales-conversation

## 2) Foundational integrity rule

Never silently promote into canonical BuyerTwin knowledge:
- BuyerTwin Simulation
- AI Synthesis
- generic model priors
- stereotypes
- speculative inference

Canonical mutation requires explicit user intent plus successful proposal/apply flow.

## 3) Deterministic buyer targeting and scope

- Named buyer: mutate that buyer only.
- Multiple named buyers: mutate only those buyers.
- Broad scope requests: perform only if contract supports scope safely.
- If broad operation is not natively supported, orchestrate per buyer and report per-buyer outcomes.

Never broaden "add this to the CFO" into all buyers.

## 4) Preserve semantic meaning

Do not silently broaden or harden claims. Preserve qualifiers and conditions such as:
- usually
- often
- may
- for established companies
- when X applies
- except when Y

Normalization may improve structure, but not meaning.

## 5) Proposal and apply contract discipline

Primary flow:
1. propose_buyer_knowledge_update
2. apply_buyer_knowledge_update

Proposal is non-mutating preview. Apply is mutation.

From current MCP contracts:
- proposal contract version: buyer_knowledge_proposal_v3
- apply contract version: buyer_knowledge_apply_v3
- proposal returns visible fields including proposal_id, destination, target_key, suggested_action, requires_confirmation, and apply_preview
- apply supports v3 proposal_id path with visible proposal fields plus submission fields.

Apply by proposal_id only.
Do not use legacy apply-path fields in apply requests.

## 6) Confirmation behavior

Distinguish:
- mutation intent from user
- confirmation policy from tool output

Respect tool policy:
- if confirmation required, do not apply before confirmation
- if confirmation not required, do not invent extra confirmation friction

## 6b) Proposal-fidelity verification

Before apply, verify the proposal faithfully represents user mutation intent.

Proposal authority and user intent authority are different:
- proposal is authoritative for what the system proposes to do
- user instruction is authoritative for what the user intended BuyerTwin to learn

Validate material fidelity across:
- target buyer and buyer scope
- intended meaning
- qualifiers, conditions, and exceptions
- correction vs addition intent
- certainty scope (for example usually vs always)
- category/destination only where materially relevant to meaning

Normalization is allowed. Semantic drift is not.

If fidelity fails:
- do not apply
- re-propose from the original user instruction without inventing explicit destination/target hints
- if still ambiguous, ask only for minimum clarification needed
- never claim the proposal was applied

General-intake classification authority rule:
- `propose_buyer_knowledge_update` is BuyerTwin-classified intake, not model-classified intake.
- Do not send `explicit_destination` or `explicit_target_key` in general propose calls.
- Never infer classification overrides from uncategorized proposals, suggested_routes, semantic failure, low/medium confidence, proposal_mismatch, or automatic retry.
- When trusted human review must explicitly re-target existing knowledge, use the dedicated resolution workflow.

Important distinction:
- confirmation policy answers whether a valid proposal needs explicit confirmation
- fidelity gate answers whether this proposal is actually the change the user asked for

Both gates must pass before apply.

## 7) Classification and routing

Use proposal result as authority for routing/classification semantics.

If user gives category intent and contract accepts routing hints, pass supported signals.

Do not invent unsupported categories or force unsupported classification rules.

## 8) Duplicate, conflict, stale, expired, mismatch

Use authoritative mutation semantics from tool results.

Observed semantic outcomes include:
- duplicate_candidate
- stale_target
- proposal_mismatch
- proposal_not_found
- proposal_expired
- confirmation_required
- apply_rejected_policy
- idempotent_replay

Rules:
- duplicate/no-op: do not claim new record created
- stale target: do not force apply; re-propose if supported
- proposal expired: generate fresh proposal
- proposal mismatch/not found: never remap proposal to another buyer/change
- idempotent replay: report deterministic replay outcome

Retry lock after proposal_mismatch:
- Do not mutate `knowledge_text`, `intent_level`, or `verification_intent` unless the user provided new information.
- Do not promote advisory `suggested_routes` into explicit targets.
- If a fresh proposal is required, replay the original user intent without invented categorization.
- Do not auto-retry by generating a fresh proposal unless the user explicitly asks to retry or supplies new information.

## 9) Provenance discipline

Preserve available source/provenance semantics supported by the contract.

Do not label user-provided knowledge as independently research-verified unless tool-supported evidence exists.
Do not label AI synthesis as customer-validated evidence.

## 10) Corrections

Treat explicit corrections as corrections, not unrelated additions.

If system surfaces conflict, expose material conflict and proceed through supported proposal/apply workflow.
Do not invent destructive replacement if unsupported.

## 11) Proposal presentation

When review is needed, present concise user-relevant details:
- target buyer
- proposed change
- destination/target key/suggested action if returned
- qualifiers preserved
- whether confirmation is required

Do not expose internal workflow internals unless needed for troubleshooting.

Include concise fidelity-relevant details in proposal review when needed:
- scope and target
- preserved qualifiers/conditions
- correction/addition framing

## 12) Success semantics

Do not say saved/updated after propose only.

Allowed progression:
- after propose: proposed update language
- after successful apply: canonical update confirmed language
- on uncertain apply/network: do not claim mutation success

On apply failure:
- report only BuyerTwin-authoritative proposal/apply state and returned failure code
- do not present model-speculative classification (for example "I would classify this as ...") as BuyerTwin authority
- do not silently re-propose/re-scope the same fact to force a different category

On uncategorized apply success:
- if result indicates `create_uncategorized` / `inbox_created`, report it as saved to Needs Review based on BuyerTwin-authoritative apply output

## 13) Multi-buyer partial success

For explicit multi-buyer mutation where only per-buyer updates are supported:
- generate independent proposals
- apply independently
- report partial success accurately
- do not claim atomic multi-buyer mutation

## 14) Intent-level precision

`explicit_instruction` must not be treated as an automatic instruction to classify into a specific destination/target.

Distinguish:
- explicit instruction to store/update knowledge, versus
- explicit instruction to classify into a named category/target.

Only the second case should use the dedicated resolution workflow where explicit destination/target is supported.
