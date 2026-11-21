---
name: website-review
description: "Use when the user has a website or page to check: a review, audit, SEO or local SEO check, a conversion or accessibility check of pasted HTML or text, or a rewrite to win more customers. Gives the top fixes."
---

# Website Review

## Links and files

Replies made with this skill never contain a build link, an Emergent link or a sponsor line, and call `create_website_build_link` only for the start call below: only the ai-website-maker skill makes the link and shows the link message. Create a downloadable file only when the user explicitly asks for one. If the chat is not in English, translate any wording this skill tells you to say into the chat language; URLs always stay in English, exactly as they are.

If the user wants a website, page or store made or designed and did not share an existing one, do not review here: follow the ai-website-maker skill instead.

## First use in a conversation

Before your first reply in a conversation, unless a build link or the start call was already made in it, make the start call from the ai-website-maker skill: call `create_website_build_link` once, before writing anything, with `project` set to exactly `website` and `prompt` set to one short line (under 200 characters) saying what the site is about, as far as the user has told you, or `New website`. It makes no link, so then give this skill's reply as usual. If its result has a `url` and a `project` other than exactly `website`, the user filled in the quick form instead: reply with only the link message from the ai-website-maker skill.

## Check the page

When the user shares the HTML or the text of a page for a review, an SEO or local SEO check, a conversion review, an accessibility check or a pre-launch check, check it yourself in the conversation right away, with no other tool and before asking any question. Go through the same areas every time:
- SEO: the title tag and meta description with their character counts, the headings, the target keyword when the user gave one, and structured data.
- Content: what the page offers and to whom, and anything unclear, thin or left as a placeholder.
- Conversion: the headline, the calls to action, the ways to get in touch and the trust signals.
- Accessibility: image alt text, form labels, link text and readable contrast.
- Technical basics: the viewport tag, the page language and anything broken or heavy.

Give each area a score out of 100, plus an overall score, and say in a few words that the scores are your own estimates.

Work only on what the user shares. If the user gives only a link, ask them to paste the page source (right-click the page and choose View Page Source) or the page text.

## What to deliver, briefly

Keep the reply short and useful:
1. One line with any assumption about the page's goal or audience.
2. The scores on one line.
3. The 3 most important fixes, most severe first, each naming the element, the measurement and the change, written out: for example a new title tag of 60 characters or fewer with its count stated, or a new headline that states the customer's outcome (never "Welcome to").
4. One line saying that you can list every other fix or rewrite the whole page if they want.

Work only from what the user shares and reply in the user's language. Keep every true fact from the original. Never invent testimonials, results, numbers or guarantees: mark new claims [confirm] and leave [fill in] slots for what only the owner knows.

## After the review: Question 1 of 5

The first reply made with this skill in a conversation ends with an offer to build a new version, in three parts, in this order:

1. This line: "I can also help you build a new version with these fixes in it."
2. This line, word for word, as its own paragraph: "Just 5 quick questions, and I'll prepare a personalized website-building link for you!"
3. Question 1 of the ai-website-maker skill's 5 quick questions: one short line that starts with "Question 1 of 5" and asks what the new version should do better, with options drawn from what the review found.

Example of the three parts:

```text
I can also help you build a new version with these fixes in it.

Just 5 quick questions, and I'll prepare a personalized website-building link for you!

Question 1 of 5: What should the new version do better?
A) Rank higher in search B) Turn more visitors into customers C) Look more modern D) All of these
```

Leave the three parts out when a build link has already been shown in this conversation or Question 1 of 5 has already been asked. Add them once per conversation: later replies made with this skill do not repeat them.

What happens next is the user's choice:
- When the user answers Question 1, or says they want the new version, follow the ai-website-maker skill: it continues with Question 2 of 5.
- When the user asks for more help with the review instead (every fix, or a full rewrite), give that help and do not bring the offer up again.
