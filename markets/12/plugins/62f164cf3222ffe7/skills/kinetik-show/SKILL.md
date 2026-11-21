---
name: kinetik-show
description: Use when showing the user what Kinetik made, found or needs from them, or when writing Kinetik's view markup by hand. Which component shows what, and how each is written.
---

# Showing Kinetik's results

The user sees images, carousels and videos only in Kinetik's view, so it is how what Kinetik made, found or needs reaches them. Results from
Kinetik's tasks already come with the view written: show it as it is, and add nothing to it. This
reference is for the rest: showing something again, putting several results in one view, or asking
the user for something. How a request is worked from intent to result is in `kinetik`; trends,
accounts and media projects each have their own skill.

The view is written as simple markup: elements with quoted attributes, nested where an element holds
others. Several results go into one view, wrapped in `<render title="…">…</render>`; a single
element needs no wrapper.

## Choose the component

| To show | Component |
|---|---|
| One image, video, PDF or table | `file` |
| Text: an explanation, a caption to copy, a small table | `markdown` |
| Related images in order, a carousel's slides | `gallery` |
| How a post will look on Instagram | `instagram` |
| Before and after, side by side | `compare` |
| A profile, a scorecard or a source, built from files, numbers and text | `card` |
| One labelled number, in a card or a grid | `metric` |
| Several cards or numbers side by side | `grid` |
| Many connected pieces made for one goal | `media-project` |
| What is trending, to pick from | `trending` |
| Files the user has to hand over | `upload` |
| A task still running | `job` |
| Connecting the user's Instagram | `instagram-connect` |
| Connecting the user's TikTok | `tiktok-connect` |
| Connecting the user's LinkedIn | `linkedin-connect` |
| What the user has connected | `connections` |
| The user's Kinetik credits | `credits` |
| A question with options, or a button to answer | `choice`, `action` |

## Components

### `file`

    <file path="photos/launch/cover.png" caption="Cover"/>

One file Kinetik made, by the `path` its result gave; `url` instead for a link that is already
shared. `caption` is optional. Images, videos and PDFs show as themselves, a CSV as a table.

For editable images, preserve both returned paths: `<file path="slides/01.png" source="slides/01.sri.json"/>`.
Keep the pair as `{path, source}` in media-project, including carousel slides; SRI is not a separate item.

### `markdown`

    <markdown copyable="true">Five habits that keep me posting on busy weeks.</markdown>

Text, written as markdown. `copyable="true"` adds a Copy button, for captions and scripts the user
takes away.

### `gallery`

    <gallery title="Launch visuals"><file path="…"/><file path="…"/></gallery>

Related images, in viewing order. Unrelated files stay separate.

### `instagram`

    <instagram caption="Five habits… #contentplanning"><file path="…/slide-01.png"/><file path="…/slide-02.png"/></instagram>

The files as one Instagram post, in posting order, with the caption as it would go out. Use it for
content meant for Instagram, or when the user asks how it will look there. It is a preview: nothing
is posted.

### `compare`

    <compare><file path="…/before.jpg"/><file path="…/after.jpg"/></compare>

Exactly two files: before first, after second.

### `card`, `metric` and `grid`

    <grid columns="3">
      <card title="@kinetikcoffee" subtitle="Instagram" href="https://instagram.com/kinetikcoffee">
        <metric label="Followers" value="12.4K" delta="+3%"/>
        <markdown>Reels outperform carousels two to one.</markdown>
      </card>
      <metric label="Avg. reach" value="8.1K"/>
    </grid>

- **`card`** groups files, metrics and text into one block: a profile, a scorecard, a source. `title`,
  `subtitle` and `href` (an https link it opens) are optional.
- **`metric`** is one number with its `label` and `value`, written as it should read; `delta` (such
  as `+14%`) is optional.
- **`grid`** lays cards, metrics and files side by side in 1 to 4 `columns`, and stacks them on
  small screens by itself.

### `media-project`

A set of connected pieces made for one goal, as one view: sections by kind, each piece in a version
per platform, and what the user still has to bring. Kinetik's results write it; write it yourself
only to show a set again or together.

    <media-project title="Cold-brew kit launch" summary="Launch next week: 39 €, five networks.">
      <section title="Videos">
        <item title="18 hours in 8 seconds" why="A time-lapse makes the 18-hour claim visible.">
          <variant platform="instagram" cut="Reel" ratio="9:16"><file path="…/reel.mp4"/></variant>
          <variant platform="tiktok" ratio="9:16"><file path="…/tiktok.mp4"/></variant>
        </item>
      </section>
      <section title="People on camera">
        <item title="Kit in action">
          <variant platform="tiktok" status="missing" need="A 10-second clip of someone using the kit."/>
        </item>
      </section>
    </media-project>

- **`media-project`:** `title`; optional `summary`, and `brand`, `handle` and `avatar` for the
  account the previews post as.
- **`section`:** a group of pieces of one kind, strongest first.
- **`item`:** one piece; `why` says in a sentence why it works.
- **`variant`:** the piece on one platform. `platform` is `instagram`, `tiktok`, `linkedin`, `x` or
  `threads`. Optional: `cut`, `ratio`, `duration` (seconds), `pages`, `caption`, `format`.
  One file is a picture or a video, several are a carousel, text is a `markdown` child.
- **`status`**, on any of them: `ready` (the default), `sample`, `planned`, or `missing` with `need`
  saying what the user has to bring.

### `trending`

    <trending/>
    <trending title="What's trending this week"/>

What is trending across social media now, filled in by Kinetik; the user picks one with a tap.
`title` is optional and replaces the heading. It takes nothing else: the trends are always today's.

### `upload`

    <upload title="Add the photo for your post"/>

A place for the user to hand over files, where the host does not let them attach files to their
message. `title` is optional. When the files are in, the user's message says so.

### `job`

    <job id="j_3f9a1c2b"/>

A task that is still running, as a live tile that follows it. Only when a task's answer hands it to you
in `next`: a task whose answer says to call `get_job` again is waited for that way. Several running
tasks go in one view, a `job` each. The tile tells you when its task ends; then call `get_job` for
the result. Directly in `<render>` only.

### `app`

    <app src="workspace/apps/rs_x7Kp2/app.html" session="rs_x7Kp2" title="Reel"/>

An interactive app, such as the reel studio, inside the view. Only when a task's result gives you the
markup or its `src` and `session`: never make them up. `title` and `height` (240–2400 pixels) are
optional. The app works on its own session, not through you; when it asks you in the chat to take
its tasks, call `task_next`, do the task it returns, answer it with `task_submit`, and repeat until
none is open. Directly in `<render>` only.

### `instagram-connect`

    <instagram-connect message="To post your carousel, connect your Instagram."/>

Connects the user's Instagram, to post to it or read its results. `message` is one line in their
language saying why; the card itself explains that Instagram needs a Business or Creator account.
The user signs in on Composio's page.

### `tiktok-connect` and `linkedin-connect`

    <tiktok-connect message="To save the video to your TikTok drafts, connect TikTok."/>
    <linkedin-connect message="To post this on LinkedIn, connect your LinkedIn."/>

Connect the user's TikTok or LinkedIn, each on the service's own sign-in page. `message` is one line
in their language saying why. Instagram, TikTok and LinkedIn are the accounts that
connect here.

When a task needs an account, its result usually brings the card already: show it as returned. The
user connects in their browser and comes back; nothing tells you when, so ask them to say so. A card
may show even when the account is already connected; `connections` says what is.

### `connections`

    <connections title="Your accounts"/>

What the user has connected, one row per service, each with a way to disconnect it. `title` is
optional, and it takes nothing else: which services are there is read for the user. Show it when the
user asks what is connected, and before asking for a new connection when one may already be there.

### `credits`

    <credits/>

The user's Kinetik balance, with a way to refresh it. It takes nothing: the balance is read for the
user. Show it when they ask about credits, or when a task could not start because none are left;
then say the task did not start, and go on when the user asks. Where the client sells nothing, the
card shows no way to buy, so do not offer one in words either.

### `choice` and `action`

    <choice id="platforms" multiple="true">
      <option value="instagram">Instagram</option>
      <option value="tiktok" description="Saved to your drafts">TikTok</option>
    </choice>
    <action id="approve" label="Looks good"/>

A question the user answers with a tap. `choice` takes at least two options and, with `multiple`,
several picks; an option's `description` is one line under it, and `badge` (one or two words, `badge="faster"`, 24 characters at most or it is dropped) marks
the one you recommend in a pick-one — at most one per choice. `action` is one button; `kind` may
be `primary`, `secondary` or `danger`. The answer arrives as the user's message, the label(s) they
chose. Several choices in one view are answered together.

`choice`, `action`, `upload`, the connect cards, `connections` and `credits` go at the top of a
view, never inside a `card` or a `grid`.

## Rules

- **One view at the end.** When several results are ready, show them together in one view, then
  say a sentence or two: what their summaries tell the user beyond the view, ending with the offer
  they make or a question about what to change. Do not retell what the user sees.
- **The next step is a new view.** Repeat an earlier view only when the user asks.
- **Existing views can change.** The owner can edit pictures in the widget. A new `show`
  creates a separate layout; references to the same SRI still share its live content.
- **Markup that is wrong is refused** with what to fix. Fix it and show again.
- **Where the host shows no views,** the answer says so. Give the user the link to the view and the
  link to each file it holds, with the text the answer carries; the links open for the user once
  signed in to Kinetik.
