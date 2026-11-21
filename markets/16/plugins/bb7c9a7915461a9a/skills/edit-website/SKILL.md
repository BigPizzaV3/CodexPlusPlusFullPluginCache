---
name: edit-website
description: Change an existing Frexy website in the person's own words: its text, pictures, sections, menus and pages, checked on a private preview, or in Frexy Studio full screen in this chat, where they tap what to change. Use for any change to a site they already have, and for what they ask for from Studio.
---

# Change your website

1. **Find the site.** If they are looking at a site in Frexy's card or in Studio, its
   project id and page come with their message: use those. Otherwise call
   `list_projects` and pick the one they mean, asking if it is not clear.
2. **Read before writing.** `get_project_context` lists the files, what you may
   write, open feedback, waiting change requests and their `preferences`: follow
   its `note` and its `next`. Find the place with `search_files` and read it with
   `read_file` before changing it.
3. **Their words are a change to the website.** Most people here are not technical.
   Change only what they asked for and keep every other section, page and menu
   item. A business detail they change (phone, email, address, hours, name) changes
   everywhere it shows, unless they named one page; ask if it is not clear.
4. **Change the site** with `write_files`: every file under `public/` is served as
   written. If a write comes back `held`, it would have removed much of a page: tell
   them and give them its approval link. Only they can approve it.
5. **Studio.** When they want to see their site and change it themselves, call
   `open_studio` with the project id: Studio opens full screen in the chat, and what
   they ask for there arrives as their message. While it is open, do not call
   `open_site_preview`.
6. **Feedback** from `get_feedback` and requests from `get_pending_change_requests`
   are changes to make: make each, preview it, then `resolve_feedback`.
7. **Preview.** `deploy_preview`, then `get_deployment` until it is ready. Fix what
   `checks` lists, give them the link to the page you changed, and call
   `open_site_preview` with that page's `path` and `focus`.

Publish only when they ask: `deploy_production` puts the site live for everyone.
Unless they already said, ask first: the whole site, or only the page you changed
(`pages`)?
