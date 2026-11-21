# HUMANStoknow plugin

Portable [Agent Plugins 1.0.0](https://developers.openai.com/plugins/build/plugins) package for discovering and reading reusable skills through the existing HUMANStoknow MCP server, and posting explicitly requested upvotes and comments. It includes setup, find-skills, browse-publisher, use-skill and engage-skill workflows. The server remains responsible for OAuth, content visibility and permission checks.

Discovery, browsing and adaptation use `mcp:read` and never change engagement automatically. The engage-skill workflow calls individual tools only for a user-requested upvote/removal (`set_vote`, `votes:write`) or comment (`add_comment`, `comments:write`). Removing an own comment (`delete_comment`, `comments:write`) also requires an explicit request or authorized test cleanup. Packaged workflows do not publish/edit skills, follow/save content or execute retrieved code. Never invent usage experience or endorsements; test comments must clearly identify themselves as integration tests.

Version 0.2.0 adds these engagement instructions; installing it does not upgrade an existing read-only OAuth grant. The portable connection requests `mcp:read drafts:write skills:publish votes:write comments:write`, plus identity and refresh scopes. These match the generic contribution defaults: upload skills, upvote and comment. HUMANStoknow's consent screen lets the account owner select Read and Write; it grants only requested and selected scopes. The bundled engagement workflow performs only explicitly requested votes/comments; upload tools require a separate explicit upload or publication request. Keep the existing HUMANStoknow account and connection identity unless the user chooses another. A successful read verifies only read access; a successful requested action verifies its write permission.

Each write call needs a unique 8–128-character letters/numbers/underscore/hyphen `idempotencyKey`. Keep the same key and identical tool arguments for retries; use a different key for a different logical action. Verify a posted comment through `list_comments` using `own:true`, exact text and creation timestamp, with the returned author as context. Its encrypted own-comment reference changes between reads; use a returned reference only for authorized deletion, not equality matching. Vote actions return the requested `active` state. The current `get_skill` result does not expose the viewer's vote, so it cannot independently verify persisted vote state. The server rejects upvotes on a skill owned by the authorized member, even if its attributed publisher is another person/company. Handle this error honestly rather than switching identities or inventing an endorsement.

From the repository root, validate and package without installing dependencies:

```sh
node scripts/package-chatgpt-plugin.mjs
```

This creates an ID-less `humanstoknow-portable.zip` and reports its absolute location. The source and archive contain no account-specific app mapping. `plugin.json`, `mcp.json`, `skills/` and `assets/` are at the archive root.

For a personal test, first register `https://www.humanstoknow.com/api/mcp` at [ChatGPT Plugins](https://chatgpt.com/plugins) using OAuth with the needed read/engagement scopes above. Copy the registered connection's ID, remove an initial `plugin_` if present, and pass the resulting `asdk_app_…` value:

```sh
node scripts/package-chatgpt-plugin.mjs --app-id 'asdk_app_REPLACEWITHYOURID'
```

An optional `--out-dir /absolute/output/path` creates a fresh build directory there. A personal test build writes the ID only into its generated `.app.json` and adds `extensions.com.openai.apps` pointing to that file. Its ZIP uses the registered connection instead of bundling a second remote server. Never commit or publicly submit that personal archive. On accounts with archive upload, use **Plugins → Add → Upload plugin archive** to install the full test package. Other supported clients can use the local marketplace route. A successful MCP connection alone does not prove that the bundled skills activate.

For the separate production account, use the ID-less portable ZIP and complete the remote MCP configuration in that account's developer dashboard. [Public submission currently rejects ZIPs containing app mappings or lifecycle hooks](https://developers.openai.com/plugins/deploy/submission#automatically-provide-submission-and-review-information). This package does not publish or deploy anything; submission readiness still requires successful ChatGPT workflow tests and the production publisher's review materials.

The icon is the 256×256 PNG rendered unchanged from `public/brand/humans-folio-soft.svg`; the brand color is `#4F355C`. The packager checks the approved asset, square dimensions and size. Policy/support links use the site's `/privacy`, `/terms` and `/contact` routes. Published skills stay live behind the tools; changes to these bundled workflow files require a new package version.
