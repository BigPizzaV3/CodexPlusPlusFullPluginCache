---
name: cloudish-deploy
description: Prepare, deploy, and troubleshoot applications for Hal9 Cloudish when the user asks to deploy an app, website, API, container, Dockerfile, or source project to Cloudish.
---

# Cloudish deployment workflow

Cloudish is Hal9's agent-first container deployment service. It runs containerized products in isolated environments and can deploy from a Docker image or source/Dockerfile, with persistent storage and a live URL.

Use this skill when the user explicitly mentions Cloudish, cloudish.ai, or asks to deploy a containerized application to Cloudish.

## Source of truth

Cloudish's agent instructions are published at https://cloudish.ai/skill.md. When that resource is available through the current environment, consult it before inventing API calls, endpoint names, request fields, authentication headers, or deployment commands.

Do not fabricate Cloudish API details. If the current environment cannot access the Cloudish skill documentation or API, explain exactly what is known and ask for the relevant Cloudish API documentation or credentials rather than guessing.

## Workflow

1. Inspect the user's project files when available.
2. Identify the application entrypoint, exposed port, Dockerfile, persistent-data requirements, environment variables, and external services.
3. If a Dockerfile exists, prefer it. If not, propose or create a minimal Dockerfile appropriate to the detected stack.
4. Check that the container binds its service to `0.0.0.0`, not only `localhost`, and that its intended port is clear.
5. Preserve secrets: never print API keys, tokens, passwords, or credentials into chat, source files, or logs.
6. Before a real deployment action, confirm the target and any material cost/spend implications if they are not already explicit.
7. Use only verified Cloudish commands/API operations from the current Cloudish documentation or an available Cloudish integration.
8. After deployment, report the deployment identifier and live URL when returned by the service, plus any important persistence, environment-variable, or networking notes.
9. If deployment fails, diagnose the concrete error first; do not claim the deployment succeeded.

## What Cloudish is for

Cloudish is designed for agents such as Claude Code, Codex, and Cursor to turn a prompt or containerized source into a live website, API, or product. Public Hal9 material says Cloudish supports Docker images or source builds, persistent storage, isolated runtimes, and a free API key with no signup.

Do not conflate Cloudish with Hal9 Startups. Cloudish is the container deployment product; Startups is a separate product-development service.

## If the user only wants setup help

Give a concise checklist covering:
- project/source location
- Dockerfile or image
- exposed application port
- required environment variables
- persistent storage paths
- Cloudish API credentials
- desired hostname/product name

If the user provides a project in the conversation, inspect it rather than asking them to restate its structure.
