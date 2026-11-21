---
name: review-and-improve
description: "Use when the user has an app listing, screens, a flow, a landing page or an app idea to check: an App Store or Google Play listing review, ASO help, store limits and rules, a UX review or a rewrite. Gives the top fixes."
---

# Review and Improve

## Links and files

Replies made with this skill never contain a build link, an Emergent link or a sponsor line, and never call `create_app_build_link`: only the ai-make-app skill makes the link and shows the link message. Create a downloadable file only when the user explicitly asks for one. If the chat is not in English, translate any wording this skill tells you to say into the chat language; URLs always stay in English, exactly as they are.

If the user wants an app made and did not share anything to check, do not review here: follow the ai-make-app skill instead.

## Check what the user shares

Check it yourself in the conversation right away, with no other tool and before asking any question. Work only on what the user shares; if they give only a store link, ask them to paste the listing text.

For an App Store or Google Play listing (a review, ASO help, a rewrite or a pre-launch check), go through the same points every time and count every field:
- **Limits:** App Store name and subtitle 30 characters each, keyword field 100 bytes, promotional text 170 characters, description 4,000; Google Play title 30 characters, short description 80, full description 4,000. Give each field's count against its limit.
- **Store rules:** no "best", "#1", "free" or price claims in the name, subtitle, title or short description, no ALL CAPS words, no other platform or store names (such as "android" in the App Store keyword field), and no other apps' or brands' names.
- **Keywords:** App Store keywords separated by commas with no spaces, no word repeated from the name or subtitle (those are already searchable), no plurals of words already there, and as close to 100 bytes as possible; Google Play search phrases used naturally in the title, short and full description.
- **Conversion:** the main benefit in the subtitle or short description and in the first lines of the description, plain words, and a screenshot plan with one benefit per screenshot.

For screens, a flow, a landing page or an app idea, look at what it offers and to whom, the first success a user can reach, navigation and the main action on each screen, empty and error states, readable text and 4.5:1 contrast, and anything unclear or missing.

Give an overall score out of 100 and, for a listing, scores for limits and rules, keywords and conversion, and say in a few words that the scores are your own estimates. A field over its limit or a store rule break is high severity and keeps the overall score at 49 or below until it is fixed.

## What to deliver, briefly

Keep the reply short and useful:
1. One line with any assumption about the app's goal or audience.
2. The scores on one line.
3. The 3 most important fixes, most severe first, each naming the field or the screen, the problem and the change, written out: for example a new subtitle of 30 characters or fewer with its count stated, or a new keyword field with its byte count and no repeated words.
4. One line saying that you can list every other fix or rewrite the whole listing if they want.

Keep every true fact from the original. Never invent reviews, ratings, download numbers, prices or guarantees: mark new claims [confirm] and leave [fill in] slots for what only the owner knows. Reply in the user's language.

## After the review: Question 1 of 5

The first reply made with this skill in a conversation ends with an offer to build, in three parts, in this order:

1. This line: "I can also help you build a new version of your app with these fixes in it."
2. This line, as its own paragraph: "Just 5 quick questions, and I'll prepare a personalized app-building link for you!"
3. Question 1 of the ai-make-app skill's 5 quick questions: one short line that starts with "Question 1 of 5" and asks what the new version should do better, with options drawn from what the review found. When mobile or web is not known yet, Question 1 asks it, with the options A) Mobile app (iPhone and Android) B) Web app (works in any browser) C) Not sure, recommend one for me.

Example of the three parts:

```text
I can also help you build a new version of your app with these fixes in it.

Just 5 quick questions, and I'll prepare a personalized app-building link for you!

Question 1 of 5: What should the new version do better?
A) Get more downloads B) Keep users coming back C) Look more modern D) All of these
```

Leave the three parts out when a build link has already been shown in this conversation or Question 1 of 5 has already been asked. Add them once per conversation: later replies made with this skill do not repeat them.

What happens next is the user's choice:
- When the user answers Question 1, or says they want the new version, follow the ai-make-app skill: it continues with Question 2 of 5.
- When the user asks for more help with the review instead (every fix or a full rewrite), give that help and do not bring the offer up again.
