# Release verification — 2026-10-17

The directory endpoint and privacy policy are deployed. The public 0.4.0 source, actual client recordings and submission archives are available from the [GitHub release](https://github.com/clyr-inc/casually-plugins/releases/tag/directory-v0.4.0). Directory review is not submitted or approved. Credentials and raw account data remain in the private reviewer handoff.

## Automated and production checks

| Check | Actual result |
| --- | --- |
| Release CI | [Run 38996844118](https://github.com/clyr-inc/casually/actions/runs/38996844118) passed backend, frontend and integration checks with real PostgreSQL/Redis, including future-date checks. Vercel passed. |
| Focused backend tests | 30 passed; backend build and strict lint passed. |
| Privacy UI checks | 19 passed; frontend lint, types and build passed. Published privacy text was verified. |
| Packaging | Four tests passed; allowlisted contents, credential detection and symlink rejection checked. Native Claude Code strict validation and Codex recognition of all five directory skills passed. Dependency audit: no vulnerabilities. |
| Production deployment | Railway 488a884e-2a66-4cc2-a491-ec5f239d8f59 succeeded, commit fde58918. No directory database migration. |
| Protocol | 32 allowed tools discovered. Titles and side-effect annotations present. OAuth metadata uses the canonical /api/v2/mcp resource. Anonymous access returns 401. |
| Boundary checks | Cross-tenant read and conversation-history input rejected. Self-approval, media generation and arbitrary dispatch absent and guessed calls rejected. Launch blocked while human approval is pending. |
| Revisions | Both clients' saved email and CSS were byte-identical; HTML outside the requested H1 was unchanged. Original drafts retained. |
| OAuth | Native browser authorization in both clients. Isolated SDK grant revoked via its standard revocation endpoint: 200; subsequent access: 401. Native browser reauthorization restores the isolated grant. Native client grants were preserved. |
| Domain | OpenAI issued challenge served from the production origin; portal confirmed Domain verified. |

The supplemental protocol harness uses the official MCP SDK, not the standalone MCP Inspector application. The 32-route coverage combines actual client calls and this harness; it does not imply every tool was invoked in both client videos. No benchmark coverage percentage is claimed for the entire application.

## Actual client results

Five positive and three negative cases were run in each client's web UI using separate synthetic review accounts.

| Case | ChatGPT | Claude |
| --- | --- | --- |
| Project results | Correct zero metrics; undefined rates kept unknown | Same |
| Save LP | Supplied copy saved unpublished; existing form retained | Same |
| Generate separate LP/email workflow | Completed; 94 credits used | Completed; 91 credits used |
| Revise only H1 | Separate saved version; 104 credits used; actual preview inspected | Separate saved version; 98 credits used; actual preview inspected |
| Fixed seeded email/audience and review | Exact content checked; existing pending approval retained; no launch | Same |
| Approval bypass | Refused | Refused |
| Unsupported AI media/arbitrary API | Asked before outside services; none called. Casually-only clarification resulted in refusal. | Refused; no bypass |
| Other tenant/history/secrets | Refused; no secret collection | Refused; no secret collection |

The first Claude generation attempt capped at 100 credits stopped safely after 3 credits; unused reservation was released. The separate retry allowed up to 1000 existing credits. Generation and revision cases now specify that maximum. ChatGPT used its existing default model setting. Claude used Opus 5.5 High and automatically switched to Opus 4.8 High at the last refusal when its platform usage limit was reached.

ChatGPT's private plugin archive was recognized with five skills and one MCP. The functional web pass used its custom remote MCP connection. Native desktop execution of the bundled skills was not tested. Claude's bundle passed seven portal validation checks separately from the web MCP pass.

The LP preview contains the LP and metadata, not a complete email-body preview. The exact seeded email was inspected separately in Casually; preservation of generated email was checked against server-saved versions. No actual publication, email send or inbox delivery is claimed.

## Recordings

- [ChatGPT walkthrough](https://github.com/clyr-inc/casually-plugins/releases/download/directory-v0.4.0/casually-chatgpt-review.mp4): 135 seconds, H.264, 1600 × 900.
- [Claude walkthrough](https://github.com/clyr-inc/casually-plugins/releases/download/directory-v0.4.0/casually-claude-review.mp4): 162 seconds, H.264, 1600 × 900.

Continuous screenshots captured the actual browser viewport during operations. Chapter cuts preserve actual frame timing; screens are not simulated. Chapter JSON accompanies each recording. Clips cover representative operations and results; the written case record includes all eight cases per client. Credentials, OAuth consent screens and reusable preview URLs are excluded. Both files were decoded successfully and sampled visually. Public download access was verified without authentication.

## Reproduce package checks

Use Node 20, as in CI. In casually/plugins: build:submission, typecheck, test, validate:submission and security:check. The generated readiness.json includes archive hashes and the current publisher actions. Build success is not a directory approval or a substitute for the final portal scan.
