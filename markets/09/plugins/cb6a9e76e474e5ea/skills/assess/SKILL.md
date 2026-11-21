---
name: assess
description: >-
  Run or resume the TAOS assessment that builds the user's expertise profile.
  Invoke when the user has no profile, asks to be assessed, asks to set up TAOS,
  or the coach reports that no profile exists yet.
---

Build the user's Talent Augmentation OS profile through the connected `taos` MCP
server. The server runs the assessment; you conduct the conversation.

1. Call `talent_assess_start` with the user's name to begin or resume the
   assessment.
2. Ask the questions it returns one at a time, in a natural back-and-forth. Do
   not answer for the user or rush them; the value is in their own reflection.
3. Follow the tool's instructions to score the answers and create the profile.
4. When the profile is saved, tell the user it is ready and switch to coaching
   (invoke the `coach` skill).
