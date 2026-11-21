# ChatGPT web, mobile, desktop, Work and Codex

This package uses Agent Plugins 1.0, one remote Fina MCP and eight skills. OpenAI's `onboardingSkill` points to configure-fina. Do not depend solely on automatic onboarding activation: each financial workflow checks saved setup too. Use the actual Fina connection exposed by the current host; do not hard-code app IDs, tool namespace prefixes, account bindings or local installations.

## No desktop prerequisite

All financial workflows use the same hosted HTTPS MCP. Setup, financial reads and authorized record changes must not require a local server, shell, filesystem, desktop application or marketplace installation. Use the connection exposed by ChatGPT on the current surface. Do not redirect a web or mobile user to desktop merely because these instructions also support Codex. If the host has not exposed or authorized Fina, report that specific connection problem instead of inventing a platform requirement.

Keep useful financial conversation available independently of artifact editing. The requested dashboard and scheduled refresh still require their actual host tools; do not claim those portions succeeded when they did not. Web/mobile workflows must never require a file on the author's computer. A local file chosen for a Codex task is not automatically a cross-device dashboard.

## Artifacts

For a dashboard the user wants to access across devices, prefer an available private cloud artifact that the host can reopen and edit. In web/mobile Chat or Work, use supported private artifacts/visualizations or persistent cloud files. In desktop Work and Codex, reuse that same supported cloud target when accessible; choose a local workspace file only for a local workflow accepted by the user. These are choices based on actual tools, not a promise every surface has the same editor. Store the exact durable target for subsequent updates. Do not upload finances to a public Site, install extra packages/plugins, or require a development server simply to answer a financial question.

## Scheduled updates

For an authorized recurring dashboard or report, use ChatGPT/Work Scheduled tasks. In Codex use its available automation tools; Codex automations and ChatGPT Scheduled are different surfaces. Discover the actual schema and follow host approval requirements. Reuse an existing routine for this target. A native task attached to the conversation is preferable when it retains access to the same artifact; do not assume a fresh scheduled conversation inherits an attachment, local path or MCP grant.

Check that the chosen execution environment can reach the authenticated Fina connection and edit the target. A local file requires the relevant computer/workspace; a cloud task cannot access an arbitrary desktop path. A project task does not automatically gain access to uploaded or project files. Use a verified durable reference supported by its editor instead.

If only a reminder is available, or the target cannot be reopened, mark scheduled updating incomplete and explain the next supported setup step. Keep the useful initial dashboard, but do not describe it as automatically maintained. Do not create a shell cron job, deploy a service or install another plugin as an implicit workaround. The private refresh descriptor and saved task must contain enough instructions for a later run to update the same object without depending on this conversation's transient tool results.

## Files, connectors and access

Use native attachment tools for supplied documents and separately authorized connectors such as Gmail for selected receipts/statements. Fina stores the financial extraction through MCP, not the original files. Do not impose a blanket ban on authorized import workflows. Read-only Fina access supports analysis; recording needs its actual write grant. Never manipulate OAuth tokens or bypass denied tool permissions.

A user-imported development package's availability can differ from a reviewed directory release. If an import is desktop-only, state the actual platform limitation rather than claiming the user's login failed or that the public plugin has already been approved. Installation, MCP authorization, setup and scheduled-run success are separate states.
