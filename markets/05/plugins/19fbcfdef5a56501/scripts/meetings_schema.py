"""Bounded tool and gateway schemas for the ChatGPT Meetings MCP."""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import TypeAlias, TypeGuard

from companion_control_v2 import PROTOCOL_VERSION, SCHEMA_SHA256
from meetings_analytics import PluginEventName, PluginEventSurface
from meetings_api_client import FEEDBACK_CATEGORIES, GATEWAY_SETTING_NAMES
from meetings_metrics import (
    CLIENT_PERFORMANCE_OPERATIONS,
    CLIENT_PERFORMANCE_TRANSITIONS,
    CLIENT_STREAMING_STATES,
    MAXIMUM_CLIENT_PERFORMANCE_DURATION_MILLISECONDS,
    NOTES_REFRESH_TRIGGERS,
)
from meetings_sentry import (
    MCP_SENTRY_KINDS,
    MCP_SENTRY_NOTIFICATIONS,
    MCP_SENTRY_OPERATIONS,
    MCP_SENTRY_PRESENTATIONS,
    MCP_SENTRY_STAGES,
    MCP_SENTRY_UPDATE_REASONS,
)

from helpers import JSONValue, is_json, is_json_value

JSONSchema: TypeAlias = dict[str, JSONValue]
_PUBLIC_RECORDING_SESSION_ID = re.compile(r"[A-Za-z0-9_-]{8,128}\Z")


def is_json_object(value: object) -> TypeGuard[JSONSchema]:
    """Check that a value is a string-keyed, recursively JSON-safe object.

    Args:
        value: Candidate decoded or application-produced value.

    Returns:
        Whether the value can cross a JSON object boundary without coercion.
    """

    return is_json(value) and all(is_json_value(item) for item in value.values())


def is_public_recording_session_id(value: object) -> TypeGuard[str]:
    """Validate one real companion v2 recording session identifier.

    Args:
        value: Candidate app-facing recording session identifier.

    Returns:
        Whether the value satisfies the generated companion identifier contract.
    """

    return isinstance(value, str) and _PUBLIC_RECORDING_SESSION_ID.fullmatch(value) is not None


def _recording_status_output_schema() -> JSONSchema:
    """Expose only the public, exact companion-control v2 recording contract."""

    companion_schema_bytes = (
        Path(__file__).with_name("companion-control.v2.schema.json").read_bytes()
    )
    if hashlib.sha256(companion_schema_bytes).hexdigest() != SCHEMA_SHA256:
        raise RuntimeError("packaged companion control v2 contract is unavailable")
    companion_schema: object = json.loads(companion_schema_bytes)
    if not is_json_object(companion_schema):
        raise RuntimeError("packaged companion control v2 contract is unavailable")
    companion_definitions = companion_schema.get("$defs")
    if not is_json_object(companion_definitions):
        raise RuntimeError("packaged companion control v2 contract is unavailable")
    companion_state = companion_definitions.get("CompanionState")
    if not is_json_object(companion_state):
        raise RuntimeError("packaged companion control v2 contract is unavailable")
    public_state: JSONSchema = dict(companion_state)
    public_properties = companion_state.get("properties")
    public_required = companion_state.get("required")
    if not is_json_object(public_properties) or not isinstance(public_required, list):
        raise RuntimeError("packaged companion control v2 contract is unavailable")
    public_state["properties"] = {
        key: value for key, value in public_properties.items() if key != "accountScopeFingerprint"
    }
    public_state["required"] = [
        value for value in public_required if value != "accountScopeFingerprint"
    ]
    definitions = dict(companion_definitions)
    definitions["PublicCompanionState"] = public_state
    definitions["RequiredUpdate"] = {
        "type": "object",
        "additionalProperties": False,
        "required": ["status", "currentVersion", "minimumVersion", "warningVersion"],
        "properties": {
            "status": {"enum": ["none", "warning", "required"]},
            **{
                field: {"type": "string", "maxLength": 128}
                for field in ("currentVersion", "minimumVersion", "warningVersion")
            },
        },
    }
    definitions["UnavailableCompanionState"] = {
        "type": "object",
        "required": [
            "status",
            "canStart",
            "canStop",
            "permissionSource",
            "permissionPresentation",
            "recovery",
        ],
        "additionalProperties": False,
        "properties": {
            "schemaVersion": {"const": 1},
            "status": {"enum": ["checking", "offline"]},
            "meetingId": {"type": "null"},
            "title": {"type": "null"},
            "meetingUrl": {"type": "null"},
            "sessionId": {"type": "null"},
            "startedAt": {"type": "null"},
            "message": {"type": "string", "maxLength": 1024},
            "canStart": {"const": False},
            "canStop": {"const": False},
            "canPause": {"const": False},
            "canResume": {"const": False},
            "permissionSource": {"const": "synthetic-offline"},
            "permissionPresentation": {
                "type": "object",
                "required": ["microphone", "systemAudio"],
                "additionalProperties": False,
                "properties": {
                    "microphone": {"enum": ["unknown", "unsupported"]},
                    "systemAudio": {"enum": ["unknown", "unsupported"]},
                },
            },
            "permissions": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "microphone": {"enum": ["notDetermined", "unknown", "unsupported"]},
                    "systemAudio": {"enum": ["notDetermined", "unknown", "unsupported"]},
                },
            },
            "recording": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "mixedBytes": {"const": 0},
                    "startedAt": {"type": "null"},
                    "lastAudioSavedLocally": {"const": False},
                    "lastAudioBytes": {"const": 0},
                    "lastAudioDurationMs": {"const": 0},
                    "lastRecording": {"type": "null"},
                },
            },
            "recovery": {
                "type": "object",
                "required": ["kind", "installed", "canInstall", "canLaunch"],
                "additionalProperties": False,
                "properties": {
                    "kind": {
                        "enum": [
                            "checking",
                            "not_installed",
                            "launch_required",
                            "quit_required",
                            "update_deferred",
                            "start_retry_required",
                        ]
                    },
                    "installed": {"type": ["boolean", "null"]},
                    "canInstall": {"type": "boolean"},
                    "canLaunch": {"type": "boolean"},
                },
            },
        },
    }
    properties: JSONSchema = {
        "ok": {"type": "boolean"},
        "protocolVersion": {"const": PROTOCOL_VERSION},
        "schemaVersion": {"const": 1},
        "state": {
            "oneOf": [
                {"$ref": "#/$defs/PublicCompanionState"},
                {"$ref": "#/$defs/UnavailableCompanionState"},
            ]
        },
        "availability": {
            "oneOf": [
                {
                    "type": "object",
                    "required": ["status"],
                    "additionalProperties": False,
                    "properties": {"status": {"const": "ready"}},
                },
                {
                    "type": "object",
                    "required": ["status", "stage"],
                    "additionalProperties": False,
                    "properties": {
                        "status": {"const": "loading"},
                        "stage": {"enum": ["launching", "connecting"]},
                    },
                },
                {
                    "type": "object",
                    "required": ["status", "reason"],
                    "additionalProperties": False,
                    "properties": {
                        "status": {"const": "error"},
                        "reason": {
                            "enum": [
                                "connection-failed",
                                "owner-invalid",
                                "companion-unavailable",
                            ]
                        },
                    },
                },
            ]
        },
        "serviceCapacity": {"enum": ["off", "warning", "blocked"]},
        "deviceSupported": {"type": "boolean"},
        "meetingsEligibility": {"$ref": "#/$defs/MeetingsEligibility"},
        "pluginAvailability": {"enum": ["available", "coming_soon"]},
        "pluginAvailabilityState": {"enum": ["checking", "unavailable", "resolved"]},
        "requiredUpdates": {
            "type": "object",
            "additionalProperties": False,
            "required": ["app", "plugin"],
            "properties": {
                target: {"$ref": "#/$defs/RequiredUpdate"} for target in ("app", "plugin", "codex")
            },
        },
        "companionPid": {"type": "integer", "minimum": 1, "maximum": 2_147_483_647},
        "companionVersion": {"type": "string", "minLength": 1, "maxLength": 64},
        "companion": {"type": "object"},
        "stateRevision": {"type": "string"},
        "runtime": {"type": "object"},
        "error": {"type": "string"},
        "code": {"type": "string"},
        "bootstrap": {"type": "object"},
    }
    properties["completion"] = {
        "type": "object",
        "required": ["outcome"],
        "additionalProperties": False,
        "properties": {"outcome": {"const": "saved"}},
    }
    properties["recordingAppInstanceSupported"] = {"type": "boolean"}
    properties["recordingOwner"] = {"type": "string", "pattern": "^[A-Za-z0-9_-]{43}$"}
    properties["recordingCorrelationId"] = {"type": "string", "pattern": "^[0-9a-f]{64}$"}
    properties["stoppedRecordingNote"] = {
        "type": "object",
        "required": ["sessionId", "meetingId"],
        "additionalProperties": False,
        "properties": {
            key: {"type": "string", "pattern": "^[A-Za-z0-9_-]{8,128}$"}
            for key in ("sessionId", "meetingId")
        },
    }
    properties["workspaceRevisions"] = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "calendar": {"type": "integer", "minimum": 1},
            "notes": {"type": "integer", "minimum": 1},
        },
    }
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "ChatGPT Meetings companion recording status v2",
        "type": "object",
        "required": ["ok", "state"],
        "additionalProperties": False,
        "properties": properties,
        "allOf": [
            {
                "if": {"properties": {"ok": {"const": True}}},
                "then": {
                    "required": ["protocolVersion"],
                    "properties": {
                        "state": {"$ref": "#/$defs/PublicCompanionState"},
                        "availability": {"properties": {"status": {"const": "ready"}}},
                    },
                    "not": {"required": ["schemaVersion"]},
                },
                "else": {
                    "properties": {
                        "state": {"$ref": "#/$defs/UnavailableCompanionState"},
                        "availability": {"properties": {"status": {"enum": ["loading", "error"]}}},
                    },
                    "not": {"required": ["protocolVersion"]},
                },
            },
            {
                "if": {"required": ["pluginAvailabilityState"]},
                "then": {
                    "anyOf": [
                        {"required": ["deviceSupported"]},
                        {"required": ["pluginAvailability"]},
                    ],
                    "if": {
                        "properties": {
                            "pluginAvailabilityState": {"enum": ["checking", "unavailable"]}
                        }
                    },
                    "then": {
                        "properties": {
                            "deviceSupported": {"const": False},
                            "pluginAvailability": {"const": "coming_soon"},
                        }
                    },
                },
            },
        ],
        "$defs": definitions,
    }


RECORDING_STATUS_OUTPUT_SCHEMA = _recording_status_output_schema()


def _schema_properties(schema: JSONSchema) -> JSONSchema:
    properties = schema.get("properties")
    if not is_json_object(properties):
        raise RuntimeError("packaged Meetings schema properties are unavailable")
    return properties


def object_schema(
    properties: Mapping[str, JSONValue] | None = None,
    required: Sequence[str] | None = None,
) -> JSONSchema:
    """Build a closed JSON object schema.

    Args:
        properties: Optional property-name to JSON-schema mappings.
        required: Optional names of properties that must be present.

    Returns:
        A JSON schema that rejects undeclared properties.
    """
    schema: JSONSchema = {
        "type": "object",
        "properties": dict(properties or {}),
        "additionalProperties": False,
    }
    if required:
        schema["required"] = list(required)
    return schema


def _analytics_event_schema() -> JSONSchema:
    """Advertise the same bounded event families enforced by analytics ingress."""
    uuid: JSONSchema = {
        "type": "string",
        "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
    }
    variants: list[JSONValue] = []
    for name in PluginEventName:
        properties: JSONSchema = {
            "surface": {"enum": [surface.value for surface in PluginEventSurface]},
            "durationMs": {"type": "integer", "minimum": 0, "maximum": 3_600_000},
        }
        required = ["surface"]
        if name in (
            PluginEventName.ONBOARDING,
            PluginEventName.CALENDAR_CONNECT,
            PluginEventName.RECORDING_START,
            PluginEventName.RECORDING_STOP,
        ):
            properties["attemptId"] = uuid
            required += ["attemptId", "stage"]
            if name == PluginEventName.ONBOARDING:
                properties.update(
                    {
                        "surface": {"const": "onboarding"},
                        "stage": {"enum": ["started", "step_viewed", "completed"]},
                        "step": {"enum": ["calendars", "context", "completion"]},
                    }
                )
                required.append("step")
            elif name == PluginEventName.CALENDAR_CONNECT:
                properties.update(
                    {
                        "stage": {"enum": ["started", "succeeded", "failed"]},
                        "provider": {"enum": ["google", "outlook"]},
                        "failureReason": {"const": "setup_link_failed"},
                    }
                )
                required.append("provider")
            else:
                properties.update(
                    {
                        "stage": {"enum": ["started", "succeeded"]},
                        "recordingMode": {"const": "local"},
                    }
                )
                required.append("recordingMode")
        metadata = object_schema(properties, required)
        if name in (
            PluginEventName.ONBOARDING,
            PluginEventName.CALENDAR_CONNECT,
            PluginEventName.RECORDING_START,
            PluginEventName.RECORDING_STOP,
        ):
            metadata["allOf"] = [
                {
                    "if": {"properties": {"stage": {"const": "started"}}},
                    "then": {"not": {"required": ["durationMs"]}},
                },
                {
                    "if": {"properties": {"stage": {"const": "failed"}}},
                    "then": {"required": ["failureReason"]},
                    "else": {"not": {"required": ["failureReason"]}},
                },
            ]
        variants.append(
            object_schema(
                {
                    "clientEventId": uuid,
                    "eventName": {"const": name.value},
                    "metadata": metadata,
                },
                required=["clientEventId", "eventName", "metadata"],
            )
        )
    return {"oneOf": variants}


CLIENT_CONTEXT_SCHEMA = object_schema(
    {
        "systemName": {"enum": ["Windows", "Darwin", "Linux", "iOS", "Android", "unknown"]},
        "surface": {"enum": ["web", "desktop", "mobile", "unknown"]},
        "codexVersion": {"type": "string", "maxLength": 128},
    },
    ["systemName", "surface"],
)

LOCAL_TITLE_SCHEMA: JSONSchema = {
    "type": "string",
    "minLength": 1,
    "maxLength": 512,
    "pattern": r"^[^\u0000-\u001f\u007f]*$",
}
CALENDAR_RECORDING_CONTEXT_SCHEMA = object_schema(
    {
        "accountScopeGeneration": {"type": "string", "minLength": 1, "maxLength": 256},
        "source": {"const": "google_calendar"},
        "eventId": {"type": "string", "minLength": 1, "maxLength": 512},
        "occurrenceStart": {"type": "string", "format": "date-time", "maxLength": 64},
        "title": LOCAL_TITLE_SCHEMA,
    },
    ["accountScopeGeneration", "source", "eventId", "occurrenceStart", "title"],
)
FORCE_START_RECORDING_SCHEMA = object_schema(
    {
        "confirmed": {"type": "boolean", "enum": [True]},
        "calendarContext": CALENDAR_RECORDING_CONTEXT_SCHEMA,
    },
    ["confirmed"],
)
LOCAL_RECORDING_CONTROL_SCHEMA = object_schema(
    {
        "expectedSessionId": {
            "type": "string",
            "minLength": 8,
            "maxLength": 128,
            "pattern": r"^[A-Za-z0-9_-]+$",
        }
    },
    ["expectedSessionId"],
)
PUBLIC_MEETING_ID_SCHEMA: JSONSchema = {
    "type": "string",
    "minLength": 1,
    "maxLength": 512,
    "pattern": r"^[A-Za-z0-9_-]+$",
}
LOCAL_NOTES_INITIAL_LIMIT_MINIMUM = 1
LOCAL_NOTES_INITIAL_LIMIT_MAXIMUM = 40
LOCAL_NOTES_PAGE_TOKEN_MAXIMUM_BYTES = 128
LOCAL_NOTES_PAGE_TOKEN_PATTERN = re.compile(r"[A-Za-z0-9_-]{32,128}")
LOCAL_NOTES_REFRESH_TRIGGERS = NOTES_REFRESH_TRIGGERS
LOCAL_NOTES_PAGE_REQUEST_SCHEMA = object_schema(
    {
        "section": {
            "type": "string",
            "enum": ["calendar"],
        },
        "initialLimit": {
            "type": "integer",
            "minimum": LOCAL_NOTES_INITIAL_LIMIT_MINIMUM,
            "maximum": LOCAL_NOTES_INITIAL_LIMIT_MAXIMUM,
        },
        "recordingStartedAt": {
            "type": "string",
            "format": "date-time",
            "maxLength": 24,
        },
        "pageToken": {
            "type": "string",
            "minLength": 32,
            "maxLength": LOCAL_NOTES_PAGE_TOKEN_MAXIMUM_BYTES,
            "pattern": r"^[A-Za-z0-9_-]{32,128}$",
        },
    }
)
_LOCAL_NOTES_PAGE_REQUEST_PROPERTIES = _schema_properties(LOCAL_NOTES_PAGE_REQUEST_SCHEMA)
LOCAL_NOTES_PAGE_REQUEST_SCHEMA["allOf"] = [
    {"not": {"required": ["initialLimit", "pageToken"]}},
    {"not": {"required": ["section", "initialLimit"]}},
    {"not": {"required": ["section", "pageToken"]}},
    {"not": {"required": ["recordingStartedAt", "pageToken"]}},
    {"not": {"required": ["recordingStartedAt", "section"]}},
]
LOCAL_UI_NATIVE_REQUEST_TARGETS = {
    "local.forceStart": "meetings.forceStart",
    "local.requestMicrophone": "meetings.requestMicrophone",
    "local.requestSystemAudio": "meetings.requestSystemAudio",
    "local.recheckAudio": "meetings.recheckAudio",
    "local.openMicrophoneSettings": "meetings.openMicrophoneSettings",
    "local.openSystemAudioSettings": "meetings.openSystemAudioSettings",
    "local.installAndLaunch": "meetings.installAndLaunch",
    "local.applyStagedUpdate": "meetings.applyStagedUpdate",
    "local.getSettings": "meetings.getSettings",
    "local.updateSettings": "meetings.updateSettings",
    "prompt.note": "chatgpt_meetings_prepare_note",
}
LOCAL_UI_REQUEST_KINDS = (
    "analytics.track",
    "home.bootstrap",
    "diagnostics.get",
    "notes.list",
    "calendar.list",
    "onboarding.profile",
    "calendar.connections",
    "context.connections",
    "connection.ensure",
    "note.get",
    "note.delete",
    "note.reprocess",
    "note.share",
    "note.shareEligibility",
    "note.feedback",
    "activity.get",
    "activity.view",
    "settings.get",
    "settings.getTarget",
    "settings.update",
    "ui.reportError",
    "ui.submitFeedback",
    "ui.reportPerformance",
    "local.getStagedUpdateStatus",
    "local.getUploads",
    "local.retryUpload",
    *LOCAL_UI_NATIVE_REQUEST_TARGETS,
)
SETTINGS_PATCH_PROPERTIES = {
    "calendarRemindersEnabled": {"type": "boolean"},
    "soundEffectsEnabled": {"type": "boolean"},
    "meetingDetectionEnabled": {"type": "boolean"},
}
LOCAL_UI_GATEWAY_SCHEMA = object_schema(
    {
        "event": _analytics_event_schema(),
        "clientContext": CLIENT_CONTEXT_SCHEMA,
        **_LOCAL_NOTES_PAGE_REQUEST_PROPERTIES,
        "request": {"type": "string", "enum": list(LOCAL_UI_REQUEST_KINDS)},
        "appInstanceId": {
            "type": "string",
            "minLength": 64,
            "maxLength": 64,
            "pattern": "^[a-f0-9]{64}$",
        },
        "ownerScopeGeneration": {
            "type": "string",
            "minLength": 43,
            "maxLength": 43,
            "pattern": "^[A-Za-z0-9_-]{43}$",
        },
        "offset": {"type": "integer", "minimum": 0, "maximum": 9_007_199_254_740_991},
        "recordingId": {
            "type": "string",
            "pattern": "^recording-[a-f0-9]{64}$",
        },
        "startDate": {
            "type": "string",
            "minLength": 10,
            "maxLength": 10,
            "pattern": r"^\d{4}-\d{2}-\d{2}$",
        },
        "endDate": {
            "type": "string",
            "minLength": 10,
            "maxLength": 10,
            "pattern": r"^\d{4}-\d{2}-\d{2}$",
        },
        "refresh": {"type": "boolean"},
        "refreshTrigger": {"type": "string", "enum": list(LOCAL_NOTES_REFRESH_TRIGGERS)},
        "noteId": PUBLIC_MEETING_ID_SCHEMA,
        "email": {"type": "string", "minLength": 3, "maxLength": 320},
        "category": {"type": "string", "enum": sorted(FEEDBACK_CATEGORIES)},
        "feedbackText": {"type": "string", "maxLength": 2_000},
        "feedbackContinuationToken": {
            "type": "string",
            "minLength": 32,
            "maxLength": 128,
            "pattern": "^[A-Za-z0-9_-]+$",
        },
        "includeDebugArtifacts": {"type": "boolean"},
        "stage": {"type": "string", "enum": sorted(MCP_SENTRY_STAGES)},
        "kind": {"type": "string", "enum": sorted(MCP_SENTRY_KINDS)},
        "presentation": {"type": "string", "enum": sorted(MCP_SENTRY_PRESENTATIONS)},
        "operation": {
            "type": "string",
            "enum": sorted(MCP_SENTRY_OPERATIONS | CLIENT_PERFORMANCE_OPERATIONS),
        },
        "transition": {"type": "string", "enum": sorted(CLIENT_PERFORMANCE_TRANSITIONS)},
        "durationMs": {
            "type": "integer",
            "minimum": 0,
            "maximum": MAXIMUM_CLIENT_PERFORMANCE_DURATION_MILLISECONDS,
        },
        "streaming": {"type": "string", "enum": sorted(CLIENT_STREAMING_STATES)},
        "notification": {"type": "string", "enum": sorted(MCP_SENTRY_NOTIFICATIONS)},
        "updateReason": {"type": "string", "enum": sorted(MCP_SENTRY_UPDATE_REASONS)},
        "uiVersion": {
            "type": "string",
            "minLength": 1,
            "maxLength": 80,
            "pattern": "^[A-Za-z0-9][A-Za-z0-9._+-]*$",
        },
        **{setting: {"type": "boolean"} for setting in sorted(GATEWAY_SETTING_NAMES)},
        "meetingId": PUBLIC_MEETING_ID_SCHEMA,
        "title": LOCAL_TITLE_SCHEMA,
        "confirmed": {"type": "boolean"},
        "calendarContext": CALENDAR_RECORDING_CONTEXT_SCHEMA,
        **SETTINGS_PATCH_PROPERTIES,
    }
)
SETTINGS_PATCH_SCHEMA = object_schema(SETTINGS_PATCH_PROPERTIES)


STRUCTURED_SETTINGS_FIELDS: JSONSchema = {
    "autoRecordEnabled": {
        "type": "boolean",
        "title": "Automatically join meetings",
        "description": "Let the meeting bot join your calendar meetings and take notes.",
    },
    "slackNotificationsEnabled": {
        "type": "boolean",
        "title": "Send notes to Slack",
        "description": "Get your meeting notes in Slack when they’re ready.",
    },
    "recordingNotificationsEnabled": {
        "type": "boolean",
        "title": "Meeting reminders",
        "description": "Get a reminder to take notes before a calendar meeting starts.",
    },
    "soundEffectsEnabled": {
        "type": "boolean",
        "title": "Recording sounds",
        "description": "Play a sound when recording starts or stops.",
    },
    "meetingDetectionEnabled": {
        "type": "boolean",
        "title": "Detect meetings",
        "description": "Get a prompt to take notes when you join a call in a supported app.",
    },
}
