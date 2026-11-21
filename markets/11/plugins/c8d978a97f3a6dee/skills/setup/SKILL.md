---
name: setup
description: First-run setup for the CmdBrief plugin. Checks that CmdBrief on the user's Mac is reachable, lists its workspaces and shows the user how to plan and send a project.
---

# Set up CmdBrief

1. Call `cmdbrief_home`. If it reports CmdBrief is not running, tell the user
   what CmdBrief needs, in three short lines:
   - CmdBrief for Mac, open and signed in to the same CmdBrief account they
     connected here.
   - **ChatGPT in the cloud** turned on in CmdBrief's Settings > Account.
   - Then ask again. Plans sent before that wait for CmdBrief for up to 7
     days.
2. Otherwise tell the user which workspaces CmdBrief has, in one line.
3. Explain the flow in three short lines:
   - Ask me to plan a project; I open the Project plan beside the chat.
   - Edit it there, then press **Send to CmdBrief** or ask me to send it.
   - Confirm it in CmdBrief and press Start. Nothing starts before that.
4. Offer a first prompt, for example "Plan a small landing page for my side
   project", and mention the CmdBrief entry in the sidebar for crew status.
