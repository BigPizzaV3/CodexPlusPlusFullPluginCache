---
name: ai-server
description: Websites hosted on Opus Growth AI Server: building, editing and publishing sites on the user's own hosting server, deploying a zip, rebuilding Next.js or Vite sites, redirects, blocked paths, headers, DNS records, form submissions and email relay, database backups, snapshots and releases, screenshots and the Google tag gateway. Use for any question or change on a website hosted with Opus Growth.
---

# AI Server websites

Follow the `opus-growth` skill for preview and confirm. AI Server is the user's own hosting server
for one or more websites. `hosting_list_servers` and `hosting_list_sites` list them; `site_info`
shows address, status and disk use. Every change is on the live site.

## Safe editing

1. Read before writing: `site_list_files`, `site_read_file`.
2. Small exact edits: `site_edit_file` (find and replace a unique text). New or whole files:
   `site_write_file`. Prefer the small edit; rewriting a whole file loses what you did not read.
3. Check the result: `site_preview` (screenshot) and `site_read_url` (status, headers and HTML as a
   browser receives it).
4. Undo: every change is snapshotted automatically. `site_versions` lists snapshots and
   `site_restore` restores the whole site or one file. Before a big change, also take
   `site_create_release_tag`; `site_release_status` shows the release safety state.

## Building and publishing

- A whole site from a zip: `hosting_deploy_site_zip`. Built frameworks (Next.js, Vite, CRA) are
  rebuilt from the source on the server with `site_rebuild`.
- New sites: `hosting_install_site_starter` (Tailwind, GSAP, components), and follow
  `site_design_guide` and `site_seo_guide` (titles, meta, structured data, sitemaps).
- Images from the web: `site_fetch` downloads, resizes or converts them. Replacing an image under
  the same file name can keep serving the old one from caches; use a new file name.
- Another website on the same server: `hosting_add_site` (own domain); `hosting_remove_site`
  removes it.

## Domains and traffic

- DNS records for domains hosted here: `site_dns_records` (TXT and CNAME, for example a Search
  Console or email verification record). System records cannot be changed.
- 301 redirects: `site_redirects` (old URL → new URL after any URL change, so rankings and links
  carry over). Blocked paths: `site_block_paths`. HTTP headers: `site_headers`.
- `site_tag_gateway` serves Google tags from the site's own domain (first-party), which helps
  measurement survive blockers; check the tags still fire afterwards (`ga4_realtime`).
- Content-Security-Policy violation reports: `site_csp_reports`.

## Forms and email

Contact form messages: `site_form_submissions`. The email relay that delivers them:
`hosting_configure_site_smtp` (called with only the server it shows the current setup). Form data
is personal data: show only what the user asks for.

## Database

`site_db_backup` before any data change; `site_db_restore` replaces the current database with a
backup, so confirm the exact backup and warn that newer data is lost.

## Trial sites

`hosting_create_trial_site` creates a temporary free trial site on an isolated server. Say clearly
that it is temporary.

## Every operation

The complete list of this area's operations, what each is for and the tool that runs it: `references/operations.md`.
