"""Private ChatGPT Meetings settings and companion bootstrap helpers."""

from __future__ import annotations

import errno
import hmac
import json
import sys
from collections.abc import Mapping
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Literal

import bootstrap_recovery
import meetings_api_client_common as api_common
import meetings_mcp
import native_runtime
from bootstrap_recovery import (
    BootstrapFailure,
    BootstrapFailureDiagnostics,
    record_authenticated_companion_recovery,
)
from codex_auth_client import AuthMaterial
from companion_client import (
    CompanionClient,
    CompanionRecoveryOutcome,
    bootstrap_recovery_client,
    companion_client,
    has_pending_listener_recovery,
    pending_listener_recovery_client,
    recover_unresponsive_companion,
    require_verified_companion_replacement,
    wait_for_companion_recording_ready,
)
from companion_restart_budget import automatic_recovery_guard, claim_automatic_restart
from control_client import (
    HANDOFF_EXIT_TIMEOUT_SECONDS,
    HANDOFF_RESPONSE_TIMEOUT_SECONDS,
    ControlConnectionUnavailable,
    ControlRequestTimedOut,
    DescriptorChanged,
    HandoffExitTimedOut,
    HandoffOwnerUnsettled,
)
from control_transport.live_client import LiveTransportError, LiveTransportFailureKind
from meetings_sentry import MCP_SENTRY_DEVICE_SETTINGS_DIAGNOSTIC_VALUES
from meetings_settings import CompanionSettingsResponseWire, SettingsReadinessStatus
from native_runtime_manager import PreparedCompanionReplacement, _NativeRuntimeLaunchRejected


def _observe_device_settings(
    diagnostics: dict[str, str],
    outcome: str,
    cancellation_event: meetings_mcp.threading.Event | None,
) -> None:
    """Log only finite request observations; report failures through bounded Sentry."""
    diagnostics["device_settings_outcome"] = (
        "cancelled" if cancellation_event is not None and cancellation_event.is_set() else outcome
    )
    safe = {
        key: value
        for key, value in diagnostics.items()
        if key in MCP_SENTRY_DEVICE_SETTINGS_DIAGNOSTIC_VALUES
        and value in MCP_SENTRY_DEVICE_SETTINGS_DIAGNOSTIC_VALUES[key]
    }
    try:
        print(
            "ChatGPT Meetings device settings: " + json.dumps(safe, sort_keys=True),
            file=sys.stderr,
            flush=True,
        )
    except (OSError, ValueError):
        # Diagnostics must not change a settings response when the host closes stderr.
        pass
    if safe.get("device_settings_outcome") not in {
        "ready",
        "loading",
        "saving",
        "unsupported-host",
        "cancelled",
    }:
        meetings_mcp.report_mcp_error(
            "settings", "runtime", operation="settings", device_settings_diagnostics=safe
        )


def settings_tool_payload(
    *,
    action: Literal["getSettings", "updateSettings"],
    arguments: Mapping[str, bool] | None = None,
    expected_owner_scope: str | None = None,
    cancellation_event: meetings_mcp.threading.Event | None = None,
    wait_for_connection: bool = False,
) -> CompanionSettingsResponseWire:
    """Read or update only the authenticated account's v2 companion settings.

    Args:
        action: Local app request selecting a settings read or sparse update.
        arguments: Validated native preference changes for an update.
        expected_owner_scope: Optional authenticated owner required by the caller.
        cancellation_event: Optional caller cancellation signal.
        wait_for_connection: Connect to an existing owner before reading settings.

    Returns:
        Companion-owned setting values, availability, and update readiness.
    """

    if cancellation_event is None:
        cancellation_event = meetings_mcp._current_rpc_cancellation_event()
    diagnostics: dict[str, str] = {
        "device_settings_action": action,
        "device_settings_phase": "preflight",
    }
    if (
        action == "updateSettings"
        and arguments is not None
        and arguments.get("meetingDetectionEnabled") is True
        and meetings_mcp.plugin_availability_blocks_start(local_fallback=True)
    ):
        raise meetings_mcp.InvalidArguments("Meeting detection is unavailable on this client.")
    unavailable: CompanionSettingsResponseWire = {
        "ok": False,
        "settings": {
            "available": False,
            "calendarRemindersEnabled": None,
            "soundEffectsEnabled": None,
            "meetingDetectionEnabled": None,
            "remindersAvailable": False,
            "soundEffectsAvailable": False,
            "meetingDetectionAvailable": False,
        },
        "readiness": {
            "status": "companion-unavailable",
            "canUpdate": False,
            "message": "Open or install the local companion to edit settings.",
        },
    }
    loading: CompanionSettingsResponseWire = {
        **unavailable,
        "readiness": {
            "status": "checking",
            "canUpdate": False,
            "message": "Waiting for Meetings local capture.",
        },
        "bootstrap": {"status": "loading"},
    }
    if meetings_mcp._should_return_bootstrap_loading_status() or (
        action == "updateSettings" and meetings_mcp._bootstrap_owner_replacement_in_flight()
    ):
        _observe_device_settings(diagnostics, "loading", cancellation_event)
        return loading
    if meetings_mcp._native_runtime_host_is_unsupported():
        _observe_device_settings(diagnostics, "unsupported-host", cancellation_event)
        return unavailable

    try:
        diagnostics["device_settings_phase"] = "authentication"
        _, owner_scope = _account_owner(expected_owner_scope, cancellation_event)
        diagnostics["device_settings_phase"] = "connection"
        client = companion_client(
            connect=action == "updateSettings" or wait_for_connection,
            cancellation_event=cancellation_event,
        )
        diagnostics["device_settings_capability"] = (
            "true" if "settings.v2" in client.negotiated_capabilities else "false"
        )
        state = client.latest_state()
        if state is None and action == "getSettings":
            failure = client.connect_in_background()
            if failure is not None:
                raise failure
            _observe_device_settings(diagnostics, "loading", cancellation_event)
            return loading
        diagnostics["device_settings_phase"] = "cached-account"
        diagnostics["device_settings_cached_account"] = (
            "missing"
            if state is None or state["accountScopeFingerprint"] is None
            else "match"
            if hmac.compare_digest(state["accountScopeFingerprint"], owner_scope)
            else "mismatch"
        )
        if (
            state is None
            or state["accountScopeFingerprint"] is None
            or not hmac.compare_digest(state["accountScopeFingerprint"], owner_scope)
        ):
            raise meetings_mcp.ControlUnavailable("native settings account does not match")
        changes: dict[str, bool] | None = None
        if action == "updateSettings":
            if arguments is None:
                raise meetings_mcp.ControlUnavailable("native settings update is empty")
            changes = dict(arguments)
            if changes.get(
                "meetingDetectionEnabled"
            ) is True and meetings_mcp.plugin_availability_blocks_start(local_fallback=True):
                raise meetings_mcp.InvalidArguments(
                    "Meeting detection is unavailable on this client."
                )
        diagnostics["device_settings_phase"] = "native-request"
        result = client.settings(
            owner_scope,
            changes=changes,
            cancellation_event=cancellation_event,
        )
        diagnostics["device_settings_native_status"] = result["status"]
        diagnostics["device_settings_can_update"] = "true" if result["canUpdate"] else "false"
        diagnostics["device_settings_phase"] = "account-recheck"
        _account_owner(owner_scope, cancellation_event)
    except (meetings_mcp.ControlUnavailable, meetings_mcp.NativeRuntimeError) as error:
        if isinstance(error, meetings_mcp.NativeRuntimeError) and not (
            meetings_mcp._native_runtime_host_is_unsupported()
        ):
            _observe_device_settings(diagnostics, "runtime-error", cancellation_event)
            raise
        if meetings_mcp._bootstrap_owner_replacement_in_flight():
            _observe_device_settings(diagnostics, "loading", cancellation_event)
            return loading
        outcome = "control-unavailable"
        if diagnostics.get("device_settings_cached_account") in {"missing", "mismatch"}:
            outcome = "cached-account-" + diagnostics["device_settings_cached_account"]
        _observe_device_settings(diagnostics, outcome, cancellation_event)
        return unavailable

    readiness: SettingsReadinessStatus = (
        "ready"
        if result["status"] == "ready"
        else "settings-saving"
        if result["status"] == "saving"
        else "settings-unavailable"
    )
    values = result["values"]
    availability = result["availability"]
    diagnostics["device_settings_phase"] = "projection"
    _observe_device_settings(
        diagnostics,
        "saving"
        if result["status"] == "saving"
        else "native-unavailable"
        if result["status"] != "ready"
        else "not-editable"
        if not result["canUpdate"]
        else "ready"
        if any(
            availability.get(capability) is True and isinstance(values.get(name), bool)
            for capability, name in (
                ("reminders", "calendarRemindersEnabled"),
                ("soundEffects", "soundEffectsEnabled"),
                ("meetingDetection", "meetingDetectionEnabled"),
            )
        )
        else "no-supported-preferences",
        cancellation_event,
    )
    return {
        "ok": readiness == "ready",
        "settings": {
            "available": readiness == "ready",
            "calendarRemindersEnabled": values.get("calendarRemindersEnabled"),
            "soundEffectsEnabled": values.get("soundEffectsEnabled"),
            "meetingDetectionEnabled": values.get("meetingDetectionEnabled"),
            "remindersAvailable": availability.get("reminders") is True,
            "soundEffectsAvailable": availability.get("soundEffects") is True,
            "meetingDetectionAvailable": availability.get("meetingDetection") is True,
        },
        "readiness": {
            "status": readiness,
            "canUpdate": readiness == "ready" and result["canUpdate"],
            "message": (
                "Meetings settings are ready."
                if readiness == "ready"
                else "Meetings settings are being saved."
                if readiness == "settings-saving"
                else "Meetings settings are unavailable."
            ),
        },
    }


_LOCAL_STRUCTURED_SETTING_NAMES = {
    "recordingNotificationsEnabled": "calendarRemindersEnabled",
    "soundEffectsEnabled": "soundEffectsEnabled",
    "meetingDetectionEnabled": "meetingDetectionEnabled",
}


def _structured_local_values(payload: CompanionSettingsResponseWire) -> dict[str, bool]:
    if not payload["ok"] or not payload["readiness"]["canUpdate"]:
        return {}
    settings = payload["settings"]
    candidates = (
        (
            "recordingNotificationsEnabled",
            settings["calendarRemindersEnabled"],
            settings["remindersAvailable"],
        ),
        ("soundEffectsEnabled", settings["soundEffectsEnabled"], settings["soundEffectsAvailable"]),
        (
            "meetingDetectionEnabled",
            settings["meetingDetectionEnabled"],
            settings["meetingDetectionAvailable"],
        ),
    )
    return {
        name: value
        for name, value, available in candidates
        if available and isinstance(value, bool)
    }


def structured_settings_payload(
    *,
    changes: Mapping[str, object] | None = None,
    cancellation_event: meetings_mcp.threading.Event | None = None,
) -> meetings_mcp.JSONSchema:
    """Read desktop settings or persist a sparse patch in its owning store.

    Args:
        changes: Named booleans to update, or None for settings discovery.
        cancellation_event: Optional caller cancellation signal.

    Returns:
        Hosted preferences plus available, authenticated device preferences.

    Raises:
        InvalidArguments: If a patch is invalid, spans stores, or targets unavailable bot settings.
        ControlUnavailable: If the account changes or local persistence fails.
    """

    if cancellation_event is None:
        cancellation_event = meetings_mcp._current_rpc_cancellation_event()
    requested = (
        meetings_mcp.normalize_record_settings_update(
            changes, allowed_names=meetings_mcp._STRUCTURED_SETTINGS_FIELDS.keys()
        )
        if changes is not None
        else {}
    )

    def reject_unavailable_enable() -> None:
        if any(
            requested.get(name) is True for name in ("autoRecordEnabled", "meetingDetectionEnabled")
        ) and meetings_mcp.plugin_availability_blocks_start(local_fallback=True):
            raise meetings_mcp.InvalidArguments(
                "Automatic meeting notes are unavailable on this client."
            )

    reject_unavailable_enable()
    hosted_changes = {
        name: value for name, value in requested.items() if name in meetings_mcp.SETTING_NAMES
    }
    local_changes = {
        name: value for name, value in requested.items() if name in _LOCAL_STRUCTURED_SETTING_NAMES
    }
    # Independent stores cannot provide one atomic write. Desktop controls send
    # sparse changes; reject a cross-store batch before either store is touched.
    if hosted_changes and local_changes:
        raise meetings_mcp.InvalidArguments("Update account and device settings separately.")
    auth, owner_scope = _account_owner(cancellation_event=cancellation_event)
    expected_account = (auth.account_id, auth.subject)
    client = meetings_mcp.get_record_interactions_client()
    # Both reads are account-bound and independent. Join the worker before any
    # mutation so failures and cancellation cannot leave background work behind.
    with ThreadPoolExecutor(max_workers=1, thread_name_prefix="meetings-settings") as executor:
        local_read = executor.submit(
            meetings_mcp.settings_tool_payload,
            action="getSettings",
            expected_owner_scope=owner_scope,
            cancellation_event=cancellation_event,
            wait_for_connection=True,
        )
        hosted = client.get_settings(
            expected_account=expected_account, cancellation_event=cancellation_event
        )
        local = local_read.result()
    if hosted_changes and not hosted.bot_settings_available:
        raise meetings_mcp.InvalidArguments(
            "Meeting bot settings are unavailable for this account."
        )
    local_values = _structured_local_values(local)
    _account_owner(owner_scope, cancellation_event)
    reject_unavailable_enable()
    if local_changes:
        if not local_changes.keys() <= local_values.keys():
            raise meetings_mcp.ControlUnavailable(
                "Open Meetings and wait for local settings to become available, then try again."
            )
        local = meetings_mcp.settings_tool_payload(
            action="updateSettings",
            arguments={
                _LOCAL_STRUCTURED_SETTING_NAMES[name]: value
                for name, value in local_changes.items()
            },
            expected_owner_scope=owner_scope,
            cancellation_event=cancellation_event,
        )
        local_values = _structured_local_values(local)
        if any(local_values.get(name) is not value for name, value in local_changes.items()):
            raise meetings_mcp.ControlUnavailable(
                "Meetings did not apply the device setting. Reopen settings and try again."
            )
    elif hosted_changes:
        hosted = client.update_settings(
            settings=hosted_changes,
            expected_account=expected_account,
            cancellation_event=cancellation_event,
        )
    _account_owner(owner_scope, cancellation_event)
    values = {**hosted.structured_values(), **local_values}
    if meetings_mcp.plugin_availability_blocks_start(local_fallback=True):
        # Omit unavailable controls without changing either store's saved preferences.
        values.pop("autoRecordEnabled", None)
        values.pop("meetingDetectionEnabled", None)
    if changes is not None:
        return {"values": values}
    fields = {
        name: field
        for name, field in meetings_mcp._STRUCTURED_SETTINGS_FIELDS.items()
        if name in values
    }
    layout: list[meetings_mcp.JSONSchema] = []
    if hosted.bot_settings_available:
        layout.append(
            {
                "kind": "group",
                "title": "Meeting Bot",
                "items": [
                    {"kind": "property", "property": name}
                    for name in fields
                    if name in meetings_mcp.SETTING_NAMES
                ],
            }
        )
    if not any(name in _LOCAL_STRUCTURED_SETTING_NAMES for name in fields):
        meetings_mcp.log_native_runtime_event(
            "settings",
            "tool-fallback",
            reason=local["readiness"]["status"],
        )
    layout.append(
        {
            "kind": "group",
            "title": "On this device",
            "items": [
                {"kind": "property", "property": name}
                for name in fields
                if name in _LOCAL_STRUCTURED_SETTING_NAMES
            ]
            or [
                {
                    "kind": "tool",
                    "tool": "meetings.open",
                    "title": "Open Meetings",
                    "description": "Open Meetings to connect local settings, then reopen this panel.",
                }
            ],
        },
    )
    return {
        "schema": {
            "type": "object",
            "properties": fields,
            "required": list(fields),
            "additionalProperties": False,
        },
        "layout": layout,
        "values": values,
    }


def _account_owner(
    expected: str | None = None,
    cancellation_event: meetings_mcp.threading.Event | None = None,
) -> tuple[AuthMaterial, str]:
    """Revalidate the exact authenticated subject and account before every handoff."""

    manager = meetings_mcp.get_process_auth_manager()
    auth = manager.get_chatgpt_auth(cancellation_event=cancellation_event)
    owner = api_common.record_owner_scope_fingerprint(auth)
    if owner is None or expected is not None and not hmac.compare_digest(owner, expected):
        raise meetings_mcp.ControlUnavailable("authenticated account owner is unavailable")
    return auth, owner


def calendar_account_scope_generation(expected: str | None = None) -> str:
    """Return the authenticated hosted Calendar account generation.

    Args:
        expected: Optional owner fingerprint that the authenticated account must match.

    Returns:
        The hosted Calendar client's opaque, account-bound browser generation.
    """

    auth, owner = _account_owner(expected)
    return meetings_mcp.get_record_calendar_client().account_scope_generation(
        api_common.record_account_fingerprint(auth), owner_scope_fingerprint=owner
    )


def _control_descriptor_hint_exists() -> bool:
    """Return a conservative, non-authorizing descriptor-owner hint.

    A missing descriptor is the normal cold-launch case. Reading full native
    status there first traverses the signed bundle, then launch_current must
    traverse it again at the execution boundary. A private, well-shaped
    descriptor whose PID the OS proves dead is the same non-owning bootstrap
    case. Malformed, non-private, live, permission-denied, or replacement-race
    descriptors remain conservative and take the full signed-status path.

    This hint never treats a descriptor as connected and never authorizes
    launch. Only launch_current can open a plugin-bundled artifact after its
    mandatory fresh verification and authoritative owner-lease/handoff checks.
    """

    return meetings_mcp.control_descriptor_may_have_live_owner()


def _bootstrap_control_is_connected(
    *,
    runtime: Mapping[str, object] | None = None,
    raise_failures: bool = False,
) -> bool:
    """Return true only for an authenticated native connection.

    Descriptor nonownership is the ordinary cold path, so it remains a cheap
    private owner hint and never constructs a companion client or asks
    RuntimeManager for status before launch. Once launch_current has returned
    its freshly verified runtime proof, polling reuses that proof and therefore
    does not add another deep signature traversal while the app writes its
    descriptor.
    """

    if not meetings_mcp._control_descriptor_hint_exists():
        return False
    try:
        resolved_runtime = (
            runtime if runtime is not None else meetings_mcp.RuntimeManager().status()
        )
        if (
            not isinstance(resolved_runtime, dict)
            or resolved_runtime.get("source") != "plugin-bundled"
        ):
            # A valid old cache descriptor is still not the plugin-local app
            # that bootstrap is allowed to own. Do not mistake it for a
            # successful bootstrap and do not ask it for control state.
            return False
        if not meetings_mcp.control_descriptor_uses_runtime_image(runtime=resolved_runtime):
            return False
        # An open stream and cached state do not prove that its owner
        # is responding. Authenticate and read state within one deadline,
        # preserving typed failures before the UI status projection consumes them.
        companion_client(runtime=resolved_runtime, connect=False).get_state(
            timeout_seconds=5.0,
        )
        return True
    except Exception:
        if raise_failures:
            raise
        return False


def _bootstrap_launch_failure(error: Exception) -> BootstrapFailure:
    """Classify a bounded cause chain and positively identify transient failures."""

    failure = BootstrapFailure.UNEXPECTED
    control_connection_failure = False
    cause: BaseException | None = error
    observed: set[int] = set()
    for _ in range(4):
        if cause is None or id(cause) in observed:
            break
        observed.add(id(cause))
        if isinstance(cause, DescriptorChanged):
            return BootstrapFailure.RUNTIME_REJECTED
        if isinstance(cause, LiveTransportError):
            if cause.kind is LiveTransportFailureKind.UNAVAILABLE:
                return BootstrapFailure.CONNECTION_UNAVAILABLE
            if cause.kind is LiveTransportFailureKind.TIMED_OUT:
                return BootstrapFailure.TIMEOUT
            # Rejection and cancellation are authoritative even when an
            # implementation detail in their cause chain looks transient.
            return BootstrapFailure.RUNTIME_REJECTED
        if isinstance(cause, native_runtime.NativeRuntimeRegistrationUnavailable):
            return BootstrapFailure.REGISTRATION_UNAVAILABLE
        if isinstance(cause, native_runtime.NativeRuntimeArtifactMissing):
            return BootstrapFailure.ARTIFACT_MISSING
        if isinstance(cause, FileNotFoundError):
            return (
                BootstrapFailure.CONNECTION_UNAVAILABLE
                if control_connection_failure
                else BootstrapFailure.MISSING_RESOURCE
            )
        if isinstance(cause, PermissionError):
            return BootstrapFailure.PERMISSION_DENIED
        if isinstance(cause, native_runtime.NativeRuntimeLockBusy):
            return BootstrapFailure.STABLE_LOCK_BUSY
        if isinstance(cause, BlockingIOError):
            return BootstrapFailure.LOCK_CONTENTION
        if isinstance(cause, _NativeRuntimeLaunchRejected):
            failure = BootstrapFailure.LAUNCHER_REJECTED
        elif isinstance(
            cause,
            (TimeoutError, ControlRequestTimedOut, HandoffExitTimedOut, HandoffOwnerUnsettled),
        ):
            failure = BootstrapFailure.TIMEOUT
        elif isinstance(cause, ControlConnectionUnavailable):
            control_connection_failure = True
            failure = BootstrapFailure.CONNECTION_UNAVAILABLE
        elif isinstance(cause, (ConnectionError, InterruptedError)):
            failure = BootstrapFailure.CONNECTION_UNAVAILABLE
        elif isinstance(cause, OSError) and not failure.retryable:
            failure = BootstrapFailure.IO_ERROR
        elif (
            isinstance(cause, meetings_mcp.NativeRuntimeError)
            and failure is BootstrapFailure.UNEXPECTED
        ):
            failure = BootstrapFailure.RUNTIME_REJECTED
        cause = cause.__cause__
    return failure


def _defer_active_bootstrap_retry() -> bool:
    """Back off the active bootstrap's single cooldown and require a responding owner."""

    with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
        if not meetings_mcp._INITIALIZE_BOOTSTRAP_ATTEMPTED:
            return False
        recovery = bootstrap_recovery.state
        recovery.retry_delay_seconds = min(
            meetings_mcp._INITIALIZE_BOOTSTRAP_MAX_RETRY_COOLDOWN_SECONDS,
            max(
                meetings_mcp._INITIALIZE_BOOTSTRAP_ACCEPTED_LAUNCH_COOLDOWN_SECONDS,
                recovery.retry_delay_seconds * 2,
            ),
        )
        meetings_mcp._INITIALIZE_BOOTSTRAP_IN_FLIGHT_UNTIL_MONOTONIC = max(
            meetings_mcp._INITIALIZE_BOOTSTRAP_IN_FLIGHT_UNTIL_MONOTONIC,
            meetings_mcp.time.monotonic() + recovery.retry_delay_seconds,
        )
        meetings_mcp._INITIALIZE_BOOTSTRAP_PENDING_REARM = True
        meetings_mcp._INITIALIZE_BOOTSTRAP_EXPLICIT_RECOVERY_REQUESTED = True
        return True


def _bootstrap_failure_diagnostics(
    error: Exception, *, require_control_io: bool = False
) -> BootstrapFailureDiagnostics:
    """Describe observed operations, never infer missing paths from exception text."""

    operation, role, code = "unknown", "unknown", "unknown"
    control_io_observed = False
    cause: BaseException | None = error
    observed: set[int] = set()
    for _ in range(4):
        if cause is None or id(cause) in observed:
            break
        observed.add(id(cause))
        if isinstance(cause, native_runtime.NativeRuntimeResourceError):
            operation, role = cause.operation.operation, cause.operation.role
        elif isinstance(cause, native_runtime.NativeRuntimeRegistrationUnavailable):
            operation, role = "verify_registration", cause.role
        elif isinstance(cause, native_runtime.NativeRuntimeArtifactMissing):
            operation, role = "resolve_native_artifact", "native_artifact"
        elif isinstance(cause, LiveTransportError):
            # A callback, identity check or local queue wait is not failed
            # endpoint I/O, even when its nested exception carries an errno.
            control_io_observed = cause.io_attempted is True and cause.kind in {
                LiveTransportFailureKind.UNAVAILABLE,
                LiveTransportFailureKind.TIMED_OUT,
            }
            if require_control_io and not control_io_observed:
                break
            operation, role = "control_transport", "control_endpoint"
        elif isinstance(cause, ControlConnectionUnavailable):
            operation, role = "control_transport", "control_endpoint"
        if isinstance(cause, OSError) and cause.errno is not None:
            code = {
                errno.ENOENT: "ENOENT",
                errno.EACCES: "EACCES",
                errno.EPERM: "EPERM",
                errno.ETIMEDOUT: "ETIMEDOUT",
                errno.ECONNREFUSED: "ECONNREFUSED",
                errno.ECONNRESET: "ECONNRESET",
                errno.EPIPE: "EPIPE",
            }.get(cause.errno, "unknown")
        cause = cause.__cause__
    if require_control_io and not control_io_observed:
        operation, role, code = "unknown", "unknown", "unknown"
    return {"failure_operation": operation, "resource_role": role, "os_error_code": code}


def _report_bootstrap_launch_failure(failure: BootstrapFailure, error: Exception) -> None:
    """Attempt each typed failure report once until verified owner recovery."""

    diagnostics = _bootstrap_failure_diagnostics(error)
    with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
        # Retain the latest boundary even when this failure class was already sent.
        bootstrap_recovery.state.last_failure = failure
        bootstrap_recovery.state.last_failure_diagnostics = diagnostics
        reported = bootstrap_recovery.state.reported_failures
        if failure in reported:
            return
        reported.add(failure)
    meetings_mcp.report_mcp_error(
        "bootstrap",
        "launch",
        mcp_build_timestamp=meetings_mcp.server_build_timestamp_utc(),
        failure_reason=failure.sentry_reason,
        **diagnostics,
    )


def _schedule_bootstrap_retry(*, require_existing_owner: bool) -> bool:
    """Queue recovery on the existing owner-update or normal bootstrap clock."""

    if require_existing_owner:
        return meetings_mcp._schedule_initialize_companion_deferred_update()
    return _defer_active_bootstrap_retry()


def _recover_bootstrap_owner(
    manager: meetings_mcp.RuntimeManager | None,
    client: CompanionClient,
    *,
    terminal_bootstrap_only: bool = True,
) -> bool | None:
    """Recover one exact owner without permissions or recording replay."""

    started = False
    recovered = False
    restart_claimed = False
    failure_reason = "unresponsive-owner-check-failed"
    active_version = client.owner.descriptor["companionVersion"]

    def report(
        outcome: Literal["started", "recovered", "failed", "blocked"],
        reason: str | None = None,
        target: str | None = None,
    ) -> None:
        meetings_mcp.report_explicit_recovery(
            outcome=outcome,
            operation="bootstrap",
            active_owner_version=active_version,
            target_owner_version=target,
            recovery_reason="terminal_bootstrap"
            if terminal_bootstrap_only
            else "owner_unresponsive",
            blocked_reason=reason,
        )

    if not meetings_mcp._FORCE_UPGRADE_LOCK.acquire(blocking=False):
        if not terminal_bootstrap_only:
            client.finish_listener_recovery()
        report("blocked", "recovery-in-progress")
        return False
    try:
        with automatic_recovery_guard(client.owner.root) as revalidate_transaction:
            with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
                meetings_mcp._INITIALIZE_BOOTSTRAP_REPLACING_OWNER = True
            prepared: PreparedCompanionReplacement | None = None

            def prepare() -> None:
                nonlocal prepared, failure_reason, restart_claimed
                failure_reason = "replacement-verification-failed"
                if prepared is None:
                    prepared = PreparedCompanionReplacement.prepare(
                        manager if manager is not None else meetings_mcp.RuntimeManager()
                    )
                prepared.revalidate()
                require_verified_companion_replacement(
                    client, prepared.identity, require_newer=terminal_bootstrap_only
                )
                if not terminal_bootstrap_only and not restart_claimed:
                    failure_reason = "restart-budget-exhausted"
                    if not claim_automatic_restart(client.owner.root):
                        raise meetings_mcp.ControlUnavailable(
                            "automatic restart budget unavailable"
                        )
                    restart_claimed = True
                failure_reason = "owner-verification-failed"

            def terminating() -> None:
                nonlocal started
                started = True
                report("started")

            outcome = recover_unresponsive_companion(
                client,
                terminal_bootstrap_only=terminal_bootstrap_only,
                for_automatic_recovery=not terminal_bootstrap_only,
                before_replacement=prepare,
                on_termination=terminating,
                revalidate_transaction=revalidate_transaction,
            )
            if outcome is CompanionRecoveryOutcome.RESPONDING:
                failure_reason = "owner-not-ready"
                state = wait_for_companion_recording_ready(
                    client,
                    client.get_state(),
                    timeout_seconds=meetings_mcp._EXPLICIT_ACTION_READY_WAIT_SECONDS,
                )
                if state is None:
                    report("failed", failure_reason)
                    return None
                revalidate_transaction()
                record_authenticated_companion_recovery()
                report("recovered", target=client.owner.descriptor["companionVersion"])
                recovered = True
                return True
            assert prepared is not None
            failure_reason = "companion-launch-failed"
            revalidate_transaction()
            prepared.launch()
            runtime = prepared.identity
            failure_reason = "owner-not-published"
            for poll in range(meetings_mcp._INITIALIZE_BOOTSTRAP_CONNECT_POLLS):
                revalidate_transaction()
                try:
                    published = meetings_mcp.control_descriptor_uses_runtime_image(runtime=runtime)
                except meetings_mcp.ControlUnavailable:
                    published = False
                if published:
                    replacement = companion_client(runtime=runtime, connect=False)
                    failure_reason = "owner-not-ready"
                    state = wait_for_companion_recording_ready(
                        replacement,
                        replacement.get_state(),
                        timeout_seconds=meetings_mcp._EXPLICIT_ACTION_READY_WAIT_SECONDS,
                    )
                    if state is None:
                        report("failed", failure_reason)
                        return None
                    revalidate_transaction()
                    record_authenticated_companion_recovery()
                    report("recovered", target=replacement.owner.descriptor["companionVersion"])
                    recovered = True
                    return True
                if poll + 1 < meetings_mcp._INITIALIZE_BOOTSTRAP_CONNECT_POLLS:
                    meetings_mcp.time.sleep(meetings_mcp._INITIALIZE_BOOTSTRAP_CONNECT_POLL_SECONDS)
            report("failed", failure_reason)
            return None
    except Exception as error:
        reason = (
            error.recovery_blocker
            if isinstance(error, meetings_mcp.CooperativeHandoffDeclined)
            else failure_reason
        )
        report("failed" if started else "blocked", reason)
        return None if isinstance(error, meetings_mcp.NativeRuntimeLaunchPending) else False
    finally:
        if started and not recovered:
            # Coalesced notifications cannot turn a failed or pending pinned
            # replacement into a second generic launch of a different image.
            with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
                if meetings_mcp._INITIALIZE_BOOTSTRAP_ATTEMPTED:
                    meetings_mcp._INITIALIZE_BOOTSTRAP_SUPPRESS_REARM = True
                meetings_mcp._INITIALIZE_BOOTSTRAP_PENDING_REARM = False
                meetings_mcp._INITIALIZE_BOOTSTRAP_EXPLICIT_RECOVERY_REQUESTED = False
        try:
            if not terminal_bootstrap_only:
                client.finish_listener_recovery()
        finally:
            meetings_mcp._FORCE_UPGRADE_LOCK.release()


def _recover_terminal_bootstrap(
    manager: meetings_mcp.RuntimeManager,
    client: CompanionClient,
) -> bool | None:
    """Use one negotiated cooperative recovery without replaying user actions."""

    if client.bootstrap_recovery_status() != "restartable":
        return client.bootstrap_recovery_status() == "restarting"
    launch_context: tuple[str, str] | None = None
    context_validation_failed = False

    def validate_launch_context() -> None:
        nonlocal launch_context, context_validation_failed
        try:
            current = manager.require_codex_launch_context()
        except meetings_mcp.NativeRuntimeError:
            context_validation_failed = True
            raise
        if launch_context is not None and current != launch_context:
            raise meetings_mcp.NativeRuntimeError("native companion launch context changed")
        launch_context = current

    with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
        meetings_mcp._INITIALIZE_BOOTSTRAP_REPLACING_OWNER = True
        # The ordinary five-second cold-launch window is shorter than this
        # bounded fresh-state + cooperative ACK/exit sequence.
        meetings_mcp._INITIALIZE_BOOTSTRAP_IN_FLIGHT_UNTIL_MONOTONIC = max(
            meetings_mcp._INITIALIZE_BOOTSTRAP_IN_FLIGHT_UNTIL_MONOTONIC,
            meetings_mcp.time.monotonic()
            + 5.0
            + HANDOFF_RESPONSE_TIMEOUT_SECONDS
            + HANDOFF_EXIT_TIMEOUT_SECONDS
            + meetings_mcp._INITIALIZE_BOOTSTRAP_ACCEPTED_LAUNCH_COOLDOWN_SECONDS,
        )
    try:
        runtime_identity = dict(client.owner.runtime)
        client.recover_failed_bootstrap(revalidate_request=validate_launch_context)
        assert launch_context is not None
        runtime = manager.launch_current(
            require_plugin_bundled=True,
            required_codex_launch_context=launch_context,
            required_runtime_identity=runtime_identity,
        )
        for poll in range(meetings_mcp._INITIALIZE_BOOTSTRAP_CONNECT_POLLS):
            if meetings_mcp._bootstrap_control_is_connected(runtime=runtime, raise_failures=True):
                return True
            if poll + 1 < meetings_mcp._INITIALIZE_BOOTSTRAP_CONNECT_POLLS:
                meetings_mcp.time.sleep(meetings_mcp._INITIALIZE_BOOTSTRAP_CONNECT_POLL_SECONDS)
        return None
    except meetings_mcp.NativeRuntimeLaunchPending:
        return None
    except Exception as error:
        # An ambiguous quit or failed exit is terminal for this local attempt.
        # The durable native budget survives any reconnect or replacement.
        failure = _bootstrap_launch_failure(error)
        if (
            client.bootstrap_recovery_requested is False
            and (context_validation_failed or failure.retryable)
            and _defer_active_bootstrap_retry()
        ):
            return None
        meetings_mcp.log_native_runtime_event(
            "bootstrap",
            "failed",
            error_kind="bootstrap-recovery",
            reason=failure.sentry_reason,
        )
        return False
    finally:
        # A notification/page-open may have coalesced a normal bootstrap while
        # this owner was being checked. Never turn an uncertain quit into a
        # second generic launch, which would lose the required host context.
        with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
            if client.bootstrap_recovery_requested is True:
                if meetings_mcp._INITIALIZE_BOOTSTRAP_ATTEMPTED:
                    # Consume the fence atomically in the outer worker, even
                    # if another notification arrives after this helper.
                    meetings_mcp._INITIALIZE_BOOTSTRAP_SUPPRESS_REARM = True
                meetings_mcp._INITIALIZE_BOOTSTRAP_PENDING_REARM = False
                meetings_mcp._INITIALIZE_BOOTSTRAP_EXPLICIT_RECOVERY_REQUESTED = False


def _best_effort_launch_bundled_companion_implementation(
    *,
    require_existing_owner: bool = False,
    handoff_reporting: native_runtime.BootstrapHandoffReporting,
) -> bool | None:
    """Reconnect or launch the verified plugin-local app after bootstrap.

    Bootstrap is not an install gesture: it must never fetch a feed, unpack
    an archive, or ask for recording permissions.  A healthy descriptor needs
    no work; an offline MCP may only open the exact app bundle that
    RuntimeManager freshly proves lives in this plugin.  The daemon retries
    an explicit launch failure once per batch; transient failed batches reuse
    its cooldown. After an accepted launch it waits for the authenticated
    descriptor instead of spawning duplicates. A busy
    authenticated handoff schedules one quiet deferred retry instead of
    immediately asking the recorder twice. Every failure is swallowed because
    the MCP handshake must remain usable for recovery UI.

    The return value is process-local scheduler state, never a public payload:
    true means a valid authenticated connection was observed; None means an
    exact verified child or retryable bootstrap remains pending; false means
    no launch was accepted and a later bootstrap signal may safely re-arm
    another bounded background attempt.
    """

    for attempt in range(meetings_mcp._INITIALIZE_BOOTSTRAP_MAX_LAUNCH_ATTEMPTS):
        try:
            manager = meetings_mcp.RuntimeManager()
        except meetings_mcp.NativeRuntimeError:
            if not meetings_mcp._native_runtime_host_is_unsupported():
                raise
            meetings_mcp.log_native_runtime_event(
                "bootstrap",
                "unavailable",
                attempt=attempt + 1,
                error_kind="platform-unsupported",
            )
            return False
        if meetings_mcp._control_descriptor_hint_exists():
            selected_runtime = manager.status()
            _, retained_runtime = meetings_mcp._select_windows_legacy_control_runtime(
                manager, selected_runtime
            )
            if retained_runtime is not None:
                # A fully verified, responsive legacy owner can keep recording
                # while private code waits for its natural exit. Do not enter
                # replacement or a repeated busy-to-idle migration loop.
                handoff_reporting.recovered = True
                return True
        connected = meetings_mcp._bootstrap_control_is_connected()
        if require_existing_owner and not connected:
            if not meetings_mcp._control_descriptor_hint_exists():
                meetings_mcp.log_native_runtime_event(
                    "update-check",
                    "unavailable",
                    attempt=attempt + 1,
                    error_kind="owner-unavailable",
                )
                return False
            # An offline descriptor still belongs in the authenticated recovery
            # lane; only exact owner identity can authorize terminating it.
        if connected:
            update_available = manager.has_plugin_bundled_update_hint() is True
            owner_runtime: Mapping[str, object] | None = None
            current_owner_image = False
            if meetings_mcp._control_descriptor_hint_exists():
                candidate_runtime = manager.status()
                if not isinstance(candidate_runtime, dict):
                    return False
                owner_runtime = candidate_runtime
                try:
                    current_owner_image = meetings_mcp.control_descriptor_uses_runtime_image(
                        runtime=owner_runtime
                    )
                except meetings_mcp.ControlUnavailable:
                    current_owner_image = False
                if not current_owner_image:
                    # The selected image may already equal the plugin source
                    # even though an older signed owner is still running.
                    # Source equality cannot hide that pending image upgrade.
                    update_available = True
            meetings_mcp.log_native_runtime_event(
                "update-check",
                "available" if update_available else "current",
                attempt=attempt + 1,
            )
            failed_bootstrap = bootstrap_recovery_client()
            if failed_bootstrap is not None:
                if update_available and failed_bootstrap.bootstrap_recovery_status() == "exhausted":
                    return _recover_bootstrap_owner(manager, failed_bootstrap)
                # The cached native proof cannot authorize a different image or
                # owner; fresh getState and the owner lease are checked at quit.
                if owner_runtime is None or not failed_bootstrap.owner.uses_runtime_image(
                    owner_runtime
                ):
                    return False
                return _recover_terminal_bootstrap(manager, failed_bootstrap)
            if not update_available:
                handoff_reporting.recovered = True
                return True
            if owner_runtime is not None and current_owner_image:
                status = meetings_mcp.ControlClient().status(
                    runtime=owner_runtime,
                    wait_for_connection=True,
                )
                state = status.get("state") if isinstance(status, dict) else None
                if (
                    not isinstance(status, dict)
                    or status.get("ok") is not True
                    or not isinstance(state, dict)
                    or not _companion_owner_allows_replacement(status)
                ):
                    if not isinstance(status, dict):
                        reason = "status-invalid"
                    elif status.get("ok") is not True:
                        reason = "status-rejected"
                    elif not isinstance(state, dict):
                        reason = "state-invalid"
                    else:
                        reason = "replacement-blocked"
                    meetings_mcp.log_native_runtime_event(
                        "bootstrap",
                        "deferred",
                        attempt=attempt + 1,
                        error_kind="protected-owner",
                        reason=reason,
                    )
                    meetings_mcp._schedule_initialize_companion_deferred_update()
                    handoff_reporting.recovered = (
                        isinstance(status, dict)
                        and status.get("ok") is True
                        and isinstance(state, dict)
                    )
                    return True
        meetings_mcp.log_native_runtime_event("bootstrap", "started", attempt=attempt + 1)
        try:
            if not manager.has_plugin_bundled_artifact_hint():
                meetings_mcp.log_native_runtime_event(
                    "bootstrap",
                    "unavailable",
                    attempt=attempt + 1,
                    error_kind="artifact-missing",
                )
                return False
            if meetings_mcp._control_descriptor_hint_exists():
                with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
                    meetings_mcp._INITIALIZE_BOOTSTRAP_REPLACING_OWNER = True
            with native_runtime.capture_bootstrap_handoff_failure(handoff_reporting):
                if require_existing_owner:
                    runtime = manager.launch_current(
                        require_plugin_bundled=True,
                        recover_unhealthy_current=True,
                        require_existing_owner=True,
                    )
                else:
                    runtime = manager.launch_current(
                        require_plugin_bundled=True,
                        recover_unhealthy_current=True,
                    )
        except meetings_mcp.NativeRuntimeUpdateDeferred:
            # Handle the typed busy case before its LaunchPending subclass.
            meetings_mcp._schedule_initialize_companion_deferred_update()
            meetings_mcp.log_native_runtime_event(
                "bootstrap",
                "deferred",
                attempt=attempt + 1,
                error_kind="update-deferred",
            )
            return False
        except meetings_mcp.NativeRuntimeLaunchPending:
            meetings_mcp.log_native_runtime_event("bootstrap", "pending", attempt=attempt + 1)
            return None
        except meetings_mcp.NativeRuntimeQuitRequired:
            if require_existing_owner:
                # A protected older owner may become safely quiescent after
                # this attempt. Re-arm the same coalesced, backed-off worker;
                # never replace the owner or replay a recording request.
                meetings_mcp._schedule_initialize_companion_deferred_update()
            meetings_mcp.log_native_runtime_event(
                "bootstrap",
                "deferred",
                attempt=attempt + 1,
                error_kind="quit-required",
            )
            return False
        except Exception as error:
            failure = _bootstrap_launch_failure(error)
            if failure is BootstrapFailure.STABLE_LOCK_BUSY:
                # Another same-installation runtime operation still owns the
                # private family lock. Preserve its recording authority and let the
                # existing coalesced cooldown observe the eventual owner rather
                # than waiting through a second lock timeout or reporting a
                # concurrent bootstrap as a terminal failure.
                meetings_mcp.log_native_runtime_event(
                    "bootstrap",
                    "pending",
                    attempt=attempt + 1,
                    error_kind="lock-contention",
                )
                _schedule_bootstrap_retry(require_existing_owner=require_existing_owner)
                return None
            meetings_mcp.log_native_runtime_event(
                "bootstrap",
                "failed",
                attempt=attempt + 1,
                error_kind="launch",
                reason=failure.sentry_reason,
            )
            # Preserve this observed failure before a new presence hint can
            # turn a disappearing registration into a quiet absent-install exit.
            # A delayed recheck still needs the current registration and owner.
            if (
                failure is not BootstrapFailure.REGISTRATION_UNAVAILABLE
                and attempt + 1 < meetings_mcp._INITIALIZE_BOOTSTRAP_MAX_LAUNCH_ATTEMPTS
            ):
                meetings_mcp.time.sleep(meetings_mcp._INITIALIZE_BOOTSTRAP_RETRY_DELAY_SECONDS)
                continue
            _report_bootstrap_launch_failure(failure, error)
            if failure.retryable and _schedule_bootstrap_retry(
                require_existing_owner=require_existing_owner
            ):
                # Every retry crosses the launch manager's fresh owner and
                # artifact verification; recording actions are never replayed.
                return None
            return False

        for poll in range(meetings_mcp._INITIALIZE_BOOTSTRAP_CONNECT_POLLS):
            try:
                connected = meetings_mcp._bootstrap_control_is_connected(
                    runtime=runtime, raise_failures=True
                )
            except Exception as error:
                failure = _bootstrap_launch_failure(error)
                _report_bootstrap_launch_failure(failure, error)
                if not failure.retryable:
                    return False
                _schedule_bootstrap_retry(require_existing_owner=require_existing_owner)
                return None
            if connected:
                failed_bootstrap = bootstrap_recovery_client()
                if failed_bootstrap is not None:
                    if not failed_bootstrap.owner.uses_runtime_image(runtime):
                        return False
                    return _recover_terminal_bootstrap(manager, failed_bootstrap)
                handoff_reporting.recovered = True
                meetings_mcp.log_native_runtime_event(
                    "bootstrap",
                    "connected",
                    platform=runtime.get("platform"),
                    version=runtime.get("version"),
                    build_timestamp=runtime.get("buildTimestamp"),
                    attempt=attempt + 1,
                )
                return True
            if poll + 1 < meetings_mcp._INITIALIZE_BOOTSTRAP_CONNECT_POLLS:
                meetings_mcp.time.sleep(meetings_mcp._INITIALIZE_BOOTSTRAP_CONNECT_POLL_SECONDS)
        meetings_mcp.log_native_runtime_event(
            "bootstrap",
            "pending",
            platform=runtime.get("platform"),
            version=runtime.get("version"),
            attempt=attempt + 1,
            error_kind="owner-not-published",
        )
        return None
    return False


def _best_effort_launch_bundled_companion(
    *,
    require_existing_owner: bool = False,
) -> bool | None:
    """Classify one bootstrap handoff after its authenticated final outcome."""

    handoff_reporting = native_runtime.BootstrapHandoffReporting()
    try:
        return _best_effort_launch_bundled_companion_implementation(
            require_existing_owner=require_existing_owner,
            handoff_reporting=handoff_reporting,
        )
    finally:
        if handoff_reporting.recovered:
            record_authenticated_companion_recovery()
        report_handoff = False
        with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
            meetings_mcp._INITIALIZE_BOOTSTRAP_REPLACING_OWNER = False
            if handoff_reporting.recovered:
                report_handoff = True
            elif handoff_reporting.diagnostics is not None:
                recovery = bootstrap_recovery.state
                report_handoff = not recovery.handoff_reported
                recovery.handoff_reported = True
        if report_handoff:
            native_runtime.report_bootstrap_handoff_outcome(handoff_reporting)


def _schedule_initialize_companion_deferred_update() -> bool:
    """Keep at most one local busy-to-idle companion-update worker alive."""

    with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
        meetings_mcp._INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_REQUESTED = True
        if meetings_mcp._INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_WORKER_SCHEDULED:
            return True
        meetings_mcp._INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_WORKER_SCHEDULED = True
        meetings_mcp._INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_WAKE.clear()
    try:
        meetings_mcp._start_initialize_bootstrap_daemon(
            meetings_mcp._run_initialize_companion_deferred_update,
            "chatgpt-meetings-deferred-update",
        )
    except Exception:
        # Bootstrap is best effort. A local thread-start failure must neither
        # break its caller nor permanently suppress a later update attempt.
        with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
            meetings_mcp._INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_WORKER_SCHEDULED = False
            meetings_mcp._INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_REQUESTED = False
        meetings_mcp.report_mcp_error(
            "bootstrap",
            "exception",
            mcp_build_timestamp=meetings_mcp.server_build_timestamp_utc(),
        )
        return False
    return True


def wake_initialize_companion_deferred_update(
    status: object,
    *,
    runtime: Mapping[str, object],
) -> None:
    """Wake a pending native update after independently verified idle capture.

    Args:
        status: Fresh authenticated companion recording and replacement state.
        runtime: Reviewed native runtime identity for the same owner.

    Returns:
        ``None`` after waking an eligible update or rejecting unsafe ownership.
    """

    if (
        runtime.get("installed") is not True
        or runtime.get("source") != "plugin-bundled"
        or not isinstance(status, dict)
        or status.get("ok") is not True
    ):
        return
    if not _companion_owner_allows_replacement(status):
        return
    with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
        if meetings_mcp._INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_WORKER_SCHEDULED:
            meetings_mcp._INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_WAKE.set()


def _companion_owner_allows_replacement(status: Mapping[str, object]) -> bool:
    state = status.get("state")
    if not isinstance(state, dict):
        return False
    recording = state.get("recording")
    lifecycle = state.get("lifecycle")
    replacement = lifecycle.get("replacement") if isinstance(lifecycle, dict) else None
    return (
        status.get("protocolVersion") == 2
        and isinstance(recording, dict)
        and recording.get("phase") == "idle"
        and isinstance(replacement, dict)
        and replacement.get("allowed") is True
        and replacement.get("blockedReason") is None
    )


def _run_initialize_companion_deferred_update() -> None:
    """Retry a declined authenticated handoff until the old owner is idle."""

    accepted_launch_rechecked = False
    retry_seconds = meetings_mcp._INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_RETRY_SECONDS
    try:
        while True:
            meetings_mcp._INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_WAKE.wait(timeout=retry_seconds)
            meetings_mcp._INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_WAKE.clear()
            with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
                meetings_mcp._INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_REQUESTED = False
            outcome = meetings_mcp._best_effort_launch_bundled_companion(
                require_existing_owner=True,
            )
            with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
                if meetings_mcp._INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_REQUESTED:
                    # launch_current observed another authenticated busy
                    # refusal; this worker owns the next quiet retry window.
                    retry_seconds = min(
                        retry_seconds * 2,
                        meetings_mcp._INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_MAX_RETRY_SECONDS,
                    )
                    continue
                if outcome is None and not accepted_launch_rechecked:
                    # An accepted launch can publish after the short status
                    # poll. Recheck it once in the next quiet window so a
                    # slow descriptor cannot strand the deferred update.
                    accepted_launch_rechecked = True
                    continue
                meetings_mcp._INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_WORKER_SCHEDULED = False
                return
    except Exception:
        # An unforeseen worker failure cannot permanently suppress a later
        # bootstrap or explicit Restart from re-arming safe recovery.
        with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
            meetings_mcp._INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_WORKER_SCHEDULED = False
            meetings_mcp._INITIALIZE_BOOTSTRAP_DEFERRED_UPDATE_REQUESTED = False
        meetings_mcp.report_mcp_error(
            "bootstrap",
            "exception",
            mcp_build_timestamp=meetings_mcp.server_build_timestamp_utc(),
        )


def _bootstrap_current_stream_owner_without_connection() -> bool:
    """Keep discovery-only MCP sessions off an already-current native stream."""

    if not meetings_mcp._control_descriptor_hint_exists():
        return False
    try:
        manager = meetings_mcp.RuntimeManager()
        if manager.has_plugin_bundled_update_hint() is not False:
            return False
        runtime = manager.status()
        if not isinstance(runtime, dict):
            return False
        verified_owner = meetings_mcp.verified_current_stream_owner_without_connection(
            runtime=runtime
        )
        if not verified_owner:
            return False
        # Source publication can race the owner proof. A newly staged update
        # must still enter the ordinary authenticated handoff/bootstrap lane.
        return manager.has_plugin_bundled_update_hint() is False
    except (
        meetings_mcp.ControlUnavailable,
        meetings_mcp.NativeRuntimeError,
        OSError,
        RuntimeError,
        TypeError,
        ValueError,
    ):
        return False


def _run_initialize_companion_bootstrap() -> None:
    """Run one bounded daemon attempt and re-arm only while still offline."""

    start_cooldown_wake = False
    start_pending_retry = False
    shortcut_without_owner_response = False
    outcome: bool | None = False
    try:
        with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
            require_owner_response = meetings_mcp._INITIALIZE_BOOTSTRAP_EXPLICIT_RECOVERY_REQUESTED
            meetings_mcp._INITIALIZE_BOOTSTRAP_EXPLICIT_RECOVERY_REQUESTED = False
        if (
            not require_owner_response
            and meetings_mcp._bootstrap_current_stream_owner_without_connection()
        ):
            shortcut_without_owner_response = True
            outcome = True
        else:
            listener_client = pending_listener_recovery_client()
            if listener_client is not None:
                outcome = _recover_bootstrap_owner(
                    None, listener_client, terminal_bootstrap_only=False
                )
                if outcome is not True:
                    # An unresolved pinned recovery cannot borrow a coalesced
                    # notification for a generic launch of a different image.
                    with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
                        meetings_mcp._INITIALIZE_BOOTSTRAP_SUPPRESS_REARM = True
            else:
                outcome = meetings_mcp._best_effort_launch_bundled_companion()
    finally:
        with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
            meetings_mcp._INITIALIZE_BOOTSTRAP_REPLACING_OWNER = False
            if meetings_mcp._INITIALIZE_BOOTSTRAP_SUPPRESS_REARM:
                meetings_mcp._INITIALIZE_BOOTSTRAP_SUPPRESS_REARM = False
                meetings_mcp._INITIALIZE_BOOTSTRAP_PENDING_REARM = False
                meetings_mcp._INITIALIZE_BOOTSTRAP_EXPLICIT_RECOVERY_REQUESTED = False
            if outcome is True:
                if meetings_mcp._INITIALIZE_BOOTSTRAP_EXPLICIT_RECOVERY_REQUESTED and (
                    shortcut_without_owner_response or has_pending_listener_recovery()
                ):
                    # Preserve a full-health request racing discovery, or a
                    # distinct listener failure after the final fresh state.
                    # The queued exact owner still needs its own health proof.
                    meetings_mcp._INITIALIZE_BOOTSTRAP_PENDING_REARM = False
                    meetings_mcp._INITIALIZE_BOOTSTRAP_COOLDOWN_WAKE_SCHEDULED = False
                    meetings_mcp._INITIALIZE_BOOTSTRAP_IN_FLIGHT_UNTIL_MONOTONIC = (
                        meetings_mcp.time.monotonic()
                        + meetings_mcp._INITIALIZE_BOOTSTRAP_ACCEPTED_LAUNCH_COOLDOWN_SECONDS
                    )
                    meetings_mcp._INITIALIZE_BOOTSTRAP_ATTEMPTED = True
                    start_pending_retry = True
                else:
                    # A connected worker is complete, not a process-lifetime latch.
                    # The production MCP may outlive several page opens, so a later
                    # open must be able to relaunch an app the user subsequently quit.
                    meetings_mcp._INITIALIZE_BOOTSTRAP_ATTEMPTED = False
                    meetings_mcp._INITIALIZE_BOOTSTRAP_IN_FLIGHT_UNTIL_MONOTONIC = 0.0
                    meetings_mcp._INITIALIZE_BOOTSTRAP_PENDING_REARM = False
                    meetings_mcp._INITIALIZE_BOOTSTRAP_EXPLICIT_RECOVERY_REQUESTED = False
                    meetings_mcp._INITIALIZE_BOOTSTRAP_COOLDOWN_WAKE_SCHEDULED = False
            elif outcome is None:
                meetings_mcp._INITIALIZE_BOOTSTRAP_ATTEMPTED = False
                meetings_mcp._INITIALIZE_BOOTSTRAP_IN_FLIGHT_UNTIL_MONOTONIC = max(
                    meetings_mcp._INITIALIZE_BOOTSTRAP_IN_FLIGHT_UNTIL_MONOTONIC,
                    meetings_mcp.time.monotonic()
                    + meetings_mcp._INITIALIZE_BOOTSTRAP_ACCEPTED_LAUNCH_COOLDOWN_SECONDS,
                )
                if (
                    meetings_mcp._INITIALIZE_BOOTSTRAP_PENDING_REARM
                    and not meetings_mcp._INITIALIZE_BOOTSTRAP_COOLDOWN_WAKE_SCHEDULED
                ):
                    meetings_mcp._INITIALIZE_BOOTSTRAP_COOLDOWN_WAKE_SCHEDULED = True
                    start_cooldown_wake = True
            else:
                meetings_mcp._INITIALIZE_BOOTSTRAP_ATTEMPTED = False
                meetings_mcp._INITIALIZE_BOOTSTRAP_IN_FLIGHT_UNTIL_MONOTONIC = 0.0
                meetings_mcp._INITIALIZE_BOOTSTRAP_COOLDOWN_WAKE_SCHEDULED = False
                if meetings_mcp._INITIALIZE_BOOTSTRAP_PENDING_REARM:
                    # Preserve one bootstrap signal that arrived while the
                    # first daemon was still deciding whether its launch was
                    # accepted. Explicit failures have no cooldown, so the
                    # follow-up can run immediately in its own daemon. It
                    # still owns a fresh bounded loader window while that
                    # retry proves the plugin-local app; otherwise status or
                    # settings can flash false offline/install truth between
                    # the two daemon attempts.
                    meetings_mcp._INITIALIZE_BOOTSTRAP_PENDING_REARM = False
                    meetings_mcp._INITIALIZE_BOOTSTRAP_IN_FLIGHT_UNTIL_MONOTONIC = (
                        meetings_mcp.time.monotonic()
                        + meetings_mcp._INITIALIZE_BOOTSTRAP_ACCEPTED_LAUNCH_COOLDOWN_SECONDS
                    )
                    meetings_mcp._INITIALIZE_BOOTSTRAP_ATTEMPTED = True
                    start_pending_retry = True
        if start_cooldown_wake:
            meetings_mcp._start_initialize_bootstrap_daemon_best_effort(
                meetings_mcp._run_initialize_companion_bootstrap_cooldown_wake,
                "chatgpt-meetings-bootstrap-cooldown",
                owns_cooldown_wake=True,
            )
        elif start_pending_retry:
            meetings_mcp._start_initialize_bootstrap_daemon_best_effort(
                meetings_mcp._run_initialize_companion_bootstrap,
                "chatgpt-meetings-bootstrap-retry",
                owns_attempt=True,
            )


def _run_initialize_companion_bootstrap_cooldown_wake() -> None:
    """Consume one remembered bootstrap signal after a launch cooldown.

    The wake never opens directly. It waits for the in-flight window, consumes
    the pending signal once, then enters the ordinary bootstrap worker whose
    first action authenticates/checks any descriptor. A companion that became
    ready during the cooldown therefore wins without a duplicate open.
    """

    while True:
        with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
            deadline = meetings_mcp._INITIALIZE_BOOTSTRAP_IN_FLIGHT_UNTIL_MONOTONIC
        remaining = deadline - meetings_mcp.time.monotonic()
        if remaining > 0:
            meetings_mcp.time.sleep(remaining)
            continue
        with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
            if not meetings_mcp._INITIALIZE_BOOTSTRAP_PENDING_REARM:
                meetings_mcp._INITIALIZE_BOOTSTRAP_COOLDOWN_WAKE_SCHEDULED = False
                return
            if (
                meetings_mcp._INITIALIZE_BOOTSTRAP_IN_FLIGHT_UNTIL_MONOTONIC
                > meetings_mcp.time.monotonic()
            ):
                continue
            meetings_mcp._INITIALIZE_BOOTSTRAP_PENDING_REARM = False
            meetings_mcp._INITIALIZE_BOOTSTRAP_COOLDOWN_WAKE_SCHEDULED = False
            meetings_mcp._INITIALIZE_BOOTSTRAP_IN_FLIGHT_UNTIL_MONOTONIC = 0.0
        meetings_mcp.schedule_initialize_companion_bootstrap()
        return


def _start_initialize_bootstrap_daemon(
    target: Callable[[], None],
    name: str,
) -> None:
    """Start one named daemon without making its caller wait for it."""

    meetings_mcp.threading.Thread(
        target=target,
        name=name,
        daemon=True,
    ).start()


def _start_initialize_bootstrap_daemon_best_effort(
    target: Callable[[], None],
    name: str,
    *,
    owns_attempt: bool = False,
    owns_cooldown_wake: bool = False,
) -> bool:
    """Start one daemon and release scheduler ownership if creation fails."""

    try:
        meetings_mcp._start_initialize_bootstrap_daemon(target, name)
    except Exception:
        # Thread creation is still on the synchronous open/initialize boundary.
        # Keep the MCP usable and avoid a phantom worker suppressing later opens.
        with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
            if owns_attempt:
                meetings_mcp._INITIALIZE_BOOTSTRAP_ATTEMPTED = False
                meetings_mcp._INITIALIZE_BOOTSTRAP_IN_FLIGHT_UNTIL_MONOTONIC = 0.0
            if owns_cooldown_wake:
                meetings_mcp._INITIALIZE_BOOTSTRAP_COOLDOWN_WAKE_SCHEDULED = False
        return False
    return True


def schedule_initialize_companion_bootstrap(*, require_owner_response: bool = False) -> None:
    """Start one non-blocking, process-local companion bootstrap attempt."""

    if meetings_mcp._native_runtime_host_is_unsupported():
        return

    # The permission-free E2E probe needs installAndLaunch to be the one
    # observable launcher so it can bind that exact child PID to descriptor
    # and signature evidence. Production ignores this switch unless the
    # isolated lane itself is explicitly enabled.
    if (
        meetings_mcp.os.environ.get("CHATGPT_MEETINGS_E2E_ISOLATED") == "1"
        and meetings_mcp.os.environ.get("CHATGPT_MEETINGS_E2E_SUPPRESS_BOOTSTRAP") == "1"
    ):
        try:
            if meetings_mcp.configured_e2e_isolation() is not None:
                return
        except meetings_mcp.NativeRuntimeError:
            # A malformed or unclaimed root is not an E2E lane. Preserve the
            # normal best-effort bootstrap semantics; launch_current itself
            # remains fail-closed if hostile E2E variables are still present.
            pass
    start_cooldown_wake = False
    start_bootstrap = False
    with meetings_mcp._INITIALIZE_BOOTSTRAP_LOCK:
        if require_owner_response:
            meetings_mcp._INITIALIZE_BOOTSTRAP_EXPLICIT_RECOVERY_REQUESTED = True
        if meetings_mcp._INITIALIZE_BOOTSTRAP_ATTEMPTED:
            # If the worker later reports an accepted-but-not-yet-connected
            # launch, it will carry this one signal into the cooldown wake.
            meetings_mcp._INITIALIZE_BOOTSTRAP_PENDING_REARM = True
            return
        if (
            meetings_mcp._INITIALIZE_BOOTSTRAP_IN_FLIGHT_UNTIL_MONOTONIC
            > meetings_mcp.time.monotonic()
        ):
            meetings_mcp._INITIALIZE_BOOTSTRAP_PENDING_REARM = True
            if not meetings_mcp._INITIALIZE_BOOTSTRAP_COOLDOWN_WAKE_SCHEDULED:
                meetings_mcp._INITIALIZE_BOOTSTRAP_COOLDOWN_WAKE_SCHEDULED = True
                start_cooldown_wake = True
        elif meetings_mcp._INITIALIZE_BOOTSTRAP_COOLDOWN_WAKE_SCHEDULED:
            # The already-scheduled wake owns the expiry edge. Let it consume
            # the pending signal instead of racing a second daemon here.
            meetings_mcp._INITIALIZE_BOOTSTRAP_PENDING_REARM = True
        else:
            # Status polls can arrive immediately after initialize/page open
            # while this daemon crosses the one required launch verification.
            # Mark the same bounded launch window before starting the thread,
            # so those polls avoid racing another deep verification. The
            # widget recognizes the fixed loader explicitly and keeps
            # Checking chrome until this deadline or a descriptor arrives.
            meetings_mcp._INITIALIZE_BOOTSTRAP_IN_FLIGHT_UNTIL_MONOTONIC = (
                meetings_mcp.time.monotonic()
                + meetings_mcp._INITIALIZE_BOOTSTRAP_ACCEPTED_LAUNCH_COOLDOWN_SECONDS
            )
            meetings_mcp._INITIALIZE_BOOTSTRAP_PENDING_REARM = False
            meetings_mcp._INITIALIZE_BOOTSTRAP_ATTEMPTED = True
            start_bootstrap = True
    if start_cooldown_wake:
        meetings_mcp._start_initialize_bootstrap_daemon_best_effort(
            meetings_mcp._run_initialize_companion_bootstrap_cooldown_wake,
            "chatgpt-meetings-bootstrap-cooldown",
            owns_cooldown_wake=True,
        )
    elif start_bootstrap:
        meetings_mcp._start_initialize_bootstrap_daemon_best_effort(
            meetings_mcp._run_initialize_companion_bootstrap,
            "chatgpt-meetings-bootstrap",
            owns_attempt=True,
        )
