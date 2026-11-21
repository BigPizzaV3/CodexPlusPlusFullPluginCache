---
name: publish-and-search
description: Preview, publish and roll back a Frexy website, put it on the person's own domain, and make sure every page meets what search engines and AI assistants look for. Use when they ask to publish or go live, to undo a published change, about their domain, or why a page is not found.
---

# Publish and search

1. **Preview first.** `deploy_preview`, then `get_deployment` until it is ready.
   Its `checks` list what a page still lacks for search and AI assistants (a title,
   a description, one main heading, alt text, links that lead somewhere) and `fit`
   what does not fit a phone: fix those and preview again.
2. **Publish only when they ask.** `deploy_production` puts the site on its live
   address for everyone. Unless they already said, ask first: the whole site, or
   only the page they changed? For one page, pass it in `pages`; every other page
   stays as it is live. A site's first publish is always the whole site, so don't
   ask then.
3. **Undo.** `rollback` puts the live site back to an earlier version.
4. **Their own domain** is connected by them in Frexy Studio's Settings; give them
   that, and the live address once it is set.
5. **The site's settings** (its name, search description and more): `read_settings`,
   and `update_settings` only when they ask.
