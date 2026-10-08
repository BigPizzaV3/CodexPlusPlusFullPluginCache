"""Portable, owner-bound JSON-RPC transport for native Meetings control.

Canonical: Microwave chatgpt-meetings-core/e2e/canonical_mcp_transport/live_client.py
Vendored: Microwave plugins/chatgpt-meetings-dev/scripts/live_client.py
Vendored: OpenAI chatgpt/oai-maintained-plugins/plugins/chatgpt-meetings/mcp/control_transport/live_client.py
Sync: python3 chatgpt-meetings-core/scripts/generate_recording_control_stream_contract.py --openai-root /path/to/openai
Check: python3 chatgpt-meetings-core/scripts/generate_recording_control_stream_contract.py --openai-root /path/to/openai --check

This canonical module intentionally depends only on the Python standard library.
Business contracts, generated schemas, owner provenance, and status caches are
validated through caller-supplied callbacks and never imported here.
"""

from __future__ import annotations

import copy
import ctypes
import errno
import io
import json
import os
import select
import socket
import stat
import struct
import sys
import threading
import time
from collections import OrderedDict, deque
from collections.abc import Callable
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import TYPE_CHECKING, Generic, Literal, Protocol, TypeVar

if TYPE_CHECKING:
    from typing import TypeGuard

_DEFAULT_MAXIMUM_FRAME_BYTES = 1_048_576
_DEFAULT_MAXIMUM_PENDING_REQUESTS = 16
_DEFAULT_MAXIMUM_CACHED_RESPONSES = 128
_CANCELLATION_CHECK_SECONDS = 0.1
_MAXIMUM_READ_CHUNK_BYTES = 64 * 1024
_WINDOWS_NAMED_PIPE_PREFIX = "\\\\.\\pipe\\"
_WINDOWS_PIPE_INPUT_POLL_SECONDS = 0.05
_WINDOWS_THREAD_TERMINATE = 0x0001
_WINDOWS_RETRYABLE_PIPE_OPEN_ERRNOS = frozenset(
    {errno.EBUSY, errno.EINVAL, errno.ENOENT, errno.EPIPE}
)
_WINDOWS_RETRYABLE_PIPE_OPEN_ERRORS = frozenset({2, 231, 232, 233})
_LOCAL_SOCKET_PROTOCOL = 0
_LOCAL_PEER_CREDENTIALS = 0x001
_LOCAL_PEER_PROCESS_ID = 0x002
_MAXIMUM_PEER_CREDENTIAL_BYTES = 128

_WindowsOperationResult = TypeVar("_WindowsOperationResult")


class LiveTransportFailureKind(Enum):
    """Recovery meaning supplied by the failing operation, independent of its message."""

    UNAVAILABLE = "unavailable"
    TIMED_OUT = "timed-out"
    CANCELLED = "cancelled"
    REJECTED = "rejected"


class LiveTransportFailureReason(Enum):
    """Concrete operation origin; consumers own any recovery decision."""

    ENDPOINT_REJECTED = "endpoint-rejected"
    ENDPOINT_MISSING = "endpoint-missing"


class LiveTransportError(RuntimeError):
    """One bounded local transport, peer identity, or JSON-RPC failure."""

    def __init__(
        self,
        kind: LiveTransportFailureKind,
        message: str,
        *,
        io_attempted: bool = False,
        diagnostic_reason: LiveTransportFailureReason | None = None,
    ) -> None:
        super().__init__(message)
        self.kind = kind
        self.diagnostic_reason = diagnostic_reason
        # Local validation/queue deadlines are not evidence of an unresponsive peer.
        # This describes the failed operation, not permission to replay or replace it.
        self.io_attempted = io_attempted


def _io_failure_kind(error: OSError | ValueError) -> LiveTransportFailureKind:
    winerror = getattr(error, "winerror", None)
    if isinstance(error, TimeoutError) or winerror == 121:  # ERROR_SEM_TIMEOUT
        return LiveTransportFailureKind.TIMED_OUT
    # Windows' exact pipe state takes precedence over its coarse CRT errno.
    if winerror in _WINDOWS_RETRYABLE_PIPE_OPEN_ERRORS or winerror == 109:
        return LiveTransportFailureKind.UNAVAILABLE
    if (
        isinstance(error, (PermissionError, NotADirectoryError)) or winerror == 5
    ):  # ERROR_ACCESS_DENIED
        return LiveTransportFailureKind.REJECTED
    return LiveTransportFailureKind.UNAVAILABLE


def _run_callback(callback: Callable[[], None], *, failure_message: str) -> None:
    try:
        callback()
    except LiveTransportError:
        raise
    except Exception as exc:
        raise LiveTransportError(LiveTransportFailureKind.REJECTED, failure_message) from exc


@dataclass(frozen=True, repr=False)
class LiveOwner:
    """The exact independently discovered native process and OS endpoint."""

    endpoint: str
    pid: int
    transport: Literal["unix-domain-socket", "windows-named-pipe"]


class _WindowsCrtApi(Protocol):
    def get_osfhandle(self, descriptor: int) -> int: ...


class _WindowsCtypesApi(Protocol):
    def WinDLL(self, name: str, *, use_last_error: bool) -> ctypes.CDLL: ...

    def get_last_error(self) -> int: ...


if TYPE_CHECKING:
    windows_crt: _WindowsCrtApi
    _windows_ctypes: _WindowsCtypesApi
elif os.name == "nt":
    import msvcrt as windows_crt

    _windows_ctypes = ctypes


def windows_kernel32() -> ctypes.CDLL:
    """Return the Windows process and named-pipe identity API."""

    return _windows_ctypes.WinDLL("kernel32", use_last_error=True)


def windows_advapi32() -> ctypes.CDLL:
    """Return the Windows process-token and SID comparison API."""

    return _windows_ctypes.WinDLL("advapi32", use_last_error=True)


class _WindowsSidAndAttributes(ctypes.Structure):
    _fields_ = [("sid", ctypes.c_void_p), ("attributes", ctypes.c_uint32)]


class _WindowsTokenUser(ctypes.Structure):
    _fields_ = [("user", _WindowsSidAndAttributes)]


def windows_process_has_same_user(kernel: ctypes.CDLL, owner_pid: int) -> bool:
    """Compare the reviewed native process and this process's TokenUser SIDs."""

    advapi = windows_advapi32()
    open_process = kernel.OpenProcess
    open_process.argtypes = [ctypes.c_uint32, ctypes.c_int, ctypes.c_uint32]
    open_process.restype = ctypes.c_void_p
    current_process = kernel.GetCurrentProcess
    current_process.argtypes = []
    current_process.restype = ctypes.c_void_p
    close_handle = kernel.CloseHandle
    close_handle.argtypes = [ctypes.c_void_p]
    close_handle.restype = ctypes.c_int
    open_token = advapi.OpenProcessToken
    open_token.argtypes = [
        ctypes.c_void_p,
        ctypes.c_uint32,
        ctypes.POINTER(ctypes.c_void_p),
    ]
    open_token.restype = ctypes.c_int
    token_information = advapi.GetTokenInformation
    token_information.argtypes = [
        ctypes.c_void_p,
        ctypes.c_int,
        ctypes.c_void_p,
        ctypes.c_uint32,
        ctypes.POINTER(ctypes.c_uint32),
    ]
    token_information.restype = ctypes.c_int
    equal_sid = advapi.EqualSid
    equal_sid.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    equal_sid.restype = ctypes.c_int

    process = open_process(0x1000, 0, owner_pid)
    if not process:
        return False
    owner_token = ctypes.c_void_p()
    client_token = ctypes.c_void_p()
    try:
        if not open_token(process, 0x0008, ctypes.byref(owner_token)) or not open_token(
            current_process(),
            0x0008,
            ctypes.byref(client_token),
        ):
            return False
        owner_size = ctypes.c_uint32()
        client_size = ctypes.c_uint32()
        token_information(owner_token, 1, None, 0, ctypes.byref(owner_size))
        token_information(client_token, 1, None, 0, ctypes.byref(client_size))
        if not owner_size.value or not client_size.value:
            return False
        owner_buffer = ctypes.create_string_buffer(owner_size.value)
        client_buffer = ctypes.create_string_buffer(client_size.value)
        if not token_information(
            owner_token,
            1,
            owner_buffer,
            owner_size.value,
            ctypes.byref(owner_size),
        ) or not token_information(
            client_token,
            1,
            client_buffer,
            client_size.value,
            ctypes.byref(client_size),
        ):
            return False
        owner_sid = _WindowsTokenUser.from_buffer(owner_buffer).user.sid
        client_sid = _WindowsTokenUser.from_buffer(client_buffer).user.sid
        return bool(
            owner_sid
            and client_sid
            and equal_sid(ctypes.c_void_p(owner_sid), ctypes.c_void_p(client_sid))
        )
    finally:
        if owner_token.value is not None:
            close_handle(owner_token)
        if client_token.value is not None:
            close_handle(client_token)
        close_handle(process)


@dataclass(repr=False)
class _WindowsOperation(Generic[_WindowsOperationResult]):
    started: threading.Event = field(default_factory=threading.Event)
    completed: threading.Event = field(default_factory=threading.Event)
    abandoned: threading.Event = field(default_factory=threading.Event)
    publication_lock: threading.Lock = field(default_factory=threading.Lock)
    result: _WindowsOperationResult | None = None
    failure: BaseException | None = None


def cancel_windows_thread(kernel: ctypes.CDLL, thread_id: int | None) -> None:
    if thread_id is None:
        return
    try:
        open_thread = kernel.OpenThread
        open_thread.argtypes = [ctypes.c_uint32, ctypes.c_int, ctypes.c_uint32]
        open_thread.restype = ctypes.c_void_p
        cancel = kernel.CancelSynchronousIo
        cancel.argtypes = [ctypes.c_void_p]
        cancel.restype = ctypes.c_int
        close_handle = kernel.CloseHandle
        close_handle.argtypes = [ctypes.c_void_p]
        close_handle.restype = ctypes.c_int
        handle = open_thread(_WINDOWS_THREAD_TERMINATE, 0, thread_id)
        if handle:
            try:
                cancel(handle)
            finally:
                close_handle(handle)
    except (AttributeError, OSError, ValueError):
        return


def _raise_if_cancelled(cancellation_event: threading.Event | None) -> None:
    if cancellation_event is not None and cancellation_event.is_set():
        raise LiveTransportError(
            LiveTransportFailureKind.CANCELLED,
            "native control stream request was cancelled",
        )


def _remaining_seconds(deadline: float, *, io_attempted: bool = False) -> float:
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        raise LiveTransportError(
            LiveTransportFailureKind.TIMED_OUT,
            "native control stream request timed out",
            io_attempted=io_attempted,
        )
    return remaining


def run_bounded_windows_operation(
    operation: Callable[[], _WindowsOperationResult],
    *,
    kernel: ctypes.CDLL,
    deadline: float,
    cancellation_event: threading.Event | None,
) -> _WindowsOperationResult:
    result: _WindowsOperation[_WindowsOperationResult] = _WindowsOperation()

    def perform() -> None:
        try:
            _raise_if_cancelled(cancellation_event)
            _remaining_seconds(deadline)
            result.started.set()
            value = operation()
            with result.publication_lock:
                abandoned = result.abandoned.is_set()
                if not abandoned:
                    result.result = value
            if abandoned and isinstance(value, io.IOBase):
                value.close()
        except BaseException as exc:
            result.failure = exc
        finally:
            result.completed.set()

    worker = threading.Thread(
        target=perform,
        daemon=True,
        name="meetings-windows-control-io",
    )
    worker.start()
    try:
        while True:
            _raise_if_cancelled(cancellation_event)
            remaining = _remaining_seconds(deadline, io_attempted=result.started.is_set())
            wait = (
                remaining
                if cancellation_event is None
                else min(remaining, _CANCELLATION_CHECK_SECONDS)
            )
            if result.completed.wait(wait):
                break
    except LiveTransportError:
        with result.publication_lock:
            result.abandoned.set()
            abandoned_value = result.result
            result.result = None
        if isinstance(abandoned_value, io.IOBase):
            abandoned_value.close()
        cancel_windows_thread(kernel, worker.native_id)
        raise
    if result.failure is not None:
        if isinstance(result.failure, LiveTransportError):
            raise result.failure
        kind = (
            _io_failure_kind(result.failure)
            if isinstance(result.failure, OSError)
            else LiveTransportFailureKind.REJECTED
        )
        raise LiveTransportError(
            kind,
            "native Windows control stream I/O failed",
            io_attempted=isinstance(result.failure, OSError)
            and result.failure.errno != errno.EBADF,
        ) from result.failure
    if result.result is None:
        raise LiveTransportError(
            LiveTransportFailureKind.REJECTED,
            "native Windows control stream I/O failed",
        )
    return result.result


def _retryable_windows_pipe_open_error(exc: OSError) -> bool:
    """Recognize the CRT translations for an advisory named-pipe wait race."""

    winerror = getattr(exc, "winerror", None)
    return (
        winerror in _WINDOWS_RETRYABLE_PIPE_OPEN_ERRORS
        or winerror is None
        and exc.errno in _WINDOWS_RETRYABLE_PIPE_OPEN_ERRNOS
    )


def _open_bounded_windows_named_pipe(
    endpoint: str,
    *,
    kernel: ctypes.CDLL,
    deadline: float,
    cancellation_event: threading.Event | None,
) -> io.FileIO:
    """Open after an advisory wait, retrying only another client's claim race."""

    wait_for_pipe = kernel.WaitNamedPipeW
    wait_for_pipe.argtypes = [ctypes.c_wchar_p, ctypes.c_uint32]
    wait_for_pipe.restype = ctypes.c_int

    def wait_until_available(wait_millis: int) -> bool:
        if wait_for_pipe(endpoint, wait_millis):
            return True
        # Last-error is thread-local: inspect it inside the same bounded worker.
        error_code = _windows_ctypes.get_last_error()
        if error_code == 121:  # ERROR_SEM_TIMEOUT
            kind = LiveTransportFailureKind.TIMED_OUT
        elif error_code in _WINDOWS_RETRYABLE_PIPE_OPEN_ERRORS or error_code == 109:
            kind = LiveTransportFailureKind.UNAVAILABLE
        else:
            kind = LiveTransportFailureKind.REJECTED
        raise LiveTransportError(
            kind,
            "native Windows control stream is unavailable",
            io_attempted=True,
            diagnostic_reason=(
                LiveTransportFailureReason.ENDPOINT_REJECTED if error_code == 5 else None
            ),
        )

    while True:
        wait_millis = max(1, int(_remaining_seconds(deadline) * 1000))
        run_bounded_windows_operation(
            lambda wait_millis=wait_millis: wait_until_available(wait_millis),
            kernel=kernel,
            deadline=deadline,
            cancellation_event=cancellation_event,
        )
        try:
            return run_bounded_windows_operation(
                lambda: io.FileIO(endpoint, mode="r+"),
                kernel=kernel,
                deadline=deadline,
                cancellation_event=cancellation_event,
            )
        except LiveTransportError as exc:
            failure = exc.__cause__
            if exc.kind is LiveTransportFailureKind.REJECTED and isinstance(failure, OSError):
                exc.diagnostic_reason = LiveTransportFailureReason.ENDPOINT_REJECTED
            if (
                exc.kind is not LiveTransportFailureKind.UNAVAILABLE
                or not isinstance(failure, OSError)
                or not _retryable_windows_pipe_open_error(failure)
            ):
                raise
            # WaitNamedPipeW is advisory: another concurrent client may consume
            # the available server instance before the CRT open. Windows ARM64
            # has surfaced that race as EINVAL; repeat the wait under the same
            # caller deadline instead of rejecting a healthy multi-client owner.
            _raise_if_cancelled(cancellation_event)
            _remaining_seconds(deadline, io_attempted=True)


class _Connection(Protocol):
    def recv(self, size: int, /) -> bytes: ...

    def sendall(self, data: bytes, /) -> None: ...

    def close(self) -> None: ...


@dataclass(repr=False)
class _WindowsQueuedWrite:
    data: bytes
    deadline: float | None
    cancellation_event: threading.Event | None
    before_send: Callable[[], None] | None
    completed: threading.Event = field(default_factory=threading.Event)
    state: Literal["queued", "writing", "finished", "abandoned"] = "queued"
    failure: BaseException | None = None
    preflight_failed: bool = False
    io_attempted: bool = False


class WindowsNamedPipeConnection:
    """Bound a local Windows pipe to server PID, user SID, and logon session."""

    _pipe: io.FileIO
    _kernel: ctypes.CDLL
    _read_deadline: float | None
    _cancellation_event: threading.Event | None
    _reader_thread_id: int | None
    _post_initialization: bool
    _io_condition: threading.Condition
    _queued_writes: deque[_WindowsQueuedWrite]
    _active_write: _WindowsQueuedWrite | None
    _closed: bool

    def __init__(
        self,
        endpoint: str,
        *,
        owner_pid: int,
        deadline: float | None = None,
        cancellation_event: threading.Event | None = None,
    ) -> None:
        if os.name != "nt":
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED,
                "native Windows control stream is unavailable",
            )
        name = endpoint[len(_WINDOWS_NAMED_PIPE_PREFIX) :]
        if (
            not endpoint.startswith(_WINDOWS_NAMED_PIPE_PREFIX)
            or not 0 < len(name) <= 256
            or "\\" in name
            or "/" in name
            or "\x00" in name
        ):
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED,
                "native Windows control stream endpoint is malformed",
            )
        self._kernel = windows_kernel32()
        self._read_deadline = deadline
        self._cancellation_event = cancellation_event
        self._reader_thread_id = None
        self._post_initialization = False
        self._io_condition = threading.Condition()
        self._queued_writes = deque()
        self._active_write = None
        self._closed = False
        try:
            if deadline is None:
                self._pipe = io.FileIO(endpoint, mode="r+")
            else:
                self._pipe = _open_bounded_windows_named_pipe(
                    endpoint,
                    kernel=self._kernel,
                    deadline=deadline,
                    cancellation_event=cancellation_event,
                )
        except LiveTransportError:
            raise
        except (AttributeError, OSError, ValueError) as exc:
            kind = (
                _io_failure_kind(exc)
                if isinstance(exc, OSError)
                else LiveTransportFailureKind.REJECTED
            )
            raise LiveTransportError(
                kind,
                "native Windows control stream is unavailable",
                io_attempted=isinstance(exc, OSError) and exc.errno != errno.EBADF,
                diagnostic_reason=(
                    LiveTransportFailureReason.ENDPOINT_REJECTED
                    if kind is LiveTransportFailureKind.REJECTED and isinstance(exc, OSError)
                    else None
                ),
            ) from exc
        try:
            self.require_owner(owner_pid)
        except Exception:
            self._pipe.close()
            raise

    def require_owner(self, owner_pid: int) -> None:
        try:
            self._require_owner(owner_pid)
        except (AttributeError, OSError, ValueError) as exc:
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED,
                "native Windows control stream peer owner does not match",
            ) from exc

    def _require_owner(self, owner_pid: int) -> None:
        kernel = self._kernel
        query_peer = kernel.GetNamedPipeServerProcessId
        query_peer.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32)]
        query_peer.restype = ctypes.c_int
        process_session = kernel.ProcessIdToSessionId
        process_session.argtypes = [ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32)]
        process_session.restype = ctypes.c_int
        peer_pid = ctypes.c_uint32()
        peer_session = ctypes.c_uint32()
        client_session = ctypes.c_uint32()
        handle = ctypes.c_void_p(windows_crt.get_osfhandle(self._pipe.fileno()))
        if (
            not query_peer(handle, ctypes.byref(peer_pid))
            or peer_pid.value != owner_pid
            or not process_session(peer_pid.value, ctypes.byref(peer_session))
            or not process_session(os.getpid(), ctypes.byref(client_session))
            or peer_session.value != client_session.value
            or not windows_process_has_same_user(kernel, owner_pid)
        ):
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED,
                "native Windows control stream peer owner does not match",
            )

    def clear_initialization_deadline(self) -> None:
        with self._io_condition:
            self._read_deadline = None
            self._cancellation_event = None
            # One synchronous Windows pipe handle cannot make progress when a
            # blocking reader and writer use it from separate threads. After
            # the sequential initialization exchange, recv's thread owns all
            # kernel I/O and request threads submit bounded writes to it.
            self._post_initialization = True
            self._io_condition.notify_all()

    def recv(self, size: int) -> bytes:
        deadline = self._read_deadline
        if self._post_initialization:
            return self._recv_post_initialization(size)
        if deadline is None:
            self._reader_thread_id = threading.get_native_id()
            received = self._pipe.read(size)
        else:
            received = run_bounded_windows_operation(
                lambda: self._pipe.read(size),
                kernel=self._kernel,
                deadline=deadline,
                cancellation_event=self._cancellation_event,
            )
        return b"" if received is None else received

    def sendall(self, data: bytes) -> None:
        if self._post_initialization:
            self._enqueue_write(
                data,
                deadline=None,
                cancellation_event=None,
                before_send=None,
            )
            return
        self._write_direct(data)

    def _write_direct(self, data: bytes) -> None:
        view = memoryview(data)
        while view:
            written = self._pipe.write(view)
            if written is None or written <= 0:
                raise OSError("native Windows control stream write failed")
            view = view[written:]

    def sendall_before(
        self,
        data: bytes,
        *,
        deadline: float,
        cancellation_event: threading.Event | None,
        before_send: Callable[[], None] | None = None,
    ) -> None:
        if self._post_initialization:
            self._enqueue_write(
                data,
                deadline=deadline,
                cancellation_event=cancellation_event,
                before_send=before_send,
            )
            return
        if before_send is not None:
            _run_callback(before_send, failure_message="native control stream preflight failed")
        view = memoryview(data)
        while view:
            written = run_bounded_windows_operation(
                lambda remaining=view: self._pipe.write(remaining),
                kernel=self._kernel,
                deadline=deadline,
                cancellation_event=cancellation_event,
            )
            if written <= 0:
                raise LiveTransportError(
                    LiveTransportFailureKind.UNAVAILABLE,
                    "native Windows control stream write failed",
                    io_attempted=True,
                )
            view = view[written:]

    def _enqueue_write(
        self,
        data: bytes,
        *,
        deadline: float | None,
        cancellation_event: threading.Event | None,
        before_send: Callable[[], None] | None,
    ) -> None:
        request = _WindowsQueuedWrite(
            bytes(data),
            deadline,
            cancellation_event,
            before_send,
        )
        with self._io_condition:
            if self._closed:
                raise LiveTransportError(
                    LiveTransportFailureKind.UNAVAILABLE,
                    "native Windows control stream is disconnected",
                )
            # LiveJsonRpcClient._write_lock admits one frame at a time. Keep
            # that bound explicit if this internal connection is called
            # directly so a stalled peer cannot accumulate an unbounded queue.
            if self._queued_writes or self._active_write is not None:
                raise LiveTransportError(
                    LiveTransportFailureKind.REJECTED,
                    "native Windows control stream write is unavailable",
                )
            self._queued_writes.append(request)
            self._io_condition.notify_all()
        try:
            while not request.completed.is_set():
                _raise_if_cancelled(cancellation_event)
                if deadline is None:
                    wait = None if cancellation_event is None else _CANCELLATION_CHECK_SECONDS
                else:
                    remaining = _remaining_seconds(deadline, io_attempted=request.io_attempted)
                    wait = (
                        remaining
                        if cancellation_event is None
                        else min(remaining, _CANCELLATION_CHECK_SECONDS)
                    )
                request.completed.wait(wait)
        except LiveTransportError as exc:
            with self._io_condition:
                if request.state == "finished" and request.failure is None:
                    return
                started = request.state == "writing"
                if request.state in {"queued", "writing"}:
                    request.state = "abandoned"
                    request.failure = exc
                    request.completed.set()
                self._io_condition.notify_all()
            if started:
                cancel_windows_thread(self._kernel, self._reader_thread_id)
            raise
        with self._io_condition:
            failure = request.failure
            state = request.state
        if failure is not None:
            if request.preflight_failed or isinstance(failure, LiveTransportError):
                raise failure
            kind = (
                _io_failure_kind(failure)
                if isinstance(failure, OSError)
                else LiveTransportFailureKind.REJECTED
            )
            raise LiveTransportError(
                kind,
                "native Windows control stream write failed",
                io_attempted=request.io_attempted,
            ) from failure
        if state != "finished":
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED,
                "native Windows control stream write failed",
            )

    def _take_queued_write(self) -> _WindowsQueuedWrite | None:
        with self._io_condition:
            if self._closed:
                raise LiveTransportError(
                    LiveTransportFailureKind.UNAVAILABLE,
                    "native Windows control stream is closed",
                )
            while self._queued_writes:
                request = self._queued_writes.popleft()
                if request.state != "queued":
                    request.completed.set()
                    continue
                try:
                    _raise_if_cancelled(request.cancellation_event)
                    if request.deadline is not None:
                        _remaining_seconds(request.deadline)
                except LiveTransportError as exc:
                    request.state = "abandoned"
                    request.failure = exc
                    request.completed.set()
                    continue
                request.state = "writing"
                self._active_write = request
                return request
            return None

    def _perform_queued_write(self, request: _WindowsQueuedWrite) -> None:
        failure: BaseException | None = None
        preflight_failed = False
        try:
            view = memoryview(request.data)
            with self._io_condition:
                if request.state != "writing":
                    return
            _raise_if_cancelled(request.cancellation_event)
            if request.deadline is not None:
                _remaining_seconds(request.deadline)
            if request.before_send is not None:
                try:
                    _run_callback(
                        request.before_send,
                        failure_message="native control stream preflight failed",
                    )
                except BaseException:
                    preflight_failed = True
                    raise
                with self._io_condition:
                    if request.state != "writing":
                        return
                _raise_if_cancelled(request.cancellation_event)
                if request.deadline is not None:
                    _remaining_seconds(request.deadline)
            while view:
                with self._io_condition:
                    if request.state != "writing":
                        return
                _raise_if_cancelled(request.cancellation_event)
                if request.deadline is not None:
                    _remaining_seconds(request.deadline, io_attempted=request.io_attempted)
                request.io_attempted = True
                written = self._pipe.write(view)
                if written is None or written <= 0:
                    raise OSError("native Windows control stream write failed")
                view = view[written:]
        except BaseException as exc:
            failure = exc
        finally:
            with self._io_condition:
                if request.state == "writing":
                    request.state = "finished"
                    request.failure = failure
                    request.preflight_failed = preflight_failed
                if self._active_write is request:
                    self._active_write = None
                request.completed.set()
                self._io_condition.notify_all()

    def _peek_available_bytes(self) -> int:
        peek = self._kernel.PeekNamedPipe
        peek.argtypes = [
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_uint32,
            ctypes.POINTER(ctypes.c_uint32),
            ctypes.POINTER(ctypes.c_uint32),
            ctypes.POINTER(ctypes.c_uint32),
        ]
        peek.restype = ctypes.c_int
        available = ctypes.c_uint32()
        handle = ctypes.c_void_p(windows_crt.get_osfhandle(self._pipe.fileno()))
        if not peek(handle, None, 0, None, ctypes.byref(available), None):
            raise OSError(
                _windows_ctypes.get_last_error(),
                "native Windows control stream peek failed",
            )
        return available.value

    def _recv_post_initialization(self, size: int) -> bytes:
        self._reader_thread_id = threading.get_native_id()
        while True:
            request = self._take_queued_write()
            if request is not None:
                self._perform_queued_write(request)
                continue
            # PeekNamedPipe is nonblocking. Reading only bytes the kernel has
            # already reported prevents an idle read from owning the
            # synchronous file object while a request is waiting to write.
            available = self._peek_available_bytes()
            if available > 0:
                received = self._pipe.read(min(size, available))
                return b"" if received is None else received
            with self._io_condition:
                if self._closed:
                    raise LiveTransportError(
                        LiveTransportFailureKind.UNAVAILABLE,
                        "native Windows control stream is closed",
                    )
                if not self._queued_writes:
                    self._io_condition.wait(_WINDOWS_PIPE_INPUT_POLL_SECONDS)

    def close(self) -> None:
        failure = LiveTransportError(
            LiveTransportFailureKind.UNAVAILABLE,
            "native Windows control stream disconnected",
        )
        with self._io_condition:
            if self._closed:
                return
            self._closed = True
            pending = tuple(self._queued_writes)
            self._queued_writes.clear()
            active = self._active_write
            for request in (*pending, active):
                if request is not None and request.state in {"queued", "writing"}:
                    request.state = "abandoned"
                    request.failure = failure
                    request.completed.set()
            self._io_condition.notify_all()
        cancel_windows_thread(self._kernel, self._reader_thread_id)
        try:
            cancel = self._kernel.CancelIoEx
            cancel.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
            cancel.restype = ctypes.c_int
            handle = ctypes.c_void_p(windows_crt.get_osfhandle(self._pipe.fileno()))
            cancel(handle, None)
        except (AttributeError, OSError, ValueError):
            pass
        self._pipe.close()


def _unix_endpoint_failure_reason(error: OSError) -> LiveTransportFailureReason | None:
    if isinstance(error, (PermissionError, NotADirectoryError)):
        return LiveTransportFailureReason.ENDPOINT_REJECTED
    if isinstance(error, FileNotFoundError):
        return LiveTransportFailureReason.ENDPOINT_MISSING
    return None


def _socket_metadata(path: Path) -> os.stat_result:
    try:
        return path.lstat()
    except OSError as exc:
        raise LiveTransportError(
            _io_failure_kind(exc),
            "native control stream endpoint is unavailable",
            diagnostic_reason=_unix_endpoint_failure_reason(exc),
        ) from exc


def _require_private_socket(endpoint: Path) -> os.stat_result:
    parent_metadata = _socket_metadata(endpoint.parent)
    if (
        not stat.S_ISDIR(parent_metadata.st_mode)
        or stat.S_IMODE(parent_metadata.st_mode) != 0o700
        or parent_metadata.st_uid != os.geteuid()
    ):
        raise LiveTransportError(
            LiveTransportFailureKind.REJECTED,
            "native control stream endpoint is unsafe",
            diagnostic_reason=LiveTransportFailureReason.ENDPOINT_REJECTED,
        )
    metadata = _socket_metadata(endpoint)
    if (
        not stat.S_ISSOCK(metadata.st_mode)
        or stat.S_IMODE(metadata.st_mode) != 0o600
        or metadata.st_uid != os.geteuid()
    ):
        raise LiveTransportError(
            LiveTransportFailureKind.REJECTED,
            "native control stream endpoint is unsafe",
            diagnostic_reason=LiveTransportFailureReason.ENDPOINT_REJECTED,
        )
    try:
        if endpoint.resolve(strict=True) != endpoint.absolute():
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED,
                "native control stream endpoint is unsafe",
                diagnostic_reason=LiveTransportFailureReason.ENDPOINT_REJECTED,
            )
    except OSError as exc:
        raise LiveTransportError(
            _io_failure_kind(exc),
            "native control stream endpoint is unavailable",
            diagnostic_reason=_unix_endpoint_failure_reason(exc),
        ) from exc
    return metadata


def require_unix_peer(connection: socket.socket, *, owner_pid: int) -> None:
    if sys.platform != "darwin":
        return
    try:
        peer_pid = struct.unpack(
            "=i",
            connection.getsockopt(_LOCAL_SOCKET_PROTOCOL, _LOCAL_PEER_PROCESS_ID, 4),
        )[0]
        credentials = connection.getsockopt(
            _LOCAL_SOCKET_PROTOCOL,
            _LOCAL_PEER_CREDENTIALS,
            _MAXIMUM_PEER_CREDENTIAL_BYTES,
        )
        if len(credentials) < 8:
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED,
                "native control stream peer credentials are unavailable",
            )
        peer_uid = struct.unpack_from("=I", credentials, 4)[0]
    except (OSError, struct.error) as exc:
        raise LiveTransportError(
            LiveTransportFailureKind.REJECTED,
            "native control stream peer credentials are unavailable",
        ) from exc
    if peer_pid != owner_pid or peer_uid != os.geteuid():
        raise LiveTransportError(
            LiveTransportFailureKind.REJECTED,
            "native control stream peer owner does not match",
        )


def _connect_unix_socket(endpoint: str, *, owner_pid: int, deadline: float) -> socket.socket:
    path = Path(endpoint)
    if not path.is_absolute():
        raise LiveTransportError(
            LiveTransportFailureKind.REJECTED,
            "native control stream endpoint is malformed",
        )
    before = _require_private_socket(path)
    connection = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    io_attempted = False
    try:
        connection.settimeout(_remaining_seconds(deadline))
        io_attempted = True
        connection.connect(str(path))
        io_attempted = False
        require_unix_peer(connection, owner_pid=owner_pid)
        after = _require_private_socket(path)
        if (before.st_dev, before.st_ino) != (after.st_dev, after.st_ino):
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED,
                "native control stream endpoint changed",
            )
    except (LiveTransportError, OSError) as exc:
        connection.close()
        if isinstance(exc, LiveTransportError):
            raise
        raise LiveTransportError(
            _io_failure_kind(exc),
            "native control stream is unavailable",
            io_attempted=io_attempted,
            diagnostic_reason=_unix_endpoint_failure_reason(exc),
        ) from exc
    return connection


def _require_connection_owner(connection: _Connection, *, owner_pid: int) -> None:
    if isinstance(connection, socket.socket):
        require_unix_peer(connection, owner_pid=owner_pid)
    elif isinstance(connection, WindowsNamedPipeConnection):
        connection.require_owner(owner_pid)


def _close_connection(connection: _Connection) -> None:
    if isinstance(connection, socket.socket):
        try:
            connection.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
    try:
        connection.close()
    except (OSError, ValueError):
        pass


def _unique_json_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON object key")
        result[key] = value
    return result


def _is_json_object(value: object) -> TypeGuard[dict[str, object]]:
    """Narrow objects produced by the typed, duplicate-free JSON decoder."""

    return isinstance(value, dict)


def _recv_unix_socket_before(
    connection: socket.socket,
    count: int,
    *,
    deadline: float,
    cancellation_event: threading.Event | None,
) -> bytes:
    io_attempted = False
    while True:
        _raise_if_cancelled(cancellation_event)
        remaining = _remaining_seconds(deadline, io_attempted=io_attempted)
        wait = (
            remaining if cancellation_event is None else min(remaining, _CANCELLATION_CHECK_SECONDS)
        )
        try:
            io_attempted = True
            readable, _, _ = select.select([connection], [], [], wait)
        except InterruptedError:
            continue
        if not readable:
            continue
        _raise_if_cancelled(cancellation_event)
        _remaining_seconds(deadline, io_attempted=True)
        try:
            return connection.recv(count, socket.MSG_DONTWAIT)
        except (BlockingIOError, InterruptedError):
            continue


def _read_exact(
    connection: _Connection,
    count: int,
    *,
    deadline: float | None = None,
    cancellation_event: threading.Event | None = None,
) -> bytes:
    result = bytearray()
    while len(result) < count:
        _raise_if_cancelled(cancellation_event)
        if deadline is not None:
            _remaining_seconds(deadline)
        try:
            chunk_size = min(count - len(result), _MAXIMUM_READ_CHUNK_BYTES)
            if isinstance(connection, socket.socket) and deadline is not None:
                chunk = _recv_unix_socket_before(
                    connection,
                    chunk_size,
                    deadline=deadline,
                    cancellation_event=cancellation_event,
                )
            else:
                chunk = connection.recv(chunk_size)
        except (OSError, ValueError) as exc:
            raise LiveTransportError(
                _io_failure_kind(exc),
                "native control stream disconnected",
                io_attempted=isinstance(exc, OSError) and exc.errno != errno.EBADF,
            ) from exc
        if not chunk:
            raise LiveTransportError(
                LiveTransportFailureKind.UNAVAILABLE,
                "native control stream disconnected",
                io_attempted=True,
            )
        result.extend(chunk)
    return bytes(result)


def read_message(
    connection: _Connection,
    *,
    maximum_frame_bytes: int,
    deadline: float | None = None,
    cancellation_event: threading.Event | None = None,
) -> dict[str, object]:
    frame_length = int.from_bytes(
        _read_exact(connection, 4, deadline=deadline, cancellation_event=cancellation_event),
        byteorder="little",
    )
    if not 0 < frame_length <= maximum_frame_bytes:
        raise LiveTransportError(
            LiveTransportFailureKind.REJECTED,
            "native control stream frame exceeds its limit",
        )
    try:
        value: object = json.loads(
            _read_exact(
                connection,
                frame_length,
                deadline=deadline,
                cancellation_event=cancellation_event,
            ).decode("utf-8"),
            object_pairs_hook=_unique_json_object,
            parse_constant=int,
        )
    except (UnicodeError, ValueError, json.JSONDecodeError) as exc:
        raise LiveTransportError(
            LiveTransportFailureKind.REJECTED,
            "native control stream message is malformed",
        ) from exc
    if not _is_json_object(value):
        raise LiveTransportError(
            LiveTransportFailureKind.REJECTED,
            "native control stream message is malformed",
        )
    return dict(value)


def canonical_json(value: object) -> str:
    try:
        return json.dumps(
            value,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
            allow_nan=False,
        )
    except (OverflowError, RecursionError, TypeError, UnicodeError, ValueError) as exc:
        raise LiveTransportError(
            LiveTransportFailureKind.REJECTED,
            "native control stream message is malformed",
        ) from exc


def _send_unix_socket_before(
    connection: socket.socket,
    data: bytes,
    *,
    deadline: float,
    cancellation_event: threading.Event | None,
    before_send: Callable[[], None] | None,
) -> None:
    view = memoryview(data)
    wrote_any = False
    io_attempted = False
    while view:
        _raise_if_cancelled(cancellation_event)
        remaining = _remaining_seconds(deadline, io_attempted=io_attempted)
        wait = (
            remaining if cancellation_event is None else min(remaining, _CANCELLATION_CHECK_SECONDS)
        )
        try:
            io_attempted = True
            _, writable, _ = select.select([], [connection], [], wait)
        except InterruptedError:
            continue
        if not writable:
            continue
        _raise_if_cancelled(cancellation_event)
        _remaining_seconds(deadline, io_attempted=True)
        if not wrote_any and before_send is not None:
            _run_callback(before_send, failure_message="native control stream preflight failed")
            _raise_if_cancelled(cancellation_event)
            _remaining_seconds(deadline)
        try:
            written = connection.send(view, socket.MSG_DONTWAIT)
        except (BlockingIOError, InterruptedError):
            continue
        if written <= 0:
            raise OSError("native Unix control stream write failed")
        wrote_any = True
        view = view[written:]


def write_message(
    connection: _Connection,
    message: dict[str, object],
    *,
    maximum_frame_bytes: int,
    deadline: float | None = None,
    cancellation_event: threading.Event | None = None,
    before_send: Callable[[], None] | None = None,
) -> None:
    encoded = canonical_json(message).encode("utf-8")
    if not 0 < len(encoded) <= maximum_frame_bytes:
        raise LiveTransportError(
            LiveTransportFailureKind.REJECTED,
            "native control stream frame exceeds its limit",
        )
    try:
        payload = len(encoded).to_bytes(4, byteorder="little") + encoded
        if isinstance(connection, socket.socket) and deadline is not None:
            _send_unix_socket_before(
                connection,
                payload,
                deadline=deadline,
                cancellation_event=cancellation_event,
                before_send=before_send,
            )
        elif isinstance(connection, WindowsNamedPipeConnection) and deadline is not None:
            connection.sendall_before(
                payload,
                deadline=deadline,
                cancellation_event=cancellation_event,
                before_send=before_send,
            )
        else:
            if before_send is not None:
                _run_callback(
                    before_send,
                    failure_message="native control stream preflight failed",
                )
            connection.sendall(payload)
    except (OSError, ValueError) as exc:
        raise LiveTransportError(
            _io_failure_kind(exc),
            "native control stream disconnected",
            io_attempted=isinstance(exc, OSError) and exc.errno != errno.EBADF,
        ) from exc


@dataclass(repr=False)
class _PendingResponse:
    request_id: str
    fingerprint: str
    ready: threading.Event = field(default_factory=threading.Event)
    response: dict[str, object] | None = None
    failure: RuntimeError | None = None


@dataclass(frozen=True, repr=False)
class _CompletedResponse:
    fingerprint: str
    response: dict[str, object]


class LiveJsonRpcClient:
    """A persistent local peer, initialization exchange, and JSON-RPC router."""

    def __init__(
        self,
        owner: LiveOwner,
        *,
        maximum_frame_bytes: int = _DEFAULT_MAXIMUM_FRAME_BYTES,
        verify_owner: Callable[[], None] | None = None,
        on_notification: Callable[[dict[str, object]], None] | None = None,
        validate_response: Callable[[dict[str, object]], None] | None = None,
        on_disconnect: Callable[[], None] | None = None,
    ) -> None:
        if (
            type(owner.pid) is not int
            or not 0 < owner.pid <= 2_147_483_647
            or type(maximum_frame_bytes) is not int
            or not 0 < maximum_frame_bytes <= _DEFAULT_MAXIMUM_FRAME_BYTES
        ):
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED,
                "native control stream owner is malformed",
            )
        self._owner = owner
        self._maximum_frame_bytes = maximum_frame_bytes
        self._verify_owner = verify_owner
        self._on_notification = on_notification
        self._validate_response = validate_response
        self._on_disconnect = on_disconnect
        self._connect_lock = threading.RLock()
        self._lock = threading.RLock()
        self._write_lock = threading.Lock()
        self._connection: _Connection | None = None
        self._connection_on_disconnect: Callable[[], None] | None = None
        self._reader: threading.Thread | None = None
        self._reader_processing: tuple[_Connection, bool] | None = None
        self._pending: dict[str, _PendingResponse] = {}
        self._completed: OrderedDict[str, _CompletedResponse] = OrderedDict()
        self._ambiguous: OrderedDict[str, None] = OrderedDict()
        self._abandoned: OrderedDict[str, None] = OrderedDict()

    @property
    def connected(self) -> bool:
        return self._connection is not None

    def connect(
        self,
        initialization: dict[str, object],
        *,
        validate_result: Callable[[dict[str, object]], None] | None = None,
        deadline: float,
        cancellation_event: threading.Event | None = None,
        on_initialized: Callable[[dict[str, object]], None] | None = None,
        on_notification: Callable[[dict[str, object]], None] | None = None,
        on_disconnect: Callable[[], None] | None = None,
    ) -> dict[str, object]:
        """Initialize one connection with optional connection-bound callbacks.

        A callback may finish after close or a later initialization. Consumers
        that cache state should capture their connection generation in these
        callbacks and reject publication from a retired generation.
        """

        _raise_if_cancelled(cancellation_event)
        _remaining_seconds(deadline)
        with self._connect_lock:
            if self._connection is not None:
                raise LiveTransportError(
                    LiveTransportFailureKind.REJECTED,
                    "native control stream is already initialized",
                )
            owner = self._owner
            if owner.transport == "unix-domain-socket":
                connection: _Connection = _connect_unix_socket(
                    owner.endpoint,
                    owner_pid=owner.pid,
                    deadline=deadline,
                )
            elif owner.transport == "windows-named-pipe":
                connection = WindowsNamedPipeConnection(
                    owner.endpoint,
                    owner_pid=owner.pid,
                    deadline=deadline,
                    cancellation_event=cancellation_event,
                )
            else:
                raise LiveTransportError(
                    LiveTransportFailureKind.REJECTED,
                    "native control stream transport is unsupported",
                )

            try:
                self._check_owner(connection)
                request_id = initialization.get("id")
                if (
                    initialization.get("jsonrpc") != "2.0"
                    or not isinstance(request_id, str)
                    or not isinstance(initialization.get("method"), str)
                    or not isinstance(initialization.get("params"), dict)
                ):
                    raise LiveTransportError(
                        LiveTransportFailureKind.REJECTED,
                        "native control stream initialization is malformed",
                    )
                write_message(
                    connection,
                    initialization,
                    maximum_frame_bytes=self._maximum_frame_bytes,
                    deadline=deadline,
                    cancellation_event=cancellation_event,
                )
                response = read_message(
                    connection,
                    maximum_frame_bytes=self._maximum_frame_bytes,
                    deadline=deadline,
                    cancellation_event=cancellation_event,
                )
                result_value = response.get("result")
                if (
                    response.get("jsonrpc") != "2.0"
                    or response.get("id") != request_id
                    or "error" in response
                    or not _is_json_object(result_value)
                ):
                    raise LiveTransportError(
                        LiveTransportFailureKind.REJECTED,
                        "native control stream initialization failed",
                    )
                result = dict(result_value)
                if validate_result is not None:
                    validate_result(result)
                _raise_if_cancelled(cancellation_event)
                _remaining_seconds(deadline)
                self._check_owner(connection)
                if on_initialized is not None:
                    on_initialized(result)
                if isinstance(connection, socket.socket):
                    connection.settimeout(None)
                else:
                    connection.clear_initialization_deadline()
                reader = threading.Thread(
                    target=self._receive_loop,
                    args=(connection, on_notification or self._on_notification),
                    daemon=True,
                    name="meetings-native-control-stream",
                )
                with self._lock:
                    self._connection = connection
                    self._connection_on_disconnect = on_disconnect or self._on_disconnect
                    self._reader = reader
                reader.start()
                return result
            except Exception as exc:
                _close_connection(connection)
                if isinstance(exc, LiveTransportError):
                    raise
                raise LiveTransportError(
                    LiveTransportFailureKind.REJECTED,
                    "native control stream initialization failed",
                ) from exc

    def request(
        self,
        message: dict[str, object],
        *,
        deadline: float,
        cancellation_event: threading.Event | None = None,
        before_send: Callable[[], None] | None = None,
        on_sent: Callable[[], None] | None = None,
    ) -> dict[str, object]:
        _raise_if_cancelled(cancellation_event)
        _remaining_seconds(deadline)
        request_id = message.get("id")
        if (
            message.get("jsonrpc") != "2.0"
            or not isinstance(request_id, str)
            or not isinstance(message.get("method"), str)
            or not isinstance(message.get("params"), dict)
        ):
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED,
                "native control stream request is malformed",
            )
        fingerprint = canonical_json(message)
        pending = _PendingResponse(request_id, fingerprint)
        with self._lock:
            connection = self._connection
            if connection is None:
                raise LiveTransportError(
                    LiveTransportFailureKind.UNAVAILABLE,
                    "native control stream is disconnected",
                )
            completed = self._completed.get(request_id)
            if completed is not None:
                if completed.fingerprint != fingerprint:
                    raise LiveTransportError(
                        LiveTransportFailureKind.REJECTED,
                        "native control stream request identity was reused",
                    )
                self._check_owner(connection)
                if self._connection is not connection:
                    raise LiveTransportError(
                        LiveTransportFailureKind.REJECTED,
                        "native control stream owner changed",
                    )
                return copy.deepcopy(completed.response)
            if request_id in self._ambiguous:
                raise LiveTransportError(
                    LiveTransportFailureKind.REJECTED,
                    "native control stream request outcome is ambiguous",
                )
            if (
                request_id in self._pending
                or len(self._pending) >= _DEFAULT_MAXIMUM_PENDING_REQUESTS
            ):
                raise LiveTransportError(
                    LiveTransportFailureKind.REJECTED,
                    "native control stream request identity is unavailable",
                )
            self._pending[request_id] = pending

        sent = False
        writing = False
        try:
            with self._write_lock:
                _raise_if_cancelled(cancellation_event)
                _remaining_seconds(deadline)
                with self._lock:
                    if self._connection is not connection:
                        raise LiveTransportError(
                            LiveTransportFailureKind.REJECTED,
                            "native control stream owner changed",
                        )
                self._check_owner(connection)
                writing = True
                write_message(
                    connection,
                    message,
                    maximum_frame_bytes=self._maximum_frame_bytes,
                    deadline=deadline,
                    cancellation_event=cancellation_event,
                    before_send=before_send,
                )
                sent = True
                if on_sent is not None:
                    _run_callback(on_sent, failure_message="native control stream request failed")
            return self._await_response(
                pending,
                connection=connection,
                deadline=deadline,
                cancellation_event=cancellation_event,
            )
        except Exception as exc:
            if (
                isinstance(exc, LiveTransportError)
                and exc.kind
                in {
                    LiveTransportFailureKind.CANCELLED,
                    LiveTransportFailureKind.TIMED_OUT,
                }
                and (sent or not writing)
            ):
                if sent:
                    with self._lock:
                        self._abandoned[request_id] = None
                        while len(self._abandoned) > _DEFAULT_MAXIMUM_CACHED_RESPONSES:
                            self._abandoned.popitem(last=False)
                raise
            self._remember_ambiguous(request_id)
            self._disconnect(connection, exc)
            raise
        finally:
            with self._lock:
                self._pending.pop(request_id, None)

    def close(self) -> None:
        with self._connect_lock:
            connection = self._connection
            if connection is not None:
                self._disconnect(connection)

    def _check_owner(self, connection: _Connection) -> None:
        try:
            _require_connection_owner(connection, owner_pid=self._owner.pid)
            if self._verify_owner is not None:
                self._verify_owner()
        except LiveTransportError:
            raise
        except Exception as exc:
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED, "native control stream owner changed"
            ) from exc

    def _await_response(
        self,
        pending: _PendingResponse,
        *,
        connection: _Connection,
        deadline: float,
        cancellation_event: threading.Event | None,
    ) -> dict[str, object]:
        io_attempted = False
        reader_processing = self._reader_processing
        while True:
            _raise_if_cancelled(cancellation_event)
            # A local callback can prevent the reader from consuming a reply.
            # Keep the original marker so even a completed callback invalidates
            # peer-timeout evidence for this wait. Reads must not wait on a lock
            # held by that local processing beyond this request's deadline.
            current_processing = self._reader_processing
            local_processing = current_processing is not reader_processing or (
                current_processing is not None
                and current_processing[0] is connection
                and current_processing[1]
            )
            remaining = _remaining_seconds(
                deadline,
                io_attempted=io_attempted and not local_processing and self._connection is connection,
            )
            wait = (
                remaining
                if cancellation_event is None
                else min(remaining, _CANCELLATION_CHECK_SECONDS)
            )
            io_attempted = True
            if not pending.ready.wait(wait):
                continue
            if pending.failure is not None:
                raise pending.failure
            if pending.response is None:
                raise LiveTransportError(
                    LiveTransportFailureKind.REJECTED,
                    "native control stream response is unavailable",
                )
            return pending.response

    def _receive_loop(
        self,
        connection: _Connection,
        on_notification: Callable[[dict[str, object]], None] | None,
    ) -> None:
        try:
            while True:
                with self._lock:
                    if self._connection is not connection:
                        return
                message = read_message(
                    connection,
                    maximum_frame_bytes=self._maximum_frame_bytes,
                )
                # The read can finish after another thread closes this stream.
                # In-flight callbacks still retain this connection's consumer.
                with self._lock:
                    if self._connection is not connection:
                        return
                    processing = (connection, True)
                    self._reader_processing = processing
                try:
                    if message.get("jsonrpc") != "2.0":
                        raise LiveTransportError(
                            LiveTransportFailureKind.REJECTED,
                            "native control stream message is malformed",
                        )
                    if "method" in message and "id" not in message:
                        if on_notification is None:
                            raise LiveTransportError(
                                LiveTransportFailureKind.REJECTED,
                                "native control stream notification is unexpected",
                            )
                        on_notification(message)
                    elif "id" in message and "method" not in message:
                        self._accept_response(message)
                    else:
                        raise LiveTransportError(
                            LiveTransportFailureKind.REJECTED,
                            "native control stream message direction is invalid",
                        )
                finally:
                    with self._lock:
                        if self._reader_processing is processing:
                            self._reader_processing = (connection, False)
        except Exception as exc:
            self._disconnect(connection, exc)

    def _accept_response(self, message: dict[str, object]) -> None:
        request_id = message.get("id")
        if isinstance(request_id, str):
            with self._lock:
                abandoned = request_id in self._abandoned
                if abandoned:
                    self._abandoned.pop(request_id)
            if abandoned:
                if "error" not in message and not _is_json_object(message.get("result")):
                    raise LiveTransportError(
                        LiveTransportFailureKind.REJECTED,
                        "native control stream response result is malformed",
                    )
                return
        if self._validate_response is not None:
            self._validate_response(message)
        if not isinstance(request_id, str):
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED,
                "native control stream response identity is malformed",
            )
        with self._lock:
            pending = self._pending.get(request_id)
            if pending is None or pending.ready.is_set():
                raise LiveTransportError(
                    LiveTransportFailureKind.REJECTED,
                    "native control stream response request is unknown",
                )
            if "error" in message:
                pending.failure = LiveTransportError(
                    LiveTransportFailureKind.REJECTED,
                    "native control stream request was declined",
                )
                pending.ready.set()
                return
            result_value = message.get("result")
            if not _is_json_object(result_value):
                raise LiveTransportError(
                    LiveTransportFailureKind.REJECTED,
                    "native control stream response result is malformed",
                )
            response: dict[str, object] = copy.deepcopy(dict(result_value))
            self._completed[request_id] = _CompletedResponse(
                pending.fingerprint,
                copy.deepcopy(response),
            )
            while len(self._completed) > _DEFAULT_MAXIMUM_CACHED_RESPONSES:
                self._completed.popitem(last=False)
            # Publish the response atomically with its completed-cache entry.
            # An update owner may close immediately after the last response
            # byte. EOF must not overtake that accepted response and turn an
            # already-committed handoff into an ambiguous client failure.
            pending.response = response
            pending.ready.set()

    def _remember_ambiguous(self, request_id: str) -> None:
        with self._lock:
            self._ambiguous[request_id] = None
            while len(self._ambiguous) > _DEFAULT_MAXIMUM_CACHED_RESPONSES:
                self._ambiguous.popitem(last=False)

    def _disconnect(self, connection: _Connection, failure: BaseException | None = None) -> None:
        with self._lock:
            if self._connection is not connection:
                return
            self._connection = None
            on_disconnect, self._connection_on_disconnect = (
                self._connection_on_disconnect,
                None,
            )
            self._reader = None
            self._completed.clear()
            self._abandoned.clear()
            # A response accepted before EOF remains authoritative. Only
            # requests without a terminal response become ambiguous when the
            # owner disconnects.
            pending = tuple(
                request for request in self._pending.values() if not request.ready.is_set()
            )
            for request in pending:
                self._ambiguous[request.request_id] = None
            while len(self._ambiguous) > _DEFAULT_MAXIMUM_CACHED_RESPONSES:
                self._ambiguous.popitem(last=False)
        if on_disconnect is not None:
            try:
                on_disconnect()
            except Exception:
                pass
        _close_connection(connection)
        if isinstance(failure, LiveTransportError):
            error = failure
        elif failure is not None:
            error = LiveTransportError(
                LiveTransportFailureKind.REJECTED, "native control stream disconnected"
            )
            error.__cause__ = failure
        else:
            error = LiveTransportError(
                LiveTransportFailureKind.UNAVAILABLE,
                "native control stream disconnected",
            )
        for request in pending:
            request.failure = error
            request.ready.set()
