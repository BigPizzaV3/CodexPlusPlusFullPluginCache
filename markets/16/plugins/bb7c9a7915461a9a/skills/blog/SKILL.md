---
name: blog
description: Write, schedule and publish blog posts on a Frexy website: posts as Markdown files with a cover picture, an author with a photo and links, tags and FAQs, and the blog's own pages. Use when the person asks for a blog, a blog post, an article, an author profile, or to schedule a post.
---

# Blog

Read `get_development_standards` with topic `blog` first: it holds the full contract.

1. **A post is a file**: `content/blog/<slug>.md` written with `write_files`, a
   `---` header then Markdown. The filename is its address (`/blog/<slug>`). Give it
   `title`, `excerpt`, `author`, `tags`, `cover` and `coverAlt`, `publishedAt`, and
   `faqs` where readers have questions.
2. **Status.** A post is a `draft` until it says otherwise. `scheduled` with a
   `publishAt` goes out by itself at that time; `published` is on the site with the
   next publish. Ask before publishing anything.
3. **Cover.** Choose a landscape photograph of the post's own subject with
   `search_images` and bring it in with `import_image`; never leave it empty.
4. **Authors** are `content/authors/<slug>.md`: `name`, `role`, `avatar` (a picture
   added with `add_image`), `url`, and `twitter`, `linkedin` or `github` as fields
   of their own; the body is the bio. A post's `author` names them by that file's
   name or by their name.
5. **The post page** (`public/blog/[slug].html`) places `{{byline}}` under the title
   and `{{authorCard}}` at the end of the article. Frexy draws both: never draw the
   author's picture or the date line by hand.
6. Write as the business would explain it to a customer: its own products and
   examples, plain words, the answer first, two or three links to its own pages.
7. `deploy_preview`, `get_deployment`, then give them the post's link.
