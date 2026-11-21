# ReadingTrack upload preparation

This package connects to the ReadingTrack remote MCP server. Public listing metadata, five positive and three negative draft review cases, and initial release notes are declared in plugin.json. Cases have not been executed against an authenticated account during this preparation.

The plugin saves supplied Markdown privately and manages private reading lists. It cannot retrieve article bodies, delete lists, or publish content. OAuth uses the pre-registered public client readingtrack-chatgpt with no client secret. Register the exact portal callback before testing the saved submission.

Country targeting is unrestricted (all available countries). The privacy-policy update is published. The demo recording is https://www.youtube.com/watch?v=t0o3iUh9OIc and is declared in plugin.json. Preparation still requires dedicated reviewer access and authenticated execution of the review cases. Provide reviewer credentials only in secure portal fields, never in this ZIP. Complete domain/developer verification, scans, legal attestations and connection checks in the portal. An upload creates a draft; it does not submit or publish it.
