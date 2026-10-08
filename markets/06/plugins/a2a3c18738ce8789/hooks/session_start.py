#!/usr/bin/env python3
import json

CONTEXT = (
    "Capability Orchestrator is available. For non-trivial user requests, "
    "first determine whether a specialist capability should handle the task. "
    "Prefer a direct specialist over a generic router, use the smallest "
    "effective set of capabilities, delegate only minimal relevant context, "
    "respect explicit user capability constraints, and never claim a "
    "capability ran unless it was actually invoked."
)

payload = {
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": CONTEXT,
    }
}

print(json.dumps(payload, ensure_ascii=False))
