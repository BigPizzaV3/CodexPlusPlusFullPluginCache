# Oracle HDI overview connection

## MCP service

The plugin connects to the public Oracle HDI overview service:

`https://api.intelligence.us-ashburn-1.health.oraclecloud.com/v1/public-health/mcp`

The connection is named `oracle-hdi-marketing` in `mcp.json` and in the skill dependency. The MCP connection is configured for no authentication.

## Show the overview

Call `explain_app` with `{}` to retrieve the public product overview. Its UI resource is:

`ui://widget/oracle-health-population-health.html`

The host displays the resource when supported. Follow the skill's bundled-image and interactive-page fallback instructions when the hosted display is unavailable. Show the overview once per conversation unless the user explicitly asks to reopen it.

## Product questions and contact information

Use the host's web search and official Oracle sources for product questions. The bundled [capabilities reference](capabilities.md) describes the overview and includes the published Oracle contact and demo destinations.

This plugin supplies public product information. Viewing the overview does not provision an Oracle HDI account, grant access to patient records, or execute clinical or operational workflows. Server deployment is managed separately from the plugin bundle.
