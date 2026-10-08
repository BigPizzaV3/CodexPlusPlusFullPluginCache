# Per-platform drafting notes

Guidance for writing the variants in step 3. Platform limits and behavior change, so treat
the numbers below as approximate: write comfortably inside them rather than to the edge, and
trust an error from `create-post` over anything stated here.

## Length

| Platform  | Practical caption length | Notes                                               |
| --------- | ------------------------ | --------------------------------------------------- |
| X/Twitter | ~280 characters          | Longer limits exist on paid tiers; do not rely on it |
| Threads   | ~500 characters          | Short and conversational                             |
| LinkedIn  | ~3,000 characters        | Truncated in-feed after roughly 3 lines              |
| Instagram | ~2,200 characters        | Truncated in-feed after roughly 125 characters       |
| Facebook  | Long-form allowed        | Shorter posts generally travel further               |
| TikTok    | ~2,200 characters        | The video carries the message; the caption is framing |
| YouTube   | Long-form description    | The first two lines show above the fold              |

Front-load the point in the first line or two everywhere. That is what shows before the
"more" cut on most feeds.

## Voice

- **LinkedIn** — professional but not stiff. Concrete specifics beat adjectives. Line breaks
  help; walls of text do not.
- **X/Twitter** — one idea per post. If it needs more room, write a thread as multiple
  `content` items rather than cramming it into one.
- **Instagram / TikTok** — the visual leads. The caption adds context or a call to action.
  Ask what media exists before writing a caption that assumes an image.
- **Threads** — conversational, closer to X than Instagram despite sharing an account.
- **Facebook** — plain and direct works better than marketing register.

## Hashtags

Only when the user asks or their existing posts use them. Check with `list-posts` if you are
unsure of their house style. A few relevant tags beat a wall of them, and hashtag-stuffing
reads as spam on LinkedIn and X in particular.

## Links

Links suppress reach on several networks, LinkedIn and Instagram most noticeably. Where the
user wants a link, offer the first-comment approach described in `SKILL.md` step 5 — but
remember it only applies to Instagram, Facebook, LinkedIn and YouTube. Anything TikTok or
Threads needs has to be in the caption itself.

## Timing

If the user has no preference, spread posts across weekdays rather than stacking them, and
avoid scheduling several posts to the same account within a couple of hours. Do not present
invented "best time to post" statistics as fact — if they want data, `get-analytics-summary`
reflects what has actually worked on their own accounts.
