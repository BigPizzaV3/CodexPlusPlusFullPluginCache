# Existing maps: impact review without native versioning

Use current capabilities. Do not create a server-versioning scheme, clone the live map or pretend the app offers map versions. Keep a dated user-held baseline and final proposed package; these are working artifacts, not authoritative server history.

Read the selected map, needed ancestors, descendants and direct interfaces. Read relevant native associations (for example process_id references) as well as returned traceability links. Follow pages or identify what is incomplete. Assess affected procedures/instructions, related processes/handovers, ownership, audits, CARs, documents and other visible links. Retrieval cannot prove that hidden records or undocumented automations are unaffected.

Prepare an impact table for every structural/meaning change: existing ID/name, operation, before/after parent/purpose, affected descendants, linked records/interface partners, evidence of impact, unresolved risks and proposed handling. Simple spelling changes may need only a brief check; reparenting, changing scope, splitting/merging or retirement need explicit review. Do not imply the helper can discover all effects.

Retain IDs when identity/meaning continues. Do not match names alone. A move changes containment but does not automatically change ownership, flow, department labels or historical meaning; preview needed companion changes separately. Avoid parent/level inconsistency and cycles.

Do not automatically repurpose a historically linked record for substantially different work. For splits/merges, show a continuity/child/link plan and seek the user's decision. Preserve original historical links unless a specifically approved supported reassignment is justified. If safe handling is unclear, leave those structural writes pending and provide an app handoff. Do not invent successor links.

Omitted/out-of-scope is not obsolete. No automatic deletion or archival. Explicit archival, if permitted, needs impact review and final approval; never cascade retirement to children by assumption. Keep unapproved siblings and unrelated fields untouched.

Before final upload compare three states: baseline, approved proposal, current target. Preserve compatible external edits, but reconcile conflicting edits to the same field, parent, level or meaning. Inspect new/removed descendants and changed links. No ETag/precondition is assumed; fresh reads reduce but do not eliminate races.

The optional offline helper ../scripts/review_map.py compares supplied snapshots and prepares a difference/impact report. It has no network or write capability. Its complete flag means the caller asserts complete retrieval; it cannot verify server visibility. Do not submit its local new-node references as UUIDs.

A final unchanged map needs no write. After partial upload, retain per-operation results and reconcile; never replay all creates or delete as rollback. Working files do not make an upload atomic. Report any effect that could not be checked and any supported model detail not persisted.
