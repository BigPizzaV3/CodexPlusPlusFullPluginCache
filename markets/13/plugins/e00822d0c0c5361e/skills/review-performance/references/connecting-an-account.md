# Connecting an ExtensionDash account

The plugin connects to `https://extensiondash.com/mcp` without credentials.
Until the user signs in, only `search_catalog` and `get_listing` work, and
every tracking tool answers that "this connection has no account".

Never ask the user to paste a token, a connection URL, or a password into the
conversation. Signing in happens in their browser, on extensiondash.com. Give
them the steps below to do themselves.

## ChatGPT

ChatGPT offers to connect the account by itself the first time a tracking tool
needs one. The user follows the prompt, signs in or signs up at
extensiondash.com, and clicks **Allow** on the consent screen. If the prompt
does not appear, they can connect the account from the plugin's settings in
ChatGPT.

## Claude (web, desktop, or Cowork)

1. Create an account at https://extensiondash.com/signup if needed.
2. Open the plugin's **Connectors** tab and connect ExtensionDash.
3. Choose **Sign in now** and **Register automatically** if authentication
   settings are shown. Sign in on extensiondash.com and click **Allow**.

Do not promise that a failed tracking call will automatically open sign-in in
Claude. This server uses a tool-level authentication error, which Claude does
not treat as the HTTP 401 needed for lazy authentication.

## Claude Code

For a plugin installation, open `/mcp`, select the plugin's ExtensionDash
server, and authenticate. Plugin server names are namespaced, so use the name
shown there.

For a standalone server named `extensions-dashboard`, run
`claude mcp login extensions-dashboard` in a terminal and follow the browser
sign-in flow.

## Codex (CLI, IDE or desktop app)

1. Create an account at https://extensiondash.com/signup if they have none.
2. Run `codex mcp login extensions-dashboard` in a terminal. A browser opens on
   the ExtensionDash consent screen; sign in and click **Allow**.
3. Start a new Codex session.

`codex mcp list` then shows `extensions-dashboard` with Auth `OAuth`.
`codex mcp logout extensions-dashboard` returns to research only.

Older setups may instead use a connection URL with a personal API token from
https://extensiondash.com/profile. That also works. Anyone holding that URL can
read and change the account's tracking, so if it leaks the user should
regenerate the token on the profile page.

## Disconnecting

Every app connected by signing in is listed under **Connected apps** on
https://extensiondash.com/profile, with a **Disconnect** button.
