"""Account-bound Home first paint from the authenticated companion v2 RPC."""

from __future__ import annotations

import hmac
import json
import threading
from collections.abc import Callable
from datetime import date, datetime, timedelta, timezone
from urllib.parse import urlsplit

import meetings_mcp
from codex_auth_client import AuthMaterial, chatgpt_auth_subject
from companion_client import companion_client
from companion_control_v2 import CalendarSnapshot, HomeSnapshot, NotesSnapshot
from control_protocol import ControlUnavailable
from meetings_api_client import (
    RecordCalendarEvent,
    RecordCalendarResponseStatus,
    RecordMeetingNote,
    RecordReadSource,
    parse_record_meeting_row,
)
from meetings_api_client_common import record_account_fingerprint, record_owner_scope_fingerprint
from meetings_mcp_projection import project_calendar_events_by_date
from meetings_metrics import record_private_note_cache_outcome
from meetings_projection_types import CalendarSectionWire, HomeBootstrapWire, NotesSectionWire
from record_handles import public_calendar_event_id

_HOME_NOTES_LIMIT = 20


def read_home_bootstrap(
    *,
    cancellation_event: threading.Event | None,
    on_verified_owner: Callable[[AuthMaterial], None] | None = None,
    notes_limit: int = _HOME_NOTES_LIMIT,
    notes_max_age: timedelta | None = None,
) -> HomeBootstrapWire:
    """Read independently validated Calendar and Notes from the companion.

    Args:
        cancellation_event: Optional cancellation for this Home bootstrap only.
        on_verified_owner: Optional callback for the final verified account owner.
        notes_limit: Maximum number of cached notes to project.
        notes_max_age: Optional freshness bound on the companion's fetch timestamp.

    Returns:
        Bounded app-private Calendar and Notes sections, or null rejected sections.
    """

    empty = HomeBootstrapWire(calendar=None, notes=None)
    _raise_if_cancelled(cancellation_event)
    auth_manager = meetings_mcp.get_process_auth_manager()
    try:
        auth_before = auth_manager.get_chatgpt_auth(
            refresh_token=False,
            cancellation_event=cancellation_event,
        )
    except meetings_mcp.CodexAuthCancelled:
        raise
    except (meetings_mcp.CodexAuthRequired, meetings_mcp.CodexAuthError):
        _log_rejection("mcp-auth")
        return empty

    owner_scope = record_owner_scope_fingerprint(auth_before)
    if owner_scope is None:
        _log_rejection("account-scope")
        return empty

    try:
        client = companion_client(cancellation_event=cancellation_event)
        native_state = client.latest_state()
        if (
            native_state is None
            or native_state["accountScopeFingerprint"] is None
            or not hmac.compare_digest(native_state["accountScopeFingerprint"], owner_scope)
        ):
            _log_rejection("account-scope")
            record_private_note_cache_outcome("rejected")
            return empty
        private_notes_cache_supported = "home.notes-source.v1" in client.negotiated_capabilities
        snapshot = client.home_snapshot(
            owner_scope,
            notes_source="private-notes" if private_notes_cache_supported else None,
            cancellation_event=cancellation_event,
        )
    except ControlUnavailable:
        _raise_if_cancelled(cancellation_event)
        _log_rejection("companion-snapshot")
        record_private_note_cache_outcome("rejected")
        return empty

    _raise_if_cancelled(cancellation_event)
    auth_after = auth_manager.peek_cached_chatgpt_auth()
    if (
        auth_after is None
        or auth_after.subject is None
        or auth_after.account_id != auth_before.account_id
        or auth_after.subject != auth_before.subject
        or chatgpt_auth_subject(auth_after) != auth_after.subject
        or record_owner_scope_fingerprint(auth_after) != owner_scope
    ):
        _log_rejection("account-changed")
        record_private_note_cache_outcome("rejected")
        return empty

    account_fingerprint = record_account_fingerprint(auth_after)
    projected = HomeBootstrapWire(calendar=None, notes=None)
    if snapshot["calendar"] is not None:
        try:
            projected["calendar"] = _project_calendar(
                snapshot["calendar"],
                account_fingerprint=account_fingerprint,
                owner_scope=owner_scope,
                cancellation_event=cancellation_event,
            )
        except (OverflowError, OSError, TypeError, ValueError):
            _log_rejection("calendar-section")
    # Older companions can still seed Calendar while canonical Notes loads.
    # A source-aware companion may seed the exact Note-rooted ids selected for
    # this owner; canonical backend reads remain authoritative.
    if private_notes_cache_supported and snapshot["notes"] is not None:
        try:
            projected["notes"] = _project_notes(
                snapshot["notes"],
                snapshot=snapshot,
                read_source="note",
                limit=notes_limit,
                max_age=notes_max_age,
                account_fingerprint=account_fingerprint,
                cancellation_event=cancellation_event,
            )
        except (ValueError, meetings_mcp.RecordMeetingsBackendError):
            _log_rejection("notes-section")

    _raise_if_cancelled(cancellation_event)
    current_auth = auth_manager.peek_cached_chatgpt_auth()
    if current_auth is None or not hmac.compare_digest(
        account_fingerprint,
        record_account_fingerprint(current_auth),
    ):
        _log_rejection("account-changed")
        record_private_note_cache_outcome("rejected")
        return empty
    if on_verified_owner is not None:
        on_verified_owner(current_auth)
    accepted = sum(section is not None for section in projected.values())
    meetings_mcp.log_native_runtime_event(
        "home-snapshot",
        "accepted" if accepted == 2 else "partial" if accepted else "empty",
    )
    if not private_notes_cache_supported:
        record_private_note_cache_outcome("unsupported_companion")
    elif snapshot["notes"] is None:
        record_private_note_cache_outcome("cold_miss")
    elif projected["notes"] is None:
        record_private_note_cache_outcome("rejected")
    else:
        record_private_note_cache_outcome("hit")
    return projected


def _project_calendar(
    snapshot: CalendarSnapshot,
    *,
    account_fingerprint: bytes,
    owner_scope: str,
    cancellation_event: threading.Event | None,
) -> CalendarSectionWire:
    rows: list[tuple[str, RecordCalendarEvent]] = []
    observed_ids: set[str] = set()
    for event in snapshot["events"]:
        raw_id = event["id"]
        if raw_id in observed_ids:
            raise ValueError("companion Calendar contains duplicate events")
        observed_ids.add(raw_id)
        status: RecordCalendarResponseStatus = event["responseStatus"]
        start = datetime.fromtimestamp(event["startAtMillis"] / 1000, tz=timezone.utc)
        end = datetime.fromtimestamp(event["endAtMillis"] / 1000, tz=timezone.utc)
        meeting_url = event["meetingUrl"]
        if meeting_url is not None:
            parsed = urlsplit(meeting_url)
            if parsed.scheme != "https" or not parsed.hostname:
                raise ValueError("companion Calendar meeting URL is malformed")
        rows.append(
            (
                raw_id,
                RecordCalendarEvent(
                    id=public_calendar_event_id(raw_id),
                    title=event["title"],
                    start_time=start.isoformat().replace("+00:00", "Z"),
                    end_time=end.isoformat().replace("+00:00", "Z"),
                    response_status=status,
                    join_url=meeting_url,
                ),
            )
        )
    view = meetings_mcp.get_record_calendar_client().publish_cached_view(
        events=tuple(rows),
        day_count=1,
        day_offset=0,
        generated_at=snapshot["generatedAt"],
        truncated=snapshot["truncated"],
        stale=snapshot["stale"],
        account_fingerprint=account_fingerprint,
        owner_scope_fingerprint=owner_scope,
        cancellation_event=cancellation_event,
    )
    projected = meetings_mcp.project_calendar_view(
        view,
        day_count=1,
        day_offset=0,
        include_private_metadata=True,
    )
    today = date.today()
    start_date = today.isoformat()
    end_date = (today + timedelta(days=1)).isoformat()
    projected["calendarStartDate"] = start_date
    projected["calendarEndDate"] = end_date
    projected["eventsByDate"] = project_calendar_events_by_date(
        projected.pop("upcoming", []), start_date, end_date
    )
    return projected


def _project_notes(
    notes: NotesSnapshot,
    *,
    snapshot: HomeSnapshot,
    read_source: RecordReadSource,
    limit: int,
    max_age: timedelta | None,
    account_fingerprint: bytes,
    cancellation_event: threading.Event | None,
) -> NotesSectionWire:
    if max_age is not None:
        fetched_at = datetime.fromisoformat(notes["fetchedAt"].replace("Z", "+00:00"))
        if fetched_at.tzinfo is None or not (
            timedelta(0) <= datetime.now(timezone.utc) - fetched_at <= max_age
        ):
            raise ValueError("companion Notes are outside the freshness window")
    rows: list[tuple[str, RecordMeetingNote]] = []
    observed_ids: set[str] = set()
    for item in notes["items"]:
        source: dict[str, object] = {
            "id": item["id"],
            "title": item["title"],
            "recordingStartTime": item["startedAt"],
            "recordingEndTime": item["endedAt"],
            "status": item["status"],
            "isEmpty": item["isEmpty"],
            "numShareRecipients": item["numShareRecipients"],
        }
        if "recordSource" in item:
            source["recordSource"] = item["recordSource"]
        if "devicePlatform" in item:
            source["devicePlatform"] = item["devicePlatform"]
        if "summaryPageId" in item:
            source["summaryPageId"] = item["summaryPageId"]
        parsed = parse_record_meeting_row(source)
        if parsed is None:
            raise ValueError("companion Note is malformed")
        raw_id, note = parsed
        if raw_id in observed_ids:
            raise ValueError("companion Notes contain duplicate identifiers")
        observed_ids.add(raw_id)
        rows.append((raw_id, note))
    response_bytes = len(
        json.dumps(snapshot, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    )
    page = meetings_mcp.get_record_meetings_client().hydrate_cached_page(
        rows=tuple(rows[:limit]),
        next_cursor=None,
        has_more=False,
        truncated=False,
        initial_limit=limit,
        account_fingerprint=account_fingerprint,
        response_bytes=response_bytes,
        read_source=read_source,
        cancellation_event=cancellation_event,
    )
    return meetings_mcp.project_meetings_page(
        page,
        generated_at=notes["fetchedAt"],
        continuation_request=False,
    )


def _raise_if_cancelled(cancellation_event: threading.Event | None) -> None:
    if cancellation_event is not None and cancellation_event.is_set():
        raise meetings_mcp.CodexAuthCancelled("Home bootstrap was cancelled.")


def _log_rejection(reason: str) -> None:
    meetings_mcp.log_native_runtime_event("home-snapshot", "rejected", error_kind=reason)
