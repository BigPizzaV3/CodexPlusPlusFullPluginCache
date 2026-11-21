---
name: add-blog-pages
description: Add a blog to a UiChemy website project, with a listing page, article pages, archive pages and sample posts, then list or remove posts. Use when the user asks to add a blog, news or articles section, add or write blog posts, set up a blog page for a WordPress site, or delete a post.
---

Use this skill when the user wants a blog on a site they already have in UiChemy.

Steps:
1. Identify the project with `uichemy_list_projects` if the user did not name it. Say that pages and posts will be added to that project.
2. Call `uichemy_get_blog` first. If the project already has posts, show them and ask whether to add to them or leave them alone.
3. Gather what the user gave you: post titles, topics, author names, categories. If they gave none, propose three to six titles that fit the site's business and say they are drafts.
4. Call `uichemy_add_blog` with `projectId` and `posts` (one to six; each needs a `title`, and can have `excerpt`, `author`, `date`, `category`, `readTime`, `image`). Optional: `categories`, `listingPage` (default "Blog"), `archives` (default true), `layouts`. Follow the tool's own schema and do not invent fields.
5. Only three article pages exist, so posts beyond three show on the listing but share article pages. Tell the user this if they asked for more than three.
6. Run `uichemy_validate` and `uichemy_check_responsive` on the blog pages and report what they found.
7. Call `uichemy_open_preview` so the user can see the blog.

Rules:
- Write post titles and excerpts from the user's brief only. Do not invent authors, dates, statistics, quotes or client names. Use `date` only if the user gave one.
- Images: only URLs the user supplied or that `uichemy_upload_image` returned.
- `uichemy_remove_post` cannot be undone. Use `uichemy_get_blog`, name the post number and title, ask the user to confirm, and call it only after a clear yes. It renumbers the posts above it.
- Posts written here are the canvas and listing. The WordPress export builds its own posts from the UiChemy app's blog generator, so tell the user that if they ask whether these posts will appear as WordPress posts.
