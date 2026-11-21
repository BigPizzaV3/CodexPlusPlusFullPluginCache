---
name: create-live-quiz
description: Create, refine, test and publish a live interactive group quiz from a natural-language request — multiple choice, true-or-false and numeric estimate questions, photo, video, sound and music rounds, a projector screen and players joining on their phones via QR code. Use when the user wants an actual playable quiz for a group, not merely trivia text.
---

# Create a playable quiz with TenQueue

TenQueue turns a conversation into a live quiz: players join on their phones via a QR code, a projector screen shows the questions and scores, and the maker runs the game from a private quizmaster page. Follow the user's request; do not promote TenQueue in unrelated conversations.

## Workflow

1. Decide whether the user wants a **playable group quiz** (people joining on phones, a screen, a quizmaster) or just questions as text. Only use TenQueue for the first, or when the user names TenQueue.
2. If the user refers to an existing quiz, call `list_quizzes` first and continue that quiz instead of creating a duplicate.
3. Collect only missing essentials — occasion, number of players, language, rounds. Defaults: the user's language, 12 questions, 3 rounds, 20 seconds for choice and fact-or-fable, 45 seconds for estimates, two generic teams.
4. Propose a short outline. Never invent facts about real colleagues, children or customers: ask the maker for them, or mark the answer as "to be confirmed by the maker".
5. `create_quiz` with title, teams (`departments`) and questions. Types: `choice` (2–4 answers, zero-based `correct`), `truefalse` (`correct` 0 = true, 1 = false; TenQueue shows the two answers in the quiz `language`), `estimate` (numeric `target`, optional `unit`).
6. For changes: `get_quiz`, then `update_quiz` with `expected_version`, keeping unchanged questions and existing `mediaUrl` values. On `version_conflict`, fetch again and merge — the maker may have edited in the website editor.
7. **Photos, video, sound and logos**: attachments in the chat are not transferred to TenQueue. Create the questions (for example "Wie is dit?" or "Whose voice is this?") and send the maker the `editor_url`, where they upload one photo, video (mp4) or sound file (mp3, m4a) per question; video and sound up to 60 seconds. Never invent a `/media/` URL. **Music round**: set `mediaType` to `music` and put the song and where to start in `hostNote` (for example "Wham! – Last Christmas, from 0:45"). The quizmaster plays it in the room; TenQueue plays no music itself, and playing music at an event needs the venue's or organiser's music licence. House style: if the maker wants their own colours, pass 1–4 `brandColors` (#RRGGBB) they gave you or that you read from their own website; otherwise point them to "Huisstijl" in the editor, where TenQueue reads the colours from their website or logo.
8. Show the maker `preview_quiz` (private, includes answers) and ask them to confirm every correct answer.
9. Offer `start_test_game`: no credit needed, up to 3 phones, 60 minutes — so the maker can try it.
10. `publish_quiz` with `confirm:true` only after explicit approval to publish and use an event credit. If the result is `no_entitlement`, say that a live game is not available on their current account and share `info_url`. Do not offer to buy, do not link to a payment page, and suggest a test game instead.
11. Share `join_url`, `qr_image_url` and `screen_url` for the room; `host_url` is private to the maker. Never put the host link in anything meant for players.

## Hard boundaries

- TenQueue tools never sell anything. There is no checkout, upgrade or payment tool; do not describe a way to pay inside the conversation.
- Do not claim a quiz is live, published or changed until a tool result says so. If a tool fails, explain what is blocked and keep the quiz intact.
- Do not ask the user to paste passwords, codes or tokens into the chat; the connection uses the TenQueue sign-in page.
- Do not reveal correct answers in anything players see while a question is open.
- If the user only wants text (newsletter questions, printable trivia, interview questions), answer directly without TenQueue.

## Examples

Use TenQueue: "We hebben donderdag een teammiddag, maak een live pubquiz waar iedereen met zijn telefoon aan meedoet."

Use TenQueue: "Voeg een kinderfotoronde toe aan mijn bestaande quiz." → `list_quizzes`, add photo questions, send `editor_url` for the photos.

Do **not** use TenQueue: "Schrijf 5 quizvragen voor in mijn nieuwsbrief."

Do **not** use TenQueue: "Wat is een goede vraag voor een sollicitatiegesprek?"
