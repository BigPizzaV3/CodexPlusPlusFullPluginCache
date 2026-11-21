# Pistonlog plugin package

For workshop users, see [Using Pistonlog in ChatGPT](../../docs/chatgpt-user-guide.md): optional connection setup, permissions, review cards, delivery status, disconnection and troubleshooting. This repository guide is not a published customer help page or proof of directory availability.

This is the source package for the ChatGPT integration. The backend is live and the account-installed [Pistonlog cloud plugin](https://chatgpt.com/plugins/plugin_asdk_app_6acb67dacd548191882ab54f627a5b9a) connected successfully on 11 October 2026. Real profile/context, booking, estimate, invoice, assigned-work, jobcard, customer and vehicle reads succeeded in ChatGPT with matching server audit evidence; host refresh rotation also succeeded. OpenAI accepted the separate public submission on 12 October: the recorded portal status is Version 1.0.0, In review and Not published. Domain verification and the 172-tool scan passed. This is the dated submission checkpoint, not a fresh public-availability check or full release certification. See [implementation status](../../docs/chatgpt-integration-progress.md).

The canonical portable files are `plugin.json`, `mcp.json`, `skills/` and `assets/icon.png`. The `.codex-plugin/plugin.json` and `.mcp.json` files support the existing Codex format. Keep names, versions, presentation and server URLs consistent. The portable format uses `streamable-http` and explicitly declares predefined OAuth client authentication; the compatibility format uses `http`. Client secrets are supplied only in the host's credential field.

The configured endpoint is the existing Pistonlog app, `https://app.pistonlog.com/api/mcp`, backed by its existing Supabase database. General rollout and supported writes are live on 11 October 2026, following Ross's explicit instruction to ship without a pilot gate. Normal membership, role, consent and plan checks still apply. Account linking and authenticated context reads are verified; individual domain workflows need their own evidence. Use synthetic records for deployed mutation checks and keep destructive/concurrency tests on the owned local test database. A separate cloud project is not required.

Run the repository consistency check:

```sh
node scripts/chatgpt/validate-package.mjs
```

The plugin-creator manifest validator and skill-creator validator have also passed locally. Their Python runtime needs PyYAML. The consistency check is dependency-free and runs in CI; it does not replace OpenAI host validation or public-directory review.

For ChatGPT setup, use the existing HTTPS endpoint and predefined OAuth client configured in production. The actual setup UI confirmed `client_secret_post` and the exact callback `https://chatgpt.com/connector_platform_oauth_redirect`. The dedicated credential was entered with Ross's approval, and sign-in, workshop consent and token exchange completed. Follow [the runbook](../../docs/chatgpt-integration-runbook.md) for account linking and permission/workflow checks. This package contains no secrets or registered app ID. Do not invent a `plugin_asdk_app...` identifier: add a registered mapping only after the host returns it.

One connection selects one workshop. The connection may expose company-shared customers and vehicles when the user grants the relevant access. Permissions are checked again on every operation, including confirmation. The server's confirmation protocol is the authorization boundary; bundled skill instructions only guide conversation behavior.

The manifests include Pistonlog's existing privacy, terms and support pages, verified reachable on 11 October 2026. Reachability does not establish that the disclosures cover this integration. The submission includes the approved synthetic reviewer account, cases and walkthrough recording. Remaining qualification and disclosure work is tracked in [the runbook](../../docs/chatgpt-integration-runbook.md) and [release protocol](../../docs/chatgpt-integration-release.md). The live rollout remains enabled at Ross's request; submission does not turn outstanding workflow, privacy, accessibility or operational checks into passes. The source package alone does not create a local marketplace entry or public submission.

Packaging follows [OpenAI's current plugin documentation](https://developers.openai.com/plugins/build/plugins).
