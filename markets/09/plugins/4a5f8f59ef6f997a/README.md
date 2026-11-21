# Cartographer plugin for ChatGPT and Codex

This folder is the OpenAI plugin package for Cartographer. It bundles the
Cartographer skills with a reference to the hosted MCP server at
`https://cartographer.studio/mcp`. The manifest in `.codex-plugin/plugin.json`
carries the listing metadata ChatGPT shows: display name, descriptions, brand
colour, composer icon, logo, legal links and starter prompts.

Everything in `skills/` is a copy. Never edit it here:

- `skills/story-mapping` comes from `3p-plugins/claude/skills/story-mapping`.
  Update it there when the MCP tool surface changes.
- Every other skill comes from the neutral skills pack in `skills-pack/` at the
  repo root.

Run `npm run skills:sync` to refresh the copies. The pack script runs it for
you, and `src/lib/skills-pack.test.ts` fails if the copies drift.

## Try it in a ChatGPT Work workspace (no review needed)

1. In ChatGPT open **Settings → Security and login** and turn on **Developer mode**
   (a workspace admin may need to allow this first).
2. Go to **Plugins**, press **+**, enter a name and description, and under
   **Connection settings** paste `https://cartographer.studio/mcp`.
3. ChatGPT discovers the tools and walks through Cartographer's OAuth login.
4. Open the plugin's **Manage** menu to set the logo and name shown in the
   sidebar, then install it into a conversation from the tools menu.
5. A workspace admin publishes it to everyone from
   **Workspace settings → Apps → Drafts → Publish**.

## Submit to the public plugin directory

1. Run `npm run plugin:chatgpt:pack` to produce
   `3p-plugins/output/cartographer-chatgpt-plugin.zip`.
2. In the OpenAI Platform plugin portal create a draft, choose **With MCP**, and
   upload the zip. The portal reads `.codex-plugin/plugin.json` for the listing.
3. On the **MCP** tab enter `https://cartographer.studio/mcp` and complete
   domain verification: copy the issued token and set it as the
   `OPENAI_APPS_CHALLENGE_TOKEN` secret so it is served from
   `https://cartographer.studio/.well-known/openai-apps-challenge`:

   ```bash
   npx wrangler secret put OPENAI_APPS_CHALLENGE_TOKEN
   ```

4. Fill in test cases and starter prompts, then submit for review.

## What the MCP server already provides

- Server identity with `title`, `websiteUrl` and `icons` in the `initialize` response.
- A title and `readOnlyHint` / `destructiveHint` / `openWorldHint` annotations on every tool.
- An explicit `outputSchema` and matching `structuredContent` response on every tool, without duplicating successful results into legacy text payloads.
- OAuth discovery at `/.well-known/oauth-authorization-server` and
  `/.well-known/oauth-protected-resource`, with PKCE and dynamic client registration.
