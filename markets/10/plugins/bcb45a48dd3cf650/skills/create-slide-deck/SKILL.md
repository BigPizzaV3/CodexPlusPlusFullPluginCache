---
name: create-slide-deck
description: Create a presentation with Youmake when the user requests a new pitch deck, lesson slides, sales presentation, or slide-based report. Use edit-project for an existing Youmake deck.
---

1. Read references/workflow.txt before calling tools. Identify the audience,
   purpose, desired length, and supplied source material. Ask for essential missing
   content; otherwise state an outline and reasonable slide-count assumption.
2. Write a slide-by-slide build prompt with a clear narrative, concise headlines,
   visual guidance, and supplied data. Label placeholders for missing metrics and
   sources; preserve the distinction between supplied facts and proposed copy.
3. Call create_project with projectType="slides", a concise name, and a fresh
   UUID requestId. Continue only after receiving the deck's project.id.
4. Call start_build with that projectId, the presentation prompt, and a separate
   fresh UUID requestId. Follow the shared status and recovery procedure.
5. Return the preview/editor links and verified status. Slide export and sharing
   are completed in the Youmake editor; these tools do not return a PPTX or PDF.
