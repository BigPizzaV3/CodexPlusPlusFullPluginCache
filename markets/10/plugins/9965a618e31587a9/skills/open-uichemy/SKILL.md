---
name: open-uichemy
description: Open the UiChemy dashboard, a project's canvas editor, or a page preview inside the chat as the built-in UiChemy panel. Use when the user says open dashboard, open UiChemy, show my projects or sites, open the editor, open or show a project, show the preview, or wants to see a change. Never open app.uichemy.com in a browser for this.
---

Use this skill whenever the user wants to see UiChemy itself: the dashboard, a project, the editor or a preview.

UiChemy has its own built-in panel. Open it with the UiChemy tools, not with a browser, computer-use or web tool.

1. Dashboard ("open dashboard", "open UiChemy", "show my projects/sites"): call `uichemy_open_projects`. It takes no arguments.
2. A project in the editor ("open my bakery site", "open the editor"): find the id with `uichemy_list_projects` if needed, then call `uichemy_open_preview` with `projectId`.
3. A full-page preview of one page ("show me the Home page", "preview it"): call `uichemy_open_preview` with `projectId`, `view: "preview"` and `pageName`.
4. After you change a project, call `uichemy_open_preview` for it so the user sees the result.

Rules:
- Do not open https://app.uichemy.com, its dashboard or its editor in a browser, an in-app browser or a computer-use tool. The panel is already signed in as the user.
- Only if the UiChemy panel tools are missing or return an error: say so in one line, then give the user the link https://app.uichemy.com to open themselves. Do not open it for them.
- A browser is still right for the user's own WordPress site (see `deploy-to-own-wordpress`), never for the UiChemy app.
