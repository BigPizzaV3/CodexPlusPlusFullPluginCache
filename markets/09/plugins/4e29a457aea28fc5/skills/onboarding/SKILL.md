---
name: onboarding
description: Start using Embedr engineering tools and connect a real saved workspace.
---
Use Embedr for electronics and PCB design. Link the user's Embedr account through the host's normal OAuth flow when required. No model API key or paid Embedr plan is required for the core design journey.

Call get_workspace_capabilities. Create a project immediately with the user's original brief and a unique idempotency key. Return its Open in Embedr link. Projects, files and ownership are the same as the web app.

Accept any circuit or PCB brief. Use explicit reversible assumptions where practical. If an actual tool capability or resource limit blocks work, explain the precise blocker, retain partial work and offer a useful next action. Do not invent a category or complexity allowlist.

You own all reasoning and repair. Use explicit source/component/engineering operations; do not send the brief to another cloud model or agent.
