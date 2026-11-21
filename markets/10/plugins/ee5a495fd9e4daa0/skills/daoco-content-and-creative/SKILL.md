---
name: daoco-content-and-creative
description: Ask Daoco to create or revise social posts, website pages, emails, images, video, or campaign content for a personal or business brand.
---

# Create content with Daoco

Read [the shared Daoco workflow](../daoco-marketing/SKILL.md) for selection, execution, retries, results, and approvals.

Carry the person's goal, audience, channel, deliverable, source material, and constraints into the request. Ask only for missing details that would change the work. Let Daoco use its saved brand knowledge and connected sources instead of making the person repeat them. Keep requested quantities and formats; a single post is not permission to launch a campaign.

When the person has the exact post text and only wants it saved or posted, use `daoco-social-posting` instead of a paid run. When this app writes the copy itself, call `get_brief` for the task and channel first and write from it.

## Ask Daoco to make it

Send production through `start_work`, or through `run_workflow` when the person names one of Daoco's workflows or a Daoco read returned one. Where `run_workflow` is not listed, describe the same work in words; a typed `/command` is read as words there. Useful workflows, where offered:

- A week of posts, posts from the person's own photos and videos (attach them), repurposing a post or page, a carousel, short vertical clips from a longer video, an email, product copy, a media kit, a page for the website.
- A point-of-view or story post (`pov`): it needs the person's own opinion or experience. The first run ends with questions, not a post. Show them, then send the person's answers in their words through `continue_work` on the same thread. Never answer for them.

Pass an `ideaId` from `list_content_ideas` to `start_work` when the work makes that idea, so it is claimed and measured.

For a revision, use `continue_work` on the existing thread and name the output and the change. Daoco handles specialists, visual styles, assets, and saved drafts. Retrieve text with `read_work` and images, video, charts, or reports with `get_output`. `list_work` with `view: "drafts"` lists saved drafts. A completed draft is not published or scheduled; when the person asks to post one, follow `daoco-social-posting` with its `postId`.

## Brief the actual deliverable

Use what fits; do not turn these into extra questions or enlarge the task.

- A batch of posts needs the count, destinations, and any theme or dates. Keep copy, creative concepts, generated media, and saved drafts distinct; an outline is not a finished batch.
- Repurposing needs the source and the destinations. Keep the source's claims and idea, with native openings, length, structure, and calls to action for each platform.
- A page needs its reader, purpose, and any source or search intent. Keep the page type (comparison, landing page, guide); not every page is a blog post.
- An image or video brief carries placement, references, exact text that must appear, and any size, duration, or style. Send references and source video as `files`, never as a local path.
- A media kit or sponsor pitch needs supported audience numbers and real offers. Missing rates and metrics stay missing.

For personal brands, ground content in the person's own expertise and experiences; for businesses, in their products, offers, and evidence. Never invent a testimonial, result, or personal anecdote to fill a brief.

## Check what came back

Before reporting success, compare the work with the request: count, destinations, format, required text, and whether the files or drafts exist. Distinguish a concept from a generated asset, and a proposed document change from an applied one.

Questions Daoco asks because only the person can supply an opinion, experience, or result are not a gap: relay them instead of asking Daoco to write it anyway. If something else requested is missing, name it. If a receipt `notice` says a file was not sent, fix the attachment first. One focused follow-up on the same thread may finish the job; after that, return the useful work and say what is missing. Do not claim to have looked at an image or video unless the client showed it to you; `get_output` returns an inline preview for images where the client displays it.
