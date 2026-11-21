---
name: build-ember-sites
description: Build, edit, restyle, fix, preview, publish, or answer capability questions about Ember content sites through the Ember MCP tools. Use for every Ember site-authoring request. Covers design-first setup, static JSX constraints, file layout, token-only styling, the check loop, preview cadence, product boundaries, and safe publishing. Combine it with the relevant specialist Ember skill when collections, forms, images/files, or an import are involved.
---

# Build and edit Ember sites

Own the complete workflow when the user asks in ordinary language. Do not make
them name Ember, provide tool steps, repeat identifiers, or say “continue.” Keep
tool mechanics out of user-facing prose unless recovery requires them.

Read `references/authoring.md` before the first file write in a new site or when
the file, design, or verification contract is not already active. Read
`references/product-boundaries.md` before answering whether Ember supports a
kind of site, feature, plan, account action, or publishing behavior.

## Route specialist work

Use this skill for the overall site workflow and also use:

- `structure-ember-content` before authoring any repeated set with two or more
  records, even if it is a fixed row with no detail pages;
- `build-ember-forms` for any form that must submit to the site owner;
- `add-ember-images-and-files` for uploads, downloads, researched imagery,
  portfolios, galleries, hero photos, or other static assets; and
- `import-sites-to-ember` when rebuilding an existing website or online
  business presence.

## Make decisions and show progress

Use the request and conversation as the brief. Ask only genuinely blocking
questions in the host chat; otherwise make sensible content and structure
decisions and author directly. Ember provides no questionnaire.
Never invent real business facts, credentials, prices, testimonials, contact
details, or claims. Use supplied or researched facts and surface material
unknowns.

Keep the live preview visible. Immediately after the studio applies a design, call
`render_preview` before any file read or write. That mounts the embedded working
tree while the build is still in progress; later file mutations reach the same
view through Ember's live-update channel. Call `render_preview` again after
meaningful checked phases, after the final clean check, and whenever the user
asks to see it. Do not render unchanged state twice or render after every
individual file write. When the user asks for a link to the unpublished draft,
or the host cannot render the embedded view, share the `previewUrl` that
`render_preview` returns — a short-lived authenticated link to the working tree;
when it expires, call `render_preview` again for a fresh one. Never invent a
preview address: the only shareable draft link is the one the tool returned.
The embedded preview's Refresh button requests a fresh authenticated link.
If it asks the user to show the preview again, call `render_preview` in chat.

When starting a new site, call `create_site` with an appropriate name derived
from the request. It creates the account resource only. Then call
`open_design_studio` exactly once with the returned site id and the shortest
useful search term for the site type, usually 1–3 words. This opens the studio
on relevant layouts instead of an unrelated default; the studio remains the
user's visual choice. Do not call `search_designs` separately while the studio
is mounted because the studio owns its in-place search updates.

The user may select an element in Ember's Live preview before asking for a
change. The conversation then carries a “[Selected element from the preview]”
block naming the site id, page, element, and usually a `Source` file and line.
Treat “this”, “here”, or an unqualified change as applying to that element: read
the named source file, edit that element (or the component it lives in), and
leave the rest of the page alone. The CSS selector and text only confirm which
element was meant; never edit by selector.

Finish every mutation batch with `check_site`, fix every reported error, and
repeat until clean. Call `publish_site` only when the user explicitly asks to
publish. Confirm before deleting a site or any user-authored/irreplaceable file.
Removing obvious selected-design demo files during an authorized build needs
no separate confirmation.

For an explicit undo, revert, or “go back to that turn” request, call
`list_checkpoints` for the site, select the exact `turnId` matching the user's
requested point, then call `rollback_site`. Never invent or shorten the id.
MCP working-tree mutations create these checkpoints automatically. A rollback
is itself recoverable in Ember, but it does not erase the external host chat.
