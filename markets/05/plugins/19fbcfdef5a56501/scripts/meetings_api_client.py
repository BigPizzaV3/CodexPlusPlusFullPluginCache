#!/usr/bin/env python3
"""Bounded authenticated API clients for the ChatGPT Meetings app."""

from __future__ import annotations

import hashlib
import hmac
import json
import logging
import math
import re
import secrets
import sys
import threading
import time
import urllib.parse
from collections.abc import Mapping
from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from http.client import HTTPException
from pathlib import Path
from typing import Callable, Literal, TypedDict, overload

from codex_auth_client import (
    AuthMaterial,
    ChatGPTAuthProvider,
    CodexAuthError,
    get_process_auth_manager,
    refresh_chatgpt_auth_after_unauthorized,
)
from meetings_analytics import PluginAnalyticsEvent
from meetings_api_client_common import (
    bounded_timeout_seconds,
    nonempty_string,
    project_meeting_title,
    record_account_fingerprint,
    record_owner_scope_fingerprint,
)
from meetings_api_client_common import (
    record_request_headers as record_request_headers,
)
from meetings_api_client_transport import (
    CONTINUATION_PAGE_LIMIT,
    MAXIMUM_CURSOR_BYTES,
    MAXIMUM_INITIAL_PAGE_LIMIT,
    MAXIMUM_PAGE_RESPONSE_BYTES,
    MINIMUM_INITIAL_PAGE_LIMIT,
    RECORD_MEETINGS_URL,
    RECORD_NOTES_URL,
    STATSIG_BOOTSTRAP_URL,
    HTTPSRecordTransport,
    RecordHTTPResult,
    RecordHTTPTransport,
    RecordRateLimitBudget,
    RecordTransportBackendError,
    RecordTransportCancelled,
    RecordTransportRateLimited,
    RecordTransportTimeout,
    authenticated_record_request,
)
from meetings_calendar_types import (
    RecordCalendarAuthError,
    RecordCalendarBackendError,
    RecordCalendarCancelled,
    RecordCalendarError,
    RecordCalendarEvent,
    RecordCalendarEventWire,
    RecordCalendarRefreshDisabled,
    RecordCalendarResponseStatus,
    RecordCalendarView,
)
from meetings_calendar_types import (
    RecordCalendarNotConnected as RecordCalendarNotConnected,
)
from meetings_calendar_types import (
    RecordCalendarSource as RecordCalendarSource,
)
from meetings_client_policy import (
    CachedAuthProvider as _CachedAuthProvider,
)
from meetings_client_policy import (
    MeetingsClientPolicies,
    statsig_gate_enabled,
)
from meetings_client_policy import (
    PluginClientContext as PluginClientContext,
)
from meetings_client_policy import (
    PluginClientPolicy as PluginClientPolicy,
)
from meetings_client_policy import (
    RequiredUpdate as RequiredUpdate,
)
from meetings_client_policy import (
    ServiceCapacity as ServiceCapacity,
)
from meetings_client_policy import (
    decode_statsig_payload as _decode_statsig_payload,
)
from meetings_connection_migration import (
    ConnectionMigration,
    ConnectionMigrationResult,
    connection_is_active,
    connection_request_body,
)
from meetings_metrics import measure_notes_lookup_stage
from meetings_note_status import (
    RecordMeetingFetchStatus as _RecordMeetingFetchStatus,
)
from meetings_note_status import (
    project_fetch_status as _project_fetch_status,
)
from meetings_note_status import (
    project_list_status as _project_list_status,
)
from meetings_note_status import (
    project_processing_stage as _project_processing_stage,
)
from meetings_note_status import (
    project_status as _project_status,
)
from meetings_sentry import (
    capture_feedback_diagnostic_scope,
    report_mcp_error,
    submit_feedback_diagnostics,
)
from meetings_settings import (
    AutomationPolicy,
    CalendarConnectionsWire,
    ContextConnectionsWire,
    HostedSettingName,
    HostedSettings,
    OnboardingProfileWire,
    project_app_connections,
)
from record_handles import (
    CALENDAR_EVENT_ID_REGISTRY,
    MEETING_ID_REGISTRY,
    PUBLIC_MEETING_ID_PATTERN,
    AccountScopedCalendarEventRegistry,
    AccountScopedMeetingRegistry,
    RecordHandleError,
    public_calendar_event_id,
    public_meeting_id,
)
from record_meeting_interaction_types import (
    MeetingsActivityWire,
    RecordMeetingDeleteWire,
    RecordMeetingFeedbackWire,
    RecordMeetingNoteStatus,
    RecordMeetingNoteWire,
    RecordMeetingPersonWire,
    RecordMeetingProcessingStage,
    RecordMeetingRenderedTranscriptRowWire,
    RecordMeetingReprocessWire,
    RecordMeetingShareEligibilityMemberWire,
    RecordMeetingShareEligibilityWire,
    RecordMeetingShareRecipientWire,
    RecordMeetingShareWire,
    RecordMeetingTranscriptEntryWire,
    RecordMeetingTranscriptStatus,
    RecordMeetingTranscriptWire,
)

from helpers import (
    ACCOUNT_SCOPE_GENERATION_PATTERN,
    account_scope_generation,
    is_json,
    is_json_array,
    local_day_bounds,
    unique_json_object,
)

# Calendar API

RECORD_CALENDAR_EVENTS_URL = "https://chatgpt.com/backend-api/meetings/calendar/events"
CALENDAR_PAGE_LIMIT = 200
MAXIMUM_CALENDAR_PAGES = 20
MAXIMUM_EVENTS = CALENDAR_PAGE_LIMIT * MAXIMUM_CALENDAR_PAGES
MAXIMUM_PROJECTED_EVENTS = 100
MAXIMUM_CALENDAR_TOTAL_RESPONSE_BYTES = 64 * 1024 * 1024
MAXIMUM_CALENDAR_CURSOR_BYTES = 8 * 1024
MAXIMUM_ENCODED_QUERY_BYTES = 32 * 1024
MAXIMUM_EVENT_ID_BYTES = 4 * 1024
MAXIMUM_CALENDAR_TIMESTAMP_BYTES = 128
_CALENDAR_ACCOUNT_SCOPE_DOMAIN = b"chatgpt-meetings-calendar-account-scope-v1\0"
_CALENDAR_OWNER_SCOPE_DOMAIN = b"chatgpt-meetings-calendar-owner-scope-v1\0"

DEFAULT_CALENDAR_TIMEOUT_SECONDS = 75.0
DEFAULT_DAY_OFFSET = 0
DEFAULT_DAY_COUNT = 1
_CALENDAR_REQUEST_TIMEOUT_MESSAGE = "Meetings Calendar request timed out."


@dataclass(frozen=True, repr=False)
class _ParsedPage:
    events: tuple[tuple[str, RecordCalendarEvent, datetime], ...]
    next_cursor: str | None
    generated_at: str
    response_bytes: int
    truncated: bool
    stale: bool


class RecordCalendarClient:
    """Fetch the server's bounded Calendar window from the authenticated backend.

    The window, backend cursors, account binding, and auth material remain
    process-local. The caller receives only the fully collected minimal DTO.
    """

    def __init__(
        self,
        auth_client: ChatGPTAuthProvider | None = None,
        *,
        handle_registry: AccountScopedCalendarEventRegistry = CALENDAR_EVENT_ID_REGISTRY,
        transport: RecordHTTPTransport | None = None,
        timeout_seconds: float = DEFAULT_CALENDAR_TIMEOUT_SECONDS,
        monotonic_clock: Callable[[], float] = time.monotonic,
        wall_clock: Callable[[], datetime] | None = None,
    ) -> None:
        self._auth_client = auth_client or get_process_auth_manager()
        self._handle_registry = handle_registry
        self._transport: RecordHTTPTransport = transport or HTTPSRecordTransport()
        self._timeout_seconds = bounded_timeout_seconds(timeout_seconds)
        self._monotonic_clock = monotonic_clock
        self._wall_clock = wall_clock or (lambda: datetime.now(timezone.utc))
        self._account_scope_secret = secrets.token_bytes(32)
        self._refresh_lock = threading.Lock()
        self._refresh_owner: tuple[bytes, str | None] | None = None
        self._refresh_generation = 0
        self._refresh_disabled_until = 0.0

    def account_scope_generation(
        self, fingerprint: bytes, *, owner_scope_fingerprint: str | None = None
    ) -> str:
        """Expose one opaque Calendar generation bound to the authenticated owner."""

        if (owner := owner_scope_fingerprint) is not None:
            if re.fullmatch(r"[a-f0-9]{64}", owner) is None:
                raise ValueError("Calendar owner scope fingerprint is invalid")
            fingerprint = hashlib.sha256(fingerprint + bytes.fromhex(owner)).digest()
        domain = _CALENDAR_OWNER_SCOPE_DOMAIN if owner else _CALENDAR_ACCOUNT_SCOPE_DOMAIN
        return account_scope_generation(self._account_scope_secret, fingerprint, domain=domain)

    def list_upcoming(
        self,
        *,
        day_offset: int = DEFAULT_DAY_OFFSET,
        day_count: int = DEFAULT_DAY_COUNT,
        refresh: bool = False,
        auth_client: ChatGPTAuthProvider | None = None,
        cancellation_event: threading.Event | None = None,
    ) -> RecordCalendarView:
        """Return one stable, deduplicated allowlisted local Calendar window."""

        _raise_if_calendar_cancelled(cancellation_event)
        if not _valid_day_window(day_offset, day_count):
            raise ValueError("Calendar day window is invalid.")
        if type(refresh) is not bool:
            raise ValueError("Calendar refresh must be a boolean.")
        if refresh and day_count != DEFAULT_DAY_COUNT:
            raise ValueError("Calendar source refresh requires a single selected day.")
        now = _normalized_now(self._wall_clock())
        window_min, window_max = local_day_bounds(
            now,
            day_offset,
            day_count,
        )
        time_min = _format_timestamp(window_min)
        time_max = _format_timestamp(window_max)
        deadline = self._monotonic_clock() + self._timeout_seconds

        request_auth_client = auth_client or self._auth_client
        auth = request_auth_client.get_chatgpt_auth(
            refresh_token=False,
            cancellation_event=cancellation_event,
        )
        account_fingerprint = record_account_fingerprint(auth)
        owner_scope_fingerprint = record_owner_scope_fingerprint(auth)
        with self._refresh_lock:
            owner = (account_fingerprint, owner_scope_fingerprint)
            if self._refresh_owner != owner:
                self._refresh_owner = owner
                self._refresh_generation += 1
                self._refresh_disabled_until = 0.0
            refresh_generation = self._refresh_generation
            remaining_pause = (
                self._refresh_disabled_until - self._monotonic_clock()
                if self._refresh_disabled_until
                else 0.0
            )
            if remaining_pause > 0:
                raise RecordCalendarRefreshDisabled(remaining_pause)
        account_scope_generation_value = self.account_scope_generation(
            account_fingerprint, owner_scope_fingerprint=owner_scope_fingerprint
        )
        refreshed = False
        cursor: str | None = None
        seen_cursors: set[str] = set()
        seen_event_ids: set[tuple[RecordCalendarSource, str]] = set()
        projected: list[tuple[datetime, str, RecordCalendarEvent]] = []
        expected_generated_at: str | None = None
        total_response_bytes = 0
        backend_truncated = False
        backend_stale = False

        for page_index in range(MAXIMUM_CALENDAR_PAGES):
            result, auth, refreshed = self._request_with_refresh(
                auth,
                account_fingerprint=account_fingerprint,
                owner_scope_fingerprint=owner_scope_fingerprint,
                refresh_generation=refresh_generation,
                refreshed=refreshed,
                account_changed_message=(
                    "ChatGPT account changed during Calendar refresh."
                    if refresh
                    else "ChatGPT account changed during Calendar query."
                ),
                url=_calendar_page_url(
                    time_min=time_min,
                    time_max=time_max,
                    cursor=cursor,
                    refresh=refresh and cursor is None,
                ),
                deadline=deadline,
                auth_client=request_auth_client,
                cancellation_event=cancellation_event,
            )

            page = _parse_page(
                result.body,
                window_min=window_min,
                window_max=window_max,
            )
            # The backend sets ``truncated`` whenever this page has a cursor,
            # in addition to durable source-sync truncation. Only the terminal
            # page distinguishes a fully drained query from an incomplete
            # source window; local page/projection caps are added separately.
            backend_truncated = page.truncated
            backend_stale = backend_stale or page.stale
            total_response_bytes += page.response_bytes
            if total_response_bytes > MAXIMUM_CALENDAR_TOTAL_RESPONSE_BYTES:
                raise RecordCalendarBackendError("Meetings Calendar returned too much data.")
            if expected_generated_at is None:
                expected_generated_at = page.generated_at
            elif not hmac.compare_digest(
                page.generated_at.encode("utf-8"),
                expected_generated_at.encode("utf-8"),
            ):
                raise RecordCalendarBackendError("Meetings Calendar changed during pagination.")
            for raw_id, event, start_instant in page.events:
                event_identity = (event.source, raw_id)
                if event_identity in seen_event_ids:
                    continue
                seen_event_ids.add(event_identity)
                if len(seen_event_ids) > MAXIMUM_EVENTS:
                    raise RecordCalendarBackendError("Meetings Calendar returned too many events.")
                projected.append((start_instant, raw_id, event))

            next_cursor = page.next_cursor
            if next_cursor is None:
                return _finalize_view(
                    projected,
                    now=now,
                    account_scope_generation=account_scope_generation_value,
                    day_count=day_count,
                    day_offset=day_offset,
                    generated_at=expected_generated_at,
                    truncated=backend_truncated,
                    stale=backend_stale,
                    account_fingerprint=account_fingerprint,
                    handle_registry=self._handle_registry,
                    cancellation_event=cancellation_event,
                )
            if next_cursor in seen_cursors:
                raise RecordCalendarBackendError("Meetings Calendar pagination did not advance.")
            seen_cursors.add(next_cursor)
            cursor = next_cursor
            if page_index + 1 >= MAXIMUM_CALENDAR_PAGES:
                return _finalize_view(
                    projected,
                    now=now,
                    account_scope_generation=account_scope_generation_value,
                    day_count=day_count,
                    day_offset=day_offset,
                    generated_at=expected_generated_at,
                    truncated=True,
                    stale=backend_stale,
                    account_fingerprint=account_fingerprint,
                    handle_registry=self._handle_registry,
                    cancellation_event=cancellation_event,
                )

        raise RecordCalendarBackendError("Meetings Calendar returned too many pages.")

    def publish_cached_view(
        self,
        *,
        events: tuple[tuple[str, RecordCalendarEvent], ...],
        day_count: int,
        day_offset: int,
        generated_at: str,
        truncated: bool,
        stale: bool,
        account_fingerprint: bytes,
        owner_scope_fingerprint: str | None = None,
        cancellation_event: threading.Event | None = None,
    ) -> RecordCalendarView:
        """Hydrate one private native Calendar view into the ordinary registry."""

        _raise_if_calendar_cancelled(cancellation_event)
        if not _valid_day_window(day_offset, day_count):
            raise ValueError("cached Calendar day window is invalid")
        if (
            len(account_fingerprint) != 32
            or _timestamp_instant(generated_at) is None
            or len(events) > MAXIMUM_PROJECTED_EVENTS
        ):
            raise ValueError("cached Calendar view is invalid")

        seen_raw_ids: set[str] = set()
        projected: list[RecordCalendarEvent] = []
        for raw_event_id, event in events:
            if (
                nonempty_string(
                    raw_event_id,
                    maximum_bytes=MAXIMUM_EVENT_ID_BYTES,
                )
                != raw_event_id
                or raw_event_id in seen_raw_ids
                or event.id != public_calendar_event_id(raw_event_id)
            ):
                raise ValueError("cached Calendar event is invalid")
            seen_raw_ids.add(raw_event_id)
            handle = self._handle_registry.register(
                raw_event_id,
                account_fingerprint=account_fingerprint,
            )
            if handle != event.id:
                raise ValueError("cached Calendar event id is invalid")
            projected.append(replace(event, id=handle))

        return RecordCalendarView(
            events=tuple(projected),
            account_scope_generation=self.account_scope_generation(
                account_fingerprint,
                owner_scope_fingerprint=owner_scope_fingerprint,
            ),
            day_count=day_count,
            day_offset=day_offset,
            generated_at=generated_at,
            truncated=truncated,
            stale=stale,
        )

    def _request_with_refresh(
        self,
        auth: AuthMaterial,
        *,
        account_fingerprint: bytes,
        owner_scope_fingerprint: str | None,
        refresh_generation: int,
        refreshed: bool,
        account_changed_message: str,
        url: str,
        deadline: float,
        auth_client: ChatGPTAuthProvider | None = None,
        cancellation_event: threading.Event | None,
    ) -> tuple[RecordHTTPResult, AuthMaterial, bool]:
        quota_budget = RecordRateLimitBudget()
        while True:
            _raise_if_calendar_cancelled(cancellation_event)
            remaining = deadline - self._monotonic_clock()
            if remaining <= 0:
                raise RecordCalendarBackendError(_CALENDAR_REQUEST_TIMEOUT_MESSAGE)
            try:
                result, auth = authenticated_record_request(
                    self._transport,
                    auth,
                    auth_client or self._auth_client,
                    url=url,
                    timeout_seconds=remaining,
                    cancellation_event=cancellation_event,
                    method="GET",
                    body=None,
                    quota_budget=quota_budget,
                )
            except RecordTransportCancelled:
                raise RecordCalendarCancelled("Meetings Calendar request was cancelled.") from None
            except RecordTransportTimeout:
                raise RecordCalendarBackendError(_CALENDAR_REQUEST_TIMEOUT_MESSAGE) from None
            except RecordTransportBackendError:
                raise RecordCalendarBackendError(
                    "Meetings Calendar could not be reached."
                ) from None
            _raise_if_calendar_cancelled(cancellation_event)
            oversized = len(result.body) > MAXIMUM_PAGE_RESPONSE_BYTES
            if result.status != 401:
                if result.status in {404, 503} and not oversized:
                    try:
                        payload: object = json.loads(
                            result.body, object_pairs_hook=unique_json_object
                        )
                    except (ValueError, UnicodeDecodeError, RecursionError):
                        payload = None
                    if (
                        result.status == 503
                        and is_json(payload)
                        and payload.get("detail") == "calendar_refresh_disabled"
                    ):
                        disabled = RecordCalendarRefreshDisabled(result.retry_after_seconds)
                        with self._refresh_lock:
                            # A late response cannot pause a replacement owner, including A-B-A.
                            if self._refresh_generation == refresh_generation:
                                self._refresh_disabled_until = max(
                                    self._refresh_disabled_until,
                                    self._monotonic_clock() + disabled.retry_after_seconds,
                                )
                        raise disabled
                    if (
                        result.status == 404
                        and is_json(payload)
                        and is_json(detail := payload.get("detail"))
                        and detail.get("code") == "calendar_not_connected"
                    ):
                        raise RecordCalendarNotConnected("Google Calendar is not connected.")
                if result.status < 200 or result.status >= 300:
                    raise RecordCalendarBackendError("Meetings Calendar returned a backend error.")
                if oversized:
                    raise RecordCalendarBackendError(
                        "Meetings Calendar returned an oversized response."
                    )
                return result, auth, refreshed
            if refreshed:
                raise RecordCalendarAuthError("ChatGPT authentication was rejected.")
            _raise_if_calendar_cancelled(cancellation_event)
            refreshed_auth = refresh_chatgpt_auth_after_unauthorized(
                auth_client or self._auth_client,
                auth,
                cancellation_event=cancellation_event,
            )
            if not hmac.compare_digest(
                record_account_fingerprint(refreshed_auth),
                account_fingerprint,
            ):
                raise RecordCalendarAuthError(account_changed_message)
            if owner_scope_fingerprint is not None and not hmac.compare_digest(
                record_owner_scope_fingerprint(refreshed_auth) or "",
                owner_scope_fingerprint,
            ):
                raise RecordCalendarAuthError(account_changed_message)
            auth = refreshed_auth
            refreshed = True


def _finalize_view(
    projected: list[tuple[datetime, str, RecordCalendarEvent]],
    *,
    now: datetime,
    account_scope_generation: str,
    day_count: int,
    day_offset: int,
    generated_at: str | None,
    truncated: bool,
    stale: bool,
    account_fingerprint: bytes,
    handle_registry: AccountScopedCalendarEventRegistry,
    cancellation_event: threading.Event | None,
) -> RecordCalendarView:
    _raise_if_calendar_cancelled(cancellation_event)
    if generated_at is None:
        raise RecordCalendarBackendError("Meetings Calendar returned an invalid generation.")
    projected.sort(key=lambda item: (item[0], item[1]))
    projection_truncated = len(projected) > MAXIMUM_PROJECTED_EVENTS
    ended: list[tuple[datetime, str, RecordCalendarEvent]] = []
    active_or_future: list[tuple[datetime, str, RecordCalendarEvent]] = []
    for item in projected:
        event_end = _timestamp_instant(item[2].end_time)
        if event_end is not None and event_end < now:
            ended.append(item)
        else:
            active_or_future.append(item)
    selected = active_or_future[:MAXIMUM_PROJECTED_EVENTS]
    remaining = MAXIMUM_PROJECTED_EVENTS - len(selected)
    if remaining:
        selected = ended[-remaining:] + selected
    selected.sort(key=lambda item: (item[0], item[1]))
    final_events: list[RecordCalendarEvent] = []
    for _start, raw_event_id, event in selected:
        handle = handle_registry.register(
            raw_event_id,
            account_fingerprint=account_fingerprint,
        )
        if handle != event.id:
            raise RecordCalendarBackendError("Meetings Calendar returned an invalid event id.")
        final_events.append(replace(event, id=handle))
    return RecordCalendarView(
        events=tuple(final_events),
        account_scope_generation=account_scope_generation,
        day_count=day_count,
        day_offset=day_offset,
        generated_at=generated_at,
        truncated=truncated or projection_truncated,
        stale=stale,
    )


def _normalized_now(value: datetime) -> datetime:
    if value.tzinfo is None:
        raise RecordCalendarBackendError("Meetings Calendar clock was unavailable.")
    try:
        return value.astimezone(timezone.utc)
    except (OverflowError, ValueError) as exc:
        raise RecordCalendarBackendError("Meetings Calendar clock was unavailable.") from exc


def _valid_day_window(day_offset: object, day_count: object) -> bool:
    if (
        isinstance(day_offset, bool)
        or not isinstance(day_offset, int)
        or isinstance(day_count, bool)
        or not isinstance(day_count, int)
    ):
        return False
    return day_count == DEFAULT_DAY_COUNT


def _format_timestamp(value: datetime) -> str:
    return value.isoformat(timespec="milliseconds").replace("+00:00", "Z")


def _calendar_page_url(
    *, time_min: str, time_max: str, cursor: str | None, refresh: bool = False
) -> str:
    query = [
        ("time_min", time_min),
        ("time_max", time_max),
        ("limit", str(CALENDAR_PAGE_LIMIT)),
    ]
    if cursor is not None:
        if not _valid_cursor(cursor):
            raise RecordCalendarBackendError("Meetings Calendar returned an invalid cursor.")
        query.append(("cursor", cursor))
    elif refresh:
        query.append(("refresh", "true"))
    encoded = urllib.parse.urlencode(query)
    if len(encoded.encode("utf-8")) > MAXIMUM_ENCODED_QUERY_BYTES:
        raise RecordCalendarBackendError("Meetings Calendar returned an invalid cursor.")
    return f"{RECORD_CALENDAR_EVENTS_URL}?{encoded}"


def _parse_page(
    body: bytes,
    *,
    window_min: datetime,
    window_max: datetime,
) -> _ParsedPage:
    try:
        payload: object = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, ValueError, RecursionError) as exc:
        raise RecordCalendarBackendError("Meetings Calendar returned an invalid response.") from exc
    if not is_json(payload):
        raise RecordCalendarBackendError("Meetings Calendar returned an invalid response.")
    rows = payload.get("events")
    if not is_json_array(rows) or len(rows) > CALENDAR_PAGE_LIMIT:
        raise RecordCalendarBackendError("Meetings Calendar returned an invalid page.")
    generated_at = _required_timestamp(payload.get("generatedAt"))
    if generated_at is None:
        raise RecordCalendarBackendError("Meetings Calendar returned an invalid generation.")
    truncated = payload.get("truncated")
    stale = payload.get("stale")
    if not isinstance(truncated, bool) or not isinstance(stale, bool):
        raise RecordCalendarBackendError("Meetings Calendar returned an invalid page.")
    events: list[tuple[str, RecordCalendarEvent, datetime]] = []
    for row in rows:
        parsed = _parse_event(
            row,
            window_min=window_min,
            window_max=window_max,
        )
        if parsed is not None:
            events.append(parsed)

    raw_cursor = payload.get("nextCursor")
    if raw_cursor is None:
        next_cursor = None
    elif isinstance(raw_cursor, str) and _valid_cursor(raw_cursor):
        next_cursor = raw_cursor
    else:
        raise RecordCalendarBackendError("Meetings Calendar returned an invalid cursor.")
    return _ParsedPage(
        events=tuple(events),
        next_cursor=next_cursor,
        generated_at=generated_at,
        response_bytes=len(body),
        truncated=truncated,
        stale=stale,
    )


def _parse_event(
    value: object,
    *,
    window_min: datetime,
    window_max: datetime,
) -> tuple[str, RecordCalendarEvent, datetime] | None:
    if not is_json(value):
        return None
    raw_id = nonempty_string(value.get("eventId"), maximum_bytes=MAXIMUM_EVENT_ID_BYTES)
    start = _required_timestamp(value.get("start"))
    if raw_id is None or start is None:
        return None
    end = _required_timestamp(value.get("end")) or start
    start_instant = _timestamp_instant(start)
    end_instant = _timestamp_instant(end)
    if start_instant is not None and end_instant is not None and end_instant < start_instant:
        end = start
        end_instant = start_instant
    if (
        start_instant is None
        or end_instant is None
        or start_instant < window_min
        or start_instant >= window_max
    ):
        return None
    title = project_meeting_title(value.get("title"))
    raw_source = value.get("source", "google_calendar")
    if raw_source not in ("google_calendar", "outlook_calendar"):
        return None
    source: RecordCalendarSource = raw_source
    return (
        raw_id,
        RecordCalendarEvent(
            id=public_calendar_event_id(raw_id),
            title=title,
            start_time=start,
            end_time=end,
            response_status=_project_response_status(value.get("responseStatus")),
            join_url=_project_join_url(value.get("meetingUrl")),
            source=source,
        ),
        start_instant,
    )


def _project_response_status(value: object) -> RecordCalendarResponseStatus:
    status = value.strip().lower() if isinstance(value, str) else ""
    if status == "accepted":
        return "accepted"
    if status == "tentative":
        return "tentative"
    if status == "declined":
        return "declined"
    return "unknown"


def _project_join_url(value: object) -> str | None:
    normalized = nonempty_string(value, maximum_bytes=2_048)
    if normalized is None:
        return None
    try:
        parsed = urllib.parse.urlsplit(normalized)
    except ValueError:
        return None
    if (
        parsed.scheme != "https"
        or not parsed.hostname
        or parsed.username is not None
        or parsed.password is not None
    ):
        return None
    return normalized


def _required_timestamp(value: object) -> str | None:
    normalized = nonempty_string(value, maximum_bytes=MAXIMUM_CALENDAR_TIMESTAMP_BYTES)
    if normalized is None or _timestamp_instant(normalized) is None:
        return None
    return normalized


def _timestamp_instant(value: str) -> datetime | None:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    try:
        return parsed.astimezone(timezone.utc)
    except (OverflowError, ValueError):
        return None


def _contains_control_character(value: str) -> bool:
    return any(ord(character) < 0x20 or ord(character) == 0x7F for character in value)


def _valid_cursor(value: str) -> bool:
    if not value or _contains_control_character(value):
        return False
    try:
        return len(value.encode("utf-8")) <= MAXIMUM_CALENDAR_CURSOR_BYTES
    except UnicodeEncodeError:
        return False


def _raise_if_calendar_cancelled(event: threading.Event | None) -> None:
    if event is not None and event.is_set():
        raise RecordCalendarCancelled("Meetings Calendar request was cancelled.")


# Notes API

DEFAULT_INITIAL_PAGE_LIMIT = 20
MAXIMUM_PAGES = 10
MAXIMUM_NOTES = 200
MAXIMUM_TOTAL_RESPONSE_BYTES = 64 * 1024 * 1024
MAXIMUM_ENCODED_CURSOR_BYTES = 16 * 1024
MAXIMUM_PAGE_TOKEN_BYTES = 128
MAXIMUM_CONTINUATION_ENTRIES = 64
CONTINUATION_TTL_SECONDS = 10 * 60.0
DEFAULT_NOTES_TIMEOUT_SECONDS = 30.0
MAXIMUM_TIMESTAMP_BYTES = 128
MEETING_ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]{1,512}$")
PAGE_TOKEN_PATTERN = re.compile(r"^[A-Za-z0-9_-]{32,128}$")
_NOTES_ACCOUNT_SCOPE_DOMAIN = b"chatgpt-meetings-notes-account-scope-v1\0"
RecordReadSource = Literal["meeting", "note"]
_NOTES_REQUEST_TIMEOUT_MESSAGE = "Meetings request timed out."


class _OptionalRecordMeetingListItemWire(TypedDict, total=False):
    processingStage: RecordMeetingProcessingStage
    resourceLink: str
    recordSource: str
    devicePlatform: Literal["ios", "android"]
    summaryPageId: str
    ccaWaitUntil: str
    sourceMeetingId: str
    sourceRecordingId: str
    recordingCorrelationPending: bool


class RecordMeetingListItemWire(_OptionalRecordMeetingListItemWire):
    """Token-free recent-note row returned to the Meetings app."""

    id: str
    title: str
    startTime: str
    endTime: str | None
    status: RecordMeetingNoteStatus
    fetchStatus: _RecordMeetingFetchStatus
    isEmpty: bool
    numShareRecipients: int


class RecordMeetingsError(RuntimeError):
    """Base class whose messages are safe for local diagnostics."""


class RecordMeetingsAuthError(RecordMeetingsError):
    """The Record API rejected both the normal and refreshed credential."""


RecordMeetingsBackendFailureKind = Literal[
    "timeout",
    "transport",
    "http_4xx",
    "http_429",
    "http_5xx",
    "invalid_response",
]


class RecordMeetingsBackendError(RecordMeetingsError):
    """A backend failure with bounded, content-free diagnostic classification."""

    def __init__(
        self,
        message: str,
        *,
        failure_kind: RecordMeetingsBackendFailureKind = "invalid_response",
        retryable: bool = False,
        retry_after_seconds: float | None = None,
    ) -> None:
        super().__init__(message)
        self.failure_kind: RecordMeetingsBackendFailureKind = failure_kind
        self.retryable: bool = retryable
        self.retry_after_seconds = retry_after_seconds


class RecordMeetingsCancelled(RecordMeetingsError):
    """The caller cancelled the Notes request."""


class RecordMeetingsPaginationResetRequired(RecordMeetingsError):
    """The opaque continuation can no longer be used for this account."""


@dataclass(frozen=True)
class RecordMeetingNote:
    """Minimal token-free DTO consumed by the Notes UI projection."""

    id: str
    title: str
    started_at: str
    ended_at: str | None
    status: RecordMeetingNoteStatus
    fetch_status: _RecordMeetingFetchStatus
    is_empty: bool
    num_share_recipients: int
    record_source: str | None = None
    device_platform: Literal["ios", "android"] | None = None
    source_meeting_id: str | None = None
    source_recording_id: str | None = None
    recording_correlation_pending: bool = False
    cca_wait_until: str | None = None
    summary_page_id: str | None = None
    processing_stage: RecordMeetingProcessingStage | None = None

    def as_widget_row(self) -> RecordMeetingListItemWire:
        """Serialize the note into the closed app-facing list-item contract.

        Returns:
            The token-free note row consumed by the Meetings app.
        """

        row: RecordMeetingListItemWire = {
            "id": self.id,
            "title": self.title,
            "startTime": self.started_at,
            "endTime": self.ended_at,
            "status": self.status,
            "fetchStatus": self.fetch_status,
            "isEmpty": self.is_empty,
            "numShareRecipients": self.num_share_recipients,
        }
        if self.record_source is not None:
            row["recordSource"] = self.record_source
        if self.recording_correlation_pending:
            row["recordingCorrelationPending"] = True
        if self.source_recording_id is not None:
            row["sourceRecordingId"] = self.source_recording_id
        if self.source_meeting_id is not None:
            row["sourceMeetingId"] = self.source_meeting_id
        if self.cca_wait_until is not None:
            row["ccaWaitUntil"] = self.cca_wait_until
        if self.summary_page_id is not None:
            row["summaryPageId"] = self.summary_page_id
        if self.processing_stage is not None:
            row["processingStage"] = self.processing_stage
        if self.device_platform is not None:
            row["devicePlatform"] = self.device_platform
        return row


@dataclass(frozen=True)
class RecordMeetingsPage:
    """One token-free Notes page plus an opaque local continuation handle."""

    notes: tuple[RecordMeetingNote, ...]
    read_source: RecordReadSource
    account_scope_generation: str
    has_more: bool
    next_page_token: str | None
    truncated: bool


@dataclass(frozen=True, repr=False)
class _FetchedBackendPage:
    rows: tuple[tuple[str, RecordMeetingNote], ...]
    next_cursor: str | None
    response_bytes: int
    account_fingerprint: bytes
    read_source: RecordReadSource


@dataclass(frozen=True, repr=False)
class _PaginationState:
    cursor: str | None
    seen_raw_ids: frozenset[str]
    seen_cursors: frozenset[str]
    page_count: int
    total_response_bytes: int
    account_fingerprint: bytes
    read_source: RecordReadSource
    buffered_rows: tuple[tuple[str, RecordMeetingNote], ...] = ()
    terminal_truncated: bool = False


@dataclass(frozen=True, repr=False)
class _ProjectedPage:
    notes: tuple[RecordMeetingNote, ...]
    read_source: RecordReadSource
    continuation_state: _PaginationState | None
    truncated: bool


@dataclass(repr=False)
class _ContinuationEntry:
    state: _PaginationState
    expires_at: float
    in_flight: bool = False
    replay: RecordMeetingsPage | None = None


class RecordMeetingsClient:
    """Fetch bounded Notes pages directly from the authenticated backend.

    Backend cursors and account lineage stay inside this process. Callers only
    receive random local continuation handles, which expire and are never
    persisted.
    """

    def __init__(
        self,
        auth_client: ChatGPTAuthProvider | None = None,
        *,
        handle_registry: AccountScopedMeetingRegistry = MEETING_ID_REGISTRY,
        transport: RecordHTTPTransport | None = None,
        timeout_seconds: float = DEFAULT_NOTES_TIMEOUT_SECONDS,
        clock: Callable[[], float] = time.monotonic,
        continuation_ttl_seconds: float = CONTINUATION_TTL_SECONDS,
        maximum_continuation_entries: int = MAXIMUM_CONTINUATION_ENTRIES,
        token_factory: Callable[[], str] | None = None,
    ) -> None:
        self._auth_client = auth_client or get_process_auth_manager()
        self._handle_registry = handle_registry
        self._transport: RecordHTTPTransport = transport or HTTPSRecordTransport()
        self._timeout_seconds = bounded_timeout_seconds(timeout_seconds)
        self._clock = clock
        if (
            isinstance(continuation_ttl_seconds, bool)
            or not math.isfinite(float(continuation_ttl_seconds))
            or not 1 <= float(continuation_ttl_seconds) <= 24 * 60 * 60
        ):
            raise ValueError("continuation_ttl_seconds is out of range")
        if (
            isinstance(maximum_continuation_entries, bool)
            or not 1 <= maximum_continuation_entries <= 1024
        ):
            raise ValueError("maximum_continuation_entries is out of range")
        self._continuation_ttl_seconds = float(continuation_ttl_seconds)
        self._maximum_continuation_entries = maximum_continuation_entries
        self._token_factory = token_factory or (lambda: secrets.token_urlsafe(32))
        self._account_scope_secret = secrets.token_bytes(32)
        self._continuation_lock = threading.Lock()
        self._continuations: dict[str, _ContinuationEntry] = {}

    def list_notes_page(
        self,
        *,
        initial_limit: int | None = None,
        page_token: str | None = None,
        recording_started_at: str | None = None,
        auth_client: ChatGPTAuthProvider | None = None,
        cancellation_event: threading.Event | None = None,
    ) -> RecordMeetingsPage:
        """Return one page; refresh auth only after one backend 401."""

        request_auth_client = auth_client or self._auth_client
        if page_token is not None:
            if initial_limit is not None or recording_started_at is not None:
                raise ValueError("initial_limit and page_token are mutually exclusive")
            return self._continue_notes_page(
                _validated_page_token(page_token),
                auth_client=request_auth_client,
                cancellation_event=cancellation_event,
            )

        limit = _validated_initial_limit(initial_limit)
        fetched = self._fetch_backend_page(
            limit=limit,
            cursor=None,
            recording_started_at=recording_started_at,
            read_source=None,
            expected_account_fingerprint=None,
            auth_client=request_auth_client,
            cancellation_event=cancellation_event,
        )
        projected = _project_backend_page(
            fetched,
            seen_raw_ids=frozenset(),
            seen_cursors=frozenset(),
            previous_page_count=0,
            previous_response_bytes=0,
        )
        return self._publish_initial_page(
            projected,
            account_scope_generation=account_scope_generation(
                self._account_scope_secret,
                fetched.account_fingerprint,
                domain=_NOTES_ACCOUNT_SCOPE_DOMAIN,
            ),
            cancellation_event=cancellation_event,
        )

    def hydrate_cached_page(
        self,
        *,
        rows: tuple[tuple[str, RecordMeetingNote], ...],
        next_cursor: str | None,
        has_more: bool,
        truncated: bool,
        initial_limit: int | None,
        account_fingerprint: bytes,
        response_bytes: int,
        read_source: RecordReadSource = "note",
        cancellation_event: threading.Event | None = None,
    ) -> RecordMeetingsPage:
        """Hydrate one private native page into the ordinary Notes registries."""

        _raise_if_notes_cancelled(cancellation_event)
        limit = _validated_initial_limit(initial_limit)
        if len(account_fingerprint) != hashlib.sha256().digest_size:
            raise ValueError("account_fingerprint is invalid")
        if read_source not in ("meeting", "note"):
            raise ValueError("cached Notes source is invalid")
        if (
            isinstance(response_bytes, bool)
            or not 0 <= response_bytes <= MAXIMUM_PAGE_RESPONSE_BYTES
        ):
            raise ValueError("response_bytes is out of range")
        if len(rows) > MAXIMUM_INITIAL_PAGE_LIMIT:
            raise ValueError("cached Notes page is too large")
        if next_cursor is not None:
            try:
                encoded_cursor = next_cursor.encode("utf-8")
            except UnicodeEncodeError as exc:
                raise ValueError("cached cursor is invalid") from exc
            if (
                not next_cursor
                or len(encoded_cursor) > MAXIMUM_CURSOR_BYTES
                or any(ord(character) < 0x20 or ord(character) == 0x7F for character in next_cursor)
            ):
                raise ValueError("cached cursor is invalid")
        if has_more != (next_cursor is not None):
            raise ValueError("cached pagination is inconsistent")

        seen_raw_ids: set[str] = set()
        for raw_id, note in rows:
            if MEETING_ID_PATTERN.fullmatch(raw_id) is None or raw_id in seen_raw_ids:
                raise ValueError("cached Notes row is invalid")
            seen_raw_ids.add(raw_id)
            registered = self._handle_registry.register(
                raw_id,
                account_fingerprint=account_fingerprint,
                source=read_source,
            )
            if registered != note.id:
                raise ValueError("cached Notes id is invalid")

        visible = tuple(note for _, note in rows[:limit])
        buffered = rows[limit:]
        continuation_state = None
        if buffered or next_cursor is not None:
            continuation_state = _PaginationState(
                cursor=next_cursor,
                seen_raw_ids=frozenset(seen_raw_ids),
                seen_cursors=(frozenset({next_cursor}) if next_cursor is not None else frozenset()),
                page_count=1,
                total_response_bytes=response_bytes,
                account_fingerprint=account_fingerprint,
                read_source=read_source,
                buffered_rows=buffered,
                terminal_truncated=truncated,
            )
        return self._publish_initial_page(
            _ProjectedPage(
                notes=visible,
                read_source=read_source,
                continuation_state=continuation_state,
                truncated=truncated if continuation_state is None else False,
            ),
            account_scope_generation=account_scope_generation(
                self._account_scope_secret,
                account_fingerprint,
                domain=_NOTES_ACCOUNT_SCOPE_DOMAIN,
            ),
            cancellation_event=cancellation_event,
        )

    def _continue_notes_page(
        self,
        page_token: str,
        *,
        auth_client: ChatGPTAuthProvider,
        cancellation_event: threading.Event | None,
    ) -> RecordMeetingsPage:
        entry, replay = self._claim_continuation(page_token)
        if replay is not None:
            self._verify_current_account(
                entry.state.account_fingerprint,
                auth_client=auth_client,
                cancellation_event=cancellation_event,
            )
            _raise_if_notes_cancelled(cancellation_event)
            return replay

        try:
            if entry.state.buffered_rows:
                self._verify_current_account(
                    entry.state.account_fingerprint,
                    auth_client=auth_client,
                    cancellation_event=cancellation_event,
                )
                _raise_if_notes_cancelled(cancellation_event)
                return self._commit_continuation(
                    page_token,
                    entry,
                    _project_buffered_page(entry.state),
                    account_scope_generation=account_scope_generation(
                        self._account_scope_secret,
                        entry.state.account_fingerprint,
                        domain=_NOTES_ACCOUNT_SCOPE_DOMAIN,
                    ),
                    cancellation_event=cancellation_event,
                )
            if entry.state.cursor is None:
                raise RecordMeetingsPaginationResetRequired("Meetings pagination must restart.")
            fetched = self._fetch_backend_page(
                limit=CONTINUATION_PAGE_LIMIT,
                cursor=entry.state.cursor,
                read_source=entry.state.read_source,
                expected_account_fingerprint=entry.state.account_fingerprint,
                auth_client=auth_client,
                cancellation_event=cancellation_event,
            )
            projected = _project_backend_page(
                fetched,
                seen_raw_ids=entry.state.seen_raw_ids,
                seen_cursors=entry.state.seen_cursors,
                previous_page_count=entry.state.page_count,
                previous_response_bytes=entry.state.total_response_bytes,
            )
            return self._commit_continuation(
                page_token,
                entry,
                projected,
                account_scope_generation=account_scope_generation(
                    self._account_scope_secret,
                    fetched.account_fingerprint,
                    domain=_NOTES_ACCOUNT_SCOPE_DOMAIN,
                ),
                cancellation_event=cancellation_event,
            )
        except Exception:
            self._release_continuation(page_token, entry)
            raise

    def _fetch_backend_page(
        self,
        *,
        limit: int,
        cursor: str | None,
        recording_started_at: str | None = None,
        read_source: RecordReadSource | None,
        expected_account_fingerprint: bytes | None,
        auth_client: ChatGPTAuthProvider,
        cancellation_event: threading.Event | None,
    ) -> _FetchedBackendPage:
        deadline = self._clock() + self._timeout_seconds
        with measure_notes_lookup_stage("backend_auth"):
            auth = auth_client.get_chatgpt_auth(
                refresh_token=False,
                cancellation_event=cancellation_event,
            )
        fingerprint = record_account_fingerprint(auth)
        _require_expected_account(fingerprint, expected_account_fingerprint)
        if read_source is None:
            read_source = "note"
        refreshed = False
        quota_budget = RecordRateLimitBudget()
        while True:
            result, auth = self._request_backend_page(
                auth,
                auth_client=auth_client,
                quota_budget=quota_budget,
                limit=limit,
                cursor=cursor,
                recording_started_at=recording_started_at,
                read_source=read_source,
                deadline=deadline,
                cancellation_event=cancellation_event,
            )
            if result.status != 401:
                rows, next_cursor = parse_record_meetings_page(
                    result.body,
                    maximum_rows=limit,
                    rows_key="notes" if read_source == "note" else "meetings",
                )
                for raw_id, note in rows:
                    registered = self._handle_registry.register(
                        raw_id,
                        account_fingerprint=fingerprint,
                        source=read_source,
                    )
                    if registered != note.id:
                        raise RecordMeetingsBackendError("Meetings returned an invalid meeting id.")
                return _FetchedBackendPage(
                    rows=tuple(rows),
                    next_cursor=next_cursor,
                    response_bytes=len(result.body),
                    account_fingerprint=fingerprint,
                    read_source=read_source,
                )
            if refreshed:
                raise RecordMeetingsAuthError("ChatGPT authentication was rejected.")
            _raise_if_notes_cancelled(cancellation_event)
            with measure_notes_lookup_stage("backend_auth"):
                auth = refresh_chatgpt_auth_after_unauthorized(
                    auth_client,
                    auth,
                    cancellation_event=cancellation_event,
                )
            fingerprint = record_account_fingerprint(auth)
            _require_expected_account(fingerprint, expected_account_fingerprint)
            refreshed = True

    def _request_backend_page(
        self,
        auth: AuthMaterial,
        *,
        auth_client: ChatGPTAuthProvider,
        quota_budget: RecordRateLimitBudget,
        limit: int,
        cursor: str | None,
        recording_started_at: str | None = None,
        read_source: RecordReadSource,
        deadline: float,
        cancellation_event: threading.Event | None,
    ) -> tuple[RecordHTTPResult, AuthMaterial]:
        _raise_if_notes_cancelled(cancellation_event)
        remaining = deadline - self._clock()
        if remaining <= 0:
            raise RecordMeetingsBackendError(
                _NOTES_REQUEST_TIMEOUT_MESSAGE,
                failure_kind="timeout",
                retryable=True,
            )
        try:
            result, auth = authenticated_record_request(
                self._transport,
                auth,
                auth_client,
                url=_notes_page_url(
                    limit=limit,
                    cursor=cursor,
                    recording_started_at=recording_started_at,
                    read_source=read_source,
                ),
                timeout_seconds=remaining,
                cancellation_event=cancellation_event,
                quota_budget=quota_budget,
            )
        except RecordTransportCancelled:
            raise RecordMeetingsCancelled("Meetings request was cancelled.") from None
        except RecordTransportRateLimited as error:
            raise RecordMeetingsBackendError(
                "Meetings returned a backend error.",
                failure_kind="http_429",
                retryable=False,
                retry_after_seconds=error.retry_after_seconds,
            ) from None
        except RecordTransportTimeout:
            raise RecordMeetingsBackendError(
                _NOTES_REQUEST_TIMEOUT_MESSAGE,
                failure_kind="timeout",
                retryable=True,
            ) from None
        except RecordTransportBackendError:
            raise RecordMeetingsBackendError(
                "Meetings could not be reached.",
                failure_kind="transport",
                retryable=True,
            ) from None
        _raise_if_notes_cancelled(cancellation_event)
        if result.status == 401:
            return result, auth
        if result.status < 200 or result.status >= 300:
            failure_kind: RecordMeetingsBackendFailureKind
            if result.status == 408:
                failure_kind = "timeout"
            elif result.status == 429:
                failure_kind = "http_429"
            elif 400 <= result.status < 500:
                failure_kind = "http_4xx"
            elif 500 <= result.status < 600:
                failure_kind = "http_5xx"
            else:
                failure_kind = "invalid_response"
            raise RecordMeetingsBackendError(
                "Meetings returned a backend error.",
                failure_kind=failure_kind,
                retryable=failure_kind in {"timeout", "http_429", "http_5xx"},
            )
        if len(result.body) > MAXIMUM_PAGE_RESPONSE_BYTES:
            raise RecordMeetingsBackendError("Meetings returned an oversized response.")
        return result, auth

    def _verify_current_account(
        self,
        expected_fingerprint: bytes,
        *,
        auth_client: ChatGPTAuthProvider,
        cancellation_event: threading.Event | None,
    ) -> None:
        auth = auth_client.get_chatgpt_auth(
            refresh_token=False,
            cancellation_event=cancellation_event,
        )
        _require_expected_account(
            record_account_fingerprint(auth),
            expected_fingerprint,
        )

    def _publish_initial_page(
        self,
        projected: _ProjectedPage,
        *,
        account_scope_generation: str,
        cancellation_event: threading.Event | None,
    ) -> RecordMeetingsPage:
        _raise_if_notes_cancelled(cancellation_event)
        if projected.continuation_state is None:
            return RecordMeetingsPage(
                notes=projected.notes,
                read_source=projected.read_source,
                account_scope_generation=account_scope_generation,
                has_more=False,
                next_page_token=None,
                truncated=projected.truncated,
            )
        with self._continuation_lock:
            _raise_if_notes_cancelled(cancellation_event)
            now = self._clock()
            self._prune_expired_locked(now)
            next_token = self._insert_continuation_locked(
                projected.continuation_state,
                now=now,
                protected_token=None,
            )
        return RecordMeetingsPage(
            notes=projected.notes,
            read_source=projected.read_source,
            account_scope_generation=account_scope_generation,
            has_more=True,
            next_page_token=next_token,
            truncated=False,
        )

    def _claim_continuation(
        self,
        page_token: str,
    ) -> tuple[_ContinuationEntry, RecordMeetingsPage | None]:
        with self._continuation_lock:
            now = self._clock()
            self._prune_expired_locked(now)
            entry = self._continuations.get(page_token)
            if entry is None:
                raise RecordMeetingsPaginationResetRequired("Meetings pagination must restart.")
            if entry.in_flight:
                # The MCP's bounded Notes lane serializes normal calls. Fail
                # closed for any direct concurrent caller instead of sending
                # the same private backend cursor twice.
                raise RecordMeetingsBackendError("Meetings pagination is already in progress.")
            entry.expires_at = now + self._continuation_ttl_seconds
            if entry.replay is not None:
                child_token = entry.replay.next_page_token
                child = self._continuations.get(child_token) if child_token is not None else None
                if child is not None:
                    child.expires_at = max(child.expires_at, entry.expires_at)
                return entry, entry.replay
            entry.in_flight = True
            return entry, None

    def _commit_continuation(
        self,
        page_token: str,
        entry: _ContinuationEntry,
        projected: _ProjectedPage,
        *,
        account_scope_generation: str,
        cancellation_event: threading.Event | None,
    ) -> RecordMeetingsPage:
        with self._continuation_lock:
            _raise_if_notes_cancelled(cancellation_event)
            if self._continuations.get(page_token) is not entry or not entry.in_flight:
                raise RecordMeetingsPaginationResetRequired("Meetings pagination must restart.")
            now = self._clock()
            next_token = None
            if projected.continuation_state is not None:
                next_token = self._insert_continuation_locked(
                    projected.continuation_state,
                    now=now,
                    protected_token=page_token,
                )
            page = RecordMeetingsPage(
                notes=projected.notes,
                read_source=projected.read_source,
                account_scope_generation=account_scope_generation,
                has_more=next_token is not None,
                next_page_token=next_token,
                truncated=projected.truncated,
            )
            entry.replay = page
            entry.in_flight = False
            entry.expires_at = now + self._continuation_ttl_seconds
            return page

    def _release_continuation(
        self,
        page_token: str,
        entry: _ContinuationEntry,
    ) -> None:
        with self._continuation_lock:
            if self._continuations.get(page_token) is entry:
                entry.in_flight = False

    def _insert_continuation_locked(
        self,
        state: _PaginationState,
        *,
        now: float,
        protected_token: str | None,
    ) -> str:
        self._prune_expired_locked(now)
        while len(self._continuations) >= self._maximum_continuation_entries:
            candidates = [
                (entry.expires_at, token)
                for token, entry in self._continuations.items()
                if token != protected_token and not entry.in_flight
            ]
            if not candidates:
                raise RecordMeetingsBackendError("Meetings pagination capacity was reached.")
            self._evict_token_locked(min(candidates)[1])

        for _attempt in range(8):
            token = self._token_factory()
            try:
                token = _validated_page_token(token)
            except ValueError as exc:
                raise RecordMeetingsBackendError(
                    "Meetings pagination could not be created."
                ) from exc
            if token not in self._continuations:
                self._continuations[token] = _ContinuationEntry(
                    state=state,
                    expires_at=now + self._continuation_ttl_seconds,
                )
                return token
        raise RecordMeetingsBackendError("Meetings pagination could not be created.")

    def _prune_expired_locked(self, now: float) -> None:
        expired = [
            token
            for token, entry in self._continuations.items()
            if not entry.in_flight and entry.expires_at <= now
        ]
        for token in expired:
            self._evict_token_locked(token)

    def _evict_token_locked(self, token: str) -> None:
        pending = {token}
        while pending:
            current = pending.pop()
            if self._continuations.pop(current, None) is None:
                continue
            for parent_token, parent in tuple(self._continuations.items()):
                if (
                    parent.replay is not None
                    and parent.replay.next_page_token == current
                    and not parent.in_flight
                ):
                    pending.add(parent_token)


def _validated_initial_limit(value: object | None) -> int:
    if value is None:
        return DEFAULT_INITIAL_PAGE_LIMIT
    if (
        isinstance(value, bool)
        or not isinstance(value, int)
        or not MINIMUM_INITIAL_PAGE_LIMIT <= value <= MAXIMUM_INITIAL_PAGE_LIMIT
    ):
        raise ValueError("initial_limit is out of range")
    return value


def _validated_page_token(value: object) -> str:
    if not isinstance(value, str):
        raise ValueError("page_token must be a string")
    try:
        encoded = value.encode("ascii")
    except UnicodeEncodeError as exc:
        raise ValueError("page_token is invalid") from exc
    if len(encoded) > MAXIMUM_PAGE_TOKEN_BYTES or PAGE_TOKEN_PATTERN.fullmatch(value) is None:
        raise ValueError("page_token is invalid")
    return value


def _require_expected_account(
    actual: bytes,
    expected: bytes | None,
) -> None:
    if expected is not None and not hmac.compare_digest(actual, expected):
        raise RecordMeetingsPaginationResetRequired("Meetings pagination must restart.")


def _project_backend_page(
    fetched: _FetchedBackendPage,
    *,
    seen_raw_ids: frozenset[str],
    seen_cursors: frozenset[str],
    previous_page_count: int,
    previous_response_bytes: int,
) -> _ProjectedPage:
    total_response_bytes = previous_response_bytes + fetched.response_bytes
    if total_response_bytes > MAXIMUM_TOTAL_RESPONSE_BYTES:
        raise RecordMeetingsBackendError("Meetings returned too much data.")

    next_seen_ids = set(seen_raw_ids)
    projected_notes: list[RecordMeetingNote] = []
    for raw_id, note in fetched.rows:
        if raw_id in next_seen_ids:
            continue
        next_seen_ids.add(raw_id)
        if len(next_seen_ids) > MAXIMUM_NOTES:
            raise RecordMeetingsBackendError("Meetings returned too many meetings.")
        projected_notes.append(note)

    page_count = previous_page_count + 1
    next_cursor = fetched.next_cursor
    if next_cursor is None:
        return _ProjectedPage(
            notes=tuple(projected_notes),
            read_source=fetched.read_source,
            continuation_state=None,
            truncated=False,
        )
    if next_cursor in seen_cursors:
        raise RecordMeetingsBackendError("Meetings pagination did not advance.")
    if (
        page_count >= MAXIMUM_PAGES
        or len(next_seen_ids) >= MAXIMUM_NOTES
        or total_response_bytes >= MAXIMUM_TOTAL_RESPONSE_BYTES
    ):
        return _ProjectedPage(
            notes=tuple(projected_notes),
            read_source=fetched.read_source,
            continuation_state=None,
            truncated=True,
        )

    next_seen_cursors = set(seen_cursors)
    next_seen_cursors.add(next_cursor)
    return _ProjectedPage(
        notes=tuple(projected_notes),
        read_source=fetched.read_source,
        continuation_state=_PaginationState(
            cursor=next_cursor,
            seen_raw_ids=frozenset(next_seen_ids),
            seen_cursors=frozenset(next_seen_cursors),
            page_count=page_count,
            total_response_bytes=total_response_bytes,
            account_fingerprint=fetched.account_fingerprint,
            read_source=fetched.read_source,
        ),
        truncated=False,
    )


def _project_buffered_page(state: _PaginationState) -> _ProjectedPage:
    """Drain a cached first page before following its private backend cursor."""

    visible_rows = state.buffered_rows[:CONTINUATION_PAGE_LIMIT]
    remaining_rows = state.buffered_rows[CONTINUATION_PAGE_LIMIT:]
    continuation_state = (
        replace(state, buffered_rows=remaining_rows)
        if remaining_rows or state.cursor is not None
        else None
    )
    return _ProjectedPage(
        notes=tuple(note for _, note in visible_rows),
        read_source=state.read_source,
        continuation_state=continuation_state,
        truncated=state.terminal_truncated if continuation_state is None else False,
    )


def _notes_page_url(
    *,
    limit: int,
    cursor: str | None,
    read_source: RecordReadSource,
    recording_started_at: str | None = None,
) -> str:
    if cursor is None:
        _validated_initial_limit(limit)
    elif limit != CONTINUATION_PAGE_LIMIT:
        raise RecordMeetingsBackendError("Meetings pagination used an invalid limit.")
    query: dict[str, str] = {"limit": str(limit)}
    query["include_unsuccessful"] = "true"
    if recording_started_at is not None:
        instant = _timestamp_instant(recording_started_at)
        if instant is None or cursor is not None or read_source != "note":
            raise ValueError("Invalid recording correlation window")
        query["recording_started_at"] = instant.isoformat(timespec="milliseconds").replace(
            "+00:00", "Z"
        )
    if cursor is not None:
        query["cursor"] = cursor
    encoded = urllib.parse.urlencode(query)
    if len(encoded.encode("utf-8")) > MAXIMUM_ENCODED_CURSOR_BYTES:
        raise RecordMeetingsBackendError("Meetings returned an invalid cursor.")
    root = RECORD_NOTES_URL if read_source == "note" else RECORD_MEETINGS_URL
    return f"{root}?{encoded}"


def parse_record_meetings_page(
    body: bytes,
    *,
    maximum_rows: int,
    rows_key: Literal["meetings", "notes"] = "meetings",
) -> tuple[list[tuple[str, RecordMeetingNote]], str | None]:
    """Parse and project one bounded Record meetings page.

    Args:
        body: Raw JSON response body from the Record meetings endpoint.
        maximum_rows: Maximum number of meetings accepted from this page.

    Returns:
        Valid projected rows and the optional validated backend cursor.

    Raises:
        RecordMeetingsBackendError: If the response or cursor is malformed.
        ValueError: If ``maximum_rows`` is outside the supported range.
    """

    if (
        isinstance(maximum_rows, bool)
        or not MINIMUM_INITIAL_PAGE_LIMIT <= maximum_rows <= MAXIMUM_INITIAL_PAGE_LIMIT
    ):
        raise ValueError("maximum_rows is out of range")
    try:
        payload: object = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError, RecursionError) as exc:
        raise RecordMeetingsBackendError("Meetings returned an invalid response.") from exc
    if not is_json(payload):
        raise RecordMeetingsBackendError("Meetings returned an invalid response.")
    rows_value = payload.get(rows_key)
    if rows_value is None:
        rows: list[object] = []
    elif is_json_array(rows_value):
        rows = rows_value
    else:
        raise RecordMeetingsBackendError("Meetings returned an invalid page.")
    if len(rows) > maximum_rows:
        raise RecordMeetingsBackendError("Meetings returned an invalid page.")
    projected: list[tuple[str, RecordMeetingNote]] = []
    for row in rows:
        parsed = parse_record_meeting_row(
            row,
            default_private_owner_count=rows_key == "notes",
        )
        if parsed is not None:
            projected.append(parsed)

    raw_cursor = payload.get("nextCursor", payload.get("next_cursor"))
    if raw_cursor is None:
        return projected, None
    if not isinstance(raw_cursor, str):
        raise RecordMeetingsBackendError("Meetings returned an invalid cursor.")
    cursor = raw_cursor.strip()
    if not cursor:
        return projected, None
    if len(cursor.encode("utf-8")) > MAXIMUM_CURSOR_BYTES:
        raise RecordMeetingsBackendError("Meetings returned an invalid cursor.")
    return projected, cursor


def parse_record_meeting_row(
    value: object,
    *,
    default_private_owner_count: bool = False,
) -> tuple[str, RecordMeetingNote] | None:
    """Project one untrusted backend meeting into the token-free list DTO.

    Args:
        value: Candidate decoded JSON meeting object.

    Returns:
        The canonical backend id and projected note, or ``None`` when unusable.
    """

    if not is_json(value):
        return None
    raw_id = nonempty_string(value.get("id"), maximum_bytes=512)
    if raw_id is None or MEETING_ID_PATTERN.fullmatch(raw_id) is None:
        return None
    started_at = _first_timestamp(
        value,
        (
            "meetingStartTime",
            "calendarStartTime",
            "calendar_start_time",
            "recordingStartTime",
            "recording_start_time",
            "startTime",
            "started_at",
            "date",
        ),
    )
    if started_at is None:
        return None
    ended_at = _first_timestamp(
        value,
        (
            "meetingEndTime",
            "calendarEndTime",
            "calendar_end_time",
            "recordingEndTime",
            "recording_end_time",
            "endTime",
            "ended_at",
        ),
    )
    title = project_meeting_title(value.get("title"))
    record_source = nonempty_string(
        value.get("recordSource"),
        maximum_bytes=256,
    )
    device_platform = _native_mobile_device_platform(
        record_source,
        value.get("devicePlatform"),
    )
    raw_share_count = value.get("numShareRecipients")
    num_share_recipients = (
        1
        if raw_share_count is None and default_private_owner_count
        else _nonnegative_int(raw_share_count)
    )
    if num_share_recipients is None:
        return None
    status = _project_list_status(value)
    if status is None:
        return None
    page_id = nonempty_string(value.get("summaryPageId"), maximum_bytes=64)
    if page_id is not None and re.fullmatch(r"page_[0-9a-f]{32}", page_id) is None:
        page_id = None
    return raw_id, RecordMeetingNote(
        id=public_meeting_id(raw_id),
        title=title,
        started_at=started_at,
        ended_at=ended_at,
        status=status,
        fetch_status=_project_fetch_status(status=status),
        is_empty=value.get("isEmpty") is True,
        num_share_recipients=num_share_recipients,
        record_source=record_source,
        device_platform=device_platform,
        summary_page_id=page_id,
        cca_wait_until=_optional_timestamp(value.get("ccaWaitUntil")),
        source_meeting_id=nonempty_string(value.get("sourceMeetingId"), maximum_bytes=128),
        source_recording_id=nonempty_string(value.get("sourceRecordingId"), maximum_bytes=64),
        recording_correlation_pending=value.get("recordingCorrelationPending") is True,
        processing_stage=_project_processing_stage(value, status),
    )


def _native_mobile_device_platform(
    record_source: str | None,
    value: object,
) -> Literal["ios", "android"] | None:
    if record_source != "meetingsapp":
        return None
    if value == "ios":
        return "ios"
    if value == "android":
        return "android"
    return None


def _nonnegative_int(value: object) -> int | None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        return None
    return value


def _first_timestamp(row: Mapping[str, object], keys: tuple[str, ...]) -> str | None:
    for key in keys:
        raw = nonempty_string(row.get(key), maximum_bytes=MAXIMUM_TIMESTAMP_BYTES)
        if raw is not None and _is_timestamp(raw):
            return raw
    return None


def _is_timestamp(value: str) -> bool:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return False
    if parsed.tzinfo is None and "T" in value:
        # Datetimes must carry an offset; a date-only backend field remains
        # acceptable because JavaScript Date.parse handles it deterministically.
        return False
    if parsed.tzinfo is not None:
        try:
            parsed.astimezone(timezone.utc)
        except (OverflowError, ValueError):
            return False
    return True


def _raise_if_notes_cancelled(event: threading.Event | None) -> None:
    if event is not None and event.is_set():
        raise RecordMeetingsCancelled("Meetings request was cancelled.")


# Meeting interaction API

BACKEND_API_ROOT = "https://chatgpt.com/backend-api"
RECORD_API_ROOT = f"{BACKEND_API_ROOT}/meetings"
MAXIMUM_FEEDBACK_CONTINUATION_ENTRIES = 128
FEEDBACK_CONTINUATION_TTL_SECONDS = 24 * 60 * 60.0
DEFAULT_INTERACTIONS_TIMEOUT_SECONDS = 45.0
MAXIMUM_PRIVATE_RESPONSE_BYTES = 768 * 1024
MAXIMUM_TEXT_FIELD_BYTES = 512 * 1024
MAXIMUM_COLLECTION_ROWS = 5_000
MAXIMUM_REQUEST_BODY_BYTES = 16 * 1024
MAXIMUM_URL_BYTES = 16 * 1024
MAXIMUM_SHARE_ELIGIBILITY_EMAIL_LENGTH = 320
FEEDBACK_CATEGORIES = frozenset(
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
_SETTING_ORDER: tuple[HostedSettingName, ...] = (
    "featureEnabled",
    "autoRecordEnabled",
    "slackNotificationsEnabled",
)
SETTING_NAMES = frozenset(_SETTING_ORDER)
GATEWAY_SETTING_NAMES = SETTING_NAMES


class RecordMeetingInteractionsError(RuntimeError):
    """Base class with a token-free, UI-safe message."""


class RecordMeetingInteractionsAuthError(RecordMeetingInteractionsError):
    """Authentication or account ownership no longer authorizes the interaction."""


class RecordMeetingInteractionsAuthRejected(RecordMeetingInteractionsAuthError):
    """The backend rejected the sole retry with refreshed ChatGPT auth."""


class RecordMeetingInteractionsBackendError(RecordMeetingInteractionsError):
    """The backend failed or returned an invalid bounded response."""

    def __init__(
        self,
        message: str,
        *,
        failure_kind: RecordMeetingsBackendFailureKind = "invalid_response",
        http_status: int | None = None,
    ) -> None:
        super().__init__(message)
        self.failure_kind: RecordMeetingsBackendFailureKind = failure_kind
        self.http_status = http_status
        self.retryable = failure_kind in {"timeout", "transport", "http_429", "http_5xx"}


class RecordMeetingInteractionsCancelled(RecordMeetingInteractionsError):
    """The caller cancelled an in-flight interaction."""


@dataclass(repr=False)
class _RequestContext:
    auth: AuthMaterial
    account_fingerprint: bytes
    deadline: float
    auth_client: ChatGPTAuthProvider
    refreshed: bool = False
    note_detail: dict[str, object] | None = None
    cleanup: bool = False
    quota_budget: RecordRateLimitBudget = field(default_factory=RecordRateLimitBudget)


@dataclass(frozen=True, slots=True)
class _LocalAutomationPolicy:
    owner_scope: str
    expires_at: float
    policy: AutomationPolicy


@dataclass(frozen=True, repr=False)
class _FeedbackContinuation:
    public_meeting_id: str
    backend_token: str
    account_fingerprint: bytes
    expires_at: float


@dataclass(frozen=True, slots=True)
class MeetingsDiscoveryRollout:
    """Optional MCP discovery features, fixed until the next connection."""

    sidebar_take_notes: bool
    search_mentions: bool


class RecordMeetingInteractionsClient(MeetingsClientPolicies[_RequestContext]):
    """Perform direct, bounded UI reads and writes without a native proxy."""

    def __init__(
        self,
        auth_client: ChatGPTAuthProvider | None = None,
        *,
        handle_registry: AccountScopedMeetingRegistry = MEETING_ID_REGISTRY,
        transport: RecordHTTPTransport | None = None,
        timeout_seconds: float = DEFAULT_INTERACTIONS_TIMEOUT_SECONDS,
        clock: Callable[[], float] = time.monotonic,
        token_factory: Callable[[], str] | None = None,
        native_policy_owner_available: Callable[[PluginClientContext | None], bool] | None = None,
    ) -> None:
        self._auth_client = auth_client or get_process_auth_manager()
        self._handle_registry = handle_registry
        self._transport: RecordHTTPTransport = transport or HTTPSRecordTransport()
        self._timeout_seconds = bounded_timeout_seconds(timeout_seconds)
        self._clock = clock
        self._token_factory = token_factory or (lambda: secrets.token_urlsafe(32))
        self._feedback_lock = threading.Lock()
        self._connection_migration = ConnectionMigration()
        self._feedback_continuations: dict[str, _FeedbackContinuation] = {}
        self._automation_policy_lock = threading.Lock()
        self._automation_policy: _LocalAutomationPolicy | None = None
        super().__init__(
            auth_client=self._auth_client,
            clock=self._clock,
            begin_request=lambda cancellation: self._begin_request(cancellation_event=cancellation),
            request_bootstrap=self._fetch_policy_bootstrap,
            request_errors=(RecordMeetingInteractionsError, CodexAuthError),
            native_policy_owner_available=native_policy_owner_available,
        )
        self._discovery_rollout_lock = threading.Lock()
        self._discovery_rollout_ready = threading.Event()
        self._discovery_rollout_stop = threading.Event()
        self._discovery_rollout_deadline: float | None = None
        self._discovery_rollout = MeetingsDiscoveryRollout(False, False)

    def _fetch_policy_bootstrap(
        self,
        context: _RequestContext,
        body: Mapping[str, object],
        cancellation_event: threading.Event,
    ) -> RecordHTTPResult:
        return self._request(
            context,
            method="POST",
            path="",
            body=body,
            cancellation_event=cancellation_event,
            statsig_bootstrap=True,
        )

    def start_discovery_rollout_lookup(self) -> None:
        """Resolve optional discovery features once, without delaying initialization."""
        with self._discovery_rollout_lock:
            if self._discovery_rollout_deadline is not None:
                return
            self._discovery_rollout_deadline = self._clock() + 5.0
        threading.Thread(
            target=self._lookup_discovery_rollout,
            name="meetings-discovery-rollout",
            daemon=True,
        ).start()

    def discovery_rollout(self) -> MeetingsDiscoveryRollout:
        """Read startup feature gates within the shared discovery deadline.

        Returns:
            Independent sidebar and mention gates; unresolved or failed lookup
            leaves both disabled until the MCP reconnects.
        """
        with self._discovery_rollout_lock:
            deadline = self._discovery_rollout_deadline
        if deadline is None:
            return MeetingsDiscoveryRollout(False, False)
        if not self._discovery_rollout_ready.wait(max(0.0, deadline - self._clock())):
            self.stop_discovery_rollout_lookup()
        with self._discovery_rollout_lock:
            return self._discovery_rollout

    def stop_discovery_rollout_lookup(self) -> None:
        """Cancel startup work and discard late results after timeout or disconnect."""
        with self._discovery_rollout_lock:
            self._discovery_rollout_stop.set()
            self._discovery_rollout = MeetingsDiscoveryRollout(False, False)
            self._discovery_rollout_ready.set()

    def _lookup_discovery_rollout(self) -> None:
        rollout = MeetingsDiscoveryRollout(False, False)
        try:
            context = self._begin_request(cancellation_event=self._discovery_rollout_stop)
            with self._discovery_rollout_lock:
                deadline = self._discovery_rollout_deadline
            if deadline is None:
                return
            context.deadline = min(context.deadline, deadline)
            result = self._request(
                context,
                method="POST",
                path="",
                body={"brand_name": "chatgpt-meetings", "window_type": "mcp"},
                cancellation_event=self._discovery_rollout_stop,
                statsig_bootstrap=True,
            )
            rollout = _decode_discovery_rollout(result.body)
        except Exception:
            # Optional discovery metadata must not prevent the Meetings app loading.
            pass
        finally:
            with self._discovery_rollout_lock:
                if (
                    not self._discovery_rollout_stop.is_set()
                    and self._discovery_rollout_deadline is not None
                    and self._clock() < self._discovery_rollout_deadline
                ):
                    self._discovery_rollout = rollout
                self._discovery_rollout_ready.set()

    def get_note(
        self,
        note_id: str,
        *,
        cancellation_event: threading.Event | None = None,
    ) -> RecordMeetingNoteWire:
        """Read the private selected-note detail for one public meeting identifier.

        Args:
            note_id: Account-scoped public meeting identifier received from the app.
            cancellation_event: Optional event used to cancel auth or backend work.

        Returns:
            The bounded note, summary, transcript, and participant projection.
        """

        context, raw_id = self._begin_note_request(
            note_id,
            cancellation_event=cancellation_event,
        )
        return self._read_note(
            context,
            raw_id=raw_id,
            exposed_id=note_id,
            cancellation_event=cancellation_event,
            read_source="note",
        )

    def resolve_note_reference(
        self,
        note_id: str,
        *,
        cancellation_event: threading.Event | None = None,
    ) -> tuple[RecordReadSource, str]:
        """Resolve one UI handle to its pinned backend source and identifier.

        Args:
            note_id: Account-scoped public identifier received from the UI.
            cancellation_event: Optional event used to cancel auth or recovery work.

        Returns:
            The session-pinned read source and its canonical backend identifier.
        """

        _, raw_id = self._begin_note_request(
            note_id,
            cancellation_event=cancellation_event,
        )
        return "note", raw_id

    def get_note_by_canonical_id(
        self,
        canonical_id: str,
        *,
        read_source: RecordReadSource = "meeting",
        cancellation_event: threading.Event | None = None,
    ) -> RecordMeetingNoteWire:
        """Read a resource using its canonical Meeting or private-note id.

        Args:
            canonical_id: Canonical identifier from a validated MCP resource URI.
            read_source: Explicit resource kind encoded in that URI.
            cancellation_event: Optional event used to cancel auth or backend work.

        Returns:
            The bounded projected meeting note.
        """

        if MEETING_ID_PATTERN.fullmatch(canonical_id) is None:
            raise RecordHandleError("Meeting resource is unavailable.")
        context = self._begin_request(cancellation_event=cancellation_event)
        return self._read_note(
            context,
            raw_id=canonical_id,
            exposed_id=canonical_id,
            cancellation_event=cancellation_event,
            read_source=read_source,
        )

    def _read_note(
        self,
        context: _RequestContext,
        *,
        raw_id: str,
        exposed_id: str,
        cancellation_event: threading.Event | None,
        read_source: RecordReadSource | None = None,
    ) -> RecordMeetingNoteWire:
        selected_source = read_source or "note"
        detail = context.note_detail
        if detail is None:
            detail = self._request_json(
                context,
                method="GET",
                path=_note_path(raw_id) if selected_source == "note" else _meeting_path(raw_id),
                cancellation_event=cancellation_event,
            )
        _require_matching_backend_id(detail, raw_id)
        if selected_source == "note":
            transcript_response = self._request(
                context,
                method="GET",
                path=_note_path(raw_id, "transcripts"),
                cancellation_event=cancellation_event,
                accepted_statuses=frozenset({404}),
            )
            unavailable_transcripts: dict[str, object] = {
                "meetingId": raw_id,
                "status": "unavailable",
                "entries": [],
            }
            transcripts = (
                unavailable_transcripts
                if transcript_response.status == 404
                else _decode_response_object(transcript_response.body)
            )
            payload = _project_private_note(exposed_id, raw_id, detail, transcripts)
            _require_private_response_size(payload)
            return payload
        summary = self._request_json(
            context,
            method="GET",
            path=_meeting_path(raw_id, "summary"),
            cancellation_event=cancellation_event,
        )
        transcripts = self._request_json(
            context,
            method="GET",
            path=_meeting_path(raw_id, "transcripts"),
            cancellation_event=cancellation_event,
        )
        payload = _project_note(exposed_id, raw_id, detail, summary, transcripts)
        _require_private_response_size(payload)
        return payload

    def share(
        self,
        note_id: str,
        *,
        email: str,
        expected_account: tuple[str, str | None] | None = None,
        cancellation_event: threading.Event | None = None,
    ) -> RecordMeetingShareWire:
        """Share one meeting with a validated email recipient.

        Args:
            note_id: Account-scoped public meeting identifier received from the app.
            email: Recipient email address.
            expected_account: Optional account and subject authorized by the app request.
            cancellation_event: Optional caller cancellation signal.

        Returns:
            The validated sharing acknowledgement with private ids removed.
        """

        normalized_email = _validated_email(email)
        payload = self._request_note_json(
            note_id,
            suffix="share",
            method="POST",
            body={"email": normalized_email},
            expected_account=expected_account,
            cancellation_event=cancellation_event,
        )
        recipient_email = _required_string(
            payload.get("recipientEmail"),
            maximum_bytes=320,
        )
        result: RecordMeetingShareWire = {
            "meeting_id": note_id,
            "recipient_email": recipient_email,
            "recipient_name": nonempty_string(
                payload.get("recipientName"),
                maximum_bytes=512,
            ),
            "access_edge_created": _required_bool(
                payload.get("accessEdgeCreated"),
                "accessEdgeCreated",
            ),
        }
        _require_private_response_size(result)
        return result

    def check_share_eligibility(
        self,
        note_id: str,
        *,
        email: object,
        expected_account: tuple[str, str | None] | None = None,
        cancellation_event: threading.Event | None = None,
    ) -> RecordMeetingShareEligibilityWire:
        """Check one exact recipient against the meeting's sharing policy.

        An empty email performs only the verified policy read needed to choose
        personal versus workspace UI. Note-rooted reads let Record resolve the
        live source Meeting and policy in one endpoint; legacy Meeting reads
        retain their account-scope bootstrap. Account-user identifiers, roles,
        and nonmatching directory entries never cross this boundary.
        """

        if not isinstance(email, str) or _contains_control_character(email):
            raise ValueError("share eligibility email is invalid")
        normalized_email = email.strip()
        try:
            normalized_email.encode("utf-8")
        except UnicodeEncodeError as exc:
            raise ValueError("share eligibility email is invalid") from exc
        if len(normalized_email) > MAXIMUM_SHARE_ELIGIBILITY_EMAIL_LENGTH:
            raise ValueError("share eligibility email is invalid")
        if normalized_email:
            normalized_email = _validated_email(normalized_email)
        context, raw_id = self._begin_note_request(
            note_id,
            expected_account=expected_account,
            cancellation_event=cancellation_event,
        )
        eligibility_payload = self._request_json(
            context,
            method="POST",
            path=_note_path(raw_id, "share/eligibility"),
            body={"email": normalized_email} if normalized_email else {},
            cancellation_event=cancellation_event,
        )
        result = _project_note_share_eligibility(
            eligibility_payload,
            requested_email=normalized_email,
        )
        _require_private_response_size(result)
        return result

    def delete_note(
        self,
        note_id: str,
        *,
        expected_account: tuple[str, str | None] | None = None,
        cancellation_event: threading.Event | None = None,
    ) -> RecordMeetingDeleteWire:
        """Delete the current account's meeting identified by its opaque handle."""

        context, raw_id = self._begin_note_request(
            note_id,
            expected_account=expected_account,
            cancellation_event=cancellation_event,
            cleanup=True,
        )
        response = self._request(
            context,
            method="DELETE",
            path=_note_path(raw_id),
            cancellation_event=cancellation_event,
        )
        if response.status != 204 or response.body:
            raise RecordMeetingInteractionsBackendError(
                "Meetings returned an invalid deletion response."
            )
        result: RecordMeetingDeleteWire = {"meeting_id": note_id, "deleted": True}
        _require_private_response_size(result)
        return result

    def reprocess_note(
        self,
        note_id: str,
        *,
        expected_account: tuple[str, str | None] | None = None,
        cancellation_event: threading.Event | None = None,
    ) -> RecordMeetingReprocessWire:
        """Request guarded reprocessing for the current account's selected note.

        Args:
            note_id: Account-scoped public note or registered Meeting identifier.
            expected_account: Account and subject authorized by the app request.
            cancellation_event: Optional caller cancellation signal.

        Returns:
            The selected public note identifier and processing acknowledgement.
            The server resolves its source and admits or resumes eligible work.
        """

        context, raw_id = self._begin_note_request(
            note_id,
            expected_account=expected_account,
            cancellation_event=cancellation_event,
        )
        result: RecordMeetingReprocessWire = {"meetingId": note_id, "status": "processing"}
        # Cold-note authorization may finish after an account switch. Fence the
        # mutation against the current cached owner without another auth probe.
        if isinstance(context.auth_client, _CachedAuthProvider):
            current_auth = context.auth_client.peek_cached_chatgpt_auth()
            if current_auth is None or (current_auth.account_id, current_auth.subject) != (
                context.auth.account_id,
                context.auth.subject,
            ):
                raise RecordMeetingInteractionsAuthError(
                    "ChatGPT account changed before the meeting update."
                )
        response = self._request(
            context,
            method="POST",
            path=_note_path(raw_id, "reprocess"),
            cancellation_event=cancellation_event,
            accepted_statuses=frozenset({409}),
        )
        if response.status == 409:
            conflict = _decode_response_object(response.body).get("detail")
            if is_json(conflict) and conflict.get("code") == "record_processing_in_progress":
                return result
        if response.status != 200:
            raise RecordMeetingInteractionsBackendError(
                "Meetings returned an invalid reprocessing response."
            )
        acknowledgement = _decode_response_object(response.body)
        if acknowledgement.get("id") != raw_id:
            raise RecordMeetingInteractionsBackendError("Meetings returned a mismatched meeting.")
        _require_matching_backend_id(acknowledgement, raw_id)
        _required_string(acknowledgement.get("workflowId"), maximum_bytes=512)
        return result

    def submit_feedback(
        self,
        note_id: str,
        *,
        category: str,
        feedback_text: str | None,
        include_debug_artifacts: bool,
        feedback_continuation_token: str | None = None,
        expected_account: tuple[str, str | None] | None = None,
        cancellation_event: threading.Event | None = None,
    ) -> RecordMeetingFeedbackWire:
        """Submit one non-idempotent meeting feedback report.

        Args:
            note_id: Account-scoped public meeting identifier received from the app.
            category: Supported feedback category.
            feedback_text: Optional bounded user feedback.
            include_debug_artifacts: Whether the backend may attach meeting content.
            feedback_continuation_token: Optional opaque continuation from an earlier report.
            expected_account: Optional account and subject authorized by the app request.
            cancellation_event: Optional caller cancellation signal.

        Returns:
            The bounded feedback acknowledgement and optional local continuation.
        """

        if category not in FEEDBACK_CATEGORIES:
            raise ValueError("feedback category is invalid")
        normalized_text = _validated_feedback_text(feedback_text)
        body: dict[str, object] = {
            "rating": category,
            "includeDebugArtifacts": include_debug_artifacts,
        }
        if normalized_text is not None:
            body["feedbackText"] = normalized_text
        context, raw_id = self._begin_note_request(
            note_id,
            expected_account=expected_account,
            cancellation_event=cancellation_event,
        )
        if feedback_continuation_token is not None:
            continuation = self._resolve_feedback_continuation(
                _validated_feedback_continuation_token(feedback_continuation_token),
                note_id=note_id,
                account_fingerprint=context.account_fingerprint,
            )
            body["feedbackContinuationToken"] = continuation.backend_token
        feedback_account = (context.auth.account_id, context.auth.subject)
        diagnostic_scope = capture_feedback_diagnostic_scope(expected_account=feedback_account)
        payload = self._request_json(
            context,
            method="POST",
            path=_note_path(raw_id, "feedback"),
            body=body,
            cancellation_event=cancellation_event,
        )
        _require_matching_backend_id(payload, raw_id)
        result: RecordMeetingFeedbackWire = {
            "meetingId": note_id,
            "feedbackId": nonempty_string(
                payload.get("sentryEventId"),
                maximum_bytes=512,
            ),
        }
        feedback_continuation = nonempty_string(
            payload.get("feedbackContinuationToken"),
            maximum_bytes=4096,
        )
        if feedback_continuation is not None:
            result["feedbackContinuationToken"] = self._publish_feedback_continuation(
                note_id=note_id,
                backend_token=feedback_continuation,
                account_fingerprint=context.account_fingerprint,
            )
        # Feedback is non-idempotent. Preserve its acknowledgement if the separate
        # plugin diagnostic upload fails, so the UI never retries the mutation.
        try:
            feedback_id = result["feedbackId"]
            if feedback_id is None:
                raise ValueError("Feedback acknowledgement has no event ID")
            submit_feedback_diagnostics(
                feedback_id,
                expected_account=feedback_account,
                expected_scope=diagnostic_scope,
            )
            result["diagnosticsUploaded"] = True
        except (HTTPException, OSError, RuntimeError, ValueError):
            result["diagnosticsUploaded"] = False
            if (
                diagnostic_scope is not None
                and capture_feedback_diagnostic_scope(expected_account=feedback_account)
                == diagnostic_scope
            ):
                report_mcp_error(
                    "interactions", "backend", operation="feedback", notification="feedback_failed"
                )
        _require_private_response_size(result)
        return result

    def get_onboarding_profile(
        self, *, cancellation_event: threading.Event | None = None
    ) -> OnboardingProfileWire:
        """Read the current user's name and authenticated internal Meetings gate.

        Args:
            cancellation_event: Caller cancellation signal.

        Returns:
            Bounded first name and internal account access, excluding raw profile fields.
        """
        context = self._begin_request(cancellation_event=cancellation_event)
        payload = self._request_json(
            context,
            method="GET",
            path="/me",
            api_scope="backend",
            cancellation_event=cancellation_event,
        )
        result = self._request(
            context,
            method="POST",
            path="",
            body={"brand_name": "chatgpt-meetings", "window_type": "mcp"},
            cancellation_event=cancellation_event,
            statsig_bootstrap=True,
        )
        internal_account_access = statsig_gate_enabled(
            _decode_statsig_payload(result.body), "meetings_internal_account_access", "3405790161"
        )
        return {
            "firstName": nonempty_string(payload.get("first_name"), maximum_bytes=256),
            "internalAccountAccess": internal_account_access,
        }

    def ensure_meetings_connection(
        self,
        *,
        expected_account: tuple[str, str | None],
        cancellation_event: threading.Event | None = None,
    ) -> ConnectionMigrationResult:
        """Ensure only the current verified user's Sheep Meetings link."""
        context = self._begin_request(cancellation_event=cancellation_event)

        def check_current() -> None:
            _raise_if_interactions_cancelled(cancellation_event)
            if self._clock() >= context.deadline:
                raise RecordMeetingInteractionsBackendError(
                    "Meetings request timed out.", failure_kind="timeout"
                )
            current = context.auth_client.get_chatgpt_auth(
                refresh_token=False, cancellation_event=cancellation_event
            )
            if (
                current.subject is None
                or (current.account_id, current.subject) != expected_account
                or record_account_fingerprint(current) != context.account_fingerprint
            ):
                raise RecordMeetingInteractionsAuthError(
                    "ChatGPT account changed during the connection migration."
                )
            context.auth = current

        def connect() -> bool:
            return connection_is_active(
                self._request_json(
                    context,
                    method="POST",
                    path="/aip/connectors/links/noauth",
                    body=connection_request_body(),
                    api_scope="backend",
                    cancellation_event=cancellation_event,
                )
            )

        return self._connection_migration.ensure(
            context.account_fingerprint, connect=connect, check_current=check_current
        )

    def get_app_connections(
        self,
        *,
        group: Literal["calendars", "context"],
        cancellation_event: threading.Event | None = None,
    ) -> CalendarConnectionsWire | ContextConnectionsWire:
        """Read canonical Apps connection states.

        Args:
            group: Provider group.
            cancellation_event: Caller cancellation signal.

        Returns:
            Provider statuses and setup links; failures propagate.
        """
        context = self._begin_request(cancellation_event=cancellation_event)
        payload = self._request_json(
            context,
            method="POST",
            path="/aip/connectors/links/list_accessible",
            body={"principals": [], "link_refresh_strategy": "BLOCKING"},
            api_scope="backend",
            cancellation_event=cancellation_event,
        )
        try:
            return project_app_connections(payload, group)
        except ValueError as exc:
            raise RecordMeetingInteractionsBackendError(
                "Invalid app connections response."
            ) from exc

    def track_event(
        self,
        event: PluginAnalyticsEvent,
        *,
        expected_account: tuple[str, str | None],
        cancellation_event: threading.Event | None = None,
    ) -> bool:
        """Hand off one observation without replaying failed deliveries.

        Args:
            event: Validated client event and bounded metadata.
            expected_account: Account and subject verified for the mounted UI.
            cancellation_event: Caller cancellation signal.

        Returns:
            Whether Record's publisher accepted the call, not durable delivery.
            Delivery failures log a warning and return False.
        """
        from meetings_host_context import get_current_codex_version
        from meetings_sentry import plugin_version

        # Telemetry is explicitly best effort, including auth, transport and parsing.
        try:
            context = self._begin_request(cancellation_event=cancellation_event)
            if (context.auth.account_id, context.auth.subject) != expected_account:
                raise RecordMeetingInteractionsAuthError("ChatGPT account changed before tracking.")
            context.deadline = min(context.deadline, self._clock() + 2.0)
            context.quota_budget.remaining_retries = 0
            payload = self._request_json(
                context,
                method="POST",
                path="/track",
                body={
                    **event,
                    "pluginVersion": plugin_version(Path(__file__).resolve().parents[1])
                    or "unknown",
                    "codexAppVersion": get_current_codex_version() or "unknown",
                    "operatingSystem": (
                        "macos"
                        if sys.platform == "darwin"
                        else "windows"
                        if sys.platform.startswith("win")
                        else "linux"
                        if sys.platform.startswith("linux")
                        else "unknown"
                    ),
                },
                cancellation_event=cancellation_event,
            )
            accepted = payload.get("accepted")
            if not isinstance(accepted, bool):
                raise RecordMeetingInteractionsBackendError("Invalid analytics acknowledgement.")
            if not accepted:
                logging.getLogger(__name__).warning("Meetings analytics delivery was not accepted.")
            return accepted
        except Exception:
            # Never include exception text, credentials or event payload in diagnostics.
            logging.getLogger(__name__).warning(
                "Meetings analytics delivery failed; observation dropped."
            )
            return False

    def meetings_activity(
        self,
        *,
        mark_viewed: bool,
        expected_account: tuple[str, str | None],
        cancellation_event: threading.Event | None = None,
    ) -> MeetingsActivityWire:
        """Read unread activity or acknowledge a visible Meetings home.

        Args:
            mark_viewed: Whether to advance the server-owned viewed timestamp.
            expected_account: Account and subject verified by the gateway.
            cancellation_event: Caller cancellation signal.

        Returns:
            The validated aggregate unread bit for that workspace.
        """
        context = self._begin_request(cancellation_event=cancellation_event)
        if (context.auth.account_id, context.auth.subject) != expected_account:
            raise RecordMeetingInteractionsAuthError(
                "ChatGPT account changed before activity request."
            )
        payload = self._request_json(
            context,
            method="POST" if mark_viewed else "GET",
            path="/activity/viewed" if mark_viewed else "/activity",
            cancellation_event=cancellation_event,
        )
        unread = payload.get("hasUnreadActivity")
        if not isinstance(unread, bool):
            raise RecordMeetingInteractionsBackendError("Invalid Meetings activity response.")
        return MeetingsActivityWire(hasUnreadActivity=unread)

    def get_settings(
        self,
        *,
        auth_client: ChatGPTAuthProvider | None = None,
        expected_account: tuple[str, str | None] | None = None,
        cancellation_event: threading.Event | None = None,
    ) -> HostedSettings:
        """Read hosted Record preferences.

        Args:
            auth_client: Request-scoped authentication provider.
            expected_account: Authorized account and subject.
            cancellation_event: Caller cancellation signal.

        Returns:
            Validated hosted settings.
        """

        context = self._begin_request(
            auth_client=auth_client,
            cancellation_event=cancellation_event,
        )
        if (
            expected_account is not None
            and (context.auth.account_id, context.auth.subject) != expected_account
        ):
            raise RecordMeetingInteractionsAuthError(
                "ChatGPT account changed before reading settings."
            )
        payload = self._request_json(
            context,
            method="GET",
            path="/settings/preferences",
            cancellation_event=cancellation_event,
        )
        return _project_settings(payload)

    def get_local_automation_policy(
        self,
        *,
        expected_owner_scope: str,
        cancellation_event: threading.Event | None = None,
    ) -> AutomationPolicy:
        """Evaluate device automation rollout for the verified native owner."""

        context = self._begin_request(cancellation_event=cancellation_event)
        owner_scope = record_owner_scope_fingerprint(context.auth)
        if owner_scope is None or not hmac.compare_digest(owner_scope, expected_owner_scope):
            raise RecordMeetingInteractionsAuthError("ChatGPT account changed during the request.")
        cached = self.peek_local_automation_policy(expected_owner_scope=owner_scope)
        if cached is not None:
            return cached
        context.deadline = min(context.deadline, self._clock() + 5.0)
        result = self._request(
            context,
            method="POST",
            path="",
            body={"brand_name": "chatgpt-meetings", "window_type": "mcp"},
            cancellation_event=cancellation_event,
            statsig_bootstrap=True,
        )
        policy = _decode_local_automation_policy(result.body)
        current_owner = record_owner_scope_fingerprint(context.auth)
        if current_owner is None or not hmac.compare_digest(current_owner, owner_scope):
            raise RecordMeetingInteractionsAuthError("ChatGPT account changed during the request.")
        _raise_if_interactions_cancelled(cancellation_event)
        with self._automation_policy_lock:
            self._automation_policy = _LocalAutomationPolicy(
                owner_scope=owner_scope,
                expires_at=self._clock() + 60.0,
                policy=policy,
            )
        return policy

    def peek_local_automation_policy(
        self,
        *,
        expected_owner_scope: str,
    ) -> AutomationPolicy | None:
        """Read an unexpired owner-bound rollout without authentication or network."""

        with self._automation_policy_lock:
            cached = self._automation_policy
            if (
                cached is not None
                and cached.expires_at > self._clock()
                and hmac.compare_digest(cached.owner_scope, expected_owner_scope)
            ):
                return cached.policy
        return None

    def update_settings(
        self,
        *,
        settings: Mapping[str, object],
        expected_account: tuple[str, str | None] | None = None,
        cancellation_event: threading.Event | None = None,
    ) -> HostedSettings:
        """Apply and verify a sparse hosted Record settings patch.

        Args:
            settings: One or more supported preference names and boolean values.
            expected_account: Optional account and subject authorized by the app request.
            cancellation_event: Optional caller cancellation signal.

        Returns:
            Validated hosted settings returned after the write.
        """

        if not settings:
            raise ValueError("setting update is invalid")
        if not set(settings).issubset(SETTING_NAMES):
            raise ValueError("setting update is invalid")
        normalized: dict[str, bool] = {}
        for setting in _SETTING_ORDER:
            if setting not in settings:
                continue
            enabled = settings[setting]
            if not isinstance(enabled, bool):
                raise ValueError("setting update is invalid")
            normalized[setting] = enabled
        context = self._begin_request(cancellation_event=cancellation_event)
        actual_account = (context.auth.account_id, context.auth.subject)
        if expected_account is not None and actual_account != expected_account:
            raise RecordMeetingInteractionsAuthError(
                "ChatGPT account changed before the settings update."
            )
        payload = self._request_json(
            context,
            method="PATCH",
            path="/settings/preferences",
            body=normalized,
            cancellation_event=cancellation_event,
        )
        projected = _project_settings(payload)
        for setting in _SETTING_ORDER:
            enabled = normalized.get(setting)
            if enabled is not None and not projected.confirms(setting, enabled):
                raise RecordMeetingInteractionsBackendError("Meetings did not apply the setting.")
        return projected

    def _begin_request(
        self,
        *,
        auth_client: ChatGPTAuthProvider | None = None,
        cancellation_event: threading.Event | None,
    ) -> _RequestContext:
        _raise_if_interactions_cancelled(cancellation_event)
        request_auth_client = auth_client or self._auth_client
        auth = request_auth_client.get_chatgpt_auth(
            refresh_token=False,
            cancellation_event=cancellation_event,
        )
        return _RequestContext(
            auth=auth,
            account_fingerprint=record_account_fingerprint(auth),
            deadline=self._clock() + self._timeout_seconds,
            auth_client=request_auth_client,
        )

    def _request_note_json(
        self,
        note_id: str,
        *,
        suffix: str,
        method: str,
        body: Mapping[str, object] | None = None,
        expected_account: tuple[str, str | None] | None = None,
        cancellation_event: threading.Event | None,
    ) -> dict[str, object]:
        context, raw_id = self._begin_note_request(
            note_id,
            expected_account=expected_account,
            cancellation_event=cancellation_event,
        )
        payload = self._request_json(
            context,
            method=method,
            path=_note_path(raw_id, suffix),
            body=body,
            cancellation_event=cancellation_event,
        )
        _require_matching_backend_id(payload, raw_id)
        return payload

    def _begin_note_request(
        self,
        note_id: str,
        *,
        cancellation_event: threading.Event | None,
        expected_account: tuple[str, str | None] | None = None,
        cleanup: bool = False,
    ) -> tuple[_RequestContext, str]:
        context = self._begin_request(cancellation_event=cancellation_event)
        context.cleanup = cleanup
        actual_account = (context.auth.account_id, context.auth.subject)
        if expected_account is not None and actual_account != expected_account:
            raise RecordMeetingInteractionsAuthError(
                "ChatGPT account changed before the meeting update."
            )
        raw_id = self._resolve_note_handle(
            context,
            note_id,
            cancellation_event=cancellation_event,
        )
        if MEETING_ID_PATTERN.fullmatch(raw_id) is None:
            raise RecordHandleError("Meeting details must be refreshed.")
        return context, raw_id

    def _resolve_note_handle(
        self,
        context: _RequestContext,
        note_id: str,
        *,
        cancellation_event: threading.Event | None,
    ) -> str:
        """Authorize a cold ID through its exact current-account detail endpoint."""

        try:
            return self._handle_registry.resolve(
                note_id,
                account_fingerprint=context.account_fingerprint,
            )
        except RecordHandleError:
            if PUBLIC_MEETING_ID_PATTERN.fullmatch(note_id) is None:
                raise
        read_source: RecordReadSource = "note"
        response = self._request(
            context,
            method="GET",
            path=_note_path(note_id),
            cancellation_event=cancellation_event,
            accepted_statuses=frozenset({404}),
        )
        if response.status == 404:
            raise RecordHandleError("Meeting details must be refreshed.")
        detail = _decode_response_object(response.body)
        # The Notes API may accept a legacy Meeting alias; never redirect an action.
        if detail.get("id") != note_id:
            raise RecordMeetingInteractionsBackendError("Meetings returned a mismatched meeting.")
        _require_matching_backend_id(detail, note_id)
        _raise_if_interactions_cancelled(cancellation_event)
        registered = self._handle_registry.register(
            note_id,
            account_fingerprint=context.account_fingerprint,
            source=read_source,
        )
        context.note_detail = detail
        return registered

    def _request_json(
        self,
        context: _RequestContext,
        *,
        method: str,
        path: str,
        body: Mapping[str, object] | None = None,
        cancellation_event: threading.Event | None,
        api_scope: Literal["record", "backend"] = "record",
    ) -> dict[str, object]:
        result = self._request(
            context,
            method=method,
            path=path,
            body=body,
            cancellation_event=cancellation_event,
            api_scope=api_scope,
        )
        return _decode_response_object(result.body)

    def _request(
        self,
        context: _RequestContext,
        *,
        method: str,
        path: str,
        body: Mapping[str, object] | None = None,
        cancellation_event: threading.Event | None,
        statsig_bootstrap: bool = False,
        api_scope: Literal["record", "backend"] = "record",
        accepted_statuses: frozenset[int] = frozenset(),
    ) -> RecordHTTPResult:
        encoded_body = _encode_request_body(body)
        while True:
            _raise_if_interactions_cancelled(cancellation_event)
            remaining = context.deadline - self._clock()
            if remaining <= 0:
                raise RecordMeetingInteractionsBackendError(
                    "Meetings request timed out.", failure_kind="timeout"
                )
            try:
                result, context.auth = authenticated_record_request(
                    self._transport,
                    context.auth,
                    context.auth_client,
                    url=(
                        STATSIG_BOOTSTRAP_URL
                        if statsig_bootstrap
                        else f"{BACKEND_API_ROOT if api_scope == 'backend' else RECORD_API_ROOT}{path}"
                    ),
                    timeout_seconds=remaining,
                    cancellation_event=cancellation_event,
                    method=method,
                    body=encoded_body,
                    statsig_bootstrap=statsig_bootstrap,
                    cleanup=context.cleanup,
                    quota_budget=context.quota_budget,
                )
            except RecordTransportCancelled:
                raise RecordMeetingInteractionsCancelled(
                    "Meetings request was cancelled."
                ) from None
            except RecordTransportTimeout:
                raise RecordMeetingInteractionsBackendError(
                    "Meetings request timed out.", failure_kind="timeout"
                ) from None
            except RecordTransportRateLimited:
                raise RecordMeetingInteractionsBackendError(
                    "Meetings is temporarily rate limited.",
                    failure_kind="http_429",
                    http_status=429,
                ) from None
            except RecordTransportBackendError:
                raise RecordMeetingInteractionsBackendError(
                    "Meetings could not be reached.", failure_kind="transport"
                ) from None
            _raise_if_interactions_cancelled(cancellation_event)
            if result.status == 401:
                if context.refreshed:
                    raise RecordMeetingInteractionsAuthRejected(
                        "ChatGPT authentication was rejected."
                    )
                refreshed_auth = refresh_chatgpt_auth_after_unauthorized(
                    context.auth_client,
                    context.auth,
                    cancellation_event=cancellation_event,
                )
                refreshed_fingerprint = record_account_fingerprint(refreshed_auth)
                if not hmac.compare_digest(
                    refreshed_fingerprint,
                    context.account_fingerprint,
                ):
                    raise RecordMeetingInteractionsAuthError(
                        "ChatGPT account changed during the request."
                    )
                context.auth = refreshed_auth
                context.refreshed = True
                continue
            if result.status in accepted_statuses:
                return result
            if result.status < 200 or result.status >= 300:
                failure_kind: RecordMeetingsBackendFailureKind = "invalid_response"
                if result.status == 408:
                    failure_kind = "timeout"
                elif result.status == 429:
                    failure_kind = "http_429"
                elif 400 <= result.status < 500:
                    failure_kind = "http_4xx"
                elif 500 <= result.status < 600:
                    failure_kind = "http_5xx"
                raise RecordMeetingInteractionsBackendError(
                    "Meetings returned a backend error.",
                    failure_kind=failure_kind,
                    http_status=result.status,
                )
            if len(result.body) > MAXIMUM_PAGE_RESPONSE_BYTES:
                raise RecordMeetingInteractionsBackendError(
                    "Meetings returned an oversized response."
                )
            return result

    def _publish_feedback_continuation(
        self,
        *,
        note_id: str,
        backend_token: str,
        account_fingerprint: bytes,
    ) -> str:
        with self._feedback_lock:
            now = self._clock()
            self._prune_feedback_continuations_locked(now)
            for _ in range(8):
                token = self._token_factory()
                if (
                    PAGE_TOKEN_PATTERN.fullmatch(token) is not None
                    and token not in self._feedback_continuations
                ):
                    break
            else:
                raise RecordMeetingInteractionsBackendError(
                    "Meetings could not create a feedback continuation."
                )
            while len(self._feedback_continuations) >= MAXIMUM_FEEDBACK_CONTINUATION_ENTRIES:
                oldest = min(
                    self._feedback_continuations,
                    key=lambda item: self._feedback_continuations[item].expires_at,
                )
                self._feedback_continuations.pop(oldest, None)
            self._feedback_continuations[token] = _FeedbackContinuation(
                public_meeting_id=note_id,
                backend_token=backend_token,
                account_fingerprint=account_fingerprint,
                expires_at=now + FEEDBACK_CONTINUATION_TTL_SECONDS,
            )
            return token

    def _resolve_feedback_continuation(
        self,
        token: str,
        *,
        note_id: str,
        account_fingerprint: bytes,
    ) -> _FeedbackContinuation:
        with self._feedback_lock:
            now = self._clock()
            self._prune_feedback_continuations_locked(now)
            continuation = self._feedback_continuations.get(token)
            if (
                continuation is None
                or continuation.public_meeting_id != note_id
                or not hmac.compare_digest(
                    continuation.account_fingerprint,
                    account_fingerprint,
                )
            ):
                raise RecordHandleError("Meeting feedback must be restarted.")
            return continuation

    def _prune_feedback_continuations_locked(self, now: float) -> None:
        expired = [
            token
            for token, continuation in self._feedback_continuations.items()
            if continuation.expires_at <= now
        ]
        for token in expired:
            self._feedback_continuations.pop(token, None)


def _meeting_path(raw_meeting_id: str, suffix: str | None = None) -> str:
    if MEETING_ID_PATTERN.fullmatch(raw_meeting_id) is None:
        raise RecordHandleError("Meeting details must be refreshed.")
    base = f"/meetings/{raw_meeting_id}"
    return f"{base}/{suffix}" if suffix is not None else base


def _note_path(raw_note_id: str, suffix: str | None = None) -> str:
    if MEETING_ID_PATTERN.fullmatch(raw_note_id) is None:
        raise RecordHandleError("Meeting details must be refreshed.")
    base = f"/notes/{raw_note_id}"
    return f"{base}/{suffix}" if suffix is not None else base


def _encode_request_body(value: Mapping[str, object] | None) -> bytes | None:
    if value is None:
        return None
    try:
        encoded = json.dumps(
            value,
            ensure_ascii=True,
            allow_nan=False,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError, UnicodeEncodeError) as exc:
        raise ValueError("request body is invalid") from exc
    if len(encoded) > MAXIMUM_REQUEST_BODY_BYTES:
        raise ValueError("request body is too large")
    return encoded


def _decode_response_object(body: bytes) -> dict[str, object]:
    try:
        value: object = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError, RecursionError) as exc:
        raise RecordMeetingInteractionsBackendError(
            "Meetings returned an invalid response."
        ) from exc
    if not is_json(value):
        raise RecordMeetingInteractionsBackendError("Meetings returned an invalid response.")
    return value


def _decode_discovery_rollout(body: bytes) -> MeetingsDiscoveryRollout:
    decoded = _decode_statsig_payload(body)
    return MeetingsDiscoveryRollout(
        sidebar_take_notes=statsig_gate_enabled(
            decoded, "chatgpt_meetings_sidebar_take_notes", "996630503"
        ),
        search_mentions=statsig_gate_enabled(
            decoded, "chatgpt_meetings_search_mentions", "3159725125"
        ),
    )


def _decode_local_automation_policy(body: bytes) -> AutomationPolicy:
    decoded = _decode_statsig_payload(body)
    if decoded is None:
        return AutomationPolicy(False)
    if not is_json(decoded) or not is_json(configs := decoded.get("dynamic_configs")):
        return AutomationPolicy(False)
    if "chatgpt_meetings_automation" in configs and "1642250802" in configs:
        return AutomationPolicy(False)
    plain_config = configs.get("chatgpt_meetings_automation")
    hashed_config = configs.get("1642250802")
    config = plain_config if plain_config is not None else hashed_config
    if config is None:
        return AutomationPolicy(False)
    if not is_json(config) or not is_json(values := config.get("value")):
        return AutomationPolicy(False)
    return AutomationPolicy(
        auto_record_popups_allowed=values.get("auto_record_popups_allowed") is True,
    )


def _require_matching_backend_id(payload: Mapping[str, object], raw_id: str) -> None:
    backend_id = payload.get("meetingId", payload.get("id"))
    if not isinstance(backend_id, str) or not hmac.compare_digest(backend_id, raw_id):
        raise RecordMeetingInteractionsBackendError("Meetings returned a mismatched meeting.")


def _project_note(
    note_id: str,
    raw_id: str,
    detail: Mapping[str, object],
    summary: Mapping[str, object],
    transcripts: Mapping[str, object],
) -> RecordMeetingNoteWire:
    _require_matching_backend_id(detail, raw_id)
    _require_matching_backend_id(summary, raw_id)
    _require_matching_backend_id(transcripts, raw_id)
    title = _required_string(detail.get("title"), maximum_bytes=4 * 1024)
    summary_markdown = _summary_markdown(summary)
    transcript = _project_transcript(transcripts, detail)
    meeting_chat = _project_meeting_chat(transcripts)
    result: RecordMeetingNoteWire = {
        "id": note_id,
        "title": title,
        "recordingStartTime": _optional_timestamp(detail.get("recordingStartTime")),
        "recordingEndTime": _optional_timestamp(detail.get("recordingEndTime")),
        "calendarStartTime": _optional_timestamp(detail.get("calendarStartTime")),
        "calendarEndTime": _optional_timestamp(detail.get("calendarEndTime")),
        "attendees": _project_people(detail.get("attendees"), require_email=False),
        "shareRecipients": _project_people(
            detail.get("shareRecipients"),
            require_email=True,
        ),
        "status": nonempty_string(detail.get("status"), maximum_bytes=128),
        "processingStatus": nonempty_string(
            detail.get("processingStatus"),
            maximum_bytes=128,
        ),
        "displayStatus": _project_status(detail),
        # ChatGPT permalinks embed the raw backend meeting id. Keep that id
        # process-local just like every other interaction lookup handle.
        "permalink": None,
        "summary": summary_markdown,
        "transcript": transcript,
        "canShareMeeting": True,
    }
    if result["displayStatus"] == "ready" and transcript["status"] == "pending":
        result["displayStatus"] = "processing"
    processing_stage = _project_processing_stage(detail, result["displayStatus"])
    if processing_stage is not None:
        result["processingStage"] = processing_stage
    processing_state = nonempty_string(detail.get("processingState"), maximum_bytes=128)
    if processing_state is not None:
        result["processingState"] = processing_state
    record_source = nonempty_string(detail.get("recordSource"), maximum_bytes=256)
    if record_source is not None:
        result["recordSource"] = record_source
    device_platform = _native_mobile_device_platform(
        record_source,
        detail.get("devicePlatform"),
    )
    if device_platform is not None:
        result["devicePlatform"] = device_platform
    if meeting_chat is not None:
        result["meetingChat"] = meeting_chat
    return result


def _project_private_note(
    note_id: str,
    raw_id: str,
    detail: Mapping[str, object],
    transcripts: Mapping[str, object],
) -> RecordMeetingNoteWire:
    _require_matching_backend_id(detail, raw_id)
    _require_matching_backend_id(transcripts, raw_id)
    transcript = _project_transcript(transcripts, detail)
    meeting_chat = _project_meeting_chat(transcripts)
    result: RecordMeetingNoteWire = {
        "id": note_id,
        "title": _required_string(detail.get("title"), maximum_bytes=4 * 1024),
        "recordingStartTime": _optional_timestamp(detail.get("meetingStartTime")),
        "recordingEndTime": _optional_timestamp(detail.get("meetingEndTime")),
        "calendarStartTime": None,
        "calendarEndTime": None,
        "attendees": [],
        "shareRecipients": _project_people(
            detail.get("sourceMeetingShareRecipients"),
            require_email=True,
        ),
        "status": nonempty_string(detail.get("status"), maximum_bytes=128),
        "processingStatus": None,
        "displayStatus": _project_status(detail),
        "permalink": None,
        "summary": nonempty_string(
            detail.get("summary"),
            maximum_bytes=MAXIMUM_TEXT_FIELD_BYTES,
            allow_controls=True,
        ),
        "transcript": transcript,
        "canShareMeeting": isinstance(detail.get("sourceMeetingShareRecipients"), list),
    }
    page_status = detail.get("summaryPageStatus")
    personal_notes_coming_soon = detail.get("personalNoteTakingComingSoon")
    if isinstance(personal_notes_coming_soon, bool):
        result["personalNoteTakingComingSoon"] = personal_notes_coming_soon
    if page_status in ("ready", "unavailable"):
        result["summaryPageStatus"] = "ready" if page_status == "ready" else "unavailable"
        page_url = nonempty_string(detail.get("summaryPageUrl"), maximum_bytes=2048)
        if page_url is not None and re.fullmatch(
            r"https://chatgpt\.com/space/[A-Za-z0-9_-]+", page_url
        ):
            result["summaryPageUrl"] = page_url
    if result["displayStatus"] == "ready" and transcript["status"] == "pending":
        result["displayStatus"] = "processing"
    processing_stage = _project_processing_stage(detail, result["displayStatus"])
    if processing_stage is not None:
        result["processingStage"] = processing_stage
    if meeting_chat is not None:
        result["meetingChat"] = meeting_chat
    return result


def _summary_markdown(summary: Mapping[str, object]) -> str | None:
    content = summary.get("content")
    if not is_json(content):
        return None
    return nonempty_string(
        content.get("bodyMarkdown"),
        maximum_bytes=MAXIMUM_TEXT_FIELD_BYTES,
        allow_controls=True,
    )


def _project_transcript(
    transcripts: Mapping[str, object],
    detail: Mapping[str, object],
) -> RecordMeetingTranscriptWire:
    rendered = transcripts.get("renderedTranscript")
    rendered_rows = _project_transcript_rows(
        rendered.get("rows") if is_json(rendered) else None,
        rendered=True,
    )
    entries: list[RecordMeetingTranscriptEntryWire] = _project_transcript_rows(
        transcripts.get("entries")
    )
    backend_status = transcripts.get("status")
    legacy_transcript = "status" not in transcripts and "entries" not in transcripts
    if legacy_transcript:
        entries = [
            {
                "speaker": row["speaker"],
                "message": row["message"],
                "timestamp": row["timestampLabel"],
                "offsetSeconds": row["offsetSeconds"],
            }
            for row in rendered_rows
        ]
    meeting_is_active = _project_status(detail) in (
        "joining",
        "waiting",
        "recording",
        "uploading",
        "processing",
    )
    if backend_status == "pending":
        status: RecordMeetingTranscriptStatus = "pending"
    elif backend_status == "preliminary":
        status = "preliminary"
    elif backend_status == "final":
        status = "final"
    elif backend_status == "unavailable":
        status = "unavailable"
    elif legacy_transcript and entries:
        status = "preliminary" if meeting_is_active else "final"
    elif meeting_is_active:
        status = "pending"
    else:
        status = "unavailable"
    return {
        "status": status,
        "entries": entries,
        "renderedTranscript": ({"rows": rendered_rows} if rendered_rows else None),
    }


def _project_meeting_chat(
    transcripts: Mapping[str, object],
) -> RecordMeetingTranscriptWire | None:
    feeds = transcripts.get("feeds")
    if not is_json_array(feeds) or len(feeds) > 128:
        return None
    for feed in feeds:
        if is_json(feed) and feed.get("id") == "meeting-chat-messages":
            entries = _project_transcript_rows(feed.get("entries"))
            return {
                "status": "final" if entries else "unavailable",
                "entries": entries,
                "renderedTranscript": None,
            }
    return None


@overload
def _project_transcript_rows(
    value: object,
    *,
    rendered: Literal[True],
) -> list[RecordMeetingRenderedTranscriptRowWire]: ...


@overload
def _project_transcript_rows(
    value: object,
    *,
    rendered: Literal[False] = False,
) -> list[RecordMeetingTranscriptEntryWire]: ...


def _project_transcript_rows(
    value: object,
    *,
    rendered: bool = False,
) -> list[RecordMeetingTranscriptEntryWire] | list[RecordMeetingRenderedTranscriptRowWire]:
    entries: list[RecordMeetingTranscriptEntryWire] = []
    rendered_rows: list[RecordMeetingRenderedTranscriptRowWire] = []
    if not is_json_array(value) or len(value) > MAXIMUM_COLLECTION_ROWS:
        return rendered_rows if rendered else entries
    for row in value:
        if not is_json(row):
            continue
        message = nonempty_string(
            row.get("message"),
            maximum_bytes=64 * 1024,
            allow_controls=True,
        )
        if message is None:
            continue
        speaker = nonempty_string(row.get("speaker"), maximum_bytes=512)
        timestamp = nonempty_string(
            row.get("timestampLabel" if rendered else "timestamp"),
            maximum_bytes=512,
        )
        offset_seconds = _optional_nonnegative_number(row.get("offsetSeconds"))
        if rendered:
            rendered_row: RecordMeetingRenderedTranscriptRowWire = {
                "speaker": speaker,
                "timestampLabel": timestamp,
                "message": message,
                "offsetSeconds": offset_seconds,
            }
            rendered_rows.append(rendered_row)
        else:
            entry: RecordMeetingTranscriptEntryWire = {
                "speaker": speaker,
                "message": message,
                "timestamp": timestamp,
                "offsetSeconds": offset_seconds,
            }
            entries.append(entry)
    return rendered_rows if rendered else entries


@overload
def _project_people(
    value: object,
    *,
    require_email: Literal[True],
) -> list[RecordMeetingShareRecipientWire]: ...


@overload
def _project_people(
    value: object,
    *,
    require_email: Literal[False],
) -> list[RecordMeetingPersonWire]: ...


def _project_people(
    value: object,
    *,
    require_email: bool,
) -> list[RecordMeetingPersonWire] | list[RecordMeetingShareRecipientWire]:
    people: list[RecordMeetingPersonWire] = []
    recipients: list[RecordMeetingShareRecipientWire] = []
    if not is_json_array(value) or len(value) > 500:
        return recipients if require_email else people
    for row in value:
        if not is_json(row):
            continue
        name = nonempty_string(row.get("name"), maximum_bytes=512)
        email = nonempty_string(row.get("email"), maximum_bytes=320)
        if require_email and email is None:
            continue
        if name is None and email is None:
            continue
        if email is not None and require_email:
            recipient: RecordMeetingShareRecipientWire = {
                "name": name,
                "email": email,
            }
            recipients.append(recipient)
        else:
            person: RecordMeetingPersonWire = {
                "name": name,
                "email": email,
            }
            people.append(person)
    return recipients if require_email else people


def _project_settings(payload: Mapping[str, object]) -> HostedSettings:
    result = HostedSettings(
        # Older backends do not advertise eligibility; keep bot controls hidden.
        bot_settings_available=_required_bool(
            payload.get("botSettingsAvailable", False), "botSettingsAvailable"
        ),
        feature_enabled=_required_bool(payload.get("featureEnabled"), "featureEnabled"),
        auto_record_enabled=_required_bool(
            payload.get("autoRecordEnabled"),
            "autoRecordEnabled",
        ),
        slack_notifications_enabled=_required_bool(
            payload.get("slackNotificationsEnabled"),
            "slackNotificationsEnabled",
        ),
        configured_feature_enabled=_required_bool(
            payload.get("configuredFeatureEnabled"), "configuredFeatureEnabled"
        ),
        configured_auto_record_enabled=_required_bool(
            payload.get("configuredAutoRecordEnabled"), "configuredAutoRecordEnabled"
        ),
        configured_slack_notifications_enabled=_required_bool(
            payload.get("configuredSlackNotificationsEnabled"),
            "configuredSlackNotificationsEnabled",
        ),
        local_recording_disabled=_required_bool(
            payload.get("localRecordingDisabled"),
            "localRecordingDisabled",
        ),
    )
    _require_private_response_size(result.to_wire())
    return result


def _validated_email(value: object) -> str:
    normalized = _required_string(value, maximum_bytes=320).strip()
    if (
        len(normalized) > 320
        or normalized.count("@") != 1
        or normalized.startswith("@")
        or normalized.endswith("@")
        or any(character.isspace() for character in normalized)
    ):
        raise ValueError("email is invalid")
    return normalized


def _project_note_share_eligibility(
    payload: Mapping[str, object],
    *,
    requested_email: str,
) -> RecordMeetingShareEligibilityWire:
    """Validate the note-rooted policy response without exposing backend ids."""

    scope = payload.get("scope")
    workspace_name_value = payload.get("workspaceName")
    member_value = payload.get("member")
    if scope == "personal":
        if (
            not set(payload).issubset({"scope", "workspaceName", "member"})
            or workspace_name_value is not None
            or member_value is not None
        ):
            raise RecordMeetingInteractionsBackendError(
                "Meetings returned an invalid share eligibility response."
            )
        return {
            "scope": "personal",
            "workspaceName": None,
            "member": None,
        }
    if scope != "workspace" or set(payload) not in (
        {"scope"},
        {"scope", "workspaceName"},
        {"scope", "member"},
        {"scope", "workspaceName", "member"},
    ):
        raise RecordMeetingInteractionsBackendError(
            "Meetings returned an invalid share eligibility response."
        )
    workspace_name = nonempty_string(workspace_name_value, maximum_bytes=512)
    if workspace_name_value is not None and workspace_name is None:
        raise RecordMeetingInteractionsBackendError(
            "Meetings returned an invalid share eligibility response."
        )
    member: RecordMeetingShareEligibilityMemberWire | None = None
    if member_value is not None:
        if (
            not requested_email
            or not is_json(member_value)
            or set(member_value)
            not in (
                {"email"},
                {"email", "name"},
            )
        ):
            raise RecordMeetingInteractionsBackendError(
                "Meetings returned an invalid share eligibility response."
            )
        try:
            member_email = _validated_email(member_value.get("email"))
        except (ValueError, RecordMeetingInteractionsBackendError) as exc:
            raise RecordMeetingInteractionsBackendError(
                "Meetings returned an invalid share eligibility response."
            ) from exc
        if member_email.casefold() != requested_email.casefold():
            raise RecordMeetingInteractionsBackendError(
                "Meetings returned an invalid share eligibility response."
            )
        member_name_value = member_value.get("name")
        member_name = nonempty_string(member_name_value, maximum_bytes=512)
        if member_name_value is not None and member_name is None:
            raise RecordMeetingInteractionsBackendError(
                "Meetings returned an invalid share eligibility response."
            )
        member = {"email": member_email, "name": member_name}
    return {
        "scope": "workspace",
        "workspaceName": workspace_name,
        "member": member,
    }


def _validated_feedback_text(value: object) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError("feedback text must be a string")
    normalized = value.strip()
    if not normalized:
        return None
    if len(normalized) > 2_000:
        raise ValueError("feedback text is too long")
    return normalized


def validate_feedback_gateway_arguments(arguments: Mapping[str, object]) -> None:
    """Validate the private gateway shape before dispatching feedback.

    Args:
        arguments: Untrusted app-gateway feedback arguments.

    Returns:
        None after every supported argument passes validation.

    Raises:
        ValueError: If an argument is missing, malformed, or unsupported.
    """

    if arguments.get("category") not in FEEDBACK_CATEGORIES:
        raise ValueError("category is invalid")
    if not isinstance(arguments.get("includeDebugArtifacts"), bool):
        raise ValueError("includeDebugArtifacts must be a boolean")
    feedback_text = arguments.get("feedbackText")
    if feedback_text is not None and (
        not isinstance(feedback_text, str) or len(feedback_text) > 2_000
    ):
        raise ValueError("feedbackText is invalid")
    continuation_token = arguments.get("feedbackContinuationToken")
    if continuation_token is not None:
        try:
            _validated_feedback_continuation_token(continuation_token)
        except ValueError as exc:
            raise ValueError("feedbackContinuationToken is invalid") from exc


def _validated_feedback_continuation_token(value: object) -> str:
    if not isinstance(value, str):
        raise ValueError("feedback continuation token must be a string")
    normalized = value.strip()
    if PAGE_TOKEN_PATTERN.fullmatch(normalized) is None:
        raise ValueError("feedback continuation token is invalid")
    return normalized


def _required_string(
    value: object,
    *,
    maximum_bytes: int,
    allow_controls: bool = False,
) -> str:
    normalized = nonempty_string(
        value,
        maximum_bytes=maximum_bytes,
        allow_controls=allow_controls,
    )
    if normalized is None:
        raise RecordMeetingInteractionsBackendError("Meetings returned an invalid response.")
    return normalized


def _optional_timestamp(value: object) -> str | None:
    normalized = nonempty_string(value, maximum_bytes=128)
    if normalized is None:
        return None
    candidate = normalized[:-1] + "+00:00" if normalized.endswith("Z") else normalized
    try:
        from datetime import datetime

        parsed = datetime.fromisoformat(candidate)
    except ValueError:
        return None
    return normalized if parsed.tzinfo is not None else None


def _optional_nonnegative_number(value: object) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    number = float(value)
    return number if math.isfinite(number) and number >= 0 else None


def _required_bool(value: object, field: str) -> bool:
    if not isinstance(value, bool):
        raise RecordMeetingInteractionsBackendError(f"Meetings returned invalid {field}.")
    return value


def _require_private_response_size(payload: Mapping[str, object]) -> None:
    try:
        size = len(
            json.dumps(
                payload,
                ensure_ascii=False,
                allow_nan=False,
                separators=(",", ":"),
            ).encode("utf-8")
        )
    except (TypeError, ValueError, UnicodeEncodeError) as exc:
        raise RecordMeetingInteractionsBackendError(
            "Meetings returned an invalid response."
        ) from exc
    if size > MAXIMUM_PRIVATE_RESPONSE_BYTES:
        raise RecordMeetingInteractionsBackendError("Meetings returned too much private data.")


def _raise_if_interactions_cancelled(event: threading.Event | None) -> None:
    if event is not None and event.is_set():
        raise RecordMeetingInteractionsCancelled("Meetings request was cancelled.")


__all__ = [
    "ACCOUNT_SCOPE_GENERATION_PATTERN",
    "DEFAULT_DAY_COUNT",
    "DEFAULT_DAY_OFFSET",
    "FEEDBACK_CATEGORIES",
    "GATEWAY_SETTING_NAMES",
    "MAXIMUM_TIMESTAMP_BYTES",
    "MEETING_ID_PATTERN",
    "PAGE_TOKEN_PATTERN",
    "RecordCalendarAuthError",
    "RecordCalendarBackendError",
    "RecordCalendarCancelled",
    "RecordCalendarClient",
    "RecordCalendarError",
    "RecordCalendarEvent",
    "RecordCalendarEventWire",
    "RecordCalendarResponseStatus",
    "RecordCalendarRefreshDisabled",
    "RecordCalendarView",
    "RecordMeetingInteractionsAuthError",
    "RecordMeetingInteractionsBackendError",
    "RecordMeetingInteractionsCancelled",
    "RecordMeetingInteractionsClient",
    "RecordMeetingInteractionsError",
    "RecordMeetingListItemWire",
    "RecordMeetingNote",
    "RecordMeetingsAuthError",
    "RecordMeetingsBackendError",
    "RecordMeetingsCancelled",
    "RecordMeetingsClient",
    "RecordMeetingsError",
    "RecordMeetingsPage",
    "RecordMeetingsPaginationResetRequired",
    "SETTING_NAMES",
    "parse_record_meeting_row",
    "parse_record_meetings_page",
    "validate_feedback_gateway_arguments",
]
