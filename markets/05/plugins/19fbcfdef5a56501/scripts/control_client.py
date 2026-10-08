#!/usr/bin/env python3
"""Authenticated live-stream client for ChatGPT Meetings native capture."""

from __future__ import annotations

import ctypes
import errno as errno
import hashlib
import hmac
import os
import plistlib as plistlib
import re
import secrets
import shutil as shutil
import signal as signal
import stat
import subprocess as subprocess
import sys as sys
import threading
import time
from collections.abc import Callable as Callable
from collections.abc import Generator, Mapping
from contextlib import contextmanager
from pathlib import Path
from types import ModuleType
from typing import Literal, Protocol

fcntl: ModuleType | None
try:
    import fcntl as _fcntl
except ImportError:  # pragma: no cover - future Windows adapter imports.
    fcntl = None
else:
    fcntl = _fcntl

import control_client_handoff as _control_client_handoff
import control_client_retention as _control_client_retention
from companion_control_v2 import is_recording_completion
from control_projection import (
    CONTROL_CAPABILITIES as CONTROL_CAPABILITIES,
)
from control_projection import (
    LOG_VIEWER_CAPABILITY as LOG_VIEWER_CAPABILITY,
)
from control_projection import (
    MAXIMUM_JAVASCRIPT_SAFE_INTEGER,
    SETTINGS_RECONCILIATION_CAPABILITY,
    WIDGET_PROJECTION_CAPABILITY,
    WINDOWS_PLATFORM_KEYS,
)
from control_projection import (
    SESSION_FENCED_CONTROLS_CAPABILITY as SESSION_FENCED_CONTROLS_CAPABILITY,
)
from control_projection import (
    SYNC_ATTEMPT_ID_CAPABILITY as SYNC_ATTEMPT_ID_CAPABILITY,
)
from control_projection import (
    UPDATE_HANDOFF_CAPABILITY as UPDATE_HANDOFF_CAPABILITY,
)
from control_projection import (
    UPDATE_HANDOFF_RESUMABLE_OUTBOX_CAPABILITY as UPDATE_HANDOFF_RESUMABLE_OUTBOX_CAPABILITY,
)
from control_projection import (
    UPDATE_HANDOFF_RESUMABLE_OUTBOX_V2_CAPABILITY as UPDATE_HANDOFF_RESUMABLE_OUTBOX_V2_CAPABILITY,
)
from control_projection import (
    UPDATE_HANDOFF_WORK_FENCE_CAPABILITY as UPDATE_HANDOFF_WORK_FENCE_CAPABILITY,
)
from control_projection import (
    sanitize_control_payload as sanitize_control_payload,
)
from control_protocol import (
    SAFE_CACHED_LAUNCHING_MESSAGE as SAFE_CACHED_LAUNCHING_MESSAGE,
)
from control_protocol import (
    SAFE_LAUNCHING_MESSAGE as SAFE_LAUNCHING_MESSAGE,
)
from control_protocol import (
    SAFE_LOCAL_REQUEST_FAILED_MESSAGE as SAFE_LOCAL_REQUEST_FAILED_MESSAGE,
)
from control_protocol import (
    SAFE_LOCAL_UNAVAILABLE_MESSAGE as SAFE_LOCAL_UNAVAILABLE_MESSAGE,
)
from control_protocol import (
    SAFE_QUIT_REQUIRED_MESSAGE as SAFE_QUIT_REQUIRED_MESSAGE,
)
from control_protocol import (
    SAFE_START_OWNER_CHANGED_MESSAGE as SAFE_START_OWNER_CHANGED_MESSAGE,
)
from control_protocol import (
    SAFE_UPDATE_DEFERRED_MESSAGE as SAFE_UPDATE_DEFERRED_MESSAGE,
)
from control_protocol import (
    ControlConnectionUnavailable,
    ControlEndpointRejected,
    ControlUnavailable,
    connecting_state,
    normalize_action_arguments,
)
from control_protocol import (
    normalize_arguments as normalize_arguments,
)
from control_transport.discovery import (
    StreamDiscovery,
    discover_transport,
    require_stream_owner,
)
from control_transport.status_cache import native_status_cache
from control_transport.stream import StreamTransport
from control_windows_identity import (
    require_windows_owner_process_image as _verify_windows_owner_process_image,  # noqa: F401
)
from control_windows_identity import (
    windows_pid_is_proven_dead as _windows_pid_is_proven_dead,
)
from meetings_sentry import plugin_version as installed_plugin_version
from native_runtime import (
    APP_NAME as APP_NAME,
)
from native_runtime import (
    APP_SUPPORT_DIRECTORY_NAME,
    ControlCapability,
    RuntimeManager,
)
from native_runtime import (
    BUNDLE_ID as BUNDLE_ID,
)
from native_runtime import (
    OFFICIAL_CACHE_PUBLISHERS as OFFICIAL_CACHE_PUBLISHERS,
)
from native_runtime import (
    SHA256_HEX_PATTERN as _SHA256_HEX_PATTERN,
)
from native_runtime import (
    NativeRuntimeError as NativeRuntimeError,
)
from native_runtime import (
    PlatformRuntimeSpec as PlatformRuntimeSpec,
)
from native_runtime import (
    log_native_runtime_event as log_native_runtime_event,
)
from native_runtime import (
    plugin_artifact_path as plugin_artifact_path,
)
from native_runtime import (
    plugin_cache_family_root as plugin_cache_family_root,
)
from native_runtime import (
    require_canonical_plugin_registration as require_canonical_plugin_registration,
)
from native_runtime import (
    runtime_spec_for as runtime_spec_for,
)
from native_runtime import (
    sha256_regular_file as sha256_regular_file,
)
from native_runtime import (
    stable_runtime_directory_name as stable_runtime_directory_name,
)
from native_runtime import (
    stable_runtime_verification_manifest as stable_runtime_verification_manifest,
)
from native_runtime import (
    validate_handoff_app as validate_handoff_app,
)
from recording_control_action_contract import (
    ControlAction,
    ControlActionArguments,
    ControlPlatform,
    parse_control_action,
    parse_control_platform,
)
from recording_control_stream_contract import (
    ControlStreamDescriptor,
    is_control_stream_descriptor,
)
from recording_status_contract import (
    RecordingHeadlessSyncStatus,
    RecordingUploadPhase,
)
from runtime_config import RUNTIME_CONFIG

from helpers import is_json, is_json_array, parse_bounded_json


class _WindowsSecurityApi(Protocol):
    def WinDLL(self, name: str, *, use_last_error: bool) -> ctypes.CDLL: ...

    def set_last_error(self, error: int) -> int: ...

    def get_last_error(self) -> int: ...


class _PosixFileApi(Protocol):
    def getuid(self) -> int: ...


RawControlDescriptor = dict[str, object]
RawControlPayload = dict[str, object]
_StreamOwnerKey = tuple[str, str, int, str]


_PROJECTION_CONTRACT_LOCK = threading.Lock()
_MAXIMUM_PROJECTION_CONTRACT_BINDINGS = 64
_PROJECTION_CONTRACT_REQUIRED_BY_BINDING: dict[tuple[str, str], dict[str, bool]] = {}
_PROJECTION_CONTRACT_HISTORY_SATURATED = False
_SETTINGS_REVISION_EPOCH_LOCK = threading.Lock()
_MAXIMUM_SETTINGS_REVISION_EPOCH_BINDINGS = 64
_SETTINGS_REVISION_EPOCH_BY_BINDING: dict[tuple[str, str], int] = {}
_NEXT_SETTINGS_REVISION_EPOCH = 1
_SETTINGS_REVISION_EPOCH_SATURATED = False
_CAPTURE_AWARE_SIGTERM_LOCK = threading.Lock()
_MAXIMUM_CAPTURE_AWARE_SIGTERM_OWNERS = 128
_CAPTURE_AWARE_SIGTERM_OWNERS: set[tuple[int, str]] = set()
DEFAULT_ROOT = (
    Path.home()
    / "Library"
    / "Application Support"
    / APP_SUPPORT_DIRECTORY_NAME
    / "LocalMeetingsControl"
)
CONTROL_APP_TARGET = RUNTIME_CONFIG.control_target
MAXIMUM_JSON_BYTES = 1 * 1024 * 1024
_STALE_OWNER_CONTROL_ACTIONS = frozenset(
    {
        ControlAction.STATUS.value,
        ControlAction.STOP.value,
        ControlAction.PAUSE.value,
        ControlAction.RESUME.value,
        ControlAction.RETRY_UPLOAD.value,
    }
)
_STREAM_TRANSPORT_LOCK = threading.RLock()
_STREAM_TRANSPORTS: dict[_StreamOwnerKey, StreamTransport] = {}
_stream_transports_shutdown = False
_STREAM_CONNECTING: set[_StreamOwnerKey] = set()
_STREAM_CONNECT_FAILURES: dict[_StreamOwnerKey, float] = {}
_STREAM_CLIENT_ID = secrets.token_urlsafe(18).replace("-", "_")
_STREAM_SEQUENCE_LOCK = threading.Lock()
_STREAM_SUBMISSION_LOCK = threading.Lock()
_stream_request_sequence = 0
_STREAM_BACKGROUND_CONNECT_SECONDS = 1.0
_STREAM_RECONNECT_COOLDOWN_SECONDS = 0.5
_STREAM_BACKGROUND_CONNECT_ATTEMPTS = 3
_QUIESCENT_START_SUCCESSOR_UPLOAD_PHASES = frozenset(
    {
        RecordingUploadPhase.IDLE.value,
        RecordingUploadPhase.UPLOADED.value,
    }
)
_QUIESCENT_HANDOFF_HEADLESS_SYNC_STATUSES = frozenset(
    {
        RecordingHeadlessSyncStatus.IDLE.value,
        RecordingHeadlessSyncStatus.DISABLED.value,
        RecordingHeadlessSyncStatus.NOT_IMPLEMENTED.value,
        RecordingHeadlessSyncStatus.COMPLETED.value,
    }
)
_DURABLE_OUTBOX_HANDOFF_UPLOAD_PHASES = frozenset(
    {
        RecordingUploadPhase.LOCAL_ONLY.value,
        RecordingUploadPhase.NEEDS_SIGN_IN.value,
        RecordingUploadPhase.NEEDS_MANUAL_RETRY.value,
    }
)
_DURABLE_OUTBOX_HANDOFF_HEADLESS_SYNC_STATUSES = frozenset(
    {
        RecordingHeadlessSyncStatus.NEEDS_ATTENTION.value,
        RecordingHeadlessSyncStatus.NEEDS_SIGN_IN.value,
    }
)
HANDOFF_RESPONSE_TIMEOUT_SECONDS = 4.0
HANDOFF_EXIT_TIMEOUT_SECONDS = 5.0
HANDOFF_OWNER_LOCK_TIMEOUT_SECONDS = 5.0
HANDOFF_OWNER_LOCK_POLL_SECONDS = 0.05
WINDOWS_ACTIVE_STATUS_TIMEOUT_SECONDS = 1.0
WINDOWS_HANDOFF_RECHECK_LIMIT = 3
OWNER_LOCK_FILENAME = "native-owner.lock"
_PLUGIN_VERSION_COMPONENT = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,79}\Z")


def _is_windows_host() -> bool:
    return os.name == "nt"


def _is_windows_platform_key(value: object) -> bool:
    """Whether a descriptor/runtime key names a supported Windows build."""

    return isinstance(value, str) and value in WINDOWS_PLATFORM_KEYS


def default_control_root() -> Path:
    """Return the per-user native bridge root for the current host."""

    if _is_windows_host():
        local_app_data = os.environ.get("LOCALAPPDATA", "").strip()
        base = Path(local_app_data) if local_app_data else Path.home() / "AppData" / "Local"
        return base / APP_SUPPORT_DIRECTORY_NAME / "LocalMeetingsControl"
    return DEFAULT_ROOT


class CooperativeHandoffRequired(ControlUnavailable):
    """A proven older companion predates the authenticated quit capability."""


class CooperativeHandoffDeclined(CooperativeHandoffRequired):
    """A proven cooperative companion is busy and may safely yield later."""

    def __init__(
        self,
        message: str,
        *,
        recovery_blocker: Literal[
            "cooperative-handoff-declined",
            "active-or-unfinished-capture",
            "ambiguous-start",
            "capture-or-recovery-in-progress",
            "owner-responded-during-recovery",
            "compatible-replacement-unavailable",
            "terminal-bootstrap-not-quiescent",
            "recent-audio-activity",
            "audio-activity-unavailable",
        ] = "cooperative-handoff-declined",
    ) -> None:
        super().__init__(message)
        self.recovery_blocker = recovery_blocker


class _DescriptorChanged(ControlUnavailable):
    """The descriptor changed across one bounded ownership observation."""


class _ControlRequestTimedOut(ControlUnavailable):
    """An authenticated request received no response before its deadline."""

    def __init__(self, message: str, *, request_dispatched: bool = False) -> None:
        super().__init__(message)
        self.request_dispatched = request_dispatched


class _HandoffExitTimedOut(ControlUnavailable):
    """An acknowledged owner retained its lease past the exit deadline."""


class _HandoffOwnerUnsettled(ControlUnavailable):
    """The status-proven owner departed or stopped responding before quit."""


def _set_projection_state(
    name: Literal[
        "_SETTINGS_REVISION_EPOCH_SATURATED",
        "_NEXT_SETTINGS_REVISION_EPOCH",
        "_PROJECTION_CONTRACT_HISTORY_SATURATED",
    ],
    value: bool | int,
) -> None:
    """Update established, externally resettable projection-state seam names."""

    setattr(sys.modules[__name__], name, value)


def _settings_revision_epoch_for_binding(
    root: Path,
    descriptor_value: ControlStreamDescriptor | RawControlDescriptor,
) -> int | None:
    """Return one opaque process-local ordinal for a verified native epoch.

    The raw native epoch is private control-plane identity and never crosses
    into MCP state. A fixed-size, non-evicting map keeps an observed binding
    stable for the life of this process. Once either the binding bound or the
    JavaScript-safe integer bound is exhausted, unknown bindings receive no
    ordinal so consumers fail closed instead of conflating two app epochs.
    """

    descriptor_epoch = descriptor_value.get("epoch")
    if not isinstance(descriptor_epoch, str) or not descriptor_epoch:
        return None
    try:
        canonical_root = str(root.resolve(strict=True))
    except (OSError, RuntimeError):
        return None
    binding = (canonical_root, descriptor_epoch)
    with _SETTINGS_REVISION_EPOCH_LOCK:
        observed = _SETTINGS_REVISION_EPOCH_BY_BINDING.get(binding)
        if observed is not None:
            return observed
        if (
            _SETTINGS_REVISION_EPOCH_SATURATED
            or len(_SETTINGS_REVISION_EPOCH_BY_BINDING) >= _MAXIMUM_SETTINGS_REVISION_EPOCH_BINDINGS
            or _NEXT_SETTINGS_REVISION_EPOCH > MAXIMUM_JAVASCRIPT_SAFE_INTEGER
        ):
            _set_projection_state("_SETTINGS_REVISION_EPOCH_SATURATED", True)
            return None
        observed = _NEXT_SETTINGS_REVISION_EPOCH
        _set_projection_state("_NEXT_SETTINGS_REVISION_EPOCH", observed + 1)
        _SETTINGS_REVISION_EPOCH_BY_BINDING[binding] = observed
        return observed


def _annotate_settings_revision_epoch(
    state: dict[str, object],
    root: Path,
    descriptor_value: ControlStreamDescriptor | RawControlDescriptor,
) -> dict[str, object]:
    """Bind a safe native settings revision to its verified app lifetime."""

    headless = state.get("headless")
    if not is_json(headless):
        return state
    settings = headless.get("settings")
    if not is_json(settings):
        return state
    revision = settings.get("revision")
    if (
        not isinstance(revision, int)
        or isinstance(revision, bool)
        or not 0 <= revision <= MAXIMUM_JAVASCRIPT_SAFE_INTEGER
    ):
        return state
    revision_epoch = _settings_revision_epoch_for_binding(root, descriptor_value)
    if revision_epoch is None:
        return state
    projected_state = dict(state)
    projected_headless = dict(headless)
    projected_settings = dict(settings)
    projected_settings["settingsRevisionEpoch"] = revision_epoch
    projected_headless["settings"] = projected_settings
    projected_state["headless"] = projected_headless
    return projected_state


def _enforce_descriptor_projection_contracts(
    state: dict[str, object],
    root: Path,
    descriptor_value: ControlStreamDescriptor | RawControlDescriptor,
) -> dict[str, object]:
    """Preserve safe descriptor-bound projections."""

    state = _annotate_settings_revision_epoch(
        state,
        root,
        descriptor_value,
    )
    epoch = descriptor_value.get("epoch")
    if (
        state.get("admissionFenced") is True
        and isinstance(epoch, str)
        and re.fullmatch(r"[A-Za-z0-9._-]{1,128}", epoch)
    ):
        state = {
            **state,
            "fenceIdentity": hashlib.sha256(f"fenced-owner-v1:{epoch}".encode()).hexdigest(),
        }
    binding = (
        str(root.resolve()),
        epoch if isinstance(epoch, str) else "",
    )
    descriptor_capabilities = descriptor_value.get("capabilities")
    descriptor_tokens: set[str] = set()
    if is_json_array(descriptor_capabilities):
        for capability in descriptor_capabilities:
            if not isinstance(capability, str):
                descriptor_tokens.clear()
                break
            descriptor_tokens.add(capability)
    headless = state.get("headless")
    public_headless: dict[str, object] = headless if is_json(headless) else {}
    headless_capabilities = public_headless.get("capabilities")
    observed_tokens: set[str] = set()
    if is_json_array(headless_capabilities):
        for capability in headless_capabilities:
            if not isinstance(capability, str):
                observed_tokens.clear()
                break
            observed_tokens.add(capability)
    with _PROJECTION_CONTRACT_LOCK:
        default_required = _PROJECTION_CONTRACT_HISTORY_SATURATED
        required = _PROJECTION_CONTRACT_REQUIRED_BY_BINDING.pop(
            binding,
            {
                SETTINGS_RECONCILIATION_CAPABILITY: default_required,
                WIDGET_PROJECTION_CAPABILITY: default_required,
            },
        )
        for capability in required:
            required[capability] |= capability in descriptor_tokens or capability in observed_tokens
        # Dict insertion order gives a dependency-free LRU. If an unusually
        # long-lived MCP process sees more epochs than the bound, forgetting
        # an evicted obligation could fail open. Saturate instead: unknown
        # future/late bindings require both fixed contracts until restart.
        _PROJECTION_CONTRACT_REQUIRED_BY_BINDING[binding] = required
        if len(_PROJECTION_CONTRACT_REQUIRED_BY_BINDING) > _MAXIMUM_PROJECTION_CONTRACT_BINDINGS:
            oldest = next(iter(_PROJECTION_CONTRACT_REQUIRED_BY_BINDING))
            del _PROJECTION_CONTRACT_REQUIRED_BY_BINDING[oldest]
            _set_projection_state("_PROJECTION_CONTRACT_HISTORY_SATURATED", True)
        required = dict(required)

    if not any(required.values()):
        return state
    projected_state = dict(state)
    projected_headless = dict(public_headless)
    projected_capabilities: list[object] = (
        list(headless_capabilities) if is_json_array(headless_capabilities) else []
    )
    for capability in (
        SETTINGS_RECONCILIATION_CAPABILITY,
        WIDGET_PROJECTION_CAPABILITY,
    ):
        if required[capability] and capability not in projected_capabilities:
            projected_capabilities.append(capability)
    projected_headless["capabilities"] = projected_capabilities
    projected_state["headless"] = projected_headless
    return projected_state


def control_root() -> Path:
    configured = os.environ.get("CHATGPT_MEETINGS_CONTROL_ROOT", "").strip()
    return Path(configured).expanduser() if configured else default_control_root()


def _windows_acl_grant_is_read_only(access_mask: int) -> bool:
    """Reject every untrusted Windows file right outside bounded read/execute."""

    # FILE_READ_DATA, FILE_READ_EA, FILE_EXECUTE, FILE_READ_ATTRIBUTES,
    # READ_CONTROL, SYNCHRONIZE, GENERIC_READ, and GENERIC_EXECUTE.
    return access_mask & ~0xA01200A9 == 0


def windows_acl_is_private(path: Path, *, allow_untrusted_read: bool = False) -> bool:
    """Check that a Windows runtime entry has only trusted ACL grants.

    Args:
        path: Runtime file or directory whose Windows ACL should be inspected.
        allow_untrusted_read: Permit read-only installer grants without granting writes.

    Returns:
        Whether only trusted principals have access or untrusted access is read-only.
    """

    if os.name != "nt":  # Unit tests can model Windows path shape on POSIX.
        return True
    windows_security: _WindowsSecurityApi = ctypes

    class AclSizeInformation(ctypes.Structure):
        _fields_ = [
            ("ace_count", ctypes.c_uint32),
            ("bytes_in_use", ctypes.c_uint32),
            ("bytes_free", ctypes.c_uint32),
        ]

    class AceHeader(ctypes.Structure):
        _fields_ = [
            ("ace_type", ctypes.c_ubyte),
            ("ace_flags", ctypes.c_ubyte),
            ("ace_size", ctypes.c_uint16),
        ]

    class SidAndAttributes(ctypes.Structure):
        _fields_ = [("sid", ctypes.c_void_p), ("attributes", ctypes.c_uint32)]

    class TokenUser(ctypes.Structure):
        _fields_ = [("user", SidAndAttributes)]

    advapi = windows_security.WinDLL("advapi32", use_last_error=True)
    kernel = windows_security.WinDLL("kernel32", use_last_error=True)
    void_pointer = ctypes.c_void_p
    pointer = ctypes.POINTER(void_pointer)
    advapi.GetNamedSecurityInfoW.argtypes = [
        ctypes.c_wchar_p,
        ctypes.c_int,
        ctypes.c_uint32,
        pointer,
        pointer,
        pointer,
        pointer,
        pointer,
    ]
    advapi.GetNamedSecurityInfoW.restype = ctypes.c_uint32
    advapi.GetAclInformation.argtypes = [
        void_pointer,
        void_pointer,
        ctypes.c_uint32,
        ctypes.c_int,
    ]
    advapi.GetAclInformation.restype = ctypes.c_int
    advapi.GetAce.argtypes = [void_pointer, ctypes.c_uint32, pointer]
    advapi.GetAce.restype = ctypes.c_int
    advapi.ConvertSidToStringSidW.argtypes = [void_pointer, pointer]
    advapi.ConvertSidToStringSidW.restype = ctypes.c_int
    advapi.OpenProcessToken.argtypes = [
        void_pointer,
        ctypes.c_uint32,
        pointer,
    ]
    advapi.OpenProcessToken.restype = ctypes.c_int
    advapi.GetTokenInformation.argtypes = [
        void_pointer,
        ctypes.c_int,
        void_pointer,
        ctypes.c_uint32,
        ctypes.POINTER(ctypes.c_uint32),
    ]
    advapi.GetTokenInformation.restype = ctypes.c_int
    kernel.GetCurrentProcess.argtypes = []
    kernel.GetCurrentProcess.restype = void_pointer
    kernel.CloseHandle.argtypes = [void_pointer]
    kernel.CloseHandle.restype = ctypes.c_int
    kernel.LocalFree.argtypes = [void_pointer]
    kernel.LocalFree.restype = void_pointer

    def sid_string(sid: int | None) -> str | None:
        if not sid:
            return None
        result = void_pointer()
        if not advapi.ConvertSidToStringSidW(void_pointer(sid), ctypes.byref(result)):
            return None
        try:
            address = result.value
            return None if address is None else ctypes.wstring_at(address)
        finally:
            kernel.LocalFree(result)

    owner = void_pointer()
    dacl = void_pointer()
    descriptor = void_pointer()
    # SE_FILE_OBJECT, OWNER_SECURITY_INFORMATION | DACL_SECURITY_INFORMATION.
    if (
        advapi.GetNamedSecurityInfoW(
            str(path),
            1,
            0x00000005,
            ctypes.byref(owner),
            None,
            ctypes.byref(dacl),
            None,
            ctypes.byref(descriptor),
        )
        != 0
    ):
        return False
    token = void_pointer()
    try:
        if not owner.value or not dacl.value:
            return False
        # TOKEN_QUERY. The first TokenUser query is the documented size probe.
        if not advapi.OpenProcessToken(kernel.GetCurrentProcess(), 0x0008, ctypes.byref(token)):
            return False
        required = ctypes.c_uint32()
        windows_security.set_last_error(0)
        queried = advapi.GetTokenInformation(token, 1, None, 0, ctypes.byref(required))
        if queried or windows_security.get_last_error() != 122 or not required.value:
            return False
        token_buffer = ctypes.create_string_buffer(required.value)
        if not advapi.GetTokenInformation(
            token,
            1,
            token_buffer,
            required.value,
            ctypes.byref(required),
        ):
            return False
        current = sid_string(ctypes.cast(token_buffer, ctypes.POINTER(TokenUser)).contents.user.sid)
        trusted_owners = {current, "S-1-5-18", "S-1-5-32-544"}
        if not current or sid_string(owner.value) not in trusted_owners:
            return False
        # OWNER RIGHTS is equivalent to the already-verified object owner and
        # is used by some per-user Windows profiles instead of an explicit SID.
        allowed = {*trusted_owners, "S-1-3-4"}
        information = AclSizeInformation()
        # AclSizeInformation. Unknown/callback/object ACEs fail closed: the
        # companion publishes only simple inheritable allow ACEs.
        if not advapi.GetAclInformation(
            dacl,
            ctypes.byref(information),
            ctypes.sizeof(information),
            2,
        ):
            return False
        for index in range(information.ace_count):
            entry = void_pointer()
            if not advapi.GetAce(dacl, index, ctypes.byref(entry)) or not entry.value:
                return False
            header = ctypes.cast(entry, ctypes.POINTER(AceHeader)).contents
            if header.ace_type == 1:  # ACCESS_DENIED_ACE_TYPE cannot disclose data.
                continue
            if header.ace_type != 0 or header.ace_size < 8:
                return False
            # ACCESS_ALLOWED_ACE stores its SID immediately after header+mask.
            if sid_string(entry.value + 8) not in allowed:
                if not allow_untrusted_read:
                    return False
                access_mask = ctypes.c_uint32.from_address(
                    entry.value + ctypes.sizeof(AceHeader)
                ).value
                if not _windows_acl_grant_is_read_only(access_mask):
                    return False
        return True
    finally:
        if token.value:
            kernel.CloseHandle(token)
        if descriptor.value:
            kernel.LocalFree(descriptor)


def require_private(path: Path, *, directory: bool) -> os.stat_result:
    try:
        metadata = path.stat()
    except OSError as exc:
        raise ControlUnavailable("native control is offline") from exc
    expected = stat.S_ISDIR if directory else stat.S_ISREG
    windows = _is_windows_host()
    reparse_point = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    try:
        unsafe_ancestor = windows and any(
            candidate.is_symlink()
            or getattr(candidate, "is_junction", lambda: False)()
            or (
                reparse_point
                and getattr(candidate.lstat(), "st_file_attributes", 0) & reparse_point
            )
            for candidate in (path, *path.parents)
        )
    except OSError as exc:
        raise ControlUnavailable("native control permissions rejected") from exc
    if path.is_symlink() or not expected(metadata.st_mode) or unsafe_ancestor:
        raise ControlUnavailable("native control permissions rejected")
    if windows and not windows_acl_is_private(path):
        raise ControlUnavailable("native control permissions rejected")
    if not windows:
        posix_files: _PosixFileApi = os
        if metadata.st_uid != posix_files.getuid() or metadata.st_mode & 0o077:
            raise ControlUnavailable("native control permissions rejected")
    return metadata


def _read_text_with_windows_share_retry(path: Path, expected: os.stat_result) -> str:
    """Read one private control file with a strict size/identity and share-retry bound."""

    deadline = time.monotonic() + 0.5
    while True:
        try:
            with path.open("rb") as source:
                opened = os.fstat(source.fileno())
                if (
                    not stat.S_ISREG(opened.st_mode)
                    or opened.st_size > MAXIMUM_JSON_BYTES
                    or opened.st_dev != expected.st_dev
                    or (opened.st_ino and expected.st_ino and opened.st_ino != expected.st_ino)
                ):
                    raise ControlUnavailable("native control file changed while reading")
                data = source.read(MAXIMUM_JSON_BYTES + 1)
            if len(data) > MAXIMUM_JSON_BYTES:
                raise ControlUnavailable("native control file is too large")
            return data.decode("utf-8")
        except PermissionError:
            if not _is_windows_host() or time.monotonic() >= deadline:
                raise
            time.sleep(0.01)


def read_json(path: Path) -> dict[str, object]:
    metadata = require_private(path, directory=False)
    if metadata.st_size > MAXIMUM_JSON_BYTES:
        raise ControlUnavailable("native control file is too large")
    try:
        payload = parse_bounded_json(_read_text_with_windows_share_retry(path, metadata))
    except (OSError, ValueError, RecursionError, UnicodeDecodeError) as exc:
        raise ControlUnavailable("native control file is malformed") from exc
    if not is_json(payload):
        raise ControlUnavailable("native control file is malformed")
    return payload


def _windows_executable_sha256(value: ControlStreamDescriptor | RawControlDescriptor) -> str:
    digest = value.get("executableSHA256")
    if not isinstance(digest, str) or _SHA256_HEX_PATTERN.fullmatch(digest) is None:
        raise ControlUnavailable("native control executable identity is malformed")
    return digest


def _optional_darwin_executable_sha256(
    value: ControlStreamDescriptor | RawControlDescriptor,
) -> str | None:
    """Return a new Darwin owner's immutable image identity when advertised."""

    digest = value.get("executableSHA256")
    if digest is None:
        # Companions released before the same-path handoff fix did not bind
        # their descriptor to the image mapped at startup.
        return None
    if not isinstance(digest, str) or _SHA256_HEX_PATTERN.fullmatch(digest) is None:
        raise ControlUnavailable("native control executable identity is malformed")
    return digest


def _optional_darwin_executable_file_identity(
    value: ControlStreamDescriptor | RawControlDescriptor,
) -> tuple[int, int] | None:
    """Return a Darwin owner's startup vnode identity when advertised."""

    device = value.get("executableDevice")
    inode = value.get("executableInode")
    if device is None and inode is None:
        return None
    maximum = (1 << 64) - 1
    if (
        type(device) is not int
        or type(inode) is not int
        or not 0 < device <= maximum
        or not 0 < inode <= maximum
    ):
        raise ControlUnavailable("native control executable identity is malformed")
    return device, inode


def _validated_control_descriptor(
    value: RawControlDescriptor,
) -> ControlStreamDescriptor:
    """Validate the generated live-stream descriptor without rewriting it."""

    candidate: object = value
    try:
        if not is_control_stream_descriptor(candidate):
            raise ControlUnavailable("native control stream descriptor is malformed")
    except (TypeError, ValueError, RecursionError) as exc:
        raise ControlUnavailable("native control stream descriptor is malformed") from exc
    if candidate["appTarget"] != CONTROL_APP_TARGET:
        raise ControlUnavailable("native control target does not match")
    capabilities = candidate["capabilities"]
    if ControlCapability.CONTROL_LOCAL_STREAM_V1.value not in capabilities:
        raise ControlUnavailable("native control capabilities do not match")
    return candidate


def _pid_is_proven_dead(pid: int) -> bool:
    """Return true only for the OS's unambiguous no-such-process result.

    Permission failures are common from the Codex MCP sandbox and do not prove
    that the owner is gone. Other probe failures are likewise ambiguous, so
    callers must keep them fail-closed rather than treating them as residue.
    """

    if _is_windows_host():
        return _windows_pid_is_proven_dead(pid)
    try:
        os.kill(pid, 0)
    except PermissionError:
        return False
    except ProcessLookupError:
        return True
    except (OSError, OverflowError) as exc:
        raise ControlUnavailable("native control descriptor liveness is unavailable") from exc
    return False


def _validate_descriptor_platform_binding(
    value: ControlStreamDescriptor | RawControlDescriptor,
    runtime: Mapping[str, object],
) -> None:
    """Bind the reduced Windows capability set to a proven Windows artifact."""

    descriptor_platform = value.get("platform")
    runtime_platform = runtime.get("platform")
    runtime_artifact_kind = runtime.get("artifactKind")
    if _is_windows_platform_key(descriptor_platform):
        if runtime_platform != descriptor_platform or runtime_artifact_kind != "windows-executable":
            raise ControlUnavailable("native control platform does not match")
    elif (
        _is_windows_platform_key(runtime_platform) or runtime_artifact_kind == "windows-executable"
    ):
        raise ControlUnavailable("native control platform does not match")


def _path_entry_may_exist(path: Path) -> bool:
    """Return false only for the filesystem's unambiguous missing result."""

    try:
        path.lstat()
    except FileNotFoundError:
        return False
    except (OSError, ValueError):
        return True
    return True


def _stream_descriptor_is_present(root: Path) -> bool:
    try:
        (root / "stream-descriptor.json").lstat()
    except FileNotFoundError:
        return False
    except OSError as exc:
        raise ControlUnavailable("native control stream discovery is unavailable") from exc
    return True


def _v2_descriptor_is_present() -> bool:
    """Recognize a v2 descriptor without treating malformed owners as legacy."""

    root = control_root()
    if not _stream_descriptor_is_present(root):
        return False
    try:
        candidate = read_json(root / "stream-descriptor.json")
    except ControlUnavailable:
        return False
    return candidate.get("protocolVersion") == 2


def _discover_control_transport(root: Path) -> StreamDiscovery:
    return discover_transport(
        root,
        read_descriptor=read_json,
        owner_lock_state=_owner_lock_state,
        pid_is_proven_dead=_pid_is_proven_dead,
        expected_app_target=CONTROL_APP_TARGET,
        plugin_version=lambda: installed_plugin_version(Path(__file__).resolve().parents[1]),
    )


def _validate_stream_runtime_owner(
    value: RawControlDescriptor,
    runtime: Mapping[str, object],
) -> None:
    _validate_descriptor_platform_binding(value, runtime)
    if not runtime.get("installed"):
        return
    expected_path = runtime.get("appPath")
    actual_path = (
        value.get("executablePath")
        if _is_windows_platform_key(value.get("platform"))
        else value.get("bundlePath")
    )
    if not isinstance(expected_path, str) or not isinstance(actual_path, str):
        raise ControlUnavailable("native control app identity is unavailable")
    try:
        if Path(expected_path).resolve(strict=True) != Path(actual_path).resolve(strict=True):
            raise ControlUnavailable("native control is not the active companion")
    except (OSError, ValueError) as exc:
        raise ControlUnavailable("native control app identity is unavailable") from exc
    if _is_windows_platform_key(value.get("platform")):
        expected_digest = runtime.get("_executableSHA256")
        actual_digest = _windows_executable_sha256(value)
        if (
            not isinstance(expected_digest, str)
            or _SHA256_HEX_PATTERN.fullmatch(expected_digest) is None
            or not hmac.compare_digest(expected_digest, actual_digest)
        ):
            raise ControlUnavailable("native control executable identity does not match")
        return

    expected_digest = runtime.get("_executableSHA256")
    actual_digest = value.get("executableSHA256")
    expected_device = runtime.get("_executableDevice")
    expected_inode = runtime.get("_executableInode")
    if (
        not isinstance(expected_digest, str)
        or _SHA256_HEX_PATTERN.fullmatch(expected_digest) is None
        or not isinstance(actual_digest, str)
        or not hmac.compare_digest(expected_digest, actual_digest)
        or type(expected_device) is not int
        or type(expected_inode) is not int
        or value.get("executableDevice") != expected_device
        or value.get("executableInode") != expected_inode
    ):
        raise ControlUnavailable("native control executable identity does not match")


def descriptor_may_have_live_owner() -> bool:
    """Fail closed when a live stream or its existing owner lease may exist."""
    root = control_root()
    try:
        require_private(root, directory=True)
    except ControlUnavailable:
        return _path_entry_may_exist(root)
    if _path_entry_may_exist(root / "stream-descriptor.json"):
        return True
    try:
        return _owner_lock_state(root) not in {"missing", "available"}
    except (ControlUnavailable, OSError, ValueError):
        return True


def descriptor(
    *,
    runtime: Mapping[str, object] | None = None,
    allow_stale_owner: bool = False,
) -> tuple[Path, RawControlDescriptor]:
    """Read the descriptor, reusing a status proof from the same MCP request.

    Widget status/open calls also need to return the runtime shape. Letting
    that one request-local status result flow through descriptor binding keeps
    us from traversing a signed app bundle twice per poll.
    """

    root = control_root()
    require_private(root, directory=True)
    discovered = _discover_control_transport(root)
    stream_descriptor: RawControlDescriptor = dict(discovered.descriptor.items())
    manager: RuntimeManager | None = None
    if runtime is None:
        manager = RuntimeManager()
        resolved_runtime = manager.status()
    else:
        resolved_runtime = runtime
    try:
        _validate_stream_runtime_owner(stream_descriptor, resolved_runtime)
    except ControlUnavailable as validation_error:
        if not allow_stale_owner or resolved_runtime.get("source") != "plugin-bundled":
            raise
        expected_app_path = resolved_runtime.get("appPath")
        if not isinstance(expected_app_path, str):
            raise ControlUnavailable(
                "native control is not the active companion"
            ) from validation_error
        try:
            expected = Path(expected_app_path).resolve(strict=True)
        except (OSError, ValueError) as exc:
            raise ControlUnavailable("native control is not the active companion") from exc
        stale_manager = manager if manager is not None else RuntimeManager()
        _schedule_stream_connection(root, discovered.descriptor)
        try:
            _source_root, stale_family_root = _runtime_handoff_source(
                resolved_runtime,
                expected,
                stale_manager.spec,
            )
            disposition, stale_root, stale_value = _handoff_descriptor(
                expected,
                stale_family_root,
                stale_manager.spec,
            )
        except ControlUnavailable as exc:
            raise ControlUnavailable("native control is not the active companion") from exc
        if disposition != "stale" or stale_root != root or stale_value != stream_descriptor:
            raise ControlUnavailable(
                "native control is not the active companion"
            ) from validation_error
    return root, stream_descriptor


def stream_control_descriptor() -> tuple[Path, ControlStreamDescriptor] | None:
    """Return only a discovered, reviewed modern native stream owner."""

    if not _stream_descriptor_is_present(control_root()):
        return None
    root, value = descriptor(allow_stale_owner=True)
    candidate: object = value
    try:
        if not is_control_stream_descriptor(candidate):
            raise ControlUnavailable("native control stream descriptor is malformed")
    except (TypeError, ValueError, RecursionError) as exc:
        raise ControlUnavailable("native control stream descriptor is malformed") from exc
    return root, candidate


def descriptor_uses_runtime_image(*, runtime: Mapping[str, object]) -> bool:
    """Whether the authenticated owner still maps the selected plugin image.

    This is deliberately separate from descriptor(): a same-path republish can
    happen while capture or upload is active, and authenticated stream status plus terminal
    controls must continue reaching that owner. Only setup, Start, and native
    bootstrap use this hint to enter the safe cooperative-handoff lane.
    """

    if _v2_descriptor_is_present():
        from companion_client import discover_companion_owner

        owner = discover_companion_owner(runtime=runtime, allow_existing_owner=True)
        return owner.uses_runtime_image(runtime)

    _root, value = descriptor(runtime=runtime)
    if runtime.get("artifactKind") == "windows-executable":
        runtime_digest = runtime.get("_executableSHA256")
        return (
            isinstance(runtime_digest, str)
            and _SHA256_HEX_PATTERN.fullmatch(runtime_digest) is not None
            and hmac.compare_digest(
                runtime_digest,
                _windows_executable_sha256(value),
            )
        )

    descriptor_file_identity = _optional_darwin_executable_file_identity(value)
    runtime_device = runtime.get("_executableDevice")
    runtime_inode = runtime.get("_executableInode")
    if (
        descriptor_file_identity is None
        or type(runtime_device) is not int
        or type(runtime_inode) is not int
        or (runtime_device, runtime_inode) != descriptor_file_identity
    ):
        return False
    descriptor_digest = _optional_darwin_executable_sha256(value)
    if descriptor_digest is not None:
        runtime_digest = runtime.get("_executableSHA256")
        if (
            not isinstance(runtime_digest, str)
            or _SHA256_HEX_PATTERN.fullmatch(runtime_digest) is None
            or not hmac.compare_digest(runtime_digest, descriptor_digest)
        ):
            return False
    return True


def verified_current_stream_owner_without_connection(
    *,
    runtime: Mapping[str, object],
    require_cached_state: bool = False,
    cached_state_allowed: Callable[[dict[str, object]], bool] | None = None,
) -> bool:
    """Check bootstrap routing without opening a connection.

    Match the live descriptor and held lease to the selected image. Peer
    authentication happens when the transport connects. If requested, require
    an already authenticated same-owner snapshot satisfying the state guard.
    """

    if runtime.get("installed") is not True or runtime.get("source") != "plugin-bundled":
        return False
    if _v2_descriptor_is_present():
        from companion_client import companion_client

        client = companion_client(runtime=runtime, connect=False, allow_existing_owner=True)
        if not client.owner.uses_runtime_image(runtime):
            return False
        if not require_cached_state:
            return True
        state = client.latest_state()
        if state is None:
            return False
        if cached_state_allowed is None:
            return True
        return cached_state_allowed(client.public_status())
    root = control_root()
    require_private(root, directory=True)
    discovered = _discover_control_transport(root)
    if not descriptor_uses_runtime_image(runtime=runtime):
        return False
    require_stream_owner(
        discovered.root,
        discovered.descriptor,
        peer_pid=discovered.descriptor["pid"],
    )
    if not require_cached_state:
        return True
    state = stream_owner_state(discovered.root, discovered.descriptor)
    return state is not None and (cached_state_allowed is None or cached_state_allowed(state))


def _require_supported_control_action(action: str, value: RawControlDescriptor) -> None:
    parsed_action = parse_control_action(action)
    platform = parse_control_platform(value.get("platform", ControlPlatform.DARWIN_UNIVERSAL.value))
    if parsed_action is ControlAction.UNKNOWN or platform is ControlPlatform.UNKNOWN:
        raise ControlUnavailable("native control action is unsupported on this platform")


def _stream_descriptor(value: RawControlDescriptor) -> ControlStreamDescriptor | None:
    if value.get("transport") not in {"unix-domain-socket", "windows-named-pipe"}:
        return None
    return _validated_control_descriptor(value)


def _stream_owner_key(root: Path, value: ControlStreamDescriptor) -> _StreamOwnerKey:
    return str(root.resolve()), value["epoch"], value["pid"], value["endpoint"]


def _next_stream_request_identity() -> tuple[str, int, str]:
    """Keep every ephemeral MCP client within one bounded native replay lane."""

    global _stream_request_sequence

    with _STREAM_SEQUENCE_LOCK:
        if _stream_request_sequence >= MAXIMUM_JAVASCRIPT_SAFE_INTEGER:
            raise ControlUnavailable("native control stream request sequence is exhausted")
        _stream_request_sequence += 1
        sequence = _stream_request_sequence
    return _STREAM_CLIENT_ID, sequence, f"{_STREAM_CLIENT_ID}_{sequence}"


def _acquire_stream_submission_lock(
    *,
    deadline: float,
    cancellation_event: threading.Event | None,
) -> None:
    """Preserve global wire ordering without extending an action deadline."""

    while True:
        if cancellation_event is not None and cancellation_event.is_set():
            raise ControlUnavailable("native control request cancelled")
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise _ControlRequestTimedOut("native control request timed out")
        if _STREAM_SUBMISSION_LOCK.acquire(timeout=min(0.05, remaining)):
            return


def _stream_transport_for_owner(root: Path, value: ControlStreamDescriptor) -> StreamTransport:
    key = _stream_owner_key(root, value)
    with _STREAM_TRANSPORT_LOCK:
        if _stream_transports_shutdown:
            raise ControlUnavailable("native control stream process is shutting down")
        existing = _STREAM_TRANSPORTS.get(key)
        if existing is not None:
            if not existing.closed:
                return existing
            _STREAM_TRANSPORTS.pop(key, None)
            _STREAM_CONNECT_FAILURES.pop(key, None)
        for previous_key, previous in tuple(_STREAM_TRANSPORTS.items()):
            previous.close()
            _STREAM_TRANSPORTS.pop(previous_key, None)
            _STREAM_CONNECT_FAILURES.pop(previous_key, None)
        current = StreamTransport(root, value)
        _STREAM_TRANSPORTS[key] = current
        return current


def close_stream_transports(*, permanent: bool = False) -> None:
    """Release owned native connections and optionally seal process admission."""

    global _stream_transports_shutdown

    with _STREAM_TRANSPORT_LOCK:
        if permanent:
            _stream_transports_shutdown = True
        transports = tuple(_STREAM_TRANSPORTS.values())
        _STREAM_TRANSPORTS.clear()
        _STREAM_CONNECT_FAILURES.clear()
    for transport in transports:
        transport.close()
    from companion_client import close_companion_clients

    close_companion_clients()


def connect_stream_owner(
    root: Path,
    value: ControlStreamDescriptor,
    *,
    deadline: float,
) -> None:
    _stream_transport_for_owner(root, value).connect(deadline=deadline)


def existing_stream_owner_transport(
    root: Path,
    value: ControlStreamDescriptor,
) -> StreamTransport | None:
    """Observe an existing exact-owner transport without connecting or creating one."""

    with _STREAM_TRANSPORT_LOCK:
        return _STREAM_TRANSPORTS.get(_stream_owner_key(root, value))


def stream_owner_state(
    root: Path,
    value: Mapping[str, object],
) -> dict[str, object] | None:
    """Read an existing exact-owner push cache without connecting or IPC."""

    candidate: object = value
    try:
        if not is_control_stream_descriptor(candidate):
            return None
    except (TypeError, ValueError, RecursionError):
        return None
    key = _stream_owner_key(root, candidate)
    with _STREAM_TRANSPORT_LOCK:
        transport = _STREAM_TRANSPORTS.get(key)
    if transport is None:
        return None
    binding = transport.active_binding
    if binding is None or binding.epoch != candidate["epoch"] or binding.pid != candidate["pid"]:
        return None
    response = native_status_cache().latest(binding)
    if response is None:
        return None
    state = response.get("state")
    return dict(state.items()) if is_json(state) else None


def _connect_stream_in_background(
    key: _StreamOwnerKey,
    transport: StreamTransport,
    platform: str,
    version: str,
) -> None:
    try:
        for attempt in range(1, _STREAM_BACKGROUND_CONNECT_ATTEMPTS + 1):
            try:
                transport.connect(deadline=time.monotonic() + _STREAM_BACKGROUND_CONNECT_SECONDS)
            except ControlUnavailable:
                error_kind = "unavailable"
            except OSError:
                error_kind = "io-error"
            except RuntimeError:
                error_kind = "runtime-error"
            except ValueError:
                error_kind = "invalid-response"
            else:
                with _STREAM_TRANSPORT_LOCK:
                    previously_exhausted = _STREAM_CONNECT_FAILURES.pop(key, None) is not None
                if previously_exhausted or attempt > 1:
                    log_native_runtime_event(
                        "connect",
                        "recovered",
                        platform=platform,
                        version=version,
                        attempt=attempt,
                    )
                return
            if attempt < _STREAM_BACKGROUND_CONNECT_ATTEMPTS:
                time.sleep(_STREAM_RECONNECT_COOLDOWN_SECONDS)
                continue
            with _STREAM_TRANSPORT_LOCK:
                _STREAM_CONNECT_FAILURES[key] = time.monotonic()
            log_native_runtime_event(
                "connect",
                "failed",
                platform=platform,
                version=version,
                attempt=attempt,
                error_kind=error_kind,
            )
            return
    finally:
        with _STREAM_TRANSPORT_LOCK:
            _STREAM_CONNECTING.discard(key)


def _schedule_stream_connection(root: Path, value: ControlStreamDescriptor) -> StreamTransport:
    key = _stream_owner_key(root, value)
    transport = _stream_transport_for_owner(root, value)
    if transport.active_binding is not None:
        return transport
    with _STREAM_TRANSPORT_LOCK:
        failed = _STREAM_CONNECT_FAILURES.get(key)
        if key in _STREAM_CONNECTING or (
            failed is not None and time.monotonic() - failed < _STREAM_RECONNECT_COOLDOWN_SECONDS
        ):
            return transport
        _STREAM_CONNECTING.add(key)
        threading.Thread(
            target=_connect_stream_in_background,
            args=(key, transport, value["platform"], value["appVersion"]),
            daemon=True,
            name="meetings-native-stream-connect",
        ).start()
    return transport


def _project_stream_response(
    response: RawControlPayload,
    *,
    action: str,
) -> RawControlPayload:
    return dict(sanitize_control_payload(response, action=action).items())


class ControlClient:
    def __init__(self) -> None:
        self.sequence = 0
        # A descriptor-bound status or lifecycle handoff uses the same client
        # and sequence space as an ordinary call. Keep the lock re-entrant so
        # call() can include runtime/descriptor resolution in its deadline
        # while _call_with_descriptor() also serializes direct callers.
        self._call_lock = threading.RLock()

    def _acquire_call_lock(
        self,
        *,
        deadline: float,
        cancellation_event: threading.Event | None,
    ) -> None:
        while True:
            if cancellation_event is not None and cancellation_event.is_set():
                raise ControlUnavailable("native control request cancelled")
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise _ControlRequestTimedOut("native control request timed out")
            if self._call_lock.acquire(timeout=min(0.05, remaining)):
                return

    def _cached_stream_status(
        self,
        root: Path,
        value: ControlStreamDescriptor,
        *,
        runtime: Mapping[str, object],
    ) -> RawControlPayload:
        transport = _schedule_stream_connection(root, value)
        binding = transport.active_binding
        if binding is None:
            key = _stream_owner_key(root, value)
            with _STREAM_TRANSPORT_LOCK:
                connection_pending = key in _STREAM_CONNECTING
                failed_at = _STREAM_CONNECT_FAILURES.get(key)
                connection_failed = (
                    failed_at is not None
                    and time.monotonic() - failed_at < _STREAM_RECONNECT_COOLDOWN_SECONDS
                )
            if connection_pending and not connection_failed:
                return connecting_state(runtime=runtime)
            binding = transport.active_binding
            if binding is None:
                return disconnected_state("native control stream is unavailable", runtime=runtime)
        if binding.epoch != value["epoch"] or binding.pid != value["pid"]:
            return disconnected_state("native control stream owner does not match", runtime=runtime)
        cached = native_status_cache().latest(binding)
        if cached is None:
            return disconnected_state("native control stream state is unavailable", runtime=runtime)
        projected = _project_stream_response(
            cached,
            action=ControlAction.STATUS.value,
        )
        projected["companionPid"] = value["pid"]
        state = projected.get("state")
        if is_json(state):
            projected["state"] = _enforce_descriptor_projection_contracts(
                state,
                root,
                dict(value.items()),
            )
        return projected

    def _call_stream_with_descriptor(
        self,
        root: Path,
        value: ControlStreamDescriptor,
        action: str,
        *,
        arguments: ControlActionArguments,
        cancellation_event: threading.Event | None,
        deadline: float,
    ) -> RawControlPayload:
        transport = _stream_transport_for_owner(root, value)
        transport.connect(deadline=deadline, cancellation_event=cancellation_event)
        if cancellation_event is not None and cancellation_event.is_set():
            raise ControlUnavailable("native control request cancelled")
        _acquire_stream_submission_lock(
            deadline=deadline,
            cancellation_event=cancellation_event,
        )
        submission_released = False

        def release_submission() -> None:
            nonlocal submission_released

            if not submission_released:
                submission_released = True
                _STREAM_SUBMISSION_LOCK.release()

        try:
            if cancellation_event is not None and cancellation_event.is_set():
                raise ControlUnavailable("native control request cancelled")
            client_id, sequence, request_id = _next_stream_request_identity()
            self.sequence += 1
            parameters: dict[str, object] = {
                "clientId": client_id,
                "sequence": sequence,
                "requestId": request_id,
                "issuedAtMillis": int(time.time() * 1000),
                "action": action,
                "arguments": dict(arguments),
            }
            response = transport.request(
                "meetings.control",
                parameters,
                request_id=request_id,
                deadline=deadline,
                cancellation_event=cancellation_event,
                on_sent=release_submission,
            )
        finally:
            release_submission()
        projected = _project_stream_response(response, action=action)
        state = projected.get("state")
        if is_json(state):
            projected["state"] = _enforce_descriptor_projection_contracts(
                state,
                root,
                dict(value.items()),
            )
        projected["companionPid"] = value["pid"]
        return projected

    def status(
        self,
        *,
        runtime: Mapping[str, object] | None = None,
        wait_for_connection: bool = False,
    ) -> dict[str, object]:
        resolved_runtime = runtime if runtime is not None else RuntimeManager().status()
        if _v2_descriptor_is_present():
            from companion_client import companion_client

            try:
                client = companion_client(
                    runtime=resolved_runtime,
                    connect=wait_for_connection,
                    allow_existing_owner=True,
                    timeout_seconds=5.0,
                )
                failure = client.connect_in_background()
                if client.latest_state() is None:
                    if failure is not None:
                        raise failure
                    status = connecting_state(runtime=resolved_runtime)
                    status["ok"] = False
                    status["availability"] = {
                        "status": "loading",
                        "stage": "connecting",
                    }
                    return status
                return client.public_status()
            except ControlUnavailable as exc:
                status = disconnected_state(str(exc), runtime=resolved_runtime)
                status["availability"] = {
                    "status": "error",
                    "reason": (
                        "connection-failed"
                        if isinstance(exc, (ControlConnectionUnavailable, ControlEndpointRejected))
                        else "owner-invalid"
                    ),
                }
                return status
        status = disconnected_state(
            "native companion control protocol v2 is unavailable",
            runtime=resolved_runtime,
        )
        status["availability"] = {
            "status": "error",
            "reason": "companion-unavailable",
        }
        return status

    def call(
        self,
        action: str,
        timeout_seconds: float = 12.0,
        *,
        arguments: ControlActionArguments | None = None,
        runtime: Mapping[str, object] | None = None,
        cancellation_event: threading.Event | None = None,
    ) -> dict[str, object]:
        deadline = time.monotonic() + max(0.0, timeout_seconds)
        self._acquire_call_lock(
            deadline=deadline,
            cancellation_event=cancellation_event,
        )
        try:
            if cancellation_event is not None and cancellation_event.is_set():
                raise ControlUnavailable("native control request cancelled")
            if action == ControlAction.START.value and arguments:
                raise ControlUnavailable("native control arguments do not match action")
            resolved_runtime = runtime if runtime is not None else RuntimeManager().status()
            if _v2_descriptor_is_present():
                return self._call_v2(
                    action,
                    arguments=arguments,
                    runtime=resolved_runtime,
                    timeout_seconds=max(0.0, deadline - time.monotonic()),
                    cancellation_event=cancellation_event,
                )
            raise ControlUnavailable("native companion control protocol v2 is unavailable")
        finally:
            self._call_lock.release()

    def _call_v2(
        self,
        action: str,
        *,
        arguments: ControlActionArguments | None,
        runtime: Mapping[str, object],
        timeout_seconds: float,
        cancellation_event: threading.Event | None,
    ) -> dict[str, object]:
        from companion_client import companion_client

        client = companion_client(
            runtime=runtime,
            allow_existing_owner=action in {ControlAction.STATUS.value, ControlAction.STOP.value},
            timeout_seconds=timeout_seconds,
            cancellation_event=cancellation_event,
        )
        supplied = dict(arguments or {})
        if action == ControlAction.START.value:
            method, parameters = "recording.start", supplied
        elif action == ControlAction.STOP.value:
            expected = supplied.get("expectedSessionId")
            if len(supplied) != 1 or not isinstance(expected, str):
                raise ControlUnavailable("native recording Stop requires its exact session")
            method = "recording.stop"
            parameters = {"expectedSessionId": client.verify_session(expected)}
        elif action == ControlAction.REQUEST_MICROPHONE.value:
            if supplied:
                raise ControlUnavailable("native recording permission request is malformed")
            method, parameters = "permissions.request", {"kind": "microphone"}
        elif action == ControlAction.REQUEST_SYSTEM_AUDIO.value:
            if supplied:
                raise ControlUnavailable("native recording permission request is malformed")
            method, parameters = "permissions.request", {"kind": "systemAudio"}
        elif action == ControlAction.STATUS.value:
            if supplied:
                raise ControlUnavailable("native recording status request is malformed")
            method, parameters = "companion.getState", {}
        elif action == ControlAction.QUIT_FOR_UPDATE.value:
            if supplied:
                raise ControlUnavailable("native update request is malformed")
            method = "lifecycle.quitForUpdate"
            parameters = {"expectedOwnerEpoch": client.owner.descriptor["ownerEpoch"]}
        else:
            raise ControlUnavailable("native companion v2 operation is unsupported")
        result = client.call(
            method,
            parameters,
            timeout_seconds=timeout_seconds,
            cancellation_event=cancellation_event,
        )
        if method == "lifecycle.quitForUpdate":
            return {"ok": result.get("disposition") == "accepted", "handoff": result}
        payload = client.public_status()
        if method == "recording.stop":
            completion = result.get("completion")
            if is_recording_completion(completion):
                payload["completion"] = {"outcome": "saved"}
        return payload

    def call_with_descriptor(
        self,
        root: Path,
        value: RawControlDescriptor,
        action: str,
        *,
        timeout_seconds: float,
        arguments: ControlActionArguments,
        cancellation_event: threading.Event | None = None,
    ) -> RawControlPayload:
        """Dispatch through the existing authenticated descriptor interception seam."""

        if cancellation_event is None:
            return self._call_with_descriptor(
                root,
                value,
                action,
                timeout_seconds=timeout_seconds,
                arguments=arguments,
            )
        return self._call_with_descriptor(
            root,
            value,
            action,
            timeout_seconds=timeout_seconds,
            arguments=arguments,
            cancellation_event=cancellation_event,
        )

    def _call_with_descriptor(
        self,
        root: Path,
        value: dict[str, object],
        action: str,
        *,
        timeout_seconds: float,
        arguments: ControlActionArguments,
        cancellation_event: threading.Event | None = None,
        deadline: float | None = None,
    ) -> dict[str, object]:
        """Send a request to an already authenticated live-stream owner."""

        resolved_deadline = (
            time.monotonic() + max(0.0, timeout_seconds) if deadline is None else deadline
        )
        self._acquire_call_lock(
            deadline=resolved_deadline,
            cancellation_event=cancellation_event,
        )
        try:
            if action not in {ControlAction.STATUS.value, ControlAction.QUIT_FOR_UPDATE.value}:
                raise ControlUnavailable("legacy companion product operations are unavailable")
            stream = _stream_descriptor(value)
            if stream is None:
                raise ControlUnavailable("native control stream descriptor is malformed")
            normalized_arguments = normalize_action_arguments(action, arguments)
            _require_supported_control_action(action, value)
            return self._call_stream_with_descriptor(
                root,
                stream,
                action,
                arguments=normalized_arguments,
                cancellation_event=cancellation_event,
                deadline=resolved_deadline,
            )
        finally:
            self._call_lock.release()


_resolved_path = _control_client_retention.resolved_path
_is_direct_versioned_plugin_app = _control_client_retention.is_direct_versioned_plugin_app
_is_stable_runtime_artifact = _control_client_retention.is_stable_runtime_artifact
_runtime_handoff_source = _control_client_retention.runtime_handoff_source
_lexical_absolute_path = _control_client_retention.lexical_absolute_path
_future_path = _control_client_retention.future_path
_exact_missing_handoff_path = _control_client_retention.exact_missing_handoff_path
_resolved_handoff_paths = _control_client_retention.resolved_handoff_paths
_expected_executable_path = _control_client_retention.expected_executable_path

_handoff_descriptor = _control_client_handoff.handoff_descriptor
_wait_for_handoff_exit = _control_client_handoff.wait_for_handoff_exit
_require_same_handoff_descriptor = _control_client_handoff.require_same_handoff_descriptor
_windows_owner_lock_state = _control_client_handoff.windows_owner_lock_state
_owner_lock_state = _control_client_handoff.owner_lock_state
_descriptor_owner_lease_is_held = _control_client_handoff.descriptor_owner_lease_is_held
_log_handoff_outcome = _control_client_handoff.log_handoff_outcome
_require_exact_handoff_owner = _control_client_handoff.require_exact_handoff_owner
force_quit_companion_owner = _control_client_handoff.force_quit_companion_owner
_perform_cooperative_handoff = _control_client_handoff.perform_cooperative_handoff
_is_quiescent_handoff_state = _control_client_handoff.is_quiescent_handoff_state
_is_fenced_handoff_ack_state = _control_client_handoff.is_fenced_handoff_ack_state
_wait_for_absent_handoff_owner_lease = _control_client_handoff.wait_for_absent_handoff_owner_lease
_require_canonical_handoff_request = _control_client_handoff.require_canonical_handoff_request
_request_update_handoff_once = _control_client_handoff.request_update_handoff_once
resolve_update_handoff_for_launch = _control_client_handoff.resolve_update_handoff_for_launch
disconnected_state = _control_client_handoff.disconnected_state


# Public aliases expose typed owner-recovery operations without forwarding layers.
# Keep wrappers only where recovery hooks intercept their private implementation.
DescriptorChanged = _DescriptorChanged
ControlRequestTimedOut = _ControlRequestTimedOut
HandoffExitTimedOut = _HandoffExitTimedOut
HandoffOwnerUnsettled = _HandoffOwnerUnsettled
OwnerControlClient = ControlClient
verify_windows_owner_process_image = _verify_windows_owner_process_image
SHA256_HEX_PATTERN = _SHA256_HEX_PATTERN
MAXIMUM_CAPTURE_AWARE_SIGTERM_OWNERS = _MAXIMUM_CAPTURE_AWARE_SIGTERM_OWNERS
optional_darwin_executable_sha256 = _optional_darwin_executable_sha256
optional_darwin_executable_file_identity = _optional_darwin_executable_file_identity
log_handoff_outcome = _log_handoff_outcome
resolved_path = _resolved_path
resolved_handoff_paths = _resolved_handoff_paths
require_canonical_handoff_request = _require_canonical_handoff_request
expected_executable_path = _expected_executable_path
is_direct_versioned_plugin_app = _is_direct_versioned_plugin_app
is_stable_runtime_artifact = _is_stable_runtime_artifact
path_entry_may_exist = _path_entry_may_exist
is_fenced_handoff_ack_state = _is_fenced_handoff_ack_state


@contextmanager
def capture_aware_sigterm_owners() -> Generator[set[tuple[int, str]]]:
    """Lock and expose the established bounded signal-history seam."""

    with _CAPTURE_AWARE_SIGTERM_LOCK:
        yield _CAPTURE_AWARE_SIGTERM_OWNERS


def is_windows_host() -> bool:
    """Return whether this process is running on the supported Windows host."""

    return _is_windows_host()


def call_with_descriptor(
    client: ControlClient,
    root: Path,
    value: RawControlDescriptor,
    action: str,
    *,
    timeout_seconds: float,
    arguments: ControlActionArguments,
    cancellation_event: threading.Event | None = None,
) -> RawControlPayload:
    """Preserve private descriptor mocks while presenting a typed public boundary."""

    if cancellation_event is None:
        return OwnerControlClient.call_with_descriptor(
            client,
            root,
            value,
            action,
            timeout_seconds=timeout_seconds,
            arguments=arguments,
        )
    return OwnerControlClient.call_with_descriptor(
        client,
        root,
        value,
        action,
        timeout_seconds=timeout_seconds,
        arguments=arguments,
        cancellation_event=cancellation_event,
    )


def owner_lock_state(root: Path | None = None) -> str:
    """Observe the existing native owner's authenticated process lease."""

    if root is None:
        return _owner_lock_state()
    return _owner_lock_state(root)


def pid_is_proven_dead(pid: int) -> bool:
    """Return true only when the operating system proves the owner is dead."""

    return _pid_is_proven_dead(pid)


def wait_for_handoff_exit(
    root: Path,
    value: RawControlDescriptor,
    *,
    timeout_seconds: float | None = None,
) -> None:
    """Wait for the exact owner and authenticated lease to leave together."""

    if timeout_seconds is None:
        _wait_for_handoff_exit(root, value)
    else:
        _wait_for_handoff_exit(root, value, timeout_seconds=timeout_seconds)
