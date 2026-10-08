"""Metadata-only consumer of Record API's MeetingsTrackRequest contract."""

from __future__ import annotations

from enum import Enum
from typing import Literal, TypedDict
from uuid import UUID

from helpers import is_json


class PluginEventName(str, Enum):
    OPENED = "opened"
    ONBOARDING = "onboarding"
    CALENDAR_CONNECT = "calendar_connect"
    RECORDING_START = "recording_start"
    RECORDING_STOP = "recording_stop"
    SURFACE_VIEWED = "surface_viewed"
    ONBOARDING_STARTED = "onboarding_started"
    ONBOARDING_COMPLETED = "onboarding_completed"


class PluginEventSurface(str, Enum):
    HOME = "home"
    SETTINGS = "settings"
    ONBOARDING = "onboarding"


class _OptionalMetadata(TypedDict, total=False):
    durationMs: int
    attemptId: str
    stage: Literal["started", "step_viewed", "completed", "succeeded", "failed"]
    step: Literal["calendars", "context", "completion"]
    provider: Literal["google", "outlook"]
    recordingMode: Literal["local"]
    failureReason: Literal["setup_link_failed"]


class PluginEventMetadata(_OptionalMetadata):
    surface: PluginEventSurface


class PluginAnalyticsEvent(TypedDict):
    clientEventId: str
    eventName: PluginEventName
    metadata: PluginEventMetadata


class PluginAnalyticsAcceptance(TypedDict):
    accepted: bool


def parse_analytics_event(value: object) -> PluginAnalyticsEvent:
    """Validate the plugin's bounded projection of the Record tracking contract.

    Args:
        value: Untrusted app payload, excluding gateway ownership fields.

    Returns:
        A metadata-only event. Raises ValueError for unsupported input.
    """
    if not is_json(value) or set(value) != {"clientEventId", "eventName", "metadata"}:
        raise ValueError("Invalid analytics event")
    event_id = value["clientEventId"]
    event_name = value["eventName"]
    metadata = value["metadata"]
    if (
        not isinstance(event_id, str)
        or len(event_id) != 36
        or str(UUID(event_id)) != event_id
        or not isinstance(event_name, str)
        or not is_json(metadata)
        or not isinstance(metadata.get("surface"), str)
    ):
        raise ValueError("Invalid analytics event")
    name = PluginEventName(event_name)
    required = {"surface"}
    allowed = {"surface", "durationMs"}
    families = {
        PluginEventName.ONBOARDING,
        PluginEventName.CALENDAR_CONNECT,
        PluginEventName.RECORDING_START,
        PluginEventName.RECORDING_STOP,
    }
    if name in families:
        required |= {"attemptId", "stage"}
        allowed |= {"attemptId", "stage"}
        if name == PluginEventName.ONBOARDING:
            required.add("step")
            allowed.add("step")
        else:
            allowed.add("failureReason")
        if name == PluginEventName.CALENDAR_CONNECT:
            required.add("provider")
            allowed.add("provider")
        if name in {PluginEventName.RECORDING_START, PluginEventName.RECORDING_STOP}:
            required.add("recordingMode")
            allowed.add("recordingMode")
    if not required <= set(metadata) <= allowed:
        raise ValueError("Invalid analytics metadata fields")
    parsed: PluginEventMetadata = {"surface": PluginEventSurface(metadata["surface"])}
    if "durationMs" in metadata:
        duration = metadata["durationMs"]
        if type(duration) is not int or not 0 <= duration <= 3_600_000:
            raise ValueError("Invalid analytics duration")
        parsed["durationMs"] = duration
    if name in families:
        attempt_id = metadata["attemptId"]
        if not isinstance(attempt_id, str) or str(UUID(attempt_id)) != attempt_id:
            raise ValueError("Invalid analytics attempt ID")
        parsed["attemptId"] = attempt_id
        stage = metadata["stage"]
        if stage == "started" and "durationMs" in metadata:
            raise ValueError("Started attempts cannot have a duration")
        if name == PluginEventName.ONBOARDING:
            if stage not in ("started", "step_viewed", "completed"):
                raise ValueError("Invalid onboarding stage")
            if stage == "started":
                parsed["stage"] = "started"
            elif stage == "step_viewed":
                parsed["stage"] = "step_viewed"
            else:
                parsed["stage"] = "completed"
            step = metadata["step"]
            if step == "calendars":
                parsed["step"] = "calendars"
            elif step == "context":
                parsed["step"] = "context"
            elif step == "completion":
                parsed["step"] = "completion"
            else:
                raise ValueError("Invalid onboarding step")
            if parsed["surface"] != PluginEventSurface.ONBOARDING:
                raise ValueError("Invalid onboarding surface")
        else:
            if stage == "started":
                parsed["stage"] = "started"
            elif stage == "succeeded":
                parsed["stage"] = "succeeded"
            elif stage == "failed":
                parsed["stage"] = "failed"
            else:
                raise ValueError("Invalid attempt stage")
            reason = metadata.get("failureReason")
            if (stage == "failed") != (reason is not None):
                raise ValueError("Only failed attempts require a failure reason")
            if reason is not None:
                if name == PluginEventName.CALENDAR_CONNECT and reason == "setup_link_failed":
                    parsed["failureReason"] = "setup_link_failed"
                else:
                    raise ValueError("Invalid failure reason")
        if name == PluginEventName.CALENDAR_CONNECT:
            if metadata["provider"] == "google":
                parsed["provider"] = "google"
            elif metadata["provider"] == "outlook":
                parsed["provider"] = "outlook"
            else:
                raise ValueError("Invalid calendar provider")
        if name in {PluginEventName.RECORDING_START, PluginEventName.RECORDING_STOP}:
            if parsed["stage"] not in ("started", "succeeded"):
                raise ValueError("Invalid recording stage")
            if metadata["recordingMode"] != "local":
                raise ValueError("Invalid recording mode")
            parsed["recordingMode"] = "local"
    return PluginAnalyticsEvent(
        clientEventId=event_id, eventName=PluginEventName(event_name), metadata=parsed
    )
