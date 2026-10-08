#!/usr/bin/env python3
"""Locate, verify, and launch the ChatGPT Meetings companion.

The signed companion is shipped beside the plugin scripts, then materialized
into an immutable, profile-isolated Codex-owned generation before local-dev or
production launch. Recordings, upload state, and the private control bridge stay
in Application Support; a
running executable never depends on a prunable plugin-cache directory.

The signed plugin-local artifact remains the distribution authority. Mutable
recording, upload, and control state never becomes an alternate runtime cache.
"""

from __future__ import annotations

import ctypes
import hashlib as hashlib

try:
    import fcntl
except ImportError:  # Windows has no POSIX descriptor/lock module.
    fcntl = None
import json
import os
import platform
import plistlib
import re
import stat
import subprocess
import sys
import threading
import time as time
import uuid as uuid
from collections.abc import Mapping, Sequence
from contextlib import contextmanager as contextmanager
from contextvars import ContextVar
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import TYPE_CHECKING, Callable, Final, Literal, Protocol
from typing import Iterator as Iterator

from meetings_sentry import (
    MCP_SENTRY_FAILURE_DIAGNOSTIC_VALUES,
    MCP_SENTRY_HANDOFF_FAILURE_REASONS,
    MCP_SENTRY_MATERIALIZE_FAILURE_REASONS,
    MCP_SENTRY_MATERIALIZE_VERIFICATION_PHASES,
    McpSentryDiagnostics,
    report_mcp_error,
    report_recovered_handoff,
)
from native_runtime_types import (
    NativeArtifactFingerprint,
    PlatformRuntimeSpec,
    PublicNativeRuntimeStatus,
)
from recording_control_action_contract import (
    ControlPlatform,
    ControlPlatformWire,
)
from recording_control_stream_contract import (
    CONTROL_STREAM_DARWIN_CAPABILITIES,
    CONTROL_STREAM_WINDOWS_CAPABILITIES,
    CONTROL_STREAM_WINDOWS_REQUIRED_UPDATE_CAPABILITIES,
)
from runtime_config import RUNTIME_CONFIG

CONTROL_CAPABILITIES_BY_PLATFORM: Final[dict[str, tuple[str, ...]]] = {
    ControlPlatform.DARWIN_UNIVERSAL.value: CONTROL_STREAM_DARWIN_CAPABILITIES,
    ControlPlatform.DARWIN_ARM64.value: CONTROL_STREAM_DARWIN_CAPABILITIES,
    ControlPlatform.DARWIN_X64.value: CONTROL_STREAM_DARWIN_CAPABILITIES,
    ControlPlatform.WINDOWS_X64.value: CONTROL_STREAM_WINDOWS_CAPABILITIES,
    ControlPlatform.WINDOWS_ARM64.value: CONTROL_STREAM_WINDOWS_CAPABILITIES,
}


class ControlCapability(str, Enum):
    """Known generated live-stream capability; unknown values grant no authority."""

    CONTROL_LOCAL_STREAM_V1 = "control.local-stream.v1"
    CAPTURE_MICROPHONE_V1 = "capture.microphone.v1"
    CAPTURE_SYSTEM_AUDIO_V1 = "capture.system-audio.v1"
    CAPTURE_CONTEXT_V1 = "capture.context.v1"
    RECORDING_LOCAL_WAV_V1 = "recording.local-wav.v1"
    RECORDING_STOP_V1 = "recording.stop.v1"
    RECORDING_PAUSE_RESUME_V1 = "recording.pause-resume.v1"
    RECORDING_SESSION_FENCED_CONTROLS_V1 = "recording.session-fenced-controls.v1"
    RECORDING_RECEIPT_V1 = "recording.receipt.v1"
    UI_FLOATING_OVERLAY_V1 = "ui.floating-overlay.v1"
    UPLOAD_OUTBOX_V1 = "upload.outbox.v1"
    UPLOAD_POST_STOP_V1 = "upload.post-stop.v1"
    UPLOAD_MANUAL_RETRY_V1 = "upload.manual-retry.v1"
    UPLOAD_MANUAL_RETRY_TARGETED_V1 = "upload.manual-retry.targeted.v1"
    HEADLESS_SETTINGS_V1 = "headless.settings.v1"
    HEADLESS_SYNC_HOOK_V1 = "headless.sync-hook.v1"
    HEADLESS_NOTE_DETAIL_V1 = "headless.note-detail.v1"
    LOGS_VIEWER_V1 = "logs.viewer.v1"
    AUTH_CODEX_READINESS_V1 = "auth.codex-readiness.v1"
    WIDGET_SNAPSHOT_V1 = "widget.snapshot.v1"
    WIDGET_RECENT_RECORDING_V1 = "widget.recent-recording.v1"
    HOME_CACHE_V1 = "home.cache.v1"
    HOME_CACHE_REFRESH_V1 = "home.cache.refresh.v1"
    CALENDAR_AUTOMATION_SYNC_V1 = "calendar.automation-sync.v1"
    LIFECYCLE_UPDATE_HANDOFF_V1 = "lifecycle.update-handoff.v1"
    LIFECYCLE_UPDATE_HANDOFF_WORK_FENCE_V1 = "lifecycle.update-handoff-work-fence.v1"
    LIFECYCLE_UPDATE_HANDOFF_RESUMABLE_OUTBOX_V1 = "lifecycle.update-handoff-resumable-outbox.v1"
    LIFECYCLE_UPDATE_HANDOFF_RESUMABLE_OUTBOX_V2 = "lifecycle.update-handoff-resumable-outbox.v2"
    LIFECYCLE_CAPTURE_AWARE_SIGTERM_V1 = "lifecycle.capture-aware-sigterm.v1"
    UNKNOWN = "unknown"

    @classmethod
    def _missing_(cls, value: object) -> ControlCapability | None:
        return cls.UNKNOWN if isinstance(value, str) else None

    def supported_on_platform(self, platform: ControlPlatform) -> bool:
        if self is type(self).UNKNOWN or platform is ControlPlatform.UNKNOWN:
            return False
        return self.value in CONTROL_CAPABILITIES_BY_PLATFORM.get(platform.value, ())


class _WindowsCtypesApi(Protocol):
    def WinDLL(self, name: str, *, use_last_error: bool) -> ctypes.CDLL: ...


# Linux Pyright stubs intentionally omit this Windows-only ctypes member.
if TYPE_CHECKING:
    _windows_ctypes: _WindowsCtypesApi
else:
    _windows_ctypes = ctypes


APP_NAME = RUNTIME_CONFIG.app_name
# One immutable runtime config binds the development checkout or production
# artifact to its matching bundle ID, state root, control target, and signer.
BUNDLE_ID = RUNTIME_CONFIG.bundle_identifier
APP_SUPPORT_DIRECTORY_NAME = RUNTIME_CONFIG.app_support_directory
TEAM_IDENTIFIER = RUNTIME_CONFIG.team_identifier
PLUGIN_FRAMEWORK_SYMLINKS = RUNTIME_CONFIG.framework_symlinks
OFFICIAL_CACHE_PUBLISHERS = frozenset(RUNTIME_CONFIG.official_cache_publishers)
PLUGIN_BUNDLE_CROSS_PROCESS_LOCK_TIMEOUT_SECONDS = 10.0
STABLE_RUNTIME_LOCK_TIMEOUT_SECONDS = 10.0
STABLE_RUNTIME_DIRECTORY_NAME = "chatgpt-meetings"
DEVELOPMENT_STABLE_RUNTIME_DIRECTORY_NAME = "chatgpt-meetings-dev"
DEVELOPMENT_SIGNING_AUTHORITY = "ChatGPT Meetings Local Development"
STABLE_RUNTIME_MANIFEST_MAX_BYTES = 16 * 1024
STABLE_RUNTIME_SCHEMA_VERSION = 1
VERIFIED_CAM_DISTRIBUTION_RELATIVE_PATH = Path("native/verified-cam-distribution.json")
NATIVE_BUILD_RECEIPT_NAME = "meetings-build-receipt.json"
LEGACY_NATIVE_BUILD_RECEIPT_NAME = "sushi-build-receipt.json"
NATIVE_BUILD_RECEIPT_NAMES = (NATIVE_BUILD_RECEIPT_NAME, LEGACY_NATIVE_BUILD_RECEIPT_NAME)
PLATFORM_OVERRIDE_ENV = "CHATGPT_MEETINGS_NATIVE_PLATFORM"
E2E_ISOLATED_ENV = "CHATGPT_MEETINGS_E2E_ISOLATED"
# Shared app configuration (including Sentry and hosted policy) deliberately
# recognizes a separate gate. Only synthesize it for the already-validated
# direct-executable E2E launch below; an ambient value must never be enough to
# activate the native isolation path.
CODEX_E2E_ISOLATED_ENV = "CHATGPT_MEETINGS_CODEX_E2E_ISOLATED"
LEGACY_CODEX_E2E_ISOLATED_ENV = "SUSHI_CODEX_MEETINGS_E2E_ISOLATED"
E2E_ROOT_ENV = "CHATGPT_MEETINGS_E2E_ROOT"
E2E_NATIVE_ROOT_ENV = "CHATGPT_MEETINGS_E2E_NATIVE_ROOT"
E2E_CAPTURE_MODE_ENV = "CHATGPT_MEETINGS_E2E_CAPTURE_MODE"
E2E_LAUNCH_REPORT_FD_ENV = "CHATGPT_MEETINGS_E2E_LAUNCH_REPORT_FD"
E2E_LAUNCH_REPORT_NONCE_ENV = "CHATGPT_MEETINGS_E2E_LAUNCH_REPORT_NONCE"
E2E_LAUNCH_REPORT_KIND = "chatgpt-meetings-e2e-launch-report"
E2E_LIVE_PROCESS_REGISTRY_RELATIVE_PATH = Path("tmp/live-processes.json")
E2E_LIVE_PROCESS_REGISTRY_MAX_BYTES = 32 * 1_024
E2E_LIVE_PROCESS_REGISTRY_MAX_ENTRIES = 64
E2E_LIVE_PROCESS_REGISTRY_LOCK_TIMEOUT_SECONDS = 2.0
E2E_COMPANION_EXEC_GATE_ARGUMENT = "--e2e-companion-exec-gate-v1"
E2E_STDIO_EXEC_GATE_ARGUMENT = "--e2e-stdio-exec-gate-v1"
E2E_STDIO_PROFILE_PROTOTYPE = "prototype"
E2E_STDIO_PROFILE_PRODUCTION = "production"
E2E_STDIO_PROFILES = frozenset({E2E_STDIO_PROFILE_PROTOTYPE, E2E_STDIO_PROFILE_PRODUCTION})
E2E_DETERMINISTIC_CAPTURE_MODE = "deterministic-rust-v1"
E2E_ROOT_MARKER = ".chatgpt-meetings-e2e-root-v1"
E2E_ROOT_MARKER_CONTENT = b"chatgpt-meetings-e2e-v1\n"
_E2E_REGISTERED_CHILD_ANCHORS_LOCK = threading.Lock()
# launch_current returns only a PID, so dropping its local Popen would let
# Popen.__del__ poll and reap a fast-exited group leader before the probe uses
# the reported handle. Retain successful E2E children for the MCP lifetime;
# the shared registry's 64-entry contract keeps this supervisor table bounded.
_E2E_REGISTERED_CHILD_ANCHORS: dict[int, subprocess.Popen[bytes]] = {}
_WINDOWS_PENDING_CHILDREN_LOCK = threading.Lock()
_MAXIMUM_WINDOWS_PENDING_CHILDREN = 16
PLUGIN_ROOT = Path(__file__).resolve().parents[1]
MAXIMUM_ARCHIVE_BYTES = 256 * 1024 * 1024
MAXIMUM_MANIFEST_BYTES = 128 * 1024
MAXIMUM_PLUGIN_FRAMEWORK_ENTRIES = 4096
MAXIMUM_PLUGIN_RESOURCE_ENTRIES = 100_000
MAXIMUM_DARWIN_MACHO_SLICES = 64
MAXIMUM_STABLE_RUNTIME_ENTRIES = 100_000
DARWIN_MACHO_CPU_TYPES = {
    "darwin-arm64": 0x0100000C,
    "darwin-x64": 0x01000007,
}
WINDOWS_PLUGIN_RUNTIME_DESCRIPTOR_RELATIVE_PATH = Path(".codex-plugin/windows-runtime.json")
WINDOWS_PRODUCTION_AZURE_ACCOUNT_NAME = "oaisidekickuploads"
WINDOWS_PRODUCTION_AZURE_CONTAINER_NAME = "chatgpt-meetings"
WINDOWS_PRODUCTION_BUNDLE_RELATIVE_PATH = Path("native/windows-production-bundle.json")
WINDOWS_PRODUCTION_LOCK_RELATIVE_PATH = Path("native/cam-windows-artifact.lock.json")
OPEN_EXIT_CHECK_TIMEOUT_SECONDS = 0.25
WINDOWS_CHILD_EXIT_CHECK_TIMEOUT_SECONDS = 0.25
WINDOWS_LAUNCH_ATTEMPT_LIMIT = 3
WINDOWS_LAUNCH_OWNER_CONFIRM_TIMEOUT_SECONDS = 5.0
WINDOWS_SIGNATURE_VERIFICATION_TIMEOUT_SECONDS = 10.0
COMPANION_CA_ENVIRONMENT_KEYS = ("CODEX_CA_CERTIFICATE", "SSL_CERT_FILE")
WINDOWS_COMPANION_ENVIRONMENT_KEYS = (
    "SYSTEMDRIVE",
    "SYSTEMROOT",
    "WINDIR",
    "PROGRAMDATA",
    "ALLUSERSPROFILE",
    "COMMONPROGRAMFILES",
    "COMMONPROGRAMFILES(X86)",
    "COMMONPROGRAMW6432",
    "LOCALAPPDATA",
    "APPDATA",
    "USERPROFILE",
    "TEMP",
    "TMP",
    *COMPANION_CA_ENVIRONMENT_KEYS,
)
GITHUB_RELEASE_COMPONENT = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\Z")
SHA256_HEX_PATTERN = re.compile(r"[a-f0-9]{64}\Z")


WINDOWS_REQUIRED_UPDATE_CAPABILITIES = frozenset(
    CONTROL_STREAM_WINDOWS_REQUIRED_UPDATE_CAPABILITIES
)


def stable_runtime_directory_name() -> str:
    """Keep the local-development native owner isolated from production."""

    if RUNTIME_CONFIG.flavor == "development" and RUNTIME_CONFIG.default_mcp_profile == "local-dev":
        return DEVELOPMENT_STABLE_RUNTIME_DIRECTORY_NAME
    return STABLE_RUNTIME_DIRECTORY_NAME


class NativeRuntimeError(RuntimeError):
    pass


class NativeRuntimeResourceOperation(Enum):
    """Observed filesystem boundaries; never inferred from a path or message."""

    RESOLVE_ARTIFACT_ROOT = ("resolve_artifact_root", "artifact_root")
    RESOLVE_NATIVE_ARTIFACT = ("resolve_native_artifact", "native_artifact")
    READ_BUNDLE_METADATA = ("read_bundle_metadata", "bundle_metadata")

    def __init__(self, operation: str, role: str) -> None:
        self.operation = operation
        self.role = role


class NativeRuntimeResourceError(NativeRuntimeError):
    """Preserve a resource boundary without granting retry or replacement authority."""

    def __init__(self, operation: NativeRuntimeResourceOperation) -> None:
        super().__init__("native runtime resource is unavailable")
        self.operation = operation


class NativeRuntimeRegistrationUnavailable(NativeRuntimeError):
    """A previously observed installation path disappeared during verification.

    This grants only a delayed recheck, never authority to launch a different
    image or terminate a running owner. The role is a fixed code, not a path.
    """

    def __init__(
        self,
        role: Literal["plugin_root", "family_root", "registration_manifest", "registered_plugin"],
    ) -> None:
        super().__init__("ChatGPT Meetings plugin registration is unavailable")
        self.role = role


class NativeRuntimeArtifactMissing(NativeRuntimeError):
    """The expected native child was absent beneath an existing plugin root."""

    def __init__(self) -> None:
        super().__init__("plugin-bundled native artifact is unavailable")


class NativeRuntimeLockBusy(NativeRuntimeError):
    """Another operation still holds a verified native runtime or bundle lock."""


class NativeRuntimeQuitRequired(NativeRuntimeError):
    """The proven older companion cannot cooperatively leave for an update.

    This is deliberately a typed local boundary instead of forwarding the
    control client's exception text. MCP can turn it into one fixed recovery
    state without leaking descriptor paths or implementation details.
    """


class NativeRuntimeUpdateDeferred(NativeRuntimeQuitRequired):
    """A proven cooperative owner is busy and may safely yield later."""


class NativeRuntimeLaunchPending(NativeRuntimeError):
    """Launch cannot safely retry while an exact spawned child remains live.

    Foreground callers still receive an error. Initialize bootstrap uses this
    marker only to adopt its existing poll/cooldown lane instead of spawning a
    second process while the first child may still converge or exit.
    """


class NativeRuntimeLaunchPendingQuitRequired(
    NativeRuntimeQuitRequired,
    NativeRuntimeLaunchPending,
):
    """A pending exact child raced a proven non-cooperative older owner."""


class NativeRuntimeLaunchPendingUpdateDeferred(
    NativeRuntimeUpdateDeferred,
    NativeRuntimeLaunchPending,
):
    """A pending exact child raced a proven busy cooperative older owner."""


@dataclass
class _WindowsPendingChild:
    process: subprocess.Popen[bytes]
    observing: bool
    codex_launch_context: tuple[str, str] | None = None


_WindowsPendingChildKey = tuple[
    str,
    str,
    str,
]
_WINDOWS_PENDING_CHILDREN: dict[_WindowsPendingChildKey, _WindowsPendingChild] = {}


class _ProcBSDInfo(ctypes.Structure):
    _fields_ = [
        ("pbi_flags", ctypes.c_uint32),
        ("pbi_status", ctypes.c_uint32),
        ("pbi_xstatus", ctypes.c_uint32),
        ("pbi_pid", ctypes.c_uint32),
        ("pbi_ppid", ctypes.c_uint32),
        ("pbi_uid", ctypes.c_uint32),
        ("pbi_gid", ctypes.c_uint32),
        ("pbi_ruid", ctypes.c_uint32),
        ("pbi_rgid", ctypes.c_uint32),
        ("pbi_svuid", ctypes.c_uint32),
        ("pbi_svgid", ctypes.c_uint32),
        ("rfu_1", ctypes.c_uint32),
        ("pbi_comm", ctypes.c_char * 16),
        ("pbi_name", ctypes.c_char * 32),
        ("pbi_nfiles", ctypes.c_uint32),
        ("pbi_pgid", ctypes.c_uint32),
        ("pbi_pjobc", ctypes.c_uint32),
        ("e_tdev", ctypes.c_uint32),
        ("e_tpgid", ctypes.c_uint32),
        ("pbi_nice", ctypes.c_int32),
        ("pbi_start_tvsec", ctypes.c_uint64),
        ("pbi_start_tvusec", ctypes.c_uint64),
    ]


from native_runtime_e2e import (
    _discard_pre_exec_e2e_child as _discard_pre_exec_e2e_child,
)
from native_runtime_e2e import (
    _e2e_companion_exec_gate as _e2e_companion_exec_gate,
)
from native_runtime_e2e import (
    _e2e_exec_gate as _e2e_exec_gate,
)
from native_runtime_e2e import (
    _e2e_stdio_exec_gate as _e2e_stdio_exec_gate,
)
from native_runtime_e2e import (
    _initialize_e2e_live_process_registry as _initialize_e2e_live_process_registry,
)
from native_runtime_e2e import (
    _live_process_registry_entry as _live_process_registry_entry,
)
from native_runtime_e2e import (
    _mutate_e2e_live_process_registry as _mutate_e2e_live_process_registry,
)
from native_runtime_e2e import (
    _process_start_identity as _process_start_identity,
)
from native_runtime_e2e import (
    _publish_e2e_launch_report as _publish_e2e_launch_report,
)
from native_runtime_e2e import (
    _read_live_process_registry_at as _read_live_process_registry_at,
)
from native_runtime_e2e import (
    _register_e2e_live_process as _register_e2e_live_process,
)
from native_runtime_e2e import (
    _require_e2e_pipe_descriptor as _require_e2e_pipe_descriptor,
)
from native_runtime_e2e import (
    _retain_registered_e2e_child as _retain_registered_e2e_child,
)
from native_runtime_e2e import (
    _spawn_registered_e2e_companion as _spawn_registered_e2e_companion,
)
from native_runtime_e2e import (
    _strict_live_process_registry as _strict_live_process_registry,
)
from native_runtime_e2e import (
    _terminate_unreported_e2e_child as _terminate_unreported_e2e_child,
)
from native_runtime_e2e import (
    _write_live_process_registry_at as _write_live_process_registry_at,
)

_PUBLIC_RUNTIME_COMPONENT = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,79}\Z")
_NATIVE_ALPHA_RELEASE_VERSION = re.compile(
    r"(0|[1-9][0-9]{0,8})\.(0|[1-9][0-9]{0,8})\.(0|[1-9][0-9]{0,8})"
    r"-alpha\.([1-9][0-9]{0,8})\Z"
)
_BUILD_TIMESTAMP_UTC_PATTERN = re.compile(
    r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z\Z"
)
_PUBLIC_RUNTIME_UPDATE_ERROR = "Native update check is unavailable"
_NATIVE_RUNTIME_EVENT_COMPONENT = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}\Z")
_NATIVE_RUNTIME_EVENT_GENERATION = re.compile(r"[a-z0-9-]+-[a-f0-9]{64}\Z")
_NATIVE_RUNTIME_HANDOFF_DISPOSITIONS = frozenset({"fallback_started", "start_failed"})
_NATIVE_RUNTIME_HANDOFF_OPERATIONS = frozenset({"new_note", "stop"})
_NATIVE_RUNTIME_RECOVERY_KINDS = frozenset(
    {
        "fallback_connection_failed",
        "owner_changed",
        "quit_required",
        "start_retry_required",
        "update_deferred",
    }
)
_NATIVE_RUNTIME_SENTRY_FAILURES = frozenset(
    {
        ("materialize", "copy"),
        ("materialize", "verify"),
        ("materialize", "publish"),
        ("handoff", "handoff"),
        ("recording", "connection"),
        ("recording", "handoff"),
        ("recording", "runtime"),
    }
)


@dataclass
class BootstrapHandoffReporting:
    """Capture one private handoff failure until bootstrap proves its outcome."""

    diagnostics: McpSentryDiagnostics | None = None
    recovered: bool = False


_BOOTSTRAP_HANDOFF_REPORTING: ContextVar[BootstrapHandoffReporting | None] = ContextVar(
    "meetings_bootstrap_handoff_reporting", default=None
)


@contextmanager
def capture_bootstrap_handoff_failure(
    episode: BootstrapHandoffReporting,
) -> Iterator[None]:
    """Scope deferred handoff telemetry to exactly one verified launch call."""

    token = _BOOTSTRAP_HANDOFF_REPORTING.set(episode)
    try:
        yield
    finally:
        _BOOTSTRAP_HANDOFF_REPORTING.reset(token)


def report_bootstrap_handoff_outcome(episode: BootstrapHandoffReporting) -> None:
    """Emit one final handoff notice or error after launch context is cleared."""

    if episode.diagnostics is None:
        return
    try:
        if episode.recovered:
            report_recovered_handoff(
                active_owner_version=episode.diagnostics.get("active_owner_version"),
                target_owner_version=episode.diagnostics.get("target_owner_version"),
                handoff_reason=episode.diagnostics.get("handoff_reason"),
            )
        else:
            report_mcp_error("handoff", "handoff", **episode.diagnostics)
    except Exception:
        # Diagnostics never interfere with verified owner recovery.
        pass


def log_native_runtime_event(
    stage: str,
    outcome: str,
    *,
    platform: object = None,
    version: object = None,
    build_timestamp: object = None,
    generation: object = None,
    previous_generation: object = None,
    attempt: object = None,
    error_kind: object = None,
    trigger: object = None,
    reason: object = None,
    active_owner_version: object = None,
    target_owner_version: object = None,
    handoff_disposition: object = None,
    recovery_kind: object = None,
    operation: object = None,
    verification_phase: object = None,
    failure_operation: object = None,
    resource_role: object = None,
    os_error_code: object = None,
    pid: object = None,
    duration_ms: object = None,
) -> None:
    """Emit a small, path-free companion update lifecycle envelope to stderr.

    Args:
        stage: Bounded lifecycle stage name.
        outcome: Bounded lifecycle outcome name.
        platform: Untrusted platform diagnostic to include when safe.
        version: Untrusted runtime version diagnostic to include when safe.
        build_timestamp: Untrusted packaged UTC timestamp to include when valid.
        generation: Untrusted active generation identifier to include when safe.
        previous_generation: Untrusted prior generation identifier to include when safe.
        attempt: Untrusted bounded retry count to include when valid.
        error_kind: Untrusted failure category to include when safe.
        trigger: Untrusted lifecycle trigger to include when safe.
        reason: Untrusted bounded reason code to include when safe.
        active_owner_version: Untrusted existing-owner version diagnostic.
        target_owner_version: Untrusted successor-owner version diagnostic.
        handoff_disposition: Untrusted handoff result diagnostic.
        recovery_kind: Untrusted recovery strategy diagnostic.
        operation: Untrusted recording operation diagnostic.
        verification_phase: Untrusted bounded materialization verification boundary.
        failure_operation: Untrusted bounded Stop failure operation.
        resource_role: Untrusted bounded Stop failure resource role.
        os_error_code: Untrusted bounded Stop operating-system error code.
        pid: Optional local process identifier when safely bounded.
        duration_ms: Optional safely bounded operation duration in milliseconds.

    Returns:
        None. Invalid or private diagnostics are omitted.
    """

    if (
        not isinstance(stage, str)
        or _NATIVE_RUNTIME_EVENT_COMPONENT.fullmatch(stage) is None
        or not isinstance(outcome, str)
        or _NATIVE_RUNTIME_EVENT_COMPONENT.fullmatch(outcome) is None
    ):
        return
    is_native_owner_handoff_failure = stage == "handoff" and error_kind == "handoff"
    handoff_reason = (
        reason if type(reason) is str and reason in MCP_SENTRY_HANDOFF_FAILURE_REASONS else None
    )
    if (stage, error_kind) == ("materialize", "verify") and (
        type(reason) is not str or reason not in MCP_SENTRY_MATERIALIZE_FAILURE_REASONS
    ):
        reason = None
    event: dict[str, str | int] = {"stage": stage, "outcome": outcome}
    for key, value in (
        ("platform", platform),
        ("version", version),
        ("errorKind", error_kind),
        ("trigger", trigger),
        ("reason", handoff_reason if is_native_owner_handoff_failure else reason),
    ):
        if isinstance(value, str) and _NATIVE_RUNTIME_EVENT_COMPONENT.fullmatch(value):
            event[key] = value
    timestamp = safe_build_timestamp_utc(build_timestamp)
    if timestamp is not None:
        event["buildTimestamp"] = timestamp
    for key, value in (
        ("generation", generation),
        ("previousGeneration", previous_generation),
    ):
        if isinstance(value, str) and _NATIVE_RUNTIME_EVENT_GENERATION.fullmatch(value):
            event[key] = value
    if type(attempt) is int and 0 <= attempt <= 1_000:
        event["attempt"] = attempt
    if type(pid) is int and 1 <= pid <= 2_147_483_647:
        event["pid"] = pid
    if type(duration_ms) is int and 0 <= duration_ms <= 3_600_000:
        event["durationMs"] = duration_ms
    diagnostics = McpSentryDiagnostics()
    is_recording_owner_failure = (
        stage == "recording"
        and isinstance(error_kind, str)
        and error_kind in {"handoff", "connection"}
    )
    if (stage, error_kind) == ("materialize", "verify") and isinstance(reason, str):
        diagnostics["failure_reason"] = reason
    if (
        (stage, error_kind) == ("materialize", "verify")
        and outcome == "failed"
        and type(verification_phase) is str
        and verification_phase in MCP_SENTRY_MATERIALIZE_VERIFICATION_PHASES
    ):
        event["verificationPhase"] = verification_phase
        diagnostics["verification_phase"] = verification_phase
    if is_recording_owner_failure or is_native_owner_handoff_failure:
        if is_native_owner_handoff_failure and handoff_reason is not None:
            diagnostics["handoff_reason"] = handoff_reason
        if (
            is_native_owner_handoff_failure
            and target_owner_version is None
            and isinstance(version, str)
            and _NATIVE_ALPHA_RELEASE_VERSION.fullmatch(version) is not None
        ):
            target_owner_version = version
        for event_key, value in (
            ("activeOwnerVersion", active_owner_version),
            ("targetOwnerVersion", target_owner_version),
        ):
            if (
                isinstance(value, str)
                and value.lower() != "unknown"
                and _PUBLIC_RUNTIME_COMPONENT.fullmatch(value)
                and (
                    not is_native_owner_handoff_failure
                    or _NATIVE_ALPHA_RELEASE_VERSION.fullmatch(value) is not None
                )
            ):
                event[event_key] = value
                if event_key == "activeOwnerVersion":
                    diagnostics["active_owner_version"] = value
                else:
                    diagnostics["target_owner_version"] = value
        if (
            isinstance(handoff_disposition, str)
            and handoff_disposition in _NATIVE_RUNTIME_HANDOFF_DISPOSITIONS
        ):
            event["handoffDisposition"] = handoff_disposition
            diagnostics["handoff_disposition"] = handoff_disposition
        if isinstance(recovery_kind, str) and recovery_kind in _NATIVE_RUNTIME_RECOVERY_KINDS:
            event["recoveryKind"] = recovery_kind
            diagnostics["recovery_kind"] = recovery_kind
        if (
            is_recording_owner_failure
            and isinstance(operation, str)
            and operation in _NATIVE_RUNTIME_HANDOFF_OPERATIONS
            and (operation != "stop" or error_kind == "connection")
        ):
            event["operation"] = operation
            diagnostics["operation"] = operation
    if (stage, error_kind, operation) == ("recording", "connection", "stop"):
        failure_candidates: tuple[
            tuple[Literal["failure_operation", "resource_role", "os_error_code"], object], ...
        ] = (
            ("failure_operation", failure_operation),
            ("resource_role", resource_role),
            ("os_error_code", os_error_code),
        )
        for key, candidate in failure_candidates:
            if candidate is not None:
                value = (
                    candidate
                    if type(candidate) is str
                    and candidate in MCP_SENTRY_FAILURE_DIAGNOSTIC_VALUES[key]
                    else "unknown"
                )
                event[key] = value
                diagnostics[key] = value
    if (
        outcome == "failed"
        and isinstance(error_kind, str)
        and (stage, error_kind) in _NATIVE_RUNTIME_SENTRY_FAILURES
    ):
        episode = _BOOTSTRAP_HANDOFF_REPORTING.get() if is_native_owner_handoff_failure else None
        if episode is not None:
            episode.diagnostics = diagnostics.copy()
        else:
            report_mcp_error(stage, error_kind, **diagnostics)
    try:
        print(
            f"ChatGPT Meetings native runtime: {json.dumps(event, sort_keys=True)}",
            file=sys.stderr,
            flush=True,
        )
    except (OSError, TypeError, ValueError):
        # A closed parent stderr pipe must not turn a valid update or recovery
        # into a failed MCP request.
        pass


def safe_build_timestamp_utc(value: object) -> str | None:
    """Accept only the immutable UTC build stamp format emitted by packaging.

    Args:
        value: Untrusted candidate build timestamp.

    Returns:
        The validated UTC timestamp, or None when the candidate is malformed.
    """

    if not isinstance(value, str) or not _BUILD_TIMESTAMP_UTC_PATTERN.fullmatch(value):
        return None
    try:
        datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return None
    return value


def public_runtime_capabilities(platform_key: object) -> tuple[str, ...]:
    """Return generated portable capabilities for any supported native platform.

    Args:
        platform_key: Untrusted candidate platform identifier.

    Returns:
        All supported generated feature capabilities, or no capabilities for an
        unknown native platform.
    """

    if not isinstance(platform_key, str):
        return ()
    if platform_key not in PLATFORM_RUNTIME_SPECS:
        return ()
    return tuple(
        capability.value
        for capability in ControlCapability
        if capability
        not in {
            ControlCapability.UNKNOWN,
            ControlCapability.CALENDAR_AUTOMATION_SYNC_V1,
            ControlCapability.HOME_CACHE_REFRESH_V1,
        }
    )


def public_runtime_status(status: Mapping[str, object]) -> PublicNativeRuntimeStatus:
    """Return the runtime facts safe to expose through MCP/model payloads.

    RuntimeManager keeps absolute paths internally because descriptor binding,
    signature verification, and LaunchServices need them. Public status only
    needs coarse install/version/capability facts; copying that projection here
    prevents a future caller from accidentally returning app/artifact paths or
    release-feed URLs.

    Args:
        status: Verified private runtime facts to sanitize for public projection.

    Returns:
        A path-free, capability-filtered runtime status payload.
    """

    raw = status
    version = raw.get("version")
    build_timestamp = safe_build_timestamp_utc(raw.get("buildTimestamp"))
    platform_key = raw.get("platform")
    artifact_kind = raw.get("artifactKind")
    source = raw.get("source")
    capabilities = raw.get("capabilities")
    allowed_capabilities = public_runtime_capabilities(platform_key)
    projected: PublicNativeRuntimeStatus = {
        "installed": raw.get("installed") is True,
        "version": (
            version
            if isinstance(version, str) and _PUBLIC_RUNTIME_COMPONENT.fullmatch(version)
            else None
        ),
        "buildTimestamp": build_timestamp,
        "platform": (
            platform_key
            if isinstance(platform_key, str) and _PUBLIC_RUNTIME_COMPONENT.fullmatch(platform_key)
            else None
        ),
        "artifactKind": (
            artifact_kind
            if isinstance(artifact_kind, str) and _PUBLIC_RUNTIME_COMPONENT.fullmatch(artifact_kind)
            else None
        ),
        "capabilities": (
            [
                capability
                for capability in capabilities
                if isinstance(capability, str) and capability in allowed_capabilities
            ]
            if isinstance(capabilities, list)
            else []
        ),
        "source": "plugin-bundled" if source == "plugin-bundled" else None,
    }
    release_version = raw.get("releaseVersion")
    release_match = (
        _NATIVE_ALPHA_RELEASE_VERSION.fullmatch(release_version)
        if isinstance(release_version, str)
        else None
    )
    if (
        raw.get("installed") is True
        and source == "plugin-bundled"
        and isinstance(platform_key, str)
        and platform_key in PLATFORM_RUNTIME_SPECS
        and release_match is not None
        and isinstance(release_version, str)
        and isinstance(version, str)
        and (
            version
            in {
                ".".join(release_match.group(index) for index in (1, 2, 3)),
                release_version,
            }
            or platform_key.startswith("windows-")
            and version == "plugin-bundled"
        )
    ):
        projected["releaseVersion"] = release_version
    updated = raw.get("updated")
    if isinstance(updated, bool):
        projected["updated"] = updated
    launching = raw.get("launching")
    if isinstance(launching, bool):
        projected["launching"] = launching
    if raw.get("updateError") == _PUBLIC_RUNTIME_UPDATE_ERROR:
        projected["updateError"] = _PUBLIC_RUNTIME_UPDATE_ERROR
    return projected


@dataclass(frozen=True)
class E2EIsolation:
    """Private roots passed to one permission-free companion proof.

    This is intentionally unavailable unless the explicit E2E bit is set.
    The normal MCP/runtime path never accepts an arbitrary HOME or native
    Application Support override from its environment.
    """

    root: Path
    home: Path
    codex_home: Path
    native_root: Path
    control_root: Path
    temp_root: Path
    required_codex_launch_context: tuple[str, str] | None = None

    def child_environment(
        self,
        *,
        capture_mode: str | None = None,
    ) -> dict[str, str]:
        """Return a tiny allowlist instead of inheriting credentials."""

        if capture_mode not in {None, E2E_DETERMINISTIC_CAPTURE_MODE}:
            raise NativeRuntimeError("E2E capture mode is invalid")

        environment = {
            "PATH": "/usr/bin:/bin:/usr/sbin:/sbin",
            "HOME": str(self.home),
            "CFFIXED_USER_HOME": str(self.home),
            "CODEX_HOME": str(self.codex_home),
            "TMPDIR": f"{self.temp_root}/",
            E2E_ISOLATED_ENV: "1",
            CODEX_E2E_ISOLATED_ENV: "1",
            LEGACY_CODEX_E2E_ISOLATED_ENV: "1",
            E2E_ROOT_ENV: str(self.root),
            E2E_NATIVE_ROOT_ENV: str(self.native_root),
            "CHATGPT_MEETINGS_E2E_SUPPRESS_BOOTSTRAP": "1",
            "CHATGPT_MEETINGS_CONTROL_ROOT": str(self.control_root),
        }
        for key in ("LANG", "LC_ALL", "__CF_USER_TEXT_ENCODING"):
            value = os.environ.get(key)
            if value:
                environment[key] = value
        if capture_mode is not None:
            environment[E2E_CAPTURE_MODE_ENV] = capture_mode
        if self.required_codex_launch_context is not None:
            context = _validated_codex_launch_context(platform="macos")
            if context is None or context != self.required_codex_launch_context:
                raise NativeRuntimeError("required Codex launch context changed or is unavailable")
            cli_path, codex_home = context
            if codex_home != str(self.codex_home) or not Path(cli_path).is_relative_to(self.root):
                raise NativeRuntimeError("required Codex launch context is outside E2E isolation")
            # This is a private fixture helper, never an ambient user CLI or
            # credential path. Preserve the exact helper through the exec gate.
            environment["CODEX_BIN"] = cli_path
            environment["CODEX_CLI_PATH"] = cli_path
        return environment


def windows_companion_environment(
    source: Mapping[str, str] | None = None,
) -> dict[str, str]:
    """Return the Windows paths and CA settings required by the native companion.

    The detached companion resolves its own Codex authentication from validated
    executable/home command-line paths. Keep the environment positive and fixed
    so credentials, proxy configuration, and test-only ChatGPT Meetings
    overrides cannot cross the process boundary.
    """

    values = os.environ if source is None else source
    return {key: value for key in WINDOWS_COMPANION_ENVIRONMENT_KEYS if (value := values.get(key))}


def darwin_companion_ca_arguments() -> list[str]:
    """Forward explicit CA settings through LaunchServices before app arguments."""

    arguments: list[str] = []
    for key in COMPANION_CA_ENVIRONMENT_KEYS:
        value = os.environ.get(key)
        if value is not None:
            arguments.extend(("--env", f"{key}={value}"))
    return arguments


@dataclass(frozen=True)
class _PluginBundleVerification:
    """One successful process-local proof for a plugin-shipped app bundle.

    Status and widget-open polls run frequently while the UI is visible. A
    full codesign --verify --deep on every one of those polls makes the first
    impression feel stuck even though the signed versioned plugin bundle has
    not changed. This cache is deliberately only a status-path acceleration:

    * it is keyed by the resolved plugin path plus identities for the bundle
      metadata, executable, helper, and signature seal;
    * failed validations are never cached;
    * launch always asks for a fresh full verification before it can hand off
      or execute anything.

    A resource changed without changing one of the cheap identities can at
    worst make a status row briefly stale in this process. It cannot authorize
    execution because launch_current bypasses this cache.
    """

    fingerprint: NativeArtifactFingerprint
    version: str
    build_timestamp: str | None
    executable_sha256: str
    stable_status_sentinel: NativeArtifactFingerprint | None = None


_PLUGIN_BUNDLE_VERIFICATION_CACHE: dict[tuple[str, str, str, bool], _PluginBundleVerification] = {}
_PLUGIN_BUNDLE_VERIFICATION_LOCK = threading.RLock()


def _darwin_runtime_spec(
    platform_key: ControlPlatformWire,
    manifest_keys: tuple[ControlPlatformWire, ...],
) -> PlatformRuntimeSpec:
    return PlatformRuntimeSpec(
        platform_key=platform_key,
        manifest_keys=manifest_keys,
        artifact_kind="macos-app-bundle",
        artifact_name=APP_NAME,
        artifact_path_kind="directory",
        identity_kind="bundleIdentifier",
        identity_value=BUNDLE_ID,
        capabilities=CONTROL_CAPABILITIES_BY_PLATFORM[platform_key],
        launch_strategy="macos-open-background",
    )


def _windows_runtime_spec(platform_key: ControlPlatformWire) -> PlatformRuntimeSpec:
    return PlatformRuntimeSpec(
        platform_key=platform_key,
        manifest_keys=(platform_key,),
        artifact_kind="windows-executable",
        artifact_name="ChatGPT Meetings.exe",
        artifact_path_kind="file",
        identity_kind="executableName",
        identity_value="ChatGPT Meetings.exe",
        capabilities=CONTROL_CAPABILITIES_BY_PLATFORM[platform_key],
        launch_strategy="windows-detached-process",
    )


PLATFORM_RUNTIME_SPECS: dict[str, PlatformRuntimeSpec] = {
    ControlPlatform.DARWIN_UNIVERSAL.value: _darwin_runtime_spec(
        ControlPlatform.DARWIN_UNIVERSAL.value, (ControlPlatform.DARWIN_UNIVERSAL.value,)
    ),
    # Prefer one honest universal artifact, then accept only the matching legacy
    # architecture key. An Intel host must never select arm64.
    ControlPlatform.DARWIN_ARM64.value: _darwin_runtime_spec(
        ControlPlatform.DARWIN_ARM64.value,
        (ControlPlatform.DARWIN_UNIVERSAL.value, ControlPlatform.DARWIN_ARM64.value),
    ),
    ControlPlatform.DARWIN_X64.value: _darwin_runtime_spec(
        ControlPlatform.DARWIN_X64.value,
        (ControlPlatform.DARWIN_UNIVERSAL.value, ControlPlatform.DARWIN_X64.value),
    ),
    ControlPlatform.WINDOWS_X64.value: _windows_runtime_spec(ControlPlatform.WINDOWS_X64.value),
    ControlPlatform.WINDOWS_ARM64.value: _windows_runtime_spec(ControlPlatform.WINDOWS_ARM64.value),
}


def _is_windows_host() -> bool:
    """Whether filesystem/launch calls are executing on Windows itself."""

    return os.name == "nt"


def _is_windows_spec(spec: PlatformRuntimeSpec) -> bool:
    return spec.platform_key in (
        ControlPlatform.WINDOWS_X64.value,
        ControlPlatform.WINDOWS_ARM64.value,
    )


def host_platform_key() -> ControlPlatformWire | None:
    """Return a feed key for a host we know how to name."""

    machine = platform.machine().lower()
    if sys.platform == "darwin" and machine in {"arm64", "aarch64"}:
        return ControlPlatform.DARWIN_ARM64.value
    if sys.platform == "darwin" and machine in {"x86_64", "amd64"}:
        return ControlPlatform.DARWIN_X64.value
    if os.name == "nt":
        # RuntimeInformation.OSArchitecture in install.ps1 selects the native
        # Windows OS architecture. A 32/64-bit emulated Codex process reports
        # its process architecture through platform.machine(), so consult the
        # native WOW64 marker first and keep install/runtime selection aligned
        # on ARM64 Windows.
        native_machine = (
            os.environ.get("PROCESSOR_ARCHITEW6432", "").strip().lower()
            or os.environ.get("PROCESSOR_ARCHITECTURE", "").strip().lower()
            or machine
        )
        if native_machine in {"amd64", "x86_64"}:
            return ControlPlatform.WINDOWS_X64.value
        if native_machine in {"arm64", "aarch64"}:
            return ControlPlatform.WINDOWS_ARM64.value
    return None


def runtime_spec_for(platform_key: str) -> PlatformRuntimeSpec:
    try:
        return PLATFORM_RUNTIME_SPECS[platform_key]
    except KeyError as exc:
        raise NativeRuntimeError(
            f"native runtime platform {platform_key!r} is unsupported"
        ) from exc


def configured_platform_spec() -> PlatformRuntimeSpec:
    """Select the host adapter, with an explicit test/future-build override.

    Windows hosts select the EXE adapter; unsupported hosts fail closed unless
    a test explicitly selects a known platform.
    """

    configured = os.environ.get(PLATFORM_OVERRIDE_ENV, "").strip()
    if configured:
        return runtime_spec_for(configured)
    detected = host_platform_key()
    if detected:
        return runtime_spec_for(detected)
    raise NativeRuntimeError("native runtime host platform is unsupported")


def _private_e2e_directory(path: Path) -> Path:
    """Create one private directory without accepting symlink traversal."""

    if not path.is_absolute() or path != Path(os.path.normpath(str(path))):
        raise NativeRuntimeError("E2E isolation root is unsafe")
    try:
        resolved_parent = path.parent.resolve(strict=True)
    except OSError as exc:
        raise NativeRuntimeError("E2E isolation root is unsafe") from exc
    if resolved_parent / path.name != path:
        raise NativeRuntimeError("E2E isolation root is unsafe")
    created = False
    try:
        path.mkdir(mode=0o700, exist_ok=False)
        created = True
    except FileExistsError:
        pass
    except OSError as exc:
        raise NativeRuntimeError("E2E isolation root is unavailable") from exc
    try:
        if created:
            os.chmod(path, 0o700)
        metadata = path.lstat()
    except OSError as exc:
        raise NativeRuntimeError("E2E isolation root is unavailable") from exc
    if (
        path.is_symlink()
        or not stat.S_ISDIR(metadata.st_mode)
        or metadata.st_uid != os.getuid()
        or stat.S_IMODE(metadata.st_mode) != 0o700
    ):
        raise NativeRuntimeError("E2E isolation root is unsafe")
    return path


def require_e2e_root_marker(root: Path) -> None:
    marker = root / E2E_ROOT_MARKER
    flags = os.O_RDONLY
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    descriptor = -1
    try:
        descriptor = os.open(marker, flags)
        metadata = os.fstat(descriptor)
        content = os.read(descriptor, len(E2E_ROOT_MARKER_CONTENT) + 1)
    except OSError as exc:
        raise NativeRuntimeError("E2E isolation root is unclaimed") from exc
    finally:
        if descriptor >= 0:
            os.close(descriptor)
    if (
        not stat.S_ISREG(metadata.st_mode)
        or metadata.st_uid != os.getuid()
        or stat.S_IMODE(metadata.st_mode) != 0o600
        or metadata.st_size != len(E2E_ROOT_MARKER_CONTENT)
        or content != E2E_ROOT_MARKER_CONTENT
    ):
        raise NativeRuntimeError("E2E isolation root is unclaimed")


def configured_e2e_isolation() -> E2EIsolation | None:
    """Resolve the dev/E2E-only private state tree, or stay on production paths.

    The one accepted input is a private absolute proof root. HOME, CODEX_HOME,
    the native state root, and the control root are derived under it so a
    caller cannot point one surface back at a user's real state.
    """

    if os.environ.get(E2E_ISOLATED_ENV) != "1":
        return None
    if allow_unsigned_test_app():
        raise NativeRuntimeError("E2E isolation requires a signed native app")
    if fcntl is None or not hasattr(os, "getuid"):
        raise NativeRuntimeError("POSIX E2E isolation is unavailable on Windows")
    configured = os.environ.get(E2E_ROOT_ENV, "").strip()
    if not configured:
        raise NativeRuntimeError("E2E isolation root is required")
    configured_root = Path(configured).expanduser()
    if not configured_root.is_absolute() or configured_root.is_symlink():
        raise NativeRuntimeError("E2E isolation root is unsafe")
    try:
        canonical_root = configured_root.resolve(strict=False)
    except OSError as exc:
        raise NativeRuntimeError("E2E isolation root is unsafe") from exc
    if not canonical_root.is_dir():
        raise NativeRuntimeError("E2E isolation root is unclaimed")
    require_e2e_root_marker(canonical_root)
    root = _private_e2e_directory(canonical_root)
    home = _private_e2e_directory(root / "home")
    codex_home = _private_e2e_directory(root / "codex-home")
    native_root = _private_e2e_directory(root / "native")
    control_root = _private_e2e_directory(native_root / "LocalMeetingsControl")
    temp_root = _private_e2e_directory(root / "tmp")
    return E2EIsolation(
        root=root,
        home=home,
        codex_home=codex_home,
        native_root=native_root,
        control_root=control_root,
        temp_root=temp_root,
    )


def configured_e2e_capture_mode(
    isolation: E2EIsolation | None,
) -> str | None:
    """Accept the fake selector only inside a fully validated isolation."""

    if isolation is None:
        return None
    value = os.environ.get(E2E_CAPTURE_MODE_ENV, "").strip()
    if not value:
        return None
    if value != E2E_DETERMINISTIC_CAPTURE_MODE:
        raise NativeRuntimeError("E2E capture mode is invalid")
    return value


def allow_unsigned_test_app() -> bool:
    return os.environ.get("CHATGPT_MEETINGS_NATIVE_ALLOW_UNSIGNED") == "1"


def _valid_authenticode_identity(subject: object, thumbprint: object) -> bool:
    return (
        isinstance(subject, str)
        and bool(subject)
        and len(subject.encode("utf-8")) <= 512
        and not any(ord(character) < 0x20 or ord(character) == 0x7F for character in subject)
        and isinstance(thumbprint, str)
        and re.fullmatch(r"[0-9A-Fa-f]{40}", thumbprint) is not None
    )


def _load_app_metadata(
    app_path: Path,
    spec: PlatformRuntimeSpec | None = None,
) -> tuple[dict[str, object], Path, Path]:
    """Read the cheap structural proof shared by status and full validation."""

    selected_spec = spec or configured_platform_spec()
    if not selected_spec.platform_key.startswith("darwin-"):
        raise NativeRuntimeError(
            f"native runtime adapter for {selected_spec.platform_key} is not implemented"
        )
    info_path = app_path / "Contents" / "Info.plist"
    try:
        with info_path.open("rb") as handle:
            info = plistlib.load(handle)
    except (OSError, plistlib.InvalidFileException) as exc:
        raise NativeRuntimeResourceError(
            NativeRuntimeResourceOperation.READ_BUNDLE_METADATA
        ) from exc
    if not isinstance(info, dict) or info.get("CFBundleIdentifier") != selected_spec.identity_value:
        raise NativeRuntimeError("native app bundle identifier does not match")
    executable_name = info.get("CFBundleExecutable")
    if not isinstance(executable_name, str) or not executable_name:
        raise NativeRuntimeError("native app executable metadata is missing")
    executable = app_path / "Contents" / "MacOS" / executable_name
    helper = app_path / "Contents" / "Resources" / "native" / "system_audio_capture"
    if not executable.is_file() or not os.access(executable, os.X_OK):
        raise NativeRuntimeError("native app executable is missing")
    if not helper.is_file() or not os.access(helper, os.X_OK):
        raise NativeRuntimeError("native system audio helper is missing")
    for key in ("NSMicrophoneUsageDescription", "NSAudioCaptureUsageDescription"):
        value = info.get(key)
        if not isinstance(value, str) or not value.strip():
            raise NativeRuntimeError(f"native app is missing {key}")
    return dict(info), executable, helper


def _load_windows_executable(
    executable_path: Path,
    spec: PlatformRuntimeSpec | None = None,
) -> Path:
    """Validate the cheap structural identity for a Windows companion."""

    selected_spec = spec or configured_platform_spec()
    if not _is_windows_spec(selected_spec):
        raise NativeRuntimeError(
            f"native runtime adapter for {selected_spec.platform_key} is not implemented"
        )
    if (
        executable_path.is_symlink()
        or not executable_path.is_file()
        or executable_path.name != selected_spec.identity_value
    ):
        raise NativeRuntimeError("native executable identity does not match")
    expected_machine = {
        "windows-x64": 0x8664,  # IMAGE_FILE_MACHINE_AMD64
        "windows-arm64": 0xAA64,  # IMAGE_FILE_MACHINE_ARM64
    }[selected_spec.platform_key]
    if _windows_pe_machine(executable_path) != expected_machine:
        raise NativeRuntimeError("native executable architecture does not match platform")
    return executable_path


def _require_darwin_macho_architecture(
    executable_path: Path,
    spec: PlatformRuntimeSpec,
) -> None:
    """Require one real thin/fat Mach-O slice for the selected Darwin host."""

    expected_cpu = DARWIN_MACHO_CPU_TYPES.get(spec.platform_key)
    if expected_cpu is None:
        # The explicit universal test/local profile predates host-slice
        # selection. Production host_platform_key always resolves arm64/x64.
        return
    try:
        with executable_path.open("rb") as handle:
            file_size = os.fstat(handle.fileno()).st_size
            prefix = handle.read(8)
            if len(prefix) != 8:
                raise NativeRuntimeError("native app Mach-O header is malformed")
            magic = prefix[:4]
            if magic == b"\xcf\xfa\xed\xfe":
                if file_size < 32:
                    raise NativeRuntimeError("native app Mach-O header is malformed")
                cpu_type = int.from_bytes(prefix[4:8], "little")
                if cpu_type != expected_cpu:
                    raise NativeRuntimeError(
                        "native app executable architecture does not match platform"
                    )
                return
            if magic not in {b"\xca\xfe\xba\xbe", b"\xca\xfe\xba\xbf"}:
                raise NativeRuntimeError("native app Mach-O header is malformed")
            is_fat64 = magic == b"\xca\xfe\xba\xbf"
            count = int.from_bytes(prefix[4:8], "big")
            entry_size = 32 if is_fat64 else 20
            table_end = 8 + count * entry_size
            if count <= 0 or count > MAXIMUM_DARWIN_MACHO_SLICES or table_end > file_size:
                raise NativeRuntimeError("native app Mach-O architecture table is malformed")
            entries = handle.read(count * entry_size)
            if len(entries) != count * entry_size:
                raise NativeRuntimeError("native app Mach-O architecture table is malformed")
            matching_slices: list[tuple[int, int]] = []
            for index in range(count):
                entry = entries[index * entry_size : (index + 1) * entry_size]
                cpu_type = int.from_bytes(entry[:4], "big")
                if is_fat64:
                    offset = int.from_bytes(entry[8:16], "big")
                    size = int.from_bytes(entry[16:24], "big")
                else:
                    offset = int.from_bytes(entry[8:12], "big")
                    size = int.from_bytes(entry[12:16], "big")
                if offset < table_end or size < 32 or offset > file_size - size:
                    raise NativeRuntimeError("native app Mach-O architecture slice is malformed")
                if cpu_type == expected_cpu:
                    matching_slices.append((offset, size))
            if len(matching_slices) != 1:
                raise NativeRuntimeError(
                    "native app executable architecture does not match platform"
                )
            offset, _size = matching_slices[0]
            handle.seek(offset)
            selected_header = handle.read(8)
            if (
                len(selected_header) != 8
                or selected_header[:4] != b"\xcf\xfa\xed\xfe"
                or int.from_bytes(selected_header[4:8], "little") != expected_cpu
            ):
                raise NativeRuntimeError("native app Mach-O architecture slice is malformed")
    except NativeRuntimeError:
        raise
    except OSError as exc:
        raise NativeRuntimeError("native app executable architecture is unavailable") from exc


def _windows_pe_machine(executable_path: Path) -> int:
    """Read the bounded DOS/PE prefix needed to bind an EXE to its CPU."""

    try:
        with executable_path.open("rb") as handle:
            file_size = os.fstat(handle.fileno()).st_size
            dos_header = handle.read(64)
            if len(dos_header) != 64 or dos_header[:2] != b"MZ":
                raise NativeRuntimeError("native executable PE header is malformed")
            pe_offset = int.from_bytes(dos_header[0x3C:0x40], "little")
            if pe_offset < 64 or pe_offset > file_size - 6:
                raise NativeRuntimeError("native executable PE header is malformed")
            handle.seek(pe_offset)
            pe_prefix = handle.read(6)
    except OSError as exc:
        raise NativeRuntimeError("native executable identity is unavailable") from exc
    if len(pe_prefix) != 6 or pe_prefix[:4] != b"PE\x00\x00":
        raise NativeRuntimeError("native executable PE header is malformed")
    return int.from_bytes(pe_prefix[4:6], "little")


def _version_from_info(info: Mapping[str, object]) -> str:
    for key in ("CFBundleShortVersionString", "CFBundleVersion"):
        value = info.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    # The bundle is still identity/signature checked by validate_app. Older
    # local fixtures did not stamp a marketing version, so keep their status
    # useful without inventing a version from an untrusted path.
    return "plugin-bundled"


def _plugin_bundle_version(info: Mapping[str, object], app_path: Path) -> str:
    """Recover the full alpha version only when signed build fields agree."""

    version = _version_from_info(info)
    match = re.fullmatch(
        r"([0-9]+\.[0-9]+\.[0-9]+)-alpha\.([1-9][0-9]*)",
        app_path.parent.name,
    )
    if match is None:
        return version
    build = info.get("CFBundleVersion")
    if version == match.group(1) and str(build) == match.group(2):
        return match.group(0)
    return version


def _plugin_bundle_release_version(info: Mapping[str, object]) -> str | None:
    """Expose a signed alpha label only when all stamped bundle fields agree."""

    release_version = info.get("ChatGPTMeetingsVersion")
    marketing_version = info.get("CFBundleShortVersionString")
    build_number = info.get("CFBundleVersion")
    if (
        not isinstance(release_version, str)
        or not isinstance(marketing_version, str)
        or not isinstance(build_number, str)
    ):
        return None
    match = _NATIVE_ALPHA_RELEASE_VERSION.fullmatch(release_version)
    if (
        match is None
        or marketing_version != ".".join(match.group(index) for index in (1, 2, 3))
        or build_number != match.group(4)
    ):
        return None
    return release_version


def _build_timestamp_from_info(info: Mapping[str, object]) -> str | None:
    return safe_build_timestamp_utc(info.get("ChatGPTMeetingsBuildTimestampUTC"))


from native_runtime_artifacts import (
    _framework_entry_identity as _framework_entry_identity,
)
from native_runtime_artifacts import (
    _native_build_receipt_path as _native_build_receipt_path,
)
from native_runtime_artifacts import (
    _optional_path_identity as _optional_path_identity,
)
from native_runtime_artifacts import (
    _path_identity as _path_identity,
)
from native_runtime_artifacts import (
    _plugin_bundle_cross_process_lock as _plugin_bundle_cross_process_lock,
)
from native_runtime_artifacts import (
    _plugin_bundle_fingerprint as _plugin_bundle_fingerprint,
)
from native_runtime_artifacts import (
    _plugin_executable_file_identity as _plugin_executable_file_identity,
)
from native_runtime_artifacts import (
    _plugin_executable_path as _plugin_executable_path,
)
from native_runtime_artifacts import (
    _plugin_framework_identities as _plugin_framework_identities,
)
from native_runtime_artifacts import (
    _plugin_resource_identities as _plugin_resource_identities,
)
from native_runtime_artifacts import (
    _plugin_verification_cache_key as _plugin_verification_cache_key,
)
from native_runtime_artifacts import (
    _read_strict_local_json as _read_strict_local_json,
)
from native_runtime_artifacts import (
    _regular_file_identity_timestamp_matches as _regular_file_identity_timestamp_matches,
)
from native_runtime_artifacts import (
    _require_windows_safe_artifact_path as _require_windows_safe_artifact_path,
)
from native_runtime_artifacts import (
    _stable_artifact_status_sentinel as _stable_artifact_status_sentinel,
)
from native_runtime_artifacts import (
    _verified_cam_distribution_manifest as _verified_cam_distribution_manifest,
)
from native_runtime_artifacts import (
    _windows_executable_launch_guard as _windows_executable_launch_guard,
)
from native_runtime_artifacts import (
    _windows_plugin_runtime_descriptor_path as _windows_plugin_runtime_descriptor_path,
)
from native_runtime_artifacts import (
    _windows_plugin_verification_manifest as _windows_plugin_verification_manifest,
)
from native_runtime_artifacts import (
    _windows_production_lock_asset_is_valid as _windows_production_lock_asset_is_valid,
)
from native_runtime_artifacts import (
    _windows_production_verification_manifest as _windows_production_verification_manifest,
)
from native_runtime_artifacts import (
    _windows_registration_launch_guard as _windows_registration_launch_guard,
)
from native_runtime_artifacts import (
    _windows_write_delete_launch_guard as _windows_write_delete_launch_guard,
)
from native_runtime_artifacts import (
    restore_plugin_framework_symlinks as restore_plugin_framework_symlinks,
)
from native_runtime_artifacts import (
    sha256_regular_file as sha256_regular_file,
)
from native_runtime_artifacts import (
    uses_production_windows_bundle as uses_production_windows_bundle,
)
from native_runtime_artifacts import (
    validate_app as validate_app,
)
from native_runtime_artifacts import (
    validate_handoff_app as validate_handoff_app,
)
from native_runtime_stable import (
    _activate_stable_generation as _activate_stable_generation,
)
from native_runtime_stable import (
    _cleanup_stable_runtime_generations as _cleanup_stable_runtime_generations,
)
from native_runtime_stable import (
    _fsync_stable_runtime_directory as _fsync_stable_runtime_directory,
)
from native_runtime_stable import (
    _fsync_stable_runtime_payload as _fsync_stable_runtime_payload,
)
from native_runtime_stable import (
    _materialize_stable_generation as _materialize_stable_generation,
)
from native_runtime_stable import (
    _official_cache_singleton_is_active as _official_cache_singleton_is_active,
)
from native_runtime_stable import (
    _official_cache_version_candidates as _official_cache_version_candidates,
)
from native_runtime_stable import (
    _private_runtime_directory as _private_runtime_directory,
)
from native_runtime_stable import (
    _read_active_stable_generation as _read_active_stable_generation,
)
from native_runtime_stable import (
    _read_stable_runtime_manifest as _read_stable_runtime_manifest,
)
from native_runtime_stable import (
    _require_stable_artifact_receipt as _require_stable_artifact_receipt,
)
from native_runtime_stable import (
    _require_windows_private_runtime_acl as _require_windows_private_runtime_acl,
)
from native_runtime_stable import (
    _require_windows_safe_lexical_runtime_parent as _require_windows_safe_lexical_runtime_parent,
)
from native_runtime_stable import (
    _resolve_plugin_handoff_for_launch as _resolve_plugin_handoff_for_launch,
)
from native_runtime_stable import (
    _stable_generation_artifact as _stable_generation_artifact,
)
from native_runtime_stable import (
    _stable_generation_name as _stable_generation_name,
)
from native_runtime_stable import (
    _stable_runtime_family_lock as _stable_runtime_family_lock,
)
from native_runtime_stable import (
    _stable_source_verification_manifest as _stable_source_verification_manifest,
)
from native_runtime_stable import (
    _strict_stable_runtime_manifest as _strict_stable_runtime_manifest,
)
from native_runtime_stable import (
    _validated_stable_generation_manifest as _validated_stable_generation_manifest,
)
from native_runtime_stable import (
    _validated_stable_windows_distribution_binding as _validated_stable_windows_distribution_binding,
)
from native_runtime_stable import (
    _verified_stable_artifact_metadata as _verified_stable_artifact_metadata,
)
from native_runtime_stable import (
    _windows_generation_sha256 as _windows_generation_sha256,
)
from native_runtime_stable import (
    _windows_source_licenses_sha256 as _windows_source_licenses_sha256,
)
from native_runtime_stable import (
    _windows_third_party_licenses_sha256 as _windows_third_party_licenses_sha256,
)
from native_runtime_stable import (
    _write_stable_runtime_manifest as _write_stable_runtime_manifest,
)
from native_runtime_stable import (
    plugin_artifact_path as plugin_artifact_path,
)
from native_runtime_stable import (
    plugin_cache_family_root as plugin_cache_family_root,
)
from native_runtime_stable import (
    require_canonical_plugin_registration as require_canonical_plugin_registration,
)
from native_runtime_stable import (
    stable_runtime_artifact_root as stable_runtime_artifact_root,
)
from native_runtime_stable import (
    stable_runtime_root as stable_runtime_root,
)
from native_runtime_stable import (
    stable_runtime_verification_manifest as stable_runtime_verification_manifest,
)


def process_start_identity(pid: int) -> tuple[int, int]:
    """Read one live process birth identity through its existing verified seam."""

    return _process_start_identity(pid)


def _reap_exited_windows_pending_children_locked() -> None:
    for key, entry in list(_WINDOWS_PENDING_CHILDREN.items()):
        if entry.process.poll() is None:
            continue
        _WINDOWS_PENDING_CHILDREN.pop(key, None)


def _require_windows_owner_matches_verified_image(
    app_path: str,
    family_root: Path,
    executable_sha256: str,
) -> None:
    """Reject a live same-path child that belongs to another verified image."""

    expected_path = str(Path(app_path))
    expected_family = str(family_root)
    with _WINDOWS_PENDING_CHILDREN_LOCK:
        _reap_exited_windows_pending_children_locked()
        conflicts = any(
            key_path == expected_path
            and key_family == expected_family
            and key_sha256 != executable_sha256
            for key_path, key_family, key_sha256 in _WINDOWS_PENDING_CHILDREN
        )
    if conflicts:
        raise NativeRuntimeLaunchPending(
            "authenticated Windows owner cannot be bound to the freshly verified image"
        )


def _claim_or_spawn_windows_pending_child(
    key: _WindowsPendingChildKey,
    app_path: str,
    authorize_spawn: Callable[[], None],
    *,
    environment: Mapping[str, str],
    creation_flags: int | None,
    required_codex_launch_context: tuple[str, str] | None = None,
) -> _WindowsPendingChild:
    """Claim one exact child observer or spawn it under a bounded registry."""

    key_app_path, _key_family_root, expected_executable_sha256 = key
    if app_path != key_app_path:
        raise NativeRuntimeError("Windows pending child identity does not match")
    with _WINDOWS_PENDING_CHILDREN_LOCK:
        _reap_exited_windows_pending_children_locked()
        entry = _WINDOWS_PENDING_CHILDREN.get(key)
        if entry is not None:
            if (
                required_codex_launch_context is not None
                and entry.codex_launch_context != required_codex_launch_context
            ):
                raise NativeRuntimeLaunchPending(
                    "pending ChatGPT Meetings launch has different Codex context"
                )
            if required_codex_launch_context is not None:
                _windows_codex_launch_arguments(
                    required_codex_launch_context=required_codex_launch_context
                )
            if entry.observing:
                raise NativeRuntimeLaunchPending(
                    "ChatGPT Meetings launch is already being observed"
                )
            entry.observing = True
            return entry
        if len(_WINDOWS_PENDING_CHILDREN) >= _MAXIMUM_WINDOWS_PENDING_CHILDREN:
            raise NativeRuntimeLaunchPending(
                "ChatGPT Meetings pending launch capacity is unavailable"
            )
        # Handoff resolution may block while another owner exits. Revalidate
        # canonical activation under the same registry lock that admits the
        # only local Popen, immediately before creating a new process.
        authorize_spawn()
        codex_arguments = (
            _windows_codex_launch_arguments(
                required_codex_launch_context=required_codex_launch_context
            )
            if required_codex_launch_context is not None
            else _windows_codex_launch_arguments()
        )
        arguments = [
            app_path,
            "--expected-executable-sha256",
            expected_executable_sha256,
            *codex_arguments,
        ]
        if creation_flags is not None:
            process = subprocess.Popen(
                arguments,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                env=environment,
                creationflags=creation_flags,
            )
        else:
            # Test/future-build overrides can exercise the portable branch on
            # non-Windows hosts without passing a Windows-only creation flag.
            process = subprocess.Popen(
                arguments,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                env=environment,
                start_new_session=True,
            )
        entry = _WindowsPendingChild(
            process=process,
            observing=True,
            codex_launch_context=required_codex_launch_context,
        )
        _WINDOWS_PENDING_CHILDREN[key] = entry
        return entry


def _release_windows_pending_child_observer(
    key: _WindowsPendingChildKey,
    entry: _WindowsPendingChild,
    *,
    keep_if_alive: bool,
) -> None:
    with _WINDOWS_PENDING_CHILDREN_LOCK:
        if _WINDOWS_PENDING_CHILDREN.get(key) is not entry:
            return
        return_code = entry.process.poll()
        if keep_if_alive and return_code is None:
            entry.observing = False
            return
        _WINDOWS_PENDING_CHILDREN.pop(key, None)


from native_runtime_manager import RuntimeManager as RuntimeManager


def main(argv: Sequence[str]) -> int:
    """Dispatch a native-runtime test gate.

    Args:
        argv: Command-line arguments after the executable name.

    Returns:
        The selected gate's exit status, or 64 for unsupported arguments.
    """

    if argv and argv[0] == E2E_COMPANION_EXEC_GATE_ARGUMENT:
        return _e2e_companion_exec_gate(list(argv[1:]))
    if argv and argv[0] == E2E_STDIO_EXEC_GATE_ARGUMENT:
        return _e2e_stdio_exec_gate(list(argv[1:]))
    return 64


_CodexLaunchContextUnavailableReason = Literal[
    "configured_path_unsupported",
    "helper_unavailable",
    "helper_launcher_manifest",
    "helper_metadata_unavailable",
    "helper_not_regular",
    "helper_not_executable",
    "home_unavailable",
    "context_not_absolute",
    "resolved_path_unsupported",
]


def _validated_codex_launch_context(
    *, platform: Literal["windows", "macos"]
) -> tuple[str, str] | None:
    """Resolve bounded executable/home context without forwarding credentials."""

    # control_client imports native_runtime, while codex_auth_client imports
    # control_client. Keep this reverse edge local so module initialization
    # cannot create a cycle. Resolving the helper only inspects it; it never
    # executes a candidate while the native companion is starting.
    from codex_auth_client import (
        CodexAuthError,
        _active_codex_home,
        _is_macos_dotslash_path,
        _resolve_codex_path,
    )

    def unavailable(reason: _CodexLaunchContextUnavailableReason) -> None:
        # This resolver runs only while preparing a native launch. Never attach
        # a path or caught exception: either can contain credential material.
        log_native_runtime_event(
            "codex_launch_context", "unavailable", platform=platform, reason=reason
        )

    reason: _CodexLaunchContextUnavailableReason = "configured_path_unsupported"
    try:
        configured_home = os.environ.get("CODEX_HOME", "")
        raw_context_paths = (
            os.environ.get("CODEX_BIN", ""),
            os.environ.get("CODEX_CLI_PATH", ""),
            configured_home,
        )
        if any(
            len(value.encode("utf-8")) > 4096
            or value != value.strip()
            or any(
                ord(character) < 32 or 127 <= ord(character) <= 159 or character in "\u2028\u2029"
                for character in value
            )
            for value in raw_context_paths
        ):
            return unavailable("configured_path_unsupported")

        reason = "helper_unavailable"
        candidate = _resolve_codex_path(None, prefer_platform_helpers=True)
        if sys.platform == "darwin" and _is_macos_dotslash_path(candidate):
            return unavailable("helper_launcher_manifest")
        reason = "helper_metadata_unavailable"
        cli_path = Path(candidate).expanduser().resolve(strict=True)
        metadata = cli_path.stat()
        if not stat.S_ISREG(metadata.st_mode):
            return unavailable("helper_not_regular")
        if not os.access(cli_path, os.X_OK):
            return unavailable("helper_not_executable")

        reason = "home_unavailable"
        codex_home = _active_codex_home(configured_home or None)
    except (AttributeError, CodexAuthError, OSError, RuntimeError, ValueError):
        return unavailable(reason)

    cli_value = str(cli_path)
    home_value = str(codex_home)
    if not cli_path.is_absolute() or not codex_home.is_absolute():
        return unavailable("context_not_absolute")
    try:
        unsafe_resolved_path = any(
            len(value.encode("utf-8")) > 4096
            or value != value.strip()
            or any(
                ord(character) < 32 or 127 <= ord(character) <= 159 or character in "\u2028\u2029"
                for character in value
            )
            for value in (cli_value, home_value)
        )
    except UnicodeError:
        return unavailable("resolved_path_unsupported")
    if unsafe_resolved_path:
        return unavailable("resolved_path_unsupported")
    return cli_value, home_value


def _windows_codex_launch_arguments(
    *, required_codex_launch_context: tuple[str, str] | None = None
) -> list[str]:
    """Give the Windows companion validated context for its own auth owner."""

    if sys.platform != "win32" and os.name != "nt":
        if required_codex_launch_context is not None:
            raise NativeRuntimeError("required Codex launch context is unavailable")
        return []
    context = _validated_codex_launch_context(platform="windows")
    if required_codex_launch_context is not None and context != required_codex_launch_context:
        raise NativeRuntimeError("required Codex launch context changed or is unavailable")
    if context is None:
        return []
    cli_value, home_value = context
    log_native_runtime_event("codex_launch_context", "available", platform="windows")
    return ["--codex-cli-path", cli_value, "--codex-home", home_value]


def _darwin_codex_launch_arguments(
    *, required_codex_launch_context: tuple[str, str] | None = None
) -> list[str]:
    """Carry only validated initiating-Codex context across LaunchServices."""

    if sys.platform != "darwin":
        if required_codex_launch_context is not None:
            raise NativeRuntimeError("required Codex launch context is unavailable")
        return []
    context = _validated_codex_launch_context(platform="macos")
    if required_codex_launch_context is not None and context != required_codex_launch_context:
        raise NativeRuntimeError("required Codex launch context changed or is unavailable")
    if context is None:
        return []
    cli_value, home_value = context
    launcher_pid = os.getppid()
    if not 0 < launcher_pid <= 2_147_483_647:
        log_native_runtime_event(
            "codex_launch_context",
            "unavailable",
            platform="macos",
            reason="launcher_pid_unavailable",
        )
        if required_codex_launch_context is not None:
            raise NativeRuntimeError("required Codex launcher process is unavailable")
        return []
    log_native_runtime_event("codex_launch_context", "available", platform="macos")
    return [
        "--args",
        "--codex-cli-path",
        cli_value,
        "--codex-home",
        home_value,
        "--codex-launcher-pid",
        str(launcher_pid),
    ]
