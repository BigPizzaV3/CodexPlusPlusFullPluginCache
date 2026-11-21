# Release notes

## 1.0.4

- Adds the captioned 1080p reviewer video walkthrough URL to the manifest.
- Aligns the Northstar proposal case with the saved-project workflow shown in
  the video and already documented in `TEST_CASES.md`.
- Includes the current OAuth base scopes needed to run the reviewer workflows
  at initial connection.
- Preserves the listing title and About copy, the remaining review cases, and
  the production MCP endpoint.

## 1.0.3

- Replaces basic task examples with five independent end-to-end reviewer
  scenarios spanning qualified prospects, proposals, client approval,
  contracts, sprint setup, and delivery-risk reporting.
- Adds precise, observable expectations for every read and write operation.
- Keeps the marketplace title, About copy, MCP endpoint, and tool surface
  unchanged.

## 1.0.2

- Updates the marketplace positioning to "From first client conversation to
  final payment."
- Introduces listing copy focused on freelancers and agencies running client
  work conversationally through ChatGPT.
- Keeps claims aligned with the currently exposed MCP tool surface.
- Does not change the MCP endpoint or tools.

## 1.0.1

- Refines the marketplace positioning around MoodLens To-Do's differentiated
  prospect-to-delivery workflow for client-facing teams.
- Highlights the connected flow across prospects, proposals, contracts,
  delivery work, documents, and tracked time.
- Does not change the MCP endpoint or tool surface.

## 1.0.0

Initial public-submission package for the MoodLens To-Do remote MCP server.

- Adds the universal plugin manifest used by ChatGPT and Codex.
- Connects to the production Streamable HTTP endpoint at
  `https://moodlenstodo.com/api/mcp`.
- Adds OAuth protected-resource and authorization-server discovery, public
  Dynamic Client Registration, exact resource/issuer binding, and S256 PKCE.
- Uses a minimal read-only initial scope with per-tool step-up challenges for
  broader reads and write actions.
- Rotates refresh tokens and atomically revokes a token family when reuse is
  detected.
- Publishes precise per-tool OAuth scopes, human titles, and complete safety
  annotations for ChatGPT, Codex, and Claude.
- Returns standards-based HTTP authentication challenges and mirrors the same
  challenge in tool-result metadata for ChatGPT account linking.
- Keeps bearer credentials out of the internal MoodLens operation executor.
- Provides listing copy, five positive reviewer test cases, three negative
  reviewer test cases, and a submission-readiness checklist.
- Uses the existing public MoodLens website, help center, privacy policy, terms,
  and production icon URLs.
- Includes no custom UI and no bundled skill in this release.
