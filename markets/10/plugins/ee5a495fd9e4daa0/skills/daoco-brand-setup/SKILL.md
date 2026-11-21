---
name: daoco-brand-setup
description: Create a personal or business brand in Daoco from a website, public profiles, the person's own description, or files in their project, walk them through the setup review step by step, and offer the first work Daoco suggests. Use when the person has no Daoco brand yet or asks to add one.
---

# Set up a brand in Daoco

Read [the shared Daoco workflow](../daoco-marketing/SKILL.md) for sign-in, tool boundaries, and running work. Signing in from the app creates a Daoco account when the person has none, so a new person can start here.

## Gather what Daoco needs

Call `list_brands` first. If the person already has a brand that fits, select it with `use_brand` instead of creating a duplicate.

`create_brand` needs a `name` and a `type`, plus something to research: `website`, `profiles`, `about`, or `files`.

- `type` is `personal` when the person is the brand (a creator, founder, consultant, or expert) and `business` for a company, product, or organization. Ask when it is unclear; do not guess from the name.
- `website` and `profiles` (public social profile URLs) are what Daoco researches. `about` is a description in the person's own words, used alone when there is nothing else. Pass what the person gave; do not write `about` for them from a guess.
- `files` takes text files from the person's own material as a map from path to full contents: brand guidelines, voice or positioning notes, product or audience docs. When the app can read the person's project, offer to send the files that describe the brand, and list which ones before sending. A `SKILL.md` with its `references/` folder is imported as a draft skill a workspace owner or admin publishes in Daoco. A Daoco brand export (from `export_brand`) sets the brand up from the export itself. Daoco cannot read paths on the caller's computer, so send contents, not paths.
- For a personal brand, `goals` (what they are after, such as clients, speaking, an audience, or brand deals) and `focus` (their niche or the role they are aiming for) shape what Daoco suggests later. Ask once; they are optional.

Tell the person before calling that the brand uses an assistant slot and counts toward the workspace's brand limit. A person who administers no workspace gets their own on the free Starter trial, with no card. If they administer several, the call returns their names and `workspaceId`s and creates nothing; ask which and call again with `workspaceId`. Use a `clientRequestId` so a retried call returns the same brand instead of creating a second one.

The new brand is selected for the app. Share the returned brand link.

## Review the setup

Research takes a few minutes. Call `review_brand_setup` with `waitSeconds` up to 30 to wait for the drafted profile, and tell the person what is happening. `researchStatus` says whether research is running, done, or failed. If it failed, `researchFailed` says why and `nextStep` is `describe`: ask the person to describe the brand (`description`) or send another link or file.

When research lands, show the drafted name, description, industry, audience, tone, voice notes, and the logo and colors it found. Then follow `nextStep`, one step at a time, asking `nextStep.question` in its own words, as every Daoco setup does:

- Business: `competitors` (the likely competitors found; the person removes, adds with a website, and confirms), `channels`, each open question, `sharpen`, then `finished`.
- Personal: `goals`, `about_file` (a bio, portfolio, or one-pager; a media kit when they want brand deals), `channels`, each open question, `sharpen`, then `finished`.
- `confirm_fact` can come up when something the person said disagrees with their site or files: show both values and pass their pick as the answer (`1`, `2`, the right value, or `skip`).

Rules for every step:

- Pass only what the person said. Given fields replace the drafted values; do not "improve" a field they accepted.
- Answer a question with its `questionId` and the person's `answer`, in their words. Answers become the brand's documents, so never answer for them, and never fill in beliefs, experiences, credentials, prices, or results they did not state. An empty answer declines a question. `skipSteps` skips a step they decline.
- Daoco Looks (visual styles for the images Daoco makes) come with example image links. Show them and pass `keepStyles` or `dismissStyles` with the person's choice. Undecided ones stay unused suggestions.
- `saveDocuments` adds the brand's own documents, such as a messaging guide, as Markdown; `addSources` adds more links for research to read.

Setup does not wait for the person. Daoco starts writing the summary, voice, documents, and competitor research when the person confirms (`confirm: true`) or about a minute after the draft is ready (`closesAt`), from what stands then. Answers and corrections are still taken until `fixesUntil`, a day after creation, and rewrite the documents they inform. Only the person who created the brand can change it. A brand set up in the Daoco dashboard, or past `fixesUntil`, is edited on its Brand page in Daoco; `review_brand_setup` says so.

## Connect accounts

After the profile, ask which accounts the person wants Daoco to post to or read from. `get_brand_status` lists the accounts Daoco found for the brand that are not connected yet, each with the `target` `get_connect_link` takes; offer a link for each one the person wants (see `daoco-social-posting`). Connecting happens in the browser through that link, never in chat. Work that reads the person's own posts needs those accounts.

## Offer the first work

`get_brand_context` reports `setup` while the brand is being set up: `researching`, `review`, `research_failed`, `writing`, or `needs_review` with a link to finish in Daoco. Report that state instead of starting work against a half-written brand.

When setup finishes, `get_brand_context` and `get_brand_status` may list `firstWork`: up to three suggested first pieces of work, such as a point-of-view post or a bio kit. Offer them in plain words and let the person choose. Run the chosen one with `run_workflow` (its command and subject) where that tool is listed, or pass its request to `start_work` as given, and follow it with the shared workflow. Starting it uses workspace tokens.
