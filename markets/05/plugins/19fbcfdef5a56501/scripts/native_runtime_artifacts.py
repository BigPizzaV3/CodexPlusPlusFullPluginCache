from __future__ import annotations

import os
from collections.abc import Mapping
from pathlib import Path
from typing import Final, Iterator

import native_runtime
from companion_control_v2 import KNOWN_CAPABILITIES as COMPANION_CAPABILITIES
from companion_control_v2 import METHOD_CONTRACTS
from native_runtime_types import (
    AuthenticodeSigningPolicy,
    NativeArtifactFingerprint,
    NativePathIdentity,
    PlatformRuntimeSpec,
    UnsignedTestSigningPolicy,
    WindowsDistributionArtifact,
    WindowsDistributionBinding,
    WindowsDistributionRelease,
    WindowsDistributionStorage,
    WindowsRuntimeVerification,
    WindowsSigningPolicy,
)
from recording_control_action_contract import is_safe_control_wire_capability

from helpers import is_json, parse_bounded_json

# Current release metadata requires v2 state and update support. Artifact
# profiles do not grant live capabilities, which are negotiated per owner.
_WINDOWS_RELEASE_REQUIRED_CAPABILITIES: Final[frozenset[str]] = frozenset(
    capability
    for method in ("companion.getState", "lifecycle.quitForUpdate")
    for capability in METHOD_CONTRACTS[method]["requiredCapabilities"]
)


def _path_identity(path: Path) -> NativePathIdentity:
    """Return a cheap identity that changes on replacement or normal edits."""

    try:
        value = path.stat()
    except OSError as exc:
        raise native_runtime.NativeRuntimeError("native app identity is unavailable") from exc
    return (
        str(path),
        value.st_dev,
        value.st_ino,
        native_runtime.stat.S_IFMT(value.st_mode),
        value.st_size,
        value.st_mtime_ns,
        value.st_ctime_ns,
    )


def _optional_path_identity(path: Path) -> NativePathIdentity:
    """Track an optional signature path without making unsigned test apps fail."""

    try:
        return native_runtime._path_identity(path)
    except native_runtime.NativeRuntimeError:
        return (str(path), "missing")


def _native_build_receipt_path(app_path: Path) -> Path:
    """Select exactly one safe current or released macOS build receipt."""

    resources = app_path / "Contents" / "Resources"
    matches: list[Path] = []
    for name in native_runtime.NATIVE_BUILD_RECEIPT_NAMES:
        candidate = resources / name
        try:
            metadata = candidate.lstat()
        except FileNotFoundError:
            continue
        except OSError as exc:
            raise native_runtime.NativeRuntimeError(
                "native app build receipt is unavailable"
            ) from exc
        if not native_runtime.stat.S_ISREG(metadata.st_mode):
            raise native_runtime.NativeRuntimeError("native app build receipt is unsafe")
        matches.append(candidate)
    if len(matches) > 1:
        raise native_runtime.NativeRuntimeError("native app build receipt is ambiguous")
    if not matches:
        raise native_runtime.NativeRuntimeError("native app build receipt is unavailable")
    return matches[0]


def _framework_entry_identity(path: Path) -> NativePathIdentity:
    """Fingerprint a framework entry without following a replaced symlink."""

    try:
        value = path.lstat()
        link_target = (
            native_runtime.os.readlink(path) if native_runtime.stat.S_ISLNK(value.st_mode) else None
        )
    except OSError as exc:
        raise native_runtime.NativeRuntimeError("native framework identity is unavailable") from exc
    return (
        str(path),
        value.st_dev,
        value.st_ino,
        native_runtime.stat.S_IFMT(value.st_mode),
        value.st_size,
        value.st_mtime_ns,
        value.st_ctime_ns,
        link_target,
    )


def _plugin_directory_identities(
    directory: Path,
    *,
    kind: str,
    maximum_entries: int,
    allow_missing: bool = False,
) -> NativeArtifactFingerprint:
    """Fingerprint a bounded artifact directory without following symlinks."""

    try:
        root_metadata = directory.lstat()
    except FileNotFoundError as exc:
        if allow_missing:
            return ((str(directory), "missing"),)
        raise native_runtime.NativeRuntimeError(f"native {kind} identity is unavailable") from exc
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(f"native {kind} identity is unavailable") from exc
    if not native_runtime.stat.S_ISDIR(root_metadata.st_mode):
        raise native_runtime.NativeRuntimeError(f"native {kind} directory is unsafe")

    identities = [native_runtime._framework_entry_identity(directory)]
    pending = [directory]
    while pending:
        current = pending.pop()
        try:
            entries = sorted(current.iterdir(), key=lambda path: path.name)
        except OSError as exc:
            raise native_runtime.NativeRuntimeError(
                f"native {kind} identity is unavailable"
            ) from exc
        for entry in entries:
            identity = native_runtime._framework_entry_identity(entry)
            identities.append(identity)
            if len(identities) > maximum_entries:
                raise native_runtime.NativeRuntimeError(f"native {kind} directory is too large")
            if identity[3] == native_runtime.stat.S_IFDIR:
                pending.append(entry)
    return tuple(identities)


def _plugin_framework_identities(contents: Path) -> NativeArtifactFingerprint:
    """Track nested signed code so a cache copy cannot reuse a stale proof."""

    return _plugin_directory_identities(
        contents / "Frameworks",
        kind="framework",
        maximum_entries=native_runtime.MAXIMUM_PLUGIN_FRAMEWORK_ENTRIES,
        allow_missing=True,
    )


def _plugin_resource_identities(contents: Path) -> NativeArtifactFingerprint:
    """Bind every sealed resource without following an atomically swapped link."""

    return _plugin_directory_identities(
        contents / "Resources",
        kind="resource",
        maximum_entries=native_runtime.MAXIMUM_PLUGIN_RESOURCE_ENTRIES,
    )


@native_runtime.contextmanager
def _plugin_bundle_cross_process_lock(
    app_path: Path,
    spec: PlatformRuntimeSpec,
) -> Iterator[None]:
    """Serialize symlink repair and verification without mutating the plugin.

    The signed bundle's Info.plist is immutable and shared by every process
    using one versioned cache image, so flocking its read-only descriptor gives
    us a cross-process lock without adding state to the sealed payload.
    """

    if native_runtime._is_windows_spec(spec) or native_runtime.fcntl is None:
        yield
        return
    lock_path = app_path / "Contents" / "Info.plist"
    flags = native_runtime.os.O_RDONLY
    if hasattr(native_runtime.os, "O_NOFOLLOW"):
        flags |= native_runtime.os.O_NOFOLLOW
    descriptor = -1
    locked = False
    deadline = (
        native_runtime.time.monotonic()
        + native_runtime.PLUGIN_BUNDLE_CROSS_PROCESS_LOCK_TIMEOUT_SECONDS
    )
    try:
        descriptor = native_runtime.os.open(lock_path, flags)
        metadata = native_runtime.os.fstat(descriptor)
        if not native_runtime.stat.S_ISREG(metadata.st_mode):
            raise native_runtime.NativeRuntimeError("native launch lock is unsafe")
        while True:
            try:
                native_runtime.fcntl.flock(
                    descriptor,
                    native_runtime.fcntl.LOCK_EX | native_runtime.fcntl.LOCK_NB,
                )
                locked = True
                break
            except BlockingIOError as lock_error:
                if native_runtime.time.monotonic() >= deadline:
                    raise native_runtime.NativeRuntimeLockBusy(
                        "native launch lock timed out"
                    ) from lock_error
                native_runtime.time.sleep(0.01)
        yield
    except native_runtime.NativeRuntimeError:
        raise
    except OSError as exc:
        raise native_runtime.NativeRuntimeError("native launch lock is unavailable") from exc
    finally:
        if descriptor >= 0:
            if locked:
                try:
                    native_runtime.fcntl.flock(descriptor, native_runtime.fcntl.LOCK_UN)
                except OSError:
                    pass
            native_runtime.os.close(descriptor)


def restore_plugin_framework_symlinks(app_path: native_runtime.Path) -> bool:
    """Restore only exact, build-declared Sentry framework symlinks.

    Internal Distribution deliberately materializes a symlink-free payload.
    The immutable runtime contract names the only links that may be restored;
    scanning an arbitrary framework layout must never expand this authority.
    A full deep signature check still follows before launch.
    """

    frameworks = app_path / "Contents" / "Frameworks"
    try:
        frameworks_metadata = frameworks.lstat()
    except FileNotFoundError:
        return False
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "native framework directory is unavailable"
        ) from exc
    if not native_runtime.stat.S_ISDIR(frameworks_metadata.st_mode):
        raise native_runtime.NativeRuntimeError("native framework directory is unsafe")

    sentry_root = frameworks / "Sentry.framework"
    try:
        sentry_metadata = sentry_root.lstat()
    except FileNotFoundError:
        return False
    except OSError as exc:
        raise native_runtime.NativeRuntimeError("native Sentry framework is unavailable") from exc
    if not native_runtime.stat.S_ISDIR(sentry_metadata.st_mode):
        raise native_runtime.NativeRuntimeError("native Sentry framework is unsafe")

    restored = False
    for relative_path, target in native_runtime.PLUGIN_FRAMEWORK_SYMLINKS:
        link = app_path / relative_path
        expected_target = native_runtime.Path(
            native_runtime.os.path.normpath(str(link.parent / target))
        )
        try:
            expected_target.relative_to(sentry_root)
        except ValueError as exc:
            raise native_runtime.NativeRuntimeError(
                "native framework link contract is unsafe"
            ) from exc
        try:
            link_metadata = link.lstat()
        except FileNotFoundError:
            link_metadata = None
        except OSError as exc:
            raise native_runtime.NativeRuntimeError("native framework link is unavailable") from exc
        if link_metadata is not None:
            if (
                not native_runtime.stat.S_ISLNK(link_metadata.st_mode)
                or native_runtime.os.readlink(link) != target
            ):
                raise native_runtime.NativeRuntimeError(
                    "native framework link does not match contract"
                )
            continue
        try:
            target_metadata = expected_target.lstat()
        except OSError as exc:
            raise native_runtime.NativeRuntimeError(
                "native framework link target is unavailable"
            ) from exc
        if native_runtime.stat.S_ISLNK(target_metadata.st_mode):
            raise native_runtime.NativeRuntimeError("native framework link target is unsafe")
        try:
            native_runtime.os.symlink(target, link)
        except FileExistsError as exc:
            raise native_runtime.NativeRuntimeError(
                "native framework link changed during restore"
            ) from exc
        except OSError as exc:
            raise native_runtime.NativeRuntimeError(
                "native framework link could not be restored"
            ) from exc
        restored = True
    return restored


def _verified_cam_distribution_manifest(
    plugin_root: Path,
    artifact_path: Path,
    *,
    include_native_identity: bool = False,
) -> dict[str, str]:
    """Bind a production cache image to OpenAI's verified Cam descriptor."""

    if native_runtime.RUNTIME_CONFIG.flavor != "production":
        return {}
    descriptor_path = plugin_root / native_runtime.VERIFIED_CAM_DISTRIBUTION_RELATIVE_PATH
    try:
        resolved_root = plugin_root.resolve(strict=True)
        resolved_descriptor = descriptor_path.resolve(strict=True)
        metadata = descriptor_path.lstat()
    except OSError as exc:
        raise native_runtime.NativeRuntimeError("verified Cam distribution is unavailable") from exc
    if (
        descriptor_path.is_symlink()
        or resolved_descriptor.parent != resolved_root / "native"
        or not native_runtime.stat.S_ISREG(metadata.st_mode)
        or metadata.st_size <= 0
        or metadata.st_size > native_runtime.MAXIMUM_MANIFEST_BYTES
        or (not native_runtime._is_windows_host() and metadata.st_mode & 0o022)
    ):
        raise native_runtime.NativeRuntimeError("verified Cam distribution is unsafe")

    descriptor_fd = -1
    try:
        descriptor_fd = native_runtime.os.open(
            resolved_descriptor,
            native_runtime.os.O_RDONLY
            | getattr(native_runtime.os, "O_BINARY", 0)
            | getattr(native_runtime.os, "O_CLOEXEC", 0)
            | getattr(native_runtime.os, "O_NOFOLLOW", 0),
        )
        opened = native_runtime.os.fstat(descriptor_fd)
        current = descriptor_path.lstat()
        if (
            not native_runtime.stat.S_ISREG(opened.st_mode)
            or not native_runtime.stat.S_ISREG(current.st_mode)
            or descriptor_path.is_symlink()
            or (opened.st_dev, opened.st_ino) != (metadata.st_dev, metadata.st_ino)
            or (current.st_dev, current.st_ino) != (metadata.st_dev, metadata.st_ino)
            or opened.st_size != metadata.st_size
        ):
            raise native_runtime.NativeRuntimeError(
                "verified Cam distribution changed while reading"
            )
        raw = native_runtime.os.read(descriptor_fd, native_runtime.MAXIMUM_MANIFEST_BYTES + 1)
        final = native_runtime.os.fstat(descriptor_fd)
        if (
            len(raw) != metadata.st_size
            or final.st_size != metadata.st_size
            or final.st_mtime_ns != opened.st_mtime_ns
            or final.st_ctime_ns != opened.st_ctime_ns
        ):
            raise native_runtime.NativeRuntimeError(
                "verified Cam distribution changed while reading"
            )
        descriptor = parse_bounded_json(raw.decode("utf-8"))
    except native_runtime.NativeRuntimeError:
        raise
    except (
        OSError,
        UnicodeDecodeError,
        ValueError,
        RecursionError,
        native_runtime.json.JSONDecodeError,
    ) as exc:
        raise native_runtime.NativeRuntimeError("verified Cam distribution is malformed") from exc
    finally:
        if descriptor_fd >= 0:
            native_runtime.os.close(descriptor_fd)
    descriptor_object = descriptor if is_json(descriptor) else {}
    native = descriptor_object.get("native")
    runtime = descriptor_object.get("runtime")
    descriptor_pair = (
        descriptor_object.get("schemaVersion"),
        descriptor_object.get("kind"),
    )
    valid_descriptor_pairs = {
        (1, "chatgpt-meetings-verified-cam-distribution"),
        (2, "chatgpt-meetings-verified-composite-distribution"),
    }
    expected_links = [
        {"path": path, "target": target}
        for path, target in native_runtime.PLUGIN_FRAMEWORK_SYMLINKS
    ]
    if (
        descriptor_pair not in valid_descriptor_pairs
        or not isinstance(native, dict)
        or native.get("bundleName") != native_runtime.APP_NAME
        or native.get("appName") != native_runtime.APP_NAME
        or native.get("bundleIdentifier") != native_runtime.BUNDLE_ID
        or native.get("teamIdentifier") != native_runtime.TEAM_IDENTIFIER
        or native.get("frameworkSymlinks") != expected_links
        or native.get("pluginRelativePath") != native_runtime.APP_NAME
        or not isinstance(runtime, dict)
        or runtime.get("profile") != "production"
        or runtime.get("serverName") != native_runtime.RUNTIME_CONFIG.server_name
        or runtime.get("controlTarget") != native_runtime.RUNTIME_CONFIG.control_target
        or runtime.get("pluginRelativePath") != "scripts"
    ):
        raise native_runtime.NativeRuntimeError("verified Cam distribution does not match runtime")
    team_identifier = native_runtime.TEAM_IDENTIFIER
    try:
        expected_artifact = (resolved_root / native["pluginRelativePath"]).resolve(strict=True)
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "verified Cam native artifact is unavailable"
        ) from exc
    if expected_artifact != artifact_path.resolve(strict=True):
        raise native_runtime.NativeRuntimeError("verified Cam native artifact path does not match")
    receipt_path = native_runtime._native_build_receipt_path(expected_artifact)
    expected_receipt_sha256 = native.get("embeddedReceiptSha256")
    if (
        not isinstance(expected_receipt_sha256, str)
        or native_runtime.SHA256_HEX_PATTERN.fullmatch(expected_receipt_sha256) is None
    ):
        raise native_runtime.NativeRuntimeError("verified Cam native receipt is unavailable")
    try:
        receipt_metadata = receipt_path.lstat()
        resolved_receipt = receipt_path.resolve(strict=True)
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "verified Cam native receipt is unavailable"
        ) from exc
    if (
        receipt_path.is_symlink()
        or resolved_receipt != receipt_path
        or not native_runtime.stat.S_ISREG(receipt_metadata.st_mode)
        or native_runtime.sha256_regular_file(receipt_path) != expected_receipt_sha256
    ):
        raise native_runtime.NativeRuntimeError("verified Cam native receipt does not match")
    verification = {"teamIdentifier": team_identifier}
    if include_native_identity:
        artifact_sha256 = native.get("sha256")
        if (
            not isinstance(artifact_sha256, str)
            or native_runtime.SHA256_HEX_PATTERN.fullmatch(artifact_sha256) is None
        ):
            raise native_runtime.NativeRuntimeError(
                "verified Cam native artifact identity is unavailable"
            )
        verification.update(
            {
                "artifactSha256": artifact_sha256,
                "embeddedReceiptSha256": expected_receipt_sha256,
            }
        )
    return verification


def _plugin_bundle_fingerprint(
    app_path: Path,
    spec: PlatformRuntimeSpec,
) -> tuple[NativeArtifactFingerprint, str, str | None]:
    """Return mutation identity for verification memoization."""

    if native_runtime._is_windows_spec(spec):
        executable = native_runtime._load_windows_executable(app_path, spec)
        signing_identity = (
            native_runtime._optional_path_identity(
                executable.parent / native_runtime.WINDOWS_PRODUCTION_BUNDLE_RELATIVE_PATH
            )
            if native_runtime.uses_production_windows_bundle(executable)
            else native_runtime._optional_path_identity(
                native_runtime._windows_plugin_runtime_descriptor_path(executable)
            )
        )
        return (
            (
                native_runtime._path_identity(executable),
                signing_identity,
            ),
            "plugin-bundled",
            None,
        )

    info, executable, helper = native_runtime._load_app_metadata(app_path, spec)
    contents = app_path / "Contents"
    identities = tuple(
        native_runtime._path_identity(path)
        for path in (
            app_path,
            contents,
            contents / "Info.plist",
            contents / "MacOS",
            executable,
            contents / "Resources",
            contents / "Resources" / "native",
            helper,
        )
    )
    identities += tuple(
        native_runtime._optional_path_identity(contents / "Resources" / name)
        for name in native_runtime.NATIVE_BUILD_RECEIPT_NAMES
    )
    signature_root = contents / "_CodeSignature"
    identities += (
        native_runtime._optional_path_identity(signature_root),
        native_runtime._optional_path_identity(signature_root / "CodeResources"),
    )
    identities += native_runtime._plugin_framework_identities(contents)
    identities += native_runtime._plugin_resource_identities(contents)
    return (
        identities,
        native_runtime._plugin_bundle_version(info, app_path),
        native_runtime._build_timestamp_from_info(info),
    )


def _stable_artifact_status_sentinel(
    artifact_path: Path,
    spec: PlatformRuntimeSpec,
) -> NativeArtifactFingerprint:
    """Return an O(1) identity for one already-verified immutable generation."""

    manifest = artifact_path.parent / ".runtime.json"
    if native_runtime._is_windows_spec(spec):
        return (
            native_runtime._path_identity(artifact_path),
            native_runtime._path_identity(manifest),
        )
    _info, executable, helper = native_runtime._load_app_metadata(artifact_path, spec)
    contents = artifact_path / "Contents"
    identities = tuple(
        native_runtime._path_identity(path)
        for path in (
            artifact_path,
            contents,
            contents / "Info.plist",
            executable,
            helper,
            native_runtime._native_build_receipt_path(artifact_path),
            manifest,
        )
    )
    return identities + (
        native_runtime._optional_path_identity(contents / "_CodeSignature" / "CodeResources"),
    )


def _require_windows_artifact_acl(path: Path) -> None:
    """Public installation files may be readable, but never writable by other users."""

    if not native_runtime._is_windows_host():
        return
    from control_client import windows_acl_is_private

    if not windows_acl_is_private(path, allow_untrusted_read=True):
        raise native_runtime.NativeRuntimeError("native artifact permissions are unsafe")


def _regular_file_identity_timestamp_matches(
    descriptor_metadata: os.stat_result,
    path_metadata: os.stat_result,
) -> bool:
    """Compare the timestamp represented consistently by both stat APIs."""

    if native_runtime._is_windows_host():
        descriptor_birthtime = getattr(descriptor_metadata, "st_birthtime_ns", None)
        path_birthtime = getattr(path_metadata, "st_birthtime_ns", None)
        if descriptor_birthtime is not None or path_birthtime is not None:
            return (
                descriptor_birthtime is not None
                and path_birthtime is not None
                and descriptor_birthtime == path_birthtime
            )
    return descriptor_metadata.st_ctime_ns == path_metadata.st_ctime_ns


def sha256_regular_file(path: Path) -> str:
    """Hash one exact regular file without following a substituted symlink."""

    flags = (
        native_runtime.os.O_RDONLY
        | getattr(native_runtime.os, "O_BINARY", 0)
        | getattr(native_runtime.os, "O_CLOEXEC", 0)
        | getattr(native_runtime.os, "O_NOFOLLOW", 0)
    )
    descriptor = -1
    try:
        path_metadata = path.lstat()
        reparse_point = getattr(native_runtime.stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
        if (
            path.is_symlink()
            or not native_runtime.stat.S_ISREG(path_metadata.st_mode)
            or (reparse_point and getattr(path_metadata, "st_file_attributes", 0) & reparse_point)
        ):
            raise native_runtime.NativeRuntimeError("native executable identity is unavailable")
        descriptor = native_runtime.os.open(path, flags)
        metadata = native_runtime.os.fstat(descriptor)
        if (
            not native_runtime.stat.S_ISREG(metadata.st_mode)
            or metadata.st_size <= 0
            or metadata.st_size > native_runtime.MAXIMUM_ARCHIVE_BYTES
            or (metadata.st_dev, metadata.st_ino) != (path_metadata.st_dev, path_metadata.st_ino)
            or metadata.st_size != path_metadata.st_size
            or metadata.st_mtime_ns != path_metadata.st_mtime_ns
            or not native_runtime._regular_file_identity_timestamp_matches(metadata, path_metadata)
        ):
            raise native_runtime.NativeRuntimeError("native executable identity is unavailable")
        digest = native_runtime.hashlib.sha256()
        remaining = metadata.st_size
        while remaining > 0:
            chunk = native_runtime.os.read(descriptor, min(remaining, 1024 * 1024))
            if not chunk:
                break
            digest.update(chunk)
            remaining -= len(chunk)
        final_metadata = native_runtime.os.fstat(descriptor)
        final_path_metadata = path.lstat()
        if (
            remaining != 0
            or path.is_symlink()
            or not native_runtime.stat.S_ISREG(final_path_metadata.st_mode)
            or (
                reparse_point
                and getattr(final_path_metadata, "st_file_attributes", 0) & reparse_point
            )
            or (final_metadata.st_dev, final_metadata.st_ino) != (metadata.st_dev, metadata.st_ino)
            or (final_path_metadata.st_dev, final_path_metadata.st_ino)
            != (metadata.st_dev, metadata.st_ino)
            or final_metadata.st_size != metadata.st_size
            or final_path_metadata.st_size != metadata.st_size
            or final_metadata.st_mtime_ns != metadata.st_mtime_ns
            or final_metadata.st_ctime_ns != metadata.st_ctime_ns
            or final_path_metadata.st_mtime_ns != metadata.st_mtime_ns
            or not native_runtime._regular_file_identity_timestamp_matches(
                metadata, final_path_metadata
            )
        ):
            raise native_runtime.NativeRuntimeError("native executable changed while hashing")
        return digest.hexdigest()
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "native executable identity is unavailable"
        ) from exc
    finally:
        if descriptor >= 0:
            native_runtime.os.close(descriptor)


def _plugin_executable_path(
    artifact_path: Path,
    spec: PlatformRuntimeSpec,
) -> Path:
    """Return the one native executable covered by a verified plugin artifact."""

    if native_runtime._is_windows_spec(spec):
        return native_runtime._load_windows_executable(artifact_path, spec)
    _info, executable, _helper = native_runtime._load_app_metadata(artifact_path, spec)
    return executable


def _plugin_executable_file_identity(
    fingerprint: NativeArtifactFingerprint,
    artifact_path: native_runtime.Path,
    spec: PlatformRuntimeSpec,
) -> tuple[int, int]:
    """Recover the verified executable vnode identity without another stat."""

    try:
        executable_path = native_runtime._plugin_executable_path(artifact_path, spec).resolve(
            strict=True
        )
        matches = [
            entry
            for entry in fingerprint
            if isinstance(entry[0], str)
            and native_runtime.Path(entry[0]).resolve(strict=False) == executable_path
        ]
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "native executable identity is unavailable"
        ) from exc
    if len(matches) != 1:
        raise native_runtime.NativeRuntimeError("native executable identity is unavailable")
    device, inode = matches[0][1:3]
    if type(device) is not int or type(inode) is not int or device <= 0 or inode <= 0:
        raise native_runtime.NativeRuntimeError("native executable identity is unavailable")
    return device, inode


@native_runtime.contextmanager
def _windows_write_delete_launch_guard(
    path: Path,
    *,
    unavailable_message: str,
) -> Iterator[None]:
    """Hold one Windows path readable but not replaceable through launch."""

    if native_runtime.os.name != "nt":
        # Portable tests exercise Windows orchestration with a platform mock;
        # the real sharing contract is covered by windows-latest.
        yield
        return

    from ctypes import wintypes

    generic_read = 0x8000_0000
    file_share_read = 0x0000_0001
    open_existing = 3
    file_attribute_normal = 0x0000_0080
    file_attribute_reparse_point = 0x0000_0400
    file_flag_open_reparse_point = 0x0020_0000

    class ByHandleFileInformation(native_runtime.ctypes.Structure):
        _fields_ = [
            ("attributes", wintypes.DWORD),
            ("created", wintypes.FILETIME),
            ("accessed", wintypes.FILETIME),
            ("written", wintypes.FILETIME),
            ("volume", wintypes.DWORD),
            ("size_high", wintypes.DWORD),
            ("size_low", wintypes.DWORD),
            ("links", wintypes.DWORD),
            ("index_high", wintypes.DWORD),
            ("index_low", wintypes.DWORD),
        ]

    kernel32 = native_runtime._windows_ctypes.WinDLL("kernel32", use_last_error=True)
    kernel32.CreateFileW.argtypes = [
        wintypes.LPCWSTR,
        wintypes.DWORD,
        wintypes.DWORD,
        wintypes.LPVOID,
        wintypes.DWORD,
        wintypes.DWORD,
        wintypes.HANDLE,
    ]
    kernel32.CreateFileW.restype = wintypes.HANDLE
    kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
    kernel32.CloseHandle.restype = wintypes.BOOL
    kernel32.GetFileInformationByHandle.argtypes = [
        wintypes.HANDLE,
        native_runtime.ctypes.POINTER(ByHandleFileInformation),
    ]
    kernel32.GetFileInformationByHandle.restype = wintypes.BOOL
    handle = kernel32.CreateFileW(
        str(path),
        generic_read,
        file_share_read,
        None,
        open_existing,
        file_attribute_normal | file_flag_open_reparse_point,
        None,
    )
    invalid_handle = native_runtime.ctypes.c_void_p(-1).value
    if handle in {None, invalid_handle}:
        raise native_runtime.NativeRuntimeError(unavailable_message)
    try:
        information = ByHandleFileInformation()
        try:
            path_metadata = path.lstat()
        except OSError as exc:
            raise native_runtime.NativeRuntimeError(unavailable_message) from exc
        if not kernel32.GetFileInformationByHandle(
            handle, native_runtime.ctypes.byref(information)
        ):
            raise native_runtime.NativeRuntimeError(unavailable_message)
        handle_inode = (information.index_high << 32) | information.index_low
        handle_size = (information.size_high << 32) | information.size_low
        reparse_point = getattr(native_runtime.stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
        if (
            path.is_symlink()
            or not native_runtime.stat.S_ISREG(path_metadata.st_mode)
            or information.attributes & file_attribute_reparse_point
            or (reparse_point and getattr(path_metadata, "st_file_attributes", 0) & reparse_point)
            or handle_inode != path_metadata.st_ino
            or handle_size != path_metadata.st_size
        ):
            raise native_runtime.NativeRuntimeError(unavailable_message)
        _require_windows_artifact_acl(path)
        yield
    finally:
        kernel32.CloseHandle(handle)


@native_runtime.contextmanager
def _windows_executable_launch_guard(path: Path) -> Iterator[None]:
    """Deny executable write/delete from verification through CreateProcess."""

    with native_runtime._windows_write_delete_launch_guard(
        path,
        unavailable_message=("verified Windows executable could not be locked for launch"),
    ):
        yield


@native_runtime.contextmanager
def _windows_registration_launch_guard(family_root: Path, *, plugin_root: Path) -> Iterator[None]:
    """Deny canonical marketplace activation replacement through CreateProcess."""

    if native_runtime.plugin_cache_family_root(plugin_root) != family_root:
        raise native_runtime.NativeRuntimeError(
            "ChatGPT Meetings plugin registration could not be locked for launch"
        )
    manifest_path = family_root.parent / ".agents" / "plugins" / "marketplace.json"
    try:
        manifest_path.lstat()
    except FileNotFoundError:
        try:
            # Use the same exact-source admission as staging and the final
            # pre-spawn check. Sealed executing releases can retain older cache
            # siblings; selecting a singleton here would reject that repair.
            native_runtime.require_canonical_plugin_registration(plugin_root, family_root)
        except native_runtime.NativeRuntimeError as exc:
            raise native_runtime.NativeRuntimeError(
                "ChatGPT Meetings plugin registration could not be locked for launch"
            ) from exc
        yield
        return
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "ChatGPT Meetings plugin registration could not be locked for launch"
        ) from exc
    with native_runtime._windows_write_delete_launch_guard(
        manifest_path,
        unavailable_message=("ChatGPT Meetings plugin registration could not be locked for launch"),
    ):
        native_runtime.require_canonical_plugin_registration(plugin_root, family_root)
        yield


def _plugin_verification_cache_key(
    app_path: Path,
    spec: PlatformRuntimeSpec,
) -> tuple[str, str, str, bool]:
    return (
        str(app_path),
        spec.platform_key,
        spec.identity_value,
        native_runtime.allow_unsigned_test_app(),
    )


def _windows_plugin_runtime_descriptor_path(artifact_path: Path) -> Path:
    """Return the installer-owned signer handoff beside a Windows EXE."""

    return artifact_path.parent / native_runtime.WINDOWS_PLUGIN_RUNTIME_DESCRIPTOR_RELATIVE_PATH


def _read_strict_local_json(
    path: Path,
    *,
    maximum_bytes: int,
    label: str,
    reject_public_writes: bool = False,
) -> dict[str, object]:
    """Read a bounded local trust manifest through one inode-bound descriptor."""

    descriptor = -1
    try:
        metadata = path.lstat()
        reparse_point = getattr(native_runtime.stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
        if (
            path.is_symlink()
            or not native_runtime.stat.S_ISREG(metadata.st_mode)
            or metadata.st_size <= 0
            or metadata.st_size > maximum_bytes
            or (reparse_point and getattr(metadata, "st_file_attributes", 0) & reparse_point)
            or (
                reject_public_writes
                and not native_runtime._is_windows_host()
                and (metadata.st_uid != native_runtime.os.getuid() or metadata.st_mode & 0o022)
            )
        ):
            raise native_runtime.NativeRuntimeError(f"{label} is unsafe")
        _require_windows_artifact_acl(path)
        descriptor = native_runtime.os.open(
            path,
            native_runtime.os.O_RDONLY
            | getattr(native_runtime.os, "O_BINARY", 0)
            | getattr(native_runtime.os, "O_CLOEXEC", 0)
            | getattr(native_runtime.os, "O_NOFOLLOW", 0),
        )
        opened = native_runtime.os.fstat(descriptor)
        current = path.lstat()
        if (
            not native_runtime.stat.S_ISREG(opened.st_mode)
            or not native_runtime.stat.S_ISREG(current.st_mode)
            or (opened.st_dev, opened.st_ino) != (metadata.st_dev, metadata.st_ino)
            or (current.st_dev, current.st_ino) != (metadata.st_dev, metadata.st_ino)
            or opened.st_size != metadata.st_size
            or (reparse_point and getattr(current, "st_file_attributes", 0) & reparse_point)
        ):
            raise native_runtime.NativeRuntimeError(f"{label} changed while reading")
        raw = native_runtime.os.read(descriptor, maximum_bytes + 1)
        final = native_runtime.os.fstat(descriptor)
        final_path = path.lstat()
        if (
            len(raw) != metadata.st_size
            or final.st_size != metadata.st_size
            or final.st_mtime_ns != opened.st_mtime_ns
            or final.st_ctime_ns != opened.st_ctime_ns
            or not native_runtime.stat.S_ISREG(final_path.st_mode)
            or path.is_symlink()
            or (final_path.st_dev, final_path.st_ino) != (metadata.st_dev, metadata.st_ino)
            or final_path.st_size != metadata.st_size
            or (reparse_point and getattr(final_path, "st_file_attributes", 0) & reparse_point)
        ):
            raise native_runtime.NativeRuntimeError(f"{label} changed while reading")

        value = parse_bounded_json(raw.decode("utf-8"))
    except native_runtime.NativeRuntimeError:
        raise
    except (
        OSError,
        UnicodeDecodeError,
        ValueError,
        RecursionError,
        native_runtime.json.JSONDecodeError,
    ) as exc:
        raise native_runtime.NativeRuntimeError(f"{label} is unavailable or malformed") from exc
    finally:
        if descriptor >= 0:
            native_runtime.os.close(descriptor)
    if not is_json(value):
        raise native_runtime.NativeRuntimeError(f"{label} is malformed")
    return value


def _windows_plugin_verification_manifest(
    artifact_path: Path,
    spec: PlatformRuntimeSpec,
) -> WindowsRuntimeVerification:
    """Resolve the reviewed trust policy for one plugin-bundled Windows EXE.

    Official Windows companions are intentionally unsigned. Their production
    authority is the reviewed immutable release lock, provenance/composite
    binding, exact executable digest, and canonical official-cache lineage.
    Custom installers retain their narrow, digest-bound signing handoff and
    require an explicit gate for unsigned artifacts. macOS companions remain
    independently signed and signature-verified.
    """

    if not native_runtime._is_windows_spec(spec):
        raise native_runtime.NativeRuntimeError("Windows runtime descriptor is unavailable")
    if native_runtime.uses_production_windows_bundle(artifact_path):
        return native_runtime._windows_production_verification_manifest(artifact_path, spec)
    descriptor_path = native_runtime._windows_plugin_runtime_descriptor_path(artifact_path)
    try:
        plugin_root = artifact_path.parent.resolve(strict=True)
        descriptor_root = descriptor_path.parent.resolve(strict=True)
        resolved_descriptor = descriptor_path.resolve(strict=True)
        metadata = resolved_descriptor.stat()
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "plugin-bundled Windows signing descriptor is unavailable"
        ) from exc
    if (
        artifact_path.parent.is_symlink()
        or descriptor_path.is_symlink()
        or descriptor_path.parent.is_symlink()
        or descriptor_root.parent != plugin_root
        or resolved_descriptor.parent != descriptor_root
        or not native_runtime.stat.S_ISREG(metadata.st_mode)
        or metadata.st_size <= 0
        or metadata.st_size > native_runtime.MAXIMUM_MANIFEST_BYTES
    ):
        raise native_runtime.NativeRuntimeError(
            "plugin-bundled Windows signing descriptor is unsafe"
        )
    for path in (artifact_path, resolved_descriptor):
        native_runtime._require_windows_safe_artifact_path(
            path, root=plugin_root, label="plugin-bundled Windows artifact"
        )
    payload = native_runtime._read_strict_local_json(
        resolved_descriptor,
        maximum_bytes=native_runtime.MAXIMUM_MANIFEST_BYTES,
        label="plugin-bundled Windows signing descriptor",
    )
    executable_sha256 = payload.get("executableSha256")
    if (
        set(payload)
        != {
            "schemaVersion",
            "platform",
            "artifactName",
            "executableSha256",
            "signing",
        }
        or type(payload.get("schemaVersion")) is not int
        or payload["schemaVersion"] != 1
        or payload.get("platform") != spec.platform_key
        or payload.get("artifactName") != spec.artifact_name
        or not isinstance(executable_sha256, str)
        or native_runtime.SHA256_HEX_PATTERN.fullmatch(executable_sha256) is None
        or executable_sha256 != native_runtime.sha256_regular_file(artifact_path)
    ):
        raise native_runtime.NativeRuntimeError(
            "plugin-bundled Windows signing descriptor is malformed"
        )
    signing = payload.get("signing")
    if not isinstance(signing, dict):
        raise native_runtime.NativeRuntimeError(
            "plugin-bundled Windows signing descriptor is malformed"
        )
    kind = signing.get("kind")
    if kind == "unsigned-test":
        if set(signing) != {"kind"} or not native_runtime.allow_unsigned_test_app():
            raise native_runtime.NativeRuntimeError(
                "plugin-bundled Windows signing descriptor is malformed"
            )
        unsigned_policy: UnsignedTestSigningPolicy = {"kind": "unsigned-test"}
        return {"signing": unsigned_policy}
    subject = signing.get("subject")
    thumbprint = signing.get("thumbprint")
    if (
        set(signing) != {"kind", "subject", "thumbprint"}
        or kind != "authenticode"
        or not isinstance(subject, str)
        or not isinstance(thumbprint, str)
        or not native_runtime._valid_authenticode_identity(subject, thumbprint)
    ):
        raise native_runtime.NativeRuntimeError(
            "plugin-bundled Windows signing descriptor is malformed"
        )
    authenticode_policy: AuthenticodeSigningPolicy = {
        "kind": "authenticode",
        "subject": subject,
        "thumbprint": thumbprint.upper(),
    }
    return {
        "signing": authenticode_policy,
    }


def uses_production_windows_bundle(artifact_path: Path) -> bool:
    """Identify the current home's official Windows cache verification policy."""

    if native_runtime.RUNTIME_CONFIG.flavor != "production":
        return False
    family_root = native_runtime.plugin_cache_family_root(artifact_path.parent)
    return bool(
        family_root is not None
        and family_root.name == native_runtime.RUNTIME_CONFIG.server_name
        and family_root.parent.name in native_runtime.OFFICIAL_CACHE_PUBLISHERS
    )


def _windows_production_lock_asset_is_valid(value: object, expected_name: str) -> bool:
    if not is_json(value) or set(value) != {"objectKey", "sha256", "sizeBytes"}:
        return False
    digest = value.get("sha256")
    size = value.get("sizeBytes")
    return bool(
        isinstance(digest, str)
        and native_runtime.SHA256_HEX_PATTERN.fullmatch(digest) is not None
        and type(size) is int
        and 0 < size <= native_runtime.MAXIMUM_ARCHIVE_BYTES
        and value.get("objectKey") == f"v3/blobs/sha256/{digest}/{expected_name}"
    )


def _windows_artifact_capabilities_are_valid(raw: object) -> bool:
    if (
        not isinstance(raw, list)
        or not raw
        or len(raw) > 256
        or any(not is_safe_control_wire_capability(capability) for capability in raw)
        or len(raw) != len(set(raw))
    ):
        return False
    capabilities = frozenset(raw)
    if not capabilities.isdisjoint(COMPANION_CAPABILITIES):
        # Any recognized v2 capability selects this entire profile. A partial
        # or mixed v2 release must never fall back to historical artifact proof.
        return _WINDOWS_RELEASE_REQUIRED_CAPABILITIES.issubset(
            capabilities
        ) and capabilities.issubset(COMPANION_CAPABILITIES)
    # Handoff also verifies older processes running from the official cache.
    # Preserve their complete, reviewed v1 artifact profile, not v1 product RPCs.
    return native_runtime.WINDOWS_REQUIRED_UPDATE_CAPABILITIES.issubset(capabilities)


def _windows_production_verification_manifest(
    artifact_path: Path,
    spec: PlatformRuntimeSpec,
) -> WindowsRuntimeVerification:
    """Bind a copied production EXE to its materialized platform entry."""

    plugin_root = artifact_path.parent
    descriptor_path = plugin_root / native_runtime.WINDOWS_PRODUCTION_BUNDLE_RELATIVE_PATH
    lock_path = plugin_root / native_runtime.WINDOWS_PRODUCTION_LOCK_RELATIVE_PATH
    composite_path = plugin_root / native_runtime.VERIFIED_CAM_DISTRIBUTION_RELATIVE_PATH
    try:
        resolved_root = plugin_root.resolve(strict=True)
        metadata = descriptor_path.lstat()
        resolved_descriptor = descriptor_path.resolve(strict=True)
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "plugin-bundled Windows distribution is unavailable"
        ) from exc
    if (
        descriptor_path.is_symlink()
        or resolved_descriptor
        != resolved_root / native_runtime.WINDOWS_PRODUCTION_BUNDLE_RELATIVE_PATH
        or not native_runtime.stat.S_ISREG(metadata.st_mode)
        or metadata.st_size <= 0
        or metadata.st_size > native_runtime.MAXIMUM_MANIFEST_BYTES
    ):
        raise native_runtime.NativeRuntimeError("plugin-bundled Windows distribution is unsafe")
    payload = native_runtime._read_strict_local_json(
        resolved_descriptor,
        maximum_bytes=native_runtime.MAXIMUM_MANIFEST_BYTES,
        label="plugin-bundled Windows distribution",
    )
    lock = native_runtime._read_strict_local_json(
        lock_path,
        maximum_bytes=native_runtime.MAXIMUM_MANIFEST_BYTES,
        label="plugin-bundled Windows artifact lock",
    )
    composite = native_runtime._read_strict_local_json(
        composite_path,
        maximum_bytes=native_runtime.MAXIMUM_MANIFEST_BYTES,
        label="plugin-bundled Windows composite distribution",
    )
    release = payload.get("release")
    platforms = payload.get("platforms")
    entry = platforms.get(spec.platform_key) if isinstance(platforms, dict) else None
    expected_relative = f"native/{spec.platform_key}/{spec.artifact_name}"
    tag = release.get("tag") if isinstance(release, dict) else None
    tag_sha = release.get("tagSha") if isinstance(release, dict) else None
    version = release.get("version") if isinstance(release, dict) else None
    signing = entry.get("signing") if isinstance(entry, dict) else None
    capabilities = entry.get("capabilities") if isinstance(entry, dict) else None
    lock_release = lock.get("release")
    lock_platforms = lock.get("platforms")
    lock_entry = lock_platforms.get(spec.platform_key) if isinstance(lock_platforms, dict) else None
    lock_executable = lock_entry.get("executable") if isinstance(lock_entry, dict) else None
    lock_fragment = lock_entry.get("fragment") if isinstance(lock_entry, dict) else None
    lock_provenance = lock_entry.get("provenance") if isinstance(lock_entry, dict) else None
    lock_storage = lock.get("storage")
    sources = composite.get("sources")
    binding = sources.get("windows") if isinstance(sources, dict) else None
    bound_release = binding.get("release") if isinstance(binding, dict) else None
    bound_lock = binding.get("lock") if isinstance(binding, dict) else None
    bound_descriptor = binding.get("descriptor") if isinstance(binding, dict) else None
    if (
        set(payload) != {"schemaVersion", "kind", "release", "platforms"}
        or type(payload.get("schemaVersion")) is not int
        or payload["schemaVersion"] != 1
        or payload.get("kind") != "chatgpt-meetings-windows-production-bundle"
        or not isinstance(release, dict)
        or set(release) != {"tag", "tagSha", "version"}
        or not isinstance(tag, str)
        or not tag
        or not tag.startswith("chatgpt-meetings-v")
        or tag.lower() == "latest"
        or not isinstance(tag_sha, str)
        or native_runtime.re.fullmatch(r"[a-f0-9]{40}", tag_sha) is None
        or not isinstance(version, str)
        or not version
        or native_runtime.GITHUB_RELEASE_COMPONENT.fullmatch(version) is None
        or tag != f"chatgpt-meetings-v{version}"
        or not isinstance(platforms, dict)
        or set(platforms) != {"windows-x64", "windows-arm64"}
        or not isinstance(entry, dict)
        or set(entry)
        != {
            "artifactName",
            "capabilities",
            "signing",
            "archiveSha256",
            "archiveSizeBytes",
            "fragmentSha256",
            "provenanceSha256",
            "executablePath",
            "executableSha256",
            "executableSizeBytes",
        }
        | ({"thirdPartyLicenses"} if "thirdPartyLicenses" in entry else set())
        or entry.get("artifactName") != spec.artifact_name
        or entry.get("executablePath") != expected_relative
        or not isinstance(entry.get("executableSha256"), str)
        or native_runtime.SHA256_HEX_PATTERN.fullmatch(entry["executableSha256"]) is None
        or type(entry.get("executableSizeBytes")) is not int
        or entry["executableSizeBytes"] <= 0
        or entry["executableSizeBytes"] > native_runtime.MAXIMUM_ARCHIVE_BYTES
        or not isinstance(entry.get("archiveSha256"), str)
        or native_runtime.SHA256_HEX_PATTERN.fullmatch(entry["archiveSha256"]) is None
        or type(entry.get("archiveSizeBytes")) is not int
        or entry["archiveSizeBytes"] <= 0
        or entry["archiveSizeBytes"] > native_runtime.MAXIMUM_ARCHIVE_BYTES
        or not isinstance(entry.get("fragmentSha256"), str)
        or native_runtime.SHA256_HEX_PATTERN.fullmatch(entry["fragmentSha256"]) is None
        or not isinstance(entry.get("provenanceSha256"), str)
        or native_runtime.SHA256_HEX_PATTERN.fullmatch(entry["provenanceSha256"]) is None
        or not isinstance(signing, dict)
        or not _windows_artifact_capabilities_are_valid(capabilities)
        or not isinstance(lock, dict)
        or set(lock) != {"schemaVersion", "kind", "storage", "release", "platforms"}
        or type(lock.get("schemaVersion")) is not int
        or lock["schemaVersion"] != 2
        or lock.get("kind") != "chatgpt-meetings-cam-windows-distribution-lock"
        or not isinstance(lock_release, dict)
        or set(lock_release) != {"tag", "tagSha"}
        or lock_release.get("tag") != tag
        or lock_release.get("tagSha") != tag_sha
        or not isinstance(lock_storage, dict)
        or set(lock_storage) != {"provider", "accountName", "containerName"}
        or lock_storage.get("provider") != "azure-blob"
        or lock_storage.get("accountName") != native_runtime.WINDOWS_PRODUCTION_AZURE_ACCOUNT_NAME
        or lock_storage.get("containerName")
        != native_runtime.WINDOWS_PRODUCTION_AZURE_CONTAINER_NAME
        or not isinstance(lock_platforms, dict)
        or set(lock_platforms) != {"windows-x64", "windows-arm64"}
        or not isinstance(lock_entry, dict)
        or set(lock_entry) != {"executable", "fragment", "provenance"}
        or not isinstance(lock_executable, dict)
        or not native_runtime._windows_production_lock_asset_is_valid(
            lock_executable,
            f"ChatGPT-Meetings-{version}-{spec.platform_key}.exe",
        )
        or not isinstance(lock_fragment, dict)
        or not native_runtime._windows_production_lock_asset_is_valid(
            lock_fragment,
            f"ChatGPT-Meetings-{version}-{spec.platform_key}-release.json",
        )
        or not isinstance(lock_provenance, dict)
        or not native_runtime._windows_production_lock_asset_is_valid(
            lock_provenance,
            f"ChatGPT-Meetings-{version}-{spec.platform_key}-provenance.json",
        )
        or lock_executable.get("sha256") != entry["executableSha256"]
        or lock_executable.get("sizeBytes") != entry["executableSizeBytes"]
        or lock_fragment.get("sha256") != entry["fragmentSha256"]
        or lock_provenance.get("sha256") != entry["provenanceSha256"]
        or type(composite.get("schemaVersion")) is not int
        or composite["schemaVersion"] != 2
        or composite.get("kind") != "chatgpt-meetings-verified-composite-distribution"
        or not isinstance(binding, dict)
        or set(binding) != {"kind", "release", "lock", "descriptor"}
        or binding.get("kind") != "chatgpt-meetings-windows-production-bundle"
        or not isinstance(bound_release, dict)
        or set(bound_release) != {"tag", "tagSha", "version"}
        or bound_release.get("tag") != tag
        or bound_release.get("tagSha") != tag_sha
        or bound_release.get("version") != version
        or not isinstance(bound_lock, dict)
        or set(bound_lock) != {"sha256", "sizeBytes"}
        or bound_lock.get("sha256") != native_runtime.sha256_regular_file(lock_path)
        or bound_lock.get("sizeBytes") != lock_path.stat().st_size
        or not isinstance(bound_descriptor, dict)
        or set(bound_descriptor) != {"sha256", "sizeBytes"}
        or bound_descriptor.get("sha256") != native_runtime.sha256_regular_file(descriptor_path)
        or bound_descriptor.get("sizeBytes") != descriptor_path.stat().st_size
    ):
        raise native_runtime.NativeRuntimeError("plugin-bundled Windows distribution is malformed")
    signing_kind = signing.get("kind")
    signing_subject = signing.get("subject")
    signing_thumbprint = signing.get("thumbprint")
    if signing_kind == "unsigned-test":
        if set(signing) != {"kind"}:
            raise native_runtime.NativeRuntimeError(
                "plugin-bundled Windows distribution is malformed"
            )
        unsigned_policy: UnsignedTestSigningPolicy = {"kind": "unsigned-test"}
        signing_policy: WindowsSigningPolicy = unsigned_policy
    elif (
        set(signing) != {"kind", "subject", "thumbprint"}
        or signing_kind != "authenticode"
        or not isinstance(signing_subject, str)
        or not isinstance(signing_thumbprint, str)
        or not native_runtime._valid_authenticode_identity(
            signing_subject,
            signing_thumbprint,
        )
    ):
        raise native_runtime.NativeRuntimeError("plugin-bundled Windows distribution is malformed")
    else:
        authenticode_policy: AuthenticodeSigningPolicy = {
            "kind": "authenticode",
            "subject": signing_subject,
            "thumbprint": signing_thumbprint,
        }
        signing_policy = authenticode_policy
    source = resolved_root / expected_relative
    native_runtime._require_windows_safe_artifact_path(
        source,
        root=resolved_root,
        label="plugin-bundled Windows executable",
    )
    native_runtime._require_windows_safe_artifact_path(
        artifact_path,
        root=resolved_root,
        label="plugin-bundled Windows executable",
    )
    try:
        source_metadata = source.lstat()
        target_metadata = artifact_path.lstat()
        resolved_source = source.resolve(strict=True)
        resolved_target = artifact_path.resolve(strict=True)
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "plugin-bundled Windows executable is unavailable"
        ) from exc
    if (
        source.is_symlink()
        or artifact_path.is_symlink()
        or resolved_source != source
        or resolved_target != artifact_path
        or not native_runtime.stat.S_ISREG(source_metadata.st_mode)
        or not native_runtime.stat.S_ISREG(target_metadata.st_mode)
        or source_metadata.st_size != entry["executableSizeBytes"]
        or target_metadata.st_size != entry["executableSizeBytes"]
        or native_runtime.sha256_regular_file(source) != entry["executableSha256"]
        or native_runtime.sha256_regular_file(artifact_path) != entry["executableSha256"]
    ):
        raise native_runtime.NativeRuntimeError(
            "plugin-bundled Windows executable does not match distribution"
        )
    lock_binding: WindowsDistributionArtifact = {
        "sha256": bound_lock["sha256"],
        "sizeBytes": bound_lock["sizeBytes"],
    }
    descriptor_binding: WindowsDistributionArtifact = {
        "sha256": bound_descriptor["sha256"],
        "sizeBytes": bound_descriptor["sizeBytes"],
    }
    composite_binding: WindowsDistributionArtifact = {
        "sha256": native_runtime.sha256_regular_file(composite_path),
        "sizeBytes": composite_path.stat().st_size,
    }
    release_binding: WindowsDistributionRelease = {
        "tag": tag,
        "tagSha": tag_sha,
        "version": version,
    }
    storage_binding: WindowsDistributionStorage = {
        "provider": "azure-blob",
        "accountName": native_runtime.WINDOWS_PRODUCTION_AZURE_ACCOUNT_NAME,
        "containerName": native_runtime.WINDOWS_PRODUCTION_AZURE_CONTAINER_NAME,
    }
    distribution_binding: WindowsDistributionBinding = {
        "kind": "chatgpt-meetings-windows-production-bundle",
        "release": release_binding,
        "storage": storage_binding,
        "lock": lock_binding,
        "descriptor": descriptor_binding,
        "composite": composite_binding,
    }
    return {
        "signing": signing_policy,
        "windowsDistribution": distribution_binding,
    }


def _require_windows_safe_artifact_path(path: Path, *, root: Path, label: str) -> None:
    """Reject reparse/symlink ancestors and unsafe ACLs before an EXE proof."""

    try:
        relative = path.relative_to(root)
    except ValueError as exc:
        raise native_runtime.NativeRuntimeError(f"{label} escaped its plugin root") from exc
    reparse_point = getattr(native_runtime.stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    try:
        root_metadata = root.lstat()
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(f"{label} root is unavailable") from exc
    if (
        root.is_symlink()
        or not native_runtime.stat.S_ISDIR(root_metadata.st_mode)
        or (reparse_point and getattr(root_metadata, "st_file_attributes", 0) & reparse_point)
    ):
        raise native_runtime.NativeRuntimeError(f"{label} root is unsafe")
    _require_windows_artifact_acl(root)
    current = root
    for index, component in enumerate(relative.parts):
        current = current / component
        try:
            metadata = current.lstat()
        except OSError as exc:
            raise native_runtime.NativeRuntimeError(f"{label} is unavailable") from exc
        leaf = index + 1 == len(relative.parts)
        if (
            current.is_symlink()
            or (reparse_point and getattr(metadata, "st_file_attributes", 0) & reparse_point)
            or (leaf and not native_runtime.stat.S_ISREG(metadata.st_mode))
            or (not leaf and not native_runtime.stat.S_ISDIR(metadata.st_mode))
        ):
            raise native_runtime.NativeRuntimeError(f"{label} is unsafe")
        _require_windows_artifact_acl(current)
    try:
        if path.resolve(strict=True) != path:
            raise native_runtime.NativeRuntimeError(f"{label} is unsafe")
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(f"{label} is unavailable") from exc


def _validated_handoff_manifest(
    app_path: Path,
    spec: PlatformRuntimeSpec,
) -> Mapping[str, object]:
    """Revalidate a handoff candidate and retain its platform verification proof."""

    try:
        native_runtime.stable_runtime_artifact_root(app_path)
        is_stable = True
    except (OSError, native_runtime.NativeRuntimeError):
        is_stable = False
    if is_stable:
        manifest = native_runtime.stable_runtime_verification_manifest(app_path, spec)
    else:
        manifest = (
            native_runtime._windows_plugin_verification_manifest(app_path, spec)
            if native_runtime._is_windows_spec(spec)
            else {"teamIdentifier": native_runtime.TEAM_IDENTIFIER}
            if native_runtime.RUNTIME_CONFIG.flavor == "production"
            else {}
        )
    native_runtime.validate_app(app_path, manifest, spec)
    return manifest


def validate_handoff_app(app_path: Path, spec: PlatformRuntimeSpec) -> None:
    """Revalidate a handoff candidate with its platform signing contract."""

    _validated_handoff_manifest(app_path, spec)


def verified_handoff_app_release_identity(app_path: Path, spec: PlatformRuntimeSpec) -> str:
    """Read the full release from the same verified image, never its display label."""

    windows = native_runtime._is_windows_spec(spec)
    identity_path = app_path if windows else app_path / "Contents" / "Info.plist"
    before = _path_identity(identity_path)
    # Same-size metadata edits can share timestamps; bind Darwin release bytes too.
    metadata_sha256 = None if windows else native_runtime.sha256_regular_file(identity_path)
    manifest = _validated_handoff_manifest(app_path, spec)
    if windows:
        distribution = manifest.get("windowsDistribution")
        release = distribution.get("release") if isinstance(distribution, dict) else None
        version = release.get("version") if isinstance(release, dict) else None
    else:
        info, _executable, _helper = native_runtime._load_app_metadata(app_path, spec)
        if info.get("ChatGPTMeetingsVersion") is None:
            # Released predecessors can predate the full stamp. The existing
            # strict parser still requires matching marketing and build fields.
            info["ChatGPTMeetingsVersion"] = (
                f"{info.get('CFBundleShortVersionString')}-alpha.{info.get('CFBundleVersion')}"
            )
        version = native_runtime._plugin_bundle_release_version(info)
    if (
        _path_identity(identity_path) != before
        or (not windows and native_runtime.sha256_regular_file(identity_path) != metadata_sha256)
        or not isinstance(version, str)
    ):
        raise native_runtime.NativeRuntimeError("native handoff release identity is unavailable")
    return version


def _verified_production_unsigned_windows(
    app_path: Path,
    manifest: Mapping[str, object],
    spec: PlatformRuntimeSpec,
) -> bool:
    """Accept unsigned Windows only from a reviewed official runtime lineage."""

    expected_keys = {"signing", "windowsDistribution"}
    if "thirdPartyLicensesSha256" in manifest:
        expected_keys.add("thirdPartyLicensesSha256")
    if (
        native_runtime.RUNTIME_CONFIG.flavor != "production"
        or set(manifest) != expected_keys
        or manifest.get("signing") != {"kind": "unsigned-test"}
    ):
        return False

    licenses_sha256 = manifest.get("thirdPartyLicensesSha256")
    try:
        if "thirdPartyLicensesSha256" in manifest:
            if (
                not isinstance(licenses_sha256, str)
                or native_runtime.SHA256_HEX_PATTERN.fullmatch(licenses_sha256) is None
                or native_runtime._windows_source_licenses_sha256(app_path, spec) != licenses_sha256
            ):
                return False
        distribution = native_runtime._validated_stable_windows_distribution_binding(
            manifest.get("windowsDistribution")
        )
        if manifest.get("windowsDistribution") != distribution:
            return False
        if native_runtime.uses_production_windows_bundle(app_path):
            source_verification = native_runtime._windows_production_verification_manifest(
                app_path,
                spec,
            )
            if isinstance(licenses_sha256, str):
                source_verification["thirdPartyLicensesSha256"] = licenses_sha256
            return manifest == source_verification

        resolved_artifact = app_path.resolve(strict=True)
        generation_root = resolved_artifact.parent
        runtime_root = native_runtime.stable_runtime_artifact_root(app_path)
        versions_root = native_runtime._private_runtime_directory(
            runtime_root / "versions",
            create=False,
        )
        if (
            app_path.is_symlink()
            or generation_root.parent != versions_root
            or resolved_artifact != generation_root / spec.artifact_name
        ):
            return False
        native_runtime._private_runtime_directory(generation_root, create=False)
        stable_manifest = native_runtime._validated_stable_generation_manifest(
            native_runtime._read_stable_runtime_manifest(generation_root / ".runtime.json"),
            spec,
        )
        if (
            generation_root.name != stable_manifest["generation"]
            and native_runtime.re.fullmatch(r"\.stage-[a-f0-9]{32}", generation_root.name) is None
        ):
            return False
        return (
            stable_manifest["verification"] == manifest
            and native_runtime.sha256_regular_file(resolved_artifact)
            == stable_manifest["executableSha256"]
        )
    except (OSError, native_runtime.NativeRuntimeError):
        return False


def validate_app(
    app_path: Path,
    manifest: Mapping[str, object],
    spec: PlatformRuntimeSpec | None = None,
) -> None:
    selected_spec = spec or native_runtime.configured_platform_spec()
    if native_runtime._is_windows_spec(selected_spec):
        executable = native_runtime._load_windows_executable(app_path, selected_spec)
        signing = manifest.get("signing")
        if (
            isinstance(signing, dict)
            and signing.get("kind") == "unsigned-test"
            and (
                native_runtime.allow_unsigned_test_app()
                or _verified_production_unsigned_windows(app_path, manifest, selected_spec)
            )
        ):
            return
        if not native_runtime._is_windows_host():
            raise native_runtime.NativeRuntimeError(
                "native Windows signature verification is unavailable"
            )
        if (
            not isinstance(signing, dict)
            or signing.get("kind") != "authenticode"
            or not native_runtime._valid_authenticode_identity(
                signing.get("subject"), signing.get("thumbprint")
            )
        ):
            raise native_runtime.NativeRuntimeError(
                "native executable signing policy is missing or malformed"
            )
        # Keep the path out of PowerShell source: a fixed, child-only
        # environment variable carries it into -LiteralPath, and fixed child
        # variables carry the pinned signer identity, so a valid Windows path
        # or manifest value cannot become script text. Authenticode is the
        # Windows analogue of the Darwin codesign gate below.
        script = (
            "$signature = Get-AuthenticodeSignature "
            "-LiteralPath $env:CHATGPT_MEETINGS_VERIFY_PATH; "
            "if ($signature.Status -ne 'Valid' -or "
            "$null -eq $signature.SignerCertificate) { exit 1 }; "
            "if ($signature.SignerCertificate.Subject -cne "
            "$env:CHATGPT_MEETINGS_VERIFY_SIGNER_SUBJECT) { exit 1 }; "
            "if ($signature.SignerCertificate.Thumbprint.ToUpperInvariant() "
            "-cne $env:CHATGPT_MEETINGS_VERIFY_SIGNER_THUMBPRINT) { exit 1 }"
        )
        environment = native_runtime.os.environ.copy()
        environment["CHATGPT_MEETINGS_VERIFY_PATH"] = str(executable)
        environment["CHATGPT_MEETINGS_VERIFY_SIGNER_SUBJECT"] = signing["subject"]
        environment["CHATGPT_MEETINGS_VERIFY_SIGNER_THUMBPRINT"] = signing["thumbprint"].upper()
        try:
            native_runtime.subprocess.run(
                [
                    "powershell.exe",
                    "-NoProfile",
                    "-NonInteractive",
                    "-Command",
                    script,
                ],
                check=True,
                stdout=native_runtime.subprocess.DEVNULL,
                stderr=native_runtime.subprocess.DEVNULL,
                env=environment,
                timeout=native_runtime.WINDOWS_SIGNATURE_VERIFICATION_TIMEOUT_SECONDS,
            )
        except (OSError, native_runtime.subprocess.TimeoutExpired) as exc:
            raise native_runtime.NativeRuntimeError(
                "native executable signature verification is unavailable"
            ) from exc
        except native_runtime.subprocess.CalledProcessError as exc:
            raise native_runtime.NativeRuntimeError(
                "native executable signature verification failed"
            ) from exc
        return

    _info, executable, helper = native_runtime._load_app_metadata(app_path, selected_spec)
    if native_runtime.RUNTIME_CONFIG.flavor == "production":
        native_runtime._require_darwin_macho_architecture(executable, selected_spec)
        native_runtime._require_darwin_macho_architecture(helper, selected_spec)
    if (
        native_runtime.allow_unsigned_test_app()
        and native_runtime.RUNTIME_CONFIG.flavor != "production"
    ):
        return
    try:
        native_runtime.subprocess.run(
            ["/usr/bin/codesign", "--verify", "--deep", "--strict", str(app_path)],
            check=True,
            stdout=native_runtime.subprocess.DEVNULL,
            stderr=native_runtime.subprocess.DEVNULL,
        )
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "native app signature verification is unavailable"
        ) from exc
    except native_runtime.subprocess.CalledProcessError as exc:
        raise native_runtime.NativeRuntimeError("native app signature verification failed") from exc
    expected_team = manifest.get("teamIdentifier", manifest.get("teamId"))
    expected_authority = manifest.get("signingAuthority")
    if (
        isinstance(expected_team, str)
        and expected_team
        or isinstance(expected_authority, str)
        and expected_authority
    ):
        try:
            details = native_runtime.subprocess.run(
                ["/usr/bin/codesign", "-dvv", str(app_path)],
                check=True,
                capture_output=True,
                text=True,
            ).stderr
        except (OSError, native_runtime.subprocess.CalledProcessError) as exc:
            raise native_runtime.NativeRuntimeError(
                "native app team identifier verification failed"
            ) from exc
        if (
            isinstance(expected_team, str)
            and expected_team
            and (f"TeamIdentifier={expected_team}" not in details)
        ):
            raise native_runtime.NativeRuntimeError("native app team identifier does not match")
        if (
            isinstance(expected_authority, str)
            and expected_authority
            and (f"Authority={expected_authority}" not in details)
        ):
            raise native_runtime.NativeRuntimeError("native app signing authority does not match")
