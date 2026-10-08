"""Typed contracts for private native runtime discovery and launch results."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Literal, TypeAlias, TypedDict

from recording_control_action_contract import ControlPlatformWire

_NativePathIdentityValue = str | int | None
NativePathIdentity = tuple[_NativePathIdentityValue, ...]
NativeArtifactFingerprint = tuple[NativePathIdentity, ...]


class MaterializeVerificationPhase(str, Enum):
    STAGED_SIGNATURE = "staged_signature"
    STAGED_IDENTITY = "staged_identity"
    GENERATION_MANIFEST = "generation_manifest"
    GENERATION_IDENTITY = "generation_identity"


@dataclass(frozen=True)
class PlatformRuntimeSpec:
    """Portable contract for one native companion artifact.

    The descriptor stays independent from the installer so Darwin bundles and
    Windows executables share one portable artifact and authenticated-control
    contract while retaining platform-specific artifact validation and launch
    boundaries. Companion feature availability comes from its authenticated
    live capability negotiation rather than this historical generated profile.
    """

    platform_key: ControlPlatformWire
    manifest_keys: tuple[ControlPlatformWire, ...]
    artifact_kind: str
    artifact_name: str
    artifact_path_kind: str
    identity_kind: str
    identity_value: str
    capabilities: tuple[str, ...]
    launch_strategy: str


class _RequiredDarwinRuntimeVerification(TypedDict):
    """Immutable payload identity shared by production and development apps."""

    artifactSha256: str
    embeddedReceiptSha256: str


class DarwinRuntimeVerification(_RequiredDarwinRuntimeVerification, total=False):
    """Exactly one profile-specific signing identity accompanies each payload."""

    teamIdentifier: str
    signingAuthority: str


class AuthenticodeSigningPolicy(TypedDict):
    """Pinned Authenticode identity for a production Windows executable."""

    kind: Literal["authenticode"]
    subject: str
    thumbprint: str


class UnsignedTestSigningPolicy(TypedDict):
    """Intentionally unsigned Windows policy; trust depends on runtime provenance."""

    kind: Literal["unsigned-test"]


WindowsSigningPolicy: TypeAlias = AuthenticodeSigningPolicy | UnsignedTestSigningPolicy


class WindowsDistributionRelease(TypedDict):
    """Immutable release identity carried by the Windows distribution proof."""

    tag: str
    tagSha: str
    version: str


class WindowsDistributionStorage(TypedDict):
    """Reviewed Azure location for a production Windows distribution."""

    provider: Literal["azure-blob"]
    accountName: str
    containerName: str


class WindowsDistributionArtifact(TypedDict):
    """Digest and byte length for one reviewed distribution artifact."""

    sha256: str
    sizeBytes: int


class WindowsDistributionBinding(TypedDict):
    """Cross-file proof binding a Windows executable to its reviewed release."""

    kind: Literal["chatgpt-meetings-windows-production-bundle"]
    release: WindowsDistributionRelease
    storage: WindowsDistributionStorage
    lock: WindowsDistributionArtifact
    descriptor: WindowsDistributionArtifact
    composite: WindowsDistributionArtifact


class _RequiredWindowsRuntimeVerification(TypedDict):
    """Fields present for every supported Windows signing policy."""

    signing: WindowsSigningPolicy


class WindowsRuntimeVerification(_RequiredWindowsRuntimeVerification, total=False):
    """Windows signing proof with an optional production distribution binding."""

    windowsDistribution: WindowsDistributionBinding
    thirdPartyLicensesSha256: str


StableRuntimeVerification: TypeAlias = DarwinRuntimeVerification | WindowsRuntimeVerification


class StableGenerationManifest(TypedDict):
    """Validated private manifest for one immutable native runtime generation."""

    schemaVersion: int
    platform: ControlPlatformWire
    artifactName: str
    generation: str
    version: str
    buildTimestamp: str | None
    executableSha256: str
    verification: StableRuntimeVerification


class _RequiredNativeRuntimeStatus(TypedDict):
    """Fields returned by every native runtime discovery result."""

    installed: bool
    version: str | None
    buildTimestamp: str | None
    appPath: str | None
    artifactPath: str | None
    platform: ControlPlatformWire
    artifactKind: str
    artifactPathKind: str
    capabilities: list[str]


class NativeRuntimeStatus(_RequiredNativeRuntimeStatus, total=False):
    """Private verified runtime facts shared by discovery and launch callers."""

    releaseVersion: str
    source: Literal["plugin-bundled"]
    updated: bool
    launching: bool
    reused: bool
    launchPid: int
    e2eIsolated: bool
    _artifactFingerprint: NativeArtifactFingerprint
    _executableSHA256: str
    _executableDevice: int
    _executableInode: int
    _sourcePluginRoot: str


class _RequiredPublicNativeRuntimeStatus(TypedDict):
    """Fields always exposed by the path-free runtime status projection."""

    installed: bool
    version: str | None
    buildTimestamp: str | None
    platform: str | None
    artifactKind: str | None
    capabilities: list[str]
    source: Literal["plugin-bundled"] | None


class PublicNativeRuntimeStatus(_RequiredPublicNativeRuntimeStatus, total=False):
    """Runtime facts safe to expose through MCP and model-visible payloads."""

    releaseVersion: str
    updated: bool
    launching: bool
    updateError: Literal["Native update check is unavailable"]
