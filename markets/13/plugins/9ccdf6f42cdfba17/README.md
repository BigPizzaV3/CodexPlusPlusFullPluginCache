# BRF-Rapporten ChatGPT marketplace package

This is a portable Agent Plugins package for the public, read-only BRF-Rapporten association lookup. It contains exactly one remote Streamable HTTP MCP server:

`https://brfrapporten.se/mcp`

It intentionally contains no `.app.json`, no `apps` declaration, no lifecycle hooks, no credentials, and no local server command. The live server advertises its two read-only tools and no-auth security scheme during OpenAI's MCP scan.

## Validate and create the upload archive

From the repository root:

```sh
node scripts/check-chatgpt-package.mjs
mkdir -p dist
(
  cd integrations/chatgpt
  zip -r ../../dist/brf-rapporten-chatgpt-plugin.zip plugin.json mcp.json assets README.md
)
```

Upload `dist/brf-rapporten-chatgpt-plugin.zip` in the OpenAI Plugins dashboard. The ZIP extracts with `plugin.json` and `mcp.json` at its root.

The strict gate requires release notes and a real video-walkthrough URL in `review.demo_recording_url`. It validates local package constraints; it does not prove the referenced URLs are live or that the portal accepts the package. After site publication, also check public materials:

```sh
node scripts/check-chatgpt-package.mjs --live
```

For incomplete authoring only, `--draft` permits an absent video URL and explicitly reports that review requirement. Do not use that mode as a submission gate.

## Remaining submission work

The package is ready to upload, but it is not a completed public submission. Before review, the publisher must:

1. Complete OpenAI individual verification for the directory identity **Adrian Martén** and have the Dashboard permission to create and submit plugins.
2. Upload the ZIP, choose the verified identity, connect `https://brfrapporten.se/mcp`, complete the dashboard's domain-verification challenge, and resolve the MCP tool scan findings.
3. Verify the declared [review walkthrough](https://brfrapporten.se/integrations/chatgpt/review-1.0.0.html) and its WebM, MP4 and caption files are publicly accessible after publication. The 100-second video sequences actual ChatGPT screenshots from all eight cases; it is not a continuous screen recording. It has no audio and includes an English WebVTT case guide on the review page. Test browser playback as well as MIME types, media headers and byte-range responses; HTTP success alone is insufficient.
4. Confirm the dashboard category and country availability, then submit only after the live MCP scan shows the two expected read-only tools.

No reviewer account is needed: the MCP endpoint has no authentication and reads only its bounded public association library.

The [public MCP privacy disclosure](https://brfrapporten.se/privacy#chatgpt) describes the tool inputs, processors, user controls and retention. Search text is not retained in the application cache or logs. The narrow hourly SQL job deletes MCP rate-limit counters once their ten-minute windows have been expired for 24 hours; verify the deployed job and successful execution before final attestation. Lovable publishes condition-based operational/security log retention, without a fixed day count; the policy states that criterion explicitly. Production evidence and its limits are recorded in `docs/security/chatgpt-submission-readiness-2026-10-20.md` in the source repository.

Review evidence was captured in ChatGPT with the visible Medium setting on 19 October 2026. The UI showed activity summaries and answers, not raw per-call arguments. Review cases are reproducible prompts and expected behavior; they do not claim that a model will use identical wording or repeat reads already present in conversation context. Source data may change after this version.
