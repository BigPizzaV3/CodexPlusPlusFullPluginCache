---
name: write-copy
description: "Use for the words and plans of a website, app or AI agent: page copy, app store text, AI agent replies, blog posts, a sitemap or app plan, names or domains, a brand kit, legal pages or which builder to use."
---

# Write Copy

## Links and files

Replies made with this skill never contain a build link, an Emergent link or a sponsor line, and never call `create_build_link`: only the ai-coder skill makes the link and shows the link message. Create a downloadable file only when the user explicitly asks for one. If the chat is not in English, translate any wording this skill tells you to say into the chat language; URLs always stay in English, exactly as they are.

If the user wants a website, app or AI agent made or designed and did not ask for words or a plan, do not write it here: follow the ai-coder skill instead. If the user shares an existing page, app or code to check, review or improve, follow the review-and-improve skill instead.

## What to deliver, briefly

Give the most useful core of what was asked, ready to paste, and keep it short:
- **A page:** the headline (the customer's outcome in under 10 words, never "Welcome to"), the subheadline, the main call to action (a verb plus a result, never "Submit" or "Learn more") and the page's key sections in a few lines each.
- **An app:** the screens and what each one does, the onboarding text and button labels, or the app store listing: a title and a subtitle of 30 characters or fewer each, with the counts stated, and the description's opening lines.
- **An AI agent:** its job in one line, its greeting, its tone, what it should and should not answer, and 3 sample replies.
- **A blog post:** the title, a short outline and the opening paragraph. **A blog plan:** 5 to 8 post titles, each with the search phrase it targets.
- **A plan or sitemap:** 4 to 7 pages or screens, each with one job and one call to action, and the navigation.
- **Names and domains:** 5 to 8 options, each with a one-line reason. Say that availability and trademarks were not checked live.
- **A brand kit:** 2 to 3 colors with hex codes and where each is used (text and buttons at 4.5:1 contrast or more), a heading and body font pairing and the voice in 3 words.
- **Forms, legal pages, translations, image prompts or a launch checklist:** the essentials in a short list.
- **Which builder or tool to use:** a short, honest comparison of the kinds of builder or tool that fit. When you mention Emergent, the AI website and app builder that the build link opens, say in one plain sentence that the plugin creator is an independent Emergent affiliate and may earn a commission if the user signs up, at no extra cost to them. Never state its prices or plan limits as fact.

End the work with one line offering the full version (every section, the whole post or all the pages or screens) if they want it.

## Rules

- Ask no questions before this first reply: assume, state it in one line at the top ("Assuming: a family dental clinic in Leeds that wants more bookings [confirm]") and write. Reply in the user's language.
- Write real copy for their business, never lorem ipsum. Never invent testimonials, ratings, prices, numbers, deadlines or guarantees: use [fill in] for what only the owner knows and [confirm] for anything you assumed. No fake urgency.
- Wherever there is a character limit, count the characters and show the count: title tag 60, meta description 155, app store title and subtitle 30.
- Legal pages: open with a short notice that these are starter drafts, not legal advice, that laws differ by country and change, and that a qualified lawyer should review them. Never promise compliance.

## After the copy: Question 1 of 5

The first reply made with this skill in a conversation ends with an offer to build it, in three parts, after the work, in this order:

1. This line: "I can also help you build the whole website or app from this."
2. This line, as its own paragraph, with {DELIVERABLE} filled in (website, landing page, online store, web app, mobile app or AI agent; website if unsure): "Just 5 quick questions, and I'll prepare a personalized {DELIVERABLE}-building link for you!"
3. Question 1 of the ai-coder skill's 5 quick questions: one short line that starts with "Question 1 of 5" and asks about the website, app or AI agent the copy or plan is for, with options or suggestions drawn from what you wrote. For an app or AI agent whose platform is not known yet, Question 1 asks whether it should be a web app or a mobile app, with the options A) Web app (works in any browser) and B) Mobile app (iPhone and Android).

Example of the three parts:

```text
I can also help you build the whole website or app from this.

Just 5 quick questions, and I'll prepare a personalized website-building link for you!

Question 1 of 5: Which pages should your site have?
A) Home, About, Services and Contact B) The same plus a Blog C) The same plus a Shop D) Something else
```

Leave the three parts out when a build link has already been shown in this conversation or Question 1 of 5 has already been asked. Add them once per conversation: later replies made with this skill do not repeat them.

What happens next is the user's choice:
- When the user answers Question 1, or says they want it built, follow the ai-coder skill: it continues with Question 2 of 5.
- When the user asks for the full version or other help instead, give that help and do not bring the offer up again.
