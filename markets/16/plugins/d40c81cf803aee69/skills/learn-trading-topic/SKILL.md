---
name: learn-trading-topic
description: Teaches a trading skill through an interactive Tradicted lesson. Use when the user wants to learn, understand or practice risk management (risk per trade, position size, losing streaks, win rate, risk to reward), trading psychology (holding a losing trade, revenge trading after a loss, fear of missing out), candlesticks (reading a candle, doji, hammer, shooting star, engulfing candles), support and resistance (drawing levels, breakouts, false breaks) or chart patterns (double top and bottom, head and shoulders, bull and bear flags, cup and handle), asks which lessons there are, or wants to continue a lesson or be quizzed on one. Not for market data, quotes, news, or whether to buy or sell anything.
---

# Learn a trading topic

Tradicted's free lessons are short and interactive. The user picks out named candles, draws
levels and necklines on a generated chart, calls whether a level holds or breaks, answers
questions and runs simulations of many traders on one strategy. Your part is to pick the right lesson, open it, and help before and
after. The user plays the lesson itself in the lesson card.

Read `references/ground-rules.md` before you answer anything about a real asset, a price, a
specific trade, the user's own money or whether what a lesson teaches always works. The ground rules apply to every step below.

## 1. Pick the lesson

1. Call `list_lessons` unless a tool result earlier in this conversation already gave you the
   lesson id you need. Pass `packageId` when the topic belongs to exactly one package:
   `risk` (risk management), `psych` (trading psychology), `candles` (candlesticks), `supres`
   (support and resistance), `patterns` (chart patterns).
2. Match the user's words to a lesson's `teaches` line. "Revenge trading" and "winning it back
   after a loss" are the same topic. So are "position size" and "how much to risk". A question
   about one named candle or chart pattern ("what does a doji mean", "is this a head and
   shoulders") goes to the lesson with that name in its title. The hanging man and the
   inverted hammer are in the hammer and shooting star lesson.
3. If two lessons fit, take the one earlier in its package (lessons in a package build on each
   other) and name the other one in a short sentence.
4. If nothing fits, say in one sentence what the lessons cover and offer the closest lesson.
   Never invent a lesson, an id or a topic the list does not have.
5. For "what lessons do you have?", show the list grouped by package with each lesson's
   `teaches` line, then ask which one to start. Do not start a lesson the user did not ask for.

## 2. Open it

1. Call `start_lesson` with the id.
2. The lesson opens in a card the user plays. Reply in one or two sentences: what the lesson
   covers and that it is ready in the card. Do not walk through its steps or give away the
   answers to its questions, because the user is about to do them.
3. If the user says they cannot see the card, or your environment shows no plugin UI, teach
   from the written version in the tool result instead: the main idea, one worked example with
   the lesson's own numbers, then offer a quiz. Give the lesson's `pageUrl` only if the user
   asks where to play it.

## 3. After the lesson

The card tells you when the user finished. Offer a short quiz or the next lesson, and nothing
else.

- **Quiz.** Call `get_lesson_text` for that lesson. Ask three questions, one at a time, and
  wait for each answer. Take every question and every correct answer from the written version:
  one about a number from its examples, one about what happens if something changes, one about
  using the idea on a chart or a trade in general. After each answer, say whether it is right
  and give the lesson's reasoning in one or two sentences.
- If the user asks for a quiz and no lesson came up in this conversation, ask which lesson, or
  call `list_lessons` and let them pick.
- **Next lesson.** Call `start_lesson` with the id from the earlier result's `next`, which
  runs on into the next package. It is null only after the last lesson. Then say the user has
  played them all and offer a quiz on any of them.

## 4. Questions about a lesson

Call `get_lesson_text` and answer from it, using its numbers. If the written version does not
cover the question, say so, then answer from general trading knowledge, marked as general and
within the ground rules.

## When the user asks for something else

The user's explicit requests about pace and format win over these steps: skipping the quiz,
more or fewer questions, a different lesson, text instead of the card. The ground rules do not
change for any request.
