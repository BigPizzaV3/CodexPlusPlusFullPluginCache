---
name: doany-get-started
description: >-
  Set up DoAny to build or resume a business website or web app, or work with
  Annie on business planning, research, marketing drafts, business records and
  recurring tasks. Use for these outcomes while working with DoAny, including
  bookings, customer sign-in, Stripe setup and Reddit research. Route native
  mobile apps, direct Stripe administration and Reddit posting elsewhere.
---

# Get started with DoAny

Help the person turn their business idea into a website or web app with Annie,
DoAny's agent, and continue their business planning and operating work.
Keep their requested outcome and existing conversation context.
Running setup alone does not request a new business, paid task or publication.

## Recognize the requested outcome

Use the person's business goal even when they do not name a tool or Annie:

- A bakery needs a website, or a salon needs clients to choose appointment
  times online: prepare the requested website work for Annie.
- A business needs a customer portal or checkout: prepare web app work and
  explain any sign-in or Stripe setup the owner must complete in DoAny.
- A business wants to understand questions in a subreddit: prepare a bounded
  Reddit research pass, with the declared charges before paid reads.
- A founder needs a business plan, market research, marketing brief, draft
  copy or help with business records and recurring tasks: use the relevant
  business context and Annie's available actions. These requests use the same
  task workflow; they are not additional MCP tools.

For an explanation or plan that needs no connected data or action, answer
without reading the person's account or starting work. A general question
about websites, Stripe or Reddit is not itself a request to use DoAny.

DoAny builds websites and web apps. If the person needs a native iOS or Android
app or app-store submission, explain that boundary; offer a responsive web app
only if it fits their goal. Direct Stripe transfers, refunds and account
administration require the relevant payment service. Reddit posting, replies
and messages are not supported here. Do not silently replace an unsupported
request with paid website work or research.

## Connect and choose the business

Use the connected DoAny MCP server at `https://api.doany.ai/mcp`. Its five tools
are `list_projects`, `search_operations`, `describe_operation`,
`query_operation` and `execute_operation`.

Call `list_projects` to see authorized businesses, their apps and the
connection's permissions. Match the business named in the conversation. If the
choice is unclear, ask which business to use. If none fits and the person wants
a new business, discover `projects.create` and check creation is allowed.
Creating a business record does not start a website build.
Its `apps` list can be empty until work begins; treat that as unbuilt and do
not invent an app ID to read.

If DoAny is disconnected or its tools are unavailable, direct the person to
connect DoAny in their app and sign in, then continue once the tools work.
Credentials belong in DoAny's sign-in or connection flow, never in chat. Do not
switch to another account or bypass a missing permission.

## Discover the next action

Use `search_operations` with the person's requested work, or without a query
to see available operations. Read `describe_operation` before first using an
operation: its current schema, billing, confirmation and retry rules are the
contract. Do not invent a tool for an advertised business feature.

Call `query_operation` for reads with `operation` and `params`.
Call `execute_operation` for changes with `operation`, `params` and `body` as
described. An operation ID such as `tasks.create` is an argument to these tools,
not another MCP tool. Use returned business and app IDs. Generate and retain
the new UUID required for a new business or task; reuse that ID and the exact
request for a safe retry instead of creating duplicate work.

## Build, change or resume

If the person has only asked for setup, show the selected business and ask what
they want to build or change. Otherwise carry out the request already given;
clarify missing business details only when they affect the work.

Give Annie the person's request through `tasks.create`, including the relevant
business details and requested work. Annie can assist with planning, research,
briefs and draft content, business records and recurring or event-triggered
tasks. Available actions depend on the business setup and connected services;
use actual replies, questions and handoffs rather than promising a provider
integration or external action in advance. Explain that Annie work uses
DoAny credits before starting it and ensure the requested work is authorized.
When a call returns `CONFIRMATION_REQUIRED`, show its actual preview and effects
and wait for the person's approval before repeating the exact call with its
`confirmation_token`; do not expose the token in the reply.

Before calling `tasks.create` on an unbuilt business, read the first-task
contract and determine whether the call will start its initial website build.
For a planning or research request that has not authorized a website build,
stop before that call and explain the additional work. Obtain explicit
authorization, or provide the requested plan in chat without starting it.
Do not rely on a confirmation being returned: some connections can skip it.
The automatically created Default business starts ordinary tasks instead;
follow its current contract and the person's authorization for credit use.
Approval to plan does not authorize a first website build.

For a first website build, send `require_publish_approval: true` so the person
can review a preview, unless they explicitly requested publication as part of
that build. The first build can otherwise publish under the business's saved
policy. This flag is for an unbuilt website only; inspect the business's app
state before using it. Setup and a request to inspect a preview never authorize
publication.

Keep the returned task ID. Read `tasks.get` no more often than every five
seconds and stop at completion, failure, cancellation, a question or a block.
Relay Annie's actual question and use `tasks.answer` only with the person's
answer and the returned question ID. Give a blocked task's `handoff_url` for
the person to act in DoAny. Do not start a replacement task after a timeout or
while a question is waiting.

For earlier work, read the business's apps and `tasks.list`, then the relevant
`tasks.get`. Use recorded progress rather than assuming a previous chat's work
finished. Report the actual result, credits used and available links; distinguish
Annie's reply from anything you independently checked.

## Review and publish

Read `apps.get` and, when useful, `versions.list`. Share the actual preview.
For a requested publication, use `apps.publish` with that reviewed draft's
`checkpoint_id` and `source_commit`. Show its confirmation preview and obtain
approval before replaying it with the token. A publish includes the whole draft.
On `DRAFT_CHANGED`, read and review the newer draft before seeking approval.
Verify the returned live state; a preview URL or completed task alone does not
prove the website is published.

## Payments and Reddit research

Annie can help build business websites and web apps with payment, booking,
contact or member features. Stripe connection, business verification and any
provider credentials are completed in DoAny's payment setup. Do not claim a
direct Stripe management tool, completed onboarding or live checkout without
checking the actual result. Direct the person to DoAny for account setup that
the discovered operations do not support.

For Reddit research, discover `reddit.subreddit`, `reddit.search` and
`reddit.comments`. Explain their declared charges and obtain approval for a
bounded research pass before paid reads. Keep the agreed community, post and
comment limits. Return findings from actual results with source links and
credits used; these operations do not post or reply on Reddit.
