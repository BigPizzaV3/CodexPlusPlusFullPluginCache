---
name: create-website
description: Create a website with Youmake when the user requests a new landing page, business site, or web application. Use edit-project for an existing Youmake project.
---

1. Read references/workflow.txt before calling tools. Identify the site's purpose,
   audience, pages, and primary action from the conversation. Ask only for missing
   information that prevents a useful first build; otherwise state assumptions.
2. Write a build prompt with the requested content, visual direction, responsive
   behavior, and functional requirements. Distinguish requested integrations from
   features that can be built without connected services.
3. Call create_project with projectType="web", a concise name, and a fresh UUID
   requestId. Continue only after receiving a project.id.
4. Call start_build with that projectId, the build prompt, and a separate fresh
   UUID requestId. Follow the shared status and recovery procedure.
5. Return the resulting preview/editor links and verified status. Publishing and
   domain setup take place in the Youmake editor; a completed build is a preview.
