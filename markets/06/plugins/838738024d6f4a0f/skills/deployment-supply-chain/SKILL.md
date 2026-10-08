---
name: deployment-supply-chain
description: Review Cloudflare CI/CD, Git integrations, build credentials, environment separation, dependencies, and release controls.
---

# Deployment and Supply-Chain Security

Review source control and CI identity/permissions, branch and environment protections, deploy hooks, build logs/artifacts, dependency lifecycle, lockfiles, secret injection, production-vs-preview configuration, Wrangler deploy targets, approval gates, provenance where available, and rollback/version history. Seek narrow, purpose-specific deploy tokens; prevent untrusted pull-request code from accessing production secrets; isolate preview data and credentials; pin dependencies where the project’s ecosystem supports it and update with tests.

Treat a green build or successful deployment as operational evidence only, not proof of secure code. Identify checks not run and supply-chain visibility gaps. Do not trigger deployments, dependency upgrades, key rotation, or CI permission changes unless the user specifically authorizes that action.
