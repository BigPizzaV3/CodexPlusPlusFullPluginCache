# Manual detection (fallback)

Use this only when the ThemeSniffer connector isn't connected and you can
fetch web pages. It is best-effort: always label the answer as a manual check
and suggest connecting ThemeSniffer for a reliable result.

Fetch only the page the user gave and, when needed, the theme's `style.css`.
Don't crawl other pages.

## 1. Is it WordPress?

Any of these in the page HTML is a strong sign:

- Asset URLs containing `/wp-content/` or `/wp-includes/`
- `<meta name="generator" content="WordPress x.y">`
- `<link rel="https://api.w.org/" ...>` (the REST API link)
- Inline style blocks with ids such as `wp-block-library-css` or
  `global-styles-inline-css`

If none appear, the site may not be WordPress, or it may hide the usual paths.
Say which one is more likely and don't guess a theme.

## 2. Find the theme

1. Look for `/wp-content/themes/<slug>/` in stylesheet and script URLs.
   - One slug: that is the active theme.
   - Two slugs: usually a child theme and its parent. The one whose
     `style.css` has a `Template:` line is the child.
2. Fetch `https://<site>/wp-content/themes/<slug>/style.css` and read the
   header comment at the top:
   - `Theme Name:` the display name
   - `Theme URI:` where the theme comes from
   - `Author:` and `Author URI:`
   - `Version:`
   - `Template:` the parent theme's slug (present only in child themes)
3. Signs of a custom or renamed theme: a slug that matches the site's or
   agency's name, an empty or generic header, or no `Theme URI`.

## 3. Page builder signs

| Builder | Signs in the HTML |
| - | - |
| Elementor | `elementor-` classes, `/plugins/elementor/` assets, generator meta "Elementor" |
| Divi | Theme slug `Divi` or `Extra`, `et_pb_` classes |
| Beaver Builder | `fl-builder` classes, `/plugins/bb-plugin/` or `/plugins/beaver-builder-lite-version/` |
| WPBakery | `vc_` / `wpb_` classes, `/plugins/js_composer/` |
| Bricks | Theme slug `bricks`, `brxe-` classes |
| Oxygen | `/plugins/oxygen/`, `ct-` and `oxy-` classes |
| Breakdance | `/plugins/breakdance/`, `bde-` classes |

## 4. Plugin signs

- `/wp-content/plugins/<slug>/` in asset URLs. The `?ver=` value is often the
  plugin version, but it can also be the WordPress version or a cache key, so
  don't present it as certain.
- HTML comments, for example "This site is optimized with the Yoast SEO
  plugin" or "Rank Math".
- Generator meta tags added by plugins (WooCommerce, Elementor, Site Kit,
  Slider Revolution).

Look up categories in the `detect-wordpress-plugins` skill's
`references/plugin-categories.md` when that skill is available.

## Limits to mention

- Caching, CDNs and security plugins can rewrite or hide asset paths.
- Plugins that only work in the admin area leave no trace on the page.
- A manual check sees one page at one moment.
