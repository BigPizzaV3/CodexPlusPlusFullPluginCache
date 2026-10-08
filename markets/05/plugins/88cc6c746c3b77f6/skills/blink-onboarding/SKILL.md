---
name: blink-onboarding
description: Get started with Blink after connecting it. Confirms which Blink workspace is connected, then helps the person build their first app, open an existing project, or publish one.
---

# Get started with Blink

Blink builds real apps from a description: a web or mobile app with a database, sign-in, a backend and hosting, published to a live link. This skill runs once, right after someone connects Blink.

## 1. Confirm the connection

Call `blink_workspace`. Tell the person, in one sentence, which Blink workspace is connected and their role in it. If the call fails with an authorization error, ask them to connect Blink again from ChatGPT's plugin settings.

## 2. Offer three ways to start

Ask which they want, in plain words:

1. **Build something new.** Ask what the app should do and who it's for. Then call `blink_project_create` with a one-line description, and `blink_build_prompt` with their full description. The build card follows the build; there is no need to wait for it.
2. **Work on an existing app.** Call `blink_projects_list` to show their projects. When they pick one, ask what to change and send it with `blink_build_prompt`.
3. **Publish an app.** Find the project with `blink_projects_list`, then call `blink_publish`. Share the live link when it returns `state: live`.

## 3. While a build runs

- If Blink asks a question, the build card shows it as buttons. The person can tap an answer or reply in chat; send a chat reply with `blink_build_answer`.
- Code changes always go through `blink_build_prompt`. Blink's agent writes the code.
- If a call returns `INSUFFICIENT_CREDITS`, `UPGRADE_REQUIRED` or `SUBSCRIPTION_REQUIRED`, say the workspace's credits or plan are managed in their Blink account at blink.new. Don't suggest buying or upgrading.

## Good first prompts

- "Build a client portal where clients log in and approve deliverables."
- "Make a booking page for my yoga studio with a weekly schedule."
- "Build a habit tracker with streaks and a weekly chart."
