---
name: get-started
description: Show the user their VibeDoctor projects and the health of one of them. Use when the user first connects VibeDoctor or asks how their project is doing.
---

# Get started with VibeDoctor

1. Call `vibedoctor_projects` to see the projects this account can use.
2. If there are none, tell the user to add a GitHub repository or website at https://app.vibedoctor.io and come back after its first scan finishes.
3. If there are several, ask which one, unless the conversation already names a repository. In a code checkout, `git remote get-url origin` names it.
4. Call `vibedoctor_status` with that project. Summarize in plain words: the overall score, how many critical and high findings are open, and the two or three files that need attention first. Use only what the tool returned.
5. Offer what can come next: checking changed files with `vibedoctor_check`, or exploring the code map with `vibedoctor_graph`.
