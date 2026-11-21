# TalkToData Email submission source

This directory is a separate public-upload package. The existing personal TalkToData Email plugin is used for rehearsal against the same production MCP endpoint, with a private ChatGPT app binding kept out of this public package.

The MCP server is deployed at `https://talktodata.navines.com/mcp/email`. Add the actual reviewer-accessible walkthrough URL to `plugin.json` after recording. Reviewer account credentials belong only in the secure Developer Portal fields, never in this package. The dedicated reviewer account returns labeled synthetic messages and simulated send/manage results; customer accounts use their authorized mailbox.

The package supports mail through IMAP and SMTP. Contacts and calendars require separate provider integrations and are not included. Gmail, Google Workspace, Outlook and Microsoft 365 are not supported by this connection.
