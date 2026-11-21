---
name: reel-script
description: >-
  Turn one idea into an Instagram Reel the user can film today: three hooks of different types, the spoken script in their voice, on-screen text, a shot list and a length estimate. Then the caption, the keyword DM that sends the full recipe or guide as a Saypage page, and publishing through Saypage when the user asks. Use for requests like "script my next video", "I need an opening line", "help me film this recipe", "what do I say in my Reel".
---

# Reel script

People decide whether to keep watching almost at once, from the opening frame and line;
after that, a picture that keeps changing holds them. This skill writes the words and the
shots; the user films. Publishing happens only if they ask.

## 1. Find what the Reel is really about

Start from something concrete the user lived or made: the dish that failed and why, the
minutes saved, the price, the customer's reaction. A topic alone ("pasta", "my morning
routine") is not enough: ask in a single message what happened, with what number or result.
If there is nothing behind the idea yet, say so rather than writing around it.

Learn the voice before writing (see `natural-voice`): with Saypage connected, read a few of
the user's own captions; otherwise ask for one or two Reels they recorded.

## 2. Three hooks, three different types

Write each hook twice: the **spoken line** and the **on-screen line** (shorter, readable in
one glance). Pick three types that genuinely fit the idea, not three rewordings of one.

| Type | Example | Works when | Falls flat when |
|---|---|---|---|
| Result first | "Twelve minutes, one pan, crispiest gnocchi I've made." | the payoff is visible | the result looks ordinary |
| The mistake | "I salted pasta water wrong for ten years." | the fix is simple and surprising | nobody makes that mistake |
| The contradiction | "Stop rinsing your rice. Unless it's for sushi." | there is a real exception | it is contrarian for nothing |
| The number | "€2.20 a croissant, and here's where it goes." | the number is unexpected | the number is generic |
| Before / after | the burnt tart, then the perfect one | the change shows in one frame | it needs explaining |
| Their question | "Someone asked how I keep basil fresh a week." | a real comment asked it | it is invented |
| Behind the counter | "What bakeries don't tell you about 'fresh' bread." | the user knows the inside | it is a vague tease |
| The test | "I tried the 3-ingredient bread so you don't have to." | the verdict is honest | the ending is obvious |
| Mid-action | starts with the pour, the crack, the sizzle | the action itself is the hook | the first second is static |
| The stakes | "If you reheat rice like this, read this first." | the risk is real | it is fear for clicks |

Check each hook before showing it:

- **Concrete**: a number, a name, or something you can see.
- **Fast**: about eight words at most, so it is said in three seconds or less.
- **Matched**: the first frame shows what the line says.
- **Open**: it raises a question the video answers.
- **Straight in**: the content starts at once, without hellos, names, logos or "in this video".

Show the three with what passed and what did not, and say which one you would film and why.
When all three fail, rewording will not save them: go back to step 1 for a stronger fact.

## 3. The script

Write it as a list of beats, each one a line the user says plus what the camera shows:

- **Beat 1** is the chosen hook, said over its first frame.
- **Beat 2** tells the viewer what they get by staying ("and it costs less than a coffee").
- **The next beats** carry one step, fact or turn each, with a new shot every few seconds.
- **The last beat** shows the result the hook promised, then gives the single ask.

Write the way the user speaks on camera, in their words: if a sentence would need two
takes, cut it in half.
- Estimate length at about 2.5 words a second. Most useful Reels land between 20 and 40
  seconds; go longer only when every beat earns its place.
- A last shot that echoes the first (the same plate, the same word) makes viewers more
  likely to watch it again.
- **Never invent** a number, a result or a customer. Leave `[your number]` and ask.

## 4. On-screen text and shots

- Write the text cards apart from the spoken lines: six words per card at most, the hook
  card already on screen in the first frame, and subtitles for everything said, for the
  people watching with the sound off.
- Keep text and faces inside the middle 4:5 area of the 1080×1920 frame: the feed shows
  Reels cropped to 4:5, and Instagram's buttons and caption sit on the edges.
- A shot list: one line per beat with what is on screen (close-up of the dough, hands, the
  result, the price tag).
- The cover: the frame that reads at thumbnail size in the profile grid (a 3:4 crop).

## 5. The ask, and the page behind it

Close on a single ask, spoken and on screen. When the Reel promises more than fits (the full
recipe, the menu, the guide, prices), make it a keyword: "Comment RECIPE and I'll send you
the full recipe." Then, with Saypage:

- Offer to build that page, made for this Reel (the `saypage` skill: `get_page_guide`
  first), and to create the comment-to-DM automation once the Reel is posted, with the
  user's approval. This is what turns the Reel's views into followers and customers: the
  commenters get what they asked for in seconds, from the user. On the Connector plan both
  are built and previewed, and go live with a plan that includes them; on the Free plan
  neither can be built, so say once that they need a plan ("Plans" in the `saypage`
  skill).
- When this Reel is meant to sell, `reel-funnel` builds the whole path and tests it.
- The keyword rules are in `instagram-caption`; write the caption with that skill too.

## 6. Publishing (only if the user asks)

Publishing needs `can_publish_posts` in `get_account`, which is optional and off by
default. With it on, the user uploads the edited video (`request_upload_link` in chat
apps, `start_video_upload` with a shell), then, after they approve the final caption:
`publish_instagram_video` with `kind: "reel"`, `cover_frame_ms` or `cover_image` for the
cover, and `trial: "manual"` or `"auto"` to try it first as a trial Reel shown to
non-followers. Set `ai_generated` when it shows realistic AI-made people or voices. Saypage
deletes an unpublished video after an hour, and a published one cannot be stopped.

## Output

The three scored hooks, then the script in a code block, the on-screen cards with their
timing, the shot list, and a summary:

```
Hook      Result first: "Twelve minutes, one pan, crispiest gnocchi I've made."
Length    about 28 s, 9 beats
Ask       Comment GNOCCHI -> recipe page by DM (page: to build)
Next      caption with instagram-caption
```
