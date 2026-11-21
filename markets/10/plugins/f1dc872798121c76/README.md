# Ample Computer

Describe an app or share your code, and build and host it with Ample Computer
from Codex, ChatGPT or Claude. Get a live HTTPS URL for an app with a backend,
a database, transactional email or uploaded images, without configuring
servers or a cloud console.

For example:

- Build a Secret Santa app that saves participants and previews assignment
  emails. Keep assignments private; send real email only when requested.
- Build a booking form that stores reservations in a database.
- Build a photo gallery that accepts uploads and serves shareable pages.

Use another tool for drafting an email or generating an image. Ample handles
the hosted app and its data; image handling means uploading, storing and
serving files. Local-only coding and another named hosting provider are
outside this plugin's scope.

## Connect

Install the plugin, then ask for something like "Deploy this project". The
first time, your assistant opens a browser page where you sign in to Ample
Computer with your email (or Google) and approve access. A new email gets a
free account. Nothing runs on your machine: the plugin talks to Ample
Computer's hosted MCP server at `https://api.ample.computer/mcp`.

## What it can do

- **Deploy any app.** Node, Python, static sites, PHP/Laravel, Ruby/Rails,
  Java/Spring, .NET, Elixir/Phoenix, Go and Rust. Ample Computer detects the
  stack, builds it and keeps every release; redeploying unchanged code is
  instant.
- **Add what the app needs.** Managed PostgreSQL (with pgvector), MySQL, Redis
  and MongoDB, S3-compatible buckets with CDN delivery, persistent volumes,
  background workers, private links between services and custom domains with
  automatic HTTPS. A database is created automatically when the app needs one.
- **Send email from your app.** With a claimed account on a paid plan, your app can send
  transactional email (sign-up confirmations, receipts, alerts) from its own
  address, with previews before anything is sent.
- **Run things on a schedule.** Scheduled jobs run a command or an HTTP request
  on a cron schedule in any time zone, or at an interval.
- **Show your apps.** An in-chat panel lists your apps, follows a deploy as it
  runs and shows logs and recent traffic.
- **Change a live app.** Edit its source and redeploy, upload files into an app
  or a bucket, or read build and runtime logs to fix a failure.

Apps sleep when idle and wake on the next request, and every plan has a hard
spending cap that is on by default. Apps run in the USA or Europe.

The plugin also includes three skills that teach the assistant how to deploy,
connect services and migrate an app from another provider.

## Learn more

- Website: https://ample.computer
- Docs for agents: https://ample.computer/AGENTS.md
- Privacy: https://ample.computer/privacy
- Terms: https://ample.computer/terms
- Support: https://ample.computer/#contact
