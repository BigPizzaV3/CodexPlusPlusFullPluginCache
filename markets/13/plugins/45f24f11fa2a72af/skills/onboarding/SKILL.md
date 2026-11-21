---
name: onboarding
description: First-run setup for Reducto Office. Checks the connection to the user's Reducto account and helps them sign in if needed.
---

# Set up Reducto Office

Reducto Office connects to the user's Reducto account. Use the account they intend to use for their documents; do not instruct them to select Reducto's internal organization or assume that they are a Reducto employee.

## Check the connection

1. If `list_files` is available, call it.
2. A successful response confirms the connection, even if the file list is empty. Tell the user the account is connected. Offer to open a blank document with `open_editor`, or continue the document task they already requested.
3. If the tools are unavailable, guide the user to enable or connect Reducto Office in their host. If the call specifically reports an authentication or authorization problem, guide them through sign-in using the supported connection flow:
   - ChatGPT: Settings → Apps → Reducto Office → Connect.
   - Codex app: Settings → MCP servers → Reducto Office → Authenticate.
   - Codex CLI: `codex mcp login reducto-office`.
   Host labels can vary; use the connection or authentication control shown for Reducto Office.
4. Sign-in happens in the browser. Ask the user to sign in with their intended Reducto account and complete the authorization flow. Do not claim that external-account access is supported until the server has actually authorized the account.
5. After sign-in, call `list_files` again. Confirm setup only if it succeeds. If tools are still unavailable, ask the user to return to the host and confirm that the connection is enabled before retrying.

## Handle problems

- Do not treat network errors, service failures, or other unrelated errors as proof that sign-in is required. Explain the reported problem accurately and suggest a retry when appropriate.
- If authorization fails after sign-in, explain the returned access problem. Do not tell the user to join Reducto's internal organization, invent account eligibility rules, or repeatedly send them through the same sign-in flow. Direct them to Reducto Office support at https://office.reducto.ai/support if the problem persists.
- Do not create or change documents merely to test authentication. `list_files` is the connection check.
- Never ask for passwords, access tokens, client secrets, or authentication codes in the conversation.
