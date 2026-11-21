# Integration Flow Builder | Agentic Integration Hub

Developer: Rameshkumar Varanganti  
Website: https://agenticintegrationhub.com/

## Purpose
First-phase, template-derived generator for SAP Cloud Integration design-time iFlow ZIPs. Does not connect to an SAP tenant or Git provider. The ZIP must be validated by importing into the target SAP tenant. This is a **working scaffold**, not a complete guided iFlow designer or a guarantee of importability.

## Important limitations
- **Requires a genuine, design-time SAP iFlow ZIP exported from SAP Cloud Integration.** No seed ZIP is included because a manufactured one may not import.
- Preserves the template's sender/receiver adapters, connections, BPMN and SAP metadata. It does not construct arbitrary flows from scratch yet.
- Renames some XML attributes and manifest fields, but certain SAP tenant/template-specific references can remain. Validate manually after import.
- Groovy resources can be added but are **not** attached to BPMN Script steps automatically.
- Template ZIP and generated archives are held transiently in memory by the API for at most 15 minutes. In-memory storage is not suitable for multi-instance deployments.
- Use approved templates without secrets and strip credentials, hostnames and sensitive data before sharing.
- No SAP credentials are required to use the generator.

## Setup
Use Python 3.11 or newer:

```bash
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
uvicorn server:app --reload --port 8000
```

Open `http://localhost:8000/docs` for Swagger UI. POST to `/generate` with a JSON body containing `template_zip_base64`, `technical_id`, `display_name`, optional `description` and optional `scripts`. The response contains a temporary `download_path`, which you open to download the ZIP. Base64 encode a template with:

```powershell
[Convert]::ToBase64String([IO.File]::ReadAllBytes('C:\\path\\to\\sap-export.zip')) | Set-Content template.b64
```

## MCP local tool

```bash
python mcp_server.py
```

This starts the MCP server in stdio mode for compatible local MCP clients. For a global ChatGPT plugin, deploy an HTTPS MCP transport and return an authenticated, expiring download URL rather than placing base64 ZIP content into chat context. Add quotas, concurrency control, upload size limits and access controls before public hosting.

## Next steps
1. Export a basic working iFlow with Timer, Content Modifier and End event from SAP Cloud Integration.
2. Export separate adapter-specific seed templates (HTTP, SOAP, SFTP, OData, SuccessFactors and others), including exception and local integration processes.
3. Map requested design JSON onto **verified** BPMN IDs, references, sequence flows, diagram coordinates and SAP adapter extensions.
4. Add ZIP round-trip tests and SAP tenant import/deploy tests.
5. Add public HTTPS MCP tool `generate_iflow` plus download URL.
6. Later add GitHub API via OAuth and commit only with explicit approval.

## SAP Business Accelerator Hub reference-content discovery

Official SAP catalog: https://api.sap.com/integrations/discoverintegrations

The MCP tool `discover_sap_reference_content(application, scenario)` supplies the official catalog entry point and a supported manual workflow. **It does not search SAP live, scrape the catalog, download restricted SAP content, or claim an integration package is present.** Users select an appropriate SAP-delivered package and, where authorized and possible, copy it into their tenant's Design workspace and export an editable design-time iFlow ZIP.

SAP documents the Cloud Integration design-time resource `IntegrationDesigntimeArtifacts` for managing iFlows and `IntegrationPackages` for packages. API access requires the proper tenant credentials and roles. Reference packages may be configure-only, and modifying copied standard content affects future update behavior.

For a future live-discovery feature, implement an authorized SAP catalog interface only after confirming a documented and accessible endpoint; keep the public catalog search separate from authenticated tenant artifact download.

References:
- https://help.sap.com/docs/integration-suite/sap-integration-suite/integration-flow-example-requests
- https://help.sap.com/docs/integration-suite/isuite-integrations-and-apis/integration-package-example-requests
- https://help.sap.com/docs/r/84b35b9c39b247e3ba2a31f02beee46d/Cloud/en-US/58f1d904868f417fb2ff3860b31c59d2.html
