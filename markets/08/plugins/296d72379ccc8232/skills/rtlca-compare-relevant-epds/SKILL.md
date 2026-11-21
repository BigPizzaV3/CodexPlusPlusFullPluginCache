---
name: rtlca-compare-relevant-epds
description: >-
  Use when a user asks to find relevant or alternative EPDs for an RTLCA project
  inventory material, compare them against the current mapping, rank by project
  GWP impact, or show the RTLCA EPD comparison UI/resource.
---

# RTLCA Compare Relevant EPDs

Use RTLCA MCP tools to identify relevant EPD candidates for a project material, then compare their project-level GWP impact against the current mapping.

## Workflow

1. Resolve the project.
   - Use `rtlca_list_projects`.
   - Match the user's project name to a project ID.
   - If multiple projects match, ask the user to choose.

2. Resolve matching inventory materials.
   - Use `rtlca_get_inventory_materials` with `projectId`, `search` and `detail: "detailed"`.
   - If multiple rows match, compare each row unless the user specifies one.
   - Record `materialId`, `identifier`, `typeIdentifier`, `branchName`, `category`, preferred quantity/unit, `lifeTime`, and current `mappedEpd`.

3. Build the EPD search description.
   - Combine `identifier`, `typeIdentifier`, `category`, and `branchName`.
   - Include useful English/Danish synonyms if obvious.
   - Prefer the material's preferred declared unit.
   - Use `rtlca_find_relevant_epd_materials` with `count: 10` by default.

4. Check comparison preconditions.
   - Do not compare if quantity is zero.
   - Do not compare if `lifeTime` is unset.
   - Report blocked rows clearly.

5. Confirm temporary-write comparison.
   - `rtlca_compare_epds` temporarily changes project mappings and restores them afterward.
   - If the user explicitly asks to compare, treat that as confirmation.
   - Otherwise ask before calling it.

6. Compare EPDs serially.
   - Run `rtlca_compare_epds` once per matching material row.
   - Do not run comparisons in parallel because the tool temporarily changes project mapping state.
   - Pass up to 10 EPD IDs from `rtlca_find_relevant_epd_materials`.
   - After each run, check `restoration.status`.
   - If restoration is not `restored`, lead with that warning.

7. Interpret results.
   - Use `rtlca_compare_epds.rows` as the authoritative project-impact ranking.
   - Remember the current mapping may appear in `rows` even if it was not in the candidate list.
   - Distinguish the overall best row, the best alternative excluding `isCurrent: true`, and whether alternatives improve, tie, or worsen the baseline.
   - Flag suspicious current mappings, such as a pure material mapped to a construction assembly.

8. Present results.
   - Prefer showing the UI/resource returned by `rtlca_compare_epds` when available.
   - Also provide a concise text summary.
   - For multiple rows, use a table with inventory row/category, current mapping, best alternative, GWP total, delta, delta percent, and restoration status.

## Output Rules

If the current mapping is best, say "current mapping remains best among the relevant shortlist."

If an alternative is better, name the alternative, GWP total, delta, and delta percentage.

If the current mapping looks semantically wrong, call it out separately, even if the GWP result is close.

Always mention skipped candidates or blocked rows.
