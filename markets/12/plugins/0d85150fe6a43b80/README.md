# HorizonX

Search [HorizonX](https://horizonx.so) in plain language and add the result to your project: animated UI components, image textures and WebGL shaders exported as HTML, Svelte or React with no runtime dependencies, plus landing page templates, UI kits and design systems from the HorizonX Library.

This plugin contains:

- **The HorizonX MCP server** at `https://horizonx.so/api/mcp`. You sign in with your HorizonX account (OAuth) the first time your agent uses it. An active HorizonX membership is required.
- **The `horizonx` skill**, which tells the agent how to search, inspect a component's parameters, export it in your project's framework and place the file next to similar components.

## Tools

| Tool | What it does | Changes anything? |
| --- | --- | --- |
| `search_components` | Searches components, textures and shaders | No |
| `get_component` | Shows one component and its parameters | No |
| `export_component` | Returns code for a component | Uses one daily export the first time |
| `search_library` | Searches templates, UI kits and design systems | No |
| `get_library_item` | Shows one Library product | No |
| `download_library_item` | Returns short-lived download links | Uses one download the first time that day |

## Data the plugin sends

The plugin sends only what you ask the agent to look up: your search text, the component or product slug, the chosen framework and any parameter overrides. These go to HorizonX over HTTPS, together with the OAuth token that identifies your account. It does not read or upload your project files. HorizonX logs tool calls to count exports and downloads against your plan. See the [privacy policy](https://horizonx.so/privacy).

## Support

[horizonx.so/support](https://horizonx.so/support) · support@horizonx.so · [Terms](https://horizonx.so/terms)
