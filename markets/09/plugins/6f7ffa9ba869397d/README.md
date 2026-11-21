# CineFlo for ChatGPT and Codex

Plan a film production with the assistant in your [CineFlo](https://cineflo.com) projects. This plugin pairs the CineFlo connector with skills that know how a production is prepared, so the assistant works the way a first AD, a script supervisor or a line producer would, not just tool by tool.

## What it does

- **Build a shot list.** The assistant checks how the project will be shot (coverage style, cameras, lenses, aspect ratio), asks once if that isn't known yet, reads the scene, and proposes coverage in your shot numbering before saving it.
- **Break down the script.** The assistant tags cast, props, wardrobe, vehicles, effects and the rest, scene by scene, reusing the elements already in your breakdown.
- **Schedule shoot days.** The assistant groups unscheduled scenes by location, time of day and cast, and lays them onto shoot days on the stripboard.
- **Prep a call sheet.** The assistant drafts a day's call sheet from the stripboard, with call times, cast statuses and locations. It never sends it: you send from CineFlo.
- **Review the budget.** The assistant reads the cost report and explains where you are over, where money is committed and what is left.
- **Start a project.** The assistant creates a project and gives you the link to import your screenplay.
- **Handle a script revision.** After a new draft is imported, the assistant shows which scenes changed and what that touches in the breakdown, shot lists and schedule, then updates what you agree to.
- **Track the shoot day.** Tell the assistant "we got 4A" or "4C needs another take" and it records it, says whether the day will make it, and moves unfinished scenes when you agree.
- **Build a prep checklist.** The assistant turns the breakdown and schedule into department to-do lists, with owners and due dates ahead of each shoot day.
- **Scout locations.** The assistant logs recce notes in the form the crew needs (power, access, noise, sun path), compares options, and links scenes to places.
- **Make a lookbook.** The assistant builds a mood board for the film, a location or a character, with notes, colour palettes and the references you name.
- **Set up cast and crew.** The assistant numbers the cast the call-sheet way, builds the crew list by department, and orders it as call sheets print.
- **Get connected.** When CineFlo isn't connected yet, the assistant still does the work in the chat, then explains what CineFlo is and how to connect it.

## Use it

**You need a CineFlo account on Pro.** Connecting an assistant is part of CineFlo Pro, which starts with a free trial. No account yet? You can create one on the sign-in page in step 1, with Google, Apple or an email address, and start the trial from there. Without CineFlo connected, the assistant still helps in the chat and tells you how to connect.

1. Install the CineFlo plugin in ChatGPT or Codex and complete its connection sign-in flow.
2. On CineFlo's consent page, choose which projects and tabs the assistant can view or edit. Manage access in CineFlo under Settings → Privacy & Data → Connected Apps.
3. Ask for a production task, such as “Build a shot list for scene 12” or “Which scenes are not scheduled?”

Version 1.4.6 includes the 13 supplied workflows and the existing general production skill. It uses CineFlo's existing Streamable HTTP MCP endpoint. Workflows check the connected tool schemas and provide drafts when a required write tool is unavailable. No credentials or project data are included.

## Data

The skills are instructions only: this plugin contains no scripts and runs nothing on your computer. The assistant reaches your projects through the CineFlo connector at `https://mcp.cineflo.com/mcp`, which is run by CineFlo (Neon Media LLC) and only reaches the projects and tabs you share with it. Contact details, pay rates and uploaded files are never shared with the assistant, nothing is sent to anyone, and the assistant asks before deleting anything you didn't name, because deleting can't be undone. See [How Connected Apps work](https://cineflo.com/connected-apps/) and the [CineFlo privacy policy](https://cineflo.com/privacy-policy/).

## Support

Questions or problems: [cineflo.com/contact](https://cineflo.com/contact/) or hello@cineflo.com.
