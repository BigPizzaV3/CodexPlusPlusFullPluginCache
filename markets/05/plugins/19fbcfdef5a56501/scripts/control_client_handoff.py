"""Authenticated cooperative owner handoff and fail-closed recovery."""

from __future__ import annotations

import stat
import threading
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from os import stat_result
from pathlib import Path
from typing import TYPE_CHECKING, NoReturn

import control_client
import control_client_live_handoff as _control_client_live_handoff
from control_projection import (
    compatible_darwin_release_identity,
    compatible_existing_owner_state,
    compatible_read_only_settings_owner_state,
)
from control_protocol import (
    ControlUnavailable as ProtocolControlUnavailable,
)
from control_protocol import compatible_native_release_version
from control_protocol import disconnected_state as protocol_disconnected_state
from control_transport.discovery import StreamDiscovery, require_stream_owner
from control_windows_identity import (
    terminate_verified_windows_owner_process as _terminate_verified_windows_owner_process,
)
from meetings_app import owner_recovery
from meetings_app.handoff import (
    HandoffProgress,
    HandoffStateObservation,
)
from meetings_app.manager import (
    MeetingsAppManager,
)
from meetings_app.models import NativeAppRuntime
from meetings_app.platforms import CompatibleOwnerOperations
from native_runtime_types import NativeRuntimeStatus, PlatformRuntimeSpec
from recording_control_action_contract import (
    ControlAction,
    ControlPlatform,
    parse_control_platform,
)
from recording_control_stream_contract import ControlStreamDescriptor, is_control_stream_descriptor
from recording_status_contract import (
    RecordingNativeStatus,
    RecordingStartupRecovery,
    RecordingState,
    RecordingUploadPhase,
    is_recording_state,
    parse_recording_schema_compatibility,
)

if TYPE_CHECKING:
    from companion_client import CompanionClient


class RecordingCaptureActive(ProtocolControlUnavailable):
    """Refuse owner replacement while authenticated recording is unfinished."""


@dataclass(frozen=True)
class _ExplicitForceRecordingObservation:
    """Pair generated recording authority with its authenticated stream state."""

    state: RecordingState
    owner_state: Mapping[str, object]


@dataclass(frozen=True)
class _VerifiedSelectedRuntime:
    """Canonical selected companion and the private identity proven for it."""

    manager: control_client.RuntimeManager
    status: NativeRuntimeStatus
    info: dict[str, object]
    executable_sha256: str
    platform: ControlPlatform
    spec: PlatformRuntimeSpec


@dataclass(frozen=True)
class _PreverifiedWindowsStagedUpdateSource:
    """One in-process proof that the old Windows source was canonical pre-install."""

    selected_runtime: _VerifiedSelectedRuntime
    runtime_identity: tuple[object, ...]
    source_root: Path
    family_root: Path


terminate_verified_windows_owner_process = _terminate_verified_windows_owner_process


_COMPATIBLE_DARWIN_CONTROL_PLATFORMS = frozenset(
    {
        ControlPlatform.DARWIN_UNIVERSAL,
        ControlPlatform.DARWIN_ARM64,
        ControlPlatform.DARWIN_X64,
    }
)
_COMPATIBLE_WINDOWS_CONTROL_PLATFORMS = frozenset(
    {
        ControlPlatform.WINDOWS_X64,
        ControlPlatform.WINDOWS_ARM64,
    }
)
_WINDOWS_SELECTED_RUNTIME_IDENTITY_FIELDS = (
    "installed",
    "source",
    "version",
    "releaseVersion",
    "platform",
    "artifactKind",
    "appPath",
    "_sourcePluginRoot",
    "_executableSHA256",
    "_executableDevice",
    "_executableInode",
)
_COMPATIBLE_DARWIN_PLATFORMS = frozenset(
    platform.value for platform in _COMPATIBLE_DARWIN_CONTROL_PLATFORMS
)
_AUTOMATIC_GRACEFUL_EXIT_TIMEOUT_SECONDS = 0.20


def _reject_native_handoff_platform(message: str) -> NoReturn:
    raise control_client.ControlUnavailable(message)


def _resolve_native_handoff_spec(platform_key: str) -> PlatformRuntimeSpec:
    try:
        return control_client.runtime_spec_for(platform_key)
    except control_client.NativeRuntimeError as exc:
        raise control_client.ControlUnavailable("native update platform is unsupported") from exc


def _authenticate_compatible_darwin_owner_for_platform(
    runtime: NativeAppRuntime,
) -> tuple[Path, control_client.RawControlDescriptor]:
    return _require_authenticated_compatible_owner(runtime.status)


def _authenticate_compatible_windows_owner_for_platform(
    runtime: NativeAppRuntime,
    allow_durable_handoff: bool,
    preverified_source: _PreverifiedWindowsStagedUpdateSource | None,
) -> tuple[Path, control_client.RawControlDescriptor]:
    if not allow_durable_handoff and preverified_source is None:
        return _require_authenticated_compatible_windows_force_update_owner(runtime.status)
    return _require_authenticated_compatible_windows_force_update_owner(
        runtime.status,
        allow_durable_handoff=allow_durable_handoff,
        preverified_source=preverified_source,
    )


def _preverify_compatible_windows_source_for_platform(
    runtime: NativeAppRuntime,
) -> _PreverifiedWindowsStagedUpdateSource:
    return preverify_compatible_windows_staged_update_source(runtime.status)


def _compatible_owner_operations() -> CompatibleOwnerOperations[
    tuple[Path, control_client.RawControlDescriptor],
    _PreverifiedWindowsStagedUpdateSource,
]:
    return CompatibleOwnerOperations(
        authenticate_darwin=_authenticate_compatible_darwin_owner_for_platform,
        authenticate_windows=_authenticate_compatible_windows_owner_for_platform,
        preverify_windows=_preverify_compatible_windows_source_for_platform,
        reject=_reject_native_handoff_platform,
    )


def _meetings_app_manager() -> MeetingsAppManager[
    tuple[Path, control_client.RawControlDescriptor],
    _PreverifiedWindowsStagedUpdateSource,
]:
    return MeetingsAppManager(
        host=control_client.sys.platform,
        resolve_spec=_resolve_native_handoff_spec,
        operations=_compatible_owner_operations(),
    )


def _typed_native_handoff_spec(
    value: object,
) -> tuple[ControlPlatform, PlatformRuntimeSpec]:
    """Resolve one generated desktop platform to its exact host-bound spec."""

    return _meetings_app_manager().resolve_platform_spec(value)


def preverify_compatible_staged_update_source(
    runtime: Mapping[str, object],
) -> _PreverifiedWindowsStagedUpdateSource | None:
    """Capture any platform-specific pre-install proof for explicit staged Update."""

    return _meetings_app_manager().preverify_staged_update_source(runtime)


def _verified_compatible_owner_image(
    value: control_client.RawControlDescriptor,
    spec: PlatformRuntimeSpec,
) -> tuple[Path, dict[str, object]]:
    """Re-attest the exact signed owner executable."""

    if (
        value.get("platform") not in _COMPATIBLE_DARWIN_PLATFORMS
        or value.get("bundleIdentifier") != control_client.BUNDLE_ID
    ):
        raise control_client.ControlUnavailable("native owner identity is incompatible")
    app_path = control_client._resolved_path(
        value.get("bundlePath"),
        message="native owner app identity is unavailable",
    )
    executable = control_client._resolved_path(
        value.get("executablePath"),
        message="native owner executable identity is unavailable",
    )
    if executable != control_client._expected_executable_path(app_path, spec):
        raise control_client.ControlUnavailable("native owner executable does not match")
    digest = control_client._optional_darwin_executable_sha256(value)
    identity = control_client._optional_darwin_executable_file_identity(value)
    if digest is None or identity is None:
        raise control_client.ControlUnavailable("native owner executable proof is missing")
    before = executable.stat()
    if (before.st_dev, before.st_ino) != identity:
        raise control_client.ControlUnavailable("native owner executable identity changed")
    if not control_client.hmac.compare_digest(
        control_client.sha256_regular_file(executable), digest
    ):
        raise control_client.ControlUnavailable("native owner executable digest changed")
    after = executable.stat()
    if (after.st_dev, after.st_ino) != identity:
        raise control_client.ControlUnavailable("native owner executable identity changed")
    control_client.validate_handoff_app(app_path, spec)
    import native_runtime

    info, verified_executable, _helper = native_runtime._load_app_metadata(app_path, spec)
    marketing_version = info.get("CFBundleShortVersionString")
    release_version = native_runtime._plugin_bundle_release_version(info)
    owner_version = value.get("appVersion")
    if (
        verified_executable != executable
        or not compatible_native_release_version(marketing_version)
        or not isinstance(owner_version, str)
        or owner_version not in (marketing_version, release_version)
    ):
        raise control_client.ControlUnavailable("native owner app version does not match")
    final = verified_executable.stat()
    if (final.st_dev, final.st_ino) != identity or not control_client.hmac.compare_digest(
        control_client.sha256_regular_file(verified_executable), digest
    ):
        raise control_client.ControlUnavailable("native owner executable identity changed")
    return app_path, info


def _verified_compatible_selected_runtime(
    runtime: Mapping[str, object],
) -> _VerifiedSelectedRuntime:
    """Force-verify the canonical selected runtime."""

    platform, spec = _typed_native_handoff_spec(runtime.get("platform"))
    if platform not in _COMPATIBLE_DARWIN_CONTROL_PLATFORMS:
        raise control_client.ControlUnavailable("compatible owner is Darwin-only")
    manager = control_client.RuntimeManager()
    verified = manager.status(force_verify=True)
    if (
        verified.get("installed") is not True
        or verified.get("source") != "plugin-bundled"
        or verified.get("platform") not in _COMPATIBLE_DARWIN_PLATFORMS
        or verified.get("artifactKind") != "macos-app-bundle"
        or not compatible_native_release_version(verified.get("version"))
        or any(
            runtime.get(field) != verified.get(field)
            for field in (
                "installed",
                "source",
                "version",
                "platform",
                "artifactKind",
                "appPath",
                "_sourcePluginRoot",
                "_executableSHA256",
                "_executableDevice",
                "_executableInode",
            )
        )
    ):
        raise control_client.ControlUnavailable("native selected runtime is not verified")
    selected = control_client._resolved_path(
        verified.get("appPath"),
        message="native selected app identity is unavailable",
    )
    source, family = control_client._runtime_handoff_source(verified, selected, spec)
    control_client.require_canonical_plugin_registration(source, family)
    import native_runtime

    selected_info, selected_executable, _helper = native_runtime._load_app_metadata(
        selected,
        spec,
    )
    selected_metadata = selected_executable.stat()
    executable_sha256 = verified.get("_executableSHA256")
    if (
        not isinstance(executable_sha256, str)
        or (selected_metadata.st_dev, selected_metadata.st_ino)
        != (verified.get("_executableDevice"), verified.get("_executableInode"))
        or not control_client.hmac.compare_digest(
            control_client.sha256_regular_file(selected_executable),
            executable_sha256,
        )
        or selected_info.get("CFBundleShortVersionString") != verified.get("version")
    ):
        raise control_client.ControlUnavailable("native selected executable changed")
    final = selected_executable.stat()
    if (final.st_dev, final.st_ino) != (selected_metadata.st_dev, selected_metadata.st_ino):
        raise control_client.ControlUnavailable("native selected executable changed")
    return _VerifiedSelectedRuntime(
        manager=manager,
        status=verified,
        info=selected_info,
        executable_sha256=executable_sha256,
        platform=platform,
        spec=spec,
    )


def _windows_selected_runtime_identity(
    runtime: Mapping[str, object],
) -> tuple[object, ...]:
    return tuple(runtime.get(field) for field in _WINDOWS_SELECTED_RUNTIME_IDENTITY_FIELDS)


def _revalidate_preverified_windows_staged_update_source(
    runtime: Mapping[str, object],
    proof: _PreverifiedWindowsStagedUpdateSource,
) -> _VerifiedSelectedRuntime:
    """Rebind one pre-install canonical proof to the same immutable stable executable."""

    platform, spec = _typed_native_handoff_spec(runtime.get("platform"))
    selected_runtime = proof.selected_runtime
    if (
        platform not in _COMPATIBLE_WINDOWS_CONTROL_PLATFORMS
        or selected_runtime.platform is not platform
        or selected_runtime.spec != spec
        or _windows_selected_runtime_identity(runtime) != proof.runtime_identity
        or _windows_selected_runtime_identity(selected_runtime.status) != proof.runtime_identity
        or selected_runtime.status.get("_sourcePluginRoot") != str(proof.source_root)
        or control_client.plugin_cache_family_root(
            proof.source_root,
            allow_missing=True,
        )
        != proof.family_root
    ):
        raise control_client.ControlUnavailable("native selected runtime is not verified")
    selected = control_client._resolved_path(
        selected_runtime.status.get("appPath"),
        message="native selected app identity is unavailable",
    )
    try:
        stable = control_client._is_stable_runtime_artifact(
            selected,
            spec,
            require_active=False,
        )
        selected_metadata = selected.stat()
        actual_digest = control_client.sha256_regular_file(selected)
    except (control_client.NativeRuntimeError, OSError) as exc:
        raise control_client.ControlUnavailable("native selected executable changed") from exc
    if (
        not stable
        or (selected_metadata.st_dev, selected_metadata.st_ino)
        != (
            selected_runtime.status.get("_executableDevice"),
            selected_runtime.status.get("_executableInode"),
        )
        or not control_client.hmac.compare_digest(
            actual_digest,
            selected_runtime.executable_sha256,
        )
    ):
        raise control_client.ControlUnavailable("native selected executable changed")
    final = selected.stat()
    if (final.st_dev, final.st_ino) != (selected_metadata.st_dev, selected_metadata.st_ino):
        raise control_client.ControlUnavailable("native selected executable changed")
    return selected_runtime


def preverify_compatible_windows_staged_update_source(
    runtime: Mapping[str, object],
) -> _PreverifiedWindowsStagedUpdateSource:
    """Mint one private old-root proof before a staged install moves registration."""

    selected_runtime = _verified_compatible_windows_selected_runtime(runtime)
    selected = control_client._resolved_path(
        selected_runtime.status.get("appPath"),
        message="native selected app identity is unavailable",
    )
    if not control_client._is_stable_runtime_artifact(
        selected,
        selected_runtime.spec,
        require_active=True,
    ):
        raise control_client.ControlUnavailable("native owner is not using the stable runtime")
    source, family = control_client._runtime_handoff_source(
        selected_runtime.status,
        selected,
        selected_runtime.spec,
    )
    return _PreverifiedWindowsStagedUpdateSource(
        selected_runtime=selected_runtime,
        runtime_identity=_windows_selected_runtime_identity(selected_runtime.status),
        source_root=source,
        family_root=family,
    )


def _verified_compatible_windows_selected_runtime(
    runtime: Mapping[str, object],
    *,
    preverified_source: _PreverifiedWindowsStagedUpdateSource | None = None,
) -> _VerifiedSelectedRuntime:
    """Force-verify the selected Windows executable before replacing a predecessor."""

    if preverified_source is not None:
        return _revalidate_preverified_windows_staged_update_source(runtime, preverified_source)
    platform, spec = _typed_native_handoff_spec(runtime.get("platform"))
    if platform not in _COMPATIBLE_WINDOWS_CONTROL_PLATFORMS:
        raise control_client.ControlUnavailable("compatible Windows owner is unavailable")
    manager = control_client.RuntimeManager()
    verified = manager.status(force_verify=True)
    if (
        verified.get("installed") is not True
        or verified.get("source") != "plugin-bundled"
        or not control_client._is_windows_platform_key(verified.get("platform"))
        or verified.get("artifactKind") != "windows-executable"
        or any(
            runtime.get(field) != verified.get(field)
            for field in _WINDOWS_SELECTED_RUNTIME_IDENTITY_FIELDS
        )
    ):
        raise control_client.ControlUnavailable("native selected runtime is not verified")
    selected = control_client._resolved_path(
        verified.get("appPath"),
        message="native selected app identity is unavailable",
    )
    source, family = control_client._runtime_handoff_source(verified, selected, spec)
    control_client.require_canonical_plugin_registration(source, family)
    selected_metadata = selected.stat()
    executable_sha256 = verified.get("_executableSHA256")
    if (
        not isinstance(executable_sha256, str)
        or (selected_metadata.st_dev, selected_metadata.st_ino)
        != (verified.get("_executableDevice"), verified.get("_executableInode"))
        or not control_client.hmac.compare_digest(
            control_client.sha256_regular_file(selected),
            executable_sha256,
        )
    ):
        raise control_client.ControlUnavailable("native selected executable changed")
    final = selected.stat()
    if (final.st_dev, final.st_ino) != (selected_metadata.st_dev, selected_metadata.st_ino):
        raise control_client.ControlUnavailable("native selected executable changed")
    return _VerifiedSelectedRuntime(
        manager=manager,
        status=verified,
        info={},
        executable_sha256=executable_sha256,
        platform=platform,
        spec=spec,
    )


def authenticated_compatible_existing_owner(
    runtime: Mapping[str, object],
    *,
    cancellation_event: threading.Event | None = None,
) -> tuple[Path, control_client.RawControlDescriptor, control_client.RawControlPayload] | None:
    """Prove one authenticated, protected desktop recorder."""

    return _authenticated_existing_owner(
        runtime,
        state_is_safe=compatible_existing_owner_state,
        cancellation_event=cancellation_event,
    )


def authenticated_read_only_settings_owner(
    runtime: Mapping[str, object],
    *,
    cancellation_event: threading.Event | None = None,
) -> tuple[Path, control_client.RawControlDescriptor, control_client.RawControlPayload] | None:
    """Prove an exact protected owner for strictly read-only native settings."""

    return _authenticated_existing_owner(
        runtime,
        state_is_safe=compatible_read_only_settings_owner_state,
        cancellation_event=cancellation_event,
    )


def _require_authenticated_compatible_owner(
    runtime: Mapping[str, object],
    *,
    descriptor_is_safe: Callable[[control_client.RawControlDescriptor], bool] | None = None,
) -> tuple[Path, control_client.RawControlDescriptor]:
    """Authenticate one exact stream owner compatible with the selected runtime."""

    if parse_control_platform(runtime.get("platform")) in _COMPATIBLE_WINDOWS_CONTROL_PLATFORMS:
        root, value = _require_authenticated_compatible_windows_force_update_owner(
            runtime,
            allow_durable_handoff=True,
        )
        if descriptor_is_safe is not None and not descriptor_is_safe(value):
            raise control_client.ControlUnavailable("native owner descriptor is incompatible")
        return root, value

    selected_runtime = _verified_compatible_selected_runtime(runtime)
    if selected_runtime.platform not in _COMPATIBLE_DARWIN_CONTROL_PLATFORMS:
        raise control_client.ControlUnavailable("compatible owner is Darwin-only")
    root, value = control_client.descriptor(
        runtime=selected_runtime.status,
        allow_stale_owner=True,
    )
    candidate: object = value
    if not is_control_stream_descriptor(candidate):
        raise control_client.ControlUnavailable("native control stream descriptor is malformed")
    control_client._validate_descriptor_platform_binding(value, selected_runtime.status)
    if descriptor_is_safe is not None and not descriptor_is_safe(value):
        raise control_client.ControlUnavailable("native owner descriptor is incompatible")
    require_stream_owner(root, candidate, peer_pid=candidate["pid"])
    _owner_path, owner_info = _verified_compatible_owner_image(value, selected_runtime.spec)
    owner_release = selected_runtime.manager._native_release_version_key(
        compatible_darwin_release_identity(owner_info)
    )
    selected_release = selected_runtime.manager._native_release_version_key(
        compatible_darwin_release_identity(selected_runtime.info)
    )
    owner_digest = candidate.get("executableSHA256")
    if not isinstance(owner_digest, str):
        raise control_client.ControlUnavailable("native owner executable identity is unavailable")
    if owner_release > selected_release or (
        owner_release == selected_release
        and not control_client.hmac.compare_digest(
            owner_digest,
            selected_runtime.executable_sha256,
        )
    ):
        raise control_client.ControlUnavailable("native owner release is incompatible")
    require_stream_owner(root, candidate, peer_pid=candidate["pid"])
    return root, value


def _require_authenticated_compatible_windows_force_update_owner(
    runtime: Mapping[str, object],
    *,
    allow_durable_handoff: bool = False,
    preverified_source: _PreverifiedWindowsStagedUpdateSource | None = None,
) -> tuple[Path, control_client.RawControlDescriptor]:
    """Authenticate one exact Windows stream owner for confirmed replacement."""

    selected_runtime = _verified_compatible_windows_selected_runtime(
        runtime,
        preverified_source=preverified_source,
    )
    if selected_runtime.platform not in _COMPATIBLE_WINDOWS_CONTROL_PLATFORMS:
        raise control_client.ControlUnavailable("compatible Windows owner is unavailable")
    root, value = control_client.descriptor(
        runtime=selected_runtime.status,
        allow_stale_owner=True,
    )
    candidate: object = value
    if not is_control_stream_descriptor(candidate):
        raise control_client.ControlUnavailable("native control stream descriptor is malformed")
    control_client._validate_descriptor_platform_binding(value, selected_runtime.status)
    if not control_client._is_windows_platform_key(candidate["platform"]):
        raise control_client.ControlUnavailable("native owner descriptor is incompatible")
    require_stream_owner(root, candidate, peer_pid=candidate["pid"])
    if not allow_durable_handoff:
        _require_idle_explicit_recording_state(root, value)
        require_stream_owner(root, candidate, peer_pid=candidate["pid"])
    return root, value


def _authenticated_existing_owner(
    runtime: Mapping[str, object],
    *,
    state_is_safe: Callable[[object], bool],
    response_state_is_safe: Callable[[object], bool] | None = None,
    descriptor_is_safe: Callable[[control_client.RawControlDescriptor], bool] | None = None,
    cancellation_event: threading.Event | None = None,
) -> tuple[Path, control_client.RawControlDescriptor, control_client.RawControlPayload] | None:
    """Authenticate one live owner against its action-specific recording policy."""

    try:
        if cancellation_event is not None and cancellation_event.is_set():
            return None
        root, value = _require_authenticated_compatible_owner(
            runtime,
            descriptor_is_safe=descriptor_is_safe,
        )
        candidate: object = value
        if not is_control_stream_descriptor(candidate):
            return None
        require_stream_owner(root, candidate, peer_pid=candidate["pid"])
        state = control_client.stream_owner_state(root, candidate)
        if state is None or not is_recording_state(state) or not state_is_safe(state):
            return None
        require_stream_owner(root, candidate, peer_pid=candidate["pid"])
        response = control_client.ControlClient()._call_with_descriptor(
            root,
            value,
            ControlAction.STATUS.value,
            timeout_seconds=control_client.WINDOWS_ACTIVE_STATUS_TIMEOUT_SECONDS,
            arguments={},
            cancellation_event=cancellation_event,
        )
        if response.get("ok") is not True or not (response_state_is_safe or state_is_safe)(
            response.get("state")
        ):
            return None
        require_stream_owner(root, candidate, peer_pid=candidate["pid"])
        return root, value, response
    except (
        control_client.ControlUnavailable,
        control_client.NativeRuntimeError,
        OSError,
        TypeError,
        ValueError,
    ):
        return None


def _has_resumable_outbox_capabilities(value: object) -> bool:
    """Require both explicitly advertised, authenticated handoff contracts."""

    if not isinstance(value, dict):
        return False
    capabilities = value.get("capabilities")
    return (
        isinstance(capabilities, list)
        and all(isinstance(capability, str) for capability in capabilities)
        and control_client.UPDATE_HANDOFF_WORK_FENCE_CAPABILITY in capabilities
        and control_client.UPDATE_HANDOFF_RESUMABLE_OUTBOX_CAPABILITY in capabilities
    )


def _has_interruptible_outbox_capabilities(value: object) -> bool:
    """Require authenticated authorization before interrupting an active upload."""

    if not isinstance(value, dict):
        return False
    capabilities = value.get("capabilities")
    return (
        isinstance(capabilities, list)
        and all(isinstance(capability, str) for capability in capabilities)
        and control_client.UPDATE_HANDOFF_WORK_FENCE_CAPABILITY in capabilities
        and control_client.UPDATE_HANDOFF_RESUMABLE_OUTBOX_V2_CAPABILITY in capabilities
    )


def _has_saved_resumable_recording(value: object) -> bool:
    """Trust only an authenticated, finalized native recording receipt."""

    if not isinstance(value, dict):
        return False
    recording = value.get("recording")
    if not isinstance(recording, dict):
        return False
    receipt = recording.get("lastRecording")
    return isinstance(receipt, dict) and receipt.get("savedLocally") is True


def _has_resumable_completed_outbox(value: object) -> bool:
    """Recognize completed-status projections backed by native v2 work fencing."""

    if not isinstance(value, dict) or not _has_interruptible_outbox_capabilities(value):
        return False
    upload = value.get("upload")
    if not isinstance(upload, dict) or (
        "hasDurableReceipt" in upload and type(upload["hasDurableReceipt"]) is not bool
    ):
        return False
    pending_count = upload.get("pendingCount")
    if not (
        type(pending_count) is int
        and 0 < pending_count <= control_client.MAXIMUM_JAVASCRIPT_SAFE_INTEGER
    ):
        return False
    phase = upload.get("phase")
    if phase == RecordingUploadPhase.IDLE.value:
        return True
    return phase == RecordingUploadPhase.UPLOADED.value and upload.get("hasDurableReceipt") is True


def _resumable_handoff_state(
    state: object,
    *,
    phase: RecordingUploadPhase,
    allow_native_progress: bool = False,
) -> bool:
    """Authenticate idle native ownership without freezing its upload progress."""

    if phase is RecordingUploadPhase.QUEUED:
        has_capabilities = _has_resumable_outbox_capabilities
    elif phase is RecordingUploadPhase.UPLOADING:
        has_capabilities = _has_interruptible_outbox_capabilities
    else:
        return False
    if (
        not isinstance(state, dict)
        or not parse_recording_schema_compatibility(
            state.get("schemaVersion"),
            field_present="schemaVersion" in state,
        ).supports_recording_authority
        or (state.get("admissionFenced") is not None and state.get("admissionFenced") is not False)
        or (
            state.get("handoffQuiescent") is not None and state.get("handoffQuiescent") is not False
        )
    ):
        return False
    upload = state.get("upload")
    if (
        not isinstance(upload, dict)
        or (not allow_native_progress and upload.get("phase") != phase.value)
        or not _has_saved_resumable_recording(state)
    ):
        return False
    return has_capabilities(state) and _is_quiescent_handoff_state(
        state,
        allow_durable_outbox=True,
        allow_resumable_queued=allow_native_progress or phase is RecordingUploadPhase.QUEUED,
        allow_resumable_uploading=phase is RecordingUploadPhase.UPLOADING,
    )


def _authenticated_resumable_owner(
    runtime: Mapping[str, object],
    *,
    phase: RecordingUploadPhase,
    cancellation_event: threading.Event | None,
) -> tuple[Path, control_client.RawControlDescriptor, control_client.RawControlPayload] | None:
    """Authenticate one native owner while its independently owned outbox drains."""

    if phase is RecordingUploadPhase.QUEUED:
        has_capabilities = _has_resumable_outbox_capabilities
    elif phase is RecordingUploadPhase.UPLOADING:
        has_capabilities = _has_interruptible_outbox_capabilities
    else:
        return None

    initial_snapshot: HandoffStateObservation | None = None

    def state_is_safe(state: object) -> bool:
        nonlocal initial_snapshot
        if not _resumable_handoff_state(state, phase=phase):
            return False
        initial_snapshot = HandoffStateObservation.from_wire(state)
        return initial_snapshot is not None

    def progressed_state_is_safe(state: object) -> bool:
        return _resumable_handoff_state(state, phase=phase, allow_native_progress=True)

    try:
        owner = _authenticated_existing_owner(
            runtime,
            state_is_safe=state_is_safe,
            response_state_is_safe=progressed_state_is_safe,
            descriptor_is_safe=has_capabilities,
            cancellation_event=cancellation_event,
        )
        if owner is None:
            return None
        root, value, response = owner
        control_client._require_same_handoff_descriptor(root, value)
        if not control_client._descriptor_owner_lease_is_held(root, value):
            return None
        candidate: object = value
        if not is_control_stream_descriptor(candidate):
            return None
        require_stream_owner(root, candidate, peer_pid=candidate["pid"])
        owner_state = control_client.stream_owner_state(root, candidate)
        if owner_state is None:
            return None
        response_state = response.get("state")
        if (
            not isinstance(response_state, dict)
            or not progressed_state_is_safe(owner_state)
            or not progressed_state_is_safe(response_state)
        ):
            return None
        if (
            initial_snapshot is None
            or HandoffProgress.from_states(
                initial=initial_snapshot.wire,
                response=response_state,
                current=owner_state,
            )
            is None
        ):
            return None
        control_client._require_same_handoff_descriptor(root, value)
        if not control_client._descriptor_owner_lease_is_held(root, value):
            return None
        if cancellation_event is not None and cancellation_event.is_set():
            return None
        return owner
    except (
        control_client.ControlUnavailable,
        control_client.NativeRuntimeError,
        OSError,
        TypeError,
        ValueError,
    ):
        return None


def authenticated_resumable_queued_owner(
    runtime: Mapping[str, object],
    *,
    cancellation_event: threading.Event | None = None,
) -> tuple[Path, control_client.RawControlDescriptor, control_client.RawControlPayload] | None:
    """Prove one authenticated owner can safely resume its exact queued upload."""

    return _authenticated_resumable_owner(
        runtime,
        phase=RecordingUploadPhase.QUEUED,
        cancellation_event=cancellation_event,
    )


def authenticated_resumable_uploading_owner(
    runtime: Mapping[str, object],
    *,
    cancellation_event: threading.Event | None = None,
) -> tuple[Path, control_client.RawControlDescriptor, control_client.RawControlPayload] | None:
    """Prove one authenticated owner may safely interrupt its sealed upload."""

    return _authenticated_resumable_owner(
        runtime,
        phase=RecordingUploadPhase.UPLOADING,
        cancellation_event=cancellation_event,
    )


def _live_stream_handoff_descriptor(
    expected_app_path: Path,
    plugin_family_root: Path,
    spec: PlatformRuntimeSpec,
    root: Path,
) -> tuple[str, Path, control_client.RawControlDescriptor]:
    """Classify a live owner only after its peer, image, lease and cache agree."""

    # Handoff is the authority that decides whether a discovered owner is the
    # selected image or a strictly proven predecessor. Calling the ordinary
    # descriptor accessor here would try to make that same decision again and
    # recurse whenever a verified newer runtime finds an older live owner.
    discovered = control_client._discover_control_transport(root)
    if not isinstance(discovered, StreamDiscovery):
        raise control_client.ControlUnavailable("native live control stream owner changed")
    stream_root = root
    stream_descriptor = discovered.descriptor
    if stream_descriptor["platform"] != spec.platform_key:
        raise control_client.ControlUnavailable(
            "native live control stream platform is incompatible"
        )
    if (
        not control_client._is_windows_platform_key(spec.platform_key)
        and stream_descriptor.get("bundleIdentifier") != control_client.BUNDLE_ID
    ):
        raise control_client.ControlUnavailable(
            "native live control stream app identity is invalid"
        )

    family, expected = control_client._resolved_handoff_paths(
        expected_app_path,
        plugin_family_root,
        spec,
    )
    actual = control_client._resolved_path(
        stream_descriptor.get("bundlePath"),
        message="native live control stream app identity is unavailable",
    )
    _control_client_live_handoff.require_reviewed_live_stream_owner_paths(
        expected,
        actual,
        family,
        spec,
    )

    try:
        control_client.validate_handoff_app(expected, spec)
        control_client.validate_handoff_app(actual, spec)
    except control_client.NativeRuntimeError as exc:
        raise control_client.ControlUnavailable(
            "native live control stream app identity does not match"
        ) from exc

    initial_state = _control_client_live_handoff.authenticated_live_stream_owner_state(
        stream_root, stream_descriptor
    )

    executable = control_client._resolved_path(
        stream_descriptor.get("executablePath"),
        message="native live control stream executable identity is unavailable",
    )
    if executable != control_client._expected_executable_path(actual, spec):
        raise control_client.ControlUnavailable(
            "native live control stream executable identity does not match"
        )

    require_stream_owner(stream_root, stream_descriptor, peer_pid=stream_descriptor["pid"])
    settled_state = control_client.stream_owner_state(stream_root, stream_descriptor)
    if settled_state is None or settled_state.get("sessionId") != initial_state.get("sessionId"):
        raise control_client.CooperativeHandoffRequired(
            "native live control stream owner changed during handoff"
        )
    _control_client_live_handoff.require_same_windows_runtime_for_handoff(expected, actual, spec)
    return ("current" if actual == expected else "stale"), stream_root, dict(stream_descriptor)


def _handoff_descriptor(
    expected_app_path: Path,
    plugin_family_root: Path,
    spec: PlatformRuntimeSpec,
) -> tuple[str, Path, control_client.RawControlDescriptor]:
    """Classify only an authenticated live-stream owner or proven-dead residue."""

    root = control_client.control_root()
    descriptor_path = root / "stream-descriptor.json"
    if not control_client.path_entry_may_exist(descriptor_path):
        if control_client.path_entry_may_exist(descriptor_path):
            raise control_client.CooperativeHandoffRequired(
                "native live control stream owner appeared during handoff"
            )
        return "absent", root, {}

    control_client.require_private(root, directory=True)
    try:
        value = control_client.read_json(descriptor_path)
    except control_client.ControlUnavailable:
        if not control_client.path_entry_may_exist(descriptor_path):
            return "absent", root, {}
        raise
    candidate: object = value
    if not is_control_stream_descriptor(candidate):
        raise control_client.ControlUnavailable("native control stream descriptor is malformed")
    if control_client.pid_is_proven_dead(candidate["pid"]):
        if control_client.owner_lock_state(root) == "held":
            raise control_client.ControlUnavailable("native live owner cannot be authenticated")
        if control_client.read_json(descriptor_path) != value:
            raise control_client.DescriptorChanged("native live control stream owner changed")
        return "absent", root, value
    return _live_stream_handoff_descriptor(
        expected_app_path,
        plugin_family_root,
        spec,
        root,
    )


def _wait_for_handoff_exit(
    root: Path,
    value: control_client.RawControlDescriptor,
    *,
    timeout_seconds: float | None = None,
) -> None:
    """Wait for the exact owner lease, not just descriptor or PID removal."""

    if timeout_seconds is None:
        timeout_seconds = control_client.HANDOFF_EXIT_TIMEOUT_SECONDS
    deadline = control_client.time.monotonic() + timeout_seconds
    descriptor_path = _handoff_descriptor_path(root, value)
    if control_client._is_windows_host():
        pid = value.get("pid")
        if type(pid) is not int:
            raise control_client.ControlUnavailable("native update handoff descriptor is malformed")
        while control_client.time.monotonic() < deadline:
            if control_client._pid_is_proven_dead(pid):
                if _control_client_live_handoff.owner_has_exited(root, value, descriptor_path):
                    return
                if control_client._path_entry_may_exist(descriptor_path):
                    current = control_client.read_json(descriptor_path)
                    if current != value:
                        raise control_client.ControlUnavailable(
                            "native update handoff descriptor changed before owner settlement"
                        )
            remaining_seconds = max(0.0, deadline - control_client.time.monotonic())
            if remaining_seconds > 0.0:
                control_client.time.sleep(
                    min(
                        control_client.HANDOFF_OWNER_LOCK_POLL_SECONDS,
                        remaining_seconds,
                    )
                )
        raise control_client._HandoffExitTimedOut("native update handoff timed out")
    while control_client.time.monotonic() < deadline:
        if _control_client_live_handoff.owner_has_exited(root, value, descriptor_path):
            return
        remaining_seconds = max(0.0, deadline - control_client.time.monotonic())
        if remaining_seconds > 0.0:
            control_client.time.sleep(
                min(
                    control_client.HANDOFF_OWNER_LOCK_POLL_SECONDS,
                    remaining_seconds,
                )
            )
    raise control_client._HandoffExitTimedOut("native update handoff timed out")


def _handoff_descriptor_path(
    root: Path,
    value: control_client.RawControlDescriptor,
) -> Path:
    """Accept only the authenticated live socket or named-pipe descriptor."""

    candidate: object = value
    try:
        if not is_control_stream_descriptor(candidate):
            raise control_client._DescriptorChanged(
                "native update handoff transport is unsupported"
            )
    except (RecursionError, TypeError, ValueError) as exc:
        raise control_client._DescriptorChanged("native update handoff descriptor changed") from exc
    return root / "stream-descriptor.json"


def _require_same_handoff_descriptor(
    root: Path, value: control_client.RawControlDescriptor
) -> None:
    """Require the exact descriptor to survive an ownership probe."""

    descriptor_path = _handoff_descriptor_path(root, value)
    try:
        current = control_client.read_json(descriptor_path)
    except control_client.ControlUnavailable as exc:
        if not control_client._path_entry_may_exist(descriptor_path):
            raise control_client._DescriptorChanged(
                "native update handoff descriptor changed"
            ) from exc
        raise
    if current != value:
        raise control_client._DescriptorChanged("native update handoff descriptor changed")


def _windows_owner_lock_state(lock_path: Path) -> str:
    """Probe the first byte covered by the companion's LockFileEx lease."""

    try:
        import msvcrt
    except ImportError as exc:  # pragma: no cover - Windows-only module.
        raise control_client.ControlUnavailable("native owner lease probe is unavailable") from exc
    try:
        control_client.require_private(lock_path, directory=False)
    except control_client.ControlUnavailable as exc:
        if not control_client._path_entry_may_exist(lock_path):
            return "missing"
        raise control_client.ControlUnavailable("native owner lease is unsafe") from exc

    windows_lock_api: dict[str, object] = {
        name: getattr(msvcrt, name) for name in ("locking", "LK_NBLCK", "LK_UNLCK")
    }
    lock = windows_lock_api["locking"]
    nonblocking_lock = windows_lock_api["LK_NBLCK"]
    unlock = windows_lock_api["LK_UNLCK"]
    if not callable(lock) or type(nonblocking_lock) is not int or type(unlock) is not int:
        raise control_client.ControlUnavailable("native owner lease probe is unavailable")
    flags = (
        control_client.os.O_RDWR
        | getattr(control_client.os, "O_BINARY", 0)
        | getattr(control_client.os, "O_NOINHERIT", 0)
    )
    try:
        descriptor = control_client.os.open(lock_path, flags)
    except FileNotFoundError:
        return "missing"
    except OSError as exc:
        raise control_client.ControlUnavailable("native owner lease is unavailable") from exc
    try:
        metadata = control_client.os.fstat(descriptor)
        path_metadata = lock_path.lstat()
        reparse_point = getattr(control_client.stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
        if (
            not control_client.stat.S_ISREG(metadata.st_mode)
            or not control_client.stat.S_ISREG(path_metadata.st_mode)
            or lock_path.is_symlink()
            or (reparse_point and getattr(path_metadata, "st_file_attributes", 0) & reparse_point)
            or (metadata.st_dev, metadata.st_ino) != (path_metadata.st_dev, path_metadata.st_ino)
        ):
            raise control_client.ControlUnavailable("native owner lease is unsafe")
        control_client.os.lseek(descriptor, 0, control_client.os.SEEK_SET)
        held = False
        try:
            # fs4 locks the complete file range through LockFileEx. The CRT's
            # one-byte nonblocking lock is backed by the same kernel byte-range
            # primitive, so a live owner conflicts without opening a second
            # lifecycle protocol in Python.
            lock(descriptor, nonblocking_lock, 1)
        except OSError as exc:
            if exc.errno in {
                control_client.errno.EACCES,
                control_client.errno.EAGAIN,
                control_client.errno.EDEADLK,
            }:
                held = True
            else:
                raise control_client.ControlUnavailable(
                    "native owner lease is unavailable"
                ) from exc
        try:
            final_metadata = control_client.require_private(lock_path, directory=False)
        except control_client.ControlUnavailable as exc:
            raise control_client.ControlUnavailable("native owner lease is unsafe") from exc
        if (metadata.st_dev, metadata.st_ino) != (
            final_metadata.st_dev,
            final_metadata.st_ino,
        ):
            raise control_client.ControlUnavailable("native owner lease is unsafe")
        if held:
            return "held"
        try:
            control_client.os.lseek(descriptor, 0, control_client.os.SEEK_SET)
            lock(descriptor, unlock, 1)
        except OSError as exc:
            raise control_client.ControlUnavailable("native owner lease is unavailable") from exc
        return "available"
    finally:
        control_client.os.close(descriptor)


def _owner_lock_state(root: Path | None = None) -> str:
    """Return missing, available, or held for the native kernel lease.

    A lock file can outlive its owner forever, so existence is never enough
    to delay launch. Open the exact private regular file read-only without
    creating it, then ask the kernel whether an exclusive non-blocking lock
    is available.
    """

    selected_root = root if root is not None else control_client.control_root()
    if not selected_root.exists():
        return "missing"
    control_client.require_private(selected_root, directory=True)
    lock_path = selected_root / control_client.OWNER_LOCK_FILENAME
    if control_client._is_windows_host():
        return control_client._windows_owner_lock_state(lock_path)
    posix_files: control_client._PosixFileApi = control_client.os
    if control_client.fcntl is None:
        raise control_client.ControlUnavailable("native owner lease probe is unavailable")

    def safe_metadata(
        metadata: stat_result,
    ) -> tuple[int, int, int, int, int]:
        if (
            not stat.S_ISREG(metadata.st_mode)
            or metadata.st_uid != posix_files.getuid()
            or metadata.st_mode & 0o077
        ):
            raise control_client.ControlUnavailable("native owner lease is unsafe")
        return (
            metadata.st_dev,
            metadata.st_ino,
            metadata.st_size,
            metadata.st_mtime_ns,
            metadata.st_ctime_ns,
        )

    try:
        before = safe_metadata(lock_path.lstat())
    except FileNotFoundError:
        return "missing"
    except OSError as exc:
        raise control_client.ControlUnavailable("native owner lease is unavailable") from exc
    flags = (
        control_client.os.O_RDONLY
        | getattr(control_client.os, "O_CLOEXEC", 0)
        | getattr(control_client.os, "O_NOFOLLOW", 0)
    )
    try:
        descriptor = control_client.os.open(lock_path, flags)
    except FileNotFoundError:
        return "missing"
    except OSError as exc:
        raise control_client.ControlUnavailable("native owner lease is unavailable") from exc
    try:
        if safe_metadata(control_client.os.fstat(descriptor)) != before:
            raise control_client.ControlUnavailable("native owner lease is unsafe")
        held = False
        try:
            control_client.fcntl.flock(
                descriptor, control_client.fcntl.LOCK_EX | control_client.fcntl.LOCK_NB
            )
        except BlockingIOError:
            held = True
        except OSError as exc:
            if exc.errno in {
                control_client.errno.EACCES,
                control_client.errno.EAGAIN,
                control_client.errno.EWOULDBLOCK,
            }:
                held = True
            else:
                raise control_client.ControlUnavailable(
                    "native owner lease is unavailable"
                ) from exc
        try:
            after = safe_metadata(lock_path.lstat())
        except OSError as exc:
            raise control_client.ControlUnavailable("native owner lease is unsafe") from exc
        if after != before or safe_metadata(control_client.os.fstat(descriptor)) != before:
            raise control_client.ControlUnavailable("native owner lease is unsafe")
        if held:
            return "held"
        try:
            control_client.fcntl.flock(descriptor, control_client.fcntl.LOCK_UN)
        except OSError as exc:
            raise control_client.ControlUnavailable("native owner lease is unavailable") from exc
        return "available"
    finally:
        control_client.os.close(descriptor)


def _descriptor_owner_lease_is_held(
    root: Path,
    value: control_client.RawControlDescriptor,
) -> bool:
    """Return whether this exact native descriptor owns the kernel lease.

    A live PID and a matching executable path are not ownership: a crashed
    companion can leave both a descriptor and a subsequently reused PID. The
    companion publishes its descriptor only while holding native-owner.lock,
    so sample that kernel fact between two exact descriptor reads. A missing
    or available lease proves this descriptor is stale; the launch path can
    safely continue because the native lease still arbitrates any replacement
    race. Ambiguous lease probes remain fail-closed.
    """

    control_client._require_same_handoff_descriptor(root, value)
    pid = value.get("pid")
    if type(pid) is not int:
        raise control_client.ControlUnavailable("native control descriptor is stale")
    if control_client._pid_is_proven_dead(pid):
        return False
    lease_state = control_client._owner_lock_state(root)
    control_client._require_same_handoff_descriptor(root, value)
    if lease_state != "held":
        return False
    if control_client._pid_is_proven_dead(pid):
        return False
    return True


def _log_handoff_outcome(outcome: str, value: control_client.RawControlDescriptor) -> None:
    """Emit fixed, path-free lifecycle outcomes at their owning boundary."""

    control_client.log_native_runtime_event("handoff", outcome, platform=value.get("platform"))


def _require_exact_handoff_owner(root: Path, value: control_client.RawControlDescriptor) -> None:
    """Revalidate the exact live peer, descriptor, executable image, and owner lease."""

    candidate: object = value
    if not is_control_stream_descriptor(candidate):
        raise control_client.ControlUnavailable("native update handoff transport is unsupported")
    require_stream_owner(root, candidate, peer_pid=candidate["pid"])


def _verified_darwin_owner_process_image(
    pid: int,
    *,
    expected_path: Path,
    expected_identity: tuple[int, int],
    expected_digest: str,
    expected_start_identity: tuple[int, int] | None = None,
) -> tuple[int, int]:
    return owner_recovery.verified_darwin_owner_process_image(
        pid,
        expected_path=expected_path,
        expected_identity=expected_identity,
        expected_digest=expected_digest,
        expected_start_identity=expected_start_identity,
    )


def _confirmed_stale_companion_owner(
    runtime: Mapping[str, object],
) -> tuple[Path, control_client.RawControlDescriptor]:
    """Identify only a proven-dead stream owner with no remaining owner lease."""

    root = control_client.control_root()
    control_client.require_private(root, directory=True)
    value = control_client.read_json(root / "stream-descriptor.json")
    candidate: object = value
    if (
        not is_control_stream_descriptor(candidate)
        or candidate["platform"] != runtime.get("platform")
        or runtime.get("installed") is not True
        or runtime.get("source") != "plugin-bundled"
        or not control_client.pid_is_proven_dead(candidate["pid"])
        or control_client.owner_lock_state(root) == "held"
    ):
        raise control_client.ControlUnavailable("native stale owner identity is unavailable")
    _require_same_handoff_descriptor(root, value)
    return root, value


def _explicit_force_recording_state(
    root: Path,
    descriptor: control_client.RawControlDescriptor,
) -> _ExplicitForceRecordingObservation:
    """Read generated recording authority from the exact authenticated live peer."""

    candidate: object = descriptor
    if not is_control_stream_descriptor(candidate):
        raise control_client.ControlUnavailable("native control stream descriptor is malformed")
    require_stream_owner(root, candidate, peer_pid=candidate["pid"])
    observed_state = control_client.stream_owner_state(root, candidate)
    if observed_state is None or not is_recording_state(observed_state):
        raise control_client.ControlUnavailable("native recording state is malformed")
    require_stream_owner(root, candidate, peer_pid=candidate["pid"])
    state: RecordingState = observed_state
    compatibility = parse_recording_schema_compatibility(
        state.get("schemaVersion"),
        field_present="schemaVersion" in state,
    )
    if not compatibility.supports_recording_authority:
        raise control_client.ControlUnavailable("native recording state is malformed")
    native_status = RecordingNativeStatus(state["status"])
    if native_status is RecordingNativeStatus.UNKNOWN:
        raise control_client.ControlUnavailable("native recording state is unsupported")
    if native_status.allows_stop(compatibility) is not state["canStop"] or (
        native_status is RecordingNativeStatus.IDLE and state.get("sessionId") is not None
    ):
        raise control_client.ControlUnavailable("native recording state is inconsistent")
    return _ExplicitForceRecordingObservation(state, observed_state)


def _require_idle_explicit_recording_state(
    root: Path,
    descriptor: control_client.RawControlDescriptor,
) -> _ExplicitForceRecordingObservation:
    """Protect recording and saving without inspecting native-owned upload work."""

    observation = _explicit_force_recording_state(root, descriptor)
    if not _meetings_app_manager().can_automatically_replace_owner(observation.owner_state):
        raise RecordingCaptureActive("native recording owner is busy")
    return observation


def require_idle_staged_update_owner(
    runtime: Mapping[str, object],
    *,
    preverified_compatible_windows_source: _PreverifiedWindowsStagedUpdateSource | None = None,
) -> None:
    """Reject active or unverifiable capture before changing plugin registration."""

    if control_client._v2_descriptor_is_present():
        from companion_client import companion_client

        client = companion_client(runtime=runtime)
        state = client.get_state()
        if (
            state["recording"]["phase"] != "idle"
            or not state["lifecycle"]["replacement"]["allowed"]
        ):
            raise RecordingCaptureActive("native recording owner is busy")
        return

    try:
        root, descriptor = control_client.descriptor(runtime=runtime)
    except control_client.ControlUnavailable:
        _handler, (root, descriptor) = _meetings_app_manager().authenticate_update_owner(
            runtime,
            preverified_source=preverified_compatible_windows_source,
        )
    _require_exact_handoff_owner(root, descriptor)
    _require_idle_explicit_recording_state(root, descriptor)
    _require_exact_handoff_owner(root, descriptor)


def require_verified_staged_update_owner(
    runtime: Mapping[str, object],
    *,
    preverified_compatible_windows_source: _PreverifiedWindowsStagedUpdateSource | None = None,
) -> CompanionClient | None:
    """Authenticate the exact explicitly forced-update owner without inspecting capture."""

    if control_client._v2_descriptor_is_present():
        from companion_client import reviewed_predecessor_companion_client

        client = reviewed_predecessor_companion_client(runtime=runtime)
        app_path = client.owner.runtime.get("appPath")
        _platform, spec = _typed_native_handoff_spec(runtime.get("platform"))
        # Installing can replace a plugin cache root; retain an immutable owner.
        if not isinstance(app_path, str) or not control_client.is_stable_runtime_artifact(
            Path(app_path), spec, require_active=False
        ):
            raise control_client.ControlUnavailable("native owner is not using the stable runtime")
        return client

    try:
        root, descriptor = control_client.descriptor(runtime=runtime)
    except control_client.ControlUnavailable:
        _handler, (root, descriptor) = _meetings_app_manager().authenticate_update_owner(
            runtime,
            preverified_source=preverified_compatible_windows_source,
        )
    _require_exact_handoff_owner(root, descriptor)
    return None


def force_quit_companion_owner(
    *,
    runtime: Mapping[str, object],
    allow_compatible_live_owner: bool = False,
    allow_compatible_idle_owner: bool = False,
    allow_stale_owner_recovery: bool = True,
    immediate: bool = False,
    revalidate_request: Callable[[], None] | None = None,
    preverified_compatible_windows_source: _PreverifiedWindowsStagedUpdateSource | None = None,
) -> None:
    """Replace one verified idle owner through the shared live-stream handoff."""

    if control_client._v2_descriptor_is_present():
        from companion_client import companion_client, quit_companion_owner

        client = companion_client(runtime=runtime, connect=not immediate)
        quit_companion_owner(client, immediate=immediate, revalidate_request=revalidate_request)
        return

    try:
        runtime_platform_value = runtime["platform"]
    except (KeyError, TypeError):
        runtime_platform_value = None
    declared_platform = parse_control_platform(runtime_platform_value)
    if runtime_platform_value is not None:
        _typed_native_handoff_spec(runtime_platform_value)
    if preverified_compatible_windows_source is not None and (
        not allow_compatible_live_owner or allow_compatible_idle_owner or allow_stale_owner_recovery
    ):
        raise control_client.ControlUnavailable("native selected runtime is not verified")

    stale_owner = False
    try:
        root, value = control_client.descriptor(runtime=runtime)
    except control_client.ControlUnavailable:
        if allow_compatible_live_owner:
            _handler, (root, value) = _meetings_app_manager().authenticate_update_owner(
                runtime,
                preverified_source=preverified_compatible_windows_source,
            )
        elif allow_stale_owner_recovery:
            try:
                root, value = _confirmed_stale_companion_owner(runtime)
                stale_owner = True
            except control_client.ControlUnavailable:
                if not allow_compatible_idle_owner:
                    raise
                compatible_owner = (
                    _meetings_app_manager().authenticate_compatible_idle_force_start_owner(runtime)
                )
                if compatible_owner is None:
                    raise
                _handler, (root, value) = compatible_owner
        else:
            raise

    candidate: object = value
    if not is_control_stream_descriptor(candidate):
        raise control_client.ControlUnavailable("native update handoff transport is unsupported")
    owner_platform, _owner_spec = _typed_native_handoff_spec(candidate["platform"])
    if declared_platform is not ControlPlatform.UNKNOWN and declared_platform != owner_platform:
        raise control_client.ControlUnavailable("native update platform does not match")
    if stale_owner:
        if control_client.owner_lock_state(root) == "held":
            raise control_client.ControlUnavailable("native live owner cannot be authenticated")
        _wait_for_handoff_exit(root, value)
        return

    _require_idle_explicit_recording_state(root, value)

    def revalidate_explicit_owner() -> None:
        if revalidate_request is not None:
            revalidate_request()
        require_stream_owner(root, candidate, peer_pid=candidate["pid"])
        _require_idle_explicit_recording_state(root, value)

    _perform_cooperative_handoff(
        control_client.ControlClient(),
        root,
        value,
        revalidate_request=revalidate_explicit_owner,
        allow_automatic_idle_replacement=True,
    )


def _perform_cooperative_handoff(
    client: control_client.ControlClient,
    root: Path,
    value: control_client.RawControlDescriptor,
    *,
    revalidate_request: Callable[[], None] | None = None,
    allow_automatic_idle_replacement: bool = False,
) -> None:
    """Route every upgrade through the shared authenticated stream handoff."""

    candidate: object = value
    if not is_control_stream_descriptor(candidate):
        raise control_client.CooperativeHandoffRequired(
            "native update requires an authenticated socket or named-pipe owner"
        )
    _perform_live_stream_cooperative_handoff(
        client,
        root,
        candidate,
        revalidate_request=revalidate_request,
        allow_automatic_idle_replacement=allow_automatic_idle_replacement,
    )


_perform_live_stream_cooperative_handoff = (
    _control_client_live_handoff.perform_live_stream_cooperative_handoff
)
_fresh_authenticated_live_stream_idle_state = (
    _control_client_live_handoff.fresh_authenticated_live_stream_idle_state
)
_verified_live_darwin_owner = _control_client_live_handoff.verified_live_darwin_owner
_replace_authenticated_live_darwin_owner = (
    _control_client_live_handoff.replace_authenticated_live_darwin_owner
)
_replace_authenticated_live_stream_idle_owner = (
    _control_client_live_handoff.replace_authenticated_live_stream_idle_owner
)


def _is_quiescent_handoff_state(
    state: object,
    *,
    allow_durable_outbox: bool = False,
    allow_resumable_queued: bool = False,
    allow_resumable_uploading: bool = False,
) -> bool:
    """Accept authenticated idle stream states without blocking durable uploads."""

    if (
        not isinstance(state, dict)
        or not parse_recording_schema_compatibility(
            state.get("schemaVersion"),
            field_present="schemaVersion" in state,
        ).supports_recording_authority
    ):
        return False
    startup = state.get("startup")
    attention = startup.get("attention") if isinstance(startup, dict) else None
    upload = state.get("upload")
    headless = state.get("headless")
    sync = headless.get("sync") if isinstance(headless, dict) else None
    markdown = sync.get("markdown") if isinstance(sync, dict) else None
    upload_phase = upload.get("phase") if isinstance(upload, dict) else None
    sync_status = sync.get("status") if isinstance(sync, dict) else None
    markdown_phase = markdown.get("phase") if isinstance(markdown, dict) else None
    pending_uploads = upload.get("pendingCount") if isinstance(upload, dict) else None
    upload_is_quiescent = (
        isinstance(upload, dict)
        and isinstance(upload_phase, str)
        and upload_phase in control_client._QUIESCENT_START_SUCCESSOR_UPLOAD_PHASES
        and type(pending_uploads) is int
        and pending_uploads == 0
    )
    if allow_durable_outbox and isinstance(upload, dict):
        upload_is_quiescent = upload_is_quiescent or (
            isinstance(upload_phase, str)
            and upload_phase in control_client._DURABLE_OUTBOX_HANDOFF_UPLOAD_PHASES
            and type(pending_uploads) is int
            and 0 <= pending_uploads <= control_client.MAXIMUM_JAVASCRIPT_SAFE_INTEGER
        )
        upload_is_quiescent = upload_is_quiescent or _has_resumable_completed_outbox(state)
        if allow_resumable_queued:
            upload_is_quiescent = upload_is_quiescent or (
                upload_phase == RecordingUploadPhase.QUEUED.value
                and type(pending_uploads) is int
                and 0 < pending_uploads <= control_client.MAXIMUM_JAVASCRIPT_SAFE_INTEGER
                and (
                    _has_resumable_outbox_capabilities(state)
                    or _has_interruptible_outbox_capabilities(state)
                )
                and _has_saved_resumable_recording(state)
            )
        if allow_resumable_uploading:
            upload_is_quiescent = upload_is_quiescent or (
                upload_phase == RecordingUploadPhase.UPLOADING.value
                and type(pending_uploads) is int
                and 0 < pending_uploads <= control_client.MAXIMUM_JAVASCRIPT_SAFE_INTEGER
                and _has_interruptible_outbox_capabilities(state)
                and _has_saved_resumable_recording(state)
                and (state.get("admissionFenced") is None or state.get("admissionFenced") is False)
                and (
                    state.get("handoffQuiescent") is None or state.get("handoffQuiescent") is False
                )
            )
    return (
        state.get("status") == RecordingNativeStatus.IDLE.value
        and state.get("canStop") is False
        and (not allow_durable_outbox or state.get("sessionId") is None)
        and isinstance(startup, dict)
        and startup.get("recovery") == RecordingStartupRecovery.READY.value
        and attention is None
        and upload_is_quiescent
        and (
            headless is None
            or (
                isinstance(headless, dict)
                and isinstance(sync, dict)
                and isinstance(sync_status, str)
                and (
                    sync_status in control_client._QUIESCENT_HANDOFF_HEADLESS_SYNC_STATUSES
                    or (
                        allow_durable_outbox
                        and sync_status
                        in control_client._DURABLE_OUTBOX_HANDOFF_HEADLESS_SYNC_STATUSES
                        and (
                            markdown is None
                            or (
                                isinstance(markdown, dict)
                                and isinstance(markdown_phase, str)
                                and markdown_phase in {"needs-attention", "needs-sign-in"}
                            )
                        )
                    )
                )
            )
        )
    )


def _is_fenced_handoff_ack_state(state: object) -> bool:
    return (
        isinstance(state, dict)
        and parse_recording_schema_compatibility(
            state.get("schemaVersion"),
            field_present="schemaVersion" in state,
        ).supports_recording_authority
        and state.get("status") == RecordingNativeStatus.IDLE.value
        and state.get("canStop") is False
        and state.get("canStart") is False
        and state.get("admissionFenced") is True
        and state.get("handoffQuiescent") is True
        and isinstance(state.get("capabilities"), list)
        and control_client.UPDATE_HANDOFF_WORK_FENCE_CAPABILITY in state["capabilities"]
    )


def _wait_for_absent_handoff_owner_lease(
    expected_app_path: Path,
    plugin_family_root: Path,
    spec: PlatformRuntimeSpec,
    *,
    timeout_seconds: float | None = None,
    source_plugin_root: Path | None = None,
) -> str:
    """Wait for lease release or reuse an owner published while it is held.

    During graceful shutdown the native app intentionally removes its
    descriptor before releasing native-owner.lock. Treat that short window as
    handoff-in-progress. During concurrent startup, the winner takes the lease
    before publishing its descriptor, so reuse that descriptor as soon as it
    appears. A missing lock remains the first-install fast path.
    """

    state = control_client._owner_lock_state()
    if state == "missing":
        return "absent"
    selected_timeout = (
        control_client.HANDOFF_OWNER_LOCK_TIMEOUT_SECONDS
        if timeout_seconds is None
        else timeout_seconds
    )
    deadline = control_client.time.monotonic() + max(0.0, selected_timeout)
    owner_root = control_client.control_root()
    stream_descriptor_path = owner_root / "stream-descriptor.json"
    while state == "held":
        # A concurrent winner acquires the lease before publishing its
        # descriptor. Re-read while the lease remains held so the losing
        # launcher can reuse only an authenticated responsive owner.
        try:
            stream_descriptor_path.lstat()
            live_owner_published = True
        except FileNotFoundError:
            live_owner_published = False
        except OSError as exc:
            raise control_client.ControlUnavailable(
                "native live control stream discovery is unavailable"
            ) from exc
        if live_owner_published:
            disposition = control_client._request_update_handoff_once(
                expected_app_path,
                plugin_family_root,
                spec,
                source_plugin_root=source_plugin_root,
            )
            if disposition != "absent":
                return disposition
        if control_client.time.monotonic() >= deadline:
            raise control_client.ControlUnavailable("native update handoff owner lease timed out")
        control_client.time.sleep(control_client.HANDOFF_OWNER_LOCK_POLL_SECONDS)
        state = control_client._owner_lock_state()
    # The file existed and the kernel proved it acquirable. Re-read the
    # descriptor before launch because another owner may have published one
    # while the outgoing process was releasing its lease.
    return control_client._request_update_handoff_once(
        expected_app_path,
        plugin_family_root,
        spec,
        source_plugin_root=source_plugin_root,
    )


def _require_canonical_handoff_request(
    expected_app_path: Path,
    plugin_family_root: Path,
    *,
    spec: PlatformRuntimeSpec,
    source_plugin_root: Path | None = None,
) -> None:
    if source_plugin_root is None and control_client._is_stable_runtime_artifact(
        expected_app_path,
        spec,
        require_active=True,
    ):
        return
    try:
        control_client.require_canonical_plugin_registration(
            source_plugin_root or expected_app_path.parent,
            plugin_family_root,
        )
    except control_client.NativeRuntimeError as exc:
        raise control_client.ControlUnavailable(
            "native update handoff requester is not canonical"
        ) from exc


def _request_update_handoff_once(
    expected_app_path: Path,
    plugin_family_root: Path,
    spec: PlatformRuntimeSpec,
    *,
    source_plugin_root: Path | None = None,
    recover_unhealthy_current: bool = False,
) -> str:
    """Reuse a verified stream owner or perform the shared stale-owner upgrade."""

    if control_client._is_windows_platform_key(spec.platform_key):
        raise control_client.ControlUnavailable("Windows handoff requires launch resolver")

    def revalidate_request() -> None:
        control_client._require_canonical_handoff_request(
            expected_app_path,
            plugin_family_root,
            spec=spec,
            source_plugin_root=source_plugin_root,
        )

    revalidate_request()
    try:
        disposition, root, value = control_client._handoff_descriptor(
            expected_app_path,
            plugin_family_root,
            spec,
        )
    except control_client.ControlUnavailable:
        root = control_client.control_root()
        if not recover_unhealthy_current or control_client.owner_lock_state(root) == "held":
            raise
        return "absent"

    if disposition == "absent":
        return disposition
    candidate: object = value
    if not is_control_stream_descriptor(candidate):
        raise control_client.ControlUnavailable("native update handoff transport is unsupported")
    require_stream_owner(root, candidate, peer_pid=candidate["pid"])
    if control_client.stream_owner_state(root, candidate) is None:
        raise control_client.CooperativeHandoffRequired(
            "native live control stream owner is no longer connected"
        )
    revalidate_request()
    if disposition == "current":
        return "current"
    _perform_cooperative_handoff(
        control_client.ControlClient(),
        root,
        value,
        revalidate_request=revalidate_request,
        allow_automatic_idle_replacement=(recover_unhealthy_current or disposition == "stale"),
    )
    return "handed-off"


def resolve_update_handoff_for_launch(
    expected_app_path: Path,
    plugin_family_root: Path,
    spec: PlatformRuntimeSpec,
    *,
    expected_executable_sha256: str | None = None,
    source_plugin_root: Path | None = None,
    recover_unhealthy_current: bool = False,
) -> str:
    """Resolve one launch using only authenticated socket or named-pipe owners."""

    if control_client._v2_descriptor_is_present():
        from companion_client import resolve_companion_handoff

        return resolve_companion_handoff(
            expected_app_path,
            plugin_family_root,
            spec,
            expected_executable_sha256=expected_executable_sha256,
            source_plugin_root=source_plugin_root,
        )

    if not control_client._is_windows_platform_key(spec.platform_key):
        disposition = _request_update_handoff_once(
            expected_app_path,
            plugin_family_root,
            spec,
            source_plugin_root=source_plugin_root,
            recover_unhealthy_current=recover_unhealthy_current,
        )
        if disposition != "absent":
            return disposition
        if (
            recover_unhealthy_current
            and control_client.owner_lock_state(control_client.control_root()) != "held"
        ):
            return "absent"
        return _wait_for_absent_handoff_owner_lease(
            expected_app_path,
            plugin_family_root,
            spec,
            source_plugin_root=source_plugin_root,
        )

    if (
        not isinstance(expected_executable_sha256, str)
        or control_client.SHA256_HEX_PATTERN.fullmatch(expected_executable_sha256) is None
    ):
        raise control_client.ControlUnavailable(
            "native update handoff executable identity is unavailable"
        )

    client = control_client.ControlClient()
    handoff_count = 0
    deadline = control_client.time.monotonic() + control_client.HANDOFF_OWNER_LOCK_TIMEOUT_SECONDS

    def revalidate_request() -> None:
        control_client._require_canonical_handoff_request(
            expected_app_path,
            plugin_family_root,
            spec=spec,
            source_plugin_root=source_plugin_root,
        )

    while True:
        revalidate_request()
        root = control_client.control_root()
        try:
            disposition, root, value = control_client._handoff_descriptor(
                expected_app_path,
                plugin_family_root,
                spec,
            )
        except control_client.DescriptorChanged:
            disposition, value = "absent", {}
        except control_client.ControlUnavailable:
            if not recover_unhealthy_current or control_client.owner_lock_state(root) == "held":
                raise
            disposition, value = "absent", {}

        if disposition in {"current", "stale"}:
            candidate: object = value
            if not is_control_stream_descriptor(candidate):
                raise control_client.ControlUnavailable(
                    "native update handoff transport is unsupported"
                )
            require_stream_owner(root, candidate, peer_pid=candidate["pid"])
            state = control_client.stream_owner_state(root, candidate)
            if state is None:
                raise control_client.CooperativeHandoffRequired(
                    "native live control stream owner is no longer connected"
                )
            if disposition == "current":
                owner_digest = candidate.get("executableSHA256")
                if not isinstance(owner_digest, str):
                    raise control_client.ControlUnavailable(
                        "native live control stream executable identity is unavailable"
                    )
                if not control_client.hmac.compare_digest(
                    owner_digest,
                    expected_executable_sha256,
                ):
                    raise control_client.ControlUnavailable(
                        "native live control stream executable identity does not match"
                    )
                return "current"
            if handoff_count >= control_client.WINDOWS_HANDOFF_RECHECK_LIMIT:
                raise control_client.ControlUnavailable(
                    "native update handoff owner lease did not settle"
                )
            _perform_cooperative_handoff(
                client,
                root,
                value,
                revalidate_request=revalidate_request,
                allow_automatic_idle_replacement=True,
            )
            handoff_count += 1
            recover_unhealthy_current = False
            deadline = (
                control_client.time.monotonic() + control_client.HANDOFF_OWNER_LOCK_TIMEOUT_SECONDS
            )
            continue

        if control_client._owner_lock_state(root) in {"missing", "available"}:
            revalidate_request()
            return "handed-off" if handoff_count else "absent"
        if control_client.time.monotonic() >= deadline:
            raise control_client.ControlUnavailable("native update handoff owner lease timed out")
        control_client.time.sleep(control_client.HANDOFF_OWNER_LOCK_POLL_SECONDS)


def disconnected_state(
    _error: str | None = None,
    *,
    safe_message: str | None = None,
    recovery_kind: str | None = None,
    runtime: Mapping[str, object] | None = None,
) -> dict[str, object]:
    """Preserve the local RuntimeManager seam while projecting fixed recovery."""

    return protocol_disconnected_state(
        _error,
        safe_message=safe_message,
        recovery_kind=recovery_kind,
        runtime=runtime if runtime is not None else control_client.RuntimeManager().status(),
    )


handoff_descriptor = _handoff_descriptor
require_same_handoff_descriptor = _require_same_handoff_descriptor
windows_owner_lock_state = _windows_owner_lock_state
owner_lock_state = _owner_lock_state
descriptor_owner_lease_is_held = _descriptor_owner_lease_is_held
log_handoff_outcome = _log_handoff_outcome
require_exact_handoff_owner = _require_exact_handoff_owner
perform_cooperative_handoff = _perform_cooperative_handoff
is_quiescent_handoff_state = _is_quiescent_handoff_state
is_fenced_handoff_ack_state = _is_fenced_handoff_ack_state
wait_for_absent_handoff_owner_lease = _wait_for_absent_handoff_owner_lease
require_canonical_handoff_request = _require_canonical_handoff_request
request_update_handoff_once = _request_update_handoff_once
COMPATIBLE_DARWIN_CONTROL_PLATFORMS = _COMPATIBLE_DARWIN_CONTROL_PLATFORMS
COMPATIBLE_WINDOWS_CONTROL_PLATFORMS = _COMPATIBLE_WINDOWS_CONTROL_PLATFORMS
COMPATIBLE_DARWIN_PLATFORMS = _COMPATIBLE_DARWIN_PLATFORMS
AUTOMATIC_GRACEFUL_EXIT_TIMEOUT_SECONDS = _AUTOMATIC_GRACEFUL_EXIT_TIMEOUT_SECONDS


def wait_for_handoff_exit(
    root: Path,
    value: control_client.RawControlDescriptor,
    *,
    timeout_seconds: float | None = None,
) -> None:
    if timeout_seconds is None:
        _wait_for_handoff_exit(root, value)
    else:
        _wait_for_handoff_exit(root, value, timeout_seconds=timeout_seconds)


def meetings_app_manager() -> MeetingsAppManager[
    tuple[Path, control_client.RawControlDescriptor],
    _PreverifiedWindowsStagedUpdateSource,
]:
    return _meetings_app_manager()


def verified_live_darwin_owner(
    descriptor: ControlStreamDescriptor,
) -> _control_client_live_handoff.VerifiedLiveDarwinOwner:
    return _verified_live_darwin_owner(descriptor)


def verified_darwin_owner_process_image(
    pid: int,
    *,
    expected_path: Path,
    expected_identity: tuple[int, int],
    expected_digest: str,
    expected_start_identity: tuple[int, int] | None = None,
) -> tuple[int, int]:
    return _verified_darwin_owner_process_image(
        pid,
        expected_path=expected_path,
        expected_identity=expected_identity,
        expected_digest=expected_digest,
        expected_start_identity=expected_start_identity,
    )


def replace_authenticated_live_stream_idle_owner(
    client: control_client.ControlClient,
    root: Path,
    descriptor: ControlStreamDescriptor,
    *,
    expected_session_id: object,
    revalidate_request: Callable[[], None] | None,
    verified_darwin_owner: _control_client_live_handoff.VerifiedLiveDarwinOwner | None = None,
) -> None:
    _replace_authenticated_live_stream_idle_owner(
        client,
        root,
        descriptor,
        expected_session_id=expected_session_id,
        revalidate_request=revalidate_request,
        verified_darwin_owner=verified_darwin_owner,
    )


def fresh_authenticated_live_stream_idle_state(
    client: control_client.ControlClient,
    root: Path,
    descriptor: ControlStreamDescriptor,
    *,
    expected_session_id: object,
    revalidate_request: Callable[[], None] | None,
    revalidate_process_identity: Callable[[], None] | None = None,
) -> dict[str, object]:
    return _fresh_authenticated_live_stream_idle_state(
        client,
        root,
        descriptor,
        expected_session_id=expected_session_id,
        revalidate_request=revalidate_request,
        revalidate_process_identity=revalidate_process_identity,
    )
