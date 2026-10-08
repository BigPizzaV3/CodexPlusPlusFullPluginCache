"""Authenticated, capability-scoped ChatGPT Meetings companion protocol v2."""

from __future__ import annotations

import copy
import hashlib
import hmac
import os
import re
import secrets
import sys
import threading
import time
from collections.abc import Callable, Generator, Mapping
from contextlib import contextmanager
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Literal

import bootstrap_recovery
from bootstrap_recovery import record_authenticated_companion_recovery
from companion_control_v2 import (
    KNOWN_CAPABILITIES,
    MAX_FRAME_BYTES,
    PROTOCOL_VERSION,
    CompanionState,
    Descriptor,
    HomeSnapshot,
    MeetingsEligibility,
    QuitForUpdateResult,
    RecordingSummary,
    Request,
    SettingsState,
    is_companion_state,
    is_descriptor,
    is_home_snapshot,
    is_initialize_result,
    is_quit_for_update_result,
    is_request,
    is_settings_state,
    is_stop_recording_result,
    parse_initialize_result,
    parse_notification,
    parse_response,
    request_is_authorized,
)
from control_protocol import (
    ControlConnectionUnavailable,
    ControlEndpointRejected,
    ControlUnavailable,
    control_transport_error,
)
from control_transport.live_client import (
    LiveJsonRpcClient,
    LiveOwner,
    LiveTransportError,
    LiveTransportFailureKind,
    LiveTransportFailureReason,
)
from meetings_host_context import get_current_codex_version
from meetings_sentry import (
    MCP_SENTRY_COMPANION_DIAGNOSTIC_VALUES,
    report_companion_termination,
    report_mcp_error,
)
from native_runtime import PlatformRuntimeSpec, RuntimeManager, log_native_runtime_event

_DESCRIPTOR_FILENAME = "stream-descriptor.json"
_MAXIMUM_ORDINARY_REQUESTS = 14
_MAXIMUM_SAFE_INTEGER = 9_007_199_254_740_991
_BACKGROUND_CONNECTION_ATTEMPTS = 3
_BACKGROUND_CONNECTION_TIMEOUT_SECONDS = 5.0
_BACKGROUND_CONNECTION_RETRY_SECONDS = 0.25
_CONTEXT_RETRY_SECONDS = 5.0
_CONTEXT_SYNC_ATTEMPTS = 3
_EXPLICIT_RECOVERY_ATTEMPTS = 3
_EXPLICIT_RECOVERY_TIMEOUT_SECONDS = 1.0
_EXPLICIT_RECOVERY_RETRY_SECONDS = 0.1
# The schema knows these diagnostics before the upload UI can present them.
_PRODUCT_CAPABILITIES = tuple(
    capability
    for capability in KNOWN_CAPABILITIES
    if capability not in {"recording.encryption-errors.v1", "recording.database-version-errors.v1"}
)
_PRODUCT_METHODS = frozenset(
    {
        "companion.getState",
        "client.setContext",
        "recording.start",
        "recording.stop",
        "recording.getUploads",
        "recording.retry",
        "permissions.recheck",
        "permissions.request",
        "permissions.openSystemSettings",
        "settings.get",
        "settings.update",
        "home.getSnapshot",
        "lifecycle.quitForUpdate",
    }
)
_CLIENTS_LOCK = threading.RLock()
_CLIENTS: dict[tuple[str, str, int], CompanionClient] = {}
_DIAGNOSTICS_LOCK = threading.RLock()
_pending_listener_recovery: CompanionClient | None = None
_listener_recovery_pending = threading.Event()


class CompanionRecoveryOutcome(Enum):
    """Whether an explicit recovery found a responding owner or terminated it."""

    RESPONDING = "responding"
    TERMINATED = "terminated"


class CompanionReplacementPolicy(Enum):
    """Capture authority required by the shared exact-owner replacement path."""

    VERIFIED_IDLE = "verified-idle"
    EXPLICIT_UNRESPONSIVE = "explicit-unresponsive"
    CLICKED_START = "clicked-start"
    TERMINAL_BOOTSTRAP = "terminal-bootstrap"
    AUTOMATIC_UNRESPONSIVE = "automatic-unresponsive"
    CONFIRMED_UPDATE = "confirmed-update"


class _CaptureRecoverySafety(Enum):
    UNKNOWN = "unknown"
    IDLE = "idle"
    PROTECTED = "protected"
    START_AMBIGUOUS = "start-ambiguous"


@dataclass
class _CompanionDiagnosticState:
    """Bounded observations with a private, unreported connection callback fence."""

    stage: str = "not-started"
    descriptor_present: bool = False
    owner_verified: bool = False
    transport: str | None = None
    companion_pid: int | None = None
    companion_version: str | None = None
    native_owner_epoch: str | None = None
    # Reuse the connection object to fence callbacks; never expose this reference.
    client: CompanionClient | None = None
    connected: bool = False
    initialized: bool = False
    state_cached: bool = False
    state_revision: int | None = None
    recording_phase: str | None = None
    recording_summary: RecordingSummary | None = None
    connection_attempts: int = 0
    status_requests: int = 0
    status_successes: int = 0
    status_failures: int = 0
    status_outcome: str = "not-requested"
    status_reason: str | None = None
    last_failure_stage: str | None = None
    last_failure_reason: str | None = None
    last_error_type: str | None = None
    last_logged_status_failure: str | None = None
    reported_status_failures: set[tuple[tuple[str, str], ...]] = field(
        default_factory=set[tuple[tuple[str, str], ...]]
    )


_DIAGNOSTICS = _CompanionDiagnosticState()
_MAXIMUM_DIAGNOSTIC_COUNT = 9_007_199_254_740_991
_MAXIMUM_STATUS_FAILURE_REPORTS = 8


def _bounded_error_type(error: BaseException) -> str:
    """Expose only a safe exception class, never its message or arguments."""

    name = type(error).__name__
    return name if name.isascii() and name.isidentifier() and len(name) <= 64 else "UnknownError"


def _connection_failure_reason(error: BaseException) -> str:
    """Classify private transport failures without exposing their raw text."""

    if isinstance(error, LiveTransportError) and error.diagnostic_reason is not None:
        return error.diagnostic_reason.value
    message = str(error).lower()
    if "cancel" in message:
        return "cancelled"
    if "timed out" in message or "timeout" in message:
        return "timeout"
    if "capabilit" in message:
        return "capability-rejected"
    if "initializ" in message:
        return "initialization-rejected"
    if "descriptor" in message:
        return "descriptor-invalid"
    if "lease" in message:
        return "owner-lease-invalid"
    if "digest" in message or "executable" in message or "image" in message:
        return "owner-image-invalid"
    if "owner" in message or "peer" in message or "platform" in message:
        return "owner-mismatch"
    if "endpoint" in message:
        return "endpoint-unavailable"
    if "disconnect" in message:
        return "disconnected"
    if "malformed" in message or "invalid" in message:
        return "invalid-response"
    return "connection-failed"


def _observe_connection_failure(
    stage: str, error: BaseException, *, client: CompanionClient | None = None
) -> None:
    reason = _connection_failure_reason(error)
    error_type = _bounded_error_type(error)
    with _DIAGNOSTICS_LOCK:
        if client is not None and _DIAGNOSTICS.client is not client:
            return
        previous = (
            _DIAGNOSTICS.last_failure_stage,
            _DIAGNOSTICS.last_failure_reason,
            _DIAGNOSTICS.last_error_type,
        )
        _DIAGNOSTICS.stage = "failed"
        _DIAGNOSTICS.connected = False
        _DIAGNOSTICS.initialized = False
        _DIAGNOSTICS.native_owner_epoch = None
        _DIAGNOSTICS.client = None
        _DIAGNOSTICS.state_cached = False
        _DIAGNOSTICS.state_revision = None
        _DIAGNOSTICS.recording_phase = None
        _DIAGNOSTICS.recording_summary = None
        _DIAGNOSTICS.last_failure_stage = stage
        _DIAGNOSTICS.last_failure_reason = reason
        _DIAGNOSTICS.last_error_type = error_type
        changed = previous != (stage, reason, error_type)
    if changed:
        log_native_runtime_event(
            f"control-{stage}",
            "failed",
            error_kind=error_type,
            reason=reason,
            pid=os.getpid(),
        )


def observe_recording_status_request(
    outcome: str,
    *,
    error: BaseException | None = None,
    reason: str | None = None,
    duration_millis: int | None = None,
) -> None:
    """Count status outcomes and log only distinct failures, without private contents."""

    if outcome not in {"started", "loading", "ready", "failed"}:
        return
    should_log = False
    with _DIAGNOSTICS_LOCK:
        if outcome == "started":
            _DIAGNOSTICS.status_requests = min(
                _MAXIMUM_DIAGNOSTIC_COUNT,
                _DIAGNOSTICS.status_requests + 1,
            )
        else:
            if outcome == "ready":
                _DIAGNOSTICS.status_successes = min(
                    _MAXIMUM_DIAGNOSTIC_COUNT,
                    _DIAGNOSTICS.status_successes + 1,
                )
                _DIAGNOSTICS.last_logged_status_failure = None
                _DIAGNOSTICS.reported_status_failures.clear()
            elif outcome == "failed":
                _DIAGNOSTICS.status_failures = min(
                    _MAXIMUM_DIAGNOSTIC_COUNT,
                    _DIAGNOSTICS.status_failures + 1,
                )
                signature = f"{reason or ''}:{type(error).__name__ if error is not None else ''}"
                should_log = signature != _DIAGNOSTICS.last_logged_status_failure
                _DIAGNOSTICS.last_logged_status_failure = signature
            _DIAGNOSTICS.status_outcome = outcome
            _DIAGNOSTICS.status_reason = reason if outcome == "failed" else None
    if should_log:
        log_native_runtime_event(
            "recording-status",
            outcome,
            reason=reason,
            error_kind=_bounded_error_type(error) if error is not None else None,
            pid=os.getpid(),
            duration_ms=duration_millis,
        )
    # Only an actual unavailable status on a supported host is a native outage
    # observation. Invalid requests, exceptions/cancellation and loading are not.
    if (
        outcome == "failed"
        and error is None
        and type(reason) is str
        and reason in {"connection-failed", "owner-invalid", "companion-unavailable"}
        and sys.platform in {"darwin", "win32"}
    ):
        try:
            diagnostics = companion_failure_diagnostics()
            diagnostics["companion_status_reason"] = reason
            failure_signature = tuple(sorted(diagnostics.items()))
            with _DIAGNOSTICS_LOCK:
                reported = _DIAGNOSTICS.reported_status_failures
                if (
                    failure_signature in reported
                    or len(reported) >= _MAXIMUM_STATUS_FAILURE_REPORTS
                ):
                    return
                reported.add(failure_signature)
            report_mcp_error(
                "recording",
                "connection",
                operation="connection",
                error_source="connection",
                notification="connection_lost",
                companion_diagnostics=diagnostics,
            )
        except Exception:
            # Diagnostics must never replace the status result or change recovery.
            pass


def companion_failure_diagnostics() -> dict[str, str]:
    """Select cached observations only; never probe the owner, disk or authentication."""

    with _DIAGNOSTICS_LOCK:
        candidates = {
            "companion_status_reason": _DIAGNOSTICS.status_reason,
            "companion_observed_stage": _DIAGNOSTICS.stage,
            "companion_observed_failure_stage": _DIAGNOSTICS.last_failure_stage,
            "companion_observed_failure_reason": _DIAGNOSTICS.last_failure_reason,
            "companion_observed_descriptor_present": str(_DIAGNOSTICS.descriptor_present).lower(),
            "companion_observed_owner_verified": str(_DIAGNOSTICS.owner_verified).lower(),
            "companion_observed_connected": str(_DIAGNOSTICS.connected).lower(),
            "companion_observed_initialized": str(_DIAGNOSTICS.initialized).lower(),
            "companion_observed_state_cached": str(_DIAGNOSTICS.state_cached).lower(),
        }
    # Do not nest the connection and bootstrap locks. Both snapshots are past
    # observations, not proof of current readiness or the cause of a UI impression.
    with bootstrap_recovery.lock:
        if failure := bootstrap_recovery.state.last_failure:
            candidates["bootstrap_last_failure_reason"] = failure.sentry_reason
        if bootstrap_diagnostics := bootstrap_recovery.state.last_failure_diagnostics:
            candidates["bootstrap_last_failure_operation"] = bootstrap_diagnostics[
                "failure_operation"
            ]
            candidates["bootstrap_last_resource_role"] = bootstrap_diagnostics["resource_role"]
            candidates["bootstrap_last_os_error_code"] = bootstrap_diagnostics["os_error_code"]
    return {
        key: value
        for key, value in candidates.items()
        if type(value) is str and value in MCP_SENTRY_COMPANION_DIAGNOSTIC_VALUES[key]
    }


def companion_connection_diagnostics() -> dict[str, object]:
    """Read memory-only native and status observations without auth or filesystem I/O."""

    with _DIAGNOSTICS_LOCK:
        failure: dict[str, object] | None = None
        if _DIAGNOSTICS.last_failure_stage is not None:
            failure = {
                "stage": _DIAGNOSTICS.last_failure_stage,
                "reason": _DIAGNOSTICS.last_failure_reason,
                "errorType": _DIAGNOSTICS.last_error_type,
            }
        return {
            "mcpPid": os.getpid(),
            "stage": _DIAGNOSTICS.stage,
            "descriptorPresent": _DIAGNOSTICS.descriptor_present,
            "ownerVerified": _DIAGNOSTICS.owner_verified,
            "transport": _DIAGNOSTICS.transport,
            "companionPid": _DIAGNOSTICS.companion_pid,
            "companionVersion": _DIAGNOSTICS.companion_version,
            "nativeOwnerEpoch": _DIAGNOSTICS.native_owner_epoch,
            "protocolVersion": PROTOCOL_VERSION if _DIAGNOSTICS.initialized else None,
            "connected": _DIAGNOSTICS.connected,
            "initialized": _DIAGNOSTICS.initialized,
            "stateCached": _DIAGNOSTICS.state_cached,
            "stateRevision": _DIAGNOSTICS.state_revision,
            "recordingPhase": _DIAGNOSTICS.recording_phase,
            "recordingSummary": copy.deepcopy(_DIAGNOSTICS.recording_summary),
            "connectionAttempts": _DIAGNOSTICS.connection_attempts,
            "statusRequests": _DIAGNOSTICS.status_requests,
            "statusSuccesses": _DIAGNOSTICS.status_successes,
            "statusFailures": _DIAGNOSTICS.status_failures,
            "lastStatusOutcome": _DIAGNOSTICS.status_outcome,
            "lastFailure": failure,
        }


@dataclass(frozen=True, repr=False)
class CompanionOwner:
    """One local descriptor and its owner metadata.

    Attributes:
        root: Private companion-control directory.
        descriptor: Generated, strictly validated v2 owner descriptor.
        runtime: Owner image metadata, verified separately before process termination.
    """

    root: Path
    descriptor: Descriptor
    runtime: Mapping[str, object]

    def uses_runtime_image(self, runtime: Mapping[str, object]) -> bool:
        """Compare the selected image without revoking this verified live owner."""

        try:
            _verify_runtime_identity(self.descriptor, runtime)
        except ControlUnavailable:
            return False
        return True


def discover_companion_owner(
    *,
    runtime: Mapping[str, object] | None = None,
    allow_existing_owner: bool = False,
) -> CompanionOwner:
    """Discover one v2 companion without granting v1 product authority.

    Args:
        runtime: Optional reviewed runtime identity for this request.
        allow_existing_owner: Connect to the running owner independently of the
            selected installation. The transport authenticates its process.

    Returns:
        The validated descriptor and captured owner metadata.

    Raises:
        ControlUnavailable: If owner, descriptor, runtime, or lease proof fails.
    """

    import control_client

    root = control_client.control_root()
    with _DIAGNOSTICS_LOCK:
        if _DIAGNOSTICS.stage not in {"ready", "connecting", "initializing"}:
            _DIAGNOSTICS.stage = "discovering"
    try:
        control_client.require_private(root, directory=True)
        raw = control_client.read_json(root / _DESCRIPTOR_FILENAME)
        if not is_descriptor(raw):
            raise ControlUnavailable("native companion v2 descriptor is unavailable")
    except (ControlUnavailable, OSError, ValueError) as error:
        with _DIAGNOSTICS_LOCK:
            _DIAGNOSTICS.descriptor_present = False
            _DIAGNOSTICS.owner_verified = False
            _DIAGNOSTICS.transport = None
            _DIAGNOSTICS.companion_pid = None
            _DIAGNOSTICS.companion_version = None
        _observe_connection_failure("discovery", error)
        raise

    with _DIAGNOSTICS_LOCK:
        observed_client = _DIAGNOSTICS.client
        owner_changed = _DIAGNOSTICS.companion_pid != raw["pid"] or (
            observed_client is not None
            and (
                observed_client.owner.root != root
                or observed_client.owner.descriptor["ownerEpoch"] != raw["ownerEpoch"]
            )
        )
        if owner_changed:
            _DIAGNOSTICS.owner_verified = False
            _DIAGNOSTICS.connected = False
            _DIAGNOSTICS.initialized = False
            _DIAGNOSTICS.native_owner_epoch = None
            _DIAGNOSTICS.client = None
            _DIAGNOSTICS.state_cached = False
            _DIAGNOSTICS.state_revision = None
            _DIAGNOSTICS.recording_phase = None
            _DIAGNOSTICS.recording_summary = None
        _DIAGNOSTICS.descriptor_present = True
        _DIAGNOSTICS.companion_pid = raw["pid"]
        _DIAGNOSTICS.companion_version = raw["companionVersion"]
        _DIAGNOSTICS.transport = raw["transport"]
        if _DIAGNOSTICS.stage not in {"ready", "connecting", "initializing"}:
            _DIAGNOSTICS.stage = "owner-verification"
    if owner_changed:
        log_native_runtime_event(
            "control-discovery",
            "descriptor-found",
            pid=os.getpid(),
        )

    try:
        if allow_existing_owner:
            # Installation files can change while their process is still recording.
            identity = raw["executableIdentity"]
            executable = Path(identity["path"])
            windows = raw["platform"] == "windows"
            owner_runtime: Mapping[str, object] = {
                "installed": True,
                "source": "running-companion",
                "platform": f"{'windows' if windows else 'darwin'}-{raw['architecture']}",
                "artifactKind": "windows-executable" if windows else "macos-app-bundle",
                "appPath": str(executable if windows else executable.parent.parent.parent),
                "_executableSHA256": identity["sha256"],
                "_executableDevice": identity.get("device"),
                "_executableInode": identity.get("inode"),
            }
        else:
            owner_runtime = runtime if runtime is not None else RuntimeManager().status()
            _verify_runtime_identity(raw, owner_runtime)
        if control_client.owner_lock_state(root) != "held":
            raise ControlUnavailable("native companion owner lease is unavailable")
        if control_client.pid_is_proven_dead(raw["pid"]):
            raise ControlUnavailable("native companion owner is unavailable")
    except (ControlUnavailable, OSError, ValueError) as error:
        with _DIAGNOSTICS_LOCK:
            _DIAGNOSTICS.owner_verified = False
        _observe_connection_failure("owner-verification", error)
        raise

    with _DIAGNOSTICS_LOCK:
        newly_verified = not _DIAGNOSTICS.owner_verified
        _DIAGNOSTICS.owner_verified = True
        if _DIAGNOSTICS.stage == "owner-verification":
            _DIAGNOSTICS.stage = "owner-verified"
    if newly_verified:
        log_native_runtime_event(
            "control-owner",
            "verified",
            pid=os.getpid(),
        )
    return CompanionOwner(root=root, descriptor=raw, runtime=owner_runtime)


def _verify_runtime_platform(descriptor: Descriptor, runtime: Mapping[str, object]) -> None:
    """Match native architecture, including host-specific owners of universal apps."""

    platform = runtime.get("platform")
    artifact_kind = runtime.get("artifactKind")
    architecture = descriptor["architecture"]
    if descriptor["platform"] == "windows":
        if (
            platform != f"windows-{architecture}"
            or artifact_kind != "windows-executable"
            or descriptor["endpoint"] != rf"\\.\pipe\chatgpt-meetings-{descriptor['ownerEpoch']}"
        ):
            raise ControlUnavailable("native companion platform does not match")
    elif (
        not isinstance(platform, str)
        or not platform.startswith("darwin-")
        or artifact_kind != "macos-app-bundle"
        or (
            platform != "darwin-universal"
            and architecture not in {"universal", platform.removeprefix("darwin-")}
        )
    ):
        raise ControlUnavailable("native companion platform does not match")


def _verify_runtime_identity(
    descriptor: Descriptor,
    runtime: Mapping[str, object],
) -> None:
    import control_client

    if runtime.get("installed") is not True:
        raise ControlUnavailable("verified native runtime is unavailable")
    _verify_runtime_platform(descriptor, runtime)
    platform = runtime.get("platform")

    identity = descriptor["executableIdentity"]
    expected_digest = runtime.get("_executableSHA256")
    if not isinstance(expected_digest, str) or not hmac.compare_digest(
        identity["sha256"], expected_digest
    ):
        raise ControlUnavailable("native companion executable digest does not match")

    app_path = runtime.get("appPath")
    if not isinstance(app_path, str) or not isinstance(platform, str):
        raise ControlUnavailable("native companion executable identity is unavailable")
    try:
        expected = control_client.expected_executable_path(
            Path(app_path),
            control_client.runtime_spec_for(platform),
        ).resolve(strict=True)
        actual = Path(identity["path"]).resolve(strict=True)
    except (OSError, ValueError, control_client.NativeRuntimeError) as exc:
        raise ControlUnavailable("native companion executable identity is unavailable") from exc
    if os.path.normcase(str(actual)) != os.path.normcase(str(expected)):
        raise ControlUnavailable("native companion executable path does not match")

    if descriptor["platform"] == "macos":
        expected_device = runtime.get("_executableDevice")
        expected_inode = runtime.get("_executableInode")
        if (
            type(expected_device) is not int
            or type(expected_inode) is not int
            or identity.get("device") != expected_device
            or identity.get("inode") != expected_inode
        ):
            raise ControlUnavailable("native companion executable identity does not match")


class VerifiedCompanionRelease(str):
    """MCP-only provenance marker; JSON/native strings cannot supply this proof."""


class CompanionClient:
    """Persistent authenticated v2 owner, pushed state, and capability routing."""

    def __init__(
        self,
        owner: CompanionOwner,
        *,
        on_workspace_changed: Callable[[str, str], None] | None = None,
        on_recording_completed: Callable[[str], None] | None = None,
    ) -> None:
        """Bind transport verification to one exact companion owner.

        Args:
            owner: Generated descriptor and independently reviewed runtime.
            on_workspace_changed: Optional private account-bound change callback.
            on_recording_completed: Optional exact native session completion callback.
        """

        self._owner = owner
        self._transport_endpoint = owner.descriptor["endpoint"]
        self._lock = threading.RLock()
        self._connection_lock = threading.Lock()
        self._connection_generation = 0
        self._transport_generation = 0
        self._context_lock = threading.Lock()
        self._codex_app_version = ""
        self._synced_codex_app_version = ""
        self._context_generation = 0
        self._context_retry_after = 0.0
        self._background_connection: threading.Thread | None = None
        self._background_connection_error: ControlUnavailable | None = None
        self._listener_recovery_error: ControlUnavailable | None = None
        self._listener_recovery_attempted = False
        self._listener_recovery_request_id: str | None = None
        self._listener_recovery_observation = 0
        self._listener_recovery_birth_identity: tuple[int, int] | None = None
        self._listener_recovery_retry_after = 0.0
        self._listener_recovery_retry_delay = 0.0
        self._connection_cancelled = threading.Event()
        self._submission_lock = threading.Lock()
        self._capture_recovery_lock = threading.Lock()
        self._capture_recovery_safety = _CaptureRecoverySafety.UNKNOWN
        self._capture_observation = 0
        self._bootstrap_capture_observed = False
        self._bootstrap_recovery_requested = False
        self._bootstrap_recovery_in_progress = False
        self._bootstrap_recovery_signalled = False
        self._client_id = f"mcp_{secrets.token_hex(16)}"
        self._sequence = 0
        self._state: CompanionState | None = None
        self._verified_release_version: str | None = None
        self._revision = -1
        self._negotiated_capabilities: frozenset[str] = frozenset()
        self._pending_requests: dict[str, Request] = {}
        self._ordinary_capacity = threading.BoundedSemaphore(_MAXIMUM_ORDINARY_REQUESTS)
        self._on_workspace_changed = on_workspace_changed
        self._on_recording_completed = on_recording_completed
        self._workspace_revisions: dict[str, int] = {"calendar": 0, "notes": 0}
        self._observed_recording_session: str | None = None
        self._completed_recording_session: str | None = None
        self._stopped_recording_note: tuple[str, str, str] | None = None
        self._transport = self._new_transport()

    def _new_transport(self) -> LiveJsonRpcClient:
        descriptor = self._owner.descriptor
        return LiveJsonRpcClient(
            LiveOwner(
                endpoint=self._transport_endpoint,
                pid=descriptor["pid"],
                transport=descriptor["transport"],
            ),
            maximum_frame_bytes=MAX_FRAME_BYTES,
            verify_owner=self._verify_owner,
            validate_response=self._validate_response,
            on_notification=self._accept_notification,
            on_disconnect=self._invalidate,
        )

    def recover_listener(self, *, cancellation_event: threading.Event | None = None) -> bool:
        """Challenge a failed listener once, then authenticate its same-owner replacement."""
        from companion_health import request_listener_repair

        with self._lock:
            failure = self._listener_recovery_error
            if self._listener_recovery_attempted:
                raise ControlUnavailable("native listener recovery was already attempted")
            if failure is None:
                return False
            if not _listener_recovery_failed(failure):
                raise ControlUnavailable("native listener recovery has no failed endpoint proof")
            self.require_unchanged_capture_observation(self._listener_recovery_observation)
            self._listener_recovery_attempted = True
        _, birth_identity = _verify_listener_recovery_owner(self)
        self._listener_recovery_birth_identity = birth_identity

        def revalidate() -> None:
            if cancellation_event is not None and cancellation_event.is_set():
                raise ControlUnavailable("native listener recovery was cancelled")
            _verify_listener_recovery_owner(self, birth_identity=birth_identity)
            self.require_unchanged_capture_observation(self._listener_recovery_observation)

        def requested(request_id: str) -> None:
            with self._lock:
                self._listener_recovery_request_id = request_id

        owner = self.owner
        endpoint = request_listener_repair(
            owner.root,
            owner_epoch=owner.descriptor["ownerEpoch"],
            pid=owner.descriptor["pid"],
            revalidate_owner=revalidate,
            cancellation_event=cancellation_event or self._connection_cancelled,
            on_request=requested,
        )
        if endpoint is None:
            return False
        if cancellation_event is not None and cancellation_event.is_set():
            raise ControlUnavailable("native listener recovery was cancelled")
        owner, _ = _verify_listener_recovery_owner(self, birth_identity=birth_identity)
        transport_descriptor = dict(owner.descriptor)
        transport_descriptor["endpoint"] = endpoint
        if not is_descriptor(transport_descriptor):
            raise ControlUnavailable("native listener endpoint is malformed")
        _verify_runtime_platform(transport_descriptor, owner.runtime)
        # A same-owner transport refresh keeps ambiguous Start and capture history.
        # The ordinary handshake alone may publish new recording/session authority.
        self._refresh_listener_transport(endpoint)
        self.get_state(timeout_seconds=1.0, cancellation_event=cancellation_event)
        return True

    @property
    def owner(self) -> CompanionOwner:
        """Return the exact authenticated v2 owner and reviewed runtime."""

        return self._owner

    @property
    def closed(self) -> bool:
        """Whether this exact owner client has been retired."""
        return self._connection_cancelled.is_set()

    @property
    def listener_recovery_birth_identity(self) -> tuple[int, int] | None:
        """Original process birth pinned before a listener health challenge."""
        return self._listener_recovery_birth_identity

    def require_listener_recovery_unanswered(self) -> None:
        """Check the file reply before revalidating in-memory recovery authority."""
        from companion_health import listener_repair_acknowledged

        with self._lock:
            request_id = self._listener_recovery_request_id
        if request_id is not None and listener_repair_acknowledged(
            self.owner.root,
            owner_epoch=self.owner.descriptor["ownerEpoch"],
            request_id=request_id,
        ):
            raise ControlUnavailable("native companion responded during recovery")
        self.require_listener_recovery_allowed()

    def require_listener_recovery_allowed(self) -> None:
        """Recheck failed-I/O and capture authority without filesystem work."""
        with self._lock:
            failure = self._listener_recovery_error
            if failure is None or not _listener_recovery_failed(failure):
                raise ControlUnavailable("native recovery requires a failed endpoint operation")
            self.require_unchanged_capture_observation(self._listener_recovery_observation)

    def finish_listener_recovery(self) -> None:
        """Let later failed reads rearm one backed-off attempt, without a heartbeat."""
        with self._lock:
            self._listener_recovery_attempted = False
            self._listener_recovery_request_id = None
            if self._listener_recovery_error is not None:
                self._listener_recovery_retry_delay = min(
                    60.0, max(5.0, self._listener_recovery_retry_delay * 2)
                )
                self._listener_recovery_retry_after = (
                    time.monotonic() + self._listener_recovery_retry_delay
                )

    @property
    def negotiated_capabilities(self) -> frozenset[str]:
        """Return only capabilities actually negotiated with this owner."""

        with self._lock:
            return self._negotiated_capabilities

    def connect(
        self,
        *,
        timeout_seconds: float = 5.0,
        cancellation_event: threading.Event | None = None,
    ) -> None:
        """Authenticate the owner and negotiate the generated v2 contract.

        Args:
            timeout_seconds: Maximum initialization and owner-verification duration.
            cancellation_event: Optional cancellation for this request only.

        Raises:
            ControlUnavailable: If the owner or generated initialization is invalid.
        """

        deadline = time.monotonic() + max(0.0, timeout_seconds)
        acquired = False
        connection_failure: ControlUnavailable | None = None
        observed_capture: int | None = None
        while not acquired:
            if self._connection_cancelled.is_set() or (
                cancellation_event is not None and cancellation_event.is_set()
            ):
                raise ControlUnavailable("native companion connection was cancelled")
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise ControlConnectionUnavailable("native companion connection timed out")
            acquired = self._connection_lock.acquire(timeout=min(0.05, remaining))
        try:
            with self._lock:
                if self._connection_cancelled.is_set():
                    raise ControlUnavailable("native companion connection was cancelled")
                if self._transport.connected and self._state is not None:
                    return
                # Retire presentation before reconnecting. A previous reader
                # may still be delivering its disconnect callback after this.
                self._invalidate()
                generation = self._connection_generation
                observed_capture = self._capture_observation
            request_id = f"init_{secrets.token_hex(16)}"
            request: dict[str, object] = {
                "jsonrpc": "2.0",
                "id": request_id,
                "method": "companion.initialize",
                "params": {
                    "protocolVersion": PROTOCOL_VERSION,
                    "client": {
                        "id": self._client_id,
                        "kind": "meetings-mcp",
                        "version": _plugin_version(),
                    },
                    "requestedCapabilities": list(_PRODUCT_CAPABILITIES),
                },
            }
            if not is_request(request):
                raise ControlUnavailable("native companion initialization is malformed")
            with _DIAGNOSTICS_LOCK:
                if self._connection_cancelled.is_set():
                    raise ControlUnavailable("native companion connection was cancelled")
                _DIAGNOSTICS.client = self
                _DIAGNOSTICS.native_owner_epoch = None
                _DIAGNOSTICS.stage = "initializing"
                _DIAGNOSTICS.connection_attempts = min(
                    _MAXIMUM_DIAGNOSTIC_COUNT,
                    _DIAGNOSTICS.connection_attempts + 1,
                )
                attempt = _DIAGNOSTICS.connection_attempts
            log_native_runtime_event(
                "control-initialize",
                "started",
                attempt=attempt,
                pid=os.getpid(),
            )
            try:
                self._transport.connect(
                    dict(request),
                    validate_result=self._validate_initialize_result,
                    on_initialized=self._publish_initialize_result,
                    deadline=deadline,
                    cancellation_event=cancellation_event or self._connection_cancelled,
                    on_notification=lambda value: self._accept_notification(
                        value, connection_generation=generation
                    ),
                    on_disconnect=lambda: self._invalidate(connection_generation=generation),
                )
            except LiveTransportError as exc:
                _observe_connection_failure("initialize", exc, client=self)
                connection_failure = control_transport_error(
                    exc, "native companion v2 connection failed"
                )
                raise connection_failure from exc
        finally:
            self._connection_lock.release()
            if (
                connection_failure is not None
                and self._background_connection is None
                and (cancellation_event is None or not cancellation_event.is_set())
            ):
                self._schedule_listener_recovery(
                    connection_failure, observed_capture=observed_capture
                )

    def connect_in_background(self) -> ControlUnavailable | None:
        """Start one shared owner-bound connection without blocking a status read.

        Returns:
            The last failed connection episode, if any. Transient failures get
            another coalesced background attempt while the existing recovery UI
            remains available. Authenticated success clears the failure.
        """

        with self._lock:
            recovery_failure = self._listener_recovery_error
            recovery_observation = self._listener_recovery_observation
        if recovery_failure is not None:
            self._schedule_listener_recovery(
                recovery_failure, observed_capture=recovery_observation
            )
        with self._lock:
            if self._state is not None and self._transport.connected:
                self._background_connection_error = None
                if (
                    not self._codex_context_pending()
                    or time.monotonic() < self._context_retry_after
                ):
                    return None
            if self._background_connection is not None:
                return self._background_connection_error
            failure = self._background_connection_error
            if failure is not None and not isinstance(failure, ControlConnectionUnavailable):
                return failure
            if self._connection_cancelled.is_set():
                return ControlUnavailable("native companion connection was cancelled")
            worker = threading.Thread(
                target=self._connect_in_background,
                name="meetings-companion-connection",
                daemon=True,
            )
            self._background_connection = worker
            with _DIAGNOSTICS_LOCK:
                _DIAGNOSTICS.stage = "connecting"
            worker.start()
            return failure

    def _connect_in_background(self) -> None:
        failure: ControlUnavailable | None = None
        version = ""
        try:
            for attempt in range(_BACKGROUND_CONNECTION_ATTEMPTS):
                if self._connection_cancelled.is_set():
                    return
                try:
                    self.connect(
                        timeout_seconds=_BACKGROUND_CONNECTION_TIMEOUT_SECONDS,
                        cancellation_event=self._connection_cancelled,
                    )
                    deadline = time.monotonic() + _BACKGROUND_CONNECTION_TIMEOUT_SECONDS
                    with self._codex_context_guard(deadline, self._connection_cancelled):
                        while True:
                            with self._lock:
                                version = self._codex_app_version
                            self._sync_codex_context(version, deadline, self._connection_cancelled)
                            with self._lock:
                                if version == self._codex_app_version:
                                    break
                    # Only selected-runtime status/settings reads use this worker.
                    # An old-owner handoff probe connects synchronously instead.
                    record_authenticated_companion_recovery()
                    failure = None
                    return
                except ControlConnectionUnavailable as exc:
                    failure = exc
                    if attempt + 1 == _BACKGROUND_CONNECTION_ATTEMPTS:
                        return
                    if self._connection_cancelled.wait(
                        _BACKGROUND_CONNECTION_RETRY_SECONDS * (2**attempt)
                    ):
                        return
                except ControlUnavailable as exc:
                    failure = exc
                    return
        finally:
            with self._lock:
                connected = self._state is not None and self._transport.connected
                if not self._connection_cancelled.is_set():
                    # A context rejection on an authenticated stream must not
                    # poison later synchronization like an unsafe owner does.
                    if failure is not None and connected:
                        self._background_connection_error = None
                        self._context_retry_after = (
                            time.monotonic() + _CONTEXT_RETRY_SECONDS
                            if version == self._codex_app_version
                            else 0.0
                        )
                    else:
                        self._background_connection_error = failure
                self._background_connection = None
                resync = (
                    not self._connection_cancelled.is_set()
                    and connected
                    and self._codex_context_pending()
                    and (failure is None or version != self._codex_app_version)
                )
            if resync:
                # Close the observation/worker-completion race without adding
                # a polling task or dropping an update until the next read.
                self.connect_in_background()
            elif failure is not None and not connected:
                self._schedule_listener_recovery(failure)

    def _schedule_listener_recovery(
        self, error: ControlUnavailable, *, observed_capture: int | None = None
    ) -> None:
        global _pending_listener_recovery

        if not _listener_recovery_failed(error):
            return
        with self._lock:
            if self._connection_cancelled.is_set() or (
                observed_capture is not None and self._capture_observation != observed_capture
            ):
                return
            self._listener_recovery_error = error
            self._listener_recovery_observation = self._capture_observation
            if (
                self._listener_recovery_attempted
                or self._background_connection is not None
                or self._capture_recovery_lock.locked()
                or time.monotonic() < self._listener_recovery_retry_after
            ):
                return
        with _CLIENTS_LOCK:
            _pending_listener_recovery = self
            _listener_recovery_pending.set()
        from meetings_mcp_lifecycle import schedule_initialize_companion_bootstrap

        schedule_initialize_companion_bootstrap(require_owner_response=True)

    def _refresh_listener_transport(self, endpoint: str) -> None:
        """Retire endpoint callbacks while retaining this owner's capture fences."""
        if not self._connection_lock.acquire(timeout=1.0):
            raise ControlUnavailable("native listener connection is busy")
        submission_acquired = False
        try:
            submission_acquired = self._submission_lock.acquire(timeout=1.0)
            if not submission_acquired:
                raise ControlUnavailable("native listener request submission is busy")
            with self._lock:
                if self._connection_cancelled.is_set():
                    raise ControlUnavailable("native listener recovery was cancelled")
                # A timed-out health read does not retire an accepted Stop.
                # Preserve its stream through completion publication; once the
                # call finishes or times out, a later repair can replace it.
                if self._transport.connected and any(
                    request["method"] == "recording.stop"
                    for request in self._pending_requests.values()
                ):
                    return
                self._transport_generation += 1
                self._invalidate()
                previous = self._transport
            previous.close()
            with self._lock:
                self._transport_endpoint = endpoint
                self._transport = self._new_transport()
                self._background_connection_error = None
                self._listener_recovery_error = None
                self._listener_recovery_attempted = False
                self._listener_recovery_request_id = None
                self._listener_recovery_birth_identity = None
        finally:
            if submission_acquired:
                self._submission_lock.release()
            self._connection_lock.release()

    def observe_codex_version(self, version: str) -> None:
        """Retain a validated desktop observation for this exact native owner."""

        if version:
            with self._lock:
                if version != self._codex_app_version:
                    self._context_retry_after = 0.0
                self._codex_app_version = version

    def _codex_context_pending(self) -> bool:
        return (
            "client.context.v1" in self._negotiated_capabilities
            and bool(self._codex_app_version)
            and self._codex_app_version != self._synced_codex_app_version
        )

    @contextmanager
    def _codex_context_guard(
        self, deadline: float, cancellation_event: threading.Event | None
    ) -> Generator[None, None, None]:
        # Serialize context changes with Start; Stop never takes this lock.
        while True:
            if self._connection_cancelled.is_set() or (
                cancellation_event is not None and cancellation_event.is_set()
            ):
                raise ControlUnavailable("native companion request was cancelled")
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise ControlConnectionUnavailable("native companion request timed out")
            if self._context_lock.acquire(timeout=min(0.05, remaining)):
                break
        try:
            yield
        finally:
            self._context_lock.release()

    def _sync_codex_context(
        self,
        version: str,
        deadline: float,
        cancellation_event: threading.Event | None,
    ) -> None:
        while version:
            self.connect(
                timeout_seconds=max(0.0, deadline - time.monotonic()),
                cancellation_event=cancellation_event,
            )
            with self._lock:
                if (
                    "client.context.v1" not in self._negotiated_capabilities
                    or version == self._synced_codex_app_version
                ):
                    return
                generation = self._context_generation
            self._call(
                "client.setContext",
                {"codexAppVersion": version},
                timeout_seconds=max(0.0, deadline - time.monotonic()),
                cancellation_event=cancellation_event,
            )
            with self._lock:
                if generation == self._context_generation and self._transport.connected:
                    self._synced_codex_app_version = version
                    return

    def remember_verified_release_version(self, release: str) -> None:
        """Retain this exact owner's verified release for policy presentation only.

        Only the immutable-image proof may supply this value. It does not grant
        control, launch or replacement authority and never replaces fresh checks.
        """

        with self._lock:
            self._verified_release_version = release

    def latest_state(self) -> CompanionState | None:
        """Read an isolated owner-bound state without performing companion I/O.

        Returns:
            The latest validated state, or ``None`` for a disconnected owner.
        """

        with self._lock:
            return copy.deepcopy(self._state) if self._state is not None else None

    def cached_meetings_eligibility(
        self,
        *,
        account_scope: str | None,
        platform: Literal["macos", "windows"],
        plugin_version: str,
        codex_version: str,
    ) -> MeetingsEligibility | None:
        """Read native policy only for the current account and acknowledged client.

        ``None`` means this owner does not support the extension. A supported
        owner with missing or mismatched context remains explicitly unresolved;
        it cannot borrow another account's or connection's accepted decision.
        This read performs no authentication, transport or network work.
        """

        with self._lock:
            if (
                "meetings.eligibility.v1" not in self._negotiated_capabilities
                or not self._transport.connected
                or self._state is None
            ):
                return None
            unresolved: MeetingsEligibility = {"status": "unresolved"}
            observation = self._state.get("meetingsEligibility", unresolved)
            decision = observation.get("decision")
            if decision is None:
                return copy.deepcopy(observation)
            expected_codex = codex_version or self._codex_app_version
            if (
                account_scope is None
                or self._state["accountScopeFingerprint"] != account_scope
                or decision["platform"] != platform
                or decision["client"]["pluginVersion"] != plugin_version
                or decision["client"].get("codexVersion", "") != expected_codex
                or (expected_codex and self._synced_codex_app_version != expected_codex)
            ):
                return unresolved
            return copy.deepcopy(observation)

    def _observe_capture_response(self, state: CompanionState) -> None:
        """Retain authenticated activity even when its revision cannot update UI state."""

        self._capture_observation += 1
        self._listener_recovery_error = None
        self._listener_recovery_retry_after = 0.0
        self._listener_recovery_retry_delay = 0.0
        if state["recording"]["phase"] in {"starting", "recording", "stopping"} or (
            state["recording"]["session"] is not None
        ):
            self._bootstrap_capture_observed = True

    def _observe_capture_recovery_safety(
        self, state: CompanionState, *, start_completed: bool = False
    ) -> None:
        """Retain capture evidence when transport invalidation clears UI state."""

        if (
            self._capture_recovery_safety is _CaptureRecoverySafety.START_AMBIGUOUS
            and not start_completed
            and state["recording"]["phase"] not in {"starting", "recording", "stopping"}
        ):
            return
        if (
            state["recording"]["phase"] != "idle"
            or not state["lifecycle"]["replacement"]["allowed"]
        ):
            self._capture_recovery_safety = _CaptureRecoverySafety.PROTECTED
        else:
            # A late idle read alone cannot reconcile a possibly admitted Start.
            self._capture_recovery_safety = _CaptureRecoverySafety.IDLE

    def require_explicit_recovery_allowed(self) -> None:
        """Reject replacement when this exact owner may still be capturing."""

        import control_client

        with self._lock:
            if self._capture_recovery_safety in {
                _CaptureRecoverySafety.PROTECTED,
                _CaptureRecoverySafety.START_AMBIGUOUS,
            }:
                raise control_client.CooperativeHandoffDeclined(
                    "native companion capture may still be active",
                    recovery_blocker="ambiguous-start"
                    if self._capture_recovery_safety is _CaptureRecoverySafety.START_AMBIGUOUS
                    else "active-or-unfinished-capture",
                )

    def require_unchanged_capture_observation(self, observation: int) -> None:
        """Revoke clicked force authority as soon as this owner responds again."""

        import control_client

        with self._lock:
            if self._capture_observation != observation:
                raise control_client.CooperativeHandoffDeclined(
                    "native companion responded during clicked recovery",
                    recovery_blocker="owner-responded-during-recovery",
                )

    def terminal_bootstrap_recovery_observation(
        self, *, fresh_state: CompanionState | None = None
    ) -> int | None:
        """Capture terminal native proof with no retained capture or ambiguous Start."""

        with self._lock:
            if fresh_state is not None and fresh_state != self._state:
                return None
            if (
                not self._bootstrap_recovery_requested
                and not self._bootstrap_recovery_in_progress
                and not self.bootstrap_recovery_pending()
                and self.bootstrap_recovery_status() in {"restartable", "exhausted"}
            ):
                return self._capture_observation
            return None

    @contextmanager
    def explicit_recovery_guard(
        self, *, for_clicked_start: bool = False
    ) -> Generator[Callable[[], None], None, None]:
        """Fence Start admission while one explicit owner recovery is in progress."""

        import control_client

        if not self._capture_recovery_lock.acquire(blocking=False):
            raise control_client.CooperativeHandoffDeclined(
                "native companion capture or recovery is already in progress",
                recovery_blocker="capture-or-recovery-in-progress",
            )
        try:
            with self._lock:
                observation = self._capture_observation

            def revalidate() -> None:
                if not for_clicked_start:
                    self.require_explicit_recovery_allowed()
                    return
                self.require_unchanged_capture_observation(observation)

            revalidate()
            yield revalidate
        finally:
            self._capture_recovery_lock.release()

    def bootstrap_recovery_status(self) -> Literal["restartable", "restarting", "exhausted"] | None:
        """Read negotiated terminal-bootstrap proof, retaining all capture fences."""

        with self._lock:
            state = self._state
            if (
                "lifecycle.bootstrap-recovery.v1" not in self._negotiated_capabilities
                or state is None
                or self._bootstrap_capture_observed
                or self._capture_recovery_safety is _CaptureRecoverySafety.START_AMBIGUOUS
            ):
                return None
            recording = state["recording"]
            if (
                recording["phase"] != "unavailable"
                or recording["session"] is not None
                or recording["controls"]["start"]["enabled"]
                or recording["controls"]["stop"]["enabled"]
                or state["lifecycle"]["replacement"]["allowed"]
            ):
                return None
            recovery = state["lifecycle"].get("bootstrapRecovery")
            return recovery["status"] if recovery is not None else None

    def bootstrap_recovery_pending(self) -> bool:
        """Keep recovery presentation quiet without granting capture authority."""

        with self._lock:
            return self._bootstrap_recovery_in_progress or (
                not self._bootstrap_recovery_requested
                and (
                    self.bootstrap_recovery_status() == "restarting"
                    or self._bootstrap_recovery_signalled
                    and self.bootstrap_recovery_status() == "restartable"
                )
            )

    @property
    def bootstrap_recovery_requested(self) -> bool:
        """Whether a quit may have crossed the serialized send boundary."""

        with self._lock:
            return self._bootstrap_recovery_requested

    def _wake_bootstrap_recovery(self) -> None:
        with self._lock:
            if (
                self._bootstrap_recovery_signalled
                or self._bootstrap_recovery_requested
                or self._bootstrap_recovery_in_progress
                or self.bootstrap_recovery_status() != "restartable"
            ):
                return
            self._bootstrap_recovery_signalled = True
        from meetings_mcp_lifecycle import schedule_initialize_companion_bootstrap

        schedule_initialize_companion_bootstrap(require_owner_response=True)

    def recover_failed_bootstrap(self, *, revalidate_request: Callable[[], None]) -> None:
        """Cooperatively retire a terminal bootstrap owner; never retry a sent quit.

        Native owns the durable retry budget. This local latch also preserves an
        ambiguous quit result, and the capture lock excludes an overlapping Start.
        The caller must validate its replacement launch context before the quit.
        """

        import control_client

        if not self._capture_recovery_lock.acquire(blocking=False):
            raise control_client.CooperativeHandoffDeclined(
                "native companion capture or recovery is already in progress"
            )
        try:
            with self._lock:
                if self._bootstrap_recovery_requested:
                    raise control_client.CooperativeHandoffDeclined(
                        "native companion bootstrap recovery was already requested"
                    )
                self._bootstrap_recovery_in_progress = True
            self.get_state(timeout_seconds=5.0)
            if self.bootstrap_recovery_status() != "restartable":
                raise control_client.CooperativeHandoffDeclined(
                    "native companion bootstrap recovery is not authorized"
                )

            def before_send() -> None:
                if self.bootstrap_recovery_status() != "restartable":
                    raise control_client.CooperativeHandoffDeclined(
                        "native companion bootstrap recovery is no longer authorized"
                    )
                revalidate_request()
                self._verify_owner()
                with self._lock:
                    # A partial write can be accepted even if on_sent never
                    # runs. Read-only or rejected preflight consumes no attempt.
                    self._bootstrap_recovery_requested = True

            response = self.quit_for_update(
                reason="bootstrap-recovery",
                timeout_seconds=control_client.HANDOFF_RESPONSE_TIMEOUT_SECONDS,
                before_send=before_send,
            )
            if response["disposition"] != "accepted" or not hmac.compare_digest(
                response["ownerEpoch"], self._owner.descriptor["ownerEpoch"]
            ):
                raise control_client.CooperativeHandoffDeclined(
                    "native companion bootstrap recovery was not accepted"
                )
            if not _wait_for_companion_exit(
                self._owner, control_client.HANDOFF_EXIT_TIMEOUT_SECONDS
            ):
                raise control_client.CooperativeHandoffRequired(
                    "native companion bootstrap recovery owner did not exit"
                )
            self.close()
            revalidate_request()
        finally:
            with self._lock:
                self._bootstrap_recovery_in_progress = False
                if not self._bootstrap_recovery_requested:
                    self._bootstrap_recovery_signalled = False
            self._capture_recovery_lock.release()

    def public_state(self) -> dict[str, object]:
        """Project companion-computed state without private account fingerprints.

        Returns:
            The app-safe recording state with its real public session identifiers.

        Raises:
            ControlUnavailable: If the authenticated owner's state is unavailable.
        """

        with self._lock:
            state = self._state
            if state is None:
                raise ControlUnavailable("native companion recording state is unavailable")
            recording = copy.deepcopy(dict(state["recording"]))
            # State and optional-field authority must belong to the same connection.
            if "recording.audio-sources.v1" not in self._negotiated_capabilities:
                recording.pop("audioSources", None)
            return {
                "revision": state["revision"],
                "recording": recording,
                "lifecycle": copy.deepcopy(state["lifecycle"]),
            }

    def public_status(self) -> dict[str, object]:
        """Build the app-safe v2 envelope without exposing private owner metadata.

        Returns:
            Validated public recording state and the authenticated companion PID.
        """

        if self.bootstrap_recovery_pending():
            from control_client import connecting_state

            status = connecting_state(runtime=self._owner.runtime)
            status["ok"] = False
            status["availability"] = {"status": "loading", "stage": "connecting"}
            return status
        with self._lock:
            public_state = self.public_state()
            status: dict[str, object] = {
                "ok": True,
                "protocolVersion": PROTOCOL_VERSION,
                "companionPid": self._owner.descriptor["pid"],
                "companionVersion": self._owner.descriptor["companionVersion"],
                "state": public_state,
            }
            native_scope = self._state["accountScopeFingerprint"] if self._state else None
            stopped_note = self._stopped_recording_note
            session = self._state["recording"]["session"] if self._state else None
            session_id = session["id"] if session is not None else None
            # Keep verified alpha/build identity with this owner-bound envelope;
            # companionVersion can be an older compatibility/display version.
            if self._verified_release_version is not None:
                status["_verifiedReleaseVersion"] = VerifiedCompanionRelease(
                    self._verified_release_version
                )
            revisions = {
                resource: revision
                for resource, revision in self._workspace_revisions.items()
                if revision > 0
            }
            completed = (
                self._completed_recording_session is not None
                and self._completed_recording_session == self._observed_recording_session
            )
        # Tag the already-cached status for the mounted Notes owner. No native
        # request or auth probe is needed, and stale snapshots remain untagged.
        try:
            import meetings_mcp
            from codex_auth_client import CodexAuthAccountUnverified
            from meetings_api_client_common import record_owner_scope_fingerprint
            from meetings_mcp_projection import workspace_owner_scope_generation

            app_instance = meetings_mcp.RECORDING_APP_INSTANCE.get()
            auth = (
                meetings_mcp.get_process_auth_manager().peek_cached_chatgpt_auth()
                if app_instance
                else None
            )
            if auth is not None:
                scope = record_owner_scope_fingerprint(auth)
                if scope is not None and scope == native_scope:
                    try:
                        owner = workspace_owner_scope_generation(
                            (auth.account_id, auth.subject), app_instance_id=app_instance
                        )
                    except CodexAuthAccountUnverified:
                        owner = None
                    if owner is not None:
                        status["recordingOwner"] = owner
                        if session_id is not None:
                            status["recordingCorrelationId"] = hashlib.sha256(
                                f"meetings-note-correlation-v1:{session_id}".encode()
                            ).hexdigest()
                        if stopped_note is not None and stopped_note[0] == native_scope:
                            status["stoppedRecordingNote"] = {
                                "sessionId": stopped_note[1],
                                "meetingId": stopped_note[2],
                            }
        except Exception:
            # Optional UI correlation cannot fail a status/Start/Stop response.
            pass
        if revisions:
            status["workspaceRevisions"] = revisions
        state = status["state"]
        if completed and isinstance(state, dict) and state["recording"]["phase"] == "idle":
            status["completion"] = {"outcome": "saved"}
        return status

    def call(
        self,
        method: str,
        params: Mapping[str, object],
        *,
        timeout_seconds: float = 12.0,
        cancellation_event: threading.Event | None = None,
        before_send: Callable[[], None] | None = None,
    ) -> dict[str, object]:
        """Run one generated, capability-authorized companion v2 method.

        Args:
            method: Exact generated companion method name.
            params: Closed method-specific generated request parameters.
            timeout_seconds: Full operation timeout, independent of admission TTL.
            cancellation_event: Optional cancellation for this request only.

        Returns:
            The method-specific, generated-schema-validated result.

        Raises:
            ControlUnavailable: If capability, owner, request, or result is invalid.
        """

        if method == "recording.start":
            return self._call_with_codex_context(
                method,
                params,
                timeout_seconds=timeout_seconds,
                cancellation_event=cancellation_event,
                before_send=before_send,
            )
        return self._call(
            method,
            params,
            timeout_seconds=timeout_seconds,
            cancellation_event=cancellation_event,
            before_send=before_send,
        )

    def _call_with_codex_context(
        self,
        method: str,
        params: Mapping[str, object],
        *,
        timeout_seconds: float,
        cancellation_event: threading.Event | None,
        before_send: Callable[[], None] | None = None,
    ) -> dict[str, object]:
        deadline = time.monotonic() + max(0.0, timeout_seconds)
        # Capture this caller's observation before waiting for another Start
        # or a background update. A different request must not replace it.
        version = get_current_codex_version()
        with self._lock:
            version = version or self._codex_app_version
        with self._codex_context_guard(deadline, cancellation_event):
            for _ in range(_CONTEXT_SYNC_ATTEMPTS):
                self._sync_codex_context(version, deadline, cancellation_event)
                with self._lock:
                    context_generation = self._context_generation
                context_changed = False
                admitted = False

                def require_context(generation: int = context_generation) -> None:
                    nonlocal context_changed, admitted

                    if before_send is not None:
                        before_send()
                    with self._lock:
                        if version and (
                            generation != self._context_generation
                            or not self._transport.connected
                            or (
                                "client.context.v1" in self._negotiated_capabilities
                                and version != self._synced_codex_app_version
                            )
                        ):
                            context_changed = not admitted
                            raise ControlUnavailable(
                                "native companion context changed before recording start"
                            )
                    admitted = True

                try:
                    return self._call(
                        method,
                        params,
                        timeout_seconds=max(0.0, deadline - time.monotonic()),
                        cancellation_event=cancellation_event,
                        before_send=require_context,
                    )
                except ControlUnavailable:
                    # Only this pre-write rejection permits resynchronization.
                    # A sent or ambiguous Start is never replayed.
                    if not context_changed:
                        raise
            raise ControlConnectionUnavailable(
                "native companion context changed before recording start"
            )

    def _call(
        self,
        method: str,
        params: Mapping[str, object],
        *,
        timeout_seconds: float = 12.0,
        cancellation_event: threading.Event | None = None,
        before_send: Callable[[], None] | None = None,
    ) -> dict[str, object]:

        deadline = time.monotonic() + max(0.0, timeout_seconds)
        if method not in _PRODUCT_METHODS:
            raise ControlUnavailable("native companion operation is unsupported")
        self.connect(
            timeout_seconds=max(0.0, deadline - time.monotonic()),
            cancellation_event=cancellation_event,
        )
        critical = method in {"recording.stop", "lifecycle.quitForUpdate"}
        acquired = False
        if not critical:
            while not acquired:
                if cancellation_event is not None and cancellation_event.is_set():
                    raise ControlUnavailable("native companion request was cancelled")
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise ControlConnectionUnavailable("native companion request timed out")
                acquired = self._ordinary_capacity.acquire(timeout=min(0.05, remaining))
        submission_acquired = False
        submission_released = False
        capture_guard_acquired = False
        request_failure: ControlUnavailable | None = None
        observed_capture: int | None = None
        request_id: str | None = None

        def release_submission() -> None:
            nonlocal submission_released

            if submission_acquired and not submission_released:
                submission_released = True
                self._submission_lock.release()

        try:
            if method == "recording.start":
                while not capture_guard_acquired:
                    if cancellation_event is not None and cancellation_event.is_set():
                        raise ControlUnavailable("native companion request was cancelled")
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        raise ControlConnectionUnavailable("native companion request timed out")
                    capture_guard_acquired = self._capture_recovery_lock.acquire(
                        timeout=min(0.05, remaining)
                    )
            while not submission_acquired:
                if cancellation_event is not None and cancellation_event.is_set():
                    raise ControlUnavailable("native companion request was cancelled")
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise ControlConnectionUnavailable("native companion request timed out")
                submission_acquired = self._submission_lock.acquire(timeout=min(0.05, remaining))
            with self._lock:
                if self._sequence >= _MAXIMUM_SAFE_INTEGER:
                    raise ControlUnavailable("native companion request sequence is exhausted")
                self._sequence += 1
                sequence = self._sequence
                capabilities = self._negotiated_capabilities
            request_id = f"request_{secrets.token_hex(16)}"
            message: dict[str, object] = {
                "jsonrpc": "2.0",
                "id": request_id,
                "method": method,
                "params": dict(params),
                "meta": {
                    "clientId": self._client_id,
                    "ownerEpoch": self._owner.descriptor["ownerEpoch"],
                    "sequence": sequence,
                    "issuedAtMillis": int(time.time() * 1000),
                },
            }
            if not is_request(message) or not request_is_authorized(message, capabilities):
                raise ControlUnavailable("native companion operation is unsupported")
            with self._lock:
                self._pending_requests[request_id] = message
                transport = self._transport
                transport_generation = self._transport_generation
                observed_capture = self._capture_observation

            preflight_failed = False

            def prepare_send() -> None:
                nonlocal preflight_failed

                try:
                    if before_send is not None:
                        before_send()
                except Exception:
                    preflight_failed = True
                    raise
                if method == "recording.start":
                    with self._lock:
                        # Preserve partial-write safety after admission, while a
                        # rejected preflight leaves existing capture evidence intact.
                        self._capture_recovery_safety = _CaptureRecoverySafety.START_AMBIGUOUS

            try:
                result = transport.request(
                    dict(message),
                    deadline=deadline,
                    cancellation_event=cancellation_event,
                    on_sent=release_submission,
                    before_send=prepare_send if method == "recording.start" else before_send,
                )
            except Exception as exc:
                if method == "recording.start" and not preflight_failed:
                    with self._lock:
                        # An unclassified failure cannot prove no Start bytes.
                        self._capture_recovery_safety = _CaptureRecoverySafety.START_AMBIGUOUS
                if isinstance(exc, LiveTransportError):
                    request_failure = control_transport_error(
                        exc, "native companion operation was unavailable"
                    )
                    raise request_failure from exc
                raise
            completed_session: str | None = None
            if method in {
                "companion.getState",
                "recording.start",
                "permissions.recheck",
                "permissions.request",
                "permissions.openSystemSettings",
            }:
                self._publish_state(
                    result,
                    allow_equal=True,
                    start_completed=method == "recording.start",
                    transport_generation=transport_generation,
                )
            elif method == "recording.stop":
                stop_result = result
                if not is_stop_recording_result(stop_result):
                    raise ControlUnavailable("native companion Stop result is malformed")
                completion = stop_result.get("completion")
                expected_session: str | None = None
                if completion is not None:
                    raw_expected_session = params.get("expectedSessionId")
                    if not isinstance(raw_expected_session, str):
                        raise ControlUnavailable(
                            "native recording completion session does not match"
                        )
                    if not hmac.compare_digest(completion["sessionId"], raw_expected_session):
                        raise ControlUnavailable(
                            "native recording completion session does not match"
                        )
                    expected_session = raw_expected_session
                self._publish_state(
                    stop_result["state"],
                    allow_equal=True,
                    transport_generation=transport_generation,
                )
                if completion is not None and completion["outcome"] == "saved":
                    completed_session = expected_session
            with self._lock:
                # Publication drops retired callbacks. RPCs must also fail and
                # keep Stop completion out of a replacement connection.
                if transport_generation != self._transport_generation:
                    raise ControlUnavailable(
                        "native companion response belongs to a retired connection"
                    )
                if completed_session is not None:
                    self._completed_recording_session = completed_session
                return result
        finally:
            if request_id is not None:
                with self._lock:
                    self._pending_requests.pop(request_id, None)
            release_submission()
            if capture_guard_acquired:
                self._capture_recovery_lock.release()
            if acquired:
                self._ordinary_capacity.release()
            if request_failure is not None and (
                cancellation_event is None or not cancellation_event.is_set()
            ):
                self._schedule_listener_recovery(request_failure, observed_capture=observed_capture)

    def get_state(
        self,
        *,
        timeout_seconds: float = 12.0,
        cancellation_event: threading.Event | None = None,
        for_start: bool = False,
    ) -> CompanionState:
        """Read fresh native state, synchronizing caller context for Start preflight."""

        call = self._call_with_codex_context if for_start else self.call
        result = call(
            "companion.getState",
            {},
            timeout_seconds=timeout_seconds,
            cancellation_event=cancellation_event,
        )
        if not is_companion_state(result):
            raise ControlUnavailable("native companion recording state is malformed")
        return result

    def recheck_audio(
        self,
        *,
        cancellation_event: threading.Event | None = None,
        revalidate_request: Callable[[], None],
    ) -> None:
        """Recheck only this owner's explicitly offered audio recovery action.

        This refreshes hardware and permission state without prompting, opening
        settings or starting capture. Native still owns audio availability.
        """

        def before_send() -> None:
            if cancellation_event is not None and cancellation_event.is_set():
                raise ControlUnavailable("native companion request was cancelled")
            revalidate_request()
            self.require_explicit_recovery_allowed()
            state = self.latest_state()
            if state is None or "recording.audio-sources.v1" not in self.negotiated_capabilities:
                raise ControlUnavailable("native audio recheck is unavailable")
            recording = state["recording"]
            notice = recording["notice"]
            if (
                recording.get("audioSources") is None
                or recording["phase"] not in {"idle", "unavailable"}
                or recording["session"] is not None
                or recording["controls"]["start"]["enabled"]
                or recording["controls"]["stop"]["enabled"]
                or not state["lifecycle"]["replacement"]["allowed"]
                or notice is None
                or notice["kind"] != "recording-unavailable"
                or notice["action"] is None
                or notice["action"]["kind"] != "recheck-audio"
            ):
                raise ControlUnavailable("native audio recheck is not authorized")

        with self.explicit_recovery_guard():
            revalidate_request()
            self.get_state(cancellation_event=cancellation_event)
            before_send()
            self.call(
                "permissions.recheck",
                {},
                cancellation_event=cancellation_event,
                before_send=before_send,
            )

    def quit_for_update(
        self,
        *,
        timeout_seconds: float = 12.0,
        cancellation_event: threading.Event | None = None,
        reason: Literal["bootstrap-recovery"] | None = None,
        before_send: Callable[[], None] | None = None,
    ) -> QuitForUpdateResult:
        """Request the authenticated owner's typed cooperative handoff decision."""

        params: dict[str, object] = {"expectedOwnerEpoch": self._owner.descriptor["ownerEpoch"]}
        if reason is not None:
            params["reason"] = reason
        result = self.call(
            "lifecycle.quitForUpdate",
            params,
            timeout_seconds=timeout_seconds,
            cancellation_event=cancellation_event,
            before_send=before_send,
        )
        if not is_quit_for_update_result(result):
            raise ControlUnavailable("native companion update handoff result is malformed")
        return result

    def settings(
        self,
        account_fingerprint: str,
        *,
        changes: Mapping[str, bool] | None = None,
        cancellation_event: threading.Event | None = None,
    ) -> SettingsState:
        """Read or update exactly the current account's companion settings.

        Args:
            account_fingerprint: Private authenticated account scope.
            changes: Optional nonempty native preference changes.
            cancellation_event: Optional request cancellation.

        Returns:
            Generated, account-bound companion settings.

        Raises:
            ControlUnavailable: If account, capability, or response does not match.
        """

        params: dict[str, object] = {"accountScopeFingerprint": account_fingerprint}
        method = "settings.get"
        if changes is not None:
            method = "settings.update"
            params["changes"] = dict(changes)
        result = self.call(method, params, cancellation_event=cancellation_event)
        if not is_settings_state(result) or not hmac.compare_digest(
            result["accountScopeFingerprint"], account_fingerprint
        ):
            raise ControlUnavailable("native companion settings account does not match")
        return result

    def home_snapshot(
        self,
        account_fingerprint: str,
        *,
        notes_source: Literal["meetings", "private-notes"] | None = None,
        cancellation_event: threading.Event | None = None,
    ) -> HomeSnapshot:
        """Read the authenticated companion-owned Home snapshot for one account.

        Args:
            account_fingerprint: Private authenticated account scope.
            notes_source: Optional source-specific Notes cache requested by the caller.
            cancellation_event: Optional request cancellation.

        Returns:
            The generated, bounded account-scoped Calendar and Notes snapshot.

        Raises:
            ControlUnavailable: If account, capability, or snapshot is invalid.
        """

        params: dict[str, object] = {"accountScopeFingerprint": account_fingerprint}
        if notes_source is not None:
            if "home.notes-source.v1" not in self.negotiated_capabilities:
                raise ControlUnavailable("native companion Notes cache source is unsupported")
            params["notesSource"] = notes_source
        if (
            notes_source == "private-notes"
            and "home.note-page-binding.v1" in self.negotiated_capabilities
        ):
            params["includePageBindings"] = True
        result = self.call(
            "home.getSnapshot",
            params,
            cancellation_event=cancellation_event,
        )
        if not is_home_snapshot(result) or not hmac.compare_digest(
            result["accountScopeFingerprint"], account_fingerprint
        ):
            raise ControlUnavailable("native companion Home account does not match")
        notes = result["notes"]
        if notes_source is not None and notes is not None and notes.get("source") != notes_source:
            raise ControlUnavailable("native companion Notes cache source does not match")
        return result

    def verify_session(self, session_id: str) -> str:
        """Verify the public session identifier against the exact active owner.

        Args:
            session_id: Public recording session identifier supplied by the UI.

        Returns:
            The same exact, authenticated companion recording session identifier.

        Raises:
            ControlUnavailable: If the session is stale or does not match this owner.
        """

        with self._lock:
            session = self._state["recording"]["session"] if self._state is not None else None
            if session is None or session["id"] != session_id:
                raise ControlUnavailable("native recording session does not match")
            return session_id

    def close(self) -> None:
        """Close this connection and revoke its owner/session capabilities."""

        with _DIAGNOSTICS_LOCK:
            # Retirement and a diagnostic claim must have one ordering.
            self._connection_cancelled.set()
        self._transport.close()
        self._invalidate()

    def _validate_initialize_result(self, value: dict[str, object]) -> None:
        initialized = parse_initialize_result(value)
        if initialized is None:
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED,
                "native companion initialization result is malformed",
            )
        if initialized["ownerEpoch"] != self._owner.descriptor["ownerEpoch"]:
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED,
                "native companion owner changed during initialization",
            )
        if "recording.control.v2" not in initialized["capabilities"]:
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED,
                "native companion recording capability was not negotiated",
            )
        value.clear()
        value.update(initialized)

    def _publish_initialize_result(self, value: dict[str, object]) -> None:
        if not is_initialize_result(value):
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED,
                "native companion initialization result is malformed",
            )
        initialized = value
        capabilities = initialized["capabilities"]
        state = initialized["state"]
        with self._lock:
            if self._connection_cancelled.is_set():
                raise LiveTransportError(
                    LiveTransportFailureKind.CANCELLED,
                    "native companion connection was cancelled",
                )
            self._observe_capture_response(state)
            if not self._accept_state_revision(state, allow_equal=True):
                raise LiveTransportError(
                    LiveTransportFailureKind.REJECTED,
                    "native companion initialization state revision regressed",
                )
            self._negotiated_capabilities = frozenset(capabilities).intersection(
                _PRODUCT_CAPABILITIES
            )
            self._context_generation += 1
            self._synced_codex_app_version = ""
            self._context_retry_after = 0.0
            self._state = copy.deepcopy(state)
            self._observe_capture_recovery_safety(state)
            self._revision = state["revision"]
            session = state["recording"]["session"]
            self._observed_recording_session = session["id"] if session is not None else None
            self._completed_recording_session = None
            self._stopped_recording_note = None
        self._wake_bootstrap_recovery()
        with _DIAGNOSTICS_LOCK:
            if _DIAGNOSTICS.client is not self:
                return
            _DIAGNOSTICS.stage = "ready"
            _DIAGNOSTICS.companion_pid = self._owner.descriptor["pid"]
            _DIAGNOSTICS.companion_version = initialized["companionVersion"]
            _DIAGNOSTICS.transport = self._owner.descriptor["transport"]
            _DIAGNOSTICS.connected = True
            _DIAGNOSTICS.initialized = True
            owner_epoch = initialized["ownerEpoch"]
            _DIAGNOSTICS.native_owner_epoch = (
                owner_epoch
                if self._owner.descriptor["platform"] == "windows"
                and owner_epoch == self._owner.descriptor["ownerEpoch"]
                and re.fullmatch(r"epoch_[0-9a-f]{32}", owner_epoch) is not None
                else None
            )
            _DIAGNOSTICS.state_cached = True
            _DIAGNOSTICS.state_revision = state["revision"]
            _DIAGNOSTICS.recording_phase = state["recording"]["phase"]
            _DIAGNOSTICS.recording_summary = state.get("recordingSummary")
            _DIAGNOSTICS.last_failure_stage = None
            _DIAGNOSTICS.last_failure_reason = None
            _DIAGNOSTICS.last_error_type = None
            _DIAGNOSTICS.status_reason = None
            _DIAGNOSTICS.last_logged_status_failure = None
            _DIAGNOSTICS.reported_status_failures.clear()
        log_native_runtime_event(
            "control-initialize",
            "completed",
            pid=os.getpid(),
        )

    def _validate_response(self, response: dict[str, object]) -> None:
        request_id = response.get("id")
        with self._lock:
            request = (
                self._pending_requests.get(request_id) if isinstance(request_id, str) else None
            )
            capabilities = self._negotiated_capabilities
        parsed = parse_response(response, request, capabilities)
        if parsed is None:
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED,
                "native companion response does not match its request",
            )
        # Normalize before the transport stores either the reply or its replay cache.
        response.clear()
        response.update(parsed)

    def _accept_notification(
        self, value: dict[str, object], *, connection_generation: int | None = None
    ) -> None:
        with self._lock:
            if not self._connection_is_current(connection_generation):
                return
            capabilities = self._negotiated_capabilities
            current_scope = (
                self._state["accountScopeFingerprint"] if self._state is not None else None
            )
        notification = parse_notification(value, capabilities)
        if notification is None:
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED, "native companion notification is unauthorized"
            )
        if notification["method"] == "companion.stateChanged":
            params = notification["params"]
            self._publish_state(
                params, allow_equal=False, connection_generation=connection_generation
            )
        elif notification["method"] == "recording.completed":
            session_id = notification["params"]["sessionId"]
            with self._lock:
                if not self._connection_is_current(connection_generation):
                    return
                if self._observed_recording_session is None or not hmac.compare_digest(
                    session_id, self._observed_recording_session
                ):
                    raise LiveTransportError(
                        LiveTransportFailureKind.REJECTED,
                        "native recording completion session does not match",
                    )
                self._completed_recording_session = session_id
            if self._on_recording_completed is not None:
                self._on_recording_completed(session_id)
        elif notification["method"] == "workspace.changed":
            params = notification["params"]
            scope = params["accountScopeFingerprint"]
            resource = params["resource"]
            if not isinstance(current_scope, str) or not hmac.compare_digest(scope, current_scope):
                raise LiveTransportError(
                    LiveTransportFailureKind.REJECTED,
                    "native companion workspace account does not match",
                )
            with self._lock:
                if not self._connection_is_current(connection_generation):
                    return
                self._workspace_revisions[resource] += 1
            if self._on_workspace_changed is not None:
                self._on_workspace_changed(resource, scope)

    def _accept_state_revision(self, state: CompanionState, *, allow_equal: bool) -> bool:
        """Keep exact-owner revision and retained capture monotonic across reconnects."""

        revision = state["revision"]
        if revision > self._revision:
            return True
        if not allow_equal:
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED, "native companion state revision regressed"
            )
        if revision < self._revision:
            return False
        return not (
            self._capture_recovery_safety is _CaptureRecoverySafety.PROTECTED
            and state["recording"]["phase"] == "idle"
            and state["lifecycle"]["replacement"]["allowed"]
        )

    def _publish_state(
        self,
        value: object,
        *,
        allow_equal: bool,
        start_completed: bool = False,
        connection_generation: int | None = None,
        transport_generation: int | None = None,
    ) -> None:
        if not is_companion_state(value):
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED, "native companion recording state is malformed"
            )
        with self._lock:
            # RPC replies still prove owner activity after an ordinary disconnect,
            # but transport replacement retires them. Notifications bind to a connection.
            if not self._connection_is_current(
                connection_generation, transport_generation=transport_generation
            ):
                return
            self._observe_capture_response(value)
            if not self._accept_state_revision(value, allow_equal=allow_equal):
                return
            revision = value["revision"]
            # Preserve an exact join observed between UI polls. This is bounded,
            # optional presentation data, never capture or completion authority.
            previous = self._state
            if (
                previous is None
                or previous["accountScopeFingerprint"] != value["accountScopeFingerprint"]
                or value["recording"]["phase"] != "idle"
            ):
                self._stopped_recording_note = None
            elif previous["recording"]["phase"] in {"recording", "stopping"}:
                prior_session = previous["recording"]["session"]
                prior_scope = previous["accountScopeFingerprint"]
                meeting_id = prior_session.get("meetingId") if prior_session is not None else None
                self._stopped_recording_note = (
                    (prior_scope, prior_session["id"], meeting_id)
                    if prior_scope is not None and prior_session is not None and meeting_id
                    else None
                )
            self._state = copy.deepcopy(value)
            self._observe_capture_recovery_safety(value, start_completed=start_completed)
            self._revision = revision
            session = value["recording"]["session"]
            if session is not None and session["id"] != self._observed_recording_session:
                self._observed_recording_session = session["id"]
                self._completed_recording_session = None
            elif value["recording"]["phase"] == "starting":
                self._observed_recording_session = None
                self._completed_recording_session = None
        phase_changed = False
        with self._lock, _DIAGNOSTICS_LOCK:
            if _DIAGNOSTICS.client is self and self._connection_is_current(
                connection_generation, transport_generation=transport_generation
            ):
                phase_changed = _DIAGNOSTICS.recording_phase != value["recording"]["phase"]
                _DIAGNOSTICS.state_cached = True
                _DIAGNOSTICS.state_revision = revision
                _DIAGNOSTICS.recording_phase = value["recording"]["phase"]
                _DIAGNOSTICS.recording_summary = value.get("recordingSummary")
        if phase_changed:
            log_native_runtime_event(
                "control-state",
                "updated",
                reason=value["recording"]["phase"],
                pid=os.getpid(),
            )
        if value["recording"]["phase"] == "idle":
            from meetings_mcp_lifecycle import wake_initialize_companion_deferred_update

            wake_initialize_companion_deferred_update(
                self.public_status(), runtime=self._owner.runtime
            )
        self._wake_bootstrap_recovery()

    def _connection_is_current(
        self, generation: int | None, *, transport_generation: int | None = None
    ) -> bool:
        return (generation is None or generation == self._connection_generation) and (
            transport_generation is None or transport_generation == self._transport_generation
        )

    def _invalidate(self, *, connection_generation: int | None = None) -> None:
        with self._lock:
            if not self._connection_is_current(connection_generation):
                return
            # Retire callbacks even when no replacement connection is opened.
            self._connection_generation += 1
            self._state = None
            # A disconnect revokes live presentation, not this owner's last
            # revision or capture evidence. Late reads must remain stale.
            self._negotiated_capabilities = frozenset()
            self._context_generation += 1
            self._synced_codex_app_version = ""
            self._workspace_revisions = {"calendar": 0, "notes": 0}
            self._observed_recording_session = None
            self._completed_recording_session = None
            self._stopped_recording_note = None
            with _DIAGNOSTICS_LOCK:
                was_connected = _DIAGNOSTICS.connected or _DIAGNOSTICS.initialized
                if _DIAGNOSTICS.client is not self:
                    return
                if _DIAGNOSTICS.stage != "failed":
                    _DIAGNOSTICS.stage = "disconnected"
                _DIAGNOSTICS.connected = False
                _DIAGNOSTICS.initialized = False
                _DIAGNOSTICS.native_owner_epoch = None
                _DIAGNOSTICS.client = None
                _DIAGNOSTICS.state_cached = False
                _DIAGNOSTICS.state_revision = None
                _DIAGNOSTICS.recording_phase = None
                _DIAGNOSTICS.recording_summary = None
        if was_connected:
            log_native_runtime_event(
                "control-connection",
                "disconnected",
                pid=os.getpid(),
            )

    def _verify_owner(self) -> None:
        import control_client

        if self._connection_cancelled.is_set():
            raise LiveTransportError(
                LiveTransportFailureKind.CANCELLED,
                "native companion connection was cancelled",
            )
        owner = self._owner
        descriptor = owner.descriptor
        current = control_client.read_json(owner.root / _DESCRIPTOR_FILENAME)
        if current != descriptor or control_client.owner_lock_state(owner.root) != "held":
            raise LiveTransportError(
                LiveTransportFailureKind.REJECTED, "native companion owner identity changed"
            )
        # The transport checks peer PID and user/session; initialize checks the
        # owner epoch. On-disk image checks belong to launch and termination.


def bootstrap_recovery_client() -> CompanionClient | None:
    """Read the latest authenticated terminal-bootstrap owner without new I/O."""

    with _DIAGNOSTICS_LOCK:
        client = _DIAGNOSTICS.client
    return client if client is not None and client.bootstrap_recovery_status() is not None else None


def cached_meetings_policy_client() -> CompanionClient | None:
    """Return the current authenticated policy owner without discovering or connecting."""

    with _DIAGNOSTICS_LOCK:
        client = _DIAGNOSTICS.client
    if client is None or "meetings.eligibility.v1" not in client.negotiated_capabilities:
        return None
    return client


def companion_client(
    *,
    runtime: Mapping[str, object] | None = None,
    connect: bool = True,
    allow_existing_owner: bool = False,
    timeout_seconds: float = 5.0,
    cancellation_event: threading.Event | None = None,
) -> CompanionClient:
    """Return the process-local client for the current authenticated v2 owner.

    Args:
        runtime: Optional already reviewed native runtime identity.
        connect: Whether to initialize the owner before returning the client.
        allow_existing_owner: Use the running owner even if its installation changed.
        timeout_seconds: Maximum owner initialization duration.
        cancellation_event: Optional request cancellation signal.

    Returns:
        The exact-owner shared companion v2 client.

    Raises:
        ControlUnavailable: If discovery, owner identity, or initialization fails.
    """

    owner = discover_companion_owner(runtime=runtime, allow_existing_owner=allow_existing_owner)
    key = (str(owner.root), owner.descriptor["ownerEpoch"], owner.descriptor["pid"])
    with _CLIENTS_LOCK:
        client = _CLIENTS.get(key)
        if client is None:
            for stale_key, stale in tuple(_CLIENTS.items()):
                if stale_key[0] == key[0] and stale_key != key:
                    _CLIENTS.pop(stale_key)
                    stale.close()
            client = CompanionClient(owner)
            _CLIENTS[key] = client
    if client.owner.descriptor != owner.descriptor:
        raise ControlUnavailable("native companion owner identity changed")
    client.observe_codex_version(get_current_codex_version())
    if connect:
        client.connect(timeout_seconds=timeout_seconds, cancellation_event=cancellation_event)
    return client


def close_companion_clients() -> None:
    """Close all owner-bound v2 clients and revoke their session capabilities."""

    global _pending_listener_recovery

    with _CLIENTS_LOCK:
        _pending_listener_recovery = None
        _listener_recovery_pending.clear()
        clients = tuple(_CLIENTS.values())
        _CLIENTS.clear()
    for client in clients:
        client.close()


def pending_listener_recovery_client() -> CompanionClient | None:
    """Consume one exact-owner failure wake; ordinary status reads never write files."""
    global _pending_listener_recovery

    with _CLIENTS_LOCK:
        client = _pending_listener_recovery
        _pending_listener_recovery = None
        _listener_recovery_pending.clear()
    return client if client is not None and not client.closed else None


def has_pending_listener_recovery() -> bool:
    """Nonblocking wake hint; exact-owner admission happens when consuming it."""
    return _listener_recovery_pending.is_set()


def _verify_listener_recovery_owner(
    client: CompanionClient,
    *,
    birth_identity: tuple[int, int] | None = None,
) -> tuple[CompanionOwner, tuple[int, int] | None]:
    import control_client

    owner = client.owner
    if client.closed:
        raise ControlUnavailable("native listener recovery was cancelled")
    _verify_runtime_identity(owner.descriptor, owner.runtime)
    identity = owner.descriptor["executableIdentity"]
    if owner.descriptor["platform"] == "macos":
        from meetings_app.owner_recovery import verified_darwin_owner_process_image

        device, inode = identity.get("device"), identity.get("inode")
        if type(device) is not int or type(inode) is not int:
            raise ControlUnavailable("native listener owner image is unavailable")
        birth_identity = verified_darwin_owner_process_image(
            owner.descriptor["pid"],
            expected_path=Path(identity["path"]),
            expected_identity=(device, inode),
            expected_digest=identity["sha256"],
            expected_start_identity=birth_identity,
        )
    else:
        from control_windows_identity import require_windows_owner_process_image

        app_path = owner.runtime.get("appPath")
        if not isinstance(app_path, str):
            raise ControlUnavailable("native listener owner image is unavailable")
        birth_identity = require_windows_owner_process_image(
            owner.descriptor["pid"],
            expected_path=Path(identity["path"]),
            app_path=Path(app_path),
            expected_digest=identity["sha256"],
            digest_reader=control_client.sha256_regular_file,
            expected_start_identity=birth_identity,
        )
    control_client.require_private(owner.root, directory=True)
    current = control_client.read_json(owner.root / _DESCRIPTOR_FILENAME)
    if not is_descriptor(current):
        raise ControlUnavailable("native listener descriptor is unavailable")
    _verify_runtime_platform(current, owner.runtime)
    if current != owner.descriptor or control_client.owner_lock_state(owner.root) != "held":
        raise ControlUnavailable("native listener owner changed")
    if client.closed:
        raise ControlUnavailable("native listener recovery was cancelled")
    return CompanionOwner(owner.root, current, owner.runtime), birth_identity


def recover_companion_listener(
    client: CompanionClient, *, cancellation_event: threading.Event | None = None
) -> bool:
    """Repair this failed listener while preserving the shared owner client."""
    return client.recover_listener(cancellation_event=cancellation_event)


def retained_windows_legacy_control_runtime(
    selected: Mapping[str, object], *, client: CompanionClient | None = None
) -> Mapping[str, object] | None:
    """Keep a verified, responsive legacy owner usable until its natural exit.

    This selects live control only, never a launch or replacement target. The
    returned release is the running image's verified release, so a staged newer
    image cannot satisfy an app-version policy on its behalf.
    """

    import native_runtime
    import native_runtime_windows_recovery
    from native_runtime_artifacts import verified_handoff_app_release_identity
    from native_runtime_stable import legacy_stable_runtime_root

    platform = selected.get("platform")
    selected_path = selected.get("appPath")
    if (
        not native_runtime_windows_recovery.enabled()
        or not isinstance(platform, str)
        or platform not in {"windows-x64", "windows-arm64"}
        or not isinstance(selected_path, str)
        or selected.get("installed") is not True
        or selected.get("source") != "plugin-bundled"
    ):
        return None
    try:
        spec = native_runtime.runtime_spec_for(platform)
        if client is None:
            client = companion_client(runtime=selected, connect=False, allow_existing_owner=True)
        descriptor = client.owner.descriptor
        if descriptor["platform"] != "windows" or descriptor[
            "architecture"
        ] != platform.removeprefix("windows-"):
            return None
        actual = Path(descriptor["executableIdentity"]["path"])
        expected = Path(selected_path)
        private_root = native_runtime.stable_runtime_root(create=False)
        if native_runtime.stable_runtime_artifact_root(expected) != private_root:
            return None
        # Direct-cache owners predate immutable generations. Their ordinary
        # official-cache verifier below must succeed; they cannot borrow pins.
        if not native_runtime.uses_production_windows_bundle(actual):
            legacy_root = legacy_stable_runtime_root(create=False)
            if (
                private_root == legacy_root
                or native_runtime.stable_runtime_artifact_root(actual) != legacy_root
            ):
                return None
        if client.bootstrap_recovery_status() is not None:
            return None
        # Live control needs a verified candidate, not an activation that could
        # change another owner's selected image during first-use migration.
        native_runtime.stable_runtime_verification_manifest(expected, spec, require_active=False)
        verified_handoff_app_release_identity(expected, spec)
        release = verified_handoff_app_release_identity(actual, spec)
        digest = native_runtime.sha256_regular_file(actual)
        if not hmac.compare_digest(digest, descriptor["executableIdentity"]["sha256"]):
            return None
        # The full verifier checks architecture, release provenance and
        # private ACLs. Revalidate the exact owner after that filesystem work.
        state = client.get_state(timeout_seconds=1.0)
        if (
            state["recording"]["phase"] not in {"idle", "starting", "recording", "stopping"}
            or client.bootstrap_recovery_status() is not None
        ):
            return None
        client.remember_verified_release_version(release)
        return {
            "installed": True,
            "source": "plugin-bundled",
            "version": "plugin-bundled",
            "platform": platform,
            "artifactKind": "windows-executable",
            "appPath": str(actual),
            "_executableSHA256": digest,
            "releaseVersion": release,
        }
    except (
        ControlUnavailable,
        LiveTransportError,
        native_runtime.NativeRuntimeError,
        OSError,
        ValueError,
    ):
        return None


def _reviewed_companion_handoff_client(
    expected_app_path: Path,
    plugin_family_root: Path,
    spec: PlatformRuntimeSpec,
    *,
    expected_executable_sha256: str,
    source_plugin_root: Path | None = None,
) -> CompanionClient | None:
    """Capture one reviewed v2 owner without connecting or granting replacement."""

    import control_client
    import control_client_live_handoff
    from native_runtime_artifacts import verified_handoff_app_release_identity

    def revalidate_request() -> None:
        control_client.require_canonical_handoff_request(
            expected_app_path,
            plugin_family_root,
            spec=spec,
            source_plugin_root=source_plugin_root,
        )

    revalidate_request()
    root = control_client.control_root()
    descriptor_value = control_client.read_json(root / _DESCRIPTOR_FILENAME)
    if not is_descriptor(descriptor_value):
        raise ControlUnavailable("native companion v2 handoff descriptor is malformed")
    descriptor = descriptor_value
    if control_client.pid_is_proven_dead(descriptor["pid"]):
        if control_client.owner_lock_state(root) == "held":
            raise ControlUnavailable("native companion v2 owner cannot be authenticated")
        return None

    family, expected = control_client.resolved_handoff_paths(
        expected_app_path,
        plugin_family_root,
        spec,
    )
    try:
        executable = Path(descriptor["executableIdentity"]["path"]).resolve(strict=True)
        actual = executable if descriptor["platform"] == "windows" else executable.parents[2]
    except (IndexError, OSError, ValueError) as error:
        raise ControlUnavailable(
            "native companion v2 executable identity is unavailable"
        ) from error
    control_client_live_handoff.require_reviewed_live_stream_owner_paths(
        expected,
        actual,
        family,
        spec,
    )
    try:
        selected_release = RuntimeManager.native_release_version_key(
            verified_handoff_app_release_identity(expected, spec)
        )
        owner_release = RuntimeManager.native_release_version_key(
            verified_handoff_app_release_identity(actual, spec)
        )
        metadata = executable.stat()
        digest = control_client.sha256_regular_file(executable)
    except (control_client.NativeRuntimeError, OSError) as error:
        raise ControlUnavailable(
            "native companion v2 executable identity is unavailable"
        ) from error
    identity = descriptor["executableIdentity"]
    if not hmac.compare_digest(identity["sha256"], digest):
        raise ControlUnavailable("native companion v2 executable digest does not match")
    if owner_release > selected_release or (
        owner_release == selected_release
        and not hmac.compare_digest(digest, expected_executable_sha256)
    ):
        raise ControlUnavailable("native companion recovery release is incompatible")
    reviewed_runtime: dict[str, object] = {
        "installed": True,
        "source": "plugin-bundled",
        "platform": spec.platform_key,
        "artifactKind": spec.artifact_kind,
        "appPath": str(actual),
        "_executableSHA256": digest,
    }
    if descriptor["platform"] == "macos":
        reviewed_runtime.update(
            {
                "_executableDevice": metadata.st_dev,
                "_executableInode": metadata.st_ino,
            }
        )
    client = companion_client(runtime=reviewed_runtime, connect=False)
    if client.owner.descriptor != descriptor:
        raise ControlUnavailable("native companion v2 owner changed during review")
    revalidate_request()
    if actual == expected.resolve(strict=False):
        if not hmac.compare_digest(expected_executable_sha256, digest):
            raise ControlUnavailable("native companion v2 selected image digest does not match")
    return client


def reviewed_predecessor_companion_client(*, runtime: Mapping[str, object]) -> CompanionClient:
    """Capture a canonical current or older v2 owner for explicit bounded recovery.

    An independently reviewed predecessor can differ from the selected image,
    but never from its captured descriptor, verified platform or release family.
    This function performs no native request, termination or launch.
    """

    import control_client
    from control_client_retention import runtime_handoff_source

    platform = runtime.get("platform")
    app_path = runtime.get("appPath")
    digest = runtime.get("_executableSHA256")
    if (
        runtime.get("installed") is not True
        or runtime.get("source") != "plugin-bundled"
        or not isinstance(platform, str)
        or not isinstance(app_path, str)
        or not isinstance(digest, str)
    ):
        raise ControlUnavailable("native selected runtime is unavailable")
    try:
        spec = control_client.runtime_spec_for(platform)
        expected = Path(app_path).resolve(strict=True)
        source, family = runtime_handoff_source(runtime, expected, spec)
        client = _reviewed_companion_handoff_client(
            expected,
            family,
            spec,
            expected_executable_sha256=digest,
            source_plugin_root=source,
        )
        if client is None:
            raise ControlUnavailable("native companion owner is unavailable")
        return client
    except (control_client.NativeRuntimeError, OSError, ValueError) as error:
        raise ControlUnavailable("native predecessor identity is unavailable") from error


def resolve_companion_handoff(
    expected_app_path: Path,
    plugin_family_root: Path,
    spec: PlatformRuntimeSpec,
    *,
    expected_executable_sha256: str | None = None,
    source_plugin_root: Path | None = None,
) -> str:
    """Launch a verified replacement after the live owner safely yields."""

    import control_client

    def revalidate_request() -> None:
        control_client.require_canonical_handoff_request(
            expected_app_path,
            plugin_family_root,
            spec=spec,
            source_plugin_root=source_plugin_root,
        )

    revalidate_request()
    control_client.validate_handoff_app(expected_app_path, spec)
    expected_executable = control_client.expected_executable_path(expected_app_path, spec)
    selected_digest = control_client.sha256_regular_file(expected_executable)
    if expected_executable_sha256 is not None and not hmac.compare_digest(
        selected_digest, expected_executable_sha256
    ):
        raise ControlUnavailable("native companion v2 selected image digest does not match")

    root = control_client.control_root()
    descriptor = control_client.read_json(root / _DESCRIPTOR_FILENAME)
    if not is_descriptor(descriptor):
        raise ControlUnavailable("native companion v2 handoff descriptor is malformed")
    owner_dead = control_client.pid_is_proven_dead(descriptor["pid"])
    lease_state = control_client.owner_lock_state(root)
    if lease_state == "available" or (owner_dead and lease_state == "missing"):
        # A released kernel lease outlives its process registration. Its PID
        # may already belong to another process; never connect to or signal it.
        # Missing leases still require a proven-dead PID. The new native owner
        # must acquire its own lease before publishing control or recording.
        if (
            control_client.read_json(root / _DESCRIPTOR_FILENAME) != descriptor
            or control_client.owner_lock_state(root) != lease_state
        ):
            raise ControlUnavailable("native companion v2 owner changed during handoff")
        revalidate_request()
        return "absent"
    if owner_dead:
        raise ControlUnavailable("native companion v2 owner cannot be authenticated")
    client = companion_client(allow_existing_owner=True, connect=False)
    if client.owner.descriptor != descriptor:
        raise ControlUnavailable("native companion v2 owner changed during handoff")
    identity = descriptor["executableIdentity"]
    if Path(identity["path"]) == expected_executable and hmac.compare_digest(
        identity["sha256"], selected_digest
    ):
        client.connect()
        revalidate_request()
        return "current"
    # Reuse the shared client's retained capture evidence before reconnecting;
    # a fresh idle response cannot resolve an ambiguous Start.
    with client.explicit_recovery_guard():
        client.get_state()
        from control_client_live_handoff import require_same_windows_runtime_for_handoff

        require_same_windows_runtime_for_handoff(expected_app_path, Path(identity["path"]), spec)
        quit_companion_owner(client, revalidate_request=revalidate_request)
    return "handed-off"


def _transport_probe_failed(error: BaseException, *, allow_endpoint_absence: bool = False) -> bool:
    """Local admission waits cannot prove the native owner is unresponsive."""

    cause: BaseException | None = error
    for _ in range(8):
        if cause is None:
            return False
        if isinstance(cause, LiveTransportError):
            return cause.kind in {
                LiveTransportFailureKind.UNAVAILABLE,
                LiveTransportFailureKind.TIMED_OUT,
            } and (
                cause.io_attempted is True
                or (
                    allow_endpoint_absence
                    and cause.kind is LiveTransportFailureKind.UNAVAILABLE
                    and cause.diagnostic_reason is LiveTransportFailureReason.ENDPOINT_MISSING
                )
            )
        cause = cause.__cause__
    return False


def _listener_recovery_failed(error: BaseException) -> bool:
    """Missing or rejected endpoints can use the separately verified health channel."""
    return isinstance(error, ControlEndpointRejected) or _transport_probe_failed(
        error, allow_endpoint_absence=True
    )


def wait_for_companion_recording_ready(
    client: CompanionClient,
    state: CompanionState,
    *,
    timeout_seconds: float,
    cancellation_event: threading.Event | None = None,
    for_start: bool = False,
) -> CompanionState | None:
    """Wait for native storage initialization after its control endpoint appears."""

    deadline = time.monotonic() + timeout_seconds
    while state["recording"].get("phase") == "unavailable":
        if cancellation_event is not None and cancellation_event.is_set():
            raise ControlUnavailable("native recovery was cancelled")
        if client.bootstrap_recovery_status() is not None:
            raise ControlUnavailable("replacement companion startup is still unavailable")
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            return None
        delay = min(0.1, remaining)
        if cancellation_event is None:
            time.sleep(delay)
        elif cancellation_event.wait(timeout=delay):
            raise ControlUnavailable("native recovery was cancelled")
        state = client.get_state(
            timeout_seconds=min(1.0, remaining),
            cancellation_event=cancellation_event,
            for_start=for_start,
        )
    return state


def recover_unresponsive_companion(
    client: CompanionClient,
    *,
    cancellation_event: threading.Event | None = None,
    on_termination: Callable[[], None] | None = None,
    before_replacement: Callable[[], None] | None = None,
    for_clicked_start: bool = False,
    terminal_bootstrap_only: bool = False,
    for_automatic_recovery: bool = False,
    revalidate_transaction: Callable[[], None] | None = None,
) -> CompanionRecoveryOutcome:
    """Repair a failed listener or replace its still-unresponsive verified owner."""

    if for_automatic_recovery and (for_clicked_start or terminal_bootstrap_only):
        raise ControlUnavailable("native recovery policies cannot be combined")

    def require_recovery_current() -> None:
        if cancellation_event is not None and cancellation_event.is_set():
            raise ControlUnavailable("native companion recovery was cancelled")
        revalidate_capture()
        if for_automatic_recovery:
            client.require_listener_recovery_allowed()
        if cancellation_event is not None and cancellation_event.is_set():
            raise ControlUnavailable("native companion recovery was cancelled")

    def require_recovery_allowed() -> None:
        require_recovery_current()
        if revalidate_transaction is not None:
            revalidate_transaction()
        if for_automatic_recovery:
            client.require_listener_recovery_unanswered()
        require_recovery_current()

    with client.explicit_recovery_guard(
        for_clicked_start=for_clicked_start or terminal_bootstrap_only or for_automatic_recovery
    ) as revalidate_capture:
        require_recovery_allowed()
        audio_activity = None
        if for_automatic_recovery:
            from companion_audio_activity import capture_audio_activity

            # Observe before the health wait so growth vetoes termination even
            # when Windows has not updated an open writer's last-write time.
            # Uncertain/recent audio never prevents non-destructive repair.
            audio_activity = capture_audio_activity(client.owner.root)
            if recover_companion_listener(client, cancellation_event=cancellation_event):
                return CompanionRecoveryOutcome.RESPONDING
            require_recovery_allowed()
            # Another cooperating client may already have repaired this
            # listener. Silence on the file channel never outranks fresh
            # authenticated control, including on Windows' unchanged pipe name.
            try:
                client.get_state(timeout_seconds=1.0, cancellation_event=cancellation_event)
            except ControlUnavailable as error:
                if not _listener_recovery_failed(error):
                    raise
            else:
                return CompanionRecoveryOutcome.RESPONDING
            require_recovery_allowed()
        local_failure: ControlConnectionUnavailable | None = None
        for attempt in range(0 if for_automatic_recovery else _EXPLICIT_RECOVERY_ATTEMPTS):
            require_recovery_allowed()
            try:
                fresh_state = client.get_state(
                    timeout_seconds=_EXPLICIT_RECOVERY_TIMEOUT_SECONDS,
                    cancellation_event=cancellation_event,
                )
            except ControlConnectionUnavailable as error:
                require_recovery_allowed()
                if terminal_bootstrap_only:
                    raise
                if not _transport_probe_failed(error):
                    local_failure = error
                if attempt + 1 < _EXPLICIT_RECOVERY_ATTEMPTS:
                    if cancellation_event is None:
                        time.sleep(_EXPLICIT_RECOVERY_RETRY_SECONDS)
                    else:
                        cancellation_event.wait(_EXPLICIT_RECOVERY_RETRY_SECONDS)
                continue
            # A responding owner retains native capture authority. A late idle
            # response still cannot reconcile a previously ambiguous Start.
            if cancellation_event is not None and cancellation_event.is_set():
                raise ControlUnavailable("native companion recovery was cancelled")
            terminal_observation = (
                client.terminal_bootstrap_recovery_observation(fresh_state=fresh_state)
                if for_clicked_start or terminal_bootstrap_only
                else None
            )
            if terminal_observation is not None and before_replacement is not None:
                # An explicit click can forward-recover a terminal startup owner.
                # Its replacement verifier must require a strictly newer image;
                # a repeated reset of the same failed build cannot repair it.
                def revalidate_terminal_capture(observation: int = terminal_observation) -> None:
                    client.require_unchanged_capture_observation(observation)

                revalidate_capture = revalidate_terminal_capture
                local_failure = None
                break
            if terminal_bootstrap_only:
                import control_client

                raise control_client.CooperativeHandoffDeclined(
                    "native companion terminal startup proof is unavailable",
                    recovery_blocker="terminal-bootstrap-not-quiescent",
                )
            client.require_explicit_recovery_allowed()
            return CompanionRecoveryOutcome.RESPONDING

        if local_failure is not None:
            raise local_failure

        def require_prepared_replacement() -> None:
            from companion_audio_activity import require_audio_inactive

            require_recovery_allowed()
            if audio_activity is not None and not client.closed:
                # Repeated by the platform adapter before every signal and
                # after reporting. After verified exit, this callback only
                # validates the prepared launch; final audio flushes are safe.
                require_audio_inactive(audio_activity)
            if before_replacement is not None:
                before_replacement()
            if audio_activity is not None and not client.closed:
                # Release verification and restart-budget I/O can block while
                # native capture keeps writing. Recheck after that preparation,
                # before the adapter's final descriptor/lease/process proof.
                require_audio_inactive(audio_activity)
            require_recovery_allowed()

        # This veto-capable preparation runs only once replacement is necessary,
        # and again at each destructive boundary; reporting cannot supply it.
        require_prepared_replacement()
        # Preserve both the original owner and capture fence through every signal.
        quit_companion_owner(
            client,
            revalidate_request=require_prepared_replacement,
            revalidate_recovery=require_recovery_current,
            policy=(
                CompanionReplacementPolicy.AUTOMATIC_UNRESPONSIVE
                if for_automatic_recovery
                else CompanionReplacementPolicy.TERMINAL_BOOTSTRAP
                if terminal_bootstrap_only
                else CompanionReplacementPolicy.CLICKED_START
                if for_clicked_start
                else CompanionReplacementPolicy.EXPLICIT_UNRESPONSIVE
            ),
            on_termination=on_termination,
        )
        return CompanionRecoveryOutcome.TERMINATED


def require_verified_companion_replacement(
    client: CompanionClient, runtime: Mapping[str, object], *, require_newer: bool
) -> None:
    """Bind recovery to verified full releases and exact image bytes."""

    import control_client
    from native_runtime_artifacts import verified_handoff_app_release_identity

    platform, target_path = runtime.get("platform"), runtime.get("appPath")
    owner_path = client.owner.runtime.get("appPath")
    owner_platform = client.owner.runtime.get("platform")
    if (
        not isinstance(platform, str)
        or not isinstance(owner_platform, str)
        or not isinstance(target_path, str)
        or not isinstance(owner_path, str)
        or runtime.get("installed") is not True
        or runtime.get("source") != "plugin-bundled"
    ):
        raise ControlUnavailable("native recovery replacement is unavailable")
    spec = control_client.runtime_spec_for(platform)
    owner_spec = control_client.runtime_spec_for(owner_platform)
    _verify_runtime_platform(client.owner.descriptor, runtime)
    _verify_runtime_identity(client.owner.descriptor, client.owner.runtime)
    target_release = RuntimeManager.native_release_version_key(
        verified_handoff_app_release_identity(Path(target_path), spec)
    )
    owner_release = RuntimeManager.native_release_version_key(
        verified_handoff_app_release_identity(Path(owner_path), owner_spec)
    )
    target_digest = control_client.sha256_regular_file(
        control_client.expected_executable_path(Path(target_path), spec)
    )
    owner_digest = client.owner.descriptor["executableIdentity"]["sha256"]
    if target_digest != runtime.get("_executableSHA256"):
        raise ControlUnavailable("native recovery replacement changed")
    if target_release < owner_release or (
        target_release == owner_release and (require_newer or target_digest != owner_digest)
    ):
        raise control_client.CooperativeHandoffDeclined(
            "native recovery requires a compatible newer release",
            recovery_blocker="compatible-replacement-unavailable",
        )


def quit_companion_owner(
    client: CompanionClient,
    *,
    revalidate_request: Callable[[], None] | None = None,
    revalidate_recovery: Callable[[], None] | None = None,
    immediate: bool = False,
    policy: CompanionReplacementPolicy = CompanionReplacementPolicy.VERIFIED_IDLE,
    on_termination: Callable[[], None] | None = None,
) -> None:
    """Replace one authenticated owner through its requested handoff policy.

    Args:
        client: Exact authenticated companion owner to replace.
        revalidate_request: Optional canonical requester proof before each destructive action.
        revalidate_recovery: Cheap cancellation and capture fence immediately before signaling.
        immediate: Force an explicitly confirmed update without requiring idle capture.
        policy: Typed capture and signal policy; immediate preserves confirmed Update callers.
        on_termination: Optional bounded report after verification, before the first signal.

    Raises:
        ControlUnavailable: If owner identity or process replacement cannot be verified.
    """

    import control_client

    if immediate:
        policy = CompanionReplacementPolicy.CONFIRMED_UPDATE
    owner = client.owner
    descriptor = owner.descriptor
    if policy is CompanionReplacementPolicy.VERIFIED_IDLE:
        initial = client.latest_state()
        if initial is None:
            raise control_client.CooperativeHandoffDeclined("native companion v2 owner is busy")
        replacement = initial["lifecycle"]["replacement"]
        if initial["recording"]["phase"] != "idle" or not replacement["allowed"]:
            raise control_client.CooperativeHandoffDeclined("native companion v2 owner is busy")
        client.require_explicit_recovery_allowed()
        if revalidate_request is not None:
            revalidate_request()
        try:
            response = client.quit_for_update(
                timeout_seconds=control_client.HANDOFF_RESPONSE_TIMEOUT_SECONDS,
            )
        except ControlUnavailable:
            response = None
        if response is not None and response["disposition"] == "accepted":
            if not hmac.compare_digest(response["ownerEpoch"], descriptor["ownerEpoch"]):
                raise ControlUnavailable("native companion v2 handoff owner does not match")
            if _wait_for_companion_exit(owner, control_client.HANDOFF_EXIT_TIMEOUT_SECONDS):
                client.close()
                if revalidate_request is not None:
                    revalidate_request()
                return

    # Cooperative quit authenticates the live peer. Forced replacement also
    # needs the original process image, which may no longer exist on disk.
    birth_identity = (
        client.listener_recovery_birth_identity
        if policy is CompanionReplacementPolicy.AUTOMATIC_UNRESPONSIVE
        else None
    )
    if policy is CompanionReplacementPolicy.AUTOMATIC_UNRESPONSIVE and birth_identity is None:
        raise ControlUnavailable("native companion v2 original process is unavailable")
    if descriptor["platform"] == "macos":
        from meetings_app.owner_recovery import verified_darwin_owner_process_image

        identity = descriptor["executableIdentity"]
        device, inode = identity.get("device"), identity.get("inode")
        if type(device) is not int or type(inode) is not int:
            raise ControlUnavailable("native companion v2 owner image is unavailable")
        birth_identity = verified_darwin_owner_process_image(
            descriptor["pid"],
            expected_path=Path(identity["path"]),
            expected_identity=(device, inode),
            expected_digest=identity["sha256"],
            expected_start_identity=birth_identity,
        )

    if policy is CompanionReplacementPolicy.VERIFIED_IDLE:
        _replace_companion_owner(client, birth_identity, revalidate_request)
    else:
        _replace_companion_owner(
            client,
            birth_identity,
            revalidate_request,
            revalidate_recovery=revalidate_recovery,
            policy=policy,
            on_termination=on_termination,
        )
    if not _wait_for_companion_exit(owner, control_client.HANDOFF_EXIT_TIMEOUT_SECONDS):
        raise control_client.CooperativeHandoffRequired("native companion v2 owner did not exit")
    report_companion_termination(
        outcome="exit_confirmed",
        policy=policy.value,
        active_owner_version=descriptor["companionVersion"],
    )
    client.close()
    if revalidate_request is not None:
        revalidate_request()


def _wait_for_companion_exit(owner: CompanionOwner, timeout_seconds: float) -> bool:
    import control_client

    deadline = time.monotonic() + timeout_seconds
    while time.monotonic() < deadline:
        if control_client.pid_is_proven_dead(owner.descriptor["pid"]):
            return control_client.owner_lock_state(owner.root) != "held"
        time.sleep(min(control_client.HANDOFF_OWNER_LOCK_POLL_SECONDS, 0.05))
    return False


def _replace_companion_owner(
    client: CompanionClient,
    birth_identity: tuple[int, int] | None,
    revalidate_request: Callable[[], None] | None,
    *,
    revalidate_recovery: Callable[[], None] | None = None,
    policy: CompanionReplacementPolicy = CompanionReplacementPolicy.VERIFIED_IDLE,
    on_termination: Callable[[], None] | None = None,
) -> None:
    import control_client
    import control_client_handoff

    owner = client.owner
    descriptor = owner.descriptor
    identity = descriptor["executableIdentity"]
    executable = Path(identity["path"])
    termination_reported = False

    def verify_replacement_authority() -> None:
        if policy is CompanionReplacementPolicy.AUTOMATIC_UNRESPONSIVE and client.closed:
            raise ControlUnavailable("native companion recovery was cancelled")
        if policy in {
            CompanionReplacementPolicy.CLICKED_START,
            CompanionReplacementPolicy.TERMINAL_BOOTSTRAP,
            CompanionReplacementPolicy.AUTOMATIC_UNRESPONSIVE,
        } and (revalidate_request is None or revalidate_recovery is None):
            raise ControlUnavailable("clicked recovery requires current owner health proof")
        if revalidate_recovery is not None:
            revalidate_recovery()
        if policy is not CompanionReplacementPolicy.VERIFIED_IDLE:
            _verify_runtime_identity(descriptor, owner.runtime)
            if policy is CompanionReplacementPolicy.EXPLICIT_UNRESPONSIVE:
                client.require_explicit_recovery_allowed()
        else:
            current = client.get_state()
            recording = current["recording"]
            replacement = current["lifecycle"]["replacement"]
            if recording["phase"] != "idle" or not replacement["allowed"]:
                raise control_client.CooperativeHandoffDeclined("native companion v2 owner is busy")
        if descriptor["platform"] == "macos":
            from meetings_app.owner_recovery import verified_darwin_owner_process_image

            device, inode = identity.get("device"), identity.get("inode")
            if type(device) is not int or type(inode) is not int or birth_identity is None:
                raise ControlUnavailable("native companion v2 original process is unavailable")
            verified_darwin_owner_process_image(
                descriptor["pid"],
                expected_path=executable,
                expected_identity=(device, inode),
                expected_digest=identity["sha256"],
                expected_start_identity=birth_identity,
            )
        if revalidate_request is not None:
            revalidate_request()
        # Preparation and process-image verification can block. Read the lease
        # only after those operations, then use an in-memory capture/cancellation
        # fence; never run a blocking requester callback after this owner proof.
        if policy is not CompanionReplacementPolicy.VERIFIED_IDLE:
            current_descriptor = control_client.read_json(owner.root / _DESCRIPTOR_FILENAME)
            if (
                current_descriptor != descriptor
                or control_client.owner_lock_state(owner.root) != "held"
            ):
                raise ControlUnavailable("native companion v2 owner identity changed")
        if descriptor["platform"] == "macos" and birth_identity is not None:
            from meetings_app.owner_recovery import require_unchanged_darwin_owner_process_birth

            require_unchanged_darwin_owner_process_birth(descriptor["pid"], birth_identity)
        if revalidate_recovery is not None:
            revalidate_recovery()
        if policy not in {
            CompanionReplacementPolicy.CONFIRMED_UPDATE,
            CompanionReplacementPolicy.CLICKED_START,
            CompanionReplacementPolicy.TERMINAL_BOOTSTRAP,
            CompanionReplacementPolicy.AUTOMATIC_UNRESPONSIVE,
        }:
            client.require_explicit_recovery_allowed()
        if policy is CompanionReplacementPolicy.AUTOMATIC_UNRESPONSIVE and client.closed:
            raise ControlUnavailable("native companion recovery was cancelled")

    def revalidate_owner() -> None:
        nonlocal termination_reported

        verify_replacement_authority()
        if on_termination is not None and not termination_reported:
            termination_reported = True
            try:
                on_termination()
            except Exception:
                # Reporting is best-effort and cannot veto a verified recovery.
                pass
            # Reporting may yield to cancellation, capture, or another owner.
            verify_replacement_authority()

    if descriptor["platform"] == "windows":
        app_path = owner.runtime.get("appPath")
        if not isinstance(app_path, str):
            raise ControlUnavailable("native companion v2 Windows image is unavailable")
        control_client_handoff.terminate_verified_windows_owner_process(
            descriptor["pid"],
            expected_path=executable,
            app_path=Path(app_path),
            expected_digest=identity["sha256"],
            digest_reader=control_client.sha256_regular_file,
            revalidate_owner=revalidate_owner,
            expected_start_identity=birth_identity,
        )
        report_companion_termination(
            outcome="signal_sent",
            method="terminate_process",
            policy=policy.value,
            active_owner_version=descriptor["companionVersion"],
        )
        return

    if policy is CompanionReplacementPolicy.CONFIRMED_UPDATE:
        revalidate_owner()
        control_client.os.kill(descriptor["pid"], control_client.signal.SIGKILL)
        report_companion_termination(
            outcome="signal_sent",
            method="sigkill",
            policy=policy.value,
            active_owner_version=descriptor["companionVersion"],
        )
        return

    owner_identity = (descriptor["pid"], descriptor["ownerEpoch"])
    with control_client.capture_aware_sigterm_owners() as signaled:
        if owner_identity not in signaled:
            if len(signaled) >= control_client.MAXIMUM_CAPTURE_AWARE_SIGTERM_OWNERS:
                raise ControlUnavailable("native companion v2 signal history is saturated")
            revalidate_owner()
            control_client.os.kill(descriptor["pid"], control_client.signal.SIGTERM)
            signaled.add(owner_identity)
            report_companion_termination(
                outcome="signal_sent",
                method="sigterm",
                policy=policy.value,
                active_owner_version=descriptor["companionVersion"],
            )
    if _wait_for_companion_exit(
        owner,
        1.0
        if policy
        in {
            CompanionReplacementPolicy.AUTOMATIC_UNRESPONSIVE,
            CompanionReplacementPolicy.CLICKED_START,
        }
        else control_client_handoff.AUTOMATIC_GRACEFUL_EXIT_TIMEOUT_SECONDS,
    ):
        return
    revalidate_owner()
    control_client.os.kill(descriptor["pid"], control_client.signal.SIGKILL)
    report_companion_termination(
        outcome="signal_sent",
        method="sigkill",
        policy=policy.value,
        active_owner_version=descriptor["companionVersion"],
    )


def _plugin_version() -> str:
    from meetings_sentry import plugin_version

    version = plugin_version(Path(__file__).resolve().parents[1])
    return version if isinstance(version, str) and version else "0.0.0"
