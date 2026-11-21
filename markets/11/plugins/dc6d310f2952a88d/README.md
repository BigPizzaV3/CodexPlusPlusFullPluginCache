# SMEPost Marketing Workdesk

SMEPost Marketing Workdesk lets ChatGPT, Codex, and Claude Code manage social content projects, folders, saved designs, and design versions through SMEPost's Workdesk MCP endpoint.

The plugin connects to `https://smepost.io/api/mcp/workdesk` and uses the existing SMEPost organization, project, folder, material, and version records. The server enforces access and upload permissions. OAuth tokens stay with the MCP host; do not copy credentials into prompts, files, or shell commands.

## Included workflows

Conversations stay in ChatGPT, Codex or Claude Code. In ChatGPT, Workdesk opens in the thread side panel beside the conversation. Project links returned by Workdesk open the ordinary SMEPost website. An explicitly approved publishing handoff opens the existing full website review.

The six bundled skills are `workdesk-basics`, `create-social-project`, `generate-social-design`, `organize-designs`, `revise-design`, and `prepare-social-content`. They guide the host through organization selection, project and folder setup, design import, version history, and optional publishing handoff.

ChatGPT should pass generated or supplied files to `import_asset_file`; SMEPost downloads them on the server, validates their image type and size, and saves them without SMEPost image-generation credits. Codex should use an image-generation capability actually available in the current session, and Claude Code should use an image supplied by the user or an already available external image tool. Neither workflow assumes image generation is available in the host. Ask before starting an SMEPost credit-gated image-generation workflow.

For imported designs, `sourceHost` records asset provenance as `chatgpt`, `codex`, or `claude_code`. The plugin does not emit Workdesk funnel events or add UTM tracking.

## Install locally

Use the checked-out repository path as the marketplace source. These commands install the plugin in the selected host; they do not publish the private repository.

### Codex

```powershell
codex plugin marketplace add C:\path\to\sme-post
codex plugin add smepost-marketing-workdesk@smepost-local
```

Start a new Codex session, complete the SMEPost sign-in when prompted, then ask the plugin to list your organizations. Codex discovers the portable manifest in `smepost-marketing-workdesk-plugin/plugin.json` and its `mcp.json`.

### Claude Code

```powershell
claude plugin marketplace add C:\path\to\sme-post --scope local
claude plugin install smepost-marketing-workdesk@smepost-local --scope local
```

Start a new Claude Code session, complete SMEPost sign-in, and ask it to list your organizations. The Claude plugin manifest is `smepost-marketing-workdesk-plugin/.claude-plugin/plugin.json`; its MCP server is configured by `smepost-marketing-workdesk-plugin/.mcp.json`.

## Production and local endpoint

Production is configured by default at `https://smepost.io/api/mcp/workdesk`. To test against SMEPost's local tunnel, change the configured MCP URL to `https://local.smepost.io/api/mcp/workdesk` before installing or in the host's local plugin configuration. Codex uses `smepost-marketing-workdesk-plugin/mcp.json`; Claude Code uses `smepost-marketing-workdesk-plugin/.mcp.json`.

For a local emulator, configure the MCP URL as `http://127.0.0.1:9002/api/mcp/workdesk`. This is intended only for local testing. The upload helper blocks loopback URLs unless you explicitly pass `--allow-localhost`.

## Import a local image

After `prepare_asset_upload` succeeds, save its result as a temporary JSON file and upload the local image:

```powershell
node smepost-marketing-workdesk-plugin/scripts/upload-asset.mjs .\prepare-result.json .\campaign-image.png
```

The helper uses Node built-ins only. It checks the 4 MiB limit and PNG, JPEG, or WebP file signature, validates the short-lived SMEPost upload URL and session expiry, performs a non-redirecting `PUT`, and prints only the upload session ID. The helper does not call `complete_asset_upload`; pass the printed ID to that MCP tool and report the design as saved only after that tool succeeds. Delete the temporary prepare-result file after use because it contains a short-lived upload capability.

For an emulator URL, add `--allow-localhost`:

```powershell
node smepost-marketing-workdesk-plugin/scripts/upload-asset.mjs .\prepare-result.json .\campaign-image.png --allow-localhost
```

## Local validation

From the repository root:

```powershell
claude plugin validate smepost-marketing-workdesk-plugin
claude plugin validate .
bun test smepost-marketing-workdesk-plugin/scripts/__tests__/upload-asset.test.mjs
```

`claude plugin validate` checks the Claude manifest, marketplace, and skills. The upload tests use a mock transport and make no network requests. They do not verify OAuth, a deployed Workdesk endpoint, or a real storage upload.

## Private repository and public extraction

Keep the SMEPost application repository private. For an independently installable public plugin, extract only:

- `smepost-marketing-workdesk-plugin/` (portable manifest, MCP config, skills, upload helper, and this README)
- `.agents/plugins/marketplace.json` with only the Workdesk entry, if distributing through a Codex marketplace
- `.claude-plugin/marketplace.json` from the repository root, with its source path pointing to the plugin package
- The plugin package's `.claude-plugin/plugin.json` and `.mcp.json`

Review the extracted marketplace paths before publication. Do not include environment files, OAuth secrets, Firebase credentials, local emulator data, private user data, or uploaded images.
