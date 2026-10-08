#!/usr/bin/env python3
"""Read allowlisted Codex usage metadata; standard library only."""

import argparse
import datetime as dt
import json
import math
import os
from pathlib import Path
import queue
import shutil
import stat
import subprocess
import sys
import threading
import time
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

UTC = dt.timezone.utc
MAX_LINE_BYTES = 2 * 1024 * 1024
READER_VERSION = "0.1.2"


def desktop_codex_candidates():
    if sys.platform != "darwin":
        return []
    return [root / app / "Contents/Resources/codex"
            for root in (Path("/Applications"), Path.home() / "Applications")
            for app in ("ChatGPT.app", "Codex.app")]


def find_codex():
    executable = shutil.which("codex")
    if executable:
        return executable
    for candidate in desktop_codex_candidates():
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return str(candidate)
    return None


def number(value):
    return (isinstance(value, (int, float)) and not isinstance(value, bool)
            and math.isfinite(value))


def pick(obj, snake, camel):
    return obj.get(snake) if snake in obj else obj.get(camel)


def timestamp(value):
    try:
        if number(value):
            return dt.datetime.fromtimestamp(value, UTC)
        if isinstance(value, str):
            value = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
            return value.astimezone(UTC) if value.tzinfo else None
    except (ValueError, OverflowError, OSError):
        pass
    return None


def display_time(value, timezone):
    parsed = timestamp(value)
    return parsed.astimezone(timezone).isoformat(timespec="seconds") if parsed else None


def window(raw, slot, now, timezone):
    if not isinstance(raw, dict):
        return None
    used = pick(raw, "used_percent", "usedPercent")
    if not number(used) or used < 0:
        return None
    minutes = pick(raw, "window_minutes", "windowDurationMins")
    if not number(minutes) or minutes <= 0:
        minutes = None
    reset = pick(raw, "resets_at", "resetsAt")
    reset_time = timestamp(reset)
    return {
        "kind": {10080: "weekly", 300: "five_hour"}.get(minutes, "other"),
        "slot": slot,
        "duration_minutes": minutes,
        "used_percent": used,
        "remaining_percent": max(0, 100 - used),
        "resets_at": reset_time.isoformat() if reset_time else None,
        "resets_at_local": display_time(reset, timezone),
        "snapshot_window_expired": reset_time <= now if reset_time else None,
    }


def reset_cards(raw, timezone):
    if not isinstance(raw, dict):
        return {"status": "unknown", "available_count": None, "details": None}
    count = pick(raw, "available_count", "availableCount")
    if not isinstance(count, int) or isinstance(count, bool) or count < 0:
        return {"status": "unknown", "available_count": None, "details": None}
    details = None
    if isinstance(raw.get("credits"), list):
        details = []
        for card in raw["credits"]:
            if not isinstance(card, dict):
                continue
            state = card.get("status")
            details.append({
                "status": state if state in {"available", "redeeming", "redeemed", "unknown"} else "unknown",
                "granted_at_local": display_time(pick(card, "granted_at", "grantedAt"), timezone),
                "expires_at_local": display_time(pick(card, "expires_at", "expiresAt"), timezone),
            })
    return {"status": "known", "available_count": count, "details": details}


def normalize_limit(raw, now, timezone):
    if not isinstance(raw, dict):
        return None
    windows = [w for slot in ("primary", "secondary")
               if (w := window(raw.get(slot), slot, now, timezone)) is not None]
    if not windows:
        return None
    paid = raw.get("credits")
    paid = paid if isinstance(paid, dict) else {}
    balance = paid.get("balance")
    # Numeric balances only. Never forward arbitrary backend strings.
    if isinstance(balance, str):
        try:
            balance = float(balance)
        except ValueError:
            balance = None
    if not number(balance):
        balance = None
    plan = pick(raw, "plan_type", "planType")
    limit_id = pick(raw, "limit_id", "limitId") or "codex"
    if not isinstance(limit_id, str) or len(limit_id) > 100:
        limit_id = "unknown"
    if not isinstance(plan, str) or len(plan) > 100:
        plan = None
    return {
        "limit_id": limit_id,
        "plan_type": plan,
        "windows": windows,
        "paid_credits": {
            "balance": balance,
            "has_credits": pick(paid, "has_credits", "hasCredits") if isinstance(pick(paid, "has_credits", "hasCredits"), bool) else None,
            "unlimited": paid.get("unlimited") if isinstance(paid.get("unlimited"), bool) else None,
        },
    }


def usage_event(record):
    """Never parse strings embedded in messages, tool output or quoted examples."""
    if not isinstance(record, dict):
        return None
    payload = record.get("payload")
    if (record.get("type") == "event_msg" and isinstance(payload, dict)
            and payload.get("type") == "token_count"):
        return {"rateLimits": payload.get("rate_limits"),
                "rateLimitResetCredits": pick(payload, "rate_limit_reset_credits", "rateLimitResetCredits")}
    if record.get("method") == "account/rateLimits/updated":
        params = record.get("params")
        return params if isinstance(params, dict) else None
    return None


def bounded_lines(stream):
    while True:
        line = stream.readline(MAX_LINE_BYTES + 1)
        if not line:
            return
        if len(line) > MAX_LINE_BYTES:
            while line and not line.endswith(b"\n"):
                line = stream.readline(MAX_LINE_BYTES + 1)
            yield None
        else:
            yield line


def local_usage(home, now, timezone):
    latest = {}
    cards = None
    unreadable = 0
    diagnostics = {
        "codex_home": str(home),
        "codex_cli": find_codex(),
        "home_exists": False,
        "history_directories_found": 0,
        "session_files_found": 0,
        "session_files_read": 0,
        "usage_events_found": 0,
        "unreadable_directories": 0,
    }
    try:
        diagnostics["home_exists"] = stat.S_ISDIR(home.stat().st_mode)
    except FileNotFoundError:
        pass
    except OSError:
        diagnostics["unreadable_directories"] += 1

    def walk_error(_error):
        diagnostics["unreadable_directories"] += 1

    for folder in (home / "sessions", home / "archived_sessions"):
        try:
            if not stat.S_ISDIR(folder.stat().st_mode):
                continue
        except FileNotFoundError:
            continue
        except OSError:
            diagnostics["unreadable_directories"] += 1
            continue
        diagnostics["history_directories_found"] += 1
        paths = (Path(directory) / name
                 for directory, _, names in os.walk(folder, onerror=walk_error)
                 for name in names if name.endswith(".jsonl"))
        for path in paths:
            if path.is_symlink():
                continue
            diagnostics["session_files_found"] += 1
            try:
                with path.open("rb") as stream:
                    for line_no, line in enumerate(bounded_lines(stream), 1):
                        if not line or not any(key in line for key in (b'"rate_limits"', b'"rateLimits"', b'"rateLimitResetCredits"')):
                            continue
                        try:
                            record = json.loads(line)
                        except (ValueError, UnicodeError):
                            continue
                        event = usage_event(record)
                        recorded = timestamp(record.get("timestamp")) if isinstance(record, dict) else None
                        if not event or not recorded or recorded > now + dt.timedelta(minutes=5):
                            continue
                        diagnostics["usage_events_found"] += 1
                        source = {"file": str(path), "line": line_no}
                        meta = {"source": source, "recorded_at": recorded.isoformat(),
                                "recorded_at_local": recorded.astimezone(timezone).isoformat(timespec="seconds"),
                                "age_seconds": max(0, int((now - recorded).total_seconds()))}
                        bucket = normalize_limit(event.get("rateLimits"), now, timezone)
                        if bucket:
                            key = bucket["limit_id"]
                            if key not in latest or recorded > latest[key][0]:
                                latest[key] = (recorded, dict(bucket, **meta))
                        summary = reset_cards(event.get("rateLimitResetCredits"), timezone)
                        if summary["status"] == "known" and (cards is None or recorded > cards[0]):
                            cards = (recorded, dict(summary, **meta))
                diagnostics["session_files_read"] += 1
            except OSError:
                unreadable += 1
    incomplete = unreadable or diagnostics["unreadable_directories"]
    if latest:
        local_status = "partial" if incomplete else "ok"
    elif incomplete:
        local_status = "history_unreadable"
    elif not diagnostics["home_exists"]:
        local_status = "codex_home_missing"
    elif not diagnostics["history_directories_found"]:
        local_status = "session_directories_missing"
    elif not diagnostics["session_files_found"]:
        local_status = "no_session_files"
    else:
        local_status = "no_rate_limit_snapshots"
    return {
        "source_type": "local_history",
        "local_status": local_status,
        "diagnostics": diagnostics,
        "account_identity": "not_verified_from_local_history",
        "limits": [v[1] for _, v in sorted(latest.items())],
        "reset_cards": cards[1] if cards else reset_cards(None, timezone),
        "unreadable_files": unreadable,
    }


def live_read(timeout=12, codex_home=None):
    executable = find_codex()
    if not executable:
        return None, "codex_cli_unavailable"
    process = None
    responses = queue.Queue()
    try:
        process = subprocess.Popen([executable, "app-server", "--stdio"],
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.DEVNULL,
                                   env=dict(os.environ, CODEX_HOME=str(codex_home)) if codex_home else None)
        def receive():
            for line in bounded_lines(process.stdout):
                if not line:
                    continue
                try:
                    message = json.loads(line)
                    if isinstance(message, dict) and message.get("id") in (1, 2):
                        responses.put(message)
                except (ValueError, UnicodeError):
                    pass
            responses.put(None)
        reader = threading.Thread(target=receive, daemon=True)
        reader.start()
        deadline = time.monotonic() + timeout
        def send(message):
            process.stdin.write((json.dumps(message) + "\n").encode())
            process.stdin.flush()
        def wait(expected):
            while True:
                response = responses.get(timeout=max(0, deadline - time.monotonic()))
                if response is None:
                    raise EOFError
                if response.get("id") == expected:
                    return response
        send({"id": 1, "method": "initialize", "params": {
            "clientInfo": {"name": "codex_usage", "version": READER_VERSION}}})
        if "error" in wait(1):
            return None, "initialization_failed"
        send({"method": "initialized"})
        send({"id": 2, "method": "account/rateLimits/read"})
        response = wait(2)
        if "error" in response:
            # Classify internally; never expose arbitrary error messages.
            message = str(response["error"]).lower()
            return None, "chatgpt_authentication_unavailable" if "auth" in message else "account_read_failed"
        result = response.get("result")
        return (result, None) if isinstance(result, dict) else (None, "invalid_response")
    except queue.Empty:
        return None, "timeout"
    except (OSError, EOFError, ValueError):
        return None, "connection_failed"
    finally:
        if process is not None:
            process.terminate()
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=2)
            if process.stdin:
                process.stdin.close()
            if process.stdout:
                process.stdout.close()


def report(home, now, timezone, live=False):
    result = local_usage(home, now, timezone)
    result.update({"reader_version": READER_VERSION,
                   "queried_at": now.isoformat(), "queried_at_local": now.astimezone(timezone).isoformat(timespec="seconds"),
                   "live_status": "not_requested"})
    if live:
        raw, error = live_read(codex_home=home)
        result["live_status"] = error or "ok"
        if raw is not None:
            live_now = dt.datetime.now(UTC)
            buckets = raw.get("rateLimitsByLimitId")
            buckets = list(buckets.values()) if isinstance(buckets, dict) and buckets else [raw.get("rateLimits")]
            normalized = [b for item in buckets if (b := normalize_limit(item, live_now, timezone))]
            # Keep live CLI data separate: its account can differ from historical sessions.
            result["live"] = {
                "source_type": "codex_app_server",
                "queried_at": live_now.isoformat(),
                "queried_at_local": live_now.astimezone(timezone).isoformat(timespec="seconds"),
                "limits": normalized,
                "reset_cards": reset_cards(raw.get("rateLimitResetCredits"), timezone),
            }
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-home", type=Path, default=Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex"))
    parser.add_argument("--timezone", help="IANA timezone; default: local machine timezone")
    parser.add_argument("--live", action="store_true", help="Also read through existing Codex CLI auth; never signs in or redeems cards")
    parser.add_argument("--json", action="store_true", help="Print structured metadata")
    args = parser.parse_args()
    try:
        timezone = ZoneInfo(args.timezone) if args.timezone else None
    except (ZoneInfoNotFoundError, ValueError):
        parser.error("Timezone unavailable. Use an installed IANA timezone or omit --timezone.")
    result = report(args.codex_home.expanduser().resolve(), dt.datetime.now(UTC), timezone, args.live)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    else:
        for bucket in result["limits"]:
            print(f"{bucket['limit_id']} / {bucket['plan_type']} — snapshot {bucket['recorded_at_local']}")
            for w in bucket["windows"]:
                state = "EXPIRED SNAPSHOT" if w["snapshot_window_expired"] else "recorded"
                print(f"  {w['kind']}: {w['remaining_percent']:g}% remaining, {w['used_percent']:g}% used ({state}); reset {w['resets_at_local']}")
            print(f"  Source: {bucket['source']['file']}:{bucket['source']['line']}")
        if not result["limits"]:
            print("Local usage unavailable: " + result["local_status"])
            print("Checked Codex home: " + result["diagnostics"]["codex_home"])
        cards = result["reset_cards"]
        print("Local reset cards: " + (str(cards["available_count"]) if cards["status"] == "known" else "unknown (not recorded)"))
        if args.live:
            print("Live query: " + result["live_status"])
            if "live" in result:
                print(json.dumps(result["live"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
