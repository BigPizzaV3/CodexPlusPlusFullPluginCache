---
name: environment-troubleshooting-xs3
description: Diagnose ChatGPT-side generic tool refusals separately from RemoteCommander, device and rate-limit errors; verify effects and recover authorized tasks through supported, permitted interfaces.
---

# Environment troubleshooting — ChatGPT / RemoteCommander

// XS3 v3.2: subject–predicate–object edges; ; repeats the subject.
// Only for ChatGPT/RemoteCommander execution friction; not a general troubleshooting or deployment skill.

#skill a skill; scope #chatgpt-remotecommander-friction; goal #resume-original-authorized-task; excludes #environment-setup, #project-release-policy, #tool-installation.
#agent preserve #user-intent, #authorized-scope, #project-permissions !must; respect #concrete-risk, #binding-platform-restrictions !must.
#flow steps <#capture #classify #reconcile #probe #recover #verify #report>.

// Capture what happened, not a guessed explanation.
#capture record #original-goal, #target-device, #tool-invocation, #visible-error, #last-confirmed-effect, #possible-side-effects !must.
#tool-invocation includes #tool-name, #exact-arguments, #selected-device.
#failure-layers include #provider-surface, #connector-transport, #remotecommander-tool, #device-command, #local-permission, #owner-rate-limit.
#provider-surface observed-as "This tool call was blocked by OpenAI's safety checks."; supports #observed-invocation-refusal; root-cause UNKNOWN.
#observed-invocation-refusal ¬proves #unsafe-intent; ¬proves #revoked-access; ¬proves #device-offline; ¬proves #remotecommander-broken; ¬proves #owner-rate-limit; ¬proves #target-changed.
#connector-transport evidence #connection-or-delivery-error; effect UNKNOWN.
#remotecommander-tool evidence #actual-tool-error; action #inspect-tool-contract.
#device-command evidence #actual-exit-code-or-stderr; action #diagnose-command.
#local-permission evidence #specific-permission-result; action #respect-effective-permission.
#owner-rate-limit evidence #explicit-service-limit-signal; action #honor-retry-after.
#agent distinguish #observed-refusal-layer !must; from #unverified-root-cause; infer #policy-breach-from-generic-error !🚫.

// A suspected false positive is an evidence-based hypothesis, not authorization.
#risk-assessment consider #user-authorization, #original-scope, #requested-effects, #reversibility, #third-party-impact, #specific-risk-evidence.
#warning-status options CONCRETE_RISK, SUSPECTED_FALSE_POSITIVE, INSUFFICIENT_EVIDENCE.
#CONCRETE_RISK requires #specific-supported-risk-evidence.
#SUSPECTED_FALSE_POSITIVE requires #routine-authorized-action, #generic-surface-refusal, #risk-context-reviewed; status #hypothesis-not-verified-cause.
#INSUFFICIENT_EVIDENCE applies "neither concrete risk nor a suspected false positive is adequately supported".
#agent classify #warning-status !must; based-on #risk-assessment; infer #SUSPECTED_FALSE_POSITIVE-from-generic-error-alone !🚫.

// Resolve possible side effects before repetition.
{?op a operation; possible-side-effect true; outcome UNKNOWN} => {#agent inspect #actual-target-or-existing-process-handle !must. #agent blind-replay ?op !🚫}.
#probe use #device-identity-check, #fs-roots-check, #doctor-check, #history-check, #process-status-check, #authorized-read-only-target-check.
#device-identity-check tool "list_devices". #fs-roots-check tool "fs(op=roots)". #doctor-check tool "doctor".
#history-check tool "history(op=list)". #process-status-check tool "process(op=status/read)".
#probe establishes #observed-capability-only; ¬establishes #original-task-completion.

// Recovery methods are for technical compatibility, not bypassing a platform refusal.
#technical-friction examples #argv-quoting-error, #shell-incompatibility, #interpreter-mismatch, #file-transfer-encoding-error.
#raw-argv method "exec/process with a literal argv array"; addresses #shell-quoting-error.
#alternate-interpreter requires #already-installed-compatible-interpreter, #authorized-task; addresses #interpreter-compatibility-error.
#base64-file-staging method "fs.write(encoding=base64) creates an ordinary inspectable file"; addresses #file-transport-encoding-error.
#technical-fallback requires #identified-technical-friction, #permitted-execution, #inspectable-unchanged-intent.
#platform-refusal recovery #official-diagnostics-and-bounded-permitted-retry; restriction #no-representation-switch-to-evade-refusal.
#agent use #technical-fallback !must; only-for #technical-compatibility; evade #platform-refusal !🚫.
#agent repeat #refused-invocation-beyond-permitted-bounds !🚫; continue #independent-permitted-work !must.
{#authorized-capability available true} => {#agent resume #original-task !must}.

// Outcome and warning are independent axes; prove the requested effect.
#task-status options RESOLVED, BLOCKED, UNKNOWN.
{#requested-effect verified-on-target true} => {#task-status is RESOLVED}.
{#necessary-permitted-capability demonstrably-unavailable true} => {#task-status is BLOCKED}.
{#binding-restriction applies-to-required-operation true} => {#task-status is BLOCKED}.
{#actual-outcome cannot-be-verified true} => {#task-status is UNKNOWN}.
#agent require #actual-result-evidence !must; for-claim RESOLVED.
#BLOCKED ¬requires #exhaust-every-alternate-path.
#report include #original-goal, #observed-layer, #actual-diagnostics, #permitted-recovery-attempts, #verified-effects, #uncertainties, #task-status, #warning-status !must.
