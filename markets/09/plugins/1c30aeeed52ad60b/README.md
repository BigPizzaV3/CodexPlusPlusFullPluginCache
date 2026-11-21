# Scaffolde Capability Builder 0.1.3 policy candidate

**Marketplace candidate, not submittable:** the production endpoint passed synthetic HTTPS tool and SDK checks. Publisher verification, deployment of the bundled approved policy pages, assistant host review, demo and scans remain open.

Node 22+ and Python 3 are sufficient; no dependency installation required.

```
node --test tests/*.test.mjs
node src/server.mjs
node scripts/demo.mjs
python3 scripts/build.py
```

The local server binds only loopback, port 8787, POST /mcp. Tests use an ephemeral port and synthetic data. Some execution sandboxes require permission to listen on loopback. JSON responses implement stateless Streamable HTTP; GET returns 405, notifications 202. Protocols 2025-06-18 and 2025-11-25 are supported. Unknown requested versions negotiate latest; unsupported version headers return 400. No sessions or persistence exist. Request bodies are capped at 64 KiB and application reads have a 10-second deadline. Deployment must wrap this service with approved HTTPS ingress and operational limits; src/worker.mjs supplies a dedicated Worker fetch adapter using the same pure core. wrangler.jsonc defines local production controls; wrangler.production.jsonc adds the approved custom domain. The production config records the deployment owner’s live settings; local config retains the tested older workerd baseline. Native rate limiting is required and fails closed when unavailable. Local handler tests run under Node; the shared review cases also passed against actual local workerd using existing Wrangler 4.134.0 with compatibility date 2026-09-24. Production HTTPS tests pass 12 active checks including exactly five positive and three negative tool cases, plus official MCP SDK initialize/list/call. See docs/READINESS.md for provenance and limits.

Tools individually expose template listing, template retrieval, structural validation and Markdown rendering. Drafts are bounded to 64 KiB overall; names 80 characters, goals 4000, other texts 2000, arrays 32 entries. The service accepts only named schema fields. It never executes instructions, resolves URLs, installs generated skills, writes user-selected files or changes external state. Draft text is data. Markdown punctuation and HTML are encoded; raw goal remains verbatim in structured output. Do not feed rendered text into an execution system without review.

Validation checks structure, claim uniqueness and evidence references only. It always reports needs_review and not_runtime_tested. No runtime safety/correctness claim is made. ID continuity across separate revisions is assistant-managed; the stateless service cannot prove it. User-supplied inputs, outputs, steps, constraints, non-goals and probes are retained as text, not executed.

The portable root plugin.json and mcp.json are canonical. The assistant skill is bundled under skills/. docs/REVIEW-CASES.json contains proposed review prompts and actual local status. The reproducible build uses an explicit allowlist and fixed ZIP metadata, excludes tests/evidence/private state, validates archive limits and emits a SHA-256 hash. The development ZIP includes service source for reproducibility; a hosted connection does not deploy that source automatically.

Local Worker verification with existing Wrangler:

```
WRANGLER_SEND_METRICS=false wrangler dev --local --ip 127.0.0.1 --port 8899
TEST_MCP_URL=http://127.0.0.1:8899/mcp node --test tests/review.test.mjs
```

The direct HTTP stalled-upload probe is skipped on the Wrangler proxy because it buffers incomplete uploads; direct Node protection and the actual workerd body helper are tested separately. tests/workerd-harness.mjs is local-only and excluded from distribution.
