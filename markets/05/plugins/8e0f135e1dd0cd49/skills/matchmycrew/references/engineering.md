# MatchMyCrew engineering reference

## Stack and boundaries

The application is a Next.js 16.3.4 TypeScript app using React 19, PostgreSQL,
Drizzle ORM, Better Auth, local/persistent backend media storage, SMTP, Docker Compose,
and MapLibre GL. It is self-hosted; do not add a managed backend or external email
provider such as Resend unless explicitly requested and documented.

For this repository, read the relevant breaking-change guidance under
`node_modules/next/dist/docs/` before writing Next.js code. Follow existing app,
component, `lib`, and route conventions. Use existing Zod schemas and database helpers.

## Security and operations

Authorization is server-side. Preserve session checks, role checks, public visibility
predicates, input validation, upload restrictions, rate limits, security headers,
structured logging, and moderation logs. Never expose secrets, private account data,
identity evidence, raw errors, or unpublished/suspended profiles through public pages,
search, sitemap, structured data, or MCP.

Production runs on the configured root server at `138.199.211.35`, user `root`, in
`/root/matchmycrew`, deployed with Docker Compose. Production changes are consequential:
inspect the current state and obtain an explicit deployment request before mutating it.

## Quality bar

Use the repository scripts as appropriate: `npm run typecheck`, `npm run lint`,
`npm run test`, `npm run test:a11y`, and `npm run build`. Format edited TypeScript and
TSX with `npm run format` or the narrowest equivalent. For schema or migration changes,
inspect generated SQL and test the affected query/route behavior. For public SEO or
MCP changes, verify canonical URLs, visibility filters, metadata, and the documented
read-only tool boundary.
