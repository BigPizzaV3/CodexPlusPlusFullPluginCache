# Tines 3B for OpenAI

OpenAI plugin for building, running, monitoring, and governing agents, apps, and automations with [Tines 3B](https://www.tines.com/3b/).

The plugin combines the complete [`tines/skills`](https://github.com/tines/skills) collection with the tools advertised by each customer's tenant-specific MCP server. MCP actions run as the signed-in user and retain that user's existing permissions.

## MCP connection

The package declares one templated MCP server in `mcp.json`:

```text
Example URL:  https://example-tenant.3b.dev/mcp
URL template: https://{tenant}.3b.dev/mcp
```

The example URL demonstrates that `example-tenant` is a valid value for `{tenant}`. Under OpenAI's templated-plugin submission guide, it is not a review or test endpoint and does not need to be running or have reviewer credentials.

When a tenant administrator configures an instance, OpenAI applies the URL template and discovers capabilities against that tenant's actual endpoint. Tines 3B supports OAuth dynamic client registration and PKCE. Each user signs in to the configured tenant; service-account tokens can read, run, and ask, but direct build and publish tools require an OAuth user connection.

## Refresh the bundled skills

Run from the repository root:

```bash
bash scripts/sync-openai-skills.sh
```

The script copies every skill from the latest `tines/skills` `main`, includes its license notices, and records the resolved commit in `vendor/tines-skills/UPSTREAM.json`. Set `TINES_SKILLS_REF` to sync a tag or branch explicitly.

Skill content in a published ZIP is a reviewed snapshot. Refresh the skills, increment `plugin.json`'s version, validate, and upload a new ZIP to publish later updates.

## Validate and package

```bash
node scripts/validate-integrations.mjs
bash scripts/package-openai-plugin.sh
```

The package script writes `dist/tines-3b-openai-<version>.zip`. Reviewer credentials and other secrets must never be added to the ZIP.

See [`SUBMISSION.md`](SUBMISSION.md) for the remaining portal and review steps.
