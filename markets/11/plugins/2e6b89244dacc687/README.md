# Channlworks plugin

Version 1.1.0 connects to the existing production MCP server at https://mcp.channlworks.com/v2/mcp using Streamable HTTP and OAuth. It includes workflow guidance for supported Channlworks records and operations.

Install the plugin, connect the Channlworks server, and complete Channlworks OAuth sign-in. The organization needs MCP Access and the signed-in role must permit the requested operations. Start with a read such as checking the active organization or summarizing campaigns.

The package contains no credentials, copied tool schemas, or fixed OAuth registration endpoints. Tools and authentication are discovered from the deployed server. Source review and public authentication metadata checks do not establish that authenticated calls work; verify those after connecting.
