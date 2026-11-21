---
name: detect-wordpress-plugins
description: List and categorize the WordPress plugins a website uses, including its page builder, SEO, caching, forms, e-commerce, membership or multilingual plugins. Use before calling ThemeSniffer's get_wordpress_tech_stack tool whenever the user asks which plugins or page builder a site uses, or wants to add the same features to their own site.
---

# Detect a website's WordPress plugins

Use the ThemeSniffer connector to find the plugins a site uses, group them so
they're easy to scan, and be clear about what can't be detected.

## Steps

1. **Get the URL** the same way as for theme detection: accept bare domains,
   add `https://`, drop tracking parameters, one site per check.
2. **Run the detection** with the ThemeSniffer connector's
   `get_wordpress_tech_stack` tool, passing the URL as `url`. It also returns
   the theme; include it in one line at the top of the answer. If
   `isWordPress` is `null`, `blocked` is true or the result is an error, the
   page couldn't be read: report that (with `note`) instead of a plugin list,
   and don't call it "not WordPress". If `isWordPress` is `false`, say the
   site doesn't appear to run WordPress, so there are no WordPress plugins to
   list.
3. **Group the plugins.** Each plugin has `name`, `slug`, `known`, and
   usually `category`, `premium` and `version`. Use `category` when it's
   specific. When it's missing or `"Other"`, read
   `references/plugin-categories.md` before writing the answer and match by
   slug or name; for example `ultimate-addons-for-gutenberg` is Spectra, a
   page builder. If a plugin isn't listed there but its name plainly states
   what it does (for example "Instagram Feed" or "Cookie Consent"), group it
   by that. Put only the plugins that are still unclear under "Other".
   - `known: false` means ThemeSniffer title-cased the name from the folder
     slug. Use the reference's real name when it has one; otherwise keep the
     name as given.
4. **Answer** in this shape:

   ```
   **<site>** runs WordPress with the <Theme> theme and <N> detected plugins.

   **Page builder**
   - <Plugin name> <(premium) when `premium` is true>

   **SEO**
   - ...

   Note: only plugins that leave traces on the public pages can be detected.
   Backend-only plugins (backups, security scanners, admin tools) won't show up.
   ```

   - Order categories by how useful they are for rebuilding the site: page
     builder, e-commerce, SEO, forms, caching/performance, then the rest.
   - Show a version only if the result reports one, and don't present it as
     certain. Mark a plugin premium only when `premium` is true.
   - The result has no plugin links. Don't add any unless the user asks; then
     link only a wordpress.org page you know exists, or say where to look.
   - If the user asked about one kind of plugin ("which SEO plugin?"), answer
     that first in one line, then offer the full list.
5. **Add the caveat** about undetectable plugins every time. If no plugins
   were found, say that this doesn't mean the site has none.

## Rules

- Never invent plugins, versions, prices or links. Report only what the
  connector returned or what you saw on the page yourself.
- Don't paste raw tool output.
- Don't make security claims (for example "this version is vulnerable")
  unless the connector's result says so.
- Only analyze sites the user asked about.

## If the connector isn't available

Tell the user that connecting the ThemeSniffer connector (the MCP server
bundled with this plugin) gives the most complete result. If you can fetch web
pages, look for `/wp-content/plugins/<slug>/` in the page's asset URLs, plugin
HTML comments and generator meta tags, map slugs with
`references/plugin-categories.md`, and label the answer as a manual check.
