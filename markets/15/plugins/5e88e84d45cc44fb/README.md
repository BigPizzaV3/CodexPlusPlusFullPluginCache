# DeltaFluency ChatGPT plugin

This directory is the portable package submitted through the ChatGPT plugin dashboard. It reuses the production streamable HTTP MCP endpoint and has a dedicated OAuth client so Claude and ChatGPT can be revoked independently.

## Before submission

1. Deploy the MCP and Identity changes.
2. Read `chatgptClientSecret` from the `falcon-oauth` Kubernetes secret and enter it as the provided OAuth client secret in the dashboard. Never add it to this package.
3. When the dashboard provides its domain-verification token, set the protected GitLab CI variable `OPENAI_APPS_CHALLENGE_TOKEN` and deploy MCP. Verify that `https://mcp.deltafluency.com/.well-known/openai-apps-challenge` returns the exact token as plain text.
4. Create a short reviewer walkthrough, upload it to an unlisted HTTPS URL, and add that URL in the dashboard review form.
5. Supply the dedicated reviewer account from `falcon-mcp-test-users` in the dashboard. Do not put its password in this package.
6. Confirm the category against the current category names offered by the dashboard.

## Build the upload

From this directory, create a ZIP whose root contains `plugin.json`, `mcp.json`, `README.md`, and `assets/`. Do not wrap these files in an extra parent directory.

```powershell
Compress-Archive -Path plugin.json,mcp.json,README.md,assets -DestinationPath ..\deltafluency-chatgpt-plugin.zip -Force
```

The plugin is intentionally read-only. It does not place orders, transfer assets, hold funds, or access exchange accounts.

The OAuth secret can be retrieved on the deployment host with:

```bash
kubectl -n falcon get secret falcon-oauth -o jsonpath='{.data.chatgptClientSecret}' | base64 -d
```
