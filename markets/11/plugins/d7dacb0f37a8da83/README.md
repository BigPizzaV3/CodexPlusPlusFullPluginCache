# VerifyEmail for ChatGPT

The contents of the plugin ZIP for the ChatGPT App Directory (OpenAI calls these "plugins"): an Agent Plugins `plugin.json` manifest, an `mcp.json` pointing at the hosted MCP server, one onboarding skill and the listing assets. Nothing here runs or builds. The MCP server itself lives in `verfiymail-backend` at `/mcp` (`https://api.tryverifyemail.com/mcp`) and exposes three tools: `verify_email`, `get_verification`, `get_account`. The names and the URL in this folder must match it exactly.

This folder is not a pnpm workspace package: no `package.json`, no `node_modules`, nothing in `pnpm-workspace.yaml`.

## Layout

```
plugin.json                   Agent Plugins manifest + extensions.com.openai (listing, review cases, publication)
mcp.json                      the single streamable-http server
skills/get-started/SKILL.md   onboarding skill the model reads (tool order, verdict vocabulary, scope)
assets/                       logo, logo-dark, composer-icon, composer-icon-dark, screenshot-1
```

Only one MCP server can be connected per plugin, and a plugin first uploaded as skills-only cannot have an MCP server added later. Always upload with `mcp.json` present from the first submission.

`plugin.json` and `SKILL.md` must not mention pricing, plan comparisons, trials, discounts or promotions; OpenAI's listing rules forbid them and review fails on it. The one allowed mention of credits in `SKILL.md` is the sentence stating that each verification costs 1 credit from the user's existing balance, and the one in `plugin.json` is the `defaultPrompt` asking for the balance.

## Validate

```sh
cd integrations/chatgpt
curl -sO https://agent-plugins.org/schemas/1.0.0/plugin.schema.json
curl -sO https://agent-plugins.org/schemas/1.0.0/mcp.schema.json
npx --yes ajv-cli@5 validate -s plugin.schema.json -d plugin.json --spec=draft2020 --strict=false
npx --yes ajv-cli@5 validate -s mcp.schema.json -d mcp.json --spec=draft2020 --strict=false
rm plugin.schema.json mcp.schema.json
```

Both schemas are self-contained draft 2020-12 documents (no external `$ref`). The plugin schema only checks the root fields and leaves `extensions.com.openai` unconstrained; the dashboard validates that part on upload. Never commit the downloaded schema files.

Quick checks worth running before a ZIP:

```sh
grep -iE 'price|pricing|credit|free|trial|discount|promo' plugin.json   # only the defaultPrompt line
grep -ic 'credit' skills/get-started/SKILL.md                            # exactly 1
file assets/*.png                                                        # four square icons, same size
```

## Assets

- The four icons are byte-for-byte copies of `landing-page/public/apple-touch-icon.png` (180x180 RGBA). Derive icons only from that file or from `landing-page/public/favicon-96.png` (96x96). Never derive from `landing-page/public/logo.png`: it is 505x512, not square, and Google has already rejected non-square icons scaled from it. Do not stretch or pad a non-square source. OpenAI needs square icons of at least 48x48.
- The dark variants are identical to the light ones; the mark is a blue tile that reads fine on a dark surface. If they are ever altered, keep them square, the same size as the light ones, and PNG.
- `assets/screenshot-1.png` is a placeholder (1280x720, charcoal `#0e1117` with the logo centred, made with ImageMagick). The owner replaces it with a real ChatGPT screenshot of the app before submission. Any PNG at least 640px wide works.

## Publish

1. Complete individual or business developer verification in the OpenAI platform organisation settings. Nothing can be submitted until the identity is verified.
2. Have a ChatGPT Plus or Pro subscription on the account that will test the app; Developer Mode requires it.
3. Prepare the reviewer account on VerifyEmail: email+password sign-in, email already verified, credits loaded, no MFA. Paste the credentials into the OpenAI dashboard's reviewer-credentials field ONLY. They are never written into the ZIP, `plugin.json`, `SKILL.md`, this README or git.
4. Zip the directory contents so `plugin.json` and `mcp.json` sit at the ZIP root: run `zip -r ../verifyemail-chatgpt.zip .` from inside `integrations/chatgpt/`, not from its parent. Upload under Plugins → "Upload new or existing plugin" and choose the verified developer identity.
5. Connect the MCP server URL (`https://api.tryverifyemail.com/mcp`) and complete the domain challenge: the dashboard issues a token; set it as the backend Worker var `OPENAI_APPS_CHALLENGE_TOKEN` and redeploy, after which `https://api.tryverifyemail.com/.well-known/openai-apps-challenge` returns the bare token (plain text, nothing else). Verify with `curl -s https://api.tryverifyemail.com/.well-known/openai-apps-challenge` before clicking Verify in the dashboard.
6. Run Scan Tools in the dashboard and fix anything it flags (tool descriptions, missing annotations) in the server task, then rescan.
7. Run all 8 test cases from `plugin.json` (5 positive, 3 negative) in Developer Mode on ChatGPT web AND the mobile app; record the outcomes.
8. Record the demo video showing the connect flow and at least one verification, host it somewhere the reviewer can reach, and set `review.demo_recording_url` in `plugin.json`; re-zip and re-upload.
9. Submit for review and complete the policy attestations.
10. Publish when approved.

Re-submissions follow the same path from step 4; bump `version` and update `publication.release_notes` first.
