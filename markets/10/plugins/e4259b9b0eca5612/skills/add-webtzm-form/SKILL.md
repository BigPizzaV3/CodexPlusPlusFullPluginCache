---
name: add-webtzm-form
description: Add an existing Webtzm form to a website using the connected workspace's embed code, while preserving the submission attributes and checking the page origin.
---

# Add a Webtzm form to this site

Use the Webtzm MCP connection to call `list_forms`, select the form the user
requested, then call `get_form` and `get_form_embed_code`. If the choice is
ambiguous, ask which form to use. If the connection is unavailable, direct the
user to connect Webtzm; do not invent an endpoint or form identifier.

Determine the deployed page's origin (scheme, host, and port) and compare it
with the form's allowed sites. If the origin is unknown, ask for it. If it is
not allowed, explain the required settings change. Update allowed sites only
when the user requests that change and the connection has write access;
preserve existing entries and use the latest `expectedRevision`.

Insert the returned embed code into the requested site file. Keep the markup
unchanged except for styling: preserve every `name` attribute, the hidden
`_webtzm_form` input and its value, the submission action/method, required
attributes, scripts, and Webtzm data attributes. Adapt classes, CSS, spacing,
and accessible presentation to the site's existing design. Do not replace
the submission handler or claim a form works on an unapproved origin.

When file editing is unavailable, return the snippet and explain where to
place it. Do not claim to have edited a website. Do not send a test submission
unless the user authorizes it. Report the selected form, the page origin,
and any remaining setup needed for delivery.
