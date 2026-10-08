"""Verified replacement fallback for authenticated live control owners."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

import control_client
import control_client_handoff as handoff
from native_runtime import NativeRuntimeError, PlatformRuntimeSpec, configured_e2e_isolation
from recording_control_action_contract import ControlAction, parse_control_platform
from recording_control_stream_contract import ControlStreamDescriptor, is_control_stream_descriptor

from helpers import is_json


class _PosixSignalApi(Protocol):
    @property
    def SIGKILL(self) -> int: ...


@dataclass(frozen=True)
class VerifiedLiveDarwinOwner:
    """Immutable image and process-birth proof for one live stream owner."""

    pid: int
    executable_path: Path
    image_identity: tuple[int, int]
    executable_digest: str
    process_start_identity: tuple[int, int]


def owner_has_exited(
    root: Path,
    value: control_client.RawControlDescriptor,
    descriptor_path: Path,
) -> bool:
    """Settle the exact owner lease without trusting live-stream crash residue."""

    candidate: object = value
    if not is_control_stream_descriptor(candidate):
        raise control_client.ControlUnavailable("native update handoff transport is unsupported")
    try:
        lease_state = control_client.owner_lock_state(root)
    except control_client.ControlUnavailable:
        return False
    if lease_state == "held":
        return False
    try:
        current = control_client.read_json(descriptor_path)
    except control_client.ControlUnavailable:
        if not control_client.path_entry_may_exist(descriptor_path):
            return True
        raise
    if current != value:
        raise control_client.ControlUnavailable(
            "native update handoff descriptor changed before owner settlement"
        )
    pid = value.get("pid")
    if type(pid) is not int:
        raise control_client.ControlUnavailable("native update handoff descriptor is malformed")

    for _ in range(2):
        if not control_client.pid_is_proven_dead(pid):
            return False
        try:
            current = control_client.read_json(descriptor_path)
        except control_client.ControlUnavailable:
            if not control_client.path_entry_may_exist(descriptor_path):
                return False
            raise
        if current != value:
            raise control_client.ControlUnavailable(
                "native update handoff descriptor changed before owner settlement"
            )
        try:
            settled_lease_state = control_client.owner_lock_state(root)
        except control_client.ControlUnavailable:
            return False
        if settled_lease_state not in {"available", "missing"}:
            return False
    return True


def require_reviewed_live_stream_owner_paths(
    expected: Path,
    actual: Path,
    family: Path,
    spec: PlatformRuntimeSpec,
) -> None:
    """Require immutable production owners; direct images are local/E2E only."""

    expected_is_authorized = control_client.is_stable_runtime_artifact(
        expected, spec, require_active=True
    )
    actual_is_authorized = control_client.is_stable_runtime_artifact(
        actual, spec, require_active=False
    )
    if expected_is_authorized and actual_is_authorized:
        return

    direct_images_allowed = control_client.RUNTIME_CONFIG.flavor == "development"
    if not direct_images_allowed:
        try:
            isolation = configured_e2e_isolation()
        except NativeRuntimeError as error:
            raise control_client.ControlUnavailable(
                "native E2E isolation is unavailable"
            ) from error
        direct_images_allowed = isolation is not None and family.is_relative_to(
            isolation.codex_home / "plugins" / "cache"
        )
    if direct_images_allowed:
        expected_is_authorized = (
            expected_is_authorized
            or control_client.is_direct_versioned_plugin_app(
                expected, family, artifact_name=spec.artifact_name
            )
        )
        actual_is_authorized = (
            actual_is_authorized
            or control_client.is_direct_versioned_plugin_app(
                actual, family, artifact_name=spec.artifact_name
            )
        )
    if not expected_is_authorized or not actual_is_authorized:
        raise control_client.ControlUnavailable(
            "native live control stream owner is not an immutable runtime"
        )


def authenticated_live_stream_owner_state(
    root: Path,
    descriptor: ControlStreamDescriptor,
) -> dict[str, object]:
    """Connect once without re-entering descriptor classification."""

    try:
        control_client.connect_stream_owner(
            root,
            descriptor,
            deadline=control_client.time.monotonic()
            + control_client.HANDOFF_RESPONSE_TIMEOUT_SECONDS,
        )
        handoff.require_stream_owner(root, descriptor, peer_pid=descriptor["pid"])
    except control_client.ControlUnavailable as exc:
        raise control_client.CooperativeHandoffRequired(
            "native live control stream owner requires an authenticated session"
        ) from exc
    state = control_client.stream_owner_state(root, descriptor)
    if state is None:
        raise control_client.CooperativeHandoffRequired(
            "native live control stream owner requires an authenticated session"
        )
    return state


def require_same_windows_runtime_for_handoff(
    expected: Path, actual: Path, spec: PlatformRuntimeSpec
) -> None:
    """Keep a legacy owner until exit when native cannot discover the new root."""

    import native_runtime
    import native_runtime_windows_recovery

    if not native_runtime_windows_recovery.enabled() or spec.platform_key not in {
        "windows-x64",
        "windows-arm64",
    }:
        return
    try:
        selected_root = native_runtime.stable_runtime_artifact_root(expected)
        owner_root = native_runtime.stable_runtime_artifact_root(actual)
        if selected_root == owner_root:
            return
        native_runtime.stable_runtime_verification_manifest(expected, spec, require_active=True)
        native_runtime.stable_runtime_verification_manifest(actual, spec, require_active=False)
    except (NativeRuntimeError, OSError, ValueError) as error:
        raise control_client.ControlUnavailable(
            "native runtime migration owner identity is unavailable"
        ) from error
    # The shipped Windows owner infers its update root from its own executable.
    # A new root is invisible to that protocol; a refused quit must not fall
    # through to process termination merely to move private code storage.
    raise control_client.CooperativeHandoffDeclined(
        "native runtime migration is waiting for the existing owner to exit"
    )


def perform_live_stream_cooperative_handoff(
    client: control_client.ControlClient,
    root: Path,
    descriptor: ControlStreamDescriptor,
    *,
    revalidate_request: Callable[[], None] | None,
    allow_automatic_idle_replacement: bool = False,
    owner_is_replaceable: Callable[[dict[str, object]], bool] | None = None,
) -> None:
    """Prefer one fenced native quit, then replace only a freshly proven idle owner."""

    value: control_client.RawControlDescriptor = dict(descriptor)
    capabilities = descriptor["capabilities"]
    if (
        control_client.UPDATE_HANDOFF_CAPABILITY not in capabilities
        or control_client.UPDATE_HANDOFF_WORK_FENCE_CAPABILITY not in capabilities
    ):
        control_client.log_handoff_outcome("declined", value)
        raise control_client.CooperativeHandoffRequired(
            "native live control stream owner does not support a fenced handoff"
        )

    platform = parse_control_platform(descriptor["platform"])
    transport = control_client.existing_stream_owner_transport(root, descriptor)
    if transport is not None and not {
        control_client.UPDATE_HANDOFF_CAPABILITY,
        control_client.UPDATE_HANDOFF_WORK_FENCE_CAPABILITY,
    }.issubset(transport.negotiated_capabilities):
        control_client.log_handoff_outcome("declined", value)
        raise control_client.CooperativeHandoffRequired(
            "native live control stream owner did not negotiate a fenced handoff"
        )

    is_replaceable = (
        owner_is_replaceable
        if owner_is_replaceable is not None
        else handoff.meetings_app_manager().can_automatically_replace_owner
    )
    handoff.require_stream_owner(root, descriptor, peer_pid=descriptor["pid"])
    initial_state = control_client.stream_owner_state(root, descriptor)
    if initial_state is None or not is_replaceable(initial_state):
        control_client.log_handoff_outcome("busy", value)
        raise control_client.CooperativeHandoffDeclined(
            "native live control stream owner is not quiescent"
        )
    if revalidate_request is not None:
        revalidate_request()
    handoff.require_stream_owner(root, descriptor, peer_pid=descriptor["pid"])
    observed_state = control_client.stream_owner_state(root, descriptor)
    if (
        observed_state is None
        or observed_state.get("sessionId") != initial_state.get("sessionId")
        or not is_replaceable(observed_state)
    ):
        control_client.log_handoff_outcome("busy", value)
        raise control_client.CooperativeHandoffDeclined(
            "native live control stream owner changed before its handoff"
        )

    verified_darwin_owner: VerifiedLiveDarwinOwner | None = None
    if allow_automatic_idle_replacement and platform in handoff.COMPATIBLE_DARWIN_CONTROL_PLATFORMS:
        try:
            verified_darwin_owner = handoff.verified_live_darwin_owner(descriptor)
        except control_client.ControlUnavailable:
            # Cooperative quit remains safe without destructive authority. A
            # later fallback must retain this failure rather than bless a new
            # process birth after the request.
            verified_darwin_owner = None
    if verified_darwin_owner is not None:
        if revalidate_request is not None:
            revalidate_request()
        handoff.require_stream_owner(root, descriptor, peer_pid=descriptor["pid"])
        handoff.verified_darwin_owner_process_image(
            verified_darwin_owner.pid,
            expected_path=verified_darwin_owner.executable_path,
            expected_identity=verified_darwin_owner.image_identity,
            expected_digest=verified_darwin_owner.executable_digest,
            expected_start_identity=verified_darwin_owner.process_start_identity,
        )

    try:
        response = control_client.call_with_descriptor(
            client,
            root,
            value,
            ControlAction.QUIT_FOR_UPDATE.value,
            timeout_seconds=control_client.HANDOFF_RESPONSE_TIMEOUT_SECONDS,
            arguments={},
        )
    except control_client.ControlUnavailable as exc:
        if isinstance(exc, control_client.ControlRequestTimedOut):
            outcome = "cooperative-timeout"
        elif isinstance(exc, control_client.ControlConnectionUnavailable):
            outcome = "cooperative-connection-unavailable"
        elif isinstance(exc, control_client.DescriptorChanged):
            outcome = "cooperative-owner-changed"
        else:
            outcome = "cooperative-unavailable"
        control_client.log_handoff_outcome(outcome, value)
        if not allow_automatic_idle_replacement:
            raise control_client.CooperativeHandoffRequired(
                "native live control stream handoff could not be acknowledged"
            ) from exc
        handoff.replace_authenticated_live_stream_idle_owner(
            client,
            root,
            descriptor,
            expected_session_id=initial_state.get("sessionId"),
            revalidate_request=revalidate_request,
            verified_darwin_owner=verified_darwin_owner,
        )
        return

    response_state = response.get("state")
    safe_response_state = (
        is_json(response_state)
        and response_state.get("sessionId") == initial_state.get("sessionId")
        and response_state.get("status") == "idle"
        and response_state.get("canStop") is False
        and (
            response.get("ok") is True
            and control_client.is_fenced_handoff_ack_state(response_state)
            or is_replaceable(response_state)
        )
    )
    if not safe_response_state:
        control_client.log_handoff_outcome("declined", value)
        raise control_client.CooperativeHandoffDeclined(
            "native live control stream handoff did not return its owner fence"
        )

    if response.get("ok") is True and control_client.is_fenced_handoff_ack_state(response_state):
        try:
            control_client.wait_for_handoff_exit(root, value)
        except control_client.HandoffExitTimedOut:
            if not allow_automatic_idle_replacement:
                raise
        else:
            control_client.log_handoff_outcome("cooperative", value)
            return
    elif response.get("ok") is not False and response.get("ok") is not True:
        control_client.log_handoff_outcome("declined", value)
        raise control_client.CooperativeHandoffDeclined(
            "native live control stream handoff response is ambiguous"
        )
    elif not allow_automatic_idle_replacement:
        control_client.log_handoff_outcome("declined", value)
        raise control_client.CooperativeHandoffDeclined(
            "native live control stream handoff did not return its owner fence"
        )

    handoff.replace_authenticated_live_stream_idle_owner(
        client,
        root,
        descriptor,
        expected_session_id=initial_state.get("sessionId"),
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
    """Read one direct owner-authenticated status immediately before replacement."""

    value: control_client.RawControlDescriptor = dict(descriptor)
    if revalidate_request is None:
        raise control_client.CooperativeHandoffRequired(
            "native live control stream replacement authorization is unavailable"
        )
    revalidate_request()
    try:
        handoff.require_stream_owner(root, descriptor, peer_pid=descriptor["pid"])
        response = control_client.call_with_descriptor(
            client,
            root,
            value,
            ControlAction.STATUS.value,
            timeout_seconds=control_client.HANDOFF_RESPONSE_TIMEOUT_SECONDS,
            arguments={},
        )
    except control_client.ControlUnavailable as exc:
        raise control_client.CooperativeHandoffRequired(
            "native live control stream idle state could not be authenticated"
        ) from exc
    state = response.get("state")
    if (
        response.get("ok") is not True
        or not is_json(state)
        or state.get("sessionId") != expected_session_id
        or not handoff.meetings_app_manager().can_force_replace_owner_without_native_ack(state)
    ):
        control_client.log_handoff_outcome("busy", value)
        raise control_client.CooperativeHandoffDeclined(
            "native live control stream owner is not safely idle"
        )
    revalidate_request()
    handoff.require_stream_owner(root, descriptor, peer_pid=descriptor["pid"])
    if revalidate_process_identity is not None:
        revalidate_process_identity()
    return state


def verified_live_darwin_owner(
    descriptor: ControlStreamDescriptor,
) -> VerifiedLiveDarwinOwner:
    """Pin one reviewed live Darwin image and its original process birth."""

    value: control_client.RawControlDescriptor = dict(descriptor)
    platform = descriptor["platform"]
    if (
        control_client.sys.platform != "darwin"
        or control_client.is_windows_host()
        or platform not in handoff.COMPATIBLE_DARWIN_PLATFORMS
        or descriptor.get("bundleIdentifier") != control_client.BUNDLE_ID
    ):
        raise control_client.CooperativeHandoffRequired(
            "native live control stream Darwin owner identity is unavailable"
        )
    image_identity = control_client.optional_darwin_executable_file_identity(value)
    executable_digest = control_client.optional_darwin_executable_sha256(value)
    if image_identity is None or executable_digest is None:
        raise control_client.CooperativeHandoffRequired(
            "native live control stream Darwin executable identity is unavailable"
        )
    app_path = control_client.resolved_path(
        descriptor.get("bundlePath"),
        message="native live control stream Darwin app identity is unavailable",
    )
    executable_path = control_client.resolved_path(
        descriptor.get("executablePath"),
        message="native live control stream Darwin executable identity is unavailable",
    )
    spec = control_client.runtime_spec_for(platform)
    if executable_path != control_client.expected_executable_path(app_path, spec):
        raise control_client.CooperativeHandoffRequired(
            "native live control stream Darwin executable identity does not match"
        )
    try:
        control_client.validate_handoff_app(app_path, spec)
        metadata = executable_path.stat()
        actual_digest = control_client.sha256_regular_file(executable_path)
    except (control_client.NativeRuntimeError, OSError) as exc:
        raise control_client.CooperativeHandoffRequired(
            "native live control stream Darwin executable identity is unavailable"
        ) from exc
    if (
        metadata.st_dev,
        metadata.st_ino,
    ) != image_identity or not control_client.hmac.compare_digest(
        actual_digest,
        executable_digest,
    ):
        raise control_client.CooperativeHandoffRequired(
            "native live control stream Darwin executable identity does not match"
        )
    pid = descriptor["pid"]
    process_start_identity = handoff.verified_darwin_owner_process_image(
        pid,
        expected_path=executable_path,
        expected_identity=image_identity,
        expected_digest=executable_digest,
    )
    return VerifiedLiveDarwinOwner(
        pid=pid,
        executable_path=executable_path,
        image_identity=image_identity,
        executable_digest=executable_digest,
        process_start_identity=process_start_identity,
    )


def replace_authenticated_live_darwin_owner(
    client: control_client.ControlClient,
    root: Path,
    descriptor: ControlStreamDescriptor,
    *,
    owner: VerifiedLiveDarwinOwner,
    expected_session_id: object,
    revalidate_request: Callable[[], None] | None,
) -> None:
    value: control_client.RawControlDescriptor = dict(descriptor)

    def revalidate_process_identity() -> None:
        handoff.verified_darwin_owner_process_image(
            owner.pid,
            expected_path=owner.executable_path,
            expected_identity=owner.image_identity,
            expected_digest=owner.executable_digest,
            expected_start_identity=owner.process_start_identity,
        )

    def revalidate_idle_owner() -> None:
        handoff.fresh_authenticated_live_stream_idle_state(
            client,
            root,
            descriptor,
            expected_session_id=expected_session_id,
            revalidate_request=revalidate_request,
            revalidate_process_identity=revalidate_process_identity,
        )

    owner_identity = (owner.pid, descriptor["epoch"])
    with control_client.capture_aware_sigterm_owners() as signaled_owners:
        already_signaled = owner_identity in signaled_owners
        if (
            not already_signaled
            and len(signaled_owners) >= control_client.MAXIMUM_CAPTURE_AWARE_SIGTERM_OWNERS
        ):
            raise control_client.CooperativeHandoffRequired(
                "native live control stream signal history is saturated"
            )
        if not already_signaled:
            try:
                revalidate_idle_owner()
                control_client.os.kill(owner.pid, control_client.signal.SIGTERM)
            except OSError as exc:
                control_client.log_handoff_outcome("fallback-failed", value)
                raise control_client.ControlUnavailable(
                    "native live control stream graceful replacement was unavailable"
                ) from exc
            signaled_owners.add(owner_identity)
            control_client.log_handoff_outcome("fallback-attempted", value)

    try:
        handoff.wait_for_handoff_exit(
            root,
            value,
            timeout_seconds=handoff.AUTOMATIC_GRACEFUL_EXIT_TIMEOUT_SECONDS,
        )
    except control_client.HandoffExitTimedOut:
        with control_client.capture_aware_sigterm_owners():
            try:
                revalidate_idle_owner()
            except control_client.CooperativeHandoffRequired as unavailable:
                # The exact owner can finish exiting just after the bounded
                # graceful wait. Recheck the canonical request, then let the
                # existing descriptor-and-lease settlement proof distinguish
                # that success from an unresponsive or replaced owner. Never
                # require a second launch attempt merely because the final
                # authenticated STATUS lost the race with normal teardown.
                if revalidate_request is not None:
                    revalidate_request()
                try:
                    handoff.wait_for_handoff_exit(root, value)
                except control_client.HandoffExitTimedOut as unsettled:
                    raise unavailable from unsettled
                control_client.log_handoff_outcome("fallback-completed", value)
                return
            try:
                kill_signal: _PosixSignalApi = control_client.signal
                control_client.os.kill(owner.pid, kill_signal.SIGKILL)
            except OSError as exc:
                control_client.log_handoff_outcome("fallback-failed", value)
                raise control_client.ControlUnavailable(
                    "native live control stream forced replacement was unavailable"
                ) from exc
            control_client.log_handoff_outcome("fallback-attempted", value)
        handoff.wait_for_handoff_exit(root, value)
    control_client.log_handoff_outcome("fallback-completed", value)


def replace_authenticated_live_windows_owner(
    client: control_client.ControlClient,
    root: Path,
    descriptor: ControlStreamDescriptor,
    *,
    expected_session_id: object,
    revalidate_request: Callable[[], None] | None,
) -> None:
    value: control_client.RawControlDescriptor = dict(descriptor)
    expected_path = control_client.resolved_path(
        descriptor.get("executablePath"),
        message="native live control stream Windows executable identity is unavailable",
    )
    app_path = control_client.resolved_path(
        descriptor.get("bundlePath"),
        message="native live control stream Windows app identity is unavailable",
    )
    expected_digest = descriptor.get("executableSHA256")
    if (
        not isinstance(expected_digest, str)
        or control_client.SHA256_HEX_PATTERN.fullmatch(expected_digest) is None
    ):
        raise control_client.CooperativeHandoffRequired(
            "native live control stream Windows executable identity is unavailable"
        )

    def revalidate_idle_owner() -> None:
        handoff.fresh_authenticated_live_stream_idle_state(
            client,
            root,
            descriptor,
            expected_session_id=expected_session_id,
            revalidate_request=revalidate_request,
        )

    handoff.terminate_verified_windows_owner_process(
        descriptor["pid"],
        expected_path=expected_path,
        app_path=app_path,
        expected_digest=expected_digest,
        digest_reader=control_client.sha256_regular_file,
        revalidate_owner=revalidate_idle_owner,
    )
    control_client.log_handoff_outcome("fallback-attempted", value)
    handoff.wait_for_handoff_exit(root, value)
    control_client.log_handoff_outcome("fallback-completed", value)


def replace_authenticated_live_stream_idle_owner(
    client: control_client.ControlClient,
    root: Path,
    descriptor: ControlStreamDescriptor,
    *,
    expected_session_id: object,
    revalidate_request: Callable[[], None] | None,
    verified_darwin_owner: VerifiedLiveDarwinOwner | None = None,
) -> None:
    """Dispatch one verified live owner through its platform process primitive."""

    platform = parse_control_platform(descriptor["platform"])
    if platform in handoff.COMPATIBLE_DARWIN_CONTROL_PLATFORMS:
        if verified_darwin_owner is None:
            raise control_client.CooperativeHandoffRequired(
                "native live control stream original Darwin process identity is unavailable"
            )
        replace_authenticated_live_darwin_owner(
            client,
            root,
            descriptor,
            owner=verified_darwin_owner,
            expected_session_id=expected_session_id,
            revalidate_request=revalidate_request,
        )
        return
    if (
        platform in handoff.COMPATIBLE_WINDOWS_CONTROL_PLATFORMS
        and control_client.is_windows_host()
    ):
        replace_authenticated_live_windows_owner(
            client,
            root,
            descriptor,
            expected_session_id=expected_session_id,
            revalidate_request=revalidate_request,
        )
        return
    raise control_client.ControlUnavailable("native live control stream platform is unsupported")
