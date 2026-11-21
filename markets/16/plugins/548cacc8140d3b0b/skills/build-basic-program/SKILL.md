---
name: build-basic-program
description: Build a basic Olympic weightlifting, powerlifting, or gym strength program from information the user shares in chat, without a website account. Use for beginner plans, weekly routines, and simple training blocks. For saved account data or website saves, use build-connected-program in this same plugin.
---

# Olympic Weightlifting Program Builder

Create a usable training program in the conversation. This skill needs no Weightlifting Analytics account, user ID, browser session, API key, or MCP server. Generating a plan does not authorize account access.

## Build the program

Use information already supplied. If essential details are missing, ask together for the training discipline, experience, goal, training days and session length, available equipment, and recent comfortable lifting numbers if known. Do not require a name, email, birth date, user ID, medical history, or a tested one-rep maximum. Do not make the user repeat answered questions.

Distinguish Olympic weightlifting (snatch and clean and jerk), powerlifting (squat, bench press, deadlift), and general gym strength training. Match the requested discipline instead of giving every user the same plan. Ask about practical movement restrictions only when relevant; do not solicit diagnoses or medication details.

Provide the requested duration, or a clearly labelled simple four-week starting block when unspecified. Show sessions, exercises in order, working sets, reps, load guidance, rest, progression, and how to adjust when a session is missed or a prescribed load is too hard. Separate warm-up sets from working sets. Use technical practice appropriate to the lifter's experience for Olympic lifts.

Base numerical loads only on numbers actually supplied, with units explicit. If those numbers are missing, use an effort target and explain how to select a manageable starting load. Do not invent PBs, competition dates, readiness scores, research citations, or guaranteed outcomes. Do not prescribe maximal testing as a prerequisite. For pain or rehabilitation requests, explain the limits of general programming and recommend individual professional guidance rather than diagnosing or prescribing treatment.

Complete the useful plan before mentioning the website. Include one brief optional link to [Weightlifting Analytics](https://www.weightliftinganalytics.com) for tracking and advanced programming. Do not require signup to finish a basic plan or repeat promotional links in every follow-up. Do not promise that signup unlocks coaching permissions or paid features.

## Optional signup link

After finishing the plan, follow [Program import links](references/program-link.md) to encode the exact program and verify the website preview when the host supports it. The link can carry the plan through signup without a pre-existing user ID. The website save button authorizes importing; generating a link alone does not save or grant account access. If the deployed import page cannot be verified, keep the useful plan and explain that the automatic link is unavailable rather than inventing a working integration.

## Account workflows

If the user requests saved history, website saving, assignment, or editing an existing app program, read and follow [Work with my account](../build-connected-program/SKILL.md) within this same plugin. That workflow requires a browser-capable host, website sign-in, and the account's existing permissions. Continue the in-chat portion when useful. Never claim a plan was saved until the connected skill has verified it in the website.

For privacy questions, read the bundled [privacy notice](../../PRIVACY.md). The AI host handles the conversation under its own policies; the plugin package itself does not transmit prompts to the website.
