"""Typed app-control routing across supported native Meetings machines."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Generic

from meetings_app.models import NativeAppRuntime, NativeCaptureObservation
from meetings_app.platforms import (
    CompatibleOwnerOperations,
    CompatibleOwnerPlatformHandler,
    OwnerT,
    ProofT,
    UnsupportedCompatibleOwnerPlatformHandler,
    is_windows_registration,
    registration_for,
)
from native_runtime_types import PlatformRuntimeSpec
from recording_control_action_contract import (
    RECORDING_CONTROL_SAFE_INTEGER_MAX,
    ControlAction,
    ControlPlatform,
    control_action_arguments_are_valid,
    parse_control_platform,
)
from recording_status_contract import (
    RecordingNativeStatus,
    RecordingStartupRecovery,
    RecordingUploadPhase,
    is_recording_startup,
    is_recording_state,
    is_recording_upload,
    parse_recording_schema_compatibility,
)

from helpers import is_json


def _runtime_platform(status: Mapping[str, object]) -> ControlPlatform:
    try:
        value = status["platform"]
    except (KeyError, TypeError):
        return ControlPlatform.UNKNOWN
    return parse_control_platform(value)


def supports_compatible_idle_windows_platform(value: object) -> bool:
    """Nonthrowing Windows-family hint for one generated platform value."""

    registration = registration_for(parse_control_platform(value))
    return registration is not None and is_windows_registration(registration)


def supports_compatible_idle_windows_owner(status: Mapping[str, object]) -> bool:
    """Nonthrowing Windows-family hint for explicit Meetings callsites."""

    return supports_compatible_idle_windows_platform(_runtime_platform(status))


def _has_finalized_streamed_recording(
    state: Mapping[str, object],
    capture: NativeCaptureObservation,
    *,
    audio_bytes: int,
    require_streaming_session: bool,
) -> bool:
    """Trust only the signed owner's exact generated hosted-stream completion."""

    recording = capture.contract
    if recording is None or "lastRecording" not in recording:
        return False
    receipt = recording["lastRecording"]
    if (
        receipt is None
        or audio_bytes <= 0
        or "streamingCompleted" not in receipt
        or receipt["streamingCompleted"] is not True
        or "savedLocally" not in receipt
        or receipt["savedLocally"] is not False
        or "audioBytes" not in receipt
        or receipt["audioBytes"] != audio_bytes
        or "recordingId" not in receipt
        or type(receipt["recordingId"]) is not str
    ):
        return False

    if "sessionId" in receipt:
        session_id = receipt["sessionId"]
        if type(session_id) is not str or not control_action_arguments_are_valid(
            ControlAction.STOP,
            {"expectedSessionId": session_id},
        ):
            return False
    elif require_streaming_session:
        return False

    if "lastAudioSavedLocally" not in recording or recording["lastAudioSavedLocally"] is not False:
        return False

    upload = state["upload"] if "upload" in state else None
    return (
        is_recording_upload(upload)
        and "phase" in upload
        and upload["phase"] == RecordingUploadPhase.UPLOADED.value
        and "hasDurableReceipt" in upload
        and upload["hasDurableReceipt"] is False
        and "completedRecordingId" in upload
        and upload["completedRecordingId"] == receipt["recordingId"]
    )


def _has_finalized_remote_recording(
    capture: NativeCaptureObservation,
    *,
    audio_bytes: int,
    mixed_bytes: int,
    require_streaming_session: bool,
) -> bool:
    """Recognize a stopped remote-only capture without inspecting its outbox."""

    recording = capture.contract
    if recording is None or "lastRecording" not in recording:
        return False
    receipt = recording["lastRecording"]
    rust = receipt["rust"] if receipt is not None and "rust" in receipt else None
    if (
        receipt is None
        or audio_bytes <= 0
        or mixed_bytes != audio_bytes
        or "recordingId" not in receipt
        or type(receipt["recordingId"]) is not str
        or "stoppedAt" not in receipt
        or not receipt["stoppedAt"].strip()
        or "savedLocally" not in receipt
        or receipt["savedLocally"] is not False
        or "streamingCompleted" in receipt
        or (
            rust is not None
            and ("terminal" not in rust or rust["terminal"] != "host-attested-finalized")
        )
        or "audioBytes" not in receipt
        or receipt["audioBytes"] != audio_bytes
        or "lastAudioSavedLocally" not in recording
        or recording["lastAudioSavedLocally"] is not False
    ):
        return False

    if "sessionId" in receipt:
        session_id = receipt["sessionId"]
        if type(session_id) is not str or not control_action_arguments_are_valid(
            ControlAction.STOP,
            {"expectedSessionId": session_id},
        ):
            return False
    elif require_streaming_session:
        return False

    return True


def can_automatically_replace_owner(
    state: Mapping[str, object],
    *,
    require_streaming_session: bool = False,
) -> bool:
    """Protect active capture without making durable uploads an update fence."""

    try:
        status = state["status"]
        can_stop = state["canStop"]
    except (KeyError, TypeError):
        return False

    if "lastCaptureFailed" in state and state["lastCaptureFailed"] is not False:
        return False

    schema_present = "schemaVersion" in state
    schema_version = state["schemaVersion"] if schema_present else None
    if schema_present:
        generated_authority = dict(state)
        generated_authority.pop("recording", None)
        if not is_recording_state(generated_authority):
            return False
    compatibility = parse_recording_schema_compatibility(
        schema_version,
        field_present=schema_present,
    )
    if "startup" in state:
        startup = state["startup"]
        if not is_recording_startup(startup) or "recovery" not in startup:
            return False
        recovery = startup["recovery"]
        if recovery not in (
            RecordingStartupRecovery.READY.value,
            RecordingStartupRecovery.BLOCKED.value,
        ):
            return False
        attention = startup["attention"] if "attention" in startup else None
        if recovery == RecordingStartupRecovery.BLOCKED.value and (
            "canStart" not in state
            or state["canStart"] is not True
            or attention
            != {
                "kind": "startup-recovery-failed",
                "stage": "outbox",
                "outcome": "returned-false",
            }
            or ("admissionFenced" in state and state["admissionFenced"] is not False)
            or ("handoffQuiescent" in state and state["handoffQuiescent"] is not False)
        ):
            return False
        if attention is not None:
            if (
                "kind" in attention and attention["kind"] == "retained-audio-needs-manual-recovery"
            ) or ("stage" in attention and attention["stage"] == "native-scratch"):
                return False
    if "recording" in state:
        capture = NativeCaptureObservation.from_value(state["recording"])
        if capture is None:
            return False
        recording = capture.wire
        mixed_bytes = 0
        if "mixedBytes" in recording:
            mixed_value = recording["mixedBytes"]
            if (
                type(mixed_value) is not int
                or not 0 <= mixed_value <= RECORDING_CONTROL_SAFE_INTEGER_MAX
            ):
                return False
            mixed_bytes = mixed_value
        if "startedAt" in recording and recording["startedAt"] not in (None, ""):
            return False
        saved_locally: bool | None = None
        if "lastAudioSavedLocally" in recording:
            saved_value = recording["lastAudioSavedLocally"]
            if type(saved_value) is not bool:
                return False
            saved_locally = saved_value
        audio_bytes = 0
        if "lastAudioBytes" in recording:
            audio_value = recording["lastAudioBytes"]
            if type(audio_value) is not int or audio_value < 0:
                return False
            audio_bytes = audio_value
        receipt: dict[str, object] | None = None
        if "lastRecording" in recording:
            receipt_value = recording["lastRecording"]
            if receipt_value is not None and not is_json(receipt_value):
                return False
            receipt = receipt_value
            if receipt is not None and (
                (
                    not receipt
                    and (
                        saved_locally is not False
                        or "lastAudioBytes" not in recording
                        or audio_bytes != 0
                    )
                )
                or ("savedLocally" in receipt and type(receipt["savedLocally"]) is not bool)
            ):
                return False

        streaming_completed = (
            receipt is not None
            and "streamingCompleted" in receipt
            and receipt["streamingCompleted"] is True
        )
        if streaming_completed and not _has_finalized_streamed_recording(
            state,
            capture,
            audio_bytes=audio_bytes,
            require_streaming_session=require_streaming_session,
        ):
            return False

        finalized_remote_recording = not streaming_completed and _has_finalized_remote_recording(
            capture,
            audio_bytes=audio_bytes,
            mixed_bytes=mixed_bytes,
            require_streaming_session=require_streaming_session,
        )
        if (saved_locally is True or audio_bytes > 0) and not (
            streaming_completed or finalized_remote_recording
        ):
            if (
                receipt is None
                or "savedLocally" not in receipt
                or receipt["savedLocally"] is not True
            ):
                return False
            if audio_bytes > 0 and (
                saved_locally is False
                or (
                    "audioBytes" in receipt
                    and (
                        type(receipt["audioBytes"]) is not int
                        or receipt["audioBytes"] != audio_bytes
                    )
                )
            ):
                return False
        if (
            mixed_bytes > 0
            and not finalized_remote_recording
            and (
                saved_locally is not True
                or audio_bytes != mixed_bytes
                or receipt is None
                or "savedLocally" not in receipt
                or receipt["savedLocally"] is not True
                or "audioBytes" not in receipt
                or type(receipt["audioBytes"]) is not int
                or receipt["audioBytes"] != mixed_bytes
            )
        ):
            return False
    if "meetingId" in state:
        meeting_id = state["meetingId"]
        if meeting_id is not None and (type(meeting_id) is not str or meeting_id != ""):
            return False
    if ("canPause" in state and state["canPause"] is not False) or (
        "canResume" in state and state["canResume"] is not False
    ):
        return False
    return (
        compatibility.supports_recording_authority
        and status == RecordingNativeStatus.IDLE.value
        and can_stop is False
        and ("sessionId" not in state or state["sessionId"] in (None, ""))
        and ("startedAt" not in state or state["startedAt"] in (None, ""))
    )


def can_force_replace_owner_without_native_ack(
    state: Mapping[str, object],
    *,
    finalized_recording_is_durable: bool = False,
    require_streaming_session: bool = False,
) -> bool:
    """Require independent finalization proof before bypassing native consent."""

    if not can_automatically_replace_owner(
        state,
        require_streaming_session=require_streaming_session,
    ):
        return False

    capture = NativeCaptureObservation.from_value(
        state["recording"] if "recording" in state else None
    )
    if capture is None:
        return False
    recording = capture.wire
    receipt = recording["lastRecording"] if "lastRecording" in recording else None
    if receipt:
        if finalized_recording_is_durable is True:
            return True
        if capture.contract is None or "lastRecording" not in capture.contract:
            return False
        generated_receipt = capture.contract["lastRecording"]
        if generated_receipt is None or "rust" not in generated_receipt:
            return False
        rust = generated_receipt["rust"]
        return (
            rust is not None
            and "terminal" in rust
            and rust["terminal"] == "host-attested-finalized"
        )
    return (
        "lastAudioSavedLocally" in recording
        and recording["lastAudioSavedLocally"] is False
        and "lastAudioBytes" in recording
        and type(recording["lastAudioBytes"]) is int
        and recording["lastAudioBytes"] == 0
    )


@dataclass(frozen=True)
class MeetingsAppManager(Generic[OwnerT, ProofT]):
    """Resolve typed machine handlers while concrete handoff policy stays injected."""

    host: str
    resolve_spec: Callable[[str], PlatformRuntimeSpec]
    operations: CompatibleOwnerOperations[OwnerT, ProofT]

    def can_automatically_replace_owner(self, state: Mapping[str, object]) -> bool:
        """Use one portable capture-only policy for automatic owner recovery."""

        return can_automatically_replace_owner(
            state,
            require_streaming_session=self.host == "win32",
        )

    def can_force_replace_owner_without_native_ack(
        self,
        state: Mapping[str, object],
        *,
        finalized_recording_is_durable: bool = False,
    ) -> bool:
        """Separate capture-idle observations from destructive finalization proof."""

        return can_force_replace_owner_without_native_ack(
            state,
            finalized_recording_is_durable=finalized_recording_is_durable,
            require_streaming_session=self.host == "win32",
        )

    def resolve_platform_spec(
        self,
        value: object,
    ) -> tuple[ControlPlatform, PlatformRuntimeSpec]:
        platform = parse_control_platform(value)
        registration = registration_for(platform)
        if registration is None:
            self.operations.reject("native update platform is unsupported")
        if self.host != registration.expected_host:
            self.operations.reject("native update platform does not match host")
        spec = self.resolve_spec(platform.value)
        if spec.platform_key != platform.value:
            self.operations.reject("native update platform does not match")
        return platform, spec

    def resolve_handler(
        self,
        status: Mapping[str, object],
    ) -> CompatibleOwnerPlatformHandler:
        platform = _runtime_platform(status)
        registration = registration_for(platform)
        if registration is None:
            return UnsupportedCompatibleOwnerPlatformHandler()
        resolved_platform, spec = self.resolve_platform_spec(platform.value)
        runtime = NativeAppRuntime(
            status=status,
            platform=resolved_platform,
            spec=spec,
        )
        return registration.factory(runtime)

    def authenticate_update_owner(
        self,
        status: Mapping[str, object],
        *,
        preverified_source: ProofT | None = None,
    ) -> tuple[CompatibleOwnerPlatformHandler, OwnerT]:
        """Route one explicit Update through its typed platform policy."""

        handler = self.resolve_handler(status)
        owner = handler.authenticate_compatible_owner(
            self.operations,
            allow_durable_handoff=handler.family == "windows",
            preverified_source=preverified_source,
        )
        return handler, owner

    def authenticate_compatible_idle_force_start_owner(
        self,
        status: Mapping[str, object],
    ) -> tuple[CompatibleOwnerPlatformHandler, OwnerT] | None:
        """Authenticate an idle Force Start owner on either supported platform."""

        handler = self.resolve_handler(status)
        if handler.runtime is None:
            return None
        owner = handler.authenticate_compatible_owner(self.operations)
        return handler, owner

    def preverify_staged_update_source(
        self,
        status: Mapping[str, object],
    ) -> ProofT | None:
        if not supports_compatible_idle_windows_owner(status):
            return None
        handler = self.resolve_handler(status)
        return handler.preverify_staged_update_source(self.operations)
