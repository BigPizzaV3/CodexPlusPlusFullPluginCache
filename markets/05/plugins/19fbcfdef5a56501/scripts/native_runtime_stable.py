"""Stable, immutable ChatGPT Meetings runtime-generation helpers."""

from __future__ import annotations

try:
    import fcntl
except ImportError:  # pragma: no cover - Windows has no flock module.
    fcntl = None
import errno
import hashlib
import json
import os
import re
import shutil
import stat
import time
import uuid
from collections.abc import Mapping
from contextlib import contextmanager
from pathlib import Path
from typing import Callable, Iterator, TypedDict

import native_runtime
from native_runtime_types import (
    AuthenticodeSigningPolicy,
    DarwinRuntimeVerification,
    MaterializeVerificationPhase,
    NativeArtifactFingerprint,
    NativeRuntimeStatus,
    StableGenerationManifest,
    StableRuntimeVerification,
    UnsignedTestSigningPolicy,
    WindowsDistributionArtifact,
    WindowsDistributionBinding,
    WindowsDistributionRelease,
    WindowsDistributionStorage,
    WindowsRuntimeVerification,
    WindowsSigningPolicy,
)

from helpers import is_json, parse_bounded_json


class _HandoffArguments(TypedDict, total=False):
    source_plugin_root: Path
    recover_unhealthy_current: bool


def plugin_artifact_path(plugin_root: Path, spec: native_runtime.PlatformRuntimeSpec) -> Path:
    """Resolve the direct plugin child without accepting path substitution.

    A top-level symlink could redirect Codex to a different signed app outside
    the plugin cache. Framework symlinks *inside* a normal macOS bundle remain
    valid and are covered by codesign verification.
    """

    root = plugin_root.expanduser()
    candidate = root / spec.artifact_name
    if candidate.is_symlink():
        raise native_runtime.NativeRuntimeError("plugin-bundled native artifact is unsafe")
    try:
        resolved_root = root.resolve(strict=True)
    except OSError as exc:
        raise native_runtime.NativeRuntimeResourceError(
            native_runtime.NativeRuntimeResourceOperation.RESOLVE_ARTIFACT_ROOT
        ) from exc
    try:
        resolved_candidate = candidate.resolve(strict=True)
    except FileNotFoundError as exc:
        # A pruned parent is not proof that the signed native child is missing.
        try:
            if root.resolve(strict=True) == resolved_root:
                raise native_runtime.NativeRuntimeArtifactMissing() from exc
        except OSError:
            pass
        # The preserved cause came from resolving the child path. A failed
        # or changed parent recheck cannot identify which component vanished.
        raise native_runtime.NativeRuntimeResourceError(
            native_runtime.NativeRuntimeResourceOperation.RESOLVE_NATIVE_ARTIFACT
        ) from exc
    except OSError as exc:
        raise native_runtime.NativeRuntimeResourceError(
            native_runtime.NativeRuntimeResourceOperation.RESOLVE_NATIVE_ARTIFACT
        ) from exc
    if resolved_candidate.parent != resolved_root:
        raise native_runtime.NativeRuntimeError("plugin-bundled native artifact escaped its root")
    if spec.artifact_path_kind == "directory":
        if not resolved_candidate.is_dir():
            raise native_runtime.NativeRuntimeError("plugin-bundled native artifact is unavailable")
    elif not resolved_candidate.is_file():
        raise native_runtime.NativeRuntimeError("plugin-bundled native artifact is unavailable")
    return resolved_candidate


def _private_runtime_directory(
    path: Path,
    *,
    owner_only: bool = True,
    create: bool = True,
) -> Path:
    """Create or validate one Codex-owned directory without path substitution."""

    if not path.is_absolute() or Path(os.path.normpath(str(path))) != path:
        raise native_runtime.NativeRuntimeError("stable native runtime root is unsafe")
    created = False
    if create:
        try:
            path.mkdir(mode=0o700, parents=False, exist_ok=False)
            created = True
        except FileExistsError:
            pass
        except OSError as exc:
            raise native_runtime.NativeRuntimeError(
                "stable native runtime root is unavailable"
            ) from exc
    try:
        metadata = path.lstat()
        resolved = path.resolve(strict=True)
        if created and not native_runtime._is_windows_host() and owner_only:
            os.chmod(path, 0o700)
            metadata = path.lstat()
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "stable native runtime root is unavailable"
        ) from exc
    reparse_point = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    if (
        path.is_symlink()
        or resolved != path
        or not stat.S_ISDIR(metadata.st_mode)
        or (reparse_point and getattr(metadata, "st_file_attributes", 0) & reparse_point)
        or (
            owner_only
            and not native_runtime._is_windows_host()
            and (metadata.st_uid != os.getuid() or metadata.st_mode & 0o077)
        )
    ):
        raise native_runtime.NativeRuntimeError("stable native runtime root is unsafe")
    if owner_only:
        native_runtime._require_windows_private_runtime_acl(path)
    return resolved


def _require_windows_safe_lexical_runtime_parent(path: Path) -> None:
    """Reject a junction/symlink ancestor before normalizing a Windows alias."""

    reparse_point = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    current = Path(path.anchor)
    try:
        for component in path.parts:
            if component != path.anchor:
                current /= component
            metadata = current.lstat()
            if (
                current.is_symlink()
                or not stat.S_ISDIR(metadata.st_mode)
                or getattr(metadata, "st_file_attributes", 0) & reparse_point
            ):
                raise native_runtime.NativeRuntimeError("stable native runtime root is unsafe")
    except native_runtime.NativeRuntimeError:
        raise
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "stable native runtime root is unavailable"
        ) from exc


def stable_runtime_root(*, create: bool = True) -> Path:
    """Return private code storage without relocating control or recording data."""

    from native_runtime_windows_recovery import enabled
    from windows_private_runtime import WindowsPrivateRuntimeError, windows_runtime_root

    if enabled():
        configured = os.environ.get("CODEX_HOME", "")
        if configured != configured.strip():
            raise native_runtime.NativeRuntimeError("stable native runtime root is unsafe")
        home = Path(configured).expanduser() if configured else Path.home() / ".codex"
        if not home.is_absolute():
            raise native_runtime.NativeRuntimeError("stable native runtime root is unsafe")
        try:
            return windows_runtime_root(
                home, native_runtime.stable_runtime_directory_name(), create=create
            )
        except (OSError, WindowsPrivateRuntimeError) as exc:
            raise native_runtime.NativeRuntimeError(
                "private Windows runtime is unavailable"
            ) from exc
    return legacy_stable_runtime_root(create=create)


def legacy_stable_runtime_root(*, create: bool = False) -> Path:
    """Retain the previous code namespace for verified existing-owner handoff."""

    configured = os.environ.get("CODEX_HOME", "")
    if configured != configured.strip():
        raise native_runtime.NativeRuntimeError("stable native runtime root is unsafe")
    codex_home = Path(configured).expanduser() if configured else Path.home() / ".codex"
    if not codex_home.is_absolute() or Path(os.path.normpath(str(codex_home))) != codex_home:
        raise native_runtime.NativeRuntimeError("stable native runtime root is unsafe")
    try:
        resolved_parent = codex_home.parent.resolve(strict=True)
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "stable native runtime root is unavailable"
        ) from exc
    if resolved_parent != codex_home.parent and native_runtime._is_windows_host():
        native_runtime._require_windows_safe_lexical_runtime_parent(codex_home.parent)
        try:
            if not codex_home.parent.samefile(resolved_parent):
                raise native_runtime.NativeRuntimeError("stable native runtime root is unsafe")
        except OSError as exc:
            raise native_runtime.NativeRuntimeError(
                "stable native runtime root is unavailable"
            ) from exc
    codex_home = resolved_parent / codex_home.name
    try:
        native_runtime._private_runtime_directory(codex_home, owner_only=False, create=create)
    except native_runtime.NativeRuntimeError:
        if native_runtime._is_windows_host() or not codex_home.is_symlink():
            raise
        try:
            codex_home = codex_home.resolve(strict=True)
        except (OSError, RuntimeError) as exc:
            raise native_runtime.NativeRuntimeError(
                "stable native runtime root is unavailable"
            ) from exc
        native_runtime._private_runtime_directory(codex_home, owner_only=False, create=create)
    runtime_root = native_runtime._private_runtime_directory(
        codex_home / native_runtime.stable_runtime_directory_name(),
        create=create,
    )
    native_runtime._private_runtime_directory(runtime_root / "versions", create=create)
    native_runtime._private_runtime_directory(runtime_root / "state", create=create)
    return runtime_root


def stable_runtime_artifact_root(artifact_path: Path) -> Path:
    """Recognize only the current root or a read-only, verified legacy namespace."""

    from native_runtime_windows_recovery import enabled

    resolved = artifact_path.resolve(strict=True)
    candidates: list[Path] = []
    try:
        candidates.append(native_runtime.stable_runtime_root(create=False))
    except native_runtime.NativeRuntimeError:
        pass
    if enabled():
        try:
            candidates.append(legacy_stable_runtime_root(create=False))
        except native_runtime.NativeRuntimeError:
            pass
    for root in candidates:
        try:
            relative = resolved.relative_to(root / "versions")
        except ValueError:
            continue
        if len(relative.parts) == 2:
            return root
    raise native_runtime.NativeRuntimeError("stable native runtime artifact is unavailable")


def _require_windows_private_runtime_acl(path: Path) -> None:
    if os.name != "nt":
        return
    # control_client owns the platform ACL proof used by every private
    # descriptor/state file. Keep the reverse edge lazy to avoid an import
    # cycle while native_runtime is initializing.
    from control_client import windows_acl_is_private

    if not windows_acl_is_private(path):
        raise native_runtime.NativeRuntimeError("stable native runtime permissions are unsafe")


@contextmanager
def _stable_runtime_family_lock(runtime_root: Path) -> Iterator[Callable[[], None]]:
    """Serialize materialization, activation, and launch across MCP processes."""

    lock_path = runtime_root / "state" / "runtime.lock"
    flags = (
        os.O_RDWR
        | os.O_CREAT
        | getattr(os, "O_BINARY", 0)
        | getattr(os, "O_CLOEXEC", 0)
        | getattr(os, "O_NOFOLLOW", 0)
    )
    descriptor = -1
    locked = False
    try:
        descriptor = os.open(lock_path, flags, 0o600)
        metadata = os.fstat(descriptor)
        path_metadata = lock_path.lstat()
        reparse_point = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
        if (
            not stat.S_ISREG(metadata.st_mode)
            or not stat.S_ISREG(path_metadata.st_mode)
            or lock_path.is_symlink()
            or (reparse_point and getattr(path_metadata, "st_file_attributes", 0) & reparse_point)
            or (metadata.st_dev, metadata.st_ino) != (path_metadata.st_dev, path_metadata.st_ino)
            or (
                not native_runtime._is_windows_host()
                and (metadata.st_uid != os.getuid() or metadata.st_mode & 0o077)
            )
        ):
            raise native_runtime.NativeRuntimeError("stable native runtime lock is unsafe")
        native_runtime._require_windows_private_runtime_acl(lock_path)
        if metadata.st_size == 0:
            os.write(descriptor, b"\x00")
            os.fsync(descriptor)
        deadline = time.monotonic() + native_runtime.STABLE_RUNTIME_LOCK_TIMEOUT_SECONDS
        while True:
            try:
                if os.name == "nt":
                    import msvcrt

                    os.lseek(descriptor, 0, os.SEEK_SET)
                    try:
                        msvcrt.locking(descriptor, msvcrt.LK_NBLCK, 1)
                    except OSError as exc:
                        if exc.errno != errno.EACCES:
                            raise
                        # The Windows CRT reports a held byte-range lock as EACCES.
                        raise BlockingIOError("stable native runtime lock is busy") from exc
                elif fcntl is not None:
                    fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
                else:
                    raise native_runtime.NativeRuntimeError(
                        "stable native runtime lock is unavailable"
                    )
                locked = True
                locked_metadata = os.fstat(descriptor)
                locked_path_metadata = lock_path.lstat()
                state_metadata = lock_path.parent.lstat()
                if (
                    lock_path.is_symlink()
                    or lock_path.parent.is_symlink()
                    or not stat.S_ISREG(locked_metadata.st_mode)
                    or not stat.S_ISREG(locked_path_metadata.st_mode)
                    or not stat.S_ISDIR(state_metadata.st_mode)
                    or (
                        reparse_point
                        and getattr(locked_path_metadata, "st_file_attributes", 0) & reparse_point
                    )
                    or (
                        reparse_point
                        and getattr(state_metadata, "st_file_attributes", 0) & reparse_point
                    )
                    or (locked_metadata.st_dev, locked_metadata.st_ino)
                    != (locked_path_metadata.st_dev, locked_path_metadata.st_ino)
                    or (
                        not native_runtime._is_windows_host()
                        and (
                            locked_metadata.st_uid != os.getuid()
                            or locked_metadata.st_mode & 0o077
                            or state_metadata.st_uid != os.getuid()
                            or state_metadata.st_mode & 0o077
                        )
                    )
                ):
                    raise native_runtime.NativeRuntimeError(
                        "stable native runtime lock changed while acquiring"
                    )
                native_runtime._require_windows_private_runtime_acl(lock_path)
                native_runtime._require_windows_private_runtime_acl(lock_path.parent)
                break
            except (BlockingIOError, OSError) as exc:
                if time.monotonic() >= deadline:
                    failure_type = (
                        native_runtime.NativeRuntimeLockBusy
                        if isinstance(exc, BlockingIOError)
                        else native_runtime.NativeRuntimeError
                    )
                    raise failure_type("stable native runtime lock timed out") from exc
                time.sleep(0.01)
        state_identity = (state_metadata.st_dev, state_metadata.st_ino)

        def revalidate() -> None:
            try:
                held_metadata = os.fstat(descriptor)
                current_metadata = lock_path.lstat()
                current_state_metadata = lock_path.parent.lstat()
            except OSError as exc:
                raise native_runtime.NativeRuntimeError(
                    "stable native runtime lock changed while held"
                ) from exc
            if (
                lock_path.is_symlink()
                or lock_path.parent.is_symlink()
                or not stat.S_ISREG(held_metadata.st_mode)
                or not stat.S_ISREG(current_metadata.st_mode)
                or not stat.S_ISDIR(current_state_metadata.st_mode)
                or (
                    reparse_point
                    and getattr(current_metadata, "st_file_attributes", 0) & reparse_point
                )
                or (
                    reparse_point
                    and getattr(current_state_metadata, "st_file_attributes", 0) & reparse_point
                )
                or (held_metadata.st_dev, held_metadata.st_ino)
                != (current_metadata.st_dev, current_metadata.st_ino)
                or (current_state_metadata.st_dev, current_state_metadata.st_ino) != state_identity
                or (
                    not native_runtime._is_windows_host()
                    and (
                        held_metadata.st_uid != os.getuid()
                        or held_metadata.st_mode & 0o077
                        or current_state_metadata.st_uid != os.getuid()
                        or current_state_metadata.st_mode & 0o077
                    )
                )
            ):
                raise native_runtime.NativeRuntimeError(
                    "stable native runtime lock changed while held"
                )
            native_runtime._require_windows_private_runtime_acl(lock_path)
            native_runtime._require_windows_private_runtime_acl(lock_path.parent)

        # All source snapshots, including nested activation revalidation, are
        # opened after this point and closed before the family lock is released.
        import native_runtime_windows_recovery

        native_runtime_windows_recovery.cleanup_abandoned_sources(runtime_root, revalidate)
        yield revalidate
    except native_runtime.NativeRuntimeError:
        raise
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "stable native runtime lock is unavailable"
        ) from exc
    finally:
        if descriptor >= 0:
            if locked:
                try:
                    if os.name == "nt":
                        import msvcrt

                        os.lseek(descriptor, 0, os.SEEK_SET)
                        msvcrt.locking(descriptor, msvcrt.LK_UNLCK, 1)
                    elif fcntl is not None:
                        fcntl.flock(descriptor, fcntl.LOCK_UN)
                except OSError:
                    pass
            os.close(descriptor)


def _strict_stable_runtime_manifest(raw: bytes) -> dict[str, object]:
    try:
        value = parse_bounded_json(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError, json.JSONDecodeError, RecursionError) as exc:
        raise native_runtime.NativeRuntimeError(
            "stable native runtime manifest is malformed"
        ) from exc
    if not is_json(value):
        raise native_runtime.NativeRuntimeError("stable native runtime manifest is malformed")
    return value


def _read_stable_runtime_manifest(path: Path) -> dict[str, object]:
    flags = (
        os.O_RDONLY
        | getattr(os, "O_BINARY", 0)
        | getattr(os, "O_CLOEXEC", 0)
        | getattr(os, "O_NOFOLLOW", 0)
    )
    descriptor = -1
    try:
        descriptor = os.open(path, flags)
        metadata = os.fstat(descriptor)
        path_metadata = path.lstat()
        reparse_point = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
        if (
            not stat.S_ISREG(metadata.st_mode)
            or not stat.S_ISREG(path_metadata.st_mode)
            or path.is_symlink()
            or (reparse_point and getattr(path_metadata, "st_file_attributes", 0) & reparse_point)
            or (metadata.st_dev, metadata.st_ino) != (path_metadata.st_dev, path_metadata.st_ino)
            or metadata.st_size <= 0
            or metadata.st_size > native_runtime.STABLE_RUNTIME_MANIFEST_MAX_BYTES
            or (
                not native_runtime._is_windows_host()
                and (metadata.st_uid != os.getuid() or metadata.st_mode & 0o077)
            )
        ):
            raise native_runtime.NativeRuntimeError("stable native runtime manifest is unsafe")
        native_runtime._require_windows_private_runtime_acl(path)
        raw = os.read(descriptor, native_runtime.STABLE_RUNTIME_MANIFEST_MAX_BYTES + 1)
        final_metadata = os.fstat(descriptor)
        if (
            len(raw) != metadata.st_size
            or final_metadata.st_size != metadata.st_size
            or final_metadata.st_mtime_ns != metadata.st_mtime_ns
            or final_metadata.st_ctime_ns != metadata.st_ctime_ns
        ):
            raise native_runtime.NativeRuntimeError(
                "stable native runtime manifest changed while reading"
            )
        return native_runtime._strict_stable_runtime_manifest(raw)
    except native_runtime.NativeRuntimeError:
        raise
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "stable native runtime manifest is unavailable"
        ) from exc
    finally:
        if descriptor >= 0:
            os.close(descriptor)


def _write_stable_runtime_manifest(
    path: Path,
    value: Mapping[str, object],
    *,
    before_replace: Callable[[], None] | None = None,
) -> None:
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    if len(raw) > native_runtime.STABLE_RUNTIME_MANIFEST_MAX_BYTES:
        raise native_runtime.NativeRuntimeError("stable native runtime manifest is oversized")
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    descriptor = -1
    try:
        descriptor = os.open(
            temporary,
            os.O_WRONLY
            | os.O_CREAT
            | os.O_EXCL
            | getattr(os, "O_BINARY", 0)
            | getattr(os, "O_CLOEXEC", 0)
            | getattr(os, "O_NOFOLLOW", 0),
            0o600,
        )
        offset = 0
        while offset < len(raw):
            written = os.write(descriptor, raw[offset:])
            if written <= 0:
                raise native_runtime.NativeRuntimeError(
                    "stable native runtime manifest write was incomplete"
                )
            offset += written
        os.fsync(descriptor)
        os.close(descriptor)
        descriptor = -1
        if before_replace is not None:
            before_replace()
        os.replace(temporary, path)
        native_runtime._fsync_stable_runtime_directory(path.parent)
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "stable native runtime manifest is unavailable"
        ) from exc
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def _fsync_stable_runtime_directory(path: Path) -> None:
    if os.name == "nt":
        return
    descriptor = -1
    try:
        descriptor = os.open(
            path,
            os.O_RDONLY
            | getattr(os, "O_DIRECTORY", 0)
            | getattr(os, "O_CLOEXEC", 0)
            | getattr(os, "O_NOFOLLOW", 0),
        )
        os.fsync(descriptor)
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "stable native runtime directory sync failed"
        ) from exc
    finally:
        if descriptor >= 0:
            os.close(descriptor)


def _fsync_stable_runtime_payload(root: Path) -> None:
    """Flush every copied regular payload file before publishing a generation."""

    entries = 0
    directories: list[Path] = []
    try:
        for directory, children, files in os.walk(root, followlinks=False):
            current = Path(directory)
            directories.append(current)
            children[:] = [child for child in children if not (current / child).is_symlink()]
            for name in files:
                path = current / name
                if path.is_symlink():
                    continue
                entries += 1
                if entries > native_runtime.MAXIMUM_STABLE_RUNTIME_ENTRIES:
                    raise native_runtime.NativeRuntimeError(
                        "stable native runtime payload is oversized"
                    )
                descriptor = os.open(
                    path,
                    (os.O_RDWR if native_runtime._is_windows_host() else os.O_RDONLY)
                    | getattr(os, "O_BINARY", 0)
                    | getattr(os, "O_CLOEXEC", 0)
                    | getattr(os, "O_NOFOLLOW", 0),
                )
                try:
                    if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                        raise native_runtime.NativeRuntimeError(
                            "stable native runtime payload is unsafe"
                        )
                    os.fsync(descriptor)
                finally:
                    os.close(descriptor)
        for directory in reversed(directories):
            native_runtime._fsync_stable_runtime_directory(directory)
    except native_runtime.NativeRuntimeError:
        raise
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "stable native runtime payload sync failed"
        ) from exc


def _stable_generation_name(spec: native_runtime.PlatformRuntimeSpec, artifact_sha256: str) -> str:
    if native_runtime.SHA256_HEX_PATTERN.fullmatch(artifact_sha256) is None:
        raise native_runtime.NativeRuntimeError(
            "stable native runtime artifact identity is unavailable"
        )
    return f"{spec.platform_key}-{artifact_sha256}"


def _windows_third_party_licenses_sha256(
    artifact_path: Path, *, expected_files: Mapping[str, object] | None = None
) -> str | None:
    """Bind the portable sibling notices, rejecting links and special files."""

    root = artifact_path.parent / "THIRD_PARTY_LICENSES"
    try:
        root.lstat()
    except FileNotFoundError as exc:
        # Older published plugins and retained generations predate the bundle.
        if expected_files is not None:
            raise native_runtime.NativeRuntimeError(
                "native third-party licenses are unavailable"
            ) from exc
        return None
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "native third-party licenses are unavailable"
        ) from exc
    entries: list[tuple[str, str, str]] = []
    pending = [root]
    reparse_point = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    try:
        while pending:
            directory = pending.pop()
            metadata = directory.lstat()
            if (
                directory.is_symlink()
                or directory.resolve(strict=True) != directory
                or not stat.S_ISDIR(metadata.st_mode)
                or (reparse_point and getattr(metadata, "st_file_attributes", 0) & reparse_point)
            ):
                raise native_runtime.NativeRuntimeError("native third-party licenses are unsafe")
            for child in directory.iterdir():
                metadata = child.lstat()
                if child.is_symlink() or (
                    reparse_point and getattr(metadata, "st_file_attributes", 0) & reparse_point
                ):
                    raise native_runtime.NativeRuntimeError(
                        "native third-party licenses are unsafe"
                    )
                relative = child.relative_to(root).as_posix()
                if stat.S_ISDIR(metadata.st_mode):
                    pending.append(child)
                    entries.append((relative, "directory", ""))
                elif stat.S_ISREG(metadata.st_mode):
                    entries.append((relative, "file", native_runtime.sha256_regular_file(child)))
                else:
                    raise native_runtime.NativeRuntimeError(
                        "native third-party licenses are unsafe"
                    )
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "native third-party licenses are unavailable"
        ) from exc
    if not any(kind == "file" for _, kind, _ in entries):
        raise native_runtime.NativeRuntimeError("native third-party licenses are empty")
    if (
        expected_files is not None
        and {relative: digest for relative, kind, digest in entries if kind == "file"}
        != expected_files
    ):
        raise native_runtime.NativeRuntimeError(
            "native third-party licenses do not match distribution"
        )
    return hashlib.sha256(
        json.dumps(sorted(entries), ensure_ascii=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def _windows_license_source_artifact(
    artifact_path: Path, spec: native_runtime.PlatformRuntimeSpec
) -> Path:
    if native_runtime.uses_production_windows_bundle(artifact_path):
        return artifact_path.parent / "native" / spec.platform_key / spec.artifact_name
    return artifact_path


def _windows_source_licenses_sha256(
    artifact_path: Path, spec: native_runtime.PlatformRuntimeSpec
) -> str | None:
    expected_files = None
    if native_runtime.uses_production_windows_bundle(artifact_path):
        descriptor = native_runtime._read_strict_local_json(
            artifact_path.parent / native_runtime.WINDOWS_PRODUCTION_BUNDLE_RELATIVE_PATH,
            maximum_bytes=native_runtime.MAXIMUM_MANIFEST_BYTES,
            label="plugin-bundled Windows distribution",
        )
        platforms = descriptor.get("platforms")
        entry = platforms.get(spec.platform_key) if is_json(platforms) else None
        if is_json(entry) and "thirdPartyLicenses" in entry:
            expected_files = entry["thirdPartyLicenses"]
            if not is_json(expected_files) or not expected_files:
                raise native_runtime.NativeRuntimeError(
                    "native third-party license manifest is malformed"
                )
    return _windows_third_party_licenses_sha256(
        _windows_license_source_artifact(artifact_path, spec), expected_files=expected_files
    )


def _windows_generation_sha256(executable_sha256: str, licenses_sha256: str | None) -> str:
    if licenses_sha256 is None:
        return executable_sha256
    return hashlib.sha256(
        f"windows-runtime-with-licenses-v1\n{executable_sha256}\n{licenses_sha256}\n".encode(
            "ascii"
        )
    ).hexdigest()


def _validated_windows_signing_policy(
    value: object,
    *,
    allow_production_unsigned: bool = False,
) -> WindowsSigningPolicy:
    if not is_json(value):
        raise native_runtime.NativeRuntimeError("stable native runtime signing policy is malformed")
    kind = value.get("kind")
    if kind == "unsigned-test":
        if set(value) != {"kind"} or not (
            allow_production_unsigned or native_runtime.allow_unsigned_test_app()
        ):
            raise native_runtime.NativeRuntimeError(
                "stable native runtime signing policy is malformed"
            )
        unsigned_policy: UnsignedTestSigningPolicy = {"kind": "unsigned-test"}
        return unsigned_policy
    subject = value.get("subject")
    thumbprint = value.get("thumbprint")
    if (
        set(value) != {"kind", "subject", "thumbprint"}
        or kind != "authenticode"
        or not isinstance(subject, str)
        or not isinstance(thumbprint, str)
        or not native_runtime._valid_authenticode_identity(subject, thumbprint)
    ):
        raise native_runtime.NativeRuntimeError("stable native runtime signing policy is malformed")
    authenticode_policy: AuthenticodeSigningPolicy = {
        "kind": "authenticode",
        "subject": subject,
        "thumbprint": thumbprint,
    }
    return authenticode_policy


def _validated_stable_windows_distribution_binding(
    value: object,
) -> WindowsDistributionBinding:
    if not is_json(value) or set(value) != {
        "kind",
        "release",
        "storage",
        "lock",
        "descriptor",
        "composite",
    }:
        raise native_runtime.NativeRuntimeError(
            "stable native runtime distribution binding is malformed"
        )
    release = value.get("release")
    storage = value.get("storage")
    if not is_json(release) or not is_json(storage):
        raise native_runtime.NativeRuntimeError(
            "stable native runtime distribution binding is malformed"
        )
    tag = release.get("tag")
    tag_sha = release.get("tagSha")
    version = release.get("version")
    if (
        value.get("kind") != "chatgpt-meetings-windows-production-bundle"
        or set(release) != {"tag", "tagSha", "version"}
        or not isinstance(tag, str)
        or not tag.startswith("chatgpt-meetings-v")
        or tag.lower() == "latest"
        or not isinstance(tag_sha, str)
        or re.fullmatch(r"[a-f0-9]{40}", tag_sha) is None
        or not isinstance(version, str)
        or not version
        or tag != f"chatgpt-meetings-v{version}"
        or set(storage) != {"provider", "accountName", "containerName"}
        or storage.get("provider") != "azure-blob"
        or storage.get("accountName") != native_runtime.WINDOWS_PRODUCTION_AZURE_ACCOUNT_NAME
        or storage.get("containerName") != native_runtime.WINDOWS_PRODUCTION_AZURE_CONTAINER_NAME
    ):
        raise native_runtime.NativeRuntimeError(
            "stable native runtime distribution binding is malformed"
        )
    artifacts: dict[str, WindowsDistributionArtifact] = {}
    for key in ("lock", "descriptor", "composite"):
        entry = value.get(key)
        if not is_json(entry):
            raise native_runtime.NativeRuntimeError(
                "stable native runtime distribution binding is malformed"
            )
        sha256 = entry.get("sha256")
        size_bytes = entry.get("sizeBytes")
        if (
            set(entry) != {"sha256", "sizeBytes"}
            or not isinstance(sha256, str)
            or native_runtime.SHA256_HEX_PATTERN.fullmatch(sha256) is None
            or type(size_bytes) is not int
            or size_bytes <= 0
            or size_bytes > native_runtime.MAXIMUM_MANIFEST_BYTES
        ):
            raise native_runtime.NativeRuntimeError(
                "stable native runtime distribution binding is malformed"
            )
        artifacts[key] = {"sha256": sha256, "sizeBytes": size_bytes}
    validated_release: WindowsDistributionRelease = {
        "tag": tag,
        "tagSha": tag_sha,
        "version": version,
    }
    validated_storage: WindowsDistributionStorage = {
        "provider": "azure-blob",
        "accountName": native_runtime.WINDOWS_PRODUCTION_AZURE_ACCOUNT_NAME,
        "containerName": native_runtime.WINDOWS_PRODUCTION_AZURE_CONTAINER_NAME,
    }
    return {
        "kind": "chatgpt-meetings-windows-production-bundle",
        "release": validated_release,
        "storage": validated_storage,
        "lock": artifacts["lock"],
        "descriptor": artifacts["descriptor"],
        "composite": artifacts["composite"],
    }


def _validated_windows_runtime_verification(
    value: dict[str, object],
) -> WindowsRuntimeVerification:
    licenses_sha256 = value.get("thirdPartyLicensesSha256")
    licenses_keys = {"thirdPartyLicensesSha256"} if "thirdPartyLicensesSha256" in value else set()
    if licenses_keys and (
        not isinstance(licenses_sha256, str)
        or native_runtime.SHA256_HEX_PATTERN.fullmatch(licenses_sha256) is None
    ):
        raise native_runtime.NativeRuntimeError(
            "stable native runtime license binding is malformed"
        )
    distribution = value.get("windowsDistribution")
    if distribution is None:
        if (
            native_runtime.RUNTIME_CONFIG.flavor == "production"
            or set(value) != {"signing"} | licenses_keys
        ):
            raise native_runtime.NativeRuntimeError(
                "stable native runtime signing policy is malformed"
            )
        validated: WindowsRuntimeVerification = {
            "signing": _validated_windows_signing_policy(value.get("signing"))
        }
    else:
        if set(value) != {"signing", "windowsDistribution"} | licenses_keys:
            raise native_runtime.NativeRuntimeError(
                "stable native runtime signing policy is malformed"
            )
        validated = {
            "signing": _validated_windows_signing_policy(
                value.get("signing"),
                allow_production_unsigned=native_runtime.RUNTIME_CONFIG.flavor == "production",
            ),
            "windowsDistribution": _validated_stable_windows_distribution_binding(distribution),
        }
    if isinstance(licenses_sha256, str):
        validated["thirdPartyLicensesSha256"] = licenses_sha256
    return validated


def _validated_darwin_runtime_verification(
    value: dict[str, object],
) -> DarwinRuntimeVerification:
    artifact_sha256 = value.get("artifactSha256")
    receipt_sha256 = value.get("embeddedReceiptSha256")
    production = native_runtime.RUNTIME_CONFIG.flavor == "production"
    identity_key = "teamIdentifier" if production else "signingAuthority"
    expected_identity = (
        native_runtime.TEAM_IDENTIFIER
        if production
        else native_runtime.DEVELOPMENT_SIGNING_AUTHORITY
    )
    identity = value.get(identity_key)
    if (
        set(value) != {identity_key, "artifactSha256", "embeddedReceiptSha256"}
        or not isinstance(identity, str)
        or identity != expected_identity
        or not isinstance(artifact_sha256, str)
        or native_runtime.SHA256_HEX_PATTERN.fullmatch(artifact_sha256) is None
        or not isinstance(receipt_sha256, str)
        or native_runtime.SHA256_HEX_PATTERN.fullmatch(receipt_sha256) is None
    ):
        raise native_runtime.NativeRuntimeError("stable native runtime signing policy is malformed")
    if production:
        return {
            "teamIdentifier": identity,
            "artifactSha256": artifact_sha256,
            "embeddedReceiptSha256": receipt_sha256,
        }
    return {
        "signingAuthority": native_runtime.DEVELOPMENT_SIGNING_AUTHORITY,
        "artifactSha256": artifact_sha256,
        "embeddedReceiptSha256": receipt_sha256,
    }


def _validated_stable_generation_manifest(
    value: Mapping[str, object],
    spec: native_runtime.PlatformRuntimeSpec,
) -> StableGenerationManifest:
    expected_keys = {
        "schemaVersion",
        "platform",
        "artifactName",
        "generation",
        "version",
        "buildTimestamp",
        "executableSha256",
        "verification",
    }
    executable_sha256 = value.get("executableSha256")
    verification = value.get("verification")
    version = value.get("version")
    build_timestamp = value.get("buildTimestamp")
    if (
        set(value) != expected_keys
        or type(value.get("schemaVersion")) is not int
        or value["schemaVersion"] != native_runtime.STABLE_RUNTIME_SCHEMA_VERSION
        or value.get("platform") != spec.platform_key
        or value.get("artifactName") != spec.artifact_name
        or not isinstance(executable_sha256, str)
        or native_runtime.SHA256_HEX_PATTERN.fullmatch(executable_sha256) is None
        or not isinstance(version, str)
        or not version
        or build_timestamp is not None
        and not isinstance(build_timestamp, str)
        or not is_json(verification)
    ):
        raise native_runtime.NativeRuntimeError("stable native runtime manifest is malformed")
    if native_runtime._is_windows_spec(spec):
        windows_verification = _validated_windows_runtime_verification(verification)
        artifact_sha256 = _windows_generation_sha256(
            executable_sha256, windows_verification.get("thirdPartyLicensesSha256")
        )
        validated_verification: StableRuntimeVerification = windows_verification
    else:
        darwin_verification = _validated_darwin_runtime_verification(verification)
        artifact_sha256 = darwin_verification["artifactSha256"]
        validated_verification = darwin_verification
    if value.get("generation") != native_runtime._stable_generation_name(spec, artifact_sha256):
        raise native_runtime.NativeRuntimeError("stable native runtime manifest is malformed")
    return {
        "schemaVersion": native_runtime.STABLE_RUNTIME_SCHEMA_VERSION,
        "platform": spec.platform_key,
        "artifactName": spec.artifact_name,
        "generation": native_runtime._stable_generation_name(spec, artifact_sha256),
        "version": version,
        "buildTimestamp": build_timestamp,
        "executableSha256": executable_sha256,
        "verification": validated_verification,
    }


def _stable_generation_artifact(
    runtime_root: Path,
    value: Mapping[str, object],
    spec: native_runtime.PlatformRuntimeSpec,
) -> Path:
    manifest = native_runtime._validated_stable_generation_manifest(value, spec)
    generation_root = runtime_root / "versions" / manifest["generation"]
    try:
        metadata = generation_root.lstat()
        resolved_generation = generation_root.resolve(strict=True)
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "stable native runtime generation is unavailable"
        ) from exc
    if (
        generation_root.is_symlink()
        or not stat.S_ISDIR(metadata.st_mode)
        or resolved_generation != generation_root
    ):
        raise native_runtime.NativeRuntimeError("stable native runtime generation is unsafe")
    native_runtime._private_runtime_directory(resolved_generation)
    return native_runtime.plugin_artifact_path(resolved_generation, spec)


def _read_active_stable_generation(
    runtime_root: Path,
    spec: native_runtime.PlatformRuntimeSpec,
) -> tuple[Path, StableGenerationManifest]:
    active = native_runtime._read_stable_runtime_manifest(runtime_root / "active")
    generation = active.get("generation")
    if (
        set(active) != {"schemaVersion", "generation"}
        or type(active.get("schemaVersion")) is not int
        or active["schemaVersion"] != native_runtime.STABLE_RUNTIME_SCHEMA_VERSION
        or not isinstance(generation, str)
        or re.fullmatch(r"[a-z0-9-]+-[a-f0-9]{64}", generation) is None
    ):
        raise native_runtime.NativeRuntimeError("stable native runtime activation is malformed")
    generation_root = runtime_root / "versions" / generation
    decoded_manifest = native_runtime._read_stable_runtime_manifest(
        generation_root / ".runtime.json"
    )
    manifest = native_runtime._validated_stable_generation_manifest(decoded_manifest, spec)
    if manifest["generation"] != generation:
        raise native_runtime.NativeRuntimeError(
            "stable native runtime activation does not match generation"
        )
    artifact = native_runtime._stable_generation_artifact(runtime_root, manifest, spec)
    return artifact, manifest


def stable_runtime_verification_manifest(
    artifact_path: Path,
    spec: native_runtime.PlatformRuntimeSpec,
    *,
    require_active: bool = False,
) -> StableRuntimeVerification:
    """Return the validated signing policy for one exact stable generation."""

    runtime_root = stable_runtime_artifact_root(artifact_path)
    try:
        resolved_artifact = artifact_path.resolve(strict=True)
        relative = resolved_artifact.relative_to(runtime_root / "versions")
    except (OSError, ValueError) as exc:
        raise native_runtime.NativeRuntimeError(
            "stable native runtime artifact is unavailable"
        ) from exc
    if (
        artifact_path.is_symlink()
        or len(relative.parts) != 2
        or relative.parts[1] != spec.artifact_name
        or re.fullmatch(r"[a-z0-9-]+-[a-f0-9]{64}", relative.parts[0]) is None
    ):
        raise native_runtime.NativeRuntimeError("stable native runtime artifact is unsafe")
    generation_root = runtime_root / "versions" / relative.parts[0]
    decoded_manifest = native_runtime._read_stable_runtime_manifest(
        generation_root / ".runtime.json"
    )
    manifest = native_runtime._validated_stable_generation_manifest(decoded_manifest, spec)
    expected_artifact = native_runtime._stable_generation_artifact(runtime_root, manifest, spec)
    if expected_artifact != resolved_artifact:
        raise native_runtime.NativeRuntimeError(
            "stable native runtime artifact does not match generation"
        )
    executable = native_runtime._plugin_executable_path(expected_artifact, spec)
    if native_runtime.sha256_regular_file(executable) != manifest["executableSha256"]:
        raise native_runtime.NativeRuntimeError(
            "stable native runtime executable does not match generation"
        )
    native_runtime._require_stable_artifact_receipt(expected_artifact, manifest, spec)
    if require_active:
        active_artifact, active_manifest = native_runtime._read_active_stable_generation(
            runtime_root, spec
        )
        if active_artifact != expected_artifact or active_manifest != manifest:
            raise native_runtime.NativeRuntimeError("stable native runtime artifact is not active")
    return manifest["verification"]


def _require_stable_artifact_receipt(
    artifact_path: Path,
    manifest: StableGenerationManifest,
    spec: native_runtime.PlatformRuntimeSpec,
) -> None:
    if native_runtime._is_windows_spec(spec):
        licenses_sha256 = manifest["verification"].get("thirdPartyLicensesSha256")
        if licenses_sha256 is not None and (
            _windows_third_party_licenses_sha256(artifact_path) != licenses_sha256
        ):
            raise native_runtime.NativeRuntimeError(
                "stable native runtime licenses do not match generation"
            )
        return
    receipt_sha256 = manifest["verification"].get("embeddedReceiptSha256")
    receipt = native_runtime._native_build_receipt_path(artifact_path)
    try:
        metadata = receipt.lstat()
        resolved = receipt.resolve(strict=True)
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "stable native runtime receipt is unavailable"
        ) from exc
    if (
        receipt.is_symlink()
        or resolved != receipt
        or not stat.S_ISREG(metadata.st_mode)
        or not isinstance(receipt_sha256, str)
        or native_runtime.sha256_regular_file(receipt) != receipt_sha256
    ):
        raise native_runtime.NativeRuntimeError(
            "stable native runtime receipt does not match generation"
        )


def _stable_source_verification_manifest(
    plugin_root: Path,
    artifact_path: Path,
    spec: native_runtime.PlatformRuntimeSpec,
) -> StableRuntimeVerification:
    """Carry only source-validated signing policy into an immutable copy."""

    if native_runtime._is_windows_spec(spec):
        windows_verification = native_runtime._windows_plugin_verification_manifest(
            artifact_path, spec
        )
        licenses_sha256 = _windows_source_licenses_sha256(artifact_path, spec)
        if licenses_sha256 is not None:
            windows_verification["thirdPartyLicensesSha256"] = licenses_sha256
        return windows_verification
    if native_runtime.RUNTIME_CONFIG.flavor != "production":
        receipt_path = native_runtime._native_build_receipt_path(artifact_path)
        receipt = native_runtime._read_strict_local_json(
            receipt_path,
            maximum_bytes=native_runtime.MAXIMUM_MANIFEST_BYTES,
            label="development native build receipt",
        )
        artifact_sha256 = receipt.get("bundle_payload_sha256")
        if (
            receipt.get("variant") != "dev"
            or receipt.get("signing_mode") != "stable-local"
            or receipt.get("bundle_identifier") != native_runtime.BUNDLE_ID
            or not isinstance(artifact_sha256, str)
            or native_runtime.SHA256_HEX_PATTERN.fullmatch(artifact_sha256) is None
        ):
            raise native_runtime.NativeRuntimeError("development native build receipt is malformed")
        return {
            "signingAuthority": native_runtime.DEVELOPMENT_SIGNING_AUTHORITY,
            "artifactSha256": artifact_sha256,
            "embeddedReceiptSha256": native_runtime.sha256_regular_file(receipt_path),
        }
    verification = native_runtime._verified_cam_distribution_manifest(
        plugin_root,
        artifact_path,
        include_native_identity=True,
    )
    artifact_sha256 = verification.get("artifactSha256")
    receipt_sha256 = verification.get("embeddedReceiptSha256")
    team_identifier = verification.get("teamIdentifier")
    if (
        not isinstance(team_identifier, str)
        or team_identifier != native_runtime.TEAM_IDENTIFIER
        or not isinstance(artifact_sha256, str)
        or not isinstance(receipt_sha256, str)
    ):
        raise native_runtime.NativeRuntimeError("stable native runtime signing policy is malformed")
    return {
        "teamIdentifier": team_identifier,
        "artifactSha256": artifact_sha256,
        "embeddedReceiptSha256": receipt_sha256,
    }


def _verified_stable_artifact_metadata(
    artifact_path: Path,
    manifest: StableGenerationManifest,
    spec: native_runtime.PlatformRuntimeSpec,
    *,
    force_verify: bool,
) -> tuple[NativeArtifactFingerprint, str, str | None, str]:
    """Verify a selected copy without applying source-path-bound provenance."""

    cache_key = native_runtime._plugin_verification_cache_key(artifact_path, spec)
    if native_runtime._is_windows_spec(spec):
        # The executable/receipt sentinel does not observe sibling notice edits.
        native_runtime._require_stable_artifact_receipt(artifact_path, manifest, spec)
    with native_runtime._PLUGIN_BUNDLE_VERIFICATION_LOCK:
        cached = native_runtime._PLUGIN_BUNDLE_VERIFICATION_CACHE.get(cache_key)
        sentinel = native_runtime._stable_artifact_status_sentinel(artifact_path, spec)
        if not force_verify and cached is not None and cached.stable_status_sentinel == sentinel:
            return (
                cached.fingerprint,
                cached.version,
                cached.build_timestamp,
                cached.executable_sha256,
            )
        fingerprint, version, build_timestamp = native_runtime._plugin_bundle_fingerprint(
            artifact_path, spec
        )
        executable = native_runtime._plugin_executable_path(artifact_path, spec)
        executable_sha256 = native_runtime.sha256_regular_file(executable)
        expected_digest = manifest["executableSha256"]
        if executable_sha256 != expected_digest:
            raise native_runtime.NativeRuntimeError(
                "stable native runtime executable does not match generation"
            )
        native_runtime._require_stable_artifact_receipt(artifact_path, manifest, spec)
        native_runtime.validate_app(artifact_path, manifest["verification"], spec)
        verified_fingerprint, verified_version, verified_timestamp = (
            native_runtime._plugin_bundle_fingerprint(
                artifact_path,
                spec,
            )
        )
        verified_digest = native_runtime.sha256_regular_file(executable)
        native_runtime._require_stable_artifact_receipt(artifact_path, manifest, spec)
        if verified_fingerprint != fingerprint or verified_digest != executable_sha256:
            raise native_runtime.NativeRuntimeError(
                "stable native runtime changed during signature verification"
            )
        native_runtime._PLUGIN_BUNDLE_VERIFICATION_CACHE[cache_key] = (
            native_runtime._PluginBundleVerification(
                fingerprint=verified_fingerprint,
                version=manifest["version"] or verified_version or version,
                build_timestamp=manifest["buildTimestamp"] or verified_timestamp or build_timestamp,
                executable_sha256=verified_digest,
                stable_status_sentinel=native_runtime._stable_artifact_status_sentinel(
                    artifact_path, spec
                ),
            )
        )
    return (
        verified_fingerprint,
        manifest["version"] or verified_version or version,
        manifest["buildTimestamp"] or verified_timestamp or build_timestamp,
        verified_digest,
    )


def _activate_stable_generation(
    runtime_root: Path,
    manifest: StableGenerationManifest,
    *,
    authorize_activation: Callable[[StableGenerationManifest], None],
    revalidate_family_lock: Callable[[], None],
) -> None:
    """Publish one already-verified generation behind the final source fence."""

    def revalidate_activation() -> None:
        revalidate_family_lock()
        authorize_activation(manifest)

    native_runtime._write_stable_runtime_manifest(
        runtime_root / "active",
        {
            "schemaVersion": native_runtime.STABLE_RUNTIME_SCHEMA_VERSION,
            "generation": manifest["generation"],
        },
        before_replace=revalidate_activation,
    )


def _remove_stable_runtime_directory(
    path: Path,
    spec: native_runtime.PlatformRuntimeSpec,
    *,
    generation: str,
    error_kind: str,
    revalidate_family_lock: Callable[[], None] | None = None,
) -> bool:
    """Best-effort remove one verified private runtime directory."""

    try:
        native_runtime._private_runtime_directory(path, create=False)
    except (OSError, RuntimeError):
        native_runtime.log_native_runtime_event(
            "cleanup",
            "failed",
            platform=spec.platform_key,
            generation=generation,
            error_kind=error_kind,
        )
        return False

    if revalidate_family_lock is not None:
        revalidate_family_lock()

    try:
        shutil.rmtree(path)
    except OSError:
        native_runtime.log_native_runtime_event(
            "cleanup",
            "failed",
            platform=spec.platform_key,
            generation=generation,
            error_kind=error_kind,
        )
        return False
    return True


def cleanup_unused_plugin_artifacts(
    plugin_root: Path,
    spec: native_runtime.PlatformRuntimeSpec,
    *,
    revalidate_family_lock: Callable[[], None],
) -> None:
    """Reclaim the other OS's payload after the host generation is verified."""

    host = native_runtime.host_platform_key()
    if native_runtime.RUNTIME_CONFIG.flavor != "production" or host is None:
        return
    windows = native_runtime._is_windows_spec(spec)
    if windows != native_runtime._is_windows_spec(native_runtime.runtime_spec_for(host)):
        return
    relative_paths = (
        (native_runtime.APP_NAME, "ChatGPT Meetings.dmg", "THIRD_PARTY_LICENSES")
        if windows
        else (
            "ChatGPT Meetings.exe",
            "THIRD_PARTY_LICENSES_WINDOWS",
            "native/windows-x64",
            "native/windows-arm64",
        )
    )
    removed = False
    for relative in relative_paths:
        try:
            family = native_runtime.plugin_cache_family_root(plugin_root)
            if family is None:
                return
            native_runtime.require_canonical_plugin_registration(plugin_root, family)
            if plugin_root.is_symlink():
                return
            # Keep the lexical cache path so removal can reject a substituted
            # ancestor instead of normalizing its link to an outside directory.
            root = Path(os.path.abspath(plugin_root))
            candidate = root / relative
            # Capture the validated parent identity; removal pins that parent
            # and keeps all mutations relative to opened directory handles.
            _private_runtime_directory(root, owner_only=False, create=False)
            if candidate.parent != root:
                _private_runtime_directory(candidate.parent, owner_only=False, create=False)
            parent_metadata = candidate.parent.stat()
            metadata = candidate.lstat()
            if stat.S_ISLNK(metadata.st_mode) or getattr(metadata, "st_file_attributes", 0) & 0x400:
                continue
            if not (stat.S_ISDIR(metadata.st_mode) or stat.S_ISREG(metadata.st_mode)):
                continue
        except FileNotFoundError:
            continue
        except (OSError, RuntimeError):
            native_runtime.log_native_runtime_event(
                "cleanup", "failed", platform=spec.platform_key, error_kind="unused_platform"
            )
            continue
        revalidate_family_lock()
        try:
            _remove_unused_plugin_payload(
                candidate, (parent_metadata.st_dev, parent_metadata.st_ino)
            )
            removed = True
        except (OSError, RuntimeError):
            native_runtime.log_native_runtime_event(
                "cleanup", "failed", platform=spec.platform_key, error_kind="unused_platform"
            )
    if removed:
        native_runtime.log_native_runtime_event(
            "cleanup", "completed", platform=spec.platform_key, reason="unused_platform"
        )


def _remove_unused_plugin_payload(path: Path, parent_identity: tuple[int, int]) -> None:
    """Bind removal to the inspected parent, including on Python 3.10."""

    if os.name == "nt":
        from windows_private_runtime import remove_cache_payload

        remove_cache_payload(path, parent_identity)
        return
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    parent_fd = os.open(path.anchor, flags)
    try:
        # Pin each lexical component without following links. A path-based
        # identity captured after validation cannot authorize a new ancestor.
        for component in path.parent.parts[1:]:
            child_fd = os.open(component, flags, dir_fd=parent_fd)
            os.close(parent_fd)
            parent_fd = child_fd
        parent = os.fstat(parent_fd)
        if (parent.st_dev, parent.st_ino) != parent_identity:
            raise native_runtime.NativeRuntimeError("plugin cleanup parent changed")
        payload = os.stat(path.name, dir_fd=parent_fd, follow_symlinks=False)
        if stat.S_ISDIR(payload.st_mode):
            payload_fd = os.open(
                path.name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=parent_fd
            )
            try:
                if not os.path.samestat(payload, os.fstat(payload_fd)):
                    raise native_runtime.NativeRuntimeError("plugin cleanup payload changed")
                # Walk the inspected object, even if its name is replaced after
                # opening. Descendant mutations stay relative to pinned handles.
                for _, directories, files, directory_fd in os.fwalk(
                    ".", topdown=False, follow_symlinks=False, dir_fd=payload_fd
                ):
                    for name in files:
                        os.unlink(name, dir_fd=directory_fd)
                    for name in directories:
                        try:
                            os.rmdir(name, dir_fd=directory_fd)
                        except NotADirectoryError:
                            os.unlink(name, dir_fd=directory_fd)
                current = os.stat(path.name, dir_fd=parent_fd, follow_symlinks=False)
                if not os.path.samestat(payload, current):
                    raise native_runtime.NativeRuntimeError("plugin cleanup payload changed")
                os.rmdir(path.name, dir_fd=parent_fd)
            finally:
                os.close(payload_fd)
        elif stat.S_ISREG(payload.st_mode):
            os.unlink(path.name, dir_fd=parent_fd)
    finally:
        os.close(parent_fd)


def _cleanup_stable_runtime_manifest_temporaries(
    runtime_root: Path,
    spec: native_runtime.PlatformRuntimeSpec,
    *,
    generation: str,
    revalidate_family_lock: Callable[[], None],
) -> None:
    """Best-effort remove private activation-manifest residue under its family lock."""

    def log_failure() -> None:
        native_runtime.log_native_runtime_event(
            "cleanup",
            "failed",
            platform=spec.platform_key,
            generation=generation,
            error_kind="manifest",
        )

    try:
        candidates = [
            entry
            for entry in runtime_root.iterdir()
            if re.fullmatch(r"\.active\.[a-f0-9]{32}\.tmp", entry.name) is not None
        ]
    except (OSError, RuntimeError):
        log_failure()
        return

    removed = False
    reparse_point = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    for candidate in candidates:
        try:
            metadata = candidate.lstat()
            if (
                candidate.is_symlink()
                or not stat.S_ISREG(metadata.st_mode)
                or (reparse_point and getattr(metadata, "st_file_attributes", 0) & reparse_point)
                or (
                    not native_runtime._is_windows_host()
                    and (metadata.st_uid != os.getuid() or metadata.st_mode & 0o077)
                )
            ):
                raise native_runtime.NativeRuntimeError(
                    "stable native runtime manifest temporary is unsafe"
                )
            native_runtime._require_windows_private_runtime_acl(candidate)
        except (OSError, RuntimeError):
            log_failure()
            continue

        revalidate_family_lock()
        try:
            candidate.unlink()
        except OSError:
            log_failure()
            continue
        removed = True

    if removed:
        native_runtime.log_native_runtime_event(
            "cleanup",
            "completed",
            platform=spec.platform_key,
            generation=generation,
            reason="manifest",
        )


def _protect_live_stable_runtime_generation(
    runtime_root: Path,
    spec: native_runtime.PlatformRuntimeSpec,
    *,
    generation: str,
    protected_generations: set[str],
) -> bool:
    """Protect a proven live owner even when activation already selected its successor."""

    # control_client imports native_runtime, so resolve this reverse edge only
    # after materialization has completed and pruning is actually necessary.
    import control_client

    try:
        if not control_client.descriptor_may_have_live_owner():
            if control_client._owner_lock_state() in {"missing", "available"}:
                return True
            raise control_client.ControlUnavailable("native owner lease is held")

        control_root = control_client.control_root()
        control_client.require_private(control_root, directory=True)
        discovered = control_client._discover_control_transport(control_root)
        if not isinstance(discovered, control_client.StreamDiscovery):
            raise control_client.ControlUnavailable("native control stream owner is unavailable")
        descriptor = discovered.descriptor
        if descriptor["platform"] != spec.platform_key:
            raise control_client.ControlUnavailable("native owner platform does not match")
        if (
            not native_runtime._is_windows_spec(spec)
            and descriptor.get("bundleIdentifier") != control_client.BUNDLE_ID
        ):
            raise control_client.ControlUnavailable("native owner bundle identity does not match")
        control_client.require_stream_owner(
            control_root,
            descriptor,
            peer_pid=descriptor["pid"],
        )

        owner_path = descriptor.get("bundlePath")
        if not isinstance(owner_path, str):
            raise control_client.ControlUnavailable("native owner artifact is unavailable")
        owner_artifact = Path(owner_path).resolve(strict=True)
        relative = owner_artifact.relative_to(runtime_root / "versions")
        if (
            len(relative.parts) != 2
            or relative.parts[1] != spec.artifact_name
            or re.fullmatch(r"[a-z0-9-]+-[a-f0-9]{64}", relative.parts[0]) is None
        ):
            raise control_client.ControlUnavailable("native owner generation is unavailable")

        native_runtime.stable_runtime_verification_manifest(
            owner_artifact,
            spec,
            require_active=False,
        )
        owner_executable = control_client.resolved_path(
            descriptor.get("executablePath"),
            message="native owner executable is unavailable",
        )
        if owner_executable != control_client.expected_executable_path(owner_artifact, spec):
            raise control_client.ControlUnavailable("native owner executable does not match")
        control_client.require_stream_owner(
            control_root,
            descriptor,
            peer_pid=descriptor["pid"],
        )
        protected_generations.add(relative.parts[0])
        return True
    except (control_client.ControlUnavailable, OSError, RuntimeError, ValueError):
        native_runtime.log_native_runtime_event(
            "cleanup",
            "failed",
            platform=spec.platform_key,
            generation=generation,
            error_kind="owner",
        )
        return False


def _cleanup_stable_runtime_generations(
    runtime_root: Path,
    spec: native_runtime.PlatformRuntimeSpec,
    *,
    generation: str,
    protected_generations: set[str],
    prune_generations: bool,
    revalidate_family_lock: Callable[[], None],
) -> None:
    """Bound abandoned stages and verified generations while their lock is held."""

    _cleanup_stable_runtime_manifest_temporaries(
        runtime_root,
        spec,
        generation=generation,
        revalidate_family_lock=revalidate_family_lock,
    )

    versions_root = runtime_root / "versions"
    try:
        entries = list(versions_root.iterdir())
    except OSError:
        native_runtime.log_native_runtime_event(
            "cleanup",
            "failed",
            platform=spec.platform_key,
            generation=generation,
            error_kind="enumeration",
        )
        return

    removed_stages = False
    generations: list[tuple[int, str, Path]] = []
    for candidate in entries:
        if re.fullmatch(r"\.stage-[a-f0-9]{32}", candidate.name) is not None:
            removed_stages = (
                _remove_stable_runtime_directory(
                    candidate,
                    spec,
                    generation=generation,
                    error_kind="staging",
                    revalidate_family_lock=revalidate_family_lock,
                )
                or removed_stages
            )
            continue

        if (
            not prune_generations
            or re.fullmatch(r"[a-z0-9-]+-[a-f0-9]{64}", candidate.name) is None
        ):
            continue
        try:
            native_runtime._private_runtime_directory(candidate, create=False)
            metadata = candidate.lstat()
        except (OSError, RuntimeError):
            native_runtime.log_native_runtime_event(
                "cleanup",
                "failed",
                platform=spec.platform_key,
                generation=generation,
                error_kind="generation",
            )
            continue
        generations.append((metadata.st_mtime_ns, candidate.name, candidate))

    if len(generations) > 2 and not _protect_live_stable_runtime_generation(
        runtime_root,
        spec,
        generation=generation,
        protected_generations=protected_generations,
    ):
        return

    removed_generations = False
    retained_generations = set(protected_generations)
    for _modified_ns, candidate_generation, candidate in sorted(generations, reverse=True):
        if candidate_generation in retained_generations:
            continue
        if len(retained_generations) < 2:
            retained_generations.add(candidate_generation)
            continue
        removed_generations = (
            _remove_stable_runtime_directory(
                candidate,
                spec,
                generation=generation,
                error_kind="generation",
                revalidate_family_lock=revalidate_family_lock,
            )
            or removed_generations
        )

    if removed_stages or removed_generations:
        native_runtime.log_native_runtime_event(
            "cleanup",
            "completed",
            platform=spec.platform_key,
            generation=generation,
            reason="generation" if removed_generations else "staging",
        )


def _materialize_verification_failure_reason(error: BaseException) -> str:
    if isinstance(error, OSError):
        return "permissions" if isinstance(error, PermissionError) else "io_error"
    if len(error.args) != 1 or type(error.args[0]) is not str:
        return "verification_failed"
    reason = {
        "stable native runtime permissions are unsafe": "permissions",
        "stable native runtime generation manifest does not match": "generation_manifest",
        "stable native runtime executable does not match generation": "artifact_digest",
        "native executable signing policy is missing or malformed": "unsigned_validation",
        "native app signature verification failed": "signature",
        "native executable signature verification failed": "signature",
    }.get(error.args[0])
    if reason is not None:
        return reason

    reason = "verification_failed"
    cause = error.__cause__
    observed = {id(error)}
    for _ in range(3):
        if cause is None or id(cause) in observed:
            break
        observed.add(id(cause))
        if isinstance(cause, PermissionError):
            return "permissions"
        if isinstance(cause, OSError):
            reason = "io_error"
        cause = cause.__cause__
    return reason


def _reconcile_windows_runtime_composite(
    runtime_root: Path,
    generation_root: Path,
    previous: Mapping[str, object],
    expected: StableGenerationManifest,
    spec: native_runtime.PlatformRuntimeSpec,
    *,
    authorize_activation: Callable[[StableGenerationManifest], None],
    revalidate_family_lock: Callable[[], None],
) -> None:
    """Rebind a verified Windows executable to a republished runtime composite."""

    mismatch = "stable native runtime generation manifest does not match"
    if (
        not native_runtime._is_windows_spec(spec)
        or native_runtime.RUNTIME_CONFIG.flavor != "production"
    ):
        raise native_runtime.NativeRuntimeError(mismatch)

    try:
        previous_manifest = native_runtime._validated_stable_generation_manifest(previous, spec)
    except native_runtime.NativeRuntimeError as error:
        raise native_runtime.NativeRuntimeError(mismatch) from error

    previous_verification = previous_manifest["verification"]
    expected_verification = expected["verification"]
    previous_distribution = previous_verification.get("windowsDistribution")
    expected_distribution = expected_verification.get("windowsDistribution")
    if not isinstance(previous_distribution, Mapping) or not isinstance(
        expected_distribution, Mapping
    ):
        raise native_runtime.NativeRuntimeError(mismatch)

    normalized = {
        **previous_manifest,
        "verification": {
            **previous_verification,
            "windowsDistribution": {
                **previous_distribution,
                "composite": expected_distribution.get("composite"),
            },
        },
    }
    if normalized != expected:
        raise native_runtime.NativeRuntimeError(mismatch)

    artifact = native_runtime._stable_generation_artifact(runtime_root, previous_manifest, spec)
    if artifact != generation_root / spec.artifact_name:
        raise native_runtime.NativeRuntimeError(mismatch)
    previous_metadata = native_runtime._verified_stable_artifact_metadata(
        artifact,
        previous_manifest,
        spec,
        force_verify=True,
    )
    if previous_metadata[3] != expected["executableSha256"]:
        raise native_runtime.NativeRuntimeError(mismatch)

    receipt_path = generation_root / ".runtime.json"

    def before_replace() -> None:
        revalidate_family_lock()
        if (
            native_runtime._stable_generation_artifact(runtime_root, previous_manifest, spec)
            != artifact
        ):
            raise native_runtime.NativeRuntimeError(
                "stable native runtime generation changed before reconciliation"
            )
        if native_runtime._read_stable_runtime_manifest(receipt_path) != previous_manifest:
            raise native_runtime.NativeRuntimeError(
                "stable native runtime generation changed before reconciliation"
            )
        if native_runtime.sha256_regular_file(artifact) != expected["executableSha256"]:
            raise native_runtime.NativeRuntimeError(
                "stable native runtime executable changed before reconciliation"
            )
        authorize_activation(expected)
        revalidate_family_lock()

    native_runtime._write_stable_runtime_manifest(
        receipt_path,
        expected,
        before_replace=before_replace,
    )
    if native_runtime._read_stable_runtime_manifest(receipt_path) != expected:
        raise native_runtime.NativeRuntimeError(
            "stable native runtime generation changed during reconciliation"
        )
    native_runtime._verified_stable_artifact_metadata(
        artifact,
        expected,
        spec,
        force_verify=True,
    )


def _copy_darwin_runtime_file(source: str, destination: str) -> str:
    """Stream bundle files without fcopyfile propagating macOS quarantine."""

    initial = os.stat(source, follow_symlinks=False)
    if not stat.S_ISREG(initial.st_mode):
        raise shutil.SpecialFileError(f"`{source}` is not a regular file")
    flags = os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW
    with os.fdopen(os.open(source, flags), "rb") as source_file:
        opened = os.fstat(source_file.fileno())
        if not stat.S_ISREG(opened.st_mode) or (opened.st_dev, opened.st_ino) != (
            initial.st_dev,
            initial.st_ino,
        ):
            raise shutil.SpecialFileError(f"`{source}` is not a regular file")
        with open(destination, "wb") as destination_file:
            shutil.copyfileobj(source_file, destination_file)
    shutil.copystat(source, destination)
    return destination


def _materialize_stable_generation(
    runtime_root: Path,
    source_artifact: Path,
    source_status: NativeRuntimeStatus,
    verification: StableRuntimeVerification,
    spec: native_runtime.PlatformRuntimeSpec,
    *,
    force_verify: bool,
    activate: bool,
    authorize_activation: Callable[[StableGenerationManifest], None],
    revalidate_family_lock: Callable[[], None],
) -> tuple[
    Path,
    StableGenerationManifest,
    bool,
    tuple[NativeArtifactFingerprint, str, str | None, str],
]:
    executable_sha256 = source_status.get("_executableSHA256")
    artifact_sha256 = (
        verification.get("artifactSha256")
        if not native_runtime._is_windows_spec(spec)
        else executable_sha256
    )
    version = source_status.get("version")
    build_timestamp = source_status.get("buildTimestamp")
    if (
        not isinstance(executable_sha256, str)
        or native_runtime.SHA256_HEX_PATTERN.fullmatch(executable_sha256) is None
        or not isinstance(artifact_sha256, str)
        or native_runtime.SHA256_HEX_PATTERN.fullmatch(artifact_sha256) is None
        or not isinstance(version, str)
        or not version
        or build_timestamp is not None
        and not isinstance(build_timestamp, str)
    ):
        raise native_runtime.NativeRuntimeError(
            "stable native runtime source identity is unavailable"
        )
    if native_runtime._is_windows_spec(spec):
        licenses_sha256 = verification.get("thirdPartyLicensesSha256")
        if licenses_sha256 is not None and not isinstance(licenses_sha256, str):
            raise native_runtime.NativeRuntimeError(
                "stable native runtime license binding is malformed"
            )
        artifact_sha256 = _windows_generation_sha256(executable_sha256, licenses_sha256)
    generation = native_runtime._stable_generation_name(spec, artifact_sha256)
    generation_root = runtime_root / "versions" / generation
    manifest = native_runtime._validated_stable_generation_manifest(
        {
            "schemaVersion": native_runtime.STABLE_RUNTIME_SCHEMA_VERSION,
            "platform": spec.platform_key,
            "artifactName": spec.artifact_name,
            "generation": generation,
            "version": version,
            "buildTimestamp": build_timestamp,
            "executableSha256": executable_sha256,
            "verification": verification,
        },
        spec,
    )
    published = False
    staged_fingerprint: NativeArtifactFingerprint | None = None
    staged_version: str | None = None
    staged_timestamp: str | None = None
    active_path = runtime_root / "active"
    active_matches = False
    active_targets_generation = False
    protected_generations = {generation}
    active_generation_is_verified = True
    active_artifact: Path | None = None
    active_manifest: StableGenerationManifest | None = None
    materialize_stage = "verify"
    verification_phase = MaterializeVerificationPhase.GENERATION_MANIFEST

    def log_materialize_failure(error: BaseException) -> None:
        native_runtime.log_native_runtime_event(
            "materialize",
            "failed",
            platform=spec.platform_key,
            version=version,
            build_timestamp=build_timestamp,
            generation=generation,
            error_kind=materialize_stage,
            verification_phase=verification_phase.value if materialize_stage == "verify" else None,
            reason=_materialize_verification_failure_reason(error)
            if materialize_stage == "verify"
            else None,
        )

    if active_path.exists() or active_path.is_symlink():
        try:
            active_artifact, active_manifest = native_runtime._read_active_stable_generation(
                runtime_root, spec
            )
            active_targets_generation = active_artifact == generation_root / spec.artifact_name
            active_matches = active_targets_generation and active_manifest == manifest
            protected_generations.add(active_manifest["generation"])
        except native_runtime.NativeRuntimeError:
            # A canonical, fully verified source is the sole authority that
            # may repair an interrupted or malformed activation pointer.
            active_matches = False
            active_generation_is_verified = False

    if (
        not native_runtime._is_windows_spec(spec)
        and native_runtime.RUNTIME_CONFIG.flavor == "production"
        and active_manifest is None
    ):
        active_generation_is_verified = False

    _cleanup_stable_runtime_generations(
        runtime_root,
        spec,
        generation=generation,
        protected_generations=protected_generations,
        prune_generations=False,
        revalidate_family_lock=revalidate_family_lock,
    )

    if not generation_root.exists():
        staging_root = runtime_root / "versions" / f".stage-{uuid.uuid4().hex}"
        materialize_stage = "copy"
        native_runtime.log_native_runtime_event(
            "materialize",
            "started",
            platform=spec.platform_key,
            version=version,
            build_timestamp=build_timestamp,
            generation=generation,
        )
        try:
            staging_root.mkdir(mode=0o700)
            destination = staging_root / spec.artifact_name
            if spec.artifact_path_kind == "directory":
                if native_runtime.sys.platform == "darwin":
                    shutil.copytree(
                        source_artifact,
                        destination,
                        symlinks=True,
                        copy_function=_copy_darwin_runtime_file,
                    )
                else:
                    shutil.copytree(source_artifact, destination, symlinks=True)
            else:
                shutil.copyfile(source_artifact, destination)
                if "thirdPartyLicensesSha256" in verification:
                    shutil.copytree(
                        _windows_license_source_artifact(source_artifact, spec).parent
                        / "THIRD_PARTY_LICENSES",
                        staging_root / "THIRD_PARTY_LICENSES",
                        symlinks=True,
                    )
            staged_artifact = native_runtime.plugin_artifact_path(staging_root, spec)
            if not native_runtime._is_windows_spec(spec):
                native_runtime.restore_plugin_framework_symlinks(staged_artifact)
            staged_executable = native_runtime._plugin_executable_path(staged_artifact, spec)
            if native_runtime.sha256_regular_file(staged_executable) != executable_sha256:
                raise native_runtime.NativeRuntimeError(
                    "stable native runtime copy does not match source"
                )
            native_runtime._require_stable_artifact_receipt(staged_artifact, manifest, spec)
            staged_fingerprint, staged_version, staged_timestamp = (
                native_runtime._plugin_bundle_fingerprint(
                    staged_artifact,
                    spec,
                )
            )
            native_runtime._write_stable_runtime_manifest(staging_root / ".runtime.json", manifest)
            materialize_stage = "durability"
            native_runtime._fsync_stable_runtime_payload(staging_root)
            materialize_stage = "verify"
            verification_phase = MaterializeVerificationPhase.STAGED_SIGNATURE
            native_runtime.validate_app(staged_artifact, verification, spec)
            verification_phase = MaterializeVerificationPhase.STAGED_IDENTITY
            verified_stage_fingerprint, verified_stage_version, verified_stage_timestamp = (
                native_runtime._plugin_bundle_fingerprint(staged_artifact, spec)
            )
            if (
                verified_stage_fingerprint != staged_fingerprint
                or native_runtime.sha256_regular_file(staged_executable) != executable_sha256
            ):
                raise native_runtime.NativeRuntimeError(
                    "stable native runtime changed during signature verification"
                )
            native_runtime._require_stable_artifact_receipt(staged_artifact, manifest, spec)
            staged_fingerprint = verified_stage_fingerprint
            staged_version = verified_stage_version
            staged_timestamp = verified_stage_timestamp
            native_runtime.log_native_runtime_event(
                "materialize",
                "verified",
                platform=spec.platform_key,
                version=version,
                build_timestamp=build_timestamp,
                generation=generation,
            )
            materialize_stage = "publish"
            revalidate_family_lock()
            os.replace(staging_root, generation_root)
            native_runtime._fsync_stable_runtime_directory(generation_root.parent)
            published = True
            native_runtime.log_native_runtime_event(
                "materialize",
                "published",
                platform=spec.platform_key,
                version=version,
                build_timestamp=build_timestamp,
                generation=generation,
            )
        except native_runtime.NativeRuntimeError as exc:
            log_materialize_failure(exc)
            raise
        except OSError as exc:
            log_materialize_failure(exc)
            raise native_runtime.NativeRuntimeError(
                "stable native runtime generation is unavailable"
            ) from exc
        finally:
            if staging_root.exists():
                _remove_stable_runtime_directory(
                    staging_root,
                    spec,
                    generation=generation,
                    error_kind="staging",
                )
    materialize_stage = "verify"
    try:
        if not published:
            existing_manifest = native_runtime._read_stable_runtime_manifest(
                generation_root / ".runtime.json"
            )
            if existing_manifest != manifest:
                _reconcile_windows_runtime_composite(
                    runtime_root,
                    generation_root,
                    existing_manifest,
                    manifest,
                    spec,
                    authorize_activation=authorize_activation,
                    revalidate_family_lock=revalidate_family_lock,
                )
                active_matches = active_targets_generation
        verification_phase = MaterializeVerificationPhase.GENERATION_IDENTITY
        artifact = native_runtime._stable_generation_artifact(runtime_root, manifest, spec)
        if published:
            fingerprint, version, build_timestamp = native_runtime._plugin_bundle_fingerprint(
                artifact, spec
            )
            executable = native_runtime._plugin_executable_path(artifact, spec)
            if (
                staged_fingerprint is None
                or tuple(entry[1:] for entry in fingerprint)
                != tuple(entry[1:] for entry in staged_fingerprint)
                or native_runtime.sha256_regular_file(executable) != executable_sha256
            ):
                raise native_runtime.NativeRuntimeError(
                    "stable native runtime changed while publishing generation"
                )
            native_runtime._require_stable_artifact_receipt(artifact, manifest, spec)
            verified_metadata = (
                fingerprint,
                manifest["version"] or staged_version or version,
                manifest["buildTimestamp"] or staged_timestamp or build_timestamp,
                executable_sha256,
            )
            with native_runtime._PLUGIN_BUNDLE_VERIFICATION_LOCK:
                native_runtime._PLUGIN_BUNDLE_VERIFICATION_CACHE[
                    native_runtime._plugin_verification_cache_key(artifact, spec)
                ] = native_runtime._PluginBundleVerification(
                    fingerprint=verified_metadata[0],
                    version=verified_metadata[1],
                    build_timestamp=verified_metadata[2],
                    executable_sha256=executable_sha256,
                    stable_status_sentinel=native_runtime._stable_artifact_status_sentinel(
                        artifact, spec
                    ),
                )
        else:
            verified_metadata = native_runtime._verified_stable_artifact_metadata(
                artifact,
                manifest,
                spec,
                force_verify=force_verify,
            )
    except native_runtime.NativeRuntimeError as exc:
        log_materialize_failure(exc)
        raise
    except OSError as exc:
        log_materialize_failure(exc)
        raise native_runtime.NativeRuntimeError(
            "stable native runtime generation is unavailable"
        ) from exc
    if activate and not active_matches:
        native_runtime._activate_stable_generation(
            runtime_root,
            manifest,
            authorize_activation=authorize_activation,
            revalidate_family_lock=revalidate_family_lock,
        )
        native_runtime.log_native_runtime_event(
            "activate",
            "completed",
            platform=spec.platform_key,
            version=manifest.get("version"),
            build_timestamp=manifest.get("buildTimestamp"),
            generation=manifest.get("generation"),
        )

    _cleanup_stable_runtime_generations(
        runtime_root,
        spec,
        generation=generation,
        protected_generations=protected_generations,
        prune_generations=active_generation_is_verified,
        revalidate_family_lock=revalidate_family_lock,
    )
    return artifact, manifest, published, verified_metadata


def plugin_cache_family_root(
    plugin_root: Path,
    *,
    allow_missing: bool = False,
) -> Path | None:
    """Return the version-family root for an installed Codex plugin.

    Installed plugins have the narrow shape
    ~/.codex/plugins/cache/<publisher>/<plugin-id>/<version>. Handoff must
    never act on a source checkout or an arbitrary app path, so callers get
    no family root unless that exact cache boundary is present.
    """

    try:
        resolved_plugin = plugin_root.expanduser().resolve(strict=not allow_missing)
    except OSError:
        return None
    configured_codex_home = os.environ.get("CODEX_HOME", "").strip()
    codex_home = (
        Path(configured_codex_home).expanduser()
        if configured_codex_home
        else Path.home() / ".codex"
    )
    cache_root = (codex_home / "plugins" / "cache").resolve()
    try:
        relative = resolved_plugin.relative_to(cache_root)
    except ValueError:
        return None
    if len(relative.parts) != 3:
        return None
    if allow_missing and (
        relative.parts[0] not in native_runtime.OFFICIAL_CACHE_PUBLISHERS
        or relative.parts[1] != native_runtime.RUNTIME_CONFIG.server_name
        or native_runtime.GITHUB_RELEASE_COMPONENT.fullmatch(relative.parts[2]) is None
    ):
        return None
    return resolved_plugin.parent


def _official_cache_directory_creation_ns(metadata: os.stat_result) -> int:
    """Read platform creation time without mistaking macOS inode changes for birth."""

    birthtime_ns = getattr(metadata, "st_birthtime_ns", None)
    if birthtime_ns is not None:
        return birthtime_ns
    birthtime = getattr(metadata, "st_birthtime", None)
    if birthtime is not None:
        return int(birthtime * 1_000_000_000)
    return metadata.st_ctime_ns


def _official_cache_complete_windows_installation(plugin_root: Path) -> bool:
    """Recognize an exact installed Windows plugin without trusting version order."""

    reparse_point = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    plugin_directory = plugin_root / ".codex-plugin"
    native_directory = plugin_root / "native"
    witnesses = (
        plugin_directory / "plugin.json",
        plugin_root / native_runtime.WINDOWS_PRODUCTION_BUNDLE_RELATIVE_PATH,
        plugin_root / native_runtime.VERIFIED_CAM_DISTRIBUTION_RELATIVE_PATH,
    )
    root_metadata = plugin_root.lstat()
    directory_metadata: dict[Path, os.stat_result] = {}
    witness_metadata: dict[Path, os.stat_result] = {}
    try:
        for directory in (plugin_directory, native_directory):
            metadata = directory.lstat()
            if (
                directory.is_symlink()
                or not stat.S_ISDIR(metadata.st_mode)
                or getattr(metadata, "st_file_attributes", 0) & reparse_point
                or directory.resolve(strict=True).parent != plugin_root
            ):
                raise native_runtime.NativeRuntimeError(
                    "ChatGPT Meetings official plugin cache is not canonical"
                )
            directory_metadata[directory] = metadata
        for witness in witnesses:
            metadata = witness.lstat()
            if (
                witness.is_symlink()
                or not stat.S_ISREG(metadata.st_mode)
                or getattr(metadata, "st_file_attributes", 0) & reparse_point
            ):
                raise native_runtime.NativeRuntimeError(
                    "ChatGPT Meetings official plugin cache is not canonical"
                )
            witness_metadata[witness] = metadata
        try:
            (plugin_root / ".installing").lstat()
        except FileNotFoundError:
            pass
        else:
            return False
    except FileNotFoundError:
        return False

    if native_runtime._is_windows_host():
        from control_client import windows_acl_is_private

        for protected in (plugin_root, plugin_directory, native_directory, *witnesses):
            if not windows_acl_is_private(protected, allow_untrusted_read=True):
                raise native_runtime.NativeRuntimeError(
                    "ChatGPT Meetings official plugin cache permissions are unsafe"
                )

    manifest_path = witnesses[0]
    descriptor = -1
    try:
        original = manifest_path.lstat()
        if (
            original.st_size <= 0
            or original.st_size > native_runtime.MAXIMUM_MANIFEST_BYTES
            or (
                not native_runtime._is_windows_host()
                and (original.st_uid != os.getuid() or original.st_mode & 0o022)
            )
        ):
            raise native_runtime.NativeRuntimeError(
                "ChatGPT Meetings installed plugin manifest is unsafe"
            )
        descriptor = os.open(
            manifest_path,
            os.O_RDONLY
            | getattr(os, "O_BINARY", 0)
            | getattr(os, "O_CLOEXEC", 0)
            | getattr(os, "O_NOFOLLOW", 0),
        )
        opened = os.fstat(descriptor)
        current = manifest_path.lstat()
        if (
            not stat.S_ISREG(opened.st_mode)
            or not stat.S_ISREG(current.st_mode)
            or manifest_path.is_symlink()
            or getattr(current, "st_file_attributes", 0) & reparse_point
            or (opened.st_dev, opened.st_ino) != (original.st_dev, original.st_ino)
            or (current.st_dev, current.st_ino) != (original.st_dev, original.st_ino)
            or opened.st_size != original.st_size
        ):
            raise native_runtime.NativeRuntimeError(
                "ChatGPT Meetings installed plugin manifest changed while reading"
            )
        raw = os.read(descriptor, native_runtime.MAXIMUM_MANIFEST_BYTES + 1)
        final = os.fstat(descriptor)
        final_path = manifest_path.lstat()
        if (
            len(raw) != original.st_size
            or final.st_size != original.st_size
            or final.st_mtime_ns != opened.st_mtime_ns
            or final.st_ctime_ns != opened.st_ctime_ns
            or not stat.S_ISREG(final_path.st_mode)
            or manifest_path.is_symlink()
            or getattr(final_path, "st_file_attributes", 0) & reparse_point
            or (final_path.st_dev, final_path.st_ino) != (original.st_dev, original.st_ino)
            or final_path.st_size != original.st_size
        ):
            raise native_runtime.NativeRuntimeError(
                "ChatGPT Meetings installed plugin manifest changed while reading"
            )
        for directory, before in directory_metadata.items():
            after = directory.lstat()
            if (
                directory.is_symlink()
                or not stat.S_ISDIR(after.st_mode)
                or getattr(after, "st_file_attributes", 0) & reparse_point
                or (after.st_dev, after.st_ino) != (before.st_dev, before.st_ino)
                or after.st_ctime_ns != before.st_ctime_ns
                or after.st_mtime_ns != before.st_mtime_ns
                or directory.resolve(strict=True).parent != plugin_root
            ):
                raise native_runtime.NativeRuntimeError(
                    "ChatGPT Meetings official plugin cache changed while reading"
                )
        for witness, before in witness_metadata.items():
            after = witness.lstat()
            if (
                witness.is_symlink()
                or not stat.S_ISREG(after.st_mode)
                or getattr(after, "st_file_attributes", 0) & reparse_point
                or (after.st_dev, after.st_ino) != (before.st_dev, before.st_ino)
                or after.st_size != before.st_size
                or after.st_mtime_ns != before.st_mtime_ns
                or after.st_ctime_ns != before.st_ctime_ns
            ):
                raise native_runtime.NativeRuntimeError(
                    "ChatGPT Meetings official plugin cache changed while reading"
                )
        current_root = plugin_root.lstat()
        if (
            plugin_root.is_symlink()
            or not stat.S_ISDIR(current_root.st_mode)
            or getattr(current_root, "st_file_attributes", 0) & reparse_point
            or (current_root.st_dev, current_root.st_ino)
            != (root_metadata.st_dev, root_metadata.st_ino)
            or current_root.st_ctime_ns != root_metadata.st_ctime_ns
            or current_root.st_mtime_ns != root_metadata.st_mtime_ns
        ):
            raise native_runtime.NativeRuntimeError(
                "ChatGPT Meetings official plugin cache changed while reading"
            )
        try:
            (plugin_root / ".installing").lstat()
        except FileNotFoundError:
            pass
        else:
            raise native_runtime.NativeRuntimeError(
                "ChatGPT Meetings official plugin cache changed while reading"
            )
        manifest = _strict_stable_runtime_manifest(raw)
    finally:
        if descriptor >= 0:
            os.close(descriptor)
    return (
        manifest.get("name") == native_runtime.RUNTIME_CONFIG.server_name
        and manifest.get("version") == plugin_root.name
    )


def _official_cache_fully_pruned_windows_installation(
    plugin_root: Path,
    original_metadata: os.stat_result,
) -> bool:
    """Prove retired plugin identity and native provenance were both removed."""

    if native_runtime._is_windows_host():
        from control_client import windows_acl_is_private

        if not windows_acl_is_private(plugin_root, allow_untrusted_read=True):
            raise native_runtime.NativeRuntimeError(
                "ChatGPT Meetings official plugin cache permissions are unsafe"
            )

    retired_paths = (
        plugin_root / ".codex-plugin",
        plugin_root / "native",
        plugin_root / ".installing",
    )
    for path in retired_paths:
        try:
            path.lstat()
        except FileNotFoundError:
            continue
        return False

    rechecked = plugin_root.lstat()
    reparse_point = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    if (
        plugin_root.is_symlink()
        or not stat.S_ISDIR(rechecked.st_mode)
        or getattr(rechecked, "st_file_attributes", 0) & reparse_point
        or (rechecked.st_dev, rechecked.st_ino)
        != (original_metadata.st_dev, original_metadata.st_ino)
        or rechecked.st_ctime_ns != original_metadata.st_ctime_ns
        or rechecked.st_mtime_ns != original_metadata.st_mtime_ns
        or plugin_root.resolve(strict=True) != plugin_root
    ):
        raise native_runtime.NativeRuntimeError(
            "ChatGPT Meetings official plugin cache is not canonical"
        )
    for path in retired_paths:
        try:
            path.lstat()
        except FileNotFoundError:
            continue
        raise native_runtime.NativeRuntimeError(
            "ChatGPT Meetings official plugin cache is not canonical"
        )
    return True


def _official_cache_version_candidates(
    family_root: Path,
    *,
    selected_plugin_root: Path | None = None,
) -> list[Path]:
    """Return real versions while rejecting fresh, incomplete, or changing contenders."""

    try:
        resolved_family = family_root.resolve(strict=True)
        versions: list[tuple[Path, os.stat_result, bool]] = []
        reparse_point = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
        for candidate in family_root.iterdir():
            if native_runtime.GITHUB_RELEASE_COMPONENT.fullmatch(candidate.name) is None:
                continue
            metadata = candidate.lstat()
            if (
                candidate.is_symlink()
                or not stat.S_ISDIR(metadata.st_mode)
                or getattr(metadata, "st_file_attributes", 0) & reparse_point
            ):
                raise native_runtime.NativeRuntimeError(
                    "ChatGPT Meetings official plugin cache is not canonical"
                )
            resolved_candidate = candidate.resolve(strict=True)
            if resolved_candidate.parent != resolved_family:
                raise native_runtime.NativeRuntimeError(
                    "ChatGPT Meetings official plugin cache is not canonical"
                )
            empty = False
            if resolved_candidate != selected_plugin_root:
                with os.scandir(candidate) as entries:
                    empty = next(entries, None) is None
                if empty:
                    rechecked = candidate.lstat()
                    if (
                        candidate.is_symlink()
                        or not stat.S_ISDIR(rechecked.st_mode)
                        or getattr(rechecked, "st_file_attributes", 0) & reparse_point
                        or (rechecked.st_dev, rechecked.st_ino)
                        != (metadata.st_dev, metadata.st_ino)
                        or rechecked.st_ctime_ns != metadata.st_ctime_ns
                        or rechecked.st_mtime_ns != metadata.st_mtime_ns
                        or candidate.resolve(strict=True) != resolved_candidate
                    ):
                        raise native_runtime.NativeRuntimeError(
                            "ChatGPT Meetings official plugin cache is not canonical"
                        )
                    with os.scandir(candidate) as recheck_entries:
                        if next(recheck_entries, None) is not None:
                            raise native_runtime.NativeRuntimeError(
                                "ChatGPT Meetings official plugin cache is not canonical"
                            )
                    metadata = rechecked
            versions.append((resolved_candidate, metadata, empty))

        selected = next(
            (version for version in versions if version[0] == selected_plugin_root),
            None,
        )
        populated = [version for version in versions if not version[2]]
        complete = (
            [
                version
                for version in populated
                if _official_cache_complete_windows_installation(version[0])
            ]
            if len(populated) > 1
            else []
        )
        if selected_plugin_root is None:
            if len(populated) == 1:
                selected = populated[0]
            elif len(complete) == 1:
                selected = complete[0]
        if selected is None:
            return [path for path, _metadata, _empty in versions]

        selected_created_ns = _official_cache_directory_creation_ns(selected[1])
        candidates: list[Path] = []
        for path, metadata, empty in versions:
            older = _official_cache_directory_creation_ns(metadata) < selected_created_ns
            if empty and older:
                continue
            if (
                not empty
                and older
                and selected in complete
                and _official_cache_fully_pruned_windows_installation(path, metadata)
            ):
                continue
            candidates.append(path)
        return candidates
    except native_runtime.NativeRuntimeError:
        raise
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "ChatGPT Meetings official plugin cache is unavailable"
        ) from exc


def _official_cache_singleton_is_active(
    plugin_root: Path,
    family_root: Path,
    publisher_root: Path,
) -> bool:
    """Prove the only installed Internal Distribution version without a manifest.

    Official Internal Distribution caches currently have no marketplace.json
    activation pointer. Accept that layout only for a build-pinned publisher,
    plugin id, and one genuine installed version. Empty pruned version
    directories are not contenders; populated alternatives stay fail-closed.
    """

    if (
        publisher_root.name not in native_runtime.OFFICIAL_CACHE_PUBLISHERS
        or family_root.name != native_runtime.RUNTIME_CONFIG.server_name
    ):
        return False
    return native_runtime._official_cache_version_candidates(
        family_root,
        selected_plugin_root=plugin_root,
    ) == [plugin_root]


def require_canonical_plugin_registration(
    plugin_root: Path,
    family_root: Path,
) -> None:
    """Reject a stale cache version when a canonical manifest names another.

    Multiple MCP processes can survive a plugin update. Version ordering is
    not a trustworthy authority here: an alpha tag, local suffix, or rollback
    can all sort incorrectly. The installer-owned marketplace manifest is the
    canonical pointer, so only the exact version root it names may initiate a
    launch/update handoff. Source checkouts and non-cache local fixtures stay
    outside this installed-plugin guard.
    """

    try:
        resolved_plugin = plugin_root.expanduser().resolve(strict=True)
    except FileNotFoundError as exc:
        raise native_runtime.NativeRuntimeRegistrationUnavailable("plugin_root") from exc
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "ChatGPT Meetings plugin registration is unavailable"
        ) from exc
    try:
        resolved_family = family_root.expanduser().resolve(strict=True)
    except FileNotFoundError as exc:
        raise native_runtime.NativeRuntimeRegistrationUnavailable("family_root") from exc
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "ChatGPT Meetings plugin registration is unavailable"
        ) from exc
    if plugin_root.is_symlink() or resolved_plugin.parent != resolved_family:
        raise native_runtime.NativeRuntimeError(
            "ChatGPT Meetings plugin registration is not canonical"
        )
    if native_runtime.plugin_cache_family_root(resolved_plugin) != resolved_family:
        # Local fixture/source launches are not installed-cache contenders.
        return
    if native_runtime.GITHUB_RELEASE_COMPONENT.fullmatch(resolved_plugin.name) is None:
        raise native_runtime.NativeRuntimeError(
            "ChatGPT Meetings plugin registration is not canonical"
        )

    marketplace_root = resolved_family.parent
    manifest_path = marketplace_root / ".agents" / "plugins" / "marketplace.json"
    if manifest_path.is_symlink():
        raise native_runtime.NativeRuntimeError(
            "ChatGPT Meetings plugin registration is not canonical"
        )
    if not manifest_path.exists():
        from native_runtime_windows_recovery import allows_running_source

        if allows_running_source(resolved_plugin, resolved_family):
            return
        if native_runtime._official_cache_singleton_is_active(
            resolved_plugin,
            resolved_family,
            marketplace_root,
        ):
            return
        # Marketplace installs must retain their installer-owned pointer. An
        # official cache with multiple versions also has no provable active
        # version and therefore fails closed.
        raise native_runtime.NativeRuntimeError(
            "ChatGPT Meetings plugin registration is unavailable"
        )
    try:
        resolved_manifest = manifest_path.resolve(strict=True)
        metadata = resolved_manifest.stat()
    except FileNotFoundError as exc:
        raise native_runtime.NativeRuntimeRegistrationUnavailable("registration_manifest") from exc
    except OSError as exc:
        raise native_runtime.NativeRuntimeError(
            "ChatGPT Meetings plugin registration is unavailable"
        ) from exc
    if (
        resolved_manifest != manifest_path
        or not stat.S_ISREG(metadata.st_mode)
        or (
            not native_runtime._is_windows_host()
            and (metadata.st_uid != os.getuid() or metadata.st_mode & 0o022)
        )
        or metadata.st_size > native_runtime.MAXIMUM_MANIFEST_BYTES
    ):
        raise native_runtime.NativeRuntimeError(
            "ChatGPT Meetings plugin registration is not canonical"
        )
    manifest = native_runtime._read_strict_local_json(
        resolved_manifest,
        maximum_bytes=native_runtime.MAXIMUM_MANIFEST_BYTES,
        label="ChatGPT Meetings plugin registration",
        reject_public_writes=True,
    )
    plugins = manifest.get("plugins") if isinstance(manifest, dict) else None
    matches = (
        [
            entry
            for entry in plugins
            if isinstance(entry, dict) and entry.get("name") == resolved_family.name
        ]
        if isinstance(plugins, list)
        else []
    )
    source = matches[0].get("source") if len(matches) == 1 else None
    registered_path = source.get("path") if isinstance(source, dict) else None
    if (
        not isinstance(manifest, dict)
        or manifest.get("name") != marketplace_root.name
        or not isinstance(source, dict)
        or source.get("source") != "local"
        or not isinstance(registered_path, str)
        or not registered_path
        or "\x00" in registered_path
    ):
        raise native_runtime.NativeRuntimeError(
            "ChatGPT Meetings plugin registration is not canonical"
        )
    try:
        registered_plugin = (marketplace_root / registered_path).resolve(strict=True)
    except FileNotFoundError as exc:
        raise native_runtime.NativeRuntimeRegistrationUnavailable("registered_plugin") from exc
    except (OSError, RuntimeError, ValueError) as exc:
        raise native_runtime.NativeRuntimeError(
            "ChatGPT Meetings plugin registration is unavailable"
        ) from exc
    if registered_plugin != resolved_plugin:
        raise native_runtime.NativeRuntimeError(
            "ChatGPT Meetings plugin registration is not canonical"
        )


def _resolve_plugin_handoff_for_launch(
    app_path: Path,
    family_root: Path,
    spec: native_runtime.PlatformRuntimeSpec,
    expected_executable_sha256: str | None = None,
    *,
    source_plugin_root: Path | None = None,
    recover_unhealthy_current: bool = False,
) -> str:
    """Map the private control resolver onto the native launch error surface."""

    # control_client imports this module, so keep the reverse edge local to
    # the execution boundary instead of introducing an import cycle at load.
    from control_client import (
        ControlUnavailable,
        CooperativeHandoffDeclined,
        CooperativeHandoffRequired,
        resolve_update_handoff_for_launch,
    )

    try:
        source_arguments: _HandoffArguments = (
            {"source_plugin_root": source_plugin_root} if source_plugin_root is not None else {}
        )
        if recover_unhealthy_current:
            source_arguments["recover_unhealthy_current"] = True
        return resolve_update_handoff_for_launch(
            app_path,
            family_root,
            spec,
            expected_executable_sha256=expected_executable_sha256,
            **source_arguments,
        )
    except CooperativeHandoffDeclined as exc:
        raise native_runtime.NativeRuntimeUpdateDeferred(
            "older ChatGPT Meetings companion is busy; update is deferred"
        ) from exc
    except CooperativeHandoffRequired as exc:
        raise native_runtime.NativeRuntimeQuitRequired(
            "older ChatGPT Meetings companion must quit before launch"
        ) from exc
    except ControlUnavailable as exc:
        raise native_runtime.NativeRuntimeError(
            "could not hand off running ChatGPT Meetings"
        ) from exc
