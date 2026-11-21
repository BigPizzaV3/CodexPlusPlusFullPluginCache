# Authoring an Ember site

Ember builds static, file-based content sites rendered by `@ember/sites` with
Hono server-side JSX. Treat the host conversation as the brief and use Ember's
MCP tools as the remote filesystem, verifier, preview, and publisher.

## Start or resume the right workflow

For a new site:

1. Call `get_account` to preflight the site limit.
2. Call `create_site` with a concise, appropriate display name derived from the
   request. It creates the site only and returns its `siteId` and next-step
   metadata; it does not mount the studio.
3. Call `open_design_studio` exactly once with that `siteId` and a concise
   `search_term` derived from the site type, usually 1–3 words (`bakery`, `law
   firm`, `wedding photographer`). Do not repeat the full brief. The result
   mounts the interactive studio with that search prefilled and running; the
   full visual catalog is component-private, not model-visible. While it is
   mounted, do not call `search_designs` separately in host chat because the
   studio uses that data-only tool to update its existing view in place.
4. Wait for the user's Apply action. The studio calls `set_design` itself and
   waits for Ember to install the chosen layout, palette, and typography.
5. When the post-Apply continuation arrives, its `design_applied` model context
   means the studio already completed `set_design`; do not call it again. Call
   `render_preview` next, before any file operation, so the embedded working tree
   is visible during the build and follows later writes through live updates.
6. Inspect what the design installed: call `list_files`; use one bulk
   `read_file` pattern such as `/{design.md,site.config.ts,components/theme.ts}`
   or `/components/**/*.tsx` when several files are needed. `read_file` accepts
   `*`, `**`, `?`, `[abc]`, and `{a,b}` Workspace patterns. Read every component
   or page you will reuse; component names and props vary by design. An exact
   existing path wins before pattern expansion, so a dynamic route such as
   `/pages/posts/[slug].tsx` can be read literally. Do not
   replace a known bulk pattern with a sequence of single-file reads.
7. Write in meaningful batches. After each batch, call `check_site`, fix every
   error, and render the completed phase.

If the host cannot render the studio, call the data-only `search_designs` with
the user's purpose and feel, use the focused matches to choose, then call
`set_design` once.

For an existing site, call `list_sites`, then `get_site`, `list_files`, and
`read_file` before editing. Prefer one wildcard `read_file` bulk operation over
many single-file reads when the files share a useful pattern. Prefer
`edit_file` for a small, exact replacement and `write_file` for a new file or
intentional full rewrite. MCP `list_files`, `write_file`, `edit_file`,
`delete_file`, and `upload_file` take one exact path; wildcard bulk operations
are supported by `read_file` only.

When the user explicitly asks to undo or return to an earlier turn, call
`list_checkpoints` and choose the complete `turnId` that matches their request,
then call `rollback_site`. Successful MCP design/file mutations are checkpointed
automatically. The rollback restores Ember's working tree; the host's own
conversation remains intact.

`set_design` is a start-of-build operation. It replaces `/pages`, `/components`,
and `/lib`; `/content` and `/public` survive. Never use it to restyle a site
with real authored work unless the user explicitly accepts that replacement.
Restyle an existing build by editing the token values in
`components/theme.ts`.

## Filesystem layout

- `site.config.ts` contains site name, navigation, footer, and metadata data.
- `components/theme.ts` contains the one stylesheet and its semantic design
  tokens.
- `components/` contains the selected design's shared JSX components.
  `PageShell` wraps every page.
- `pages/` is file-based routing. `pages/index.tsx` serves `/`,
  `pages/about.tsx` serves `/about`, and Markdown pages are also supported.
- `content/<collection>/*.md` contains independently editable collection
  entries with YAML frontmatter and a Markdown body.
- `lib/content.ts` contains collection readers such as `listEntries` and
  `loadEntry`; loaded Markdown is returned as already-rendered `bodyHtml` for
  the design's `Prose` component.
- `public/` contains static assets. Drop the prefix when referencing them:
  `/public/images/hero.webp` serves as `/images/hero.webp`.

The applied design seeds example pages or collection entries. Remove all
unrelated demo content before handoff.

## Constraints that always hold

- Render on the server only: no React hooks, client state, hydration,
  React event callbacks, or `window`/`document` in a component body. Emit
  optional progressive enhancement as static vanilla-JavaScript strings or
  inline scripts; never execute it from a component body.
- Do not add live data sources, visitor-facing APIs, server endpoints,
  scheduled jobs, or runtime application/data fetches. Normal asset requests,
  generated-image URLs, and declared third-party embeds are allowed. Use host
  research tools during the conversation and write findings into pages or
  content as a static snapshot.
- Style through the selected design. Change colors, fonts, spacing, radii, and
  other visual values only through semantic token values in
  `components/theme.ts`. Put any new component's structural CSS in that same
  file and make it consume the tokens. Do not use inline styles or create a
  second styling system.
- Compose pages from the design's existing components. Read a component before
  using it; add a local component and its CSS to `theme.ts` only when the design
  lacks a needed structure.
- Keep the design's permanent chrome: the no-FOUC theme bootstrap `<script>` and
  the fonts `<link>` in `PageShell`'s `<head>`, the `ThemeToggle` in the nav, and
  the `:root[data-theme="dark"]` token block in `theme.ts`. `/design.md` holds
  only what is distinct about the selected design.
- Keep navigation and footer data in `site.config.ts`, rendering in the shared
  components, and page content in pages or collections.
- Build CSS mobile-first. The un-mediaed rule is the phone layout; widen with
  `@media (min-width: ...)` and avoid horizontal overflow.
- A dynamic route such as `pages/posts/[slug].tsx` must export
  `getStaticPaths()` and enumerate every rendered slug.

## Images and files

Image work is complete when every intended visual slot renders a relevant,
high-quality image from a valid non-empty source, carries appropriate alt text,
and remains truthful about what it depicts. Keep any working existing image
until an equal or better replacement is in place. A finished site has no
unfilled image placeholders. If truthful imagery is unavailable, remove the
unused placeholder or ask for the real asset instead of presenting an empty
frame as completed work.

A valid source may be a direct public HTTPS URL (including a stock provider such
as Unsplash), an existing site path, or a path returned by `upload_file` when a
managed Ember copy is useful. Choose the source strategy that best fits the
request. Do not imply that stock depicts the actual business, products, people,
portfolio, or place. For detailed asset options, use the
`add-ember-images-and-files` skill.

## Forms

Use the `build-ember-forms` skill for every submit-to-owner workflow. There is
no per-site form-count cap or persistent slot registry: give contact,
waitlists, RSVPs, applications, quote requests, and other distinct workflows
their own stable `data-ember-form` ids instead of merging them. Reuse an id only
for the same logical form with the same fields and behavior. For forms generated
from repeated records, derive a valid id from the record's stable slug. Removing
all rendered occurrences removes the form from the next published manifest;
historical submissions remain in Ember's Forms history.

## Gated access (shared code or members)

A `protect.json` file at the workspace root can put paths behind a gate. Two
modes exist, and each gate rule names an ordinary rendered page as its
always-accessible `gatePage`:

- A code gate (`{"id": "downloads", "code": "SUNRISE-2026", "paths":
  ["/downloads"], "gatePage": "/downloads/unlock"}`) is a shared-code latch.
  Its gate page posts a field named `code` to `/__ember/unlock`.
- A members gate (`{"id": "members", "access": "members", "paths":
  ["/members"], "gatePage": "/members/signin", "sentPage":
  "/members/check-email"}`, no `code`) admits only the site's member roster:
  visitors enter their email on the gate page and receive a sign-in link by
  email. Build two pages for it, both in the site's own shell:
  - The gate page — a form posting a field named `email` to
    `/__ember/member/request`. Sending the link is a round trip, so the submit
    button uses the same busy state a form's does (`onsubmit` handler that
    disables the button, sets `aria-busy`, and swaps its label from
    `data-ember-busy`, with the `[disabled]::after` spinner in `currentColor`,
    `cursor: wait`, and a `prefers-reduced-motion` fallback — see the forms
    skill). Keep an inline message here for `?member_error=1`, which is where
    an expired or invalid link lands.
  - The check-your-email page named by the gate's `sentPage` — a message page,
    never the form again: a sign-in link is on its way from this site, good
    for about 15 minutes, check the spam folder, and a link back to the gate
    page to try another address. The visitor arrives there with
    `?member_sent=1` and the page needs nothing from it. `sentPage` belongs on
    the gate rule, not in the form, because that page normally lives inside
    the gated area and only the rule can keep it always accessible — like
    `gatePage`. It must render, or `check_site` reports it.

  Keep the confirmation copy conditional ("if that address belongs to a
  member…") — the response never reveals whether an address is on the roster.
  Never write member emails into site files; the roster lives platform-side
  and is not something these tools edit. The owner adds and removes members in the Ember builder under Site Settings → Members, by asking the Ember chat agent (its `membership` tool), or with the `ember sites members …` CLI. Tell the owner
  that when they ask you to add someone. In the builder preview, entering any
  active site-member address or any Ember account email on the owning account's
  team signs in immediately as that identity without sending an email.
  Published-site sign-in still uses the emailed link.

A path covers itself and its descendants; a gate may list several paths, a
site may declare several gates (member and code gates coexist), and the first
matching gate wins — which areas are gated is site structure, decided with
exactly the protected-pages path rules, while the member roster itself is
owner-managed platform data. Both
modes build and preview on every plan; publishing a gated site is plan-gated
(`protected_pages` for code gates, `membership` for member areas) — report a
402 with the gate rather than retrying. Adding people to the member roster is
plan-gated immediately (a listed member can really sign in), unlike building
the member area — the owner tests with their own account email and upgrades
when they want to add members.

## Verify and publish

`check_site` compiles, type-checks, renders every route, checks
`getStaticPaths`, and validates content, internal links, and public assets. Errors
identify a phase such as `compile`, `getStaticPaths`, `render`, `link`,
`content`, or `typecheck`. Fix the source of every error and re-run the check;
do not remove a meaningful route merely to get a green result.

Use `render_preview` after meaningful checked build phases and after the final
clean check. Avoid a second preview when the final check did not change anything
since the last rendered phase. The preview is the working tree; publishing
creates or updates the public snapshot. Call `publish_site` only on an explicit
publish request and only after a clean check. Publishing may be plan-gated; use
`get_account` for current facts and report a 402 without retrying. Hosts that
support it show Ember's own final confirmation, or an upgrade link when the plan
blocks publishing; when the result says the user did not confirm or the upgrade
is not complete, nothing was published, so say so and do not retry unasked.
