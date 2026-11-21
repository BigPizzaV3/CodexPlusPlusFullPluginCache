# Connecting OptiSigns

> (https://support.optisigns.com/hc/en-us/articles/56987330525587). Keep the user-facing wording
> host-neutral.

## How it connects

- The plugin's connector is `https://optisigns-mcp.optisigns.com/mcp`.
- The user signs in on the OptiSigns sign-in page (email and password, Google or Microsoft) and approves
  the requested permissions. No API keys.
- Works on any OptiSigns plan, at no extra cost.

## Common problems, and the one-line fix to give

| What happens | Tell the user |
|---|---|
| Calls fail as not signed in | "Connect your OptiSigns account from this plugin's connector settings, then try again." |
| The connector is turned off for the account | "An account owner or super admin needs to turn on **Enable AI connector (MCP)** in OptiSigns → Preferences → General." |
| Work or school workspace, can't add the connector | "Your workspace admin needs to add or allow the OptiSigns connector first." |
| Access denied for an action | "Your OptiSigns role may not allow this; ask an account admin, or sign in with an account that can edit screens and content." |
| Several teams | Ask which team to use; every action happens in one team. |
| Signed in, but no screens | Offer a laptop test screen (Mac or Windows player app), or pair a screen once it shows its pairing code. |
| File uploads fail | "Upload the file in the OptiSigns portal and I'll take it from there." |

Link the Help Center article above for step-by-step setup. Never ask the user for passwords or tokens.
