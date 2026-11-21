# Spoon Simple — public AI plugin package

Portable OpenAI Agent Plugins package for the Spoon Simple recipe and grocery workflow.

The public remote MCP server is **https://www.spoonsimple.com/mcp**. This plugin uses Spoon Simple's existing recipe catalog and Instacart referral handoff. It does **not** place grocery orders.

## Files

- `plugin.json` — plugin identity and ChatGPT directory metadata.
- `mcp.json` — remote, unauthenticated, read-and-shop-preview MCP connection.
- `skills/plan-and-shop/SKILL.md` — optional workflow instructions.

## Build a submission ZIP

From the repository root:

```sh
python3 scripts/build-spoon-simple-plugin.py
```

Upload the resulting `dist/spoon-simple-plugin.zip` in the [OpenAI plugin submission portal](https://platform.openai.com/plugins). Do not put API keys or credentials in the ZIP.

## Before submission

1. Merge the verified MCP endpoint to `main`, deploy on Vercel, set `SPOON_MCP_ENABLED=true`, and verify the public endpoint.
2. Finish five positive and three negative MCP prompt tests (see `docs/spoon-simple-ai-plugin-review-cases.md`).
3. Confirm privacy policy and retention details, get the exact OpenAI domain-verification token from the portal and set `OPENAI_APPS_CHALLENGE` on Vercel if required.
4. Verify the OpenAI business publisher identity, submit the ZIP, resolve scans, add a real demonstration video, and publish once approved.

If checkout-link generation remains off for launch, describe the grocery-list-to-website fallback accurately in the submitted description. Publishing requires a human review and approval step on OpenAI's side.
