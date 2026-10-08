"""Authenticated runtime provenance for stream-only companion handoffs."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

import control_client
from native_runtime_types import PlatformRuntimeSpec
from runtime_config import RUNTIME_CONFIG


def _resolved_path(value: object, *, message: str) -> Path:
    if not isinstance(value, str) or not value:
        raise control_client.ControlUnavailable(message)
    try:
        return control_client.Path(value).resolve(strict=True)
    except (OSError, ValueError) as exc:
        raise control_client.ControlUnavailable(message) from exc


def _is_direct_versioned_plugin_app(
    path: Path,
    family_root: Path,
    *,
    artifact_name: str = RUNTIME_CONFIG.app_name,
) -> bool:
    """Allow only the exact family-root/version/artifact path.

    The family root is derived by native_runtime from Codex's plugin cache;
    accepting arbitrary descendants would let a descriptor point at an
    unrelated signed app copied under a writable subtree.
    """

    try:
        relative = path.relative_to(family_root)
    except ValueError:
        return False
    return (
        len(relative.parts) == 2
        and control_client._PLUGIN_VERSION_COMPONENT.fullmatch(relative.parts[0]) is not None
        and relative.parts[-1] == artifact_name
    )


def _is_stable_runtime_artifact(
    path: Path,
    spec: PlatformRuntimeSpec,
    *,
    require_active: bool,
) -> bool:
    from native_runtime import stable_runtime_artifact_root

    try:
        stable_runtime_artifact_root(path)
        control_client.stable_runtime_verification_manifest(
            path, spec, require_active=require_active
        )
    except (OSError, control_client.NativeRuntimeError):
        return False
    return True


def _runtime_handoff_source(
    runtime: Mapping[str, object],
    expected: Path,
    spec: PlatformRuntimeSpec,
) -> tuple[Path, Path]:
    """Authorize the source cache while an immutable generation owns execution."""

    source_value = runtime.get("_sourcePluginRoot")
    source_root = expected.parent
    source_missing = False
    if isinstance(source_value, str) and source_value:
        try:
            source_root = control_client._resolved_path(
                source_value,
                message="native update handoff requester is not canonical",
            )
        except control_client.ControlUnavailable:
            source_root = control_client._exact_missing_handoff_path(
                source_value,
                message="native update handoff requester is not canonical",
            )
            source_missing = True
    family_root = control_client.plugin_cache_family_root(source_root, allow_missing=source_missing)
    if family_root is None:
        raise control_client.ControlUnavailable("native update handoff requester is not canonical")
    if not source_missing:
        try:
            control_client.require_canonical_plugin_registration(source_root, family_root)
            if source_root != expected.parent:
                control_client.plugin_artifact_path(source_root, spec)
        except control_client.NativeRuntimeError as exc:
            raise control_client.ControlUnavailable(
                "native update handoff requester is not canonical"
            ) from exc
    if source_root != expected.parent and not control_client._is_stable_runtime_artifact(
        expected,
        spec,
        require_active=True,
    ):
        raise control_client.ControlUnavailable("native update handoff app identity does not match")
    return source_root, family_root


def _lexical_absolute_path(value: object, *, message: str) -> Path:
    """Read one absolute, normalized path without requiring it to exist.

    A retained handoff receipt is needed precisely when Codex has already
    pruned the old bundle path. We still reject relative paths, traversal,
    and non-normalized spellings before considering that narrow recovery
    lane; the receipt was minted only while the original path existed and
    validated.
    """

    if not isinstance(value, str) or not value:
        raise control_client.ControlUnavailable(message)
    candidate = control_client.Path(value).expanduser()
    if not candidate.is_absolute():
        raise control_client.ControlUnavailable(message)
    normalized = control_client.Path(control_client.os.path.normpath(str(candidate)))
    if normalized != candidate:
        raise control_client.ControlUnavailable(message)
    return normalized


def _future_path(value: object, *, message: str) -> Path:
    """Normalize an absolute cache path even when its last child is absent."""

    candidate = control_client._lexical_absolute_path(value, message=message)
    try:
        return candidate.resolve(strict=False)
    except (OSError, ValueError) as exc:
        raise control_client.ControlUnavailable(message) from exc


def _exact_missing_handoff_path(value: object, *, message: str) -> Path:
    """Return one lexically canonical path only when it is truly absent."""

    if not isinstance(value, str) or not value or not control_client.os.path.isabs(value):
        raise control_client.ControlUnavailable(message)
    candidate = control_client.Path(value)
    if str(candidate) != value or control_client.os.path.normpath(value) != value:
        raise control_client.ControlUnavailable(message)
    if control_client._path_entry_may_exist(candidate):
        raise control_client.ControlUnavailable(message)
    try:
        resolved = candidate.resolve(strict=False)
    except (OSError, ValueError) as exc:
        raise control_client.ControlUnavailable(message) from exc
    if resolved != candidate:
        raise control_client.ControlUnavailable(message)
    return candidate


def _resolved_handoff_paths(
    expected_app_path: Path,
    plugin_family_root: Path,
    spec: PlatformRuntimeSpec,
) -> tuple[Path, Path]:
    expected = control_client._resolved_path(
        str(expected_app_path),
        message="native update handoff app identity is unavailable",
    )
    try:
        family = control_client._resolved_path(
            str(plugin_family_root),
            message="native update handoff plugin cache is unavailable",
        )
    except control_client.ControlUnavailable:
        # An immutable active generation can outlive a completely pruned
        # official cache family. Its validated manifest is the replacement
        # authority; the absent family is used only as a narrowly checked
        # lexical namespace for the old descriptor, never as executable
        # provenance.
        if not control_client._is_stable_runtime_artifact(expected, spec, require_active=True):
            raise
        family = control_client._future_path(
            str(plugin_family_root),
            message="native update handoff plugin cache is unavailable",
        )
        configured_home = control_client.os.environ.get("CODEX_HOME", "")
        if configured_home != configured_home.strip():
            raise control_client.ControlUnavailable(
                "native update handoff plugin cache is unavailable"
            ) from None
        codex_home = (
            control_client.Path(configured_home).expanduser()
            if configured_home
            else control_client.Path.home() / ".codex"
        )
        try:
            relative = family.relative_to((codex_home / "plugins" / "cache").resolve(strict=False))
        except (OSError, ValueError) as exc:
            raise control_client.ControlUnavailable(
                "native update handoff plugin cache is unavailable"
            ) from exc
        if (
            len(relative.parts) != 2
            or relative.parts[0] not in control_client.OFFICIAL_CACHE_PUBLISHERS
            or relative.parts[1] != control_client.RUNTIME_CONFIG.server_name
        ):
            raise control_client.ControlUnavailable(
                "native update handoff plugin cache is unavailable"
            ) from None
    return family, expected


def _expected_executable_path(
    app_path: Path,
    spec: PlatformRuntimeSpec,
) -> Path:
    if spec.artifact_kind == "windows-executable":
        return control_client._resolved_path(
            str(app_path),
            message="native update handoff app identity is unavailable",
        )
    try:
        with (app_path / "Contents" / "Info.plist").open("rb") as handle:
            info = control_client.plistlib.load(handle)
    except (OSError, control_client.plistlib.InvalidFileException) as exc:
        raise control_client.ControlUnavailable(
            "native update handoff app identity is unavailable"
        ) from exc
    executable = info.get("CFBundleExecutable") if isinstance(info, dict) else None
    if not isinstance(executable, str) or not executable:
        raise control_client.ControlUnavailable("native update handoff app identity is unavailable")
    return control_client._resolved_path(
        str(app_path / "Contents" / "MacOS" / executable),
        message="native update handoff app identity is unavailable",
    )


resolved_path = _resolved_path
is_direct_versioned_plugin_app = _is_direct_versioned_plugin_app
is_stable_runtime_artifact = _is_stable_runtime_artifact
runtime_handoff_source = _runtime_handoff_source
lexical_absolute_path = _lexical_absolute_path
future_path = _future_path
exact_missing_handoff_path = _exact_missing_handoff_path
resolved_handoff_paths = _resolved_handoff_paths
expected_executable_path = _expected_executable_path
