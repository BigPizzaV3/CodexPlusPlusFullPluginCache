# Mason

Mason helps property managers investigate and manage maintenance, coordinate
people and appointments, maintain policies, and understand their portfolio.
This plugin pairs ten workflow skills with the remote Mason MCP connector. It
requires an existing authorized Mason account and access to the property manager
you select during OAuth consent.

## What you can ask

| Workflow                 | Example request                                                              | Bundled skill              |
| ------------------------ | ---------------------------------------------------------------------------- | -------------------------- |
| Investigation            | “Why is the sink repair still open? Show the evidence.”                      | `mason-maintenance-triage` |
| Work orders and projects | “Open work orders for these punch-list items and group them in a project.”   | `mason-work-orders`        |
| Dispatch and estimates   | “Request an estimate from the vendor I named for this repair.”               | `mason-dispatch`           |
| Appointments             | “Move this technician's visit to the agreed window on Friday.”               | `mason-scheduling`         |
| Inspections              | “Check the inspection's access notes and explain what is still unconfirmed.” | `mason-inspections`        |
| Vendors and technicians  | “Find our emergency plumbing vendors and show their saved restrictions.”     | `mason-vendors`            |
| Policies and guidelines  | “Update our future troubleshooting guidance with this correction.”           | `mason-policies`           |
| Communications           | “Draft a resident update about that appointment. Don't send it.”             | `mason-communications`     |
| Portfolio summary        | “Summarize my open maintenance work and decisions needed.”                   | `mason-maintenance-digest` |
| Recurring reports        | “Preview a weekly backlog report. Don't schedule delivery yet.”              | `mason-reports`            |

The bundle supplies discoverable workflows. Detailed PM and shared skills remain
served by Mason through `get_mason_briefing`, `list_skills`, and `read_skill`,
along with current account policies and tool schemas. The plugin retrieves those
references when needed instead of shipping a copy of the internal skill library
or customer configuration. The workflows do not grant access or independently
authorize actions. Availability depends on your account and connection scopes.

## Connect your account

Install the plugin in a supported host, then connect Mason using its OAuth flow.
In Claude, open the plugin's Connectors tab and connect Mason. In ChatGPT, follow
the plugin's connection prompt. Confirm the selected property manager and scopes.
The remote endpoint is <https://mason.enduring-labs.com/api/mcp>.

- `mason.read` retrieves records and workflow references within your connection.
- `mason.write`, when additionally consented, permits the changes and workflows
  available to your account. Successful writes execute immediately under your
  host's tool permissions. Some workflows notify people, send messages, or call.

Ask “Which Mason user and property manager am I connected as?” to check the
connection. A read-only connection cannot write even when a prompt approves an
action. To change scopes, reconnect and give fresh OAuth consent. Revoke access
in Mason → Settings → Connected apps. Revocation does not delete business records
or existing audit history.

## Behavior and data handling

The plugin contains text skills, manifests, and a logo. It installs no executable,
local MCP process, hook, background job, or permission override. Its MCP server
configuration connects only to Mason's fixed HTTPS endpoint. It does not request
local files, environment credentials, or the host's entire conversation history.

Requested tool calls send their arguments to Mason and return account-scoped
business data, which may include contact information and communications. Mason
may consult the property manager's configured integrations to fulfill an action.
Authorized workflow and communication tools may notify people through those
integrations. A draft remains a draft unless you request further action. A queued
message is not proof of delivery. Stop Mason and the server's other safeguards
remain enforced; a blocked communication is not permission to switch channels.

The host processes information under its own terms and plan; installing this
plugin does not place a personal AI account under Mason's provider agreements.
See the [connector privacy notice](https://mason.enduring-labs.com/docs/mcp/privacy)
and [terms](https://www.thisismason.com/legal/terms).

## License

This plugin is proprietary and distributed under the [Mason Plugin Limited Use
License](LICENSE). You may install and use it with an authorized Mason account,
including for business use and internal deployment to authorized users.
The license restricts redistribution, modification, and reuse of its skill
instructions in other products, including competing services. It permits
authorized platform distribution and preserves rights granted under applicable
platform terms and law. Public source visibility does not grant general reuse
rights. The included name and logo identify Mason; they do not authorize
rebranding or endorsement. See LICENSE for the complete terms.

## Support

See the [connection guide](https://mason.enduring-labs.com/docs/mcp) or contact
[hello@thisismason.com](mailto:hello@thisismason.com). For an unexpected result,
include the work-order link and approximate time, without passwords or tokens.
If an action's result is uncertain, inspect Mason before repeating it.
