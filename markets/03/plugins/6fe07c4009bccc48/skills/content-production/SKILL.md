---
name: content-production
description: Write, edit and publish articles for a brand. Use for drafting an article, generating a brief or topic ideas, bulk creating content, adding a featured image, translating an article, exporting, or publishing to a connected CMS such as WordPress, Webflow, Shopify or Squarespace. Do not use for keyword research or for measuring how content performs.
---

# Content production

Take an article from idea to published, using the brand's own voice and connected CMS.

Every tool here is scoped to one brand and takes `brand_id`.

## Step 1: resolve the brand

Call `list_brands`. If more than one, ask which. Keep `brand_id` for every later call.

## Step 2: agree the subject before generating

Generation costs credits and takes minutes, so settle the subject first.

- The user has a topic: use it.
- The user wants ideas: call `generate_topic_suggestions` and let them choose.
- The user wants to close an AI visibility gap: get the gap from the ai-visibility-report skill first, then write against it.

Set the title deliberately. `create_content` accepts both `title` and `prompt`, and they do different jobs:

- `title` is the exact headline to publish under.
- `prompt` is the brief for the writer, for example "cover ROI, include two case studies".

If the user gives an exact headline, pass it as `title`. Do not paraphrase it into the brief, and do not let the brief overwrite it. The title also steers the featured image, so a wrong title produces a wrong image.

## Step 3: generate

Call `create_content` with `brand_id` and the agreed `title` and `prompt`. Optional: `type` (how_to, listicle, comparison) and `model` from `list_ai_models`.

Generation is asynchronous:

1. Note the returned content id.
2. Poll `get_content_job_status` with `content_id`. Do not poll faster than every 20 seconds.
3. When it completes, call `get_content` to read the draft.

For many articles at once use `bulk_create_content`, but confirm the full list with the user first. It multiplies both credits and review effort. Check the plan's remaining usage with `get_workspace_details` before a large batch, so the limit is known before the spend rather than after it.

## Step 4: revise

- `update_content` for edits you can make directly, including the title and body.
- `regenerate_article` to rewrite from a changed brief. This replaces the draft, so confirm before calling it.
- `bulk_update_content` for the same change across several articles, for example a status move.

## Step 5: add the image

1. `generate_image` with a prompt describing the subject. Base it on the article title, not the brief.
2. `set_article_image` to attach it.

## Step 6: publish

1. `list_connectors` to see which CMS destinations the brand has connected. If none, tell the user to connect one in the brand's Connectors settings and stop.
2. `publish_content` with `content_id` and the chosen `integration_id`.
3. `list_publications` to confirm it landed and to get the live URL.

Squarespace is the exception. It exposes no API for creating posts, so use `export_content` to produce an import file that the user uploads themselves. Say this plainly rather than implying an automatic publish.

Other paths: `import_content` brings existing articles in, `manage_translations` produces other language versions.

## Boundaries

- Never publish without explicit confirmation. Publishing is public and hard to undo. Show the title, the destination and the URL, then wait for a yes.
- Never bulk create or regenerate without confirming scope, for the same reason.
- `delete_content` is destructive. Confirm, and list exactly what will be deleted.
- Do not claim an article is live until `list_publications` shows it. A queued publish is not a published one.
