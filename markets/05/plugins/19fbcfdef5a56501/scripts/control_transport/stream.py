"""Meetings-specific contracts and passive state over the portable live client."""

from __future__ import annotations

import secrets
import threading
import time
from collections.abc import Callable
from pathlib import Path

from control_projection import UPDATE_HANDOFF_CAPABILITY, UPDATE_HANDOFF_WORK_FENCE_CAPABILITY
from control_protocol import ControlUnavailable, control_transport_error
from control_transport.discovery import (
    parse_plugin_core_version,
    require_stream_lease,
    require_stream_owner,
)
from control_transport.live_client import LiveJsonRpcClient, LiveOwner, LiveTransportError
from control_transport.status_cache import NativeStatusCache, StatusBinding, native_status_cache
from meetings_sentry import plugin_version
from recording_control_action_contract import ControlAction
from recording_control_stream_contract import (
    CONTROL_STREAM_CONTROL_METHOD,
    CONTROL_STREAM_DARWIN_CAPABILITIES,
    CONTROL_STREAM_LIVE_PROTOCOL_VERSION,
    CONTROL_STREAM_MAX_FRAME_BYTES,
    CONTROL_STREAM_MAX_REQUEST_TTL_MILLIS,
    CONTROL_STREAM_SCHEMA_VERSION,
    CONTROL_STREAM_WINDOWS_CAPABILITIES,
    ControlStreamDescriptor,
    ControlStreamInitializeParams,
    ControlStreamJsonRpcRequest,
    is_control_stream_control_params,
    is_control_stream_descriptor,
    is_control_stream_initialize_params,
    is_control_stream_initialize_result,
    is_control_stream_json_rpc_request,
    is_control_stream_json_rpc_response,
    is_control_stream_negotiation,
    is_control_stream_state_notification,
)
from recording_status_contract import is_recording_status_response

from helpers import is_json

_STREAM_CAPABILITY = "control.local-stream.v1"
_SUPPORTED_CAPABILITIES = frozenset(
    (
        *CONTROL_STREAM_DARWIN_CAPABILITIES,
        *CONTROL_STREAM_WINDOWS_CAPABILITIES,
        _STREAM_CAPABILITY,
    )
) - frozenset({"calendar.automation-sync.v1", "home.cache.refresh.v1"})
_UPDATE_HANDOFF_CAPABILITIES = frozenset(
    (UPDATE_HANDOFF_CAPABILITY, UPDATE_HANDOFF_WORK_FENCE_CAPABILITY)
)


def _require_fresh_control_request(issued_at_millis: int, request_ttl_millis: int) -> None:
    now_millis = int(time.time() * 1000)
    maximum_future_skew = min(request_ttl_millis, CONTROL_STREAM_MAX_REQUEST_TTL_MILLIS)
    if not now_millis - request_ttl_millis <= issued_at_millis <= now_millis + maximum_future_skew:
        raise ControlUnavailable("native control stream request is stale")


class StreamTransport:
    """Generated native authority, owner provenance, and passive pushed state."""

    def __init__(self, root: Path, descriptor: ControlStreamDescriptor) -> None:
        if not is_control_stream_descriptor(descriptor):
            raise ControlUnavailable("native control stream descriptor is malformed")
        self._root = root
        self._descriptor = descriptor
        self._cache: NativeStatusCache = native_status_cache()
        self._lock = threading.RLock()
        self._connect_lock = threading.RLock()
        self._closed = False
        self._binding: StatusBinding | None = None
        self._negotiated_capabilities: frozenset[str] = frozenset()
        self._last_notification_revision = 0
        self._live = LiveJsonRpcClient(
            LiveOwner(
                endpoint=descriptor["endpoint"],
                pid=descriptor["pid"],
                transport=descriptor["transport"],
            ),
            maximum_frame_bytes=CONTROL_STREAM_MAX_FRAME_BYTES,
            verify_owner=self._verify_owner,
            on_notification=self._accept_notification,
            validate_response=self._validate_response,
            on_disconnect=self._disconnected,
        )

    @property
    def active_binding(self) -> StatusBinding | None:
        return self._binding

    @property
    def closed(self) -> bool:
        with self._lock:
            return self._closed

    @property
    def negotiated_capabilities(self) -> frozenset[str]:
        with self._lock:
            return self._negotiated_capabilities

    def connect(
        self,
        *,
        deadline: float,
        cancellation_event: threading.Event | None = None,
    ) -> None:
        """Publish native state only after the reusable client proves its owner."""

        while True:
            if cancellation_event is not None and cancellation_event.is_set():
                raise ControlUnavailable("native control stream request was cancelled")
            with self._lock:
                if self._closed:
                    raise ControlUnavailable("native control stream is closed")
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise ControlUnavailable("native control stream request timed out")
            if self._connect_lock.acquire(timeout=min(0.05, remaining)):
                break

        try:
            if self._closed:
                raise ControlUnavailable("native control stream is closed")
            if self._binding is not None and self._live.connected:
                return
            if self._binding is not None:
                self._disconnected()
            version = plugin_version(Path(__file__).resolve().parents[2])
            minimum = self._descriptor["compatibility"]["destination"]["minimumPluginVersion"]
            version_core = parse_plugin_core_version(version)
            minimum_core = parse_plugin_core_version(minimum)
            if (
                version is None
                or version_core is None
                or minimum_core is None
                or version_core < minimum_core
            ):
                raise ControlUnavailable("native control stream plugin version is unsupported")
            capabilities = [
                capability
                for capability in self._descriptor["capabilities"]
                if capability in _SUPPORTED_CAPABILITIES
            ]
            client_version = ".".join(str(component) for component in version_core)
            parameters: ControlStreamInitializeParams = {
                "clientKind": "chatgpt-meetings-plugin",
                "clientVersion": client_version,
                "supportedStreamSchemaVersions": [CONTROL_STREAM_SCHEMA_VERSION],
                "supportedLiveControlProtocolVersions": [CONTROL_STREAM_LIVE_PROTOCOL_VERSION],
                "capabilities": capabilities,
            }
            if not is_control_stream_initialize_params(parameters):
                raise ControlUnavailable("native control stream initialization is malformed")
            request: ControlStreamJsonRpcRequest = {
                "jsonrpc": "2.0",
                "id": f"initialize_{secrets.token_urlsafe(18)}",
                "method": "meetings.initialize",
                "params": parameters,
            }
            if not is_control_stream_json_rpc_request(request):
                raise ControlUnavailable("native control stream initialization is malformed")

            negotiated_capabilities: frozenset[str] = frozenset()

            def validate_result(result: dict[str, object]) -> None:
                nonlocal negotiated_capabilities
                if (
                    not is_control_stream_initialize_result(result)
                    or not is_control_stream_negotiation(parameters, result)
                    or result["epoch"] != self._descriptor["epoch"]
                    or result["platform"] != self._descriptor["platform"]
                    or result["appVersion"] != self._descriptor["appVersion"]
                    or _STREAM_CAPABILITY not in result["capabilities"]
                ):
                    raise ControlUnavailable(
                        "native control stream owner negotiation does not match"
                    )
                negotiated_capabilities = frozenset(result["capabilities"])

            def publish_initial_state(result: dict[str, object]) -> None:
                binding = self._cache.connect(
                    epoch=self._descriptor["epoch"],
                    pid=self._descriptor["pid"],
                    session_id=secrets.token_urlsafe(24),
                )
                try:
                    if not self._cache.publish(
                        binding,
                        self._status_response(result.get("state")),
                    ):
                        raise ControlUnavailable("native control stream initial state is malformed")
                    with self._lock:
                        if self._closed:
                            raise ControlUnavailable("native control stream is closed")
                        self._binding = binding
                        self._negotiated_capabilities = negotiated_capabilities
                        self._last_notification_revision = 0
                except Exception:
                    self._cache.disconnect(binding)
                    raise

            try:
                self._live.connect(
                    dict(request),
                    validate_result=validate_result,
                    deadline=deadline,
                    cancellation_event=cancellation_event,
                    on_initialized=publish_initial_state,
                )
            except LiveTransportError as exc:
                self._disconnected()
                raise control_transport_error(exc, str(exc)) from exc
            except Exception:
                self._disconnected()
                raise
        finally:
            # EOF retirement never waits behind a potentially long native
            # handshake. Its owner finishes cleanup before releasing this
            # connection gate, so a late handshake cannot resurrect a slot.
            with self._lock:
                if self._closed:
                    self._live.close()
                    self._disconnected()
                self._connect_lock.release()

    def request(
        self,
        method: str,
        params: dict[str, object],
        *,
        request_id: str,
        deadline: float,
        cancellation_event: threading.Event | None = None,
        on_sent: Callable[[], None] | None = None,
    ) -> dict[str, object]:
        """Validate one generated request; the canonical client sends it once."""

        if (
            method != CONTROL_STREAM_CONTROL_METHOD
            or not is_control_stream_control_params(params)
            or params["requestId"] != request_id
        ):
            raise ControlUnavailable("native control stream request is malformed")
        if params["action"] == ControlAction.QUIT_FOR_UPDATE.value and (
            not _UPDATE_HANDOFF_CAPABILITIES.issubset(self.negotiated_capabilities)
        ):
            raise ControlUnavailable("native control stream update handoff was not negotiated")
        if (
            params["action"] == ControlAction.RETRY_UPLOAD_TARGET.value
            and "upload.manual-retry.targeted.v1" not in self.negotiated_capabilities
        ):
            raise ControlUnavailable("native targeted upload retry was not negotiated")
        _require_fresh_control_request(
            params["issuedAtMillis"],
            self._descriptor["requestTTLMillis"],
        )
        request: ControlStreamJsonRpcRequest = {
            "jsonrpc": "2.0",
            "id": request_id,
            "method": "meetings.control",
            "params": params,
        }
        if not is_control_stream_json_rpc_request(request):
            raise ControlUnavailable("native control stream request is malformed")
        try:
            return self._live.request(
                dict(request),
                deadline=deadline,
                cancellation_event=cancellation_event,
                before_send=lambda: _require_fresh_control_request(
                    params["issuedAtMillis"],
                    self._descriptor["requestTTLMillis"],
                ),
                on_sent=on_sent,
            )
        except LiveTransportError as exc:
            raise control_transport_error(exc, str(exc)) from exc

    def close(self) -> None:
        with self._lock:
            self._closed = True
            if not self._connect_lock.acquire(blocking=False):
                return
            try:
                self._live.close()
                self._disconnected()
            finally:
                self._connect_lock.release()

    def _verify_owner(self) -> None:
        require_stream_owner(
            self._root,
            self._descriptor,
            peer_pid=self._descriptor["pid"],
        )

    def _status_response(self, state: object) -> dict[str, object]:
        if not is_json(state):
            raise ControlUnavailable("native control stream state is malformed")
        response: dict[str, object] = {
            "ok": True,
            "state": state,
            "companionPid": self._descriptor["pid"],
        }
        if "schemaVersion" in state:
            response["schemaVersion"] = state["schemaVersion"]
        return response

    def _accept_notification(self, message: dict[str, object]) -> None:
        if not is_control_stream_state_notification(message):
            raise ControlUnavailable("native control stream notification is malformed")
        require_stream_lease(self._root, self._descriptor)
        params = message["params"]
        revision = params["revision"]
        if (
            params["epoch"] != self._descriptor["epoch"]
            or revision <= self._last_notification_revision
        ):
            raise ControlUnavailable("native control stream state owner or revision changed")
        binding = self._binding
        if binding is None or not self._cache.publish(
            binding,
            self._status_response(params["state"]),
        ):
            raise ControlUnavailable("native control stream state owner changed")
        self._last_notification_revision = revision

    @staticmethod
    def _validate_response(message: dict[str, object]) -> None:
        if not is_control_stream_json_rpc_response(message):
            raise ControlUnavailable("native control stream response is malformed")
        if "result" in message and not is_recording_status_response(message["result"]):
            raise ControlUnavailable("native control stream response result is malformed")

    def _disconnected(self) -> None:
        with self._lock:
            binding, self._binding = self._binding, None
            self._negotiated_capabilities = frozenset()
            self._last_notification_revision = 0
        if binding is not None:
            self._cache.disconnect(binding)
