# KamuiDash

Manage your apps on KamuiDash from ChatGPT or Codex. This update adds two workflow skills to the existing KamuiDash MCP connection.

## Included skills

- `kamui-deploy-workflows`: inspect available repository evidence, recommend commands for Go, Node.js, Python, Ruby or static sites, publish or update authorized apps, guide custom-domain DNS setup, and verify the requested result.
- `kamui-troubleshooting`: match failures to deployment and application logs, explain established facts and unknown causes, and propose supported repairs.

## Access and authorization

Connect your KamuiDash account through the existing OAuth connection. GitHub deployments also require the KamuiDash GitHub App to access your selected repository. Repository inspection uses separately available authorized source readers; the KamuiDash MCP server does not read repository files.

Changes require the host/server approvals and the user's authorized scope. The workflow explains public exposure, applicable cost, and service or data impact. Enter secrets in secure KamuiDash dashboard settings, never in chat or tool arguments.

When requested and authorized, host-provided GitHub tools may inspect source or prepare and push deployment files to the selected repository. HTTP requests may check the app URL or the user's custom domain. Those capabilities depend on the host and the user's existing permissions. DNS records are entered in the user's DNS provider management screen; the KamuiDash MCP server does not edit external DNS.

## Try asking

- "Publish this repository on KamuiDash. Recommend the commands from its source."
- "The new deployment failed, but the old version still responds. Check the logs."
- "Connect this app to my domain and tell me which DNS records to add and how to check them."

## Links

- [Dashboard](https://dashboard.kamui-platform.com/)
- [Documentation](https://docs.kamui-platform.com/mcp.html)
- [Privacy policy](https://dashboard.kamui-platform.com/en/documents/privacy-policy)
- [Terms of service](https://dashboard.kamui-platform.com/en/documents/terms-of-use)
- [Support](https://dashboard.kamui-platform.com/en/inquiry)

## License

MIT; see `LICENSE`.
