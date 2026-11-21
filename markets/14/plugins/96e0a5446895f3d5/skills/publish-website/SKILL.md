---
name: publish-website
description: Build a static web page or small site and put it online with publish.my. Use when the user wants a page, landing page, menu, event page, report, dashboard, slide deck, prototype or demo published, shared or "put online", or wants to update a site they published before.
---

# Publish a website with publish.my

publish.my hosts static files at `https://<id>.publish.my`. The `publish_files` tool takes the
complete set of files for one site and returns its public link.

## Build the site

- Static files only: HTML, CSS, JavaScript, images, fonts, PDF, audio and video. No server code,
  databases, build steps or environment variables.
- Put `index.html` at the root. Link other files with relative paths (`style.css`, `img/logo.svg`),
  never absolute local paths.
- A single self-contained `index.html` is often best for one page. Use separate files when the site
  has several pages or larger assets.
- Make it work on phones: `<meta name="viewport" content="width=device-width, initial-scale=1">`.
- Send text files as `utf8` and images or fonts as `base64`.
- Everything published is public to anyone with the link. Don't include passwords, API keys, private
  contact details or other personal data unless the user clearly wants them public.

## Publish

1. Call `publish_files` with every file of the site.
2. Give the user the returned link.
3. Remember the site id it reports, so a later change updates the same address.

## Update a site

- Call `publish_files` with the site's `project_id` and the complete new set of files. It replaces the
  whole site, so include unchanged files too.
- If the tool says the site is live, ask the user to confirm replacing it. Only after they say yes,
  call it again with `confirm_update: true`.

## Other requests

- `list_sites` shows the user's sites with their status and views.
- Deleting a site or adding a password to it is done by the user in the console at
  https://console.publish.my. There is no tool for these.
- Don't publish deceptive pages such as fake login forms or impersonations of real organisations.
