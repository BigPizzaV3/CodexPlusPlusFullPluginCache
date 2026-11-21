---
name: import-sites-to-ember
description: Rebuild or migrate an existing website, Google Business profile, social profile, or other online business presence into Ember. Use when the user asks to import, recreate, migrate, modernize, or improve an existing site. Preserves verified identity, content, navigation, branding, forms, social links, locations, and source images while adapting them to Ember's design system and static-site boundaries.
---

# Import an existing presence into Ember

Rebuild the source in Ember; do not pixel-clone its layout. Preserve the
source's purpose, verified identity, information architecture, substantive
content, branding, and real assets inside the selected Ember design. Never
invent missing facts or testimonials.

Use the `build-ember-sites` workflow for account preflight, site creation, the
interactive design studio, batching, checks, previews, and publishing. Also use
`structure-ember-content`, `build-ember-forms`, and
`add-ember-images-and-files` wherever their triggers apply.

## Inventory before authoring

Build a migration manifest before creating or editing an Ember site. This is a
hard gate: do not select/apply a design or author pages, components, content,
configuration, or public assets until the manifest is complete. Start with
`sitemap.xml` when available, then follow every same-origin link reachable from
navigation and page bodies. Record each source URL and destination route,
title and metadata, navigation position, substantive copy, contact facts, form
behavior, download, and image. Preserve source paths when Ember can represent
them; record every intentional exclusion.

The manifest must include all of the following:

- Desktop, tablet, and mobile captures, with viewport dimensions and source
  URL. If a full-page capture is unreadable, use viewport and section captures
  rather than inferring what it contains.
- A source-order section geometry inventory: approximate heights, container
  widths, columns, alignment, image/text placement, major spacing, and how
  those relationships change across the three viewports.
- An asset inventory covering logo, favicon, every meaningful `<img>`,
  `picture`/`srcset` candidate, CSS background, carousel slide, gallery item,
  factual team/product/location image, and download. Record role, source page,
  exact candidate URLs, selected highest-suitable original, alt/caption,
  intended Ember reference, and status. Enumerate every carousel/gallery state,
  not only the item visible during capture.
- An interaction inventory covering desktop/mobile navigation, sticky or
  overlay headers, anchors, carousels, tabs/accordions, buttons and links,
  forms and validation, maps, embeds, downloads, and unsupported behavior.
- Reconciliation totals for pages, sections, assets, forms, social links,
  maps, downloads, and interactions, with a named exception for every gap.

When the site exists, persist this working checklist as
`/.ember/import-manifest.md` before authoring so subsequent passes can reconcile
against the same evidence. Do not claim discovery is complete while a count is
unknown or an observed source element has no manifest row.

Use the host's available browsing or user-provided material to inventory all
in-scope pages, navigation order and hierarchy, headings, copy, offerings,
prices, identifiers, contact details, locations, hours, forms, social links,
logo, fonts, colors, and meaningful images. Preserve a multi-page source as
real pages rather than flattening navigation into anchors; keep a genuinely
single-page source single-page.

If the source cannot be inventoried, do not create or edit an Ember site. State
exactly what is missing and ask for a reachable URL, site export,
screenshots/assets, or explicit approval for a partial migration. If sources
conflict, surface the conflict and ask rather than choosing or inventing a
fact. Do not fill unknown business facts with plausible prose.

## Rebuild faithfully

- Keep the verified business or project name prominent in text, not only in a
  logo, slogan, or image. Rename the Ember site with `update_site` once known.
- Preserve exact addresses, phones, emails, hours, prices, location details,
  and social destinations. Use the full verified address in map embeds.
- Preserve the source's page and content grouping while adapting presentation
  to the chosen Ember components.
- Recreate repeated content as Markdown collection entries, not arrays in JSX.
- Classify every form and interactive flow before rebuilding it. Map only
  submit-to-owner forms to Ember's supported `data-ember-form` contract and a
  real thank-you page; match field order, labels, types, choices, required
  states, validation hints, consent, and CTA. Preserve every distinct source
  workflow as a distinct Ember form with its own stable id; there is no
  per-site form-count cap, so never merge a waitlist, RSVP, application, or
  quote request into the contact form to conserve forms. Reuse an id only for
  the same logical form with the same fields and behavior. Tell the user to
  configure recipients in Ember's Forms view. Until they do, describe the form
  as built but not configured; afterward, describe it as configured but not
  yet verified until the owner confirms a real submission, inbox entry,
  redirect, and notification. Never claim inbox or notification delivery was
  verified from the MCP host. Do not silently replace file
  uploads, payments/carts, accounts, live booking/inventory, calculators, or
  custom integrations; preserve an honest external link or supported
  third-party embed when possible, otherwise explain the gap and ask the user.
- For every meaningful source asset, record its URL, role, and alt/caption.
  Success means the highest suitable original is represented by a stable,
  reachable source with the right semantics. A direct public HTTPS URL or an
  Ember-managed path returned by `upload_file` are both valid; choose the
  strategy that best preserves fidelity and reliability. Exclude only duplicate
  variants, trackers, or inaccessible/licence-restricted files, report each
  exclusion, and never substitute unrelated imagery for available original
  work.
- Apply identifiable brand colors and practical font choices through token
  values in `components/theme.ts`; keep logos legible rather than forcing them
  into a text-only wordmark slot.

## Compare and hand off

After the build, reconcile the migration manifest row by row and report
page/form/asset counts plus exceptions. Compare every in-scope source page against the Ember result.
Confirm all substantive content, forms, social links, locations, and usable
source images are represented; remove every piece of demo content. Run
`check_site`, fix every issue, and inspect every route in `render_preview`.

Tell the user what was retained and name any page, image, link, or fact that
could not be accessed. Let the user review the preview and decide when to
publish.
