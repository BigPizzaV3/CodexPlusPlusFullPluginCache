#!/usr/bin/env python3
"""Public, display-safe projection for ChatGPT Meetings native control."""

from __future__ import annotations

import logging
import math
import re
from urllib.parse import urlsplit

from control_protocol import (
    SAFE_LOCAL_REQUEST_FAILED_MESSAGE,
    SAFE_LOCAL_UNAVAILABLE_MESSAGE,
    ControlUnavailable,
    compatible_native_release_version,
)
from native_runtime import ControlCapability
from recording_control_action_contract import (
    ControlAction,
    ControlAutomationFlags,
    ControlAutomationPolicy,
    ControlAutomationPolicyCTA,
    ControlPlatform,
    control_action_arguments_are_valid,
    is_control_automation_flags,
)
from recording_control_stream_contract import (
    CONTROL_STREAM_LIVE_PROTOCOL_VERSION,
)
from recording_status_contract import (
    RECORDING_HEADLESS_SYNC_STATUS_VALUES,
    RECORDING_NATIVE_STATUS_VALUES,
    RECORDING_PERMISSION_VALUES,
    RECORDING_STARTUP_RECOVERY_VALUES,
    RECORDING_STATUS_SCHEMA_VERSION,
    RECORDING_STATUS_SCHEMA_VERSION_MAX,
    RECORDING_UPLOAD_PHASE_VALUES,
    RecordingHeadlessSettings,
    RecordingHeadlessSyncStatus,
    RecordingHeadlessWidgetProjection,
    RecordingNativeStatus,
    RecordingPermissionPresentation,
    RecordingPermissions,
    RecordingStartup,
    RecordingStartupRecovery,
    RecordingUploadPhase,
    is_recording_details,
    is_recording_startup,
    is_recording_upload,
    parse_recording_schema_compatibility,
    parse_recording_status,
)

from helpers import is_json, is_json_array

# These are deliberately open boundaries: release metadata, authenticated wire,
# and sanitized projections must preserve legacy and additive observations.
DarwinReleaseMetadata = dict[str, object]
RawNativeState = dict[str, object]
PublicNativeState = dict[str, object]
PublicNativeBranch = dict[str, object]
PublicNoteDetail = dict[str, object]
PublicControlPayload = dict[str, object]

MAXIMUM_JAVASCRIPT_SAFE_INTEGER = RECORDING_STATUS_SCHEMA_VERSION_MAX
_RECORDING_STATUS_LOGGER = logging.getLogger(__name__)
_SAFE_RECORDING_SCHEMA_DIAGNOSTIC = re.compile(r"[A-Za-z0-9_.-]{1,64}\Z")
_SENSITIVE_RECORDING_SCHEMA_DIAGNOSTIC = re.compile(
    r"(?:^sk-|token|bearer|secret|credential|password|authorization|api[_-]?key|cookie|private)",
    re.IGNORECASE,
)
SAFE_UNSUPPORTED_RECORDING_SCHEMA_MESSAGE = "Meetings recording status uses an unsupported schema"

UPDATE_HANDOFF_CAPABILITY = ControlCapability.LIFECYCLE_UPDATE_HANDOFF_V1.value
UPDATE_HANDOFF_WORK_FENCE_CAPABILITY = (
    ControlCapability.LIFECYCLE_UPDATE_HANDOFF_WORK_FENCE_V1.value
)
UPDATE_HANDOFF_RESUMABLE_OUTBOX_CAPABILITY = (
    ControlCapability.LIFECYCLE_UPDATE_HANDOFF_RESUMABLE_OUTBOX_V1.value
)
UPDATE_HANDOFF_RESUMABLE_OUTBOX_V2_CAPABILITY = (
    ControlCapability.LIFECYCLE_UPDATE_HANDOFF_RESUMABLE_OUTBOX_V2.value
)
LOG_VIEWER_CAPABILITY = ControlCapability.LOGS_VIEWER_V1.value
HOME_BOOTSTRAP_CAPABILITIES = (ControlCapability.HOME_CACHE_V1.value,)
SETTINGS_RECONCILIATION_CAPABILITY = "headless.settings-reconciliation.v1"
WIDGET_PROJECTION_CAPABILITY = "headless.widget-projection.v1"
SYNC_ATTEMPT_ID_CAPABILITY = "headless.sync-attempt-id.v1"
SESSION_FENCED_CONTROLS_CAPABILITY = ControlCapability.RECORDING_SESSION_FENCED_CONTROLS_V1.value
CONTROL_REQUIRED_CAPABILITIES = (
    ControlCapability.CONTROL_LOCAL_STREAM_V1.value,
    ControlCapability.CAPTURE_CONTEXT_V1.value,
    ControlCapability.RECORDING_STOP_V1.value,
    ControlCapability.RECORDING_PAUSE_RESUME_V1.value,
    ControlCapability.RECORDING_RECEIPT_V1.value,
    ControlCapability.UPLOAD_OUTBOX_V1.value,
    ControlCapability.UPLOAD_POST_STOP_V1.value,
    ControlCapability.UPLOAD_MANUAL_RETRY_V1.value,
    ControlCapability.HEADLESS_SETTINGS_V1.value,
    ControlCapability.HEADLESS_SYNC_HOOK_V1.value,
    ControlCapability.HEADLESS_NOTE_DETAIL_V1.value,
    LOG_VIEWER_CAPABILITY,
    ControlCapability.AUTH_CODEX_READINESS_V1.value,
)
WINDOWS_PLATFORM_KEYS = frozenset(
    (ControlPlatform.WINDOWS_X64.value, ControlPlatform.WINDOWS_ARM64.value)
)
CONTROL_CAPABILITIES = (
    *CONTROL_REQUIRED_CAPABILITIES,
    UPDATE_HANDOFF_CAPABILITY,
    SESSION_FENCED_CONTROLS_CAPABILITY,
)


def _compatible_protected_owner_state(state: object) -> bool:
    """Require one strictly safe, schema-compatible idle companion owner."""

    if (
        not is_json(state)
        or not parse_recording_schema_compatibility(
            state.get("schemaVersion"),
            field_present="schemaVersion" in state,
        ).supports_recording_authority
        or state.get("status") != RecordingNativeStatus.IDLE.value
        or state.get("canStop") is not False
        or state.get("sessionId") is not None
        or (state.get("admissionFenced") is not None and state.get("admissionFenced") is not False)
        or (
            state.get("handoffQuiescent") is not None and state.get("handoffQuiescent") is not False
        )
    ):
        return False
    startup = state.get("startup")
    if not is_recording_startup(startup):
        return False
    recovery = startup.get("recovery")
    attention = startup.get("attention")
    if recovery == RecordingStartupRecovery.READY.value:
        if attention is not None and attention != {"kind": _RETAINED_AUDIO_ATTENTION_KIND}:
            return False
    elif (
        recovery != RecordingStartupRecovery.BLOCKED.value
        or state.get("canStart") is not True
        or attention
        != {
            "kind": _STARTUP_RECOVERY_FAILURE_KIND,
            "stage": "outbox",
            "outcome": "returned-false",
        }
    ):
        return False

    return True


def compatible_existing_owner_state(state: object) -> bool:
    """Require a signed compatible owner that is safe to keep recording with."""

    return (
        is_json(state)
        and state.get("canStart") is True
        and _compatible_protected_owner_state(state)
    )


def compatible_read_only_settings_owner_state(state: object) -> bool:
    """Require a safe companion owner without granting recording authority."""

    return (
        is_json(state)
        and isinstance(state.get("canStart"), bool)
        and _compatible_protected_owner_state(state)
    )


def compatible_darwin_release_identity(info: DarwinReleaseMetadata) -> str:
    """Require one bounded native release identity before ordering builds."""

    marketing_version = info.get("CFBundleShortVersionString")
    if not compatible_native_release_version(marketing_version):
        raise ControlUnavailable("native release version is unsupported")
    release_version = info.get("ChatGPTMeetingsVersion")
    if release_version is None:
        build_number = info.get("CFBundleVersion")
        if (
            not isinstance(build_number, str)
            or re.fullmatch(r"[1-9][0-9]{0,8}", build_number) is None
        ):
            raise ControlUnavailable("native release build is malformed")
        return f"{marketing_version}-alpha.{build_number}"
    if (
        not isinstance(release_version, str)
        or release_version.split("-", 1)[0].split("+", 1)[0] != marketing_version
    ):
        raise ControlUnavailable("native release version is malformed")
    return release_version


_PUBLIC_NATIVE_STATE_KEYS = frozenset(
    {
        "schemaVersion",
        "status",
        "meetingId",
        "sessionId",
        "startedAt",
        "message",
        "lastCaptureFailed",
        "canStart",
        "canStop",
        "admissionFenced",
        "handoffQuiescent",
        "canPause",
        "canResume",
        "permissions",
        "recording",
        "upload",
        "startup",
        "capabilities",
        "source",
        "bridge",
        "settings",
        "policy",
        "headless",
        "syncRequest",
    }
)
_OPAQUE_NATIVE_MEETING_ID_PATTERN = re.compile(r"^(?:upcoming|hosted|recording)-[a-f0-9]{64}\Z")
_OPAQUE_NATIVE_RECORDING_ID_PATTERN = re.compile(r"^recording-[a-f0-9]{64}\Z")
_OPAQUE_NATIVE_SESSION_ID_PATTERN = re.compile(
    r"(?:session_[a-f0-9]{32}|session-[a-f0-9]{8}-[a-f0-9]{4}-"
    r"[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})\Z"
)
_MAXIMUM_NOTE_DETAIL_BYTES = 256 * 1024
_SAFE_NOTE_DETAIL_STATUSES = frozenset({"ready", "processing", "unavailable", "needs-sign-in"})
_PUBLIC_NATIVE_CAPABILITIES = frozenset(
    {
        *CONTROL_CAPABILITIES,
        UPDATE_HANDOFF_WORK_FENCE_CAPABILITY,
        UPDATE_HANDOFF_RESUMABLE_OUTBOX_CAPABILITY,
        UPDATE_HANDOFF_RESUMABLE_OUTBOX_V2_CAPABILITY,
        ControlCapability.UPLOAD_MANUAL_RETRY_TARGETED_V1.value,
    }
)


_PUBLIC_HEADLESS_CAPABILITIES = frozenset(
    {
        *_PUBLIC_NATIVE_CAPABILITIES,
        *HOME_BOOTSTRAP_CAPABILITIES,
        SETTINGS_RECONCILIATION_CAPABILITY,
        WIDGET_PROJECTION_CAPABILITY,
        SYNC_ATTEMPT_ID_CAPABILITY,
    }
)
_SAFE_NATIVE_TIMESTAMP_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z\Z")
_SAFE_NOTE_DETAIL_SCOPE_REVISION_PATTERN = re.compile(r"[a-f0-9]{32}\.[0-9]{1,20}\Z")
_SAFE_SYNC_ATTEMPT_ID_PATTERN = re.compile(r"[a-f0-9]{32}\Z")
_RETAINED_AUDIO_ATTENTION_KIND = "retained-audio-needs-manual-recovery"
_STARTUP_RECOVERY_FAILURE_KIND = "startup-recovery-failed"
_STARTUP_RECOVERY_FAILURE_PAIRS = frozenset(
    {
        ("outbox", "returned-false"),
        ("rust-report", "returned-false"),
        ("rust-report", "threw"),
        ("native-scratch", "threw"),
    }
)
_PUBLIC_NATIVE_BRANCH_KEYS: dict[str, frozenset[str]] = {
    "recording": frozenset(
        {
            "mixedBytes",
            "activityLevel",
            "startedAt",
            "lastAudioSavedLocally",
            "lastAudioBytes",
            "lastAudioDurationMs",
            "lastRecording",
        }
    ),
    "lastRecording": frozenset(
        {
            "meetingId",
            "recordingId",
            "sessionId",
            "startedAt",
            "stoppedAt",
            "savedLocally",
            "streamingCompleted",
            "audioBytes",
            "audioDurationMs",
        }
    ),
    "upload": frozenset(
        {
            "phase",
            "pendingCount",
            "hasDurableReceipt",
            "canRetry",
            "retryRecordingId",
            "completedRecordingId",
            "completedMeetingId",
            "queue",
        }
    ),
    "startup": frozenset({"recovery", "attention"}),
    "bridge": frozenset({"target", "protocolVersion"}),
    "settings": frozenset(
        {
            "schemaVersion",
            "available",
            "backgroundEnabled",
            "soundEffectsEnabled",
            "calendarSyncEnabled",
            "calendarReminderEnabled",
            "meetingDetectionEnabled",
            "syncIntervalMinutes",
            "syncIntervalBoundsMinutes",
        }
    ),
    "syncIntervalBoundsMinutes": frozenset({"minimum", "maximum"}),
    "headless": frozenset(
        {
            "status",
            "auth",
            "noteDetail",
            "sync",
            "settings",
            "widgetProjection",
            "capabilities",
        }
    ),
    "widgetProjection": frozenset({"status"}),
    "auth": frozenset({"status", "canUpload"}),
    # The companion exposes only fixed revocation metadata here. The monotonic
    # process-local revision contains no scope identity; it lets the webview
    # clear A's text after an A -> unavailable -> B transition even if both
    # sampled endpoints say available. Private content remains action-scoped.
    "noteDetail": frozenset({"available", "scopeRevision"}),
    "sync": frozenset(
        {
            "status",
            "attemptId",
            "lastRequestedAt",
            "calendarImplementation",
            "markdownImplementation",
            "calendar",
            "markdown",
        }
    ),
    "calendar": frozenset(
        {
            "phase",
            "connected",
            "eventCount",
            "skippedEventCount",
            "lastAttemptAtMs",
            "lastSuccessfulSyncAtMs",
            "retainedLastGood",
            "scopeBound",
        }
    ),
    "markdown": frozenset(
        {
            "phase",
            "receiptCount",
            "projectedCount",
            "writtenCount",
            "waitingCount",
        }
    ),
    "syncRequest": frozenset({"disposition", "attemptId"}),
}
_SAFE_NATIVE_STRING_VALUES: dict[str, frozenset[str]] = {
    "status": frozenset(RECORDING_NATIVE_STATUS_VALUES),
    "recovery": frozenset(RECORDING_STARTUP_RECOVERY_VALUES),
    "source": frozenset({"chatgpt-meetings-native"}),
    "target": frozenset({"chatgpt-meetings", "chatgpt-meetings-dev"}),
    "calendarImplementation": frozenset({"ready"}),
    "markdownImplementation": frozenset({"ready"}),
    "disposition": frozenset({"queued", "already-running", "suppressed"}),
}
_SAFE_NATIVE_PHASE_VALUES: dict[str, frozenset[str]] = {
    "upload": frozenset(RECORDING_UPLOAD_PHASE_VALUES),
    "calendar": frozenset(
        {
            "idle",
            "refreshing",
            "ready",
            "retained-last-good",
            "unavailable",
            "auth-unavailable",
        }
    ),
    "markdown": frozenset(
        {
            "idle",
            "disabled",
            "syncing",
            "synced",
            "waiting-for-projection",
            "needs-sign-in",
            "needs-attention",
        }
    ),
}
_SAFE_POLICY_STATUSES = frozenset({"loading", "ready", "empty", "error"})
_SAFE_POLICY_SEVERITIES = frozenset({"info", "warning"})
_SAFE_POLICY_KEYS = frozenset({"status", "title", "message", "severity", "cta", "automation"})
_SAFE_POLICY_CTA_KEYS = frozenset({"label", "url"})
_SAFE_PERMISSION_PRESENTATIONS = frozenset(
    value
    for value in RECORDING_PERMISSION_VALUES
    if value != RecordingPermissionPresentation.UNKNOWN.value
)
_NATIVE_PERMISSION_SOURCE = "native"


def _fixed_policy_payload(status: str) -> ControlAutomationPolicy:
    """Return the only non-config copy allowed for transitional states."""

    if status == "loading":
        return {
            "status": "loading",
            "title": "Checking for a Meetings message",
            "message": "Loading the latest message for this Codex account.",
            "severity": "info",
            "cta": None,
            "automation": {
                "autoRecordPopupsAllowed": False,
            },
        }
    if status == "error":
        return {
            "status": "error",
            "title": "Meetings message unavailable",
            "message": "The latest Meetings message could not be loaded.",
            "severity": "warning",
            "cta": None,
            "automation": {
                "autoRecordPopupsAllowed": False,
            },
        }
    return {
        "status": "empty",
        "title": "",
        "message": "",
        "severity": "info",
        "cta": None,
        "automation": {
            "autoRecordPopupsAllowed": False,
        },
    }


fixed_policy_payload = _fixed_policy_payload


def _safe_policy_text(value: object, *, maximum_bytes: int) -> str | None:
    """Collapse bounded display copy and reject control characters."""

    if not isinstance(value, str):
        return None
    collapsed = " ".join(value.split()).strip()
    if (
        not collapsed
        or len(collapsed.encode("utf-8")) > maximum_bytes
        or any(ord(character) < 32 or ord(character) == 127 for character in collapsed)
    ):
        return None
    return collapsed


def _safe_policy_cta(value: object) -> ControlAutomationPolicyCTA | None:
    if not is_json(value) or not set(value).issubset(_SAFE_POLICY_CTA_KEYS):
        return None
    label = _safe_policy_text(value.get("label"), maximum_bytes=64)
    raw_url = _safe_policy_text(value.get("url"), maximum_bytes=2_048)
    if not label or not raw_url:
        return None
    parsed = urlsplit(raw_url)
    if (
        parsed.scheme.lower() != "https"
        or not parsed.hostname
        or parsed.username is not None
        or parsed.password is not None
    ):
        return None
    return {"label": label, "url": raw_url}


def safe_policy_payload(value: object) -> ControlAutomationPolicy:
    """Project the native notice to a fixed, display-only MCP shape.

    The signed native state is still not a license to expose arbitrary
    Statsig initialize values to a model or iframe. Replacing the whole
    policy object drops raw payloads, identities, rule metadata, and future
    fields from cached companions.

    Args:
        value: Untrusted signed policy payload from the native companion.

    Returns:
        A bounded display-only policy using fixed fallback copy when invalid.
    """

    if not is_json(value) or not set(value).issubset(_SAFE_POLICY_KEYS):
        return _fixed_policy_payload("error")
    status = value.get("status")
    if not isinstance(status, str) or status not in _SAFE_POLICY_STATUSES:
        return _fixed_policy_payload("error")
    raw_automation = value.get("automation")
    automation: ControlAutomationFlags
    if is_control_automation_flags(raw_automation):
        automation = raw_automation
    else:
        automation = {
            "autoRecordPopupsAllowed": False,
        }
    if status in {"loading", "error"}:
        return _fixed_policy_payload(status)
    if status == "empty":
        policy = _fixed_policy_payload(status)
        policy["automation"] = automation
        return policy

    message = _safe_policy_text(value.get("message"), maximum_bytes=1_024)
    if not message:
        policy = _fixed_policy_payload("empty")
        policy["automation"] = automation
        return policy
    title = _safe_policy_text(value.get("title"), maximum_bytes=120)
    severity = value.get("severity")
    return {
        "status": "ready",
        "title": title or "Meetings",
        "message": message,
        "severity": (
            severity
            if isinstance(severity, str) and severity in _SAFE_POLICY_SEVERITIES
            else "info"
        ),
        "cta": _safe_policy_cta(value.get("cta")),
        "automation": automation,
    }


def _safe_note_detail_payload(value: object) -> PublicNoteDetail:
    """Project one transient explicit-selection detail response.

    This field never belongs to authenticated stream state. Keep it narrow enough that a
    stale or hostile companion cannot smuggle paths, ids, titles, or arbitrary
    response branches through the one app-only detail action. Summary and
    transcript stay separate so the app can truthfully render a missing
    summary without turning transcript text into summary copy.
    """

    if not is_json(value):
        return {"status": "unavailable"}
    status = value.get("status")
    if not isinstance(status, str) or status not in _SAFE_NOTE_DETAIL_STATUSES:
        return {"status": "unavailable"}
    scope_revision = value.get("scopeRevision")
    revision_is_safe = (
        isinstance(scope_revision, str)
        and _SAFE_NOTE_DETAIL_SCOPE_REVISION_PATTERN.fullmatch(scope_revision) is not None
    )
    if status != "ready":
        if set(value) == {"status"}:
            return {"status": status}
        if set(value) == {"status", "scopeRevision"} and revision_is_safe:
            return {"status": status, "scopeRevision": scope_revision}
        return {"status": "unavailable"}
    if set(value) != {"status", "summary", "transcript", "scopeRevision"} or not revision_is_safe:
        return {"status": "unavailable"}

    def safe_text(raw: object) -> object:
        if raw is None:
            return None
        if not isinstance(raw, str):
            return object()
        normalized = raw.replace("\r\n", "\n").replace("\r", "\n").strip()
        if len(normalized.encode("utf-8")) > _MAXIMUM_NOTE_DETAIL_BYTES or any(
            ord(character) < 32 and character not in {"\t", "\n"} for character in normalized
        ):
            return object()
        return normalized or None

    summary = safe_text(value.get("summary"))
    transcript = safe_text(value.get("transcript"))
    if (summary is not None and not isinstance(summary, str)) or (
        transcript is not None and not isinstance(transcript, str)
    ):
        return {"status": "unavailable"}
    total_bytes = sum(
        len(field.encode("utf-8")) for field in (summary, transcript) if isinstance(field, str)
    )
    if total_bytes > _MAXIMUM_NOTE_DETAIL_BYTES:
        return {"status": "unavailable"}
    return {
        "status": "ready",
        "summary": summary,
        "transcript": transcript,
        "scopeRevision": scope_revision,
    }


def _safe_opaque_native_meeting_id(value: object) -> str | None:
    """Keep only widget-owned opaque correlation, never provider identifiers."""

    if not isinstance(value, str) or not _OPAQUE_NATIVE_MEETING_ID_PATTERN.fullmatch(value):
        return None
    return value


def _safe_opaque_native_recording_id(value: object) -> str | None:
    """Keep only the exact opaque local-intent join, never raw intent ids."""

    if not isinstance(value, str) or not _OPAQUE_NATIVE_RECORDING_ID_PATTERN.fullmatch(value):
        return None
    return value


def _verified_durable_recording_completion(value: RawNativeState, upload: RawNativeState) -> bool:
    """Preserve a verified historical completion across newer capture and uploads."""

    if upload.get("hasDurableReceipt") is not True or value.get("admissionFenced") is True:
        return False

    recording = value.get("recording")
    if not is_json(recording):
        return False
    receipt = recording.get("lastRecording")
    if not is_json(receipt) or receipt.get("savedLocally") is not True:
        return False

    recording_id = _safe_opaque_native_recording_id(upload.get("completedRecordingId"))
    if recording_id is None or receipt.get("recordingId") != recording_id:
        return False

    meeting_id = _safe_opaque_native_meeting_id(upload.get("completedMeetingId"))
    return meeting_id is not None and meeting_id.startswith("hosted-")


def _verified_streaming_recording_completion(
    value: RawNativeState,
    *,
    allow_fenced_streaming_completion: bool = False,
) -> bool:
    """Accept acknowledged direct upload for its exact authenticated recording."""

    recording = value.get("recording")
    upload = value.get("upload")
    if not is_recording_details(recording) or not is_recording_upload(upload):
        return False
    receipt = recording.get("lastRecording")
    if (
        receipt is None
        or receipt.get("streamingCompleted") is not True
        or upload.get("phase") != RecordingUploadPhase.UPLOADED.value
    ):
        return False
    if value.get("admissionFenced") is True and not (
        allow_fenced_streaming_completion
        and value.get("handoffQuiescent") is True
        and value.get("status") == RecordingNativeStatus.IDLE.value
        and value.get("canStart") is False
        and value.get("canStop") is False
        and value.get("canPause", False) is False
        and value.get("canResume", False) is False
        and value.get("sessionId") is None
        and value.get("startedAt") is None
    ):
        return False

    recording_id = receipt.get("recordingId")
    # Generated receipt/upload validators already constrain both identifier formats.
    if recording_id is None or upload.get("completedRecordingId") != recording_id:
        return False

    if any(
        session_id is not None
        and not control_action_arguments_are_valid(
            ControlAction.STOP,
            {"expectedSessionId": session_id},
        )
        for session_id in (value.get("sessionId"), receipt.get("sessionId"))
    ):
        return False

    state_meeting = value.get("meetingId")
    receipt_meeting = receipt.get("meetingId")
    if any(
        meeting_id is not None and _safe_opaque_native_meeting_id(meeting_id) is None
        for meeting_id in (state_meeting, receipt_meeting)
    ):
        return False
    if (
        isinstance(state_meeting, str)
        and state_meeting.startswith("hosted-")
        and receipt_meeting is not None
        and state_meeting != receipt_meeting
    ):
        return False

    completed_meeting = upload.get("completedMeetingId")
    return completed_meeting is None or (
        _safe_opaque_native_meeting_id(completed_meeting) is not None
        and completed_meeting.startswith("hosted-")
        and (receipt_meeting is None or completed_meeting == receipt_meeting)
        and (
            not isinstance(state_meeting, str)
            or not state_meeting.startswith("hosted-")
            or completed_meeting == state_meeting
        )
    )


_DROP_NATIVE_VALUE = object()


def _safe_observed_recording_schema_version(value: object) -> object:
    """Keep only bounded, display-safe authenticated version diagnostics."""

    if value is None or type(value) is bool:
        return value
    if type(value) is int and abs(value) <= MAXIMUM_JAVASCRIPT_SAFE_INTEGER:
        return value
    if (
        type(value) is float
        and math.isfinite(value)
        and abs(value) <= MAXIMUM_JAVASCRIPT_SAFE_INTEGER
    ):
        return value
    if (
        isinstance(value, str)
        and _SAFE_RECORDING_SCHEMA_DIAGNOSTIC.fullmatch(value)
        and not _SENSITIVE_RECORDING_SCHEMA_DIAGNOSTIC.search(value)
    ):
        return value
    return None


def _mark_unsupported_recording_schema(
    state: PublicNativeState,
    *,
    field: str,
    value: object,
) -> None:
    """Make unknown authenticated recording contracts strictly non-actionable."""

    observed = _safe_observed_recording_schema_version(value)
    _RECORDING_STATUS_LOGGER.warning(
        "Unsupported Meetings recording contract %s=%r",
        field,
        observed,
    )
    state["status"] = RecordingNativeStatus.UNKNOWN.value
    state.update(dict.fromkeys(("canStart", "canStop", "canPause", "canResume"), False))
    state["message"] = SAFE_UNSUPPORTED_RECORDING_SCHEMA_MESSAGE


def _safe_native_scalar(key: str, value: object, *, branch: str | None = None) -> object:
    """Project one scalar from an allowlisted native branch."""

    if key == "schemaVersion" and branch is None:
        return _safe_observed_recording_schema_version(value)
    if key == "meetingId":
        return _safe_opaque_native_meeting_id(value)
    if key == "recordingId":
        return _safe_opaque_native_recording_id(value)
    if key in {"retryRecordingId", "completedRecordingId"}:
        return (
            value
            if control_action_arguments_are_valid(
                ControlAction.RETRY_UPLOAD_TARGET,
                {"recordingId": value},
            )
            else _DROP_NATIVE_VALUE
        )
    if key == "completedMeetingId":
        return (
            value
            if isinstance(value, str)
            and value.startswith("hosted-")
            and _safe_opaque_native_meeting_id(value) == value
            else _DROP_NATIVE_VALUE
        )
    if key == "sessionId":
        return (
            value
            if isinstance(value, str) and _OPAQUE_NATIVE_SESSION_ID_PATTERN.fullmatch(value)
            else _DROP_NATIVE_VALUE
        )
    if key in {"startedAt", "stoppedAt", "lastRequestedAt"}:
        return (
            value
            if isinstance(value, str) and _SAFE_NATIVE_TIMESTAMP_PATTERN.fullmatch(value)
            else None
        )
    if key == "phase":
        allowed = _SAFE_NATIVE_PHASE_VALUES.get(branch or "", frozenset())
        return value if isinstance(value, str) and value in allowed else _DROP_NATIVE_VALUE
    if key in _SAFE_NATIVE_STRING_VALUES:
        return (
            value
            if isinstance(value, str) and value in _SAFE_NATIVE_STRING_VALUES[key]
            else _DROP_NATIVE_VALUE
        )
    if key == "scopeRevision":
        return (
            value
            if isinstance(value, str) and _SAFE_NOTE_DETAIL_SCOPE_REVISION_PATTERN.fullmatch(value)
            else _DROP_NATIVE_VALUE
        )
    if key == "attemptId":
        return (
            value
            if isinstance(value, str) and _SAFE_SYNC_ATTEMPT_ID_PATTERN.fullmatch(value)
            else _DROP_NATIVE_VALUE
        )
    if key in {
        "canStart",
        "canStop",
        "admissionFenced",
        "handoffQuiescent",
        "canPause",
        "lastCaptureFailed",
        "canResume",
        "lastAudioSavedLocally",
        "savedLocally",
        "streamingCompleted",
        "hasDurableReceipt",
        "canRetry",
        "available",
        "backgroundEnabled",
        "soundEffectsEnabled",
        "calendarSyncEnabled",
        "calendarReminderEnabled",
        "meetingDetectionEnabled",
        "canUpload",
        "connected",
        "retainedLastGood",
        "scopeBound",
    }:
        return value if isinstance(value, bool) else _DROP_NATIVE_VALUE
    if key == "activityLevel":
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            number = float(value)
            if math.isfinite(number) and 0 <= number <= 1:
                return number
        return _DROP_NATIVE_VALUE
    if key in {
        "mixedBytes",
        "lastAudioBytes",
        "lastAudioDurationMs",
        "audioBytes",
        "audioDurationMs",
        "pendingCount",
        "protocolVersion",
        "schemaVersion",
        "syncIntervalMinutes",
        "minimum",
        "maximum",
        "eventCount",
        "skippedEventCount",
        "lastAttemptAtMs",
        "lastSuccessfulSyncAtMs",
        "receiptCount",
        "projectedCount",
        "writtenCount",
        "waitingCount",
    }:
        return (
            value
            if isinstance(value, int) and not isinstance(value, bool) and value >= 0
            else _DROP_NATIVE_VALUE
        )
    return _DROP_NATIVE_VALUE


def _safe_native_capabilities(
    value: object,
    *,
    allowed: frozenset[str] = _PUBLIC_NATIVE_CAPABILITIES,
) -> list[str]:
    if not is_json_array(value):
        return []
    return [
        capability for capability in value if isinstance(capability, str) and capability in allowed
    ]


def _public_headless_settings(value: object) -> RecordingHeadlessSettings:
    """Project only the fixed durable post-save reconciliation contract."""

    if not is_json(value):
        return {}
    projected: RecordingHeadlessSettings = {}
    status = value.get("status")
    if isinstance(status, str) and status in {
        "saving",
        "saved-reconciling",
        "ready",
        "unavailable",
    }:
        projected["status"] = status
    saved = value.get("saved")
    if isinstance(saved, bool):
        projected["saved"] = saved
    projection = value.get("projection")
    if isinstance(projection, str) and projection in {
        "pending",
        "reconciling",
        "settled",
        "unavailable",
    }:
        projected["projection"] = projection
    revision = value.get("revision")
    if (
        isinstance(revision, int)
        and not isinstance(revision, bool)
        and 0 <= revision <= MAXIMUM_JAVASCRIPT_SAFE_INTEGER
    ):
        projected["revision"] = revision
    return projected


def _public_headless_widget_projection(value: object) -> RecordingHeadlessWidgetProjection:
    """Project only the fixed public-row publication obligation."""

    if not is_json(value):
        return {}
    status = value.get("status")
    return (
        {"status": status} if isinstance(status, str) and status in {"revoking", "settled"} else {}
    )


def _public_native_startup(value: object) -> RecordingStartup:
    """Keep Start authority separate from fixed manual-attention copy."""

    if not is_json(value):
        return {}
    recovery = value.get("recovery")
    valid_recoveries = _SAFE_NATIVE_STRING_VALUES["recovery"]
    if not isinstance(recovery, str) or recovery not in valid_recoveries:
        return {}
    projected: RecordingStartup = {"recovery": recovery}
    attention = value.get("attention")
    if (
        recovery == RecordingStartupRecovery.READY.value
        and is_json(attention)
        and set(attention) == {"kind"}
        and attention.get("kind") == _RETAINED_AUDIO_ATTENTION_KIND
    ):
        projected["attention"] = {"kind": _RETAINED_AUDIO_ATTENTION_KIND}
    elif (
        recovery == RecordingStartupRecovery.BLOCKED.value
        and is_json(attention)
        and set(attention) == {"kind", "stage", "outcome"}
        and attention.get("kind") == _STARTUP_RECOVERY_FAILURE_KIND
        and isinstance(attention.get("stage"), str)
        and isinstance(attention.get("outcome"), str)
        and (attention["stage"], attention["outcome"]) in _STARTUP_RECOVERY_FAILURE_PAIRS
    ):
        projected["attention"] = {
            "kind": _STARTUP_RECOVERY_FAILURE_KIND,
            "stage": attention["stage"],
            "outcome": attention["outcome"],
        }
    return projected


def _public_native_upload_queue(value: object) -> dict[str, object] | None:
    """Preserve only bounded authenticated local recording observations."""

    if not is_json(value) or set(value) != {"items"}:
        return None
    items = value["items"]
    if not is_json_array(items) or len(items) > 24:
        return None
    projected: list[dict[str, object]] = []
    seen: set[str] = set()
    required = {"recordingId", "phase", "createdAt", "audioDurationMs", "audioBytes"}
    phases = {"queued", "uploading", "needs-sign-in", "needs-manual-retry"}
    for item in items:
        if not is_json(item) or set(item) != required:
            return None
        recording_id = _safe_opaque_native_recording_id(item["recordingId"])
        created_at = item["createdAt"]
        phase = item["phase"]
        duration = item["audioDurationMs"]
        audio_bytes = item["audioBytes"]
        if (
            recording_id is None
            or recording_id in seen
            or not isinstance(phase, str)
            or phase not in phases
            or not isinstance(created_at, str)
            or len(created_at) > 64
            or _SAFE_NATIVE_TIMESTAMP_PATTERN.fullmatch(created_at) is None
            or type(duration) is not int
            or not 0 <= duration <= MAXIMUM_JAVASCRIPT_SAFE_INTEGER
            or type(audio_bytes) is not int
            or not 0 <= audio_bytes <= MAXIMUM_JAVASCRIPT_SAFE_INTEGER
        ):
            return None
        seen.add(recording_id)
        projected.append(
            {
                "recordingId": recording_id,
                "phase": phase,
                "createdAt": created_at,
                "audioDurationMs": duration,
                "audioBytes": audio_bytes,
            }
        )
    return {"items": projected}


def _public_native_branch(value: object, branch: str) -> PublicNativeBranch | RecordingStartup:
    """Strictly project one known nested native state branch."""

    if branch == "startup":
        return _public_native_startup(value)
    if not is_json(value):
        return {}
    projected: PublicNativeBranch = {}
    for key in _PUBLIC_NATIVE_BRANCH_KEYS[branch]:
        if key not in value:
            continue
        if branch == "upload" and key == "queue":
            queue = _public_native_upload_queue(value[key])
            if queue is not None:
                projected[key] = queue
            continue
        if branch == "headless" and key == "settings":
            projected[key] = _public_headless_settings(value[key])
            continue
        if branch == "headless" and key == "widgetProjection":
            projected[key] = _public_headless_widget_projection(value[key])
            continue
        if branch == "headless" and key == "status":
            candidate = value[key]
            if isinstance(candidate, str) and candidate in {
                "projection-revoking",
                "settings-saving",
                "settings-reconciling",
            }:
                projected[key] = candidate
                continue
        if key in _PUBLIC_NATIVE_BRANCH_KEYS:
            projected[key] = _public_native_branch(value[key], key)
            continue
        if key == "capabilities":
            projected[key] = _safe_native_capabilities(
                value[key],
                allowed=(
                    _PUBLIC_HEADLESS_CAPABILITIES
                    if branch == "headless"
                    else _PUBLIC_NATIVE_CAPABILITIES
                ),
            )
            continue
        safe_value = _safe_native_scalar(key, value[key], branch=branch)
        if safe_value is not _DROP_NATIVE_VALUE:
            projected[key] = safe_value
    return projected


def _permission_presentation(value: object) -> RecordingPermissions:
    """Project signed permission state into bounded display-only values.

    This is presentation metadata, never authorization. A malformed or old
    companion can only produce `unknown`; it cannot make the webview believe
    a capture permission is granted.
    """

    permissions = value if is_json(value) else {}

    def safe_permission(key: str) -> str:
        candidate = permissions.get(key)
        return (
            candidate
            if isinstance(candidate, str) and candidate in _SAFE_PERMISSION_PRESENTATIONS
            else RecordingPermissionPresentation.UNKNOWN.value
        )

    return {
        "microphone": safe_permission("microphone"),
        "systemAudio": safe_permission("systemAudio"),
    }


def _mark_native_permission_state(
    state: PublicNativeState,
    *,
    raw_permissions: object = None,
) -> None:
    """Attach provenance without trusting arbitrary native presentation."""

    permissions = _permission_presentation(
        state.get("permissions") if raw_permissions is None else raw_permissions
    )
    # Keep the compatibility field because the current UI still reads it, but
    # replace the whole nested object instead of merely adding a sanitized
    # sibling. Older companions can otherwise smuggle paths/tokens through it.
    state["permissions"] = dict(permissions)
    state["permissionSource"] = _NATIVE_PERMISSION_SOURCE
    state["permissionPresentation"] = dict(permissions)


def _project_recording_authority(
    value: RawNativeState,
    state: PublicNativeState,
    *,
    streaming_completed: bool,
) -> None:
    """Keep every recording control inside its authenticated, typed contract."""

    compatibility = parse_recording_schema_compatibility(
        value.get("schemaVersion"),
        field_present="schemaVersion" in value,
    )
    native_status = parse_recording_status(value.get("status"))
    if not compatibility.supports_recording_authority:
        _mark_unsupported_recording_schema(
            state,
            field="state.schemaVersion",
            value=value.get("schemaVersion"),
        )
        return
    if native_status is RecordingNativeStatus.UNKNOWN:
        _mark_unsupported_recording_schema(
            state,
            field="state.status",
            value=value.get("status"),
        )
        return

    required_controls = ("canStart", "canStop")
    if any(key in value and type(value[key]) is not bool for key in required_controls) or (
        "schemaVersion" in value and not all(key in value for key in required_controls)
    ):
        malformed_key = next(
            (key for key in required_controls if type(value.get(key)) is not bool),
            "canStart",
        )
        _mark_unsupported_recording_schema(
            state,
            field=f"state.{malformed_key}",
            value=value.get(malformed_key),
        )
        return

    state["status"] = native_status.value
    for key, predicate in (
        ("canStart", native_status.allows_start),
        ("canStop", native_status.allows_stop),
        ("canPause", native_status.allows_pause),
        ("canResume", native_status.allows_resume),
    ):
        state[key] = value.get(key) is True and predicate(compatibility)

    if ("permissions" in value or "permissionPresentation" in value) and any(
        is_json(presentation := state.get(branch))
        and presentation.get(key) in {"unknown", "denied", "unsupported"}
        for branch in ("permissions", "permissionPresentation")
        for key in ("microphone", "systemAudio")
    ):
        state["canStart"] = False

    if "bridge" in value:
        raw_bridge = value["bridge"]
        raw_version = raw_bridge.get("protocolVersion") if is_json(raw_bridge) else None
        raw_generation = raw_bridge.get("controlGeneration") if is_json(raw_bridge) else None
        raw_target = raw_bridge.get("target") if is_json(raw_bridge) else None
        if (
            not is_json(raw_bridge)
            or (
                "target" in raw_bridge
                and (
                    not isinstance(raw_target, str)
                    or raw_target not in _SAFE_NATIVE_STRING_VALUES["target"]
                )
            )
            or type(raw_version) is not int
            or raw_version != CONTROL_STREAM_LIVE_PROTOCOL_VERSION
            or "controlGeneration" in raw_bridge
        ):
            bridge = state.get("bridge")
            if not is_json(bridge):
                bridge = {}
                state["bridge"] = bridge
            if "target" not in bridge:
                bridge["target"] = RecordingNativeStatus.UNKNOWN.value
            if type(raw_version) is not int or raw_version != CONTROL_STREAM_LIVE_PROTOCOL_VERSION:
                malformed_field = "protocolVersion"
                observed = raw_version
            elif is_json(raw_bridge) and "controlGeneration" in raw_bridge:
                malformed_field = "controlGeneration"
                observed = raw_generation
            else:
                malformed_field = "target"
                observed = raw_target
            _mark_unsupported_recording_schema(
                state,
                field=f"state.bridge.{malformed_field}",
                value=observed,
            )
            return

    if "upload" in value:
        raw_upload = value["upload"]
        raw_phase = raw_upload.get("phase") if is_json(raw_upload) else None
        valid_upload = is_json(raw_upload) and (
            "phase" not in raw_upload
            or isinstance(raw_phase, str)
            and raw_phase in RECORDING_UPLOAD_PHASE_VALUES
        )
        if not valid_upload:
            # Historical uploads are optional; redact all unverifiable receipt,
            # retry, and message data without revoking local recorder authority.
            state["upload"] = {"phase": RecordingUploadPhase.UNKNOWN.value}
        if valid_upload and is_json(raw_upload) and "retryRecordingId" in raw_upload:
            upload = state.get("upload")
            capabilities = state.get("capabilities")
            if is_json(upload) and not (
                is_json_array(capabilities)
                and ControlCapability.UPLOAD_MANUAL_RETRY_TARGETED_V1.value in capabilities
                and raw_upload.get("canRetry") is True
                and control_action_arguments_are_valid(
                    ControlAction.RETRY_UPLOAD_TARGET,
                    {"recordingId": raw_upload.get("retryRecordingId")},
                )
            ):
                upload.pop("retryRecordingId", None)
        if (
            valid_upload
            and is_json(raw_upload)
            and ("completedRecordingId" in raw_upload or "completedMeetingId" in raw_upload)
        ):
            upload = state.get("upload")
            if is_json(upload) and not (
                streaming_completed or _verified_durable_recording_completion(value, raw_upload)
            ):
                upload.pop("completedRecordingId", None)
                upload.pop("completedMeetingId", None)

    if "startup" in value:
        raw_startup = value["startup"]
        raw_recovery = raw_startup.get("recovery") if is_json(raw_startup) else None
        if (
            not is_json(raw_startup)
            or not isinstance(raw_recovery, str)
            or raw_recovery not in RECORDING_STARTUP_RECOVERY_VALUES
        ):
            state["startup"] = {"recovery": RecordingStartupRecovery.UNKNOWN.value}
            _mark_unsupported_recording_schema(
                state,
                field="state.startup.recovery",
                value=raw_recovery,
            )
            return

    if "headless" in value:
        raw_headless = value["headless"]
        if not is_json(raw_headless):
            state["headless"] = {"sync": {"status": RecordingHeadlessSyncStatus.UNKNOWN.value}}
        elif "sync" in raw_headless:
            raw_sync = raw_headless["sync"]
            raw_sync_status = raw_sync.get("status") if is_json(raw_sync) else None
            if (
                not is_json(raw_sync)
                or not isinstance(raw_sync_status, str)
                or raw_sync_status not in RECORDING_HEADLESS_SYNC_STATUS_VALUES
            ):
                state["headless"] = {"sync": {"status": RecordingHeadlessSyncStatus.UNKNOWN.value}}


def _public_native_state(
    value: object,
    *,
    allow_fenced_streaming_completion: bool = False,
) -> PublicNativeState:
    """Project one verified native state into its public compatibility shape."""

    if not is_json(value):
        return {}
    state: PublicNativeState = {}
    for key in _PUBLIC_NATIVE_STATE_KEYS:
        if key not in value or key in {"meetingId", "message", "permissions", "policy"}:
            continue
        if key in _PUBLIC_NATIVE_BRANCH_KEYS:
            state[key] = _public_native_branch(value[key], key)
            continue
        if key == "capabilities":
            state[key] = _safe_native_capabilities(value[key])
            continue
        safe_value = _safe_native_scalar(key, value[key])
        if safe_value is not _DROP_NATIVE_VALUE:
            state[key] = safe_value
    streaming_completed = _verified_streaming_recording_completion(
        value,
        allow_fenced_streaming_completion=allow_fenced_streaming_completion,
    )
    recording = state.get("recording")
    if is_json(recording):
        receipt = recording.get("lastRecording")
        if (
            is_json(receipt)
            and receipt.get("streamingCompleted") is True
            and not streaming_completed
        ):
            receipt.pop("streamingCompleted", None)
    if "meetingId" in value:
        state["meetingId"] = _safe_opaque_native_meeting_id(value["meetingId"])
    if "permissions" in value:
        _mark_native_permission_state(state, raw_permissions=value["permissions"])
        if "permissionPresentation" in value:
            state["permissionPresentation"] = _permission_presentation(
                value["permissionPresentation"]
            )
    elif "permissionPresentation" in value:
        state["permissionSource"] = _NATIVE_PERMISSION_SOURCE
        state["permissionPresentation"] = _permission_presentation(value["permissionPresentation"])
    else:
        # A legacy companion never attested permission presentation. Inventing
        # explicit unknown permissions would revoke its authenticated Start.
        state["permissionSource"] = _NATIVE_PERMISSION_SOURCE
    state["message"] = _safe_state_message(state, streaming_completed=streaming_completed)
    if "policy" in value:
        state["policy"] = safe_policy_payload(value.get("policy"))
    _project_recording_authority(
        value,
        state,
        streaming_completed=streaming_completed,
    )
    return state


public_native_state = _public_native_state


def _safe_state_message(
    state: PublicNativeState,
    *,
    streaming_completed: bool,
) -> str:
    """Return fixed UI/model copy without trusting native error strings."""

    status = parse_recording_status(state.get("status"))
    status_copy: dict[RecordingNativeStatus, str] = {
        RecordingNativeStatus.PREPARING: "Protecting local recording",
        RecordingNativeStatus.STARTING: "Starting microphone and system audio",
        RecordingNativeStatus.RECORDING: "Recording microphone and system audio",
        RecordingNativeStatus.PAUSING: "Pausing recording",
        RecordingNativeStatus.PAUSED: "Recording paused",
        RecordingNativeStatus.RESUMING: "Resuming recording",
        RecordingNativeStatus.STOPPING: "Finalizing the recording",
        RecordingNativeStatus.FINALIZATION_FAILED: (
            "Recording could not finish saving. Select Retry Stop to try again."
        ),
        RecordingNativeStatus.OFFLINE: SAFE_LOCAL_UNAVAILABLE_MESSAGE,
    }
    if status in status_copy:
        return status_copy[status]

    startup = state.get("startup")
    if is_json(startup):
        recovery = startup.get("recovery")
        if recovery == RecordingStartupRecovery.RECOVERING.value:
            return "Recovering saved recordings"
        if recovery == RecordingStartupRecovery.BLOCKED.value:
            attention = startup.get("attention")
            if (
                is_json(attention)
                and attention.get("kind") == "startup-recovery-failed"
                and attention.get("stage") == "outbox"
            ):
                return "Upload recovery needs attention; recording remains available"
            return "Recording recovery needs attention"
        attention = startup.get("attention")
        if recovery == RecordingStartupRecovery.READY.value and is_json(attention):
            return "Retained audio may be incomplete and needs manual recovery"

    if state.get("lastCaptureFailed") is True:
        return "Recording stopped before it could be saved"

    recording = state.get("recording")
    if is_recording_details(recording):
        receipt = recording.get("lastRecording")
        if receipt is not None and (receipt.get("savedLocally") is True or streaming_completed):
            return "Recording saved"

    permissions = state.get("permissions")
    if is_json(permissions):
        if permissions.get("microphone") != RecordingPermissionPresentation.GRANTED.value:
            return "Microphone access is required. Enable Meetings in your system privacy settings."
        if permissions.get("systemAudio") == RecordingPermissionPresentation.UNSUPPORTED.value:
            return "System audio is unavailable on this device"
        if permissions.get("systemAudio") != RecordingPermissionPresentation.GRANTED.value:
            return (
                "System audio access is required. Enable Meetings in your system privacy settings."
            )
    return "Local capture ready"


def sanitize_control_payload(
    payload: object,
    *,
    action: str | None = None,
) -> PublicControlPayload:
    """Make verified native state safe for MCP, widgets, and model context."""

    if not is_json(payload):
        return {"ok": False, "error": SAFE_LOCAL_REQUEST_FAILED_MESSAGE}
    sanitized: PublicControlPayload = {
        "ok": payload.get("ok") is True,
    }
    projected_state: PublicNativeState | None = None
    if "state" in payload:
        projected_state = _public_native_state(
            payload.get("state"),
            allow_fenced_streaming_completion=(
                action == ControlAction.QUIT_FOR_UPDATE.value and payload.get("ok") is True
            ),
        )
        sanitized["state"] = projected_state
    if "schemaVersion" in payload:
        raw_version = payload["schemaVersion"]
        sanitized["schemaVersion"] = _safe_observed_recording_schema_version(raw_version)
        raw_state = payload.get("state")
        if (
            type(raw_version) is not int
            or raw_version != RECORDING_STATUS_SCHEMA_VERSION
            or not is_json(raw_state)
            or type(raw_state.get("schemaVersion")) is not int
            or raw_state.get("schemaVersion") != raw_version
        ):
            if projected_state is None:
                projected_state = {}
                sanitized["state"] = projected_state
            _mark_unsupported_recording_schema(
                projected_state,
                field="schemaVersion",
                value=raw_version,
            )
    if action == "getNoteDetail":
        sanitized["detail"] = (
            _safe_note_detail_payload(payload.get("detail"))
            if payload.get("ok") is True
            else {"status": "unavailable"}
        )
    if action == "openLogViewer":
        log_viewer = payload.get("logViewer")
        sanitized["logViewer"] = {
            "opened": bool(
                payload.get("ok") is True
                and is_json(log_viewer)
                and set(log_viewer) == {"opened"}
                and log_viewer.get("opened") is True
            )
        }
    if "error" in payload:
        sanitized["error"] = SAFE_LOCAL_REQUEST_FAILED_MESSAGE
    return sanitized
