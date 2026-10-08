# GENERATED FILE. DO NOT EDIT.
# Source: chatgpt-meetings-core/contracts/recording-status.v1.schema.json
# SHA-256: 890061368df7aa59a222dbea9a710e629c8b9ceb42ce86c851700c40bb8104b8
# Regenerate: python3 chatgpt-meetings-core/scripts/generate_recording_status_contract.py
# Coordinate status consumers explicitly; OpenAI v3 compatibility bindings are frozen.
# Native-produced recording status and MCP-owned offline projection. Endpoint
# schemaVersion 1 is independent of live-control protocolVersion 1 and owner
# generations. An omitted version denotes a legacy response; malformed or future
# versions and bounded unknown values remain non-actionable. Verify the current live
# owner, epoch, platform capabilities, permissions, and recording session before any
# recording, upload, or process mutation.

from __future__ import annotations

import re
from enum import Enum
from typing import TYPE_CHECKING, Final, TypedDict

if TYPE_CHECKING:
    from typing import TypeGuard
else:
    try:
        from typing import TypeGuard
    except ImportError:

        class TypeGuard:
            """Keep schema guards importable on Python 3.9 without dependencies."""

            @classmethod
            def __class_getitem__(cls, _value: object) -> type[bool]:
                return bool


RECORDING_STATUS_SCHEMA_NAME: Final[str] = "chatgpt-meetings.recording-status"
RECORDING_STATUS_SCHEMA_VERSION: Final[int] = 1
RECORDING_STATUS_SCHEMA_VERSION_MAX: Final[int] = 9_007_199_254_740_991
RECORDING_STATUS_SCHEMA_SHA256: Final[str] = (
    "890061368df7aa59a222dbea9a710e629c8b9ceb42ce86c851700c40bb8104b8"
)


class RecordingSchemaCompatibility(str, Enum):
    """Explicit schema proof; unsupported versions never authorize capture."""

    LEGACY = "legacy"
    V1 = "v1"
    UNSUPPORTED = "unsupported"

    @property
    def supports_recording_authority(self) -> bool:
        return self in (
            RecordingSchemaCompatibility.LEGACY,
            RecordingSchemaCompatibility.V1,
        )


def parse_recording_schema_compatibility(
    value: object, *, field_present: bool
) -> RecordingSchemaCompatibility:
    """Require explicit absence or the exact integer schema version."""
    if not field_present:
        return (
            RecordingSchemaCompatibility.LEGACY
            if value is None
            else RecordingSchemaCompatibility.UNSUPPORTED
        )
    return (
        RecordingSchemaCompatibility.V1
        if type(value) is int and value == RECORDING_STATUS_SCHEMA_VERSION
        else RecordingSchemaCompatibility.UNSUPPORTED
    )


RECORDING_NATIVE_STATUS_VALUES: Final[tuple[str, ...]] = (
    "idle",
    "preparing",
    "starting",
    "recording",
    "pausing",
    "paused",
    "resuming",
    "stopping",
    "finalization-failed",
    "offline",
    "ready",
    "settings-unavailable",
    "checking",
    "signed-out",
    "unavailable",
    "disabled",
    "needs-sign-in",
    "needs-attention",
    "not-implemented",
    "syncing",
    "queued",
    "completed",
)


class RecordingNativeStatus(str, Enum):
    """
    Portable native recording lifecycle; derive action booleans from verified state and
    treat unknown values as non-actionable.
    """

    IDLE = "idle"
    PREPARING = "preparing"
    STARTING = "starting"
    RECORDING = "recording"
    PAUSING = "pausing"
    PAUSED = "paused"
    RESUMING = "resuming"
    STOPPING = "stopping"
    FINALIZATION_FAILED = "finalization-failed"
    OFFLINE = "offline"
    READY = "ready"
    SETTINGS_UNAVAILABLE = "settings-unavailable"
    CHECKING = "checking"
    SIGNED_OUT = "signed-out"
    UNAVAILABLE = "unavailable"
    DISABLED = "disabled"
    NEEDS_SIGN_IN = "needs-sign-in"
    NEEDS_ATTENTION = "needs-attention"
    NOT_IMPLEMENTED = "not-implemented"
    SYNCING = "syncing"
    QUEUED = "queued"
    COMPLETED = "completed"
    UNKNOWN = "unknown"

    @classmethod
    def _missing_(cls, value: object) -> RecordingNativeStatus | None:
        return cls.UNKNOWN if isinstance(value, str) else None

    def allows_start(self, compatibility: RecordingSchemaCompatibility) -> bool:
        """Permission, startup and fence proofs are additionally mandatory."""
        return compatibility.supports_recording_authority and self is type(self).IDLE

    def allows_stop(self, compatibility: RecordingSchemaCompatibility) -> bool:
        """Retain the platform-specific authenticated Stop fence."""
        return compatibility.supports_recording_authority and self in (
            type(self).RECORDING,
            type(self).PAUSING,
            type(self).PAUSED,
            type(self).RESUMING,
            type(self).FINALIZATION_FAILED,
        )

    def allows_pause(self, compatibility: RecordingSchemaCompatibility) -> bool:
        recording = type(self).RECORDING
        return compatibility.supports_recording_authority and self is recording

    def allows_resume(self, compatibility: RecordingSchemaCompatibility) -> bool:
        """The native-observed maximum-audio-size proof remains required."""
        return compatibility.supports_recording_authority and self is type(self).PAUSED


RECORDING_UPLOAD_PHASE_VALUES: Final[tuple[str, ...]] = (
    "idle",
    "waiting-for-artifact",
    "queued",
    "uploading",
    "uploaded",
    "needs-sign-in",
    "local-only",
    "needs-manual-retry",
    "failed",
)


class RecordingUploadPhase(str, Enum):
    """
    Native-owned upload lifecycle; a phase alone never proves a receipt or authorizes
    retry.
    """

    IDLE = "idle"
    WAITING_FOR_ARTIFACT = "waiting-for-artifact"
    QUEUED = "queued"
    UPLOADING = "uploading"
    UPLOADED = "uploaded"
    NEEDS_SIGN_IN = "needs-sign-in"
    LOCAL_ONLY = "local-only"
    NEEDS_MANUAL_RETRY = "needs-manual-retry"
    FAILED = "failed"
    UNKNOWN = "unknown"

    @classmethod
    def _missing_(cls, value: object) -> RecordingUploadPhase | None:
        return cls.UNKNOWN if isinstance(value, str) else None


RECORDING_PERMISSION_VALUES: Final[tuple[str, ...]] = (
    "granted",
    "denied",
    "notDetermined",
    "unsupported",
    "unknown",
)


class RecordingPermissionPresentation(str, Enum):
    """
    Platform-specific permission presentation; a displayed value alone never grants
    native capture permission.
    """

    GRANTED = "granted"
    DENIED = "denied"
    NOT_DETERMINED = "notDetermined"
    UNSUPPORTED = "unsupported"
    UNKNOWN = "unknown"

    @classmethod
    def _missing_(cls, value: object) -> RecordingPermissionPresentation | None:
        return cls.UNKNOWN if isinstance(value, str) else None


RECORDING_RECOVERY_KIND_VALUES: Final[tuple[str, ...]] = (
    "checking",
    "not_installed",
    "launch_required",
    "launching",
    "quit_required",
    "update_deferred",
    "start_retry_required",
)


class RecordingRecoveryKind(str, Enum):
    """
    Bounded native recovery diagnosis; polling never implicitly installs, launches,
    restarts, or retries.
    """

    CHECKING = "checking"
    NOT_INSTALLED = "not_installed"
    LAUNCH_REQUIRED = "launch_required"
    LAUNCHING = "launching"
    QUIT_REQUIRED = "quit_required"
    UPDATE_DEFERRED = "update_deferred"
    START_RETRY_REQUIRED = "start_retry_required"
    UNKNOWN = "unknown"

    @classmethod
    def _missing_(cls, value: object) -> RecordingRecoveryKind | None:
        return cls.UNKNOWN if isinstance(value, str) else None


RECORDING_STARTUP_RECOVERY_VALUES: Final[tuple[str, ...]] = (
    "recovering",
    "ready",
    "blocked",
)


class RecordingStartupRecovery(str, Enum):
    """
    Native-owned startup readiness; blocked or unknown recovery cannot authorize
    recording.
    """

    RECOVERING = "recovering"
    READY = "ready"
    BLOCKED = "blocked"
    UNKNOWN = "unknown"

    @classmethod
    def _missing_(cls, value: object) -> RecordingStartupRecovery | None:
        return cls.UNKNOWN if isinstance(value, str) else None


RECORDING_HEADLESS_SYNC_STATUS_VALUES: Final[tuple[str, ...]] = (
    "idle",
    "disabled",
    "needs-sign-in",
    "needs-attention",
    "not-implemented",
    "syncing",
    "queued",
    "completed",
)


class RecordingHeadlessSyncStatus(str, Enum):
    """
    Platform-advertised background sync observation, never independent recording or
    process authority.
    """

    IDLE = "idle"
    DISABLED = "disabled"
    NEEDS_SIGN_IN = "needs-sign-in"
    NEEDS_ATTENTION = "needs-attention"
    NOT_IMPLEMENTED = "not-implemented"
    SYNCING = "syncing"
    QUEUED = "queued"
    COMPLETED = "completed"
    UNKNOWN = "unknown"

    @classmethod
    def _missing_(cls, value: object) -> RecordingHeadlessSyncStatus | None:
        return cls.UNKNOWN if isinstance(value, str) else None


class RecordingPermissions(TypedDict, total=False):
    """
    Native-reported platform permissions; unknown values remain observable and
    non-authorizing.
    """

    # Native microphone permission presentation; unknown values must fail closed.
    microphone: RecordingPermissionPresentation | str
    # Platform-specific system-audio permission; never assume support or authorization.
    systemAudio: RecordingPermissionPresentation | str


class _RequiredRecordingRecovery(TypedDict):
    # Bounded recovery diagnosis; an unknown recovery never launches, retries, or
    # restarts.
    kind: RecordingRecoveryKind | str


class RecordingRecovery(_RequiredRecordingRecovery, total=False):
    """
    Native recovery report; install, launch, restart, and retry require separate
    explicit authorization.
    """

    # Observed exact boolean or null; it does not prove a verified native installation.
    installed: bool | None
    # Presentation only; installation requires an explicit authorized user action.
    canInstall: bool | None
    # Presentation only; polling never automatically launches or restarts a companion.
    canLaunch: bool | None


class RecordingRustReceipt(TypedDict, total=False):
    """
    Bounded, path-free Rust capture evidence; receipt observations never prove upload,
    account, or process authority.
    """

    # Observed Rust receipt protocol identity, independent of recording endpoint and
    # control transport versions.
    protocolVersion: int
    # Observed nonnegative native capture start count.
    startCount: int
    # Observed nonnegative native effect acknowledgement count.
    effectAckCount: int
    # Observed nonnegative native host binding count.
    bindingCount: int
    # Observed nonnegative native capture stop count.
    stopCount: int
    # Observed nonnegative microphone packet count.
    microphonePacketCount: int
    # Observed nonnegative microphone packet sequence.
    microphoneLastSequence: int
    # Observed nonnegative system audio packet count.
    systemPacketCount: int
    # Observed nonnegative system audio packet sequence.
    systemLastSequence: int
    # Observed nonnegative pending PCM byte count; raw audio remains native-owned.
    pendingPCMBytes: int
    # Observed nonnegative captured PCM byte count; raw audio remains native-owned.
    totalPCMBytes: int
    # Observed nonnegative WAV byte count; paths and raw audio never cross this
    # boundary.
    wavBytes: int
    # Observed nonnegative native capture duration in milliseconds.
    durationMs: int
    # Bounded observed Rust capture completeness; unknown values never prove a durable
    # receipt.
    completeness: str
    # Bounded observed Rust terminal state; unknown values never authorize recovery.
    terminal: str
    # Exact native sink-commit observation; never substitute it for a hosted upload
    # receipt.
    sinkCommitted: bool
    # Optional public WAV digest; omission and explicit null remain legacy-compatible.
    wavSha256: str | None
    # Exact native observation that finalization preceded outbox admission.
    terminalBeforeOutboxAdmission: bool
    # Exact native observation that the recorded artifact reopened cleanly.
    cleanReopen: bool


class RecordingUploadReceipt(TypedDict, total=False):
    """
    Peer-verified, path-free native recording receipt; validate recording identity and
    durable hosted acknowledgement independently.
    """

    # Optional opaque public meeting association; never expose a private meeting
    # identifier.
    meetingId: str | None
    # Optional exact opaque recording identifier; never infer or guess a retry target.
    recordingId: str | None
    # Optional historical recording session observation; it never grants Stop or process
    # ownership.
    sessionId: str | None
    # Optional legacy recording title; never promote it to a public hosted meeting
    # projection.
    title: str | None
    # Optional historical meeting URL; never expose or use it as authenticated control
    # authority.
    meetingUrl: str | None
    # Optional observed Windows automation scope; authenticate the current owner and
    # account separately.
    automationScopeFingerprint: str | None
    # Optional observed capture-start timestamp; it does not prove ownership.
    startedAt: str | None
    # Observed native capture-stop timestamp; it does not prove hosted upload.
    stoppedAt: str
    # Exact local-save observation; local persistence is not a durable hosted upload
    # receipt.
    savedLocally: bool
    # Exact owner-, account-, and session-fenced hosted audio streaming completion;
    # absence or false never proves upload.
    streamingCompleted: bool
    # Exact bounded nonnegative captured audio byte count; never expose raw audio.
    audioBytes: int
    # Exact bounded nonnegative capture duration in milliseconds.
    audioDurationMs: int
    # Optional path-free Rust capture receipt; absence and explicit null preserve legacy
    # native snapshots.
    rust: RecordingRustReceipt | None


class RecordingDetails(TypedDict, total=False):
    """
    Authenticated native recording observations and local receipt; never infer upload,
    permissions, or process authority.
    """

    # Exact bounded nonnegative locally mixed audio byte count.
    mixedBytes: int
    # Optional observed recording start timestamp; never substitute it for session
    # ownership.
    startedAt: str | None
    # Exact native local-save observation; it never proves hosted upload.
    lastAudioSavedLocally: bool
    # Exact bounded nonnegative most-recent recording audio byte count.
    lastAudioBytes: int
    # Exact bounded nonnegative most-recent recording duration in milliseconds.
    lastAudioDurationMs: int
    # Optional peer-verified native local recording receipt; null and legacy omission
    # never authorize retry.
    lastRecording: RecordingUploadReceipt | None
    # Optional bounded display-only recording pause reason.
    pauseReason: str | None
    # Optional bounded display-only recording activity warning.
    activityWarning: str | None
    # Optional exact bounded recording signal observation in milliseconds.
    lastSignalMs: int | None
    # Optional exact bounded recording speech observation in milliseconds.
    lastSpeechMs: int | None
    # Exact native microphone health observation; it never grants permission.
    micHealthy: bool
    # Exact native system-audio health observation; it never grants permission.
    systemHealthy: bool


class RecordingUpload(TypedDict, total=False):
    """
    Native upload state; durable acknowledgement and user-confirmed exact-target retry
    require independent proof.
    """

    # Native upload observation; unknown or completed values never prove durable
    # success.
    phase: RecordingUploadPhase | str
    # Sanitized native upload preparation message; it never proves a durable receipt or
    # authorizes upload retry.
    message: str
    # Exact bounded nonnegative integer; booleans, fractional values, and out-of-range
    # counts are invalid.
    pendingCount: int
    # True only for an authenticated durable native upload receipt; never infer success
    # from a phase.
    hasDurableReceipt: bool
    # Presentation only; retry still requires an explicit user action and a verified
    # native target.
    canRetry: bool
    # Optional authenticated exact recording target; omission is legacy-compatible and
    # never permits broad or guessed retry.
    retryRecordingId: str | None
    # Optional exact current-account recording with a verified, owner-fenced durable
    # hosted completion; omission never proves upload success.
    completedRecordingId: str | None
    # Optional opaque current-account hosted meeting paired with an exact owner-fenced
    # completed recording; omission never authorizes guessed note access.
    completedMeetingId: str | None
    # Bounded account- and owner-fenced upload observations; absence never authorizes
    # upload, retry, recording, or recovery.
    queue: dict[str, object]


class RecordingStartup(TypedDict, total=False):
    """
    Native startup readiness and bounded attention; observation never starts or restarts
    a companion.
    """

    # Observable startup recovery; unknown values must not authorize recording.
    recovery: RecordingStartupRecovery | str
    # Bounded native diagnostic; never include private paths, tokens, or raw audio.
    attention: dict[str, object] | None


class RecordingHeadlessAuth(TypedDict, total=False):
    """
    Observed native headless authentication readiness; it never replaces account,
    live-owner, or epoch verification.
    """

    # Known native authentication readiness or bounded future observation; unknown
    # values grant no account or upload authority.
    status: RecordingNativeStatus | str
    # Exact presentation-only native upload readiness; durable receipt and account
    # verification remain mandatory.
    canUpload: bool


class RecordingHeadlessCalendar(TypedDict, total=False):
    """
    Path-free native Calendar synchronization observation; never expose meetings,
    account identity, or recording authority.
    """

    # Bounded observed Calendar sync phase; unknown values never authorize background
    # work.
    phase: str
    # Exact observed Calendar connection state; it does not prove account authority.
    connected: bool
    # Exact bounded nonnegative count of observed Calendar events.
    eventCount: int
    # Exact bounded nonnegative count of skipped Calendar events.
    skippedEventCount: int
    # Exact bounded nonnegative last Calendar sync attempt timestamp.
    lastAttemptAtMs: int
    # Exact bounded nonnegative last successful Calendar sync timestamp.
    lastSuccessfulSyncAtMs: int
    # Exact observation that same-scope last-good Calendar state was retained.
    retainedLastGood: bool
    # Exact observation of account-bound Calendar scope; authenticate the owner
    # independently.
    scopeBound: bool


class RecordingHeadlessMarkdown(TypedDict, total=False):
    """
    Path-free native Markdown synchronization observation; never expose transcript,
    account, meeting identity, or paths.
    """

    # Bounded observed Markdown sync phase; unknown values never authorize recording.
    phase: str
    # Exact bounded nonnegative count of observed Markdown receipts.
    receiptCount: int
    # Exact bounded nonnegative count of projected hosted meetings.
    projectedCount: int
    # Exact bounded nonnegative count of written Markdown summaries.
    writtenCount: int
    # Exact bounded nonnegative count of pending Markdown projections.
    waitingCount: int
    # Sanitized display-only Markdown synchronization message.
    message: str


class RecordingHeadlessNoteDetail(TypedDict, total=False):
    """
    Observed owner-scoped note-detail lease; authenticate account scope and the exact
    live lease before reading.
    """

    # Exact display-only note-detail availability; it never grants access without the
    # current owner-scoped lease.
    available: bool
    # Opaque owner-scoped note-detail revision; account identity never crosses this
    # projection.
    scopeRevision: str


class RecordingHeadlessSettings(TypedDict, total=False):
    """
    Revisioned owner-scoped headless settings projection; verify account, revision
    epoch, and reconciliation before use.
    """

    # Bounded native settings reconciliation observation; unknown values remain
    # non-actionable.
    status: str
    # Exact observed settings persistence; it never grants recording or upload
    # authority.
    saved: bool
    # Bounded native settings projection observation.
    projection: str
    # Exact bounded nonnegative settings revision; validate its epoch independently.
    revision: int
    # Exact bounded nonnegative native settings revision epoch; account scope remains
    # private.
    settingsRevisionEpoch: int


class RecordingHeadlessWidgetProjection(TypedDict, total=False):
    """
    Revisioned owner-scoped native widget projection readiness; it never grants
    recording or background authority.
    """

    # Bounded native widget projection observation; unknown values remain
    # non-actionable.
    status: str


class RecordingHeadlessSync(TypedDict, total=False):
    """
    Observed native background sync; unavailable platform capabilities must remain
    unavailable.
    """

    # Observed native sync lifecycle; unknown values grant no background authority.
    status: RecordingHeadlessSyncStatus | str
    # Sanitized native synchronization presentation message.
    message: str
    # Optional safe Calendar synchronization snapshot; absence and explicit null
    # preserve legacy native state.
    calendar: RecordingHeadlessCalendar | None
    # Optional path-free Markdown synchronization snapshot; absence and explicit null
    # preserve legacy native state.
    markdown: RecordingHeadlessMarkdown | None
    # Optional opaque native sync attempt identity; it never substitutes for owner
    # authority.
    attemptId: str | None
    # Optional observed native sync request timestamp.
    lastRequestedAt: str | None
    # Bounded observed native Calendar implementation availability.
    calendarImplementation: str
    # Bounded observed native Markdown implementation availability.
    markdownImplementation: str


class RecordingHeadless(TypedDict, total=False):
    """
    Platform-advertised native headless state; it never creates an unsupported recording
    companion.
    """

    # Known native headless availability or bounded future observation; unknown values
    # never authorize background work.
    status: RecordingNativeStatus | str
    auth: RecordingHeadlessAuth
    sync: RecordingHeadlessSync
    noteDetail: RecordingHeadlessNoteDetail
    settings: RecordingHeadlessSettings
    widgetProjection: RecordingHeadlessWidgetProjection
    # Optional owner-scoped projection revision; absence and null preserve old native
    # snapshots.
    _projectionRevision: str | None
    # Bounded distinct authenticated headless capabilities; unknown additive
    # observations never grant authority.
    capabilities: list[str]


class RecordingBridge(TypedDict, total=False):
    """
    Authenticated live-control transport observation; protocolVersion 1 is independent
    of endpoint schemaVersion 1 and the descriptor owner epoch.
    """

    # Observed exact transport integer; authenticate live-control protocolVersion 1
    # independently.
    protocolVersion: int


class _RequiredRecordingState(TypedDict):
    # Known lifecycle or bounded observable unknown; an unknown status never authorizes
    # Start, Stop, retry, or recovery.
    status: RecordingNativeStatus | str
    # Compatibility projection of verified native state; never treat this boolean as
    # independent recording authority.
    canStart: bool
    # Compatibility projection of verified native state; preserve the authenticated
    # active-session fence.
    canStop: bool


class RecordingState(_RequiredRecordingState, total=False):
    """
    Authoritative native recording state; verify schema compatibility, owner,
    capability, permission, and session before deriving action authority.
    """

    schemaVersion: int
    # Observed bounded capabilities; use only the negotiated generated live-control
    # profile and never promote additive names to authority.
    capabilities: list[str]
    # Optional native meeting association; it is not an authenticated control
    # identifier.
    meetingId: str | None
    # Authenticated active recording session; session-fenced Stop must match this exact
    # opaque identity.
    sessionId: str | None
    # Observed recording start time; timestamps alone never prove session ownership.
    startedAt: str | None
    # Bounded, sanitized presentation message without paths, credentials, or raw audio.
    message: str
    # Native Windows capture-failure observation; absence remains legacy-compatible and
    # never authorizes capture, upload, or process recovery.
    lastCaptureFailed: bool
    # Presentation only; verify authenticated state, platform capability, and session.
    canPause: bool
    # Presentation only; retain the authenticated session and native audio-size guards.
    canResume: bool
    # Observed Start admission fence; never replay an ambiguous admitted request.
    admissionFenced: bool
    # Observed native handoff fence; independently authenticate the successor and lease.
    handoffQuiescent: bool
    permissions: RecordingPermissions
    permissionPresentation: RecordingPermissions
    recording: RecordingDetails
    upload: RecordingUpload
    startup: RecordingStartup
    recovery: RecordingRecovery
    # Platform-advertised native headless state; it never creates an unsupported
    # recording companion.
    headless: RecordingHeadless
    # Authenticated live-control transport observation; protocolVersion 1 is independent
    # of endpoint schemaVersion 1 and the descriptor owner epoch.
    bridge: RecordingBridge


class _RequiredRecordingStatusResponse(TypedDict):
    # Exact JSON boolean result; success never replaces live-owner, epoch, recording, or
    # session verification.
    ok: bool
    state: RecordingState


class RecordingStatusResponse(_RequiredRecordingStatusResponse, total=False):
    """
    Native-produced recording status and MCP-owned offline projection. Endpoint
    schemaVersion 1 is independent of live-control protocolVersion 1 and owner
    generations. An omitted version denotes a legacy response; malformed or future
    versions and bounded unknown values remain non-actionable. Verify the current live
    owner, epoch, platform capabilities, permissions, and recording session before any
    recording, upload, or process mutation.
    """

    schemaVersion: int
    # Return only a bounded, sanitized diagnostic; never expose tokens, paths, audio, or
    # signing material.
    error: str | None
    # Bounded diagnostic category; an error code never authorizes automatic recovery.
    code: str | None
    # Observed platform runtime details, not authenticated recording or process
    # ownership.
    runtime: dict[str, object]
    # Observed native companion details; validate the exact live endpoint publication
    # and held owner lease separately.
    companion: dict[str, object]
    # Observed positive native PID; never signal it without authenticating the same live
    # owner and lease.
    companionPid: int


def _is_recording_bounded_integer(
    value: object,
    *,
    minimum: int | None = 0,
    maximum: int | None = RECORDING_STATUS_SCHEMA_VERSION_MAX,
) -> bool:
    """Validate exact integers against their schema-specific bounds."""
    return (
        type(value) is int
        and (minimum is None or minimum <= value)
        and (maximum is None or value <= maximum)
    )


def _is_recording_json_object(value: object) -> TypeGuard[dict[str, object]]:
    return isinstance(value, dict) and all(isinstance(key, str) for key in value)


def _is_safe_recording_capability(value: object) -> bool:
    return (
        isinstance(value, str)
        and 0 < len(value) <= 128
        and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*\.v[0-9]+", value) is not None
    )


def _is_recording_control_capabilities(value: object) -> bool:
    return (
        isinstance(value, list)
        and len(value) <= 256
        and all(_is_safe_recording_capability(item) for item in value)
        and len(set(value)) == len(value)
    )


def _is_recording_upload_queue(value: object) -> bool:
    """Reject malformed rows and fields outside the safe upload projection."""
    if not _is_recording_json_object(value) or set(value) != {"items"}:
        return False
    items = value["items"]
    if not isinstance(items, list) or len(items) > 24:
        return False
    for item in items:
        if not _is_recording_json_object(item):
            return False
        if set(item) != {"recordingId", "phase", "createdAt", "audioDurationMs", "audioBytes"}:
            return False
        identifier = item["recordingId"]
        if (
            not isinstance(identifier, str)
            or re.fullmatch("^recording-[a-f0-9]{64}$", identifier) is None
        ):
            return False
        phase = item["phase"]
        if not isinstance(phase, str) or phase not in {
            "queued",
            "uploading",
            "needs-sign-in",
            "needs-manual-retry",
        }:
            return False
        created_at = item["createdAt"]
        if not isinstance(created_at, str) or not (1 <= len(created_at) <= 64):
            return False
        for key in ("audioDurationMs", "audioBytes"):
            if not _is_recording_bounded_integer(
                item[key],
                minimum=0,
                maximum=9_007_199_254_740_991,
            ):
                return False
    return True


def is_safe_recording_wire_value(value: object) -> TypeGuard[str]:
    """Accept bounded future vocabulary without granting it authority."""
    return (
        isinstance(value, str)
        and 1 <= len(value) <= 64
        and re.fullmatch("^[A-Za-z0-9][A-Za-z0-9_-]*$", value) is not None
    )


def is_recording_permissions(value: object) -> TypeGuard[RecordingPermissions]:
    if not _is_recording_json_object(value):
        return False
    if "microphone" in value:
        field_value = value["microphone"]
        if not (is_safe_recording_wire_value(field_value)):
            return False
    if "systemAudio" in value:
        field_value = value["systemAudio"]
        if not (is_safe_recording_wire_value(field_value)):
            return False
    return True


def is_recording_recovery(value: object) -> TypeGuard[RecordingRecovery]:
    if not _is_recording_json_object(value):
        return False
    if "kind" not in value or not (is_safe_recording_wire_value(value["kind"])):
        return False
    if "installed" in value:
        field_value = value["installed"]
        if not (field_value is None or isinstance(field_value, bool)):
            return False
    if "canInstall" in value:
        field_value = value["canInstall"]
        if not (field_value is None or isinstance(field_value, bool)):
            return False
    if "canLaunch" in value:
        field_value = value["canLaunch"]
        if not (field_value is None or isinstance(field_value, bool)):
            return False
    return True


def is_recording_rust_receipt(value: object) -> TypeGuard[RecordingRustReceipt]:
    if not _is_recording_json_object(value):
        return False
    if "protocolVersion" in value:
        field_value = value["protocolVersion"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "startCount" in value:
        field_value = value["startCount"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "effectAckCount" in value:
        field_value = value["effectAckCount"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "bindingCount" in value:
        field_value = value["bindingCount"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "stopCount" in value and not (_is_recording_bounded_integer(value["stopCount"])):
        return False
    if "microphonePacketCount" in value:
        field_value = value["microphonePacketCount"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "microphoneLastSequence" in value:
        field_value = value["microphoneLastSequence"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "systemPacketCount" in value:
        field_value = value["systemPacketCount"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "systemLastSequence" in value:
        field_value = value["systemLastSequence"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "pendingPCMBytes" in value:
        field_value = value["pendingPCMBytes"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "totalPCMBytes" in value:
        field_value = value["totalPCMBytes"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "wavBytes" in value and not (_is_recording_bounded_integer(value["wavBytes"])):
        return False
    if "durationMs" in value:
        field_value = value["durationMs"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "completeness" in value:
        field_value = value["completeness"]
        if not (is_safe_recording_wire_value(field_value)):
            return False
    if "terminal" in value and not (is_safe_recording_wire_value(value["terminal"])):
        return False
    if "sinkCommitted" in value and not (isinstance(value["sinkCommitted"], bool)):
        return False
    if "wavSha256" in value:
        field_value = value["wavSha256"]
        if not (
            field_value is None
            or isinstance(field_value, str)
            and re.fullmatch("^[a-f0-9]{64}$", field_value) is not None
        ):
            return False
    if "terminalBeforeOutboxAdmission" in value:
        field_value = value["terminalBeforeOutboxAdmission"]
        if not (isinstance(field_value, bool)):
            return False
    if "cleanReopen" in value and not (isinstance(value["cleanReopen"], bool)):
        return False
    return True


def is_recording_upload_receipt(value: object) -> TypeGuard[RecordingUploadReceipt]:
    if not _is_recording_json_object(value):
        return False
    if "meetingId" in value:
        field_value = value["meetingId"]
        if not (field_value is None or isinstance(field_value, str)):
            return False
    if "recordingId" in value:
        field_value = value["recordingId"]
        if not (
            field_value is None
            or isinstance(field_value, str)
            and re.fullmatch("^recording-[a-f0-9]{64}$", field_value) is not None
        ):
            return False
    if "sessionId" in value:
        field_value = value["sessionId"]
        if not (field_value is None or isinstance(field_value, str)):
            return False
    if "title" in value:
        field_value = value["title"]
        if not (field_value is None or isinstance(field_value, str)):
            return False
    if "meetingUrl" in value:
        field_value = value["meetingUrl"]
        if not (field_value is None or isinstance(field_value, str)):
            return False
    if "automationScopeFingerprint" in value:
        field_value = value["automationScopeFingerprint"]
        if not (field_value is None or isinstance(field_value, str)):
            return False
    if "startedAt" in value:
        field_value = value["startedAt"]
        if not (field_value is None or isinstance(field_value, str)):
            return False
    if "stoppedAt" in value and not (isinstance(value["stoppedAt"], str)):
        return False
    if "savedLocally" in value and not (isinstance(value["savedLocally"], bool)):
        return False
    if "streamingCompleted" in value:
        field_value = value["streamingCompleted"]
        if not (isinstance(field_value, bool)):
            return False
    if "audioBytes" in value:
        field_value = value["audioBytes"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "audioDurationMs" in value:
        field_value = value["audioDurationMs"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "rust" in value:
        field_value = value["rust"]
        if not (field_value is None or is_recording_rust_receipt(field_value)):
            return False
    return True


def is_recording_details(value: object) -> TypeGuard[RecordingDetails]:
    if not _is_recording_json_object(value):
        return False
    if "mixedBytes" in value:
        field_value = value["mixedBytes"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "startedAt" in value:
        field_value = value["startedAt"]
        if not (field_value is None or isinstance(field_value, str)):
            return False
    if "lastAudioSavedLocally" in value:
        field_value = value["lastAudioSavedLocally"]
        if not (isinstance(field_value, bool)):
            return False
    if "lastAudioBytes" in value:
        field_value = value["lastAudioBytes"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "lastAudioDurationMs" in value:
        field_value = value["lastAudioDurationMs"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "lastRecording" in value:
        field_value = value["lastRecording"]
        if not (field_value is None or is_recording_upload_receipt(field_value)):
            return False
    if "pauseReason" in value:
        field_value = value["pauseReason"]
        if not (field_value is None or isinstance(field_value, str)):
            return False
    if "activityWarning" in value:
        field_value = value["activityWarning"]
        if not (field_value is None or isinstance(field_value, str)):
            return False
    if "lastSignalMs" in value:
        field_value = value["lastSignalMs"]
        if not (field_value is None or _is_recording_bounded_integer(field_value)):
            return False
    if "lastSpeechMs" in value:
        field_value = value["lastSpeechMs"]
        if not (field_value is None or _is_recording_bounded_integer(field_value)):
            return False
    if "micHealthy" in value and not (isinstance(value["micHealthy"], bool)):
        return False
    if "systemHealthy" in value and not (isinstance(value["systemHealthy"], bool)):
        return False
    return True


def is_recording_upload(value: object) -> TypeGuard[RecordingUpload]:
    if not _is_recording_json_object(value):
        return False
    if "phase" in value and not (is_safe_recording_wire_value(value["phase"])):
        return False
    if "message" in value and not (isinstance(value["message"], str)):
        return False
    if "pendingCount" in value:
        field_value = value["pendingCount"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "hasDurableReceipt" in value:
        field_value = value["hasDurableReceipt"]
        if not (isinstance(field_value, bool)):
            return False
    if "canRetry" in value and not (isinstance(value["canRetry"], bool)):
        return False
    if "retryRecordingId" in value:
        field_value = value["retryRecordingId"]
        if not (
            field_value is None
            or isinstance(field_value, str)
            and re.fullmatch("^recording-[a-f0-9]{64}$", field_value) is not None
        ):
            return False
    if "completedRecordingId" in value:
        field_value = value["completedRecordingId"]
        if not (
            field_value is None
            or isinstance(field_value, str)
            and re.fullmatch("^recording-[a-f0-9]{64}$", field_value) is not None
        ):
            return False
    if "completedMeetingId" in value:
        field_value = value["completedMeetingId"]
        if not (
            field_value is None
            or isinstance(field_value, str)
            and re.fullmatch("^hosted-[a-f0-9]{64}$", field_value) is not None
        ):
            return False
    if "queue" in value and not (_is_recording_upload_queue(value["queue"])):
        return False
    return True


def is_recording_startup(value: object) -> TypeGuard[RecordingStartup]:
    if not _is_recording_json_object(value):
        return False
    if "recovery" in value and not (is_safe_recording_wire_value(value["recovery"])):
        return False
    if "attention" in value:
        field_value = value["attention"]
        if not (field_value is None or _is_recording_json_object(field_value)):
            return False
    return True


def is_recording_headless_auth(value: object) -> TypeGuard[RecordingHeadlessAuth]:
    if not _is_recording_json_object(value):
        return False
    if "status" in value and not (is_safe_recording_wire_value(value["status"])):
        return False
    if "canUpload" in value and not (isinstance(value["canUpload"], bool)):
        return False
    return True


def is_recording_headless_calendar(value: object) -> TypeGuard[RecordingHeadlessCalendar]:
    if not _is_recording_json_object(value):
        return False
    if "phase" in value and not (is_safe_recording_wire_value(value["phase"])):
        return False
    if "connected" in value and not (isinstance(value["connected"], bool)):
        return False
    if "eventCount" in value:
        field_value = value["eventCount"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "skippedEventCount" in value:
        field_value = value["skippedEventCount"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "lastAttemptAtMs" in value:
        field_value = value["lastAttemptAtMs"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "lastSuccessfulSyncAtMs" in value:
        field_value = value["lastSuccessfulSyncAtMs"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "retainedLastGood" in value:
        field_value = value["retainedLastGood"]
        if not (isinstance(field_value, bool)):
            return False
    if "scopeBound" in value and not (isinstance(value["scopeBound"], bool)):
        return False
    return True


def is_recording_headless_markdown(value: object) -> TypeGuard[RecordingHeadlessMarkdown]:
    if not _is_recording_json_object(value):
        return False
    if "phase" in value and not (is_safe_recording_wire_value(value["phase"])):
        return False
    if "receiptCount" in value:
        field_value = value["receiptCount"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "projectedCount" in value:
        field_value = value["projectedCount"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "writtenCount" in value:
        field_value = value["writtenCount"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "waitingCount" in value:
        field_value = value["waitingCount"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    if "message" in value and not (isinstance(value["message"], str)):
        return False
    return True


def is_recording_headless_note_detail(value: object) -> TypeGuard[RecordingHeadlessNoteDetail]:
    if not _is_recording_json_object(value):
        return False
    if "available" in value and not (isinstance(value["available"], bool)):
        return False
    if "scopeRevision" in value and not (isinstance(value["scopeRevision"], str)):
        return False
    return True


def is_recording_headless_settings(value: object) -> TypeGuard[RecordingHeadlessSettings]:
    if not _is_recording_json_object(value):
        return False
    if "status" in value and not (is_safe_recording_wire_value(value["status"])):
        return False
    if "saved" in value and not (isinstance(value["saved"], bool)):
        return False
    if "projection" in value:
        field_value = value["projection"]
        if not (is_safe_recording_wire_value(field_value)):
            return False
    if "revision" in value and not (_is_recording_bounded_integer(value["revision"])):
        return False
    if "settingsRevisionEpoch" in value:
        field_value = value["settingsRevisionEpoch"]
        if not (_is_recording_bounded_integer(field_value)):
            return False
    return True


def is_recording_headless_widget_projection(
    value: object,
) -> TypeGuard[RecordingHeadlessWidgetProjection]:
    if not _is_recording_json_object(value):
        return False
    if "status" in value and not (is_safe_recording_wire_value(value["status"])):
        return False
    return True


def is_recording_headless_sync(value: object) -> TypeGuard[RecordingHeadlessSync]:
    if not _is_recording_json_object(value):
        return False
    if "status" in value and not (is_safe_recording_wire_value(value["status"])):
        return False
    if "message" in value and not (isinstance(value["message"], str)):
        return False
    if "calendar" in value:
        field_value = value["calendar"]
        if not (field_value is None or is_recording_headless_calendar(field_value)):
            return False
    if "markdown" in value:
        field_value = value["markdown"]
        if not (field_value is None or is_recording_headless_markdown(field_value)):
            return False
    if "attemptId" in value:
        field_value = value["attemptId"]
        if not (field_value is None or isinstance(field_value, str)):
            return False
    if "lastRequestedAt" in value:
        field_value = value["lastRequestedAt"]
        if not (field_value is None or isinstance(field_value, str)):
            return False
    if "calendarImplementation" in value:
        field_value = value["calendarImplementation"]
        if not (is_safe_recording_wire_value(field_value)):
            return False
    if "markdownImplementation" in value:
        field_value = value["markdownImplementation"]
        if not (is_safe_recording_wire_value(field_value)):
            return False
    return True


def is_recording_headless(value: object) -> TypeGuard[RecordingHeadless]:
    if not _is_recording_json_object(value):
        return False
    if "status" in value and not (is_safe_recording_wire_value(value["status"])):
        return False
    if "auth" in value and not (is_recording_headless_auth(value["auth"])):
        return False
    if "sync" in value and not (is_recording_headless_sync(value["sync"])):
        return False
    if "noteDetail" in value:
        field_value = value["noteDetail"]
        if not (is_recording_headless_note_detail(field_value)):
            return False
    if "settings" in value and not (is_recording_headless_settings(value["settings"])):
        return False
    if "widgetProjection" in value:
        field_value = value["widgetProjection"]
        if not (is_recording_headless_widget_projection(field_value)):
            return False
    if "_projectionRevision" in value:
        field_value = value["_projectionRevision"]
        if not (field_value is None or isinstance(field_value, str)):
            return False
    if "capabilities" in value:
        field_value = value["capabilities"]
        if not (_is_recording_control_capabilities(field_value)):
            return False
    return True


def is_recording_bridge(value: object) -> TypeGuard[RecordingBridge]:
    if not _is_recording_json_object(value):
        return False
    if "protocolVersion" in value:
        field_value = value["protocolVersion"]
        if not (_is_recording_bounded_integer(field_value, minimum=1)):
            return False
    return True


def is_recording_state(value: object) -> TypeGuard[RecordingState]:
    if not _is_recording_json_object(value):
        return False
    if "schemaVersion" in value:
        field_value = value["schemaVersion"]
        if not (_is_recording_bounded_integer(field_value, minimum=1)):
            return False
    if "status" not in value or not (is_safe_recording_wire_value(value["status"])):
        return False
    if "capabilities" in value:
        field_value = value["capabilities"]
        if not (_is_recording_control_capabilities(field_value)):
            return False
    if "meetingId" in value:
        field_value = value["meetingId"]
        if not (field_value is None or isinstance(field_value, str)):
            return False
    if "sessionId" in value:
        field_value = value["sessionId"]
        if not (field_value is None or isinstance(field_value, str)):
            return False
    if "startedAt" in value:
        field_value = value["startedAt"]
        if not (field_value is None or isinstance(field_value, str)):
            return False
    if "message" in value and not (isinstance(value["message"], str)):
        return False
    if "lastCaptureFailed" in value:
        field_value = value["lastCaptureFailed"]
        if not (isinstance(field_value, bool)):
            return False
    if "canStart" not in value or not (isinstance(value["canStart"], bool)):
        return False
    if "canStop" not in value or not (isinstance(value["canStop"], bool)):
        return False
    if "canPause" in value and not (isinstance(value["canPause"], bool)):
        return False
    if "canResume" in value and not (isinstance(value["canResume"], bool)):
        return False
    if "admissionFenced" in value and not (isinstance(value["admissionFenced"], bool)):
        return False
    if "handoffQuiescent" in value:
        field_value = value["handoffQuiescent"]
        if not (isinstance(field_value, bool)):
            return False
    if "permissions" in value and not (is_recording_permissions(value["permissions"])):
        return False
    if "permissionPresentation" in value:
        field_value = value["permissionPresentation"]
        if not (is_recording_permissions(field_value)):
            return False
    if "recording" in value and not (is_recording_details(value["recording"])):
        return False
    if "upload" in value and not (is_recording_upload(value["upload"])):
        return False
    if "startup" in value and not (is_recording_startup(value["startup"])):
        return False
    if "recovery" in value and not (is_recording_recovery(value["recovery"])):
        return False
    if "headless" in value and not (is_recording_headless(value["headless"])):
        return False
    if "bridge" in value and not (is_recording_bridge(value["bridge"])):
        return False
    return True


def is_recording_status_response(value: object) -> TypeGuard[RecordingStatusResponse]:
    if not _is_recording_json_object(value):
        return False
    if "schemaVersion" in value:
        field_value = value["schemaVersion"]
        if not (_is_recording_bounded_integer(field_value, minimum=1)):
            return False
    if "ok" not in value or not (isinstance(value["ok"], bool)):
        return False
    if "state" not in value or not (is_recording_state(value["state"])):
        return False
    if "error" in value:
        field_value = value["error"]
        if not (field_value is None or isinstance(field_value, str)):
            return False
    if "code" in value:
        field_value = value["code"]
        if not (field_value is None or isinstance(field_value, str)):
            return False
    if "runtime" in value and not (_is_recording_json_object(value["runtime"])):
        return False
    if "companion" in value and not (_is_recording_json_object(value["companion"])):
        return False
    if "companionPid" in value:
        field_value = value["companionPid"]
        if not (_is_recording_bounded_integer(field_value, minimum=1)):
            return False
    return True


def parse_recording_status(value: object) -> RecordingNativeStatus:
    """Map missing, malformed and future status to non-actionable UNKNOWN."""
    if not isinstance(value, str):
        return RecordingNativeStatus.UNKNOWN
    return RecordingNativeStatus(value)


def parse_recording_state_contract(
    value: object,
) -> tuple[RecordingNativeStatus, RecordingSchemaCompatibility]:
    """Classify one wire state without granting malformed capture authority."""
    if not isinstance(value, dict):
        return RecordingNativeStatus.UNKNOWN, RecordingSchemaCompatibility.UNSUPPORTED
    return (
        parse_recording_status(value.get("status")),
        parse_recording_schema_compatibility(
            value.get("schemaVersion"),
            field_present="schemaVersion" in value,
        ),
    )
