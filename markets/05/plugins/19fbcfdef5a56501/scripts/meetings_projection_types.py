"""Shared typed projections for Meetings Calendar and Notes data."""

from __future__ import annotations

from typing import Literal, TypedDict

from meetings_api_client import RecordCalendarEventWire, RecordMeetingListItemWire


class SnapshotStateWire(TypedDict):
    """Bounded terminal state shared by app snapshot sections."""

    status: str


class _OptionalNotesPaginationWire(TypedDict, total=False):
    """Optional app-private Notes pagination markers."""

    lineageRestarted: Literal[True]


class NotesPaginationWire(_OptionalNotesPaginationWire):
    """Opaque Notes pagination state returned to the Meetings app."""

    accountScopeGeneration: str | None
    hasMore: bool
    nextPageToken: str | None
    truncated: bool
    resetRequired: bool


class _OptionalSnapshotSectionWire(TypedDict, total=False):
    """Legacy flat rows remain internal to compatibility-only projections."""

    upcoming: list[RecordCalendarEventWire]


class NotesSectionWire(_OptionalSnapshotSectionWire):
    """Complete Notes section returned to the Meetings app."""

    generatedAt: str | None
    notes: list[RecordMeetingListItemWire]
    snapshotSection: Literal["notes"]
    calendarAccountScopeGeneration: None
    calendarTruncated: bool
    calendarStale: bool
    recentRecording: None
    snapshotState: SnapshotStateWire
    notesPagination: NotesPaginationWire


class _OptionalCalendarSectionWire(_OptionalSnapshotSectionWire, total=False):
    """Absolute local-date metadata for app-owned Calendar requests."""

    calendarStartDate: str
    calendarEndDate: str
    eventsByDate: dict[str, list[RecordCalendarEventWire]]


class CalendarSectionWire(_OptionalCalendarSectionWire):
    """Complete Calendar section returned to the Meetings app."""

    generatedAt: str | None
    notes: list[RecordMeetingListItemWire]
    snapshotSection: Literal["calendar"]
    calendarAccountScopeGeneration: str | None
    calendarDayCount: int
    calendarDayOffset: int
    calendarTruncated: bool
    calendarStale: bool
    recentRecording: None
    snapshotState: SnapshotStateWire
    notesPagination: NotesPaginationWire


class HomeBootstrapWire(TypedDict):
    """Independently accepted native-cache sections for first paint."""

    calendar: CalendarSectionWire | None
    notes: NotesSectionWire | None
