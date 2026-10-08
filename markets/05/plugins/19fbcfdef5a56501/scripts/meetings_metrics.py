"""Privacy-safe, dependency-free operational metrics for the Meetings client."""

from __future__ import annotations

import json
import os
import re
import sys
import threading
import time
from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, TypeAlias, TypedDict
from urllib.request import HTTPSHandler, Request, build_opener

from meetings_sentry import (
    cached_metrics_account_matches,
    codex_app_version,
    is_isolated_e2e,
    plugin_marketplace,
    plugin_version,
)
from runtime_config import RUNTIME_CONFIG

from helpers import NoRedirectHandler, create_https_context

_PLUGIN_ROOT = Path(__file__).resolve().parents[1]
_STATSC_ENDPOINT = "https://chatgpt.com/ces/statsc/flush"
_STATSC_NAMESPACE = "chatgpt_meetings"
_STATSC_FLUSH_INTERVAL_SECONDS = 60.0
_STATSC_POST_TIMEOUT_SECONDS = 1.0
_STATSC_SHUTDOWN_FLUSH_TIMEOUT_SECONDS = 1.25
MAXIMUM_CLIENT_PERFORMANCE_DURATION_MILLISECONDS = 3_600_000
_MAXIMUM_COUNTER_KEYS = 128
_MAXIMUM_COUNTERS_PER_FLUSH = 128
_MAXIMUM_COUNTER_VALUE = 2**31 - 1
_SAFE_TAG_VALUE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._+-]{0,79}\Z")
_METRIC_NAMES = frozenset(
    {
        "client_operation_attempt",
        "client_operation_latency_bucket",
        "client_operation_result",
        "private_note_cache_outcome",
        "client_action_latency_bucket",
        "auth_cache_failure",
        "auth_fetch_latency_bucket",
        "notes_lookup_latency_bucket",
        "client_surface_health",
    }
)
_ALLOWED_TAG_KEYS = frozenset(
    {
        "environment",
        "auth_cache_operation",
        "auth_transport",
        "cache_outcome",
        "failure_reason",
        "latency_bucket",
        "lookup_stage",
        "mcp_version",
        "operation",
        "platform",
        "refresh_trigger",
        "result",
        "streaming",
        "surface",
        "transition",
        "ui_version",
        "problem",
    }
)

ClientOperation: TypeAlias = Literal[
    "home_bootstrap",
    "notes_load",
    "note_detail",
    "calendar_load",
    "settings_read",
    "settings_write",
    "recording_start",
    "recording_stop",
    "recording_status",
]
ClientOperationResult: TypeAlias = Literal["success", "error", "cancelled"]
AuthCacheOperation: TypeAlias = Literal["initialize", "read", "write", "delete"]
AuthFetchTransport: TypeAlias = Literal["isolated_child"]
AuthFetchResult: TypeAlias = Literal["success", "error", "cancelled"]
PrivateNoteCacheOutcome: TypeAlias = Literal[
    "hit",
    "cold_miss",
    "unsupported_companion",
    "rejected",
]
NotesLookupStage: TypeAlias = Literal["backend_page", "backend_auth", "backend_http"]
_NOTES_LOOKUP_STAGES = frozenset({"backend_page", "backend_auth", "backend_http"})
NotesRefreshTrigger: TypeAlias = Literal["initial", "background", "manual"]
NOTES_REFRESH_TRIGGERS: tuple[NotesRefreshTrigger, ...] = ("initial", "background", "manual")
ClientFailureReason: TypeAlias = Literal[
    "auth",
    "backend",
    "connection",
    "invalid_response",
    "not_found",
    "timeout",
]
CLIENT_OPERATIONS = frozenset(
    {
        "home_bootstrap",
        "notes_load",
        "note_detail",
        "calendar_load",
        "settings_read",
        "settings_write",
        "recording_start",
        "recording_stop",
        "recording_status",
    }
)
CLIENT_OPERATION_RESULTS = frozenset({"success", "error", "cancelled"})
AUTH_CACHE_OPERATIONS = frozenset({"initialize", "read", "write", "delete"})
AUTH_FETCH_TRANSPORTS = frozenset({"isolated_child"})
AUTH_FETCH_RESULTS = frozenset({"success", "error", "cancelled"})
CLIENT_PERFORMANCE_OPERATIONS = frozenset(
    {
        "home_bootstrap",
        "notes_load",
        "note_detail",
        "calendar_load",
        "recording_start",
        "recording_stop",
    }
)
CLIENT_PERFORMANCE_TRANSITIONS_BY_OPERATION: Mapping[str, frozenset[str]] = {
    "calendar_load": frozenset({"surface_active", "surface_load_failure"}),
    "notes_load": frozenset(
        {"open_to_render", "open_to_timeout", "surface_active", "surface_load_failure"}
    ),
    "note_detail": frozenset(
        {"open_to_render", "open_to_timeout", "surface_active", "surface_load_failure"}
    ),
    "recording_start": frozenset(
        {"click_to_recording", "click_to_start_failed", "click_to_start_timeout"}
    ),
    "recording_stop": frozenset({"click_to_saving", "click_to_ready", "saving_to_ready"}),
}
CLIENT_PERFORMANCE_TRANSITIONS = frozenset(
    transition
    for transitions in CLIENT_PERFORMANCE_TRANSITIONS_BY_OPERATION.values()
    for transition in transitions
)
CLIENT_STREAMING_STATES = frozenset({"yes", "no", "unknown"})
CLIENT_FAILURE_REASONS = frozenset(
    {"auth", "backend", "connection", "invalid_response", "not_found", "timeout"}
)
PRIVATE_NOTE_CACHE_OUTCOMES = frozenset({"hit", "cold_miss", "unsupported_companion", "rejected"})

_LATENCY_BUCKETS: tuple[tuple[int, str], ...] = (
    (100, "lt_100ms"),
    (250, "100ms_to_250ms"),
    (500, "250ms_to_500ms"),
    (1_000, "500ms_to_1s"),
    (2_000, "1s_to_2s"),
    (5_000, "2s_to_5s"),
    (10_000, "5s_to_10s"),
    (20_000, "10s_to_20s"),
    (30_000, "20s_to_30s"),
    (60_000, "30s_to_60s"),
    (120_000, "60s_to_120s"),
)


class _StatscCounter(TypedDict):
    namespace: str
    metric: str
    tags: dict[str, str]
    value: int


class _StatscFlushRequest(TypedDict):
    counters: list[_StatscCounter]
    client_type: str


@dataclass(frozen=True, slots=True)
class _MetricKey:
    metric: str
    tags: tuple[tuple[str, str], ...]


def _platform() -> str:
    if sys.platform == "darwin":
        return "macos"
    if sys.platform.startswith("win"):
        return "windows"
    if sys.platform.startswith("linux"):
        return "linux"
    return "unknown"


def _metrics_disabled() -> bool:
    return is_isolated_e2e() or (
        os.environ.get("CHATGPT_MEETINGS_STATSC_DISABLED", "").lower() in {"1", "true"}
    )


def _safe_tags(tags: Mapping[str, object]) -> dict[str, str] | None:
    if len(tags) > 10:
        return None
    safe: dict[str, str] = {}
    for key, value in tags.items():
        if (
            key not in _ALLOWED_TAG_KEYS
            or _SAFE_TAG_VALUE.fullmatch(key) is None
            or not isinstance(value, str)
            or _SAFE_TAG_VALUE.fullmatch(value) is None
        ):
            return None
        safe[key] = value
    return safe


def _base_tags(*, plugin_root: Path = _PLUGIN_ROOT) -> dict[str, str] | None:
    version = plugin_version(plugin_root)
    if version is None:
        return None
    return {
        "surface": "plugin_ui",
        "platform": _platform(),
        "ui_version": version,
        "mcp_version": version,
        "codex_app_version": codex_app_version(),
        "environment": RUNTIME_CONFIG.flavor,
        "marketplace": plugin_marketplace(plugin_root),
    }


class _StatscClient:
    """Coalesce bounded counter keys and flush them off the JSON-RPC thread."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._counters: dict[_MetricKey, int] = {}
        self._flush_timer: threading.Timer | None = None
        self._post_in_flight = False
        self._post_thread: threading.Thread | None = None

    def record(self, metric: str, tags: Mapping[str, object]) -> bool:
        if _metrics_disabled() or metric not in _METRIC_NAMES:
            return False
        base_tags = _base_tags()
        safe_tags = _safe_tags(tags)
        if base_tags is None or safe_tags is None:
            return False
        merged = {**base_tags, **safe_tags}
        key = _MetricKey(metric=metric, tags=tuple(sorted(merged.items())))
        with self._lock:
            if key not in self._counters and len(self._counters) >= _MAXIMUM_COUNTER_KEYS:
                return False
            self._counters[key] = min(
                _MAXIMUM_COUNTER_VALUE,
                self._counters.get(key, 0) + 1,
            )
            should_flush = len(self._counters) >= _MAXIMUM_COUNTERS_PER_FLUSH
            if not should_flush:
                self._schedule_flush_locked()
        if should_flush:
            self.flush()
        return True

    def flush(self) -> bool:
        with self._lock:
            if self._post_in_flight or not self._counters:
                return False
            if self._flush_timer is not None:
                self._flush_timer.cancel()
                self._flush_timer = None
            pending = self._counters
            self._counters = {}
            self._post_in_flight = True
            worker = threading.Thread(
                target=self._post,
                args=(pending,),
                name="meetings-statsc",
                daemon=True,
            )
            self._post_thread = worker
            try:
                worker.start()
            except Exception:
                started = False
            else:
                started = True
        if not started:
            self._complete_post()
            return False
        return True

    def flush_and_wait(self, timeout_seconds: float) -> bool:
        """Give queued counters a bounded delivery opportunity during shutdown."""

        deadline = time.monotonic() + max(0.0, timeout_seconds)
        with self._lock:
            if self._flush_timer is not None:
                self._flush_timer.cancel()
                self._flush_timer = None
            worker = self._post_thread
        if worker is not None:
            worker.join(timeout=max(0.0, deadline - time.monotonic()))
            if worker.is_alive():
                return False

        self.flush()
        with self._lock:
            worker = self._post_thread
        if worker is not None:
            worker.join(timeout=max(0.0, deadline - time.monotonic()))
            if worker.is_alive():
                return False

        with self._lock:
            if self._flush_timer is not None:
                self._flush_timer.cancel()
                self._flush_timer = None
            return not self._post_in_flight and not self._counters

    def _schedule_flush_locked(self) -> None:
        if self._flush_timer is not None or self._post_in_flight or not self._counters:
            return
        timer = threading.Timer(_STATSC_FLUSH_INTERVAL_SECONDS, self.flush)
        timer.daemon = True
        self._flush_timer = timer
        try:
            timer.start()
        except Exception:
            self._flush_timer = None

    def _post(self, pending: dict[_MetricKey, int]) -> None:
        try:
            payload = _flush_request(pending)
            request = Request(
                _STATSC_ENDPOINT,
                data=json.dumps(payload, separators=(",", ":"), ensure_ascii=True).encode("ascii"),
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "chatgpt-meetings-mcp",
                },
                method="POST",
            )
            with build_opener(
                NoRedirectHandler(), HTTPSHandler(context=create_https_context())
            ).open(
                request,
                timeout=_STATSC_POST_TIMEOUT_SECONDS,
            ):
                pass
        except Exception:
            pass
        finally:
            self._complete_post()

    def _complete_post(self) -> None:
        with self._lock:
            self._post_in_flight = False
            self._post_thread = None
            # CES may have accepted a batch whose acknowledgement was lost.
            # Do not replay it; newly recorded counters still get their own flush.
            self._schedule_flush_locked()


def _flush_request(counters: Mapping[_MetricKey, int]) -> _StatscFlushRequest:
    return {
        "counters": [
            {
                "namespace": _STATSC_NAMESPACE,
                "metric": key.metric,
                "tags": dict(key.tags),
                "value": value,
            }
            for key, value in counters.items()
        ],
        "client_type": _platform(),
    }


_CLIENT = _StatscClient()


def _record_metric(metric: str, tags: Mapping[str, object]) -> bool:
    try:
        return _CLIENT.record(metric, tags)
    except Exception:
        # Operational telemetry must never affect the Meetings client path.
        return False


def client_operation_for_tool_call(
    tool_name: str,
    arguments: Mapping[str, object],
) -> ClientOperation | None:
    """Classify only reliability-critical app-only operations."""

    if tool_name == "chatgpt_meetings_get_snapshot":
        request = arguments.get("request")
        if not isinstance(request, str):
            return None
        operation_by_request: dict[str, ClientOperation] = {
            "home.bootstrap": "home_bootstrap",
            "notes.list": "notes_load",
            "note.get": "note_detail",
            "calendar.list": "calendar_load",
            "settings.get": "settings_read",
            "local.getSettings": "settings_read",
            "settings.update": "settings_write",
            "local.updateSettings": "settings_write",
        }
        return operation_by_request.get(request)
    operation_by_tool: dict[str, ClientOperation] = {
        "chatgpt_meetings_local_status": "recording_status",
        "chatgpt_meetings_start_local": "recording_start",
        "chatgpt_meetings_stop_local": "recording_stop",
    }
    return operation_by_tool.get(tool_name)


def notes_refresh_trigger_for_tool_call(
    tool_name: str,
    arguments: Mapping[str, object],
) -> NotesRefreshTrigger | None:
    """Classify only finite refresh metadata on the private Notes operation."""

    if tool_name != "chatgpt_meetings_get_snapshot" or arguments.get("request") != "notes.list":
        return None
    trigger = arguments.get("refreshTrigger")
    allowed_triggers: dict[str, NotesRefreshTrigger] = {
        "initial": "initial",
        "background": "background",
        "manual": "manual",
    }
    return allowed_triggers.get(trigger) if isinstance(trigger, str) else None


def record_client_operation_attempt(
    operation: ClientOperation,
    *,
    refresh_trigger: NotesRefreshTrigger | None = None,
) -> bool:
    if operation not in CLIENT_OPERATIONS or (
        refresh_trigger is not None
        and (operation != "notes_load" or refresh_trigger not in NOTES_REFRESH_TRIGGERS)
    ):
        return False
    tags: dict[str, str] = {"operation": operation}
    if refresh_trigger is not None:
        tags["refresh_trigger"] = refresh_trigger
    return _record_metric("client_operation_attempt", tags)


def record_client_operation_result(
    operation: ClientOperation,
    result: ClientOperationResult,
    failure_reason: ClientFailureReason | None = None,
    *,
    refresh_trigger: NotesRefreshTrigger | None = None,
) -> bool:
    if (
        operation not in CLIENT_OPERATIONS
        or result not in CLIENT_OPERATION_RESULTS
        or (
            refresh_trigger is not None
            and (operation != "notes_load" or refresh_trigger not in NOTES_REFRESH_TRIGGERS)
        )
    ):
        return False
    if result == "error":
        if failure_reason not in CLIENT_FAILURE_REASONS:
            return False
    elif failure_reason is not None:
        return False
    tags: dict[str, str] = {"operation": operation, "result": result}
    if failure_reason is not None:
        tags["failure_reason"] = failure_reason
    if refresh_trigger is not None:
        tags["refresh_trigger"] = refresh_trigger
    return _record_metric("client_operation_result", tags)


def record_client_load_impact(
    problem: Literal["active", "load_failure", "start_attempt", "start_failure"],
    *,
    expected_account: tuple[str, str | None],
) -> bool:
    """Observe owner-fenced client outcomes, including failures in the active population."""

    if problem not in {"active", "load_failure", "start_attempt", "start_failure"}:
        return False
    if not cached_metrics_account_matches(expected_account):
        return False
    # The MCP package version is trusted; the mounted UI version is not known here.
    recorded = True
    is_start = problem in {"start_attempt", "start_failure"}
    population = "start_attempt" if is_start else "active"
    for observed_problem in (
        (population, problem) if problem in {"load_failure", "start_failure"} else (population,)
    ):
        recorded = (
            _record_metric(
                "client_surface_health",
                {
                    "problem": observed_problem,
                    "ui_version": "unknown",
                    "transition": "recording_start_outcome" if is_start else "surface_health",
                },
            )
            and recorded
        )
    return recorded


def client_operation_latency_bucket(duration_milliseconds: object) -> str | None:
    """Project one bounded duration into a fixed, low-cardinality bucket."""

    if (
        isinstance(duration_milliseconds, bool)
        or not isinstance(duration_milliseconds, int)
        or duration_milliseconds < 0
        or duration_milliseconds > MAXIMUM_CLIENT_PERFORMANCE_DURATION_MILLISECONDS
    ):
        return None
    for maximum, bucket in _LATENCY_BUCKETS:
        if duration_milliseconds < maximum:
            return bucket
    return "gte_120s"


def record_client_operation_latency(
    operation: ClientOperation,
    result: ClientOperationResult,
    duration_milliseconds: int,
) -> bool:
    """Count one terminal RPC latency without identifiers or raw timing values."""

    latency_bucket = client_operation_latency_bucket(duration_milliseconds)
    if (
        operation not in CLIENT_PERFORMANCE_OPERATIONS
        or result not in CLIENT_OPERATION_RESULTS
        or latency_bucket is None
    ):
        return False
    return _record_metric(
        "client_operation_latency_bucket",
        {
            "operation": operation,
            "result": result,
            "latency_bucket": latency_bucket,
        },
    )


@contextmanager
def measure_notes_lookup_stage(stage: NotesLookupStage) -> Iterator[None]:
    """Time one lookup boundary, including failures, without recording request data."""

    started = time.perf_counter()
    try:
        yield
    finally:
        duration_ms = max(0, int((time.perf_counter() - started) * 1000))
        bucket = client_operation_latency_bucket(duration_ms)
        if stage in _NOTES_LOOKUP_STAGES and bucket is not None:
            _record_metric(
                "notes_lookup_latency_bucket",
                {"lookup_stage": stage, "latency_bucket": bucket},
            )
            try:
                print(
                    "ChatGPT Meetings lookup timing: "
                    + json.dumps({"stage": stage, "durationMs": duration_ms}, sort_keys=True),
                    file=sys.stderr,
                    flush=True,
                )
            except (OSError, ValueError):
                pass


def record_private_note_cache_outcome(outcome: PrivateNoteCacheOutcome) -> bool:
    """Count whether the private-note Home cache was usable, without identifiers."""

    if outcome not in PRIVATE_NOTE_CACHE_OUTCOMES:
        return False
    return _record_metric("private_note_cache_outcome", {"cache_outcome": outcome})


def record_client_action_latency(
    operation: str,
    transition: str,
    duration_milliseconds: int,
    streaming: str,
    *,
    expected_account: tuple[str, str | None] | None = None,
) -> bool:
    """Count a bounded UI timing or current foreground health observation."""

    latency_bucket = client_operation_latency_bucket(duration_milliseconds)
    if (
        operation not in CLIENT_PERFORMANCE_OPERATIONS
        or transition not in CLIENT_PERFORMANCE_TRANSITIONS_BY_OPERATION.get(operation, ())
        or streaming not in CLIENT_STREAMING_STATES
        or latency_bucket is None
    ):
        return False
    if transition in {"surface_active", "surface_load_failure"}:
        if duration_milliseconds != 0 or streaming != "unknown" or expected_account is None:
            return False
        return record_client_load_impact(
            "load_failure" if transition == "surface_load_failure" else "active",
            expected_account=expected_account,
        )
    if operation == "recording_start" and expected_account is not None:
        record_client_load_impact(
            "start_attempt" if transition == "click_to_recording" else "start_failure",
            expected_account=expected_account,
        )
    return _record_metric(
        "client_action_latency_bucket",
        {
            "operation": operation,
            "transition": transition,
            "latency_bucket": latency_bucket,
            "streaming": streaming,
            **(
                {"result": "success" if transition == "click_to_recording" else "error"}
                if operation == "recording_start" and expected_account is not None
                else {}
            ),
            **({"ui_version": "unknown"} if transition.startswith("open_to_") else {}),
        },
    )


def record_auth_cache_failure(operation: AuthCacheOperation) -> bool:
    """Count protected-auth-cache failures using only a bounded operation tag."""

    if operation not in AUTH_CACHE_OPERATIONS:
        return False
    return _record_metric("auth_cache_failure", {"auth_cache_operation": operation})


def record_auth_fetch_latency(
    transport: AuthFetchTransport,
    result: AuthFetchResult,
    duration_milliseconds: int,
) -> bool:
    """Count one bounded disposable Codex auth attempt by transport and result."""

    latency_bucket = client_operation_latency_bucket(duration_milliseconds)
    if (
        transport not in AUTH_FETCH_TRANSPORTS
        or result not in AUTH_FETCH_RESULTS
        or latency_bucket is None
    ):
        return False
    return _record_metric(
        "auth_fetch_latency_bucket",
        {
            "auth_transport": transport,
            "result": result,
            "latency_bucket": latency_bucket,
        },
    )


def flush_client_operation_metrics(
    timeout_seconds: float = _STATSC_SHUTDOWN_FLUSH_TIMEOUT_SECONDS,
) -> bool:
    """Flush pending client counters without blocking shutdown indefinitely."""

    try:
        return _CLIENT.flush_and_wait(timeout_seconds)
    except Exception:
        return False
