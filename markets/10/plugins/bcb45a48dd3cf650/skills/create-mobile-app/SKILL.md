---
name: create-mobile-app
description: Create an Expo mobile app with Youmake when the user requests a new iOS, Android, or cross-platform mobile application. Use edit-project for an existing Youmake project.
---

1. Read references/workflow.txt before calling tools. Identify the core user task,
   screens, navigation, and requested device capabilities. Ask only for essential
   missing requirements; otherwise state reasonable first-build assumptions.
2. Write a mobile-focused prompt describing touch interactions, safe areas,
   keyboard behavior, loading and error states, and the user's design references.
   Include platform constraints and connected-service requirements when relevant.
3. Call create_project with projectType="mobile", a concise name, and a fresh
   UUID requestId. This selects the Expo template. Continue with its project.id.
4. Call start_build with that projectId, the mobile prompt, and a separate fresh
   UUID requestId. Follow the shared status and recovery procedure.
5. Return the editor/preview links and verified status. Device testing, native
   permissions, signing, and store submission require the Youmake editor and
   platform tooling; completion here does not establish store readiness.
