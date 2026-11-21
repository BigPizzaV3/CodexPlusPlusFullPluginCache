# Maker

Build, edit, preview, and publish websites from an AI conversation using your Maker account. Browse projects, work with source files, check TypeScript errors, and publish an approved version to a live URL.

## Connect your account

You need a [Maker account](https://ai.maker.co/) and access to the organization containing your projects. Add Maker through your assistant's connector settings, then sign in to Maker and approve the requested permissions.

| Assistant | MCP server URL | Setup and tool documentation |
| --- | --- | --- |
| ChatGPT and Codex | `https://ai.maker.co/mcp` | [Maker documentation](https://ai.maker.co/mcp/readme) |
| Claude | `https://ai.maker.co/mcp/core` | [Maker documentation for Claude](https://ai.maker.co/mcp/core/readme) |

### Use the plugin in Claude Code

Clone this repository, then load the plugin from its folder for the current Claude Code session:

```sh
git clone https://github.com/makerinc/maker-plugin.git
claude --plugin-dir ./maker-plugin
```

In Claude Code, run `/mcp`, select Maker, and follow the OAuth sign-in flow to connect your account.

For each new session, run `claude --plugin-dir ./maker-plugin` again from the directory where you cloned the repository, or pass the plugin folder's absolute path. The plugin includes workflows for finding your connected organization and project, and publishing an approved website.

## Try it

- “Show my Maker projects.”
- “Check my landing page for TypeScript errors and show me its preview.”
- “Prepare my website for publication and ask me before publishing.”
- “Give me the embed code for my published website.”

## Permissions and data

Maker uses your connected organization's permissions. Editing and publication require the applicable access and account entitlements. Publication requires your explicit approval of the version being published.

You choose and connect your client, and it requests data from your Maker account. Requested tool inputs are sent to Maker. Depending on the tools used, responses can include account and organization details, plan and billing status, team size, project source and screenshots, comments and version history labels, integration names and status, publication results, and diagnostic data such as preview console logs and TypeScript results. Credentials stored for connected integrations are not returned. Preview screenshots are returned inline without creating public storage URLs. See Maker's [privacy policy](https://www.maker.co/privacy-policy) and [terms of service](https://www.maker.co/terms) for data handling and service terms.

## Support

Email [support@maker.co](mailto:support@maker.co) or see the [Maker documentation](https://ai.maker.co/mcp/readme).

## License

This plugin package is available under the [MIT license](LICENSE). Maker's hosted service is governed by its [terms of service](https://www.maker.co/terms).
