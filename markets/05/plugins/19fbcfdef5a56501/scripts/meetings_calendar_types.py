"""Calendar wire types, validated views, and safe client failures."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Literal, TypedDict

RecordCalendarResponseStatus = Literal["accepted", "tentative", "unknown", "declined"]
RecordCalendarSource = Literal["google_calendar", "outlook_calendar"]


class _OptionalRecordCalendarEventWire(TypedDict, total=False):
    joinUrl: str | None
    source: RecordCalendarSource


class RecordCalendarEventWire(_OptionalRecordCalendarEventWire):
    """Provider-id-free upcoming event returned to the Meetings app."""

    id: str
    title: str
    startTime: str
    endTime: str
    responseStatus: RecordCalendarResponseStatus


class RecordCalendarError(RuntimeError):
    """Base class whose messages are safe for local diagnostics."""


class RecordCalendarAuthError(RecordCalendarError):
    """The Calendar API rejected both normal and refreshed credentials."""


class RecordCalendarBackendError(RecordCalendarError):
    """The Calendar API was unavailable or returned an invalid bounded payload."""


class RecordCalendarRefreshDisabled(RecordCalendarBackendError):
    """Calendar refresh is paused by the server for this authenticated owner."""

    def __init__(self, retry_after_seconds: float | None = None) -> None:
        super().__init__("Meetings Calendar refresh is temporarily disabled.")
        self.retry_after_seconds = (
            retry_after_seconds
            if retry_after_seconds is not None
            and not isinstance(retry_after_seconds, bool)
            and math.isfinite(retry_after_seconds)
            and 0 < retry_after_seconds <= (2**53 - 1) / 1_000
            else 300.0
        )


class RecordCalendarNotConnected(RecordCalendarError):
    """The Calendar API confirmed that this account has no connector link."""


class RecordCalendarCancelled(RecordCalendarError):
    """The caller cancelled the Calendar request."""


@dataclass(frozen=True, repr=False)
class RecordCalendarEvent:
    """Minimal token- and provider-id-free DTO consumed by the Calendar UI."""

    id: str
    title: str
    start_time: str
    end_time: str
    response_status: RecordCalendarResponseStatus
    join_url: str | None = None
    source: RecordCalendarSource = "google_calendar"

    def as_widget_row(
        self,
        *,
        include_private_metadata: bool = False,
    ) -> RecordCalendarEventWire:
        """Serialize the event into the closed app-facing calendar contract.

        Args:
            include_private_metadata: Whether to include the validated meeting URL.

        Returns:
            The provider-id-free upcoming event consumed by the Meetings app.
        """

        row: RecordCalendarEventWire = {
            "id": self.id,
            "title": self.title,
            "startTime": self.start_time,
            "endTime": self.end_time,
            "responseStatus": self.response_status,
        }
        if include_private_metadata:
            row["joinUrl"] = self.join_url
        if self.source != "google_calendar":
            row["source"] = self.source
        return row


@dataclass(frozen=True, repr=False)
class RecordCalendarView:
    """One complete bounded Calendar window, never a backend cursor page."""

    events: tuple[RecordCalendarEvent, ...]
    account_scope_generation: str
    day_count: int
    day_offset: int
    generated_at: str
    truncated: bool
    stale: bool
