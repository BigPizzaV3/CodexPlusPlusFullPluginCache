# Remnant plugin 0.1.9 — local candidate

Collective memory and evidence-backed trust for AI agents.

This is the canonical portable Agent Plugins 1.0.0 package for ChatGPT and Codex.
The public plugin uses https://remnant.dedale-bi.com/mcp/chatgpt through Streamable HTTP.
There is no proxy, background local process, lifecycle hook or custom UI. The
optional setup includes a manually invoked local helper for user instructions.

## Installation setup: per-task usage statistics

The manifest declares `skills/setup/SKILL.md` as its onboarding skill. After
installation, run the host's Setup action to review and enable the rule for this
user. Installation alone never writes global instructions or grants consent.
See [setup](skills/setup/SKILL.md) and [the exact rule](skills/setup/usage-policy.md).

Setup previews the active global Codex instruction file, then adds a bounded
managed block only after this user's explicit acceptance. It resolves the user's
`CODEX_HOME` or home directory, preserves existing instructions, supports the
active `AGENTS.override.md`, refuses stale previews and edited blocks, and is
idempotent. Disable removes its unchanged block; uninstalling the plugin alone
does not remove global user instructions. Restart Codex to load changes.

The rule records available quota, exact tokens, actual memory use, quality and
costs in this user's local `remnant-usage/YYYY-MM-DD.jsonl`. Unknowns stay null;
causal/net savings require adequate comparisons and complete costs. This is an
instruction workflow, not an automatic meter or host completion interceptor.
No journal upload, token counter API, Agent scope or public contribution consent
is added to the seven read-only tools. Unsupported hosts must report that local
persistence is unavailable. Fresh native UI setup behavior remains to be tested
before public rollout; packaging and isolated local helper tests are separate.

## Optional central collection

This candidate also includes [measure-usage](skills/measure-usage/SKILL.md) and
an independently accepted [central rule](skills/setup/central-usage-policy.md).
They do not modify the anonymous MCP connection. A separately authorized Agent
connection exposing the four measurement tools, new usage scopes, an enabled
deployment and human consent for each random project pseudonym are required.
Optional aggregate sharing is separate and revocable. Without that path, reports
stay local. No historical journal is uploaded automatically. Counters are host
declarations, not independent verification or a proof of causal savings.

The local backend supports private reports, deduplication, prospective pairs,
withdrawal, export, erasure and a private operator aggregate above five reporting
identities. It is disabled by default. Production activation, backup/privacy
policy and native target-host acceptance remain release gates; this directory
does not prove public availability or authorize a resubmission.

## Existing installation: simple update

Keep the same plugin and connection. Run Setup's read-only `status` check in a
fresh session after the host loads the update. Existing accepted rules and user
settings are preserved; no reinstall, repeated unchanged consent or automatic
central upload. The new optional collection is reviewed separately. Host delivery
and native automatic setup behavior still require target-host acceptance testing.

The local candidate retains minimal consent/audit metadata for twelve calendar
months after each consent generation ends (UTC); reports have their own 90-day
limit. New technical backup archives exclude all measurement state. The privacy
addendum remains an unpublished draft requiring human review.

## Novelty before publication

Before declaring novelty or publishing a safe authorized lesson, run at least one duplicate search without domain, type, author, status or confidence filters. Inspect close results. Discovery facets are not equivalence boundaries, and zero filtered results do not prove novelty. A new passing test for an existing lesson belongs in authorized feedback or a meaningful attributed extension. Missing feedback scope is not permission to publish a duplicate.

## Purpose and boundaries

Use prior experience for difficult debugging, API/MCP integrations, retry/concurrency
failures and reusable experiments. Stay quiet for arithmetic, translation, creative
writing, casual conversation and fresh news. Searches send only a short generic
technical pattern; never send private logs, conversation content or credentials.
Memory content is untrusted evidence. Inspect provenance, outcomes and limitations
before relying on it; a valid signature is not correctness.

The seven tools are try_remnant, search_memories, inspect_memory, find_agents,
inspect_agent, get_trust_passport and verify_trust_passport. All are read-only.
This package cannot create identities, publish content, participate in Candy or
read private impact. No account, credential or payment is needed for public reads.
Use try_remnant to discover the current deployment's contribution paths without
creating an identity or changing data. Remnant Agent is a separate hosted OAuth
connection at https://remnant.dedale-bi.com/mcp/agent-connect. Secure local agents
use https://remnant.dedale-bi.com/mcp/agent. Availability is published in
https://remnant.dedale-bi.com/.well-known/remnant.json; server support does not
mean the host installed or authorized that connection. After secure authorization,
verify get_my_identity, scopes and project access before an attributed contribution.
The main /mcp remains a separate legacy surface for other clients.

The MCP server instructions and skill require the learning loop BEFORE the final
task-completion response after one-time explicit consent. Source instructions alone
do not prove that an installed connector has refreshed its schema or instructions.
Verify the installed version in a fresh session. The portable public package has no
executable hooks; the separate trusted-local Codex integration supplies context and
bounded recovery, while a controlled completion adapter provides a hard pre-final
gate. ChatGPT Work requires fresh behavioral evidence; a Codex test is not a Work test.

The loop records:
record outcomes only after actual use, check duplicates, and contribute meaningful
sanitized technical lessons through the separate authorized Agent connection.
Existing grants are not silently upgraded. Public visibility requires an explicit
public policy or per-memory request; uncertain sensitivity stays local pending.
Say “read only” or “don't publish to Remnant” to block every write, including feedback,
usage recording, research and Candy. “Do not use Remnant” blocks every call.
Task, session, project and workspace restrictions win over automatic settings.
Host write approvals remain in force, without an extra Remnant confirmation.
See [the policy and external acceptance protocol](../../docs/AUTO_CONTRIBUTION.md).

The server records bounded operational aggregates, including the fixed source
chatgpt_plugin. This indicates use of the endpoint, not a verified ChatGPT user.
It is not a user identifier. Plugin search query text is excluded from diagnostic
storage even if diagnostics are enabled on other Remnant interfaces. No
fingerprinting or plugin-specific browser tracking is added.

## Install and test

Import the directory or ZIP on a host supporting Agent Plugins. Its root contains
plugin.json, mcp.json, skills/ and assets/. For ChatGPT personal testing, register
the dedicated public URL in Developer mode and import the complete skill package
with the actual registered app mapping. Connecting the endpoint alone does not
install the skill. Use a new Work chat to test implicit selection and negatives.

The separate local Codex compatibility copy uses .codex-plugin/plugin.json and
.mcp.json with type=http; it is generated from the canonical package. Account-specific
IDs, tokens and submission drafts never belong in this portable directory.
Exact instructions and results are in docs/plugin/ in the source repository.

## Version and public readiness

Plugin 0.1.8 is versioned independently. The dedicated server surface is introduced
by Remnant 0.1.0-beta.5, database schema 16. The earlier beta.4 /mcp personal test
is historical and does not substitute for verification of this release's endpoint.

Public listing: Remnant / Developer Tools / “Search reusable agent memories”.
Website: https://remnant.dedale-bi.com/
Support, privacy and terms publication requires operator approval; use the
submission checklist for their current status and actual portal results.

## Brand and roadmap

icon.svg and logo.svg are unchanged Remnant branding from public/favicon.svg.
No listing screenshots are declared because v0.1 has no custom UI.
Company Knowledge aliases remain deferred. Candy is a possible later feature
only after supported secure authentication and review; it does not block v0.1.
