# AI ROI Calculator plugin

Built directly into spicyadvisory's Cloudflare Pages application.

- Endpoint after deployment: `POST /api/roi-mcp`
- Shared website and plugin engine: `www/ai-roi-model.mjs`
- Tools: `calculate_ai_roi`, `get_roi_methodology`
- Authentication: none. Stateless aggregate calculations; no private data retrieval or external calls.
- Publisher requested by Toni: Toni Dos Santos - We Call Shotgun.
- Requested availability: worldwide. UK/GBP assumptions remain explicit.
- No additional runtime dependencies, model API key or hosting account.

The website keeps its existing UI, numbers and calculation function. The plugin adds structured comparison output with gross value, costs, net value, net ROI and benefit-to-cost ratio. The web page and MCP endpoint import the same model, so a coefficient change reaches both.

## Checks

```sh
node --test tests/roi-mcp.test.mjs
npm run verify
```

The fixture preserves the website model before extraction at commit cf31d08597ab4b71265a9fe4300265baa005c9aa. Tests compare its values against the shared engine, validate boundary cases and exercise MCP requests and Pages middleware routing.

## Build an installable archive

Push this branch and use the Cloudflare Pages preview produced by the repository's existing integration. After the production change is deployed, run:

```sh
node scripts/package-roi-plugin.mjs --endpoint https://wecallshotgun.com/api/roi-mcp --out /absolute/path/wcs-ai-roi-calculator.zip
```

For a development connection, use the exact verified Pages preview endpoint instead. The packager checks initialization, discovery and a live calculation before writing the archive. It never labels a guessed endpoint as live. A preview package is for testing, not the production directory submission.

## Public review preparation

The manifest includes worldwide targeting, the intended publisher, both original WCS icons, example prompts, release notes and five positive / three negative review cases. All conversational cases remain unrun until exercised through the installed plugin; backend tests alone don't prove tool selection.

Before public submission:

- Verify the publishing identity in OpenAI's portal matches the intended owner.
- Update the published privacy notice to cover this endpoint's processing of aggregate team/cost inputs. Application code doesn't save them or log request bodies. Cloudflare's infrastructure processing and retention still need accurate disclosure.
- Supply published terms that apply to this plugin.
- Confirm the no-payments/no-purchases declaration for review.
- Record and host a real ChatGPT demo, then add its URL to the review metadata.

The existing website and support URLs are included. Privacy, terms and recording URLs are omitted until they are verified. This package isn't yet ready for public submission. Installation for private testing is a separate step.

## Demo script

After installation, start a screen recording in ChatGPT with sample data. Run the first positive prompt from plugin.json. Show both costs and net values. Change both costs to zero and show that ROI is undefined. Ask for the calculation method, then ask for exact French payroll costs to demonstrate the scope boundary. Stop recording, check readability and ensure no credentials or unrelated private content are visible. Host the real recording at a reviewer-accessible URL. This script isn't itself a demo recording.

## Current private release

Version 1.0.3 uses the display name AI ROI Calculator and the original logo supplied by Toni on 6 October 2026. The same logo is used on both themes. The existing package identity remains wcs-ai-roi-calculator. Its production endpoint is https://wecallshotgun.com/api/roi-mcp.

Private plugin: https://chatgpt.com/plugins/plugins_6ac48faa3d788191b70c55ef381b1e94

Public review has not been submitted. The approved terms and plugin privacy addition are included in this release. A real recorded demo and the final portal checks remain pending.
