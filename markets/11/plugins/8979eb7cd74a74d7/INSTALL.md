# Kikin for ChatGPT Desktop

This package connects ChatGPT Desktop to Kikin's existing MCP service. It contains
no account credentials or company data. Downloading and extracting the ZIP does
not install the plugin.

## Before you start

- Use an up-to-date ChatGPT Desktop app with Work mode or Codex and access to
  local plugins. Your workspace's plugin policy must allow this installation.
- Sign in with your Kikin company owner or member account when connecting.
  Kikin must have enabled MCP access for that user. Contact Kikin if access is
  unavailable; installation does not grant access to a company.

## Install through a personal local marketplace

1. Extract the ZIP. Copy the folder containing `plugin.json`, `mcp.json`,
   `INSTALL.md` and `assets/` to `~/.codex/plugins/kikin`. Here `~` means your home
   folder. Create the parent folders if needed.
2. Add Kikin to `~/.agents/plugins/marketplace.json`. If this file already exists,
   keep its name and other plugins and append the Kikin entry to its `plugins`
   array. If it does not exist, create the folders and file using this example:

   ```json
   {
     "name": "kikin-local",
     "interface": {
       "displayName": "Kikin local"
     },
     "plugins": [
       {
         "name": "kikin",
         "source": {
           "source": "local",
           "path": "./.codex/plugins/kikin"
         },
         "policy": {
           "installation": "AVAILABLE",
           "authentication": "ON_INSTALL"
         },
         "category": "Finance"
       }
     ]
   }
   ```

   The source path is relative to the marketplace root (your home folder), not
   the `.agents/plugins/` folder. Keep the extracted files in this location.
3. Restart ChatGPT Desktop. In Work mode or Codex, open the Plugins Directory,
   choose your personal/local marketplace and install **Kikin**.
4. Connect the MCP server when prompted. Complete the Kikin login in your browser
   with the company account you intend to use, then return to ChatGPT Desktop.
5. Start a new chat, enable Kikin and ask: "Use Kikin to confirm my connected
   company." The existing `whoami` tool identifies the connected user and company.

The supported manual route is described in
[OpenAI's plugin packaging guide](https://developers.openai.com/plugins/build/plugins#install-a-local-plugin-manually).
This download is for local Desktop installation; it is not a public-directory
listing or a double-click ZIP installer.

## Update or troubleshoot

For an update, replace the files in `~/.codex/plugins/kikin` with the new extracted
package, then restart ChatGPT Desktop so the local installation picks up the
change. If Kikin does not appear, check that the marketplace's source path points
to the folder containing `plugin.json` and that local plugins are allowed by your
workspace. If login or company access fails, contact Kikin using your usual
support channel. Never paste access tokens into the package or marketplace file.
