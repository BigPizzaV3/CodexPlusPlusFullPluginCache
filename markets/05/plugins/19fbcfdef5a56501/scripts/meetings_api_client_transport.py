#!/usr/bin/env python3
"""Bounded, cookie-free HTTPS transport for direct Meetings API clients."""

from __future__ import annotations

import hmac
import http.client
import json
import math
import random
import re
import socket
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import deque
from collections.abc import Callable
from concurrent.futures import Future
from concurrent.futures import TimeoutError as FutureTimeoutError
from contextlib import nullcontext
from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Protocol, TypeGuard, cast

from codex_auth_client import (
    AuthMaterial,
    ChatGPTAuthProvider,
    CodexAuthAccountUnverified,
    CodexAuthCancelled,
)
from meetings_analytics import parse_analytics_event
from meetings_api_client_common import record_account_fingerprint, record_request_headers
from meetings_connection_migration import MEETINGS_CONNECTION_URL, connection_request_body
from meetings_metrics import measure_notes_lookup_stage

from helpers import create_https_context, is_json, unique_json_object

RECORD_MEETINGS_URL = "https://chatgpt.com/backend-api/meetings/meetings"
RECORD_NOTES_URL = "https://chatgpt.com/backend-api/meetings/notes"
CALENDAR_CONNECTIONS_URL = "https://chatgpt.com/backend-api/aip/connectors/links/list_accessible"
STATSIG_BOOTSTRAP_URL = "https://chatgpt.com/backend-api/wham/statsig/bootstrap"
STATSIG_BOOTSTRAP_BODY = b'{"brand_name":"chatgpt-meetings","window_type":"mcp"}'
MINIMUM_INITIAL_PAGE_LIMIT = 1
MAXIMUM_INITIAL_PAGE_LIMIT = 40
CONTINUATION_PAGE_LIMIT = 15
MAXIMUM_PAGE_RESPONSE_BYTES = 16 * 1024 * 1024
MAXIMUM_CURSOR_BYTES = 8 * 1024
_MAXIMUM_SOCKET_TIMEOUT_SECONDS = 75.0
_HTTP_CANCELLATION_CHECK_SECONDS = 0.025

_CALENDAR_QUERY_TIMESTAMP_PATTERN = re.compile(
    r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3}Z$"
)
_MAXIMUM_TIMESTAMP_BYTES = 128
_REQUEST_TIMEOUT_MESSAGE = "Meetings request timed out."


class RecordTransportError(RuntimeError):
    """Base class for bounded Record transport failures."""


class RecordTransportBackendError(RecordTransportError):
    """The Record transport failed or observed an invalid bounded response."""


class RecordTransportTimeout(RecordTransportBackendError):
    """The Record transport exceeded its caller-supplied deadline."""


class RecordTransportCancelled(RecordTransportError):
    """The caller cancelled an in-flight Record transport request."""


class RecordTransportRateLimited(RecordTransportBackendError):
    """The request cannot retry within its remaining attempt or time budget."""

    def __init__(self, retry_after_seconds: float) -> None:
        super().__init__("Meetings is temporarily rate limited.")
        self.retry_after_seconds = retry_after_seconds


@dataclass(frozen=True, slots=True)
class RecordHTTPResult:
    """Bounded HTTP status and response body returned by Record transports."""

    status: int
    body: bytes
    retry_after_seconds: float | None = None


@dataclass(slots=True)
class RecordRateLimitBudget:
    """Quota retries left in one request, including its single auth refresh."""

    remaining_retries: int = 2


@dataclass(slots=True)
class _RateLimitCooldown:
    ready_at: float
    failures: int
    probing: bool = False


class RecordRateLimitRetry:
    """Share transient owner cooldowns without serializing healthy requests."""

    def __init__(
        self,
        *,
        clock: Callable[[], float] = time.monotonic,
        random_fraction: Callable[[], float] = random.random,
        wait: Callable[[float, threading.Event | None], None] | None = None,
    ) -> None:
        self._clock = clock
        self._random_fraction = random_fraction
        self._wait = wait or self._cancelable_wait
        self._lock = threading.Lock()
        self._cooldowns: dict[bytes, _RateLimitCooldown] = {}

    @staticmethod
    def _cancelable_wait(seconds: float, cancellation_event: threading.Event | None) -> None:
        if cancellation_event is None:
            time.sleep(seconds)
        elif cancellation_event.wait(seconds):
            raise RecordTransportCancelled("Meetings request was cancelled.")

    def request(
        self,
        operation: Callable[[float], RecordHTTPResult],
        *,
        owner: bytes,
        method: str,
        timeout_seconds: float,
        cancellation_event: threading.Event | None,
        verify_owner: Callable[[float], None],
        budget: RecordRateLimitBudget | None = None,
    ) -> RecordHTTPResult:
        """Retry only reads or an explicit pre-handler request-quota rejection.

        The existing caller deadline covers the entire retry sequence. One probe
        per throttled owner is released at a time; healthy requests stay concurrent.
        No response bodies, credentials, or resource identifiers enter the cooldown.
        """

        deadline = self._clock() + timeout_seconds
        budget = budget or RecordRateLimitBudget()
        waited = False
        attempt = 0
        while attempt < 3:
            probe: _RateLimitCooldown | None = None
            while True:
                _raise_if_cancelled(cancellation_event)
                now = self._clock()
                remaining = deadline - now
                if remaining <= 0:
                    raise RecordTransportTimeout(_REQUEST_TIMEOUT_MESSAGE)
                with self._lock:
                    cooldown = self._cooldowns.get(owner)
                    delay = max(0.0, cooldown.ready_at - now) if cooldown else 0.0
                    if cooldown is not None and cooldown.probing:
                        delay = max(delay, _HTTP_CANCELLATION_CHECK_SECONDS)
                    elif delay <= 0:
                        if cooldown is not None:
                            cooldown.probing = True
                            probe = cooldown
                        break
                if delay >= remaining:
                    raise RecordTransportRateLimited(delay)
                self._wait(min(delay, _HTTP_CANCELLATION_CHECK_SECONDS), cancellation_event)
                waited = True
            try:
                if waited or attempt:
                    verify_owner(max(0.0, deadline - self._clock()))
                _raise_if_cancelled(cancellation_event)
                with self._lock:
                    # Cached-auth recovery may wait while an in-flight response
                    # extends the shared floor. Reserve that newer cooldown too.
                    if self._cooldowns.get(owner) is not probe:
                        continue
                remaining = deadline - self._clock()
                if remaining <= 0:
                    raise RecordTransportTimeout(_REQUEST_TIMEOUT_MESSAGE)
                attempt += 1
                result = operation(remaining)
                _raise_if_cancelled(cancellation_event)
                if result.status != 429 or (
                    method != "GET" and not _is_request_quota_rejection(result.body)
                ):
                    with self._lock:
                        if self._cooldowns.get(owner) is probe:
                            self._cooldowns.pop(owner, None)
                    return result
                with self._lock:
                    previous = self._cooldowns.get(owner)
                    failures = min(7, previous.failures + 1) if previous else 1
                    fallback = min(60.0, 2.0 ** (failures - 1))
                    delay = max(
                        result.retry_after_seconds or 0.0,
                        fallback * (0.5 + 0.5 * self._random_fraction()),
                    )
                    ready_at = self._clock() + delay
                    if previous is not None:
                        ready_at = max(ready_at, previous.ready_at)
                    # Bounded process-local state; never evict a live owner's floor.
                    if owner not in self._cooldowns and len(self._cooldowns) >= 256:
                        expired = [
                            key
                            for key, item in self._cooldowns.items()
                            if item.ready_at <= self._clock() and not item.probing
                        ]
                        for key in expired:
                            self._cooldowns.pop(key, None)
                        if len(self._cooldowns) >= 256:
                            raise RecordTransportRateLimited(delay)
                    self._cooldowns[owner] = _RateLimitCooldown(ready_at, failures)
                if budget.remaining_retries == 0:
                    raise RecordTransportRateLimited(max(0.0, ready_at - self._clock()))
                budget.remaining_retries -= 1
            finally:
                if probe is not None:
                    with self._lock:
                        probe.probing = False
        raise AssertionError("Rate-limit attempt budget was not enforced")


def _is_request_quota_rejection(body: bytes) -> bool:
    if len(body) > 8192:
        return False
    try:
        payload: object = json.loads(body, object_pairs_hook=unique_json_object)
    except (ValueError, UnicodeError, RecursionError):
        return False
    return is_json(payload) and payload.get("detail") == "record_api_request_quota_exceeded"


PROCESS_RECORD_RATE_LIMIT_RETRY = RecordRateLimitRetry()


class _RequestDeadlineCancellation(threading.Event):
    """Bound this auth waiter without cancelling the shared auth refresh flight."""

    def __init__(self, caller: threading.Event | None, timeout_seconds: float) -> None:
        super().__init__()
        self._caller = caller
        self._deadline = time.monotonic() + timeout_seconds

    def is_set(self) -> bool:
        return (
            super().is_set()
            or (self._caller is not None and self._caller.is_set())
            or time.monotonic() >= self._deadline
        )

    def wait(self, timeout: float | None = None) -> bool:
        deadline = self._deadline
        if timeout is not None:
            deadline = min(deadline, time.monotonic() + timeout)
        while not self.is_set():
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                break
            super().wait(min(remaining, 0.025))
        return self.is_set()


def authenticated_record_request(
    transport: RecordHTTPTransport,
    auth: AuthMaterial,
    auth_client: ChatGPTAuthProvider,
    *,
    url: str,
    timeout_seconds: float,
    cancellation_event: threading.Event | None,
    method: str = "GET",
    body: bytes | None = None,
    statsig_bootstrap: bool = False,
    cleanup: bool = False,
    quota_budget: RecordRateLimitBudget | None = None,
) -> tuple[RecordHTTPResult, AuthMaterial]:
    path = urllib.parse.urlsplit(url).path
    is_notes_page = method == "GET" and path in {
        "/backend-api/meetings/notes",
        "/backend-api/meetings/meetings",
    }
    expected_owner = record_account_fingerprint(auth)
    request_auth = auth

    def verify_owner(remaining: float) -> None:
        nonlocal request_auth
        auth_cancellation = _RequestDeadlineCancellation(cancellation_event, remaining)
        try:
            with measure_notes_lookup_stage("backend_auth") if is_notes_page else nullcontext():
                current = auth_client.get_chatgpt_auth(
                    refresh_token=False, cancellation_event=auth_cancellation
                )
        except CodexAuthCancelled:
            if cancellation_event is not None and cancellation_event.is_set():
                raise
            raise RecordTransportTimeout("Meetings request timed out.") from None
        if not hmac.compare_digest(record_account_fingerprint(current), expected_owner):
            raise CodexAuthAccountUnverified("ChatGPT account changed during the request.")
        request_auth = current

    def operation(remaining: float) -> RecordHTTPResult:
        headers = record_request_headers(request_auth, has_json_body=body is not None)
        if statsig_bootstrap:
            headers["originator"] = "codex_desktop"
        if url in {CALENDAR_CONNECTIONS_URL, MEETINGS_CONNECTION_URL}:
            headers["OAI-Product-Sku"] = "CODEX"
        with measure_notes_lookup_stage("backend_http") if is_notes_page else nullcontext():
            return transport.request(
                url=url,
                headers=headers,
                timeout_seconds=remaining,
                cancellation_event=cancellation_event,
                method=method,
                body=body,
            )

    # Cleanup and preference opt-out stay usable during a read/request cooldown.
    # Native Start/Stop/end/upload recovery has its own recording retry owner.
    if (
        not url.startswith("https://chatgpt.com/backend-api/meetings/")
        or cleanup
        or method == "DELETE"
        or (
            method == "PATCH"
            and path
            in {"/backend-api/meetings/settings", "/backend-api/meetings/settings/preferences"}
        )
    ):
        return operation(timeout_seconds), request_auth
    result = PROCESS_RECORD_RATE_LIMIT_RETRY.request(
        operation,
        owner=expected_owner,
        method=method,
        timeout_seconds=timeout_seconds,
        cancellation_event=cancellation_event,
        verify_owner=verify_owner,
        budget=quota_budget,
    )
    return result, request_auth


class RecordHTTPTransport(Protocol):
    """Structural transport injected into authenticated Record API clients."""

    def request(
        self,
        *,
        url: str,
        headers: dict[str, str],
        timeout_seconds: float,
        cancellation_event: threading.Event | None,
        method: str = "GET",
        body: bytes | None = None,
    ) -> RecordHTTPResult:
        """Perform one bounded Record API request.

        Args:
            url: Absolute allowlisted Record API URL.
            headers: Request headers including current authenticated material.
            timeout_seconds: Remaining request deadline in seconds.
            cancellation_event: Optional caller cancellation signal.
            method: HTTP method for this request.
            body: Optional encoded JSON request body.

        Returns:
            The bounded status and body observed by the transport.
        """

        ...


class _ResponseHeaders(Protocol):
    def get(self, key: str, default: object = None, /) -> object:
        """Return one response-header value."""

        ...


class _HTTPResponse(Protocol):
    @property
    def headers(self) -> _ResponseHeaders:
        """Return the response headers."""

        ...

    def getcode(self) -> int:
        """Return the numeric HTTP status."""

        ...

    def read(self, size: int) -> bytes:
        """Read up to ``size`` response bytes."""

        ...

    def close(self) -> None:
        """Close the response stream."""

        ...


class _HTTPOpener(Protocol):
    def open(
        self,
        request: urllib.request.Request,
        /,
        *,
        timeout: float,
    ) -> _HTTPResponse:
        """Open one request with a bounded socket timeout."""

        ...


class _HTTPAbortTarget(Protocol):
    def close(self) -> None:
        """Interrupt one active connection or response."""

        ...


class _HTTPRequestExecution:
    """Bind one bounded HTTP operation to its current abortable transport."""

    def __init__(self, operation: Callable[[], RecordHTTPResult]) -> None:
        self.operation = operation
        self.future: Future[RecordHTTPResult] = Future()
        self._lock = threading.Lock()
        self._target: _HTTPAbortTarget | None = None
        self._abandoned = False

    def set_abort_target(self, target: _HTTPAbortTarget) -> None:
        with self._lock:
            abandoned = self._abandoned
            if not abandoned:
                self._target = target
        if abandoned:
            try:
                target.close()
            except (OSError, ValueError):
                pass
            raise RecordTransportCancelled("Meetings request was cancelled.")

    def require_active(self) -> None:
        with self._lock:
            abandoned = self._abandoned
        if abandoned:
            raise RecordTransportCancelled("Meetings request was cancelled.")

    def clear_abort_target(self, target: _HTTPAbortTarget) -> None:
        with self._lock:
            if self._target is target:
                self._target = None

    def abandon(self) -> None:
        with self._lock:
            self._abandoned = True
            target = self._target
            self._target = None
        self.future.cancel()
        if target is not None:
            try:
                target.close()
            except (OSError, ValueError):
                pass


class _HTTPExecutionContext(threading.local):
    current: _HTTPRequestExecution | None

    def __init__(self) -> None:
        self.current = None


_HTTP_EXECUTION_CONTEXT = _HTTPExecutionContext()


class _SharedHTTPExecutionPool:
    """Keep blocking DNS, TLS, headers, and body reads off the requesting thread."""

    _MAXIMUM_WORKERS = 4
    _MAXIMUM_PENDING_REQUESTS = 16

    def __init__(self) -> None:
        self._condition = threading.Condition()
        self._pending: deque[_HTTPRequestExecution] = deque()
        self._workers: list[threading.Thread] = []
        self._idle_workers = 0

    def submit(self, operation: Callable[[], RecordHTTPResult]) -> _HTTPRequestExecution:
        execution = _HTTPRequestExecution(operation)
        with self._condition:
            if len(self._pending) >= self._MAXIMUM_PENDING_REQUESTS:
                raise RecordTransportBackendError("Meetings request capacity is unavailable.")
            self._pending.append(execution)
            if (
                self._idle_workers < len(self._pending)
                and len(self._workers) < self._MAXIMUM_WORKERS
            ):
                worker = threading.Thread(
                    target=self._run,
                    name=f"record-meetings-http-{len(self._workers) + 1}",
                    daemon=True,
                )
                self._workers.append(worker)
                worker.start()
            self._condition.notify()
        return execution

    def _run(self) -> None:
        while True:
            with self._condition:
                self._idle_workers += 1
                try:
                    while not self._pending:
                        self._condition.wait()
                    execution = self._pending.popleft()
                finally:
                    self._idle_workers -= 1
            if not execution.future.set_running_or_notify_cancel():
                continue
            _HTTP_EXECUTION_CONTEXT.current = execution
            try:
                result = execution.operation()
            except BaseException as error:
                execution.future.set_exception(error)
            else:
                execution.future.set_result(result)
            finally:
                _HTTP_EXECUTION_CONTEXT.current = None


_PROCESS_HTTP_EXECUTION_POOL = _SharedHTTPExecutionPool()


class _PooledHTTPResponse:
    """Return an exhausted HTTPS connection to the process-local pool."""

    def __init__(
        self,
        response: http.client.HTTPResponse,
        connection: http.client.HTTPSConnection,
        pool: _PooledHTTPSOpener,
    ) -> None:
        self._response = response
        self._connection: http.client.HTTPSConnection | None = connection
        self._pool = pool
        self._exhausted = False
        self._lock = threading.Lock()

    @property
    def headers(self) -> _ResponseHeaders:
        return cast(_ResponseHeaders, self._response.headers)

    def getcode(self) -> int:
        return self._response.getcode()

    def read(self, size: int) -> bytes:
        chunk = self._response.read(size)
        if not chunk:
            self._exhausted = True
        return chunk

    def close(self) -> None:
        with self._lock:
            connection = self._connection
            self._connection = None
        if connection is None:
            return
        reusable = self._exhausted and not self._response.will_close
        self._response.close()
        if reusable:
            self._pool.release(connection)
        else:
            connection.close()


class _PooledHTTPSOpener:
    """Reuse bounded, cookie-free TLS connections for the fixed Record origin."""

    _MAXIMUM_IDLE_CONNECTIONS = 8
    _MAXIMUM_IDLE_SECONDS = 30.0

    def __init__(self) -> None:
        self._idle: list[tuple[float, http.client.HTTPSConnection]] = []
        self._lock = threading.Lock()

    def open(
        self,
        request: urllib.request.Request,
        /,
        *,
        timeout: float,
    ) -> _HTTPResponse:
        parsed = urllib.parse.urlsplit(request.full_url)
        if parsed.hostname is None:
            raise RecordTransportBackendError("Meetings request was invalid.")
        connection: http.client.HTTPSConnection | None = None
        stale_connections: list[http.client.HTTPSConnection] = []
        now = time.monotonic()
        with self._lock:
            while self._idle:
                released_at, candidate = self._idle.pop()
                if now - released_at <= self._MAXIMUM_IDLE_SECONDS:
                    connection = candidate
                    break
                stale_connections.append(candidate)
        for stale_connection in stale_connections:
            stale_connection.close()
        reused_connection = connection is not None
        if connection is None:
            connection = self._new_connection(parsed, timeout=timeout)
        else:
            connection.timeout = timeout
            if connection.sock is not None:
                connection.sock.settimeout(timeout)
        path = parsed.path or "/"
        if parsed.query:
            path += f"?{parsed.query}"
        execution = _HTTP_EXECUTION_CONTEXT.current
        while True:
            if execution is not None:
                execution.set_abort_target(connection)
            try:
                if connection.sock is None:
                    connection.connect()
                    if execution is not None:
                        execution.require_active()
                connection.request(
                    request.get_method(),
                    path,
                    body=request.data,
                    headers=dict(request.header_items()),
                )
                response = connection.getresponse()
            except (OSError, http.client.HTTPException):
                connection.close()
                if execution is not None:
                    execution.clear_abort_target(connection)
                if not reused_connection or request.get_method() != "GET":
                    raise
                # A stale keep-alive can fail after its original server has
                # closed it. Replay only an idempotent read, exactly once.
                reused_connection = False
                connection = self._new_connection(parsed, timeout=timeout)
                continue
            except BaseException:
                connection.close()
                if execution is not None:
                    execution.clear_abort_target(connection)
                raise
            pooled_response = _PooledHTTPResponse(response, connection, self)
            if execution is not None:
                execution.set_abort_target(pooled_response)
            return pooled_response

    @staticmethod
    def _new_connection(
        parsed: urllib.parse.SplitResult, *, timeout: float
    ) -> http.client.HTTPSConnection:
        hostname = parsed.hostname
        if hostname is None:
            raise RecordTransportBackendError("Meetings request was invalid.")
        try:
            context = create_https_context()
        except (OSError, ValueError):
            raise RecordTransportBackendError(
                "Meetings TLS trust could not be configured. Check CODEX_CA_CERTIFICATE or SSL_CERT_FILE."
            ) from None
        proxy = urllib.request.getproxies().get("https")
        if proxy is not None and not urllib.request.proxy_bypass(hostname):
            proxy_address = urllib.parse.urlsplit(proxy)
            if proxy_address.scheme != "http" or proxy_address.hostname is None:
                raise RecordTransportBackendError("Meetings HTTPS proxy is unavailable.")
            connection = http.client.HTTPSConnection(
                proxy_address.hostname,
                port=proxy_address.port or 80,
                timeout=timeout,
                context=context,
            )
            connection.set_tunnel(hostname, port=parsed.port or 443)
            return connection
        return http.client.HTTPSConnection(hostname, timeout=timeout, context=context)

    def release(self, connection: http.client.HTTPSConnection) -> None:
        with self._lock:
            if len(self._idle) < self._MAXIMUM_IDLE_CONNECTIONS:
                self._idle.append((time.monotonic(), connection))
                return
        connection.close()


_PROCESS_HTTPS_OPENER = _PooledHTTPSOpener()


class HTTPSRecordTransport:
    """Process-cached, cookie-free HTTPS transport with a bounded response body."""

    def __init__(self, opener: _HTTPOpener | None = None) -> None:
        # Every authenticated backend client shares one bounded process-local
        # connection pool. Injected openers remain a deterministic test seam.
        self._opener = opener or _PROCESS_HTTPS_OPENER

    def request(
        self,
        *,
        url: str,
        headers: dict[str, str],
        timeout_seconds: float,
        cancellation_event: threading.Event | None,
        method: str = "GET",
        body: bytes | None = None,
    ) -> RecordHTTPResult:
        """Perform one cookie-free HTTPS request.

        Args:
            url: Absolute allowlisted Record API URL.
            headers: Request headers including current authenticated material.
            timeout_seconds: Remaining request deadline in seconds.
            cancellation_event: Optional caller cancellation signal.
            method: HTTP method for this request.
            body: Optional encoded JSON request body.

        Returns:
            The bounded HTTP status and response body.
        """

        if (
            isinstance(timeout_seconds, bool)
            or not math.isfinite(timeout_seconds)
            or timeout_seconds <= 0
        ):
            raise RecordTransportTimeout(_REQUEST_TIMEOUT_MESSAGE)
        if self._opener is _PROCESS_HTTPS_OPENER and (
            not _is_allowed_record_request(method, url, body)
            or not _are_allowed_record_headers(
                headers,
                has_json_body=body is not None,
                allow_statsig_originator=url == STATSIG_BOOTSTRAP_URL,
                allow_calendar_product_sku=url
                in {CALENDAR_CONNECTIONS_URL, MEETINGS_CONNECTION_URL},
            )
        ):
            raise RecordTransportBackendError("Meetings request was invalid.")
        _raise_if_cancelled(cancellation_event)
        deadline = time.monotonic() + timeout_seconds
        execution = _PROCESS_HTTP_EXECUTION_POOL.submit(
            lambda: _inline_https_request(
                self._opener,
                url=url,
                headers=headers,
                timeout_seconds=timeout_seconds,
                cancellation_event=cancellation_event,
                method=method,
                body=body,
                deadline=deadline,
            )
        )
        while True:
            if cancellation_event is not None and cancellation_event.is_set():
                execution.abandon()
                raise RecordTransportCancelled("Meetings request was cancelled.")
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                execution.abandon()
                raise RecordTransportTimeout(_REQUEST_TIMEOUT_MESSAGE)
            try:
                return execution.future.result(
                    timeout=(
                        min(remaining, _HTTP_CANCELLATION_CHECK_SECONDS)
                        if cancellation_event is not None
                        else remaining
                    )
                )
            except FutureTimeoutError:
                continue
            except (OSError, RecordTransportBackendError) as error:
                if cancellation_event is not None and cancellation_event.is_set():
                    raise RecordTransportCancelled("Meetings request was cancelled.") from None
                if time.monotonic() >= deadline:
                    raise RecordTransportTimeout(_REQUEST_TIMEOUT_MESSAGE) from None
                raise error


def _inline_https_request(
    opener: _HTTPOpener,
    *,
    url: str,
    headers: dict[str, str],
    timeout_seconds: float,
    cancellation_event: threading.Event | None,
    method: str = "GET",
    body: bytes | None = None,
    deadline: float | None = None,
) -> RecordHTTPResult:
    """Perform one bounded request using a pooled or explicitly injected opener."""

    _raise_if_cancelled(cancellation_event)
    if deadline is None:
        deadline = time.monotonic() + timeout_seconds
    request = urllib.request.Request(
        url,
        headers=headers,
        data=body,
        method=method,
    )
    response: _HTTPResponse | None = None
    try:
        try:
            response = opener.open(
                request,
                timeout=min(timeout_seconds, _MAXIMUM_SOCKET_TIMEOUT_SECONDS),
            )
        except urllib.error.HTTPError as exc:
            # HTTPError is also the bounded response stream for non-2xx status
            # codes, despite the narrower typeshed protocol for its headers.
            response = cast(_HTTPResponse, exc)
        execution = _HTTP_EXECUTION_CONTEXT.current
        if execution is not None:
            execution.set_abort_target(response)
        _raise_if_cancelled(cancellation_event)
        _raise_if_deadline_expired(deadline)
        status = int(response.getcode())
        declared_length = _content_length(response.headers)
        if declared_length is not None and declared_length > MAXIMUM_PAGE_RESPONSE_BYTES:
            raise RecordTransportBackendError("Meetings returned an oversized response.")
        response_body = _read_bounded_response(
            response,
            cancellation_event,
            deadline=deadline,
        )
        return RecordHTTPResult(
            status=status,
            body=response_body,
            retry_after_seconds=(
                _retry_after_seconds(response.headers) if status in {429, 503} else None
            ),
        )
    except RecordTransportCancelled:
        raise
    except (
        OSError,
        TimeoutError,
        urllib.error.URLError,
        socket.timeout,
        http.client.HTTPException,
    ) as exc:
        _raise_if_cancelled(cancellation_event)
        _raise_if_deadline_expired(deadline)
        raise RecordTransportBackendError("Meetings could not be reached.") from exc
    finally:
        if response is not None:
            try:
                response.close()
            except OSError:
                pass


def _retry_after_seconds(headers: _ResponseHeaders) -> float | None:
    raw = headers.get("Retry-After")
    if not isinstance(raw, str) or len(raw) > 256:
        return None
    value = raw.strip()
    if re.fullmatch(r"[0-9]+(?:\.[0-9]+)?", value):
        seconds = float(value)
        return seconds if math.isfinite(seconds) else None
    try:
        instant = parsedate_to_datetime(value)
        if instant.tzinfo is None:
            return None
        now = time.time()
        response_date = headers.get("Date")
        if isinstance(response_date, str) and len(response_date) <= 256:
            try:
                server_now = parsedate_to_datetime(response_date)
                if server_now.tzinfo is not None:
                    now = server_now.timestamp()
            except (ValueError, TypeError, OverflowError):
                pass
        return max(0.0, instant.timestamp() - now)
    except (ValueError, TypeError, OverflowError):
        return None


def _content_length(headers: _ResponseHeaders | None) -> int | None:
    raw = headers.get("Content-Length") if headers is not None else None
    if isinstance(raw, bool) or not isinstance(raw, (int, str)):
        return None
    try:
        value = int(raw)
    except (TypeError, ValueError):
        return None
    return value if value >= 0 else None


def _read_bounded_response(
    response: _HTTPResponse,
    cancellation_event: threading.Event | None,
    *,
    deadline: float,
) -> bytes:
    body = bytearray()
    while True:
        _raise_if_cancelled(cancellation_event)
        _raise_if_deadline_expired(deadline)
        try:
            chunk = response.read(
                min(
                    64 * 1024,
                    MAXIMUM_PAGE_RESPONSE_BYTES + 1 - len(body),
                )
            )
        except (OSError, ValueError, http.client.HTTPException) as exc:
            _raise_if_cancelled(cancellation_event)
            _raise_if_deadline_expired(deadline)
            raise RecordTransportBackendError("Meetings returned an incomplete response.") from exc
        if not chunk:
            _raise_if_cancelled(cancellation_event)
            _raise_if_deadline_expired(deadline)
            return bytes(body)
        _raise_if_deadline_expired(deadline)
        body.extend(chunk)
        if len(body) > MAXIMUM_PAGE_RESPONSE_BYTES:
            raise RecordTransportBackendError("Meetings returned an oversized response.")


def _raise_if_deadline_expired(deadline: float) -> None:
    if time.monotonic() >= deadline:
        raise RecordTransportTimeout(_REQUEST_TIMEOUT_MESSAGE)


def _raise_if_cancelled(event: threading.Event | None) -> None:
    if event is not None and event.is_set():
        raise RecordTransportCancelled("Meetings request was cancelled.")


_RECORD_INTERACTION_PATH_PATTERN = re.compile(
    r"^/backend-api/meetings/meetings/([A-Za-z0-9_-]{1,512})"
    r"(?:/(summary|transcripts|share/eligibility|share|feedback))?$"
)
_RECORD_NOTE_INTERACTION_PATH_PATTERN = re.compile(
    r"^/backend-api/meetings/notes/([A-Za-z0-9_-]{1,512})"
    r"(?:/(transcripts|share/eligibility|share|feedback|reprocess))?$"
)


def _is_allowed_versioned_statsig_body(body: bytes | None) -> bool:
    if body is None or len(body) > 256:
        return False
    try:
        value = json.loads(body, object_pairs_hook=unique_json_object)
    except (ValueError, UnicodeError):
        return False
    if not is_json(value):
        return False
    if set(value) == {"brand_name", "window_type", "app_version"}:
        allowed_context = value["window_type"] == "mcp"
    elif set(value) == {"brand_name", "window_type", "app_version", "system_name"}:
        allowed_context = (
            isinstance(value["window_type"], str)
            and value["window_type"] in {"web", "desktop", "mobile", "unknown"}
            and isinstance(value["system_name"], str)
            and value["system_name"] in {"Windows", "Darwin", "Linux", "iOS", "Android", "unknown"}
        )
    else:
        return False
    return (
        allowed_context
        and value["brand_name"] == "chatgpt-meetings"
        and isinstance(value["app_version"], str)
        and re.fullmatch(
            r"(?:0|[1-9][0-9]{0,8})\.(?:0|[1-9][0-9]{0,8})\.(?:0|[1-9][0-9]{0,8})"
            r"(?:-(?!0[0-9]+(?:[.+]|$))[0-9A-Za-z-]+"
            r"(?:\.(?!0[0-9]+(?:[.+]|$))[0-9A-Za-z-]+)*)?"
            r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?",
            value["app_version"],
        )
        is not None
    )


def _is_allowed_record_request(
    method: str,
    url: str,
    body: bytes | None,
) -> bool:
    try:
        parsed = urllib.parse.urlsplit(url)
        # Python 3.10 rejects an empty string with strict parsing; no query is
        # valid for the fixed authenticated endpoints below on every runtime.
        query = (
            urllib.parse.parse_qsl(
                parsed.query,
                keep_blank_values=True,
                strict_parsing=True,
                max_num_fields=4,
            )
            if parsed.query
            else []
        )
    except ValueError:
        return False
    if (
        method not in {"GET", "POST", "PATCH", "DELETE"}
        or parsed.scheme != "https"
        or parsed.netloc != "chatgpt.com"
        or parsed.fragment
    ):
        return False
    if parsed.path == "/backend-api/me":
        return url == "https://chatgpt.com/backend-api/me" and method == "GET" and body is None
    if parsed.path == "/backend-api/wham/statsig/bootstrap":
        return (
            url == STATSIG_BOOTSTRAP_URL
            and method == "POST"
            and (body == STATSIG_BOOTSTRAP_BODY or _is_allowed_versioned_statsig_body(body))
        )
    if parsed.path == "/backend-api/meetings/meetings":
        return method == "GET" and body is None and _is_allowed_record_notes_query(query)
    if parsed.path == "/backend-api/meetings/notes":
        return method == "GET" and body is None and _is_allowed_record_notes_query(query)
    if url == CALENDAR_CONNECTIONS_URL:
        return method == "POST" and _decoded_json_object(body) == {
            "principals": [],
            "link_refresh_strategy": "BLOCKING",
        }
    if url == MEETINGS_CONNECTION_URL:
        payload = _decoded_json_object(body)
        return (
            method == "POST"
            and payload is not None
            and payload == connection_request_body()
            and payload.get("ensure_exists") is True
        )
    if parsed.path == "/backend-api/accounts":
        return method == "GET" and body is None and not query
    if parsed.path == "/backend-api/meetings/calendar/events":
        return method == "GET" and body is None and _is_allowed_record_calendar_query(query)
    if parsed.path == "/backend-api/meetings/track":
        payload = _decoded_json_object(body)
        if (
            method != "POST"
            or query
            or payload is None
            or set(payload)
            != {
                "clientEventId",
                "eventName",
                "metadata",
                "pluginVersion",
                "codexAppVersion",
                "operatingSystem",
            }
        ):
            return False
        version = payload["pluginVersion"]
        if (
            not isinstance(version, str)
            or len(version) > 80
            or re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._+-]*", version) is None
        ):
            return False
        codex_version = payload["codexAppVersion"]
        if (
            not isinstance(codex_version, str)
            or len(codex_version) > 80
            or re.fullmatch(
                r"(?:unknown|[0-9]{1,9}\.[0-9]{1,9}\.[0-9]{1,9}(?:[-+][A-Za-z0-9][A-Za-z0-9.+-]{0,39})?)",
                codex_version,
            )
            is None
            or payload["operatingSystem"] not in ("macos", "windows", "linux", "unknown")
        ):
            return False
        try:
            parse_analytics_event(
                {
                    key: value
                    for key, value in payload.items()
                    if key not in {"pluginVersion", "codexAppVersion", "operatingSystem"}
                }
            )
        except ValueError:
            return False
        return True
    if parsed.path == "/backend-api/meetings/activity":
        return method == "GET" and body is None and not query
    if parsed.path == "/backend-api/meetings/activity/viewed":
        return method == "POST" and body is None and not query
    if parsed.path == "/backend-api/meetings/settings/preferences":
        if query:
            return False
        if method == "GET":
            return body is None
        return method == "PATCH" and _is_allowed_settings_body(body)
    note_path_match = _RECORD_NOTE_INTERACTION_PATH_PATTERN.fullmatch(parsed.path)
    if note_path_match is not None:
        suffix = note_path_match.group(2)
        if query:
            return False
        if suffix == "share":
            return method == "POST" and _is_allowed_share_body(body)
        if suffix == "share/eligibility":
            return method == "POST" and _is_allowed_share_eligibility_body(body)
        if suffix == "feedback":
            return method == "POST" and _is_allowed_feedback_body(body)
        if suffix == "reprocess":
            return method == "POST" and body is None
        if method == "DELETE":
            return suffix is None and body is None
        return method == "GET" and body is None and suffix in {None, "transcripts"}
    path_match = _RECORD_INTERACTION_PATH_PATTERN.fullmatch(parsed.path)
    if path_match is None:
        return False
    suffix = path_match.group(2)
    if query:
        return False
    if suffix in {"share", "share/eligibility"}:
        return method == "POST" and _is_allowed_share_body(body)
    if suffix == "feedback":
        return method == "POST" and _is_allowed_feedback_body(body)
    if method == "DELETE":
        return suffix is None and body is None
    return method == "GET" and body is None and suffix in {None, "summary", "transcripts"}


def _decoded_json_object(body: bytes | None) -> dict[str, object] | None:
    if body is None or not body or len(body) > 16 * 1024:
        return None
    try:
        value: object = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError, RecursionError):
        return None
    return value if is_json(value) else None


def _is_allowed_settings_body(body: bytes | None) -> bool:
    value = _decoded_json_object(body)
    return bool(
        value
        and set(value).issubset(
            {
                "featureEnabled",
                "autoRecordEnabled",
                "slackNotificationsEnabled",
            }
        )
        and all(isinstance(item, bool) for item in value.values())
    )


def _is_allowed_share_eligibility_body(body: bytes | None) -> bool:
    value = _decoded_json_object(body)
    return value == {} or _is_allowed_share_body(body)


def _is_allowed_share_body(body: bytes | None) -> bool:
    value = _decoded_json_object(body)
    if value is None or set(value) != {"email"}:
        return False
    email = value.get("email")
    return (
        isinstance(email, str)
        and 3 <= len(email) <= 320
        and email.count("@") == 1
        and not email.startswith("@")
        and not email.endswith("@")
        and not any(character.isspace() for character in email)
        and not _contains_header_control_character(email)
    )


_FEEDBACK_CATEGORIES = frozenset(
    {
        "good_bot",
        "bad_bot",
        "other",
        "bot_did_not_join",
        "bot_disconnected",
        "recording_missing",
        "transcript_issue",
        "summary_issue",
        "calendar_schedule_issue",
    }
)


def _is_allowed_feedback_body(body: bytes | None) -> bool:
    value = _decoded_json_object(body)
    if value is None or not {"rating", "includeDebugArtifacts"}.issubset(value):
        return False
    if set(value) - {
        "rating",
        "feedbackText",
        "includeDebugArtifacts",
        "feedbackContinuationToken",
    }:
        return False
    text = value.get("feedbackText")
    continuation_token = value.get("feedbackContinuationToken")
    return (
        value.get("rating") in _FEEDBACK_CATEGORIES
        and isinstance(value.get("includeDebugArtifacts"), bool)
        and (text is None or isinstance(text, str) and len(text) <= 2_000)
        and (
            continuation_token is None
            or isinstance(continuation_token, str)
            and 1 <= len(continuation_token) <= 2_048
            and not _contains_header_control_character(continuation_token)
            and not any(character.isspace() for character in continuation_token)
        )
    )


def _is_allowed_record_notes_query(query: list[tuple[str, str]]) -> bool:
    if len(query) not in {1, 2, 3} or query[0][0] != "limit":
        return False
    try:
        limit = int(query[0][1])
    except ValueError:
        return False
    if str(limit) != query[0][1]:
        return False
    remaining = query[1:]
    if remaining[:1] == [("include_unsuccessful", "true")]:
        remaining = remaining[1:]
    if remaining and remaining[0][0] == "recording_started_at":
        if len(remaining) != 1 or _canonical_calendar_query_datetime(remaining[0][1]) is None:
            return False
        remaining = remaining[1:]
    if not remaining:
        return MINIMUM_INITIAL_PAGE_LIMIT <= limit <= MAXIMUM_INITIAL_PAGE_LIMIT
    if (
        len(remaining) != 1
        or limit != CONTINUATION_PAGE_LIMIT
        or remaining[0][0] != "cursor"
        or not remaining[0][1]
        or _contains_header_control_character(remaining[0][1])
    ):
        return False
    try:
        return len(remaining[0][1].encode("utf-8")) <= MAXIMUM_CURSOR_BYTES
    except UnicodeEncodeError:
        return False


def _is_allowed_record_calendar_query(query: list[tuple[str, str]]) -> bool:
    if len(query) not in {3, 4}:
        return False
    if [key for key, _value in query[:3]] != ["time_min", "time_max", "limit"]:
        return False
    if query[2][1] != "200":
        return False
    time_min = _canonical_calendar_query_datetime(query[0][1])
    time_max = _canonical_calendar_query_datetime(query[1][1])
    if time_min is None or time_max is None:
        return False
    local_start = time_min.astimezone()
    local_end = time_max.astimezone()
    if (
        local_start.timetz().replace(tzinfo=None) != datetime.min.time()
        or local_end.timetz().replace(tzinfo=None) != datetime.min.time()
        or (local_end.date() - local_start.date()).days != 1
    ):
        return False
    if len(query) == 3:
        return True
    option_key, option_value = query[3]
    if option_key == "refresh":
        return option_value == "true"
    if (
        option_key != "cursor"
        or not option_value
        or _contains_header_control_character(option_value)
    ):
        return False
    try:
        return len(option_value.encode("utf-8")) <= MAXIMUM_CURSOR_BYTES
    except UnicodeEncodeError:
        return False


def _canonical_calendar_query_datetime(value: str) -> datetime | None:
    try:
        encoded = value.encode("utf-8")
    except UnicodeEncodeError:
        return None
    if (
        len(encoded) > _MAXIMUM_TIMESTAMP_BYTES
        or _CALENDAR_QUERY_TIMESTAMP_PATTERN.fullmatch(value) is None
    ):
        return None
    try:
        parsed = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        return None
    return parsed.replace(tzinfo=timezone.utc)


def _are_allowed_record_headers(
    value: object,
    *,
    has_json_body: bool = False,
    allow_statsig_originator: bool = False,
    allow_calendar_product_sku: bool = False,
) -> TypeGuard[dict[str, str]]:
    expected_headers = {
        "Accept",
        "Authorization",
        "Cache-Control",
        "ChatGPT-Account-Id",
        "User-Agent",
    }
    if has_json_body:
        expected_headers.add("Content-Type")
    if allow_statsig_originator:
        expected_headers.add("originator")
    if allow_calendar_product_sku:
        expected_headers.add("OAI-Product-Sku")
    if not is_json(value) or set(value) != expected_headers:
        return False
    if not all(isinstance(item, str) for item in value.values()):
        return False
    authorization = value["Authorization"]
    account_id = value["ChatGPT-Account-Id"]
    if not isinstance(authorization, str) or not isinstance(account_id, str):
        return False
    try:
        authorization_bytes = authorization.encode("ascii")
        account_id_bytes = account_id.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return (
        value["Accept"] == "application/json"
        and value["Cache-Control"] == "no-store"
        and value["User-Agent"] == "ChatGPT Meetings/1.0"
        and (not has_json_body or value.get("Content-Type") == "application/json")
        and (not allow_statsig_originator or value.get("originator") == "codex_desktop")
        and (not allow_calendar_product_sku or value.get("OAI-Product-Sku") == "CODEX")
        and authorization.startswith("Bearer ")
        and len(authorization_bytes) > len("Bearer ")
        and len(authorization_bytes) <= 64 * 1024 + len("Bearer ")
        and 0 < len(account_id_bytes) <= 256
        and not _contains_header_control_character(authorization)
        and not _contains_header_control_character(account_id)
    )


def _contains_header_control_character(value: str) -> bool:
    return any(ord(character) < 0x20 or ord(character) == 0x7F for character in value)


__all__ = [
    "CONTINUATION_PAGE_LIMIT",
    "HTTPSRecordTransport",
    "MAXIMUM_CURSOR_BYTES",
    "MAXIMUM_INITIAL_PAGE_LIMIT",
    "MAXIMUM_PAGE_RESPONSE_BYTES",
    "MINIMUM_INITIAL_PAGE_LIMIT",
    "RECORD_MEETINGS_URL",
    "RECORD_NOTES_URL",
    "RecordHTTPResult",
    "RecordHTTPTransport",
    "RecordTransportBackendError",
    "RecordTransportCancelled",
    "RecordTransportError",
    "RecordTransportTimeout",
]
