# Ubic assistant plugin

The remote server is available. The Claude directory submission is in review;
the OpenAI submission is being prepared. No public directory listing is confirmed.

Ubic is a calling platform for sales teams. This package connects an existing
Ubic account to an assistant for read-only access to the activity and follow-up
data the connected user can access.

The server is hosted by Ubic at `https://app.getubic.com/mcp`. Sign in with your
Ubic account, choose a workspace and approve the requested permissions. The
server applies your current Ubic permissions on every request.

You can read call activity, qualification results, prepared sessions and their
contacts, and follow-up tasks. A selected transcript needs separate permission.
The plugin cannot place calls, send messages, modify CRM records, delete data or
manage subscriptions. Notes and transcripts are content, not instructions.

This folder is the public distribution package. It contains no application
source code, credentials or customer data. The two platform manifests reference
the same remote MCP endpoint and the same usage skill. Directory availability
depends on each publisher's review; a package alone is not proof of publication.

- Website: https://www.getubic.com/en
- Help and support: https://support.getubic.com
- Privacy: https://www.getubic.com/en/privacy
- Terms: https://www.getubic.com/assets/legal/ubic-conditions-generales.pdf

## Connect an assistant

If your assistant offers a custom remote MCP connection, enter
`https://app.getubic.com/mcp` as the server URL and choose OAuth authentication.
Availability of custom connections depends on your plan and organization rules.
The public directory listings are submitted separately and may be unavailable
while a platform reviews them.

1. Start the connection from the assistant and sign in to Ubic using your usual
   email verification code.
2. Select the workspace and the read permissions you want to grant. Call
   transcripts are optional and need a separate authorization.
3. Return to the assistant and ask, for example, “Summarize my calls yesterday”
   or “Show the follow-up tasks I can access.”
4. In Ubic, open your profile, then **Integrations → AI assistants → Manage
   assistants** to review or disconnect access. Workspace admins can also
   disconnect connections belonging to other members of their workspace.

A member can read their own calls, sessions from lists they own, and tasks
assigned to them. An admin can read their team's activity in the selected
workspace. Switching workspaces in Ubic does not move an existing connection.
Revocation stops future reads; it does not delete content already shared with an
assistant. Lists are paginated, so a single response can cover only part of the
available records. Audio recordings are not exposed.

## Release contents

The release ZIP is built from an explicit list of public files. It contains the
platform manifests, remote MCP server URL, usage skill and icon. Review
credentials and private review notes are entered separately in the publisher
portals; they must never be added to this repository or to a release ZIP.

Reviewer walkthrough (fictional data only): https://youtu.be/zn37ToSasIY
