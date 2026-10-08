# Baseten

Set up the Baseten CLI, authenticate with Baseten through browser OAuth, verify the active profile, and install Baseten's official skill globally for general model API, deployment, development, and monitoring workflows.

This plugin contains one onboarding skill and does not vendor model-specific deployment workflows. After onboarding, use the globally installed official Baseten skill for workload implementation.

## Official Baseten skill

The official skill is maintained by Baseten at [basetenlabs/baseten-skills](https://github.com/basetenlabs/baseten-skills) and gives the agent current guidance for managing a Baseten workspace: deployment status and health, logs and debugging, promoting deployments, adjusting autoscaling, and related operations. It is read-only by default, with mutations gated through the agent's normal approval policy.

Baseten's [Connect your coding agent](https://docs.baseten.co/agent-setup) guide documents the full agent toolkit — the skill plus two optional MCP servers (`https://api.baseten.co/mcp` for workspace management, which requires a dedicated API key, and `https://docs.baseten.co/mcp` for documentation search). This plugin's onboarding installs only the skill; add the MCP servers separately by following that guide if deeper workspace integration is needed.

## Requirements

- Install Homebrew before running onboarding on macOS or Linux. The skill uses Baseten's documented `brew tap basetenlabs/baseten && brew install baseten` flow; on Windows it uses the documented manual binary install from Baseten's GitHub releases.
- Install Node.js with `npx` to install Baseten's official skill from [basetenlabs/baseten-skills](https://github.com/basetenlabs/baseten-skills).
- Complete Baseten CLI authentication in Baseten's browser flow (`baseten auth login`). Never paste credentials into chat.
- Export `BASETEN_API_KEY` when a Model API or inference client requires API-key authentication. Keep it out of source files, logs, and command arguments.

The Baseten CLI is in beta; commands and flags may change. Authoring Chains, Training jobs, and Loops still uses the separate Truss CLI, which this plugin installs only on explicit request for such a workload.

Deployments can consume billed GPU resources. The onboarding skill performs no deployment and requires explicit user approval before a later workflow creates or changes cloud resources.

The positive and negative test cases and their coverage are documented in [test_prompts.md](test_prompts.md).

## Distribution

This plugin is intended for submission to the [OpenAI plugin directory](https://developers.openai.com/plugins/deploy/submission) as a skills-only package published by Baseten.
