---
name: get-started
description: First-run setup for the Project Simple plugin. Use when the plugin has just been installed or connected, when the user asks how to get started, or when no account or project id is known yet in this conversation.
---

Run this once after the user connects Project Simple. The goal is that the user sees their
projects and asks their first question.

1. Call `list_my_accounts_and_projects`. It returns the accounts the signed-in user belongs to and
   the projects in each one. Every other tool needs the ids it returns.
2. If it fails with "MCP is not enabled for this account", tell the user to ask their Project
   Simple administrator or support to switch the assistant feature on. Do not retry.
3. If it asks for sign-in, let the user sign in. Logins expire; that is expected.
4. Show the user the accounts and projects by name. If there is exactly one project, use it.
   If there are several, ask which one they want to work in and remember the choice for the rest
   of the conversation.
5. Briefly say what you can do here: find and read items, create and move work, plan and start
   sprints, check capacity and time off, manage goals and milestones, keep TODOs and ideas, and run
   retrospectives. Mention that you cannot delete items or epics and that you act with their own
   permissions.
6. Suggest three things to try:
   - "What am I working on?"
   - "What is in the current sprint for my team?"
   - "Show me item PS-142." (use the project's real key prefix if an item was already shown)

Then follow the `project-simple-rules` skill for everything that comes after.
