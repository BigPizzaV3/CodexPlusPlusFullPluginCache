"""Authenticate a private Windows source copy using the executing release's pins.

The installed cache is a byte transport. Only build-generated constants in the
already executing MCP authorize native bytes; mutable cache JSON never does.
"""

# native_runtime remains the shared, monkeypatchable facade for its split
# implementation modules; the private names below are those existing seams.
# pyright: reportPrivateUsage=false

from __future__ import annotations

import os
import re
import shutil
import stat
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

import native_runtime
from native_runtime_types import (
    NativeArtifactFingerprint,
    NativeRuntimeStatus,
    PlatformRuntimeSpec,
    StableGenerationManifest,
    WindowsRuntimeVerification,
)
from native_runtime_windows_pins import (
    WINDOWS_RUNTIME_PINNED_FILES,
    WINDOWS_RUNTIME_PLUGIN_VERSION,
    WINDOWS_RUNTIME_WINDOWS_BINDING,
)
from windows_private_runtime import WindowsPrivateRuntimeError, fresh_private_directory

from helpers import is_json

MAXIMUM_SOURCE_CLEANUP_ROOTS = 8
MAXIMUM_SOURCE_CLEANUP_ENTRIES = 8192
MAXIMUM_SOURCE_CLEANUP_DEPTH = 32
MAXIMUM_SOURCE_CLEANUP_BYTES = 512 * 1024 * 1024


def _private_source_tree(root: Path) -> tuple[int, int]:
    """Validate an entire bounded scratch tree before deleting any of it."""
    native_runtime._private_runtime_directory(root, create=False)
    identity = root.lstat()
    pending = [(root, 0)]
    entries = 0
    size = 0
    while pending:
        path, depth = pending.pop()
        metadata = path.lstat()
        entries += 1
        if (
            entries > MAXIMUM_SOURCE_CLEANUP_ENTRIES
            or depth > MAXIMUM_SOURCE_CLEANUP_DEPTH
            or stat.S_ISLNK(metadata.st_mode)
            or getattr(metadata, "st_file_attributes", 0) & 0x400
            or not (stat.S_ISDIR(metadata.st_mode) or stat.S_ISREG(metadata.st_mode))
            or (stat.S_ISREG(metadata.st_mode) and metadata.st_nlink != 1)
        ):
            raise native_runtime.NativeRuntimeError("private Windows source tree is unsafe")
        native_runtime._require_windows_private_runtime_acl(path)
        if stat.S_ISDIR(metadata.st_mode):
            with os.scandir(path) as children:
                for child in children:
                    if entries + len(pending) >= MAXIMUM_SOURCE_CLEANUP_ENTRIES:
                        raise native_runtime.NativeRuntimeError(
                            "private Windows source is too large"
                        )
                    pending.append((Path(child.path), depth + 1))
        else:
            size += metadata.st_size
            if size > MAXIMUM_SOURCE_CLEANUP_BYTES:
                raise native_runtime.NativeRuntimeError("private Windows source is too large")
    return identity.st_dev, identity.st_ino


def cleanup_abandoned_sources(runtime_root: Path, revalidate_lock: Callable[[], None]) -> None:
    """Reclaim crash residue once, before a family-lock holder opens any snapshot.

    Snapshot contexts can nest during activation, so neither snapshot entry nor
    generation cleanup may perform this sweep. The family lock proves liveness;
    current-user trust and private ancestry protect the inspected deletion graph.
    """
    if not enabled():
        return

    def failed() -> None:
        native_runtime.log_native_runtime_event("cleanup", "failed", error_kind="source")

    try:
        if native_runtime.stable_runtime_root(create=False) != runtime_root:
            raise native_runtime.NativeRuntimeError("private Windows source root changed")
        root_metadata = runtime_root.lstat()
        root_identity = root_metadata.st_dev, root_metadata.st_ino
        candidates: list[Path] = []
        with os.scandir(runtime_root) as entries:
            for index, entry in enumerate(entries):
                if index >= 256 or len(candidates) >= MAXIMUM_SOURCE_CLEANUP_ROOTS:
                    break
                if re.fullmatch(r"source--[a-f0-9]{32}", entry.name) is not None:
                    candidates.append(Path(entry.path))
    except (OSError, RuntimeError):
        failed()
        return

    for candidate in candidates:
        try:
            identity = _private_source_tree(candidate)
            native_runtime._private_runtime_directory(runtime_root, create=False)
            root_metadata = runtime_root.lstat()
            native_runtime._private_runtime_directory(candidate, create=False)
            current = candidate.lstat()
            if (root_metadata.st_dev, root_metadata.st_ino) != root_identity or (
                current.st_dev,
                current.st_ino,
            ) != identity:
                raise native_runtime.NativeRuntimeError("private Windows source changed")
        except (OSError, RuntimeError):
            failed()
            continue
        # A replaced lock is an authorization failure, not a cleanup warning.
        revalidate_lock()
        try:
            shutil.rmtree(candidate)
        except OSError:
            failed()


def enabled() -> bool:
    return (
        native_runtime._is_windows_host()
        and native_runtime.RUNTIME_CONFIG.flavor == "production"
        and WINDOWS_RUNTIME_PLUGIN_VERSION is not None
        and bool(WINDOWS_RUNTIME_PINNED_FILES)
    )


def uses_pinned_source(plugin_root: Path) -> bool:
    """Use executing-code pins only for that code's own source directory.

    Snapshot still requires the sealed version and exact bytes. A failed own-
    source proof must not fall back to ordinary metadata verification. Distinct
    successors retain the ordinary private-ACL and provenance verifier instead.
    """

    return enabled() and plugin_root.resolve(strict=False) == native_runtime.PLUGIN_ROOT.resolve(
        strict=False
    )


def allows_running_source(plugin_root: Path, family_root: Path) -> bool:
    """Admit the host-launched sealed release when old caches lack a pointer.

    Directory age is only a conservative stale-process fence. It never supplies
    an expected native digest or admits bytes from another version.
    """

    if (
        not enabled()
        or plugin_root.name != WINDOWS_RUNTIME_PLUGIN_VERSION
        or plugin_root != native_runtime.PLUGIN_ROOT.resolve(strict=True)
        or family_root.name != native_runtime.RUNTIME_CONFIG.server_name
        or family_root.parent.name not in native_runtime.OFFICIAL_CACHE_PUBLISHERS
        or native_runtime.plugin_cache_family_root(plugin_root) != family_root
    ):
        return False
    from native_runtime_stable import _official_cache_directory_creation_ns

    selected = plugin_root.lstat()
    if plugin_root.is_symlink() or getattr(selected, "st_file_attributes", 0) & 0x400:
        return False
    if (plugin_root / ".installing").exists():
        return False
    selected_created = _official_cache_directory_creation_ns(selected)
    for candidate in family_root.iterdir():
        if candidate == plugin_root:
            continue
        if native_runtime.GITHUB_RELEASE_COMPONENT.fullmatch(candidate.name) is None:
            continue
        metadata = candidate.lstat()
        if (
            candidate.is_symlink()
            or not stat.S_ISDIR(metadata.st_mode)
            or getattr(metadata, "st_file_attributes", 0) & 0x400
            or candidate.resolve(strict=True).parent != family_root
            or _official_cache_directory_creation_ns(metadata) >= selected_created
        ):
            return False
    return True


@dataclass(frozen=True)
class WindowsSourceSnapshot:
    artifact: Path
    status: NativeRuntimeStatus
    verification: WindowsRuntimeVerification


def source_fingerprint(plugin_root: Path, spec: PlatformRuntimeSpec) -> NativeArtifactFingerprint:
    files = WINDOWS_RUNTIME_PINNED_FILES.get(spec.platform_key, {})
    return tuple(
        native_runtime._path_identity(plugin_root / relative) for relative in sorted(files)
    )


def _pinned_files(plugin_root: Path, spec: PlatformRuntimeSpec) -> dict[str, tuple[int, str]]:
    if not uses_pinned_source(plugin_root) or plugin_root.name != WINDOWS_RUNTIME_PLUGIN_VERSION:
        raise native_runtime.NativeRuntimeError("Windows recovery release identity is unavailable")
    pins = WINDOWS_RUNTIME_PINNED_FILES.get(spec.platform_key)
    if not pins or len(pins) > 8192:
        raise native_runtime.NativeRuntimeError("Windows recovery inventory is unavailable")
    for relative, (size, digest) in pins.items():
        parts = PurePosixPath(relative).parts
        if (
            not parts
            or parts[0] != "native"
            or ".." in parts
            or "\\" in relative
            or ":" in relative
            or relative != PurePosixPath(relative).as_posix()
            or not 0 < size <= native_runtime.MAXIMUM_ARCHIVE_BYTES
            or native_runtime.SHA256_HEX_PATTERN.fullmatch(digest) is None
            or any(parent.as_posix() in pins for parent in PurePosixPath(relative).parents)
        ):
            raise native_runtime.NativeRuntimeError("Windows recovery inventory is malformed")
    if not all(
        relative in pins
        for relative in (
            native_runtime.WINDOWS_PRODUCTION_BUNDLE_RELATIVE_PATH.as_posix(),
            native_runtime.WINDOWS_PRODUCTION_LOCK_RELATIVE_PATH.as_posix(),
            f"native/{spec.platform_key}/{spec.artifact_name}",
        )
    ):
        raise native_runtime.NativeRuntimeError("Windows recovery inventory is incomplete")
    return pins


def pinned_generation(plugin_root: Path, spec: PlatformRuntimeSpec) -> str:
    """Compare desired code identity without re-verifying an unused cache copy.

    The executing release's pins define the generation, including license files.
    This is only an update hint: reusing a current generation still requires its
    independent artifact and owner proofs. Every launch or changed generation
    retains snapshot's complete byte verification, even if the cache is damaged.
    """

    pins = _pinned_files(plugin_root, spec)
    executable_digest = pins[f"native/{spec.platform_key}/{spec.artifact_name}"][1]
    license_prefix = f"native/{spec.platform_key}/THIRD_PARTY_LICENSES/"
    entries: set[tuple[str, str, str]] = set()
    for relative, (_, digest) in pins.items():
        if relative.startswith(license_prefix):
            license_path = PurePosixPath(relative[len(license_prefix) :])
            entries.add((license_path.as_posix(), "file", digest))
            for parent in license_path.parents:
                if parent != PurePosixPath("."):
                    entries.add((parent.as_posix(), "directory", ""))
    licenses_digest = (
        native_runtime.hashlib.sha256(
            native_runtime.json.dumps(
                sorted(entries), ensure_ascii=True, separators=(",", ":")
            ).encode("utf-8")
        ).hexdigest()
        if entries
        else None
    )
    return native_runtime._stable_generation_name(
        spec, native_runtime._windows_generation_sha256(executable_digest, licenses_digest)
    )


def require_matching_manifest(
    source: WindowsSourceSnapshot, expected: StableGenerationManifest, spec: PlatformRuntimeSpec
) -> None:
    digest = source.status.get("_executableSHA256")
    if not isinstance(digest, str):
        raise native_runtime.NativeRuntimeError("Windows source identity is unavailable")
    generation_digest = native_runtime._windows_generation_sha256(
        digest, source.verification.get("thirdPartyLicensesSha256")
    )
    if (
        expected["generation"] != native_runtime._stable_generation_name(spec, generation_digest)
        or expected["executableSha256"] != digest
        or expected["version"] != source.status.get("version")
        or expected["buildTimestamp"] != source.status.get("buildTimestamp")
        or expected["verification"] != source.verification
    ):
        raise native_runtime.NativeRuntimeError("Windows source changed before activation")


def _copy_file(source: Path, destination: Path, size: int, digest: str | None) -> None:
    """Bound the read and authenticate the new file, never the source's ACL."""

    before = source.lstat()
    if (
        not stat.S_ISREG(before.st_mode)
        or before.st_size != size
        or before.st_size <= 0
        or source.is_symlink()
        or getattr(before, "st_file_attributes", 0) & 0x400
    ):
        raise native_runtime.NativeRuntimeError("pinned Windows source file is unsafe")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with source.open("rb") as incoming, destination.open("xb") as outgoing:
        opened = os.fstat(incoming.fileno())
        if not stat.S_ISREG(opened.st_mode):
            raise native_runtime.NativeRuntimeError("pinned Windows source is not a regular file")
        remaining = size
        while remaining:
            chunk = incoming.read(min(remaining, 1024 * 1024))
            if not chunk:
                raise native_runtime.NativeRuntimeError("pinned Windows source is incomplete")
            outgoing.write(chunk)
            remaining -= len(chunk)
        if incoming.read(1):
            raise native_runtime.NativeRuntimeError("pinned Windows source changed size")
        outgoing.flush()
        os.fsync(outgoing.fileno())
    if digest is not None and native_runtime.sha256_regular_file(destination) != digest:
        raise native_runtime.NativeRuntimeError(
            "Windows source does not match the executing release"
        )


@contextmanager
def snapshot(
    plugin_root: Path, runtime_root: Path, spec: PlatformRuntimeSpec
) -> Iterator[WindowsSourceSnapshot]:
    """Copy sealed native inputs while the caller holds the runtime family lock."""

    pins = _pinned_files(plugin_root, spec)
    family = native_runtime.plugin_cache_family_root(plugin_root)
    if (
        family is None
        or family.name != native_runtime.RUNTIME_CONFIG.server_name
        or family.parent.name not in native_runtime.OFFICIAL_CACHE_PUBLISHERS
    ):
        raise native_runtime.NativeRuntimeError(
            "Windows recovery requires the official plugin cache"
        )
    native_runtime.require_canonical_plugin_registration(plugin_root, family)
    owned_root: Path | None = None
    try:
        with fresh_private_directory(runtime_root, "source-") as private_root:
            owned_root = private_root
            for relative, (size, digest) in pins.items():
                _copy_file(plugin_root / relative, private_root / relative, size, digest)

            # This composite also binds the MCP archive, so its complete hash
            # cannot be embedded in that archive. Its Windows subtree must equal
            # the independently pinned build value before it is used as evidence.
            composite = native_runtime.VERIFIED_CAM_DISTRIBUTION_RELATIVE_PATH
            composite_size = (plugin_root / composite).stat().st_size
            if not 0 < composite_size <= native_runtime.MAXIMUM_MANIFEST_BYTES:
                raise native_runtime.NativeRuntimeError("Windows distribution is too large")
            _copy_file(plugin_root / composite, private_root / composite, composite_size, None)
            decoded = native_runtime._read_strict_local_json(
                private_root / composite,
                maximum_bytes=native_runtime.MAXIMUM_MANIFEST_BYTES,
                label="private Windows distribution",
            )
            sources = decoded.get("sources")
            if (
                decoded.get("schemaVersion") != 2
                or decoded.get("kind") != "chatgpt-meetings-verified-composite-distribution"
                or not is_json(sources)
                or sources.get("windows") != WINDOWS_RUNTIME_WINDOWS_BINDING
            ):
                raise native_runtime.NativeRuntimeError(
                    "Windows distribution does not match release"
                )
            relative_executable = f"native/{spec.platform_key}/{spec.artifact_name}"
            executable_pin = pins.get(relative_executable)
            if executable_pin is None:
                raise native_runtime.NativeRuntimeError("Windows executable pin is unavailable")
            artifact = private_root / spec.artifact_name
            _copy_file(private_root / relative_executable, artifact, *executable_pin)
            license_prefix = f"native/{spec.platform_key}/THIRD_PARTY_LICENSES/"
            for relative, pin in pins.items():
                if relative.startswith(license_prefix):
                    _copy_file(
                        private_root / relative,
                        private_root / "THIRD_PARTY_LICENSES" / relative[len(license_prefix) :],
                        *pin,
                    )
            # Explicit internal call: a private authenticated snapshot is not a
            # second official plugin registration and must not enter that lookup.
            verification = native_runtime._windows_production_verification_manifest(artifact, spec)
            licenses = native_runtime._windows_source_licenses_sha256(artifact, spec)
            if licenses is not None:
                verification["thirdPartyLicensesSha256"] = licenses
            # Generation metadata must agree with ordinary source verification.
            # Policy releaseVersion is projected separately from the verified distribution.
            fingerprint, version, timestamp = native_runtime._plugin_bundle_fingerprint(
                artifact, spec
            )
            distribution = verification.get("windowsDistribution")
            if distribution is None:
                raise native_runtime.NativeRuntimeError("Windows release binding is unavailable")
            status: NativeRuntimeStatus = {
                "installed": True,
                "version": version,
                "buildTimestamp": timestamp,
                "appPath": str(artifact),
                "artifactPath": str(artifact),
                "platform": spec.platform_key,
                "artifactKind": spec.artifact_kind,
                "artifactPathKind": spec.artifact_path_kind,
                "capabilities": [],
                "source": "plugin-bundled",
                "_artifactFingerprint": fingerprint,
                "_executableSHA256": executable_pin[1],
            }
            yield WindowsSourceSnapshot(artifact, status, verification)
    except (OSError, WindowsPrivateRuntimeError) as exc:
        raise native_runtime.NativeRuntimeError("private Windows source is unavailable") from exc
    finally:
        # Close directory pins before removing this operation's private scratch
        # copy. Installed cache, stable generations and user data are untouched.
        if owned_root is not None:
            try:
                shutil.rmtree(owned_root)
            except OSError as exc:
                raise native_runtime.NativeRuntimeError(
                    "private Windows source cleanup is incomplete"
                ) from exc
