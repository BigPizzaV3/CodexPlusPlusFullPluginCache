---
name: websitepublisher-api
description: >
   Build and publish websites, web apps, webshops, and admin dashboards through
   conversation using WebsitePublisher.ai. Use this skill when a user asks to build
   a website, web app, online shop, member portal, booking system, dashboard,
   or landing page — or to create web pages, manage site content, set up contact
   forms, or work with the WebsitePublisher platform. Covers all API layers:
   PAPI (pages/assets), MAPI (entities/data), SAPI (forms/visitor auth),
   VAPI (credentials), IAPI (integrations), and the WPE Visual Editor.
license: MIT
metadata:
   author: websitepublisher-ai
   version: "3.0.1"
   website: https://www.websitepublisher.ai
   docs: https://www.websitepublisher.ai/docs
   mcp: https://mcp.websitepublisher.ai
---

# WebsitePublisher.ai — Agent Skill

> Build and publish real websites, web apps, and webshops through conversation. No WordPress. No hosting setup. No CMS.
> The AI Web Platform — you describe it, the AI builds it.

---

## Why WebsitePublisher — What AI Alone Cannot Do

Every AI can generate HTML. But generating code is not the same as having a website.

| Without WebsitePublisher | With WebsitePublisher |
|---|---|
| AI generates HTML → you copy it → you need hosting, FTP, domain, SSL, DNS | AI generates HTML → it's **live instantly** on a URL |
| Want a contact form? Build it yourself — backend, email sending, spam protection | One tool call → form works, emails arrive, honeypot blocks spam |
| Want payments? Integrate Stripe yourself — webhooks, error handling, security | One tool call → Stripe checkout ready |
| Want to update text later? Ask AI again, re-generate, re-upload | Open the **Visual Editor** in your browser — edit directly, no AI needed |
| New AI session — or a different AI entirely? The model forgot everything | **The platform remembers, not the model.** Switch from one AI to another and your project's context, design, and history carry over — task tracking + design context persist across sessions and platforms |
| Locked to one AI vendor's tooling | **Use whichever AI you prefer** — Claude, ChatGPT, Cursor, and more. Your site and data don't change. Model-agnostic by design |
| Dynamic data (menu, team, products)? Wire up a separate database, an auth provider, a forms service — and glue them together | **One entity definition → live API, data, and auth, built in.** No extra accounts, no integration plumbing |

**WebsitePublisher is not a website builder.** It is the infrastructure layer that turns
AI-generated content into real, working web products — with data, forms, auth, payments,
integrations, and visual editing built in.

**Anything that lives on the web is in scope**, on the same building blocks
(pages + entities + visitor/admin auth + integrations + scheduled tasks):
marketing sites and landing pages, **webshops** with checkout, discounts, and loyalty,
**web apps** and internal tools, **member portals** with magic-link login,
**admin dashboards** with full CRUD, booking and lead-gen systems, blogs, prediction
games, and more. When a user asks for "an app", "a shop", "a portal", or "a tool" —
this platform builds it. Do not narrow the conversation to "a website".

---

## ⚠️ IMPORTANT: Read This First

**If the `get_skill` tool is available: call it before doing anything else.**
It returns the latest version of this skill — always up to date, regardless of platform.

If `get_skill` is not available, continue with this document.

---

## You Are the Builder — Solve It Yourself

You build and operate the site. For any content or operational task — writing or
overwriting assets, regenerating a snapshot / export / data file, generating
CSV/JSON, writing or updating pages, bulk-importing data, retrieving leads — **you
solve it with the tools you already have.** Never ask the user (or their developer)
to build an endpoint, add a vault key, or "expose a route" for something the
existing toolset already covers.

**Before you ever conclude a capability is missing:**

1. Check your MCP tools — `upload_asset`, `patch_asset`, `update_page`, `patch_page`,
   `create_page`, `execute_integration`, `list_assets`, `get_asset`.
2. **List what's actually wired on the project — don't rely on memory or even this
   document.** `list_integrations(project_id)` returns every integration (configured
   *and* available) with all its endpoints straight from the manifest;
   `get_integration_schema(project_id, service)` returns the exact input fields for an
   endpoint; `list_assets(project_id)` shows every existing file. These are the ground
   truth — query them before assuming a capability, endpoint, or asset is missing. Then
   cross-check the **Asset Proxy**, **Admin-Only IAPI Calls**, and **API Quick Reference**
   sections of this skill.
3. **Never invent or guess endpoints.** The IAPI route is always
   `/project/{id}/{service}/{endpoint}` — match the host and shape the project already
   uses (check an existing working call or the project's admin/WSA bridge; some setups
   expose IAPI at `api.websitepublisher.ai/iapi/...`, others at an `iapi.` subdomain).
   `/mapi` is entities/data only and has no asset-write route. A made-up top-level
   route like `/project/{id}/upload-asset` returns `404`; that is your mistake, not a
   platform gap. Asset writes go through the `asset_proxy/upload` endpoint.

**Canonical asset write (so this never recurs):**

| Where | How |
|---|---|
| Server-side (you, via MCP) | `upload_asset(slug, content_text \| content, overwrite: true)` to create/replace; `patch_asset(slug, patches)` for in-place text edits |
| Browser admin panel | `POST /iapi/project/{id}/asset-proxy/upload` with `Authorization: Bearer wsa_…`, body `{ slug, base64, overwrite: true }` |

Asset Proxy is **not images-only** — it takes any `slug` and stores any bytes in the
PAPI asset system. Writing a JSON/CSV/text data file (e.g. a products snapshot) is the
same call: base64-encode the text and send it with its `.json`/`.csv` slug. It needs
**no new endpoint and no vault key.**

**Solvable task vs genuine platform gap:**

- **Solvable — DO it. Never escalate. Never request keys or endpoints for:** asset
  write/overwrite · snapshot / export / data-file generation · page write or content
  update · bulk import · lead retrieval · admin auth.
- **Genuine platform gap — report it via `capability_requests`, but do NOT hand off
  the build.** Only when *no* MCP tool **and** *no* documented IAPI/PAPI endpoint exists
  for the operation and it needs a platform-side code change. **LAST RESORT** — never a
  shortcut around solvable work:
  ```
  execute_integration(service: "capability_requests", endpoint: "submit-request",
    input: { ...the operation you need, what you tried, why each was insufficient... })
  ```
  This persists the gap so the platform team can review and build it generically.
  Do not ask the site's developer to hand-build a redundant route, and do not request
  `AAPI_*` or vault keys to perform content, asset, or export work — those authenticate
  via `wsa_` or your MCP session and never need vault AI keys.

---

## Step 1 — Check Connection

Before doing anything, verify the user is connected to WebsitePublisher.ai.

**If connected** (tools respond correctly): proceed to Step 2.

**If not connected**: explain in simple terms:

> "To build your website I need to connect to WebsitePublisher.ai. All you need is your email address — I'll guide you through the rest. It takes about 30 seconds."

Direct the user to sign in at: **https://www.websitepublisher.ai/dashboard**
After signing in, they return here and you continue from Step 2.

---

## Step 2 — Choose the Path

Once connected, ask ONE simple question:

> "What would you like to do? I can build you a brand new website, web app, or shop, redesign your existing site, or if you're not sure yet — I can show you what's possible in a few minutes."

### Path A — "Wow Me" (show first, ask later)

The user is curious but not yet convinced. **Do not ask a long list of questions.**

Ask only:
> "What kind of business or project is this for? Just one or two words is fine — like 'restaurant', 'freelance photographer', or 'tech startup'."

Then immediately build a **complete, impressive demo website** based on that one answer. Use your creativity. Make it beautiful. Show what AI can do.

After the demo is live, share the URL and say:
> "Here's what I built in a few minutes. Want to make it yours? I have a few quick questions to personalise it."

Then move to the intake (Path B) — the user is now convinced.

### Path B — Full Intake (user knows what they want)

Ask questions **one at a time**, conversationally. Do not present a form or list.
Speak like a consultant, not a questionnaire. Use simple, friendly language.

**Phase 1 — Goal (start here)**
- What should the website achieve? (get customers, show portfolio, sell something, inform people?)
- Who is the target audience?
- Does a website already exist? If yes: what needs to improve?

**Phase 2 — Identity**
- Business or project name?
- What does the business do? (ask for a short description in their own words)
- Contact details: email, phone, address (only ask what is relevant)
- Logo and brand colours available? (if yes: ask them to share)

**Phase 3 — Style & Technical**
- Three websites they like the look of (not necessarily competitors) — and why?
- Domain name already registered? If yes: which one?
- Any specific pages needed? (about, services, contact, blog, portfolio...)
- Any keywords important for search engines?

**Do not ask all questions if answers make some irrelevant.** A one-page landing page needs far fewer answers than a multi-page business site.

### Path C — Redesign Existing Website

The user has an existing website and wants it improved or migrated to WebsitePublisher.

1. **Ask for the URL** of the existing website
2. **Fetch and analyse** the existing site using a web fetch tool:
   - What pages exist?
   - What is the content, structure, and messaging?
   - What works well? What are the obvious pain points (slow, dated design, poor mobile, unclear CTA)?
3. **Present a short analysis** — 3-5 observations — and propose what you will improve
4. Ask one confirmation question:
   > "I'll keep all your content but give it a fresh design with better structure. Any specific things you want to keep or change?"
5. Build the new version — same content, improved design, better UX
6. **Migrate images** — use `upload_asset` with `source_url` to import images from the old site
   to the CDN (see "Assets — Importing Images from External URLs" below)
7. Share the URL and point out the specific improvements made

**Do not ask for a long list of preferences before showing something.** Analyse → propose → build → refine.

---

## Design Guidelines

> **Before building any HTML, fetch the design skill for detailed guidelines:**
> Call `get_skill` with `skill_name="design"` — it contains comprehensive typography, color,
> layout, animation, and atmosphere guidelines that produce professional-quality websites.
>
> If a `frontend-design` skill is also available in your environment, read that too.
> The guidelines below are a minimal fallback. The design skill is always more complete.

Every website you build must look **professionally designed**, not like AI-generated template output.
Follow these principles:

### Typography
Choose distinctive, characterful fonts — never default to generic families like Arial, Inter, Roboto, or system fonts.
Pair a display font (for headings) with a refined body font. Google Fonts is available via `<link>` tags.

### Color & Theme
Commit to a cohesive palette with **one dominant color and sharp accents**. Avoid timid, evenly-distributed palettes.
Use CSS custom properties (`--color-primary`, `--color-accent`, etc.) for consistency across pages.
Vary between light and dark themes — do not always default to white backgrounds.

### Layout & Composition
Break out of predictable grid patterns. Use asymmetry, generous whitespace, overlapping elements, or full-bleed sections to create visual interest.
Every page should have a clear visual hierarchy that guides the visitor's eye.

### Motion & Micro-interactions
Add CSS animations for page load reveals (staggered `animation-delay`), hover state transitions, and scroll-triggered effects.
Prioritize CSS-only solutions. One well-orchestrated entrance animation creates more impact than scattered effects.

### Atmosphere
Create depth and texture — not flat solid-color blocks. Use gradient meshes, subtle noise/grain overlays, layered transparencies, or dramatic shadows depending on the aesthetic.

### The Rule
**No two websites should look the same.** Match the design to the business, audience, and purpose.
A law firm looks nothing like a skate shop. A restaurant looks nothing like a SaaS landing page.
If the user has not specified a style preference, choose a bold direction and commit to it.

---

## Step 3 — Build the Website or App

### Project Setup

1. Get available projects: use `list_projects`
2. If no project exists or user wants a new one: use `create_project` with a name (and optional subdomain)
3. Note the `project_id` — used in every subsequent call
4. **Check design context:** call `get_project_status` — if `design_context` is set, use those colors, fonts, and style notes as the foundation for all pages you build. If `design_context` is null, ask the user for their preferred colors, fonts, and style direction during intake, then save it:
   ```
   execute_integration(
     project_id: ...,
     service: "site_context",
     endpoint: "set-context",
     input: {
       color_palette: { primary: "#...", secondary: "#...", accent: "#...", background: "#...", text: "#..." },
       fonts: { heading: "Font Name", body: "Font Name" },
       style_notes: "Short description of the visual direction",
       locale: "en"
     }
   )
   ```
   This ensures all future sessions automatically match the same design language.

### Integration-First — the decision gate

**Before writing ANY custom data or business logic, ask: does a platform endpoint
already exist for this?** Run `list_integrations(project_id)` first. If the endpoint
exists, use it — do not rebuild it in page JavaScript.

This is a **security rule**, not a convenience: integrations are server-side backed —
credentials in the Vault, input validation, rate limiting, CSRF, and multi-tenant
scoping are handled by the platform. Custom client-side logic for the same job is
manipulable by any visitor (prices, stock, points, order data) and untested.

| ❌ Never hand-roll in page JS | ✅ Platform owns it |
|---|---|
| Summing cart line items into a total | Read `cart.subtotal_cents` from the cart endpoint |
| Computing a discount / tier price | `discount` / pricing endpoints calculate it |
| Checking or updating stock | Inventory endpoints check-stock server-side |
| Writing loyalty/points balances | Loyalty endpoints do accrual and redemption |
| Creating or mutating orders | `order-management` endpoints |

**Ownership boundary:** the integration owns totals, tax, discounts, stock, points,
and order creation. You own the form and rendering the values the integration
returns. If you catch yourself re-computing a number the platform already returns —
stop.

**When an integration call fails:** every failure carries a structured
`error_object` — `type`, `code`, and `message` are always present; `field` and a
`recovery` hint appear when applicable. **Read it before changing approach.** Never
replace an integration with custom code because the first call failed — fix the
call (or trace it with the Request Tracer) instead.

### Page Structure Guidelines

Plan the pages before building. Common structures:

| Website type | Recommended pages |
|---|---|
| Landing page | index only |
| Business / SME | index, about, services, contact |
| Portfolio | index, work/projects, about, contact |
| Restaurant | index, menu, about, reservations/contact |
| Blog | index, blog-overview, post-template, about |

Always create an `index` page first — this becomes the homepage.

### Fragments — Reusable Components Across Pages

When a website has more than one page, shared elements like headers, footers, and
navigation **must** be built as fragments — not copied between pages.

**What is a fragment?** A reusable HTML snippet stored once and included in any page.
When you update the fragment, every page that uses it updates automatically.

**When to use fragments:**
- Navigation / header — always
- Footer — always
- Any section that appears on 2+ pages (CTA banner, sidebar, cookie notice)

**How to create and use fragments — one tool, operation-based:**

All fragment work goes through the single `fragments` tool. Pick an `operation`:
`list`, `create`, `update`, `patch`, `delete`, `versions`, `rollback`.

1. Create the fragment:
   ```
   fragments(operation: "create", project_id: 12345,
     name: "site-header", content: "<header>...</header>")
   ```

2. Include it in any page with an SSI comment:
   ```html
   <!--#wps-include fragment="site-header" -->
   ```
   The platform replaces this comment with the fragment content at render time.
   The comment is invisible to visitors.

3. Change the fragment once → all pages reflect the change:
   - **Small edit → `patch`** (targeted find/replace, token-efficient, keeps version history):
     ```
     fragments(operation: "patch", project_id: 12345, name: "site-header",
       patches: [{ operation: "replace", find: "<a href=\"/old\">", replace: "<a href=\"/new\">" }],
       patch_summary: "Update nav link")
     ```
     Each `find` must match **exactly once**. Use `operation: "delete"` in a patch to remove a snippet.
   - **Full rewrite → `update`** (full content replace; supports `base_version_hash`
     optimistic lock from `list` — a mismatch returns 409; `force: true` skips the check):
     ```
     fragments(operation: "update", project_id: 12345, name: "site-header",
       content: "<header>...updated...</header>")
     ```

4. Version history & rollback:
   ```
   fragments(operation: "versions", project_id: 12345, name: "site-header")
   fragments(operation: "rollback", project_id: 12345, name: "site-header", target_version: 3)
   ```

All changes invalidate the page cache automatically.

**Rules:**
- Every multi-page site MUST use fragments for header and footer
- Fragment names should be descriptive: `site-header`, `site-footer`, `cta-banner`
- A fragment is a complete HTML block — it does not include `<!DOCTYPE>`, `<html>`, or `<head>`
- List existing fragments + their versions: `fragments(operation: "list", project_id: 12345)`
- Never copy-paste the same header/footer HTML into multiple pages
- The old tool names (`create_fragment`, `update_fragment`, `list_fragments`,
  `delete_fragment`) still dispatch but are **deprecated** — always use `fragments`

### Building Pages

Every page must be a **complete, valid HTML document**:

```html
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Page Title</title>
   <!-- Optimizer - Canonical -->
   <!-- Optimizer - Custom Meta -->
   <!-- Optimizer - Open Graph -->
   <!-- Optimizer - Header Javascripts -->
</head>
<body>

<!--#wps-include fragment="site-header" -->

<!-- page content here -->

<!--#wps-include fragment="site-footer" -->

<!-- Optimizer - Footer Javascripts -->
</body>
</html>
```

**Critical:** Always include the `<!-- Optimizer - ... -->` comment tags exactly as shown.
These activate WebsitePublisher's built-in SEO engine: canonical tags, Open Graph headers,
custom scripts, and tracking injection. They are invisible to visitors — the platform
processes and removes them automatically.

### Page Metadata

When creating or updating a page, you can pass these metadata fields:

```json
{
   "slug": "about",
   "content": "<!DOCTYPE html>...",
   "meta": {
      "seo_title": "About Us — Company Name",
      "seo_description": "We are a ...",
      "seo_keywords": "keyword1, keyword2",
      "seo_robots_index": true,
      "seo_robots_follow": true,
      "page_language": "en",
      "landingpage": false
   }
}
```

| Field | Default | Notes |
|---|---|---|
| `seo_title` | Page name | Shown in browser tab and search results |
| `seo_description` | — | Search result snippet, 150-160 chars ideal |
| `seo_keywords` | — | Maximum 9, comma-separated |
| `seo_robots_index` | false | Set true to include in sitemap and search engines |
| `seo_robots_follow` | false | Set true to allow link following |
| `page_language` | — | ISO code e.g. "en", "nl", "de" |
| `landingpage` | false | Set true to make this the homepage |
| `redirect_code` | — | 301 or 302 — turns page into a redirect |
| `redirect_destination` | — | Full URL or relative path for redirect target |

> **Note about `landingpage: true`** — when set, the platform serves the page at `/`
> AND 301-redirects its slug (e.g. `/dashboard`, `/index.html`) to `/`. This affects
> any client-side `window.location.replace()` call: redirect to **`/`**, not to the
> page slug, or you create a redirect loop.
>
> Common pitfall: after admin login, `replace('/dashboard')` loops if `/dashboard`
> is `landingpage: true`. Use `replace('/')` instead.

### Visual Editor (WPE) — Edit Without AI

The Visual Editor allows website owners to make changes directly in their browser —
no AI conversation needed. This is important: **users are not locked into AI for every update.**

What the Visual Editor supports:
- **Upload and replace images** — click any placeholder, upload a photo, crop and position it
- **Drag-and-drop reorder** — rearrange sections, cards, and content blocks visually
- **Edit text and styles** — change colors, fonts, spacing directly on the page
- **Lightbox preview** — full-size image viewing for galleries and portfolios

After edits, the user clicks "Save & Close" and changes are live immediately.
No deployment, no AI, no code.

**When to offer the Visual Editor:**
- After building a website → always create an edit session for image replacement
- When the user says "I want to rearrange the sections" → edit session
- When the user says "I'll update the photos myself" → edit session with instructions
- When handing off a finished site → mention that they can always edit visually

**How to create an edit session:**
```
create_edit_session(project_id: 12345, slug: "index")
→ returns edit_url — share this with the user
```

After the session, retrieve what changed:
```
get_edit_session_changes(project_id: 12345, session_id: "...")
→ returns list of changes made by the user
```

#### ⚠️ Placeholder images — mandatory rules for the Visual Editor

When building pages with image slots for the Visual Editor, follow these strict rules:

**Rule 1 — Use `data-wpe-slot` on every `<img>` tag**
The editor uses this attribute to identify the correct img on upload.
Without it, the editor cannot replace the image.

**Rule 2 — The `src` MUST be a working URL**
An empty `src=""` or a 404 URL makes the image invisible in the browser.
The editor can only target images that actually render on the page.
Always use `https://placehold.co/` as placeholder — it loads reliably.

**Correct example:**
```html
<img
        src="https://placehold.co/800x600/D6EEF2/1B5E6B?text=Photo+description"
        data-wpe-slot="unique-slot-name"
        alt="Description"
        id="unique-slot-name">
```

**Placehold.co format:** `https://placehold.co/{width}x{height}/{background}/{text}?text={label}`
Use colors matching the site's color scheme so placeholders look polished.

**Never do this:**
```html
<!-- ❌ Empty src — invisible, not clickable -->
<img src="" data-wpe-slot="my-photo">

<!-- ❌ Non-existent path — 404, invisible -->
<img src="/assets/my-photo.jpg" data-wpe-slot="my-photo">
```

**After upload via the editor** the `src` is automatically replaced by the CDN URL
(`cdn.websitepublisher.ai/custom/wid{id}/images/...`).

#### Common placeholder dimensions

| Usage | Dimensions |
|---|---|
| Hero wide | 1200x675 |
| Photo 4:3 | 800x600 |
| Portrait | 600x800 |
| Nav logo | 240x48 |
| Team card | 600x520 |

#### ⚠️ Image performance — mandatory rules

Every `<img>` tag MUST include `width` and `height` attributes matching the rendered dimensions. This prevents Cumulative Layout Shift (CLS) — without them, the browser cannot reserve space before the image loads, causing visible page jumps.

Images below the fold MUST include `loading="lazy"`. This defers loading until the image is near the viewport, reducing initial page weight and improving mobile performance.

**Rules:**

| Rule | Why |
|---|---|
| Always set `width` and `height` on `<img>` | Prevents CLS — browser reserves space before load |
| Add `loading="lazy"` to below-fold images | Defers load — critical for pages with many images |
| Hero images and above-fold logos: keep eager | These are visible immediately — lazy would delay them |
| Match dimensions to CSS rendered size | Use the pixel values from CSS (e.g. if CSS says `width: 28px`, set `width="28" height="28"`) |

**Correct examples:**
```html
<!-- Above fold: dimensions only, no lazy -->
<img src="https://cdn.websitepublisher.ai/custom/wid12345/logo.svg" alt="Logo" width="80" height="80">

<!-- Below fold: dimensions + lazy -->
<img src="https://cdn.websitepublisher.ai/custom/wid12345/logo/ChatGPT.png" alt="ChatGPT" width="28" height="28" loading="lazy">
```

**Never do this:**
```html
<!-- ❌ No dimensions, no lazy — causes CLS and eager-loads everything -->
<img src="https://cdn.websitepublisher.ai/custom/wid12345/images/photo.jpg" alt="Photo">
```

**Impact:** A page with 11 images missing `loading="lazy"` fires 11 simultaneous CDN requests on page load. On mobile (slower network, in-app mail browsers), this causes blank pages and multi-second load delays. Adding lazy loading reduced this to 1-2 eager requests with the rest deferred.

### Assets — Images, CSS, JS, and Files

Assets are files stored on the WebsitePublisher CDN (`cdn.websitepublisher.ai/custom/wid{id}/...`).
Use `upload_asset` to add images, stylesheets, JavaScript, fonts, PDFs, and other static files
to a project. Assets are served globally with caching — fast and reliable.

**Three ways to provide content:**

| Parameter | Use for | Example |
|---|---|---|
| `source_url` | Import from any public URL — the server fetches it for you | Images from existing websites, Unsplash, DALL·E, any HTTPS URL |
| `content` | Base64-encoded binary data | Images generated locally or received as base64 |
| `content_text` | Plain text content (saves tokens vs base64) | CSS, JS, JSON, SVG, HTML, XML, MD files |

Always provide exactly **one** of the three. Never combine them.

#### Importing Images from External URLs

The `source_url` parameter is the easiest way to bring images into a project. The server
fetches the file, validates it (HTTPS only, no internal IPs), and stores it on the CDN.
This works for **any public HTTPS URL** — not limited to any specific platform.

**Common use cases:**
- Migrating images from an existing website (WordPress, Wix, Squarespace, any CMS)
- Importing stock photos from Unsplash, Pexels, or similar services
- Saving AI-generated images (DALL·E, Midjourney URLs)
- Pulling logos or assets from a client's current hosting

**Example — import a single image:**
```
upload_asset(
  project_id: 12345,
  slug: "images/hero-photo.jpg",
  source_url: "https://existing-site.com/wp-content/uploads/2025/hero.jpg"
)
→ CDN URL: cdn.websitepublisher.ai/custom/wid12345/images/hero-photo.jpg
```

**Example — batch import from an existing site:**
```
upload_asset(project_id: 12345, slug: "images/project-1.jpg", source_url: "https://old-site.nl/uploads/photo1.jpg")
upload_asset(project_id: 12345, slug: "images/project-2.jpg", source_url: "https://old-site.nl/uploads/photo2.jpg")
upload_asset(project_id: 12345, slug: "images/team-photo.jpg", source_url: "https://old-site.nl/uploads/team.jpg")
```

Then reference the new CDN URLs in your page HTML:
```html
<img src="https://cdn.websitepublisher.ai/custom/wid12345/images/project-1.jpg" alt="Project photo">
```

**Rules:**
- `source_url` must be HTTPS — HTTP URLs are rejected
- Internal/private IP addresses are blocked (SSRF protection)
- Works for images (JPEG, PNG, WebP, GIF), PDF, fonts (.woff, .woff2, .ttf), and .ico files
- Set `overwrite: true` to replace an existing asset with the same slug
- The slug determines the CDN path — use descriptive names: `images/hero.jpg`, `images/team/jan.jpg`
- Alt text can be set via the `alt` parameter for images

**When migrating a website:** list all images on the old site first (via web fetch, sitemap,
or CMS tools), then upload each one with `source_url`. Update page HTML to reference the
new CDN URLs. The old site must remain accessible until all images have been imported.

#### Uploading Text-Based Assets

For CSS, JavaScript, JSON, SVG, and other text files, use `content_text` instead of base64
encoding. This is more token-efficient and easier to read:

```
upload_asset(
  project_id: 12345,
  slug: "css/custom-styles.css",
  content_text: "body { font-family: 'Inter', sans-serif; }"
)
```

#### Managing Existing Assets

| Action | Tool |
|---|---|
| List all assets | `list_assets(project_id: 12345)` |
| Read asset content | `get_asset(project_id: 12345, slug: "js/app.js")` |
| Edit text asset in place | `patch_asset(project_id: 12345, slug: "js/app.js", patches: [...])` |
| Replace asset | `upload_asset(project_id: 12345, slug: "images/old.jpg", source_url: "...", overwrite: true)` |
| Delete asset | `delete_asset(project_id: 12345, slug: "images/unused.jpg")` |

### Dynamic Data (MAPI) — When Entities Make Sense

**Use MAPI entities when content is managed independently of page design** — the
owner (or a different AI session) should be able to add, remove, or reorder items
without touching page HTML.

**Use MAPI + SSR for:**

| Content type | Entity name | Example fields |
|---|---|---|
| Menu items | `menuitems` | name, description, price, category, sort_order |
| Team members | `team` | name, role, bio, photo_url, sort_order |
| Services / offerings | `services` | title, description, icon, price, sort_order |
| Portfolio projects | `projects` | title, description, image_url, link, category, sort_order |
| Testimonials / reviews | `testimonials` | name, role, company, quote, photo_url |
| Blog posts | `posts` | title, slug, content, author, published_at, featured_image |
| FAQ items | `faq` | question, answer, category, sort_order |
| Events | `events` | title, date, location, description, registration_url |
| Products (showcase) | `products` | name, description, price, image_url, category |

**Use static HTML when:**
- Content is small and fixed (≤5 items that rarely change — e.g. 3 services on an about page)
- The page is a one-off (hero text, about narrative, single landing page)
- The owner will only update content through an AI session anyway
- It's page structure and layout (sections, containers)

**Don't over-engineer.** A restaurant with 8 menu items that change twice a year
does not need a MAPI entity + SSR template + admin panel. Static HTML with clear
structure is fine — the AI can update it in 30 seconds when the menu changes.

**The trigger for MAPI:** when you hear "I want to add/remove items myself" or when
items will grow beyond 10, or when multiple pages show the same data differently
(e.g. a shop overview AND a homepage featured section both pulling from products).

**How to build with MAPI — two tools, operation-based:**

Schema work goes through `entities` (operations: `list`, `create`, `update`, `delete`,
`schema`, `add_property`, `delete_property`). Data work goes through `records`
(operations: `list`, `get`, `create`, `update`, `delete`).
Property types: `varchar`, `text`, `int`, `datetime`, `tinyint`.

1. Define the entity:
   ```
   entities(operation: "create", project_id: 12345, entity_name: "services",
     properties: [
       { name: "title", type: "varchar", required: true },
       { name: "description", type: "text" },
       { name: "icon", type: "varchar" },
       { name: "price", type: "varchar" },
       { name: "sort_order", type: "int" }
     ],
     public_read: true
   )
   ```
   ⚠️ `public_read: true` makes the data **publicly readable** via
   `/mapi/public/{projectId}/{entity}` — use it only for content that belongs on the
   public site (menus, team, services). **Never** on personal or financial data
   (customers, orders, loyalty). See **Data Access Control** below.

2. Create records:
   ```
   records(operation: "create", project_id: 12345, entity_name: "services", data: {
     title: "Web Design", description: "...", icon: "🎨", price: "From €499", sort_order: 1
   })
   ```
   `records(operation: "update", ...)` is partial — only provided fields change.
   Add a column later with `entities(operation: "add_property", entity_name: "services",
   property_name: "badge", type: "varchar")`; inspect the schema with
   `entities(operation: "schema", entity_name: "services")`.

3. **Render with SSR (preferred — SEO-friendly):**

   Use `<!--#wps-mapi -->` template tags in your HTML. The platform renders entity data
   server-side before delivering the page, so search engines see full content immediately.

   ```html
   <!--#wps-mapi entity="services" sort="sort_order:asc" -->
   <div class="service-card">
     <span class="service-icon">{{icon}}</span>
     <h3>{{title}}</h3>
     <p>{{description | truncate:150}}</p>
     {{#if price}}
       <span class="price">{{price}}</span>
     {{/if}}
   </div>
   <!--#wps-mapi-empty -->
   <p>No services available yet.</p>
   <!--#/wps-mapi -->
   ```

   This is the **default choice** for rendering MAPI data. Always use SSR unless the page
   needs interactive features like client-side search, filtering, or live updates.

4. Render with JavaScript (only when interactivity is needed):

   Use client-side `fetch()` when the user needs to search, filter, or sort dynamically
   **in the browser**. SSR and JS can coexist on the same page.

   ```javascript
   fetch('https://api.websitepublisher.ai/mapi/public/{project_id}/services')
     .then(r => r.json())
     .then(data => {
       const container = document.getElementById('services-grid');
       data.data
         .sort((a, b) => (a.sort_order || 0) - (b.sort_order || 0))
         .forEach(service => {
           container.innerHTML += `
             <div class="service-card">
               <span class="service-icon">${service.icon}</span>
               <h3>${service.title}</h3>
               <p>${service.description}</p>
             </div>`;
         });
     });
   ```

### MAPI SSR — Template Reference

SSR uses Handlebars-inspired syntax processed server-side by the Optimizer.
The data is embedded directly in the HTML — no JavaScript needed, fully indexable by search engines.

#### Basic Syntax

```
{{field}}              → HTML-escaped output
{{{field}}}            → Raw output (for HTML content fields)
{{field | filter}}     → Apply a filter
{{field | filter:arg}} → Filter with argument
{{nested.field}}       → Dot notation for JSON fields
```

#### Tag Attributes

```html
<!--#wps-mapi
  entity="products"           Required: entity name
  sort="price:asc"            Optional: field:asc or field:desc
  limit="50"                  Optional: max records (default: 100, max: 500)
  offset="0"                  Optional: skip N records
  filter="category:shoes"     Optional: field:value pairs, ; separated
  wrap="div"                  Optional: wrapper element (default: div)
  wrap-class="product-grid"   Optional: CSS class on wrapper
-->
```

Multiple filters: `filter="category:shoes;in_stock:1;featured:1"`

#### Conditionals

```html
{{#if field}}
  Shown when field is truthy (not null, not empty, not 0)
{{#else}}
  Shown when field is falsy
{{/if}}

{{#unless field}}
  Shown when field is falsy (inverse of #if)
{{/unless}}
```

Comparison operators:
```html
{{#if price > 100}}         Greater than
{{#if stock == 0}}          Equals
{{#if status != "draft"}}   Not equals
{{#if rating >= 4}}         Greater or equal
{{#if category == "sale"}}  String comparison
```

#### Loop Metadata

Inside the `<!--#wps-mapi -->` block, these variables are available:

```
{{@index}}   → 0-based index
{{@number}}  → 1-based number
{{@first}}   → true if first item
{{@last}}    → true if last item
{{@count}}   → total items rendered
{{@even}}    → true if even index
{{@odd}}     → true if odd index
```

#### Nested Loops (array fields)

For JSON array fields within a record:

```html
{{#each images}}
  <img src="{{this}}" alt="Photo">
{{/each}}

{{#each specs}}
  <dt>{{this.label}}</dt>
  <dd>{{this.value}}</dd>
{{/each}}
```

#### Advanced Template Features

**Parent context in loops** — access fields from the outer record inside `#each`:
```html
{{#each images}}
  <img src="{{this}}" alt="{{../name}} photo {{@number}}">
{{/each}}
```

**Scope helper** — `#with` narrows the context to a nested object:
```html
{{#with address}}
  <p>{{street}}, {{city}} {{zip}}</p>
{{/with}}
```

**Repeat helper** — `#times` renders a block N times (useful for star ratings):
```html
{{#times 5}}<span class="star">★</span>{{/times}}
```

**Join helper** — concatenate array items with a separator:
```html
<p>Tags: {{#join tags ", "}}</p>
```

**Template comments** — invisible in rendered output:
```html
{{!-- This comment won't appear in the HTML --}}
```

**Literal escaping** — prevent template processing:
```html
\{{this will appear literally as curly braces\}}
```

**Empty attribute shorthand** — alternative to the `wps-mapi-empty` block:
```html
<!--#wps-mapi entity="products" empty="No products found." -->
<div>{{name}}</div>
<!--#/wps-mapi -->
```

#### Available Filters

| Filter | Example | Output |
|---|---|---|
| `truncate:N` | `{{text \| truncate:120}}` | Cuts at word boundary, adds "..." |
| `upper` | `{{name \| upper}}` | UPPERCASE |
| `lower` | `{{name \| lower}}` | lowercase |
| `capitalize` | `{{name \| capitalize}}` | First letter uppercase |
| `number:N` | `{{price \| number:2}}` | Formatted number (comma decimal, dot thousands) |
| `multiply:N` | `{{cents \| multiply:0.01}}` | Multiply value |
| `add:N` / `subtract:N` | `{{price \| add:5}}` | Arithmetic |
| `round:N` | `{{rating \| round:1}}` | Round to N decimals |
| `currency:CODE` | `{{price \| currency:EUR}}` | "€ 29,95" |
| `date:FORMAT` | `{{created_at \| date:d-m-Y}}` | Formatted date |
| `date:relative` | `{{created_at \| date:relative}}` | "2 dagen geleden" |
| `default:VALUE` | `{{bio \| default:No bio}}` | Fallback if empty |
| `striptags` | `{{html \| striptags}}` | Strip HTML tags |
| `nl2br` | `{{text \| nl2br}}` | Newlines to `<br>` tags |
| `slug` | `{{title \| slug}}` | URL-safe slug |
| `urlencode` | `{{query \| urlencode}}` | URL-encode value |
| `md5` | `{{email \| md5}}` | MD5 hash (useful for Gravatar URLs) |
| `json_pretty` | `{{data \| json_pretty}}` | Pretty-print JSON (debugging) |
| `count` / `length` | `{{items \| count}}` | Array/string length |

Filters can be chained: `{{price | multiply:0.01 | number:2}}`

#### Empty State

```html
<!--#wps-mapi entity="products" filter="category:sale" -->
<div class="product">{{name}} — {{price}}</div>
<!--#wps-mapi-empty -->
<p>No products on sale right now.</p>
<!--#/wps-mapi -->
```

#### Single Record Mode

Render one specific record by ID or field match:

```html
<!--#wps-mapi entity="products" record="42" match="id" -->
<h1>{{name}}</h1>
<p>{{description}}</p>
<!--#/wps-mapi -->
```

**URL-based slug matching** (live — via `_template.html` wildcard routing):
```html
<!--#wps-mapi entity="products" record=":slug" match="slug" -->
<h1>{{name}}</h1>
<p>{{{description}}}</p>
<!--#wps-mapi-empty -->
<p>Product not found.</p>
<!--#/wps-mapi -->
```
When a visitor opens `/products/wireless-headphones`, the Optimizer serves
`/products/_template.html` and resolves `:slug` to `wireless-headphones` for the
MAPI lookup. A non-existent slug falls into the `-empty` branch (serve a 404
status or a redirect there). `record=":slug"` always takes the **last URL
segment** as the match value.

#### Dynamic Routed Pages (detail + related list)

A routed page can match a **parent record** (a category, a branch, a "zebra"…)
and show a **related list** next to it that is filtered server-side on that
parent. Fully indexable, no client-side JS required. One page template, two
branches driven by routing (`source`, `entity`, `match="slug"` on the page):

- **match branch** (slug found) → the matched parent + its filtered list
- **empty branch** (no/unknown slug) → the overview (all items)

```html
<!--#wps-mapi entity="categories" source="catalog" record=":slug" match="slug" -->

  <!-- MATCH BRANCH: parent is top-level → {{name}}, {{slug}}, {{id}} -->
  <h1>{{name}}</h1>
  <div class="product-grid">
    <!--#wps-mapi entity="products" source="catalog"
        filter="status:active;category_slug:$route.slug" sort="name:asc" limit="500" -->
      <a class="product-card" href="/product/{{slug}}">{{name}}</a>
    <!--#wps-mapi-empty -->
      <p>No products in this category.</p>
    <!--#/wps-mapi -->
  </div>

<!--#wps-mapi-empty -->

  <!-- EMPTY BRANCH: the overview -->
  <h1>Our products</h1>
  <div class="product-grid">
    <!--#wps-mapi entity="products" source="catalog"
        filter="status:active" sort="name:asc" limit="500" -->
      <a class="product-card" href="/product/{{slug}}">{{name}}</a>
    <!--#/wps-mapi -->
  </div>

<!--#/wps-mapi -->
```

With `record=":slug"` the last URL segment is the match value:
`/products` → slug `products` (not found → empty branch = overview),
`/products/kliklijsten` → slug `kliklijsten` (match branch).

#### Dynamic Filter Tokens

The nested list can inject a value from the **parent / the URL** into its
`filter` via a server-side token. Tokens are resolved before the filter is
parsed — outside the template engine — so they are safe to use in `filter`
attributes (`{{...}}` braces are **not**, see below).

| Token | Resolves to | Notes |
|---|---|---|
| `$route.slug` | last URL segment | request-stable — **preferred** |
| `$route.N` | N-th URL segment (0-based) | request-stable |
| `$parent.<field>` | field from the router-matched record | generic, but **currently unreliable** inside a nested loop (the matched record may be `null` while the inner loop runs) — prefer `$route.slug` |

```html
filter="status:active;category_slug:$route.slug"
```

Unresolvable tokens fall back to `''` → the row simply doesn't match (safe
failure mode). No `$` token present → no-op.

**Hard rules (why no Handlebars in a filter):**

- **Never put `{{...}}` in a `filter` attribute.** `{{id}}` resolves empty in
  the nested scope; `{{../id}}` and `{{#if}}` get processed by the engine and
  corrupt the SSR comment delimiters → the empty branch leaks into the output.
  Use `$route.` / `$parent.` tokens instead of braces.
- **Never wrap an SSR loop in `{{#if}}`.** Same reason. Use the native
  match/empty branch split shown above.

**Prerequisite — filterable field must be top-level.** Filters only match
top-level keys. To filter products on category slug, the catalog normalizer must
expose `category_slug` top-level on each product (it does for `source=catalog`).
A field that only exists nested (e.g. `category.slug`) is not filterable.

#### Per-Record SEO — `<!--#wps-seo -->` (routed detail pages)

On a **routed detail page** (`_template.html` / `record=":slug"`), every record would
otherwise share the same page-level `<title>` and description — a go-live SEO blocker
(duplicate titles). The `<!--#wps-seo -->` tag injects per-record SEO **server-side**
into the `<head>`: `<title>`, meta description, Open Graph, and JSON-LD — before any
crawler sees the page, no JavaScript involved. One tag per page. Works for both
`source="catalog"` and plain MAPI entities (no `source` attribute).

```html
<!--#wps-seo source="catalog" entity="products" record=":slug" match="slug"
     title="{{name}} — Site Name"
     description="{{short_description | striptags | truncate:160}}" -->
  <meta property="og:type" content="product">
  <meta property="og:title" content="{{name}} — Site Name">
  <meta property="og:description" content="{{short_description | striptags | truncate:160}}">
  {{#each images}}{{#if @first}}<meta property="og:image" content="{{this}}">{{/if}}{{/each}}
  <script type="application/ld+json">{"@context":"https://schema.org","@type":"Product","name":"{{name}}","sku":"{{sku}}"{{#each images}}{{#if @first}},"image":"{{this}}"{{/if}}{{/each}}}</script>
<!--#/wps-seo -->
```

**Attributes** (on the open tag): `source` / `entity` / `match` work as in `wps-mapi`
(the tag is self-describing — it does not inherit route context). `record` accepts
`:slug` (last URL segment), `:N` (N-th segment), or a literal value.
`title` and `description` go **as attributes** and may contain template tokens.

**Critical rule — title/description are ATTRIBUTES, never elements.** Do not put a
`<title>` or description `<meta>` element inside the block: the platform strips the
first `<title>` unconditionally during SEO processing, so an inline element gets
clobbered before your override runs. Attributes for title/description; all other
head-HTML (OG, JSON-LD) goes in the block body.

**Behavior:**
- No `<!--#wps-seo` tag on the page → output is byte-identical (safe everywhere)
- Strips the page-level duplicates it overrides (title, description, og:title,
  og:description) and places the per-record versions authoritatively in `<head>`
- Record not found → the block disappears; the page falls back to page-level SEO

**Caveats:**
- The template engine HTML-escapes `{{ }}` — JSON-LD string values containing `&` or
  `"` come out entity-encoded (valid JSON, cosmetically off). Keep JSON-LD fields to
  safe data: name, sku, image URL.
- Price/`offers` in JSON-LD is deliberately **not** included by default — whether
  prices appear in Google (incl./excl. VAT, variable pricing) is the site owner's call.
- Test SSR on the `*.websitepublisher.ai` **preview domain** — an uninitialized
  placeholder page on a custom domain may serve fallback content instead of the
  SSR pipeline.

#### SSR Wrapper Attributes

The SSR injector adds `data-mapi-ssr` attributes to rendered blocks:

```html
<div data-mapi-ssr="products" data-mapi-count="12">
  <!-- rendered product cards -->
</div>
```

JavaScript can use these to enhance SSR-rendered content (e.g. add client-side
search/filter on top of the server-rendered list). SSR and JS coexist naturally.

**CSS gotcha (always needed for an SSR list inside grid/flex).** Each SSR loop
renders inside its `<div data-mapi-ssr="…">` wrapper. A grid/flex container
around the loop then has only **one** child → one column. Fix:

```css
[data-mapi-ssr] { display: contents; }
```

#### Complete Examples

**Product grid (webshop):**
```html
<!--#wps-mapi entity="products" sort="name:asc" filter="active:1" -->
<div class="product-card {{#if featured}}featured{{/if}}">
  <a href="/products/{{slug}}">
    <img src="{{image | default:https://placehold.co/400x300}}" alt="{{name}}">
    <h3>{{name}}</h3>
    <p>{{description | truncate:100}}</p>
    {{#if sale_price}}
      <span class="original">{{price | multiply:0.01 | currency:EUR}}</span>
      <span class="sale">{{sale_price | multiply:0.01 | currency:EUR}}</span>
    {{#else}}
      <span class="price">{{price | multiply:0.01 | currency:EUR}}</span>
    {{/if}}
  </a>
</div>
<!--#/wps-mapi -->
```

**Blog post list:**
```html
<!--#wps-mapi entity="posts" sort="published_at:desc" limit="10" filter="status:published" -->
<article>
  <time>{{published_at | date:d M Y}}</time>
  <h2><a href="/blog/{{slug}}">{{title}}</a></h2>
  <p>{{content | striptags | truncate:200}}</p>
  {{#if author}}<span>By {{author}}</span>{{/if}}
</article>
<!--#/wps-mapi -->
```

**Team page:**
```html
<!--#wps-mapi entity="team" sort="sort_order:asc" -->
<div class="team-member">
   <img src="{{photo | default:https://placehold.co/300x300}}" alt="{{name}}">
   <h3>{{name}}</h3>
   <p class="role">{{role}}</p>
   {{#if bio}}<p>{{bio | truncate:200}}</p>{{/if}}
</div>
<!--#/wps-mapi -->
```

### When to use SSR vs JavaScript vs Static HTML

| Scenario | Use | Why |
|---|---|---|
| Product catalog (10+ items, public) | **SSR** | SEO, owner adds products via admin |
| Blog, portfolio grid, FAQ (growing) | **SSR** | SEO, content changes independently |
| 3 services on about page | **Static HTML** | Too few items, rarely changes |
| 4 team members, small company | **Static HTML** | AI updates faster than building MAPI+SSR |
| Client-side search/filter | **JS** | User interaction required |
| Live price updates, stock status | **JS** | Real-time data needed |
| Shopping cart, wishlist | **JS** | User-specific state |
| Product list WITH search bar | **SSR + JS** | SSR for initial load + SEO, JS for interaction |
| Admin dashboard tables | **JS only** | No SEO needed, always behind login |

**Decision flow:**
1. Will Google need to index this content? → Consider SSR
2. Will the content grow beyond 10 items? → Consider MAPI entity
3. Does the owner need to update without AI? → MAPI + admin panel
4. Is it ≤5 fixed items on one page? → **Static HTML is fine**
5. Does the user interact with it? → Add JS (on top of SSR if SEO matters)

SSR and JS can coexist — use SSR for the initial server-rendered content and JS
for interactive enhancement on top.

### Data Access Control — `public_read` vs `policy_json`

Two different switches control who can touch entity data. Confusing them creates
real data leaks — this exact mistake has exposed full customer databases in the wild.

**`public_read` is a VISIBILITY flag, not a security control.**
Setting `public_read: true` only enables anonymous read via
`/mapi/public/{projectId}/{entity}`. It does **not** protect the entity and does
**not** restrict writes. It has exactly one job: making public-site content
(menus, team, services, blog posts) readable without auth.

**`policy_json` is the access control.** An entity is access-controlled **only if
it carries an explicit `policy_json`** (set via `entities(operation: "update",
entity_name: ..., policy_json: {...})`). The policy defines per-action rules and
an `owner_field` for row-level scoping.

Rules that follow from this:

- **Sensitive data (customers, orders, loyalty accounts, anything with PII or
  money) must NEVER rely on `public_read` for protection.** Give those entities a
  `policy_json`, or keep `public_read: false` and access them only via owner-level
  calls or a dedicated integration.
- **Visitor-scoped entities** (each logged-in visitor sees/edits only their OWN
  rows) need two things: a `policy_json` on the entity **and** a real owner column
  (e.g. `owner_email`) that exists as an actual entity property. The policy's
  `owner_field` must map to a real column — the engine fails closed otherwise.
- **A denied write surfaces as HTTP `404 Not found` — not `403`.** This is by
  design (no existence leak). If a legitimate-looking write returns 404, check the
  caller identity and the entity policy first, not the record.
- **Admin panels need no extra wiring.** The platform data-grid and `wsa_` admin
  sessions run with owner authority over the site — admin CRUD works on
  policy-protected entities automatically.
- Get the exact policy shape from `get_skill(skill_name: "dev")` before setting
  `policy_json` on an entity with real user data — the server validates the JSON
  is well-formed, not that your rules are semantically correct.
- Access control is currently **opt-in** (only entities with an explicit
  `policy_json` are enforced). Strict mode is the platform's end state — design
  entities with explicit policies **now** so nothing breaks later.

**Visitor "My Account" / "My Orders" pages — supported pattern:**
The e-commerce order endpoints `list-orders` and `get-order` are callable from a
**verified SAPI visitor session**. The server scopes results to the session email
automatically: a visitor sees only their own orders, a client-supplied
`customer_email` filter is ignored, and a cross-customer `get-order` returns 404.
Build the page with the SAPI client (visitor auth section below) and call these
endpoints from the visitor session — no admin token, no custom filtering, no
workarounds. All other order endpoints (`create-order`, `update-status`,
`get-order-by-payment`, line-meta) remain owner-only.

---

## Contact Forms (SAPI) — Critical Pattern

**Always follow this exact pattern.** Deviating from it will cause "no valid session" errors,
especially on Safari and custom domains where third-party cookies are blocked.

### Step 1 — Configure the form (server-side, via MCP tool)

```
configure_form(
  project_id: 12345,
  form_name: "contact",
  required_fields: ["name", "email", "message"],
  action: {
    type: "iapi",
    service: "resend",
    endpoint: "send-email",
    input_template: {
      from: "noreply@websitepublisher.ai",
      to: "owner@example.com",
      subject: "New contact from {{fields.name}}",
      html: "<p>From: {{fields.name}} ({{fields.email}})</p><p>{{fields.message}}</p>"
    }
  },
  max_submits_per_session: 5
)
```

### Step 2 — Add the CDN script + form handler to the page

**Always use the CDN library.** Do not write inline session management code.
The library handles sessions, CSRF tokens, stale session recovery, and all headers automatically.

> ⚠️ **`WP.sapi()` is for visitor-facing forms only** — contact forms, file uploads,
> member-area magic links. **Do not use it for admin authentication.** Admin login and
> admin-only IAPI calls use direct `fetch()` to `/iapi/project/{id}/admin-auth/...` with
> `Authorization: Bearer` headers — see the **Admin-Protected Pages** section below.

```html
<script src="https://cdn.websitepublisher.ai/js/sapi-client.js"></script>
<script>
   var sapi = WP.sapi(PROJECT_ID);

   document.getElementById('my-form').addEventListener('submit', function(e) {
      e.preventDefault();
      var btn = this.querySelector('button[type="submit"]');
      btn.disabled = true;
      btn.textContent = 'Sending...';

      sapi.submitForm('contact', {
         name:    document.getElementById('name').value.trim(),
         email:   document.getElementById('email').value.trim(),
         message: document.getElementById('message').value.trim(),
         website: '',  // honeypot: leave empty, bots fill this in
      }).then(function(r) {
         if (r.ok) {
            window.location.href = '/thank-you';
         } else {
            btn.disabled = false;
            btn.textContent = 'Send';
            alert(r.data.error && r.data.error.message || 'Something went wrong.');
         }
      });
   });
</script>
```

### What the CDN library handles for you

| Feature | How |
|---|---|
| Session creation + resume | `WP.sapi(PROJECT_ID)` pre-warms on init |
| CSRF token management | Sent via `X-CSRF-Token` header + `_csrf` body (dual) |
| Session ID header | `X-Session-Id` header on every request |
| Stale session recovery | 401 response -> auto-clear -> fresh session -> retry (max 1) |
| Per-project storage keys | `wp_{projectId}_sid` -- no cross-site conflicts |
| Safari ITP compatibility | Uses sessionStorage (first-party, never blocked) |
| Auth state preservation | After successful POST, only CSRF is cleared -- session ID survives |

### Key rules -- never forget these:

| Rule | Why |
|---|---|
| Always include `website: ''` in the fields object | Honeypot field -- bots fill it in, humans leave it empty. Server silently drops the submission if non-empty |
| Never pre-fill the honeypot field | An empty string is required -- any value triggers bot detection |
| Replace `PROJECT_ID` with the actual numeric project ID | The library uses this to scope sessions and build API URLs |

### Forms with File Upload

Forms can accept image uploads from visitors via the SAPI upload endpoint.
Uploads are stored as project assets on the CDN -- no bearer token needed.

> **Building an admin panel with image upload?** See "Image Upload in Admin Panels"
> under the Admin-Protected Pages section — it shows how to combine admin auth
> with SAPI upload on the same page.

**Flow:** upload file(s) first -> collect CDN URLs -> include in form submit fields.

```javascript
// Upload a file using the CDN library
var sapi = WP.sapi(PROJECT_ID);

async function uploadFile(file) {
   // getSession() handles caching + resume automatically
   var session = await sapi.getSession();

   var form = new FormData();
   form.append('file', file);
   form.append('_csrf', session.csrf_token);
   form.append('form_name', 'intake');

   var res = await fetch(
           'https://api.websitepublisher.ai/sapi/project/' + PROJECT_ID + '/form/upload',
           {
              method: 'POST',
              headers: { 'X-Session-Id': session.session_id },
              body: form   // no Content-Type header -- browser sets multipart boundary
           }
   );

   var data = await res.json();
   if (data.success) {
      // Clear stored CSRF -- the library will fetch a fresh one on next call
      sapi.clearSession();
      return data.data.asset_url;   // CDN URL ready for use
   }
   throw new Error(data.error && data.error.message || 'Upload failed');
}
```

**Upload rules:**

| Rule | Value |
|---|---|
| Allowed types | JPEG, PNG, WebP only |
| Max file size | 5 MB per file |
| Max per session | 10 uploads |
| CSRF | Single-use -- library handles refresh automatically for submitForm(), manual clear needed after raw fetch upload |
| Response includes | `asset_url`, `filename`, `mime_type`, `size`, `width`, `height`, `uploads_remaining` |

**Include uploaded URLs in form submit:**
```javascript
// After uploading, pass CDN URLs as regular form fields
sapi.submitForm('intake', {
   name: '...',
   email: '...',
   image_url_1: uploadedUrl1,  // CDN URL from upload response
   image_url_2: uploadedUrl2,
   website: '',  // honeypot
});
```

---

## Step 4 — Go Live Checklist

Before handing over to the user, verify:

- [ ] Homepage has `landingpage: true` (or was created first)
- [ ] All pages that should be findable have `seo_robots_index: true`
- [ ] All pages have `seo_title` and `seo_description`
- [ ] All `<!-- Optimizer - ... -->` comment tags are present in every page
- [ ] Multi-page sites use **fragments** for header and footer (not copy-pasted HTML)
- [ ] Repeating content uses **MAPI entities** (not hardcoded static HTML)
- [ ] Contact form (if any) uses the CDN library (`sapi-client.js`) — no inline session code
- [ ] Thank-you page exists if form redirects after submit
- [ ] Terms / privacy page exists if form collects personal data
- [ ] Design uses distinctive typography and cohesive color palette (not generic AI defaults)
- [ ] Design context saved via `execute_integration(service: "site_context")` for future consistency
- [ ] Website URL shared with user: `https://{subdomain}.websitepublisher.ai`
- [ ] Contact form includes `website: ''` honeypot field in the fields object
- [ ] Visual Editor session offered for image replacement and final tweaks

### Mandatory Security Review (before going live)

A site must **not** be presented as live until this review passes. Run it as the
final gate — never skip it, even for a quick demo that the user intends to keep.

- [ ] **No secrets in client code.** No API keys, tokens, or passwords in page HTML,
      inline JS, or assets. All credentials use `{{vault:...}}` references —
      resolved server-side, never delivered to the browser.
- [ ] **Admin pages are auth-guarded.** Every admin/dashboard page enforces the
      IAPI Admin Auth guard server-side. No admin-only data or actions reachable
      without a valid `wsa_` session. No client-side-only "hidden" protection.
- [ ] **Entity exposure is intentional.** `public_read` is enabled only on entities
      meant to be public. No personal data, leads, orders, or admin records exposed
      via public MAPI endpoints. Remember: `public_read` is a visibility flag, not
      protection — sensitive entities carry a `policy_json` or stay
      `public_read: false` (see **Data Access Control**).
- [ ] **Money math is server-side.** Checkout totals, discounts, tier/volume pricing,
      and loyalty points are computed and validated **by the platform integrations** —
      never trusted from client-side JS, `localStorage`, or hidden form fields. A
      visitor must not be able to change what they pay or what they earn by editing
      the page. (Real exploits found pre-go-live: client-computed order totals and
      client-written loyalty points.)
- [ ] **Admin is protected server-side.** No `showAdmin()`-style JS toggles, hidden
      DOM, or devtools-bypassable checks as the only barrier — every admin page and
      admin data call enforces the `wsa_` auth guard server-side.
- [ ] **No sensitive files on the public CDN.** Exports, snapshots, or data files
      containing customer/order data are served through an authenticated route
      (admin auth / asset proxy), never as a world-readable CDN asset.
- [ ] **Form input is validated.** Required fields set, honeypot present, file
      uploads (if any) restricted to expected types/sizes via SAPI upload.
- [ ] **No customer-supplied HTML rendered unescaped.** Visitor/lead/form data shown
      back on a page is escaped — no raw injection into the DOM.
- [ ] **Legal pages present where required.** Terms / privacy page exists whenever the
      site collects personal data (forms, auth, leads).

If any item fails, fix it before declaring the site live. Log the outcome of this
review in TAPI (`add_task_history`) so the security gate is traceable per project.

---

## Platform Knowledge

### What WebsitePublisher handles automatically

| Feature | How it works |
|---|---|
| **Sitemap** | Auto-generated. Pages appear when `seo_robots_index: true` |
| **robots.txt** | Auto-generated with "Allow all" + sitemap reference |
| **SSL certificate** | Auto-provisioned via Let's Encrypt on custom domains |
| **Canonical tags** | Injected by Optimizer when comment tag is present |
| **Open Graph** | Injected by Optimizer (uses SEO title/description) |
| **Static caching** | Pages are served as static files — extremely fast |
| **CDN** | Assets served via cdn.websitepublisher.ai |

### What requires API calls

| Feature | API |
|---|---|
| Pages and content | PAPI |
| Reusable components (header, footer) | PAPI Fragments |
| Dynamic data / entities | MAPI |
| Contact forms | SAPI |
| Third-party integrations | IAPI + VAPI |
| Visual editing (browser) | WPE |
| Clone a website | WAPI clone endpoint |

---

## Built-in Integrations — Composable Building Blocks

WebsitePublisher's integrations are not a feature list — they are composable building
blocks. Every integration speaks the same interface
(`execute_integration(service, endpoint, input)`), authenticates the same way (the Vault),
and is callable from any AI on any platform via MCP. This means the AI doesn't *build* a
payment flow, an email pipeline, or a lead system — it *assembles* them from pieces that
are already wired, secured, and maintained. Generating code gives you a draft; snapping
integrations together gives you a working system.

### Don't reinvent the wheel

WebsitePublisher includes pre-built integrations for common website needs.
You do not need to build email sending, payment processing, or SMS from scratch.
Each integration is a single tool call — credentials are stored securely in the Vault,
the platform handles authentication, rate limiting, and error handling.

### Discover what's available — list it, don't guess

You never have to guess which integrations or endpoints exist. Two tools read the
**live manifest** for the current project — they are the source of truth, more current
than this document:

- `list_integrations(project_id)` — every integration, split into **configured** (vault
  secrets present, ready to call now) and **available** (needs setup), each with its full
  endpoint list and descriptions. A typical project already has dozens wired
  (asset upload, exports, payments, email, shipping, imports, analytics, and more).
- `get_integration_schema(project_id, service)` — the exact input fields (name, required,
  type, limits) for every endpoint of one integration. Call this before
  `execute_integration` so you send the correct body the first time.

If a task seems to need a capability you have no tool for, run `list_integrations` **first**.
The endpoint almost always already exists. Inventing an HTTP route, guessing a hostname,
or asking the user to build an endpoint is the wrong move — the manifest already tells you
what is there and how to call it.

### Available Integrations

| Service | Category | What it does | Tool call |
|---|---|---|---|
| **Resend** | Email | Transactional emails (contact forms, notifications) | `execute_integration(service: "resend", endpoint: "send-email")` |
| **Mailgun** | Email | Domain-level email sending | `execute_integration(service: "mailgun", endpoint: "send-email")` |
| **SendGrid** | Email | High-volume email delivery | `execute_integration(service: "sendgrid", endpoint: "send-email")` |
| **Stripe** | Payments | Checkout sessions, payment processing | `execute_integration(service: "stripe", endpoint: "create-checkout-session")` |
| **Mollie** | Payments | European payments (iDEAL, Bancontact, cards) | `execute_integration(service: "mollie", endpoint: "create-payment")` |
| **Twilio** | SMS | Text messages (confirmations, alerts) | `execute_integration(service: "twilio", endpoint: "send-sms")` |
| **Lead Capture** | Built-in | Store form submissions as leads | Form action `{"type": "leads"}` |
| **Admin Auth** | Built-in | Password-protected admin areas (email/password login, Bearer token auth) | `execute_integration(service: "admin_auth", endpoint: "login")` |
| **Auth Keys** | Built-in | Request project API keys stored in vault (human-approved) | `execute_integration(service: "auth_keys", endpoint: "request-key")` |
| **Asset Proxy** | Built-in | Upload/delete assets from browser admin panels (no WPA key needed) | `execute_integration(service: "asset-proxy", endpoint: "upload")` |
| **Site Context** | Built-in | Store design tokens (colors, fonts, style, locale) across sessions | `execute_integration(service: "site_context", endpoint: "set-context")` |
| **Product Catalog** | Built-in | Products, variants, categories, bulk import | `execute_integration(service: "product-catalog", endpoint: "list-products")` |
| **Request Tracer** | Built-in | Debug API + page requests in real-time | `execute_integration(service: "tracer", endpoint: "start")` |
| **Capability Requests** | Built-in | Report a genuine platform gap (LAST RESORT — see "You Are the Builder") | `execute_integration(service: "capability_requests", endpoint: "submit-request")` |

### How integrations work

1. **Setup** — Store the API key: `setup_integration(service: "resend", secrets: {"resend_api_key": "re_..."})`
2. **Use** — Call the integration: `execute_integration(service: "resend", endpoint: "send-email", input: {...})`
3. **Done** — The platform resolves credentials, validates input, proxies the request, returns the result

API keys are **never exposed** to the AI or the browser. The Vault encrypts them at rest
and the integration proxy resolves them server-side at execution time.

### Vault References — `{{vault:...}}`

> Written with `...` as placeholder throughout this document: examples containing a
> literal key-shaped reference are redacted by the platform's secret filter when this
> skill is delivered via `get_skill`. In real templates and integration inputs, write
> the actual key name — no spaces, no dots: two opening braces, `vault:your_key_name`,
> two closing braces.

The IAPI proxy resolves `{{vault:...}}` references (two opening braces, then `vault:` + your key name, then two closing braces — no spaces) server-side before making API calls.
This is the core security mechanism that keeps secrets out of AI conversations and browser code.

**Where vault references work (server-side only):**

| Context | Works? | Example |
|---|---|---|
| `execute_integration` input | ✅ | `"api_key": "{{vault:...}}"` (e.g. key `stripe_key`) |
| Scheduled tasks (AAPI) | ✅ | Vault refs in task payload resolved at execution |
| IAPI proxy calls | ✅ | Bearer token from vault |
| Browser JavaScript | ❌ | Browser cannot access vault — use admin auth (`wsa_`) instead |
| Page HTML source | ❌ | Would expose secrets to anyone viewing source |
| MCP tool responses | ❌ | VaultSanitizer strips any leaked vault values |

**Critical rule:** Never put vault keys in browser-facing code. If a browser page needs
to call an authenticated API, use the **admin auth pattern** (`wsa_` token) for data
operations and **SAPI upload** for file uploads. The vault exists for server-side
integrations only.

### When to use integrations

| User wants... | Use this |
|---|---|
| Contact form that sends email | SAPI form + Resend integration |
| Accept payments on website | Stripe or Mollie integration |
| SMS confirmation after booking | Twilio integration |
| Store leads from multiple forms | Built-in Lead Capture |
| Password-protected admin dashboard | Admin Auth (IAPI admin session) |
| Member area with magic link / code login | SAPI Visitor Auth |
| Remember design choices across sessions | Site Context integration |
| Import 50-500 products at once | `bulk-upsert-products` (Product Catalog) |
| Upload images from admin panel (browser) | **Asset Proxy** (PAPI assets) or **SAPI upload** (form uploads) |
| Request a project API key securely | Auth Keys (human-approved, vault-stored) |
| Debug failing requests or slow pages | Request Tracer |

**Always check if an integration exists before building custom solutions.**
The built-in integrations handle authentication, error handling, rate limiting,
and security — reimplementing these is unnecessary and error-prone.

### Bulk Product Import

For large catalogs, use `bulk-upsert-products` instead of looping `create-product`:

```
execute_integration(
  service: "product-catalog",
  endpoint: "bulk-upsert-products",
  input: {
    "items": [
      {"sku": "TSH-001", "name": "Classic Tee", "price_cents": 2999, "status": "active"},
      {"sku": "TSH-002", "name": "V-Neck Tee", "price_cents": 3499, "status": "active"},
      {"sku": "TSH-001", "price_cents": 2799}
    ]
  }
)
```

Each item is matched by SKU: existing → update, new → create (needs `name` + `price_cents`).
Max 500 items per call. Response includes per-item status and `summary.by_error_type`.

**Always check `result.failed` and `result.summary.by_error_type`** — `success: true`
means the call itself worked, not that every item succeeded.

### Debugging with Request Tracer

When something isn't working — a page returns wrong data, an integration fails,
or performance is slow — use the Request Tracer to see exactly what happened:

1. **Start a trace session:**
   ```
   execute_integration(
     service: "tracer",
     endpoint: "start",
     input: { "ttl": 120, "include_optimizer": true }
   )
   → returns hash (e.g., "tr_abc12345")
   ```

2. **Perform the operation that's failing** — create a page, submit a form, call an integration

3. **Read the trace:**
   ```
   execute_integration(
     service: "tracer",
     endpoint: "logs",
     input: { "hash": "tr_abc12345" }
   )
   ```

The trace shows every API request and page render with HTTP method, path, status
code, duration, SQL query summary, and which server handled the request.

Integration failures include typed error data (`error_type`, `error_code`, and
`error_field` / `recovery` when applicable) so you can see exactly what went
wrong without guessing.

**When to use the tracer:**
- Page renders wrong content → trace optimizer request, check SQL queries
- Integration call fails → trace API request, check `error_type` and `recovery`
- Request is slow → check `duration_ms` and `db.total_ms` breakdown
- "It works sometimes" → `server` field shows which node handled each request

**Options:**
- `include_optimizer: true` — also trace public page renders (default: off)
- `include_sql: false` — skip SQL summary (default: on)
- `ttl: 10-300` — session duration in seconds (default: 60)

---

## Admin-Protected Pages — IAPI Admin Auth

> **⚠️ Need to upload images from an admin panel?** Do NOT use `upload_asset`,
> vault keys, or MAPI asset routes from the browser. Use **Asset Proxy**
> (`/iapi/project/{id}/asset-proxy/upload` with your `wsa_` admin token) — it's
> the simplest option. See "Image Upload in Admin Panels" below.

When building dashboards, admin panels, or any page that requires a logged-in admin
(not a public visitor), use the IAPI Admin Auth pattern. This is separate from
SAPI Visitor Auth — they serve different purposes.

| Feature | Admin Auth (IAPI) | Visitor Auth (SAPI) |
|---|---|---|
| **Use case** | Admin dashboards, CMS, internal tools | Member areas, gated content, loyalty portals |
| **Login method** | Email + password | Magic link or verification code |
| **Token storage** | `sessionStorage.admin_token` | Managed by sapi-client.js internally |
| **API calls** | Direct `fetch()` to `/iapi/project/{id}/...` with `Authorization: Bearer` | `WP.sapi(id).call(...)` via CDN library |
| **Token prefix** | `wsa_` (server-side) | Session ID (no token exposed to page) |

### Admin Login

```javascript
const PROJECT_ID = 12345; // replace with actual project ID

async function login(email, password) {
   const r = await fetch(`/iapi/project/${PROJECT_ID}/admin-auth/login`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({email, password})
   });
   const data = await r.json();
   if (data.success && data.token) {
      sessionStorage.setItem('admin_token', data.token);
      localStorage.setItem('admin_token', data.token);
      document.cookie = `admin_token=${data.token}; path=/; max-age=28800; SameSite=Lax`;
   }
   return data;
}
```

Triple storage (sessionStorage + localStorage + cookie) ensures the token survives
page navigations, tab reopens, and server-side middleware checks.

After login, redirect to **`/`** if your dashboard page is set as `landingpage: true`.
See the note about `landingpage` under Page Metadata.

### Admin-Only IAPI Calls

```javascript
async function callAdmin(service, endpoint, payload) {
   const token = sessionStorage.getItem('admin_token');
   if (!token) { window.location.replace('/login'); return; }

   const r = await fetch(`/iapi/project/${PROJECT_ID}/${service}/${endpoint}`, {
      method: 'POST',
      headers: {
         'Content-Type': 'application/json',
         'Authorization': 'Bearer ' + token
      },
      body: JSON.stringify(payload)
   });

   if (r.status === 401) {
      sessionStorage.removeItem('admin_token');
      localStorage.removeItem('admin_token');
      window.location.replace('/login');
      return;
   }
   return r.json();
}

// Usage:
const leads = await callAdmin('leads', 'get-leads', { page: 1, per_page: 25 });
const msg   = await callAdmin('anthropic', 'create-message', { prompt: '...' });
```

**Important:** Use direct `fetch()` — not `WP.sapi().call()`. The SAPI client library
is for visitor sessions. Admin calls use `Authorization: Bearer` headers on `/iapi/` routes.

### Page Rendering — Auth Guard

```html
<body>
<script>
   // Immediate redirect — no hidden body, no async check
   var token = sessionStorage.getItem('admin_token')
           || localStorage.getItem('admin_token');
   if (!token) window.location.replace('/login');
</script>

<!-- page content renders immediately for authenticated users -->
<h1>Dashboard</h1>
<!-- ... -->
</body>
```

**Never do this:**
```html
<!-- ❌ FORBIDDEN — causes flash of invisible content, breaks on slow connections -->
<body style="visibility:hidden">
<script>
   checkAuth().then(() => document.body.style.visibility = 'visible');
</script>
```

The correct pattern is: redirect immediately if no token, render normally if token exists.
Auth validation happens on the first API call — if the token is expired, the 401 handler
clears storage and redirects to login.

### Logout

```javascript
function logout() {
   sessionStorage.removeItem('admin_token');
   localStorage.removeItem('admin_token');
   document.cookie = 'admin_token=; path=/; max-age=0';
   window.location.replace('/login');
}
```

### Creating Admin Users

Admin users are created via the Admin Auth integration:

```
execute_integration(
  project_id: 12345,
  service: "admin_auth",
  endpoint: "create_user",
  input: { email: "admin@example.com", password: "securepassword" }
)
```

The `create_user` endpoint accepts only `email` and `password` — no name field.
The email serves as the unique identifier and login credential.

### Decision Tree — Which Auth System?

```
Does the page need login?
├── No → No auth needed (public page)
└── Yes
    ├── Is the user an admin/owner managing content?
    │   └── Use Admin Auth (IAPI) — this section
    └── Is the user a visitor/member accessing gated content?
        └── Use Visitor Auth (SAPI) — see "Contact Forms (SAPI)" section
```

### Common Pitfalls — Why Admin Auth Has Its Own Pattern

Multiple AI builds have walked into the same trap: trying to call admin endpoints
via the SAPI execute route (`WP.sapi().call('/execute/admin_auth/login', ...)`).
That path requires a visitor session bootstrap and CSRF tokens — machinery the SAPI
library wraps for visitor forms but that does not align with how admin auth issues
and validates `wsa_` Bearer tokens.

**The canonical admin auth path is always:**

| Step | Call | Auth header |
|------|------|------------|
| 1. Login | `POST /iapi/project/{id}/admin-auth/login` | None — body has email + password |
| 2. Store token | sessionStorage + localStorage + cookie | — |
| 3. Authenticated calls | `POST /iapi/project/{id}/{service}/{endpoint}` | `Authorization: Bearer wsa_...` |
| 4. Verify on page load | `POST /iapi/project/{id}/admin-auth/verify` | None — body has token |
| 5. Logout | `POST /iapi/project/{id}/admin-auth/logout` | None — body has token |

**Anti-patterns — never do these for admin auth:**

- ❌ `WP.sapi().call('/execute/admin_auth/login', ...)` — that route is for visitor SAPI flows
- ❌ Manual `GET /sapi/session` + `X-CSRF-Token` headers — admin auth doesn't use the SAPI session layer
- ❌ Reading the token from `r.data.token` after a SAPI execute call — wrong envelope shape
- ❌ `<body style="visibility:hidden">` while running an async auth check — see Page Rendering above
- ❌ URL with underscore for login/verify/logout: `/iapi/project/{id}/admin_auth/login` — those specific routes are `admin-auth` (hyphen)

The IAPI route is fully self-contained: no session, no CSRF, just `Authorization: Bearer`
on the request. If you find yourself adding session bootstrap or CSRF token logic to an
admin page, stop — you've taken the wrong turn.

### Image Upload in Admin Panels

Admin panels often need image upload — for portfolio management, product photos, team
pictures, or any content the admin manages visually.

There are two approaches. **Asset Proxy** stores files in the PAPI asset system (visible
in `list_assets`, manageable). **SAPI upload** stores files in the form uploads bucket.
Both return CDN URLs. Choose based on whether you need the files in the project's asset system.

#### Option A — Asset Proxy (recommended for admin panels)

Uses the admin's existing `wsa_` token. No extra setup needed — no SAPI form, no CDN script.
Files go into the PAPI asset system.

```javascript
const PROJECT_ID = 12345;

function getAdminToken() {
  return sessionStorage.getItem('admin_token');
}

// Convert file to base64
function fileToBase64(file) {
  return new Promise(function(resolve, reject) {
    var reader = new FileReader();
    reader.onload = function() { resolve(reader.result.split(',')[1]); };
    reader.onerror = reject;
    reader.readAsDataURL(file);
  });
}

// Upload via asset-proxy (uses admin token, no WPA key needed)
async function uploadImage(file, slug) {
  var base64 = await fileToBase64(file);

  var res = await fetch('/iapi/project/' + PROJECT_ID + '/asset-proxy/upload', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + getAdminToken()
    },
    body: JSON.stringify({
      slug: slug,          // e.g. "images/product-42.jpg"
      base64: base64,
      overwrite: true
    })
  });

  if (res.status === 401) { window.location.replace('/login'); return; }
  var data = await res.json();
  if (data.success) {
    return data.asset_url;  // CDN URL: cdn.websitepublisher.ai/custom/wid.../images/...
  }
  throw new Error(data.message || 'Upload failed');
}

// Combined: upload image, then save product
document.getElementById('product-form').addEventListener('submit', async function(e) {
  e.preventDefault();
  var file = document.getElementById('photo').files[0];
  var name = document.getElementById('name').value;
  var slug = 'images/product-' + Date.now() + '.' + file.name.split('.').pop();

  var imageUrl = file ? await uploadImage(file, slug) : null;
  await saveProduct(name, imageUrl);  // IAPI call with wsa_ token (see Admin-Only IAPI Calls)
});
```

#### Option B — SAPI Upload (alternative, requires form setup)

```javascript
const PROJECT_ID = 12345;
var sapi = WP.sapi(PROJECT_ID);  // SAPI session for uploads

// Admin is logged in — wsa_ token in sessionStorage (see Admin Login above)
function getAdminToken() {
  return sessionStorage.getItem('admin_token');
}

// Image upload — uses SAPI (no admin token needed)
async function uploadImage(file) {
  var session = await sapi.getSession();
  var form = new FormData();
  form.append('file', file);
  form.append('_csrf', session.csrf_token);
  form.append('form_name', 'admin_upload');

  var res = await fetch(
    'https://api.websitepublisher.ai/sapi/project/' + PROJECT_ID + '/form/upload',
    {
      method: 'POST',
      headers: { 'X-Session-Id': session.session_id },
      body: form
    }
  );

  var data = await res.json();
  if (data.success) {
    sapi.clearSession();  // CSRF is single-use
    return data.data.asset_url;  // CDN URL: cdn.websitepublisher.ai/custom/wid.../images/...
  }
  throw new Error(data.error?.message || 'Upload failed');
}

// Save data with image URL — uses admin auth (wsa_ token)
async function saveProduct(name, imageUrl) {
  var res = await fetch('/iapi/project/' + PROJECT_ID + '/product-catalog/create-product', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + getAdminToken()
    },
    body: JSON.stringify({ name: name, image_url: imageUrl })
  });
  if (res.status === 401) { window.location.replace('/login'); return; }
  return res.json();
}

// Combined flow: upload image, then save record
document.getElementById('product-form').addEventListener('submit', async function(e) {
  e.preventDefault();
  var file = document.getElementById('photo').files[0];
  var name = document.getElementById('name').value;

  var imageUrl = file ? await uploadImage(file) : null;
  await saveProduct(name, imageUrl);
});
```

#### Setup Requirements

For image upload to work in an admin panel, you need:

1. **A SAPI form configured** for the upload (even a minimal one):
   ```
   configure_form(
     project_id: 12345,
     form_name: "admin_upload",
     required_fields: [],
     action: { type: "none" },
     max_submits_per_session: 20
   )
   ```

2. **The CDN script** on the page:
   ```html
   <script src="https://cdn.websitepublisher.ai/js/sapi-client.js"></script>
   ```

3. **Admin auth** already working (see Admin Login above)

#### How the Auth Systems Coexist

| Operation | Auth system | Token | Endpoint |
|---|---|---|---|
| Admin login | IAPI Admin Auth | `wsa_` | `/iapi/project/{id}/admin-auth/login` |
| Read/write data | IAPI | `wsa_` Bearer | `/iapi/project/{id}/{service}/{endpoint}` |
| Upload image (Option A) | IAPI Asset Proxy | `wsa_` Bearer | `/iapi/project/{id}/asset-proxy/upload` |
| Upload image (Option B) | SAPI | Session + CSRF | `/sapi/project/{id}/form/upload` |
| Result | — | — | CDN URL in `asset_url` response field |

With **Option A** (asset-proxy), everything uses the same `wsa_` admin token — simpler code,
no second auth system needed.

With **Option B** (SAPI upload), the SAPI session lives separately in
`sessionStorage.wp_{projectId}_sid` and never conflicts with the admin token.

#### Common Mistake

Do NOT try to upload images via `upload_asset` or MAPI asset routes from the browser.
Those are MCP/API tools, not browser endpoints.

**These approaches will NOT work for browser-based uploads:**

- `POST /mapi/project/{id}/assets` with `wsa_` token → 401 (wsa_ not accepted for asset writes)
- `/iapi/project/{id}/upload-asset` → 404 (does not exist)
- A made-up top-level route like `/project/{id}/upload-asset` (missing the `{service}` segment) → 404 — asset writes are `asset_proxy/upload`; the IAPI route shape is always `/project/{id}/{service}/{endpoint}`
- Vault keys (`{{vault:wpa_...}}`) in browser JavaScript → vault refs are server-side only
- Custom API proxy with vault key → proxy passes the literal string, not the resolved value

**Use Asset Proxy (Option A) or SAPI upload (Option B)** — both handle auth correctly
and return CDN URLs. Asset Proxy is simpler because it uses the same `wsa_` token
you already have for data operations.

**Asset Proxy is not images-only.** It accepts any `slug` and stores any bytes in the
PAPI asset system. To write or refresh a JSON/CSV/text data file from an admin panel
(e.g. regenerating a products snapshot at `data/products-snapshot.json`), base64-encode
the text and POST the same `{ slug, base64, overwrite: true }` body — no special
"snapshot" or "data" route exists or is needed. Server-side (agent/MCP), use
`upload_asset(content_text=…, overwrite=true)` instead.

### Vault-Based API Keys (AI-Requested)

When building admin panels or integrations that need server-side API access,
the AI can request a project key **without ever seeing the raw token**.
The project owner approves via email — the key goes directly into the vault.

#### The Flow

1. **AI requests a key:**
   ```
   execute_integration(
     project_id: 12345,
     service: "auth_keys",
     endpoint: "request-key",
     input: {
       vault_key_name: "wpa_dashboard",
       purpose: "Leads dashboard — read and update leads"
     }
   )
   ```
   Response: `{ status: "pending_approval", request_id: "req_a1b2c3..." }`

2. **Project owner receives email** → clicks confirmation link → key is created

3. **AI checks status** (optional, same session):
   ```
   execute_integration(
     project_id: 12345,
     service: "auth_keys",
     endpoint: "check-status",
     input: { request_id: "req_a1b2c3..." }
   )
   ```
   Response: `{ status: "approved" }` (or `"pending"` / `"expired"`)

4. **AI uses the vault reference** in IAPI proxy calls, scheduled tasks, or page templates:
   `{{vault:...}}` with the key name from step 1 (here: `wpa_dashboard`)

The AI never sees the actual token. The key exists only in the vault and is resolved
server-side by the IAPI proxy.

#### Key Rules

- `vault_key_name` **must** start with `wpa_` (prevents overwriting other vault secrets)
- `purpose` is required — it's shown to the owner in the confirmation email
- Max 2 pending requests per project at a time
- Unconfirmed requests expire after 1 hour
- Each confirmation link works only once

#### When to Use This

Use `auth_keys` when a page or scheduled task needs to make authenticated API calls
and no WPA key exists in the vault yet. Common scenarios: admin dashboards,
automated data sync tasks, headless API integrations.

Do NOT use this for visitor-facing pages — those use SAPI sessions (no Bearer token needed).

---

## AI Continuity — Staying on Track Across Sessions

AI assistants typically lose all context when a conversation ends.
WebsitePublisher solves this with infrastructure layers that preserve knowledge:

### Skills (this document)
You are reading a skill right now. Skills are structured instructions that teach AI
how to work with the platform — which patterns to follow, which mistakes to avoid,
and which tools to use. Without skills, every AI session would rediscover
how the platform works from scratch.

**Always call `get_skill` at the start of a session.** It ensures you follow current
best practices, regardless of which AI platform the user is on.

### Design Context (site_context integration)

Design decisions should be **saved immediately** when made — not at the end of a
session when they might be forgotten. Use `site_context` as a living design brief
that any AI session can pick up.

`site_context` stores **design tokens only**: `color_palette`, `fonts`,
`style_notes`, `locale`. Build status, page progress, and to-dos do **not** belong
here — that is what Task Tracking (TAPI, next section) is for. Sending any other
field returns `"No valid fields provided"`.

**Save after every design decision** — writes are a **deep merge**: only the fields
you send are overwritten, everything else is preserved:
```
execute_integration(
  service: "site_context",
  endpoint: "set-context",
  input: {
    color_palette: { primary: "#2D5016", secondary: "#F5F0E8", accent: "#B8860B",
                     background: "#FAF7F2", text: "#1A1A1A" },
    fonts: { heading: "Playfair Display", body: "Inter" },
    style_notes: "Warm, artisanal, Japanese-inspired minimalism",
    locale: "en"
  }
)
```

Field reference: `color_palette` keys are `primary`, `secondary`, `accent`,
`background`, `text` (hex strings). `fonts` keys are `heading` and `body`
(font family names). `style_notes` is free text, max 500 chars. `locale` is
ISO 639-1 (`"nl"`, `"en"`, `"de"`).

**Sections** — a project with more than one visual style (e.g. public site vs admin
panel vs email templates) stores each as a named section via the optional `section`
parameter (`"frontend"`, `"admin"`, ...). Without it, reads and writes target
`"default"`. Max 10 sections per project. The `"default"` section is also included
in the `get_project_status` response.

**Retrieve at the start of every session:**
```
execute_integration(service: "site_context", endpoint: "get-context", input: {})
```
Pass `section: "all"` to get every section as a keyed object.

**List which sections exist:**
```
execute_integration(service: "site_context", endpoint: "list-sections", input: {})
```

**Delete context** — ⚠️ omitting `section` deletes **ALL** sections for the project.
Always pass the section explicitly:
```
execute_integration(service: "site_context", endpoint: "delete-context",
  input: { section: "admin" })
```

This is the single most important continuity tool. Without it, a new AI session
has to ask the user to re-explain every design choice.

### Task Tracking (TAPI)

For multi-session website builds, track progress with tasks so no work gets lost
or repeated. Each task has a slug, status, and history — visible across sessions.

**Create tasks for each build phase:**
```
create_task(slug: "homepage-build", title: "Build homepage with hero + features")
create_task(slug: "shop-pages", title: "Shop overview + product detail pages")
create_task(slug: "contact-form", title: "Contact form with Resend email")
create_task(slug: "admin-dashboard", title: "Admin panel with auth + CRUD")
```

**Update progress as you work:**
```
add_task_history(
  slug: "homepage-build",
  type: "progress",
  status: "done",
  completion_pct: 100,
  summary: "Homepage live: hero section, 3 feature cards, testimonials, CTA"
)
```

**Start of next session — check what's done and what's next:**
```
list_tasks(status: "in_progress")   # What's being worked on
list_tasks(status: "open")          # What hasn't started yet
```

This gives every AI session — regardless of platform — a shared understanding of
where the project stands. The user doesn't have to re-explain what was already built.

### Scheduled Tasks (AAPI)
Websites sometimes need automated actions: publish a page at a specific time,
send a weekly email digest, update data records on a schedule. The AAPI layer
handles this without requiring the AI or the user to be present.

Available via: `create_scheduled_task`, `list_scheduled_tasks`

### Visual Editor (WPE)
The user does not need to start a new AI conversation for every small change.
The Visual Editor lets them update images, reorder content, and adjust styles
directly in their browser — at any time, without AI involvement.

These layers ensure that the **quality and consistency of the website do not depend
on which AI session is active.** The platform remembers — the AI doesn't have to.

---

## API Quick Reference

### Base URLs
```
Pages & Assets:    https://api.websitepublisher.ai/papi/
Entities & Data:   https://api.websitepublisher.ai/mapi/
Forms & Sessions:  https://api.websitepublisher.ai/sapi/
Vault:             https://api.websitepublisher.ai/vapi/
Integrations:      https://api.websitepublisher.ai/iapi/
Dashboard:         https://api.websitepublisher.ai/dapi/
```

### Key PAPI Endpoints
```
GET    /papi/projects                           List projects
POST   /papi/projects                           Create project
GET    /papi/project/{id}/pages                 List pages
POST   /papi/project/{id}/pages                 Create page
PUT    /papi/project/{id}/pages/{slug}          Update page
DELETE /papi/project/{id}/pages/{slug}          Delete page
POST   /papi/project/{id}/assets                Upload asset
GET    /papi/project/{id}/pages?type=fragment   List fragments
```

### Key IAPI Endpoints
```
POST   /iapi/project/{id}/{service}/{endpoint}   Execute integration

# Examples:
POST   /iapi/project/{id}/leads/submit-lead          Store a lead
POST   /iapi/project/{id}/leads/get-leads             Retrieve leads (authenticated)
POST   /iapi/project/{id}/leads/update-status         Update lead status
POST   /iapi/project/{id}/resend/send-email           Send email via Resend
POST   /iapi/project/{id}/mollie/create-payment       Create Mollie payment
POST   /iapi/project/{id}/site_context/set-context    Save design context (deep merge)
POST   /iapi/project/{id}/site_context/get-context    Get design context (section or "all")
POST   /iapi/project/{id}/site_context/list-sections  List stored context sections
POST   /iapi/project/{id}/site_context/delete-context Delete a section (no section = ALL)
POST   /iapi/project/{id}/capability_requests/submit-request  Report platform gap (last resort)
POST   /iapi/project/{id}/product-catalog/bulk-upsert-products  Bulk import (up to 500)
POST   /iapi/project/{id}/tracer/start                Start debug trace session
POST   /iapi/project/{id}/tracer/logs                 Read trace entries
```

### Key SAPI Endpoints (visitor-facing, no bearer token)
```
GET    /sapi/project/{id}/session                Start or resume session
GET    /sapi/project/{id}/csrf/refresh           Refresh CSRF token
POST   /sapi/project/{id}/form/submit            Submit form data
POST   /sapi/project/{id}/form/upload            Upload image (multipart)
POST   /sapi/project/{id}/auth/request           Request magic link/code
POST   /sapi/project/{id}/auth/verify            Verify code
GET    /sapi/project/{id}/auth/status            Check auth status
```

### Lead Capture

Form submissions with `action: {"type": "leads"}` are stored in the platform's
built-in lead capture — no integration setup required.

**Retrieve leads via MCP tool:**
```
leads_get_leads  →  project_id (+ optional: status, form_name, page, per_page)
```

**Retrieve leads via HTTP (for dashboard pages / browser JavaScript):**
```
POST /iapi/project/{id}/leads/get-leads
Authorization: Bearer {wps_token}
Content-Type: application/json
Body: {"page": 1, "per_page": 25}

Optional filters: status (new/contacted/converted), form_name, date_from, date_to
```

**Important:** Leads are always authenticated — there is no public URL.
Never ask for routing files to find the leads endpoint — the URL above is canonical.

**Configure lead capture on a form:**
```json
{
   "form_name": "contact",
   "actions": [{"type": "leads"}],
   "required_fields": ["name", "email"]
}
```

---

## For Platform Developers

If you are working on the WebsitePublisher.ai platform itself rather than building
a customer website, a separate development skill is available with internal conventions,
TAPI task tracking workflow, and infrastructure reference:

```
https://www.websitepublisher.ai/skills/websitepublisher-dev/SKILL.md
```

### Full Documentation
https://www.websitepublisher.ai/docs

### MCP Setup (for Claude Desktop, Cursor, Windsurf, GitHub Copilot)
https://www.websitepublisher.ai/docs/mcp
