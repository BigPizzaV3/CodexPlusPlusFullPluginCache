"""Bounded JSON projection: ignored values are scanned, never JSON-decoded.

Raw input bytes still enter memory. This is minimisation, not a claim that a
mixed record file can be read without encountering private bytes.
"""
from __future__ import annotations

import json
import re

from .storage import WeatherError, digest

TEXT = ("text", 256)
IDENTIFIER = ("text", 96)
NUMBER = ("number", 128)
FLAG = ("bool", 8)
COUNT_FIELDS = {key: NUMBER for key in (
    "input_tokens", "output_tokens", "cached_input_tokens", "reasoning_output_tokens",
    "total_tokens", "cache_write_input_tokens", "inputTokens", "outputTokens",
    "cachedInputTokens", "reasoningOutputTokens", "totalTokens", "cacheWriteInputTokens")}
WINDOW = {key: NUMBER for key in ("usedPercent", "used_percent", "windowDurationMins", "window_minutes", "resetsAt", "resets_at")}
BUCKET = {"limitId": IDENTIFIER, "limit_id": IDENTIFIER, "primary": WINDOW, "secondary": WINDOW}
LIMITS = {**BUCKET, "rateLimits": BUCKET, "rateLimitsByLimitId": {"*": BUCKET}}
EFFORT = {key: ("text", 64) for key in ("reasoningEffort", "reasoning_effort", "model_reasoning_effort", "effort")}


class Strict(dict):
    """Reject unknown envelope fields without decoding their values."""


def project_json(raw: bytes, schema):
    """Project allowlisted fields with bounded nesting, strings and arrays."""
    if len(raw) > 4 * 1024 * 1024:
        raise WeatherError("Projection input exceeds its byte limit")
    index, length = 0, len(raw)

    def space():
        nonlocal index
        while index < length and raw[index] in b" \t\r\n":
            index += 1

    def string_end():
        nonlocal index
        start = index
        index += 1
        while index < length:
            char = raw[index]
            index += 1
            if char == 34:
                return start, index
            if char < 32:
                raise ValueError("Invalid JSON string")
            if char == 92:
                if index >= length or raw[index] not in b'"\\/bfnrtu':
                    raise ValueError("Invalid JSON escape")
                escape = raw[index]
                index += 1
                if escape == 117:
                    if index + 4 > length or not re.fullmatch(b"[0-9a-fA-F]{4}", raw[index:index + 4]):
                        raise ValueError("Invalid Unicode escape")
                    index += 4
        raise ValueError("Unterminated JSON string")

    def value(selected, depth=0):
        nonlocal index
        if depth > 64:
            raise ValueError("JSON nesting exceeds limit")
        space()
        if index >= length:
            raise ValueError("Missing JSON value")
        char = raw[index]
        if isinstance(selected, tuple) and selected[0] == "present":
            start = index
            value(None, depth)
            return raw[start:index] not in (b"null", b"false", b'""', b"{}", b"[]", b"0")
        if char == 123:
            index += 1
            result = {} if isinstance(selected, dict) else None
            space()
            if index < length and raw[index] == 125:
                index += 1
                return result
            while True:
                space()
                if index >= length or raw[index] != 34:
                    raise ValueError("Missing object key")
                start, end = string_end()
                # Unknown keys in ignored subtrees are not decoded either.
                key = json.loads(raw[start:end]) if result is not None and end - start <= 256 else None
                space()
                if index >= length or raw[index] != 58:
                    raise ValueError("Missing colon")
                index += 1
                selector = selected.get(key, selected.get("*")) if result is not None else None
                if isinstance(selected, Strict) and selector is None:
                    raise ValueError("Unknown envelope field")
                item = value(selector, depth + 1)
                if selector is not None:
                    if key in result or len(result) >= 128:
                        raise ValueError("Duplicate selected key or too many fields")
                    result[key] = item
                space()
                if index < length and raw[index] == 125:
                    index += 1
                    return result
                if index >= length or raw[index] != 44:
                    raise ValueError("Missing object separator")
                index += 1
        if char == 91:
            index += 1
            result = [] if isinstance(selected, list) else None
            space()
            if index < length and raw[index] == 93:
                index += 1
                return result
            count = 0
            while True:
                item = value(selected[0] if result is not None else None, depth + 1)
                count += 1
                if result is not None:
                    if count > 500:
                        raise ValueError("Too many selected array items")
                    result.append(item)
                space()
                if index < length and raw[index] == 93:
                    index += 1
                    return result
                if index >= length or raw[index] != 44:
                    raise ValueError("Missing array separator")
                index += 1
        start = index
        if char == 34:
            _, end = string_end()
        else:
            while index < length and raw[index] not in b" \t\r\n,]}":
                index += 1
            end = index
            token = raw[start:end]
            if token not in (b"null", b"true", b"false") and not re.fullmatch(b"-?(?:0|[1-9][0-9]*)(?:\\.[0-9]+)?(?:[eE][+-]?[0-9]+)?", token):
                raise ValueError("Invalid primitive")
        if not isinstance(selected, tuple):
            return None
        kind, maximum = selected
        if end - start > maximum * 6 + 2:
            raise ValueError("Selected scalar exceeds limit")
        result = json.loads(raw[start:end])
        if result is None:
            return None
        expected = {"text": str, "number": (int, float), "bool": bool}[kind]
        if (kind == "number" and type(result) not in expected) or (kind != "number" and type(result) is not expected):
            raise ValueError("Unexpected selected scalar type")
        if isinstance(result, str) and len(result) > maximum:
            raise ValueError("Selected text exceeds limit")
        return result

    result = value(schema)
    space()
    if index != length:
        raise ValueError("Trailing JSON input")
    return result


def project_rollout(raw):
    envelope = project_json(raw, {"type": ("text", 32)})
    if not isinstance(envelope, dict):
        raise ValueError("Record must be an object")
    kind = envelope.get("type")
    payload = {}
    if kind == "session_meta":
        payload = {"id": IDENTIFIER, "cwd": ("text", 4096), "cli_version": ("text", 64),
                   "parent_thread_id": IDENTIFIER, "parentThreadId": IDENTIFIER,
                   "source": {"subagent": {}}}
    elif kind == "turn_context":
        payload = {"turn_id": IDENTIFIER, "model": TEXT, **EFFORT}
    elif kind == "event_msg":
        event_payload = project_json(raw, {"payload": {"type": ("text", 32)}}).get("payload")
        if not isinstance(event_payload, dict):
            raise ValueError("Event payload must be an object")
        event = event_payload.get("type")
        if event == "token_count":
            payload = {"type": ("text", 32), "rate_limits": LIMITS, "info": {
                "model_context_window": NUMBER, "last_token_usage": COUNT_FIELDS,
                "total_token_usage": {"total_tokens": NUMBER}}}
        elif event in {"task_started", "task_complete", "task_completed", "turn_aborted", "context_compacted"}:
            payload = {"type": ("text", 32), "turn_id": IDENTIFIER, "model_context_window": NUMBER}
    elif kind != "compacted":
        return {"type": kind}  # No message/tool/summary payload is decoded.
    result = project_json(raw, {"type": ("text", 32), "timestamp": ("text", 64), "payload": payload})
    if isinstance(result.get("payload"), dict) and isinstance(result["payload"].get("turn_id"), str):
        result["payload"]["turn_id"] = digest(result["payload"]["turn_id"].encode())
    return result


def project_notification(raw):
    return project_json(raw, {"observed_at": NUMBER, "message": {"id": ("present", 0), "method": TEXT, "params": {
        "threadId": IDENTIFIER, "turnId": IDENTIFIER, "turn": {"id": IDENTIFIER, "status": TEXT},
        "threadSettings": {"model": TEXT, **EFFORT}, "toModel": TEXT, **EFFORT,
        "tokenUsage": {"last": COUNT_FIELDS, "total": {"totalTokens": NUMBER}, "modelContextWindow": NUMBER},
        "item": {"type": TEXT}, **LIMITS}}})


def project_replay(raw, control=False):
    message = {"id": ("present", 0), "method": TEXT, "params": {
        "threadId": IDENTIFIER, "turnId": IDENTIFIER, "turn": {
            "id": IDENTIFIER, "status": TEXT, "error": ("present", 0)},
        "threadSettings": {"model": TEXT, **EFFORT}, "toModel": TEXT, **EFFORT,
        "tokenUsage": {"last": COUNT_FIELDS, "modelContextWindow": NUMBER},
        "item": {"id": TEXT, "type": TEXT, "status": TEXT, "success": FLAG,
                 "error": ("present", 0), "processId": TEXT, "senderThreadId": IDENTIFIER,
                 "receiverThreadIds": [IDENTIFIER]}}}
    schema = {"schema_version": NUMBER, "engine_version": TEXT, "thread_id": IDENTIFIER,
              "workspace": ("text", 4096), "events": [Strict({"observed_at": NUMBER, "message": message})]}
    if control:
        schema.update(turn_id=IDENTIFIER, inventory={}, same_live_server=FLAG)
    else:
        schema.update(thread_response={"thread": {"id": IDENTIFIER, "parentThreadId": IDENTIFIER,
            "cwd": ("text", 4096), "status": {"type": TEXT}, "model": TEXT,
            "modelProvider": TEXT, "reasoningEffort": ("text", 64)}}, config_response={"config": {
                "model": TEXT, "model_provider": TEXT, "model_reasoning_effort": ("text", 64),
                "model_context_window": NUMBER, "model_auto_compact_token_limit": NUMBER,
                "model_auto_compact_token_limit_scope": TEXT}})
        schema = Strict(schema)
    return project_json(raw, schema)
