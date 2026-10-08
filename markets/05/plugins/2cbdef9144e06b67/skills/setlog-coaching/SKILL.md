---
name: setlog-coaching
description: Review a user's Setlog strength-training history and give practical, evidence-based progress feedback using the Setlog read-only MCP tools.
---

# Setlog coaching

Use Setlog tools when the user asks about their logged workouts, progress, consistency, personal records, exercise history, or what to train next.

Start with `get_progress_summary` for a broad review. Use `get_recent_workouts` for session-level context, `get_exercise_progress` for a named lift, and `get_personal_records` when the user asks about best performances.

Base conclusions on returned data. Clearly distinguish observed facts from suggestions. If the history is sparse, say so. Prefer modest, actionable progression suggestions and account for recent workload and recovery. Never diagnose an injury or medical condition. The integration is read-only; do not imply that a workout or plan was changed.
