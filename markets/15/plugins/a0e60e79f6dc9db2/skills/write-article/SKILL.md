---
name: write-article
description: Write and stage a blog post, news article, announcement, case study or guide in Agility CMS from a topic or brief. Use when the user asks to write, draft or post an article or blog post. Covers finding the right list, filling author, category and tag fields, the body, an image, the excerpt and SEO description, saving as a draft, and translating.
---

# Write an article in Agility CMS

An article is a content item in a list such as BlogPosts or News. This skill
covers the whole job; the rules for saving fields come from the `edit-content`
skill, and the voice from the `brand-voice` skill.

## 1. Gather the brief

Before writing, know:

- the topic, the audience and the one point the article must make
- the facts to use (a release note, a product page, the user's notes). Do not
  invent facts, numbers, customer names or quotes. If something is missing, ask
  or leave a clearly marked placeholder.
- the brand guidelines, if the user has them (see `brand-voice`)
- an image: a file the user provides, or an asset already in Agility

## 2. Find where articles live

1. Confirm the instance and locale.
2. Call `get_containers` and pick the article list. If several could fit
   (BlogPosts, News, Resources), ask.
3. Call `get_content_model_details` for its model. Note the body field (rich
   text or Markdown), the slug, excerpt, image, author, category and tag fields,
   and which are required.
4. Read one or two recent articles with `get_content_items` and
   `get_content_item` to copy how fields are actually used: body format, slug
   style, excerpt length, how many tags.

## 3. Resolve linked fields to real IDs

Author, category and tags are usually links to other lists. Find the IDs with
`get_content_items` on those lists (or `search_instance`) and use the companion
field names shown in the model (for example `Author_ValueField` and
`Author_TextField`). Use existing categories and tags. Do not create new ones
unless the user asks.

## 4. Write

- A headline that says what the reader gets, then a body that leads with the
  point. Use the body format the model expects: HTML for rich text, Markdown for
  a Markdown field. Use headings for anything longer than a few paragraphs.
- A slug from the headline: lowercase, hyphens, no dates unless the site uses
  them.
- An excerpt of one or two sentences, plain text. Reuse it as the SEO meta
  description if the item has SEO fields (140 to 160 characters works best).
- Links inside the site use the `~/` prefix, for example `~/products`.

## 5. Image

Use an asset from `list_media`, or upload the user's file with
`initialize_media_upload` and use the URL it returns. Give it real alt text in
`label`.

## 6. Save and check

1. `save_content_items` with `contentID: -1`, every field, and
   `releaseDate: null`, `pullDate: null`.
2. Read it back with `get_content_item` and check the body, links and image.
3. Give the user the editor link and a short summary: title, slug, author,
   category, tags, and anything left as a placeholder. Say it is a draft.

Publish only if the user asks, using the `publish-and-workflow` skill.

## Translations

If the user wants other languages, translate after the original is approved.
Save each translation in its locale with the same container, keep the slug
consistent with the site's convention, and do not translate IDs, URLs or code.
Report each locale's result.
