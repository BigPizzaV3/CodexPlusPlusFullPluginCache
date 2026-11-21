# Claude Connectors Directory listing

Use this copy in the Claude.ai remote MCP submission portal.

## Connection

- Server URL: `https://moodlenstodo.com/api/mcp`
- Transport: Streamable HTTP
- URL model: Every user connects to the same URL
- Authentication: OAuth with Dynamic Client Registration (`oauth_dcr`)
- Authentication timing: Tools can be listed before sign-in; protected tool
  calls start OAuth when required
- Documentation: `https://moodlenstodo.com/mcp.html`

## Public listing

- Server name: MoodLens To-Do
- Proposed tagline: Manage tasks, docs, boards, sprints, and meetings.
- Proposed primary category: Productivity
- Proposed permanent slug: `moodlens-todo`
- Company: Moodlens Technology
- Company website: `https://moodlenstodo.com`
- Privacy policy: `https://moodlenstodo.com/privacy-policy`
- Support URL: `https://moodlenstodo.com/help-center`
- Support email: `support@moodlens-ai.com`
- Icon: `https://moodlenstodo.com/pwa-512x512.png`
- Reads data: Yes
- Writes data: Yes
- Allowed link URIs: None. This release does not expose `ui/open-link`.

Confirm the category and permanent slug in the portal before submission.

## Description

MoodLens To-Do connects Claude to an authorized project workspace. Users can
review and search tasks, documents, boards, columns, sprints, meetings,
comments, subtasks, form responses, and time-tracking information. With the
appropriate write scopes, they can create and update work items, manage
document blocks and database rows, add comments and subtasks, work with boards
and columns, and start or stop task timers.

Access is limited to the workspace selected during MoodLens OAuth consent and
the scopes granted for the requested tools. Read and write operations are
separate purpose-built tools, and tools that modify or delete data are marked
with destructive annotations so Claude can request confirmation.

## Primary use cases

1. Review open tasks, priorities, due dates, and blockers.
2. Summarize an active sprint using current workspace records.
3. Find and read project documents or structured document blocks.
4. Create a confirmed task, comment, subtask, meeting, sprint, or board.
5. Update a selected task or document after the user identifies the target.

## User prerequisites

- A MoodLens account.
- Owner or admin access to the workspace being connected.
- A plan and account state that allow MoodLens API access.
- Consent to the scopes requested by the Claude tool being used.

## Data handling notes

- The MCP server calls MoodLens's own first-party backend.
- The connector receives tool arguments and returns authorized MoodLens
  workspace records; it does not request Claude memory or unrelated chat
  history.
- This release has no payment-transfer tools and no AI image, video, or audio
  generation tools.
- Do not answer portal questions about regulated health data, sponsored
  content, country availability, or legal attestations until the responsible
  business or legal owner confirms them.

## Reviewer access

Provide a fully populated test account only through Claude's secure submission
fields. Include the login method, every required step, the reviewer workspace
name, and any plan prerequisite. Never put reviewer credentials in this
repository.

