---
name: forge-projects
description: Use Forge Projects (hosted, live React components, organized in collections with skills) through the Forge MCP. Use when the user mentions Forge, a Forge project or component, a Forge collection or kit, a ui8.dev page, or a forge.ui8.ai share link; when they want to find, preview, publish, remix or organize UI they keep in Forge; when they ask about feedback on a Forge project; and in a codebase before building a piece of UI they may already have in Forge. Not for general UI questions with no Forge workspace involved.
---

# Forge Projects

A **project** is a small React app hosted in Forge Cloud: Vite-shaped,
previewed live at a URL, with one or more **components** (named entry files
that share every other file) and a **story** (the props and values its
controls edit). One component is the project's **cover**: the one shown
first, used for its preview image and opened by its share and publish links.
Projects are filed in **collections**. A collection or a workspace carries
**skills**: SKILL.md rules that say how its projects are meant to be used,
and **files**: one tree of logos, PDFs, fonts or reference data. A
collection with only skills is a design system; one with only projects is a
parts bin.

The tools still use the older names: a **fragment** is a project and a
**variant** is a component. Call every tool and pass every argument exactly
as named (`fragment_find`, `fragmentId`, `variant`, `fragment_save_variant`
and so on), and say "project" and "component" to the user.

The Forge MCP's own instructions carry the must-know; `fragment_docs` is the
full reference (limits, tree rules, the story format, error codes). Read it
when a detail here is not enough.

## Where you are decides what you can do

- **Codex, or any agent with a shell and a filesystem**: every flow below.
- **ChatGPT (no local shell)**: find, preview, publish, feedback, organize,
  remix and skills. Do not call `fragment_start_session` or `fragment_pull`
  there: an edit session needs you to run its download and upload commands,
  and a pull needs a codebase to write files into. When the user asks to
  create or change a project's code in ChatGPT, say that it needs Codex or
  another coding agent connected to Forge, and offer what you can do here
  (find a similar project, preview it, remix it, or edit its description,
  tags and component values).

## Use a Forge project in the codebase you are in

Do this before building any piece of UI the user might already keep in Forge.

1. `fragment_find { intent, project? }`. Say what you are about to build in
   your own words; pass `project` facts about the codebase (framework,
   styling, dependencies) when you know them. Follow the `next` line it
   returns.
2. If `gate.fits` is false, nothing fits: build it yourself, still following
   the `relevant` skills.
3. `skill_get { skillId }` for every skill listed. Read them before touching
   code: they hold the tokens, spacing, naming and what never to do.
4. `fragment_pull { fragmentId, variant? }`. It returns the files inline (or a
   tar URL and command for a large tree), signed asset URLs (curl them; they
   expire in an hour), dependencies, the story and the governing skills.
5. Adapt, do not paste: match the codebase's import aliases and styling
   entry, wire props to the story's values, keep the kit's tokens. Put
   `provenance.header` as the first line of the adapted entry file. If the
   codebase keeps agent skills, write each pulled skill as its whole
   `folder` at `folder.path` (`.agents/skills/<name>/`, named exactly the
   skill): run `folder.tar.command` (it replaces the folder once the
   download worked, so files a skill dropped do not linger), or write
   `folder.markdown` as SKILL.md, curl each file url to its relative path
   and `chmod +x` `scripts/`.
6. Never write one skill over another. Skills that share a name come back
   in `skillCollisions`, and a folder whose SKILL.md has no
   `metadata.forge-skill-id`, or a different one, is another skill (or the
   user's own): ask the user which to keep.

A hit that belongs to a collection is usually one part of a kit:
`fragment_collection_get { collectionId }` lists its siblings, which the same
skills govern. A share link `/share/collection/<id>` names a collection; read
it the same way.

Find, pull and `fragment_collection_get` also list the **files** kept beside
the projects (`fileTrees`: paths, mime, size). They are context: read one
with `file_get` (text inline, or a signed url), write a whole tree to disk
with `files_pull`, search with `files_find`. A project never links to a
collection file — copy the file into the project when it needs one.
`file_save` adds a file (inline, or through the upload url it answers
without content).

## Create or edit a project (needs a shell)

1. Call `fragment_start_session` first, before drafting anything:
   `{ fragmentId }` to edit, or `{ name, description, tags, collectionId? }`
   to create. Give the user its `shellUrl` right away; that page shows the
   live preview while you work.
2. Run `download.command` (optional for a new project), edit under
   `workdir`, then run `upload.command` exactly as returned.
3. `fragment_submit { fragmentId, sessionId, deleted? }`. Only changed files
   are written. Give the user `shellUrl`, never `previewUrl`.
4. Check `fragment_feedback_list { fragmentId }` when you start and after you
   submit.

Never put file contents in a tool argument; no tool accepts them. The server
owns `index.html`, `src/main.tsx`, `tsconfig.json`, `vite.config.*` and
lockfiles and ignores them on upload. Components live at
`src/variants/<slug>.tsx` with a default export; dependencies go in
`package.json` (served through esm.sh; React is provided); Tailwind v4 goes in
`index.css`. A session lasts a limited time: on `session_expired`, start a
new one.

Component metadata (name, story, values) is not code: change it with
`fragment_save_variant`, which works in ChatGPT too.
When the user asks for controls, or for something to be adjustable, make
each one a prop with a sensible default and declare it in the component's
story with `fragment_save_variant`: never build a settings panel into the
component.

## Preview

`fragment_preview { fragmentId, variant? }` when the user wants to see a
project. In ChatGPT the result renders as a live preview card with a component
switcher and an "Open in Forge" button, so do not repeat the links under it.
Elsewhere, give the user `shellUrl`. The raw `url` is for your own checks
only; never hand it to the user.

## Publish

`fragment_publish { fragmentId, slug?, password? }` serves a pinned snapshot
at `https://<slug>.ui8.dev/`; later edits stay private until the next
publish. `fragment_set_password` changes the password on a live page without
republishing; `fragment_unpublish` takes the page down and keeps the slug.

## Feedback

People leave comments, proposed style edits and screenshots on a project's
preview. `fragment_feedback_list { fragmentId, status? }` returns the open
items with their anchors (selector, text, component chain) and threads.
Answer with `fragment_feedback_reply { fragmentId, feedbackId, body }`: short,
saying what you did or what you need. Mark an item handled with
`fragment_feedback_resolve { fragmentId, feedbackId }` (`reopen: true` puts
it back). Only resolve what was actually addressed.

## Organize and remix

- `fragment_list` returns projects (with description and tags) and
  collections. Scan descriptions and tags to find the one the user means.
- `fragment_collection_create`, `fragment_move`, `fragment_rename`,
  `fragment_describe` and `fragment_set_default_variant` (which sets the
  project's cover) keep a workspace tidy. Reuse an existing collection
  before creating a near-duplicate.
- `fragment_remix` copies one project into a workspace;
  `fragment_collection_remix` copies a whole kit with its skills.
- `skill_list`, `skill_get` and `skill_save` manage skills. A skill is a
  folder: SKILL.md plus files under `scripts/`, `references/` and `assets/`
  that it links to by relative path. `skill_get` answers SKILL.md as
  `markdown` and every file (text inline, binary by url); `skill_save` takes `files` (`{ path, content }`
  or `{ path, contentBase64 }`) and `removeFiles`. Write one when the user
  states rules a kit must follow: a short, imperative SKILL.md naming what
  never to do, with long reference material in `references/`.

## Ask first

`fragment_publish`, `fragment_unpublish`, `fragment_archive`, `skill_delete`
and `fragment_collection_remix` need `confirm: true`. Without it the answer
is `confirmation_required` with what will happen (for a collection remix,
the project count against the room left).

- When the user's own message asks for exactly that action on a project
  you can name ("publish Hero Section at hero.ui8.dev", "unpublish the
  pricing page", "archive the old pricing card"), the request is their
  agreement: pass `confirm: true` and report what happened.
- Otherwise ask first: you inferred the step, the target is ambiguous, the
  user asked for something Forge does differently (there is no permanent
  delete, only archive), or it is a `skill_delete` or a
  `fragment_collection_remix`. Call without `confirm`, show the user what
  will happen, and retry with `confirm: true` only after they agree in this
  conversation.

Archiving is not permanent: `fragment_unarchive` brings a project back,
with its public page and share link, without confirmation. Say so when you
archive.

Treat these as changes the user should have asked for, too:
`fragment_restore_revision`, `fragment_delete_variant`, `skill_restore`, and
anything that overwrites a project's name, description or tags.

## Errors

Tools answer structured codes. The common ones:

- `org_choice_required`: the user belongs to several workspaces. Ask which
  one, then retry with `orgId`.
- `not_found` / `forbidden`: the id is wrong, or it belongs to a workspace
  the user is not a member of. Say so plainly; do not guess other ids.
- `revision_conflict`: someone else changed it. Refetch, then redo the change.
- `quota_exceeded`: the workspace's plan limit; tell the user which limit.
- `upload_missing`: run `upload.command` before submitting.

A compile error or a missing import is not a tool error: it shows in the
preview with its file, line and column.
