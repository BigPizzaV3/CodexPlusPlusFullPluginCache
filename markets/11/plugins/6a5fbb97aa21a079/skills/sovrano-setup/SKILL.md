---
name: sovrano-setup
description: Get started with Sovrano after installation or when no concrete sponsorship task has been supplied. Begins with the user's real sponsorship decision, resolves workspace onboarding and hands the work to Sovrano Companion. Not for a concrete task that can start immediately or for marketing work unrelated to sponsorship.
---

# Get started with Sovrano

Start useful work, not a feature tour.

## First move

If the user supplied a sponsorship task, proposal, package, budget, market question or decision material, acknowledge the goal and hand off immediately to the Sovrano Companion skill.

Otherwise say that Sovrano helps a team keep one sponsorship situation and its evidence together through **Frame → Evaluate → Prepare → Review**. End with one question:

**What sponsorship decision are you working on, and are you buying or selling the rights?**

## Profile and workspace

Call `get_sovrano_profile` once the user begins. Follow its onboarding journey:

- `new`: use the real decision to establish a workspace and Frame. Create the workspace only after the user chooses its name, kind and member type and approves the save.
- `invited`: give only the missing workspace, role and decision-right orientation, then continue with active or assigned work.
- `select_workspace`: list exact matches and ask which company or client workspace to use.
- `returning`: continue from the selected workspace without repeating the introduction.

If authentication is required, direct the user to the host's Sovrano sign-in screen. Normal users use the email-code route. Passwords, email codes, tokens and consent stay in that screen rather than chat.

## Handoff

Continue under the Sovrano Companion skill. Onboarding is complete when the user has a selected workspace and a saved useful Frame or evaluation, not when every feature has been explained.
