---
name: add-web-chat
description: Use when an admin wants a chat on their website with Ciarem, asks for the web chat code again, or says the chat bubble doesn't show on their site.
---

# Add the web chat to a website

Admins only: if a tool answers `requires_admin`, tell the user only workspace admins can set up the web chat.

1. Ask for the website's address and any other domain the chat should load on (for example with and without www).
2. Call `connect_webchat` with `display_name` (how the user will recognise the site; customers don't see it) and `allowed_origins`, each a full origin like https://www.example.com with no path. Pass `position` and `primary_color` (#rrggbb) only if the user asked for them.
3. Give them the `snippet` in a code block and say where it goes: on every page of the site, before `</body>`. With a site builder, it goes wherever the builder accepts custom code for every page.
4. If the chat doesn't show, call `get_webchat_snippet` and check three things: the site's domain is in `allowed_origins` (add it with `connect_webchat`), `enabled` is true, and the tag is on every page before `</body>`.
5. The AI answers the web chat like any other channel: offer to show a reply with `test_ai_reply`.

WhatsApp, Instagram and Messenger connect in the Ciarem web app with the user's Meta login, not from here: share `app_url` from `get_profile`.
