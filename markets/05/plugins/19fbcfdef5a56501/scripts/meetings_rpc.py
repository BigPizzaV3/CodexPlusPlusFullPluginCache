"""Bounded JSON-RPC transport for the Meetings MCP server."""

from __future__ import annotations

import json
import math
import queue
import sys
import threading
import time
from collections import deque
from collections.abc import Callable, Collection, Mapping
from dataclasses import dataclass, field
from enum import Enum
from typing import Literal, Protocol, TypeAlias, TypeGuard

import codex_auth_client
from meetings_client_policy import update_version
from meetings_metrics import (
    CLIENT_PERFORMANCE_OPERATIONS,
    MAXIMUM_CLIENT_PERFORMANCE_DURATION_MILLISECONDS,
    ClientFailureReason,
    ClientOperation,
    ClientOperationResult,
    NotesRefreshTrigger,
    client_operation_for_tool_call,
    flush_client_operation_metrics,
    notes_refresh_trigger_for_tool_call,
    record_client_operation_attempt,
    record_client_operation_latency,
    record_client_operation_result,
)
from meetings_schema import JSONSchema, JSONValue, is_json_object, is_public_recording_session_id
from meetings_sentry import record_codex_app_version, record_codex_client_info, report_mcp_error
from meetings_tool_context import scoped_tool_arguments

MAXIMUM_RPC_LINE_BYTES = 1 * 1024 * 1024
MAXIMUM_BACKGROUND_RPC_REQUESTS = 8
MAXIMUM_BACKGROUND_LIFECYCLE_RPC_REQUESTS = 4
MAXIMUM_BUFFERED_RPC_INPUT_FRAMES = 8
MAXIMUM_BUFFERED_RPC_OBSERVATIONS = MAXIMUM_BUFFERED_RPC_INPUT_FRAMES + 2
BACKGROUND_RPC_SHUTDOWN_GRACE_SECONDS = 0.25
CODEX_AUTH_CHANGE_CAPABILITY = "codex/auth-change"
CODEX_AUTH_CHANGED_NOTIFICATION = "notifications/codex/authChanged"
# Keep explicit native mutations on the lifecycle lane fenced by terminal Stop.
LOCAL_UI_LIFECYCLE_REQUESTS = frozenset(
    {
        "local.forceStart",
        "local.requestMicrophone",
        "local.requestSystemAudio",
        "local.recheckAudio",
        "local.openMicrophoneSettings",
        "local.openSystemAudioSettings",
        "local.installAndLaunch",
        "local.applyStagedUpdate",
    }
)

RPCId: TypeAlias = str | int | float
RPCMessage: TypeAlias = JSONValue
RPCResponse: TypeAlias = JSONSchema
_RPCRequestObject: TypeAlias = dict[str, JSONValue]
_RPCDispatchLane: TypeAlias = Literal[
    "bootstrap",
    "notes",
    "notes-pagination",
    "note-interaction",
    "settings",
    "calendar",
]
_RPCSubmission: TypeAlias = Literal["accepted", "cancelled", "rejected"]
_RPCWorkState: TypeAlias = Literal[
    "pending",
    "running",
    "responding",
    "cancelled",
    "done",
]


class RPCHandler(Protocol):
    """Handle one decoded JSON-RPC message."""

    def __call__(
        self,
        message: RPCMessage,
        *,
        cancellation_event: threading.Event | None = None,
    ) -> RPCResponse | None: ...


class RPCInputStream(Protocol):
    """Provide binary newline-delimited JSON-RPC input."""

    def readline(self, limit: int = -1, /) -> bytes: ...


class RPCOutputStream(Protocol):
    """Provide binary newline-delimited JSON-RPC output."""

    def write(self, data: bytes, /) -> int | None: ...

    def flush(self) -> None: ...


class _PrivateMeetingsResponse(Protocol):
    request: str
    ok: bool
    data: Mapping[str, object] | None
    error_kind: str | None
    retryable: bool
    backend_auth_rejected: bool


class _RPCService(Protocol):
    DEFAULT_PROFILE: str
    SUPPORTED_PROFILES: Collection[str]
    PROFILE_PROTOTYPE: str
    PROFILE_LOCAL_DEV: str
    PROFILE_PRODUCTION: str
    APP_UI_PROFILES: Collection[str]
    APP_TOOL_NAME_SET: Collection[str]
    APP_TOOL_TARGETS: Mapping[str, str]
    MCP_PROTOCOL_VERSION: str
    STRUCTURED_SETTINGS_READ_TOOL: str
    STRUCTURED_SETTINGS_UPDATE_TOOL: str
    MEETING_MENTIONS_TOOL: str
    DISPLAY_NAME: str
    WIDGET_URI: str
    WIDGET_MIME: str
    SAFE_LOCAL_REQUEST_FAILED_MESSAGE: str
    InvalidArguments: type[Exception]
    MeetingResourceReadError: type[Exception]
    RecordMeetingsCancelled: type[Exception]
    CodexAuthCancelled: type[Exception]

    def schedule_initialize_companion_bootstrap(self) -> None: ...

    def set_rpc_cancellation_event(
        self,
        event: threading.Event | None,
    ) -> threading.Event | None: ...

    def server_info(self, profile: str) -> JSONSchema: ...

    def tool_definitions(self, profile: str) -> list[JSONSchema]: ...

    def require_empty_arguments(self, name: str, arguments: JSONSchema) -> None: ...

    def normalize_local_recording_control(self, arguments: JSONSchema) -> JSONSchema: ...

    def call_tool(
        self,
        name: str,
        arguments: JSONSchema,
        *,
        profile: str = ...,
        host_app_version: str | None = ...,
    ) -> JSONSchema | _PrivateMeetingsResponse: ...

    def private_meetings_tool_result(
        self,
        response: _PrivateMeetingsResponse,
    ) -> RPCResponse: ...

    def tool_result(
        self,
        payload: JSONSchema,
        include_widget: bool = False,
        *,
        extra_meta: JSONSchema | None = None,
    ) -> RPCResponse: ...

    def resource_contents(self) -> JSONSchema: ...

    def meeting_resource_contents(
        self,
        uri: JSONValue | None,
        *,
        cancellation_event: threading.Event | None,
    ) -> JSONSchema: ...

    def meeting_resource_templates(self) -> list[JSONSchema]: ...


def rpc_response(message_id: RPCId | None, result: JSONValue) -> RPCResponse:
    """Build one successful JSON-RPC response.

    Args:
        message_id: Correlation id from the request, or ``None`` for a protocol error.
        result: JSON-compatible result payload.

    Returns:
        A complete JSON-RPC success response.
    """

    return {"jsonrpc": "2.0", "id": message_id, "result": result}


def rpc_error(message_id: RPCId | None, code: int, message: str) -> RPCResponse:
    """Build one JSON-RPC error response.

    Args:
        message_id: Correlation id from the request, or ``None`` when unavailable.
        code: JSON-RPC error code.
        message: Safe client-visible error summary.

    Returns:
        A complete JSON-RPC error response.
    """

    return {
        "jsonrpc": "2.0",
        "id": message_id,
        "error": {"code": code, "message": message},
    }


class _SerializedRPCWriter:
    """Write one complete JSON-RPC line at a time across dispatch lanes."""

    def __init__(self, output: RPCOutputStream) -> None:
        self._output = output
        self._lock = threading.Lock()
        self._state_lock = threading.Lock()
        self._enabled = True
        self._failed = threading.Event()
        self._failure_callback: Callable[[], None] | None = None

    @property
    def failed(self) -> bool:
        return self._failed.is_set()

    def _mark_failed(self) -> None:
        # Publish failure before disabling so the reader/dispatcher can stop
        # admission even if another lane is currently waiting on the write lock.
        with self._state_lock:
            if self._failed.is_set():
                return
            self._failed.set()
            self._enabled = False
            failure_callback = self._failure_callback
        # The callback may wake a foreground reader that immediately checks
        # admission. Never invoke it while holding the admission state lock.
        if failure_callback is not None:
            failure_callback()

    def register_failure_callback(self, callback: Callable[[], None]) -> None:
        """Wake an event-driven reader, including failures before registration."""

        with self._state_lock:
            self._failure_callback = callback
            already_failed = self._failed.is_set()
        if already_failed:
            callback()

    def admit_request(self) -> bool:
        """Linearize request admission against terminal output failure."""

        with self._state_lock:
            return self._enabled and not self._failed.is_set()

    def write(self, response: RPCResponse) -> bool:
        if not self.admit_request():
            return False
        try:
            line = (
                json.dumps(
                    response,
                    ensure_ascii=False,
                    separators=(",", ":"),
                    allow_nan=False,
                )
                + "\n"
            ).encode("utf-8")
        except (TypeError, ValueError, OverflowError):
            self._mark_failed()
            return False
        with self._lock:
            if not self.admit_request():
                return False
            try:
                written = self._output.write(line)
                if isinstance(written, int) and written != len(line):
                    raise OSError("short JSON-RPC write")
                self._output.flush()
            except (BrokenPipeError, OSError, ValueError):
                self._mark_failed()
                return False
        return True

    def disable(self) -> None:
        # Do not wait on the output lock here: its owner may itself be blocked
        # on a pipe whose reader disappeared at the same EOF boundary. The
        # assignment is enough to make every not-yet-started write fail closed,
        # while the daemon lane lets an already-blocked write die with process
        # teardown instead of defeating the bounded shutdown deadline.
        with self._state_lock:
            self._enabled = False


def _supports_codex_auth_changes(params: JSONValue | None) -> bool:
    capabilities = params.get("capabilities") if isinstance(params, dict) else None
    experimental = capabilities.get("experimental") if isinstance(capabilities, dict) else None
    return isinstance(experimental, dict) and isinstance(
        experimental.get(CODEX_AUTH_CHANGE_CAPABILITY), dict
    )


def _valid_auth_generation(value: JSONValue | None) -> TypeGuard[int]:
    return isinstance(value, int) and not isinstance(value, bool) and 0 <= value < 2**64


class _CodexAuthChangeSession:
    """Apply negotiated auth fences as frames enter this stdio connection."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._manager: codex_auth_client.CodexAuthManager | None = None
        self._closed = False

    def observe_input(
        self,
        message: RPCMessage,
        *,
        on_owner_changed: Callable[[], None] | None = None,
    ) -> bool:
        if not isinstance(message, dict) or message.get("jsonrpc") != "2.0":
            return False
        method = message.get("method")
        if method == "initialize":
            if (
                "id" not in message
                or not _valid_rpc_id(message.get("id"))
                or message.get("params") is not None
                and not isinstance(message.get("params"), dict)
            ):
                return False
            with self._lock:
                if not self._closed:
                    if _supports_codex_auth_changes(message.get("params")):
                        self._manager = codex_auth_client.get_process_auth_manager()
                        self._manager.begin_auth_change_session()
                    elif self._manager is not None:
                        self._manager.end_auth_change_session()
                        self._manager = None
            return False
        if method != CODEX_AUTH_CHANGED_NOTIFICATION:
            return False
        # This extension accepts only notifications, never id-bearing requests.
        params = message.get("params")
        if "id" in message or not isinstance(params, dict):
            return True
        generation = params.get("generation")
        owner_generation = params.get("ownerGeneration")
        if not _valid_auth_generation(generation) or not _valid_auth_generation(owner_generation):
            return True
        with self._lock:
            if not self._closed and self._manager is not None:
                if on_owner_changed is None:
                    self._manager.handle_auth_changed(
                        generation=generation,
                        owner_generation=owner_generation,
                    )
                else:
                    self._manager.handle_auth_changed(
                        generation=generation,
                        owner_generation=owner_generation,
                        on_owner_changed=on_owner_changed,
                    )
        return True

    def close(self) -> None:
        """Fence late auth refreshes once, including terminal output failures."""

        with self._lock:
            self._closed = True
            if self._manager is not None:
                self._manager.end_auth_change_session()
                self._manager = None


@dataclass
class _BackgroundRPCWork:
    message: _RPCRequestObject
    message_id: RPCId
    serialization_key: str | None = None
    state: _RPCWorkState = "pending"
    cancellation_event: threading.Event = field(default_factory=threading.Event)
    terminal_fences: set[int] = field(default_factory=lambda: set[int]())

    def is_cancelled(self) -> bool:
        return self.state == "cancelled"


@dataclass
class _BufferedBackgroundRPCObservation:
    message_id: RPCId
    cancelled: bool = False
    terminal_fences: set[int] = field(default_factory=lambda: set[int]())
    account_scoped: bool = False


class _SharedRPCRequestScheduler:
    """Schedule independent RPC classes on one bounded, reusable daemon pool."""

    def __init__(self, *, maximum_workers: int) -> None:
        if maximum_workers < 1:
            raise ValueError("maximum_workers must be positive")
        self._maximum_workers = maximum_workers
        self._condition = threading.Condition()
        self._pending: deque[Callable[[], None]] = deque()
        self._workers: list[threading.Thread] = []
        self._idle_workers = 0
        self._closed = False

    def submit(self, callback: Callable[[], None]) -> None:
        with self._condition:
            if self._closed:
                raise RuntimeError("RPC request scheduler is closed")
            self._pending.append(callback)
            if (
                self._idle_workers < len(self._pending)
                and len(self._workers) < self._maximum_workers
            ):
                worker = threading.Thread(
                    target=self._run,
                    name=f"chatgpt-meetings-mcp-request-{len(self._workers) + 1}",
                    daemon=True,
                )
                self._workers.append(worker)
                worker.start()
            self._condition.notify()

    def shutdown(self, timeout_seconds: float) -> None:
        deadline = time.monotonic() + max(0.0, timeout_seconds)
        with self._condition:
            self._closed = True
            self._pending.clear()
            workers = tuple(self._workers)
            self._condition.notify_all()
        for worker in workers:
            worker.join(timeout=max(0.0, deadline - time.monotonic()))

    def _run(self) -> None:
        while True:
            with self._condition:
                self._idle_workers += 1
                try:
                    while not self._closed and not self._pending:
                        self._condition.wait()
                    if self._closed and not self._pending:
                        return
                    callback = self._pending.popleft()
                finally:
                    self._idle_workers -= 1
            callback()


class _BoundedBackgroundRPCDispatcher:
    """Bound cancellable work while serializing only explicitly related mutations."""

    def __init__(
        self,
        writer: _SerializedRPCWriter,
        handler: RPCHandler,
        *,
        maximum_outstanding: int,
        accepts_message: Callable[[RPCMessage], bool] | None = None,
        worker_name: str = "chatgpt-meetings-mcp-detail",
        scheduler: _SharedRPCRequestScheduler | None = None,
        maximum_concurrent: int = 1,
        serialization_key: Callable[[RPCMessage], str | None] | None = None,
    ) -> None:
        if maximum_outstanding < 1:
            raise ValueError("maximum_outstanding must be positive")
        if not 1 <= maximum_concurrent <= maximum_outstanding:
            raise ValueError("maximum_concurrent must be within outstanding capacity")
        if scheduler is None and maximum_concurrent != 1:
            raise ValueError("concurrent work requires a shared request scheduler")
        self._writer = writer
        self._handler = handler
        self._accepts_message = accepts_message or _uses_background_rpc_lane
        self._maximum_outstanding = maximum_outstanding
        self._maximum_concurrent = maximum_concurrent
        self._serialization_key = serialization_key
        self._condition = threading.Condition()
        self._pending: deque[_BackgroundRPCWork] = deque()
        self._running: list[_BackgroundRPCWork] = []
        self._buffered_observations: deque[_BufferedBackgroundRPCObservation] = deque()
        self._outstanding = 0
        self._next_terminal_fence = 0
        self._active_terminal_fences: set[int] = set()
        self._accepting = True
        self._shutdown_requested = False
        self._emit_responses = True
        self._scheduler = scheduler
        self._scheduled = 0
        self._worker: threading.Thread | None = None
        if scheduler is None:
            self._worker = threading.Thread(
                target=self._run,
                name=worker_name,
                daemon=True,
            )
            self._worker.start()

    def _schedule_locked(self) -> None:
        if (
            self._scheduler is None
            or not self._pending
            or self._active_terminal_fences
            or self._shutdown_requested
        ):
            return
        available = self._maximum_concurrent - len(self._running)
        if available <= 0:
            return
        occupied_keys = {
            work.serialization_key for work in self._running if work.serialization_key is not None
        }
        runnable = 0
        for work in self._pending:
            if work.serialization_key is not None:
                if work.serialization_key in occupied_keys:
                    continue
                occupied_keys.add(work.serialization_key)
            runnable += 1
            if runnable >= available:
                break
        while self._scheduled < runnable:
            self._scheduled += 1
            self._scheduler.submit(self._run_scheduled)

    def observe_buffered_input(self, message: RPCMessage) -> None:
        """Remember bounded read-ahead order so early cancellation is durable."""

        if self._accepts_message(message):
            message_id = _request_id(message)
            if message_id is None:
                raise RuntimeError("background RPC lane accepted a request without an id")
            with self._condition:
                # The pump can hold at most its queue plus the frame currently
                # waiting to enter that queue. Exceeding that bound means the
                # ordering proof is broken, so terminate the pump fail-closed
                # rather than dropping a cancellation occurrence.
                if len(self._buffered_observations) >= MAXIMUM_BUFFERED_RPC_OBSERVATIONS:
                    raise RuntimeError("buffered RPC observation overflow")
                self._buffered_observations.append(
                    _BufferedBackgroundRPCObservation(
                        message_id, account_scoped=_uses_account_scoped_rpc(message)
                    )
                )
            return

        is_cancellation, cancelled_id = _cancelled_background_request_id(message)
        if is_cancellation and cancelled_id is not None:
            self.cancel(cancelled_id)

    def submit(self, message: RPCMessage) -> _RPCSubmission:
        message_id = _request_id(message)
        if not isinstance(message, dict) or message_id is None:
            return "rejected"
        with self._condition:
            observation: _BufferedBackgroundRPCObservation | None = None
            for candidate in self._buffered_observations:
                if _rpc_ids_equal(candidate.message_id, message_id):
                    observation = candidate
                    self._buffered_observations.remove(candidate)
                    break
            if observation is not None and observation.cancelled:
                return "cancelled"
            if (
                not self._accepting
                or not self._writer.admit_request()
                or self._outstanding >= self._maximum_outstanding
            ):
                return "rejected"
            self._outstanding += 1
            work = _BackgroundRPCWork(
                message,
                message_id,
                serialization_key=(
                    self._serialization_key(message)
                    if self._serialization_key is not None
                    else None
                ),
            )
            if observation is not None:
                work.terminal_fences.update(observation.terminal_fences)
            self._pending.append(work)
            self._schedule_locked()
            self._condition.notify()
            return "accepted"

    def cancel(self, message_id: RPCId) -> bool:
        """Cancel one owned background request without a stale response."""

        cancelled = False
        with self._condition:
            for work in self._pending:
                if _rpc_ids_equal(work.message_id, message_id):
                    self._pending.remove(work)
                    work.state = "cancelled"
                    work.cancellation_event.set()
                    self._outstanding -= 1
                    cancelled = True
                    break
            if not cancelled:
                for work in self._running:
                    if _rpc_ids_equal(work.message_id, message_id) and work.state == "running":
                        work.state = "cancelled"
                        work.cancellation_event.set()
                        cancelled = True
                        break
            if not cancelled:
                for observation in self._buffered_observations:
                    if not observation.cancelled and _rpc_ids_equal(
                        observation.message_id, message_id
                    ):
                        observation.cancelled = True
                        cancelled = True
                        break
            self._condition.notify_all()
        return cancelled

    def supersede_all(self, *, account_scoped_only: bool = False) -> list[RPCId]:
        """Cancel admitted/read-ahead work at an owner or terminal Stop boundary."""

        superseded: list[RPCId] = []
        with self._condition:
            for work in tuple(self._pending):
                if account_scoped_only and not _uses_account_scoped_rpc(work.message):
                    continue
                self._pending.remove(work)
                work.state = "cancelled"
                work.cancellation_event.set()
                self._outstanding -= 1
                superseded.append(work.message_id)
            for work in self._running:
                if account_scoped_only and not _uses_account_scoped_rpc(work.message):
                    continue
                if work.state == "running":
                    work.cancellation_event.set()
                    params = _tool_call_params(work.message) if account_scoped_only else None
                    arguments = params.get("arguments") if params is not None else None
                    if (
                        params is not None
                        and params.get("name") == "chatgpt_meetings_get_snapshot"
                        and isinstance(arguments, dict)
                        and arguments.get("request") == "ui.submitFeedback"
                    ):
                        # The sender owns cancellation before POST and acknowledgement
                        # after acceptance. Keep its sole terminal response pending.
                        continue
                    work.state = "cancelled"
                    superseded.append(work.message_id)
            for observation in self._buffered_observations:
                if account_scoped_only and not observation.account_scoped:
                    continue
                if not observation.cancelled:
                    observation.cancelled = True
                    superseded.append(observation.message_id)
            self._condition.notify_all()
        return superseded

    def fail_stop(self) -> None:
        """Stop admission and cooperatively abandon accepted background work."""

        with self._condition:
            self._fail_stop_locked()

    def begin_terminal_fence(self) -> int:
        """Hold pre-Stop lifecycle work until a fenced native Stop settles."""

        with self._condition:
            self._next_terminal_fence += 1
            fence = self._next_terminal_fence
            self._active_terminal_fences.add(fence)
            for work in self._pending:
                work.terminal_fences.add(fence)
            for work in self._running:
                if work.state == "running":
                    work.terminal_fences.add(fence)
            for observation in self._buffered_observations:
                if not observation.cancelled:
                    observation.terminal_fences.add(fence)
            self._condition.notify_all()
            return fence

    def resolve_terminal_fence(self, fence: int, *, accepted: bool) -> list[RPCId]:
        """Cancel only pre-Stop work after the native session check accepts."""

        superseded: list[RPCId] = []
        with self._condition:
            for work in tuple(self._pending):
                if fence not in work.terminal_fences:
                    continue
                work.terminal_fences.discard(fence)
                if not accepted:
                    continue
                self._pending.remove(work)
                work.state = "cancelled"
                work.cancellation_event.set()
                self._outstanding -= 1
                superseded.append(work.message_id)
            for work in self._running:
                if fence not in work.terminal_fences:
                    continue
                work.terminal_fences.discard(fence)
                if accepted and work.state == "running":
                    work.state = "cancelled"
                    work.cancellation_event.set()
                    superseded.append(work.message_id)
            for observation in self._buffered_observations:
                if fence not in observation.terminal_fences:
                    continue
                observation.terminal_fences.discard(fence)
                if accepted and not observation.cancelled:
                    observation.cancelled = True
                    superseded.append(observation.message_id)
            return superseded

    def finish_terminal_fence(self, fence: int) -> None:
        """Release post-Stop lifecycle work after the terminal response."""

        with self._condition:
            self._active_terminal_fences.discard(fence)
            self._schedule_locked()
            self._condition.notify_all()

    def _drop_pending_locked(self) -> None:
        dropped = len(self._pending)
        for work in self._pending:
            work.state = "cancelled"
            work.cancellation_event.set()
        self._pending.clear()
        self._outstanding -= dropped

    def _fail_stop_locked(self) -> None:
        self._accepting = False
        self._emit_responses = False
        self._drop_pending_locked()
        self._buffered_observations.clear()
        self._active_terminal_fences.clear()
        for work in self._running:
            if work.state == "running":
                work.state = "cancelled"
                work.cancellation_event.set()
        self._shutdown_requested = True
        self._condition.notify_all()

    def shutdown(self, timeout_seconds: float) -> bool:
        """Cancel accepted work, then give cooperative cleanup a bounded grace."""

        deadline = time.monotonic() + max(0.0, timeout_seconds)
        timed_out = False
        with self._condition:
            self._accepting = False
            self._emit_responses = False
            self._drop_pending_locked()
            self._buffered_observations.clear()
            self._active_terminal_fences.clear()
            for work in self._running:
                work.state = "cancelled"
                work.cancellation_event.set()
            self._shutdown_requested = True
            self._condition.notify_all()
            while self._outstanding > 0:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    timed_out = True
                    break
                self._condition.wait(timeout=remaining)

        if timed_out:
            # stdin EOF means the client is gone. Prevent a late native
            # completion from writing into a reused test stream or broken pipe.
            self._writer.disable()
        if self._worker is not None:
            self._worker.join(timeout=max(0.0, deadline - time.monotonic()))
        return not timed_out

    def _run(self) -> None:
        while True:
            with self._condition:
                while not self._shutdown_requested and (
                    not self._pending or self._active_terminal_fences
                ):
                    self._condition.wait()
                if self._shutdown_requested and not self._pending:
                    return
                if self._writer.failed:
                    self._fail_stop_locked()
                    return
                work = self._pending.popleft()
                work.state = "running"
                self._running.append(work)

            self._run_work(work)

    def _run_scheduled(self) -> None:
        with self._condition:
            self._scheduled -= 1
            if self._shutdown_requested or not self._pending or self._active_terminal_fences:
                return
            if self._writer.failed:
                self._fail_stop_locked()
                return
            occupied_keys = {
                running.serialization_key
                for running in self._running
                if running.serialization_key is not None
            }
            work = next(
                (
                    pending
                    for pending in self._pending
                    if pending.serialization_key is None
                    or pending.serialization_key not in occupied_keys
                ),
                None,
            )
            if work is None or len(self._running) >= self._maximum_concurrent:
                return
            self._pending.remove(work)
            work.state = "running"
            self._running.append(work)
        self._run_work(work)
        with self._condition:
            self._schedule_locked()

    def _run_work(self, work: _BackgroundRPCWork) -> None:
        try:
            response = self._handler(
                work.message,
                cancellation_event=work.cancellation_event,
            )
        except Exception:
            report_mcp_error("rpc", "exception")
            response = rpc_error(work.message_id, -32603, "Internal error")

        with self._condition:
            emit_response = self._emit_responses and not work.is_cancelled()
            if emit_response:
                # Cancellation that arrives after this commit observes a
                # completed request and cannot create a second response.
                work.state = "responding"
        write_succeeded = True
        if emit_response and response is not None:
            write_succeeded = self._writer.write(response)

        with self._condition:
            if not write_succeeded:
                self._fail_stop_locked()
            work.state = "done"
            self._running.remove(work)
            self._outstanding -= 1
            self._condition.notify_all()


def _background_rpc_lane(message: RPCMessage) -> _RPCDispatchLane | None:
    """Classify one valid slow request without interpreting malformed arguments."""

    if (
        isinstance(message, dict)
        and message.get("jsonrpc") == "2.0"
        and "id" in message
        and _valid_rpc_id(message.get("id"))
        and message.get("method") == "tools/list"
    ):
        # Optional startup rollout evaluation must not block Ping or recording control.
        return "bootstrap"

    if (
        isinstance(message, dict)
        and message.get("jsonrpc") == "2.0"
        and "id" in message
        and _valid_rpc_id(message.get("id"))
        and message.get("method") == "resources/read"
    ):
        resource_params = message.get("params")
        resource_uri = resource_params.get("uri") if isinstance(resource_params, dict) else None
        if isinstance(resource_uri, str) and resource_uri.startswith(
            ("meetings://meeting/", "meetings://note/")
        ):
            return "note-interaction"

    params = _tool_call_params(message)
    if params is None:
        return None
    if params.get("name") in {"settings.read", "settings.update"}:
        return "settings"
    if params.get("name") == "meetings.search_mentions":
        return "notes"
    if params.get("name") != "chatgpt_meetings_get_snapshot":
        return None
    arguments = params.get("arguments")
    if arguments is not None and not isinstance(arguments, dict):
        return None
    request = arguments.get("request") if isinstance(arguments, dict) else None
    if request in LOCAL_UI_LIFECYCLE_REQUESTS:
        return None
    if request in {
        "settings.get",
        "settings.update",
    }:
        return "settings"
    if request == "home.bootstrap":
        return "bootstrap"
    if arguments == {"section": "calendar"} or request == "calendar.list":
        return "calendar"
    if request == "notes.list":
        return (
            "notes-pagination"
            if isinstance(arguments, dict) and "pageToken" in arguments
            else "notes"
        )
    if request is None:
        return "notes"
    return "note-interaction"


def _uses_background_rpc_lane(message: RPCMessage) -> bool:
    return _background_rpc_lane(message) is not None


def _background_mutation_serialization_key(message: RPCMessage) -> str | None:
    """Serialize writes to one resource without introducing product-specific lanes."""

    params = _tool_call_params(message)
    if params is None:
        return None
    if params.get("name") == "settings.update":
        arguments = params.get("arguments")
        changes = arguments.get("set") if isinstance(arguments, dict) else None
        if isinstance(changes, dict) and any(
            name in changes
            for name in (
                "recordingNotificationsEnabled",
                "soundEffectsEnabled",
                "meetingDetectionEnabled",
            )
        ):
            return "native-settings"
        return "hosted-settings"
    if params.get("name") != "chatgpt_meetings_get_snapshot":
        return None
    arguments = params.get("arguments")
    if not isinstance(arguments, dict):
        return None
    request = arguments.get("request")
    if request == "settings.update":
        return "hosted-settings"
    if request == "local.updateSettings":
        return "native-settings"
    if request == "local.retryUpload":
        recording_id = arguments.get("recordingId")
        return f"recording:{recording_id}" if isinstance(recording_id, str) else "invalid-upload"
    if request not in {"note.delete", "note.reprocess", "note.share", "note.feedback"}:
        return None
    note_id = arguments.get("noteId")
    return f"note:{note_id}" if isinstance(note_id, str) else "invalid-note-mutation"


def _uses_lifecycle_rpc_lane(message: RPCMessage) -> bool:
    """Isolate non-terminal local mutations so status and Stop can overtake."""

    params = _tool_call_params(message)
    if params is None:
        return False
    name = params.get("name")
    arguments = params.get("arguments")
    if name == "chatgpt_meetings_get_snapshot":
        return (
            isinstance(arguments, dict) and arguments.get("request") in LOCAL_UI_LIFECYCLE_REQUESTS
        )
    if name not in {
        "meetings.requestMicrophone",
        "meetings.requestSystemAudio",
        "meetings.recheckAudio",
        "meetings.start",
        "meetings.installAndLaunch",
        "meetings.applyStagedUpdate",
        "chatgpt_meetings_start_local",
        "chatgpt_meetings_take_notes",
        "meetings.takeNotes",
    }:
        return False
    return arguments is None or isinstance(arguments, dict)


def _uses_account_scoped_rpc(message: RPCMessage) -> bool:
    """Identify hosted account work without cancelling device-owned controls."""

    if _background_rpc_lane(message) is None:
        return False
    params = _tool_call_params(message)
    if params is None:
        # The background lane also accepts authenticated Meetings resources.
        return True
    arguments = params.get("arguments")
    request = arguments.get("request") if isinstance(arguments, dict) else None
    return request is None or (
        isinstance(request, str)
        and (
            request.startswith(("notes.", "note.", "calendar.", "settings."))
            or request
            in {
                "analytics.track",
                "home.bootstrap",
                "connection.ensure",
                "prompt.note",
                "local.getUploads",
                "local.retryUpload",
                "ui.submitFeedback",
            }
        )
    )


def _is_terminal_stop_rpc(message: RPCMessage) -> bool:
    params = _tool_call_params(message)
    if params is None or params.get("name") not in {
        "meetings.stop",
        "chatgpt_meetings_stop_local",
    }:
        return False
    arguments = params.get("arguments")
    return arguments is None or (isinstance(arguments, dict) and not arguments)


def _is_fenced_stop_rpc(message: RPCMessage) -> bool:
    params = _tool_call_params(message)
    if params is None or params.get("name") not in {
        "meetings.stop",
        "chatgpt_meetings_stop_local",
    }:
        return False
    arguments = params.get("arguments")
    return (
        isinstance(arguments, dict)
        and set(arguments) == {"expectedSessionId"}
        and is_public_recording_session_id(arguments["expectedSessionId"])
    )


def _accepted_terminal_stop_response(response: RPCResponse | None) -> bool:
    if not isinstance(response, dict):
        return False
    result = response.get("result")
    if not isinstance(result, dict) or result.get("isError") is True:
        return False
    structured = result.get("structuredContent")
    if not isinstance(structured, dict) or structured.get("ok") is not True:
        return False
    state = structured.get("state")
    if not isinstance(state, dict):
        return False
    if structured.get("protocolVersion") != 2:
        return False
    recording = state.get("recording")
    if not isinstance(recording, dict):
        return False
    controls = recording.get("controls")
    stop = controls.get("stop") if isinstance(controls, dict) else None
    return (
        recording.get("phase") == "idle"
        and recording.get("session") is None
        and isinstance(stop, dict)
        and stop.get("enabled") is False
    )


def _tool_call_params(message: RPCMessage) -> _RPCRequestObject | None:
    if (
        not isinstance(message, dict)
        or message.get("jsonrpc") != "2.0"
        or "id" not in message
        or not _valid_rpc_id(message.get("id"))
        or message.get("method") != "tools/call"
    ):
        return None
    params = message.get("params")
    return params if isinstance(params, dict) else None


def _cancelled_background_request_id(
    message: RPCMessage,
) -> tuple[Literal[False], None] | tuple[Literal[True], RPCId]:
    if not isinstance(message, dict) or message.get("jsonrpc") != "2.0" or "id" in message:
        return False, None
    method = message.get("method")
    params = message.get("params")
    if not isinstance(params, dict):
        return False, None
    if method == "notifications/cancelled":
        request_id = params.get("requestId")
        reason = params.get("reason")
        if (
            request_id is not None
            and _valid_rpc_id(request_id)
            and (reason is None or isinstance(reason, str))
        ):
            return True, request_id
    if method == "$/cancelRequest":
        request_id = params.get("id")
        if request_id is not None and _valid_rpc_id(request_id):
            return True, request_id
    return False, None


def _valid_rpc_id(value: object) -> TypeGuard[RPCId]:
    if isinstance(value, str):
        return True
    if isinstance(value, int) and not isinstance(value, bool):
        return True
    return isinstance(value, float) and math.isfinite(value)


def _rpc_ids_equal(left: object, right: object) -> bool:
    """Compare already-validated IDs without Python's bool/int aliasing."""

    if not _valid_rpc_id(left) or not _valid_rpc_id(right):
        return False
    if isinstance(left, str) or isinstance(right, str):
        return isinstance(left, str) and isinstance(right, str) and left == right
    return left == right


def _request_id(message: RPCMessage) -> RPCId | None:
    if not isinstance(message, dict) or "id" not in message:
        return None
    message_id = message["id"]
    return message_id if _valid_rpc_id(message_id) else None


def _record_client_operation_payload(
    operation: ClientOperation,
    payload: JSONSchema | _PrivateMeetingsResponse,
    cancellation_event: threading.Event | None,
    started_at_nanoseconds: int | None,
    *,
    refresh_trigger: NotesRefreshTrigger | None = None,
) -> None:
    """Record one terminal outcome without inspecting user or error text."""

    if isinstance(payload, dict):
        readiness = payload.get("readiness")
        error_kind: str | None = (
            "connection"
            if isinstance(readiness, dict) and readiness.get("status") == "companion-unavailable"
            else None
        )
        candidate_ok = payload.get("ok")
        ok = candidate_ok if isinstance(candidate_ok, bool) else None
    else:
        error_kind = "backend" if payload.backend_auth_rejected else payload.error_kind
        ok = payload.ok
    if error_kind == "cancelled":
        _record_client_operation_outcome(
            operation,
            "cancelled",
            started_at_nanoseconds,
            refresh_trigger=refresh_trigger,
        )
        return
    if ok is False and cancellation_event is not None and cancellation_event.is_set():
        _record_client_operation_outcome(
            operation,
            "cancelled",
            started_at_nanoseconds,
            refresh_trigger=refresh_trigger,
        )
        return
    if ok is not False:
        _record_client_operation_outcome(
            operation,
            "success",
            started_at_nanoseconds,
            refresh_trigger=refresh_trigger,
        )
        return
    reason_by_error_kind: dict[str, ClientFailureReason] = {
        "auth": "auth",
        "backend": "backend",
        "connection": "connection",
        "invalid-handle": "not_found",
        "invalid-response": "invalid_response",
        "timeout": "timeout",
    }
    reason = reason_by_error_kind.get(error_kind) if error_kind is not None else None
    if reason is None:
        reason = (
            "connection"
            if operation in {"recording_start", "recording_stop", "recording_status"}
            else "backend"
        )
    _record_client_operation_outcome(
        operation,
        "error",
        started_at_nanoseconds,
        reason,
        refresh_trigger=refresh_trigger,
    )


def _record_client_operation_outcome(
    operation: ClientOperation,
    result: ClientOperationResult,
    started_at_nanoseconds: int | None,
    failure_reason: ClientFailureReason | None = None,
    *,
    refresh_trigger: NotesRefreshTrigger | None = None,
) -> None:
    if refresh_trigger is not None:
        if failure_reason is None:
            record_client_operation_result(operation, result, refresh_trigger=refresh_trigger)
        else:
            record_client_operation_result(
                operation,
                result,
                failure_reason,
                refresh_trigger=refresh_trigger,
            )
    elif failure_reason is None:
        record_client_operation_result(operation, result)
    else:
        record_client_operation_result(operation, result, failure_reason)
    if started_at_nanoseconds is not None:
        try:
            completed_at_nanoseconds = time.monotonic_ns()
        except Exception:
            return
        elapsed_milliseconds = min(
            MAXIMUM_CLIENT_PERFORMANCE_DURATION_MILLISECONDS,
            max(0, completed_at_nanoseconds - started_at_nanoseconds) // 1_000_000,
        )
        record_client_operation_latency(operation, result, elapsed_milliseconds)


def _client_operation_started_at_nanoseconds(operation: ClientOperation | None) -> int | None:
    if operation not in CLIENT_PERFORMANCE_OPERATIONS:
        return None
    try:
        return time.monotonic_ns()
    except Exception:
        return None


def _record_client_operation_start(
    operation: ClientOperation,
    refresh_trigger: NotesRefreshTrigger | None,
) -> None:
    if refresh_trigger is None:
        record_client_operation_attempt(operation)
    else:
        record_client_operation_attempt(operation, refresh_trigger=refresh_trigger)


def _record_client_operation_exception(
    operation: ClientOperation,
    error: Exception,
    cancellation_event: threading.Event | None,
    started_at_nanoseconds: int | None,
    *,
    refresh_trigger: NotesRefreshTrigger | None = None,
) -> None:
    if cancellation_event is not None and cancellation_event.is_set():
        _record_client_operation_outcome(
            operation,
            "cancelled",
            started_at_nanoseconds,
            refresh_trigger=refresh_trigger,
        )
    elif isinstance(error, TimeoutError):
        _record_client_operation_outcome(
            operation,
            "error",
            started_at_nanoseconds,
            "timeout",
            refresh_trigger=refresh_trigger,
        )
    elif isinstance(error, ConnectionError):
        _record_client_operation_outcome(
            operation,
            "error",
            started_at_nanoseconds,
            "connection",
            refresh_trigger=refresh_trigger,
        )
    else:
        reason = (
            "connection"
            if operation in {"recording_start", "recording_stop", "recording_status"}
            else "backend"
        )
        _record_client_operation_outcome(
            operation,
            "error",
            started_at_nanoseconds,
            reason,
            refresh_trigger=refresh_trigger,
        )


def handle_rpc(
    message: RPCMessage,
    *,
    service: _RPCService,
    cancellation_event: threading.Event | None = None,
    profile: str | None = None,
) -> RPCResponse | None:
    """Dispatch one decoded JSON-RPC message through the Meetings service.

    Args:
        message: Decoded JSON value received from the MCP client.
        service: Meetings application operations used by the transport.
        cancellation_event: Optional cooperative cancellation signal.
        profile: Optional MCP tool profile override.

    Returns:
        A JSON-RPC response for requests, or ``None`` for notifications and
        client responses that must not receive another response.
    """

    if profile is None:
        profile = service.DEFAULT_PROFILE
    if profile not in service.SUPPORTED_PROFILES:
        raise ValueError(f"unknown MCP profile: {profile}")
    if not isinstance(message, dict):
        return rpc_error(None, -32600, "Invalid Request")
    if message.get("jsonrpc") != "2.0":
        return rpc_error(None, -32600, "Invalid Request")
    message_id = _request_id(message)
    if "id" in message and message_id is None:
        return rpc_error(None, -32600, "Invalid Request")
    # Ignore response frames; never reply with an error to another response.
    if "method" not in message and ("result" in message or "error" in message):
        return None
    method = message.get("method")
    if not isinstance(method, str):
        return rpc_error(message_id, -32600, "Invalid Request")
    # Valid JSON-RPC notifications have no id and never receive a response.
    # MCP tool calls are request/response operations, so an id-less tools/call
    # is ignored rather than allowed to consume private detail capacity or
    # perform an app action without an owning request.
    if "id" not in message or method.startswith("notifications/") or method == "$/cancelRequest":
        return None
    if message_id is None:
        return rpc_error(None, -32600, "Invalid Request")
    raw_params = message.get("params")
    if raw_params is not None and not isinstance(raw_params, dict):
        return rpc_error(message_id, -32602, "Invalid params")
    params = raw_params or {}
    if method == "initialize":
        record_codex_client_info(params.get("clientInfo"))
        capabilities: JSONSchema = {
            "tools": {"listChanged": False},
            "resources": {"listChanged": False, "subscribe": False},
        }
        experimental: JSONSchema = {}
        if _supports_codex_auth_changes(params):
            experimental[CODEX_AUTH_CHANGE_CAPABILITY] = {}
        if profile in service.APP_UI_PROFILES:
            # This runtime uses MCP 2025-11-25, before capabilities.extensions.
            experimental["openai/settings"] = {
                "readTool": service.STRUCTURED_SETTINGS_READ_TOOL,
                "updateTool": service.STRUCTURED_SETTINGS_UPDATE_TOOL,
            }
        if experimental:
            capabilities["experimental"] = experimental
        # Starting the verified background companion does not start recording
        # or request microphone permissions; every supported runtime profile
        # shares its coalesced recovery lane before an explicit capture gesture.
        if profile in (
            service.PROFILE_PROTOTYPE,
            service.PROFILE_LOCAL_DEV,
            service.PROFILE_PRODUCTION,
        ):
            service.schedule_initialize_companion_bootstrap()
        return rpc_response(
            message_id,
            {
                "protocolVersion": service.MCP_PROTOCOL_VERSION,
                "capabilities": capabilities,
                "serverInfo": service.server_info(profile),
                "instructions": (
                    "Use the Meetings UI for local capture. "
                    "Native install, permission, local recording, and hosted "
                    "bot dispatch actions are app-only user gestures."
                ),
            },
        )
    if method == "ping":
        return rpc_response(message_id, {})
    if method == "tools/list":
        return rpc_response(
            message_id,
            {"tools": service.tool_definitions(profile)},
        )
    if method == "tools/call":
        name = params.get("name")
        arguments = params.get("arguments", {})
        if arguments is None:
            arguments = {}
        if not isinstance(name, str) or not isinstance(arguments, dict):
            return rpc_error(message_id, -32602, "tools/call requires an argument object")
        if profile in service.APP_UI_PROFILES and name not in service.APP_TOOL_NAME_SET:
            return rpc_error(message_id, -32602, "unknown tool")
        if profile in service.APP_UI_PROFILES:
            # Observe before attempt/auth metrics and before dispatch can emit Sentry events.
            record_codex_app_version(params.get("_meta"))
        is_recording_status = name == "chatgpt_meetings_local_status"
        status_started_at = time.monotonic() if is_recording_status else None
        if is_recording_status:
            from companion_client import observe_recording_status_request

            observe_recording_status_request("started")
        dispatch_name = (
            service.APP_TOOL_TARGETS.get(name, name) if profile in service.APP_UI_PROFILES else name
        )
        client_operation = (
            client_operation_for_tool_call(name, arguments)
            if profile in service.APP_UI_PROFILES
            else None
        )
        operation_started_at_nanoseconds = _client_operation_started_at_nanoseconds(
            client_operation
        )
        refresh_trigger = notes_refresh_trigger_for_tool_call(name, arguments)
        if client_operation is not None:
            _record_client_operation_start(client_operation, refresh_trigger)
        try:
            metadata = params.get("_meta")
            codex_version = (
                update_version(metadata.get("chatgpt-meetings/codex-app-version"))
                if profile in service.APP_UI_PROFILES and isinstance(metadata, dict)
                else ""
            )
            # Scope optional UI metadata without changing recording action arguments.
            with scoped_tool_arguments(
                dispatch_name,
                arguments,
                app_ui_allowed=profile in service.APP_UI_PROFILES,
                host_app_version=codex_version or None,
                recording_app_instance=(
                    metadata.get("chatgpt-meetings/app-instance-id")
                    if isinstance(metadata, dict)
                    else None
                ),
            ) as scoped_arguments:
                assert is_json_object(scoped_arguments)
                arguments = scoped_arguments
                if profile in service.APP_UI_PROFILES and name == "chatgpt_meetings_start_local":
                    # Calendar Start adds bounded context; toolbar Start stays empty.
                    service.require_empty_arguments(
                        name,
                        {
                            key: value
                            for key, value in arguments.items()
                            if key not in {"clientContext", "calendarContext"}
                        },
                    )
                elif profile in service.APP_UI_PROFILES and name == "chatgpt_meetings_stop_local":
                    arguments = service.normalize_local_recording_control(arguments)
                previous_cancellation = service.set_rpc_cancellation_event(cancellation_event)
                try:
                    # Preserve the ordinary two-argument prototype boundary for
                    # existing test seams. Both profiles use canonical backend
                    # reads and never consult native Notes snapshots.
                    payload = (
                        service.call_tool(name, arguments)
                        if profile == service.PROFILE_PROTOTYPE
                        else service.call_tool(
                            dispatch_name,
                            arguments,
                            profile=profile,
                            host_app_version=codex_version or None,
                        )
                    )
                finally:
                    service.set_rpc_cancellation_event(previous_cancellation)
            if client_operation is not None:
                _record_client_operation_payload(
                    client_operation,
                    payload,
                    cancellation_event,
                    operation_started_at_nanoseconds,
                    refresh_trigger=refresh_trigger,
                )
            if not isinstance(payload, dict):
                return rpc_response(
                    message_id,
                    service.private_meetings_tool_result(payload),
                )
            if is_recording_status and profile in service.APP_UI_PROFILES:
                # Negotiate presentation context on existing reads, independently
                # of native control versions. Old UI bundles ignore this field.
                payload = {**payload, "recordingAppInstanceSupported": True}
            if name == service.MEETING_MENTIONS_TOOL:
                return rpc_response(message_id, {"content": [], "structuredContent": payload})
            extra_meta: JSONSchema | None = None
            if name in {"chatgpt_meetings_open", "meetings.open"}:
                extra_meta = {"snapshot": payload["snapshot"]}
                if profile in service.APP_UI_PROFILES:
                    extra_meta["meetingsUiGateway"] = "v1"
            result = service.tool_result(
                payload,
                include_widget=name in {"meetings.open", "chatgpt_meetings_open"},
                extra_meta=extra_meta,
            )
            if is_recording_status and (
                cancellation_event is None or not cancellation_event.is_set()
            ):
                from companion_client import observe_recording_status_request

                availability = payload.get("availability")
                availability_status = (
                    availability.get("status") if isinstance(availability, dict) else None
                )
                if payload.get("ok") is True:
                    outcome = "ready"
                    reason = None
                elif availability_status == "loading":
                    outcome = "loading"
                    reason = None
                else:
                    outcome = "failed"
                    candidate = (
                        availability.get("reason") if isinstance(availability, dict) else None
                    )
                    reason = (
                        candidate
                        if isinstance(candidate, str)
                        and candidate
                        in {"connection-failed", "owner-invalid", "companion-unavailable"}
                        else "invalid-status-response"
                    )
                observe_recording_status_request(
                    outcome,
                    reason=reason,
                    duration_millis=(
                        round((time.monotonic() - status_started_at) * 1000)
                        if status_started_at is not None
                        else None
                    ),
                )
            return rpc_response(message_id, result)
        except service.InvalidArguments as exc:
            if is_recording_status:
                from companion_client import observe_recording_status_request

                observe_recording_status_request(
                    "failed",
                    error=exc,
                    reason="invalid-arguments",
                    duration_millis=(
                        round((time.monotonic() - status_started_at) * 1000)
                        if status_started_at is not None
                        else None
                    ),
                )
            if client_operation is not None:
                _record_client_operation_outcome(
                    client_operation,
                    "error",
                    operation_started_at_nanoseconds,
                    "invalid_response",
                    refresh_trigger=refresh_trigger,
                )
            return rpc_error(message_id, -32602, str(exc))
        except Exception as exc:
            if name == service.MEETING_MENTIONS_TOOL and isinstance(
                exc,
                (
                    service.MeetingResourceReadError,
                    service.RecordMeetingsCancelled,
                    service.CodexAuthCancelled,
                ),
            ):
                return rpc_error(message_id, -32000, "Meeting suggestions are unavailable.")
            from native_runtime import log_native_runtime_event

            error_type = type(exc).__name__
            log_native_runtime_event(
                "mcp-tool",
                "failed",
                trigger=name,
                error_kind=(
                    error_type
                    if error_type.isascii() and error_type.isidentifier() and len(error_type) <= 64
                    else "UnknownError"
                ),
                reason="exception",
            )
            if is_recording_status:
                from companion_client import observe_recording_status_request

                observe_recording_status_request(
                    "failed",
                    error=exc,
                    reason="mcp-exception",
                    duration_millis=(
                        round((time.monotonic() - status_started_at) * 1000)
                        if status_started_at is not None
                        else None
                    ),
                )
            if client_operation is not None:
                _record_client_operation_exception(
                    client_operation,
                    exc,
                    cancellation_event,
                    operation_started_at_nanoseconds,
                    refresh_trigger=refresh_trigger,
                )
            report_mcp_error("rpc", "exception")
            return rpc_response(
                message_id,
                service.tool_result(
                    {
                        "ok": False,
                        "error": service.SAFE_LOCAL_REQUEST_FAILED_MESSAGE,
                    }
                ),
            )
    if method == "resources/list":
        return rpc_response(
            message_id,
            {
                "resources": [
                    {
                        "name": "chatgpt-meetings-home",
                        "title": service.DISPLAY_NAME,
                        "uri": service.WIDGET_URI,
                        "description": (
                            "Fullscreen Meetings workspace with direct-backend "
                            "Calendar and Notes plus local recording controls."
                        ),
                        "mimeType": service.WIDGET_MIME,
                    }
                ]
            },
        )
    if method == "resources/read":
        uri = params.get("uri")
        if uri == service.WIDGET_URI:
            return rpc_response(message_id, service.resource_contents())
        try:
            return rpc_response(
                message_id,
                service.meeting_resource_contents(
                    uri,
                    cancellation_event=cancellation_event,
                ),
            )
        except service.InvalidArguments as exc:
            return rpc_error(message_id, -32602, str(exc))
        except service.MeetingResourceReadError:
            return rpc_error(message_id, -32000, "Meeting resource is unavailable.")
        except Exception:
            report_mcp_error("rpc", "exception")
            return rpc_error(message_id, -32000, "Meeting resource is unavailable.")
    if method == "resources/templates/list":
        return rpc_response(
            message_id,
            {"resourceTemplates": service.meeting_resource_templates()},
        )
    if method == "prompts/list":
        return rpc_response(message_id, {"prompts": []})
    return rpc_error(message_id, -32601, f"Method not found: {method}")


def _discard_oversized_rpc_frame_remainder(
    input_stream: RPCInputStream,
    prefix: bytes,
) -> None:
    """Consume one rejected physical line without retaining attacker bytes."""

    chunk = prefix
    while chunk and not chunk.endswith(b"\n"):
        chunk = input_stream.readline(MAXIMUM_RPC_LINE_BYTES + 1)


class _RPCInputMarker(Enum):
    EOF = "eof"
    OVERSIZED = "oversized"
    TERMINATED = "terminated"
    OBSERVED_CANCELLATION = "observed-cancellation"


@dataclass(frozen=True)
class _RPCCancelledRequests:
    """Complete cancelled calls at their owner boundary's ordered input position."""

    request_ids: tuple[RPCId, ...]


_RPCInputItem: TypeAlias = bytes | _RPCInputMarker | _RPCCancelledRequests


class _BoundedRPCInputPump:
    """Read one line ahead so background output failure can wake the server."""

    def __init__(
        self,
        input_stream: RPCInputStream,
        *,
        input_observer: Callable[[RPCMessage], bool | _RPCCancelledRequests | None],
        disconnect_observer: Callable[[], None] | None = None,
    ) -> None:
        self._input_stream = input_stream
        self._input_observer = input_observer
        self._disconnect_observer = disconnect_observer
        self._items: queue.Queue[_RPCInputItem] = queue.Queue(
            maxsize=MAXIMUM_BUFFERED_RPC_INPUT_FRAMES
        )
        self._stop = threading.Event()
        self._thread = threading.Thread(
            target=self._run,
            name="chatgpt-meetings-mcp-input",
            daemon=True,
        )
        self._thread.start()

    def _offer(self, item: _RPCInputItem) -> bool:
        while not self._stop.is_set():
            try:
                self._items.put(item, timeout=0.05)
                return True
            except queue.Full:
                continue
        return False

    def _run(self) -> None:
        while not self._stop.is_set():
            try:
                line = self._input_stream.readline(MAXIMUM_RPC_LINE_BYTES + 1)
                if len(line) > MAXIMUM_RPC_LINE_BYTES:
                    _discard_oversized_rpc_frame_remainder(self._input_stream, line)
                    item: _RPCInputItem = _RPCInputMarker.OVERSIZED
                else:
                    item = line
            except Exception:
                line = b""
                item = line
            if line and item is not _RPCInputMarker.OVERSIZED:
                try:
                    observed: RPCMessage = json.loads(
                        line,
                        parse_constant=int,
                    )
                except (ValueError, UnicodeDecodeError, RecursionError):
                    observed = None
                if observed is not None:
                    try:
                        observation = self._input_observer(observed)
                    except Exception:
                        line = b""
                        item = line
                    else:
                        is_cancellation, _ = _cancelled_background_request_id(observed)
                        if isinstance(observation, _RPCCancelledRequests):
                            item = observation
                        elif observation or is_cancellation:
                            # The observer already applied this ordered control
                            # frame against buffered/running work or a pending
                            # server-owned request. Do not replay it later on
                            # the foreground reader after IDs are reused.
                            item = _RPCInputMarker.OBSERVED_CANCELLATION
            if not line and self._disconnect_observer is not None:
                try:
                    self._disconnect_observer()
                except Exception:
                    # Disconnect cleanup is best-effort: an unavailable
                    # provider must never prevent ordinary EOF propagation.
                    pass
            if not self._offer(item) or not line:
                return

    def wake_on_output_failure(self) -> None:
        """Wake an idle reader without waiting behind bounded input backpressure."""

        try:
            self._items.put_nowait(_RPCInputMarker.TERMINATED)
        except queue.Full:
            # A full queue already guarantees the reader cannot block in get.
            # Its failure checks reject every buffered request instead.
            return

    def next_line(self, writer: _SerializedRPCWriter) -> _RPCInputItem:
        while not writer.failed:
            try:
                # Untimed Queue.get is uninterruptible on Windows, so retain
                # its existing timeout there while keeping POSIX event-driven.
                line = (
                    self._items.get(timeout=0.05) if sys.platform == "win32" else self._items.get()
                )
            except queue.Empty:
                continue
            if writer.failed or line is _RPCInputMarker.TERMINATED:
                return _RPCInputMarker.TERMINATED
            return _RPCInputMarker.EOF if not line else line
        return _RPCInputMarker.TERMINATED

    def stop(self) -> None:
        self._stop.set()
        self._thread.join(timeout=0.05)


def serve_rpc(
    input_stream: RPCInputStream,
    output_stream: RPCOutputStream,
    *,
    handler: RPCHandler,
    maximum_background_requests: int = MAXIMUM_BACKGROUND_RPC_REQUESTS,
    maximum_lifecycle_requests: int = MAXIMUM_BACKGROUND_LIFECYCLE_RPC_REQUESTS,
    shutdown_grace_seconds: float = BACKGROUND_RPC_SHUTDOWN_GRACE_SECONDS,
    disconnect_observer: Callable[[], None] | None = None,
) -> None:
    """Serve JSON-RPC with one shared scheduler and ordered request classes.

    Args:
        input_stream: Binary newline-delimited JSON-RPC input.
        output_stream: Binary newline-delimited JSON-RPC output.
        handler: Application request handler.
        maximum_background_requests: Shared hosted-request outstanding bound.
        maximum_lifecycle_requests: Outstanding native lifecycle request bound.
        shutdown_grace_seconds: Cooperative worker shutdown deadline.
        disconnect_observer: Optional best-effort callback when input closes.

    Returns:
        ``None`` after EOF, output failure, or terminal input failure.
    """

    writer = _SerializedRPCWriter(output_stream)
    auth_changes = _CodexAuthChangeSession()
    scheduler = _SharedRPCRequestScheduler(maximum_workers=8)

    background = _BoundedBackgroundRPCDispatcher(
        writer,
        handler,
        maximum_outstanding=maximum_background_requests,
        accepts_message=_uses_background_rpc_lane,
        scheduler=scheduler,
        # Keep scheduler capacity available for recording mutations, even
        # when backend reads stall.
        maximum_concurrent=min(maximum_background_requests, 6),
        serialization_key=_background_mutation_serialization_key,
    )
    lifecycle = _BoundedBackgroundRPCDispatcher(
        writer,
        handler,
        maximum_outstanding=maximum_lifecycle_requests,
        accepts_message=_uses_lifecycle_rpc_lane,
        scheduler=scheduler,
    )
    dispatchers = (background, lifecycle)
    terminal_cancellations: deque[list[RPCId]] = deque()
    terminal_cancellations_lock = threading.Lock()
    fenced_terminal_gates: deque[int] = deque()
    fenced_terminal_gates_lock = threading.Lock()

    def observe_buffered_input(message: RPCMessage) -> bool | _RPCCancelledRequests:
        # Owner invalidation must precede any worker admitted after this frame,
        # even while the foreground is busy with an earlier request.
        cancelled_ids: list[RPCId] = []

        def cancel_previous_owner() -> None:
            cancelled_ids.extend(background.supersede_all(account_scoped_only=True))

        if auth_changes.observe_input(message, on_owner_changed=cancel_previous_owner):
            # The pump never writes output while applying an auth fence. Keep
            # these responses before any later request that reuses their IDs.
            return _RPCCancelledRequests(tuple(cancelled_ids))
        for dispatcher in dispatchers:
            dispatcher.observe_buffered_input(message)
        if _is_terminal_stop_rpc(message):
            # Apply the barrier at read time. The pump may have buffered
            # mutations before Stop while the foreground handles an earlier
            # request; none of them may execute after the terminal action.
            superseded = lifecycle.supersede_all()
            with terminal_cancellations_lock:
                terminal_cancellations.append(superseded)
        elif _is_fenced_stop_rpc(message):
            fence = lifecycle.begin_terminal_fence()
            with fenced_terminal_gates_lock:
                fenced_terminal_gates.append(fence)
        return False

    def observe_disconnect() -> None:
        auth_changes.close()
        # Release cancellable native work before retiring its owner connection.
        for dispatcher in dispatchers:
            dispatcher.fail_stop()
        if disconnect_observer is not None:
            disconnect_observer()

    input_pump = _BoundedRPCInputPump(
        input_stream,
        input_observer=observe_buffered_input,
        disconnect_observer=observe_disconnect,
    )
    writer.register_failure_callback(input_pump.wake_on_output_failure)

    def write_response(response: RPCResponse) -> bool:
        if writer.write(response):
            return True
        for dispatcher in dispatchers:
            dispatcher.fail_stop()
        return False

    try:
        while True:
            line = input_pump.next_line(writer)
            if isinstance(line, _RPCCancelledRequests):
                for cancelled_id in line.request_ids:
                    if not write_response(rpc_error(cancelled_id, -32800, "Request cancelled")):
                        return
                continue
            if line in {_RPCInputMarker.EOF, _RPCInputMarker.TERMINATED}:
                return
            if line is _RPCInputMarker.OBSERVED_CANCELLATION:
                continue
            if line is _RPCInputMarker.OVERSIZED:
                if not write_response(rpc_error(None, -32700, "Request exceeds maximum size")):
                    return
                continue
            if not isinstance(line, bytes):
                raise RuntimeError("unexpected RPC input marker")
            try:
                decoded: RPCMessage = json.loads(
                    line,
                    parse_constant=int,
                )
            except (ValueError, UnicodeDecodeError, RecursionError):
                if not write_response(rpc_error(None, -32700, "Parse error")):
                    return
                continue

            if writer.failed:
                return

            is_cancellation, cancelled_id = _cancelled_background_request_id(decoded)
            if is_cancellation and cancelled_id is not None:
                for dispatcher in dispatchers:
                    dispatcher.cancel(cancelled_id)
                continue

            if _uses_background_rpc_lane(decoded):
                dispatcher = background
            elif _uses_lifecycle_rpc_lane(decoded):
                dispatcher = lifecycle
            else:
                dispatcher = None
            if dispatcher is not None:
                submission = dispatcher.submit(decoded)
                if submission == "cancelled":
                    continue
                if submission != "accepted":
                    if writer.failed:
                        return
                    message_id = _request_id(decoded)
                    if not write_response(rpc_error(message_id, -32000, "Server busy")):
                        return
                continue

            if not writer.admit_request():
                return
            try:
                response = handler(decoded)
            except Exception:
                report_mcp_error("rpc", "exception")
                message_id = _request_id(decoded)
                response = rpc_error(message_id, -32603, "Internal error")
            fenced_gate: int | None = None
            fenced_superseded: list[RPCId] = []
            if _is_fenced_stop_rpc(decoded):
                with fenced_terminal_gates_lock:
                    fenced_gate = fenced_terminal_gates.popleft() if fenced_terminal_gates else None
                if fenced_gate is not None:
                    fenced_superseded = lifecycle.resolve_terminal_fence(
                        fenced_gate,
                        accepted=_accepted_terminal_stop_response(response),
                    )
            if response is not None and not write_response(response):
                return
            if _is_terminal_stop_rpc(decoded):
                with terminal_cancellations_lock:
                    superseded = terminal_cancellations.popleft() if terminal_cancellations else []
                # Return the terminal result first, then complete callers of
                # superseded mutations with a bounded cancellation error. A
                # stale Start can neither re-arm capture nor hang its widget.
                for superseded_id in superseded:
                    if not write_response(rpc_error(superseded_id, -32800, "Request cancelled")):
                        return
            elif fenced_gate is not None:
                for superseded_id in fenced_superseded:
                    if not write_response(rpc_error(superseded_id, -32800, "Request cancelled")):
                        return
                lifecycle.finish_terminal_fence(fenced_gate)
    finally:
        auth_changes.close()
        input_pump.stop()
        # Signal every lane before any grace wait. A blocked detail or hosted
        # bot request must not delay cancellation of an in-flight native
        # permission/Start request, and total shutdown stays on one deadline.
        for dispatcher in dispatchers:
            dispatcher.fail_stop()
        deadline = time.monotonic() + max(0.0, shutdown_grace_seconds)
        for dispatcher in dispatchers:
            dispatcher.shutdown(max(0.0, deadline - time.monotonic()))
        scheduler.shutdown(max(0.0, deadline - time.monotonic()))
        flush_client_operation_metrics()
