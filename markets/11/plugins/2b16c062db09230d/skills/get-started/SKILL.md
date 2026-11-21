---
name: get-started
description: Check the Aveiro connection and help the user choose a site and a task. Use right after Aveiro is connected, or when the user asks what Aveiro can do or which sites it can reach.
---

# Get started with Aveiro

This workflow only reads data. Explicit instructions from the user take priority over these steps.

1. Call `aveiro_me` to confirm the connection. Tell the user, in plain words, what the connection allows (for example writing pages, publishing, media, social drafts, newsletters) and how many sites it can reach. If the call fails with an authorization error, ask the user to reconnect Aveiro and stop.
2. Call `aveiro_list_sites` and show the sites by name. Use the site IDs it returns; never guess one.
3. If there are no sites, offer to create one. Call `aveiro_list_templates`, let the user pick a template and a name, and call `aveiro_create_site` only after they confirm.
4. Ask which site to work on and what they want to do. Suggest only tasks the connection allows, such as:
   - draft a blog post or update a page,
   - review unpublished changes and publish them,
   - draft a newsletter or social posts about recent content.
5. Continue with the matching workflow: `write-and-publish-pages` for pages, `draft-newsletters-and-social-posts` for newsletters and social posts.

Do not create, change or publish anything in this workflow except a site the user asked for in step 3.
