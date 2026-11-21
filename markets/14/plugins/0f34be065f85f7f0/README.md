# MealSnap

Ask your assistant about your MealSnap food diary: look back at a week, find a past meal, or read a saved review. MealSnap's connection only reads. It can't add, change or delete anything in your diary. Calorie figures are estimates, not exact counts. Each meal's estimate is a range.

The plugin adds one remote MCP server, `https://api.mealsnap.app/mcp`, run by MealSnap.

## Connect your diary

MealSnap Pro is required, and you need MealSnap 3.3 or later on your iPhone. Install this plugin, then connect MealSnap from your assistant. Your assistant opens a MealSnap page that asks for a code. Get the code in MealSnap on your iPhone, under Settings, then Connected assistants. Choose Claude or ChatGPT there, or Connect a different tool for Claude Code, Codex and other tools on your computer. Type the code only on mealsnap.app, never into a chat.

In a Claude Code session, on version 2.1.275 or later, install it with:

```text
/plugin install mealsnap --marketplace xtazz/mealsnap-assistant
```

On older versions, run `/plugin marketplace add xtazz/mealsnap-assistant`, then `/plugin install mealsnap@mealsnap-assistant`. Then run `/mcp` to sign in.

Install steps for Claude, Claude Code, Codex, ChatGPT and other assistants are in the [MealSnap assistant README](https://github.com/xtazz/mealsnap-assistant#install). The [connection guide](https://mealsnap.app/connect) walks through adding MealSnap to Claude or ChatGPT by its address.

## Try asking

- How was my week of eating?
- Which foods show up most often?
- What did my last weekly review say?

## Data and controls

The assistant reads the diary you connect: meals, drinks, activities and day ratings, the hunger and fullness you recorded, estimated calorie ranges, summaries and trends, and your saved weekly and monthly reviews.

It can also read the body measurements you recorded.

Photos are on when you connect. The assistant can see the photos you added to meals, drinks and activities, unless you turn photos off for that connection. Body photos are never sent. MealSnap doesn't send your name, email address, date of birth, saved locations or body photos through a connection. What you wrote in notes, descriptions and tags, and the text of your reviews, can still be read, including any names or places in it.

Turn photos off or disconnect in MealSnap, under Settings, then Connected assistants. Data already read can remain in your assistant's conversations under that provider's policies and controls.

MealSnap provides a food record, not medical or nutritional advice. See the [privacy policy](https://mealsnap.app/privacy), [service terms](https://mealsnap.app/terms), and [setup and support page](https://mealsnap.app/connect). Contact support@mealsnap.app for help.
