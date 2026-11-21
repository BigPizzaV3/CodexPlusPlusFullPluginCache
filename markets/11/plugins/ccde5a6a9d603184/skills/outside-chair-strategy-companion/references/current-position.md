# Explain the current position

1. After workspace selection, call `get_attention_queue` and `get_strategy_context` once. In a workspace with more than one active member, also call `get_team_context` once when available. Call `get_approved_review` only when the user asks about the frozen review itself.
2. Answer in this order:
   - current priorities and material change;
   - challenged or invalidated assumptions;
   - decisions and open actions;
   - open or contested deliberations, preserving attribution and dissent;
   - up to five highest-severity attention items;
   - interpretation, clearly labelled, only if useful.
3. Collapse lower-priority items into a count and offer them on request.
4. Never report a free-text signpost as crossed merely because it requires assessment.
5. Do not write during a current-position request unless the user separately approves a displayed proposal.
6. For broad language such as “pulse”, “signals”, “drivers”, “what changed?” or
   “what needs attention?”, answer directly under the natural headings `Current pulse`,
   `Important developments`, `Drivers`, `Watchpoints` and `Decisions required`,
   omitting empty headings when that improves clarity. Do not name
   observations, signposts or evidence as object types unless naturally helpful.
