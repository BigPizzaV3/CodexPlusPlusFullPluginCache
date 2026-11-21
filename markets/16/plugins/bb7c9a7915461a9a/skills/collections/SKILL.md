---
name: collections
description: Manage structured content on a Frexy website, its CMS: collections such as products, services, team members, listings or locations, their fields, records, and a page for each record or a list on any page. Use when the person wants repeated items they can add to and edit without touching the page.
---

# Collections

Read `get_development_standards` with topic `cms` first: it holds the full contract.

1. **See what exists** with `list_collections`, `list_records` and `get_record`.
2. **Define a collection** with `create_collection` (its fields and their types),
   or change one with `update_collection`.
3. **Write records** with `create_record` and `update_record`, using the person's
   own content; never invent people, prices or reviews. `set_record_status`
   publishes one, and a change to published content goes live by itself within a
   minute: no `deploy_production` is needed for it.
4. **Show them on the site**, written into the HTML so search engines and AI
   assistants read them:
   - a list on any page: `<template data-frexy-each="<collection>">` holding one
     record's markup with `{{field}}` tokens;
   - a page per record: `public/<collection>/[slug].html` with
     `<meta name="frexy:collection" content="<collection>">` in its head.
5. `deploy_preview`, `get_deployment`, then give them the page's link.
