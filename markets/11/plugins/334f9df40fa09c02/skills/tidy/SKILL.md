---
name: tidy
description: Tidy the user's Albo brain. Find orphan pages, contradictions, stale pages, duplicates and broken [[links]], show a read-only preview first, then fix only what the user approves. Use when the user asks to tidy, clean up, review or maintain their Albo brain, or as a scheduled weekly routine.
metadata:
  triggers:
    - '"tidy my brain", "clean up Albo", "brain maintenance", "review my notes for problems"'
    - a scheduled tidy run (weekly works well)
    - the user notices duplicates, broken links or out-of-date pages
---

# Tidy the Albo brain

A routine for keeping the brain healthy. It runs in two phases: a **read-only
preview**, then **fixes the user approves**. Nothing is changed during the
preview.

Brain tools appear only for people in an Albo team. If the brain tools aren't
connected, say the Albo brain isn't set up for this account and stop.

## Scheduling it

Users can run this on a schedule (for example a weekly scheduled task in their
AI app) with a prompt like:

> Run the Albo tidy skill on my personal brain. Show me the preview and wait for
> my approval before changing anything.

On a scheduled run with nobody to approve, stop after the preview and leave it
as the report.

## Phase 1: read-only preview

Ask which brain to tidy if it isn't clear (`sources_list` shows them). Tidy one
brain at a time and pass its `source_id` to every call. Some of these tools
aren't on the default list but are still callable; if your app needs their
schemas, call `request_tools` with `{"tools": ["find_orphans", "find_contradictions", "wanted_pages"]}`.

1. **Orphans:** `find_orphans` lists pages with no links in or out. For each,
   suggest pages it should link to, or say it can be merged or archived.
2. **Contradictions:** `find_contradictions` (start with `severity: "high"`)
   lists pairs of pages that disagree. Read both sides with `get_page` and say
   which one looks current, from dates and timelines.
3. **Stale pages:** `list_pages` with `sort: "updated_asc"` shows the
   longest-untouched pages. Flag ones whose compiled truth still describes
   something as upcoming or in progress well after its date.
4. **Duplicates:** look for pages about the same person, project or place under
   different slugs or names, using `resolve_slugs`, `search` for the title and
   other names, and `list_pages` by `type`.
5. **Broken links:** `wanted_pages` lists `[[links]]` that point at no page.
   Each is either a typo of an existing slug (fix the link) or something worth a
   page (suggest creating it).

Show the preview as a short numbered list grouped by kind, each item with the
slugs involved and the fix you propose. Say how many pages you checked.

## Phase 2: fix what's approved

Make only the fixes the user approved, one at a time:

- **Fix a link:** `edit_page` on the linking page, replacing the broken
  `[[slug]]`.
- **Link an orphan:** `edit_page` to add a `[[slug]]` mention in a related page,
  or `add_link` for a typed relationship.
- **Resolve a contradiction:** update the out-of-date page's compiled truth and
  add a timeline entry with `add_timeline_entry` explaining the change.
- **Refresh a stale page:** rewrite its compiled truth from its own timeline and
  linked pages. Don't invent new facts.
- **Merge duplicates:** read both pages, write the merged page to the slug with
  more backlinks (`get_backlinks`) with both timelines combined in date order,
  repoint links from the other slug, then `delete_page` the other page (soft
  delete, recoverable with `restore_page`).

For every write:

- Read the page first with `get_page` `include_content: true` and pass its
  `expected_revision`. `put_page` replaces the whole page.
- Mark full-page writes with `put_page` `ingested_via: "skill:tidy-brain"` and
  a `reason`, so the brain records the tidy run. Give `edit_page` a `reason`
  starting with "tidy-brain:".
- Keep the timeline append-only. Never delete or rewrite old entries.

## Needs extra approval

Ask again, separately, before any write that **widens** who can see something:
merging a personal page into a team brain, moving content between brains,
copying across sources, or loosening a page's `readable_by`. Loosening
`readable_by` is held for an org admin's approval in any case. Never move
health, family, money or other private matters into a team brain.

## Finish

Report what changed (slugs and one line each), what was skipped, and what still
needs a decision.
