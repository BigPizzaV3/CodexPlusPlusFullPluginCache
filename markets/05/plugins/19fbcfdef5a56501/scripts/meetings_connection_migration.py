"""Account-scoped single-flight for ensuring the Sheep Meetings connection."""

from __future__ import annotations

import threading
from collections.abc import Callable, Mapping
from concurrent.futures import CancelledError as FutureCancelledError
from concurrent.futures import Future
from concurrent.futures import TimeoutError as FutureTimeoutError
from typing import Literal, TypedDict

MEETINGS_CONNECTION_URL = "https://chatgpt.com/backend-api/aip/connectors/links/noauth"
MEETINGS_CONNECTOR_ID = "connector_openai_chatgpt_meetings"
MEETINGS_ACTIONS = ("get_profile", "find_all", "fetch")


def connection_request_body() -> dict[str, object]:
    return {
        "connector_id": MEETINGS_CONNECTOR_ID,
        "name": "Meetings",
        "action_names": list(MEETINGS_ACTIONS),
        "ensure_exists": True,
    }


def connection_is_active(link: Mapping[str, object]) -> bool:
    """Validate the ensure response without inferring workspace policy access."""
    return (
        isinstance(link.get("id"), str)
        and bool(link["id"])
        and link.get("connector_id") == MEETINGS_CONNECTOR_ID
        and link.get("auth_type") == "NONE"
        and link.get("auth_status") == "ACTIVE"
        and link.get("connector_status") in (None, "ENABLED")
    )


class ConnectionMigrationResult(TypedDict):
    status: Literal["connected", "unavailable"]


class ConnectionMigration:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._inflight: dict[bytes, Future[ConnectionMigrationResult]] = {}

    def ensure(
        self,
        owner: bytes,
        *,
        connect: Callable[[], bool],
        check_current: Callable[[], None],
    ) -> ConnectionMigrationResult:
        while True:
            check_current()
            with self._lock:
                future = self._inflight.get(owner)
                leader = future is None
                if future is None:
                    future = Future[ConnectionMigrationResult]()
                    self._inflight[owner] = future
            if leader:
                break
            try:
                while True:
                    check_current()
                    try:
                        result = future.result(timeout=0.05)
                        check_current()
                        return result
                    except FutureTimeoutError:
                        continue
            except FutureCancelledError:
                # A superseded caller cannot cancel another surface's migration.
                continue
        try:
            check_current()
            connected = connect()
            check_current()
            result: ConnectionMigrationResult = {
                "status": "connected" if connected else "unavailable",
            }
            future.set_result(result)
            return result
        except BaseException as error:
            try:
                check_current()
            except BaseException:
                with self._lock:
                    self._inflight.pop(owner, None)
                    future.cancel()
            else:
                future.set_exception(error)
            raise
        finally:
            with self._lock:
                if self._inflight.get(owner) is future:
                    self._inflight.pop(owner)
