"""Fail-closed live-stream discovery for authenticated native owners."""

from __future__ import annotations

import os
import re
import stat
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from control_protocol import ControlUnavailable
from recording_control_action_contract import is_control_identifier
from recording_control_stream_contract import (
    CONTROL_STREAM_LIVE_PROTOCOL_VERSION,
    CONTROL_STREAM_SCHEMA_VERSION,
    ControlStreamDescriptor,
    is_control_stream_descriptor,
)

from helpers import is_json, is_json_array

_STREAM_DESCRIPTOR_FILENAME = "stream-descriptor.json"
_STREAM_CAPABILITY = "control.local-stream.v1"
_CAPABILITY = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\.v[0-9]+\Z")
_SEMANTIC_VERSION = re.compile(
    r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-local\.[a-f0-9]{32})?\Z"
)
_SHA256 = re.compile(r"[a-f0-9]{64}\Z")
_WINDOWS_PLATFORMS = frozenset({"windows-x64", "windows-arm64"})


def _darwin_socket_root() -> Path:
    """Return the fixed production root for native Darwin control sockets."""

    return Path("/private/tmp")


@dataclass(frozen=True, repr=False)
class StreamDiscovery:
    """The untouched descriptor for an exact live stream-native owner."""

    root: Path
    descriptor: ControlStreamDescriptor


def parse_plugin_core_version(value: object) -> tuple[int, int, int] | None:
    """Return the compatibility core for a release or immutable local build."""

    if not isinstance(value, str) or len(value) > 80:
        return None
    matched = _SEMANTIC_VERSION.fullmatch(value)
    if matched is None:
        return None
    major, minor, patch = matched.groups()
    return int(major), int(minor), int(patch)


def _require_compatible_stream_owner(
    value: dict[str, object],
    *,
    expected_app_target: str,
    plugin_version: Callable[[], str | None],
) -> ControlStreamDescriptor:
    candidate: object = value
    try:
        valid = is_control_stream_descriptor(candidate)
    except (TypeError, ValueError, RecursionError):
        valid = False
    if not valid or not is_control_stream_descriptor(candidate):
        raise ControlUnavailable("native control stream descriptor is malformed")

    if (
        candidate["schemaVersion"] != CONTROL_STREAM_SCHEMA_VERSION
        or type(candidate["liveControlProtocolVersion"]) is not int
        or candidate["liveControlProtocolVersion"] != CONTROL_STREAM_LIVE_PROTOCOL_VERSION
        or not is_control_identifier(candidate["epoch"])
        or candidate["appTarget"] != expected_app_target
    ):
        raise ControlUnavailable("native control stream authority does not match")

    capabilities: object = candidate["capabilities"]
    if (
        not is_json_array(capabilities)
        or not 1 <= len(capabilities) <= 64
        or not all(
            isinstance(capability, str)
            and len(capability) <= 128
            and _CAPABILITY.fullmatch(capability) is not None
            for capability in capabilities
        )
        or len(set(capabilities)) != len(capabilities)
        or _STREAM_CAPABILITY not in capabilities
    ):
        raise ControlUnavailable("native control stream capabilities do not match")

    compatibility: object = candidate["compatibility"]
    source = compatibility.get("source") if is_json(compatibility) else None
    destination = compatibility.get("destination") if is_json(compatibility) else None
    minimum_version = (
        parse_plugin_core_version(destination.get("minimumPluginVersion"))
        if is_json(destination)
        else None
    )
    installed_version = parse_plugin_core_version(plugin_version())
    if (
        not is_json(source)
        or source.get("kind") != "chatgpt-meetings-native"
        or source.get("version") != candidate["appVersion"]
        or not is_json(destination)
        or destination.get("kind") != "chatgpt-meetings-plugin"
        or minimum_version is None
        or installed_version is None
        or installed_version < minimum_version
    ):
        raise ControlUnavailable("native control stream compatibility does not match")

    if candidate["platform"] in _WINDOWS_PLATFORMS:
        digest = candidate.get("executableSHA256")
        if not isinstance(digest, str) or _SHA256.fullmatch(digest) is None:
            raise ControlUnavailable("native control executable identity is malformed")
    return candidate


def _require_private_stream_endpoint(value: ControlStreamDescriptor) -> None:
    epoch = value["epoch"]
    endpoint = value["endpoint"]
    if value["platform"] in _WINDOWS_PLATFORMS:
        expected = rf"\\.\pipe\chatgpt-meetings-{epoch}"
        if value["transport"] != "windows-named-pipe" or endpoint != expected:
            raise ControlUnavailable("native control stream endpoint is unsafe")
        return

    if os.name == "nt":
        raise ControlUnavailable("native control platform does not match")

    user_id = os.geteuid()
    parent = _darwin_socket_root() / f"chatgpt-meetings-{user_id}"
    expected = parent / f"{epoch}.sock"
    if value["transport"] != "unix-domain-socket" or endpoint != str(expected):
        raise ControlUnavailable("native control stream endpoint is unsafe")
    try:
        parent_metadata = parent.lstat()
        endpoint_metadata = expected.lstat()
        canonical_parent = parent.resolve(strict=True)
        canonical_endpoint = expected.resolve(strict=True)
    except (OSError, ValueError) as exc:
        raise ControlUnavailable("native control stream endpoint is unavailable") from exc
    if (
        parent.is_symlink()
        or expected.is_symlink()
        or canonical_parent != parent
        or canonical_endpoint != expected
        or not stat.S_ISDIR(parent_metadata.st_mode)
        or parent_metadata.st_uid != user_id
        or stat.S_IMODE(parent_metadata.st_mode) != 0o700
        or not stat.S_ISSOCK(endpoint_metadata.st_mode)
        or endpoint_metadata.st_uid != user_id
        or stat.S_IMODE(endpoint_metadata.st_mode) != 0o600
    ):
        raise ControlUnavailable("native control stream endpoint is unsafe")


def require_stream_lease(
    root: Path,
    descriptor: ControlStreamDescriptor,
) -> None:
    """Revalidate an exact published owner without rehashing its image."""

    import control_client

    descriptor_path = root / _STREAM_DESCRIPTOR_FILENAME
    if control_client.read_json(descriptor_path) != descriptor or (
        control_client.owner_lock_state(root) != "held"
    ):
        raise ControlUnavailable("native control stream owner identity changed")


def require_stream_owner(
    root: Path,
    descriptor: ControlStreamDescriptor,
    *,
    peer_pid: int,
) -> None:
    """Bind the connected peer to the exact leased, live native executable."""

    import control_client

    if type(peer_pid) is not int or peer_pid != descriptor["pid"]:
        raise ControlUnavailable("native control stream owner identity changed")
    require_stream_lease(root, descriptor)

    expected_path = control_client.resolved_path(
        descriptor.get("executablePath"),
        message="native control stream owner executable is unavailable",
    )
    expected_digest = descriptor.get("executableSHA256")
    if not isinstance(expected_digest, str) or _SHA256.fullmatch(expected_digest) is None:
        raise ControlUnavailable("native control stream owner executable is unavailable")

    if descriptor["platform"] in _WINDOWS_PLATFORMS:
        app_path = control_client.resolved_path(
            descriptor.get("bundlePath"),
            message="native control stream owner executable is unavailable",
        )
        control_client.verify_windows_owner_process_image(
            peer_pid,
            expected_path=expected_path,
            app_path=app_path,
            expected_digest=expected_digest,
            digest_reader=control_client.sha256_regular_file,
        )
        expected_start_identity: tuple[int, int] | None = None
    else:
        executable_device = descriptor.get("executableDevice")
        executable_inode = descriptor.get("executableInode")
        if (
            type(executable_device) is not int
            or executable_device <= 0
            or type(executable_inode) is not int
            or executable_inode <= 0
        ):
            raise ControlUnavailable("native control stream owner executable is unavailable")

        from meetings_app.owner_recovery import verified_darwin_owner_process_image

        expected_start_identity = verified_darwin_owner_process_image(
            peer_pid,
            expected_path=expected_path,
            expected_identity=(executable_device, executable_inode),
            expected_digest=expected_digest,
        )

    require_stream_lease(root, descriptor)
    if expected_start_identity is not None:
        from meetings_app.owner_recovery import require_unchanged_darwin_owner_process_birth

        require_unchanged_darwin_owner_process_birth(peer_pid, expected_start_identity)


def discover_transport(
    root: Path,
    *,
    read_descriptor: Callable[[Path], dict[str, object]],
    owner_lock_state: Callable[[Path], str],
    pid_is_proven_dead: Callable[[int], bool],
    expected_app_target: str,
    plugin_version: Callable[[], str | None],
) -> StreamDiscovery:
    """Discover only an authenticated local socket or Windows named pipe."""

    stream_path = root / _STREAM_DESCRIPTOR_FILENAME
    try:
        stream_path.lstat()
    except FileNotFoundError as exc:
        raise ControlUnavailable("native control stream descriptor is unavailable") from exc
    except OSError as exc:
        raise ControlUnavailable("native control stream discovery is unavailable") from exc

    original = read_descriptor(stream_path)
    stream = _require_compatible_stream_owner(
        original,
        expected_app_target=expected_app_target,
        plugin_version=plugin_version,
    )
    _require_private_stream_endpoint(stream)
    if pid_is_proven_dead(stream["pid"]):
        raise ControlUnavailable("native control stream descriptor is stale")
    if owner_lock_state(root) != "held":
        raise ControlUnavailable("native control stream owner lease is unavailable")
    if read_descriptor(stream_path) != original or pid_is_proven_dead(stream["pid"]):
        raise ControlUnavailable("native control stream owner changed during discovery")
    return StreamDiscovery(root, stream)
