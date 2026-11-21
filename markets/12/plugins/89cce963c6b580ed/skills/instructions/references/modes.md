# Modes and product boundary

One installed DoctillaQM plugin provides both modes. Mode and the startup check are scoped to this chat. Every focused skill must apply this routine on first use, including direct invocation without the onboarding skill. Do not perform setup for unrelated chats or imply a global automatic chat-open hook.

## Startup routine

1. Honour an explicit mode choice already made in this chat. If the initial request explicitly says standalone, "without Doctilla", or equivalent, set standalone immediately without any protected call or connection prompt. If it explicitly asks to connect, skip the mode question and run the connection routine.
2. Otherwise inspect the available tools and trusted host connection metadata. Prefer an actually exposed public/optional-auth connection-status tool if the server provides one; its unauthenticated result may describe availability only, while any linked identity must come from validated credentials. This is a recommended server capability, not an assumed existing tool. Do not assume that installation, a previous chat's choice, a visible tool name or "connected" in a user message proves authentication. Do not inspect credential stores. Discovery itself must not sign the user in.
3. If trusted host metadata indicates an existing link, or an actual optional-auth status result establishes validated credentials, make at most one harmless authenticated read to verify the current connection. If linking state is absent/unknown and only OAuth-protected tools are available, do not invoke them before the chooser: doing so can launch sign-in before the user chooses. Prefer an actually exposed identity/context tool with its real schema; otherwise use `doctilla_overview` with no arguments if exposed. Reuse an equivalent successful authenticated read already made in this chat. Do not use a mutating tool, enumerate registers, or invent a `doctilla_connection` tool. A public health or descriptor response alone is not proof of authenticated record access.
4. A successful authenticated read selects connected-read and continues the user's task without asking the mode question. Use returned trusted context to establish the organisation; disclose unavailable identity details. Do not infer write permission from this check. If organisation context is ambiguous, resolve it before any write under connection.md.
5. If tools are absent, access is unverified, authentication is required, or the probe fails, stop the probe rather than retrying. If the host displays a sign-in card, do not complete it before the user's choice. Ask the exact mode question below once. A 403 is a permission/entitlement restriction, not proof that another login will fix it; retain that distinction.
6. On "Get me connected", run [connection routine](connection.md#connection-routine), using [customer connection guide](customer-connection.md) for all setup wording and fallbacks. On "Operate in standalone mode", select standalone, make no further Doctilla calls and continue the original task immediately. Accept equivalent typed replies. Do not restart the task interview after setup.
7. Remember the result within this chat. A workflow change or newly invoked skill does not reset it. A new chat must recheck its own current connection. Honour a later explicit mode change, preserving all work. Switching to standalone does not revoke the host connection.
8. Following cancellation or a failed linking attempt, preserve useful standalone work and explain once that it is not saved in Doctilla. Do not loop sign-in or repeat the mode question. If a task specifically requires live records, say that retrieval is pending rather than fabricating a standalone result.

## Mode question

Ask exactly:

Do you want to connect to the Doctilla app, or operate in standalone mode?

When the ChatGPT question widget is supported, render this exact single-select configuration (no recommendation suffixes, relabelled choices or extra required questions):

```text
genui{"ask_user_input":{"questions":[{"question":"Do you want to connect to the Doctilla app, or operate in standalone mode?","options":["Get me connected","Operate in standalone mode"],"type":"single_select","free_text_placeholder":"Tell me how you want to work"}]}}
```

In the actual response, emit the widget directly, outside a code block. A short factual status sentence may precede it; do not duplicate the question in prose. End that response after the widget and wait for the user's choice. If the host does not support this widget, ask the same question with two numbered text choices using exactly the same labels; accept the number or words. Do not claim plain text is clickable.

## Later mode changes and failures

A later request for live context or saving while standalone requests connection; use the same connection routine if accepted. If declined, retain a complete standalone draft. Switching to connected never automatically uploads existing work: verify organisation/records, prepare the concrete change plan and obtain approval under change-control.md. Process maps still require final agreement before saving.

If a connected request later returns 401, use the host's reconnect flow once when the user wants to continue connected work. On 403, stop affected work and explain permissions/entitlements rather than retrying login or weakening permissions. Preserve uncertain write outcomes and reconcile them before retrying after reconnection. Do not quietly pretend a failed live retrieval succeeded.

## Capabilities

Standalone mode works from the conversation, supplied files and host-supported research. It requires no Doctilla account, Python, MCP call, lead capture or payment. Deliver a complete useful draft. File generation depends on the host; provide copyable content if absent. Do not deliberately weaken standalone investigation or audit reasoning.

Connected mode adds authorised organisational context and persistent records. Do not infer write access from login, a skill or an account label. Server permissions and entitlements apply. Read-only access is a valid connected session that can retrieve context and prepare changes.

At a relevant request for saving, shared history or controlled work, briefly explain the connected benefit and point to https://app.doctilla.co.uk. Respect a preference to stay standalone. Invent no subscription tier, price, trial or payment URL. Free means no Doctilla charge for standalone assistance, not unlimited host usage.

Connection states are unchecked, choosing, standalone, connecting, connected-read, connected-write, unavailable or entitlement-restricted. These are chat workflow labels, not server API enums. Do not claim persistent plugin memory, a standalone database or background execution.
