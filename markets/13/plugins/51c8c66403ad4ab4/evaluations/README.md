# Routing and client acceptance evaluations

Use routing.json unchanged for baseline and candidate. Run each case three times
in fresh tasks on Codex desktop/CLI, Claude Code/Desktop/Web, ChatGPT MCP, and
Gemini CLI. Use a test account with the named fixtures; substitute only fixture
names, not intent. No evaluation may change production data.

Record JSONL rows with: variant (baseline/candidate), scenario_id, repetition,
client, client_version, model, model_version, first_skill, handoffs, completed,
wrong_domain_calls, invalid_arguments, corrective_calls, tool_calls,
unauthorized_mutations, latency_ms, response_bytes, notes.

Use nonempty strings for client/model identities and versions, a fixture
scenario ID, and integer repetition 1, 2, or 3. `completed` is a JSON boolean;
call/error/mutation counts and `response_bytes` are nonnegative integers.
`latency_ms` is a finite nonnegative number. `first_skill` is one of setup,
operations, diagnostics, or analysis; `handoffs` is an array of those names and
`notes` is a string. Malformed rows fail validation before scoring, including
unrecognized variants, missing fields, negative counts, and non-finite latency.

Record the observed skill and handoffs even when they are wrong. The reporter
compares them against each fixture's `starting_skill` and `allowed_handoffs`,
reporting `incorrect_initial_skills` and `disallowed_handoffs`. Such observations
remain in the comparison; they are not malformed rows. Neither derived score
may regress for a client/model, even when aggregate call counts improve.

Read tool traces to assess skill/tool selection; do not infer completion from
agent prose alone. Cases needing consent must stop before writes until the
scripted consent arrives. Unavailable tools and permission errors must not lead
to alternate-endpoint bypasses. Record absence of a host feature as unsupported,
not a passing test. Keep credentials, user data and SQL results out of reports.

Run `python3 scripts/plugins/report_routing_evals.py report.jsonl` to compare
completion, errors, call counts, response size and median/p95 latency. Both
variants must include all scenarios and matching client/model/repetition coverage.
No fabricated baseline or model results are permitted.

Release gates: zero unauthorized mutations; no authorization regression; all
contract tests pass; reduced wrong-domain/corrective calls without lower task
completion. Verify three-to-one analysis startup separately from overall latency.

For each real client also test fresh install (exactly one authorization flow),
concurrent skills, reconnect, expiry, stale-registration migration, representative
reads/writes, MCP Apps rendering where available and guided-input fallbacks.
Count interactive authorization flows, not HTTP redirect hops. Record any
host-specific duplicate-login behavior as a blocking acceptance failure.

For shared-grant acceptance, authorize `/mcp` once and reuse the resulting token
at all three same-environment endpoints. Verify standalone grants cannot cross
endpoints, read-only scopes still reject writes, and expiry rejects the token
everywhere. Confirm pre-rollout tokens/codes retain their audiences. Separately
check host credential-store behavior; server token acceptance alone does not prove
that independently configured client integrations reuse authentication.

### Refresh-token acceptance

On each supported client, refresh discovery, register with `authorization_code`
and `refresh_token`, and authorize once. Confirm that expiry of the 12-hour access
token triggers a refresh exchange with no browser login, that the client stores the
rotated refresh token, and that account and analysis calls still share the connection.
Exercise simultaneous refresh requests and retry after a lost response within the
30-second retry window. After revocation, idle expiry or absolute expiry, confirm
that the client requests authorization rather than looping on refresh. Existing
access-token-only installations need one new authorization; independently installed
integrations still have independent client credential stores. Backend tests cannot
establish these client UI behaviors.

For the Redis transaction regression suite, set `MCP_REFRESH_TEST_REDIS_URL` to a
local disposable Redis URL and run `app/mcp/test_refresh_tokens.py` with the normal
synthetic backend test environment. Tests use a unique key prefix and remove only
their own keys; they do not flush the database.
