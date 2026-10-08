"""Passive, owner-bound snapshots from the authenticated native control stream."""

from __future__ import annotations

import copy
import json
import re
import threading
from collections.abc import Mapping
from dataclasses import dataclass

from recording_control_action_contract import (
    RECORDING_CONTROL_SAFE_INTEGER_MAX,
)
from recording_status_contract import is_recording_status_response

from helpers import is_json, is_json_value

_MAXIMUM_STATUS_SNAPSHOT_BYTES = 1_048_576
_MAXIMUM_NATIVE_OWNER_PID = 2_147_483_647
_STREAM_IDENTIFIER = re.compile(r"^[A-Za-z0-9_-]{1,128}$")


@dataclass(frozen=True, repr=False)
class StatusBinding:
    """Exact authenticated owner and one non-reusable stream connection."""

    epoch: str
    pid: int
    session_id: str
    generation: int


@dataclass(frozen=True, repr=False)
class _StatusSnapshot:
    binding: StatusBinding
    revision: int
    payload: dict[str, object]


class NativeStatusCache:
    """A bounded push cache; reading never locks or performs native I/O.

    The stream verifies the same-user native OS peer and descriptor ownership
    before projecting unsigned JSON-RPC state notifications into this cache.
    Generated state validation is defense in depth, not a substitute for the
    transport's peer authentication. A new connection or disconnect
    synchronously invalidates its predecessor.
    """

    def __init__(self) -> None:
        self._lock = threading.RLock()
        self._binding: StatusBinding | None = None
        self._snapshot: _StatusSnapshot | None = None
        self._generation = 0
        self._revision = 0

    @property
    def active_binding(self) -> StatusBinding | None:
        """Read the active stream capability without waiting for a writer."""

        return self._binding

    def connect(self, *, epoch: str, pid: int, session_id: str) -> StatusBinding:
        """Invalidate prior observations and mint one unique connection binding."""

        if (
            type(epoch) is not str
            or _STREAM_IDENTIFIER.fullmatch(epoch) is None
            or type(pid) is not int
            or not 0 < pid <= _MAXIMUM_NATIVE_OWNER_PID
            or type(session_id) is not str
            or _STREAM_IDENTIFIER.fullmatch(session_id) is None
        ):
            raise ValueError("native status owner identity is malformed")

        with self._lock:
            if self._generation >= RECORDING_CONTROL_SAFE_INTEGER_MAX:
                raise OverflowError("native status connection generation is exhausted")
            self._generation += 1
            binding = StatusBinding(epoch, pid, session_id, self._generation)
            self._snapshot = None
            self._revision = 0
            self._binding = binding

        return binding

    def publish(
        self,
        binding: StatusBinding,
        status: Mapping[str, object],
        *,
        revision: int | None = None,
    ) -> bool:
        """Publish a bounded response only for its exact live stream session."""

        if self._binding is not binding:
            return False
        payload = self._validated_payload(status, owner_pid=binding.pid)
        if payload is None:
            return False

        with self._lock:
            if self._binding is not binding:
                return False
            next_revision = self._revision + 1 if revision is None else revision
            if (
                type(next_revision) is not int
                or not self._revision < next_revision <= RECORDING_CONTROL_SAFE_INTEGER_MAX
            ):
                return False
            self._snapshot = _StatusSnapshot(binding, next_revision, payload)
            self._revision = next_revision

        return True

    def latest(self, binding: StatusBinding | None = None) -> dict[str, object] | None:
        """Return an isolated snapshot without locks, IPC, polling, or refresh."""

        active = self._binding
        snapshot = self._snapshot
        if (
            active is None
            or (binding is not None and active is not binding)
            or snapshot is None
            or snapshot.binding is not active
        ):
            return None

        result = copy.deepcopy(snapshot.payload)
        if self._binding is not active or self._snapshot is not snapshot:
            return None
        return result

    def disconnect(self, binding: StatusBinding | None = None) -> None:
        """Synchronously revoke only the current authenticated stream session."""

        with self._lock:
            active = self._binding
            if active is None or (binding is not None and active is not binding):
                return
            self._binding = None
            self._snapshot = None
            self._revision = 0

    @staticmethod
    def _validated_payload(
        status: Mapping[str, object],
        *,
        owner_pid: int,
    ) -> dict[str, object] | None:
        if (
            not is_json(status)
            or status.get("ok") is not True
            or not is_recording_status_response(status)
            or "localCalendar" in status
        ):
            return None
        if "companionPid" in status and (
            type(status["companionPid"]) is not int or status["companionPid"] != owner_pid
        ):
            return None
        state = status["state"] if "state" in status else None
        if not is_json(state):
            return None
        if "schemaVersion" in status and (
            "schemaVersion" not in state or status["schemaVersion"] != state["schemaVersion"]
        ):
            return None

        try:
            if not is_json_value(status):
                return None
            encoded = json.dumps(
                status,
                ensure_ascii=True,
                allow_nan=False,
                separators=(",", ":"),
            ).encode("utf-8")
            if len(encoded) > _MAXIMUM_STATUS_SNAPSHOT_BYTES:
                return None
            decoded: object = json.loads(encoded)
        except (OverflowError, RecursionError, TypeError, ValueError):
            return None
        return decoded if is_json(decoded) else None


STATUS_CACHE = NativeStatusCache()


def native_status_cache() -> NativeStatusCache:
    """Return the process-local cache shared by transport and control clients."""

    return STATUS_CACHE
