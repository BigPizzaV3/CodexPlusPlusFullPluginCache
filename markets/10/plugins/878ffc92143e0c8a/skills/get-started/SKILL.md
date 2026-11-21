---
name: get-started
description: Connect URLMe to create short or branded links, or draft, preview, and publish project showcase pages with the user's approval.
---

Help the user complete their requested action: a real short link or a project showcase. Connect their URLMe workspace through the plugin's OAuth flow when needed. After the connection succeeds, call `get_profile` and `get_usage` once to confirm the selected workspace and capacity, then continue the user's original request. Preserve any destination, public project details, and label supplied before sign-in; do not make the user repeat them. When the user wants a showcase, follow the showcase workflow below instead of creating an unrelated short link.

## Project showcase workflow

1. Call `list_showcases` to find existing pages and current server-provided limits, colors, and Stripe-aligned inquiry allowances. Free includes one page and two colors; all paid plans include premium features with their respective limits. Do not infer paid access from the user's claim or a plan name alone.
2. For a new page, gather the HTTPS project URL, project title, public creator/business name, and a short introduction. Never publish a private account email or infer a public identity from account details. Call `create_showcase` with a fresh UUID requestId, retaining that same ID and exact arguments for any uncertain retry. Creation saves an unpublished draft; it never publishes. Do not create a page just because the plugin was installed.
3. Call `get_showcase` and present the saved destination, title, introduction, public creator, accent, inquiry setting, and publication state. Return its private editorUrl for visual preview and optional screenshot upload. Its publicUrl does not work until publication. Cover uploads and visitor inquiry access remain in the web console; never claim to upload an image or read an inquiry with these tools.
4. For edits, use `update_showcase` with the latest expectedUpdatedAt. Do not change live content silently: explain that a published page must be explicitly unpublished before editing its draft. Preserve any existing cover image.
5. Ask for explicit confirmation to publish the exact previewed content. Only then call `publish_showcase` with that page ID and its latest expectedUpdatedAt, and return the actual publicUrl from the result. A request to create a draft is not permission to publish. If the page changed, read it again and obtain approval of the new preview before publishing.
6. Call `unpublish_showcase` only when the user explicitly asks to take that exact page offline. It preserves saved content and existing inquiries. It does not cancel billing.

Showcase tools require showcases:read and showcases:write permissions and a current owner/admin membership. Reconnect through normal OAuth consent when additional showcase permissions are needed; do not silently reuse old short-link grants. Never request API keys, start a paid checkout, or change a subscription in chat. Explain real quota/paid-feature errors and link to https://app.urlme.link/billing when appropriate, without claiming an upgrade succeeded.

## Short-link workflow

If the user already supplied a destination URL and requested shortening, call `create_short_link` with that URL as soon as authorization is complete. The default `urlme.link` domain needs no custom-domain setup, payment, API key, alias, description, or expiration. Omit optional fields unless requested. Do not ask the user to connect a domain or select optional settings before making a standard link.

If setup starts without a destination, ask just one question: "What URL would you like to shorten?" Mention briefly that they can use `https://example.com` for a first test. Once they answer, create the link. Never create a link merely because the plugin was installed; the user must request creation or agree to a test.

Return the real short URL as a clickable link and confirm it is saved in the connected workspace. Keep the first success response short. Offer one relevant next action, such as viewing the link or creating another, after the working link is visible.

If a tool returns an error, explain its actual reason in plain language and the next action needed. Do not announce success or invent a short URL. If authorization expired, reconnect and resume the original request. If the outcome of a creation request is uncertain after a timeout, check recent links before retrying to avoid duplicates. If the user explicitly requests a branded domain that is not connected, explain that requirement and offer a standard `urlme.link` link; do not substitute silently.

After first-link creation, explain relevant features when the user asks: URLMe can create standard or branded short links on a connected custom domain, choose custom aliases, add private descriptions, schedule expiration, list recent links with redirect analytics, update private descriptions, pause or resume redirects, permanently expire links, identify the connected workspace, and report current plan usage and resource counts. These are examples for later exploration, not a setup checklist:

- “Shorten this URL and label it for my launch.”
- “Create a branded link on my connected domain with the alias welcome.”
- “Show my newest links, redirect counts, and recent activity.”
- “Pause the campaign link.”
- “How much of my plan have I used?”

When the user asks to create a link, preserve the destination exactly and pass a description only when the user provided or requested one. Use the workspace's default URLMe domain unless the user names a connected custom domain. Never invent a short URL; return only the URL produced by `create_short_link`.

The URLMe product also provides searchable workspace history, DNS and HTTPS custom-domain setup, bulk creation, private tags and filtering, UTM parameters, destination changes, deletion, downloadable QR codes, CSV export, REST API automation with idempotent retries, per-integration API-key creation and revocation, and subscription management through its web console or REST API. These actions are not exposed by this MCP server. When the user requests one of them, explain the boundary and direct the user to the appropriate URLMe console or API workflow rather than claiming the action was completed.

Before calling `expire_link`, identify the exact link and ask for confirmation because expiration is permanent. Pause and resume links only when the target link is unambiguous. Do not request, display, or store URLMe API keys in chat; OAuth supplies the connection.
