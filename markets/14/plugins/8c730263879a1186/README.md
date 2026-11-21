# viaSocket MCP plugin

Publisher: viaSocket  
Website: https://viasocket.com/  
MCP endpoint: https://connect.viasocket.com/mcp  
Supplied logo URL: https://stuff.thingsofbrand.com/viasocket.com/images/imgf_logo-2.png

This package configures a remote Streamable HTTP MCP connection to the supplied viaSocket endpoint. The viaSocket MCP website describes built-in authentication, but the endpoint's OAuth handshake and exposed tools have not been independently inspected in this environment. Confirm the server's actual OAuth behavior and tool list in a compatible MCP client before public submission.

## Marketplace submission gaps

- The supplied logo could not be downloaded in the build environment, so no copied logo asset is included. Add the actual official square logo file and set `logo` and `composerIcon` to its relative path before submission to a directory that requires packaged icons.
- Support, privacy policy, and terms URLs were not supplied or verified. Add real public URLs before submitting to a marketplace that requires them.
- This is a portable plugin package; creating it does not publish the MCP server or create public marketplace listings.
