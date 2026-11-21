---
name: wordpress
description: WordPress sites with Opus Growth (Opus Growth Connector plugin) - posts and pages, Elementor and other page builders, menus, media, SEO plugin fields, translations, plugins, theme files, tracking codes, caching and speed, backups, Contact Form 7 and WooCommerce. Use for any change or question about a connected WordPress site. Covers backing up first, drafts by default, cache purging after edits and the changes that can break a live site.
---

# WordPress

Follow the `opus-growth` skill for preview and confirm. Sites connect through the Opus Growth
Connector plugin; `list_wordpress_sites` lists them, `wordpress_site_info` shows theme, plugins and
versions. Every change happens on the user's live site.

## Before changing anything

1. **Read first**: the post (`wordpress_get_post`), the page build (`wordpress_page_design`), the
   menu (`wordpress_menus`), the setting (`wordpress_option`) you are about to change.
2. **Back up before risky work** (theme files, plugin installs or removals, bulk replace, speed
   settings): `wordpress_full_backup` (UpdraftPlus) and check its status.
3. **One change, previewed**, then purge the cache (`wordpress_purge_cache`) and look at the live
   page (`site_read_url` reads it as a browser gets it). A cached old page is the most common
   "the change did not work".

## Content

- New posts and pages are drafts by default (`wordpress_create_post`); publish only when asked.
- Find text across the site: `wordpress_search_content`; replace it everywhere:
  `wordpress_bulk_replace` (preview lists every affected post; check it for unintended matches
  such as a word inside a URL).
- Page builders: `wordpress_page_design` tells which builder built the page. Elementor pages are
  edited with `wordpress_edit_page_design` (texts, buttons, images, styles), not by rewriting the
  post body, which Elementor would ignore or overwrite.
- Menus: `wordpress_edit_menu` adds, renames, relinks, reorders or removes links.
- Media: `wordpress_upload_media` takes a public image URL; `wordpress_media` browses the library.
- Categories and tags: `wordpress_terms`. Authors' display names: `wordpress_users`.

## SEO and languages

- Meta title, description, canonical and noindex per page: `wordpress_set_seo` (reads the active
  SEO plugin, `wordpress_seo`). Titles about 50-60 characters, descriptions about 150-160, each
  unique.
- Multilingual sites (Polylang or WPML): `wordpress_languages`, and connect translations with
  `wordpress_link_translations` so search engines get correct hreflang links.

## Tracking

`wordpress_tracking` lists every place the site loads Tag Manager or Analytics (theme, plugins,
header code). Two places loading the same tag double-count every visit; keep exactly one.
`wordpress_set_tracking` sets the GTM or GA ID or adds tracking code.

## Plugins, theme and settings

- `wordpress_list_plugins`, `wordpress_install_plugin` (wordpress.org), `wordpress_manage_plugin`
  (activate, deactivate, update, delete). Activating a second caching or security plugin next to
  an existing one can break the site with a server error; check what is active first.
- Theme files: `wordpress_theme_file` reads and edits the active theme. Prefer a child theme:
  parent theme edits are lost on the next theme update.
- `wordpress_option` reads or changes one setting by name. Changing site URL, home or permalink
  settings can take the site offline; do not change those without the user's explicit request.
- `wordpress_core_files` hides version-revealing files (readme.html) for basic hardening.
- Keep the connector current: `wordpress_update_connector`.

## Speed

`wordpress_performance` shows caching and optimisation settings; `wordpress_set_performance` turns
them on or off; `wordpress_critical_css` checks or regenerates LiteSpeed critical CSS. Measure
before and after with `seo_core_web_vitals`. Aggressive JavaScript deferral or CSS combination can
break sliders, menus or forms: change one setting at a time and check the live page.

## Forms and shop

- Contact Form 7: `wordpress_contact_forms`; `wordpress_test_contact_form` submits a real test
  entry and reports mail_sent, mail_failed (usually an email/SMTP setup problem, which also stops a
  form-submit conversion from firing), validation_failed or spam. A sent test reaches the form's
  recipient inbox; tell the user to expect it.
- WooCommerce: `wordpress_woo_products`, `wordpress_woo_orders`, `wordpress_woo_create_product`
  (simple products). Orders contain customers' personal data: show only what the user needs.

## Every operation

The complete list of this area's operations, what each is for and the tool that runs it: `references/operations.md`.
