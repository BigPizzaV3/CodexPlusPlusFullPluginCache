# ISMS Copilot

ISMS Copilot is a governance, risk and compliance (GRC) assistant with access to
the user's ISMS Copilot account, served by the `ismscopilot` MCP server.

## When to use it

Use it when the user wants ISMS Copilot's compliance specialist or their ISMS
Copilot account data for ISO 27001/27701/42001, SOC 2, GDPR, NIS 2, DORA, EU AI
Act, Cyber Resilience Act, NIST SP 800-171/CMMC, HIPAA or PCI DSS work:
interpretation, policy drafting, control mapping, gap analysis, Statement of
Applicability justifications, risk registers and audit preparation.

Keep code, git, local files and shell work local. Do not send them to the
specialist.

## How to use it

- Start one conversation per deliverable with `create_conversation`, then use
  `send_message` for follow-ups on it. Pass `workspace_id` when the user names a
  workspace.
- The specialist already knows the frameworks, so send the user's question as
  written. Do not paste framework text first.
- Mode: `fast` by default, `think` for multi-step work, `beyond` for long
  research-grade drafting (not available on every plan).
- Pass `answer_format` `brief` or `decision` for a compact reply.
- When a call returns status `generating`, call `get_reply` until the reply is
  complete.
- Call `set_company_context` only when the user asks to update their company
  profile.

## Sign-in and data

The server uses OAuth 2.1: the user signs in to their ISMS Copilot account in a
browser. If the tools are not available yet, tell the user to run
`/mcp auth ismscopilot`. Do not ask the user for API keys or passwords, and do not send
health records, payment card data or government ID numbers to the specialist.

Answers are informational and are not legal advice: have a qualified
professional review legal or regulatory interpretations before they are relied
on or shared.
