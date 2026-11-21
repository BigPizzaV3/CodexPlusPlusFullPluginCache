# Oracle Analytics template package

Version 1.0.1. Package name: `oracle-analytics`. Publisher: Oracle Analytics.

This package follows the Beta Partner Package Submission Guide for Templated Plugins supplied on October 17, 2026. It contains one remote templated MCP server, four shared skills, listing assets, and review materials. It does not deploy the Oracle Analytics service.

## Endpoint configuration

Supported customer endpoint pattern:

`https://{instance}.analytics.ocp.oraclecloud.com/api/mcp`

The `instance` value is the deployment-specific hostname label. The existing example value is `stdemoinstsjc-idsrwtwtdcht-95-sj`, producing:

`https://stdemoinstsjc-idsrwtwtdcht-95-sj.analytics.ocp.oraclecloud.com/api/mcp`

The guide defines `url` as illustrative. It is not a review endpoint and does not require example-instance credentials. A workspace administrator supplies the actual endpoint when configuring an instance. Endpoint authentication discovery happens at that point.

The server uses Streamable HTTP. The only authentication default is `auth.type: oauth`. Client registration mode, client identifiers, OAuth endpoints and scopes are omitted so the template does not impose unconfirmed deployment-specific defaults. No secrets are packaged. According to the guide, editable configuration uses administrator settings first, then defaults discovered from the actual endpoint, then template defaults; the final settings must match endpoint capabilities.

## Shared skills

The four skills cover content discovery, analytical questions, catalog management and catalog permission changes. Each uses the selected instance's connection and current tool output. Catalog mutations and access changes retain their approval requirements. Query results retain the guard against inferred units.

The guide describes inheritance from published template releases. Availability of instance creation, discovery and inherited updates must be confirmed by the OpenAI beta contact for the destination workspace.

## Submission and review materials

Send this ZIP through the beta submission channel supplied by the OpenAI contact. Ask that contact how to associate this package with the existing Oracle Analytics registration. The package does not contain a private app binding or a migration instruction.

Five positive and three negative cases remain in the manifest. Their setup now refers to a configured test instance; illustrative dataset/workbook names must be replaced with existing test fixtures where needed. All cases for this template version are Not run. The historical demonstration link is retained as supporting material, not proof that this template version has passed instance setup or testing.

No ordinary MCP server is declared alongside the template. The ZIP contains no `.app.json`, lifecycle hooks, customer credentials, or local test evidence.
