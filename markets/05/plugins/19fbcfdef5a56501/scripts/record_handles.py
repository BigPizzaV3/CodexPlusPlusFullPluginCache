#!/usr/bin/env python3
"""Bounded account-scoped authorization for public Record identifiers."""

from __future__ import annotations

import hmac
import re
import threading
import time
from collections import OrderedDict
from dataclasses import dataclass
from typing import Callable

PUBLIC_MEETING_ID_PATTERN = re.compile(r"[A-Za-z0-9_-]{1,512}")
PUBLIC_CALENDAR_EVENT_ID_PATTERN = re.compile(r"[^\x00-\x1f\x7f]{1,512}")
DEFAULT_HANDLE_TTL_SECONDS = 60 * 60.0
DEFAULT_MAXIMUM_HANDLES = 512


class RecordHandleError(RuntimeError):
    """A public identifier is unknown, expired, or account-mismatched."""


@dataclass(frozen=True, repr=False)
class _AuthorizedIdentifier:
    raw_id: str
    account_fingerprint: bytes
    expires_at: float
    source: str | None = None


def public_meeting_id(raw_meeting_id: str) -> str:
    """Validate and return the public backend meeting identifier unchanged.

    Args:
        raw_meeting_id: Public Record meeting identifier.

    Returns:
        The original, validated meeting identifier.
    """

    if PUBLIC_MEETING_ID_PATTERN.fullmatch(raw_meeting_id) is None:
        raise ValueError("raw meeting id is invalid")
    return raw_meeting_id


def public_calendar_event_id(raw_event_id: str) -> str:
    """Validate and return the public Calendar event identifier unchanged.

    Args:
        raw_event_id: Public Record Calendar event identifier.

    Returns:
        The original, validated Calendar event identifier.
    """

    if PUBLIC_CALENDAR_EVENT_ID_PATTERN.fullmatch(raw_event_id) is None:
        raise ValueError("raw event id is invalid")
    return raw_event_id


class _AccountScopedIdentifierRegistry:
    def __init__(
        self,
        *,
        handle_for: Callable[[str], str],
        pattern: re.Pattern[str],
        refresh_error: str,
        ttl_seconds: float,
        maximum_handles: int,
        clock: Callable[[], float],
    ) -> None:
        if isinstance(ttl_seconds, bool):
            raise ValueError("ttl_seconds is invalid")
        if not 1 <= float(ttl_seconds) <= 24 * 60 * 60:
            raise ValueError("ttl_seconds is out of range")
        if isinstance(maximum_handles, bool) or not 1 <= maximum_handles <= 4096:
            raise ValueError("maximum_handles is out of range")
        self._handle_for = handle_for
        self._pattern = pattern
        self._refresh_error = refresh_error
        self._ttl_seconds = float(ttl_seconds)
        self._maximum_handles = maximum_handles
        self._clock = clock
        self._lock = threading.Lock()
        self._entries: OrderedDict[str, _AuthorizedIdentifier] = OrderedDict()

    def register(
        self,
        raw_id: str,
        *,
        account_fingerprint: bytes,
        source: str | None = None,
    ) -> str:
        if len(account_fingerprint) != 32:
            raise ValueError("account fingerprint is invalid")
        handle = self._handle_for(raw_id)
        with self._lock:
            now = self._clock()
            self._prune_locked(now)
            self._entries[handle] = _AuthorizedIdentifier(
                raw_id=raw_id,
                account_fingerprint=account_fingerprint,
                expires_at=now + self._ttl_seconds,
                source=source,
            )
            self._entries.move_to_end(handle)
            while len(self._entries) > self._maximum_handles:
                self._entries.popitem(last=False)
        return handle

    def resolve(self, handle: str, *, account_fingerprint: bytes) -> str:
        return self._resolve_entry(handle, account_fingerprint=account_fingerprint).raw_id

    def resolve_source(self, handle: str, *, account_fingerprint: bytes) -> str | None:
        """Return internal source metadata pinned when the handle was registered."""

        return self._resolve_entry(handle, account_fingerprint=account_fingerprint).source

    def _resolve_entry(
        self,
        handle: str,
        *,
        account_fingerprint: bytes,
    ) -> _AuthorizedIdentifier:
        if self._pattern.fullmatch(handle) is None or len(account_fingerprint) != 32:
            raise RecordHandleError(self._refresh_error)
        with self._lock:
            now = self._clock()
            self._prune_locked(now)
            entry = self._entries.get(handle)
            if entry is None or not hmac.compare_digest(
                entry.account_fingerprint,
                account_fingerprint,
            ):
                raise RecordHandleError(self._refresh_error)
            self._entries[handle] = _AuthorizedIdentifier(
                raw_id=entry.raw_id,
                account_fingerprint=entry.account_fingerprint,
                expires_at=now + self._ttl_seconds,
                source=entry.source,
            )
            self._entries.move_to_end(handle)
            return self._entries[handle]

    def _prune_locked(self, now: float) -> None:
        expired = [handle for handle, entry in self._entries.items() if entry.expires_at <= now]
        for handle in expired:
            self._entries.pop(handle, None)


class AccountScopedMeetingRegistry(_AccountScopedIdentifierRegistry):
    """Keep public meeting identifiers bounded and account-authorized."""

    def __init__(
        self,
        *,
        ttl_seconds: float = DEFAULT_HANDLE_TTL_SECONDS,
        maximum_handles: int = DEFAULT_MAXIMUM_HANDLES,
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        super().__init__(
            handle_for=public_meeting_id,
            pattern=PUBLIC_MEETING_ID_PATTERN,
            refresh_error="Meeting details must be refreshed.",
            ttl_seconds=ttl_seconds,
            maximum_handles=maximum_handles,
            clock=clock,
        )


class AccountScopedCalendarEventRegistry(_AccountScopedIdentifierRegistry):
    """Keep public Calendar identifiers bounded and account-authorized."""

    def __init__(
        self,
        *,
        ttl_seconds: float = DEFAULT_HANDLE_TTL_SECONDS,
        maximum_handles: int = DEFAULT_MAXIMUM_HANDLES,
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        super().__init__(
            handle_for=public_calendar_event_id,
            pattern=PUBLIC_CALENDAR_EVENT_ID_PATTERN,
            refresh_error="Calendar must be refreshed.",
            ttl_seconds=ttl_seconds,
            maximum_handles=maximum_handles,
            clock=clock,
        )


MEETING_ID_REGISTRY = AccountScopedMeetingRegistry()
CALENDAR_EVENT_ID_REGISTRY = AccountScopedCalendarEventRegistry()


__all__ = [
    "MEETING_ID_REGISTRY",
    "CALENDAR_EVENT_ID_REGISTRY",
    "PUBLIC_MEETING_ID_PATTERN",
    "PUBLIC_CALENDAR_EVENT_ID_PATTERN",
    "AccountScopedMeetingRegistry",
    "AccountScopedCalendarEventRegistry",
    "RecordHandleError",
    "public_meeting_id",
    "public_calendar_event_id",
]
