# GENERATED FILE. DO NOT EDIT.
# Source: chatgpt-meetings-core/contracts/recording-control-stream.v1.schema.json
# SHA-256: f1d971ca1469127abc6b6accc565e4ce936d20a955466470d59159f0fbb24f8f
# Regenerate: python3 chatgpt-meetings-core/scripts/generate_recording_control_stream_contract.py

from __future__ import annotations

import json
import math
import re
from typing import TYPE_CHECKING, Final, Literal, TypedDict

from recording_control_action_contract import (
    ControlActionArguments,
    ControlActionWire,
    is_control_action_arguments,
    is_control_action_wire,
)
from recording_status_contract import (
    RecordingState,
    is_recording_state,
)

if TYPE_CHECKING:
    from typing import TypeGuard
else:
    try:
        from typing import TypeGuard
    except ImportError:

        class TypeGuard:
            """Keep the generated boundary usable on Python 3.9."""

            @classmethod
            def __class_getitem__(cls, _value: object) -> type[bool]:
                return bool


CONTROL_STREAM_SCHEMA_NAME: Final[str] = "chatgpt-meetings.recording-control-stream"
CONTROL_STREAM_SCHEMA_VERSION: Final[int] = 1
CONTROL_STREAM_LIVE_PROTOCOL_VERSION: Final[int] = 1
CONTROL_STREAM_FRAME_PREFIX_BYTE_ORDER: Final[str] = "little-endian"
CONTROL_STREAM_MAX_FRAME_BYTES: Final[int] = 1_048_576
CONTROL_STREAM_MAX_CLIENTS: Final[int] = 16
CONTROL_STREAM_MAX_CACHED_RESPONSES: Final[int] = 128
CONTROL_STREAM_MAX_REQUEST_TTL_MILLIS: Final[int] = 5_000
CONTROL_STREAM_SAFE_INTEGER_MAX: Final[int] = 9_007_199_254_740_991
CONTROL_STREAM_INITIALIZE_METHOD: Final[str] = "meetings.initialize"
CONTROL_STREAM_CONTROL_METHOD: Final[str] = "meetings.control"
CONTROL_STREAM_STATE_CHANGED_METHOD: Final[str] = "meetings.stateChanged"
CONTROL_STREAM_DARWIN_CAPABILITIES: Final[tuple[str, ...]] = (
    "auth.codex-readiness.v1",
    "capture.context.v1",
    "control.local-stream.v1",
    "headless.note-detail.v1",
    "headless.settings.v1",
    "headless.sync-hook.v1",
    "home.cache.refresh.v1",
    "home.cache.v1",
    "lifecycle.capture-aware-sigterm.v1",
    "lifecycle.update-handoff-resumable-outbox.v1",
    "lifecycle.update-handoff-resumable-outbox.v2",
    "lifecycle.update-handoff-work-fence.v1",
    "lifecycle.update-handoff.v1",
    "logs.viewer.v1",
    "recording.pause-resume.v1",
    "recording.receipt.v1",
    "recording.session-fenced-controls.v1",
    "recording.stop.v1",
    "upload.manual-retry.targeted.v1",
    "upload.manual-retry.v1",
    "upload.outbox.v1",
    "upload.post-stop.v1",
    "widget.recent-recording.v1",
    "widget.snapshot.v1",
)
CONTROL_STREAM_WINDOWS_CAPABILITIES: Final[tuple[str, ...]] = (
    "control.local-stream.v1",
    "capture.microphone.v1",
    "capture.system-audio.v1",
    "capture.context.v1",
    "recording.local-wav.v1",
    "recording.stop.v1",
    "recording.pause-resume.v1",
    "recording.session-fenced-controls.v1",
    "recording.receipt.v1",
    "ui.floating-overlay.v1",
    "headless.settings.v1",
    "headless.sync-hook.v1",
    "headless.note-detail.v1",
    "logs.viewer.v1",
    "auth.codex-readiness.v1",
    "calendar.automation-sync.v1",
    "lifecycle.update-handoff.v1",
    "lifecycle.update-handoff-work-fence.v1",
)
CONTROL_STREAM_WINDOWS_REQUIRED_UPDATE_CAPABILITIES: Final[tuple[str, ...]] = (
    "control.local-stream.v1",
    "capture.microphone.v1",
    "capture.system-audio.v1",
    "recording.local-wav.v1",
    "recording.stop.v1",
    "recording.pause-resume.v1",
    "recording.session-fenced-controls.v1",
    "recording.receipt.v1",
    "lifecycle.update-handoff.v1",
    "lifecycle.update-handoff-work-fence.v1",
)
CONTROL_STREAM_SCHEMA_SHA256: Final[str] = (
    "f1d971ca1469127abc6b6accc565e4ce936d20a955466470d59159f0fbb24f8f"
)

ControlStreamPlatform = Literal[
    "darwin-universal", "darwin-arm64", "darwin-x64", "windows-x64", "windows-arm64"
]
ControlStreamTransport = Literal["unix-domain-socket", "windows-named-pipe"]


class ControlStreamCompatibilitySource(TypedDict):
    kind: Literal["chatgpt-meetings-native"]
    version: str


class ControlStreamCompatibilityDestination(TypedDict):
    kind: Literal["chatgpt-meetings-plugin"]
    minimumPluginVersion: str


class ControlStreamCompatibility(TypedDict):
    source: ControlStreamCompatibilitySource
    destination: ControlStreamCompatibilityDestination


class _RequiredControlStreamDescriptor(TypedDict):
    schemaVersion: Literal[1]
    liveControlProtocolVersion: Literal[1]
    epoch: str
    pid: int
    requestTTLMillis: int
    transport: ControlStreamTransport
    endpoint: str
    appTarget: str
    platform: ControlStreamPlatform
    appVersion: str
    capabilities: list[str]
    compatibility: ControlStreamCompatibility


class ControlStreamDescriptor(_RequiredControlStreamDescriptor, total=False):
    appDisplayName: str
    bundleIdentifier: str
    bundlePath: str
    installPath: str
    executablePath: str
    executableSHA256: str
    executableDevice: int
    executableInode: int
    e2eIsolation: dict[str, object]


class ControlStreamInitializeParams(TypedDict):
    clientKind: Literal["chatgpt-meetings-plugin"]
    clientVersion: str
    supportedStreamSchemaVersions: list[int]
    supportedLiveControlProtocolVersions: list[int]
    capabilities: list[str]


class ControlStreamInitializeResult(TypedDict):
    streamSchemaVersion: Literal[1]
    liveControlProtocolVersion: Literal[1]
    serverKind: Literal["chatgpt-meetings-native"]
    epoch: str
    platform: ControlStreamPlatform
    appVersion: str
    capabilities: list[str]
    state: RecordingState


class ControlStreamControlParams(TypedDict):
    clientId: str
    sequence: int
    requestId: str
    issuedAtMillis: int
    action: ControlActionWire
    arguments: ControlActionArguments


class ControlStreamJsonRpcRequest(TypedDict):
    jsonrpc: Literal["2.0"]
    id: str
    method: Literal["meetings.initialize", "meetings.control"]
    params: ControlStreamInitializeParams | ControlStreamControlParams


class _RequiredControlStreamJsonRpcError(TypedDict):
    code: int
    message: str


class ControlStreamJsonRpcError(_RequiredControlStreamJsonRpcError, total=False):
    data: dict[str, object]


class _RequiredControlStreamJsonRpcResponse(TypedDict):
    jsonrpc: Literal["2.0"]
    id: str


class ControlStreamJsonRpcResponse(_RequiredControlStreamJsonRpcResponse, total=False):
    result: dict[str, object]
    error: ControlStreamJsonRpcError


class ControlStreamStateNotificationParams(TypedDict):
    epoch: str
    revision: int
    state: RecordingState


class ControlStreamStateNotification(TypedDict):
    jsonrpc: Literal["2.0"]
    method: Literal["meetings.stateChanged"]
    params: ControlStreamStateNotificationParams


_IDENTIFIER = re.compile(r"[A-Za-z0-9_-]{8,128}", re.ASCII)
_CAPABILITY = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\.v[0-9]+", re.ASCII)
_PLUGIN_VERSION = re.compile(r"[0-9]+\.[0-9]+\.[0-9]+", re.ASCII)
_SHA256 = re.compile(r"[a-f0-9]{64}", re.ASCII)
_PLATFORMS: Final[frozenset[str]] = frozenset(
    ("darwin-universal", "darwin-arm64", "darwin-x64", "windows-x64", "windows-arm64")
)
_DESCRIPTOR_REQUIRED: Final[frozenset[str]] = frozenset(
    (
        "schemaVersion",
        "liveControlProtocolVersion",
        "epoch",
        "pid",
        "requestTTLMillis",
        "transport",
        "endpoint",
        "appTarget",
        "platform",
        "appVersion",
        "capabilities",
        "compatibility",
    )
)
_DESCRIPTOR_OPTIONAL: Final[frozenset[str]] = frozenset(
    (
        "appDisplayName",
        "bundleIdentifier",
        "bundlePath",
        "installPath",
        "executablePath",
        "executableSHA256",
        "executableDevice",
        "executableInode",
        "e2eIsolation",
    )
)


def _exact_keys(
    value: object,
    required: frozenset[str],
    optional: frozenset[str] = frozenset(),
) -> TypeGuard[dict[str, object]]:
    if type(value) is not dict or any(type(key) is not str for key in value):
        return False
    keys = frozenset(value)
    return required <= keys and keys <= required | optional


def _bounded_integer(
    value: object,
    minimum: int = 0,
    maximum: int = CONTROL_STREAM_SAFE_INTEGER_MAX,
) -> TypeGuard[int]:
    return type(value) is int and minimum <= value <= maximum


def _bounded_text(value: object, maximum: int, minimum: int = 1) -> TypeGuard[str]:
    return type(value) is str and minimum <= len(value) <= maximum


def _identifier(value: object) -> TypeGuard[str]:
    return type(value) is str and _IDENTIFIER.fullmatch(value) is not None


def _plugin_version(value: object) -> TypeGuard[str]:
    return _bounded_text(value, 32, 5) and _PLUGIN_VERSION.fullmatch(value) is not None


def _capabilities(value: object) -> TypeGuard[list[str]]:
    if type(value) is not list or not 1 <= len(value) <= 64:
        return False
    for item in value:
        if not _bounded_text(item, 128) or _CAPABILITY.fullmatch(item) is None:
            return False
    return len(set(value)) == len(value) and "control.local-stream.v1" in value


def _supported_versions(value: object) -> TypeGuard[list[int]]:
    if type(value) is not list or not 1 <= len(value) <= 16:
        return False
    if any(not _bounded_integer(item, 1) for item in value):
        return False
    return len(set(value)) == len(value) and 1 in value


def _json_value_is_safe(value: object, seen: set[int], depth: int = 0) -> bool:
    if depth > 64:
        return False
    if value is None or type(value) in (bool, str):
        return True
    if type(value) is int:
        return -CONTROL_STREAM_SAFE_INTEGER_MAX <= value <= CONTROL_STREAM_SAFE_INTEGER_MAX
    if type(value) is float:
        return math.isfinite(value) and (
            not value.is_integer() or abs(value) <= CONTROL_STREAM_SAFE_INTEGER_MAX
        )
    if type(value) not in (dict, list):
        return False
    identity = id(value)
    if identity in seen:
        return False
    seen.add(identity)
    try:
        if type(value) is dict:
            return all(
                type(key) is str and _json_value_is_safe(item, seen, depth + 1)
                for key, item in value.items()
            )
        return isinstance(value, list) and all(
            _json_value_is_safe(item, seen, depth + 1) for item in value
        )
    finally:
        seen.remove(identity)


def _bounded_json_object(value: object) -> bool:
    if type(value) is not dict or not _json_value_is_safe(value, set()):
        return False
    try:
        encoded = json.dumps(
            value,
            allow_nan=False,
            ensure_ascii=False,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError, OverflowError, RecursionError, UnicodeEncodeError):
        return False
    return 0 < len(encoded) <= CONTROL_STREAM_MAX_FRAME_BYTES


def _is_live_recording_state(value: object) -> TypeGuard[RecordingState]:
    if type(value) is not dict:
        return False
    known_state = dict(value)
    if "upload" in known_state:
        if type(known_state["upload"]) is not dict:
            return False
        known_state.pop("upload")
    recording = known_state.get("recording")
    if type(recording) is dict:
        last_recording = recording.get("lastRecording")
        if type(last_recording) is dict:
            rust = last_recording.get("rust")
            if rust is not None and type(rust) is not dict:
                return False
            known_recording = dict(recording)
            known_last_recording = dict(last_recording)
            known_last_recording.pop("rust", None)
            identifier = known_last_recording.get("recordingId")
            if (
                isinstance(identifier, str)
                and re.fullmatch(r"recording_[a-f0-9]{32}", identifier) is not None
            ):
                known_last_recording.pop("recordingId")
            known_recording["lastRecording"] = known_last_recording
            known_state["recording"] = known_recording
    return is_recording_state(known_state)


def _compatibility(value: object) -> bool:
    if not _exact_keys(value, frozenset(("source", "destination"))):
        return False
    source = value["source"]
    destination = value["destination"]
    return (
        _exact_keys(source, frozenset(("kind", "version")))
        and source["kind"] == "chatgpt-meetings-native"
        and _bounded_text(source["version"], 64)
        and _exact_keys(destination, frozenset(("kind", "minimumPluginVersion")))
        and destination["kind"] == "chatgpt-meetings-plugin"
        and _plugin_version(destination["minimumPluginVersion"])
    )


def is_control_stream_descriptor(value: object) -> TypeGuard[ControlStreamDescriptor]:
    if not _exact_keys(value, _DESCRIPTOR_REQUIRED, _DESCRIPTOR_OPTIONAL):
        return False
    if not (
        _bounded_integer(value["schemaVersion"], 1, 1)
        and _bounded_integer(value["liveControlProtocolVersion"], 1, 1)
        and _identifier(value["epoch"])
        and _bounded_integer(value["pid"], 1, 2_147_483_647)
        and _bounded_integer(value["requestTTLMillis"], 1, CONTROL_STREAM_MAX_REQUEST_TTL_MILLIS)
        and _bounded_text(value["endpoint"], 4096)
        and not any(character in value["endpoint"] for character in ("\0", "\r", "\n"))
        and _bounded_text(value["appTarget"], 256)
        and _bounded_text(value["appVersion"], 64)
        and type(value["platform"]) is str
        and value["platform"] in _PLATFORMS
        and _capabilities(value["capabilities"])
        and _compatibility(value["compatibility"])
    ):
        return False

    windows = value["platform"].startswith("windows-")
    expected_transport = "windows-named-pipe" if windows else "unix-domain-socket"
    if value["transport"] != expected_transport:
        return False
    if windows and not {"executablePath", "executableSHA256"} <= value.keys():
        return False
    for field, maximum in (
        ("appDisplayName", 256),
        ("bundleIdentifier", 256),
        ("bundlePath", 4096),
        ("installPath", 4096),
        ("executablePath", 4096),
    ):
        if field in value and not _bounded_text(value[field], maximum):
            return False
    if "executableSHA256" in value and (
        type(value["executableSHA256"]) is not str
        or _SHA256.fullmatch(value["executableSHA256"]) is None
    ):
        return False
    if ("executableDevice" in value) != ("executableInode" in value):
        return False
    for field in ("executableDevice", "executableInode"):
        if field in value and not _bounded_integer(value[field], 1):
            return False
    if "e2eIsolation" in value and type(value["e2eIsolation"]) is not dict:
        return False
    return _bounded_json_object(value)


def is_control_stream_initialize_params(value: object) -> TypeGuard[ControlStreamInitializeParams]:
    return (
        _exact_keys(
            value,
            frozenset(
                (
                    "clientKind",
                    "clientVersion",
                    "supportedStreamSchemaVersions",
                    "supportedLiveControlProtocolVersions",
                    "capabilities",
                )
            ),
        )
        and value["clientKind"] == "chatgpt-meetings-plugin"
        and _plugin_version(value["clientVersion"])
        and _supported_versions(value["supportedStreamSchemaVersions"])
        and _supported_versions(value["supportedLiveControlProtocolVersions"])
        and _capabilities(value["capabilities"])
        and _bounded_json_object(value)
    )


def is_control_stream_initialize_result(value: object) -> TypeGuard[ControlStreamInitializeResult]:
    return (
        _exact_keys(
            value,
            frozenset(
                (
                    "streamSchemaVersion",
                    "liveControlProtocolVersion",
                    "serverKind",
                    "epoch",
                    "platform",
                    "appVersion",
                    "capabilities",
                    "state",
                )
            ),
        )
        and _bounded_integer(value["streamSchemaVersion"], 1, 1)
        and _bounded_integer(value["liveControlProtocolVersion"], 1, 1)
        and value["serverKind"] == "chatgpt-meetings-native"
        and _identifier(value["epoch"])
        and type(value["platform"]) is str
        and value["platform"] in _PLATFORMS
        and _bounded_text(value["appVersion"], 64)
        and _capabilities(value["capabilities"])
        and _is_live_recording_state(value["state"])
        and _bounded_json_object(value)
    )


def is_control_stream_negotiation(params: object, result: object) -> bool:
    return (
        is_control_stream_initialize_params(params)
        and is_control_stream_initialize_result(result)
        and result["streamSchemaVersion"] in params["supportedStreamSchemaVersions"]
        and result["liveControlProtocolVersion"] in params["supportedLiveControlProtocolVersions"]
        and frozenset(result["capabilities"]) <= frozenset(params["capabilities"])
    )


def is_control_stream_control_params(value: object) -> TypeGuard[ControlStreamControlParams]:
    return (
        _exact_keys(
            value,
            frozenset(
                ("clientId", "sequence", "requestId", "issuedAtMillis", "action", "arguments")
            ),
        )
        and _identifier(value["clientId"])
        and _bounded_integer(value["sequence"], 1)
        and _identifier(value["requestId"])
        and _bounded_integer(value["issuedAtMillis"], 1)
        and is_control_action_wire(value["action"])
        and is_control_action_arguments(value["arguments"], value["action"])
        and _bounded_json_object(value)
    )


def is_control_stream_json_rpc_request(value: object) -> TypeGuard[ControlStreamJsonRpcRequest]:
    if not (
        _exact_keys(value, frozenset(("jsonrpc", "id", "method", "params")))
        and value["jsonrpc"] == "2.0"
        and _identifier(value["id"])
        and _bounded_json_object(value)
    ):
        return False
    if value["method"] == CONTROL_STREAM_INITIALIZE_METHOD:
        return is_control_stream_initialize_params(value["params"])
    if value["method"] == CONTROL_STREAM_CONTROL_METHOD:
        params = value["params"]
        return is_control_stream_control_params(params) and value["id"] == params["requestId"]
    return False


def is_control_stream_json_rpc_error(value: object) -> TypeGuard[ControlStreamJsonRpcError]:
    return (
        _exact_keys(value, frozenset(("code", "message")), frozenset(("data",)))
        and _bounded_integer(value["code"], -CONTROL_STREAM_SAFE_INTEGER_MAX)
        and _bounded_text(value["message"], 1024)
        and ("data" not in value or type(value["data"]) is dict)
        and _bounded_json_object(value)
    )


def is_control_stream_json_rpc_response(value: object) -> TypeGuard[ControlStreamJsonRpcResponse]:
    if not (
        _exact_keys(value, frozenset(("jsonrpc", "id")), frozenset(("result", "error")))
        and value["jsonrpc"] == "2.0"
        and _identifier(value["id"])
        and (("result" in value) != ("error" in value))
        and _bounded_json_object(value)
    ):
        return False
    if "error" in value:
        return is_control_stream_json_rpc_error(value["error"])
    return type(value["result"]) is dict


def is_control_stream_state_notification_params(
    value: object,
) -> TypeGuard[ControlStreamStateNotificationParams]:
    return (
        _exact_keys(value, frozenset(("epoch", "revision", "state")))
        and _identifier(value["epoch"])
        and _bounded_integer(value["revision"], 1)
        and _is_live_recording_state(value["state"])
        and _bounded_json_object(value)
    )


def is_control_stream_state_notification(
    value: object,
) -> TypeGuard[ControlStreamStateNotification]:
    return (
        _exact_keys(value, frozenset(("jsonrpc", "method", "params")))
        and value["jsonrpc"] == "2.0"
        and value["method"] == CONTROL_STREAM_STATE_CHANGED_METHOD
        and is_control_stream_state_notification_params(value["params"])
        and _bounded_json_object(value)
    )
