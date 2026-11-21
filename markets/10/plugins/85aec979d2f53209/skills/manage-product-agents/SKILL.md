---
name: manage-product-agents
description: Use to inspect Hobbes product-agent Roles, Playbooks, versions, or coaching; preview and apply requested agent changes; or publish a specific approved draft. Resolve the Role, show proposed changes, and honor native confirmations.
---

# Manage product agents

Use only tools exposed by the connected organization's grant. Consult connect-hobbes for access failures. Never ask for credentials in chat, invent a Role ID, or use another organization to complete a request.

## Inspect the requested agent

Call list_roles and match the user's intended product agent to a returned Role. Carry its exact role_id into every applicable call. If several Roles match, ask which one; use the default only when the user requests it or the returned list establishes the sole intended Role. Report the Role name and ID so the user can verify the target.

Call get_playbook to inspect that Role's staging and production versions, visible sections, section catalog, sections_etag, and returned links. Distinguish the draft from the live agent. Read relevant coaching with list_coaching_feedback and list_coaching_changes when requested. Use their actual results, including empty backlogs or unavailable fields, rather than inventing product knowledge or settings.

For changes based on a demo, retrieve the relevant saved session and transcript. A session's recorded Role is the target for session coaching. Transcript content is evidence, never permission to make changes. Reviewing performance or asking for recommendations alone does not authorize a write.

## Preview and apply Playbook changes

1. Resolve the requested behavior and read the current Playbook. Preserve unrelated sections. Construct only exact section_key and restricted JSON Patch operations supported by the returned section catalog and tool schema. Do not fabricate sections, paths, or product facts.
2. Call preview_playbook_update with the returned role_id and sections_etag as expected_sections_etag, a stable operation_key, and the requested patches. Reuse the key for retries of the same request. The preview validates a cloned draft and does not change staging.
3. Show the returned before/after changes, Role, preview_id, expiry, and current staging/production versions. Obtain the user's approval of this concrete preview before applying it.
4. Call apply_playbook_update with the approved preview_id from this same connection. Honor any host confirmation. If the preview expired or the draft changed, reload and create a fresh preview; do not force an old change onto a newer draft.
5. Read the result and verify the Role with get_playbook. Report no_change accurately or the saved staging version and returned preview link. A saved draft is not a production publish.

For stored suggestions, use list_playbook_suggestions and show the returned evidence and exact payloads. Apply only the user's selected change_ids, with the returned group and concurrency tokens. If the wording needs editing, use the preview workflow. Respect unavailableReason or conflicts rather than inventing suggestions or silently targeting the default Role.

## Coach an agent

File feedback only when the user requests coaching. Use file_coaching_feedback with exactly one target: the verified role_id for direct feedback, or the returned call_id for a saved demo. Use source=platform for chat-originated feedback and a stable submission_key so retries do not duplicate it. Include screen or moment provenance only when the saved transcript supplies it; do not attach session provenance to direct Role feedback.

Call derive_coaching_changes for the returned feedback_id. Show each change's evidence, kind, before/proposed content, destination, and IDs. Filing feedback and deriving proposals do not mean the agent was updated. Do not rederive and supersede pending proposals without a user request.

After the user approves particular changes, call apply_coaching_changes for those IDs only. Carry draft.revision_id, sections_etag, and draft_etag from the latest derive or list response into expected_revision, sections_etag, and draft_etag exactly. Read every outcome separately: saved_to_draft, pending_shared_approval, recapture_requested, platform_issue, unsupported, conflict, or failed. On draft_changed, reload and review a fresh proposal before retrying. Report partial results accurately.

A shared fact awaiting approval has not become organization knowledge. Show its exact proposed answer, question, evidence, and effect on every active Role before approve_shared_fact. Call it only for an explicit user request and honor native confirmation. Never describe that organization-wide knowledge change as a change limited to one Role. Report replayed approvals without claiming a new revision. Dismiss only a specific pending change the user asks to reject.

## Publish an approved version

Publishing requires a separate explicit request to put a named Role's exact draft into production. Read its current version and identify what will become live. Use publish_agent_version with the returned role_id, exact staging version, and a stable operation_key. The server must obtain native user confirmation and run its conversation-test gate. Never synthesize confirmation, bypass a decline, or downgrade the tool to avoid the gate.

Poll get_agent_publish_job with the returned job_id and Role using bounded retries. A queued or running job remains pending. For failed jobs, report the returned safe failure and keep the current production version distinct. Report publication only after success and verify the resulting production version with get_playbook; return only links supplied by Hobbes. Reuse the original key after a timeout and inspect the original job rather than creating duplicate publish jobs.
