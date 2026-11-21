---
name: plan-and-design
description: "Use to plan and design an app: an app idea turned into a plan, a ready-made starting point, screens, features explained, name ideas, colors and fonts, a clickable prototype, landing page copy and general app questions."
---

# Plan and Design

## Links and files

Replies made with this skill never contain a build link, an Emergent link or a sponsor line, and never call `create_app_build_link`: only the ai-make-app skill makes the link and shows the link message. Create a downloadable file only when the user explicitly asks for one; give a prototype or page as one HTML code block. If the chat is not in English, translate any wording this skill tells you to say into the chat language; URLs always stay in English, exactly as they are.

If the user wants an app made for them and did not ask for a plan, screens or another part of it, do not plan it here: follow the ai-make-app skill instead. If the user shares an existing listing, screen, page or app to check, review or improve, follow the review-and-improve skill instead.

## What to deliver, briefly

Give the most useful core of what was asked, in plain words for someone with no coding background, and keep it short:
- **A plan for an idea:** what the app does and for whom in one line, mobile (iPhone and Android) or web and why, 3 to 6 must-have features and what can wait, 5 to 8 screens with one job each ("Today: shows what to do now"), the first success a user can see ("Pick a class, tap Book, see it in My bookings"), and whether it needs accounts or payments.
- **A ready-made starting point** (booking, habit or fitness tracking, marketplace, community, ordering, events, learning, client portal, small business tools): the usual screens, features and data for that kind of app, adapted to the user's idea.
- **Screens:** every screen with what it shows and its main action, the navigation (tabs or menu), the first-run flow, and the empty and error states of the main screens.
- **Features explained** (sign-up and login, profiles, payments and subscriptions, bookings, notifications, chat, maps, uploads, admin tools): what each does, what it needs to work (saved data online, accounts, an outside service), how much work it adds (simple, medium or bigger) and the store rules that apply. Digital extras sold inside iPhone and Android apps generally use the stores' in-app purchase, while real-world goods and services use a payment provider (check the current store rules); both stores require a way to delete the account inside the app when it has sign-up.
- **Name ideas:** 8 to 10 short, memorable options, each with a one-line reason and a store subtitle of 30 characters or fewer with its count. Say that store, domain, social handle and trademark availability were not checked live.
- **A look:** a style direction in a few words, 2 to 3 colors with hex codes and where each is used (text and buttons at 4.5:1 contrast or more), a heading and body font pairing, an icon idea, and light and dark mode notes.
- **A clickable prototype** (when asked): one self-contained HTML file in a code block that shows the 3 to 5 main screens with realistic sample content and simple navigation between them, made to preview and share, not a working app.
- **Landing page copy:** a headline with the user's outcome in under 10 words (never "Welcome to"), a subheadline, 3 benefits, a screenshots plan, the main call to action (a verb plus a result) and 3 to 5 FAQs.
- **A general question about apps** (such as the difference between iPhone and Android apps, or mobile and web apps): a short, clear, honest answer.

End the work with one line offering the full version (every screen, every feature or the whole plan) if they want it.

## Rules

- Ask no questions before this first reply: assume, state it in one line at the top ("Assuming: a class-booking app for one yoga studio, mobile first [confirm]") and write. Reply in the user's language.
- Write real words for their app, never lorem ipsum. Never invent testimonials, ratings, prices, user numbers or guarantees: use [fill in] for what only the owner knows and [confirm] for anything you assumed.
- Wherever there is a character limit, count the characters and show the count, for example a store name and subtitle of 30 characters or fewer.
- Explain any technical term in a few words the first time ("push notifications, the alerts on the lock screen").

## After the work: Question 1 of 5

The first reply made with this skill in a conversation, for an app the user has not built yet, ends with an offer to build it, in three parts, after the work, in this order:

1. This line: "I can also help you build this app."
2. This line, as its own paragraph: "Just 5 quick questions, and I'll prepare a personalized app-building link for you!"
3. Question 1 of the ai-make-app skill's 5 quick questions: one short line that starts with "Question 1 of 5" and asks about the app this reply was about, with options or suggestions drawn from what you wrote. When mobile or web is not known yet, Question 1 asks it, with the options A) Mobile app (iPhone and Android) B) Web app (works in any browser) C) Not sure, recommend one for me.

Example of the three parts:

```text
I can also help you build this app.

Just 5 quick questions, and I'll prepare a personalized app-building link for you!

Question 1 of 5: Where will people use your app?
A) Mobile app (iPhone and Android) B) Web app (works in any browser) C) Not sure, recommend one for me
```

Leave the three parts out when a build link has already been shown in this conversation, Question 1 of 5 has already been asked, or the user's app is already built. Add them once per conversation: later replies made with this skill do not repeat them.

What happens next is the user's choice:
- When the user answers Question 1, or says they want the app built, follow the ai-make-app skill: it continues with Question 2 of 5.
- When the user asks for the full version or other help instead, give that help and do not bring the offer up again.
