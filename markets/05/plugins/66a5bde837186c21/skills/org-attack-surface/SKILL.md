---
name: org-attack-surface
description: "Map an organisation from verified legal entities to attributable domains, ASNs, netblocks and public services. Use for authorised corporate-footprint and attack-surface discovery while separating candidates from proven ownership and scan scope."
---

# Organisation Attack Surface

## Authorisation and safety

- Confirm the target is owned by the user or covered by written authorisation before sending target-directed traffic, executing bundled recon scripts, validating credentials, enumerating users, scanning ports or scheduling recurring checks. Record the exact in-scope domains, IP ranges, methods, rate limits and engagement window.
- Passive analysis of user-supplied data and public documentation may proceed without target interaction. Clearly label unverified attribution and do not convert discovered sibling assets into scan scope.
- Do not exploit vulnerabilities, bypass access controls, submit or replay credentials, perform password spraying, induce state changes, evade detection, send phishing messages, access non-public data or use destructive probes.
- Treat exposed secrets and personal data as sensitive. Minimise collection, redact reports, avoid unnecessary validation and follow the engagement's evidence-handling and disclosure rules.
- Stop when authorisation is absent or ambiguous, a technique would exceed scope, rate limiting or defensive blocking appears, or an action could materially affect a system. Ask for a narrower safe action.

## Workflow

1. Establish whether the request is passive analysis or involves target interaction. For interaction, capture the scope and authority required above before proceeding.
2. Read [references/source-playbook.md](references/source-playbook.md), searching within it for the topic relevant to the request. Load only the relevant sections into working context.
3. Prefer passive and keyless sources first. Separate observed facts, attribution inferences, hypotheses and proposed validation.
4. Use bundled scripts only when they directly support the authorised task. Inspect their prerequisites and resolved target/output paths before execution; do not install dependencies or run network operations implicitly.
5. Preserve source URLs, timestamps, commands, hashes and confidence so another analyst can reproduce the result. Redact secrets and unnecessary personal data from deliverables.
6. Report scope, method, evidence, confidence, limitations, findings and proportionate next actions. Never represent a candidate asset, guessed identity, exposure or exploitability as proven without supporting evidence.

## Source and licence

This adaptation preserves methodology from Sachin Sharma's `elementalsouls/Claude-OSINT`, pinned at commit `13d920413448c026b52ac74efee0f1eb39dd81ff`. See the package-level `ATTRIBUTION.md`, `LICENSE`, and `LICENSE-CONTENT`.
