---
name: get-started
description: Set up WPZOOM after installing it - check that a WordPress site is connected, help connect one if not, and show what you can do on it.
---

# Get started with WPZOOM

1. Call `list_sites`.
2. If no site is connected yet, explain the two steps the user takes on their own WordPress site:
   - In WordPress, go to Plugins → Add New, search for "WPZOOM AI Connect", install and activate it.
   - Open AI Connect in the WordPress admin menu and press "Connect this site", or call `pair_site` with the site's address and give the user the link it returns. WordPress asks them to approve the connection once.
   Then call `list_sites` again.
3. Once a site is connected, call `wpzoom_site_overview` for it and tell the user, briefly, which theme the site uses and what you can change there.
4. Suggest three things to try, for example: "Run a checkup of my site", "Switch my site to a darker color palette", "Create an About page with a team section and a contact form".

Never ask for the user's WordPress password: the connection uses an application password the user approves on their own site.
