"""Bounded, on-demand repair of an independently verified native listener."""

from __future__ import annotations

import os
import stat
import tempfile
import threading
import time
import uuid
from collections.abc import Callable
from pathlib import Path

from companion_control_health import (
    HEALTH_MAX_BYTES,
    HealthResponse,
    is_health_request,
    is_health_response,
    is_health_support,
)
from control_protocol import ControlUnavailable, canonical_json

from helpers import is_json, parse_bounded_json

_SUPPORT_FILE = "health-support.json"
_REQUEST_FILE = "health-request.json"
_RESPONSE_FILE = "health-response.json"
_MAX_RESPONSE_WAIT_SECONDS = 3.0


def _identity(metadata: os.stat_result) -> tuple[int, int]:
    return metadata.st_dev, metadata.st_ino


def _read_file(path: Path) -> dict[str, object] | None:
    import control_client

    try:
        path.lstat()
    except FileNotFoundError:
        return None
    metadata = control_client.require_private(path, directory=False)
    if metadata.st_size > HEALTH_MAX_BYTES or metadata.st_nlink != 1:
        raise ControlUnavailable("native listener health file is too large")
    descriptor = os.open(
        path,
        os.O_RDONLY
        | getattr(os, "O_BINARY", 0)
        | getattr(os, "O_CLOEXEC", 0)
        | getattr(os, "O_NOFOLLOW", 0)
        | getattr(os, "O_NONBLOCK", 0),
    )
    try:
        opened = os.fstat(descriptor)
        if (
            not stat.S_ISREG(opened.st_mode)
            or opened.st_nlink != 1
            or _identity(opened) != _identity(metadata)
        ):
            raise ControlUnavailable("native listener health file changed")
        data = os.read(descriptor, HEALTH_MAX_BYTES + 1)
        if len(data) > HEALTH_MAX_BYTES:
            raise ControlUnavailable("native listener health file is too large")
        if _identity(control_client.require_private(path, directory=False)) != _identity(opened):
            raise ControlUnavailable("native listener health file changed")
    finally:
        os.close(descriptor)
    value = parse_bounded_json(data.decode("utf-8"))
    if not is_json(value):
        raise ControlUnavailable("native listener health file is malformed")
    return value


def _write_request(root: Path, value: dict[str, object], root_identity: tuple[int, int]) -> None:
    import control_client

    payload = canonical_json(value).encode("utf-8")
    if len(payload) > HEALTH_MAX_BYTES or not is_health_request(value):
        raise ControlUnavailable("native listener health request is too large")
    path = root / _REQUEST_FILE
    previous = _read_file(path)
    if previous is not None and not is_health_request(previous):
        raise ControlUnavailable("native listener health request was rejected")
    descriptor, temporary_name = tempfile.mkstemp(prefix=".health-request-", dir=root)
    temporary = Path(temporary_name)
    created = os.fstat(descriptor)
    try:
        # Windows inherits the verified private parent's ACL; check it before
        # writing. POSIX mkstemp creates the new file with mode 0600.
        if _identity(control_client.require_private(temporary, directory=False)) != _identity(
            created
        ):
            raise ControlUnavailable("native listener health request changed")
        with os.fdopen(descriptor, "wb", closefd=False) as stream:
            stream.write(payload)
            stream.flush()
        # Windows cannot rename a CRT-open file without delete sharing.
        os.close(descriptor)
        descriptor = -1
        if _identity(control_client.require_private(temporary, directory=False)) != _identity(
            created
        ):
            raise ControlUnavailable("native listener health request changed")
        if _identity(control_client.require_private(root, directory=True)) != root_identity:
            raise ControlUnavailable("native listener health root changed")
        current = _read_file(path)
        if current != previous:
            raise ControlUnavailable("native listener health request changed")
        os.replace(temporary, path)
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        try:
            if _identity(temporary.lstat()) == _identity(created):
                temporary.unlink()
        except FileNotFoundError:
            pass


def request_listener_repair(
    root: Path,
    *,
    owner_epoch: str,
    pid: int,
    revalidate_owner: Callable[[], None],
    cancellation_event: threading.Event,
    on_request: Callable[[str], None],
    timeout_seconds: float = _MAX_RESPONSE_WAIT_SECONDS,
) -> str | None:
    """Ask an advertised owner to repair its listener, never to mutate capture.

    One request returns on a matching reply, with a three-second maximum wait.
    None means unsupported or unanswered. A matching acknowledgement supplies
    an endpoint for independently verified, authenticated stream connection; it
    is not recording or replacement authority.
    """
    import control_client

    try:
        root_identity = _identity(control_client.require_private(root, directory=True))
        marker = _read_file(root / _SUPPORT_FILE)
        if marker is None:
            return None
        if not is_health_support(marker):
            raise ControlUnavailable("native listener health support was rejected")
        if marker["pid"] != pid or marker["ownerEpoch"] != owner_epoch:
            return None
        if cancellation_event.is_set():
            raise ControlUnavailable("native listener recovery was cancelled")
        revalidate_owner()
        request_id = str(uuid.uuid4())
        timeout_seconds = min(_MAX_RESPONSE_WAIT_SECONDS, max(0.0, timeout_seconds))
        deadline = time.monotonic() + timeout_seconds
        request: dict[str, object] = {
            "version": 1,
            "ownerEpoch": owner_epoch,
            "requestId": request_id,
            "deadlineUnixMillis": int((time.time() + timeout_seconds) * 1000),
        }
        _write_request(root, request, root_identity)
        on_request(request_id)
        while True:
            if cancellation_event.is_set():
                raise ControlUnavailable("native listener recovery was cancelled")
            if time.monotonic() >= deadline:
                return None
            if _identity(control_client.require_private(root, directory=True)) != root_identity:
                raise ControlUnavailable("native listener health root changed")
            response = _listener_repair_response(
                root, owner_epoch=owner_epoch, request_id=request_id
            )
            if response is not None:
                return response["endpoint"]
            cancellation_event.wait(min(0.025, max(0.0, deadline - time.monotonic())))
    except (OSError, ValueError, RecursionError) as error:
        raise ControlUnavailable("native listener health exchange is unavailable") from error


def listener_repair_acknowledged(root: Path, *, owner_epoch: str, request_id: str) -> bool:
    """A late acknowledgement still revokes a pending unresponsive-owner decision."""
    return (
        _listener_repair_response(root, owner_epoch=owner_epoch, request_id=request_id) is not None
    )


def _listener_repair_response(
    root: Path, *, owner_epoch: str, request_id: str
) -> HealthResponse | None:
    try:
        response = _read_file(root / _RESPONSE_FILE)
        if response is None:
            return None
        if not is_health_response(response):
            raise ControlUnavailable("native listener health response was rejected")
        if response["ownerEpoch"] == owner_epoch and response["requestId"] == request_id:
            return response
        return None
    except (OSError, ValueError, RecursionError) as error:
        raise ControlUnavailable("native listener health response is unavailable") from error
