"""MCP tool surface. Run with mcp run mcp_server.py or python mcp_server.py."""
import base64, os
from mcp.server.fastmcp import FastMCP
from generator import generate, inspect_template

mcp = FastMCP('Integration Flow Builder')

@mcp.tool()
def inspect_sap_iflow_template(template_zip_base64: str) -> dict:
    """Inspect a genuine SAP design-time iFlow ZIP before generation."""
    return inspect_template(base64.b64decode(template_zip_base64, validate=True))

@mcp.tool()
def create_sap_iflow_zip(template_zip_base64: str, technical_id: str, display_name: str, description: str = '') -> dict:
    """Generate a template-derived iFlow ZIP. Returns base64 ZIP for a client to save."""
    output, validation = generate(base64.b64decode(template_zip_base64, validate=True), technical_id, display_name, description)
    return {'filename': technical_id+'.zip', 'zip_base64':base64.b64encode(output).decode(), 'validation':validation}

@mcp.tool()
def discover_sap_reference_content(application: str, scenario: str = '') -> dict:
    """Provide official SAP integration discovery entry points and safe import steps.

    This is catalog navigation, not live catalog search or automatic content download.
    """
    if not application.strip():
        raise ValueError('Application or product is required')
    return {
        'application': application.strip()[:120],
        'scenario': scenario.strip()[:240],
        'catalog_url': 'https://api.sap.com/integrations/discoverintegrations',
        'catalog_source': 'SAP Business Accelerator Hub',
        'live_search_performed': False,
        'steps': [
            'Open the official catalog and search by application and scenario.',
            'Review integration package descriptions, documentation and applicable use restrictions.',
            'If permitted, copy the package into the SAP Cloud Integration Design workspace.',
            'Export an editable design-time iFlow ZIP from the tenant and provide it as a template.',
            'Generate a derivative ZIP and confirm import and runtime behavior in a test tenant.'
        ],
        'note': 'Some packages are configure-only or cannot be downloaded. No download or import is attempted.'
    }

if __name__ == '__main__':
    mcp.run()
