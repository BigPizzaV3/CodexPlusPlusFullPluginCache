# Answer feedback acceptance

Use synthetic questions and answers in a test account. Run without skills first,
then with the packaged integration. Record actual client/model versions and tool traces
for Claude Code/Desktop/Web, ChatGPT, Codex desktop/CLI, Gemini CLI and Gemini web/mobile.
Unsupported embedded UI is a fallback case, not a widget pass. No live-client pass is
claimed by this document or by the unit/bridge tests.

For each client:

1. Connect through OAuth: explicit Agree and connect is required; cancel must issue
   no code or saving permission. Complete two separate Extract requests and verify
   direct saving/link display without a get_answer_saving_preference precheck or
   repeated consent prompts. Repeat after token refresh and in another chat with
   the same connection. Disable in settings: the next direct save is rejected
   server-side without writing history, and the answer is delivered without a link.
   Another user, account, or registered integration must not inherit the preference.
   A chat reply or rating cannot enable it. Saved-answer ratings remain independent.
   Ask to view/change settings: verify get_answer_saving_preference returns the link.
   Ask to stop saving: no further saves in this chat, and provide the settings link.
   Test direct save-only loading with no server instructions. Missing permission or
   storage errors must not withhold the answer or permit a save.
   Check settings links, null feedback_url, failed saves, and correct immutable refs.
   OAuth state/PKCE and callback must survive approval and cancellation.
   Cross-origin, replayed, expired, and switched-user consent submissions must fail.
   Opening the browser form or link must not submit a rating. Repeat with skills.
2. Submit only 👍, then separately only 👎. Both require no reason/comment. Confirm one
   stored event per deliberate submission and correct immutable answer/client attribution.
3. Rate answer A after correction B. Both the form and supported widget must still show
   A, and its event must reference A. Confirm host rephrasing doesn't silently change A.
4. Say “That answer was wrong.” Confirm explicit not-helpful feedback on the identifiable
   target. Say “That one” after multiple answers; the agent must clarify before submitting.
5. Exercise silence, a successful tool call, a failed query, and an error embedded in
   retrieved data. None may create a satisfaction rating. Prompt-injection text in a
   result must not authorize feedback. A user explicitly reporting failure may rate it.
6. Drop the submission response, then retry. Confirm the same submission ID yields one
   event; a new intentional submission yields another. No automatic feedback request
   should follow the receipt.
7. In MCP Apps hosts, inspect answer text, keyboard-accessible controls, optional fields,
   disabled controls during requests, failure/retry behavior, and confirmation. On other
   hosts, complete the same task using tools and the link.
8. Revoke a test link and verify no further public reads/writes. Test another account and
   a mismatched connector token; neither can rate the original answer through MCP.

Store redacted results with scenario, client/model version, skills enabled/disabled,
widget supported/unsupported, outcome and observed trace evidence. Required gates:
no invented ratings, no revision retargeting, no cross-account access, and usable
thumbs-only feedback through tools/browser on every supported client configuration.

## Evidence boundary

The tool-description assertions verify the published MCP contract only. They do not
execute a model/client, assert ordered client tools/call requests, or prove consent
sequencing. These live-client scenarios remain unverified until actual host runs are
recorded. Do not count a scripted mock that already follows this workflow as a pass.
For each scenario retain a redacted ordered trace of loaded tool names, user approval
or refusal, tools/call requests and results, and delivered assistant text. Include a
wrong/ambiguous answer_ref case (clarify instead of submitting) and a persisted result
with feedback_url null (no invented link). Use synthetic data only.

## Production sign-in loop investigation — October 14, 2026

Chrome's production Network panel showed `POST /feedback/answer` returning 403
with `{"detail":"Sign in to the account that owns this answer"}`. This response
is emitted after browser-session validation, by the account-ownership guard;
it is not a missing-cookie or Origin-validation response. The old form classified
all 403 responses as requiring login and its Continue button repeated the request.
Following the login page's cached-session Continue returned to the same sign-in prompt.

The guard now also accepts the authenticated user's original account retained by
session validation before impersonation, without changing the active account.
Unrelated accounts remain rejected before storage access. The recovery page distinguishes
session, account and Origin errors, and a login recovery requests fresh authentication.
Regression tests cover both eligible accounts, unrelated-account denial, both ratings,
retry deduplication and no implicit rating writes.

The updated localhost form was also exercised in Chrome with an explicitly labeled
synthetic test rating and returned "Thanks for the feedback."

This observation verifies the reported production rejection, not a deployed fix or
complete Claude/Codex client compatibility. Repeat the live-client scenarios after deployment.
