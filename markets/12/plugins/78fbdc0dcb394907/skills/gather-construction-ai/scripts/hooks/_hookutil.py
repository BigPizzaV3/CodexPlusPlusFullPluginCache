"""Shared helpers for Gather plugin PostToolUse command hooks.

Deterministic hook: no model call. Rule P3.6 - PostToolUse hooks are command
type unless justified in writing.
"""
import json
import sys


def read_input():
    """Read and parse the hook JSON payload from stdin. Never raises."""
    try:
        raw = sys.stdin.read()
        return json.loads(raw) if raw else {}
    except Exception:
        return {}


def extract_tool_response(payload):
    """Normalize MCP text/structured content and Gather response envelopes."""
    value = payload.get("tool_response")
    for _ in range(12):
        if isinstance(value, str):
            parsed = _try_json(value)
            return value if parsed is None else _unwrap(parsed)
        if isinstance(value, dict) and value.get("isError"):
            return None
        if isinstance(value, dict) and "structuredContent" in value:
            value = value["structuredContent"]
        elif isinstance(value, dict) and isinstance(value.get("content"), list):
            value = value["content"]
        elif isinstance(value, list) and value and all(isinstance(x, dict) and x.get("type") == "text" for x in value):
            value = "\n".join(x.get("text", "") for x in value)
        else:
            return _unwrap(value)
    return None


def _unwrap(value):
    for _ in range(12):
        if not isinstance(value, dict):
            break
        if "data" in value and ("_meta" in value or set(value).issubset({"data", "pagination", "success"})):
            value = value["data"]
        else:
            break
    return value


def _try_json(text):
    try:
        return json.loads(text)
    except Exception:
        return None


def safe_exit(lines):
    """Print at most the given lines (list of str) and exit 0. Silent if empty."""
    try:
        if lines:
            print("\n".join(l for l in lines if l))
    except Exception:
        pass
    sys.exit(0)
