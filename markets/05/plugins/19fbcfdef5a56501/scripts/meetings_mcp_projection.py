"""Strict backend projections and app-only gateway helpers."""

from __future__ import annotations

import hmac
import json
import logging
import re
import secrets
import sys
import threading
from collections.abc import Callable, Mapping
from collections.abc import Set as AbstractSet
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Literal, TypeAlias, TypedDict, cast

import meetings_mcp
from codex_auth_client import (
    AuthCacheDiagnostics,
    AuthFailureReason,
    AuthMaterial,
    CodexAuthAccountChanged,
    CodexAuthAccountUnverified,
    CodexAuthUnavailable,
    chatgpt_auth_subject,
)
from companion_control_v2 import is_retry_upload_result, is_uploads_result, validate_definition
from meetings_analytics import PluginAnalyticsAcceptance, parse_analytics_event
from meetings_api_client import (
    RecordCalendarEventWire,
    RecordCalendarNotConnected,
    RecordCalendarRefreshDisabled,
    RecordCalendarView,
    RecordMeetingInteractionsAuthRejected,
    RecordMeetingsBackendFailureKind,
    RecordMeetingsPage,
)
from meetings_api_client_common import record_account_fingerprint, record_owner_scope_fingerprint
from meetings_api_client_transport import CONTINUATION_PAGE_LIMIT
from meetings_connection_migration import ConnectionMigrationResult
from meetings_metrics import (
    CLIENT_PERFORMANCE_OPERATIONS,
    CLIENT_PERFORMANCE_TRANSITIONS_BY_OPERATION,
    CLIENT_STREAMING_STATES,
    MAXIMUM_CLIENT_PERFORMANCE_DURATION_MILLISECONDS,
    measure_notes_lookup_stage,
    record_client_action_latency,
)
from meetings_projection_types import (
    CalendarSectionWire,
    HomeBootstrapWire,
    NotesPaginationWire,
    NotesSectionWire,
)
from meetings_prompt import build_resource_link
from meetings_schema import LOCAL_NOTES_REFRESH_TRIGGERS, JSONSchema, is_public_recording_session_id
from meetings_sentry import (
    MCP_SENTRY_BACKEND_FAILURE_REASONS,
    MCP_SENTRY_NOTIFICATIONS,
    MCP_SENTRY_OPERATIONS,
    MCP_SENTRY_PRESENTATIONS,
    MCP_SENTRY_SETTINGS_AUTH_FAILURE_REASONS,
    MCP_SENTRY_UPDATE_REASONS,
    McpSentryDiagnostics,
    report_mcp_ready,
    report_ui_opened,
    reset_notes_backend_error_episode,
    submit_user_feedback,
)
from meetings_settings import (
    CalendarConnectionsWire,
    ContextConnectionsWire,
    HostedSettingsWire,
    OnboardingProfileWire,
)
from record_meeting_interaction_types import (
    MeetingsActivityWire,
    RecordMeetingDeleteWire,
    RecordMeetingFeedbackWire,
    RecordMeetingNoteWire,
    RecordMeetingReprocessWire,
    RecordMeetingShareEligibilityWire,
    RecordMeetingShareWire,
)

from helpers import ACCOUNT_SCOPE_GENERATION_PATTERN, account_scope_generation, is_json

_WORKSPACE_OWNER_SCOPE_SECRET = secrets.token_bytes(32)
_WORKSPACE_OWNER_SCOPE_DOMAIN = b"chatgpt-meetings-workspace-owner-scope-v1\0"
_WORKSPACE_APP_INSTANCE_OWNER_SCOPE_DOMAIN = (
    b"chatgpt-meetings-workspace-owner-app-instance-scope-v1\0"
)
_WORKSPACE_APP_INSTANCE_ID_PATTERN = re.compile(r"^[a-f0-9]{64}$")


class NotesRecordingArguments(TypedDict, total=False):
    """Optional validated timestamp for read-only recording identity lookup."""

    recording_started_at: str


class NormalizedNotesPageArguments(NotesRecordingArguments, total=False):
    """Validated legacy Notes pagination or Calendar-section selection."""

    section: Literal["calendar"]
    initial_limit: int
    page_token: str


class _NoteMutationAccountArguments(TypedDict, total=False):
    expected_account: tuple[str, str | None]


@dataclass(frozen=True)
class LegacySnapshotGatewayRequest:
    """Validated compatibility request without an explicit operation name."""

    arguments: NormalizedNotesPageArguments


@dataclass(frozen=True)
class RoutedGatewayRequest:
    """Validated explicit gateway request and its operation-specific values."""

    request: str
    arguments: Mapping[str, object]
    app_instance_id: str | None = None


NormalizedGatewayRequest = LegacySnapshotGatewayRequest | RoutedGatewayRequest


class RecordingStopArguments(TypedDict):
    """Exact public recording session identifier required for companion v2 Stop."""

    expectedSessionId: str


PrivateMeetingsData: TypeAlias = (
    PluginAnalyticsAcceptance
    | MeetingsActivityWire
    | OnboardingProfileWire
    | AuthCacheDiagnostics
    | HomeBootstrapWire
    | NotesSectionWire
    | CalendarSectionWire
    | RecordMeetingDeleteWire
    | RecordMeetingNoteWire
    | RecordMeetingReprocessWire
    | RecordMeetingFeedbackWire
    | RecordMeetingShareWire
    | RecordMeetingShareEligibilityWire
    | HostedSettingsWire
    | CalendarConnectionsWire
    | ContextConnectionsWire
    | ConnectionMigrationResult
    | dict[str, object]
)

SettingsFailureReason: TypeAlias = (
    AuthFailureReason | RecordMeetingsBackendFailureKind | Literal["http_401"]
)


@dataclass(frozen=True, slots=True)
class PrivateMeetingsResponse:
    """One app-only gateway result before MCP metadata serialization."""

    request: str
    ok: bool
    data: PrivateMeetingsData | None = None
    error_kind: str | None = None
    retryable: bool = False
    owner_scope_generation: str | None = None
    # Telemetry only; the serialized response retains its auth error.
    backend_auth_rejected: bool = False
    retry_after_seconds: float | None = None
    failure_reason: SettingsFailureReason | None = None
    error_source: Literal["auth", "backend"] | None = None
    http_status: int | None = None


def _verified_cached_account_id() -> tuple[str, str | None] | None:
    """Read current process account ownership without starting an auth probe."""

    material = meetings_mcp.get_process_auth_manager().peek_cached_chatgpt_auth()
    return None if material is None else (material.account_id, material.subject)


def _retains_verified_account(
    initial_account_id: tuple[str, str | None] | None,
) -> bool:
    """Retain private UI only when the same account was verified throughout."""

    current_account_id = _verified_cached_account_id()
    return initial_account_id is not None and current_account_id == initial_account_id


def _establish_request_account(
    initial_account_id: tuple[str, str | None] | None,
    client: object,
    *,
    cancellation_event: threading.Event | None,
) -> tuple[str, str | None] | None:
    """Bind cold production requests before their account-scoped backend operation."""

    if initial_account_id is not None:
        return initial_account_id
    manager = meetings_mcp.get_process_auth_manager()
    if getattr(client, "_auth_client", None) is not manager:
        return None
    material = manager.get_chatgpt_auth(
        refresh_token=False,
        cancellation_event=cancellation_event,
    )
    return material.account_id, material.subject


def _observed_account_changed(
    initial_account_id: tuple[str, str | None] | None,
) -> bool:
    """Reject only an account boundary that has already been observed locally."""

    return initial_account_id is not None and not _retains_verified_account(initial_account_id)


def _establish_snapshot_account(
    initial_account_id: tuple[str, str | None] | None,
    request: str,
    *,
    cancellation_event: threading.Event | None,
) -> tuple[str, str | None] | None:
    """Capture production ownership before even the first cold backend snapshot."""

    if initial_account_id is not None:
        return initial_account_id
    if request == "notes.list":
        if meetings_mcp.read_backend_meetings_view is not read_backend_meetings_view:
            return None
        client = meetings_mcp.get_record_meetings_client()
    else:
        if meetings_mcp.read_backend_calendar_view is not read_backend_calendar_view:
            return None
        client = meetings_mcp.get_record_calendar_client()
    return _establish_request_account(
        initial_account_id,
        client,
        cancellation_event=cancellation_event,
    )


def workspace_owner_scope_generation(
    expected_account: tuple[str, str | None] | None,
    *,
    app_instance_id: str | None = None,
    cancellation_event: threading.Event | None = None,
) -> str | None:
    """Privately witness the original verified account without an auth probe."""

    if expected_account is None:
        return None
    if cancellation_event is not None and cancellation_event.is_set():
        raise meetings_mcp.CodexAuthCancelled("ChatGPT authentication was cancelled")
    material = cast(
        object,
        meetings_mcp.get_process_auth_manager().peek_cached_chatgpt_auth(),
    )
    if material is None:
        raise CodexAuthAccountUnverified("ChatGPT account could not be verified")
    if not isinstance(material, AuthMaterial):
        return None
    if (
        (material.account_id, material.subject) != expected_account
        or material.subject is None
        or chatgpt_auth_subject(material) != material.subject
    ):
        raise CodexAuthAccountUnverified("ChatGPT account could not be verified")
    account_fingerprint = record_account_fingerprint(material)
    if app_instance_id is None:
        generation = account_scope_generation(
            _WORKSPACE_OWNER_SCOPE_SECRET,
            account_fingerprint,
            domain=_WORKSPACE_OWNER_SCOPE_DOMAIN,
        )
    else:
        generation = account_scope_generation(
            account_fingerprint,
            bytes.fromhex(app_instance_id),
            domain=_WORKSPACE_APP_INSTANCE_OWNER_SCOPE_DOMAIN,
        )
    if cancellation_event is not None and cancellation_event.is_set():
        raise meetings_mcp.CodexAuthCancelled("ChatGPT authentication was cancelled")
    return generation


def read_backend_meetings_view(
    *,
    initial_limit: int | None = None,
    page_token: str | None = None,
    recording_started_at: str | None = None,
    cancellation_event: threading.Event | None = None,
    backend_failure_handler: Callable[[bool], None] | None = None,
    backend_auth_failure_handler: Callable[[], None] | None = None,
    backend_rate_limit_handler: Callable[[float], None] | None = None,
) -> NotesSectionWire:
    """Fetch production app Notes directly from the bounded Record backend client.

    Args:
        initial_limit: Optional bounded initial page size.
        page_token: Optional opaque continuation token.
        recording_started_at: Optional start timestamp for first-page identity reads.
        cancellation_event: Optional caller cancellation signal.
        backend_failure_handler: Private-only callback receiving safe retryability.
        backend_auth_failure_handler: Private-only signal for rejected refreshed auth.
        backend_rate_limit_handler: Private-only remaining server cooldown.

    Returns:
        A terminal Notes section for the app.
    """

    initial_account_id = _verified_cached_account_id()
    try:
        client = meetings_mcp.get_record_meetings_client()
        with measure_notes_lookup_stage("backend_auth"):
            initial_account_id = _establish_request_account(
                initial_account_id, client, cancellation_event=cancellation_event
            )
        correlation: NotesRecordingArguments = {}
        if recording_started_at is not None:
            correlation["recording_started_at"] = recording_started_at
        with measure_notes_lookup_stage("backend_page"):
            page = client.list_notes_page(
                initial_limit=initial_limit,
                page_token=page_token,
                **correlation,
                cancellation_event=cancellation_event,
            )
    except (meetings_mcp.CodexAuthCancelled, meetings_mcp.RecordMeetingsCancelled):
        raise
    except meetings_mcp.RecordMeetingsPaginationResetRequired:
        if page_token is not None:
            if not _retains_verified_account(initial_account_id):
                reset_notes_backend_error_episode()
                return _empty_notes_view("auth-error")
            recovered = read_backend_meetings_view(
                initial_limit=CONTINUATION_PAGE_LIMIT,
                cancellation_event=cancellation_event,
                backend_failure_handler=backend_failure_handler,
                backend_auth_failure_handler=backend_auth_failure_handler,
                backend_rate_limit_handler=backend_rate_limit_handler,
            )
            if not _retains_verified_account(initial_account_id):
                reset_notes_backend_error_episode()
                return _empty_notes_view("auth-error")
            if recovered["snapshotState"]["status"] in {"ready", "empty"}:
                recovered["notesPagination"]["lineageRestarted"] = True
            return recovered
        reset_notes_backend_error_episode()
        meetings_mcp.report_mcp_error(
            "notes",
            "invalid-response",
            mcp_build_timestamp=meetings_mcp.server_build_timestamp_utc(),
        )
        return _empty_notes_view("backend-error", reset_required=True)
    except CodexAuthAccountUnverified:
        reset_notes_backend_error_episode()
        report_mcp_ready(auth_settled=True)
        return _empty_notes_view("auth-error")
    except (CodexAuthUnavailable, meetings_mcp.RecordMeetingsBackendError) as error:
        if not _retains_verified_account(initial_account_id):
            reset_notes_backend_error_episode()
            return _empty_notes_view("auth-error")
        report_mcp_ready(auth_settled=True)
        if isinstance(error, CodexAuthUnavailable):
            failure_reason, retryable = "transport", True
        else:
            failure_reason = error.failure_kind
            if failure_reason not in MCP_SENTRY_BACKEND_FAILURE_REASONS:
                failure_reason = "invalid_response"
            retryable = error.retryable is True and failure_reason in {
                "timeout",
                "transport",
                "http_429",
                "http_5xx",
            }
        meetings_mcp.report_mcp_error(
            "notes",
            "backend",
            mcp_build_timestamp=meetings_mcp.server_build_timestamp_utc(),
            failure_reason=failure_reason,
            retryable=retryable,
        )
        if backend_failure_handler is not None:
            backend_failure_handler(retryable)
        if (
            isinstance(error, meetings_mcp.RecordMeetingsBackendError)
            and error.retry_after_seconds is not None
            and backend_rate_limit_handler is not None
        ):
            backend_rate_limit_handler(error.retry_after_seconds)
        return _empty_notes_view("backend-error")
    except (meetings_mcp.CodexAuthError, meetings_mcp.RecordMeetingsAuthError) as error:
        if (
            isinstance(error, meetings_mcp.RecordMeetingsAuthError)
            and backend_auth_failure_handler is not None
            and _retains_verified_account(initial_account_id)
        ):
            backend_auth_failure_handler()
        reset_notes_backend_error_episode()
        report_mcp_ready(auth_settled=True)
        return _empty_notes_view("auth-error")
    if _observed_account_changed(initial_account_id):
        reset_notes_backend_error_episode()
        return _empty_notes_view("auth-error")
    reset_notes_backend_error_episode()
    report_mcp_ready(auth_settled=True)
    return meetings_mcp.project_meetings_page(
        page,
        generated_at=_now_iso8601(),
        continuation_request=page_token is not None,
    )


def project_meetings_page(
    page: RecordMeetingsPage,
    *,
    generated_at: str,
    continuation_request: bool,
) -> NotesSectionWire:
    """Serialize one hydrated Notes page through the canonical UI DTO.

    Args:
        page: Hydrated and account-bound Notes page.
        generated_at: Timestamp exposed for this projection.
        continuation_request: Whether the page continues an existing list.

    Returns:
        The minimal Notes section consumed by the Meetings app.
    """

    projected_notes = [note.as_widget_row() for note in page.notes]
    for row in projected_notes:
        row["resourceLink"] = build_resource_link(
            row["id"], server_name=meetings_mcp.SERVER_NAME, resource_kind=page.read_source
        )
    return {
        "generatedAt": generated_at,
        "upcoming": [],
        "notes": projected_notes,
        "snapshotSection": "notes",
        "calendarAccountScopeGeneration": None,
        "calendarTruncated": False,
        "calendarStale": False,
        "recentRecording": None,
        "snapshotState": {
            "status": (
                "ready" if projected_notes or page.has_more or continuation_request else "empty"
            ),
        },
        "notesPagination": {
            "accountScopeGeneration": page.account_scope_generation,
            "hasMore": page.has_more,
            "nextPageToken": page.next_page_token,
            "truncated": page.truncated,
            "resetRequired": False,
        },
    }


def _empty_notes_pagination(*, reset_required: bool = False) -> NotesPaginationWire:
    return {
        "accountScopeGeneration": None,
        "hasMore": False,
        "nextPageToken": None,
        "truncated": False,
        "resetRequired": reset_required,
    }


def _empty_notes_view(
    status: str,
    *,
    reset_required: bool = False,
) -> NotesSectionWire:
    """Return a content-free terminal Notes section.

    Args:
        status: Safe terminal state exposed to the app.
        reset_required: Whether the app must discard its pagination lineage.

    Returns:
        A complete Notes section without meetings or private identifiers.
    """

    return {
        "generatedAt": None,
        "upcoming": [],
        "notes": [],
        "snapshotSection": "notes",
        "calendarAccountScopeGeneration": None,
        "calendarTruncated": False,
        "calendarStale": False,
        "recentRecording": None,
        "snapshotState": {"status": status},
        "notesPagination": _empty_notes_pagination(reset_required=reset_required),
    }


empty_notes_view = _empty_notes_view


def read_backend_calendar_view(
    *,
    day_count: int = 1,
    day_offset: int = 0,
    refresh: bool = False,
    include_private_metadata: bool = False,
    cancellation_event: threading.Event | None = None,
    not_connected_handler: Callable[[], None] | None = None,
    refresh_disabled_handler: Callable[[float], None] | None = None,
) -> CalendarSectionWire:
    """Fetch production app Upcoming directly from the Record Calendar backend.

    Args:
        day_count: Number of local Calendar days to request.
        day_offset: Offset from the current local day.
        refresh: Whether an explicit user refresh should poll the source first.
        include_private_metadata: Whether to retain event metadata for the
            authenticated app-only response.
        cancellation_event: Optional caller cancellation signal.
        not_connected_handler: Report a confirmed missing connector to the private gateway.
        refresh_disabled_handler: Report a Calendar-only server pause to the private gateway.

    Returns:
        A terminal Calendar section for the app.
    """

    initial_account_id = _verified_cached_account_id()
    try:
        client = meetings_mcp.get_record_calendar_client()
        initial_account_id = _establish_request_account(
            initial_account_id, client, cancellation_event=cancellation_event
        )
        if refresh:
            view = client.list_upcoming(
                day_count=day_count,
                day_offset=day_offset,
                refresh=True,
                cancellation_event=cancellation_event,
            )
        else:
            view = client.list_upcoming(
                day_count=day_count,
                day_offset=day_offset,
                cancellation_event=cancellation_event,
            )
    except (meetings_mcp.CodexAuthCancelled, meetings_mcp.RecordCalendarCancelled):
        raise
    except CodexAuthAccountUnverified:
        return _empty_calendar_view(
            "auth-error",
            day_count=day_count,
            day_offset=day_offset,
        )
    except RecordCalendarNotConnected:
        if not _retains_verified_account(initial_account_id):
            return _empty_calendar_view("auth-error", day_count=day_count, day_offset=day_offset)
        if not_connected_handler is not None:
            not_connected_handler()
        return _empty_calendar_view("backend-error", day_count=day_count, day_offset=day_offset)
    except (CodexAuthUnavailable, meetings_mcp.RecordCalendarBackendError) as error:
        if not _retains_verified_account(initial_account_id):
            return _empty_calendar_view(
                "auth-error",
                day_count=day_count,
                day_offset=day_offset,
            )
        if isinstance(error, RecordCalendarRefreshDisabled):
            if refresh_disabled_handler is not None:
                refresh_disabled_handler(error.retry_after_seconds)
        else:
            meetings_mcp.report_mcp_error(
                "calendar",
                "backend",
                mcp_build_timestamp=meetings_mcp.server_build_timestamp_utc(),
            )
        unavailable = _empty_calendar_view(
            "backend-error", day_count=day_count, day_offset=day_offset
        )
        try:
            generation = meetings_mcp.calendar_account_scope_generation()
            if type(generation) is str and ACCOUNT_SCOPE_GENERATION_PATTERN.fullmatch(generation):
                unavailable["calendarAccountScopeGeneration"] = generation
        except meetings_mcp.CodexAuthCancelled:
            raise
        except CodexAuthAccountUnverified:
            return _empty_calendar_view("auth-error", day_count=day_count, day_offset=day_offset)
        except CodexAuthUnavailable:
            if not _retains_verified_account(initial_account_id):
                return _empty_calendar_view(
                    "auth-error", day_count=day_count, day_offset=day_offset
                )
        except meetings_mcp.CodexAuthError:
            return _empty_calendar_view("auth-error", day_count=day_count, day_offset=day_offset)
        except (meetings_mcp.ControlUnavailable, ValueError):
            pass
        return unavailable
    except (meetings_mcp.CodexAuthError, meetings_mcp.RecordCalendarAuthError):
        return _empty_calendar_view(
            "auth-error",
            day_count=day_count,
            day_offset=day_offset,
        )
    if _observed_account_changed(initial_account_id):
        return _empty_calendar_view(
            "auth-error",
            day_count=day_count,
            day_offset=day_offset,
        )
    return meetings_mcp.project_calendar_view(
        view,
        day_count=day_count,
        day_offset=day_offset,
        include_private_metadata=include_private_metadata,
    )


def project_calendar_events_by_date(
    events: list[RecordCalendarEventWire],
    start_date: str,
    end_date: str,
) -> dict[str, list[RecordCalendarEventWire]]:
    """Preserve every requested local date, including verified empty dates."""

    current = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)
    events_by_date: dict[str, list[RecordCalendarEventWire]] = {}
    while current < end:
        events_by_date[current.isoformat()] = []
        current += timedelta(days=1)

    for event in events:
        event_date = (
            datetime.fromisoformat(event["startTime"].replace("Z", "+00:00"))
            .astimezone()
            .date()
            .isoformat()
        )
        if event_date in events_by_date:
            events_by_date[event_date].append(event)
    return events_by_date


def _empty_calendar_view(
    status: str,
    *,
    day_count: int,
    day_offset: int,
) -> CalendarSectionWire:
    """Return a content-free terminal Calendar section.

    Args:
        status: Safe terminal state exposed to the app.
        day_count: Number of local Calendar days represented by the result.
        day_offset: Offset from the current local Calendar day.

    Returns:
        A complete Calendar section without events or private identifiers.
    """

    return {
        "generatedAt": None,
        "upcoming": [],
        "notes": [],
        "snapshotSection": "calendar",
        "calendarAccountScopeGeneration": None,
        "calendarDayCount": day_count,
        "calendarDayOffset": day_offset,
        "calendarTruncated": False,
        "calendarStale": False,
        "recentRecording": None,
        "snapshotState": {"status": status},
        "notesPagination": _empty_notes_pagination(),
    }


def project_calendar_view(
    view: RecordCalendarView,
    *,
    day_count: int,
    day_offset: int,
    include_private_metadata: bool,
) -> CalendarSectionWire:
    """Serialize one hydrated Calendar view through the canonical UI DTO.

    Args:
        view: Hydrated and account-bound Calendar view.
        day_count: Requested number of Calendar days.
        day_offset: Requested offset from the current local day.
        include_private_metadata: Whether to retain private event metadata for
            the authenticated app-only response.

    Returns:
        The minimal Calendar section consumed by the Meetings app.
    """

    projected_events = [
        event.as_widget_row(include_private_metadata=include_private_metadata)
        for event in view.events
    ]
    return {
        "generatedAt": view.generated_at,
        "upcoming": projected_events,
        "notes": [],
        "snapshotSection": "calendar",
        "calendarAccountScopeGeneration": view.account_scope_generation,
        "calendarDayCount": day_count,
        "calendarDayOffset": day_offset,
        "calendarTruncated": view.truncated,
        "calendarStale": view.stale,
        "recentRecording": None,
        "snapshotState": {
            "status": "ready" if projected_events else "empty",
        },
        "notesPagination": _empty_notes_pagination(),
    }


def _now_iso8601() -> str:
    return (
        meetings_mcp.datetime.now(meetings_mcp.timezone.utc)
        .isoformat(timespec="milliseconds")
        .replace("+00:00", "Z")
    )


def require_empty_arguments(name: str, arguments: Mapping[str, object]) -> None:
    """Require one tool call to have no arguments.

    Args:
        name: Tool name used in the validation error.
        arguments: Candidate tool arguments.

    Returns:
        None after successful validation.

    Raises:
        InvalidArguments: If any argument is present.
    """

    if arguments:
        raise meetings_mcp.InvalidArguments(f"{name} requires an empty argument object")


def normalize_local_recording_control(
    arguments: Mapping[str, object],
) -> RecordingStopArguments:
    """Validate the exact public session fence for companion v2 Stop.

    Args:
        arguments: Candidate app-supplied control arguments.

    Returns:
        The exact app-facing companion v2 Stop arguments.

    Raises:
        InvalidArguments: If the fence is missing, extra, or malformed.
    """

    if set(arguments) != {"expectedSessionId"}:
        raise meetings_mcp.InvalidArguments("recording control arguments are malformed")
    if not is_public_recording_session_id(arguments["expectedSessionId"]):
        raise meetings_mcp.InvalidArguments(
            "expectedSessionId must be a valid recording session id"
        )
    expected_session_id = arguments["expectedSessionId"]
    assert isinstance(expected_session_id, str)
    return {"expectedSessionId": expected_session_id}


def require_tool_arguments(
    name: str,
    arguments: Mapping[str, object],
    required: tuple[str, ...],
    optional: tuple[str, ...] = (),
) -> None:
    """Require exactly the declared tool argument names.

    Args:
        name: Tool name used in validation errors.
        arguments: Candidate tool arguments.
        required: Required argument names.
        optional: Optional argument names.

    Returns:
        None after successful validation.

    Raises:
        InvalidArguments: If a required argument is absent or another argument
            is unsupported.
    """

    unknown = set(arguments) - set(required) - set(optional)
    missing = [key for key in required if key not in arguments]
    if unknown or missing:
        if missing:
            raise meetings_mcp.InvalidArguments(f"{name} requires argument: {missing[0]}")
        raise meetings_mcp.InvalidArguments(f"{name} does not support argument: {min(unknown)}")


def normalize_local_notes_page_arguments(
    arguments: Mapping[str, object],
) -> NormalizedNotesPageArguments:
    """Validate legacy Notes pagination or Calendar-section selection.

    Args:
        arguments: Candidate legacy snapshot arguments.

    Returns:
        Validated internal pagination names and values.

    Raises:
        InvalidArguments: If arguments conflict or exceed their bounds.
    """

    allowed = {"section", "initialLimit", "pageToken", "recordingStartedAt"}
    unknown = set(arguments) - allowed
    if unknown:
        raise meetings_mcp.InvalidArguments(
            f"chatgpt_meetings_get_snapshot does not support argument: {min(unknown)}"
        )
    correlation: NormalizedNotesPageArguments = {}
    if "recordingStartedAt" in arguments:
        value = arguments["recordingStartedAt"]
        if (
            not isinstance(value, str)
            or len(value) != 24
            or "section" in arguments
            or "pageToken" in arguments
        ):
            raise meetings_mcp.InvalidArguments("recordingStartedAt requires an initial Notes page")
        try:
            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError as error:
            raise meetings_mcp.InvalidArguments(
                "recordingStartedAt must be a UTC timestamp"
            ) from error
        correlation["recording_started_at"] = value
    if "section" in arguments:
        if arguments["section"] != "calendar":
            raise meetings_mcp.InvalidArguments("section must be calendar")
        if "initialLimit" in arguments or "pageToken" in arguments:
            raise meetings_mcp.InvalidArguments(
                "section and Notes pagination arguments are mutually exclusive"
            )
        return {"section": "calendar"}
    if "initialLimit" in arguments and "pageToken" in arguments:
        raise meetings_mcp.InvalidArguments("initialLimit and pageToken are mutually exclusive")
    if "pageToken" in arguments:
        page_token = arguments["pageToken"]
        if not isinstance(page_token, str):
            raise meetings_mcp.InvalidArguments("pageToken must be a string")
        try:
            encoded = page_token.encode("ascii")
        except UnicodeEncodeError as exc:
            raise meetings_mcp.InvalidArguments("pageToken is malformed") from exc
        if (
            len(encoded) > meetings_mcp.LOCAL_NOTES_PAGE_TOKEN_MAXIMUM_BYTES
            or meetings_mcp.LOCAL_NOTES_PAGE_TOKEN_PATTERN.fullmatch(page_token) is None
        ):
            raise meetings_mcp.InvalidArguments("pageToken is malformed")
        return {"page_token": page_token}
    if "initialLimit" in arguments:
        initial_limit = arguments["initialLimit"]
        if (
            isinstance(initial_limit, bool)
            or not isinstance(initial_limit, int)
            or not meetings_mcp.LOCAL_NOTES_INITIAL_LIMIT_MINIMUM
            <= initial_limit
            <= meetings_mcp.LOCAL_NOTES_INITIAL_LIMIT_MAXIMUM
        ):
            raise meetings_mcp.InvalidArguments("initialLimit must be an integer from 1 to 40")
        return {"initial_limit": initial_limit, **correlation}
    return correlation


def normalize_record_settings_update(
    arguments: Mapping[str, object],
    *,
    allowed_names: AbstractSet[str],
) -> dict[str, bool]:
    """Validate one sparse settings patch.

    Args:
        arguments: Candidate preference names and boolean values.
        allowed_names: Preferences supported by the requesting surface.

    Returns:
        A nonempty sparse boolean patch.

    Raises:
        InvalidArguments: If the patch is empty or contains unsupported values.
    """

    unknown = arguments.keys() - allowed_names
    if unknown:
        raise meetings_mcp.InvalidArguments(
            f"settings.update does not support argument: {min(unknown)}"
        )
    if not arguments:
        raise meetings_mcp.InvalidArguments("settings.update requires at least one setting")
    normalized: dict[str, bool] = {}
    for setting, enabled in arguments.items():
        if not isinstance(enabled, bool):
            raise meetings_mcp.InvalidArguments(f"{setting} must be a boolean")
        normalized[setting] = enabled
    return normalized


def normalize_local_ui_gateway_request(
    arguments: Mapping[str, object],
) -> NormalizedGatewayRequest:
    """Validate one app UI request into an explicit internal request model.

    Args:
        arguments: Untrusted app gateway arguments.

    Returns:
        A legacy snapshot request or an explicitly routed gateway request.

    Raises:
        InvalidArguments: If the request name or operation-specific values are
            unsupported or malformed.
    """

    request = arguments.get("request")
    if request is None:
        return LegacySnapshotGatewayRequest(
            arguments=normalize_local_notes_page_arguments(arguments),
        )
    if not isinstance(request, str) or request not in meetings_mcp.LOCAL_UI_REQUEST_KINDS:
        raise meetings_mcp.InvalidArguments("request is unsupported")

    allowed_by_request = {
        "analytics.track": {"request", "appInstanceId", "ownerScopeGeneration", "event"},
        "home.bootstrap": {"request", "appInstanceId"},
        "local.getUploads": {"request", "appInstanceId", "ownerScopeGeneration", "offset"},
        "local.retryUpload": {"request", "appInstanceId", "ownerScopeGeneration", "recordingId"},
        "diagnostics.get": {"request", "appInstanceId"},
        "notes.list": {
            "request",
            "appInstanceId",
            "initialLimit",
            "pageToken",
            "refreshTrigger",
            "recordingStartedAt",
        },
        "calendar.list": {
            "request",
            "appInstanceId",
            "startDate",
            "endDate",
            "refresh",
        },
        "note.get": {"request", "noteId"},
        "note.delete": {"request", "noteId", "confirmed"},
        "note.reprocess": {"request", "noteId"},
        "note.share": {"request", "noteId", "email"},
        "note.shareEligibility": {"request", "noteId", "email"},
        "note.feedback": {
            "request",
            "noteId",
            "category",
            "feedbackText",
            "feedbackContinuationToken",
            "includeDebugArtifacts",
        },
        "activity.get": {"request"},
        "activity.view": {"request", "appInstanceId", "ownerScopeGeneration"},
        "settings.get": {"request"},
        "settings.getTarget": {"request"},
        "onboarding.profile": {"request", "appInstanceId"},
        "calendar.connections": {"request"},
        "context.connections": {"request"},
        "connection.ensure": {"request", "appInstanceId", "ownerScopeGeneration"},
        "settings.update": {"request", *meetings_mcp.GATEWAY_SETTING_NAMES},
        "ui.submitFeedback": {"request", "appInstanceId", "feedbackText"},
        "ui.reportError": {
            "request",
            "stage",
            "kind",
            "uiVersion",
            "presentation",
            "operation",
            "notification",
            "updateReason",
        },
        "ui.reportPerformance": {
            "request",
            "appInstanceId",
            "ownerScopeGeneration",
            "operation",
            "transition",
            "durationMs",
            "streaming",
        },
        "local.getStagedUpdateStatus": {"request"},
        "local.forceStart": {"request", "confirmed", "calendarContext"},
        "local.requestMicrophone": {"request"},
        "local.requestSystemAudio": {"request"},
        "local.recheckAudio": {"request"},
        "local.openMicrophoneSettings": {"request"},
        "local.openSystemAudioSettings": {"request"},
        "local.installAndLaunch": {"request"},
        "local.applyStagedUpdate": {"request", "confirmed"},
        "local.getSettings": {"request"},
        "local.updateSettings": {
            "request",
            "calendarRemindersEnabled",
            "soundEffectsEnabled",
            "meetingDetectionEnabled",
        },
        "prompt.note": {"request", "meetingId", "title"},
    }
    required_by_request = {
        "analytics.track": {"request", "appInstanceId", "ownerScopeGeneration", "event"},
        "home.bootstrap": {"request"},
        "local.getUploads": {"request"},
        "local.retryUpload": {"request", "ownerScopeGeneration", "recordingId"},
        "diagnostics.get": {"request"},
        "notes.list": {"request"},
        "calendar.list": {"request", "startDate", "endDate"},
        "note.get": {"request", "noteId"},
        "note.delete": {"request", "noteId", "confirmed"},
        "note.reprocess": {"request", "noteId"},
        "note.share": {"request", "noteId", "email"},
        "note.shareEligibility": {"request", "noteId"},
        "note.feedback": {
            "request",
            "noteId",
            "category",
            "includeDebugArtifacts",
        },
        "activity.get": {"request"},
        "activity.view": {"request", "appInstanceId", "ownerScopeGeneration"},
        "settings.get": {"request"},
        "settings.getTarget": {"request"},
        "onboarding.profile": {"request"},
        "calendar.connections": {"request"},
        "context.connections": {"request"},
        "connection.ensure": {"request", "ownerScopeGeneration"},
        "settings.update": {"request"},
        "ui.submitFeedback": {"request", "feedbackText"},
        "ui.reportError": {"request", "stage", "kind", "uiVersion"},
        "ui.reportPerformance": {
            "request",
            "operation",
            "transition",
            "durationMs",
            "streaming",
        },
        "local.getStagedUpdateStatus": {"request"},
        "local.forceStart": {"request", "confirmed"},
        "local.requestMicrophone": {"request"},
        "local.requestSystemAudio": {"request"},
        "local.recheckAudio": {"request"},
        "local.openMicrophoneSettings": {"request"},
        "local.openSystemAudioSettings": {"request"},
        "local.installAndLaunch": {"request"},
        "local.applyStagedUpdate": {"request", "confirmed"},
        "local.getSettings": {"request"},
        "local.updateSettings": {"request"},
        "prompt.note": {"request", "meetingId", "title"},
    }
    unknown = set(arguments) - allowed_by_request[request]
    missing = required_by_request[request] - set(arguments)
    if unknown:
        raise meetings_mcp.InvalidArguments(f"{request} does not support argument: {min(unknown)}")
    if missing:
        raise meetings_mcp.InvalidArguments(f"{request} requires argument: {min(missing)}")

    app_instance_id: str | None = None
    if "appInstanceId" in arguments:
        candidate = arguments["appInstanceId"]
        if (
            not isinstance(candidate, str)
            or _WORKSPACE_APP_INSTANCE_ID_PATTERN.fullmatch(candidate) is None
        ):
            raise meetings_mcp.InvalidArguments("appInstanceId is invalid")
        app_instance_id = candidate

    normalized = {
        key: value
        for key, value in arguments.items()
        if key not in {"request", "appInstanceId", "refreshTrigger"}
    }
    if request in {
        "activity.view",
        "local.getUploads",
        "local.retryUpload",
        "connection.ensure",
        "analytics.track",
    }:
        if "ownerScopeGeneration" in normalized:
            owner_generation = normalized["ownerScopeGeneration"]
            if (
                not isinstance(owner_generation, str)
                or re.fullmatch(ACCOUNT_SCOPE_GENERATION_PATTERN, owner_generation) is None
            ):
                raise meetings_mcp.InvalidArguments("ownerScopeGeneration is invalid")
        if request == "analytics.track":
            try:
                normalized["event"] = dict(parse_analytics_event(normalized["event"]))
            except ValueError:
                raise meetings_mcp.InvalidArguments("analytics.track event is invalid") from None
        if request == "local.getUploads":
            offset = normalized.get("offset", 0)
            if not validate_definition("SafeInteger", offset):
                raise meetings_mcp.InvalidArguments("offset is invalid")
            if "ownerScopeGeneration" not in normalized and (
                app_instance_id is None or offset != 0
            ):
                raise meetings_mcp.InvalidArguments(
                    "Upload recovery bootstrap requires appInstanceId and offset zero"
                )
            normalized["offset"] = offset
        elif request == "local.retryUpload" and not validate_definition(
            "UploadRecordingId", normalized["recordingId"]
        ):
            raise meetings_mcp.InvalidArguments("recordingId is invalid")
        return RoutedGatewayRequest(
            request=request, arguments=normalized, app_instance_id=app_instance_id
        )
    if request == "settings.update":
        return RoutedGatewayRequest(
            request=request,
            arguments=normalize_record_settings_update(
                normalized, allowed_names=meetings_mcp.GATEWAY_SETTING_NAMES
            ),
        )
    if request == "ui.submitFeedback":
        feedback_text = normalized["feedbackText"]
        if (
            not isinstance(feedback_text, str)
            or not feedback_text.strip()
            or len(feedback_text) > 2_000
        ):
            raise meetings_mcp.InvalidArguments("feedbackText must contain 1 to 2000 characters")
        return RoutedGatewayRequest(
            request=request, arguments={"feedbackText": feedback_text.strip()}
        )
    if request == "ui.reportPerformance":
        operation = normalized["operation"]
        transition = normalized["transition"]
        duration_milliseconds = normalized["durationMs"]
        streaming = normalized["streaming"]
        if not isinstance(operation, str) or operation not in CLIENT_PERFORMANCE_OPERATIONS:
            raise meetings_mcp.InvalidArguments("performance operation is invalid")
        if not isinstance(
            transition, str
        ) or transition not in CLIENT_PERFORMANCE_TRANSITIONS_BY_OPERATION.get(operation, ()):
            raise meetings_mcp.InvalidArguments("performance transition is invalid")
        if (
            isinstance(duration_milliseconds, bool)
            or not isinstance(duration_milliseconds, int)
            or duration_milliseconds < 0
            or duration_milliseconds > MAXIMUM_CLIENT_PERFORMANCE_DURATION_MILLISECONDS
        ):
            raise meetings_mcp.InvalidArguments("performance duration is invalid")
        if not isinstance(streaming, str) or streaming not in CLIENT_STREAMING_STATES:
            raise meetings_mcp.InvalidArguments("performance streaming state is invalid")
        if transition in {"surface_active", "surface_load_failure"} and (
            duration_milliseconds != 0 or streaming != "unknown"
        ):
            raise meetings_mcp.InvalidArguments("surface health observation is invalid")
        owner_generation = normalized.get("ownerScopeGeneration")
        if owner_generation is not None and (
            not isinstance(owner_generation, str)
            or re.fullmatch(ACCOUNT_SCOPE_GENERATION_PATTERN, owner_generation) is None
        ):
            raise meetings_mcp.InvalidArguments("ownerScopeGeneration is invalid")
        if transition in {"surface_active", "surface_load_failure"} and (
            owner_generation is None or app_instance_id is None
        ):
            raise meetings_mcp.InvalidArguments("surface health requires verified ownership")
        return RoutedGatewayRequest(
            request=request, arguments=normalized, app_instance_id=app_instance_id
        )
    if request == "ui.reportError":
        stage = normalized["stage"]
        kind = normalized["kind"]
        ui_version = normalized["uiVersion"]
        if not isinstance(stage, str) or stage not in meetings_mcp.MCP_SENTRY_STAGES:
            raise meetings_mcp.InvalidArguments("stage is invalid")
        if not isinstance(kind, str) or kind not in meetings_mcp.MCP_SENTRY_KINDS:
            raise meetings_mcp.InvalidArguments("kind is invalid")
        if (
            not isinstance(ui_version, str)
            or meetings_mcp.re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._+-]{0,79}", ui_version) is None
        ):
            raise meetings_mcp.InvalidArguments("uiVersion is invalid")
        optional_context = {
            "presentation": MCP_SENTRY_PRESENTATIONS,
            "operation": MCP_SENTRY_OPERATIONS,
            "notification": MCP_SENTRY_NOTIFICATIONS,
            "updateReason": MCP_SENTRY_UPDATE_REASONS,
        }
        for context_key, allowed_values in optional_context.items():
            if context_key not in normalized:
                continue
            context_value = normalized[context_key]
            if not isinstance(context_value, str) or context_value not in allowed_values:
                raise meetings_mcp.InvalidArguments(f"{context_key} is invalid")
        if "updateReason" in normalized and (
            stage != "popup"
            or kind != "update"
            or normalized.get("operation") != "update"
            or normalized.get("notification") != "update_failed"
            or normalized.get("presentation") not in {None, "dialog"}
        ):
            raise meetings_mcp.InvalidArguments("updateReason is invalid")
        return RoutedGatewayRequest(request=request, arguments=normalized)
    if request == "local.getStagedUpdateStatus":
        return RoutedGatewayRequest(request=request, arguments={})
    if request == "local.forceStart":
        if normalized["confirmed"] is not True:
            raise meetings_mcp.InvalidArguments("force start requires explicit confirmation")
        return RoutedGatewayRequest(
            request=request,
            arguments={
                "confirmed": True,
                **(
                    {"calendarContext": normalized["calendarContext"]}
                    if "calendarContext" in normalized
                    else {}
                ),
            },
        )
    if request == "local.applyStagedUpdate":
        if normalized["confirmed"] is not True:
            raise meetings_mcp.InvalidArguments("staged update requires an explicit user gesture")
        return RoutedGatewayRequest(request=request, arguments={"confirmed": True})
    if request == "local.updateSettings":
        return RoutedGatewayRequest(
            request=request,
            arguments=normalize_settings_patch(normalized),
        )
    if request == "prompt.note":
        return RoutedGatewayRequest(
            request=request,
            arguments={
                "meetingId": meetings_mcp.require_prompt_meeting_id(normalized["meetingId"]),
                "title": meetings_mcp.require_prompt_title(normalized["title"]),
            },
        )
    if request in meetings_mcp.LOCAL_UI_NATIVE_REQUEST_TARGETS:
        return RoutedGatewayRequest(request=request, arguments={})
    if request in {"home.bootstrap", "diagnostics.get"}:
        return RoutedGatewayRequest(request=request, arguments={}, app_instance_id=app_instance_id)
    if request == "notes.list":
        if "refreshTrigger" in arguments and arguments["refreshTrigger"] not in (
            LOCAL_NOTES_REFRESH_TRIGGERS
        ):
            raise meetings_mcp.InvalidArguments("refreshTrigger is invalid")
        return RoutedGatewayRequest(
            request=request,
            arguments=normalize_local_notes_page_arguments(normalized),
            app_instance_id=app_instance_id,
        )
    if request == "calendar.list":
        raw_start_date = normalized["startDate"]
        raw_end_date = normalized["endDate"]
        if not isinstance(raw_start_date, str) or not isinstance(raw_end_date, str):
            raise meetings_mcp.InvalidArguments("calendar.list dates must be local ISO dates")
        try:
            start_date = date.fromisoformat(raw_start_date)
            end_date = date.fromisoformat(raw_end_date)
        except ValueError as error:
            raise meetings_mcp.InvalidArguments(
                "calendar.list dates must be local ISO dates"
            ) from error
        if start_date.isoformat() != raw_start_date or end_date.isoformat() != raw_end_date:
            raise meetings_mcp.InvalidArguments("calendar.list dates must be local ISO dates")
        day_offset = (start_date - date.today()).days
        day_count = (end_date - start_date).days
        if day_count != 1:
            raise meetings_mcp.InvalidArguments("calendar.list requires exactly one local day")
        calendar_arguments: dict[str, object] = {
            "day_count": day_count,
            "day_offset": day_offset,
            "start_date": raw_start_date,
            "end_date": raw_end_date,
        }
        if "refresh" in normalized:
            refresh = normalized["refresh"]
            if not isinstance(refresh, bool):
                raise meetings_mcp.InvalidArguments("refresh must be a boolean")
            if refresh and day_count != 1:
                raise meetings_mcp.InvalidArguments(
                    "calendar.list source refresh requires a single selected day"
                )
            calendar_arguments["refresh"] = refresh
        return RoutedGatewayRequest(
            request=request,
            arguments=calendar_arguments,
            app_instance_id=app_instance_id,
        )
    if request.startswith("note."):
        note_id = normalized.get("noteId")
        if (
            not isinstance(note_id, str)
            or meetings_mcp.MEETING_ID_PATTERN.fullmatch(note_id) is None
        ):
            raise meetings_mcp.InvalidArguments("noteId must be a valid meeting id")
    if request == "note.delete" and normalized["confirmed"] is not True:
        raise meetings_mcp.InvalidArguments("deleting a meeting requires explicit confirmation")
    if request == "note.share":
        email = normalized.get("email")
        if (
            not isinstance(email, str)
            or len(email) > 320
            or email.count("@") != 1
            or any(character.isspace() for character in email)
        ):
            raise meetings_mcp.InvalidArguments("email is invalid")
    if request == "note.shareEligibility":
        email = normalized.get("email", "")
        if not isinstance(email, str) or len(email) > 320:
            raise meetings_mcp.InvalidArguments("share eligibility email is invalid")
        normalized_email = email.strip()
        if normalized_email and (
            normalized_email.count("@") != 1
            or normalized_email.startswith("@")
            or normalized_email.endswith("@")
            or any(character.isspace() for character in normalized_email)
        ):
            raise meetings_mcp.InvalidArguments("share eligibility email is invalid")
        try:
            normalized_email.encode("utf-8")
        except UnicodeEncodeError as exc:
            raise meetings_mcp.InvalidArguments("share eligibility email is invalid") from exc
    if request == "note.feedback":
        try:
            meetings_mcp.validate_feedback_gateway_arguments(normalized)
        except ValueError as exc:
            raise meetings_mcp.InvalidArguments(str(exc)) from exc
    return RoutedGatewayRequest(
        request=request,
        arguments=normalized,
        app_instance_id=app_instance_id,
    )


def _report_private_ui_error(arguments: Mapping[str, object]) -> None:
    """Validate and report one bounded app-only UI error."""

    stage = arguments["stage"]
    kind = arguments["kind"]
    ui_version = arguments["uiVersion"]
    if not isinstance(stage, str) or not isinstance(kind, str) or not isinstance(ui_version, str):
        raise meetings_mcp.InvalidArguments("error report arguments are malformed")
    operation = arguments.get("operation")
    if operation is None:
        operation = {
            "recording": "new_note",
            "notes": "notes",
            "calendar": "calendar",
            "settings": "settings",
        }.get(stage)
    presentation = arguments.get("presentation")
    notification = arguments.get("notification")
    update_reason = arguments.get("updateReason")
    if (
        (operation is not None and not isinstance(operation, str))
        or (presentation is not None and not isinstance(presentation, str))
        or (notification is not None and not isinstance(notification, str))
        or (update_reason is not None and not isinstance(update_reason, str))
    ):
        raise meetings_mcp.InvalidArguments("error report context is malformed")
    error_source = {
        "auth": "auth",
        "backend": "backend",
        "connection": "connection",
        "invalid-response": "invalid_response",
    }.get(kind)
    diagnostics = McpSentryDiagnostics()
    if operation is not None:
        diagnostics["operation"] = operation
    if error_source is not None:
        diagnostics["error_source"] = error_source
    if presentation is not None:
        diagnostics["presentation"] = presentation
    if notification is not None:
        diagnostics["notification"] = notification
    if update_reason is not None:
        diagnostics["update_reason"] = update_reason
    if (stage, kind) == ("recording", "connection"):
        from companion_client import companion_failure_diagnostics

        diagnostics["companion_diagnostics"] = companion_failure_diagnostics()
    meetings_mcp.report_mcp_error(
        stage,
        kind,
        ui_version=ui_version,
        mcp_build_timestamp=meetings_mcp.server_build_timestamp_utc(),
        **diagnostics,
    )


def _report_private_ui_performance(
    arguments: Mapping[str, object], *, app_instance_id: str | None
) -> None:
    """Count one validated user-visible transition without error reporting."""

    operation = arguments["operation"]
    transition = arguments["transition"]
    duration_milliseconds = arguments["durationMs"]
    streaming = arguments["streaming"]
    if (
        not isinstance(operation, str)
        or not isinstance(transition, str)
        or isinstance(duration_milliseconds, bool)
        or not isinstance(duration_milliseconds, int)
        or not isinstance(streaming, str)
    ):
        raise meetings_mcp.InvalidArguments("performance report arguments are malformed")
    expected_account = None
    owner_generation = arguments.get("ownerScopeGeneration")
    if app_instance_id is not None and isinstance(owner_generation, str):
        candidate = _verified_cached_account_id()
        try:
            if (
                workspace_owner_scope_generation(candidate, app_instance_id=app_instance_id)
                == owner_generation
            ):
                expected_account = candidate
        except CodexAuthAccountUnverified:
            pass
    if expected_account is not None:
        record_client_action_latency(
            operation,
            transition,
            duration_milliseconds,
            streaming,
            expected_account=expected_account,
        )
    elif transition not in {"surface_active", "surface_load_failure"}:
        # Legacy or stale owners retain timing diagnostics, never current-user impact.
        record_client_action_latency(operation, transition, duration_milliseconds, streaming)
    if transition == "open_to_timeout":
        meetings_mcp.report_mcp_error("render", "timeout", ui_version="unknown", operation="render")


def _read_private_notes_response(
    arguments: Mapping[str, object],
    *,
    initial_account_id: tuple[str, str | None] | None,
    app_instance_id: str | None,
    cancellation_event: threading.Event | None,
) -> PrivateMeetingsResponse:
    """Keep Notes failure metadata private while preserving its UI projection."""

    initial_limit = arguments.get("initial_limit")
    page_token = arguments.get("page_token")
    recording_started_at = arguments.get("recording_started_at")
    if recording_started_at is not None and not isinstance(recording_started_at, str):
        raise meetings_mcp.InvalidArguments("recordingStartedAt is malformed")
    if initial_limit is not None and (
        isinstance(initial_limit, bool) or not isinstance(initial_limit, int)
    ):
        raise meetings_mcp.InvalidArguments("initialLimit is malformed")
    if page_token is not None and not isinstance(page_token, str):
        raise meetings_mcp.InvalidArguments("pageToken is malformed")
    backend_retryability: list[bool] = []
    backend_auth_rejections: list[bool] = []
    backend_rate_limits: list[float] = []
    initial_account_id = _establish_snapshot_account(
        initial_account_id,
        "notes.list",
        cancellation_event=cancellation_event,
    )
    correlation: NotesRecordingArguments = {}
    if recording_started_at is not None:
        correlation["recording_started_at"] = recording_started_at
    payload = meetings_mcp.read_backend_meetings_view(
        initial_limit=initial_limit,
        page_token=page_token,
        **correlation,
        cancellation_event=cancellation_event,
        backend_failure_handler=backend_retryability.append,
        backend_auth_failure_handler=lambda: backend_auth_rejections.append(True),
        backend_rate_limit_handler=backend_rate_limits.append,
    )
    return _private_snapshot_response(
        "notes.list",
        payload,
        retryable=backend_retryability[0] if backend_retryability else None,
        backend_auth_rejected=bool(backend_auth_rejections),
        retry_after_seconds=backend_rate_limits[0] if backend_rate_limits else None,
        expected_account=initial_account_id,
        app_instance_id=app_instance_id,
        cancellation_event=cancellation_event,
    )


def _submit_private_user_feedback(
    arguments: Mapping[str, object], *, cancellation_event: threading.Event | None
) -> PrivateMeetingsResponse:
    request = "ui.submitFeedback"
    feedback_text = arguments["feedbackText"]
    if not isinstance(feedback_text, str):
        raise meetings_mcp.InvalidArguments("feedbackText is malformed")
    if cancellation_event is not None and cancellation_event.is_set():
        return _failed_private_response(request, "cancelled")
    try:
        feedback_id = submit_user_feedback(feedback_text, cancellation_event=cancellation_event)
    except (OSError, RuntimeError, ValueError):
        if cancellation_event is not None and cancellation_event.is_set():
            return _failed_private_response(request, "cancelled")
        return _failed_private_response(request, "backend")
    return PrivateMeetingsResponse(request=request, ok=True, data={"feedbackId": feedback_id})


def _read_private_calendar_response(
    arguments: Mapping[str, object],
    *,
    initial_account_id: tuple[str, str | None] | None,
    app_instance_id: str | None,
    cancellation_event: threading.Event | None,
) -> PrivateMeetingsResponse:
    """Project Calendar results and recovery metadata for the verified UI owner."""
    request = "calendar.list"
    day_count = arguments["day_count"]
    day_offset = arguments["day_offset"]
    start_date = arguments["start_date"]
    end_date = arguments["end_date"]
    refresh = arguments.get("refresh", False)
    if (
        isinstance(day_count, bool)
        or not isinstance(day_count, int)
        or isinstance(day_offset, bool)
        or not isinstance(day_offset, int)
        or not isinstance(start_date, str)
        or not isinstance(end_date, str)
        or not isinstance(refresh, bool)
    ):
        raise meetings_mcp.InvalidArguments("calendar.list arguments are malformed")
    initial_account_id = _establish_snapshot_account(
        initial_account_id,
        request,
        cancellation_event=cancellation_event,
    )
    not_connected: list[bool] = []
    refresh_disabled: list[float] = []
    payload = meetings_mcp.read_backend_calendar_view(
        day_count=day_count,
        day_offset=day_offset,
        refresh=refresh,
        include_private_metadata=True,
        cancellation_event=cancellation_event,
        not_connected_handler=lambda: not_connected.append(True),
        refresh_disabled_handler=refresh_disabled.append,
    )
    payload["calendarStartDate"] = start_date
    payload["calendarEndDate"] = end_date
    payload["eventsByDate"] = project_calendar_events_by_date(
        payload.pop("upcoming", []), start_date, end_date
    )
    return _private_snapshot_response(
        request,
        payload,
        backend_error_kind=(
            "calendar_not_connected"
            if not_connected
            else "calendar_refresh_disabled"
            if refresh_disabled
            else "backend"
        ),
        retryable=not not_connected,
        retry_after_seconds=refresh_disabled[0] if refresh_disabled else None,
        expected_account=initial_account_id,
        app_instance_id=app_instance_id,
        cancellation_event=cancellation_event,
    )


def _track_private_analytics(
    arguments: Mapping[str, object],
    *,
    app_instance_id: str | None,
    cancellation_event: threading.Event | None,
) -> PrivateMeetingsResponse:
    """Drop analytics failures without entering product error reporting."""

    accepted = False
    try:
        client = meetings_mcp.get_record_interactions_client()
        account = _establish_request_account(
            _verified_cached_account_id(), client, cancellation_event=cancellation_event
        )
        if (
            account is None
            or workspace_owner_scope_generation(
                account, app_instance_id=app_instance_id, cancellation_event=cancellation_event
            )
            != arguments["ownerScopeGeneration"]
        ):
            raise CodexAuthAccountUnverified("Analytics owner is no longer current")
        accepted = client.track_event(
            parse_analytics_event(arguments["event"]),
            expected_account=account,
            cancellation_event=cancellation_event,
        )
        if _observed_account_changed(account):
            raise CodexAuthAccountUnverified("Analytics owner changed during delivery")
    except Exception:
        # The app receives a normal negative acknowledgement; no Sentry error,
        # auth-recovery state, exception text or event payload escapes this boundary.
        logging.getLogger(__name__).warning("Meetings analytics unavailable; observation dropped.")
        accepted = False
    return PrivateMeetingsResponse(
        request="analytics.track", ok=True, data=PluginAnalyticsAcceptance(accepted=accepted)
    )


def read_private_meetings_response(
    request: str,
    arguments: Mapping[str, object],
    *,
    app_instance_id: str | None = None,
    cancellation_event: threading.Event | None,
) -> PrivateMeetingsResponse:
    """Execute one validated app-only request.

    Args:
        request: Explicit gateway operation name.
        arguments: Values validated for that operation.
        app_instance_id: Optional in-memory mounted-workspace ownership nonce.
        cancellation_event: Optional caller cancellation signal.

    Returns:
        A private component response whose data is excluded from model-visible
        result fields.
    """

    if request == "analytics.track":
        return _track_private_analytics(
            arguments, app_instance_id=app_instance_id, cancellation_event=cancellation_event
        )

    if request == "ui.submitFeedback":
        return _submit_private_user_feedback(arguments, cancellation_event=cancellation_event)

    if request in {"settings.get", "settings.update"}:
        return _read_private_settings_response(
            request, arguments, cancellation_event=cancellation_event
        )

    if request == "ui.reportPerformance":
        _report_private_ui_performance(arguments, app_instance_id=app_instance_id)
        return PrivateMeetingsResponse(request=request, ok=True)

    if request == "diagnostics.get":
        from companion_client import companion_connection_diagnostics

        return PrivateMeetingsResponse(
            request=request,
            ok=True,
            data={
                "auth": meetings_mcp.get_process_auth_manager().peek_auth_diagnostics(),
                "companion": companion_connection_diagnostics(),
            },
        )

    initial_account_id = _verified_cached_account_id()
    try:
        if request in {"local.getUploads", "local.retryUpload"}:
            return _recording_upload_response(
                request,
                arguments,
                app_instance_id=app_instance_id,
                cancellation_event=cancellation_event,
            )
        if request == "home.bootstrap":
            from meetings_home_bootstrap import read_home_bootstrap

            verified_owners: list[AuthMaterial] = []
            home = read_home_bootstrap(
                cancellation_event=cancellation_event,
                on_verified_owner=verified_owners.append,
            )
            owner = verified_owners[0] if verified_owners else None
            response = PrivateMeetingsResponse(
                request=request,
                ok=True,
                data=home,
                owner_scope_generation=(
                    workspace_owner_scope_generation(
                        (owner.account_id, owner.subject),
                        app_instance_id=app_instance_id,
                        cancellation_event=cancellation_event,
                    )
                    if owner is not None
                    else None
                ),
            )
            report_ui_opened(app_instance_id=app_instance_id)
            return response
        if request == "ui.reportError":
            _report_private_ui_error(arguments)
            return PrivateMeetingsResponse(request=request, ok=True)
        if request == "notes.list":
            return _read_private_notes_response(
                arguments,
                initial_account_id=initial_account_id,
                app_instance_id=app_instance_id,
                cancellation_event=cancellation_event,
            )
        if request == "calendar.list":
            return _read_private_calendar_response(
                arguments,
                initial_account_id=initial_account_id,
                app_instance_id=app_instance_id,
                cancellation_event=cancellation_event,
            )
        client = meetings_mcp.get_record_interactions_client()
        initial_account_id = _establish_request_account(
            initial_account_id, client, cancellation_event=cancellation_event
        )
        note_id = arguments.get("noteId") if request.startswith("note.") else ""
        if not isinstance(note_id, str):
            raise meetings_mcp.InvalidArguments("noteId must be a valid meeting id")
        if request in {
            "note.delete",
            "note.reprocess",
            "note.share",
            "note.shareEligibility",
            "note.feedback",
        } and _observed_account_changed(initial_account_id):
            return _failed_private_response(request, "auth")
        note_mutation_account: _NoteMutationAccountArguments = {}
        if initial_account_id is not None:
            note_mutation_account["expected_account"] = initial_account_id
        if request == "note.get":
            data = client.get_note(
                note_id,
                cancellation_event=cancellation_event,
            )
        elif request == "note.delete":
            data = client.delete_note(
                note_id,
                cancellation_event=cancellation_event,
                **note_mutation_account,
            )
        elif request == "note.reprocess":
            data = client.reprocess_note(
                note_id,
                cancellation_event=cancellation_event,
                **note_mutation_account,
            )
        elif request == "note.share":
            email = arguments["email"]
            if not isinstance(email, str):
                raise meetings_mcp.InvalidArguments("email is malformed")
            data = client.share(
                note_id,
                email=email,
                cancellation_event=cancellation_event,
                **note_mutation_account,
            )
        elif request == "note.shareEligibility":
            email = arguments.get("email", "")
            if not isinstance(email, str):
                raise meetings_mcp.InvalidArguments("share eligibility email is malformed")
            data = client.check_share_eligibility(
                note_id,
                email=email,
                cancellation_event=cancellation_event,
                **note_mutation_account,
            )
        elif request == "note.feedback":
            category = arguments["category"]
            feedback_text = arguments.get("feedbackText")
            include_debug_artifacts = arguments["includeDebugArtifacts"]
            feedback_continuation_token = arguments.get("feedbackContinuationToken")
            if (
                not isinstance(category, str)
                or (feedback_text is not None and not isinstance(feedback_text, str))
                or not isinstance(include_debug_artifacts, bool)
                or (
                    feedback_continuation_token is not None
                    and not isinstance(feedback_continuation_token, str)
                )
            ):
                raise meetings_mcp.InvalidArguments("feedback arguments are malformed")
            data = client.submit_feedback(
                note_id,
                category=category,
                feedback_text=feedback_text,
                include_debug_artifacts=include_debug_artifacts,
                feedback_continuation_token=feedback_continuation_token,
                cancellation_event=cancellation_event,
                **note_mutation_account,
            )
        elif request == "onboarding.profile":
            return _private_onboarding_profile_response(
                client.get_onboarding_profile(cancellation_event=cancellation_event),
                initial_account_id,
                app_instance_id=app_instance_id,
                cancellation_event=cancellation_event,
            )
        elif request == "connection.ensure":
            if (
                initial_account_id is None
                or workspace_owner_scope_generation(
                    initial_account_id,
                    app_instance_id=app_instance_id,
                    cancellation_event=cancellation_event,
                )
                != arguments["ownerScopeGeneration"]
            ):
                return _failed_private_response(request, "auth")
            data = client.ensure_meetings_connection(
                expected_account=initial_account_id,
                cancellation_event=cancellation_event,
            )
        elif request in {"activity.get", "activity.view"}:
            if initial_account_id is None:
                raise CodexAuthAccountUnverified("ChatGPT account could not be verified")
            if request == "activity.view":
                owner_generation = workspace_owner_scope_generation(
                    initial_account_id,
                    app_instance_id=app_instance_id,
                    cancellation_event=cancellation_event,
                )
                if (
                    owner_generation is None
                    or owner_generation != arguments["ownerScopeGeneration"]
                ):
                    raise CodexAuthAccountUnverified("ChatGPT account changed")
            data = client.meetings_activity(
                mark_viewed=request == "activity.view",
                expected_account=initial_account_id,
                cancellation_event=cancellation_event,
            )
        elif request in {"calendar.connections", "context.connections"}:
            data = client.get_app_connections(
                group="calendars" if request == "calendar.connections" else "context",
                cancellation_event=cancellation_event,
            )
        else:
            raise meetings_mcp.InvalidArguments("request is unsupported")
        if _observed_account_changed(initial_account_id):
            return _failed_private_response(request, "auth")
        return PrivateMeetingsResponse(request=request, ok=True, data=data)
    except meetings_mcp.RecordHandleError:
        return _failed_private_response(request, "invalid-handle")
    except (
        meetings_mcp.CodexAuthCancelled,
        meetings_mcp.RecordMeetingsCancelled,
        meetings_mcp.RecordCalendarCancelled,
        meetings_mcp.RecordMeetingInteractionsCancelled,
    ):
        return _failed_private_response(request, "cancelled")
    except CodexAuthAccountUnverified:
        return _failed_private_response(request, "auth")
    except (
        CodexAuthUnavailable,
        meetings_mcp.RecordCalendarBackendError,
        meetings_mcp.RecordMeetingInteractionsBackendError,
        meetings_mcp.ControlUnavailable,
        meetings_mcp.NativeRuntimeError,
    ):
        if request in {"local.getUploads", "local.retryUpload"}:
            return PrivateMeetingsResponse(
                request=request,
                ok=False,
                data={"available": False},
                error_kind="upload" if _retains_verified_account(initial_account_id) else "auth",
            )
        if not _retains_verified_account(initial_account_id):
            return _failed_private_response(request, "auth")
        stage = "calendar" if request.startswith("calendar.") else "interactions"
        meetings_mcp.report_mcp_error(
            stage,
            "backend",
            mcp_build_timestamp=meetings_mcp.server_build_timestamp_utc(),
        )
        return _failed_private_response(request, "backend")
    except (
        meetings_mcp.CodexAuthError,
        meetings_mcp.RecordCalendarAuthError,
        meetings_mcp.RecordMeetingInteractionsAuthError,
    ) as error:
        return _failed_private_response(
            request,
            "auth",
            backend_auth_rejected=(
                request == "note.get"
                and isinstance(error, RecordMeetingInteractionsAuthRejected)
                and _retains_verified_account(initial_account_id)
            ),
        )


def _private_onboarding_profile_response(
    profile: OnboardingProfileWire,
    account: tuple[str, str | None] | None,
    *,
    app_instance_id: str | None,
    cancellation_event: threading.Event | None,
) -> PrivateMeetingsResponse:
    """Bind internal gate authority to the verified owner of this mounted app."""
    if _observed_account_changed(account):
        return _failed_private_response("onboarding.profile", "auth")
    return PrivateMeetingsResponse(
        request="onboarding.profile",
        ok=True,
        data=profile,
        owner_scope_generation=(
            workspace_owner_scope_generation(
                account,
                app_instance_id=app_instance_id,
                cancellation_event=cancellation_event,
            )
            if account is not None
            else None
        ),
    )


def _read_private_settings_response(
    request: str,
    arguments: Mapping[str, object],
    *,
    cancellation_event: threading.Event | None,
) -> PrivateMeetingsResponse:
    initial_account_id = _verified_cached_account_id()
    try:
        client = meetings_mcp.get_record_interactions_client()
        initial_account_id = _establish_request_account(
            initial_account_id, client, cancellation_event=cancellation_event
        )
        if request == "settings.get":
            settings = client.get_settings(cancellation_event=cancellation_event)
        else:
            if _observed_account_changed(initial_account_id):
                raise CodexAuthAccountChanged("ChatGPT account changed")
            if arguments.get(
                "autoRecordEnabled"
            ) is True and meetings_mcp.plugin_availability_blocks_start(local_fallback=True):
                raise meetings_mcp.InvalidArguments(
                    "Automatic meeting notes are unavailable on this client."
                )
            settings = (
                client.update_settings(settings=arguments, cancellation_event=cancellation_event)
                if initial_account_id is None
                else client.update_settings(
                    settings=arguments,
                    expected_account=initial_account_id,
                    cancellation_event=cancellation_event,
                )
            )
        if _observed_account_changed(initial_account_id):
            raise CodexAuthAccountChanged("ChatGPT account changed")
        if (
            request == "settings.update"
            and arguments.get("featureEnabled") is True
            and settings.configured_feature_enabled
            and not settings.feature_enabled
            and (cancellation_event is None or not cancellation_event.is_set())
        ):
            # A saved preference is not proof of effective access or its failure cause.
            meetings_mcp.report_mcp_error(
                "settings",
                "backend",
                mcp_build_timestamp=meetings_mcp.server_build_timestamp_utc(),
                operation="settings",
                error_source="backend",
                failure_reason="activation_not_effective",
            )
        return PrivateMeetingsResponse(request=request, ok=True, data=settings.to_wire())
    except (meetings_mcp.CodexAuthCancelled, meetings_mcp.RecordMeetingInteractionsCancelled):
        return _failed_private_response(request, "cancelled")
    except CodexAuthAccountUnverified as error:
        return _settings_failure_response(request, "auth", error)
    except (CodexAuthUnavailable, meetings_mcp.RecordMeetingInteractionsBackendError) as error:
        return _settings_failure_response(
            request,
            "backend" if _retains_verified_account(initial_account_id) else "auth",
            error,
        )
    except (meetings_mcp.CodexAuthError, meetings_mcp.RecordMeetingInteractionsAuthError) as error:
        return _settings_failure_response(request, "auth", error)


def _settings_failure_response(
    request: str,
    kind: Literal["auth", "backend"],
    error: Exception,
) -> PrivateMeetingsResponse:
    """Report finite settings failure evidence without exceptions or credentials."""
    reason: SettingsFailureReason = "session_unverified"
    source: Literal["auth", "backend"] = "auth"
    http_status: int | None = None
    retryable = True
    if isinstance(error, meetings_mcp.RecordMeetingInteractionsBackendError):
        source = "backend"
        reason = (
            error.failure_kind
            if error.failure_kind in MCP_SENTRY_BACKEND_FAILURE_REASONS
            else "invalid_response"
        )
        retryable = error.retryable
        if type(error.http_status) is int and 100 <= error.http_status <= 599:
            http_status = error.http_status
    elif isinstance(error, RecordMeetingInteractionsAuthRejected):
        reason, source, http_status = "http_401", "backend", 401
    elif isinstance(error, meetings_mcp.CodexAuthError):
        if error.failure_reason in MCP_SENTRY_SETTINGS_AUTH_FAILURE_REASONS:
            reason = error.failure_reason
    diagnostics = McpSentryDiagnostics(
        operation="settings",
        failure_reason=reason,
        error_source=source,
        retryable=retryable,
    )
    if http_status is not None:
        diagnostics["http_status"] = http_status
    meetings_mcp.report_mcp_error(
        "settings",
        kind,
        mcp_build_timestamp=meetings_mcp.server_build_timestamp_utc(),
        **diagnostics,
    )
    try:
        print(
            "ChatGPT Meetings settings: "
            + json.dumps({"request": request, "kind": kind, **diagnostics}, sort_keys=True),
            file=sys.stderr,
            flush=True,
        )
    except (OSError, TypeError, ValueError):
        pass
    return PrivateMeetingsResponse(
        request=request,
        ok=False,
        error_kind=kind,
        retryable=retryable,
        failure_reason=reason,
        error_source=source,
        http_status=http_status,
    )


def _recording_upload_response(
    request: str,
    arguments: Mapping[str, object],
    *,
    app_instance_id: str | None,
    cancellation_event: threading.Event | None,
) -> PrivateMeetingsResponse:
    """Project native-owned recovery without coupling local rows to native auth."""

    from companion_client import companion_client
    from control_protocol import ControlConnectionUnavailable

    auth_manager = meetings_mcp.get_process_auth_manager()
    auth = auth_manager.peek_cached_chatgpt_auth()
    if auth is None:
        # A blocked workspace may have no other authenticated read to renew
        # verification. Recovery shares the existing bounded, single-flight read.
        auth = auth_manager.get_chatgpt_auth(
            refresh_token=False,
            cancellation_event=cancellation_event,
        )
    scope = record_owner_scope_fingerprint(auth)
    if scope is None:
        raise CodexAuthAccountUnverified("ChatGPT account could not be verified")
    expected_account = (auth.account_id, auth.subject)
    owner_generation = workspace_owner_scope_generation(
        expected_account,
        app_instance_id=app_instance_id,
        cancellation_event=cancellation_event,
    )
    # A mounted surface may discover its private owner with the first upload
    # page while ordinary workspace reads are blocked. Later reads and every
    # retry retain their expected-owner fence.
    if owner_generation is None or (
        (request == "local.retryUpload" or "ownerScopeGeneration" in arguments)
        and owner_generation != arguments.get("ownerScopeGeneration")
    ):
        raise CodexAuthAccountUnverified("ChatGPT account changed")
    try:
        client = companion_client(cancellation_event=cancellation_event)
    except (meetings_mcp.ControlUnavailable, meetings_mcp.NativeRuntimeError, OSError, ValueError):
        if request == "local.retryUpload":
            raise
        client = None
    state = client.latest_state() if client is not None else None
    upload_read_failed = False
    data: dict[str, object]
    if (
        client is None
        or "recording.recovery.v1" not in client.negotiated_capabilities
        or state is None
    ):
        if request == "local.retryUpload":
            raise meetings_mcp.ControlUnavailable("native upload retry is unavailable")
        # The private owner witness is authenticated by MCP independently of
        # native availability. It grants neither queue data nor retry authority.
        data = {"available": False}
    else:
        native_scope = state["accountScopeFingerprint"]
        if request == "local.getUploads":
            # The native core filters hosted rows to this caller and may also
            # return unbound local recordings while its own auth recovers.
            offset = arguments["offset"]
            if isinstance(offset, bool) or not isinstance(offset, int):
                raise meetings_mcp.InvalidArguments("offset is invalid")
            try:
                result = client.call(
                    "recording.getUploads",
                    {"accountScopeFingerprint": scope, "offset": offset},
                    cancellation_event=cancellation_event,
                )
            except ControlConnectionUnavailable:
                upload_read_failed = True
                data = {"available": False}
            else:
                if not is_uploads_result(result) or not hmac.compare_digest(
                    result["accountScopeFingerprint"], scope
                ):
                    raise meetings_mcp.ControlUnavailable(
                        "native companion uploads account does not match"
                    )
                data = {"available": True, "queue": result["queue"]}
        else:
            if native_scope != scope:
                raise CodexAuthAccountUnverified("native upload account does not match")
            recording_id = arguments["recordingId"]
            if not isinstance(recording_id, str):
                raise meetings_mcp.InvalidArguments("recordingId is invalid")
            accepted = client.call(
                "recording.retry",
                {"accountScopeFingerprint": scope, "recordingId": recording_id},
                cancellation_event=cancellation_event,
            )
            if not is_retry_upload_result(accepted):
                raise meetings_mcp.ControlUnavailable(
                    "native companion upload retry result is malformed"
                )
            data = {"accepted": accepted["accepted"]}
        current_state = client.latest_state()
        if current_state is None:
            if request == "local.retryUpload":
                raise CodexAuthAccountUnverified("ChatGPT account changed")
            upload_read_failed = False
            data = {"available": False}
        elif current_state["accountScopeFingerprint"] != native_scope:
            raise CodexAuthAccountUnverified("ChatGPT account changed")
    if (
        workspace_owner_scope_generation(
            expected_account,
            app_instance_id=app_instance_id,
            cancellation_event=cancellation_event,
        )
        != owner_generation
    ):
        raise CodexAuthAccountUnverified("ChatGPT account changed")
    if upload_read_failed:
        # A request timeout can leave the authenticated stream healthy. Keep
        # recovery retryable rather than declaring its capability unavailable.
        return _failed_private_response(request, "upload")
    return PrivateMeetingsResponse(
        request=request, ok=True, data=data, owner_scope_generation=owner_generation
    )


def _failed_private_response(
    request: str,
    error_kind: str,
    *,
    data: NotesSectionWire | CalendarSectionWire | None = None,
    retryable: bool = True,
    owner_scope_generation: str | None = None,
    backend_auth_rejected: bool = False,
    retry_after_seconds: float | None = None,
) -> PrivateMeetingsResponse:
    return PrivateMeetingsResponse(
        request=request,
        ok=False,
        data=data,
        error_kind=error_kind,
        retryable=retryable,
        owner_scope_generation=owner_scope_generation,
        backend_auth_rejected=backend_auth_rejected,
        retry_after_seconds=retry_after_seconds,
    )


def _private_snapshot_response(
    request: str,
    payload: NotesSectionWire | CalendarSectionWire,
    *,
    retryable: bool | None = None,
    backend_error_kind: Literal[
        "backend", "calendar_not_connected", "calendar_refresh_disabled"
    ] = "backend",
    backend_auth_rejected: bool = False,
    retry_after_seconds: float | None = None,
    expected_account: tuple[str, str | None] | None = None,
    app_instance_id: str | None = None,
    cancellation_event: threading.Event | None = None,
) -> PrivateMeetingsResponse:
    if cancellation_event is not None and cancellation_event.is_set():
        return _failed_private_response(request, "cancelled")
    state = payload.get("snapshotState")
    status = state.get("status") if is_json(state) else None
    if status == "auth-error":
        return _failed_private_response(
            request,
            "auth",
            data=payload,
            backend_auth_rejected=(
                backend_auth_rejected and _retains_verified_account(expected_account)
            ),
        )
    if status == "backend-error":
        return _failed_private_response(
            request,
            backend_error_kind,
            data=payload,
            retryable=retryable is not False,
            retry_after_seconds=retry_after_seconds,
            owner_scope_generation=workspace_owner_scope_generation(
                expected_account,
                app_instance_id=app_instance_id,
                cancellation_event=cancellation_event,
            ),
        )
    return PrivateMeetingsResponse(
        request=request,
        ok=True,
        data=payload,
        owner_scope_generation=workspace_owner_scope_generation(
            expected_account,
            app_instance_id=app_instance_id,
            cancellation_event=cancellation_event,
        ),
    )


def normalize_settings_patch(
    arguments: Mapping[str, object],
    *,
    tool_name: str = "meetings.updateSettings",
) -> dict[str, bool]:
    """Validate the only settings values allowed across the MCP boundary.

    The signed native bridge remains the persistence authority. This first
    boundary is intentionally path-free and rejects Python's bool-as-int edge
    before an untrusted webview value reaches the native request envelope.

    Args:
        arguments: Candidate native settings patch.
        tool_name: Tool name used in validation errors.

    Returns:
        A validated generated native settings patch.

    Raises:
        InvalidArguments: If a setting is unsupported, malformed, or violates
            its prerequisite policy.
    """

    allowed = ("calendarRemindersEnabled", "soundEffectsEnabled", "meetingDetectionEnabled")
    require_tool_arguments(tool_name, arguments, (), allowed)
    normalized: dict[str, bool] = {}
    for key in allowed:
        if key not in arguments:
            continue
        value = arguments[key]
        if not isinstance(value, bool):
            raise meetings_mcp.InvalidArguments(f"{key} must be a boolean")
        normalized[key] = value
    if not normalized:
        raise meetings_mcp.InvalidArguments("at least one companion setting is required")
    return normalized


def read_server_icon(path: Path) -> bytes | None:
    try:
        metadata = path.lstat()
    except OSError:
        return None
    if (
        not meetings_mcp.stat.S_ISREG(metadata.st_mode)
        or metadata.st_size <= 0
        or metadata.st_size > meetings_mcp.SERVER_ICON_MAXIMUM_BYTES
    ):
        return None
    try:
        value = path.read_bytes()
    except OSError:
        return None
    if len(value) != metadata.st_size:
        return None
    stripped = value.strip()
    if (
        not stripped.startswith(b"<svg ")
        or not stripped.endswith(b"</svg>")
        or b'xmlns="http://www.w3.org/2000/svg"' not in stripped
    ):
        return None
    return value


def asset_icons(
    specs: tuple[tuple[str | None, str], ...],
    *,
    size: Literal["16x16", "any"],
) -> list[JSONSchema]:
    # Production releases carry their own immutable icon copies beside the
    # runtime. Source/dev packages retain the normal plugin-level assets path.
    for root in (meetings_mcp.SCRIPT_ROOT / "assets", meetings_mcp.PLUGIN_ROOT / "assets"):
        icons: list[JSONSchema] = []
        for theme, file_name in specs:
            value = read_server_icon(root / file_name)
            if value is None:
                break
            encoded = meetings_mcp.base64.b64encode(value).decode("ascii")
            icon: JSONSchema = {
                "src": f"data:{meetings_mcp.SERVER_ICON_MIME_TYPE};base64,{encoded}",
                "mimeType": meetings_mcp.SERVER_ICON_MIME_TYPE,
                "sizes": [size],
            }
            if theme is not None:
                icon["theme"] = theme
            icons.append(icon)
        if len(icons) == len(specs):
            return icons
    return []


def server_icons() -> list[JSONSchema]:
    return asset_icons(meetings_mcp.SERVER_ICON_SPECS, size="16x16")


def meeting_resource_icons() -> list[JSONSchema]:
    return asset_icons(meetings_mcp.MEETING_RESOURCE_ICON_SPECS, size="any")


def server_info(profile: str) -> JSONSchema:
    """Return the server identity advertised during MCP initialization.

    Args:
        profile: Runtime profile controlling development presentation.

    Returns:
        A JSON-compatible MCP server-info object.
    """

    return {
        "name": meetings_mcp.SERVER_NAME,
        "title": (
            "Meetings (Dev)"
            if profile == meetings_mcp.PROFILE_LOCAL_DEV
            or (meetings_mcp.PLUGIN_ROOT / ".codex-plugin/local-bundle.json").is_file()
            else meetings_mcp.DISPLAY_NAME
        ),
        "version": meetings_mcp.SERVER_VERSION,
        "icons": server_icons(),
    }


def app_only_meta() -> JSONSchema:
    return {
        "ui": {"visibility": ["app"]},
        "openai/widgetAccessible": True,
    }


def widget_meta(
    global_entrypoint: bool = False,
    *,
    quick_action_tool: str = "chatgpt_meetings_take_notes",
    sidebar_take_notes_enabled: bool = False,
) -> JSONSchema:
    meta: JSONSchema = {
        "ui": {
            "resourceUri": meetings_mcp.WIDGET_URI,
            "visibility": ["app"],
        },
        "ui/resourceUri": meetings_mcp.WIDGET_URI,
        "openai/outputTemplate": meetings_mcp.WIDGET_URI,
        "openai/widgetAccessible": True,
        "openai/toolInvocation/invoking": "Opening Meetings…",
        "openai/toolInvocation/invoked": "Meetings is ready",
    }
    if global_entrypoint:
        entrypoint: JSONSchema = {"type": "global"}
        icons = asset_icons((("light", "take-notes.svg"), ("dark", "take-notes.svg")), size="any")
        if icons and sidebar_take_notes_enabled:
            entrypoint["quickAction"] = {
                "title": "Take notes",
                "icons": icons,
                "target": {
                    "type": "tool",
                    "name": quick_action_tool,
                    "arguments": {},
                },
            }
        entrypoints = [entrypoint]
        meta["openai/ui"] = {"entrypoints": entrypoints}
        meta["com.openai"] = {"ui": {"entrypoints": entrypoints}}
    return meta


def private_meetings_tool_result(
    response: PrivateMeetingsResponse,
) -> JSONSchema:
    """Keep app-only Meetings data out of conversation-visible result fields.

    Args:
        response: Typed private gateway result.

    Returns:
        A minimal public envelope with the private result in component metadata.
    """

    structured: dict[str, object] = {
        "ok": response.ok,
        "request": response.request,
    }
    private: dict[str, object] = {
        "schemaVersion": 1,
        "request": response.request,
    }
    if response.data is not None:
        private["data"] = response.data
    if response.request == "home.bootstrap" and response.ok:
        private["connectionMigrationSupported"] = True
    if response.owner_scope_generation is not None and (
        response.ok
        or response.error_kind in {"backend", "calendar_refresh_disabled", "calendar_not_connected"}
    ):
        private["ownerScopeGeneration"] = response.owner_scope_generation
    if not response.ok:
        error: dict[str, object] = {
            "kind": response.error_kind or "backend",
            "retryable": response.retryable,
        }
        structured["error"] = error
        private_error = dict(error)
        if response.retry_after_seconds is not None:
            private_error["retryAfterSeconds"] = response.retry_after_seconds
        if response.request in {"settings.get", "settings.update"}:
            if response.failure_reason is not None:
                private_error["failureReason"] = response.failure_reason
            if response.error_source is not None:
                private_error["errorSource"] = response.error_source
            if response.http_status is not None:
                private_error["httpStatus"] = response.http_status
        private["error"] = private_error
    return meetings_mcp.tool_result(
        structured,
        extra_meta={"meetingsResponse": private},
    )


def resource_contents() -> JSONSchema:
    """Read the packaged Meetings widget as one MCP resource.

    Returns:
        The widget source and its bounded presentation metadata.
    """

    widget_bytes = meetings_mcp.WIDGET_PATH.read_bytes()
    return {
        "contents": [
            {
                "uri": meetings_mcp.WIDGET_URI,
                "mimeType": meetings_mcp.WIDGET_MIME,
                "text": widget_bytes.decode("utf-8"),
                "_meta": {
                    "openai/ui": {"availableDisplayModes": ["inline"]},
                    "ui": {
                        "prefersBorder": False,
                        "csp": {
                            "connectDomains": [],
                            "resourceDomains": ["https://*.oaiusercontent.com"],
                        },
                    },
                    "openai/widgetCSP": {
                        "connect_domains": [],
                        "resource_domains": ["https://*.oaiusercontent.com"],
                    },
                    "openai/widgetDescription": (
                        "A fullscreen Meetings workspace with upcoming "
                        "meetings, notes, and local capture controls."
                    ),
                    "openai/widgetPrefersBorder": False,
                    "openai/widgetHeightHint": 760,
                    "openai/widgetShowCodexWidgetInline": True,
                    "openai/widgetMinFrameHeight": 560,
                },
            }
        ]
    }


def meeting_resource_templates() -> list[JSONSchema]:
    """Describe the authenticated Meeting and private-note resource contracts.

    Returns:
        Canonical resource templates for both rollout read sources.
    """

    shared = {
        "title": "Meeting note",
        "mimeType": meetings_mcp.MEETING_RESOURCE_MIME,
        "icons": meeting_resource_icons(),
    }
    return [
        {
            **shared,
            "name": "private-meeting-note",
            "uriTemplate": meetings_mcp.NOTE_RESOURCE_URI_TEMPLATE,
            "description": "Read one authenticated private note and its meeting context.",
        },
        {
            **shared,
            "name": "meeting-note-compatibility",
            "uriTemplate": meetings_mcp.MEETING_RESOURCE_URI_TEMPLATE,
            "description": "Read one authenticated legacy Meeting note.",
        },
    ]


def record_id_from_resource_uri(uri: str) -> tuple[Literal["meeting", "note"], str]:
    parsed = meetings_mcp.urlparse(uri)
    if (
        parsed.scheme != "meetings"
        or parsed.netloc not in {"meeting", "note"}
        or parsed.params
        or parsed.query
        or parsed.fragment
    ):
        raise meetings_mcp.InvalidArguments("unknown resource URI")
    canonical_id = parsed.path.removeprefix("/")
    if (
        not canonical_id
        or "/" in canonical_id
        or not meetings_mcp.MEETING_ID_PATTERN.fullmatch(canonical_id)
    ):
        raise meetings_mcp.InvalidArguments("unknown resource URI")
    return ("note" if parsed.netloc == "note" else "meeting"), canonical_id
