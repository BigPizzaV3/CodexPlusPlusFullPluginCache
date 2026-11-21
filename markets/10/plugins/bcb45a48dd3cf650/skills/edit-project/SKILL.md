---
name: edit-project
description: Continue or modify an existing Youmake website, mobile app, or slide deck when the user requests changes to its content, design, or functionality.
---

1. Read references/workflow.txt before calling tools. Resolve the target using a
   project ID already supplied by Youmake or list_projects. Use pagination when
   needed. If multiple projects fit the request, ask the user to choose.
2. Call get_project with the selected projectId. Proceed when canEdit is true;
   otherwise explain that editor access is needed. Preserve its projectType.
3. Write a prompt containing the requested change and the existing behavior to
   preserve. Obtain clarification before an ambiguous destructive change. Reuse
   the existing project rather than creating a duplicate.
4. Call start_build with that projectId, the edit prompt, and a fresh UUID
   requestId. Follow the shared status and recovery procedure.
5. Report the verified build status and editor/preview links. Describe the
   requested change as confirmed only if tool results or inspection establish it.
