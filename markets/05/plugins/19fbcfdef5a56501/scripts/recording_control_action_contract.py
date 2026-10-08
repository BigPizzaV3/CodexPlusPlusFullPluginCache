# GENERATED FILE. DO NOT EDIT.
# Source: chatgpt-meetings-core/contracts/recording-control-actions.v1.schema.json
# SHA-256: 64eefa0fcedaa37ea4a4b3c5565dff4b5f88708457886bd32a3e83cc433e9a20
# Regenerate: python3 chatgpt-meetings-core/scripts/generate_recording_status_contract.py
# Transport-neutral live action, argument, platform, and local-calendar authority shared
# by authenticated native control runtimes.

from __future__ import annotations

import re
from enum import Enum
from typing import TYPE_CHECKING, Final, Literal, TypedDict, Union, overload

if TYPE_CHECKING:
    from typing import TypeGuard
else:
    try:
        from typing import TypeGuard
    except ImportError:

        class TypeGuard:
            """Keep generated action guards importable on Python 3.9."""

            @classmethod
            def __class_getitem__(cls, _value: object) -> type[bool]:
                return bool


RECORDING_CONTROL_ACTIONS_SCHEMA_NAME: Final[str] = "chatgpt-meetings.recording-control-actions"
RECORDING_CONTROL_ACTIONS_SCHEMA_VERSION: Final[int] = 1
RECORDING_CONTROL_ACTIONS_SCHEMA_SHA256: Final[str] = (
    "64eefa0fcedaa37ea4a4b3c5565dff4b5f88708457886bd32a3e83cc433e9a20"
)
RECORDING_CONTROL_SAFE_INTEGER_MAX: Final[int] = 9_007_199_254_740_991
LOCAL_CALENDAR_QUERY_MAXIMUM_WINDOW_MILLIS: Final[int] = 3_888_000_000
LOCAL_CALENDAR_QUERY_MAXIMUM_EVENTS: Final[int] = 64


CONTROL_ACTION_VALUES: Final[tuple[str, ...]] = (
    "status",
    "getSettings",
    "getLocalCalendar",
    "listAudioDevices",
    "updateSettings",
    "requestMicrophone",
    "requestSystemAudio",
    "start",
    "stop",
    "pause",
    "resume",
    "dismissActivityWarning",
    "retryUpload",
    "retryUploadTarget",
    "syncNow",
    "syncAutomation",
    "refreshHomeCache",
    "getNoteDetail",
    "openLogViewer",
    "quitForUpdate",
)


class ControlAction(str, Enum):
    """
    Known explicitly authorized live native action; validate its exact arguments and
    authenticated platform profile.
    """

    STATUS = "status"
    GET_SETTINGS = "getSettings"
    GET_LOCAL_CALENDAR = "getLocalCalendar"
    LIST_AUDIO_DEVICES = "listAudioDevices"
    UPDATE_SETTINGS = "updateSettings"
    REQUEST_MICROPHONE = "requestMicrophone"
    REQUEST_SYSTEM_AUDIO = "requestSystemAudio"
    START = "start"
    STOP = "stop"
    PAUSE = "pause"
    RESUME = "resume"
    DISMISS_ACTIVITY_WARNING = "dismissActivityWarning"
    RETRY_UPLOAD = "retryUpload"
    RETRY_UPLOAD_TARGET = "retryUploadTarget"
    SYNC_NOW = "syncNow"
    SYNC_AUTOMATION = "syncAutomation"
    REFRESH_HOME_CACHE = "refreshHomeCache"
    GET_NOTE_DETAIL = "getNoteDetail"
    OPEN_LOG_VIEWER = "openLogViewer"
    QUIT_FOR_UPDATE = "quitForUpdate"
    UNKNOWN = "unknown"

    @classmethod
    def _missing_(cls, value: object) -> ControlAction | None:
        return cls.UNKNOWN if isinstance(value, str) else None

    def supported_on_platform(self, platform: ControlPlatform) -> bool:
        """Unknown and cross-platform values never authorize control."""
        if self is type(self).UNKNOWN or platform is ControlPlatform.UNKNOWN:
            return False
        return self.value in CONTROL_ACTIONS_BY_PLATFORM.get(platform.value, ())


CONTROL_PLATFORM_VALUES: Final[tuple[str, ...]] = (
    "darwin-universal",
    "darwin-arm64",
    "darwin-x64",
    "windows-x64",
    "windows-arm64",
)


class ControlPlatform(str, Enum):
    """
    Authenticated macOS or Windows live companion identity; unknown platforms and Linux
    grant no native authority.
    """

    DARWIN_UNIVERSAL = "darwin-universal"
    DARWIN_ARM64 = "darwin-arm64"
    DARWIN_X64 = "darwin-x64"
    WINDOWS_X64 = "windows-x64"
    WINDOWS_ARM64 = "windows-arm64"
    UNKNOWN = "unknown"

    @classmethod
    def _missing_(cls, value: object) -> ControlPlatform | None:
        return cls.UNKNOWN if isinstance(value, str) else None


ControlActionWire = Literal[
    "status",
    "getSettings",
    "getLocalCalendar",
    "listAudioDevices",
    "updateSettings",
    "requestMicrophone",
    "requestSystemAudio",
    "start",
    "stop",
    "pause",
    "resume",
    "dismissActivityWarning",
    "retryUpload",
    "retryUploadTarget",
    "syncNow",
    "syncAutomation",
    "refreshHomeCache",
    "getNoteDetail",
    "openLogViewer",
    "quitForUpdate",
]


ControlPlatformWire = Literal[
    "darwin-universal",
    "darwin-arm64",
    "darwin-x64",
    "windows-x64",
    "windows-arm64",
]


RECORDING_CONTROL_DARWIN_ACTIONS: Final[tuple[str, ...]] = (
    "status",
    "getSettings",
    "getLocalCalendar",
    "updateSettings",
    "requestMicrophone",
    "requestSystemAudio",
    "start",
    "stop",
    "pause",
    "resume",
    "dismissActivityWarning",
    "retryUpload",
    "retryUploadTarget",
    "syncNow",
    "refreshHomeCache",
    "getNoteDetail",
    "openLogViewer",
    "quitForUpdate",
)


RECORDING_CONTROL_WINDOWS_ACTIONS: Final[tuple[str, ...]] = (
    "status",
    "getSettings",
    "getLocalCalendar",
    "listAudioDevices",
    "updateSettings",
    "requestMicrophone",
    "requestSystemAudio",
    "start",
    "stop",
    "pause",
    "resume",
    "dismissActivityWarning",
    "retryUpload",
    "syncNow",
    "syncAutomation",
    "getNoteDetail",
    "openLogViewer",
    "quitForUpdate",
)


CONTROL_ACTIONS_BY_PLATFORM: Final[dict[str, tuple[str, ...]]] = {
    "darwin-universal": RECORDING_CONTROL_DARWIN_ACTIONS,
    "darwin-arm64": RECORDING_CONTROL_DARWIN_ACTIONS,
    "darwin-x64": RECORDING_CONTROL_DARWIN_ACTIONS,
    "windows-x64": RECORDING_CONTROL_WINDOWS_ACTIONS,
    "windows-arm64": RECORDING_CONTROL_WINDOWS_ACTIONS,
}


class _RequiredControlAutomationFlags(TypedDict):
    # Whether the account-scoped policy permits native recording reminders.
    autoRecordPopupsAllowed: bool


class ControlAutomationFlags(_RequiredControlAutomationFlags, total=False):
    """
    Exact authenticated reminder permissions. No flag grants recording authority;
    capture starts only after an explicit user action.
    """

    # Deprecated compatibility-only flag for retired native meeting detection; current
    # companions ignore it.
    meetingDetectionAllowed: bool


class ControlAutomationPolicyCTA(TypedDict):
    """
    Bounded display-only HTTPS policy action. The authenticated native platform still
    verifies URL syntax and rejects embedded credentials.
    """

    # Sanitized display-only action label; producers additionally enforce the 64-byte
    # UTF-8 limit.
    label: str
    # Credential-free HTTPS action URL; producers independently verify its host and the
    # 2048-byte UTF-8 limit.
    url: str


class ControlAutomationPolicy(TypedDict):
    """
    Exact account-scoped native automation policy. Transitional statuses and recording
    permissions retain their existing authenticated native validation.
    """

    # Exact existing native policy lifecycle; an unknown or transitional status never
    # authorizes recording.
    status: str
    # Display-only policy title; an empty title is preserved for existing non-ready
    # policy states.
    title: str
    # Display-only policy message; an empty message is preserved for existing non-ready
    # policy states.
    message: str
    # Exact existing policy presentation severity; presentation never grants recording
    # authority.
    severity: str
    # Optional display-only policy action; null preserves the native empty, loading,
    # error, and no-action cases.
    cta: ControlAutomationPolicyCTA | None
    # Exact authenticated reminder permissions. No flag grants recording authority;
    # capture starts only after an explicit user action.
    automation: ControlAutomationFlags


class ControlAutomationEvent(TypedDict):
    """
    Exact account-scoped, sanitized upcoming native meeting. Native validation
    additionally verifies temporal ordering, supported meeting URL, and authenticated
    scope.
    """

    # Opaque upcoming meeting identity; raw provider identifiers never cross the
    # authenticated transport.
    meetingId: str
    # Sanitized meeting title; native validation additionally enforces trimmed, nonempty
    # text and its 512-byte UTF-8 limit.
    title: str
    # Exact positive JSON-safe meeting start; zero, negatives, booleans, floats, and
    # overflow are rejected on every platform.
    startAtMillis: int
    # Exact positive JSON-safe meeting end; native validation additionally requires the
    # end to follow the start.
    endAtMillis: int
    # Exact native-projected meeting response; an unknown response is an observation,
    # never recording authority.
    responseStatus: str
    # Exact account-scoped native calendar decision.
    meetingDecision: str
    # Sanitized HTTPS meeting URL; native validation independently requires a supported
    # provider and rejects embedded credentials.
    meetingUrl: str


class ControlAutomationCalendar(TypedDict):
    """
    Exact bounded authoritative account-scoped calendar. Native validation independently
    verifies all timestamp ordering, freshness, authority, supported providers, and
    recording permissions.
    """

    # Exact nonnegative JSON-safe account authority issuance time in microseconds.
    authorityIssuedAtMicros: int
    # Exact nonnegative JSON-safe native calendar validation time in milliseconds.
    validatedAtMillis: int
    # Exact nonnegative JSON-safe account-scoped calendar generation time in
    # milliseconds.
    generatedAtMillis: int
    # Exact nonnegative JSON-safe native calendar freshness deadline in milliseconds.
    freshUntilMillis: int
    # Whether the calendar has authenticated account authority; false never permits an
    # event.
    authoritative: bool
    # Whether independently verified hosted policy permits this account's native
    # automation.
    hostedAutomationAllowed: bool
    # Whether account-scoped native recording setup is complete; it never substitutes
    # for recording consent.
    localSetupComplete: bool
    # At most 64 sanitized account-scoped upcoming native calendar events.
    events: list[ControlAutomationEvent]


class ControlLocalCalendarEvent(TypedDict):
    """Private owner-fenced event; never persist, log, expose to models, or publish."""

    id: str  # Opaque owner-bound event ID; never expose raw provider identifiers.
    title: str  # Bounded display title; never include notes, attendees, or metadata.
    startAtMillis: int  # Positive JavaScript-safe event start in Unix milliseconds.
    endAtMillis: int  # Positive JavaScript-safe event end strictly after its start.
    # Optional bounded supported HTTPS conference URL; unsupported is null.
    meetingUrl: str | None
    # Opaque calendar ID explicitly selected by the authenticated owner.
    calendarID: str


class ControlLocalCalendarQueryResult(TypedDict):
    """Private owner-fenced result; never persist, log, expose to models, or publish."""

    # 64 owner-fenced, deduplicated selected-source events maximum.
    events: list[ControlLocalCalendarEvent]


class EmptyActionArguments(TypedDict):
    """
    Actions with no arguments require exactly the empty object; additive keys are not
    permitted.
    """

    pass


class SessionFencedActionArguments(TypedDict, total=False):
    """
    Explicit Stop, pause, resume, or dismissal; match the exact authenticated active
    session when supplied.
    """

    # Optional exact authenticated active session; legacy omission is permitted but
    # never guess or stop a replacement recording.
    expectedSessionId: str


class StartActionArguments(TypedDict, total=False):
    """
    Explicit native Start arguments; validate optional bounded meeting metadata without
    replaying ambiguous admission.
    """

    # Optional bounded native meeting identity; it does not replace owner, epoch, or
    # session validation.
    meetingId: str
    # Optional bounded user-facing title; never treat meeting metadata as authorization.
    title: str
    # Optional bounded meeting URL; validate it without replacing authenticated Start
    # ownership.
    meetingUrl: str


class SyncNowActionArguments(TypedDict):
    """
    Native sync request with an exact real JSON boolean; implicit recovery and restart
    remain forbidden.
    """

    # Exact JSON boolean; integers never authorize automatic sync or recovery.
    automatic: bool


class UpdateSettingsActionArguments(TypedDict, total=False):
    """
    Strict platform-supported settings; reject unknown keys, boolean integers, invalid
    bounds, and unsupported devices.
    """

    # Exact user-authorized JSON boolean; integers and implicit background launch are
    # invalid.
    backgroundEnabled: bool
    # Exact user-authorized JSON boolean for supported native Calendar sync.
    calendarSyncEnabled: bool
    # Exact user-authorized JSON boolean; reminders never imply recording consent.
    calendarReminderEnabled: bool
    # Deprecated compatibility-only boolean; current native companions ignore this
    # retired setting.
    meetingDetectionEnabled: bool
    # Deprecated compatibility-only account fence for the retired meeting-detection
    # setting.
    expectedMeetingDetectionOwnerScopeFingerprint: str
    # Exact device-local JSON boolean controlling native recording start, stop, and
    # attention sounds.
    soundEffectsEnabled: bool
    # Explicit local consent; only user-initiated enablement may prompt the OS.
    localCalendarSyncEnabled: bool
    # 64 distinct selected owner-bound calendar IDs; empty means no sync.
    selectedLocalCalendarIDs: list[str]
    # Explicit owner-scoped task; null restores the current-task default.
    localCalendarThreadID: str | None
    # Bind the exact account owner before any mutation, persistence, or OS consent.
    expectedLocalCalendarOwnerScopeFingerprint: str
    # Exact bounded integer cadence; reject booleans, floats, and values outside
    # 5..1440.
    syncIntervalMinutes: int
    # Optional bounded verified platform microphone identity; never infer permission.
    microphoneDeviceId: str | None
    # Optional bounded verified platform audio device; unsupported devices remain
    # invalid.
    systemAudioDeviceId: str | None


class GetLocalCalendarActionArguments(TypedDict):
    """Private owner-fenced local read; never prompts, records, or goes public."""

    startAtMillis: int  # Inclusive positive JavaScript-safe Unix millisecond start.
    endAtMillis: int  # Exclusive positive JavaScript-safe Unix millisecond end.
    limit: int  # Owner-fenced selected-source event cap after native deduplication.


class NoteDetailActionArguments(TypedDict):
    """
    Exact bounded native-hosted note identity; never substitute an unvalidated raw
    identifier.
    """

    # Exact opaque native-hosted note identifier; reject paths, raw IDs, and newline
    # injection.
    noteId: str


class TargetedRetryActionArguments(TypedDict):
    """
    User-confirmed upload retry for exactly one authenticated native recording; never
    guess, broaden, or automatically replay the target.
    """

    # Exactly the authenticated native-owned recording selected by the user's explicit
    # retry.
    recordingId: str


class AutomationSyncActionArguments(TypedDict):
    """
    Windows-specific authenticated automation projection; verify exact account scope and
    platform capability first.
    """

    # Exact lowercase SHA-256 account-scope fingerprint; it identifies authority but
    # never contains a credential or grants an action by itself.
    scopeFingerprint: str
    # Exact account-scoped native automation policy. Transitional statuses and recording
    # permissions retain their existing authenticated native validation.
    policy: ControlAutomationPolicy
    # Exact bounded authoritative account-scoped calendar. Native validation
    # independently verifies all timestamp ordering, freshness, authority, supported
    # providers, and recording permissions.
    calendar: ControlAutomationCalendar


ControlActionArguments = Union[  # noqa: UP007 - sealed runtime uses Python 3.9
    EmptyActionArguments,
    SessionFencedActionArguments,
    StartActionArguments,
    SyncNowActionArguments,
    UpdateSettingsActionArguments,
    GetLocalCalendarActionArguments,
    NoteDetailActionArguments,
    TargetedRetryActionArguments,
    AutomationSyncActionArguments,
]


def _is_action_bounded_integer(
    value: object, minimum: int = 0, maximum: int = RECORDING_CONTROL_SAFE_INTEGER_MAX
) -> bool:
    return type(value) is int and minimum <= value <= maximum


def parse_control_action(value: object) -> ControlAction:
    return ControlAction(value) if isinstance(value, str) else ControlAction.UNKNOWN


def is_control_action_wire(value: object) -> TypeGuard[ControlActionWire]:
    """Narrow a known wire discriminator without changing or validating a request."""
    return isinstance(value, str) and value in CONTROL_ACTION_VALUES


def parse_control_platform(value: object) -> ControlPlatform:
    return ControlPlatform(value) if isinstance(value, str) else ControlPlatform.UNKNOWN


def control_action_supported_on_platform(
    action: ControlAction,
    platform: ControlPlatform,
) -> bool:
    return action.supported_on_platform(platform)


def _exact_control_keys(value: object, keys: frozenset[str]) -> TypeGuard[dict[str, object]]:
    return isinstance(value, dict) and set(value) == keys


def _control_identifier(value: object) -> bool:
    return (
        isinstance(value, str)
        and 8 <= len(value) <= 128
        and re.fullmatch(r"[A-Za-z0-9_-]+", value) is not None
    )


def is_control_identifier(value: object) -> TypeGuard[str]:
    """Validate an authenticated identifier with the live-action grammar."""
    return _control_identifier(value)


def is_safe_control_wire_capability(value: object) -> TypeGuard[str]:
    """Validate a bounded additive wire value without granting it authority."""
    return (
        isinstance(value, str)
        and 0 < len(value) <= 128
        and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*\.v[0-9]+", value) is not None
    )


def _control_fingerprint(value: object) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[a-f0-9]{64}", value) is not None


def _control_safe_integer(value: object) -> bool:
    return _is_action_bounded_integer(value, maximum=RECORDING_CONTROL_SAFE_INTEGER_MAX)


def is_control_automation_flags(value: object) -> TypeGuard[ControlAutomationFlags]:
    keys = frozenset({"autoRecordPopupsAllowed"})
    if not (
        _exact_control_keys(value, keys)
        or _exact_control_keys(value, keys | {"meetingDetectionAllowed"})
    ):
        return False
    return all(isinstance(flag, bool) for flag in value.values())


def is_control_automation_policy_cta(
    value: object,
) -> TypeGuard[ControlAutomationPolicyCTA]:
    if not _exact_control_keys(value, frozenset({"label", "url"})):
        return False
    label, url = value["label"], value["url"]
    return (
        isinstance(label, str)
        and 0 < len(label) <= 64
        and isinstance(url, str)
        and 0 < len(url) <= 2_048
        and url.lower().startswith("https://")
    )


def is_control_automation_policy(value: object) -> TypeGuard[ControlAutomationPolicy]:
    keys = frozenset({"status", "title", "message", "severity", "cta", "automation"})
    if not _exact_control_keys(value, keys):
        return False
    title, message, cta = value["title"], value["message"], value["cta"]
    status, severity = value["status"], value["severity"]
    return (
        isinstance(status, str)
        and status in {"loading", "ready", "empty", "error"}
        and isinstance(title, str)
        and len(title) <= 120
        and isinstance(message, str)
        and len(message) <= 1_024
        and isinstance(severity, str)
        and severity in {"info", "warning"}
        and (cta is None or is_control_automation_policy_cta(cta))
        and is_control_automation_flags(value["automation"])
    )


def is_control_automation_event(value: object) -> TypeGuard[ControlAutomationEvent]:
    keys = frozenset(
        {
            "meetingId",
            "title",
            "startAtMillis",
            "endAtMillis",
            "responseStatus",
            "meetingDecision",
            "meetingUrl",
        }
    )
    if not _exact_control_keys(value, keys):
        return False
    meeting_id, title, url = value["meetingId"], value["title"], value["meetingUrl"]
    start, end = value["startAtMillis"], value["endAtMillis"]
    response, decision = value["responseStatus"], value["meetingDecision"]
    return (
        isinstance(meeting_id, str)
        and re.fullmatch(r"upcoming-[a-f0-9]{64}", meeting_id) is not None
        and isinstance(title, str)
        and 0 < len(title) <= 512
        and _is_action_bounded_integer(start, minimum=1, maximum=RECORDING_CONTROL_SAFE_INTEGER_MAX)
        and _is_action_bounded_integer(end, minimum=1, maximum=RECORDING_CONTROL_SAFE_INTEGER_MAX)
        and isinstance(response, str)
        and response in {"accepted", "declined", "tentative", "needs_action", "unknown"}
        and isinstance(decision, str)
        and decision in {"join", "skip"}
        and isinstance(url, str)
        and 0 < len(url) <= 2_048
        and url.lower().startswith("https://")
    )


def is_control_automation_calendar(
    value: object,
) -> TypeGuard[ControlAutomationCalendar]:
    keys = frozenset(
        {
            "authorityIssuedAtMicros",
            "validatedAtMillis",
            "generatedAtMillis",
            "freshUntilMillis",
            "authoritative",
            "hostedAutomationAllowed",
            "localSetupComplete",
            "events",
        }
    )
    if not _exact_control_keys(value, keys):
        return False
    events = value["events"]
    return (
        all(
            _control_safe_integer(value[key])
            for key in (
                "authorityIssuedAtMicros",
                "validatedAtMillis",
                "generatedAtMillis",
                "freshUntilMillis",
            )
        )
        and all(
            isinstance(value[key], bool)
            for key in (
                "authoritative",
                "hostedAutomationAllowed",
                "localSetupComplete",
            )
        )
        and isinstance(events, list)
        and len(events) <= 64
        and all(is_control_automation_event(event) for event in events)
    )


def _control_action_arguments_are_valid(action: ControlAction, value: object) -> bool:
    if not isinstance(value, dict) or any(not isinstance(key, str) for key in value):
        return False
    keys = set(value)
    if action in {
        ControlAction.STATUS,
        ControlAction.GET_SETTINGS,
        ControlAction.LIST_AUDIO_DEVICES,
        ControlAction.REQUEST_MICROPHONE,
        ControlAction.REQUEST_SYSTEM_AUDIO,
        ControlAction.RETRY_UPLOAD,
        ControlAction.REFRESH_HOME_CACHE,
        ControlAction.OPEN_LOG_VIEWER,
        ControlAction.QUIT_FOR_UPDATE,
    }:
        return not keys
    if action in {
        ControlAction.STOP,
        ControlAction.PAUSE,
        ControlAction.RESUME,
        ControlAction.DISMISS_ACTIVITY_WARNING,
    }:
        session = value.get("expectedSessionId")
        return keys <= {"expectedSessionId"} and (
            "expectedSessionId" not in keys
            or isinstance(session, str)
            and re.fullmatch(
                r"session_[a-f0-9]{32}|session-[a-f0-9]{8}-[a-f0-9]{4}-"
                r"[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
                session,
            )
            is not None
        )
    if action is ControlAction.START:
        if not keys <= {"meetingId", "title", "meetingUrl"}:
            return False
        meeting_id = value.get("meetingId")
        title = value.get("title")
        meeting_url = value.get("meetingUrl")
        meeting_id_pattern = r"[A-Za-z0-9][A-Za-z0-9._:@-]{0,255}"
        valid_title = isinstance(title, str) and 0 < len(title) <= 512
        return (
            (
                "meetingId" not in keys
                or isinstance(meeting_id, str)
                and re.fullmatch(meeting_id_pattern, meeting_id) is not None
            )
            and ("title" not in keys or valid_title)
            and (
                "meetingUrl" not in keys
                or isinstance(meeting_url, str)
                and 0 < len(meeting_url) <= 2048
            )
        )
    if action is ControlAction.SYNC_NOW:
        return keys == {"automatic"} and isinstance(value.get("automatic"), bool)
    if action is ControlAction.GET_LOCAL_CALENDAR:
        if keys != {"startAtMillis", "endAtMillis", "limit"}:
            return False
        start = value.get("startAtMillis")
        end = value.get("endAtMillis")
        limit = value.get("limit")
        return (
            type(start) is int
            and type(end) is int
            and type(limit) is int
            and 0 < start < end <= RECORDING_CONTROL_SAFE_INTEGER_MAX
            and 0 < limit <= LOCAL_CALENDAR_QUERY_MAXIMUM_EVENTS
            and end - start <= LOCAL_CALENDAR_QUERY_MAXIMUM_WINDOW_MILLIS
        )
    if action is ControlAction.GET_NOTE_DETAIL:
        note = value.get("noteId")
        return (
            keys == {"noteId"}
            and isinstance(note, str)
            and (re.fullmatch(r"hosted-[a-f0-9]{64}", note) is not None)
        )
    if action is ControlAction.RETRY_UPLOAD_TARGET:
        recording = value.get("recordingId")
        return (
            keys == {"recordingId"}
            and isinstance(recording, str)
            and (re.fullmatch(r"recording-[a-f0-9]{64}", recording) is not None)
        )
    if action is ControlAction.SYNC_AUTOMATION:
        return (
            keys == {"scopeFingerprint", "policy", "calendar"}
            and _control_fingerprint(value.get("scopeFingerprint"))
            and is_control_automation_policy(value.get("policy"))
            and is_control_automation_calendar(value.get("calendar"))
        )
    if action is ControlAction.UPDATE_SETTINGS:
        permitted = {
            "backgroundEnabled",
            "soundEffectsEnabled",
            "calendarSyncEnabled",
            "calendarReminderEnabled",
            "meetingDetectionEnabled",
            "expectedMeetingDetectionOwnerScopeFingerprint",
            "localCalendarSyncEnabled",
            "selectedLocalCalendarIDs",
            "localCalendarThreadID",
            "expectedLocalCalendarOwnerScopeFingerprint",
            "syncIntervalMinutes",
            "microphoneDeviceId",
            "systemAudioDeviceId",
        }
        if not keys <= permitted:
            return False
        for key in (
            "backgroundEnabled",
            "soundEffectsEnabled",
            "calendarSyncEnabled",
            "calendarReminderEnabled",
            "meetingDetectionEnabled",
            "localCalendarSyncEnabled",
        ):
            if key in value and not isinstance(value[key], bool):
                return False
        if "syncIntervalMinutes" in value:
            interval = value["syncIntervalMinutes"]
            if not _is_action_bounded_integer(interval, minimum=5, maximum=1_440):
                return False
        if "selectedLocalCalendarIDs" in value:
            calendars = value["selectedLocalCalendarIDs"]
            if not isinstance(calendars, list) or len(calendars) > 64:
                return False
            if any(
                not isinstance(calendar, str) or not 0 < len(calendar) <= 512
                for calendar in calendars
            ) or len(set(calendars)) != len(calendars):
                return False
        if "localCalendarThreadID" in value:
            thread = value["localCalendarThreadID"]
            if thread is not None and (
                not isinstance(thread, str)
                or re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:@-]{0,255}", thread) is None
            ):
                return False
        if "expectedLocalCalendarOwnerScopeFingerprint" in value and not _control_fingerprint(
            value["expectedLocalCalendarOwnerScopeFingerprint"]
        ):
            return False
        if "expectedMeetingDetectionOwnerScopeFingerprint" in value and not _control_fingerprint(
            value["expectedMeetingDetectionOwnerScopeFingerprint"]
        ):
            return False
        for key, maximum in (
            ("microphoneDeviceId", 512),
            ("systemAudioDeviceId", 512),
        ):
            if (
                key in value
                and value[key] is not None
                and (not isinstance(value[key], str) or len(value[key]) > maximum)
            ):
                return False
        return True
    return False


@overload
def is_control_action_arguments(
    value: object,
    action: Literal[ControlAction.SYNC_AUTOMATION],
) -> TypeGuard[AutomationSyncActionArguments]: ...


@overload
def is_control_action_arguments(
    value: object,
    action: object,
) -> TypeGuard[ControlActionArguments]: ...


def is_control_action_arguments(
    value: object,
    action: object,
) -> TypeGuard[ControlActionArguments]:
    """Narrow authenticated arguments using their generated action contract."""
    parsed = parse_control_action(action)
    return parsed is not ControlAction.UNKNOWN and _control_action_arguments_are_valid(
        parsed, value
    )


def control_action_arguments_are_valid(action: object, value: object) -> bool:
    """Preserve the existing action-first recording control validator."""
    return is_control_action_arguments(value, action)


def is_control_local_calendar_event(
    value: object,
) -> TypeGuard[ControlLocalCalendarEvent]:
    if not _exact_control_keys(value, ControlLocalCalendarEvent.__required_keys__):
        return False
    hosted = value.copy()
    calendar = hosted.pop("calendarID")
    hosted["meetingId"] = hosted.pop("id")
    hosted["responseStatus"], hosted["meetingDecision"] = "unknown", "skip"
    if hosted["meetingUrl"] is None:
        hosted["meetingUrl"] = "https://local.invalid"
    return (
        isinstance(calendar, str)
        and 0 < len(calendar) <= 512
        and is_control_automation_event(hosted)
        and hosted["startAtMillis"] < hosted["endAtMillis"]
    )


def is_control_local_calendar_query_result(
    value: object,
) -> TypeGuard[ControlLocalCalendarQueryResult]:
    if not _exact_control_keys(value, frozenset({"events"})):
        return False
    events = value["events"]
    return (
        isinstance(events, list)
        and len(events) <= LOCAL_CALENDAR_QUERY_MAXIMUM_EVENTS
        and all(is_control_local_calendar_event(event) for event in events)
    )
