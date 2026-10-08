"""Project Record lifecycle states for Meetings note lists and details."""

from __future__ import annotations

import re
from collections.abc import Mapping
from typing import Literal

from meetings_api_client_common import nonempty_string
from record_meeting_interaction_types import RecordMeetingNoteStatus, RecordMeetingProcessingStage

from helpers import is_json

RecordMeetingFetchStatus = Literal["fetchable", "processing", "unavailable"]


_NOTE_WAITING_STATUSES = frozenset({"waiting_room"})
_NOTE_JOINING_STATUSES = frozenset(
    {
        "dispatched",
        "joining",
        "joining_meeting",
        "not_attempted",
        "pending",
        "pending_join",
        "pending_start",
        "queue",
        "queued",
        "queued_for_start",
        "replacement_pending_start",
        "waiting",
    }
)
_NOTE_RECORDING_STATUSES = frozenset(
    {
        "active",
        "capturing",
        "in_progress",
        "joined",
        "joined_meeting",
        "live",
        "recording",
        "recording_in_progress",
        "running",
        "started",
    }
)
_NOTE_UPLOADING_STATUSES = frozenset({"uploading"})
_NOTE_PROCESSING_STATUSES = frozenset(
    {
        "diarized",
        "diarizing",
        "gathering_meeting_data",
        "preparing_transcript",
        "processing",
        "reprocessing",
        "summarizing",
        "summarizing_from_original_transcript",
        "summarizing_without_audio",
        "transcribing",
    }
)
_NOTE_ACTIVE_STATUSES = (
    _NOTE_WAITING_STATUSES
    | _NOTE_JOINING_STATUSES
    | _NOTE_RECORDING_STATUSES
    | _NOTE_UPLOADING_STATUSES
    | _NOTE_PROCESSING_STATUSES
)
_NOTE_GENERIC_ACTIVE_STATUSES = frozenset({"active", "in_progress", "running"})
_NOTE_FAILED_STATUSES = frozenset(
    {
        "blocked",
        "caas_launch_failed",
        "canceled",
        "cancelled",
        "container_start_failed",
        "denied",
        "dispatch_failed",
        "failed",
        "failure",
        "host_denied_admission",
        "in_waiting_room_timeout",
        "join_failed",
        "join_failed_internal",
        "join_failed_waiting_room_timeout",
        "join_timeout",
        "left_meeting",
        "pending_start_failed",
        "start_failed",
        "stopped",
        "waiting_room_timeout",
    }
)
_NOTE_PRE_CAPTURE_TERMINAL_STATUSES = frozenset(
    {
        "blocked",
        "caas_launch_failed",
        "canceled",
        "cancelled",
        "container_start_failed",
        "denied",
        "dispatch_failed",
        "host_denied_admission",
        "in_waiting_room_timeout",
        "join_failed",
        "join_failed_internal",
        "join_failed_waiting_room_timeout",
        "join_timeout",
        "pending_start_failed",
        "start_failed",
        "stopped",
        "waiting_room_timeout",
    }
)
_NOTE_PRE_CAPTURE_STATUSES = (
    _NOTE_WAITING_STATUSES | _NOTE_JOINING_STATUSES | _NOTE_PRE_CAPTURE_TERMINAL_STATUSES
)
_NOTE_READY_STATUSES = frozenset(
    {
        "complete",
        "completed",
        "done",
        "finished",
        "notes_published",
        "processed",
        "ready",
        "succeeded",
        "success",
    }
)


def project_status(row: Mapping[str, object]) -> RecordMeetingNoteStatus:
    labels = _project_status_labels(row)
    if any(
        label in _NOTE_FAILED_STATUSES or label.endswith(("_failed", "_failure"))
        for _, label in labels
    ):
        return "failed"
    active_hosted_status = any(
        index < 4 and label in _NOTE_ACTIVE_STATUSES for index, label in labels
    )
    for _, label in labels:
        if label == "cca_complete" and not active_hosted_status:
            return "cca_complete"
        if label in _NOTE_WAITING_STATUSES:
            return "waiting"
        if label in _NOTE_JOINING_STATUSES:
            return "joining"
        if label in _NOTE_RECORDING_STATUSES:
            return "recording"
        if label in _NOTE_UPLOADING_STATUSES:
            return "uploading"
        if label in _NOTE_PROCESSING_STATUSES:
            return "processing"
        if label in _NOTE_READY_STATUSES and not active_hosted_status:
            return "ready"
    return "ready"


def _project_status_labels(
    row: Mapping[str, object],
) -> tuple[tuple[int, str], ...]:
    status_value = row.get("status")
    status: Mapping[str, object] = status_value if is_json(status_value) else {}
    candidates = (
        status.get("processingStatus"),
        row.get("processingStatus"),
        status.get("processingState"),
        row.get("processingState"),
        status.get("status"),
        status_value if isinstance(status_value, str) else None,
    )
    labels = tuple(
        (index, re.sub(r"[-\s]+", "_", value.lower()))
        for index, candidate in enumerate(candidates)
        if (value := nonempty_string(candidate, maximum_bytes=128)) is not None
    )
    return labels


def project_list_status(
    row: Mapping[str, object],
) -> RecordMeetingNoteStatus | None:
    """Project only lifecycle states that belong in the Past notes surface."""

    status_value = row.get("status")
    if is_json(status_value):
        labels = _project_status_labels(row)
        if any(label in _NOTE_PRE_CAPTURE_STATUSES for _, label in labels):
            return None
        legacy_status = project_status(row)
        return legacy_status

    top_level_status = _normalized_status_label(status_value)
    if top_level_status == "cca_complete":
        return "cca_complete"
    if top_level_status is None:
        # Historical completed rows may not carry a status. Do not promote a
        # processing or failure side-channel into a lifecycle outcome.
        return "ready" if project_status(row) == "ready" else None
    if top_level_status in _NOTE_READY_STATUSES:
        return "ready"
    if top_level_status == "empty":
        return "ready"
    if top_level_status in {"failed", "failure"}:
        return "failed"
    if top_level_status in _NOTE_WAITING_STATUSES | _NOTE_JOINING_STATUSES:
        return None
    if top_level_status in _NOTE_ACTIVE_STATUSES:
        return _project_active_list_status(row, top_level_status=top_level_status)
    return None


def _project_active_list_status(
    row: Mapping[str, object],
    *,
    top_level_status: str,
) -> RecordMeetingNoteStatus | None:
    """Refine an active lifecycle without accepting stale terminal signals."""

    if top_level_status not in _NOTE_GENERIC_ACTIVE_STATUSES:
        if top_level_status in _NOTE_RECORDING_STATUSES:
            return "recording"
        if top_level_status in _NOTE_UPLOADING_STATUSES:
            return "uploading"
        if top_level_status in _NOTE_PROCESSING_STATUSES:
            return "processing"

    for _, label in _project_status_labels(row):
        if label in _NOTE_PRE_CAPTURE_STATUSES:
            return None
        if label in _NOTE_RECORDING_STATUSES:
            return "recording"
        if label in _NOTE_UPLOADING_STATUSES:
            return "uploading"
        if label in _NOTE_PROCESSING_STATUSES:
            return "processing"
    return None


def project_processing_stage(
    row: Mapping[str, object], status: RecordMeetingNoteStatus
) -> RecordMeetingProcessingStage | None:
    if status != "processing":
        return None
    for index, label in _project_status_labels(row):
        if index > 1:
            continue
        if label in {"transcribing", "diarizing", "preparing_transcript"}:
            return "transcribing"
        if label in {
            "summarizing",
            "summarizing_from_original_transcript",
            "summarizing_without_audio",
        }:
            return "preparing-notes"
    return None


def _normalized_status_label(value: object) -> str | None:
    label = nonempty_string(value, maximum_bytes=128)
    if label is None:
        return None
    return re.sub(r"[-\s]+", "_", label.lower())


def project_fetch_status(
    *,
    status: RecordMeetingNoteStatus,
) -> RecordMeetingFetchStatus:
    if status in {"joining", "waiting", "recording", "uploading", "processing"}:
        return "processing"
    if status in {"ready", "cca_complete"}:
        return "fetchable"
    return "unavailable"
