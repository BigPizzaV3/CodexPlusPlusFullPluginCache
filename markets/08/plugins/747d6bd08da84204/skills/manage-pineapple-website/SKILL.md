---
name: manage-pineapple-website
description: Make user-requested changes to an existing Pineapple website, including draft pages and blog posts, supported blocks, SEO, assets, business details, design, listings, testimonials or translations, using scoped tools and action review.
---

Make only the changes the user requested. Use the connected Pineapple MCP tools and their current schemas; this skill does not grant account access or action approval.

Before reading account data, check whether the requested operation is supported. Deleting records, unpublishing, removing domains, managing teams, buying subscriptions or credits, registering domains and taking payments are outside this plugin. For an unsupported-only request, explain that boundary without account reads, substitute writes or a brief. Do not start a purchase flow, ask for payment or plan choices, or return checkout/upgrade links. Attaching an already-owned domain is distinct from registering or buying one and still requires a named target and separate approval. For a mixed request, address only the supported portion within its existing permissions.

## Identify and read

Resolve the exact workspace, website and page or record from supplied context or minimal discovery. Use `pineapple_list_workspaces` and `search` when needed; if several targets match, ask the user to choose. Use `fetch` only with a Pineapple URI returned by `search`, never a guessed URI or a raw document ID. Use returned document IDs with the corresponding structured tools.

Request only the relevant category access. No access leaves private category data unavailable, although basic workspace/site names and IDs can remain visible. Read allows inspection, not editing; Write includes the category's read access where supported. Briefs is write-only and analytics is read-only. Do not treat unavailable data as empty or bypass a missing scope with another tool or direct API.

Read the current fields and revision needed for the requested change. For pages, reuse `pineapple_list_pages`, `pineapple_list_page_blocks` and `pineapple_get_page_seo` as appropriate. Preserve existing block IDs and unrelated fields. Public block editing is limited to the types and static properties in the advertised schema, not arbitrary code or all editor blocks.

## Blog posts

Create a requested blog post with `pineapple_create_page`, `page_type: BLOG_PAGE` and its Markdown content, using the selected website and intended pathname. New posts are drafts; creating or editing one does not authorize publication.

For an existing post, read its current blocks and SEO before changing the requested supported fields. Preserve its block IDs, unrelated content and revision guards; do not create a replacement post to work around an unsupported edit. Use the same action-review and readback flow below. Documentation-site workflows are not part of this skill's supported release.

## Review and execute

Use the relevant advertised mutation, its exact target IDs and revision guards, and a new schema-valid request_id for the distinct change. Explain the concrete change, preserving unrelated content. When Pineapple returns a review link, show it and wait for approval in Pineapple; OAuth consent and a user saying “yes” in chat do not replace the server action review.

Continue an approved operation with its original request_id and unchanged arguments. After timeout or ambiguous failure, read back the target before considering a retry. Never create a new request ID merely to bypass pending, cancelled, expired or uncertain approval. For a stale revision, reread and obtain a fresh review for the revised operation.

Upload only a user-provided attachment using the native file input required by `pineapple_upload_attachment`. Stored assets and inserting an Image block are separate operations; review each. Do not substitute another file if an upload fails. Warn when the reviewed upload makes the asset accessible through a shareable URL.

Only use customer-supplied testimonial text; fictional demonstrations must remain explicitly fictional. Product and service tools manage listings, not payments. Translation generation uses the existing allowance; do not silently regenerate every page, buy credits, or equate translation generation with publication.

## Verify and report

Free hosted website addresses use `<subdomain>.pineapple.page`, managed through website subdomain settings rather than custom-domain attachment. Use the website's returned address instead of inventing one. Attaching an already-owned domain or subdomain is a separate flow subject to the account's plan and hosting configuration. `pineapplebuilder.com` is Pineapple's platform domain, not the free website suffix; a deliberately configured company-owned subdomain is a custom-domain case, not automatically a working website. Use the current tools to check eligibility and setup status, and verify the published page before reporting that the address works.

Read back the changed fields and revision using the relevant read tool. Report exactly what was saved, what remains unverified, and whether the result is a draft or published. Preview rendering is separate evidence from persistence. Never claim indexing, revenue, or a working domain from a successful settings write alone.

Publishing and domain changes require an explicit user request naming the target and the normal separate action review. A general request to improve, save, prepare, or launch-plan a website is not authorization to publish or change its domain. Read `pineapple_get_publication_review` when relevant; do not assume shared navigation, translations or other pages are included. Do not delete records, unpublish, remove or buy domains, manage teams, take payments, or use internal tools to get around these exclusions.
