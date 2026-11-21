---
name: build-frontend
description: Build or fix a website front end that reads content from Agility CMS - fetching content and pages, rendering components, linked lists, images and rich text, caching and revalidation on publish, preview and Web Studio visual editing. Use when a developer is coding against Agility (Next.js or any framework), adding a component end to end, or debugging content that renders wrong or not at all.
---

# Build a front end on Agility CMS

## Ground yourself first

- Read the project's `AGENTS.md` or `CLAUDE.md` if it has one. It holds the
  project's conventions and instance facts.
- For SDK and API details, search Agility's documentation (the Agility
  Knowledgebase MCP's `search_docs` and `fetch_doc`, if connected, or
  https://agilitycms.com/docs). Do not guess method names or parameters.
- For a new Next.js site, start from the Agility Next.js Starter
  (https://github.com/agility/agilitycms-nextjs-starter) and extend its patterns.
- Before writing code against a model, read it with the Agility CMS tools
  (`get_component_model_details`, `get_content_model_details`) and use the real
  field names.

## Add a component end to end

1. List existing models (`get_component_models`, `get_content_models`) and reuse
   one if it fits.
2. Create or update the model with the `content-modeling` skill, then read it
   back.
3. Write the component following the project's existing pattern. In the Next.js
   starter: an async server component receives its content ID, fetches its own
   fields through the project's data layer, and fetches linked lists separately
   by reference name.
4. Register it in the component registry under the model's reference name, or it
   renders as "not found".
5. Add sample content (saved as drafts) and check it in development.

## Data rules that fail silently

- **List limits:** content list calls return 10 items by default and at most 250
  per request. Always pass `take`, and page with `skip` until you have read
  `totalCount`.
- **Field names** arrive with only the first letter lowercased: `Title` is
  `fields.title`, but `URL` is `fields.uRL`.
- **Values can arrive as strings:** numbers and booleans may come back as `"12"`
  and `"false"` (which is truthy). Convert them in the data layer and type the
  converted shape. Test date fields with a time near midnight; they can shift by
  the instance's time zone.
- **Linked content depth:** a field that links to a whole list can come back as
  a stub with only the list's reference name. Fetch the list separately, or set
  the link depth, according to the docs for your SDK.
- **Reference names:** reads return container reference names lowercased. Use the
  exact case from `get_containers` when writing.
- **Missing items:** a deleted component can stay listed on a published page
  until the page is republished. Make components render nothing when their item
  is missing instead of throwing.

## Caching and publishing

- Route every CMS read through one data layer that sets cache tags, and have the
  publish webhook revalidate exactly those tags. A read that skips the data layer,
  or a tag that does not match what the webhook sends, works in development and
  then updates only when the cache expires.
- Development and preview read Staging content with the preview key. "It works
  locally" does not prove content is published. Check the live site in a private
  window.

## Preview and Web Studio

- Preview must validate the preview key, not just check that one is present.
  Otherwise anyone can read drafts on the public site.
- For Web Studio click-to-edit, the rendered HTML needs `data-agility-*`
  attributes: `data-agility-component` only on a component's root element,
  `data-agility-field` on each rendered field (the element must contain only
  that field's value), `data-agility-nested-listitem` on items rendered from a
  linked list, and `data-agility-html` on rich text. Search the docs for "Web
  Studio setup" for the full list and the page and instance attributes.
- The site must allow being framed by the Agility app, and an instance has one
  preview domain, so plan multi-site preview routing early.

## Before calling it done

Run the project's build, which catches components that break on real content.
Then check one page in preview and, after publishing, on the live site.
