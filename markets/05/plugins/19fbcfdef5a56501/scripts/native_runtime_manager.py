"""ChatGPT Meetings native-runtime discovery, activation, and launch manager."""

# This legacy facade intentionally retains native_runtime's private, monkeypatchable
# compatibility seams; every unknown, missing, and unsafe type diagnostic stays strict.
# pyright: reportPrivateUsage=false

from __future__ import annotations

import re
import stat
import subprocess
import time
from collections.abc import Mapping
from contextlib import nullcontext
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Callable

import native_runtime
import native_runtime_windows_recovery as windows_recovery
from native_runtime_stable import cleanup_unused_plugin_artifacts
from native_runtime_types import (
    NativeArtifactFingerprint,
    NativeRuntimeStatus,
    StableGenerationManifest,
    StableRuntimeVerification,
)

from helpers import is_json

_NATIVE_RELEASE_VERSION_PATTERN = re.compile(
    r"(0|[1-9][0-9]{0,8})\.(0|[1-9][0-9]{0,8})\.(0|[1-9][0-9]{0,8})"
    r"(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?\Z"
)


class _NativeRuntimeLaunchRejected(native_runtime.NativeRuntimeError):
    """The verified platform launcher rejected its authenticated native child."""


class RuntimeManager:
    def __init__(
        self,
        spec: native_runtime.PlatformRuntimeSpec | None = None,
        plugin_root: Path | None = None,
    ) -> None:
        self.spec = spec or native_runtime.configured_platform_spec()
        # Resolve from this imported module, not cwd or an environment
        # variable. Codex may launch MCP servers from arbitrary directories.
        self.plugin_root = (plugin_root or native_runtime.PLUGIN_ROOT).expanduser()

    def _uses_stable_runtime(self) -> bool:
        return native_runtime.RUNTIME_CONFIG.flavor == "production" or (
            native_runtime.RUNTIME_CONFIG.flavor == "development"
            and native_runtime.RUNTIME_CONFIG.default_mcp_profile == "local-dev"
        )

    @staticmethod
    def _handoff_failure_reason(error: native_runtime.NativeRuntimeError) -> str:
        """Classify bounded authenticated-owner failures without exposing exception data."""

        from control_client import (
            ControlRequestTimedOut,
            DescriptorChanged,
            HandoffExitTimedOut,
            HandoffOwnerUnsettled,
        )

        reason = "handoff_unavailable"
        cause = error.__cause__
        for _ in range(4):
            if cause is None:
                break
            if isinstance(cause, DescriptorChanged):
                return "owner_changed"
            if isinstance(cause, ControlRequestTimedOut):
                reason = "timeout"
            elif isinstance(cause, (HandoffOwnerUnsettled, HandoffExitTimedOut)) and (
                reason == "handoff_unavailable"
            ):
                reason = "owner_unresponsive"
            cause = cause.__cause__
        return reason

    def _base_status(self) -> NativeRuntimeStatus:
        return {
            "installed": False,
            "version": None,
            "buildTimestamp": None,
            "appPath": None,
            "artifactPath": None,
            "platform": self.spec.platform_key,
            "artifactKind": self.spec.artifact_kind,
            "artifactPathKind": self.spec.artifact_path_kind,
            "capabilities": [],
        }

    def _plugin_artifact_is_present(self) -> bool:
        candidate = self.plugin_root / self.spec.artifact_name
        # is_symlink catches a broken top-level substitution and fails closed.
        return candidate.exists() or candidate.is_symlink()

    def has_plugin_bundled_artifact_hint(self) -> bool:
        """Return only a cheap presence hint for cold-start routing.

        This is deliberately not an installation or execution proof. The
        initialize bootstrap uses it only to decide whether an absent control
        descriptor can skip a redundant status traversal before launch.
        launch_current still performs canonical registration checks and a
        fresh full signature verification before it can execute anything.
        """

        if self._plugin_artifact_is_present():
            return True
        if not self._uses_stable_runtime():
            return False
        try:
            active = native_runtime.stable_runtime_root(create=False) / "active"
        except native_runtime.NativeRuntimeError:
            return False
        try:
            metadata = active.lstat()
        except OSError:
            return False
        reparse_point = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
        return (
            not active.is_symlink()
            and stat.S_ISREG(metadata.st_mode)
            and 0 < metadata.st_size <= native_runtime.STABLE_RUNTIME_MANIFEST_MAX_BYTES
            and not (reparse_point and getattr(metadata, "st_file_attributes", 0) & reparse_point)
        )

    def has_plugin_bundled_update_hint(self) -> bool:
        """Return whether a canonical source advertises a newer immutable generation."""

        if not self._uses_stable_runtime() or not self._plugin_artifact_is_present():
            return False
        source_artifact = self.plugin_root / self.spec.artifact_name
        try:
            try:
                runtime_root = native_runtime.stable_runtime_root(create=False)
                _active_artifact, active = native_runtime._read_active_stable_generation(
                    runtime_root, self.spec
                )
            except native_runtime.NativeRuntimeError:
                # With no usable active generation, the ordinary cold-launch
                # path already verifies and publishes the source. There is
                # no outgoing owner to stage or hand off first.
                return False
            family_root = native_runtime.plugin_cache_family_root(self.plugin_root)
            if family_root is None:
                return True
            native_runtime.require_canonical_plugin_registration(self.plugin_root, family_root)
            if windows_recovery.uses_pinned_source(self.plugin_root):
                return active.get("generation") != windows_recovery.pinned_generation(
                    self.plugin_root, self.spec
                )
            if native_runtime._is_windows_spec(self.spec):
                descriptor = native_runtime._read_strict_local_json(
                    self.plugin_root / native_runtime.WINDOWS_PRODUCTION_BUNDLE_RELATIVE_PATH,
                    maximum_bytes=native_runtime.MAXIMUM_MANIFEST_BYTES,
                    label="plugin-bundled Windows distribution",
                )
                platforms = descriptor.get("platforms")
                entry = platforms.get(self.spec.platform_key) if is_json(platforms) else None
                source_digest = entry.get("executableSha256") if is_json(entry) else None
            else:
                source_digest = native_runtime._stable_source_verification_manifest(
                    self.plugin_root,
                    source_artifact,
                    self.spec,
                ).get("artifactSha256")
            if (
                not isinstance(source_digest, str)
                or native_runtime.SHA256_HEX_PATTERN.fullmatch(source_digest) is None
            ):
                return True
            if native_runtime._is_windows_spec(self.spec):
                source_digest = native_runtime._windows_generation_sha256(
                    source_digest,
                    native_runtime._windows_source_licenses_sha256(
                        native_runtime.plugin_artifact_path(self.plugin_root, self.spec), self.spec
                    ),
                )
            return active.get("generation") != native_runtime._stable_generation_name(
                self.spec, source_digest
            )
        except native_runtime.NativeRuntimeError:
            # This is a routing hint, never execution authority. A present but
            # malformed authority must take the full verified lane and fail
            # closed instead of hiding behind a healthy old stable owner.
            return True

    @staticmethod
    def _native_release_version_key(
        value: object,
    ) -> tuple[int, int, int, int, tuple[tuple[int, int | str], ...]]:
        if not isinstance(value, str) or len(value) > 128:
            raise native_runtime.NativeRuntimeError("native release version is malformed")
        matched = _NATIVE_RELEASE_VERSION_PATTERN.fullmatch(value)
        if matched is None:
            raise native_runtime.NativeRuntimeError("native release version is malformed")
        identifiers: list[tuple[int, int | str]] = []
        prerelease = matched.group(4)
        if prerelease is not None:
            for identifier in prerelease.split("."):
                if identifier.isdigit():
                    if len(identifier) > 1 and identifier.startswith("0"):
                        raise native_runtime.NativeRuntimeError(
                            "native release version is malformed"
                        )
                    identifiers.append((0, int(identifier)))
                else:
                    identifiers.append((1, identifier))
        return (
            int(matched.group(1)),
            int(matched.group(2)),
            int(matched.group(3)),
            int(prerelease is None),
            tuple(identifiers),
        )

    @staticmethod
    def native_release_version_key(
        value: object,
    ) -> tuple[int, int, int, int, tuple[tuple[int, int | str], ...]]:
        """Expose the canonical, strictly validated native release ordering."""

        return RuntimeManager._native_release_version_key(value)

    def _require_automatic_native_upgrade(
        self,
        active_artifact: Path,
        active_manifest: StableGenerationManifest,
    ) -> NativeArtifactFingerprint:
        """Reject a signed downgrade on the background existing-owner lane.

        Canonical published rollback is intentional when a user explicitly
        launches the replacement, so this fence is deliberately limited to
        automatic owner-only updates. Marketing/status versions collapse
        Darwin alpha builds and are constant on Windows; use only the fully
        verified platform release identities instead.
        """

        source_artifact = native_runtime.plugin_artifact_path(self.plugin_root, self.spec)
        native_runtime._verified_stable_artifact_metadata(
            active_artifact,
            active_manifest,
            self.spec,
            force_verify=True,
        )
        if native_runtime._is_windows_spec(self.spec):
            if windows_recovery.uses_pinned_source(self.plugin_root):
                with windows_recovery.snapshot(
                    self.plugin_root, native_runtime.stable_runtime_root(), self.spec
                ) as pinned:
                    source_verification = pinned.verification
                    source_fingerprint = windows_recovery.source_fingerprint(
                        self.plugin_root, self.spec
                    )
            else:
                source_fingerprint, _, _, _ = self._verified_plugin_metadata(
                    source_artifact,
                    force_verify=True,
                )
                source_verification = native_runtime._windows_production_verification_manifest(
                    source_artifact,
                    self.spec,
                )
            active_verification = active_manifest["verification"]
            active_distribution = (
                active_verification["windowsDistribution"]
                if "windowsDistribution" in active_verification
                else None
            )
            source_distribution = (
                source_verification["windowsDistribution"]
                if "windowsDistribution" in source_verification
                else None
            )
            active_release = (
                active_distribution["release"] if active_distribution is not None else None
            )
            source_release = (
                source_distribution["release"] if source_distribution is not None else None
            )
            active_version = active_release["version"] if active_release is not None else None
            source_version = source_release["version"] if source_release is not None else None
        else:
            source_status, _ = self._readonly_stable_source_status(source_artifact)
            if "_artifactFingerprint" not in source_status:
                raise native_runtime.NativeRuntimeError(
                    "stable native runtime source identity is unavailable"
                )
            source_fingerprint = source_status["_artifactFingerprint"]
            active_info, _, _ = native_runtime._load_app_metadata(active_artifact, self.spec)
            source_info, _, _ = native_runtime._load_app_metadata(source_artifact, self.spec)

            def darwin_release_version(
                info: Mapping[str, object],
                fallback: object,
            ) -> object:
                marketing_version = info.get("CFBundleShortVersionString")
                release_version = info.get("ChatGPTMeetingsVersion")
                if release_version is None:
                    build_number = info.get("CFBundleVersion")
                    marketing_match = (
                        _NATIVE_RELEASE_VERSION_PATTERN.fullmatch(marketing_version)
                        if isinstance(marketing_version, str)
                        else None
                    )
                    if (
                        isinstance(build_number, str)
                        and re.fullmatch(r"[1-9][0-9]{0,8}", build_number) is not None
                        and marketing_match is not None
                        and marketing_match.group(4) is None
                    ):
                        return f"{marketing_version}-alpha.{build_number}"
                    return fallback
                if not isinstance(release_version, str) or marketing_version not in {
                    release_version,
                    release_version.split("-", 1)[0].split("+", 1)[0],
                }:
                    raise native_runtime.NativeRuntimeError("native release version is malformed")
                return release_version

            active_version = darwin_release_version(active_info, active_manifest.get("version"))
            source_version = darwin_release_version(
                source_info,
                source_info.get("CFBundleShortVersionString"),
            )

        if self._native_release_version_key(source_version) < self._native_release_version_key(
            active_version
        ):
            raise native_runtime.NativeRuntimeError("automatic native downgrade is not allowed")
        return source_fingerprint

    def _verified_plugin_metadata(
        self,
        artifact_path: Path,
        *,
        force_verify: bool,
    ) -> tuple[NativeArtifactFingerprint, str, str | None, str]:
        """Return verified identity metadata, memoizing only successful proofs.

        The lock intentionally covers the expensive verifier. Without it,
        initialize and the first widget open can race and each run a deep
        codesign traversal for the same immutable plugin version.
        """

        cache_key = native_runtime._plugin_verification_cache_key(artifact_path, self.spec)
        with (
            native_runtime._PLUGIN_BUNDLE_VERIFICATION_LOCK,
            native_runtime._plugin_bundle_cross_process_lock(artifact_path, self.spec),
        ):
            verification_manifest: Mapping[str, object] = {}
            if not native_runtime._is_windows_spec(self.spec):
                verification_manifest = native_runtime._verified_cam_distribution_manifest(
                    self.plugin_root,
                    artifact_path,
                )
                native_runtime.restore_plugin_framework_symlinks(artifact_path)
            fingerprint, version, _build_timestamp = native_runtime._plugin_bundle_fingerprint(
                artifact_path,
                self.spec,
            )
            cached = native_runtime._PLUGIN_BUNDLE_VERIFICATION_CACHE.get(cache_key)
            if not force_verify and cached is not None and cached.fingerprint == fingerprint:
                return (
                    cached.fingerprint,
                    cached.version,
                    cached.build_timestamp,
                    cached.executable_sha256,
                )

            # A launch can never rely on a prior status poll. Re-run the full
            # signature check even when its cheap file identity is unchanged.
            executable_path = native_runtime._plugin_executable_path(artifact_path, self.spec)
            candidate_executable_sha256 = native_runtime.sha256_regular_file(executable_path)
            if native_runtime._is_windows_spec(self.spec):
                verification_manifest = native_runtime._windows_plugin_verification_manifest(
                    artifact_path,
                    self.spec,
                )
            native_runtime.validate_app(artifact_path, verification_manifest, self.spec)
            (
                verified_fingerprint,
                verified_version,
                verified_build_timestamp,
            ) = native_runtime._plugin_bundle_fingerprint(artifact_path, self.spec)
            verified_executable_sha256 = native_runtime.sha256_regular_file(executable_path)
            if (
                verified_fingerprint != fingerprint
                or verified_executable_sha256 != candidate_executable_sha256
            ):
                # Do not cache a bundle that changed while it was being
                # checked. One retry handles an ordinary atomic replacement;
                # a continuously mutating bundle stays fail-closed.
                retry_fingerprint, _, _ = native_runtime._plugin_bundle_fingerprint(
                    artifact_path,
                    self.spec,
                )
                executable_path = native_runtime._plugin_executable_path(artifact_path, self.spec)
                retry_executable_sha256 = native_runtime.sha256_regular_file(executable_path)
                if native_runtime._is_windows_spec(self.spec):
                    verification_manifest = native_runtime._windows_plugin_verification_manifest(
                        artifact_path,
                        self.spec,
                    )
                native_runtime.validate_app(artifact_path, verification_manifest, self.spec)
                (
                    stable_fingerprint,
                    stable_version,
                    stable_build_timestamp,
                ) = native_runtime._plugin_bundle_fingerprint(artifact_path, self.spec)
                stable_executable_sha256 = native_runtime.sha256_regular_file(executable_path)
                if (
                    stable_fingerprint != retry_fingerprint
                    or stable_executable_sha256 != retry_executable_sha256
                ):
                    raise native_runtime.NativeRuntimeError(
                        "native app changed during signature verification"
                    )
                verified_fingerprint = stable_fingerprint
                verified_version = stable_version
                verified_build_timestamp = stable_build_timestamp
                verified_executable_sha256 = stable_executable_sha256
            executable_sha256 = verified_executable_sha256
            final_fingerprint, _, _ = native_runtime._plugin_bundle_fingerprint(
                artifact_path,
                self.spec,
            )
            if final_fingerprint != verified_fingerprint:
                raise native_runtime.NativeRuntimeError(
                    "native app changed while hashing executable identity"
                )
            native_runtime._PLUGIN_BUNDLE_VERIFICATION_CACHE[cache_key] = (
                native_runtime._PluginBundleVerification(
                    fingerprint=verified_fingerprint,
                    version=verified_version or version,
                    build_timestamp=verified_build_timestamp,
                    executable_sha256=executable_sha256,
                )
            )
            return (
                verified_fingerprint,
                verified_version or version,
                verified_build_timestamp,
                executable_sha256,
            )

    def _plugin_status(self, *, force_verify: bool = False) -> NativeRuntimeStatus:
        artifact_path = native_runtime.plugin_artifact_path(self.plugin_root, self.spec)
        # The plugin package is the distribution boundary. Status polls reuse
        # a successful process-local proof when the critical file identities
        # are unchanged; launch passes force_verify so execution still always
        # crosses the full platform identity/signature boundary immediately
        # beforehand.
        (
            fingerprint,
            version,
            build_timestamp,
            executable_sha256,
        ) = self._verified_plugin_metadata(
            artifact_path,
            force_verify=force_verify,
        )
        executable_device, executable_inode = native_runtime._plugin_executable_file_identity(
            fingerprint,
            artifact_path,
            self.spec,
        )
        release_version = self._presentation_release_version(artifact_path, fingerprint)
        status: NativeRuntimeStatus = {
            **self._base_status(),
            "installed": True,
            "version": version,
            "buildTimestamp": build_timestamp,
            "appPath": str(artifact_path),
            "artifactPath": str(artifact_path),
            "source": "plugin-bundled",
            # Private execution identity. Public projection drops this field;
            # both platforms use it to prevent adopting a live process from a
            # same-path cache image that force-verification has superseded.
            "_artifactFingerprint": fingerprint,
            "_executableSHA256": executable_sha256,
            "_executableDevice": executable_device,
            "_executableInode": executable_inode,
        }
        if release_version is not None:
            status["releaseVersion"] = release_version
        return status

    def _presentation_release_version(
        self,
        artifact_path: Path,
        fingerprint: NativeArtifactFingerprint,
        *,
        manifest: StableGenerationManifest | None = None,
    ) -> str | None:
        """Read display-only release metadata from the verified active artifact."""

        if native_runtime._is_windows_spec(self.spec):
            if manifest is None:
                return None
            verification: Mapping[str, object] = manifest["verification"]
            distribution = verification.get("windowsDistribution")
            if not is_json(distribution):
                return None
            release = distribution.get("release")
            if not is_json(release):
                return None
            release_version = release.get("version")
            if (
                not isinstance(release_version, str)
                or native_runtime._NATIVE_ALPHA_RELEASE_VERSION.fullmatch(release_version) is None
            ):
                return None
            return release_version

        info_path = artifact_path / "Contents" / "Info.plist"
        try:
            if len(fingerprint) <= 2:
                return None
            expected_identity = fingerprint[2]
            if native_runtime._path_identity(info_path) != expected_identity:
                return None
            with info_path.open("rb") as handle:
                info = native_runtime.plistlib.load(handle)
            if native_runtime._path_identity(info_path) != expected_identity:
                return None
        except (
            native_runtime.NativeRuntimeError,
            OSError,
            native_runtime.plistlib.InvalidFileException,
        ):
            return None
        if not is_json(info):
            return None
        return native_runtime._plugin_bundle_release_version(info)

    def _readonly_stable_source_status(
        self,
        artifact_path: Path,
    ) -> tuple[NativeRuntimeStatus, StableRuntimeVerification]:
        """Authenticate a symlink-free companion source without modifying it.

        Internal Distribution deliberately removes signed framework links
        from the immutable plugin cache. Check the pinned native descriptor
        and receipt before snapshotting the source; only the private staged
        copy may restore those links and undergo deep signature verification.
        """

        with (
            native_runtime._PLUGIN_BUNDLE_VERIFICATION_LOCK,
            native_runtime._plugin_bundle_cross_process_lock(artifact_path, self.spec),
        ):
            verification = native_runtime._stable_source_verification_manifest(
                self.plugin_root,
                artifact_path,
                self.spec,
            )
            if native_runtime.RUNTIME_CONFIG.flavor != "production":
                native_runtime.validate_app(artifact_path, verification, self.spec)
            fingerprint, version, build_timestamp = native_runtime._plugin_bundle_fingerprint(
                artifact_path,
                self.spec,
            )
            executable = native_runtime._plugin_executable_path(artifact_path, self.spec)
            executable_sha256 = native_runtime.sha256_regular_file(executable)
            final_fingerprint, _, _ = native_runtime._plugin_bundle_fingerprint(
                artifact_path,
                self.spec,
            )
            if (
                final_fingerprint != fingerprint
                or native_runtime.sha256_regular_file(executable) != executable_sha256
            ):
                raise native_runtime.NativeRuntimeError(
                    "stable native runtime source changed while reading"
                )
            executable_device, executable_inode = native_runtime._plugin_executable_file_identity(
                fingerprint,
                artifact_path,
                self.spec,
            )

        return (
            {
                **self._base_status(),
                "installed": True,
                "version": version,
                "buildTimestamp": build_timestamp,
                "appPath": str(artifact_path),
                "artifactPath": str(artifact_path),
                "source": "plugin-bundled",
                "_artifactFingerprint": fingerprint,
                "_executableSHA256": executable_sha256,
                "_executableDevice": executable_device,
                "_executableInode": executable_inode,
            },
            verification,
        )

    def _revalidate_stable_source_activation(
        self,
        family_root: Path,
        expected_manifest: StableGenerationManifest,
    ) -> None:
        """Freshly prove that the canonical source still authorizes activation."""

        native_runtime.require_canonical_plugin_registration(self.plugin_root, family_root)
        if windows_recovery.uses_pinned_source(self.plugin_root):
            with windows_recovery.snapshot(
                self.plugin_root, native_runtime.stable_runtime_root(), self.spec
            ) as pinned:
                windows_recovery.require_matching_manifest(pinned, expected_manifest, self.spec)
            return
        source_artifact = native_runtime.plugin_artifact_path(self.plugin_root, self.spec)
        fingerprint, version, build_timestamp = native_runtime._plugin_bundle_fingerprint(
            source_artifact,
            self.spec,
        )
        executable_sha256 = native_runtime.sha256_regular_file(
            native_runtime._plugin_executable_path(source_artifact, self.spec)
        )
        verification = native_runtime._stable_source_verification_manifest(
            self.plugin_root,
            source_artifact,
            self.spec,
        )
        final_fingerprint, _, _ = native_runtime._plugin_bundle_fingerprint(
            source_artifact, self.spec
        )
        if final_fingerprint != fingerprint:
            raise native_runtime.NativeRuntimeError(
                "stable native runtime source changed before activation"
            )
        artifact_sha256 = (
            verification.get("artifactSha256")
            if not native_runtime._is_windows_spec(self.spec)
            else executable_sha256
        )
        if not isinstance(artifact_sha256, str):
            raise native_runtime.NativeRuntimeError(
                "stable native runtime source identity is unavailable"
            )
        if native_runtime._is_windows_spec(self.spec):
            licenses_sha256 = verification.get("thirdPartyLicensesSha256")
            if licenses_sha256 is not None and not isinstance(licenses_sha256, str):
                raise native_runtime.NativeRuntimeError(
                    "stable native runtime license binding is malformed"
                )
            artifact_sha256 = native_runtime._windows_generation_sha256(
                executable_sha256, licenses_sha256
            )
        current_manifest = native_runtime._validated_stable_generation_manifest(
            {
                "schemaVersion": native_runtime.STABLE_RUNTIME_SCHEMA_VERSION,
                "platform": self.spec.platform_key,
                "artifactName": self.spec.artifact_name,
                "generation": native_runtime._stable_generation_name(self.spec, artifact_sha256),
                "version": version,
                "buildTimestamp": build_timestamp,
                "executableSha256": executable_sha256,
                "verification": verification,
            },
            self.spec,
        )
        if current_manifest != expected_manifest:
            raise native_runtime.NativeRuntimeError(
                "stable native runtime source changed before activation"
            )

    def _stable_status_locked(
        self,
        *,
        force_verify: bool,
        activate: bool = True,
        revalidate_family_lock: Callable[[], None],
    ) -> NativeRuntimeStatus:
        runtime_root = native_runtime.stable_runtime_root()
        published = False
        if self._plugin_artifact_is_present():
            source_artifact = native_runtime.plugin_artifact_path(self.plugin_root, self.spec)
            family_root = native_runtime.plugin_cache_family_root(self.plugin_root)
            if family_root is None:
                raise native_runtime.NativeRuntimeError(
                    "canonical plugin cache registration is required for stable runtime"
                )
            native_runtime.require_canonical_plugin_registration(self.plugin_root, family_root)
            source_context = (
                windows_recovery.snapshot(self.plugin_root, runtime_root, self.spec)
                if windows_recovery.uses_pinned_source(self.plugin_root)
                else nullcontext(None)
            )
            with source_context as pinned:
                if pinned is not None:
                    source_artifact = pinned.artifact
                    source_status = pinned.status
                    verification = pinned.verification
                elif native_runtime._is_windows_spec(self.spec):
                    source_status = self._plugin_status(force_verify=force_verify)
                    verification = native_runtime._stable_source_verification_manifest(
                        self.plugin_root,
                        source_artifact,
                        self.spec,
                    )
                else:
                    source_status, verification = self._readonly_stable_source_status(
                        source_artifact
                    )
                artifact, manifest, published, verified_metadata = (
                    native_runtime._materialize_stable_generation(
                        runtime_root,
                        source_artifact,
                        source_status,
                        verification,
                        self.spec,
                        force_verify=force_verify,
                        activate=activate,
                        authorize_activation=lambda expected_manifest: (
                            self._revalidate_stable_source_activation(
                                family_root,
                                expected_manifest,
                            )
                        ),
                        revalidate_family_lock=revalidate_family_lock,
                    )
                )
            cleanup_unused_plugin_artifacts(
                self.plugin_root,
                self.spec,
                revalidate_family_lock=revalidate_family_lock,
            )
        else:
            artifact, manifest = native_runtime._read_active_stable_generation(
                runtime_root, self.spec
            )
            verified_metadata = native_runtime._verified_stable_artifact_metadata(
                artifact,
                manifest,
                self.spec,
                force_verify=force_verify,
            )
            generation = manifest["generation"]
            native_runtime._cleanup_stable_runtime_generations(
                runtime_root,
                self.spec,
                generation=generation,
                protected_generations={generation},
                prune_generations=True,
                revalidate_family_lock=revalidate_family_lock,
            )
        fingerprint, version, build_timestamp, executable_sha256 = verified_metadata
        executable_device, executable_inode = native_runtime._plugin_executable_file_identity(
            fingerprint,
            artifact,
            self.spec,
        )
        release_version = self._presentation_release_version(
            artifact,
            fingerprint,
            manifest=manifest,
        )
        status: NativeRuntimeStatus = {
            **self._base_status(),
            "installed": True,
            "version": version,
            "buildTimestamp": build_timestamp,
            "appPath": str(artifact),
            "artifactPath": str(artifact),
            "source": "plugin-bundled",
            "updated": published,
            "_artifactFingerprint": fingerprint,
            "_executableSHA256": executable_sha256,
            "_executableDevice": executable_device,
            "_executableInode": executable_inode,
            "_sourcePluginRoot": str(self.plugin_root.resolve(strict=False)),
        }
        if release_version is not None:
            status["releaseVersion"] = release_version
        return status

    def _stable_status(self, *, force_verify: bool) -> NativeRuntimeStatus:
        runtime_root = native_runtime.stable_runtime_root()
        with native_runtime._stable_runtime_family_lock(runtime_root) as revalidate:
            return self._stable_status_locked(
                force_verify=force_verify,
                revalidate_family_lock=revalidate,
            )

    def _stable_readonly_status(self, *, force_verify: bool) -> NativeRuntimeStatus:
        runtime_root = native_runtime.stable_runtime_root(create=False)
        artifact, manifest = native_runtime._read_active_stable_generation(runtime_root, self.spec)
        fingerprint, version, build_timestamp, executable_sha256 = (
            native_runtime._verified_stable_artifact_metadata(
                artifact,
                manifest,
                self.spec,
                force_verify=force_verify,
            )
        )
        executable_device, executable_inode = native_runtime._plugin_executable_file_identity(
            fingerprint,
            artifact,
            self.spec,
        )
        release_version = self._presentation_release_version(
            artifact,
            fingerprint,
            manifest=manifest,
        )
        status: NativeRuntimeStatus = {
            **self._base_status(),
            "installed": True,
            "version": version,
            "buildTimestamp": build_timestamp,
            "appPath": str(artifact),
            "artifactPath": str(artifact),
            "source": "plugin-bundled",
            "updated": False,
            "_artifactFingerprint": fingerprint,
            "_executableSHA256": executable_sha256,
            "_executableDevice": executable_device,
            "_executableInode": executable_inode,
            "_sourcePluginRoot": str(self.plugin_root.resolve(strict=False)),
        }
        if release_version is not None:
            status["releaseVersion"] = release_version
        return status

    def status(self, *, force_verify: bool = False) -> NativeRuntimeStatus:
        if self._uses_stable_runtime():
            try:
                return self._stable_readonly_status(force_verify=force_verify)
            except native_runtime.NativeRuntimeError:
                return self._base_status()
        if not self._plugin_artifact_is_present():
            return self._base_status()
        try:
            return self._plugin_status(force_verify=force_verify)
        except native_runtime.NativeRuntimeError:
            return self._base_status()

    def ensure_installed(self) -> NativeRuntimeStatus:
        if self._uses_stable_runtime():
            return self._stable_status(force_verify=False)
        if not self._plugin_artifact_is_present():
            raise native_runtime.NativeRuntimeError(
                "plugin-bundled ChatGPT Meetings is not installed"
            )
        # This is still a discovery/update result, not an execution boundary.
        # launch_current performs the mandatory fresh proof.
        return {**self._plugin_status(), "updated": False}

    def prepare_plugin_bundled_replacement(self) -> NativeRuntimeStatus:
        """Verify and stage a successor without changing the active owner.

        A historical v1 owner may predate immutable runtime generations, so a
        read-only active status can legitimately report no installed runtime.
        Bootstrap still needs a fully verified replacement before asking that
        authenticated idle owner to exit. Keep any existing active pointer
        unchanged until the old owner has safely yielded.
        """

        if not self._plugin_artifact_is_present():
            raise native_runtime.NativeRuntimeError(
                "plugin-bundled ChatGPT Meetings is not installed"
            )
        if not self._uses_stable_runtime():
            return self._plugin_status(force_verify=True)

        runtime_root = native_runtime.stable_runtime_root()
        with native_runtime._stable_runtime_family_lock(runtime_root) as revalidate:
            return self._stable_status_locked(
                force_verify=True,
                activate=False,
                revalidate_family_lock=revalidate,
            )

    def activate_prepared_plugin_bundled_replacement(
        self, expected: Mapping[str, object]
    ) -> NativeRuntimeStatus:
        """Activate only the replacement proved before an existing owner exited."""

        runtime_root = native_runtime.stable_runtime_root()
        with native_runtime._stable_runtime_family_lock(runtime_root) as revalidate:
            prepared = self._stable_status_locked(
                force_verify=True, activate=False, revalidate_family_lock=revalidate
            )
            app_path = prepared.get("appPath")
            if (
                not isinstance(app_path, str)
                or app_path != expected.get("appPath")
                or not isinstance(expected.get("_executableSHA256"), str)
                or prepared.get("_executableSHA256") != expected.get("_executableSHA256")
            ):
                raise native_runtime.NativeRuntimeError("prepared native replacement changed")
            family = native_runtime.plugin_cache_family_root(self.plugin_root)
            if family is None:
                raise native_runtime.NativeRuntimeError("native replacement is not canonical")
            manifest = native_runtime._validated_stable_generation_manifest(
                native_runtime._read_stable_runtime_manifest(
                    Path(app_path).parent / ".runtime.json"
                ),
                self.spec,
            )
            native_runtime._activate_stable_generation(
                runtime_root,
                manifest,
                authorize_activation=lambda value: self._revalidate_stable_source_activation(
                    family, value
                ),
                revalidate_family_lock=revalidate,
            )
            return prepared

    def require_codex_launch_context(self) -> tuple[str, str]:
        """Validate recovery launch arguments before the current owner may quit."""

        isolation = native_runtime.configured_e2e_isolation()
        if self.spec.launch_strategy == "macos-open-background":
            context = native_runtime._validated_codex_launch_context(platform="macos")
            build_arguments = native_runtime._darwin_codex_launch_arguments
        elif self.spec.launch_strategy == "windows-detached-process":
            context = native_runtime._validated_codex_launch_context(platform="windows")
            build_arguments = native_runtime._windows_codex_launch_arguments
        else:
            raise native_runtime.NativeRuntimeError("required Codex launch context is unavailable")
        if context is None:
            raise native_runtime.NativeRuntimeError("required Codex launch context is unavailable")
        build_arguments(required_codex_launch_context=context)
        if isolation is not None:
            replace(isolation, required_codex_launch_context=context).child_environment()
        return context

    def launch_current(
        self,
        *,
        require_plugin_bundled: bool = False,
        recover_unhealthy_current: bool = False,
        require_existing_owner: bool = False,
        required_codex_launch_context: tuple[str, str] | None = None,
        required_runtime_identity: Mapping[str, object] | None = None,
    ) -> NativeRuntimeStatus:
        if (
            required_codex_launch_context is not None
            and self.require_codex_launch_context() != required_codex_launch_context
        ):
            raise native_runtime.NativeRuntimeError("required Codex launch context changed")
        authenticated_handoff_completed = False
        if self._uses_stable_runtime():
            runtime_root = native_runtime.stable_runtime_root()
            with native_runtime._stable_runtime_family_lock(runtime_root) as revalidate:
                source_present = self._plugin_artifact_is_present()
                cache_family_root = native_runtime.plugin_cache_family_root(
                    self.plugin_root,
                    allow_missing=not source_present,
                )
                if cache_family_root is not None and source_present:
                    native_runtime.require_canonical_plugin_registration(
                        self.plugin_root,
                        cache_family_root,
                    )
                if (
                    required_codex_launch_context is None
                    and cache_family_root is not None
                    and source_present
                    and self.has_plugin_bundled_update_hint()
                ):
                    # Fully stage and verify B while A remains selected.
                    # Recipients authorize Quit against the active target, so
                    # select B immediately before handoff and restore the
                    # still-verified A pointer on a proven pre-ACK refusal.
                    # The family lock covers both replacements and the
                    # authenticated work-fence keeps active capture safe.
                    _active_artifact, previous_manifest = (
                        native_runtime._read_active_stable_generation(runtime_root, self.spec)
                    )
                    automatic_source_fingerprint = (
                        self._require_automatic_native_upgrade(_active_artifact, previous_manifest)
                        if require_existing_owner
                        else None
                    )
                    native_runtime.log_native_runtime_event(
                        "update-check",
                        "available",
                        platform=self.spec.platform_key,
                        previous_generation=previous_manifest.get("generation"),
                    )
                    staged = self._stable_status_locked(
                        force_verify=True,
                        activate=False,
                        revalidate_family_lock=revalidate,
                    )
                    if automatic_source_fingerprint is not None:
                        if windows_recovery.uses_pinned_source(self.plugin_root):
                            current_source_fingerprint = windows_recovery.source_fingerprint(
                                self.plugin_root, self.spec
                            )
                        else:
                            current_source_fingerprint, _, _ = (
                                native_runtime._plugin_bundle_fingerprint(
                                    native_runtime.plugin_artifact_path(
                                        self.plugin_root, self.spec
                                    ),
                                    self.spec,
                                )
                            )
                        if current_source_fingerprint != automatic_source_fingerprint:
                            raise native_runtime.NativeRuntimeError(
                                "native release changed before automatic update"
                            )
                    staged_app_path = staged.get("appPath")
                    staged_executable_sha256 = staged.get("_executableSHA256")
                    if not isinstance(staged_app_path, str) or not isinstance(
                        staged_executable_sha256, str
                    ):
                        raise native_runtime.NativeRuntimeError(
                            "staged native runtime identity is unavailable"
                        )
                    decoded_staged_manifest = native_runtime._read_stable_runtime_manifest(
                        Path(staged_app_path).parent / ".runtime.json"
                    )
                    staged_manifest = native_runtime._validated_stable_generation_manifest(
                        decoded_staged_manifest,
                        self.spec,
                    )
                    native_runtime._activate_stable_generation(
                        runtime_root,
                        staged_manifest,
                        authorize_activation=lambda expected_manifest: (
                            self._revalidate_stable_source_activation(
                                cache_family_root,
                                expected_manifest,
                            )
                        ),
                        revalidate_family_lock=revalidate,
                    )
                    native_runtime.log_native_runtime_event(
                        "activate",
                        "completed",
                        platform=self.spec.platform_key,
                        version=staged_manifest.get("version"),
                        build_timestamp=staged_manifest.get("buildTimestamp"),
                        generation=staged_manifest.get("generation"),
                        previous_generation=previous_manifest.get("generation"),
                    )
                    native_runtime.log_native_runtime_event(
                        "handoff",
                        "started",
                        platform=self.spec.platform_key,
                        version=staged_manifest.get("version"),
                        build_timestamp=staged_manifest.get("buildTimestamp"),
                        generation=staged_manifest.get("generation"),
                        previous_generation=previous_manifest.get("generation"),
                    )
                    try:
                        # A normal update must be able to replace an authenticated idle
                        # owner even when an older native refuses Quit because its durable
                        # outbox is nonempty. The recovery path rereads signed capture state,
                        # binds the exact process image, and revalidates immediately before
                        # termination; recording or finalization still fail closed.
                        handoff_disposition = native_runtime._resolve_plugin_handoff_for_launch(
                            Path(staged_app_path),
                            cache_family_root,
                            self.spec,
                            staged_executable_sha256,
                            source_plugin_root=self.plugin_root,
                            recover_unhealthy_current=True,
                        )
                        if require_existing_owner and handoff_disposition == "absent":
                            raise native_runtime.NativeRuntimeQuitRequired(
                                "authenticated ChatGPT Meetings owner disappeared before update"
                            )
                        authenticated_handoff_completed = handoff_disposition == "handed-off"
                    except (
                        native_runtime.NativeRuntimeUpdateDeferred,
                        native_runtime.NativeRuntimeQuitRequired,
                    ) as handoff_error:
                        native_runtime.log_native_runtime_event(
                            "handoff",
                            "deferred",
                            platform=self.spec.platform_key,
                            version=staged_manifest.get("version"),
                            build_timestamp=staged_manifest.get("buildTimestamp"),
                            generation=staged_manifest.get("generation"),
                            previous_generation=previous_manifest.get("generation"),
                            error_kind=(
                                "update-deferred"
                                if isinstance(
                                    handoff_error, native_runtime.NativeRuntimeUpdateDeferred
                                )
                                else "quit-required"
                            ),
                        )
                        # These typed refusals happen before an accepted
                        # handoff and prove A is still the live owner. Verify
                        # its executable, resources, receipt, and signature
                        # again immediately before restoring the pointer. If
                        # A changed, leave fully verified B selected and keep
                        # the original typed recovery. An ambiguous post-ACK
                        # timeout also leaves B selected.
                        try:
                            native_runtime._verified_stable_artifact_metadata(
                                _active_artifact,
                                previous_manifest,
                                self.spec,
                                force_verify=True,
                            )
                        except native_runtime.NativeRuntimeError as verification_error:
                            raise handoff_error from verification_error
                        revalidate()
                        native_runtime._write_stable_runtime_manifest(
                            runtime_root / "active",
                            {
                                "schemaVersion": native_runtime.STABLE_RUNTIME_SCHEMA_VERSION,
                                "generation": previous_manifest["generation"],
                            },
                            before_replace=revalidate,
                        )
                        native_runtime.log_native_runtime_event(
                            "activate",
                            "restored",
                            platform=self.spec.platform_key,
                            version=previous_manifest.get("version"),
                            build_timestamp=previous_manifest.get("buildTimestamp"),
                            generation=previous_manifest.get("generation"),
                            previous_generation=staged_manifest.get("generation"),
                        )
                        raise
                    except native_runtime.NativeRuntimeError as handoff_error:
                        try:
                            active_fingerprint: NativeArtifactFingerprint = (
                                ()
                                if native_runtime._is_windows_spec(self.spec)
                                else native_runtime._verified_stable_artifact_metadata(
                                    _active_artifact,
                                    previous_manifest,
                                    self.spec,
                                    force_verify=False,
                                )[0]
                            )
                            active_release_version = self._presentation_release_version(
                                _active_artifact,
                                active_fingerprint,
                                manifest=previous_manifest,
                            )
                        except Exception:
                            # Diagnostics never replace the authenticated handoff error.
                            active_release_version = None
                        native_runtime.log_native_runtime_event(
                            "handoff",
                            "failed",
                            platform=self.spec.platform_key,
                            version=staged_manifest.get("version"),
                            build_timestamp=staged_manifest.get("buildTimestamp"),
                            generation=staged_manifest.get("generation"),
                            previous_generation=previous_manifest.get("generation"),
                            error_kind="handoff",
                            reason=self._handoff_failure_reason(handoff_error),
                            active_owner_version=active_release_version,
                            target_owner_version=staged.get("releaseVersion"),
                        )
                        raise
                    native_runtime.log_native_runtime_event(
                        "handoff",
                        "completed",
                        platform=self.spec.platform_key,
                        version=staged_manifest.get("version"),
                        build_timestamp=staged_manifest.get("buildTimestamp"),
                        generation=staged_manifest.get("generation"),
                        previous_generation=previous_manifest.get("generation"),
                    )
                # Recovery may restart the selected app after its cooperative
                # exit, but cannot turn that permission into an update handoff.
                status = (
                    self._stable_readonly_status(force_verify=True)
                    if required_codex_launch_context is not None
                    else self._stable_status_locked(
                        force_verify=True,
                        revalidate_family_lock=revalidate,
                    )
                )
                status_app_path = status.get("appPath")
                if not isinstance(status_app_path, str):
                    raise native_runtime.NativeRuntimeError(
                        "active native runtime identity is unavailable"
                    )
                artifact = Path(status_app_path)
                if self.spec.launch_strategy == "windows-detached-process":
                    if cache_family_root is None:
                        raise native_runtime.NativeRuntimeError(
                            "canonical plugin cache registration is required on Windows"
                        )
                    with (
                        native_runtime._windows_executable_launch_guard(artifact),
                        native_runtime._windows_registration_launch_guard(
                            cache_family_root, plugin_root=self.plugin_root
                        )
                        if source_present
                        else nullcontext(),
                    ):
                        return self._launch_current_guarded(
                            require_plugin_bundled=require_plugin_bundled,
                            guarded_executable=artifact,
                            preverified_status=status,
                            source_plugin_root=self.plugin_root if source_present else None,
                            preverified_family_root=cache_family_root,
                            revalidate_family_lock=revalidate,
                            recover_unhealthy_current=recover_unhealthy_current,
                            require_existing_owner=require_existing_owner,
                            authenticated_handoff_completed=authenticated_handoff_completed,
                            required_codex_launch_context=required_codex_launch_context,
                            required_runtime_identity=required_runtime_identity,
                        )
                return self._launch_current_guarded(
                    require_plugin_bundled=require_plugin_bundled,
                    guarded_executable=None,
                    preverified_status=status,
                    source_plugin_root=self.plugin_root if source_present else None,
                    preverified_family_root=cache_family_root,
                    revalidate_family_lock=revalidate,
                    recover_unhealthy_current=recover_unhealthy_current,
                    require_existing_owner=require_existing_owner,
                    authenticated_handoff_completed=authenticated_handoff_completed,
                    required_codex_launch_context=required_codex_launch_context,
                    required_runtime_identity=required_runtime_identity,
                )
        if self.spec.launch_strategy == "windows-detached-process":
            cache_family_root = native_runtime.plugin_cache_family_root(self.plugin_root)
            if cache_family_root is None:
                message = (
                    "canonical plugin cache registration is required on Windows"
                    if self._plugin_artifact_is_present()
                    else "plugin-bundled ChatGPT Meetings is required on Windows"
                )
                raise native_runtime.NativeRuntimeError(message)
            native_runtime.require_canonical_plugin_registration(
                self.plugin_root,
                cache_family_root,
            )
            executable = native_runtime.plugin_artifact_path(self.plugin_root, self.spec)
            with (
                native_runtime._windows_executable_launch_guard(executable),
                native_runtime._windows_registration_launch_guard(
                    cache_family_root, plugin_root=self.plugin_root
                ),
            ):
                return self._launch_current_guarded(
                    require_plugin_bundled=require_plugin_bundled,
                    guarded_executable=executable,
                    recover_unhealthy_current=recover_unhealthy_current,
                    require_existing_owner=require_existing_owner,
                    required_codex_launch_context=required_codex_launch_context,
                    required_runtime_identity=required_runtime_identity,
                )
        return self._launch_current_guarded(
            require_plugin_bundled=require_plugin_bundled,
            guarded_executable=None,
            recover_unhealthy_current=recover_unhealthy_current,
            require_existing_owner=require_existing_owner,
            required_codex_launch_context=required_codex_launch_context,
            required_runtime_identity=required_runtime_identity,
        )

    def _launch_current_guarded(
        self,
        *,
        require_plugin_bundled: bool,
        guarded_executable: Path | None,
        preverified_status: NativeRuntimeStatus | None = None,
        source_plugin_root: Path | None = None,
        preverified_family_root: Path | None = None,
        revalidate_family_lock: Callable[[], None] | None = None,
        recover_unhealthy_current: bool = False,
        require_existing_owner: bool = False,
        authenticated_handoff_completed: bool = False,
        required_codex_launch_context: tuple[str, str] | None = None,
        required_runtime_identity: Mapping[str, object] | None = None,
    ) -> NativeRuntimeStatus:
        """Force-verify and launch the current runtime.

        Initialize bootstrap keeps its explicit plugin-bundle requirement so
        a companion that disappears after the cheap presence hint cannot be
        reported as an authenticated launch.
        """

        if self.spec.launch_strategy not in {
            "macos-open-background",
            "windows-detached-process",
        }:
            raise native_runtime.NativeRuntimeError(
                f"native runtime launcher for {self.spec.platform_key} is not implemented"
            )
        if self.spec.launch_strategy == "windows-detached-process" and guarded_executable is None:
            raise native_runtime.NativeRuntimeError(
                "guarded Windows executable is required for launch"
            )
        isolation = native_runtime.configured_e2e_isolation()
        if required_codex_launch_context is not None and isolation is not None:
            isolation = replace(
                isolation, required_codex_launch_context=required_codex_launch_context
            )
        capture_mode = native_runtime.configured_e2e_capture_mode(isolation)
        revalidate = revalidate_family_lock or (lambda: None)
        recovery_arguments = (
            {"recover_unhealthy_current": True} if recover_unhealthy_current else {}
        )
        registration_root = source_plugin_root or self.plugin_root
        cache_family_root = preverified_family_root or native_runtime.plugin_cache_family_root(
            registration_root
        )
        if cache_family_root is not None and (
            source_plugin_root is not None or not self._uses_stable_runtime()
        ):
            native_runtime.require_canonical_plugin_registration(
                registration_root,
                cache_family_root,
            )
        # Status/UI polls can use the process-local verifier memo. Launch and
        # update handoff may not: this is the execution authorization boundary.
        status = preverified_status or self.status(force_verify=True)
        app_path = status.get("appPath")
        if (
            self.spec.launch_strategy == "windows-detached-process"
            and status.get("source") != "plugin-bundled"
        ):
            raise native_runtime.NativeRuntimeError(
                "plugin-bundled ChatGPT Meetings is required on Windows"
            )
        if require_plugin_bundled and status.get("source") != "plugin-bundled":
            raise native_runtime.NativeRuntimeError(
                "plugin-bundled ChatGPT Meetings is unavailable"
            )
        if not status.get("installed") or not isinstance(app_path, str):
            raise native_runtime.NativeRuntimeError("ChatGPT Meetings is not installed")
        if required_runtime_identity is not None and (
            app_path != required_runtime_identity.get("appPath")
            or not isinstance(required_runtime_identity.get("_executableSHA256"), str)
            or status.get("_executableSHA256") != required_runtime_identity.get("_executableSHA256")
        ):
            raise native_runtime.NativeRuntimeError("native recovery runtime identity changed")
        if guarded_executable is not None:
            try:
                resolved_app_path = Path(app_path).resolve(strict=True)
            except OSError as exc:
                raise native_runtime.NativeRuntimeError(
                    "guarded Windows executable identity is unavailable"
                ) from exc
            guarded_digest = native_runtime.sha256_regular_file(guarded_executable)
            if (
                resolved_app_path != guarded_executable
                or status.get("_executableSHA256") != guarded_digest
            ):
                raise native_runtime.NativeRuntimeError(
                    "guarded Windows executable identity does not match"
                )
        family_root = cache_family_root if status.get("source") == "plugin-bundled" else None
        if self.spec.launch_strategy == "windows-detached-process" and family_root is None:
            raise native_runtime.NativeRuntimeError(
                "canonical plugin cache registration is required on Windows"
            )
        raw_executable_sha256 = status.get("_executableSHA256")
        executable_sha256 = (
            raw_executable_sha256 if isinstance(raw_executable_sha256, str) else None
        )
        if self.spec.launch_strategy == "windows-detached-process" and (
            executable_sha256 is None
            or native_runtime.SHA256_HEX_PATTERN.fullmatch(executable_sha256) is None
        ):
            raise native_runtime.NativeRuntimeError(
                "verified Windows artifact identity is unavailable"
            )

        def resolve_owner(*, recover_unhealthy: bool = False) -> str:
            if required_codex_launch_context is None:
                assert family_root is not None
                return native_runtime._resolve_plugin_handoff_for_launch(
                    Path(app_path),
                    family_root,
                    self.spec,
                    executable_sha256,
                    source_plugin_root=source_plugin_root,
                    **(recovery_arguments if recover_unhealthy else {}),
                )
            from companion_client import companion_client
            from control_client import ControlUnavailable, owner_lock_state

            try:
                if owner_lock_state() in {"missing", "available"}:
                    return "absent"
                # Preserve the device-owned current-image reuse contract.
                # Authentication may not authorize replacement of another image.
                companion_client(runtime=status)
            except ControlUnavailable as error:
                raise native_runtime.NativeRuntimeError(
                    "native recovery owner could not be authenticated"
                ) from error
            return "current"

        handoff_disposition: str | None = None
        if family_root is not None or required_codex_launch_context is not None:
            handoff_disposition = resolve_owner(recover_unhealthy=True)
            if (
                require_existing_owner
                and handoff_disposition == "absent"
                and not authenticated_handoff_completed
            ):
                raise native_runtime.NativeRuntimeQuitRequired(
                    "authenticated ChatGPT Meetings owner disappeared before update"
                )

            if handoff_disposition == "current":
                if self.spec.launch_strategy == "windows-detached-process":
                    assert family_root is not None
                    if executable_sha256 is None:
                        raise native_runtime.NativeRuntimeError(
                            "verified Windows artifact identity is unavailable"
                        )
                    native_runtime._require_windows_owner_matches_verified_image(
                        app_path,
                        family_root,
                        executable_sha256,
                    )
                    return {**status, "launching": False, "reused": True}
                if isolation is None:
                    # A proven Darwin owner already holds the exact image.
                    # Reopening it on every explicit setup/Start recovery
                    # adds LaunchServices churn and can duplicate UI state.
                    return {**status, "launching": False, "reused": True}

        if self.spec.launch_strategy == "windows-detached-process":
            if family_root is None:
                raise native_runtime.NativeRuntimeError(
                    "canonical plugin cache registration is required on Windows"
                )
            if executable_sha256 is None:
                raise native_runtime.NativeRuntimeError(
                    "verified Windows artifact identity is unavailable"
                )
            creation_flags = (
                getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
                | getattr(subprocess, "DETACHED_PROCESS", 0)
                | getattr(subprocess, "CREATE_NO_WINDOW", 0)
            )
            launch_creation_flags = creation_flags if native_runtime._is_windows_host() else None
            launch_environment = native_runtime.windows_companion_environment()

            # The Windows-only canonical-family guard above makes this exact
            # key mandatory for every supported launch.
            pending_child_key = (
                str(Path(app_path)),
                str(family_root),
                executable_sha256,
            )

            def authorize_spawn() -> None:
                revalidate()
                if source_plugin_root is not None or not self._uses_stable_runtime():
                    native_runtime.require_canonical_plugin_registration(
                        registration_root,
                        family_root,
                    )
                else:
                    native_runtime.stable_runtime_verification_manifest(
                        Path(app_path),
                        self.spec,
                        require_active=True,
                    )

            for attempt in range(native_runtime.WINDOWS_LAUNCH_ATTEMPT_LIMIT):
                pending_child: native_runtime._WindowsPendingChild | None = None
                try:
                    # The resolver immediately above revalidated canonical
                    # registration before this process-local adoption.
                    pending_child = native_runtime._claim_or_spawn_windows_pending_child(
                        pending_child_key,
                        app_path,
                        authorize_spawn,
                        environment=launch_environment,
                        creation_flags=launch_creation_flags,
                        **(
                            {"required_codex_launch_context": required_codex_launch_context}
                            if required_codex_launch_context is not None
                            else {}
                        ),
                    )
                    process = pending_child.process
                except OSError as exc:
                    raise native_runtime.NativeRuntimeError(
                        "could not launch ChatGPT Meetings"
                    ) from exc

                owner_confirmation_deadline = (
                    time.monotonic() + native_runtime.WINDOWS_LAUNCH_OWNER_CONFIRM_TIMEOUT_SECONDS
                )
                try:
                    while True:
                        try:
                            child_return_code = process.wait(
                                timeout=native_runtime.WINDOWS_CHILD_EXIT_CHECK_TIMEOUT_SECONDS
                            )
                        except subprocess.TimeoutExpired as wait_error:
                            try:
                                handoff_disposition = resolve_owner()
                            except native_runtime.NativeRuntimeUpdateDeferred as exc:
                                if process.poll() is None:
                                    raise native_runtime.NativeRuntimeLaunchPendingUpdateDeferred(
                                        "older ChatGPT Meetings companion is busy "
                                        "while launch remains in flight"
                                    ) from exc
                                raise
                            except native_runtime.NativeRuntimeQuitRequired as exc:
                                if process.poll() is None:
                                    raise native_runtime.NativeRuntimeLaunchPendingQuitRequired(
                                        "older ChatGPT Meetings companion must quit "
                                        "while launch remains in flight"
                                    ) from exc
                                raise
                            except native_runtime.NativeRuntimeError as exc:
                                # Resolver failure is fail-closed for any
                                # future spawn, but cannot revoke this exact
                                # live child without an unsafe hard kill.
                                if process.poll() is None:
                                    raise native_runtime.NativeRuntimeLaunchPending(
                                        "ChatGPT Meetings launch remains in flight "
                                        "after owner authorization failed"
                                    ) from exc
                                raise
                            if handoff_disposition == "current":
                                native_runtime._require_windows_owner_matches_verified_image(
                                    app_path,
                                    family_root,
                                    executable_sha256,
                                )
                                native_runtime._release_windows_pending_child_observer(
                                    pending_child_key,
                                    pending_child,
                                    # The resolver proves an owner, but
                                    # does not expose whether it is this
                                    # exact child or a concurrent winner.
                                    # Keep a still-live child tracked until
                                    # it exits or is observed again.
                                    keep_if_alive=True,
                                )
                                pending_child = None
                                return {
                                    **status,
                                    "launching": False,
                                    "reused": True,
                                }
                            if time.monotonic() >= owner_confirmation_deadline:
                                # Liveness is not authenticated ownership.
                                # Foreground callers receive an error while
                                # initialize adopts the pending child through
                                # its existing poll/cooldown lane.
                                raise native_runtime.NativeRuntimeLaunchPending(
                                    "ChatGPT Meetings launch remains in flight "
                                    "without an authenticated owner"
                                ) from wait_error
                            continue

                        native_runtime._release_windows_pending_child_observer(
                            pending_child_key,
                            pending_child,
                            keep_if_alive=False,
                        )
                        pending_child = None
                        if child_return_code != 0:
                            raise _NativeRuntimeLaunchRejected("could not launch ChatGPT Meetings")

                        # A duplicate Rust child exits zero without publishing
                        # local control after another launcher wins the kernel
                        # lease. Never report that losing PID as launching:
                        # re-resolve the exact owner (and canonical
                        # registration) before retrying.
                        handoff_disposition = resolve_owner()
                        if handoff_disposition == "current":
                            native_runtime._require_windows_owner_matches_verified_image(
                                app_path,
                                family_root,
                                executable_sha256,
                            )
                            return {
                                **status,
                                "launching": False,
                                "reused": True,
                            }
                        break
                except BaseException:
                    if pending_child is not None:
                        native_runtime._release_windows_pending_child_observer(
                            pending_child_key,
                            pending_child,
                            keep_if_alive=True,
                        )
                    raise

                if attempt + 1 == native_runtime.WINDOWS_LAUNCH_ATTEMPT_LIMIT:
                    raise native_runtime.NativeRuntimeError(
                        "ChatGPT Meetings exited before local control became available"
                    )

            raise AssertionError("unreachable Windows launch attempt state")

        # Keep bootstrap in the background without asking LaunchServices to
        # hide the accessory app; hidden state can suppress its nonactivating
        # recording and reminder panels.
        if family_root is not None and (
            source_plugin_root is not None or not self._uses_stable_runtime()
        ):
            native_runtime.require_canonical_plugin_registration(registration_root, family_root)
        open_flag = "-g"
        if required_codex_launch_context is not None or (
            family_root is not None and handoff_disposition != "current"
        ):
            open_flag = "-ng"
        executable: Path | None = None
        launch_arguments: list[str] = []
        try:
            if isolation is not None:
                # LaunchServices cannot carry a private HOME/CODEX_HOME tree
                # into the exact app process. In this explicit Dev/E2E lane,
                # execute only the already-verified packaged executable and
                # pass a credential-free allowlisted environment.
                _, executable, _ = native_runtime._load_app_metadata(Path(app_path), self.spec)
            elif required_codex_launch_context is None:
                launch_arguments = native_runtime._darwin_codex_launch_arguments()
            if family_root is not None:
                # Metadata and launcher-context preparation can yield. Keep
                # the force-verified fingerprint/digest and canonical
                # activation checks at the final authorizing boundary so a
                # same-path replacement cannot reach either spawn path.
                if self._uses_stable_runtime():
                    active_artifact, active_manifest = (
                        native_runtime._read_active_stable_generation(
                            native_runtime.stable_runtime_root(), self.spec
                        )
                    )
                    if active_artifact != Path(app_path):
                        raise native_runtime.NativeRuntimeError(
                            "native app changed during update handoff"
                        )
                    verified_fingerprint, _, _, verified_executable_sha256 = (
                        native_runtime._verified_stable_artifact_metadata(
                            active_artifact,
                            active_manifest,
                            self.spec,
                            force_verify=True,
                        )
                    )
                else:
                    verified_fingerprint, _, _, verified_executable_sha256 = (
                        self._verified_plugin_metadata(Path(app_path), force_verify=True)
                    )
                if (
                    verified_fingerprint != status.get("_artifactFingerprint")
                    or verified_executable_sha256 != executable_sha256
                ):
                    raise native_runtime.NativeRuntimeError(
                        "native app changed during update handoff"
                    )
                if source_plugin_root is not None or not self._uses_stable_runtime():
                    native_runtime.require_canonical_plugin_registration(
                        registration_root, family_root
                    )
            if isolation is not None:
                if executable is None:
                    raise native_runtime.NativeRuntimeError(
                        "native executable metadata is unavailable"
                    )
                revalidate()
                process = native_runtime._spawn_registered_e2e_companion(
                    executable,
                    isolation=isolation,
                    capture_mode=capture_mode,
                )
                return {
                    **status,
                    "launching": True,
                    "launchPid": process.pid,
                    "e2eIsolated": True,
                }
            revalidate()
            if required_codex_launch_context is not None:
                launch_arguments = native_runtime._darwin_codex_launch_arguments(
                    required_codex_launch_context=required_codex_launch_context
                )
            launcher = subprocess.Popen(
                [
                    "/usr/bin/open",
                    open_flag,
                    app_path,
                    *native_runtime.darwin_companion_ca_arguments(),
                    *launch_arguments,
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True,
            )
            # /usr/bin/open normally exits immediately after LaunchServices
            # accepts the request. Waiting only for that short handoff lets a
            # non-zero result become a retryable bootstrap failure instead of
            # being silently reported as "launching". If LaunchServices is
            # merely slow, keep the launch non-blocking after this small
            # bounded observation window.
            try:
                open_return_code = launcher.wait(
                    timeout=native_runtime.OPEN_EXIT_CHECK_TIMEOUT_SECONDS
                )
            except subprocess.TimeoutExpired:
                open_return_code = None
            if isinstance(open_return_code, int) and open_return_code != 0:
                raise _NativeRuntimeLaunchRejected("could not launch ChatGPT Meetings")
        except OSError as exc:
            raise native_runtime.NativeRuntimeError("could not launch ChatGPT Meetings") from exc
        return {**status, "launching": True}


@dataclass(frozen=True)
class PreparedCompanionReplacement:
    manager: RuntimeManager
    identity: Mapping[str, object]
    codex_context: tuple[str, str]

    @classmethod
    def prepare(cls, manager: RuntimeManager) -> PreparedCompanionReplacement:
        return cls(
            manager,
            manager.prepare_plugin_bundled_replacement(),
            manager.require_codex_launch_context(),
        )

    def revalidate(self) -> None:
        current = self.manager.prepare_plugin_bundled_replacement()
        if (
            current.get("appPath") != self.identity.get("appPath")
            or not isinstance(self.identity.get("_executableSHA256"), str)
            or current.get("_executableSHA256") != self.identity.get("_executableSHA256")
            or self.manager.require_codex_launch_context() != self.codex_context
        ):
            raise native_runtime.NativeRuntimeError("prepared native replacement changed")

    def launch(self) -> Mapping[str, object]:
        self.revalidate()
        self.manager.activate_prepared_plugin_bundled_replacement(self.identity)
        return self.manager.launch_current(
            require_plugin_bundled=True,
            required_codex_launch_context=self.codex_context,
            required_runtime_identity=self.identity,
        )
