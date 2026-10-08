"""Account-scoped operator and visitor policies for the Meetings plugin."""

from __future__ import annotations

import json
import threading
from collections.abc import Callable, Mapping
from dataclasses import dataclass, field
from typing import Generic, Literal, Protocol, TypedDict, TypeVar, runtime_checkable

from codex_auth_client import AuthMaterial, ChatGPTAuthProvider
from companion_control_v2 import MeetingsEligibility
from meetings_api_client_common import record_owner_scope_fingerprint
from meetings_api_client_transport import MAXIMUM_PAGE_RESPONSE_BYTES, RecordHTTPResult
from meetings_client_policy_defaults import CODEX_MINIMUM_VERSION
from meetings_prompt import InvalidArguments
from native_runtime import NativeRuntimeError, RuntimeManager

from helpers import is_json, unique_json_object

ServiceCapacity = Literal["off", "warning", "blocked"]
PluginAvailabilityState = Literal["checking", "unavailable", "resolved"]
_POLICY_REFRESH_SECONDS = 600
_INITIAL_POLICY_RETRY_SECONDS = 30


@dataclass(frozen=True)
class PluginClientContext:
    """Finite, non-authorizing visitor attributes used only for UI policy targeting."""

    system_name: str
    surface: str
    # The build is observed per request; policy targeting/cache identity stays finite.
    codex_version: str = field(default="", compare=False)


@dataclass(frozen=True)
class PluginClientPolicy:
    service_capacity: ServiceCapacity = "off"
    device_supported: bool = True
    availability_state: PluginAvailabilityState = "resolved"


STRUCTURED_SETTINGS_READ_TOOL = "settings.read"
STRUCTURED_SETTINGS_UPDATE_TOOL = "settings.update"

_CLIENT_CONTEXT_TOOLS = frozenset(
    {
        "meetings.status",
        "meetings.start",
        "meetings.forceStart",
        "meetings.requestMicrophone",
        "meetings.requestSystemAudio",
        "meetings.recheckAudio",
        "meetings.openMicrophoneSettings",
        "meetings.openSystemAudioSettings",
        "meetings.installAndLaunch",
        "meetings.getSettings",
        "meetings.updateSettings",
        STRUCTURED_SETTINGS_READ_TOOL,
        STRUCTURED_SETTINGS_UPDATE_TOOL,
    }
)
_CLIENT_CONTEXT_GATEWAY_REQUESTS = frozenset(
    {
        "local.forceStart",
        "local.requestMicrophone",
        "local.requestSystemAudio",
        "local.recheckAudio",
        "local.openMicrophoneSettings",
        "local.openSystemAudioSettings",
        "local.installAndLaunch",
        "local.getSettings",
        "local.updateSettings",
        "settings.get",
        "settings.update",
    }
)


def parse_plugin_client_context(
    name: str, value: object, *, request: object, app_ui: bool, codex_version: str = ""
) -> PluginClientContext:
    """Validate visitor attributes only for supported app-only tool calls.

    Args:
        name: Canonical tool name after app-profile routing.
        value: Untrusted clientContext argument.
        request: Gateway request discriminator, if supplied.
        app_ui: Whether the active MCP profile permits app-only tools.
        codex_version: Observed desktop host metadata, preferred over UI context.

    Returns:
        Validated system and surface attributes for this request.

    Raises:
        InvalidArguments: The tool/profile or visitor attributes are unsupported.
    """
    allowed = name in _CLIENT_CONTEXT_TOOLS or (
        name == "chatgpt_meetings_get_snapshot"
        and isinstance(request, str)
        and request in _CLIENT_CONTEXT_GATEWAY_REQUESTS
    )
    if not app_ui or not allowed:
        raise InvalidArguments("clientContext is unsupported for this tool")
    if (
        not is_json(value)
        or not {"systemName", "surface"}.issubset(value)
        or not set(value).issubset({"systemName", "surface", "codexVersion"})
    ):
        raise InvalidArguments("clientContext requires systemName and surface")
    system_name, surface = value["systemName"], value["surface"]
    if (
        not isinstance(system_name, str)
        or system_name not in {"Windows", "Darwin", "Linux", "iOS", "Android", "unknown"}
        or not isinstance(surface, str)
        or surface not in {"web", "desktop", "mobile", "unknown"}
    ):
        raise InvalidArguments("clientContext is unsupported")
    return PluginClientContext(
        system_name,
        surface,
        update_version(codex_version or value.get("codexVersion", ""))
        if surface == "desktop"
        else "",
    )


@dataclass
class _PluginClientPolicyCache:
    policy: PluginClientPolicy
    refresh_at: float = 0.0
    required_updates: dict[str, tuple[str, str]] = field(default_factory=dict[str, tuple[str, str]])
    initial_retry_used: bool = False
    native_owned: bool = False
    operator_revision: int = 0
    native_owner: tuple[str, str, int] | None = None
    native_app_version: str = ""


def _initial_plugin_policy(client_context: PluginClientContext) -> PluginClientPolicy:
    # macOS is a product invariant; device support never waits for remote policy.
    macos = client_context.system_name == "Darwin"
    return PluginClientPolicy(
        device_supported=macos,
        availability_state="resolved" if macos else "checking",
    )


class RequiredUpdate(TypedDict):
    status: Literal["none", "warning", "required"]
    currentVersion: str
    minimumVersion: str
    warningVersion: str


@dataclass(frozen=True)
class NativeMeetingsPolicy:
    observation: MeetingsEligibility
    policy: PluginClientPolicy
    required_updates: dict[str, RequiredUpdate]
    blocks_start: bool


def project_native_meetings_policy(
    observation: MeetingsEligibility, *, windows: bool, codex_version: str
) -> NativeMeetingsPolicy:
    """Project native policy without another cache or coupling to audio readiness."""

    decision = observation.get("decision")
    if decision is None:
        # Preserve standalone macOS capture without requiring authentication or
        # networking. Windows retains its existing unresolved availability hold.
        codex = codex_required_update(codex_version)
        return NativeMeetingsPolicy(
            observation,
            PluginClientPolicy(
                device_supported=not windows,
                availability_state=(
                    ("unavailable" if observation["status"] == "error" else "checking")
                    if windows
                    else "resolved"
                ),
            ),
            {"app": required_update(""), "plugin": required_update(""), "codex": codex},
            windows or codex["status"] == "required",
        )
    updates: dict[str, RequiredUpdate] = {
        target: decision["requiredUpdates"][target] for target in ("app", "plugin", "codex")
    }
    # Older owners can know the unified config without the packaged baseline.
    # The plugin must enforce its own minimum even when it reuses that cache.
    remote_codex = updates["codex"]
    updates["codex"] = codex_required_update(
        codex_version or remote_codex["currentVersion"],
        remote_codex["minimumVersion"],
        remote_codex["warningVersion"],
    )
    return NativeMeetingsPolicy(
        observation,
        PluginClientPolicy(
            service_capacity=decision["serviceCapacity"],
            device_supported=decision["pluginAvailability"] == "available",
        ),
        updates,
        not decision["canUseMeetings"] or updates["codex"]["status"] == "required",
    )


@runtime_checkable
class CachedAuthProvider(Protocol):
    def peek_cached_chatgpt_auth(self) -> AuthMaterial | None: ...


REQUIRED_UPDATE_CONFIGS = {
    "app": ("chatgpt_meetings_app_required_update", "2005588112"),
    "plugin": ("chatgpt_meetings_plugin_required_update", "4063913208"),
}
CLIENT_POLICY_CONFIG = ("chatgpt_meetings_client_policy", "3108265259")
MINIMUM_VERSIONS_CONFIG = ("chatgpt_meetings_minimum_versions", "634879111")


def update_version(value: object) -> str:
    """Validate bounded release metadata once before policy comparison."""
    if not isinstance(value, str) or len(value) > 128:
        return ""
    try:
        RuntimeManager.native_release_version_key(value)
    except NativeRuntimeError:
        return ""
    return value


@dataclass(frozen=True)
class _DecodedClientPolicy:
    required_updates: dict[str, tuple[str, str]] = field(default_factory=dict[str, tuple[str, str]])
    service_capacity: ServiceCapacity | None = None


def _update_floors(value: object, *, complete: bool = False) -> tuple[str, str] | None:
    if not is_json(value) or (
        complete and not {"minimum_version", "warning_version"}.issubset(value)
    ):
        return None
    minimum, warning = value.get("minimum_version", ""), value.get("warning_version", "")
    if not all(
        isinstance(item, str) and (item == "" or update_version(item))
        for item in (minimum, warning)
    ):
        return None
    return update_version(minimum), update_version(warning)


def decode_client_policy(body: bytes) -> _DecodedClientPolicy:
    """Prefer one atomic policy; only its absence permits legacy rollout fallback."""
    decoded = decode_statsig_payload(body)
    if decoded is None or not is_json(configs := decoded.get("dynamic_configs")):
        return _DecodedClientPolicy()
    name, hashed = CLIENT_POLICY_CONFIG
    if name not in configs and hashed not in configs:
        updates = decode_required_updates(body)
        updates["codex"] = ("", "")
        _apply_minimum_versions(configs, updates)
        return _DecodedClientPolicy(updates, decode_service_capacity(body))
    if name in configs and hashed in configs:
        return _DecodedClientPolicy()
    config = configs.get(name, configs.get(hashed))
    if not is_json(config) or not is_json(values := config.get("value")):
        return _DecodedClientPolicy()
    if type(values.get("schema_version")) is not int or values["schema_version"] != 1:
        return _DecodedClientPolicy()
    capacity, availability = values.get("service_capacity"), values.get("plugin_availability")
    if not isinstance(capacity, str) or not isinstance(availability, str):
        return _DecodedClientPolicy()
    if capacity not in ("off", "warning", "blocked") or availability not in (
        "available",
        "coming_soon",
    ):
        return _DecodedClientPolicy()
    if not is_json(updates := values.get("updates")):
        return _DecodedClientPolicy()
    floors: dict[str, tuple[str, str]] = {}
    for target in ("app", "plugin", "codex"):
        parsed = _update_floors(updates.get(target), complete=True)
        if parsed is None:
            return _DecodedClientPolicy()
        floors[target] = parsed
    _apply_minimum_versions(configs, floors)
    return _DecodedClientPolicy(floors, capacity)


def _apply_minimum_versions(
    configs: Mapping[str, object], floors: dict[str, tuple[str, str]]
) -> None:
    """Map the compatibility app floor to the desktop, preserving canonical policy."""
    name, hashed = MINIMUM_VERSIONS_CONFIG
    if name in configs and hashed in configs:
        return
    config = configs.get(name, configs.get(hashed))
    if not is_json(config) or not is_json(values := config.get("value")):
        return
    for target, key in (("codex", "minimum_app_version"), ("plugin", "minimum_plugin_version")):
        minimum = update_version(values.get(key))
        current, warning = floors.get(target, ("", ""))
        if minimum and (
            not current
            or RuntimeManager.native_release_version_key(minimum)
            > RuntimeManager.native_release_version_key(current)
        ):
            floors[target] = (minimum, warning)


def required_update(current: str, minimum: str = "", warning: str = "") -> RequiredUpdate:
    def below(threshold: str) -> bool:
        return bool(threshold) and (
            not current
            or RuntimeManager.native_release_version_key(current)
            < RuntimeManager.native_release_version_key(threshold)
        )

    return {
        "status": "required" if below(minimum) else "warning" if below(warning) else "none",
        "currentVersion": current,
        "minimumVersion": minimum,
        "warningVersion": warning,
    }


def codex_required_update(version: str, minimum: str = "", warning: str = "") -> RequiredUpdate:
    """Use the packaged minimum before remote policy, which may only raise it."""

    current = update_version(version)
    minimum = max(
        (CODEX_MINIMUM_VERSION, update_version(minimum) or CODEX_MINIMUM_VERSION),
        key=RuntimeManager.native_release_version_key,
    )
    policy = required_update(current, minimum, update_version(warning))
    if not current:
        # An absent desktop observation does not prove an outdated host.
        policy["status"] = "none"
    return policy


def _evaluate_required_updates(
    configs: Mapping[str, tuple[str, str]],
    plugin_version: str,
    app_version: object,
    client_context: PluginClientContext | None,
) -> dict[str, RequiredUpdate]:
    versions = {"plugin": plugin_version, "app": app_version}
    if client_context is not None and client_context.surface == "desktop":
        versions["codex"] = client_context.codex_version
    return {
        target: (codex_required_update if target == "codex" else required_update)(
            update_version(version), *configs.get(target, ("", ""))
        )
        for target, version in versions.items()
    }


def decode_required_updates(body: bytes) -> dict[str, tuple[str, str]]:
    decoded = decode_statsig_payload(body)
    if decoded is None or not is_json(configs := decoded.get("dynamic_configs")):
        return {}
    result: dict[str, tuple[str, str]] = {}
    for target, (name, hashed) in REQUIRED_UPDATE_CONFIGS.items():
        if name in configs and hashed in configs:
            continue
        if name not in configs and hashed not in configs:
            result[target] = ("", "")
            continue
        config = configs.get(name, configs.get(hashed))
        if not is_json(config) or not is_json(values := config.get("value")):
            continue
        floors = _update_floors(values)
        if floors is not None:
            result[target] = floors
    return result


def decode_service_capacity(body: bytes) -> ServiceCapacity | None:
    """Accept only the versioned operator policy; malformed refreshes retain the cache."""
    decoded = decode_statsig_payload(body)
    if decoded is None or not is_json(configs := decoded.get("dynamic_configs")):
        return None
    name, hashed = "chatgpt_meetings_capacity", "130174101"
    if name in configs and hashed in configs:
        return None
    if name not in configs and hashed not in configs:
        return "off"
    config = configs.get(name, configs.get(hashed))
    if not is_json(config) or not is_json(values := config.get("value")):
        return None
    if type(values.get("schema_version")) is not int or values["schema_version"] != 1:
        return None
    mode = values.get("mode")
    if isinstance(mode, str) and (mode == "off" or mode == "warning" or mode == "blocked"):
        return mode
    return None


def decode_device_supported(body: bytes) -> bool | None:
    """Read device support without applying account or recording opt-in policy.

    Args:
        body: Authenticated Statsig bootstrap response.

    Returns:
        Whether the device is supported, or None for an absent or malformed decision.
    """
    decoded = decode_statsig_payload(body)
    if decoded is None or not is_json(gates := decoded.get("feature_gates")):
        return None
    name, hashed = "meetings_device_supported", "2084749772"
    if name in gates and hashed in gates:
        return None
    gate = gates.get(name, gates.get(hashed))
    if not is_json(gate):
        return None
    value = gate.get("value")
    return value if isinstance(value, bool) else None


def statsig_gate_enabled(payload: Mapping[str, object] | None, name: str, hashed: str) -> bool:
    """Read an explicit enabled gate without ambiguous plain/hashed entries.

    Args:
        payload: Strictly decoded authenticated Statsig bootstrap payload.
        name: Plain gate name.
        hashed: Statsig unsigned 32-bit name hash in decimal form.

    Returns:
        True only for one well-formed gate with the boolean value true.
    """
    if payload is None or not is_json(gates := payload.get("feature_gates")):
        return False
    gate = gates.get(name, gates.get(hashed))
    return not (name in gates and hashed in gates) and is_json(gate) and gate.get("value") is True


def decode_statsig_payload(body: bytes) -> dict[str, object] | None:
    # Codex bootstrap includes other clients' flags and can exceed 6 MiB.
    # Keep parsing bounded by the same ceiling as the authenticated transport.
    if len(body) > MAXIMUM_PAGE_RESPONSE_BYTES:
        return None
    try:
        envelope: object = json.loads(body.decode("utf-8"), object_pairs_hook=unique_json_object)
        if not is_json(envelope) or set(envelope) != {"statsigPayload"}:
            raise ValueError("invalid rollout envelope")
        payload = envelope["statsigPayload"]
        if (
            not isinstance(payload, str)
            or len(payload.encode("utf-8")) > MAXIMUM_PAGE_RESPONSE_BYTES
        ):
            raise ValueError("invalid rollout payload")
        decoded: object = json.loads(payload, object_pairs_hook=unique_json_object)
    except (UnicodeError, ValueError, RecursionError):
        return None
    return decoded if is_json(decoded) else None


class PolicyRequestContext(Protocol):
    auth: AuthMaterial
    deadline: float


_PolicyRequest = TypeVar("_PolicyRequest", bound=PolicyRequestContext)


class MeetingsClientPolicies(Generic[_PolicyRequest]):
    """Own policy state while the API client owns authenticated request execution."""

    def __init__(
        self,
        *,
        auth_client: ChatGPTAuthProvider,
        clock: Callable[[], float],
        begin_request: Callable[[threading.Event], _PolicyRequest],
        request_bootstrap: Callable[
            [_PolicyRequest, Mapping[str, object], threading.Event], RecordHTTPResult
        ],
        request_errors: tuple[type[Exception], ...],
        native_policy_owner_available: Callable[[PluginClientContext | None], bool] | None = None,
    ) -> None:
        self._auth_client = auth_client
        self._clock = clock
        self._begin_policy_request = begin_request
        self._request_policy_bootstrap = request_bootstrap
        self._policy_request_errors = request_errors
        self._native_policy_owner_available: Callable[[PluginClientContext | None], bool] = (
            native_policy_owner_available or (lambda _: False)
        )
        self._required_update_lock = threading.Lock()
        self._required_update_configs: dict[str, tuple[str, str]] = {}
        self._service_capacity: ServiceCapacity = "off"
        self._required_update_owner: str | None = None
        self._required_update_generation = 0
        self._required_update_stop = threading.Event()
        self._required_update_polling = False
        self._plugin_client_policies: dict[PluginClientContext, _PluginClientPolicyCache] = {}
        self._plugin_client_policy_wake = threading.Event()
        self._plugin_client_policy_polling = False

    def observe_native_policy(
        self,
        client_context: PluginClientContext,
        policy: NativeMeetingsPolicy,
        *,
        account_scope: str | None,
        native_owner: tuple[str, str, int],
        owner_is_current: Callable[[], bool],
        plugin_version: str,
    ) -> NativeMeetingsPolicy:
        """Hand accepted operator settings to the existing visitor fallback cache.

        The caller first validates the native account and acknowledged client
        context. Native recording authority is never transferred. Device support
        remains independently evaluated; native ownership fences fallback operator writes.
        """
        with self._required_update_lock:
            self._sync_required_update_owner()
            if not owner_is_current():
                return policy
            entry = self._plugin_client_policies.get(client_context)
            decision = policy.observation.get("decision")
            if decision is None:
                if (
                    entry is not None
                    and entry.native_owner == native_owner
                    and (account_scope is None or account_scope == self._required_update_owner)
                ):
                    # A new host build may await acknowledgement by this same
                    # owner. Keep operator floors, not its old native authority.
                    # Missing cached auth is transient; an observed account
                    # switch already revokes this entry in the owner sync above.
                    updates = _evaluate_required_updates(
                        entry.required_updates,
                        plugin_version,
                        entry.native_app_version,
                        client_context,
                    )
                    return NativeMeetingsPolicy(
                        policy.observation,
                        entry.policy,
                        updates,
                        policy.blocks_start
                        or entry.policy.service_capacity == "blocked"
                        or not entry.policy.device_supported
                        or any(update["status"] == "required" for update in updates.values()),
                    )
                # An unresolved successor must not resurrect its predecessor's
                # native decision after its next disconnect.
                if entry is not None:
                    entry.operator_revision += 1
                    entry.required_updates.clear()
                    entry.native_owner = None
                    entry.native_app_version = ""
                    entry.policy = PluginClientPolicy(
                        service_capacity="off",
                        device_supported=entry.policy.device_supported,
                        availability_state=entry.policy.availability_state,
                    )
                return policy
            if account_scope is None or account_scope != self._required_update_owner:
                return policy
            if entry is None:
                entry = _PluginClientPolicyCache(_initial_plugin_policy(client_context))
                self._plugin_client_policies[client_context] = entry
                self._plugin_client_policy_wake.set()
            # Native owns operator policy; preserve independently resolved device
            # support across repeated native snapshots.
            entry.policy = PluginClientPolicy(
                service_capacity=policy.policy.service_capacity,
                device_supported=entry.policy.device_supported,
                availability_state=entry.policy.availability_state,
            )
            entry.required_updates = {
                target: (
                    decision["requiredUpdates"][target]["minimumVersion"],
                    decision["requiredUpdates"][target]["warningVersion"],
                )
                for target in ("app", "plugin", "codex")
            }
            entry.operator_revision += 1
            entry.native_owned = True
            entry.native_owner = native_owner
            entry.native_app_version = decision["requiredUpdates"]["app"]["currentVersion"]
            return policy

    def has_native_policy_handoff(self, client_context: PluginClientContext) -> bool:
        """Check for a local visitor's accepted handoff without creating a cache or worker."""
        with self._required_update_lock:
            self._sync_required_update_owner()
            entry = self._plugin_client_policies.get(client_context)
            return entry is not None and entry.native_owner is not None

    def peek_required_updates(
        self,
        *,
        plugin_version: str,
        app_version: object,
        client_context: PluginClientContext | None = None,
    ) -> dict[str, RequiredUpdate]:
        """Read cached policy only; recording never waits for authentication or network."""
        with self._required_update_lock:
            self._sync_required_update_owner()
            entry = self._plugin_client_policies.get(client_context) if client_context else None
            # Preserve existing app/plugin restrictions while a visitor's first
            # policy is pending or malformed. Never borrow another visitor's cache.
            configs = {
                target: self._required_update_configs.get(target, ("", ""))
                for target in ("app", "plugin", "codex")
            }
            if entry is not None:
                configs.update(entry.required_updates)
            return _evaluate_required_updates(configs, plugin_version, app_version, client_context)

    def peek_service_capacity(self) -> ServiceCapacity:
        """Read the current owner's cached mode without auth or network on Start."""
        with self._required_update_lock:
            self._sync_required_update_owner()
            return self._service_capacity

    def peek_plugin_client_policy(
        self, client_context: PluginClientContext, *, plugin_version: str
    ) -> PluginClientPolicy:
        """Return cached visitor policy; schedule bounded background work without waiting."""
        with self._required_update_lock:
            self._sync_required_update_owner()
            if client_context not in self._plugin_client_policies:
                self._plugin_client_policies[client_context] = _PluginClientPolicyCache(
                    _initial_plugin_policy(client_context)
                )
                self._plugin_client_policy_wake.set()
            entry = self._plugin_client_policies[client_context]
            if entry.native_owned and not self._native_policy_owner_available(client_context):
                # Preserve the accepted settings while immediately resuming the
                # same fallback worker after disconnect or a legacy successor.
                entry.native_owned = False
                entry.refresh_at = 0.0
                self._plugin_client_policy_wake.set()
            policy = entry.policy
            start_worker = not self._plugin_client_policy_polling
            self._plugin_client_policy_polling = True
        if start_worker:
            threading.Thread(
                target=self._poll_plugin_client_policies,
                args=(plugin_version,),
                name="meetings-plugin-client-policy",
                daemon=True,
            ).start()
        return policy

    def _poll_plugin_client_policies(self, plugin_version: str) -> None:
        while not self._required_update_stop.is_set():
            self._plugin_client_policy_wake.clear()
            with self._required_update_lock:
                self._sync_required_update_owner()
                now = self._clock()
                due = [
                    context
                    for context, entry in self._plugin_client_policies.items()
                    if entry.refresh_at <= now
                ]
                for context in due:
                    self._plugin_client_policies[context].refresh_at = now + _POLICY_REFRESH_SECONDS
            for context in due:
                if self._required_update_stop.is_set():
                    return
                self._refresh_plugin_client_policy(context, plugin_version)
            with self._required_update_lock:
                delay = min(
                    (
                        entry.refresh_at - self._clock()
                        for entry in self._plugin_client_policies.values()
                    ),
                    default=_POLICY_REFRESH_SECONDS,
                )
            self._plugin_client_policy_wake.wait(max(0.0, delay))

    def _refresh_plugin_client_policy(
        self, client_context: PluginClientContext, plugin_version: str
    ) -> None:
        with self._required_update_lock:
            generation: int | None = self._sync_required_update_owner()
            entry = self._plugin_client_policies.get(client_context)
            if entry is None:
                return
            if self._native_policy_owner_available(client_context):
                entry.native_owned = True
                if client_context.system_name == "Darwin":
                    # Native supplies capacity/version rules; Mac needs no device lookup.
                    return
                # Other platforms still need an independent device-gate refresh.
            operator_revision = entry.operator_revision
        try:
            context = self._begin_policy_request(self._required_update_stop)
            owner = record_owner_scope_fingerprint(context.auth)
            with self._required_update_lock:
                generation = self._sync_required_update_owner(context.auth)
                if owner is None or owner != self._required_update_owner:
                    generation = None
                    return
                if self._plugin_client_policies.get(client_context) is not entry:
                    return
                entry.refresh_at = self._clock() + _POLICY_REFRESH_SECONDS
            context.deadline = min(context.deadline, self._clock() + 5.0)
            result = self._request_policy_bootstrap(
                context,
                {
                    "brand_name": "chatgpt-meetings",
                    "window_type": client_context.surface,
                    "system_name": client_context.system_name,
                    "app_version": plugin_version,
                },
                self._required_update_stop,
            )
            if owner != record_owner_scope_fingerprint(context.auth):
                return
            decoded = decode_client_policy(result.body)
            device_supported = (
                True
                if client_context.system_name == "Darwin"
                else decode_device_supported(result.body)
            )
            with self._required_update_lock:
                if (
                    generation != self._sync_required_update_owner()
                    or self._plugin_client_policies.get(client_context) is not entry
                ):
                    return
                # A request predating a native handoff may still resolve the
                # device gate, but cannot replace newer operator restrictions.
                owns_operators = (
                    not entry.native_owned and entry.operator_revision == operator_revision
                )
                if owns_operators:
                    entry.required_updates.update(decoded.required_updates)
                entry.policy = PluginClientPolicy(
                    service_capacity=decoded.service_capacity
                    if owns_operators and decoded.service_capacity is not None
                    else entry.policy.service_capacity,
                    device_supported=(
                        device_supported
                        if device_supported is not None
                        else entry.policy.device_supported
                    ),
                    availability_state=(
                        "resolved"
                        if device_supported is not None
                        else entry.policy.availability_state
                    ),
                )
        except self._policy_request_errors:
            # Non-Mac devices start held; only a valid explicit decision changes that.
            pass
        finally:
            with self._required_update_lock:
                if (
                    generation == self._sync_required_update_owner()
                    and self._plugin_client_policies.get(client_context) is entry
                    and entry.policy.availability_state != "resolved"
                ):
                    entry.policy = PluginClientPolicy(
                        service_capacity=entry.policy.service_capacity,
                        device_supported=entry.policy.device_supported,
                        availability_state="unavailable",
                    )
                    # One early retry recovers a cold-start failure without changing the
                    # steady-state refresh cadence or making UI/Start wait on the network.
                    if not entry.initial_retry_used:
                        entry.initial_retry_used = True
                        entry.refresh_at = self._clock() + _INITIAL_POLICY_RETRY_SECONDS

    def _sync_required_update_owner(self, auth: AuthMaterial | None = None) -> int:
        """Under the policy lock, discard floors belonging to a different observed owner."""
        if isinstance(self._auth_client, CachedAuthProvider):
            auth = self._auth_client.peek_cached_chatgpt_auth()
        owner = record_owner_scope_fingerprint(auth) if auth is not None else None
        if owner is None:
            # Expiry or a transient verification failure is not an observed switch.
            return self._required_update_generation
        if owner != self._required_update_owner:
            self._required_update_owner = owner
            self._required_update_generation += 1
            self._required_update_configs.clear()
            self._service_capacity = "off"
            for client_context, entry in self._plugin_client_policies.items():
                entry.policy = _initial_plugin_policy(client_context)
                entry.required_updates.clear()
                entry.refresh_at = 0.0
                entry.initial_retry_used = False
                entry.native_owned = False
                entry.native_owner = None
                entry.native_app_version = ""
            self._plugin_client_policy_wake.set()
        return self._required_update_generation

    def start_required_update_polling(self, *, plugin_version: str) -> None:
        """Refresh operator policies every ten minutes, even with no visible UI."""
        with self._required_update_lock:
            if self._required_update_polling:
                return
            self._required_update_polling = True
        threading.Thread(
            target=self._poll_required_updates,
            args=(plugin_version,),
            name="meetings-required-update",
            daemon=True,
        ).start()

    def stop_required_update_polling(self) -> None:
        self._required_update_stop.set()
        self._plugin_client_policy_wake.set()

    def _poll_required_updates(self, plugin_version: str) -> None:
        while not self._required_update_stop.is_set():
            self._refresh_required_updates(plugin_version)
            if self._required_update_stop.wait(_POLICY_REFRESH_SECONDS):
                break

    def _refresh_required_updates(self, plugin_version: str) -> None:
        if self._native_policy_owner_available(None):
            return
        try:
            context = self._begin_policy_request(self._required_update_stop)
            owner = record_owner_scope_fingerprint(context.auth)
            with self._required_update_lock:
                generation = self._sync_required_update_owner(context.auth)
                if owner is None or owner != self._required_update_owner:
                    return
            context.deadline = min(context.deadline, self._clock() + 5.0)
            result = self._request_policy_bootstrap(
                context,
                {
                    "brand_name": "chatgpt-meetings",
                    "window_type": "mcp",
                    "app_version": plugin_version,
                },
                self._required_update_stop,
            )
            if owner != record_owner_scope_fingerprint(context.auth):
                return
            decoded = decode_client_policy(result.body)
            with self._required_update_lock:
                if generation == self._sync_required_update_owner():
                    self._required_update_configs.update(decoded.required_updates)
                    if decoded.service_capacity is not None:
                        self._service_capacity = decoded.service_capacity
        except self._policy_request_errors:
            # Preserve a known restriction through transient failure; explicit empty
            # thresholds in a successful refresh remove it.
            pass
