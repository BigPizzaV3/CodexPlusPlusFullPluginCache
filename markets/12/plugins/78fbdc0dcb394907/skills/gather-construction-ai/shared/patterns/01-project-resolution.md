# Pattern 1: Project Resolution

Every skill that accesses project data must resolve which project the user means. Follow this sequence:

1. Check `the user’s request` for a project name
2. If found, call `getMyProjects` and fuzzy-match against the argument
   - If exactly one match → use it
   - If multiple matches → show them and ask the user to pick
   - If no match → call `getProjects` (all workspace projects) and try again
3. If `the user’s request` has no project name:
   - Call `getMyProjects`
   - If the user has exactly one project → use it automatically
   - If multiple → list them and ask which one
4. Once resolved, store the project UUID and name for all subsequent calls in the same skill run

**Key rule:** Never guess. If ambiguous, ask. Getting the wrong project means every subsequent API call returns wrong data.
