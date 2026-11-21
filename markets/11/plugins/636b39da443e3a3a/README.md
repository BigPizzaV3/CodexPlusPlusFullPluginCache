# PAM — Property AI Manager

Run your UK rental portfolio from a conversation. PAM is the property operating system for UK landlords from Let Safe Limited; this plugin connects Claude or ChatGPT to your PAM account.

## Install

- **Claude** (web, desktop, mobile, Cowork): find PAM in the plugin directory, or add this repository as a marketplace under Customize → Plugins → Add → Add marketplace and install **pam-property-ai-manager**.
- **Claude Code**: `claude plugin marketplace add callum-coder/PAM-Plugin` then `claude plugin install pam-property-ai-manager@pam`.
- **ChatGPT**: find PAM in the plugin directory. The same folder is submitted there as a plugin with the MCP server at `https://app.propertyaimanager.com/mcp`.

Full setup guide for every client, including read-only connections: https://www.propertyaimanager.com/connect-ai

## Use it

Connect PAM from the plugin's Connectors tab (you sign in to PAM and approve the connection once). Then ask things like:

- "Which of my certificates expire in the next 90 days?"
- "Has the rent come in for Nelson Street this month?"
- "The boiler at 12 High Street is leaking — get PAM to find a plumber."
- "I paid £180 for the gutter repair, book it as an expense."
- "I've got a new tenant for the flat: Sarah Khan, 07700 900123, starting 1 December at £1,250 a month."

Three skills teach the assistant PAM's workflows: reading your portfolio, logging repairs and expenses, and onboarding a tenant. Anything that contacts people or spends money asks you before it happens.

## Data

The connector sends your questions and the details you give (property references, amounts, dates, applicant names and mobiles) to your own PAM account at app.propertyaimanager.com, and returns what PAM holds about your properties. Nothing is stored by the plugin itself. You can disconnect at any time from PAM → Settings → Integrations → Claude & ChatGPT. Privacy policy: https://www.propertyaimanager.com/privacy
