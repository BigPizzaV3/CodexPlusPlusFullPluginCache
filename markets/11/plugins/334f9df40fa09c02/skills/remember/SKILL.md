---
name: remember
description: Save lasting decisions, facts, preferences and project context to the user's Albo brain straight away, without asking first, as compiled truth plus a dated timeline entry with its source and [[slug]] links. Use when the user decides, learns or changes something that will matter later. Never saves health, family, money or other private matters unless asked, and never to a team brain. For saving a link, place, recipe, film or book to the Albo library, use the save skill instead.
metadata:
  triggers:
    - the user decides something ("let's go with …", "we'll launch on …")
    - the user learns or corrects something lasting ("actually, Ana leads sales now")
    - the user states a preference or taste that will matter later
    - '"remember that …", "note that …", "keep this in Albo"'
---

# Remember in the Albo brain

When you and the user decide, learn or change something lasting, save it to
Albo right away. Don't ask "shall I save this?" first; save it, then say in one
line what you saved and where.

Brain tools appear only for people in an Albo team. If `remember` and
`put_page` aren't connected, skip this skill quietly.

## What to save, and what never to save

- **Save:** decisions and their reasons, plans and dates, who owns what,
  preferences and tastes, corrections to earlier facts, and the project context
  a teammate would need.
- **Don't save** small talk, one-off questions, or anything already in the brain
  unchanged.
- **Never save health, family, money or other private matters** (relationships,
  legal trouble, beliefs and so on) unless the user explicitly asks you to. Even
  then, save them only to their **personal** brain, **never to a team (org or
  group) brain**.

## Pick the right brain

- `whoami` shows the default write source (`source_id`). `sources_list` shows
  every brain the user can read and whether it is `writable`.
- `personal` is the user's own brain. Org and group sources are shared with that
  team, so only put team work there.
- Keep the scope the user is working in: personal matters go to `personal`, and
  team project context goes to that team's source. Pass `source_id` whenever the
  default isn't right. Never move content into a wider brain than the one it
  came from without the user's say-so.

## Steps

1. **Check what's there.** `search` (or `resolve_slugs`) for the person,
   project, place or topic. If a page exists, read it with `get_page`
   `include_content: true`.
2. **A single fact about a person, company or thing:** use `remember` with
   `fact`, `entity` (the subject's name or slug), `kind` (`fact`, `preference`,
   `commitment`, `event` or `belief`) and `provenance` (required: where it came
   from, e.g. "Chat with Isaac in Claude, 2026-11-10"). If it corrects an
   earlier fact, pass that fact's id as `replaces`.
3. **A decision, plan or project change on a page:**
   - **Update the compiled truth.** The text above the timeline is the current
     best summary. Rewrite the affected lines so they're true now. For a small
     change use `edit_page` with the page's `expected_revision`.
   - **Append to the timeline.** Use `add_timeline_entry` with `slug`, `date`
     (YYYY-MM-DD), a one-line `summary`, optional `detail`, and `source`. The
     timeline is append-only: never rewrite or delete old entries; add a new one
     that supersedes them.
4. **A new page:** use `put_page` with a lowercase slug such as
   `projects/lisbon-offsite` or `people/ana-silva`, and a `request_id` UUID.
   Format:

   ```markdown
   ---
   type: project
   title: Lisbon offsite
   tags: [offsite, 2027]
   ---

   Team offsite in Lisbon, 12–14 March 2027. [[people/ana-silva]] owns the
   venue; budget agreed with [[projects/2027-planning]].

   <!-- timeline -->

   ## Timeline

   - **2026-11-10** | Chose Lisbon over Porto for the offsite.
     Cheaper flights for most of the team.
     [Source: Chat with Isaac in Claude, 2026-11-10]
   ```

5. **Link it.** Write `[[slug]]` links to the people, projects and places the
   page mentions. Links to existing pages become edges automatically; check
   slugs with `resolve_slugs` so links don't dangle.
6. **Tell the user** in one line: what you saved, the slug, and which brain.

## Notes

- `put_page` **replaces the whole page**. Always read the page with `get_page`
  `include_content: true` and send back the complete content. Prefer
  `edit_page` for changes and `append_page` to add text.
- Keep a `request_id` UUID per write and replay it unchanged if a reply is lost.
  Writes commit before the reply, so there's nothing to poll.
- A page with `readable_by` is limited to those members. Never loosen it; that
  needs an org admin's approval.
- Never invent facts, dates or sources. If the source is the conversation, say
  so.
