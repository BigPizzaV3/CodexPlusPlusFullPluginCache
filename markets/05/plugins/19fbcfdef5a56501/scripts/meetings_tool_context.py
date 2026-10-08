"""Validated request-local context shared by nested Meetings tool dispatch."""

from __future__ import annotations

import re
import sys
from collections.abc import Iterator
from contextlib import contextmanager
from contextvars import ContextVar

from meetings_client_policy import (
    STRUCTURED_SETTINGS_READ_TOOL,
    STRUCTURED_SETTINGS_UPDATE_TOOL,
    PluginClientContext,
    parse_plugin_client_context,
    update_version,
)
from meetings_host_context import get_current_codex_version, scoped_codex_version
from meetings_schema import is_json_object

RECORDING_APP_INSTANCE: ContextVar[str | None] = ContextVar("recording_app_instance", default=None)

CLIENT_CONTEXT: ContextVar[PluginClientContext | None] = ContextVar(
    "meetings_plugin_client_context", default=None
)


@contextmanager
def scoped_tool_arguments(
    name: str,
    arguments: object | None,
    *,
    app_ui_allowed: bool,
    host_app_version: str | None = None,
    recording_app_instance: object = None,
) -> Iterator[object | None]:
    """Strip validated context and restore both scopes even on failed nested calls."""
    codex_version = update_version(host_app_version) or get_current_codex_version()
    context = CLIENT_CONTEXT.get()
    if is_json_object(arguments) and "clientContext" in arguments:
        context = parse_plugin_client_context(
            name,
            arguments["clientContext"],
            request=arguments.get("request"),
            app_ui=app_ui_allowed,
            codex_version=codex_version,
        )
        arguments = {key: value for key, value in arguments.items() if key != "clientContext"}
    if context is not None and context.surface == "desktop" and codex_version:
        context = PluginClientContext(context.system_name, context.surface, codex_version)
    if context is None and (
        codex_version
        or name
        in {
            "meetings.takeNotes",
            "meetings.getSettings",
            "meetings.updateSettings",
            STRUCTURED_SETTINGS_READ_TOOL,
            STRUCTURED_SETTINGS_UPDATE_TOOL,
        }
    ):
        context = PluginClientContext(
            {"win32": "Windows", "darwin": "Darwin", "linux": "Linux"}.get(sys.platform, "unknown"),
            "desktop",
            codex_version,
        )
    # App metadata is not forwarded by every desktop host. Only the read-only
    # status tool accepts this argument; it never reaches the native protocol.
    if app_ui_allowed and name == "meetings.status" and is_json_object(arguments):
        if "appInstanceId" in arguments:
            recording_app_instance = arguments["appInstanceId"]
            arguments = {key: value for key, value in arguments.items() if key != "appInstanceId"}
    app_instance = RECORDING_APP_INSTANCE.get()
    if recording_app_instance is not None:
        # Malformed optional presentation metadata must never break Start/Stop.
        app_instance = (
            recording_app_instance
            if app_ui_allowed
            and name in {"meetings.status", "meetings.start", "meetings.stop"}
            and isinstance(recording_app_instance, str)
            and re.fullmatch(r"[a-f0-9]{64}", recording_app_instance) is not None
            else None
        )
    instance_token = RECORDING_APP_INSTANCE.set(app_instance)
    token = CLIENT_CONTEXT.set(context)
    try:
        with scoped_codex_version(context.codex_version if context is not None else ""):
            yield arguments
    finally:
        CLIENT_CONTEXT.reset(token)
        RECORDING_APP_INSTANCE.reset(instance_token)
