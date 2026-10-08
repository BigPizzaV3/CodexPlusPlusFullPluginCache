#!/usr/bin/env python3
"""Live-stream request validation and fixed Meetings recovery contracts."""

from __future__ import annotations

import json
import re
from collections.abc import Mapping
from urllib.parse import urlsplit

from control_transport.live_client import (
    LiveTransportError,
    LiveTransportFailureKind,
    LiveTransportFailureReason,
)
from native_runtime import NativeRuntimeError, RuntimeManager, public_runtime_status
from recording_control_action_contract import (
    ControlAction,
    ControlActionArguments,
    is_control_action_arguments,
    parse_control_action,
)
from recording_status_contract import (
    RECORDING_STATUS_SCHEMA_VERSION,
    RecordingNativeStatus,
    RecordingPermissionPresentation,
    RecordingRecoveryKind,
)

from helpers import is_json

_SAFE_MEETING_ID_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:@-]{0,255}\Z")
_SHA256_HEX_PATTERN = re.compile(r"[a-f0-9]{64}\Z")

SAFE_LOCAL_UNAVAILABLE_MESSAGE = "Meetings local capture is unavailable"
SAFE_LOCAL_REQUEST_FAILED_MESSAGE = "Local recording request could not be completed"
SAFE_CHECKING_MESSAGE = "Checking Meetings local capture…"
SAFE_START_OWNER_CHANGED_MESSAGE = (
    "Meetings restarted before the recording start was admitted. Retry."
)
SAFE_LAUNCHING_MESSAGE = "Opening Meetings. Waiting for its local control…"
SAFE_CACHED_LAUNCHING_MESSAGE = (
    "Opening the verified Meetings app. "
    "The update check is unavailable, so this launch is using "
    "the last verified version."
)
SAFE_QUIT_REQUIRED_MESSAGE = (
    "Finish any active recording, quit the older Meetings app, then retry the update."
)
SAFE_UPDATE_DEFERRED_MESSAGE = (
    "Finish any active recording. Meetings will retry the "
    "update automatically; select Restart to try again now."
)
_SAFE_DISCONNECTED_MESSAGES = frozenset(
    {
        SAFE_LOCAL_UNAVAILABLE_MESSAGE,
        SAFE_LAUNCHING_MESSAGE,
        SAFE_CACHED_LAUNCHING_MESSAGE,
        SAFE_QUIT_REQUIRED_MESSAGE,
        SAFE_UPDATE_DEFERRED_MESSAGE,
        SAFE_START_OWNER_CHANGED_MESSAGE,
    }
)
_SYNTHETIC_OFFLINE_PERMISSION_SOURCE = "synthetic-offline"


class ControlUnavailable(RuntimeError):
    """The authenticated local-control request or recovery contract was unavailable."""


class ControlConnectionUnavailable(ControlUnavailable):
    """A local connection or request can recover without replaying the operation."""


class ControlEndpointRejected(ControlUnavailable):
    """Endpoint checks failed; only independently verified owner recovery may proceed."""


def control_transport_error(error: LiveTransportError, message: str) -> ControlUnavailable:
    """Preserve the producer's recovery policy at every control boundary.

    Recovery retries connection and owner validation, never the failed operation.
    This match is exhaustive so adding a transport kind requires a policy choice.
    """

    match error.kind:
        case LiveTransportFailureKind.UNAVAILABLE | LiveTransportFailureKind.TIMED_OUT:
            return ControlConnectionUnavailable(message)
        case LiveTransportFailureKind.REJECTED:
            if error.diagnostic_reason is LiveTransportFailureReason.ENDPOINT_REJECTED:
                return ControlEndpointRejected(message)
            return ControlUnavailable(message)
        case LiveTransportFailureKind.CANCELLED:
            return ControlUnavailable(message)


def compatible_native_release_version(value: object) -> bool:
    """Validate a bounded native release without enumerating shipped versions."""

    if not isinstance(value, str) or len(value) > 64:
        return False
    try:
        RuntimeManager.native_release_version_key(value)
    except NativeRuntimeError:
        return False
    return True


def canonical_json(value: object) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
        allow_nan=False,
    )


def normalize_arguments(arguments: object) -> dict[str, object]:
    """Return canonical JSON arguments for an authenticated live stream.

    The native bridge is still the authority for action-specific validation.
    Normalizing here prevents Python-only values, non-string keys, and NaN
    from producing a request that the companion cannot faithfully decode.
    """

    if arguments is None:
        return {}
    if not is_json(arguments):
        raise ControlUnavailable("native control arguments must be a JSON object")
    try:
        decoded: object = json.loads(canonical_json(arguments))
    except (TypeError, ValueError, json.JSONDecodeError) as exc:
        raise ControlUnavailable("native control arguments are not valid JSON") from exc
    if not is_json(decoded):
        raise ControlUnavailable("native control arguments must be a JSON object")
    return decoded


def normalize_action_arguments(
    action: object,
    arguments: object,
) -> ControlActionArguments:
    """Validate the complete stream argument schema for one native action.

    Keep this allowlist in the stream transport boundary itself: callers may
    not send undeclared fields or use an action as a generic secret-bearing bag.
    """

    parsed_action = parse_control_action(action)
    if parsed_action in {
        ControlAction.UNKNOWN,
        ControlAction.SYNC_AUTOMATION,
        ControlAction.REFRESH_HOME_CACHE,
        ControlAction.LIST_AUDIO_DEVICES,
    }:
        raise ControlUnavailable("native control action is unsupported")
    normalized = normalize_arguments(arguments)
    if not is_control_action_arguments(normalized, parsed_action):
        raise ControlUnavailable("native control arguments do not match action")
    if parsed_action is ControlAction.START:
        meeting_id = normalized.get("meetingId")
        if meeting_id is not None and (
            not isinstance(meeting_id, str)
            or _SAFE_MEETING_ID_PATTERN.fullmatch(meeting_id) is None
        ):
            raise ControlUnavailable("native control arguments do not match action")
        title = normalized.get("title")
        if title is not None and (
            not isinstance(title, str)
            or not title.strip()
            or len(title.strip()) > 512
            or any(ord(character) < 32 or ord(character) == 127 for character in title)
        ):
            raise ControlUnavailable("native control arguments do not match action")
        meeting_url = normalized.get("meetingUrl")
        if meeting_url is not None:
            if (
                not isinstance(meeting_url, str)
                or len(meeting_url) > 2_048
                or any(ord(character) < 32 or ord(character) == 127 for character in meeting_url)
            ):
                raise ControlUnavailable("native control arguments do not match action")
            try:
                parsed = urlsplit(meeting_url)
                hostname = parsed.hostname
            except ValueError as exc:
                raise ControlUnavailable("native control arguments do not match action") from exc
            if (
                parsed.scheme.lower() not in {"http", "https"}
                or not hostname
                or parsed.username is not None
                or parsed.password is not None
            ):
                raise ControlUnavailable("native control arguments do not match action")
    elif parsed_action is ControlAction.UPDATE_SETTINGS:
        for key in ("microphoneDeviceId", "systemAudioDeviceId"):
            device_id = normalized.get(key)
            if device_id is not None and (
                not isinstance(device_id, str) or _SHA256_HEX_PATTERN.fullmatch(device_id) is None
            ):
                raise ControlUnavailable("native control arguments do not match action")
    return normalized


def disconnected_state(
    _error: str | None = None,
    *,
    safe_message: str | None = None,
    recovery_kind: str | None = None,
    runtime: Mapping[str, object] | None = None,
) -> dict[str, object]:
    """Return fixed offline copy; exception text can contain local paths.

    safe_message must be one of this module's fixed recovery literals.
    Positional exception text is intentionally ignored.
    """

    resolved_runtime = runtime if runtime is not None else RuntimeManager().status()
    message = (
        safe_message
        if safe_message in _SAFE_DISCONNECTED_MESSAGES
        else SAFE_LOCAL_UNAVAILABLE_MESSAGE
    )
    safe_recovery_kind = (
        RecordingRecoveryKind.QUIT_REQUIRED.value
        if (
            recovery_kind == RecordingRecoveryKind.QUIT_REQUIRED.value
            and message == SAFE_QUIT_REQUIRED_MESSAGE
        )
        else RecordingRecoveryKind.UPDATE_DEFERRED.value
        if (
            recovery_kind == RecordingRecoveryKind.UPDATE_DEFERRED.value
            and message == SAFE_UPDATE_DEFERRED_MESSAGE
        )
        else RecordingRecoveryKind.START_RETRY_REQUIRED.value
        if (
            recovery_kind == RecordingRecoveryKind.START_RETRY_REQUIRED.value
            and message == SAFE_START_OWNER_CHANGED_MESSAGE
        )
        else RecordingRecoveryKind.LAUNCH_REQUIRED.value
        if resolved_runtime["installed"]
        else RecordingRecoveryKind.NOT_INSTALLED.value
    )
    return {
        "schemaVersion": RECORDING_STATUS_SCHEMA_VERSION,
        "ok": False,
        "error": SAFE_LOCAL_UNAVAILABLE_MESSAGE,
        "runtime": public_runtime_status(resolved_runtime),
        "state": {
            "schemaVersion": RECORDING_STATUS_SCHEMA_VERSION,
            "status": RecordingNativeStatus.OFFLINE.value,
            "meetingId": None,
            "title": None,
            "meetingUrl": None,
            "sessionId": None,
            "startedAt": None,
            "message": message,
            "canStart": False,
            "canStop": False,
            "canPause": False,
            "canResume": False,
            "permissionSource": _SYNTHETIC_OFFLINE_PERMISSION_SOURCE,
            "permissionPresentation": {
                "microphone": RecordingPermissionPresentation.UNKNOWN.value,
                "systemAudio": RecordingPermissionPresentation.UNKNOWN.value,
            },
            "permissions": {
                "microphone": RecordingPermissionPresentation.NOT_DETERMINED.value,
                "systemAudio": RecordingPermissionPresentation.NOT_DETERMINED.value,
            },
            "recording": {
                "mixedBytes": 0,
                "startedAt": None,
                "lastAudioSavedLocally": False,
                "lastAudioBytes": 0,
                "lastAudioDurationMs": 0,
                "lastRecording": None,
            },
            "recovery": {
                "kind": safe_recovery_kind,
                "installed": resolved_runtime["installed"],
                "canInstall": True,
                "canLaunch": resolved_runtime["installed"],
            },
        },
    }


def connecting_state(*, runtime: Mapping[str, object]) -> dict[str, object]:
    """Keep a discovered owner's first stream observation safely non-actionable."""

    payload = disconnected_state(runtime=runtime)
    state = payload.get("state")
    if not is_json(state):
        raise ControlUnavailable("native control state is malformed")

    payload["ok"] = True
    payload.pop("error", None)
    state.update(
        {
            "status": RecordingNativeStatus.CHECKING.value,
            "message": SAFE_CHECKING_MESSAGE,
            "permissions": {},
            "recovery": {
                "kind": RecordingRecoveryKind.CHECKING.value,
                "installed": runtime.get("installed") is True,
                "canInstall": False,
                "canLaunch": False,
            },
        }
    )
    return payload
