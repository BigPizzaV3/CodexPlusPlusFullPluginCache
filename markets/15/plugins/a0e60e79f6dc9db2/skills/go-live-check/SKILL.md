---
name: go-live-check
description: Find out why Agility CMS content or a page is not showing, or is out of date, on the live website, and check that content is really live before a launch or demo. Use when the user says something is published but missing, blank, old or 404, or asks to verify that a page and its content are live.
---

# Why isn't it live?

Work through these in order. Use the read tools; change nothing until you have
told the user what you found and they agree to the fix.

1. **Is it published at all?** Read the item (`get_content_item`) or page
   (`get_page`) and check its state. Saving creates a draft; only publishing
   makes it live.
2. **Are the page's components published?** A page and the content items in its
   zones are published separately. Read each module's content item and check its
   state. Unpublished module content shows as missing or old sections.
3. **Release and pull dates.** A pull date in the past takes an item off the
   site; a release date in the future keeps it off until then. Dates are read as
   US Eastern time. If either is set by mistake, offer to re-save with `null`.
4. **Right locale?** The page or item may be published in one locale but viewed
   in another. Check which locale the site is showing.
5. **Timing and caching.** A publish usually reaches the site within seconds; a
   large batch can take a minute or two, and scheduled changes up to about 15
   minutes. Cached pages may need two refreshes. A brand-new page can 404 briefly
   if the site rebuilt before the sitemap included it.
6. **A deleted component.** If a component's content item was deleted, the live
   page keeps listing it until the page is published again.
7. **Preview vs. live.** Development and preview show drafts. Check the live site
   in a private window, so a preview cookie is not showing drafts.

If everything in Agility is published and correct but the site still shows old
content, the problem is in the website (its cache or publish webhook). Say so;
for developers, the `build-frontend` skill covers caching and webhooks.

Report what you checked, what you found for each step, and the one change you
recommend.
