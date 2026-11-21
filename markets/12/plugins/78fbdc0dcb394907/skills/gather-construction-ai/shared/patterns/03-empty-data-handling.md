# Pattern 3: Empty Data Handling

When an API call returns no data for the requested period/project, do not silently produce an empty report. Instead:

1. State clearly: "No [data type] found for [project] between [dates]"
2. Suggest possible causes:
   - Wrong project? (list available projects)
   - Wrong date range? (suggest trying a broader range)
   - Data not yet recorded? (e.g., progress data may not be entered for recent shifts)
   - Report not configured? (some dashboard reports require setup in Gather)
3. Offer to retry with different parameters

**Key rule:** An empty result is an answer, not an error. But it needs context so the user knows whether to adjust their query or investigate a data gap.
