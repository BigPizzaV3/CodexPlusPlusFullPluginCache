---
name: setup
description: "Set up Donkey Cut after installing the plugin: confirm the connected account, then open or create the first cloud project. Use right after installation or when the user asks how to start with Donkey Cut."
---

# Getting started with Donkey Cut
1. Call account_status. Tell the user their plan, AI credit balance and cloud storage in one line. Editing, previews and exports are free; hosted AI generation spends credits.
2. Call list_projects. When projects exist, name the three most recent and ask which to open. When there are none, ask what the video is for and its shape (9:16 for TikTok, Reels and Shorts, 16:9 for YouTube, 1:1 square), then call create_project.
3. Call open_project for the chosen project. The editor card holds the timeline, media panel and preview; keep it open while editing.
4. Ask the user to attach footage or paste a link, and bring it in with import_media.
Projects saved on a Mac or in a browser reach ChatGPT once the user saves them to the cloud in Donkey Cut. Ask before creating a project the user did not request.
