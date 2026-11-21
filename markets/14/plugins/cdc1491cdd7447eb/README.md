# Siarix plugin upload package

This package uses OpenAI's supported Codex compatibility format. Its root contains `.codex-plugin/plugin.json`, `.mcp.json` and the referenced logo asset. Upload the ZIP as supplied; do not add an enclosing folder.

## Upload

1. Open https://platform.openai.com/plugins and choose your owning organization/project.
2. For the existing Siarix draft, use Upload new version; for a new draft, use Upload new or existing plugin.
3. Upload siarix-plugin-upload.zip. Metadata should show Website https://siarix.tech and the Siarix logo.
4. Open MCPs and connect the Siarix server with OAuth. Automatic client registration uses the live Supabase discovery configuration; the package contains no client secret.
5. Complete the domain verification challenge shown by the dashboard and sign in to Siarix through its normal consent screen.
6. Before submitting for review, run the included five positive and three negative cases with an authorized reviewer account. Enter reviewer credentials only in the dashboard's secure Review details form, and supply a genuine reviewer-accessible demonstration video there.

The hosted server already runs separately on Azure. Uploading this package does not deploy website code or merge GitHub branches. OpenAI's validation/review and publication remain separate steps.

## Included functionality

The server exposes only siarix_list_mind_twins. It checks the caller's identity, workspace membership and existing paid access. Other control-plane tools, private state access and write operations are outside this connector's scope. No purchases or upgrades are initiated inside the plugin.

## Website field

In this compatibility format, the listing URL is interface.websiteURL inside .codex-plugin/plugin.json. homepage and author.url also point to https://siarix.tech. The four required listing URLs are populated.

For the portable Agent Plugins format, the corresponding listing field is extensions.com.openai.interface.websiteURL. publication.websiteURL is not the listing field.

## Logo

assets/siarix-logo.png is the original gold-and-cyan Siarix website logo, reduced to an opaque 128 x 128 RGB PNG. The file is under 10,000 bytes. The same included asset is used for the primary logo and composer icon.

## Review status

The included cases define expected behavior; this ZIP does not claim those cases have been executed through the OpenAI review portal. The domain-verification token, a demonstration video URL and reviewer sign-in credentials have not been fabricated or embedded. Add them in the dashboard when requested. The publisher identity is selected and verified separately in the dashboard.
