"""Privacy-safe, dependency-free Sentry reporting for the Meetings MCP."""

from __future__ import annotations

import json
import os
import plistlib
import re
import stat
import sys
import threading
import time
import uuid
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal, TypeAlias, TypedDict
from urllib.parse import urlsplit
from urllib.request import HTTPSHandler, Request, build_opener

from bootstrap_recovery import BootstrapFailure
from native_runtime_types import MaterializeVerificationPhase
from runtime_config import RUNTIME_CONFIG

from helpers import NoRedirectHandler, create_https_context, is_json

_PLUGIN_ROOT = Path(__file__).resolve().parents[1]
_PLUGIN_MARKETPLACES = frozenset(
    {
        "openai-internal-testing",
        "openai-curated-remote",
        "openai-workspace",
        "chatgpt-meetings",
        "microwave",
    }
)
_MAXIMUM_METADATA_BYTES = 128 * 1024
_MAXIMUM_EVENTS_PER_PROCESS = 64
_MAXIMUM_USER_INTERFACE_EVENTS_PER_PROCESS = 32
_MAXIMUM_PRESENTATION_EVENTS_PER_PROCESS = 32
_MAXIMUM_TRACKED_UI_OPENED_INSTANCES = 128
_MAXIMUM_CONCURRENT_POSTS = 4
_MAXIMUM_CONCURRENT_USER_INTERFACE_POSTS = 2
_MAXIMUM_CONCURRENT_PRESENTATION_POSTS = 2
_POST_TIMEOUT_SECONDS = 1.0
_SAFE_VERSION = re.compile(r"[A-Za-z0-9][A-Za-z0-9._+-]{0,79}\Z")
_SAFE_CODEX_VERSION = re.compile(
    r"[0-9]{1,9}\.[0-9]{1,9}\.[0-9]{1,9}(?:[-+][A-Za-z0-9][A-Za-z0-9.+-]{0,39})?\Z"
)
_SAFE_NATIVE_ALPHA_RELEASE = re.compile(
    r"(?:0|[1-9][0-9]{0,8})\.(?:0|[1-9][0-9]{0,8})\."
    r"(?:0|[1-9][0-9]{0,8})-alpha\.[1-9][0-9]{0,8}\Z"
)
_SAFE_TIMESTAMP = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z\Z")
_SAFE_SENTRY_HOST = re.compile(r"(?:[a-z0-9-]+\.)*sentry\.io\Z")
_SAFE_SENTRY_KEY = re.compile(r"[A-Za-z0-9_-]{1,128}\Z")
_SAFE_SENTRY_USER_ID = re.compile(r"user-[A-Za-z0-9_-]{1,123}\Z")
_SAFE_UI_APP_INSTANCE_ID = re.compile(r"[a-f0-9]{64}\Z")
_SAFE_NATIVE_OWNER_EPOCH = re.compile(r"epoch_[0-9a-f]{32}\Z")
# The canonical authenticated `user.id` and this random per-launch `sessionId`
# are privacy-approved, intentionally retained identifiers and must survive
# future privacy sanitization/audits. Neither contains email, IP, account,
# device, or token data; the session is never persisted.
_SENTRY_SESSION_ID = str(uuid.uuid4())
MCP_SENTRY_STAGES = frozenset(
    {
        "auth",
        "bootstrap",
        "calendar",
        "connect",
        "handoff",
        "initialize",
        "interactions",
        "materialize",
        "note-detail",
        "notes",
        "popup",
        "recording",
        "render",
        "rpc",
        "settings",
    }
)
MCP_SENTRY_AUTH_FAILURE_REASONS = frozenset(
    {
        "spawn",
        "timeout",
        "protocol",
        "io",
        "remote",
        "unsupported",
        "eof",
        "oversize",
        "invalid_auth",
        "account_unverified",
    }
)
MCP_SENTRY_AUTH_REQUESTED_STORES = frozenset({"file", "keyring", "unavailable"})
MCP_SENTRY_KINDS = frozenset(
    {
        "auth",
        "backend",
        "connection",
        "copy",
        "exception",
        "handoff",
        "host-action",
        "invalid-response",
        "launch",
        "permission",
        "recovery",
        "runtime",
        "timeout",
        "update",
        "upload",
        "verify",
        "publish",
    }
)
_SENTRY_HANDOFF_DISPOSITIONS = frozenset({"fallback_started", "start_failed"})
MCP_SENTRY_HANDOFF_FAILURE_REASONS = frozenset(
    {"owner_changed", "owner_unresponsive", "timeout", "handoff_unavailable"}
)
_SENTRY_RECOVERY_KINDS = frozenset(
    {
        "fallback_connection_failed",
        "owner_changed",
        "quit_required",
        "start_retry_required",
        "update_deferred",
    }
)
MCP_SENTRY_PRESENTATIONS = frozenset({"banner", "dialog", "inline", "queue", "sound", "toast"})
MCP_SENTRY_OPERATIONS = frozenset(
    {
        "calendar",
        "connection",
        "copy_notes",
        "copy_transcript",
        "debug",
        "delete",
        "feedback",
        "finalization",
        "manual_retry",
        "new_chat",
        "new_note",
        "notes",
        "onboarding",
        "open_settings",
        "permission",
        "recording",
        "recovery",
        "render",
        "settings",
        "share",
        "sound",
        "start",
        "stop",
        "update",
        "upload",
    }
)
MCP_SENTRY_NOTIFICATIONS = frozenset(
    {
        "banner_presented",
        "calendar_failed",
        "clipboard_failed",
        "connection_lost",
        "debug_failed",
        "delete_failed",
        "dialog_presented",
        "feedback_failed",
        "finalization_failed",
        "force_update_required",
        "host_action_failed",
        "inline_error_presented",
        "new_chat_failed",
        "notes_missing",
        "notes_refresh_failed",
        "permission_action_failed",
        "permission_denied",
        "permission_required",
        "queue_attention",
        "recording_interrupted",
        "recording_sign_in_required",
        "recovery_failed",
        "recovery_required",
        "render_failed",
        "settings_failed",
        "share_failed",
        "sound_failed",
        "sound_repeated",
        "sound_unexpected",
        "start_failed",
        "stop_failed",
        "toast_presented",
        "update_available",
        "update_failed",
        "upload_failed",
        "upload_manual_retry",
        "upload_needs_sign_in",
        "upload_queue_presented",
    }
)
MCP_SENTRY_UPDATE_REASONS = frozenset(
    {
        "install_failed",
        "launch_failed",
        "runtime_verification_failed",
        "terminate_failed",
        "registration_remove_failed",
    }
)
MCP_SENTRY_BACKEND_FAILURE_REASONS = frozenset(
    {"timeout", "transport", "http_4xx", "http_429", "http_5xx", "invalid_response"}
)
MCP_SENTRY_SETTINGS_AUTH_FAILURE_REASONS = frozenset(
    {
        "session_unverified",
        "missing_access_token",
        "auth_required",
        "account_changed",
        "invalid_auth_response",
        "host_auth_unavailable",
        "host_auth_timeout",
        "host_auth_unsupported",
        "host_auth_error",
    }
)
_SETTINGS_ACTIVATION_FAILURE_REASON = "activation_not_effective"
MCP_SENTRY_BOOTSTRAP_FAILURE_REASONS = frozenset(
    failure.sentry_reason for failure in BootstrapFailure
)
MCP_SENTRY_FAILURE_DIAGNOSTIC_VALUES = {
    "failure_operation": frozenset(
        {
            "unknown",
            "verify_registration",
            "resolve_native_artifact",
            "resolve_artifact_root",
            "read_bundle_metadata",
            "control_transport",
        }
    ),
    "resource_role": frozenset(
        {
            "unknown",
            "plugin_root",
            "family_root",
            "registration_manifest",
            "registered_plugin",
            "native_artifact",
            "artifact_root",
            "bundle_metadata",
            "control_endpoint",
        }
    ),
    "os_error_code": frozenset(
        {
            "unknown",
            "ENOENT",
            "EACCES",
            "EPERM",
            "ETIMEDOUT",
            "ECONNREFUSED",
            "ECONNRESET",
            "EPIPE",
        }
    ),
}
MCP_SENTRY_COMPANION_DIAGNOSTIC_VALUES = {
    "companion_status_reason": frozenset(
        {
            "connection-failed",
            "owner-invalid",
            "companion-unavailable",
            "invalid-status-response",
            "invalid-arguments",
            "mcp-exception",
            "request-failed",
        }
    ),
    "companion_observed_stage": frozenset(
        {
            "not-started",
            "discovering",
            "owner-verification",
            "owner-verified",
            "connecting",
            "initializing",
            "ready",
            "failed",
            "disconnected",
        }
    ),
    "companion_observed_failure_stage": frozenset(
        {"discovery", "owner-verification", "initialize"}
    ),
    "companion_observed_failure_reason": frozenset(
        {
            "cancelled",
            "timeout",
            "capability-rejected",
            "initialization-rejected",
            "descriptor-invalid",
            "owner-lease-invalid",
            "owner-image-invalid",
            "owner-mismatch",
            "endpoint-unavailable",
            "endpoint-rejected",
            "endpoint-missing",
            "disconnected",
            "invalid-response",
            "connection-failed",
        }
    ),
    **{
        f"companion_observed_{key}": frozenset({"true", "false"})
        for key in (
            "descriptor_present",
            "owner_verified",
            "connected",
            "initialized",
            "state_cached",
        )
    },
    "bootstrap_last_failure_reason": MCP_SENTRY_BOOTSTRAP_FAILURE_REASONS,
    **{
        f"bootstrap_last_{key}": values
        for key, values in MCP_SENTRY_FAILURE_DIAGNOSTIC_VALUES.items()
    },
}
_BOOTSTRAP_FAILURE_EXPLANATIONS = {
    "registration_unavailable": "A registration path was absent during verification. The cause of its absence is unknown; retry must revalidate registration and owner.",
    "artifact_missing": "The expected native artifact was absent beneath an existing plugin root. The cause of its absence is unknown.",
    "missing_resource": "A resource was not found at the reported operation when known. The underlying cause is unknown; this does not prove the native app is missing.",
    "permission_denied": "An operation was denied. The denied resource or permission may be unknown.",
    "runtime_rejected": "Runtime validation rejected the launch or control connection. The specific rejected invariant is unknown.",
    "io_error": "An I/O or control-connection operation failed. The underlying cause may be unknown.",
    "timeout": "An operation timed out. The reason it did not complete is unknown.",
    "lock_contention": "An operation could not acquire its lock. This does not establish a missing or damaged artifact.",
    "launcher_rejected": "The native launcher rejected the request. The underlying cause is unknown.",
    "unexpected": "Bootstrap failed with an unclassified error. The underlying cause is unknown.",
}
MCP_SENTRY_MATERIALIZE_FAILURE_REASONS = frozenset(
    "artifact_digest generation_manifest io_error permissions signature "
    "unsigned_validation verification_failed".split()
)
MCP_SENTRY_MATERIALIZE_VERIFICATION_PHASES = frozenset(
    phase.value for phase in MaterializeVerificationPhase
)
_RETRYABLE_BACKEND_FAILURE_REASONS = frozenset({"timeout", "transport", "http_429", "http_5xx"})
_SENTRY_ERROR_SOURCES = frozenset({"auth", "backend", "connection", "invalid_response"})
_EVENT_LOCK = threading.Lock()
_codex_version: str | None = None
_codex_app_version = "unknown"
_NOTES_FAILURE_SIGNATURES: set[tuple[str, str, str, str]] = set()
_AUTH_FAILURE_SIGNATURES: set[tuple[str, str]] = set()
_POST_SLOTS = threading.BoundedSemaphore(_MAXIMUM_CONCURRENT_POSTS)
_USER_INTERFACE_POST_SLOTS = threading.BoundedSemaphore(_MAXIMUM_CONCURRENT_USER_INTERFACE_POSTS)
_PRESENTATION_POST_SLOTS = threading.BoundedSemaphore(_MAXIMUM_CONCURRENT_PRESENTATION_POSTS)
_HANDOFF_NOTICE_POST_SLOTS = threading.BoundedSemaphore(1)
# One replacement may emit started, SIGTERM, SIGKILL, verified exit and recovered
# before a slow post completes. Keep that full transaction within the bound.
_EXPLICIT_RECOVERY_POST_SLOTS = threading.BoundedSemaphore(5)
_MAXIMUM_EXPLICIT_RECOVERY_EVENTS = 32
_EXPLICIT_RECOVERY_BLOCK_REASONS = frozenset(
    {
        "unknown",
        "recovery-in-progress",
        "bootstrap-replacement-in-progress",
        "bootstrap-recovery-pending",
        "cooperative-handoff-declined",
        "active-or-unfinished-capture",
        "ambiguous-start",
        "capture-or-recovery-in-progress",
        "owner-responded-during-recovery",
        "compatible-replacement-unavailable",
        "terminal-bootstrap-not-quiescent",
        "owner-verification-failed",
        "unresponsive-owner-check-failed",
        "replacement-verification-failed",
        "plugin-install-failed",
        "companion-launch-failed",
        "owner-not-published",
        "owner-not-ready",
        "restart-budget-exhausted",
        "recent-audio-activity",
        "audio-activity-unavailable",
    }
)
CompanionTerminationPolicy: TypeAlias = Literal[
    "verified-idle",
    "explicit-unresponsive",
    "clicked-start",
    "terminal-bootstrap",
    "automatic-unresponsive",
    "confirmed-update",
]
_COMPANION_TERMINATION_POLICIES = frozenset(
    {
        "verified-idle",
        "explicit-unresponsive",
        "clicked-start",
        "terminal-bootstrap",
        "automatic-unresponsive",
        "confirmed-update",
    }
)
_COMPANION_TERMINATION_METHODS = frozenset({"sigterm", "sigkill", "terminate_process"})
_COMPANION_TERMINATION_OUTCOMES = frozenset({"signal_sent", "exit_confirmed"})
_explicit_recovery_events_started = 0
_UI_OPENED_POST_SLOTS = threading.BoundedSemaphore(1)
_FEEDBACK_POST_SLOTS = threading.BoundedSemaphore(2)
_events_started = 0
_user_interface_events_started = 0
_presentation_events_started = 0
_mcp_ready_reported = False
_mcp_ready_armed = False
_handoff_notice_reported = False
_pending_ui_opened_instances: dict[str, None] = {}
_reported_ui_opened_instances: dict[str, None] = {}

# Feedback attaches only actual, sanitized MCP error-report attempts in this
# process. It never ingests stderr, host/native log files, or meeting content.
_MAXIMUM_DIAGNOSTIC_EVENTS = 128
_MAXIMUM_DIAGNOSTIC_LINE_BYTES = 2_048
_MAXIMUM_DIAGNOSTIC_ATTACHMENT_BYTES = 64 * 1024
_DIAGNOSTIC_RETENTION_SECONDS = 30 * 60
_DIAGNOSTIC_LOCK = threading.Lock()
_DiagnosticScope: TypeAlias = tuple[object, int, str | None]
_diagnostic_scope: _DiagnosticScope | None = None
_diagnostic_events: deque[tuple[float, bytes]] = deque()
_diagnostic_truncated = False
MCP_SENTRY_DEVICE_SETTINGS_DIAGNOSTIC_VALUES = {
    "device_settings_action": frozenset({"getSettings", "updateSettings"}),
    "device_settings_phase": frozenset(
        {
            "preflight",
            "authentication",
            "connection",
            "cached-account",
            "native-request",
            "account-recheck",
            "projection",
        }
    ),
    "device_settings_outcome": frozenset(
        {
            "ready",
            "loading",
            "unsupported-host",
            "cached-account-missing",
            "cached-account-mismatch",
            "control-unavailable",
            "runtime-error",
            "saving",
            "native-unavailable",
            "not-editable",
            "no-supported-preferences",
            "cancelled",
        }
    ),
    "device_settings_cached_account": frozenset({"missing", "match", "mismatch"}),
    "device_settings_capability": frozenset({"true", "false"}),
    "device_settings_native_status": frozenset({"ready", "saving", "unavailable"}),
    "device_settings_can_update": frozenset({"true", "false"}),
}

_DIAGNOSTIC_TAG_VALUES = {
    **MCP_SENTRY_DEVICE_SETTINGS_DIAGNOSTIC_VALUES,
    "marketplace": _PLUGIN_MARKETPLACES | {"other", "unknown"},
    "stage": MCP_SENTRY_STAGES,
    "kind": MCP_SENTRY_KINDS,
    "operation": MCP_SENTRY_OPERATIONS,
    "error_source": _SENTRY_ERROR_SOURCES,
    "auth_requested_store": MCP_SENTRY_AUTH_REQUESTED_STORES,
    "failure_reason": (
        MCP_SENTRY_BACKEND_FAILURE_REASONS
        | MCP_SENTRY_AUTH_FAILURE_REASONS
        | MCP_SENTRY_SETTINGS_AUTH_FAILURE_REASONS
        | MCP_SENTRY_BOOTSTRAP_FAILURE_REASONS
        | MCP_SENTRY_MATERIALIZE_FAILURE_REASONS
        | {"http_401", _SETTINGS_ACTIVATION_FAILURE_REASON}
    ),
    "retryable": frozenset({"true", "false"}),
    "os": frozenset({"macos", "windows", "linux", "unknown"}),
    "presentation": MCP_SENTRY_PRESENTATIONS,
    "notification": MCP_SENTRY_NOTIFICATIONS,
    "update_reason": MCP_SENTRY_UPDATE_REASONS,
    "verification_phase": MCP_SENTRY_MATERIALIZE_VERIFICATION_PHASES,
    **MCP_SENTRY_FAILURE_DIAGNOSTIC_VALUES,
    **MCP_SENTRY_COMPANION_DIAGNOSTIC_VALUES,
    "recovery_trigger": frozenset({"user_click", "automatic"}),
    "recovery_outcome": frozenset({"started", "recovered", "failed", "blocked"}),
    "recovery_reason": _EXPLICIT_RECOVERY_BLOCK_REASONS
    | {"owner_unresponsive", "terminal_bootstrap"},
    "recovery_failure_reason": _EXPLICIT_RECOVERY_BLOCK_REASONS,
    "recovery_cause": frozenset({"owner_unresponsive", "terminal_bootstrap"}),
    "termination_outcome": _COMPANION_TERMINATION_OUTCOMES,
    "termination_method": _COMPANION_TERMINATION_METHODS,
    "termination_policy": _COMPANION_TERMINATION_POLICIES,
}
_DIAGNOSTIC_VERSION_TAGS = frozenset(
    {
        "mcp_version",
        "ui_version",
        "native_version",
        "codex_version",
        "codex_app_version",
        "active_native_version",
        "target_native_version",
    }
)


class _OptionalMcpSentryEvent(TypedDict, total=False):
    user: dict[str, str]


class _McpSentryEnvelope(_OptionalMcpSentryEvent):
    """Allowlisted JSON event sent by the local Meetings reporter."""

    event_id: str
    timestamp: str
    platform: str
    level: str
    logger: str
    message: str
    release: str
    environment: str
    tags: dict[str, str]


class McpSentryEvent(_McpSentryEnvelope, total=False):
    contexts: dict[str, dict[str, str]]


class McpSentryFeedbackEvent(_McpSentryEnvelope):
    """Explicit user feedback, separate from automatic error telemetry."""

    type: Literal["feedback"]
    contexts: dict[str, dict[str, str]]


class McpSentryDiagnostics(TypedDict, total=False):
    """Exact optional reporter arguments, including genuinely boolean retryability."""

    active_owner_version: str
    target_owner_version: str
    handoff_disposition: str
    handoff_reason: str
    recovery_kind: str
    operation: str
    error_source: str
    presentation: str
    notification: str
    update_reason: str
    failure_reason: str
    auth_requested_store: str
    verification_phase: str
    failure_operation: str
    resource_role: str
    os_error_code: str
    companion_diagnostics: dict[str, str]
    device_settings_diagnostics: dict[str, str]
    retryable: bool
    http_status: int


def _safe_regular_file(path: Path) -> bytes | None:
    try:
        metadata = path.lstat()
    except OSError:
        return None
    if (
        path.is_symlink()
        or not stat.S_ISREG(metadata.st_mode)
        or metadata.st_size <= 0
        or metadata.st_size > _MAXIMUM_METADATA_BYTES
        or (hasattr(os, "getuid") and metadata.st_uid != os.getuid())
        or (os.name != "nt" and metadata.st_mode & 0o022)
    ):
        return None
    try:
        value = path.read_bytes()
    except OSError:
        return None
    return value if len(value) == metadata.st_size else None


def _safe_component(value: object, pattern: re.Pattern[str]) -> str | None:
    return value if isinstance(value, str) and pattern.fullmatch(value) is not None else None


def is_isolated_e2e() -> bool:
    """Recognize current and previously released isolated-test gates."""

    return any(
        os.environ.get(name, "").lower() in {"1", "true"}
        for name in (
            "CHATGPT_MEETINGS_E2E_ISOLATED",
            "CHATGPT_MEETINGS_CODEX_E2E_ISOLATED",
            "SUSHI_CODEX_MEETINGS_E2E_ISOLATED",
        )
    )


def plugin_version(plugin_root: Path) -> str | None:
    """Return the validated version from a Meetings plugin manifest.

    Args:
        plugin_root: Root of the packaged Meetings plugin.

    Returns:
        The bounded plugin version, or `None` when the manifest is unavailable
        or invalid.
    """

    value = _safe_regular_file(plugin_root / ".codex-plugin" / "plugin.json")
    if value is None:
        return None
    try:
        decoded: object = json.loads(value)
    except (UnicodeDecodeError, json.JSONDecodeError):
        return None
    expected_name = (
        RUNTIME_CONFIG.server_name
        if RUNTIME_CONFIG.default_mcp_profile == "local-dev"
        else "chatgpt-meetings"
    )
    if not is_json(decoded) or decoded.get("name") != expected_name:
        return None
    return _safe_component(decoded.get("version"), _SAFE_VERSION)


def _native_metadata(plugin_root: Path) -> dict[str, str]:
    windows_version: str | None = None
    if sys.platform.startswith("win"):
        lock_path = plugin_root / "native" / "cam-windows-artifact.lock.json"
        if lock_path.parent.is_symlink():
            return {}
        if (value := _safe_regular_file(lock_path)) is not None:
            try:
                lock = json.loads(value)
                release = lock["release"]
                tag = release["tag"]
                if (
                    lock.get("schemaVersion") != 2
                    or lock.get("kind") != "chatgpt-meetings-cam-windows-distribution-lock"
                    or set(release) != {"tag", "tagSha"}
                    or not is_json(lock["platforms"])
                    or set(lock["platforms"]) != {"windows-x64", "windows-arm64"}
                    or not tag.startswith("chatgpt-meetings-v")
                    or re.fullmatch(r"[a-f0-9]{40}", release["tagSha"]) is None
                ):
                    return {}
                windows_version = _safe_component(
                    tag.removeprefix("chatgpt-meetings-v"), _SAFE_NATIVE_ALPHA_RELEASE
                )
            except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError, AttributeError):
                return {}
            if windows_version is None:
                return {}
    app_path = plugin_root / RUNTIME_CONFIG.app_name
    info_path = app_path / "Contents" / "Info.plist"
    try:
        if app_path.is_symlink() or info_path.parent.is_symlink():
            return {}
    except OSError:
        return {}
    value = _safe_regular_file(info_path)
    if value is None:
        return {"native_version": windows_version} if windows_version is not None else {}
    try:
        decoded: object = plistlib.loads(value)
    except (plistlib.InvalidFileException, ValueError, TypeError, OverflowError):
        return {}
    if (
        not is_json(decoded)
        or decoded.get("CFBundleIdentifier") != RUNTIME_CONFIG.bundle_identifier
    ):
        return {}
    result: dict[str, str] = {}
    version = windows_version or _safe_component(
        decoded.get("ChatGPTMeetingsVersion"), _SAFE_VERSION
    )
    build_timestamp = _safe_component(
        decoded.get("ChatGPTMeetingsBuildTimestampUTC"),
        _SAFE_TIMESTAMP,
    )
    dsn = decoded.get("ChatGPTMeetingsSentryDSN")
    if version is not None:
        result["native_version"] = version
    if build_timestamp is not None:
        result["native_build_timestamp"] = build_timestamp
    if isinstance(dsn, str):
        result["dsn"] = dsn
    return result


def _sentry_endpoint(dsn: object) -> tuple[str, str] | None:
    if not isinstance(dsn, str) or not dsn or any(character.isspace() for character in dsn):
        return None
    try:
        parsed = urlsplit(dsn)
        hostname = parsed.hostname
        public_key = parsed.username
        valid = (
            parsed.scheme == "https"
            and hostname is not None
            and _SAFE_SENTRY_HOST.fullmatch(hostname) is not None
            and public_key is not None
            and _SAFE_SENTRY_KEY.fullmatch(public_key) is not None
            and parsed.password is None
            and parsed.port is None
            and re.fullmatch(r"/[1-9][0-9]*", parsed.path) is not None
            and not parsed.query
            and not parsed.fragment
        )
    except ValueError:
        return None
    if not valid or hostname is None or public_key is None:
        return None
    return f"https://{hostname}/api/{parsed.path[1:]}/store/", public_key


def _cached_feedback_account() -> tuple[str, str | None] | None:
    """Read the current feedback owner without loading or refreshing credentials."""
    auth_module = sys.modules.get("codex_auth_client")
    manager = getattr(auth_module, "_process_auth_manager", None)
    if manager is None:
        return None
    try:
        material = manager.peek_cached_chatgpt_auth()
        return (material.account_id, material.subject) if material is not None else None
    except Exception:
        return None


def _cached_sentry_user_id(
    expected_account: tuple[str, str | None] | None = None,
) -> str | None:
    """Read the authenticated Codex user without loading or refreshing auth."""

    auth_module = sys.modules.get("codex_auth_client")
    if auth_module is None:
        return None
    auth_manager = getattr(auth_module, "_process_auth_manager", None)
    if auth_manager is None:
        return None
    try:
        material = auth_manager.peek_cached_chatgpt_auth()
        if material is None or (
            expected_account is not None
            and (material.account_id, material.subject) != expected_account
        ):
            return None
        auth_claim = auth_module._jwt_payload(material.token).get(auth_module._AUTH_CLAIM_NAMESPACE)
        if not is_json(auth_claim):
            return None
        user_id = auth_claim.get("user_id")
        if user_id is None:
            user_id = auth_claim.get("chatgpt_user_id")
        return _safe_component(user_id, _SAFE_SENTRY_USER_ID)
    except Exception:
        return None


def _cached_native_owner_epoch() -> str | None:
    """Read only the currently connected, verified Windows owner's cached epoch."""

    if sys.platform != "win32":
        return None
    companion_module = sys.modules.get("companion_client")
    if companion_module is None:
        return None
    try:
        diagnostics = companion_module.companion_connection_diagnostics()
        if not all(
            diagnostics.get(key) is True for key in ("ownerVerified", "connected", "initialized")
        ):
            return None
        return _safe_component(diagnostics.get("nativeOwnerEpoch"), _SAFE_NATIVE_OWNER_EPOCH)
    except Exception:
        return None


def record_codex_client_info(client_info: object) -> None:
    """Remember the initialized Codex runtime version, without retaining other client data."""

    version = (
        _safe_component(client_info.get("version"), _SAFE_CODEX_VERSION)
        if is_json(client_info) and client_info.get("name") == "codex-mcp-client"
        else None
    )
    global _codex_version, _codex_app_version
    with _EVENT_LOCK:
        _codex_version = version
        _codex_app_version = "unknown"


def record_codex_app_version(metadata: object) -> None:
    """Remember bounded desktop build metadata forwarded by the connected UI.

    Args:
        metadata: Tool-call metadata; only the dedicated version field is retained.

    Returns:
        None. Missing metadata preserves the observation for background telemetry.
    """

    if not is_json(metadata) or "chatgpt-meetings/codex-app-version" not in metadata:
        return
    version = _safe_component(metadata["chatgpt-meetings/codex-app-version"], _SAFE_CODEX_VERSION)
    global _codex_app_version
    with _EVENT_LOCK:
        _codex_app_version = version or "unknown"


def codex_app_version() -> str:
    """Read the observed desktop version without probing the host or authentication.

    Returns:
        The bounded desktop build, or `unknown` before a supported UI connects.
    """

    with _EVENT_LOCK:
        return _codex_app_version


def cached_metrics_account_matches(
    expected_account: tuple[str, str | None],
) -> bool:
    """Confirm cached auth still belongs to the reporting account without refreshing."""

    auth_module = sys.modules.get("codex_auth_client")
    if auth_module is None:
        return False
    auth_manager = getattr(auth_module, "_process_auth_manager", None)
    if auth_manager is None:
        return False
    try:
        material = auth_manager.peek_cached_chatgpt_auth()
        return material is not None and (material.account_id, material.subject) == expected_account
    except Exception:
        return False


def build_mcp_sentry_event(
    stage: object,
    kind: object,
    *,
    ui_version: object = None,
    mcp_build_timestamp: object = None,
    active_owner_version: object = None,
    target_owner_version: object = None,
    handoff_disposition: object = None,
    handoff_reason: object = None,
    recovery_kind: object = None,
    operation: object = None,
    error_source: object = None,
    presentation: object = None,
    notification: object = None,
    update_reason: object = None,
    failure_reason: object = None,
    auth_requested_store: object = None,
    verification_phase: object = None,
    failure_operation: object = None,
    resource_role: object = None,
    os_error_code: object = None,
    companion_diagnostics: object = None,
    device_settings_diagnostics: object = None,
    retryable: object = None,
    http_status: object = None,
    lifecycle: bool = False,
    recovered_handoff: bool = False,
    plugin_root: Path = _PLUGIN_ROOT,
) -> tuple[str, str, McpSentryEvent] | None:
    """Build one allowlisted event without accepting raw error or request data.

    Args:
        stage: Candidate lifecycle stage.
        kind: Candidate error kind.
        ui_version: Candidate widget version.
        mcp_build_timestamp: Candidate MCP build timestamp.
        active_owner_version: Candidate authenticated active-owner version.
        target_owner_version: Candidate authenticated target-owner version.
        handoff_disposition: Candidate handoff outcome.
        handoff_reason: Candidate bounded native update handoff failure cause.
        recovery_kind: Candidate recovery classification.
        operation: Candidate bounded user operation.
        error_source: Candidate bounded error source.
        presentation: Candidate bounded visible notification surface.
        notification: Candidate bounded visible notification classification.
        update_reason: Candidate bounded user-confirmed native update failure.
        failure_reason: Candidate bounded auth, backend, or native failure classification.
        auth_requested_store: Auth child's requested store, not its managed effective store.
        verification_phase: Candidate bounded native materialization verification boundary.
        failure_operation: Candidate bounded bootstrap or Stop failure operation.
        resource_role: Candidate bounded failure resource role, never a path.
        os_error_code: Candidate bounded operating-system error code.
        companion_diagnostics: Last observed, finite companion context; not a fresh probe.
        device_settings_diagnostics: Finite observations from this device-settings request.
        retryable: Whether the classified Notes/settings backend failure may be retried.
        http_status: Candidate settings HTTP response status, never response contents.
        lifecycle: Whether to emit the internal correlated MCP-ready event.
        recovered_handoff: Whether an authenticated bootstrap handoff recovered.
        plugin_root: Root of the packaged Meetings plugin.

    Returns:
        The Sentry endpoint, public key, and allowlisted event, or `None` when
        configuration or candidate metadata is invalid.
    """

    if (
        not isinstance(stage, str)
        or stage not in MCP_SENTRY_STAGES
        or not isinstance(kind, str)
        or kind not in MCP_SENTRY_KINDS
    ):
        return None
    safe_ui_version = _safe_component(ui_version, _SAFE_VERSION)
    if (ui_version is not None and safe_ui_version is None) or (
        lifecycle and (safe_ui_version is not None or (stage, kind) != ("bootstrap", "launch"))
    ):
        return None
    if type(recovered_handoff) is not bool or (
        recovered_handoff
        and (
            (stage, kind) != ("handoff", "handoff")
            or safe_ui_version is not None
            or lifecycle
            or mcp_build_timestamp is not None
            or handoff_disposition is not None
            or recovery_kind is not None
            or operation is not None
            or presentation is not None
            or notification is not None
            or error_source is not None
            or update_reason is not None
            or failure_reason is not None
            or retryable is not None
        )
    ):
        return None
    safe_mcp_build_timestamp = _safe_component(mcp_build_timestamp, _SAFE_TIMESTAMP)
    if mcp_build_timestamp is not None and safe_mcp_build_timestamp is None:
        return None
    if is_isolated_e2e():
        return None

    mcp_version = plugin_version(plugin_root)
    native_metadata = _native_metadata(plugin_root)
    endpoint = _sentry_endpoint(native_metadata.get("dsn"))
    if endpoint is None:
        endpoint = _sentry_endpoint(os.environ.get("CHATGPT_MEETINGS_SENTRY_DSN"))
    if mcp_version is None or endpoint is None:
        return None
    component = "chatgpt-meetings-ui" if safe_ui_version is not None else "chatgpt-meetings-mcp"
    is_native_handoff_error = safe_ui_version is None and stage == "handoff" and kind == "handoff"
    is_presentation_event = isinstance(presentation, str) and (
        presentation in MCP_SENTRY_PRESENTATIONS
    )
    tags: dict[str, str] = {
        "surface": (
            "chatgpt_meetings_ui" if safe_ui_version is not None else "chatgpt_meetings_mcp"
        ),
        "stage": stage,
        "kind": kind,
        "event_type": "notice"
        if recovered_handoff
        else "user_visible"
        if is_presentation_event
        else "error",
        "mcp_version": mcp_version,
        "app_version": mcp_version,
        "sessionId": _SENTRY_SESSION_ID,
        "os": (
            "macos"
            if sys.platform == "darwin"
            else "windows"
            if sys.platform.startswith("win")
            else "linux"
            if sys.platform.startswith("linux")
            else "unknown"
        ),
    }
    if safe_ui_version is not None:
        # Preserve unknown for a retained UI whose version is unavailable.
        # Other caller versions stay clamped to avoid exfiltration tags.
        tags["ui_version"] = "unknown" if safe_ui_version == "unknown" else mcp_version
    if safe_mcp_build_timestamp is not None:
        tags["mcp_build_timestamp"] = safe_mcp_build_timestamp
    tags.update(
        {
            key: value
            for key, value in native_metadata.items()
            if key in {"native_version", "native_build_timestamp"}
        }
    )
    # Owner versions are supplied only after the caller authenticates the
    # native owner. Reject malformed diagnostics without losing the error.
    owner_version_pattern = _SAFE_NATIVE_ALPHA_RELEASE if is_native_handoff_error else _SAFE_VERSION
    active_native_version = _safe_component(active_owner_version, owner_version_pattern)
    if active_native_version is not None and active_native_version.lower() != "unknown":
        tags["active_native_version"] = active_native_version
    target_native_version = _safe_component(target_owner_version, owner_version_pattern)
    if is_native_handoff_error and target_native_version is None:
        packaged_native_version = _safe_component(
            native_metadata.get("native_version"),
            _SAFE_NATIVE_ALPHA_RELEASE,
        )
        if target_owner_version is None or (
            isinstance(target_owner_version, str)
            and packaged_native_version is not None
            and target_owner_version == packaged_native_version.split("-alpha.", 1)[0]
        ):
            target_native_version = packaged_native_version
    if target_native_version is not None and target_native_version.lower() != "unknown":
        tags["target_native_version"] = target_native_version
    if is_native_handoff_error:
        tags["operation"] = "update"
        tags["handoff_outcome"] = "recovered" if recovered_handoff else "failed"
        if type(handoff_reason) is str and handoff_reason in MCP_SENTRY_HANDOFF_FAILURE_REASONS:
            tags["handoff_reason"] = handoff_reason
    if isinstance(handoff_disposition, str) and (
        handoff_disposition in _SENTRY_HANDOFF_DISPOSITIONS
    ):
        tags["handoff_outcome"] = handoff_disposition
    if isinstance(recovery_kind, str) and recovery_kind in _SENTRY_RECOVERY_KINDS:
        tags["recovery_kind"] = recovery_kind
    if (
        not is_native_handoff_error
        and isinstance(operation, str)
        and operation in MCP_SENTRY_OPERATIONS
        and (
            operation != "stop"
            or (safe_ui_version is None and stage == "recording" and kind == "connection")
        )
    ):
        tags["operation"] = operation
    if isinstance(error_source, str) and error_source in _SENTRY_ERROR_SOURCES:
        tags["error_source"] = error_source
    if isinstance(presentation, str) and presentation in MCP_SENTRY_PRESENTATIONS:
        tags["presentation"] = presentation
    if isinstance(notification, str) and notification in MCP_SENTRY_NOTIFICATIONS:
        tags["notification"] = notification
    if (
        isinstance(update_reason, str)
        and update_reason in MCP_SENTRY_UPDATE_REASONS
        and operation == "update"
        and (
            (
                safe_ui_version is None
                and (stage, kind) == ("bootstrap", "runtime")
                and notification is None
                and presentation is None
            )
            or (
                safe_ui_version is not None
                and (stage, kind) == ("popup", "update")
                and notification == "update_failed"
                and (presentation is None or presentation == "dialog")
            )
        )
    ):
        tags["update_reason"] = update_reason
    if (
        safe_ui_version is None
        and not lifecycle
        and type(failure_reason) is str
        and (
            (stage, kind) == ("bootstrap", "launch")
            and failure_reason in MCP_SENTRY_BOOTSTRAP_FAILURE_REASONS
            or (stage, kind) == ("materialize", "verify")
            and failure_reason in MCP_SENTRY_MATERIALIZE_FAILURE_REASONS
        )
        and retryable is None
    ):
        tags["failure_reason"] = failure_reason
    if (
        (stage, kind) == ("auth", "auth")
        and safe_ui_version is None
        and not is_presentation_event
        and type(failure_reason) is str
        and failure_reason in MCP_SENTRY_AUTH_FAILURE_REASONS
        and type(auth_requested_store) is str
        and auth_requested_store in MCP_SENTRY_AUTH_REQUESTED_STORES
    ):
        tags["failure_reason"] = failure_reason
        tags["auth_requested_store"] = auth_requested_store
    if (
        (stage, kind) == ("materialize", "verify")
        and safe_ui_version is None
        and not is_presentation_event
        and type(verification_phase) is str
        and verification_phase in MCP_SENTRY_MATERIALIZE_VERIFICATION_PHASES
    ):
        tags["verification_phase"] = verification_phase
    if (
        safe_ui_version is None
        and stage in {"notes", "settings"}
        and kind == "backend"
        and isinstance(failure_reason, str)
        and failure_reason in MCP_SENTRY_BACKEND_FAILURE_REASONS
        and isinstance(retryable, bool)
        and retryable == (failure_reason in _RETRYABLE_BACKEND_FAILURE_REASONS)
    ):
        tags["failure_reason"] = failure_reason
        tags["retryable"] = "true" if retryable else "false"
        if stage == "settings" and type(http_status) is int and 100 <= http_status <= 599:
            tags["http_status"] = str(http_status)
    if (
        safe_ui_version is None
        and stage == "settings"
        and kind in {"auth", "backend"}
        and type(retryable) is bool
        and isinstance(failure_reason, str)
        and (
            error_source == "auth"
            and failure_reason in MCP_SENTRY_SETTINGS_AUTH_FAILURE_REASONS
            or error_source == "backend"
            and failure_reason == "http_401"
            and type(http_status) is int
            and http_status == 401
            or error_source == "backend"
            and failure_reason in MCP_SENTRY_BACKEND_FAILURE_REASONS
            and retryable == (failure_reason in _RETRYABLE_BACKEND_FAILURE_REASONS)
        )
    ):
        tags["failure_reason"] = failure_reason
        tags["retryable"] = "true" if retryable else "false"
        if error_source == "backend" and type(http_status) is int and 100 <= http_status <= 599:
            tags["http_status"] = str(http_status)
    if (
        (stage, kind) == ("settings", "backend")
        and safe_ui_version is None
        and not is_presentation_event
        and operation == "settings"
        and error_source == "backend"
        and failure_reason == _SETTINGS_ACTIVATION_FAILURE_REASON
        and retryable is None
        and http_status is None
    ):
        tags["failure_reason"] = _SETTINGS_ACTIVATION_FAILURE_REASON
    if lifecycle:
        native_version = _safe_component(
            native_metadata.get("native_version"), _SAFE_NATIVE_ALPHA_RELEASE
        )
        if native_version is None:
            return None
        tags = {
            "surface": "chatgpt_meetings_mcp",
            "event_type": "lifecycle",
            "os": tags["os"],
            "mcp_version": mcp_version,
            "ui_version": mcp_version,
            "target_native_version": native_version,
            "sessionId": _SENTRY_SESSION_ID,
        }
    tags["marketplace"] = plugin_marketplace(plugin_root)
    if native_owner_epoch := _cached_native_owner_epoch():
        tags["native_owner_epoch"] = native_owner_epoch
    with _EVENT_LOCK:
        tags["codex_app_version"] = _codex_app_version
        if _codex_version is not None:
            tags["codex_version"] = _codex_version
    event: McpSentryEvent = {
        "event_id": uuid.uuid4().hex,
        "timestamp": datetime.now(timezone.utc)
        .isoformat(timespec="seconds")
        .replace("+00:00", "Z"),
        "platform": "python",
        "level": "info"
        if lifecycle or recovered_handoff
        else "warning"
        if is_presentation_event
        else "error",
        "logger": component,
        "message": "chatgpt_meetings.lifecycle.mcp_ready"
        if lifecycle
        else f"{component}:{stage}:{kind}:recovered"
        if recovered_handoff
        else f"{component}:{stage}:{kind}:user_visible"
        if is_presentation_event
        else f"{component}:{stage}:{kind}",
        "release": f"{component}@{mcp_version}",
        "environment": RUNTIME_CONFIG.flavor,
        "tags": tags,
    }
    is_bootstrap_failure = (stage, kind) == ("bootstrap", "launch") and "failure_reason" in tags
    is_stop_connection_failure = (
        (stage, kind) == ("recording", "connection")
        and tags.get("operation") == "stop"
        and safe_ui_version is None
        and any(value is not None for value in (failure_operation, resource_role, os_error_code))
    )
    if is_bootstrap_failure or is_stop_connection_failure:
        for key, candidate in (
            ("failure_operation", failure_operation),
            ("resource_role", resource_role),
            ("os_error_code", os_error_code),
        ):
            tags[key] = (
                candidate
                if type(candidate) is str and candidate in MCP_SENTRY_FAILURE_DIAGNOSTIC_VALUES[key]
                else "unknown"
            )
    if is_bootstrap_failure:
        event["contexts"] = {
            "bootstrap_failure": {
                "explanation": _BOOTSTRAP_FAILURE_EXPLANATIONS[tags["failure_reason"]],
                "cause_certainty": "unconfirmed",
            }
        }
    if (
        (stage, kind) == ("recording", "connection")
        and is_json(companion_diagnostics)
        and type(companion_diagnostics) is dict
    ):
        for key, allowed in MCP_SENTRY_COMPANION_DIAGNOSTIC_VALUES.items():
            candidate = companion_diagnostics.get(key)
            if type(candidate) is str and candidate in allowed:
                tags[key] = candidate
    if (
        (stage, kind) == ("settings", "runtime")
        and safe_ui_version is None
        and not is_presentation_event
        and is_json(device_settings_diagnostics)
        and type(device_settings_diagnostics) is dict
    ):
        for key, allowed in MCP_SENTRY_DEVICE_SETTINGS_DIAGNOSTIC_VALUES.items():
            candidate = device_settings_diagnostics.get(key)
            if type(candidate) is str and candidate in allowed:
                tags[key] = candidate
    if user_id := _cached_sentry_user_id():
        event["user"] = {"id": user_id}
    return endpoint[0], endpoint[1], event


def build_mcp_ready_event(
    *,
    plugin_root: Path = _PLUGIN_ROOT,
) -> tuple[str, str, McpSentryEvent] | None:
    """Build one correlated ready event using the common verified Sentry envelope."""
    return build_mcp_sentry_event("bootstrap", "launch", lifecycle=True, plugin_root=plugin_root)


def build_ui_opened_event(
    *,
    plugin_root: Path = _PLUGIN_ROOT,
) -> tuple[str, str, McpSentryEvent] | None:
    """Build a mounted-UI lifecycle event only for an authenticated user."""

    prepared = build_mcp_sentry_event("bootstrap", "launch", plugin_root=plugin_root)
    if prepared is None or prepared[2].get("user") is None:
        return None
    event = prepared[2]
    event["message"] = "chatgpt_meetings.lifecycle.ui_opened"
    event["level"] = "info"
    event["tags"]["event_type"] = "lifecycle"
    return prepared


def plugin_marketplace(plugin_root: Path) -> str:
    from native_runtime_stable import plugin_cache_family_root

    family_root = plugin_cache_family_root(plugin_root)
    if family_root is None:
        return "unknown"
    # Attribute the running installation, not the build profile or update target.
    marketplace = family_root.parent.name
    return marketplace if marketplace in _PLUGIN_MARKETPLACES else "other"


def _cached_diagnostic_scope(
    *, expected_account: tuple[str, str | None] | None = None
) -> _DiagnosticScope | None:
    """Read an opaque in-memory owner fence, never load or refresh credentials."""
    auth_module = sys.modules.get("codex_auth_client")
    manager = getattr(auth_module, "_process_auth_manager", None)
    if manager is None:
        return (None, 0, None) if expected_account is None else None
    try:
        scope: tuple[object, ...] = manager.peek_diagnostic_scope(expected_account=expected_account)
        if (
            len(scope) == 2
            and type(scope[0]) is int
            and (scope[1] is None or isinstance(scope[1], str))
        ):
            if expected_account is not None and scope[1] is None:
                return None
            return manager, scope[0], scope[1]
    except Exception:
        pass
    return None


def _diagnostic_record(event: McpSentryEvent) -> dict[str, str]:
    """Project a second, strict allowlist; never retain event user or contexts."""
    record = {"sessionId": _SENTRY_SESSION_ID}
    event_id = event.get("event_id", "")
    if re.fullmatch(r"[a-f0-9]{32}", event_id) is not None:
        record["event_id"] = event_id
    timestamp = event.get("timestamp", "")
    if _SAFE_TIMESTAMP.fullmatch(timestamp) is not None:
        record["timestamp"] = timestamp
    for key, value in event.get("tags", {}).items():
        if key in _DIAGNOSTIC_TAG_VALUES and value in _DIAGNOSTIC_TAG_VALUES[key]:
            record[key] = value
        elif key in _DIAGNOSTIC_VERSION_TAGS and (
            value == "unknown" or _SAFE_CODEX_VERSION.fullmatch(value) is not None
        ):
            record[key] = value
        elif key == "http_status" and re.fullmatch(r"[1-5][0-9]{2}", value) is not None:
            record[key] = value
    return record


def _scope_diagnostic_history_locked(scope: _DiagnosticScope, now: float) -> None:
    global _diagnostic_scope, _diagnostic_truncated
    if _diagnostic_scope != scope:
        _diagnostic_events.clear()
        _diagnostic_scope = scope
        _diagnostic_truncated = False
    while _diagnostic_events and now - _diagnostic_events[0][0] > _DIAGNOSTIC_RETENTION_SECONDS:
        _diagnostic_events.popleft()


def _record_diagnostic_event(event: McpSentryEvent, scope: _DiagnosticScope | None) -> None:
    """Retain real report attempts, even when automatic Sentry capacity is full."""
    if scope is None or _cached_diagnostic_scope() != scope:
        return
    line = json.dumps(_diagnostic_record(event), sort_keys=True, separators=(",", ":")).encode(
        "ascii"
    )
    if len(line) > _MAXIMUM_DIAGNOSTIC_LINE_BYTES:
        return
    global _diagnostic_truncated
    with _DIAGNOSTIC_LOCK:
        now = time.monotonic()
        _scope_diagnostic_history_locked(scope, now)
        while len(_diagnostic_events) >= _MAXIMUM_DIAGNOSTIC_EVENTS:
            _diagnostic_events.popleft()
            _diagnostic_truncated = True
        _diagnostic_events.append((now, line))


def _feedback_diagnostic_attachment(event: McpSentryEvent, scope: _DiagnosticScope | None) -> bytes:
    if scope is None or _cached_diagnostic_scope() != scope:
        raise RuntimeError("Feedback diagnostics are unavailable after an account change")
    with _DIAGNOSTIC_LOCK:
        _scope_diagnostic_history_locked(scope, time.monotonic())
        lines = [line for _, line in _diagnostic_events]
        truncated = _diagnostic_truncated
    # Reserve a small bounded header so the newest complete records fit exactly.
    remaining = _MAXIMUM_DIAGNOSTIC_ATTACHMENT_BYTES - 2_048
    recent: list[bytes] = []
    for line in reversed(lines):
        if len(line) + 1 > remaining:
            truncated = True
            break
        recent.append(line)
        remaining -= len(line) + 1
    header = {
        "source": "meetings_mcp_in_process_diagnostics",
        "status": "recent_events" if recent else "no_recent_events",
        "event_count": len(recent),
        "retention_seconds": _DIAGNOSTIC_RETENTION_SECONDS,
        "truncated": truncated,
        "snapshot": _diagnostic_record(event),
    }
    payload = (
        b"\n".join(
            [
                json.dumps(header, sort_keys=True, separators=(",", ":")).encode("ascii"),
                *reversed(recent),
            ]
        )
        + b"\n"
    )
    if len(payload) > _MAXIMUM_DIAGNOSTIC_ATTACHMENT_BYTES:
        raise RuntimeError("Feedback diagnostics exceed the attachment limit")
    return payload


def submit_user_feedback(
    feedback_text: str,
    *,
    cancellation_event: threading.Event | None = None,
    plugin_root: Path = _PLUGIN_ROOT,
) -> str:
    """Send an explicit Home feedback message and acknowledge only accepted delivery.

    Uses Sentry's feedback envelope, without sampling, automatic retries, meeting
    content, or the slots reserved for operational errors. Attach bounded recent
    in-process diagnostics; this is not a collection of host/native log files.
    """

    if not feedback_text.strip() or len(feedback_text) > 2_000:
        raise ValueError("feedbackText must contain 1 to 2000 characters")
    if cancellation_event is not None and cancellation_event.is_set():
        raise RuntimeError("Feedback was cancelled")
    expected_account = _cached_feedback_account()
    scope = capture_feedback_diagnostic_scope(expected_account=expected_account)
    if expected_account is None and scope is not None and scope[2] is not None:
        raise RuntimeError("Feedback diagnostics are unavailable after an account change")
    return _submit_feedback_envelope(
        feedback_text.strip(),
        source="meetings_home",
        scope=scope,
        expected_account=expected_account,
        cancellation_event=cancellation_event,
        plugin_root=plugin_root,
    )


def capture_feedback_diagnostic_scope(
    *, expected_account: tuple[str, str | None] | None = None
) -> _DiagnosticScope | None:
    """Capture the owner fence before a feedback mutation, without auth IO."""
    return _cached_diagnostic_scope(expected_account=expected_account)


def submit_feedback_diagnostics(
    related_feedback_id: str,
    *,
    expected_account: tuple[str, str | None],
    expected_scope: _DiagnosticScope | None,
    plugin_root: Path = _PLUGIN_ROOT,
) -> str:
    """Attach local logs to a separate plugin event linked to accepted Record feedback.

    Record feedback belongs to a different Sentry project. Its event id is only
    a bounded correlation tag; this envelope always receives its own event id.
    """
    if re.fullmatch(r"[a-f0-9]{32}", related_feedback_id) is None:
        raise ValueError("Feedback correlation id is invalid")
    return _submit_feedback_envelope(
        "Diagnostic logs for meeting feedback",
        source="meetings_note",
        scope=expected_scope,
        expected_account=expected_account,
        related_feedback_id=related_feedback_id,
        plugin_root=plugin_root,
    )


def _submit_feedback_envelope(
    feedback_text: str,
    *,
    source: Literal["meetings_home", "meetings_note"],
    scope: _DiagnosticScope | None,
    expected_account: tuple[str, str | None] | None = None,
    related_feedback_id: str | None = None,
    cancellation_event: threading.Event | None = None,
    plugin_root: Path,
) -> str:
    prepared = build_mcp_sentry_event(
        "interactions",
        "host-action",
        ui_version=plugin_version(plugin_root),
        operation="feedback",
        plugin_root=plugin_root,
    )
    if prepared is None or not _FEEDBACK_POST_SLOTS.acquire(blocking=False):
        raise RuntimeError("Feedback is unavailable")
    try:
        endpoint, public_key, base_event = prepared
        attachment = _feedback_diagnostic_attachment(base_event, scope)
        event: McpSentryFeedbackEvent = {
            **base_event,
            "type": "feedback",
            "level": "info",
            "message": "Meetings user feedback",
            "contexts": {"feedback": {"message": feedback_text, "source": source}},
        }
        # The base event can observe a transient owner while auth changes.
        # Only immutable auth material matching the feedback owner may identify it.
        event.pop("user", None)
        if expected_account is not None:
            user_id = _cached_sentry_user_id(expected_account)
            if user_id is not None:
                event["user"] = {"id": user_id}
        event["tags"]["event_type"] = "feedback"
        event["tags"].pop("kind", None)
        if related_feedback_id is not None:
            event["tags"]["record_feedback_event_id"] = related_feedback_id
        payload = json.dumps(event, ensure_ascii=True, separators=(",", ":")).encode("ascii")
        envelope = b"\n".join(
            (
                json.dumps({"event_id": event["event_id"], "sent_at": event["timestamp"]}).encode(),
                json.dumps({"type": "feedback", "length": len(payload)}).encode(),
                payload,
                json.dumps(
                    {
                        "type": "attachment",
                        "filename": "meetings-mcp-diagnostics.log",
                        "content_type": "text/plain",
                        "length": len(attachment),
                    }
                ).encode(),
                attachment,
                b"",
            )
        )
        if _cached_diagnostic_scope() != scope:
            raise RuntimeError("Feedback diagnostics are unavailable after an account change")
        request = Request(
            endpoint.removesuffix("store/") + "envelope/",
            data=envelope,
            headers={
                "Content-Type": "application/x-sentry-envelope",
                "User-Agent": "chatgpt-meetings-mcp",
                "X-Sentry-Auth": f"Sentry sentry_version=7, sentry_key={public_key}",
            },
            method="POST",
        )
        opener = build_opener(NoRedirectHandler(), HTTPSHandler(context=create_https_context()))
        # The RPC owner may have changed before Home captured its current scope.
        # Retain that earlier cancellation fence until the POST begins. Once sent,
        # preserve an accepted acknowledgement rather than invite a duplicate send.
        if cancellation_event is not None and cancellation_event.is_set():
            raise RuntimeError("Feedback was cancelled")
        with opener.open(request, timeout=5.0) as response:
            if not 200 <= response.status < 300:
                raise RuntimeError("Feedback was not accepted")
        return event["event_id"]
    finally:
        _FEEDBACK_POST_SLOTS.release()


def _post_mcp_sentry_event(
    endpoint: str,
    public_key: str,
    event: McpSentryEvent,
    presentation_slot_acquired: bool = False,
    user_interface_slot_acquired: bool = False,
    release_error_slot: bool = True,
    handoff_notice_slot_acquired: bool = False,
) -> None:
    try:
        request = Request(
            endpoint,
            data=json.dumps(event, separators=(",", ":"), ensure_ascii=True).encode("ascii"),
            headers={
                "Content-Type": "application/json",
                "User-Agent": "chatgpt-meetings-mcp",
                "X-Sentry-Auth": f"Sentry sentry_version=7, sentry_key={public_key}",
            },
            method="POST",
        )
        with build_opener(NoRedirectHandler(), HTTPSHandler(context=create_https_context())).open(
            request,
            timeout=_POST_TIMEOUT_SECONDS,
        ):
            pass
    except Exception:
        # Telemetry is best effort and must never affect JSON-RPC or bootstrap.
        pass
    finally:
        if release_error_slot:
            _POST_SLOTS.release()
        if presentation_slot_acquired:
            _PRESENTATION_POST_SLOTS.release()
        if user_interface_slot_acquired:
            _USER_INTERFACE_POST_SLOTS.release()
        if handoff_notice_slot_acquired:
            _HANDOFF_NOTICE_POST_SLOTS.release()


def _post_ui_opened_event(
    endpoint: str,
    public_key: str,
    event: McpSentryEvent,
) -> None:
    """Keep mounted-UI lifecycle transport separate from error capacity."""

    try:
        _post_mcp_sentry_event(endpoint, public_key, event, False, False, False)
    finally:
        _UI_OPENED_POST_SLOTS.release()


def report_recovered_handoff(
    *,
    active_owner_version: str | None = None,
    target_owner_version: str | None = None,
    handoff_reason: str | None = None,
) -> bool:
    """Report one recovered owner handoff without consuming error capacity."""

    global _handoff_notice_reported
    acquired = False
    marked = False
    try:
        prepared = build_mcp_sentry_event(
            "handoff",
            "handoff",
            active_owner_version=active_owner_version,
            target_owner_version=target_owner_version,
            handoff_reason=handoff_reason,
            recovered_handoff=True,
        )
        if prepared is None or not _HANDOFF_NOTICE_POST_SLOTS.acquire(blocking=False):
            return False
        acquired = True
        with _EVENT_LOCK:
            if _handoff_notice_reported:
                _HANDOFF_NOTICE_POST_SLOTS.release()
                acquired = False
                return False
            _handoff_notice_reported = True
            marked = True
        threading.Thread(
            target=_post_mcp_sentry_event,
            args=(*prepared, False, False, False, True),
            name="chatgpt-meetings-handoff-notice",
            daemon=True,
        ).start()
        return True
    except Exception:
        if marked:
            with _EVENT_LOCK:
                _handoff_notice_reported = False
        if acquired:
            _HANDOFF_NOTICE_POST_SLOTS.release()
        return False


def build_explicit_recovery_event(
    *,
    outcome: object,
    operation: object,
    active_owner_version: object = None,
    target_owner_version: object = None,
    blocked_reason: object = None,
    recovery_reason: object = "owner_unresponsive",
    plugin_root: Path = _PLUGIN_ROOT,
) -> tuple[str, str, McpSentryEvent] | None:
    """Build a finite recovery event through the shared sanitized envelope."""

    if type(outcome) is not str or outcome not in {"started", "recovered", "failed", "blocked"}:
        return None
    if type(operation) is not str or operation not in {"start", "reconnect", "bootstrap"}:
        return None
    if type(recovery_reason) is not str or recovery_reason not in {
        "owner_unresponsive",
        "terminal_bootstrap",
    }:
        return None
    prepared = build_mcp_sentry_event(
        "recording",
        "recovery",
        operation="start" if operation == "start" else "recovery",
        active_owner_version=active_owner_version,
        target_owner_version=target_owner_version,
        plugin_root=plugin_root,
    )
    if prepared is None:
        return None
    event = prepared[2]
    event["level"] = (
        "error" if outcome == "failed" else "warning" if outcome == "blocked" else "info"
    )
    event["message"] = f"chatgpt-meetings-mcp:recording:recovery:{outcome}"
    event["tags"].update(
        {
            "event_type": "error" if outcome == "failed" else "notice",
            "recovery_trigger": "automatic" if operation == "bootstrap" else "user_click",
            "recovery_reason": recovery_reason,
            "recovery_cause": recovery_reason,
            "recovery_outcome": outcome,
        }
    )
    if outcome == "blocked":
        event["tags"]["recovery_reason"] = (
            blocked_reason
            if type(blocked_reason) is str and blocked_reason in _EXPLICIT_RECOVERY_BLOCK_REASONS
            else "unknown"
        )
    elif outcome == "failed":
        event["tags"]["recovery_failure_reason"] = (
            blocked_reason
            if type(blocked_reason) is str and blocked_reason in _EXPLICIT_RECOVERY_BLOCK_REASONS
            else "unknown"
        )
    return prepared


def build_companion_termination_event(
    *,
    outcome: object,
    policy: object,
    active_owner_version: object = None,
    method: object = None,
    plugin_root: Path = _PLUGIN_ROOT,
) -> tuple[str, str, McpSentryEvent] | None:
    """Report a completed OS signal call or verified exit, never an attempted kill."""

    if type(outcome) is not str or outcome not in _COMPANION_TERMINATION_OUTCOMES:
        return None
    if type(policy) is not str or policy not in _COMPANION_TERMINATION_POLICIES:
        return None
    if outcome == "signal_sent":
        if type(method) is not str or method not in _COMPANION_TERMINATION_METHODS:
            return None
    elif method is not None:
        return None
    prepared = build_mcp_sentry_event(
        "handoff",
        "recovery",
        operation="recovery",
        active_owner_version=active_owner_version,
        plugin_root=plugin_root,
    )
    if prepared is None:
        return None
    event = prepared[2]
    event["level"] = "info"
    event["message"] = f"chatgpt-meetings-mcp:handoff:termination:{outcome}"
    event["tags"].update(
        {
            "event_type": "notice",
            "termination_outcome": outcome,
            "termination_policy": policy,
        }
    )
    if isinstance(method, str):
        event["tags"]["termination_method"] = method
    return prepared


def _post_explicit_recovery_event(endpoint: str, public_key: str, event: McpSentryEvent) -> None:
    try:
        _post_mcp_sentry_event(endpoint, public_key, event, False, False, False)
    finally:
        _EXPLICIT_RECOVERY_POST_SLOTS.release()


def report_explicit_recovery(
    *,
    outcome: Literal["started", "recovered", "failed", "blocked"],
    operation: Literal["start", "reconnect", "bootstrap"],
    active_owner_version: str | None = None,
    target_owner_version: str | None = None,
    blocked_reason: str | None = None,
    recovery_reason: Literal["owner_unresponsive", "terminal_bootstrap"] = "owner_unresponsive",
) -> bool:
    """Report bounded recovery stages without consuming recording-error capacity."""

    try:
        prepared = build_explicit_recovery_event(
            outcome=outcome,
            operation=operation,
            active_owner_version=active_owner_version,
            target_owner_version=target_owner_version,
            blocked_reason=blocked_reason,
            recovery_reason=recovery_reason,
        )
    except Exception:
        return False
    return _report_recovery_event(prepared)


def report_companion_termination(
    *,
    outcome: Literal["signal_sent", "exit_confirmed"],
    policy: CompanionTerminationPolicy,
    active_owner_version: str,
    method: Literal["sigterm", "sigkill", "terminate_process"] | None = None,
) -> bool:
    """Queue finite termination evidence through the existing recovery report budget."""

    try:
        prepared = build_companion_termination_event(
            outcome=outcome,
            policy=policy,
            active_owner_version=active_owner_version,
            method=method,
        )
    except Exception:
        return False
    return _report_recovery_event(prepared)


def _report_recovery_event(prepared: tuple[str, str, McpSentryEvent] | None) -> bool:
    global _explicit_recovery_events_started
    acquired = False
    counted = False
    try:
        if prepared is not None:
            _record_diagnostic_event(prepared[2], _cached_diagnostic_scope())
        if prepared is None or not _EXPLICIT_RECOVERY_POST_SLOTS.acquire(blocking=False):
            return False
        acquired = True
        with _EVENT_LOCK:
            if _explicit_recovery_events_started >= _MAXIMUM_EXPLICIT_RECOVERY_EVENTS:
                _EXPLICIT_RECOVERY_POST_SLOTS.release()
                acquired = False
                return False
            _explicit_recovery_events_started += 1
            counted = True
        threading.Thread(
            target=_post_explicit_recovery_event,
            args=prepared,
            name="chatgpt-meetings-recovery",
            daemon=True,
        ).start()
        return True
    except Exception:
        if counted:
            with _EVENT_LOCK:
                _explicit_recovery_events_started -= 1
        if acquired:
            _EXPLICIT_RECOVERY_POST_SLOTS.release()
        return False


def report_ui_opened(
    *,
    app_instance_id: str | None = None,
    auth_settled: bool = False,
) -> bool:
    """Report each mounted surface once after its authenticated user is known."""

    instance_to_report: str | None = None
    acquired = False
    marked = False
    try:
        with _EVENT_LOCK:
            if auth_settled:
                if app_instance_id is not None or not _pending_ui_opened_instances:
                    return False
            else:
                if (
                    not isinstance(app_instance_id, str)
                    or _SAFE_UI_APP_INSTANCE_ID.fullmatch(app_instance_id) is None
                    or app_instance_id in _reported_ui_opened_instances
                ):
                    return False
                if app_instance_id not in _pending_ui_opened_instances:
                    if len(_pending_ui_opened_instances) >= _MAXIMUM_TRACKED_UI_OPENED_INSTANCES:
                        _pending_ui_opened_instances.pop(next(iter(_pending_ui_opened_instances)))
                    _pending_ui_opened_instances[app_instance_id] = None

        if _cached_sentry_user_id() is None:
            return False
        prepared = build_ui_opened_event()
        if prepared is None or not _UI_OPENED_POST_SLOTS.acquire(blocking=False):
            return False
        acquired = True

        with _EVENT_LOCK:
            if not _pending_ui_opened_instances:
                _UI_OPENED_POST_SLOTS.release()
                acquired = False
                return False
            instance_to_report = next(iter(_pending_ui_opened_instances))
            _pending_ui_opened_instances.pop(instance_to_report)
            _reported_ui_opened_instances[instance_to_report] = None
            if len(_reported_ui_opened_instances) > _MAXIMUM_TRACKED_UI_OPENED_INSTANCES:
                _reported_ui_opened_instances.pop(next(iter(_reported_ui_opened_instances)))
            marked = True

        threading.Thread(
            target=_post_ui_opened_event,
            args=prepared,
            name="chatgpt-meetings-ui-opened",
            daemon=True,
        ).start()
        return True
    except Exception:
        if marked and instance_to_report is not None:
            with _EVENT_LOCK:
                _reported_ui_opened_instances.pop(instance_to_report, None)
                _pending_ui_opened_instances[instance_to_report] = None
        if acquired:
            _UI_OPENED_POST_SLOTS.release()
        return False


def _report_mcp_ready() -> bool:
    """Schedule one correlated lifecycle event without consuming error budgets."""

    global _mcp_ready_reported
    marked = False
    try:
        prepared = build_mcp_ready_event()
        if prepared is None:
            return False
        with _EVENT_LOCK:
            if _mcp_ready_reported:
                return False
            _mcp_ready_reported = True
            marked = True
        threading.Thread(
            target=_post_mcp_sentry_event,
            args=(*prepared, False, False, False),
            name="chatgpt-meetings-lifecycle",
            daemon=True,
        ).start()
        return True
    except Exception:
        if marked:
            with _EVENT_LOCK:
                _mcp_ready_reported = False
        return False


def report_mcp_ready(*, auth_settled: bool = False) -> bool:
    """Emit after existing authentication settles without loading or refreshing it."""

    global _mcp_ready_armed
    if auth_settled:
        report_ui_opened(auth_settled=True)
    with _EVENT_LOCK:
        if _mcp_ready_reported or (auth_settled and not _mcp_ready_armed):
            return False
        _mcp_ready_armed = True
    if not auth_settled and _cached_sentry_user_id() is None:
        return False
    return _report_mcp_ready()


def reset_notes_backend_error_episode() -> None:
    """Rearm bounded Notes failure causes after account recovery or success."""
    with _EVENT_LOCK:
        _NOTES_FAILURE_SIGNATURES.clear()


def report_mcp_error(
    stage: str,
    kind: str,
    *,
    ui_version: str | None = None,
    mcp_build_timestamp: str | None = None,
    active_owner_version: str | None = None,
    target_owner_version: str | None = None,
    handoff_disposition: str | None = None,
    handoff_reason: str | None = None,
    recovery_kind: str | None = None,
    operation: str | None = None,
    error_source: str | None = None,
    presentation: str | None = None,
    notification: str | None = None,
    update_reason: str | None = None,
    failure_reason: str | None = None,
    auth_requested_store: str | None = None,
    verification_phase: str | None = None,
    failure_operation: str | None = None,
    resource_role: str | None = None,
    os_error_code: str | None = None,
    companion_diagnostics: dict[str, str] | None = None,
    device_settings_diagnostics: dict[str, str] | None = None,
    retryable: bool | None = None,
    http_status: int | None = None,
) -> bool:
    """Schedule one bounded, fail-open Sentry report and never block stdio.

    Args:
        stage: Candidate lifecycle stage.
        kind: Candidate error kind.
        ui_version: Candidate widget version.
        mcp_build_timestamp: Candidate MCP build timestamp.
        active_owner_version: Candidate authenticated active-owner version.
        target_owner_version: Candidate authenticated target-owner version.
        handoff_disposition: Candidate handoff outcome.
        handoff_reason: Candidate bounded native update handoff failure cause.
        recovery_kind: Candidate recovery classification.
        operation: Candidate bounded user operation.
        error_source: Candidate bounded error source.
        presentation: Candidate bounded visible notification surface.
        notification: Candidate bounded visible notification classification.
        update_reason: Candidate bounded user-confirmed native update failure.
        failure_reason: Candidate bounded auth, backend, or native failure classification.
        auth_requested_store: Auth child's requested store, not its managed effective store.
        verification_phase: Candidate bounded native materialization verification boundary.
        failure_operation: Candidate bounded bootstrap or Stop failure operation.
        resource_role: Candidate bounded failure resource role, never a path.
        os_error_code: Candidate bounded operating-system error code.
        companion_diagnostics: Last observed, finite companion context; not a fresh probe.
        device_settings_diagnostics: Finite observations from this device-settings request.
        retryable: Whether the classified Notes/settings backend failure may be retried.
        http_status: Candidate settings HTTP response status, never response contents.

    Returns:
        `True` when a background report was scheduled, otherwise `False`.
    """

    acquired = False
    user_interface_acquired = False
    presentation_acquired = False
    counted = False
    user_interface_counted = False
    presentation_counted = False
    notes_signature: tuple[str, str, str, str] | None = None
    auth_signature: tuple[str, str] | None = None
    try:
        diagnostic_scope = _cached_diagnostic_scope()
        diagnostics = McpSentryDiagnostics()
        if active_owner_version is not None:
            diagnostics["active_owner_version"] = active_owner_version
        if target_owner_version is not None:
            diagnostics["target_owner_version"] = target_owner_version
        if handoff_disposition is not None:
            diagnostics["handoff_disposition"] = handoff_disposition
        if handoff_reason is not None:
            diagnostics["handoff_reason"] = handoff_reason
        if recovery_kind is not None:
            diagnostics["recovery_kind"] = recovery_kind
        if operation is not None:
            diagnostics["operation"] = operation
        if error_source is not None:
            diagnostics["error_source"] = error_source
        if presentation is not None:
            diagnostics["presentation"] = presentation
        if notification is not None:
            diagnostics["notification"] = notification
        if update_reason is not None:
            diagnostics["update_reason"] = update_reason
        if failure_reason is not None:
            diagnostics["failure_reason"] = failure_reason
        if auth_requested_store is not None:
            diagnostics["auth_requested_store"] = auth_requested_store
        if verification_phase is not None:
            diagnostics["verification_phase"] = verification_phase
        if failure_operation is not None:
            diagnostics["failure_operation"] = failure_operation
        if resource_role is not None:
            diagnostics["resource_role"] = resource_role
        if os_error_code is not None:
            diagnostics["os_error_code"] = os_error_code
        if companion_diagnostics is not None:
            diagnostics["companion_diagnostics"] = companion_diagnostics
        if device_settings_diagnostics is not None:
            diagnostics["device_settings_diagnostics"] = device_settings_diagnostics
        if retryable is not None:
            diagnostics["retryable"] = retryable
        if http_status is not None:
            diagnostics["http_status"] = http_status
        prepared = build_mcp_sentry_event(
            stage,
            kind,
            ui_version=ui_version,
            mcp_build_timestamp=mcp_build_timestamp,
            **diagnostics,
        )
        if prepared is None:
            return False
        _record_diagnostic_event(prepared[2], diagnostic_scope)
        event_tags = prepared[2].get("tags", {})
        if (
            stage == "notes"
            and kind == "backend"
            and {"failure_reason", "retryable"} <= event_tags.keys()
        ):
            notes_signature = (stage, kind, event_tags["failure_reason"], event_tags["retryable"])
        if (stage, kind) == ("auth", "auth") and {
            "failure_reason",
            "auth_requested_store",
        } <= event_tags.keys():
            auth_signature = (event_tags["failure_reason"], event_tags["auth_requested_store"])
        is_user_interface_event = ui_version is not None
        if is_user_interface_event:
            if not _USER_INTERFACE_POST_SLOTS.acquire(blocking=False):
                return False
            user_interface_acquired = True
        is_presentation_event = (
            isinstance(presentation, str) and presentation in MCP_SENTRY_PRESENTATIONS
        )
        if is_presentation_event:
            if not _PRESENTATION_POST_SLOTS.acquire(blocking=False):
                if user_interface_acquired:
                    _USER_INTERFACE_POST_SLOTS.release()
                    user_interface_acquired = False
                return False
            presentation_acquired = True
        if not _POST_SLOTS.acquire(blocking=False):
            if presentation_acquired:
                _PRESENTATION_POST_SLOTS.release()
                presentation_acquired = False
            if user_interface_acquired:
                _USER_INTERFACE_POST_SLOTS.release()
                user_interface_acquired = False
            return False
        acquired = True
        global _events_started, _presentation_events_started, _user_interface_events_started
        with _EVENT_LOCK:
            if (
                _events_started >= _MAXIMUM_EVENTS_PER_PROCESS
                or is_user_interface_event
                and _user_interface_events_started >= _MAXIMUM_USER_INTERFACE_EVENTS_PER_PROCESS
                or notes_signature is not None
                and notes_signature in _NOTES_FAILURE_SIGNATURES
                or auth_signature is not None
                and auth_signature in _AUTH_FAILURE_SIGNATURES
            ):
                _POST_SLOTS.release()
                acquired = False
                if presentation_acquired:
                    _PRESENTATION_POST_SLOTS.release()
                    presentation_acquired = False
                if user_interface_acquired:
                    _USER_INTERFACE_POST_SLOTS.release()
                    user_interface_acquired = False
                return False
            if (
                is_presentation_event
                and _presentation_events_started >= _MAXIMUM_PRESENTATION_EVENTS_PER_PROCESS
            ):
                _POST_SLOTS.release()
                acquired = False
                if presentation_acquired:
                    _PRESENTATION_POST_SLOTS.release()
                    presentation_acquired = False
                if user_interface_acquired:
                    _USER_INTERFACE_POST_SLOTS.release()
                    user_interface_acquired = False
                return False
            _events_started += 1
            counted = True
            if notes_signature is not None:
                _NOTES_FAILURE_SIGNATURES.add(notes_signature)
            if auth_signature is not None:
                _AUTH_FAILURE_SIGNATURES.add(auth_signature)
            if is_user_interface_event:
                _user_interface_events_started += 1
                user_interface_counted = True
            if is_presentation_event:
                _presentation_events_started += 1
                presentation_counted = True
        threading.Thread(
            target=_post_mcp_sentry_event,
            args=(*prepared, presentation_acquired, user_interface_acquired),
            name="chatgpt-meetings-sentry",
            daemon=True,
        ).start()
        return True
    except Exception:
        if counted:
            with _EVENT_LOCK:
                _events_started -= 1
                if notes_signature is not None:
                    _NOTES_FAILURE_SIGNATURES.discard(notes_signature)
                if auth_signature is not None:
                    _AUTH_FAILURE_SIGNATURES.discard(auth_signature)
                if user_interface_counted:
                    _user_interface_events_started -= 1
                if presentation_counted:
                    _presentation_events_started -= 1
        if acquired:
            _POST_SLOTS.release()
        if presentation_acquired:
            _PRESENTATION_POST_SLOTS.release()
        if user_interface_acquired:
            _USER_INTERFACE_POST_SLOTS.release()
        return False
