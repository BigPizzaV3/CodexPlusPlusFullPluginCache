# Plan limits

What an account can do depends on its plan: how many projects it can have, how
many websites and addresses a project can use, whether people can leave voice
messages and how many new submissions a 30-day period includes.
`get_next_steps` reports this account's current plan and its limits
(`facts.projects[].plan`); when a limit blocks something, say which limit
applies.

Agents cannot buy, start or change a plan, and do not suggest one. The owner
manages the plan in the Voicedot dashboard. Plan details are on the pricing
page.

Every plan includes MCP for coding agents, address modes (see `address_modes`)
and an unlimited number of external reviewers, who need no account.

## Addresses

Every address is an exact HTTPS origin with its port; plain HTTP is refused,
also for local development, which needs a certificate.

- On a plan with the one-website rule, all public addresses of a project
  belong to one website (one registrable domain and its subdomains) and at most
  3 addresses count. Addresses that work only on the visitor's own computer
  never count.
- Other plans allow several websites per project, up to 50 addresses per
  project.
- An address a coding agent added on the visitor's own computer is confirmed
  at once. Any other address a coding agent added waits for a first message
  from that address and stops collecting after 7 days without one, unless a
  person confirms it in the dashboard.

## When submissions wait

On a plan with a 30-day allowance, new submissions beyond it wait in a queue
of up to 100 whose content stays hidden in the dashboard, notifications and
MCP until the allowance renews; further comments are refused. Replies,
discussions and MCP reads do not count.

## Teammates

In a workspace with teammates, every active member has access to all its
projects. Only the owner invites teammates and decides who may create
additional projects; this permission does not restrict work on existing
projects or their addresses. A coding-agent connection may still be limited
to selected projects and specific actions.

## Plan changes

A cancellation or plan change takes effect at the end of the paid period.
Projects beyond the new plan's limits become unavailable to agents; nothing is
deleted. Addresses a project already has keep working, but adding an address
beyond the plan's address rules is refused.
