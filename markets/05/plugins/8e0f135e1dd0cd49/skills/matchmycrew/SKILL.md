---
name: matchmycrew
description: Build, change, review, and operate MatchMyCrew.com product work using its marketplace domain model, editorial design system, self-hosted architecture, and safety boundaries.
---

# MatchMyCrew

Use this skill for work on the MatchMyCrew.com application, repository, public content,
MCP integration, or product-facing technical decisions. Treat the repository and its
canonical docs as the source of truth; inspect the relevant existing implementation
before changing it.

## Product stance

- MatchMyCrew is an international, English-first marketplace for discovering and
  connecting creative-production professionals. Clients and providers may be the same
  account.
- The core flow is: search by craft/service and location, evaluate a public provider
  profile, then start a private inquiry. Provider profiles are the primary product
  object; provider is the stable term for a listed professional.
- Trust matters: published profiles, verified accounts, reviews, reporting, and
  moderation must be represented honestly. Do not imply booking, payment, identity
  document handling, or real-time messaging exists unless the implementation supports it.
- Keep future booking, availability management, payments, and localization in mind, but
  do not pull deferred features into the current release without an explicit request.

## Working rules

1. Read the relevant reference below before making a material product, UI, or
   infrastructure decision.
2. Reuse existing schemas, helpers, tokens, components, auth/session checks, rate
   limits, and public-visibility predicates. Do not create a parallel convention.
3. Preserve privacy and authorization boundaries server-side. Public discovery may only
   expose published, non-suspended profiles; authenticated MCP access is read-only for
   provider discovery unless the user explicitly requests a separately supported flow.
4. Keep UI copy concise, concrete, and English-first. Design for future localization:
   avoid embedding meaning in text concatenation, layout assumptions, or unexplained
   abbreviations.
5. Verify proportionately. For code changes use the narrowest relevant tests first,
   then run formatting, type checking, linting, and build when the change warrants it.
   For UI changes, check responsive behavior, keyboard focus, reduced motion, dark mode,
   and accessible names. Run Prettier on edited source.

## References

- Read [product.md](references/product.md) for domain language, scope, trust rules,
  and feature boundaries.
- Read [design.md](references/design.md) for the implemented visual and interaction
  system before changing public UI.
- Read [engineering.md](references/engineering.md) for architecture, security,
  deployment, and validation conventions before changing backend or operations.

When repository documentation conflicts with this skill, follow the repository's
current canonical documentation and update the skill only if the rule is stable and
reusable.
