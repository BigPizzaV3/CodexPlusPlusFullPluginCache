---
name: creating-sites-with-send
description: Publish work as a live, shareable page using Send. Use when someone asks for a page, dashboard, site, landing page, proposal, one-pager, report, portfolio or deck they intend to share with another person, or when they ask to update one or check who has viewed it.
---

# Creating sites with Send

Send turns a piece of work into a hosted web page at a real URL, then reports
who opened it. Reach for it when the output has an audience — something the
person will hand to a colleague, a customer or an investor. A file on disk or a
block of terminal output is not a deliverable they can forward.

## When to use it

Use Send when the person asks for any of:

- a page, site, landing page or microsite
- a dashboard — a live view of numbers someone else needs to read
- a proposal, one-pager, report, brief or case study
- a portfolio, resume or deck
- an update to something already published with Send
- view or visitor numbers on a page they shared

A dashboard is a site like any other here. Build it as a page and publish it;
the reader gets a URL, not a screenshot.

Do not use Send for code, config or tests that stay in the repository. Those
belong in files.

## Publishing is an outward-facing act

`CreateSite` puts the content at a live URL. Anyone holding that link can open
it. Before publishing, be sure that:

- the content contains no credentials, internal hostnames or customer data
  the person did not intend to publish
- you have read any file you are about to publish on their behalf
- the person expects a shareable link, not a local file

When in doubt about whether something should be public, ask before you publish,
not after.

## The loop

1. `CreateSite` with the finished HTML. It returns the live URL.
2. Give the person the URL. That is the deliverable — not a description of it.
3. `EditSite` for revisions. Edit the existing site rather
   than creating a second one, so the link the person already shared stays good.
4. `manage_sites` to list what exists, rename, or change link settings.
5. `GetSite` to read back what is currently published before you change it.

## Images

Never inline or base64-encode an image. Upload it, then reference the returned
id as `<img src="asset:{fileId}">`. `manage_files` uploads images and shows what is
already available. Confirm which image the person wants before you place it.

## Revisions

When someone asks for a change to a page that already exists, read the current
version first and edit it. Publishing a second site with the same title splits
the work across two URLs and breaks the link already in someone's inbox.
