---
name: looki-profile
description: Retrieve the user's Looki account profile through the connected Looki MCP; use for questions about the user's Looki identity or when name, email, timezone, region, or another profile field is required to answer or interpret a request.
---

# Looki Profile

Retrieve account-level information from the user's Looki profile. Keep this workflow separate from captured memories: profile fields describe the account and must not be treated as evidence of activities or experiences.

## Workflow

1. Call `Looki:get_user_profile` once.
2. Select only the profile fields required by the request.
3. Use the returned timezone to interpret relative dates when another Looki workflow needs it.
4. Answer directly from the returned profile and state when a requested field is absent.

## Example requests

- "What timezone is my Looki account using?"
- "Show me my Looki profile."
- "Which region is associated with my Looki account?"

## Guardrails

- Use Looki MCP tools only; authentication is provided by the connected OAuth session.
- If Looki tools are unavailable, ask the user to enable the Looki plugin and complete OAuth.
- Treat name, email, birthday, gender, timezone, and region as sensitive personal data.
- Do not expose the full profile when one field is sufficient.
- Do not infer identity, demographics, preferences, relationships, or behavior beyond the returned fields.
- Do not request API credentials or read local credential files.

## Response style

- Lead with the requested profile information.
- Avoid repeating identifiers or unrelated private fields.
- Explain briefly when a profile field is being used only to interpret another request, such as resolving “today” in the user's timezone.
