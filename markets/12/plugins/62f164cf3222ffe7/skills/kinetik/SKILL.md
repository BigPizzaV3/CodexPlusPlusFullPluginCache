---
name: kinetik
description: Use whenever the user wants help with their social media through Kinetik: researching trends and their niche, reading a post or video they link, analyzing an account, getting ideas, a content plan or the best format for a post, or making, changing, finding or posting images, carousels, short videos and campaigns; also when they ask what Kinetik can do. How a request goes from the user's words to what they see.
---

# Working with Kinetik

Kinetik researches the user's niche, understands their account, and makes and posts content in their
brand: their look and their voice. It keeps everything it makes, across every chat.

## Read the request as an intent

- **Something new** (a post, a carousel, a Reel): Kinetik makes it.
- **An effect for their photo or video**, named or to be picked: Kinetik picks and makes it with
  `create_content`, from their file added with `upload_files`; it offers the choice when there is one.
- **A change** to something made before: Kinetik changes that piece. Find it first when the chat does
  not hold it. A change makes a new version; the earlier ones stay, so the user can go back.
  Live editable pictures are the exception below: use the current render as the editing base.
- **Many connected pieces for one topic or goal:** `kinetik-media-projects`.
- **"What did I make", "last week's carousels"**: Kinetik finds it.
- **Ideas on demand** (a month of content, a launch plan, ten hooks for tomorrow): they come back in
  the chat as text. Making them is the next step, when the user wants it.
- **What is trending**, across social media or in their niche: `kinetik-trends`.
- **What is in a post or video they link** (Instagram, TikTok, YouTube): `research`, the link in its
  query; Kinetik watches it and reads what it says.
- **Which format a post they plan should take**, or posts like it that took off on Instagram, LinkedIn or X:
  `get_post_format_recommendations`, one idea per call.
- **Understanding an account** (how it performs, what to post next, what to stop) **and posting**:
  `kinetik-accounts`.

Images, carousels and videos the user asks Kinetik for are made with `create_content`, so they come
out in their brand and are kept with the rest of their content. Pass the request as the user said it,
even a bare "make a carousel": add nothing and do not ask first, unless a trend pick says otherwise; Kinetik asks for what is missing.

## Content takes minutes

Making content is work that runs for a few minutes. Independent pieces can be started together. Then
wait for each piece of work as Kinetik's answer says: call `get_job` again, or show its tile and end
your turn, and the tile tells you when the work is done, has failed or has a question. Slow is normal:
the same work is never started twice. When everything is done, show it all
together in one view, since that is the only place the user sees images and videos. Then, in a sentence
or two and without retelling what they see, pass on what Kinetik's summary says that the view does not:
whose content it is, what was chosen for them, what differs from their request. End with its offer, or
ask what they would change.

## When Kinetik asks

Kinetik comes back with a question when it needs something only the user has: a photo, a topic, an
account to connect. Ask the user exactly that, in their language. With their answer, ask Kinetik for
the same thing again, in the same turn. Where the task takes `continue_job`, pass the job that asked
there, their reply as `answer` and the same arguments as before: Kinetik goes on from where it stopped.
An answer that is a file is the answer: add it with `upload_files` and ask Kinetik again with its paths,
without asking the user to confirm it or to allow its use.

## The user's files

Photos, videos and documents go to Kinetik first, then into what it makes. Where the user can attach
files to their message, they attach them there; elsewhere Kinetik's own upload form takes them.
A photo from earlier in the chat belongs to the earlier piece: a new request starts from new material
unless the user says to reuse it.
