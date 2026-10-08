"""A small, process-shared limit for automatic native-owner replacement."""

from __future__ import annotations

import os
import stat
import tempfile
import time
from collections.abc import Callable, Generator
from contextlib import contextmanager
from pathlib import Path

from control_protocol import ControlUnavailable, canonical_json

from helpers import is_json, is_json_array, parse_bounded_json

MAXIMUM_AUTOMATIC_RESTARTS = 3
AUTOMATIC_RESTART_WINDOW_SECONDS = 300
_RECEIPT = "automatic-restart-budget.json"
_LOCK = "automatic-restart-budget.lock"
_RECOVERY_LOCK = "listener-recovery.lock"
_MAXIMUM_BYTES = 512
_MAXIMUM_CLOCK = (1 << 63) - 1


def _identity(metadata: os.stat_result) -> tuple[int, int]:
    return metadata.st_dev, metadata.st_ino


def _lock(descriptor: int) -> None:
    if os.name == "nt":
        import msvcrt

        os.lseek(descriptor, 0, os.SEEK_SET)
        msvcrt.locking(descriptor, msvcrt.LK_NBLCK, 1)
    else:
        import fcntl

        fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)


def _open_private(path: Path) -> tuple[int, bool]:
    import control_client

    flags = (
        os.O_RDWR
        | getattr(os, "O_BINARY", 0)
        | getattr(os, "O_CLOEXEC", 0)
        | getattr(os, "O_NOFOLLOW", 0)
        | getattr(os, "O_NONBLOCK", 0)
    )
    try:
        return os.open(path, flags | os.O_CREAT | os.O_EXCL, 0o600), True
    except FileExistsError:
        control_client.require_private(path, directory=False)
        return os.open(path, flags), False


def _validate_file(
    root: Path,
    root_identity: tuple[int, int],
    path: Path,
    descriptor: int,
    opened: os.stat_result,
) -> None:
    import control_client

    current = control_client.require_private(path, directory=False)
    held = os.fstat(descriptor)
    if (
        _identity(control_client.require_private(root, directory=True)) != root_identity
        or _identity(current) != _identity(opened)
        or _identity(held) != _identity(opened)
        or not stat.S_ISREG(held.st_mode)
        or held.st_nlink != 1
        or held.st_size > _MAXIMUM_BYTES
    ):
        raise ControlUnavailable("automatic recovery file changed")


@contextmanager
def _private_lock(
    root: Path, filename: str
) -> Generator[tuple[tuple[int, int], Callable[[], None]], None, None]:
    import control_client

    descriptor = -1
    try:
        root_identity = _identity(control_client.require_private(root, directory=True))
        path = root / filename
        descriptor, _ = _open_private(path)
        opened = os.fstat(descriptor)

        def revalidate() -> None:
            _validate_file(root, root_identity, path, descriptor, opened)

        revalidate()
        _lock(descriptor)
        revalidate()
        yield root_identity, revalidate
    except OSError as error:
        raise ControlUnavailable(
            "automatic recovery is unavailable or already in progress"
        ) from error
    finally:
        if descriptor >= 0:
            # Closing the sole descriptor releases flock / the Windows byte lock.
            os.close(descriptor)


@contextmanager
def automatic_recovery_guard(root: Path) -> Generator[Callable[[], None], None, None]:
    """Coalesce the whole health-check/termination attempt across MCP processes.

    Call the yielded validator at destructive boundaries. A concurrent attempt
    cannot overwrite the shared challenge while this guard remains held.
    """
    with _private_lock(root, _RECOVERY_LOCK) as (_, revalidate):
        yield revalidate


def _claims(payload: bytes) -> list[int]:
    value = parse_bounded_json(payload.decode("utf-8"))
    if (
        not is_json(value)
        or set(value) != {"version", "monotonicNanoseconds"}
        or type(value.get("version")) is not int
        or value["version"] != 1
    ):
        raise ValueError("invalid automatic restart budget")
    raw = value["monotonicNanoseconds"]
    if not is_json_array(raw) or not 1 <= len(raw) <= MAXIMUM_AUTOMATIC_RESTARTS:
        raise ValueError("invalid automatic restart budget")
    result: list[int] = []
    for item in raw:
        if type(item) is not int or not 0 <= item <= _MAXIMUM_CLOCK:
            raise ValueError("invalid automatic restart budget")
        if result and item < result[-1]:
            raise ValueError("invalid automatic restart budget")
        result.append(item)
    return result


def _read_receipt(
    root: Path, root_identity: tuple[int, int]
) -> tuple[bytes, tuple[int, int]] | None:
    import control_client

    path = root / _RECEIPT
    try:
        path.lstat()
    except FileNotFoundError:
        return None
    expected = control_client.require_private(path, directory=False)
    descriptor = os.open(
        path,
        os.O_RDONLY
        | getattr(os, "O_BINARY", 0)
        | getattr(os, "O_CLOEXEC", 0)
        | getattr(os, "O_NOFOLLOW", 0)
        | getattr(os, "O_NONBLOCK", 0),
    )
    try:
        _validate_file(root, root_identity, path, descriptor, expected)
        payload = os.read(descriptor, _MAXIMUM_BYTES + 1)
        _validate_file(root, root_identity, path, descriptor, expected)
        if len(payload) > _MAXIMUM_BYTES:
            raise ControlUnavailable("automatic recovery file is too large")
        return payload, _identity(expected)
    finally:
        os.close(descriptor)


def claim_automatic_restart(root: Path, *, monotonic_ns: int | None = None) -> bool:
    """Durably reserve one attempt before termination; never poll on healthy I/O.

    The system monotonic clock is shared across Python 3.10+ processes. A lower
    clock origin clears the previous boot's claims, whose owners cannot survive
    reboot. Wall-clock corrections, owner epochs and successful connections do
    not replenish the rolling budget. Contention and unsafe receipts fail closed.
    """
    import control_client

    try:
        # The independent empty lock remains stable while the receipt is first
        # initialized. Competing creators cannot mistake partial initialization
        # for a malformed receipt or strand the creator behind another reader.
        with _private_lock(root, _LOCK) as (root_identity, revalidate_lock):
            path = root / _RECEIPT
            existing = _read_receipt(root, root_identity)
            previous = [] if existing is None else _claims(existing[0])
            now = time.monotonic_ns() if monotonic_ns is None else monotonic_ns
            if type(now) is not int or not 0 <= now <= _MAXIMUM_CLOCK:
                return False
            if previous and now < previous[-1]:
                previous = []
            window = AUTOMATIC_RESTART_WINDOW_SECONDS * 1_000_000_000
            retained = [claim for claim in previous if now - claim < window]
            if len(retained) >= MAXIMUM_AUTOMATIC_RESTARTS:
                return False
            retained.append(now)
            updated = canonical_json({"version": 1, "monotonicNanoseconds": retained}).encode(
                "utf-8"
            )
            revalidate_lock()
            descriptor, temporary_name = tempfile.mkstemp(
                prefix=".automatic-restart-budget-", dir=root
            )
            temporary = Path(temporary_name)
            created = os.fstat(descriptor)
            try:
                # An incomplete write stays unpublished. Validate inherited
                # Windows ACLs before bytes, then close before atomic rename.
                _validate_file(root, root_identity, temporary, descriptor, created)
                if os.write(descriptor, updated) != len(updated):
                    return False
                os.fsync(descriptor)
                _validate_file(root, root_identity, temporary, descriptor, created)
                os.close(descriptor)
                descriptor = -1
                revalidate_lock()
                current = control_client.require_private(temporary, directory=False)
                if _identity(current) != _identity(created) or current.st_nlink != 1:
                    return False
                if _read_receipt(root, root_identity) != existing:
                    return False
                revalidate_lock()
                os.replace(temporary, path)
                if _read_receipt(root, root_identity) != (updated, _identity(created)):
                    return False
            finally:
                if descriptor >= 0:
                    os.close(descriptor)
                try:
                    current = control_client.require_private(temporary, directory=False)
                    revalidate_lock()
                    if _identity(current) == _identity(created) and current.st_nlink == 1:
                        temporary.unlink()
                except (OSError, ControlUnavailable):
                    pass
            if os.name != "nt":
                directory = os.open(root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
                try:
                    if _identity(os.fstat(directory)) != root_identity:
                        return False
                    os.fsync(directory)
                finally:
                    os.close(directory)
            return True
    except (OSError, ValueError, RecursionError, ControlUnavailable):
        return False
