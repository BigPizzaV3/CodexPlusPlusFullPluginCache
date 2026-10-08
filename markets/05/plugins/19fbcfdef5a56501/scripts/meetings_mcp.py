#!/usr/bin/env python3
"""Dependency-light MCP App server for Meetings native capture."""

# Helper shards intentionally import this complete, monkeypatchable parent API.
# ruff: noqa: F401

from __future__ import annotations

import argparse
import base64
import copy
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import threading
import time
from collections.abc import Callable, Mapping
from contextvars import copy_context
from dataclasses import dataclass, replace
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Literal, TypedDict
from urllib.parse import unquote, urlparse

import bootstrap_recovery
import meetings_rpc  # noqa: E402
import native_runtime_windows_recovery as windows_recovery
from codex_auth_client import (  # noqa: E402
    CodexAuthCancelled,
    CodexAuthError,
    CodexAuthRequired,
    _active_codex_home,
    _resolve_codex_path,
    close_process_auth,
    get_process_auth_manager,
    warm_process_auth,
)
from companion_client import (  # noqa: E402
    CompanionClient,
    CompanionRecoveryOutcome,
    VerifiedCompanionRelease,
    cached_meetings_policy_client,
    companion_client,
    quit_companion_owner,
    recover_unresponsive_companion,
    require_verified_companion_replacement,
    retained_windows_legacy_control_runtime,
    wait_for_companion_recording_ready,
)
from companion_control_v2 import (  # noqa: E402
    PROTOCOL_VERSION,
    CalendarRecordingContext,
    CompanionState,
    is_companion_state,
    validate_definition,
)
from control_client import (  # noqa: E402
    MAXIMUM_JAVASCRIPT_SAFE_INTEGER,
    SAFE_LAUNCHING_MESSAGE,
    SAFE_LOCAL_REQUEST_FAILED_MESSAGE,  # noqa: F401
    SAFE_QUIT_REQUIRED_MESSAGE,
    SAFE_START_OWNER_CHANGED_MESSAGE,
    SAFE_UPDATE_DEFERRED_MESSAGE,
    SETTINGS_RECONCILIATION_CAPABILITY,
    UPDATE_HANDOFF_RESUMABLE_OUTBOX_CAPABILITY,
    UPDATE_HANDOFF_RESUMABLE_OUTBOX_V2_CAPABILITY,
    ControlClient,
    ControlUnavailable,
    CooperativeHandoffDeclined,
    close_stream_transports,
    disconnected_state,
    force_quit_companion_owner,
    verified_current_stream_owner_without_connection,
)
from control_client import (
    descriptor_may_have_live_owner as control_descriptor_may_have_live_owner,
)
from control_client import (
    descriptor_uses_runtime_image as control_descriptor_uses_runtime_image,
)
from control_client_handoff import (
    authenticated_resumable_queued_owner,
    authenticated_resumable_uploading_owner,
    preverify_compatible_staged_update_source,
    require_verified_staged_update_owner,
)
from control_projection import compatible_existing_owner_state
from meetings_api_client import (  # noqa: E402
    GATEWAY_SETTING_NAMES,
    MAXIMUM_TIMESTAMP_BYTES,
    MEETING_ID_PATTERN,
    SETTING_NAMES,
    PluginClientContext,
    PluginClientPolicy,
    RecordCalendarAuthError,
    RecordCalendarBackendError,
    RecordCalendarCancelled,
    RecordCalendarClient,
    RecordCalendarEvent,
    RecordMeetingInteractionsAuthError,
    RecordMeetingInteractionsBackendError,
    RecordMeetingInteractionsCancelled,
    RecordMeetingInteractionsClient,
    RecordMeetingNote,
    RecordMeetingsAuthError,
    RecordMeetingsBackendError,
    RecordMeetingsCancelled,
    RecordMeetingsClient,
    RecordMeetingsPaginationResetRequired,
    parse_record_meeting_row,
    validate_feedback_gateway_arguments,
)
from meetings_api_client_common import record_account_fingerprint, record_owner_scope_fingerprint
from meetings_app.manager import supports_compatible_idle_windows_owner
from meetings_client_policy import (
    STRUCTURED_SETTINGS_READ_TOOL,
    STRUCTURED_SETTINGS_UPDATE_TOOL,
    NativeMeetingsPolicy,
    project_native_meetings_policy,
)
from meetings_host_context import get_current_codex_version
from meetings_prompt import (
    PROMPT_MEETING_ID_PATTERN,
    InvalidArguments,
    PromptPayload,
    build_note_payload,
    require_prompt_meeting_id,
    require_prompt_title,
    require_string,
)
from meetings_rpc import (  # noqa: E402, F401
    BACKGROUND_RPC_SHUTDOWN_GRACE_SECONDS,
    LOCAL_UI_LIFECYCLE_REQUESTS,
    MAXIMUM_BACKGROUND_LIFECYCLE_RPC_REQUESTS,
    MAXIMUM_BACKGROUND_RPC_REQUESTS,
    MAXIMUM_BUFFERED_RPC_INPUT_FRAMES,
    MAXIMUM_BUFFERED_RPC_OBSERVATIONS,
    MAXIMUM_RPC_LINE_BYTES,
    RPCHandler,
    RPCInputStream,
    RPCMessage,
    RPCOutputStream,
    RPCResponse,
    _background_rpc_lane,
    _BoundedBackgroundRPCDispatcher,
    _is_fenced_stop_rpc,
    _is_terminal_stop_rpc,
    _SerializedRPCWriter,
    _uses_background_rpc_lane,
    _uses_lifecycle_rpc_lane,
    rpc_error,
    rpc_response,
)
from meetings_schema import (  # noqa: E402
    CALENDAR_RECORDING_CONTEXT_SCHEMA,
    CLIENT_CONTEXT_SCHEMA,
    FORCE_START_RECORDING_SCHEMA,
    LOCAL_NOTES_INITIAL_LIMIT_MAXIMUM,
    LOCAL_NOTES_INITIAL_LIMIT_MINIMUM,
    LOCAL_NOTES_PAGE_TOKEN_MAXIMUM_BYTES,
    LOCAL_NOTES_PAGE_TOKEN_PATTERN,
    LOCAL_RECORDING_CONTROL_SCHEMA,
    LOCAL_TITLE_SCHEMA,
    LOCAL_UI_GATEWAY_SCHEMA,
    LOCAL_UI_NATIVE_REQUEST_TARGETS,
    LOCAL_UI_REQUEST_KINDS,
    PUBLIC_MEETING_ID_SCHEMA,
    RECORDING_STATUS_OUTPUT_SCHEMA,
    SETTINGS_PATCH_SCHEMA,
    JSONSchema,
    is_json_object,
    object_schema,
)
from meetings_schema import (
    STRUCTURED_SETTINGS_FIELDS as _STRUCTURED_SETTINGS_FIELDS,
)
from meetings_sentry import (  # noqa: E402
    MCP_SENTRY_KINDS,
    MCP_SENTRY_STAGES,
    plugin_version,
    report_explicit_recovery,
    report_mcp_error,
    report_mcp_ready,
)
from meetings_settings import CompanionSettingsResponseWire
from meetings_tool_context import (
    CLIENT_CONTEXT as _PLUGIN_CLIENT_CONTEXT,
)
from meetings_tool_context import (
    RECORDING_APP_INSTANCE as RECORDING_APP_INSTANCE,
)
from meetings_tool_context import scoped_tool_arguments
from native_runtime import (  # noqa: E402
    GITHUB_RELEASE_COMPONENT,
    PLATFORM_OVERRIDE_ENV,
    ControlCapability,
    NativeRuntimeError,
    NativeRuntimeLaunchPending,
    NativeRuntimeQuitRequired,
    NativeRuntimeUpdateDeferred,
    RuntimeManager,
    configured_e2e_isolation,
    host_platform_key,
    log_native_runtime_event,
    plugin_cache_family_root,
    public_runtime_status,
    require_canonical_plugin_registration,
    runtime_spec_for,
    safe_build_timestamp_utc,
)
from native_runtime import (
    log_native_runtime_event as _log_native_recording_pipeline_event,
)
from native_runtime_manager import PreparedCompanionReplacement
from record_handles import (  # noqa: E402
    CALENDAR_EVENT_ID_REGISTRY,
    PUBLIC_MEETING_ID_PATTERN,
    RecordHandleError,
    public_calendar_event_id,
    public_meeting_id,
)
from runtime_config import (  # noqa: E402
    LOCAL_DEVELOPMENT_MARKETPLACE,
    LOCAL_DEVELOPMENT_PLUGIN,
    RUNTIME_CONFIG,
    TRUSTED_MEETINGS_PLUGIN_PUBLISHERS,
)

from helpers import JSONValue


class _RecordingControlArguments(TypedDict, total=False):
    """App-visible v2 recording arguments; Start is empty and Stop is fenced."""

    expectedSessionId: str


_RecordingAction = Literal["start", "stop", "requestMicrophone", "requestSystemAudio"]

SCRIPT_ROOT = Path(__file__).resolve().parent
PLUGIN_ROOT = SCRIPT_ROOT.parent
# Production runtime packaging stamps this fallback for standalone verification.
# An installed plugin manifest remains authoritative so local content-derived
# plugin versions and the MCP initialize response always agree.
PACKAGED_SERVER_VERSION: str | None = "0.8.77"
SERVER_NAME = RUNTIME_CONFIG.server_name
_server_version = plugin_version(PLUGIN_ROOT) or PACKAGED_SERVER_VERSION
if _server_version is None:
    raise RuntimeError("Meetings plugin version is unavailable")
SERVER_VERSION: str = _server_version
MCP_PROTOCOL_VERSION = "2025-11-25"
# Packaging replaces this sentinel in the copied plugin. Source checkouts and
# legacy packages stay explicitly unstamped instead of inventing a build time
# from a file mtime or the current clock.
SERVER_BUILD_TIMESTAMP_UTC = "2026-10-01T03:15:46Z"
DISPLAY_NAME = "Meetings (Beta)"
WIDGET_URI = "ui://chatgpt-meetings/home.html"
WIDGET_MIME = "text/html;profile=mcp-app"
MEETING_RESOURCE_URI_TEMPLATE = "meetings://meeting/{meetingId}"
NOTE_RESOURCE_URI_TEMPLATE = "meetings://note/{noteId}"
MEETING_RESOURCE_MIME = "application/json"
WIDGET_PATH = PLUGIN_ROOT / "assets" / "meetings-app.html"
SERVER_ICON_SPECS = ((None, "chatgpt-meetings-sidebar.svg"),)
MEETING_RESOURCE_ICON_SPECS = (
    ("light", "meeting-resource-note-light.svg"),
    ("dark", "meeting-resource-note-dark.svg"),
)
SERVER_ICON_MIME_TYPE = "image/svg+xml"
SERVER_ICON_MAXIMUM_BYTES = 16 * 1024
PROFILE_PROTOTYPE = "prototype"
PROFILE_LOCAL_DEV = "local-dev"
PROFILE_PRODUCTION = "production"
DEFAULT_PROFILE = RUNTIME_CONFIG.default_mcp_profile
SUPPORTED_PROFILES = (PROFILE_PROTOTYPE, PROFILE_LOCAL_DEV, PROFILE_PRODUCTION)
APP_UI_PROFILES = frozenset({PROFILE_LOCAL_DEV, PROFILE_PRODUCTION})
APP_TOOL_NAMES = (
    "meetings.open",
    "chatgpt_meetings_get_snapshot",
    "chatgpt_meetings_local_status",
    "chatgpt_meetings_start_local",
    "chatgpt_meetings_stop_local",
    "chatgpt_meetings_take_notes",
)
MEETING_MENTIONS_TOOL = "meetings.search_mentions"
MEETING_MENTION_CATALOG_LIMIT = 25
APP_TOOL_NAME_SET = frozenset(
    (
        *APP_TOOL_NAMES,
        STRUCTURED_SETTINGS_READ_TOOL,
        STRUCTURED_SETTINGS_UPDATE_TOOL,
        MEETING_MENTIONS_TOOL,
    )
)
APP_TOOL_TARGETS = {
    "meetings.open": "chatgpt_meetings_open",
    "chatgpt_meetings_get_snapshot": "chatgpt_meetings_get_snapshot",
    "chatgpt_meetings_local_status": "meetings.status",
    "chatgpt_meetings_start_local": "meetings.start",
    "chatgpt_meetings_stop_local": "meetings.stop",
    "chatgpt_meetings_take_notes": "meetings.takeNotes",
}
# Non-terminal capture mutations can legitimately wait on a bounded native
# lease, update check, or operating-system prompt. Keep that work off the
# status and Stop lanes so both remain responsive.
SAFE_OPENING_MESSAGE = "Checking Meetings local capture…"
SETTINGS_SAVING_MESSAGE = "Saving settings…"
SETTINGS_RECONCILING_MESSAGE = "Settings saved; finishing local cleanup."
STATE_REVISION_PREFIX = "state-v1-"

_INITIALIZE_BOOTSTRAP_LOCK = bootstrap_recovery.lock
_FORCE_START_LOCK = threading.Lock()
_FORCE_UPGRADE_LOCK = threading.Lock()
_STAGED_PLUGIN_NAME = RUNTIME_CONFIG.plugin_name
_PLUGIN_MANIFEST_RELATIVE_PATH = Path(".codex-plugin/plugin.json")
_PLUGIN_VERSION_PATTERN = re.compile(
    r"(0|[1-9][0-9]{0,8})\.(0|[1-9][0-9]{0,8})\.(0|[1-9][0-9]{0,8})\Z"
)
_LOCAL_PLUGIN_VERSION_PATTERN = re.compile(
    r"(?P<core>(?:0|[1-9][0-9]{0,8})\.(?:0|[1-9][0-9]{0,8})"
    r"\.(?:0|[1-9][0-9]{0,8}))-local\.[a-f0-9]{32}\Z"
)
_MAXIMUM_PLUGIN_MANIFEST_BYTES = 64 * 1024
_MAXIMUM_CODEX_PLUGIN_RESULT_BYTES = 64 * 1024
_INITIALIZE_BOOTSTRAP_ATTEMPTED = False
# Bootstrap and retries stay off the request lane and remain bounded.
_INITIALIZE_BOOTSTRAP_MAX_LAUNCH_ATTEMPTS = 2
_INITIALIZE_BOOTSTRAP_RETRY_DELAY_SECONDS = 0.10
_INITIALIZE_BOOTSTRAP_CONNECT_POLLS = 8
_INITIALIZE_BOOTSTRAP_CONNECT_POLL_SECONDS = 0.10
_EXPLICIT_ACTION_DESCRIPTOR_WAIT_SECONDS = 12.0
_EXPLICIT_ACTION_DESCRIPTOR_POLL_SECONDS = 0.10
_EXPLICIT_ACTION_READY_WAIT_SECONDS = 12.0
_EXPLICIT_ACTIONS_REQUIRING_CURRENT_IMAGE = frozenset(
    {
        "requestMicrophone",
        "requestSystemAudio",
        "start",
    }
)
_TERMINAL_CONTROL_ACTIONS = frozenset({"stop"})
# A short cooldown prevents duplicate opens while descriptor publication settles.
_INITIALIZE_BOOTSTRAP_ACCEPTED_LAUNCH_COOLDOWN_SECONDS = 5.0
_INITIALIZE_BOOTSTRAP_MAX_RETRY_COOLDOWN_SECONDS = 60.0
_INITIALIZE_BOOTSTRAP_IN_FLIGHT_UNTIL_MONOTONIC = 0.0
_INITIALIZE_BOOTSTRAP_REPLACING_OWNER = False
_INITIALIZE_BOOTSTRAP_PENDING_REARM = False
_INITIALIZE_BOOTSTRAP_SUPPRESS_REARM = False
_INITIALIZE_BOOTSTRAP_EXPLICIT_RECOVERY_REQUESTED = False
_INITIALIZE_BOOTSTRAP_COOLDOWN_WAKE_SCHEDULED = False
# One quiet retry lets an authenticated busy owner finish before updating.
_INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_RETRY_SECONDS = 30.0
_INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_MAX_RETRY_SECONDS = 60.0
_INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_WORKER_SCHEDULED = False
_INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_REQUESTED = False
_INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_WAKE = threading.Event()


def server_build_timestamp_utc() -> str | None:
    return safe_build_timestamp_utc(SERVER_BUILD_TIMESTAMP_UTC)


class MeetingResourceReadError(RuntimeError):
    """One meeting resource could not be read through its authenticated handle."""


@dataclass(frozen=True)
class _ToolAnnotations:
    read_only: bool
    idempotent: bool
    open_world: bool

    def _to_wire(self) -> JSONSchema:
        return {
            "readOnlyHint": self.read_only,
            "destructiveHint": False,
            "idempotentHint": self.idempotent,
            "openWorldHint": self.open_world,
        }


@dataclass(frozen=True)
class _ToolDefinition:
    name: str
    title: str
    description: str
    input_schema: JSONSchema
    annotations: _ToolAnnotations
    meta: JSONSchema | None = None
    output_schema: JSONSchema | None = None
    icons: list[JSONSchema] | None = None

    def _to_wire(self) -> JSONSchema:
        definition: JSONSchema = {
            "name": self.name,
            "title": self.title,
            "description": self.description,
            "inputSchema": self.input_schema,
            "annotations": self.annotations._to_wire(),
            "execution": {"taskSupport": "forbidden"},
        }
        if self.meta is not None:
            definition["_meta"] = self.meta
        if self.output_schema is not None:
            definition["outputSchema"] = self.output_schema
        if self.icons is not None:
            definition["icons"] = self.icons
        return definition


def _tool(
    name: str,
    title: str,
    description: str,
    *,
    read_only: bool,
    meta: JSONSchema | None = None,
    input_schema: JSONSchema | None = None,
    output_schema: JSONSchema | None = None,
    icons: list[JSONSchema] | None = None,
    idempotent: bool | None = None,
    open_world: bool = False,
) -> _ToolDefinition:
    return _ToolDefinition(
        name=name,
        title=title,
        description=description,
        input_schema=input_schema if input_schema is not None else object_schema(),
        annotations=_ToolAnnotations(
            read_only=read_only,
            idempotent=read_only if idempotent is None else idempotent,
            open_world=open_world,
        ),
        meta=meta,
        output_schema=output_schema,
        icons=icons,
    )


def _app_only_tool(
    name: str,
    title: str,
    description: str,
    *,
    input_schema: JSONSchema | None = None,
    idempotent: bool | None = None,
    open_world: bool = False,
) -> _ToolDefinition:
    return _tool(
        name,
        title,
        description,
        read_only=False,
        meta=_app_only_meta(),
        input_schema=input_schema,
        idempotent=idempotent,
        open_world=open_world,
    )


def tool_definitions(
    profile: str = DEFAULT_PROFILE,
) -> list[JSONSchema]:
    """Return the exact tool contract for one supported MCP profile.

    Args:
        profile: Prototype, local-development, or production tool-profile name.

    Returns:
        JSON-compatible MCP tool definitions in their configured order.
    """

    if profile not in SUPPORTED_PROFILES:
        raise ValueError(f"unknown MCP profile: {profile}")
    local_bundle = (PLUGIN_ROOT / ".codex-plugin/local-bundle.json").is_file()
    sidebar_title = (
        "Meetings (Dev)" if profile == PROFILE_LOCAL_DEV or local_bundle else DISPLAY_NAME
    )
    definitions = [
        _tool(
            "chatgpt_meetings_open",
            sidebar_title,
            (
                "Open the Meetings workspace with upcoming meetings, "
                "recent notes, and local recording controls."
            ),
            read_only=True,
            icons=_server_icons(),
            meta=_widget_meta(
                global_entrypoint=True,
                sidebar_take_notes_enabled=(
                    get_record_interactions_client().discovery_rollout().sidebar_take_notes
                ),
                quick_action_tool=(
                    "meetings.takeNotes"
                    if profile == PROFILE_PROTOTYPE
                    else "chatgpt_meetings_take_notes"
                ),
            ),
        ),
        _tool(
            "chatgpt_meetings_get_snapshot",
            "Get the current meetings view",
            (
                "Refresh the Meetings UI. The production app reads "
                "Calendar and recent notes directly from the authenticated "
                "ChatGPT backend."
            ),
            read_only=True,
            meta=_app_only_meta(),
            input_schema=(
                LOCAL_UI_GATEWAY_SCHEMA if profile in APP_UI_PROFILES else object_schema()
            ),
            open_world=profile in APP_UI_PROFILES,
        ),
        _tool(
            "chatgpt_meetings_prepare_note",
            "Prepare meeting-note retrieval",
            "Create the source-grounded Codex request used when a user opens a meeting note.",
            read_only=True,
            meta=_app_only_meta(),
            input_schema=object_schema(
                {
                    "meetingId": PUBLIC_MEETING_ID_SCHEMA,
                    "title": LOCAL_TITLE_SCHEMA,
                },
                ["meetingId", "title"],
            ),
        ),
        _tool(
            "meetings.status",
            "Get Meetings status",
            "Read safe local runtime, permission, and recording status.",
            read_only=True,
            meta=_widget_meta(),
            output_schema=RECORDING_STATUS_OUTPUT_SCHEMA,
        ),
        _tool(
            "meetings.getSettings",
            "Get Meetings settings",
            "Read signed, path-free settings from the local native companion.",
            read_only=True,
            meta=_app_only_meta(),
        ),
        _app_only_tool(
            "meetings.updateSettings",
            "Update Meetings settings",
            (
                "App-only user gesture: update bounded background, calendar "
                "reminder and sound-effect preferences."
            ),
            input_schema=SETTINGS_PATCH_SCHEMA,
            idempotent=True,
        ),
        _app_only_tool(
            "meetings.installAndLaunch",
            "Install and launch Meetings",
            "App-only user gesture: verify and start the plugin-bundled native companion.",
        ),
        _app_only_tool(
            "meetings.applyStagedUpdate",
            "Update Meetings",
            (
                "App-only user gesture: install the available Internal Testing "
                "plugin only while authenticated recording is idle, then cooperatively "
                "replace the verified native owner and relaunch it."
            ),
            input_schema=FORCE_START_RECORDING_SCHEMA,
        ),
        _app_only_tool(
            "meetings.requestMicrophone",
            "Enable microphone",
            "App-only user gesture: ask the operating system for microphone access.",
        ),
        _app_only_tool(
            "meetings.requestSystemAudio",
            "Enable system audio",
            "App-only user gesture: ask the operating system for system audio access.",
        ),
        _app_only_tool(
            "meetings.start",
            "Start recording",
            "App-only user gesture: start local microphone and system audio capture.",
        ),
        _app_only_tool(
            "meetings.takeNotes",
            "Take notes",
            "App-only sidebar gesture: request capture permissions if needed and start note taking once.",
        ),
        _app_only_tool(
            "meetings.forceStart",
            "Force start recording",
            (
                "App-only, user-confirmed Force start recovery after a failed "
                "Start: restart only an authenticated, safely idle Meetings "
                "companion and preserve active, paused, stopping, finalizing, "
                "or unfinished recording. Queued or in-flight durable uploads "
                "never block this explicit action. Start one new local "
                "recording exactly once."
            ),
            input_schema=FORCE_START_RECORDING_SCHEMA,
        ),
        _app_only_tool(
            "meetings.stop",
            "Stop recording",
            "App-only user gesture: stop and durably finalize local capture.",
            input_schema=LOCAL_RECORDING_CONTROL_SCHEMA,
        ),
    ]
    if profile == PROFILE_PROTOTYPE:
        # Destructive recovery is available only in the installed production runtime.
        return [
            definition._to_wire()
            for definition in definitions
            if definition.name not in {"meetings.applyStagedUpdate", "meetings.forceStart"}
        ]

    definitions_by_name: dict[str, _ToolDefinition] = {
        definition.name: definition for definition in definitions
    }
    app_definitions: list[_ToolDefinition] = []
    for app_name in APP_TOOL_NAMES:
        definition = definitions_by_name[APP_TOOL_TARGETS[app_name]]
        definition = replace(definition, name=app_name)
        if app_name == "meetings.open":
            definition = replace(
                definition,
                title=sidebar_title,
                annotations=replace(
                    definition.annotations,
                    read_only=False,
                    idempotent=True,
                ),
            )
        elif app_name == "chatgpt_meetings_local_status":
            definition = replace(
                definition,
                title="Get local recording status",
                meta=_app_only_meta(),
                annotations=replace(definition.annotations, read_only=True),
                input_schema=object_schema(
                    {
                        "clientContext": CLIENT_CONTEXT_SCHEMA,
                        "appInstanceId": {"type": "string", "pattern": "^[a-f0-9]{64}$"},
                    }
                ),
            )
        elif app_name == "chatgpt_meetings_get_snapshot":
            definition = replace(
                definition,
                title="Use the Meetings workspace",
                description=("App-only gateway for bounded Meetings UI reads and explicit writes."),
                annotations=replace(
                    definition.annotations,
                    read_only=False,
                    idempotent=False,
                ),
            )
        elif app_name == "chatgpt_meetings_start_local":
            definition = replace(
                definition,
                title="Start local recording",
                description=(
                    "App-only user gesture: start native microphone and system audio "
                    "capture without dispatching a meeting bot."
                ),
                input_schema=object_schema(
                    {
                        "clientContext": CLIENT_CONTEXT_SCHEMA,
                        "calendarContext": CALENDAR_RECORDING_CONTEXT_SCHEMA,
                    }
                ),
            )
        elif app_name == "chatgpt_meetings_stop_local":
            definition = replace(
                definition,
                title="Stop local recording",
                input_schema=LOCAL_RECORDING_CONTROL_SCHEMA,
            )
        app_definitions.append(definition)
    if (
        profile in APP_UI_PROFILES
        and tuple(definition.name for definition in app_definitions) != RUNTIME_CONFIG.tool_names
    ):
        raise RuntimeError("Meetings app tool contract does not match runtime config")
    if profile in APP_UI_PROFILES:
        app_definitions.extend(
            [
                _tool(
                    STRUCTURED_SETTINGS_READ_TOOL,
                    "Read Meetings preferences",
                    "Read the saved Meetings preferences for the desktop settings panel.",
                    read_only=True,
                    input_schema=object_schema({"clientContext": CLIENT_CONTEXT_SCHEMA}),
                    meta={
                        **_widget_meta(),
                        # Codex resolves plugin links through UI entrypoints, then prefers
                        # the native settings capability for this same server/read tool.
                        "openai/ui": {"entrypoints": [{"type": "settings"}]},
                        # Older Codex discovers settings on this tool, before capabilities.
                        "openai/settings": {"updateTool": STRUCTURED_SETTINGS_UPDATE_TOOL},
                    },
                    output_schema=object_schema(
                        {
                            "schema": {"type": "object"},
                            "values": {"type": "object"},
                            "layout": {"type": "array", "items": {"type": "object"}},
                        },
                        ["schema", "values"],
                    ),
                ),
                _tool(
                    STRUCTURED_SETTINGS_UPDATE_TOOL,
                    "Update Meetings preferences",
                    "Save selected Meetings preferences from the desktop settings panel.",
                    read_only=False,
                    idempotent=True,
                    meta=_app_only_meta(),
                    input_schema=object_schema(
                        {
                            "clientContext": CLIENT_CONTEXT_SCHEMA,
                            "set": {
                                "type": "object",
                                "properties": _STRUCTURED_SETTINGS_FIELDS,
                                "additionalProperties": False,
                                "minProperties": 1,
                            },
                        },
                        ["set"],
                    ),
                    output_schema=object_schema({"values": {"type": "object"}}, ["values"]),
                ),
            ]
        )
        if get_record_interactions_client().discovery_rollout().search_mentions:
            app_definitions.append(
                _tool(
                    MEETING_MENTIONS_TOOL,
                    "Meetings",
                    "Pick a recent meeting note, or search recent notes by title.",
                    read_only=True,
                    meta={
                        **_app_only_meta(),
                        "openai/extensions": {"mentions/search": {"preload": True}},
                    },
                    input_schema=object_schema(
                        {
                            "query": {"type": "string", "maxLength": 256},
                            "preload": {"type": "boolean"},
                            "path": {"description": "Ignored legacy mention-navigation field."},
                        },
                        ["query"],
                    ),
                )
            )
    return [definition._to_wire() for definition in app_definitions]


from meetings_mcp_projection import (
    CalendarSectionWire,
    LegacySnapshotGatewayRequest,
    NotesRecordingArguments,
    NotesSectionWire,
    PrivateMeetingsResponse,
    _private_snapshot_response,
    empty_notes_view,
    meeting_resource_templates,
    normalize_local_notes_page_arguments,
    normalize_local_recording_control,
    normalize_local_ui_gateway_request,
    normalize_record_settings_update,
    normalize_settings_patch,
    private_meetings_tool_result,
    project_calendar_view,
    project_meetings_page,
    read_backend_calendar_view,
    read_backend_meetings_view,
    read_private_meetings_response,
    require_empty_arguments,
    require_tool_arguments,
    resource_contents,
    server_info,
)
from meetings_mcp_projection import (
    app_only_meta as _app_only_meta,
)
from meetings_mcp_projection import (
    asset_icons as _asset_icons,
)
from meetings_mcp_projection import (
    meeting_resource_icons as _meeting_resource_icons,
)
from meetings_mcp_projection import (
    read_server_icon as _read_server_icon,
)
from meetings_mcp_projection import (
    record_id_from_resource_uri as _record_id_from_resource_uri,
)
from meetings_mcp_projection import (
    server_icons as _server_icons,
)
from meetings_mcp_projection import (
    widget_meta as _widget_meta,
)


class _PrivateLegacySnapshot(dict[str, object]):
    """Preserve legacy direct reads while keeping their RPC result component-only."""

    __slots__ = ("response",)

    def __init__(
        self,
        request: str,
        payload: NotesSectionWire | CalendarSectionWire,
    ) -> None:
        super().__init__(payload)
        self.response = _private_snapshot_response(request, payload)


class _TakeNotesResult(dict[str, JSONValue]):
    """Bounded sidebar feedback, rendered by the host's quick-action toast."""

    def __init__(self, ok: bool, message: str, *, loading: bool = False) -> None:
        super().__init__(ok=ok, message=message)
        self.message = message
        self.loading = loading
        if loading:
            self["bootstrap"] = {"status": "loading"}


def _take_notes_loading() -> _TakeNotesResult:
    return _TakeNotesResult(
        False, "Meetings is getting ready. Click Take notes again when it’s ready.", loading=True
    )


def _take_notes_unavailable(
    state: CompanionState | None = None, *, client: CompanionClient | None = None
) -> _TakeNotesResult:
    if client is not None and client.bootstrap_recovery_pending() is True:
        return _take_notes_loading()
    if state is not None:
        recording = state["recording"]
        if recording["phase"] in {"starting", "recording", "stopping"}:
            return _TakeNotesResult(False, "Note taking already in progress.")
        for permission, label in (("microphone", "microphone"), ("systemAudio", "system audio")):
            if recording["permissions"][permission]["status"] == "denied":
                return _TakeNotesResult(
                    False,
                    f"Allow {label} access for ChatGPT Meetings in system settings, "
                    "then click Take notes again.",
                )
    return _TakeNotesResult(False, "Couldn’t start note taking. Open Meetings and try again.")


def _prepare_sidebar_take_notes(
    client: CompanionClient,
    state: CompanionState,
    *,
    cancellation_event: threading.Event | None,
    runtime: Mapping[str, object],
) -> CompanionState | _TakeNotesResult:
    if client.bootstrap_recovery_pending() is True:
        return _take_notes_loading()
    if (
        cancellation_event is not None and cancellation_event.is_set()
    ) or _recording_policy_blocks_start(runtime):
        return _take_notes_unavailable()
    recording = state["recording"]
    notice = recording["notice"]
    action = notice["action"] if notice is not None else None
    if action is not None and action["kind"] == "recheck-audio":
        _recheck_audio(client, runtime=runtime, cancellation_event=cancellation_event)
        return _take_notes_after_audio_refresh(client.latest_state())
    if (
        recording["phase"] == "idle"
        and not recording["controls"]["start"]["enabled"]
        and recording["controls"]["start"]["disabledReason"] == "permission-denied"
        and state["lifecycle"]["replacement"]["allowed"]
        and action is not None
        and action["kind"] == "open-system-settings"
        and recording["permissions"][action["permission"]]["status"] == "denied"
    ):
        # Only an already-denied permission at click time opens settings. A new
        # denial during this click's OS prompts returns guidance without opening
        # another surface. Keep this action on the same authenticated owner.
        client.call(
            "permissions.openSystemSettings",
            {"kind": action["permission"]},
            cancellation_event=cancellation_event,
        )
        return _take_notes_after_audio_refresh(client.latest_state())
    # Stay on this authenticated owner through every OS prompt. Never resolve a
    # replacement client or replay Start when a prompt returns or is cancelled.
    requested: set[str] = set()
    for legacy_permission in ("microphone", "systemAudio"):
        if (
            cancellation_event is not None and cancellation_event.is_set()
        ) or _recording_policy_blocks_start(runtime):
            return _take_notes_unavailable()
        recording = state["recording"]
        if recording["phase"] != "idle":
            return _take_notes_unavailable(state)
        if recording["controls"]["start"]["enabled"]:
            return state
        if (
            recording["controls"]["start"]["disabledReason"] != "permission-required"
            or not state["lifecycle"]["replacement"]["allowed"]
        ):
            return _take_notes_unavailable(state)
        permission = legacy_permission
        if "audioSources" in recording:
            notice = recording["notice"]
            action = notice["action"] if notice is not None else None
            if (
                "recording.audio-sources.v1" not in client.negotiated_capabilities
                or action is None
                or action["kind"] != "request-permission"
            ):
                return _take_notes_unavailable(state)
            permission = action["permission"]
            if (
                permission in requested
                or recording["permissions"][permission]["status"] != "promptable"
                or not recording["permissions"][permission]["canRequest"]
            ):
                return _take_notes_unavailable(state)
        elif any(
            value["status"] not in {"granted", "promptable"}
            for value in (
                recording["permissions"]["microphone"],
                recording["permissions"]["systemAudio"],
            )
        ):
            return _take_notes_unavailable(state)
        if not recording["permissions"][permission]["canRequest"]:
            continue
        requested.add(permission)
        client.call(
            "permissions.request",
            {"kind": permission},
            timeout_seconds=180.0,
            cancellation_event=cancellation_event,
        )
        state = client.get_state(cancellation_event=cancellation_event)
    if not state["recording"]["controls"]["start"]["enabled"]:
        return _take_notes_unavailable(state)
    return state


def _take_notes_after_audio_refresh(state: CompanionState | None) -> _TakeNotesResult:
    if state is not None and state["recording"]["controls"]["start"]["enabled"]:
        return _TakeNotesResult(True, "Audio is ready. Click Take notes to start.")
    if state is not None:
        notice = state["recording"]["notice"]
        if notice is not None and notice["kind"] == "recording-unavailable":
            return _TakeNotesResult(False, notice["message"])
    return _take_notes_unavailable(state)


def _recheck_audio(
    client: CompanionClient,
    *,
    runtime: Mapping[str, object],
    cancellation_event: threading.Event | None,
) -> None:
    def revalidate_request() -> None:
        verified_release = client.public_status().get("_verifiedReleaseVersion")
        policy_runtime = (
            {**runtime, "releaseVersion": verified_release}
            if isinstance(verified_release, VerifiedCompanionRelease)
            else runtime
        )
        if (
            cancellation_event is not None and cancellation_event.is_set()
        ) or _recording_policy_blocks_start(policy_runtime):
            raise ControlUnavailable("native audio recheck is unavailable")

    client.recheck_audio(
        cancellation_event=cancellation_event, revalidate_request=revalidate_request
    )


def take_notes() -> _TakeNotesResult:
    try:
        result = call_action("start", sidebar_take_notes=True)
    except (ControlUnavailable, NativeRuntimeError):
        return _take_notes_unavailable()
    return result if isinstance(result, _TakeNotesResult) else _take_notes_unavailable()


_RECORD_MEETINGS_CLIENT_LOCK = threading.Lock()
_RECORD_MEETINGS_CLIENT: RecordMeetingsClient | None = None
_RECORD_CALENDAR_CLIENT_LOCK = threading.Lock()
_RECORD_CALENDAR_CLIENT: RecordCalendarClient | None = None
_RECORD_INTERACTIONS_CLIENT_LOCK = threading.Lock()
_RECORD_INTERACTIONS_CLIENT: RecordMeetingInteractionsClient | None = None


def get_record_meetings_client() -> RecordMeetingsClient:
    """Return the process-wide Record meetings-list client.

    Returns:
        The lazily initialized meetings-list client.
    """

    global _RECORD_MEETINGS_CLIENT
    with _RECORD_MEETINGS_CLIENT_LOCK:
        if _RECORD_MEETINGS_CLIENT is None:
            _RECORD_MEETINGS_CLIENT = RecordMeetingsClient(get_process_auth_manager())
        return _RECORD_MEETINGS_CLIENT


def get_record_calendar_client() -> RecordCalendarClient:
    """Return the process-wide Record Calendar client.

    Returns:
        The lazily initialized Calendar client.
    """

    global _RECORD_CALENDAR_CLIENT
    with _RECORD_CALENDAR_CLIENT_LOCK:
        if _RECORD_CALENDAR_CLIENT is None:
            _RECORD_CALENDAR_CLIENT = RecordCalendarClient(get_process_auth_manager())
        return _RECORD_CALENDAR_CLIENT


def get_record_interactions_client() -> RecordMeetingInteractionsClient:
    """Return the process-wide Record interactions client.

    Returns:
        The lazily initialized note-interactions client.
    """

    global _RECORD_INTERACTIONS_CLIENT
    with _RECORD_INTERACTIONS_CLIENT_LOCK:
        if _RECORD_INTERACTIONS_CLIENT is None:
            _RECORD_INTERACTIONS_CLIENT = RecordMeetingInteractionsClient(
                get_process_auth_manager(),
                native_policy_owner_available=lambda context: (
                    _native_policy_owner_for_context(context) is not None
                ),
            )
        return _RECORD_INTERACTIONS_CLIENT


from meetings_mcp_lifecycle import (
    _best_effort_launch_bundled_companion,
    _bootstrap_control_is_connected,
    _bootstrap_current_stream_owner_without_connection,
    _bootstrap_failure_diagnostics,
    _control_descriptor_hint_exists,
    _run_initialize_companion_bootstrap,
    _run_initialize_companion_bootstrap_cooldown_wake,
    _run_initialize_companion_deferred_update,
    _schedule_initialize_companion_deferred_update,
    _start_initialize_bootstrap_daemon,
    _start_initialize_bootstrap_daemon_best_effort,
    calendar_account_scope_generation,
    schedule_initialize_companion_bootstrap,
    settings_tool_payload,
    structured_settings_payload,
)
from meetings_mcp_lifecycle import (
    wake_initialize_companion_deferred_update as _wake_initialize_companion_deferred_update,
)


def with_runtime(
    payload: Mapping[str, object],
    *,
    runtime: Mapping[str, object] | None = None,
) -> JSONSchema:
    """Attach one request-local runtime proof without a second deep probe.

    Args:
        payload: Native or MCP-owned status fields to expose.
        runtime: Optional already-verified runtime facts.

    Returns:
        A path-free, recursively JSON-safe status envelope.

    Raises:
        ValueError: If application-produced status is not JSON-safe.
    """

    resolved_runtime = runtime if runtime is not None else RuntimeManager().status()
    result: dict[str, object] = dict(payload)
    verified_owner_release = result.pop("_verifiedReleaseVersion", None)
    # RuntimeManager needs private absolute paths for verification/launch, but
    # neither the model nor webview needs them after that proof completes.
    result["runtime"] = public_runtime_status(resolved_runtime)
    native_policy = _current_native_meetings_policy()
    policy = _current_plugin_client_policy(
        local_fallback=native_policy is not None, observe_native=False
    )
    fallback_context = _fallback_policy_context() if native_policy is None else None
    result["serviceCapacity"] = policy.service_capacity
    if _fallback_policy_context() is not None or native_policy is not None:
        result["deviceSupported"] = policy.device_supported
        # Compatibility for UI bundles opened before the boolean contract shipped.
        result["pluginAvailability"] = "available" if policy.device_supported else "coming_soon"
        result["pluginAvailabilityState"] = policy.availability_state
    if native_policy is not None:
        result["meetingsEligibility"] = native_policy.observation
        result["requiredUpdates"] = native_policy.required_updates
    else:
        result["requiredUpdates"] = get_record_interactions_client().peek_required_updates(
            plugin_version=SERVER_VERSION,
            app_version=(
                verified_owner_release
                if isinstance(verified_owner_release, VerifiedCompanionRelease)
                else resolved_runtime.get("releaseVersion")
            ),
            client_context=fallback_context,
        )
    result["companion"] = {
        "displayName": DISPLAY_NAME,
        "buildTimestamp": server_build_timestamp_utc(),
        "protocolVersion": PROTOCOL_VERSION,
    }
    if not is_json_object(result):
        raise ValueError("recording status is not a JSON object")
    result["stateRevision"] = semantic_state_revision(result)
    return result


def runtime_recovery_payload(
    runtime: Mapping[str, object] | None,
    recovery_kind: str,
    safe_message: str,
) -> JSONSchema:
    """Build one fixed recovery response with public runtime evidence.

    Args:
        runtime: Optional already-verified runtime facts.
        recovery_kind: Bounded recovery classification.
        safe_message: User-presentable recovery copy.

    Returns:
        A path-free, recursively JSON-safe recovery envelope.
    """

    return with_runtime(
        disconnected_state(
            safe_message=safe_message,
            recovery_kind=recovery_kind,
            runtime=runtime,
        ),
        runtime=runtime,
    )


def semantic_state_revision(payload: Mapping[str, object]) -> str:
    """Return a stable, path-free cursor for user-visible local state.

    Args:
        payload: Candidate public recording status.

    Returns:
        A content-derived revision that ignores high-frequency audio meters.

    Raises:
        ValueError: If the candidate status is not recursively JSON-safe.
    """

    if not is_json_object(payload):
        raise ValueError("recording status is not a JSON object")
    material = copy.deepcopy(payload)
    material.pop("stateRevision", None)
    state = material.get("state")
    if isinstance(state, dict):
        recording = state.get("recording")
        if isinstance(recording, dict):
            recording.pop("activityLevel", None)
            recording.pop("mixedBytes", None)
    encoded = json.dumps(
        material,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
        allow_nan=False,
    ).encode("utf-8")
    return STATE_REVISION_PREFIX + hashlib.sha256(encoded).hexdigest()


def opening_shell_payload() -> JSONSchema:
    """Return a fixed non-authorizing first-paint shape.

    Opening the MCP app is not a signed native status request. Omitting runtime
    facts is intentional: treating an unknown install state as false would
    turn ordinary cold boot into a bogus setup prompt. The widget's static
    shell and its deferred status lane can show progress immediately while
    this payload makes no permission or Start claim.

    Returns:
        A fixed JSON-safe status shell carrying no runtime authority.
    """

    return {
        "state": {
            "status": "offline",
            "message": SAFE_OPENING_MESSAGE,
            "canStart": False,
            "canStop": False,
            "canPause": False,
            "canResume": False,
            "permissionSource": "synthetic-offline",
            "permissionPresentation": {
                "microphone": "unknown",
                "systemAudio": "unknown",
            },
            "permissions": {},
            "recovery": {
                "kind": "checking",
                "installed": None,
                "canInstall": False,
                "canLaunch": False,
            },
        },
        "companion": {
            "displayName": DISPLAY_NAME,
            "buildTimestamp": server_build_timestamp_utc(),
            "protocolVersion": PROTOCOL_VERSION,
        },
    }


def _native_runtime_host_is_unsupported() -> bool:
    """Recognize only hosts without a native adapter or an explicit test override."""

    return host_platform_key() is None and not os.environ.get(PLATFORM_OVERRIDE_ENV, "").strip()


def _unsupported_native_runtime_status() -> JSONSchema:
    """Keep unsupported-host recording inert without blocking hosted Meetings data."""

    runtime: dict[str, object] = {"installed": False, "capabilities": []}
    payload = disconnected_state(runtime=runtime)
    payload["availability"] = {
        "status": "error",
        "reason": "companion-unavailable",
    }
    state = payload["state"]
    assert isinstance(state, dict)
    unsupported_permissions = {
        "microphone": "unsupported",
        "systemAudio": "unsupported",
    }
    state.update(
        {
            "message": "Local recording is not supported on this device.",
            "permissionPresentation": unsupported_permissions,
            "permissions": dict(unsupported_permissions),
            "recovery": {
                "kind": "not_installed",
                "installed": False,
                "canInstall": False,
                "canLaunch": False,
            },
        }
    )
    return with_runtime(payload, runtime=runtime)


def _bootstrap_loading_status_payload(
    stage: Literal["launching", "connecting"] = "launching",
) -> JSONSchema:
    """Return a bounded status hint with no install or Start authority.

    Bootstrap owns the fresh launch proof both before descriptor publication
    and while its verified owner finishes connecting. Returning the same fixed
    loading shell used by widget open keeps status responsive without inventing
    runtime, permission, auth, or Start facts while that proof is in flight.
    """

    payload = opening_shell_payload()
    payload["ok"] = False
    # This fixed marker is intentionally outside native state: it is not a
    # signed claim and carries no runtime/install/auth/permission authority.
    # The webview uses it only to keep bounded Checking chrome visible.
    payload["bootstrap"] = {"status": "loading"}
    payload["availability"] = {"status": "loading", "stage": stage}
    return payload


def _should_return_bootstrap_loading_status() -> bool:
    """Use the loader only before a descriptor exists and before expiry.

    Descriptor presence is deliberately checked first and conservatively:
    unreadable or ambiguous entries take the canonical signed-status path.
    The monotonic deadline prevents a failed or crashed bootstrap from
    masking genuine offline/install recovery forever.
    """

    if _control_descriptor_hint_exists():
        return False
    with _INITIALIZE_BOOTSTRAP_LOCK:
        return _INITIALIZE_BOOTSTRAP_IN_FLIGHT_UNTIL_MONOTONIC > time.monotonic() and (
            bootstrap_recovery.state.retry_delay_seconds == 0.0
            or _INITIALIZE_BOOTSTRAP_REPLACING_OWNER
        )


def _bootstrap_owner_replacement_in_flight() -> bool:
    """Recognize only the bounded, active verified-owner replacement lane."""

    with _INITIALIZE_BOOTSTRAP_LOCK:
        return (
            _INITIALIZE_BOOTSTRAP_REPLACING_OWNER
            and _INITIALIZE_BOOTSTRAP_IN_FLIGHT_UNTIL_MONOTONIC > time.monotonic()
        )


def read_status() -> JSONSchema:
    """Project cached native status while coalescing read-only owner connections.

    Returns:
        A path-free, recursively JSON-safe recording status.
    """
    if _should_return_bootstrap_loading_status():
        return _bootstrap_loading_status_payload()
    try:
        runtime = RuntimeManager().status()
    except NativeRuntimeError:
        if not _native_runtime_host_is_unsupported():
            raise
        return _unsupported_native_runtime_status()
    status = ControlClient().status(runtime=runtime)
    state = status.get("state")
    with _INITIALIZE_BOOTSTRAP_LOCK:
        update_deferred = _INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_WORKER_SCHEDULED
        bootstrap_in_flight = _INITIALIZE_BOOTSTRAP_IN_FLIGHT_UNTIL_MONOTONIC > time.monotonic()
        replacing_owner = _INITIALIZE_BOOTSTRAP_REPLACING_OWNER
        initial_attempt = bootstrap_recovery.state.retry_delay_seconds == 0.0
    availability = status.get("availability")
    if (
        bootstrap_in_flight
        # A failed batch keeps retrying, but its cooldown cannot hide the
        # existing error/recovery actions behind an indefinitely renewed loader.
        and (initial_attempt or replacing_owner)
        and isinstance(availability, dict)
        and availability.get("status") == "error"
        and (
            availability.get("reason") in {"connection-failed", "companion-unavailable"}
            or (replacing_owner and availability.get("reason") == "owner-invalid")
        )
    ):
        return _bootstrap_loading_status_payload("connecting")
    if (
        isinstance(status, dict)
        and status.get("ok") is not True
        and isinstance(state, dict)
        and state.get("status") == "offline"
        and runtime.get("installed") is True
        and runtime.get("source") == "plugin-bundled"
    ):
        if update_deferred:
            # This is fixed recovery copy, never native authority. A status
            # poll can truthfully explain the pending update while the old
            # path remains busy and the current plugin stays offline.
            status = disconnected_state(
                safe_message=SAFE_UPDATE_DEFERRED_MESSAGE,
                recovery_kind="update_deferred",
                runtime=runtime,
            )
    status = dict(status)
    if status.get("ok") is True:
        status["availability"] = {"status": "ready"}
    elif not isinstance(status.get("availability"), dict):
        status["availability"] = {
            "status": "error",
            "reason": "companion-unavailable",
        }
    if "companionUpdate" in status:
        # Native payloads cannot advertise this unsigned MCP-owned hint.
        status = {key: value for key, value in status.items() if key != "companionUpdate"}
    return with_runtime(status, runtime=runtime)


def _log_recording_pipeline_step(
    action: str,
    outcome: str,
    *,
    runtime: Mapping[str, object] | None = None,
    cancellation_event: threading.Event | None = None,
    error_kind: str | None = None,
    reason: str | None = None,
) -> None:
    """Log only bounded native recording progress without changing its outcome."""
    if action not in {"start", "stop", "force-start"} or (
        cancellation_event is not None and cancellation_event.is_set()
    ):
        return
    _log_native_recording_pipeline_event(
        "recording",
        outcome,
        platform=runtime.get("platform") if isinstance(runtime, dict) else None,
        version=runtime.get("version") if isinstance(runtime, dict) else None,
        trigger=action,
        error_kind=error_kind,
        reason=reason,
    )


def _recording_pipeline_failure_reason(payload: object) -> str:
    """Classify native refusal without logging errors, identifiers, or paths."""
    if not isinstance(payload, dict):
        return "invalid-response"
    state = payload.get("state")
    if not isinstance(state, dict):
        return "invalid-response"
    if state.get("canStop") is True:
        return "recording-active"
    if state.get("admissionFenced") is True:
        return "owner-handoff-pending"
    if state.get("status") in {
        "signed-out",
        "needs-sign-in",
    }:
        return "sign-in-required"
    permissions = state.get("permissionPresentation")
    if isinstance(permissions, dict):
        if "denied" in (
            permissions.get("microphone"),
            permissions.get("systemAudio"),
        ):
            return "permission-denied"
        if "unsupported" in (
            permissions.get("microphone"),
            permissions.get("systemAudio"),
        ):
            return "permission-unsupported"
    startup = state.get("startup")
    if isinstance(startup, dict):
        if startup.get("recovery") == "recovering":
            return "startup-recovery-pending"
        if startup.get("recovery") == "blocked" or startup.get("attention") is not None:
            return "startup-recovery-blocked"
    recording = state.get("recording")
    if isinstance(recording, dict):
        phase = recording.get("phase")
        if phase in {"starting", "recording", "stopping"}:
            return "recording-active"
        if phase == "unavailable":
            notice = recording.get("notice")
            if isinstance(notice, dict) and notice.get("kind") == "permission-denied":
                return "permission-denied"
            return "companion-unavailable"
    if state.get("status") in {
        "offline",
        "unavailable",
    }:
        return "companion-unavailable"
    return "native-request-rejected"


def _log_explicit_recording_start_failure(
    action: str,
    kind: str,
    *,
    cancellation_event: threading.Event | None,
    runtime: Mapping[str, object] | None = None,
    active_owner_version: object = None,
    handoff_disposition: str | None = None,
    recovery_kind: str | None = None,
    error: Exception | None = None,
) -> None:
    if action not in {"start", "stop"} or (
        cancellation_event is not None and cancellation_event.is_set()
    ):
        return
    diagnostics: dict[str, object] = {}
    if action == "stop":
        diagnostics["operation"] = "stop"
        if error is not None:
            diagnostics.update(_bootstrap_failure_diagnostics(error, require_control_io=True))
    elif handoff_disposition is not None:
        diagnostics["operation"] = "new_note"
        diagnostics["handoff_disposition"] = handoff_disposition
        if runtime is not None:
            target = public_runtime_status(runtime)
            if target.get("installed") is True and target.get("source") == "plugin-bundled":
                diagnostics["target_owner_version"] = target.get("version")
        if active_owner_version is not None:
            diagnostics["active_owner_version"] = active_owner_version
        if recovery_kind is not None:
            diagnostics["recovery_kind"] = recovery_kind
    log_native_runtime_event("recording", "failed", error_kind=kind, **diagnostics)


def _required_update_blocks_start(runtime: Mapping[str, object]) -> bool:
    return any(
        policy["status"] == "required"
        for policy in get_record_interactions_client()
        .peek_required_updates(
            plugin_version=SERVER_VERSION,
            app_version=runtime.get("releaseVersion"),
            client_context=_fallback_policy_context(),
        )
        .values()
    )


def _recording_policy_blocks_start(runtime: Mapping[str, object]) -> bool:
    native_policy = _current_native_meetings_policy()
    if native_policy is not None and native_policy.blocks_start:
        return True
    policy = _current_plugin_client_policy()
    return (
        policy.service_capacity == "blocked"
        or not policy.device_supported
        or _required_update_blocks_start(runtime)
    )


def _calendar_recording_context(value: object) -> CalendarRecordingContext:
    """Bind a clicked Calendar row to cached auth without delaying capture for a read."""
    if not isinstance(value, dict) or set(value) != {
        "accountScopeGeneration",
        "source",
        "eventId",
        "occurrenceStart",
        "title",
    }:
        raise InvalidArguments("Calendar recording context is invalid")
    generation, event_id = value["accountScopeGeneration"], value["eventId"]
    start, title = value["occurrenceStart"], value["title"]
    if (
        value["source"] != "google_calendar"
        or not isinstance(generation, str)
        or not isinstance(event_id, str)
        or not isinstance(start, str)
        or not isinstance(title, str)
    ):
        raise InvalidArguments("Calendar recording context is invalid")
    auth = get_process_auth_manager().peek_cached_chatgpt_auth()
    scope = record_owner_scope_fingerprint(auth) if auth is not None else None
    if auth is None or scope is None:
        raise InvalidArguments("Calendar must be refreshed")
    fingerprint = record_account_fingerprint(auth)
    if generation != get_record_calendar_client().account_scope_generation(
        fingerprint, owner_scope_fingerprint=scope
    ):
        raise InvalidArguments("Calendar must be refreshed")
    try:
        event_id = CALENDAR_EVENT_ID_REGISTRY.resolve(event_id, account_fingerprint=fingerprint)
    except RecordHandleError as error:
        raise InvalidArguments("Calendar must be refreshed") from error
    # Native recording metadata is bounded in UTF-8 bytes. The occurrence still
    # resolves the full authoritative Calendar title during hosted enrichment.
    title = title.encode("utf-8")[:512].decode("utf-8", errors="ignore")
    context: CalendarRecordingContext = {
        "accountScopeFingerprint": scope,
        "source": "google_calendar",
        "eventId": event_id,
        "occurrenceStart": start,
        "title": title,
    }
    if not validate_definition("CalendarRecordingContext", context):
        raise InvalidArguments("Calendar recording context is invalid")
    return context


def _select_windows_legacy_control_runtime(
    manager: RuntimeManager, runtime: Mapping[str, object]
) -> tuple[Mapping[str, object], Mapping[str, object] | None]:
    """Verify first-use migration without activating or replacing a live owner."""

    selected = runtime
    if (
        windows_recovery.enabled()
        and runtime.get("installed") is not True
        and control_descriptor_may_have_live_owner()
    ):
        try:
            selected = manager.prepare_plugin_bundled_replacement()
        except NativeRuntimeError:
            return runtime, None
    retained = retained_windows_legacy_control_runtime(selected)
    return (selected, retained) if retained is not None else (runtime, None)


def call_action(
    action: _RecordingAction,
    *,
    arguments: _RecordingControlArguments | None = None,
    cancellation_event: threading.Event | None = None,
    sidebar_take_notes: bool = False,
    calendar_context: object = None,
) -> JSONSchema:
    """Run one explicit native recording action.

    Args:
        action: Generated native control action.
        arguments: Optional generated action-specific arguments.
        cancellation_event: Optional caller cancellation signal.
        sidebar_take_notes: Include first-use permissions and bounded sidebar feedback.
        calendar_context: Optional app-only Calendar occurrence, validated before dispatch.

    Returns:
        A path-free, recursively JSON-safe action result.
    """
    if cancellation_event is None:
        cancellation_event = _current_rpc_cancellation_event()
    if cancellation_event is not None and cancellation_event.is_set():
        return {"ok": False}
    if action == "start" and arguments:
        # The v2 Start contract has no arguments. Reject before any recovery or
        # launch, preserving the transport boundary's empty-argument policy.
        return with_runtime(
            disconnected_state(runtime={"installed": False}), runtime={"installed": False}
        )
    _log_recording_pipeline_step(action, "started", cancellation_event=cancellation_event)
    try:
        manager = RuntimeManager()
        runtime = manager.status()
    except NativeRuntimeError:
        if not _native_runtime_host_is_unsupported():
            raise
        return _unsupported_native_runtime_status()
    if cancellation_event is not None and cancellation_event.is_set():
        return {"ok": False}
    retained_runtime = None
    if action in {"start", "requestMicrophone", "requestSystemAudio"}:
        runtime, retained_runtime = _select_windows_legacy_control_runtime(manager, runtime)
    if cancellation_event is not None and cancellation_event.is_set():
        return {"ok": False}
    policy_runtime = retained_runtime or runtime
    if action in {"start", "requestMicrophone", "requestSystemAudio"} and (
        _recording_policy_blocks_start(policy_runtime)
    ):
        return with_runtime(ControlClient().status(runtime=policy_runtime), runtime=policy_runtime)
    if retained_runtime is not None and action in {"requestMicrophone", "requestSystemAudio"}:
        runtime = retained_runtime
    _log_recording_pipeline_step(
        action,
        "runtime-verified",
        runtime=runtime,
        cancellation_event=cancellation_event,
    )
    cold_bundled_launch = (
        action in _EXPLICIT_ACTIONS_REQUIRING_CURRENT_IMAGE
        and runtime.get("installed") is not True
        and manager.has_plugin_bundled_artifact_hint()
    )
    if (
        action not in _TERMINAL_CONTROL_ACTIONS
        and runtime.get("installed") is not True
        and not cold_bundled_launch
    ):
        _log_explicit_recording_start_failure(
            action,
            "runtime",
            cancellation_event=cancellation_event,
        )
        return with_runtime(disconnected_state(runtime=runtime), runtime=runtime)
    if action == "start":
        return _run_clicked_companion_action(
            manager,
            runtime,
            operation="start",
            pipeline_action="start",
            cancellation_event=cancellation_event,
            sidebar_take_notes=sidebar_take_notes,
            calendar_context=calendar_context,
        )
    if action in _EXPLICIT_ACTIONS_REQUIRING_CURRENT_IMAGE and (
        cold_bundled_launch
        or (runtime.get("installed") is True and runtime.get("source") == "plugin-bundled")
    ):
        if cold_bundled_launch:
            current_image = False
        else:
            try:
                current_image = (
                    retained_runtime is not None
                    or manager.has_plugin_bundled_update_hint() is not True
                ) and control_descriptor_uses_runtime_image(runtime=runtime)
            except ControlUnavailable:
                current_image = False
        if not current_image:
            _log_recording_pipeline_step(
                action,
                "launching",
                runtime=runtime,
                cancellation_event=cancellation_event,
            )
            try:
                launch = manager.launch_current(
                    require_plugin_bundled=True,
                    recover_unhealthy_current=True,
                )
            except NativeRuntimeUpdateDeferred:
                if cancellation_event is not None and cancellation_event.is_set():
                    return {"ok": False}
                _log_explicit_recording_start_failure(
                    action,
                    "handoff",
                    cancellation_event=cancellation_event,
                    runtime=runtime,
                    handoff_disposition="start_failed",
                    recovery_kind="update_deferred",
                )
                _schedule_initialize_companion_deferred_update()
                return runtime_recovery_payload(
                    runtime,
                    "update_deferred",
                    SAFE_UPDATE_DEFERRED_MESSAGE,
                )
            except NativeRuntimeQuitRequired:
                if cancellation_event is not None and cancellation_event.is_set():
                    return {"ok": False}
                _log_explicit_recording_start_failure(
                    action,
                    "handoff",
                    cancellation_event=cancellation_event,
                    runtime=runtime,
                    handoff_disposition="start_failed",
                    recovery_kind="quit_required",
                )
                return runtime_recovery_payload(
                    runtime,
                    "quit_required",
                    SAFE_QUIT_REQUIRED_MESSAGE,
                )
            except NativeRuntimeError:
                _log_explicit_recording_start_failure(
                    action,
                    "runtime",
                    cancellation_event=cancellation_event,
                )
                return with_runtime(disconnected_state(runtime=runtime), runtime=runtime)
            runtime = {**runtime, **launch}
            _log_recording_pipeline_step(
                action,
                "launched",
                runtime=runtime,
                cancellation_event=cancellation_event,
            )
            # A handed-off Darwin owner launches asynchronously. Keep this
            # explicit click alive until the replacement publishes its exact
            # descriptor, then deliver the original permission/Start request.
            if launch.get("launching") is True:
                current_image = False
                descriptor_deadline = time.monotonic() + _EXPLICIT_ACTION_DESCRIPTOR_WAIT_SECONDS
                while True:
                    if cancellation_event is not None and cancellation_event.is_set():
                        return {"ok": False}
                    try:
                        current_image = control_descriptor_uses_runtime_image(runtime=runtime)
                    except ControlUnavailable:
                        current_image = False
                    if current_image:
                        break
                    remaining = descriptor_deadline - time.monotonic()
                    if remaining <= 0:
                        break
                    poll_seconds = min(
                        _EXPLICIT_ACTION_DESCRIPTOR_POLL_SECONDS,
                        remaining,
                    )
                    if cancellation_event is None:
                        time.sleep(poll_seconds)
                    elif cancellation_event.wait(timeout=poll_seconds):
                        return {"ok": False}
                if not current_image:
                    _log_explicit_recording_start_failure(
                        action,
                        "connection",
                        cancellation_event=cancellation_event,
                    )
                    return with_runtime(
                        disconnected_state(runtime=runtime),
                        runtime=runtime,
                    )
    try:
        # Keep explicit permission requests alive while the user answers the
        # native prompt so cancellation cannot orphan it.
        timeout = 180.0 if action in _EXPLICIT_ACTIONS_REQUIRING_CURRENT_IMAGE else 12.0
        _log_recording_pipeline_step(
            action,
            "dispatching",
            runtime=runtime,
            cancellation_event=cancellation_event,
        )
        client = ControlClient()
        if action in {"requestMicrophone", "requestSystemAudio"} and _recording_policy_blocks_start(
            runtime
        ):
            return with_runtime(client.status(runtime=runtime), runtime=runtime)
        if cancellation_event is None:
            payload = client.call(
                action,
                timeout_seconds=timeout,
                arguments=arguments,
                runtime=runtime,
            )
        else:
            payload = client.call(
                action,
                timeout_seconds=timeout,
                arguments=arguments,
                runtime=runtime,
                cancellation_event=cancellation_event,
            )
        if action == "stop":
            _wake_initialize_companion_deferred_update(payload, runtime=runtime)
        succeeded = isinstance(payload, dict) and payload.get("ok") is True
        _log_recording_pipeline_step(
            action,
            "succeeded" if succeeded else "failed",
            runtime=runtime,
            cancellation_event=cancellation_event,
            error_kind=None if succeeded else "runtime",
            reason=(
                "recording-stopped" if succeeded else _recording_pipeline_failure_reason(payload)
            ),
        )
        return with_runtime(payload, runtime=runtime)
    except ControlUnavailable as error:
        # Control exceptions can include a path from a local runtime probe.
        _log_explicit_recording_start_failure(
            action, "connection", cancellation_event=cancellation_event, error=error
        )
        return with_runtime(disconnected_state(runtime=runtime), runtime=runtime)


class _RPCCancellationContext(threading.local):
    event: threading.Event | None

    def __init__(self) -> None:
        self.event = None


_RPC_CANCELLATION_CONTEXT = _RPCCancellationContext()


def _current_rpc_cancellation_event() -> threading.Event | None:
    return _RPC_CANCELLATION_CONTEXT.event


def set_rpc_cancellation_event(
    event: threading.Event | None,
) -> threading.Event | None:
    """Replace the current dispatch cancellation signal.

    Args:
        event: Cooperative cancellation signal for the active request.

    Returns:
        The previously active cancellation signal, if any.
    """

    previous = _RPC_CANCELLATION_CONTEXT.event
    _RPC_CANCELLATION_CONTEXT.event = event
    return previous


class StagedPluginInstallError(RuntimeError):
    """The local staged Meetings plugin could not be installed safely."""


class LocalPluginRegistrationRemovalError(RuntimeError):
    """The previous Meetings registration could not be removed safely."""


@dataclass(frozen=True)
class _InstalledPluginRegistration:
    marketplace_name: str
    plugin_name: str
    version: str

    @property
    def plugin_id(self) -> str:
        return f"{self.plugin_name}@{self.marketplace_name}"

    @property
    def path_identity(self) -> str:
        return f"{self.marketplace_name}/{self.plugin_name}/{self.version}"

    def is_same_registration(self, other: _InstalledPluginRegistration) -> bool:
        return (
            self.marketplace_name == other.marketplace_name
            and self.plugin_name == other.plugin_name
        )


def _plugin_version_key(value: object) -> tuple[int, int, int]:
    if not isinstance(value, str):
        raise StagedPluginInstallError("plugin version is invalid")
    matched = _PLUGIN_VERSION_PATTERN.fullmatch(value)
    if matched is None:
        raise StagedPluginInstallError("plugin version is invalid")
    return (
        int(matched.group(1)),
        int(matched.group(2)),
        int(matched.group(3)),
    )


def _current_plugin_version_key(value: object) -> tuple[int, int, int]:
    if isinstance(value, str):
        matched = _LOCAL_PLUGIN_VERSION_PATTERN.fullmatch(value)
        if matched is not None:
            value = matched.group("core")
    return _plugin_version_key(value)


def _installed_plugin_registration(
    plugin_root: Path,
) -> _InstalledPluginRegistration | None:
    """Return the exact qualified registration and version for an installed plugin."""

    try:
        resolved_root = plugin_root.expanduser().resolve(strict=True)
    except OSError:
        return None
    family_root = plugin_cache_family_root(resolved_root)
    if family_root is None or resolved_root.parent != family_root:
        return None
    marketplace_name = family_root.parent.name
    plugin_name = family_root.name
    version = resolved_root.name
    registration = _InstalledPluginRegistration(
        marketplace_name=marketplace_name,
        plugin_name=plugin_name,
        version=version,
    )
    if (
        (plugin_name != _STAGED_PLUGIN_NAME and not _is_development_registration(registration))
        or GITHUB_RELEASE_COMPONENT.fullmatch(marketplace_name) is None
        or GITHUB_RELEASE_COMPONENT.fullmatch(plugin_name) is None
    ):
        return None
    try:
        _current_plugin_version_key(version)
        require_canonical_plugin_registration(plugin_root, family_root)
    except (StagedPluginInstallError, NativeRuntimeError):
        return None
    return registration


def _read_meetings_plugin_version(manifest_path: Path) -> str:
    try:
        metadata = manifest_path.lstat()
        if (
            manifest_path.is_symlink()
            or not stat.S_ISREG(metadata.st_mode)
            or not 0 < metadata.st_size <= _MAXIMUM_PLUGIN_MANIFEST_BYTES
        ):
            raise StagedPluginInstallError("plugin manifest is invalid")
        value = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise StagedPluginInstallError("plugin manifest is unavailable") from exc
    if not isinstance(value, dict) or value.get("name") != _STAGED_PLUGIN_NAME:
        raise StagedPluginInstallError("plugin identity is invalid")
    version = value.get("version")
    _plugin_version_key(version)
    if not isinstance(version, str):
        raise StagedPluginInstallError("plugin version is invalid")
    return version


def _is_development_registration(registration: _InstalledPluginRegistration) -> bool:
    """Allow only the explicit local preview to migrate to Internal Testing."""

    return (
        RUNTIME_CONFIG.flavor == "development"
        and RUNTIME_CONFIG.distribution == "internal"
        and RUNTIME_CONFIG.development_update_policy == "local-to-internal"
        and (
            registration.plugin_name == RUNTIME_CONFIG.plugin_name
            or (
                registration.plugin_name == LOCAL_DEVELOPMENT_PLUGIN
                and RUNTIME_CONFIG.server_name == LOCAL_DEVELOPMENT_PLUGIN
            )
        )
        and registration.marketplace_name == LOCAL_DEVELOPMENT_MARKETPLACE
    )


def _active_marketplace_name(
    active_registration: _InstalledPluginRegistration | None,
) -> str:
    """Require the installed registration to agree with its sealed distribution."""

    if active_registration is None:
        raise StagedPluginInstallError("Meetings plugin registration is unavailable")
    if not _is_development_registration(active_registration) and (
        active_registration.plugin_name != RUNTIME_CONFIG.plugin_name
        or active_registration.marketplace_name != RUNTIME_CONFIG.marketplace_name
    ):
        raise StagedPluginInstallError("Meetings plugin distribution does not match runtime config")
    return active_registration.marketplace_name


def _staged_marketplace_name(
    active_registration: _InstalledPluginRegistration | None,
) -> str:
    """Preserve the active publisher, except for an explicit development migration."""

    _active_marketplace_name(active_registration)
    return RUNTIME_CONFIG.marketplace_name


def _staged_plugin_manifest(marketplace_name: str) -> Path:
    if marketplace_name not in TRUSTED_MEETINGS_PLUGIN_PUBLISHERS:
        raise StagedPluginInstallError("staged Meetings marketplace is not trusted")
    return (
        Path(".tmp")
        / "marketplaces"
        / marketplace_name
        / ".agents"
        / "plugins"
        / _STAGED_PLUGIN_NAME
        / _PLUGIN_MANIFEST_RELATIVE_PATH
    )


def _staged_plugin_update_is_available(
    active_registration: _InstalledPluginRegistration,
    staged_version: str,
) -> bool:
    """Return whether the same-distribution staged plugin may replace the active plugin."""

    if active_registration.marketplace_name != _staged_marketplace_name(active_registration):
        return True
    return _plugin_version_key(staged_version) > _current_plugin_version_key(
        active_registration.version
    )


def get_staged_meetings_update_status() -> JSONSchema:
    """Return one bounded, path-free comparison of the active and staged plugins."""

    active_registration = _installed_plugin_registration(PLUGIN_ROOT)
    if active_registration is None:
        return {"updateAvailable": False}
    try:
        active_home = _active_codex_home(None)
        marketplace_name = _staged_marketplace_name(active_registration)
        staged_version = _read_meetings_plugin_version(
            active_home / _staged_plugin_manifest(marketplace_name)
        )
        update_available = _staged_plugin_update_is_available(
            active_registration,
            staged_version,
        )
    except (CodexAuthError, OSError, StagedPluginInstallError):
        return {"updateAvailable": False}
    if not update_available:
        return {"updateAvailable": False}
    return {
        "updateAvailable": True,
        "active": {
            "marketplaceName": active_registration.marketplace_name,
            "version": active_registration.version,
        },
        "staged": {
            "marketplaceName": marketplace_name,
            "version": staged_version,
        },
    }


def install_staged_meetings_plugin(
    current_registration: _InstalledPluginRegistration | None = None,
) -> Path:
    """Install the current distribution's already-local snapshot with bundled Codex."""

    if current_registration is None:
        current_registration = _installed_plugin_registration(PLUGIN_ROOT)
    marketplace_name = _staged_marketplace_name(current_registration)
    assert current_registration is not None
    try:
        active_home = _active_codex_home(None)
        codex_path = _resolve_codex_path(None)
    except CodexAuthError as exc:
        raise StagedPluginInstallError("Codex CLI is unavailable") from exc

    staged_manifest = active_home / _staged_plugin_manifest(marketplace_name)
    staged_version = _read_meetings_plugin_version(staged_manifest)
    minimum_version = (
        current_registration.version
        if current_registration.marketplace_name == marketplace_name
        else None
    )
    if minimum_version is not None and _plugin_version_key(
        staged_version
    ) < _current_plugin_version_key(minimum_version):
        raise StagedPluginInstallError("staged Meetings plugin is older than this plugin")

    environment = os.environ.copy()
    environment["CODEX_HOME"] = str(active_home)
    try:
        completed = subprocess.run(
            [
                codex_path,
                "plugin",
                "add",
                "--json",
                f"{_STAGED_PLUGIN_NAME}@{marketplace_name}",
            ],
            check=False,
            cwd=active_home,
            env=environment,
            stdin=subprocess.DEVNULL,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=120,
        )
    except (OSError, UnicodeError, subprocess.SubprocessError) as exc:
        raise StagedPluginInstallError("Codex CLI invocation failed") from exc
    if (
        completed.returncode != 0
        or len(completed.stdout.encode("utf-8")) > _MAXIMUM_CODEX_PLUGIN_RESULT_BYTES
    ):
        raise StagedPluginInstallError("Codex CLI rejected the plugin installation")
    try:
        result = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise StagedPluginInstallError("Codex CLI returned invalid JSON") from exc
    if (
        not isinstance(result, dict)
        or result.get("pluginId") != f"{_STAGED_PLUGIN_NAME}@{marketplace_name}"
        or result.get("name") != _STAGED_PLUGIN_NAME
        or result.get("marketplaceName") != marketplace_name
        or result.get("version") != staged_version
    ):
        raise StagedPluginInstallError("Codex installed an unexpected plugin")

    installed_value = result.get("installedPath")
    expected_path = (
        active_home / "plugins" / "cache" / marketplace_name / _STAGED_PLUGIN_NAME / staged_version
    )
    if not isinstance(installed_value, str) or Path(installed_value) != expected_path:
        raise StagedPluginInstallError("Codex returned an unexpected plugin path")
    try:
        installed_path = Path(installed_value).resolve(strict=True)
    except OSError as exc:
        raise StagedPluginInstallError("installed Meetings plugin is unavailable") from exc
    if installed_path != expected_path or (
        _read_meetings_plugin_version(installed_path / _PLUGIN_MANIFEST_RELATIVE_PATH)
        != staged_version
    ):
        raise StagedPluginInstallError("installed Meetings plugin is invalid")
    return installed_path


def _codex_reports_plugin_not_installed(
    completed: subprocess.CompletedProcess[str],
) -> bool:
    if completed.returncode == 0:
        return False
    diagnostics = [value.strip() for value in (completed.stdout, completed.stderr) if value.strip()]
    if len(diagnostics) != 1:
        return False
    diagnostic = diagnostics[0]
    if diagnostic.casefold().startswith("error:"):
        diagnostic = diagnostic[6:].strip()
    return diagnostic.casefold() in {"not installed", "plugin is not installed"}


def remove_meetings_plugin_registration(
    registration: _InstalledPluginRegistration,
) -> None:
    """Remove the exact previously installed Meetings registration with bundled Codex."""

    if not _is_development_registration(registration):
        raise LocalPluginRegistrationRemovalError("Meetings registration migration is disabled")
    try:
        active_home = _active_codex_home(None)
        codex_path = _resolve_codex_path(None)
    except CodexAuthError as exc:
        raise LocalPluginRegistrationRemovalError("Codex CLI is unavailable") from exc

    environment = os.environ.copy()
    environment["CODEX_HOME"] = str(active_home)
    try:
        completed = subprocess.run(
            [
                codex_path,
                "plugin",
                "remove",
                "--json",
                registration.plugin_id,
            ],
            check=False,
            cwd=active_home,
            env=environment,
            stdin=subprocess.DEVNULL,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=120,
        )
    except (OSError, UnicodeError, subprocess.SubprocessError) as exc:
        raise LocalPluginRegistrationRemovalError("Codex CLI invocation failed") from exc
    if (
        len(completed.stdout.encode("utf-8")) > _MAXIMUM_CODEX_PLUGIN_RESULT_BYTES
        or len(completed.stderr.encode("utf-8")) > _MAXIMUM_CODEX_PLUGIN_RESULT_BYTES
    ):
        raise LocalPluginRegistrationRemovalError("Codex CLI rejected the registration removal")
    if completed.returncode != 0:
        if _codex_reports_plugin_not_installed(completed):
            return
        raise LocalPluginRegistrationRemovalError("Codex CLI rejected the registration removal")
    try:
        result = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise LocalPluginRegistrationRemovalError("Codex CLI returned invalid JSON") from exc
    if (
        not isinstance(result, dict)
        or result.get("pluginId") != registration.plugin_id
        or result.get("name") != registration.plugin_name
        or result.get("marketplaceName") != registration.marketplace_name
    ):
        raise LocalPluginRegistrationRemovalError("Codex removed an unexpected plugin registration")


def _staged_update_failure(
    reason: str,
    *,
    previous_plugin: str | None = None,
) -> JSONSchema:
    report_mcp_error(
        "bootstrap",
        "runtime",
        mcp_build_timestamp=server_build_timestamp_utc(),
        operation="update",
        update_reason=reason,
    )
    result: JSONSchema = {"ok": False, "reason": reason}
    if previous_plugin is not None:
        result["previousPlugin"] = previous_plugin
    return result


def apply_staged_meetings_update(
    arguments: Mapping[str, object],
    *,
    cancellation_event: threading.Event | None = None,
) -> JSONSchema:
    """Install a staged plugin and replace only its exact verified native owner."""

    if set(arguments) != {"confirmed"} or arguments.get("confirmed") is not True:
        raise InvalidArguments("staged update requires an explicit user gesture")
    if cancellation_event is None:
        cancellation_event = _current_rpc_cancellation_event()
    if cancellation_event is not None and cancellation_event.is_set():
        return {"ok": False, "reason": "cancelled"}
    if not _FORCE_UPGRADE_LOCK.acquire(blocking=False):
        return {"ok": False, "reason": "already_running"}

    def require_not_cancelled() -> None:
        if cancellation_event is not None and cancellation_event.is_set():
            raise ControlUnavailable("native owner recovery was cancelled")

    try:
        old_registration = _installed_plugin_registration(PLUGIN_ROOT)
        try:
            marketplace_name = _staged_marketplace_name(old_registration)
        except StagedPluginInstallError:
            return _staged_update_failure("install_failed")
        try:
            old_runtime = RuntimeManager().status(force_verify=True)
            owner_may_exist = control_descriptor_may_have_live_owner()
            preverified_windows_source = None
            preverified_companion = None
            # A same-version add replaces its cache root. Installing first is safe
            # only when a live owner runs from the immutable stable runtime.
            if owner_may_exist and (
                old_runtime.get("installed") is not True
                or old_runtime.get("source") != "plugin-bundled"
                or not isinstance(old_runtime.get("_sourcePluginRoot"), str)
            ):
                raise ControlUnavailable("native owner is not using the stable runtime")
            if owner_may_exist and supports_compatible_idle_windows_owner(old_runtime):
                preverified_windows_source = preverify_compatible_staged_update_source(old_runtime)
            if owner_may_exist:
                preverified_companion = require_verified_staged_update_owner(
                    old_runtime,
                    preverified_compatible_windows_source=preverified_windows_source,
                )
            require_not_cancelled()
        except (ControlUnavailable, NativeRuntimeError):
            return _staged_update_failure("runtime_verification_failed")

        try:
            installed_root = install_staged_meetings_plugin(old_registration)
        except StagedPluginInstallError:
            return _staged_update_failure("install_failed")

        try:
            if preverified_windows_source is not None:
                installed_family = plugin_cache_family_root(installed_root)
                if installed_family is None:
                    raise NativeRuntimeError("installed Meetings plugin is not canonical")
                require_canonical_plugin_registration(installed_root, installed_family)
            new_manager = RuntimeManager(plugin_root=installed_root)
            prepared_replacement = (
                PreparedCompanionReplacement.prepare(new_manager)
                if windows_recovery.enabled()
                else None
            )
            if prepared_replacement is not None:
                require_not_cancelled()
        except (NativeRuntimeError, ControlUnavailable):
            return _staged_update_failure("launch_failed")

        def revalidate_replacement() -> None:
            require_not_cancelled()
            if prepared_replacement is not None:
                prepared_replacement.revalidate()
            require_not_cancelled()

        try:
            try:
                revalidate_replacement()
                if preverified_companion is not None:
                    quit_companion_owner(
                        preverified_companion,
                        immediate=True,
                        revalidate_request=revalidate_replacement,
                    )
                elif owner_may_exist:
                    if prepared_replacement is not None:
                        force_quit_companion_owner(
                            runtime=old_runtime,
                            allow_compatible_live_owner=True,
                            allow_stale_owner_recovery=False,
                            immediate=True,
                            preverified_compatible_windows_source=preverified_windows_source,
                            revalidate_request=revalidate_replacement,
                        )
                    else:
                        force_quit_companion_owner(
                            runtime=old_runtime,
                            allow_compatible_live_owner=True,
                            allow_stale_owner_recovery=False,
                            immediate=True,
                            preverified_compatible_windows_source=preverified_windows_source,
                        )
            except ControlUnavailable:
                require_not_cancelled()
                # Launch remains the final owner-lease authority; use this hint
                # only to distinguish a proven-absent owner from ambiguity.
                if control_descriptor_may_have_live_owner():
                    raise
        except (ControlUnavailable, NativeRuntimeError):
            return _staged_update_failure("terminate_failed")

        try:
            if prepared_replacement is not None:
                require_not_cancelled()
                prepared_replacement.launch()
            else:
                new_manager.launch_current(require_plugin_bundled=True)
        except (NativeRuntimeError, ControlUnavailable):
            return _staged_update_failure("launch_failed")

        if old_registration is not None:
            # Keep previous-registration removal last so this MCP can finish
            # replacing the native owner before Codex refreshes its plugin catalog.
            try:
                _remove_previous_meetings_registration(
                    old_registration,
                    installed_root=installed_root,
                    marketplace_name=marketplace_name,
                )
            except LocalPluginRegistrationRemovalError:
                return _staged_update_failure(
                    "registration_remove_failed",
                    previous_plugin=old_registration.path_identity,
                )
        return {"ok": True}
    finally:
        _FORCE_UPGRADE_LOCK.release()


def _remove_previous_meetings_registration(
    registration: _InstalledPluginRegistration | None,
    *,
    installed_root: Path,
    marketplace_name: str,
) -> None:
    """Remove an old registration only after the installed companion has launched."""

    if registration is None:
        return
    installed = _InstalledPluginRegistration(
        marketplace_name=marketplace_name,
        plugin_name=_STAGED_PLUGIN_NAME,
        version=installed_root.name,
    )
    if not registration.is_same_registration(installed):
        remove_meetings_plugin_registration(registration)


def _run_clicked_companion_action(
    manager: RuntimeManager,
    runtime: Mapping[str, object],
    *,
    operation: Literal["start", "reconnect"],
    cancellation_event: threading.Event | None,
    pipeline_action: Literal["start", "force-start"] = "force-start",
    sidebar_take_notes: bool = False,
    calendar_context: object = None,
) -> JSONSchema:
    """Recover one explicitly clicked owner, then prove the selected owner responds.

    Bounded health probes and termination retain the same verified client. Windows
    recovery may preinstall a staged successor only when that exact owner has an
    immutable image, then verifies the replacement before any destructive action.
    Other paths keep their existing post-exit install order. Launch retains the
    owner lease authority and never repeats destructive Update.
    """

    escalation_started = False
    owner_terminated = False
    owner_ready = False
    blocked_reported = False
    active_version: str | None = None
    failure_reason = "owner-verification-failed"
    terminal_bootstrap = False
    replacement_still_loading = False

    def log_progress(
        outcome: str, *, error_kind: str | None = None, reason: str | None = None
    ) -> None:
        if operation == "start":
            _log_recording_pipeline_step(
                pipeline_action,
                outcome,
                runtime=runtime,
                cancellation_event=cancellation_event,
                error_kind=error_kind,
                reason=reason,
            )

    def require_not_cancelled() -> None:
        if cancellation_event is not None and cancellation_event.is_set():
            raise ControlUnavailable("native recovery was cancelled")

    def report_termination() -> None:
        nonlocal escalation_started
        escalation_started = True
        log_progress("owner-stopping")
        report_explicit_recovery(
            outcome="started",
            operation=operation,
            active_owner_version=active_version,
            recovery_reason="terminal_bootstrap" if terminal_bootstrap else "owner_unresponsive",
        )

    def report_blocked(reason: str) -> None:
        nonlocal blocked_reported
        if blocked_reported or (cancellation_event is not None and cancellation_event.is_set()):
            return
        blocked_reported = True
        report_explicit_recovery(
            outcome="blocked",
            operation=operation,
            active_owner_version=active_version,
            blocked_reason=reason,
            recovery_reason="terminal_bootstrap" if terminal_bootstrap else "owner_unresponsive",
        )

    if not _FORCE_UPGRADE_LOCK.acquire(blocking=False):
        log_progress("deferred", error_kind="already-in-flight")
        report_blocked("recovery-in-progress")
        if sidebar_take_notes:
            return _TakeNotesResult(False, "Meetings is busy. Try again shortly.")
        return runtime_recovery_payload(runtime, "update_deferred", SAFE_UPDATE_DEFERRED_MESSAGE)

    try:
        if _bootstrap_owner_replacement_in_flight():
            report_blocked("bootstrap-replacement-in-progress")
            return (
                _take_notes_loading()
                if sidebar_take_notes
                else _bootstrap_loading_status_payload("connecting")
            )
        require_not_cancelled()
        platform = runtime.get("platform")
        if isinstance(platform, str):
            runtime_spec_for(platform)
        client = None
        registration = None
        installed_root = None
        marketplace_name = None
        bundled_update = False
        prepared_replacement: PreparedCompanionReplacement | None = None

        def prepare_clicked_replacement() -> None:
            nonlocal prepared_replacement, manager, installed_root, registration, marketplace_name
            nonlocal failure_reason, terminal_bootstrap
            previous_reason = failure_reason
            failure_reason = "replacement-verification-failed"
            require_not_cancelled()
            assert client is not None
            terminal_bootstrap = terminal_bootstrap or (
                operation == "start"
                and client.terminal_bootstrap_recovery_observation() is not None
            )
            if prepared_replacement is None:
                if get_staged_meetings_update_status().get("updateAvailable") is True:
                    assert client is not None
                    owner_path = client.owner.runtime.get("appPath")
                    owner_platform = client.owner.runtime.get("platform")
                    if not isinstance(owner_path, str) or not isinstance(owner_platform, str):
                        raise ControlUnavailable("native owner image is unavailable")
                    # Never overwrite a direct-cache owner while it is still loaded.
                    # The captured client's generation, not selected status, proves
                    # whether installing before termination is safe.
                    from control_client import is_stable_runtime_artifact

                    if not is_stable_runtime_artifact(
                        Path(owner_path), runtime_spec_for(owner_platform), require_active=False
                    ):
                        raise ControlUnavailable("staged native update requires an immutable owner")
                    failure_reason = "plugin-install-failed"
                    registration = _installed_plugin_registration(PLUGIN_ROOT)
                    marketplace_name = _staged_marketplace_name(registration)
                    installed_root = install_staged_meetings_plugin(registration)
                    require_not_cancelled()
                    manager = RuntimeManager(plugin_root=installed_root)
                failure_reason = "replacement-verification-failed"
                prepared_replacement = PreparedCompanionReplacement.prepare(manager)
            failure_reason = "replacement-verification-failed"
            prepared_replacement.revalidate()
            if operation == "start":
                require_verified_companion_replacement(
                    client, prepared_replacement.identity, require_newer=terminal_bootstrap
                )
            require_not_cancelled()
            failure_reason = previous_reason

        if control_descriptor_may_have_live_owner():
            try:
                if (
                    runtime.get("installed") is not True
                    or runtime.get("source") != "plugin-bundled"
                ):
                    raise ControlUnavailable("native companion is unavailable")
                client = companion_client(runtime=runtime, connect=False, allow_existing_owner=True)
            except ControlUnavailable:
                # Unknown or historical v1 owners retain the independently
                # verified idle handoff; discovery grants no force authority.
                bundled_update = True
            if client is not None:
                active_version = client.owner.descriptor["companionVersion"]
                if client.bootstrap_recovery_pending() is True:
                    report_blocked("bootstrap-recovery-pending")
                    return (
                        _take_notes_loading()
                        if sidebar_take_notes
                        else with_runtime(client.public_status(), runtime=runtime)
                    )
                try:
                    log_progress("probing")
                    failure_reason = "unresponsive-owner-check-failed"
                    outcome = recover_unresponsive_companion(
                        client,
                        for_clicked_start=operation == "start",
                        cancellation_event=cancellation_event,
                        on_termination=report_termination,
                        before_replacement=prepare_clicked_replacement
                        if operation == "start" or windows_recovery.enabled()
                        else None,
                    )
                except CooperativeHandoffDeclined as refusal:
                    report_blocked(refusal.recovery_blocker)
                    # Preserve a fresh native blocker or active Stop control without
                    # treating refusal as permission to replay an ambiguous Start.
                    try:
                        protected = client.get_state(
                            timeout_seconds=1.0, cancellation_event=cancellation_event
                        )
                    except ControlUnavailable as error:
                        raise refusal from error
                    if not protected["recording"]["controls"]["start"]["enabled"]:
                        log_progress(
                            "deferred",
                            reason=protected["recording"]["controls"]["start"].get(
                                "disabledReason"
                            ),
                        )
                        if sidebar_take_notes:
                            return _take_notes_unavailable(protected, client=client)
                        return with_runtime(client.public_status(), runtime=runtime)
                    raise
                owner_terminated = outcome is CompanionRecoveryOutcome.TERMINATED
                if owner_terminated:
                    log_progress("owner-stopped")

        if client is not None and not owner_terminated:
            try:
                retained_runtime = (
                    retained_windows_legacy_control_runtime(runtime, client=client)
                    if operation == "start"
                    else None
                )
                if retained_runtime is not None:
                    runtime = retained_runtime
                    bundled_update = False
                else:
                    bundled_update = (
                        manager.has_plugin_bundled_update_hint() is True
                        or not control_descriptor_uses_runtime_image(runtime=runtime)
                    )
            except ControlUnavailable:
                bundled_update = True
        if client is None or owner_terminated or bundled_update:
            require_not_cancelled()
            if (
                owner_terminated
                and prepared_replacement is None
                and get_staged_meetings_update_status().get("updateAvailable") is True
            ):
                failure_reason = "plugin-install-failed"
                log_progress("installing")
                registration = _installed_plugin_registration(PLUGIN_ROOT)
                marketplace_name = _staged_marketplace_name(registration)
                installed_root = install_staged_meetings_plugin(registration)
                require_not_cancelled()
                manager = RuntimeManager(plugin_root=installed_root)
                log_progress("installed")
            failure_reason = "companion-launch-failed"
            log_progress("launching")
            if prepared_replacement is not None:
                prepared_replacement.launch()
            elif bundled_update:
                manager.launch_current(require_plugin_bundled=True, recover_unhealthy_current=True)
            else:
                manager.launch_current(require_plugin_bundled=True)
            log_progress("launched")
            require_not_cancelled()
            runtime = manager.status(force_verify=True)
            log_progress("runtime-verified")
            if runtime.get("installed") is not True or runtime.get("source") != "plugin-bundled":
                raise ControlUnavailable("updated native companion is unavailable")
            failure_reason = "owner-not-published"
            deadline = time.monotonic() + _EXPLICIT_ACTION_DESCRIPTOR_WAIT_SECONDS
            while True:
                require_not_cancelled()
                try:
                    if control_descriptor_uses_runtime_image(runtime=runtime):
                        break
                except ControlUnavailable:
                    pass
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise ControlUnavailable("updated native companion is unavailable")
                delay = min(_EXPLICIT_ACTION_DESCRIPTOR_POLL_SECONDS, remaining)
                if cancellation_event is None:
                    time.sleep(delay)
                else:
                    cancellation_event.wait(timeout=delay)
            client = companion_client(runtime=runtime, connect=False)

        failure_reason = "owner-not-ready"
        state = client.get_state(
            cancellation_event=cancellation_event, for_start=operation == "start"
        )
        if owner_terminated:
            ready_state = wait_for_companion_recording_ready(
                client,
                state,
                timeout_seconds=_EXPLICIT_ACTION_READY_WAIT_SECONDS,
                cancellation_event=cancellation_event,
                for_start=operation == "start",
            )
            if ready_state is None:
                replacement_still_loading = True
                raise ControlUnavailable("replacement companion startup is still initializing")
            state = ready_state
        log_progress("owner-ready")
        owner_ready = True
        if escalation_started:
            report_explicit_recovery(
                outcome="recovered",
                operation=operation,
                active_owner_version=active_version,
                target_owner_version=client.owner.descriptor["companionVersion"],
                recovery_reason="terminal_bootstrap"
                if terminal_bootstrap
                else "owner_unresponsive",
            )
            escalation_started = False
        require_not_cancelled()
        # Native owns recovery and permission blockers. Dispatch on the same
        # freshly read owner, and never replay an ambiguous Start after restart.
        if sidebar_take_notes:
            if _recording_policy_blocks_start(runtime):
                return _take_notes_unavailable()
            prepared = _prepare_sidebar_take_notes(
                client, state, cancellation_event=cancellation_event, runtime=runtime
            )
            if isinstance(prepared, _TakeNotesResult):
                return prepared
            state = prepared
            require_not_cancelled()
        start_enabled = state["recording"]["controls"]["start"]["enabled"]
        start_result: dict[str, object] | None = None
        if operation == "start" and _recording_policy_blocks_start(runtime):
            start_enabled = False
        if operation == "start":
            if start_enabled:
                failure_reason = "recording-start-failed"
                log_progress("dispatching")
                # Validate after recovery and permissions, against the current account.
                # Negotiate with the final owner; an old companion retains empty Start.
                start_parameters: dict[str, object] = {}
                if (
                    calendar_context is not None
                    and "recording.calendar-context.v1" in client.negotiated_capabilities
                ):
                    start_parameters["calendarContext"] = _calendar_recording_context(
                        calendar_context
                    )
                start_context = copy_context()
                policy_rejected = False

                def require_start_policy() -> None:
                    nonlocal policy_rejected

                    # Windows preflight runs on the I/O worker; retain this caller's
                    # visitor/build while reading the latest cached policy.
                    if start_context.run(_recording_policy_blocks_start, runtime):
                        policy_rejected = True
                        raise ControlUnavailable("recording start is blocked by policy")

                try:
                    start_result = client.call(
                        "recording.start",
                        start_parameters,
                        timeout_seconds=180.0,
                        cancellation_event=cancellation_event,
                        before_send=require_start_policy,
                    )
                except ControlUnavailable:
                    if not policy_rejected:
                        raise
                    start_enabled = False
                    log_progress("deferred", reason="policy-blocked")
            else:
                log_progress(
                    "deferred", reason=state["recording"]["controls"]["start"].get("disabledReason")
                )
        payload = with_runtime(client.public_status(), runtime=runtime)
        if operation == "start" and start_enabled:
            # The authenticated response completed this request; its native
            # recording presentation remains the authority for actual capture.
            log_progress("succeeded", reason="request-completed")
        # Registration removal can refresh the MCP host, so finish the clicked
        # operation before removing a migrated registration.
        if installed_root is not None and marketplace_name is not None:
            try:
                _remove_previous_meetings_registration(
                    registration, installed_root=installed_root, marketplace_name=marketplace_name
                )
            except LocalPluginRegistrationRemovalError:
                # A completed Start must retain its authoritative Stop control.
                report_mcp_error(
                    "bootstrap", "runtime", mcp_build_timestamp=server_build_timestamp_utc()
                )
        if sidebar_take_notes:
            if (
                is_companion_state(start_result)
                and start_result["recording"]["phase"] == "idle"
                and start_result["recording"]["session"] is None
                and not start_result["recording"]["controls"]["stop"]["enabled"]
            ):
                # Start can finish idle after cancellation or an already-stopped
                # recording. Acknowledge the request without inferring its cause;
                # a later idle read cannot prove a failed or ambiguous Start completed.
                return _TakeNotesResult(True, "Request completed.")
            latest = client.latest_state()
            if (
                start_enabled
                and latest is not None
                and latest["recording"]["phase"] in {"starting", "recording"}
            ):
                return _TakeNotesResult(True, "Note taking started.")
            return _take_notes_unavailable(latest, client=client)
        return payload
    except (
        ControlUnavailable,
        NativeRuntimeError,
        StagedPluginInstallError,
        LocalPluginRegistrationRemovalError,
    ) as error:
        if escalation_started:
            report_explicit_recovery(
                outcome="failed",
                operation=operation,
                active_owner_version=active_version,
                blocked_reason=error.recovery_blocker
                if isinstance(error, CooperativeHandoffDeclined)
                else failure_reason,
                recovery_reason="terminal_bootstrap"
                if terminal_bootstrap
                else "owner_unresponsive",
            )
        if cancellation_event is not None and cancellation_event.is_set():
            return {"ok": False}
        if replacement_still_loading:
            log_progress("deferred", reason="owner-not-ready")
            return (
                _take_notes_loading()
                if sidebar_take_notes
                else _bootstrap_loading_status_payload("connecting")
            )
        if (
            not escalation_started
            and not owner_terminated
            and not owner_ready
            and failure_reason != "recording-start-failed"
        ):
            report_blocked(failure_reason)
        if (operation == "reconnect" and isinstance(error, NativeRuntimeUpdateDeferred)) or (
            pipeline_action == "start"
            and isinstance(error, (NativeRuntimeUpdateDeferred, NativeRuntimeQuitRequired))
        ):
            _schedule_initialize_companion_deferred_update()
        deferred = isinstance(
            error,
            (CooperativeHandoffDeclined, NativeRuntimeUpdateDeferred, NativeRuntimeQuitRequired),
        )
        log_progress(
            "deferred" if deferred else "failed",
            error_kind="runtime"
            if isinstance(
                error,
                (NativeRuntimeError, StagedPluginInstallError, LocalPluginRegistrationRemovalError),
            )
            else "connection",
            reason=failure_reason,
        )
        if (
            pipeline_action == "start"
            and isinstance(error, NativeRuntimeQuitRequired)
            and not isinstance(error, NativeRuntimeUpdateDeferred)
        ):
            return runtime_recovery_payload(runtime, "quit_required", SAFE_QUIT_REQUIRED_MESSAGE)
        return runtime_recovery_payload(runtime, "update_deferred", SAFE_UPDATE_DEFERRED_MESSAGE)
    finally:
        _FORCE_UPGRADE_LOCK.release()


def force_start_recording(
    arguments: Mapping[str, object],
    *,
    cancellation_event: threading.Event | None = None,
) -> JSONSchema:
    """Recover an explicit Take notes click and Start once when native authorizes it."""

    if set(arguments) - {"confirmed", "calendarContext"} or arguments.get("confirmed") is not True:
        raise InvalidArguments("force start requires explicit confirmation")
    if "calendarContext" in arguments and not isinstance(arguments["calendarContext"], dict):
        raise InvalidArguments("Calendar recording context is invalid")
    if cancellation_event is None:
        cancellation_event = _current_rpc_cancellation_event()
    if cancellation_event is not None and cancellation_event.is_set():
        return {"ok": False}
    _log_recording_pipeline_step("force-start", "started", cancellation_event=cancellation_event)
    if not _FORCE_START_LOCK.acquire(blocking=False):
        _log_recording_pipeline_step(
            "force-start",
            "deferred",
            cancellation_event=cancellation_event,
            error_kind="already-in-flight",
        )
        return runtime_recovery_payload(
            {"installed": False}, "update_deferred", SAFE_UPDATE_DEFERRED_MESSAGE
        )
    runtime: Mapping[str, object] = {"installed": False}
    native_runtime_selected = False
    try:
        manager = RuntimeManager()
        native_runtime_selected = True
        runtime = manager.status(force_verify=True)
        runtime, retained_runtime = _select_windows_legacy_control_runtime(manager, runtime)
        if cancellation_event is not None and cancellation_event.is_set():
            return {"ok": False}
        policy_runtime = retained_runtime or runtime
        if _recording_policy_blocks_start(policy_runtime):
            return with_runtime(
                ControlClient().status(runtime=policy_runtime), runtime=policy_runtime
            )
        _log_recording_pipeline_step(
            "force-start",
            "runtime-verified",
            runtime=runtime,
            cancellation_event=cancellation_event,
        )
        return _run_clicked_companion_action(
            manager,
            runtime,
            operation="start",
            cancellation_event=cancellation_event,
            calendar_context=arguments.get("calendarContext"),
        )
    except (
        NativeRuntimeError,
        ControlUnavailable,
        StagedPluginInstallError,
        LocalPluginRegistrationRemovalError,
    ) as error:
        if cancellation_event is not None and cancellation_event.is_set():
            return {"ok": False}
        if not native_runtime_selected and _native_runtime_host_is_unsupported():
            return _unsupported_native_runtime_status()
        _log_recording_pipeline_step(
            "force-start",
            "deferred" if isinstance(error, NativeRuntimeUpdateDeferred) else "failed",
            runtime=runtime,
            cancellation_event=cancellation_event,
            error_kind="runtime"
            if isinstance(
                error,
                (NativeRuntimeError, StagedPluginInstallError, LocalPluginRegistrationRemovalError),
            )
            else "connection",
            reason="companion-unavailable",
        )
        return runtime_recovery_payload(runtime, "update_deferred", SAFE_UPDATE_DEFERRED_MESSAGE)
    finally:
        _FORCE_START_LOCK.release()


def _set_synthetic_recovery_kind(payload: dict[str, object], kind: str) -> None:
    state = payload["state"]
    if (
        not isinstance(state, dict)
        or not isinstance(state.get("status"), str)
        or type(state.get("canStart")) is not bool
        or type(state.get("canStop")) is not bool
    ):
        raise ControlUnavailable("native recording state is malformed")
    recovery = state.get("recovery")
    if not isinstance(recovery, dict):
        raise ControlUnavailable("native recording recovery is malformed")
    recovery["kind"] = kind


def _native_policy_owner_for_context(context: PluginClientContext | None) -> CompanionClient | None:
    """Restrict native policy ownership to the matching local desktop visitor."""

    system_name = {"win32": "Windows", "darwin": "Darwin"}.get(sys.platform)
    if system_name is None or (
        context is not None and (context.surface != "desktop" or context.system_name != system_name)
    ):
        return None
    return cached_meetings_policy_client()


def _current_native_meetings_policy() -> NativeMeetingsPolicy | None:
    """Read an authenticated local owner's cached policy, never visitor fallback."""

    context = _PLUGIN_CLIENT_CONTEXT.get()
    client = _native_policy_owner_for_context(context)
    if client is None:
        return None
    auth = get_process_auth_manager().peek_cached_chatgpt_auth()
    scope = record_owner_scope_fingerprint(auth) if auth is not None else None
    observation = client.cached_meetings_eligibility(
        account_scope=scope,
        platform="windows" if sys.platform == "win32" else "macos",
        plugin_version=SERVER_VERSION,
        codex_version=context.codex_version if context is not None else get_current_codex_version(),
    )
    if observation is None:
        return None
    policy = project_native_meetings_policy(
        observation,
        windows=sys.platform == "win32",
        codex_version=context.codex_version if context is not None else get_current_codex_version(),
    )
    local_context = context or PluginClientContext(
        "Windows" if sys.platform == "win32" else "Darwin", "desktop", get_current_codex_version()
    )
    owner = client.owner
    return get_record_interactions_client().observe_native_policy(
        local_context,
        policy,
        account_scope=scope,
        native_owner=(str(owner.root), owner.descriptor["ownerEpoch"], owner.descriptor["pid"]),
        owner_is_current=lambda: _native_policy_owner_for_context(context) is client,
        plugin_version=SERVER_VERSION,
    )


def _fallback_policy_context() -> PluginClientContext | None:
    """Reuse a local native handoff for metadata-free callers without inferring a build."""
    context = _PLUGIN_CLIENT_CONTEXT.get()
    if context is None and (
        system_name := {"win32": "Windows", "darwin": "Darwin"}.get(sys.platform)
    ):
        local_context = PluginClientContext(system_name, "desktop", get_current_codex_version())
        if get_record_interactions_client().has_native_policy_handoff(local_context):
            return local_context
    return context


def _current_plugin_client_policy(
    *, local_fallback: bool = False, observe_native: bool = True
) -> PluginClientPolicy:
    native_policy = _current_native_meetings_policy() if observe_native else None
    context = _fallback_policy_context()
    if context is None and (local_fallback or native_policy is not None):
        context = PluginClientContext(
            {"win32": "Windows", "darwin": "Darwin", "linux": "Linux"}.get(sys.platform, "unknown"),
            "desktop",
            get_current_codex_version(),
        )
    client = get_record_interactions_client()
    if context is None:
        return PluginClientPolicy(service_capacity=client.peek_service_capacity())
    return client.peek_plugin_client_policy(context, plugin_version=SERVER_VERSION)


def plugin_availability_blocks_start(*, local_fallback: bool = False) -> bool:
    return not _current_plugin_client_policy(local_fallback=local_fallback).device_supported


def call_tool(
    name: str,
    arguments: object | None = None,
    *,
    host_app_version: str | None = None,
    cancellation_event: threading.Event | None = None,
    profile: str = DEFAULT_PROFILE,
) -> (
    JSONSchema
    | CalendarSectionWire
    | NotesSectionWire
    | PrivateMeetingsResponse
    | _PrivateLegacySnapshot
    | PromptPayload
    | CompanionSettingsResponseWire
):
    """Dispatch a tool with request-scoped visitor attributes.

    Args:
        name: Canonical tool name.
        arguments: Validated tool arguments, including optional visitor context.
        host_app_version: Desktop host version from app-only RPC metadata. Nested
            dispatch inherits the current request; independent requests never reuse it.
        cancellation_event: Cancellation signal for the active request.
        profile: Installed MCP profile controlling available tools.

    Returns:
        The tool's public or app-private response envelope.
    """
    with scoped_tool_arguments(
        name,
        arguments,
        app_ui_allowed=profile in APP_UI_PROFILES,
        host_app_version=host_app_version,
    ) as scoped_arguments:
        return _call_tool(
            name, scoped_arguments, cancellation_event=cancellation_event, profile=profile
        )


def _call_tool(
    name: str,
    arguments: object | None = None,
    *,
    cancellation_event: threading.Event | None = None,
    profile: str = DEFAULT_PROFILE,
) -> (
    JSONSchema
    | CalendarSectionWire
    | NotesSectionWire
    | PrivateMeetingsResponse
    | _PrivateLegacySnapshot
    | PromptPayload
    | CompanionSettingsResponseWire
):
    """Dispatch one validated Meetings tool call.

    Args:
        name: Registered MCP tool name.
        arguments: Candidate JSON object supplied by the caller.
        cancellation_event: Optional caller cancellation signal.
        profile: Active MCP tool profile.

    Returns:
        The tool-specific typed response or private gateway envelope.

    Raises:
        InvalidArguments: If the profile or argument object is unsupported.
        ValueError: If the tool name is unknown.
    """

    if arguments is None:
        arguments = {}
    if not is_json_object(arguments):
        raise InvalidArguments("tool arguments must be an object")
    if profile not in SUPPORTED_PROFILES:
        raise InvalidArguments("tool profile is unsupported")

    if name == MEETING_MENTIONS_TOOL:
        if (
            profile not in APP_UI_PROFILES
            or not get_record_interactions_client().discovery_rollout().search_mentions
        ):
            raise InvalidArguments("unknown tool")
        # Ignore legacy navigation paths; Meetings searches a flat list of notes.
        require_tool_arguments(name, arguments, ("query",), ("path", "preload"))
        query = arguments.get("query")
        if not isinstance(query, str) or len(query) > 256:
            raise InvalidArguments("query must be a string of at most 256 characters")
        preload = arguments.get("preload", False)
        if not isinstance(preload, bool):
            raise InvalidArguments("preload must be a boolean")
        if preload:
            # Host-driven catalog loading respects cached host and plugin floors
            # as the blocked workspace without starting auth or native discovery.
            native_policy = _current_native_meetings_policy()
            updates = (
                native_policy.required_updates
                if native_policy is not None
                else get_record_interactions_client().peek_required_updates(
                    plugin_version=SERVER_VERSION,
                    app_version=None,
                    client_context=_fallback_policy_context(),
                )
            )
            if any(
                update["status"] == "required"
                for target, update in updates.items()
                if target in {"codex", "plugin"}
            ):
                return {"items": []}
        return _recent_meeting_mentions(
            cancellation_event=(
                cancellation_event
                if cancellation_event is not None
                else _current_rpc_cancellation_event()
            ),
        )

    if name in {STRUCTURED_SETTINGS_READ_TOOL, STRUCTURED_SETTINGS_UPDATE_TOOL}:
        if profile not in APP_UI_PROFILES:
            raise InvalidArguments("unknown tool")
        effective_cancellation = (
            cancellation_event
            if cancellation_event is not None
            else _current_rpc_cancellation_event()
        )
        if name == STRUCTURED_SETTINGS_READ_TOOL:
            require_empty_arguments(name, arguments)
            return structured_settings_payload(cancellation_event=effective_cancellation)
        if set(arguments) != {"set"} or not is_json_object(arguments["set"]):
            raise InvalidArguments("settings.update requires a set object")
        return structured_settings_payload(
            changes=arguments["set"], cancellation_event=effective_cancellation
        )

    if name in {"chatgpt_meetings_open", "meetings.open"}:
        require_empty_arguments(name, arguments)
        payload = opening_shell_payload()
        payload["resourceUri"] = WIDGET_URI
        # Opening returns a fixed loader; the deferred canonical backend lanes
        # hydrate Calendar and Notes after the app connects.
        snapshot = empty_notes_view("loading")
        if profile in APP_UI_PROFILES:
            # A cached bearer makes this a no-op; cold auth warms in the
            # background without delaying the page or forcing token refresh.
            try:
                warm_process_auth()
            except CodexAuthError:
                pass
            # Page open is the local-UI gesture that starts the exact verified
            # bundled companion. This only schedules a daemon: it never installs,
            # records, or requests capture permissions before returning the UI.
            log_native_runtime_event("bootstrap", "scheduled", trigger="page-open")
            schedule_initialize_companion_bootstrap(require_owner_response=True)
        if not is_json_object(snapshot):
            raise ValueError("opening snapshot is not a JSON object")
        payload["snapshot"] = snapshot
        return payload
    if name == "chatgpt_meetings_get_snapshot":
        if profile in APP_UI_PROFILES:
            gateway_request = normalize_local_ui_gateway_request(arguments)
            effective_cancellation = (
                cancellation_event
                if cancellation_event is not None
                else _current_rpc_cancellation_event()
            )
            if not isinstance(gateway_request, LegacySnapshotGatewayRequest):
                if (
                    gateway_request.request == "settings.update"
                    and gateway_request.arguments.get("autoRecordEnabled") is True
                    and plugin_availability_blocks_start(local_fallback=True)
                ):
                    raise InvalidArguments(
                        "Automatic meeting notes are unavailable on this client."
                    )
                if gateway_request.request == "settings.getTarget":
                    registration = _installed_plugin_registration(PLUGIN_ROOT)
                    return PrivateMeetingsResponse(
                        request=gateway_request.request,
                        ok=registration is not None,
                        data={"pluginId": registration.plugin_id} if registration else None,
                        error_kind=None if registration else "backend",
                    )
                if gateway_request.request == "local.getStagedUpdateStatus":
                    return get_staged_meetings_update_status()
                target = LOCAL_UI_NATIVE_REQUEST_TARGETS.get(gateway_request.request)
                if target is not None:
                    return call_tool(
                        target,
                        gateway_request.arguments,
                        cancellation_event=effective_cancellation,
                        profile=profile,
                    )
                if gateway_request.app_instance_id is not None:
                    return read_private_meetings_response(
                        gateway_request.request,
                        gateway_request.arguments,
                        app_instance_id=gateway_request.app_instance_id,
                        cancellation_event=effective_cancellation,
                    )
                return read_private_meetings_response(
                    gateway_request.request,
                    gateway_request.arguments,
                    cancellation_event=effective_cancellation,
                )
            page_arguments = gateway_request.arguments
            if page_arguments.get("section") == "calendar":
                return _PrivateLegacySnapshot(
                    "calendar.list",
                    read_backend_calendar_view(
                        cancellation_event=effective_cancellation,
                    ),
                )
            correlation: NotesRecordingArguments = {}
            if "recording_started_at" in page_arguments:
                correlation["recording_started_at"] = page_arguments["recording_started_at"]
            return _PrivateLegacySnapshot(
                "notes.list",
                read_backend_meetings_view(
                    initial_limit=page_arguments.get("initial_limit"),
                    page_token=page_arguments.get("page_token"),
                    **correlation,
                    cancellation_event=effective_cancellation,
                ),
            )
        require_empty_arguments(name, arguments)
        return read_backend_meetings_view(
            cancellation_event=(
                cancellation_event
                if cancellation_event is not None
                else _current_rpc_cancellation_event()
            ),
        )
    if name == "chatgpt_meetings_prepare_note":
        require_tool_arguments(name, arguments, ("meetingId", "title"))
        note_id = require_prompt_meeting_id(arguments["meetingId"])
        title = require_prompt_title(arguments["title"])
        registration = _installed_plugin_registration(PLUGIN_ROOT)
        try:
            marketplace_name = _active_marketplace_name(registration)
        except StagedPluginInstallError as exc:
            raise InvalidArguments(
                "Meetings plugin registration does not match runtime config"
            ) from exc
        assert registration is not None
        read_source, canonical_id = get_record_interactions_client().resolve_note_reference(
            note_id,
            cancellation_event=cancellation_event,
        )
        return build_note_payload(
            canonical_id,
            title,
            server_name=SERVER_NAME,
            resource_kind=read_source,
            marketplace_name=marketplace_name,
            plugin_name=registration.plugin_name,
            allow_local_development=marketplace_name == LOCAL_DEVELOPMENT_MARKETPLACE,
        )
    if name == "meetings.status":
        require_empty_arguments(name, arguments)
        return read_status()
    if name == "meetings.getSettings":
        require_empty_arguments(name, arguments)
        return settings_tool_payload(action="getSettings")
    if name == "meetings.updateSettings":
        if arguments.get("meetingDetectionEnabled") is True and plugin_availability_blocks_start():
            raise InvalidArguments("Meeting detection is unavailable on this client.")
        return settings_tool_payload(
            action="updateSettings",
            arguments=normalize_settings_patch(arguments, tool_name=name),
        )
    if name == "meetings.applyStagedUpdate":
        return apply_staged_meetings_update(
            arguments,
            cancellation_event=(
                cancellation_event
                if cancellation_event is not None
                else _current_rpc_cancellation_event()
            ),
        )
    if name == "meetings.installAndLaunch":
        require_empty_arguments(name, arguments)
        if plugin_availability_blocks_start():
            return read_status()
        if cancellation_event is None:
            cancellation_event = _current_rpc_cancellation_event()
        if cancellation_event is not None and cancellation_event.is_set():
            return {"ok": False}
        observed_runtime: Mapping[str, object] | None = None
        try:
            manager = RuntimeManager()
            observed_runtime = manager.status()
            if cancellation_event is not None and cancellation_event.is_set():
                return {"ok": False}
            # ensure_installed can activate B before an authenticated A has
            # declined the update. Reconnect must enter the staged, work-aware
            # launch boundary directly so a busy owner keeps A selected.
            runtime = observed_runtime
            if control_descriptor_may_have_live_owner():
                return _run_clicked_companion_action(
                    manager, runtime, operation="reconnect", cancellation_event=cancellation_event
                )
            launch = manager.launch_current(
                require_plugin_bundled=True,
                recover_unhealthy_current=True,
            )
            launch_runtime = {**runtime, **launch}
            if launch.get("reused") is True:
                # Reuse preserves authenticated stream state; an unreadable owner stays offline.
                live_runtime = {**launch_runtime, "launching": False}
                try:
                    live_payload = ControlClient().status(
                        runtime=live_runtime,
                        wait_for_connection=True,
                    )
                except ControlUnavailable:
                    live_payload = {}
                if isinstance(live_payload, dict) and live_payload.get("ok") is True:
                    return with_runtime(live_payload, runtime=live_runtime)
                return with_runtime(
                    disconnected_state(runtime=live_runtime),
                    runtime=live_runtime,
                )
            payload = disconnected_state(
                safe_message=SAFE_LAUNCHING_MESSAGE,
                runtime=launch_runtime,
            )
            payload["ok"] = True
            payload.pop("error", None)
            payload["runtime"] = launch_runtime
            _set_synthetic_recovery_kind(payload, "launching")
            return with_runtime(payload, runtime=launch_runtime)
        except NativeRuntimeUpdateDeferred:
            if cancellation_event is not None and cancellation_event.is_set():
                return {"ok": False}
            _schedule_initialize_companion_deferred_update()
            return runtime_recovery_payload(
                observed_runtime,
                "update_deferred",
                SAFE_UPDATE_DEFERRED_MESSAGE,
            )
        except NativeRuntimeQuitRequired:
            return runtime_recovery_payload(
                observed_runtime,
                "quit_required",
                SAFE_QUIT_REQUIRED_MESSAGE,
            )
        except (
            NativeRuntimeError,
            ControlUnavailable,
            StagedPluginInstallError,
            LocalPluginRegistrationRemovalError,
        ):
            if cancellation_event is not None and cancellation_event.is_set():
                return {"ok": False}
            if observed_runtime is None and _native_runtime_host_is_unsupported():
                return _unsupported_native_runtime_status()
            report_mcp_error(
                "bootstrap",
                "runtime",
                mcp_build_timestamp=server_build_timestamp_utc(),
            )
            payload = disconnected_state(runtime=observed_runtime)
            _set_synthetic_recovery_kind(payload, "install_failed")
            return with_runtime(payload, runtime=observed_runtime)
    actions: dict[str, _RecordingAction] = {
        "meetings.requestMicrophone": "requestMicrophone",
        "meetings.requestSystemAudio": "requestSystemAudio",
        "meetings.stop": "stop",
    }
    if name == "meetings.start":
        require_empty_arguments(
            name, {key: value for key, value in arguments.items() if key != "calendarContext"}
        )
        if "calendarContext" in arguments:
            if not isinstance(arguments["calendarContext"], dict):
                raise InvalidArguments("Calendar recording context is invalid")
            return call_action("start", calendar_context=arguments["calendarContext"])
        return call_action("start")
    if name == "meetings.takeNotes":
        require_empty_arguments(name, arguments)
        return take_notes()
    if name == "meetings.forceStart":
        return force_start_recording(arguments, cancellation_event=cancellation_event)
    if name == "meetings.recheckAudio":
        require_empty_arguments(name, arguments)
        from companion_client import companion_client

        runtime = RuntimeManager().status()
        if _recording_policy_blocks_start(runtime):
            return read_status()
        client = companion_client(runtime=runtime, cancellation_event=cancellation_event)
        _recheck_audio(client, runtime=runtime, cancellation_event=cancellation_event)
        return with_runtime(client.public_status(), runtime=runtime)
    if name in {"meetings.openMicrophoneSettings", "meetings.openSystemAudioSettings"}:
        require_empty_arguments(name, arguments)
        if plugin_availability_blocks_start():
            return read_status()
        from companion_client import companion_client

        runtime = RuntimeManager().status()
        client = companion_client(runtime=runtime, cancellation_event=cancellation_event)
        permission = "microphone" if name == "meetings.openMicrophoneSettings" else "systemAudio"
        if plugin_availability_blocks_start():
            return with_runtime(client.public_status(), runtime=runtime)
        client.call(
            "permissions.openSystemSettings",
            {"kind": permission},
            cancellation_event=cancellation_event,
        )
        return with_runtime(client.public_status(), runtime=runtime)
    if name in actions:
        control_arguments: _RecordingControlArguments = {}
        if name == "meetings.stop":
            validated_stop = normalize_local_recording_control(arguments)
            control_arguments = {"expectedSessionId": validated_stop["expectedSessionId"]}
        else:
            require_empty_arguments(name, arguments)
            if plugin_availability_blocks_start():
                return read_status()
        if control_arguments:
            return call_action(actions[name], arguments=control_arguments)
        return call_action(actions[name])
    raise ValueError(f"unknown Meetings tool: {name}")


def tool_result(
    payload: Mapping[str, object],
    include_widget: bool = False,
    *,
    extra_meta: Mapping[str, object] | None = None,
) -> JSONSchema:
    """Serialize one validated tool payload into an MCP call result.

    Args:
        payload: Conversation-visible structured content.
        include_widget: Whether to attach the Meetings widget metadata.
        extra_meta: Optional component-only metadata.

    Returns:
        A recursively JSON-safe MCP call result.

    Raises:
        ValueError: If application-produced content is not JSON-safe.
    """

    if isinstance(payload, _PrivateLegacySnapshot):
        return private_meetings_tool_result(payload.response)
    if isinstance(payload, _TakeNotesResult):
        return {
            "content": [{"type": "text", "text": payload.message}],
            "structuredContent": dict(payload),
            "isError": payload["ok"] is not True and not payload.loading,
        }
    if not is_json_object(payload):
        raise ValueError("tool payload is not a JSON object")
    result: JSONSchema = {
        "content": [
            {
                "type": "text",
                "text": json.dumps(
                    payload,
                    ensure_ascii=False,
                    sort_keys=True,
                    allow_nan=False,
                ),
            }
        ],
        "structuredContent": payload,
        "isError": not bool(payload.get("ok", True)),
    }
    meta = _widget_meta() if include_widget else {}
    if extra_meta is not None:
        if not is_json_object(extra_meta):
            raise ValueError("tool metadata is not a JSON object")
        meta.update(extra_meta)
    if meta:
        result["_meta"] = meta
    return result


def _recent_meeting_mentions(*, cancellation_event: threading.Event | None) -> JSONSchema:
    """Return a bounded catalog of recent readable notes for host-side filtering."""

    from meetings_home_bootstrap import read_home_bootstrap

    view = read_home_bootstrap(
        cancellation_event=cancellation_event,
        notes_limit=MEETING_MENTION_CATALOG_LIMIT,
        notes_max_age=timedelta(minutes=15),
    )["notes"]
    if view is None:
        view = read_backend_meetings_view(
            initial_limit=MEETING_MENTION_CATALOG_LIMIT,
            cancellation_event=cancellation_event,
        )
    if view["snapshotState"]["status"] not in {"ready", "empty"}:
        raise MeetingResourceReadError("Meeting suggestions are unavailable.")
    items: list[JSONValue] = []
    seen_uris: set[str] = set()
    now = datetime.now().astimezone()
    for row in view["notes"]:
        if row["fetchStatus"] != "fetchable" or row["isEmpty"]:
            continue
        # Keep the canonical projection's distinct Note and legacy Meeting routes.
        resource_link = row.get("resourceLink")
        if resource_link is None:
            continue
        uri = unquote(urlparse(resource_link).path.lstrip("/"))
        if uri in seen_uris:
            continue
        seen_uris.add(uri)
        try:
            # Date-only notes have no start time or timezone to convert.
            local_date = date.fromisoformat(row["startTime"])
            time_label = ""
        except ValueError:
            local_start = datetime.fromisoformat(
                row["startTime"].replace("Z", "+00:00")
            ).astimezone()
            local_date = local_start.date()
            time_label = f" · {local_start.strftime('%I:%M %p').lstrip('0')}"
        if local_date == now.date():
            date_label = "Today"
        elif local_date == now.date() - timedelta(days=1):
            date_label = "Yesterday"
        else:
            date_label = f"{local_date.strftime('%b')} {local_date.day}"
        description = date_label + time_label
        items.append(
            {
                "type": "resource_link",
                "uri": uri,
                "name": row["title"],
                "title": row["title"],
                "description": description,
                "mimeType": MEETING_RESOURCE_MIME,
                "icons": _meeting_resource_icons(),
            }
        )
    return {"items": items}


def meeting_resource_contents(
    uri: object,
    *,
    cancellation_event: threading.Event | None,
) -> JSONSchema:
    """Read one bounded meeting note through its canonical meeting id.

    Args:
        uri: Candidate canonical meeting resource URI.
        cancellation_event: Optional caller cancellation signal.

    Returns:
        One JSON-encoded authenticated meeting note resource.

    Raises:
        InvalidArguments: If the URI is not a canonical meeting resource.
        MeetingResourceReadError: If the authenticated note cannot be read.
    """

    if not isinstance(uri, str):
        raise InvalidArguments("meeting resource URI must be a string")
    read_source, canonical_id = _record_id_from_resource_uri(uri)
    try:
        note = get_record_interactions_client().get_note_by_canonical_id(
            canonical_id,
            read_source=read_source,
            cancellation_event=cancellation_event,
        )
    except RecordMeetingInteractionsBackendError:
        report_mcp_error(
            "interactions",
            "backend",
            mcp_build_timestamp=server_build_timestamp_utc(),
        )
        raise MeetingResourceReadError("Meeting resource is unavailable.") from None
    except (CodexAuthCancelled, RecordMeetingInteractionsCancelled, RecordHandleError):
        raise MeetingResourceReadError("Meeting resource is unavailable.") from None
    except (CodexAuthError, RecordMeetingInteractionsAuthError):
        raise MeetingResourceReadError("Meeting resource is unavailable.") from None
    return {
        "contents": [
            {
                "uri": uri,
                "mimeType": MEETING_RESOURCE_MIME,
                "text": json.dumps(
                    note,
                    ensure_ascii=True,
                    separators=(",", ":"),
                    sort_keys=True,
                ),
            }
        ]
    }


def handle_rpc(
    message: RPCMessage,
    *,
    cancellation_event: threading.Event | None = None,
    profile: str = DEFAULT_PROFILE,
) -> RPCResponse | None:
    """Dispatch one request through the Meetings application boundary.

    Args:
        message: Decoded JSON-RPC message.
        cancellation_event: Optional cooperative cancellation signal.
        profile: MCP tool profile used for application dispatch.

    Returns:
        A JSON-RPC response for requests, or ``None`` for notifications.
    """

    response = meetings_rpc.handle_rpc(
        message,
        # Python has no static module-interface type. Keep the one dynamic
        # composition seam here; meetings_rpc type-checks every use against
        # its closed service protocol.
        service=sys.modules[__name__],  # pyright: ignore[reportArgumentType]
        cancellation_event=cancellation_event,
        profile=profile,
    )
    if (
        profile == PROFILE_PRODUCTION
        and isinstance(message, dict)
        and message.get("method") == "initialize"
        and isinstance(response, dict)
        and "result" in response
        and "error" not in response
    ):
        try:
            report_mcp_ready()
        except Exception:
            # Lifecycle reporting must never affect MCP readiness.
            pass
    return response


def serve_rpc(
    input_stream: RPCInputStream,
    output_stream: RPCOutputStream,
    *,
    handler: RPCHandler = handle_rpc,
    maximum_background_requests: int = MAXIMUM_BACKGROUND_RPC_REQUESTS,
    maximum_lifecycle_requests: int = MAXIMUM_BACKGROUND_LIFECYCLE_RPC_REQUESTS,
    shutdown_grace_seconds: float = BACKGROUND_RPC_SHUTDOWN_GRACE_SECONDS,
    disconnect_observer: Callable[[], None] | None = None,
) -> None:
    """Serve JSON-RPC while keeping application state in this module.

    Args:
        input_stream: Binary newline-delimited JSON-RPC input.
        output_stream: Binary newline-delimited JSON-RPC output.
        handler: Application request handler.
        maximum_background_requests: Shared hosted-request outstanding bound.
        maximum_lifecycle_requests: Outstanding native lifecycle request bound.
        shutdown_grace_seconds: Cooperative worker shutdown deadline.
        disconnect_observer: Optional best-effort callback when input closes.

    Returns:
        ``None`` after EOF, output failure, or terminal input failure.
    """

    meetings_rpc.serve_rpc(
        input_stream,
        output_stream,
        handler=handler,
        maximum_background_requests=maximum_background_requests,
        maximum_lifecycle_requests=maximum_lifecycle_requests,
        shutdown_grace_seconds=shutdown_grace_seconds,
        disconnect_observer=disconnect_observer,
    )


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Serve the Meetings MCP App over stdio.",
    )
    parser.add_argument(
        "--profile",
        choices=SUPPORTED_PROFILES,
        default=DEFAULT_PROFILE,
    )
    arguments = parser.parse_args(argv)

    def configured_handler(
        message: RPCMessage,
        *,
        cancellation_event: threading.Event | None = None,
    ) -> RPCResponse | None:
        return handle_rpc(
            message,
            cancellation_event=cancellation_event,
            profile=arguments.profile,
        )

    warm_process_auth()
    process_auth_manager = get_process_auth_manager()
    interactions_client = get_record_interactions_client()
    interactions_client.start_discovery_rollout_lookup()
    interactions_client.start_required_update_polling(plugin_version=SERVER_VERSION)

    def close_owned_process_resources() -> None:
        interactions_client.stop_discovery_rollout_lookup()
        interactions_client.stop_required_update_polling()
        try:
            close_stream_transports(permanent=True)
        finally:
            process_auth_manager.close()

    try:
        serve_rpc(
            sys.stdin.buffer,
            sys.stdout.buffer,
            handler=configured_handler,
            disconnect_observer=close_owned_process_resources,
        )
    finally:
        interactions_client.stop_required_update_polling()
        interactions_client.stop_discovery_rollout_lookup()
        try:
            close_stream_transports(permanent=True)
        finally:
            close_process_auth()
