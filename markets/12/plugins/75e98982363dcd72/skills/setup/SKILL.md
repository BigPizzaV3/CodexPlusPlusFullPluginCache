---
name: setup
description: Connect Polytweaks to ChatGPT or Codex and verify access when the user installs or sets up the Polytweaks plugin.
---

# Set up Polytweaks

Use English by default; honor an explicit user request for another language. Browser or host locale alone is not a language preference for Polytweaks.

Use the host's Polytweaks account connection flow. The user signs in to Polytweaks and reviews the requested permissions there. Never request a password, access token, or client secret in the conversation.

If the tools report an authorization challenge, let the host present account linking. After the connection succeeds, use a minimal `list_models` request to verify access. An empty library is a successful connection. Do not claim a connection succeeded before a successful tool result.

The embedded library and viewer use that verified connection through an app-only broker; they do not need a second Polytweaks web login. The frame receives no bearer token or general website session. A failed embedded connection is not a reason to request credentials in chat or expand its permissions. The standalone website keeps its normal sign-in.

Keep setup confirmation brief and continue with the user's task. Do not narrate the library opening or repeat its visible metadata, and do not append a read-only/no-changes report. If an introduction is useful, use one sentence: Polytweaks takes the 3D files created in Astra or this chat into versioned models for review, sharing and AR presentation. Do not recite the tool list or all sharing permissions after connecting.

Creation and editing use authoring tools actually available in the current chat. Saving requires a request to persist the model; model, review and direct AR links require the corresponding sharing request. Existing authorization is sufficient. A model link allows viewing and AR; a review link adds comments and editing one's own comments. Downloads are independent and off by default; passwords are optional and links expire. Explain those settings when relevant to the requested share, not as a setup checklist.

This workflow does not require an OpenAI API key, run cloud revisions, or provide Sign in with ChatGPT identity. It does not install Blender or change the chat's selected model. Verify host authoring and file-transfer support before claiming the full create/edit/preview/save flow is available. Do not collect credentials or imply that the package can enable an unavailable service.

If the connection is unavailable, report the error without claiming setup succeeded. A local Codex chat can still follow `../model-library/SKILL.md` for local authoring and file handoff. Do not make up a connection URL, substitute credentials, or claim that reading a skill or installing the package deploys its server. Users can revoke account access from Polytweaks Settings → Manage ChatGPT access.
