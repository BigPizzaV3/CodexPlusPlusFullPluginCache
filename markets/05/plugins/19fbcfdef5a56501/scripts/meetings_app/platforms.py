"""Typed per-platform adapters for native Meetings app ownership."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Generic, Literal, NoReturn, Protocol, TypeVar

from meetings_app.models import NativeAppRuntime
from native_runtime_types import PlatformRuntimeSpec
from recording_control_action_contract import ControlPlatform

OwnerT = TypeVar("OwnerT")
ProofT = TypeVar("ProofT")


@dataclass(frozen=True)
class CompatibleOwnerOperations(Generic[OwnerT, ProofT]):
    """Injected handoff operations keep this platform layer dependency-free."""

    authenticate_darwin: Callable[[NativeAppRuntime], OwnerT]
    authenticate_windows: Callable[[NativeAppRuntime, bool, ProofT | None], OwnerT]
    preverify_windows: Callable[[NativeAppRuntime], ProofT]
    reject: Callable[[str], NoReturn]


class CompatibleOwnerPlatformHandler(Protocol):
    """Typed per-machine adapter; shared handoff policy stays outside."""

    @property
    def runtime(self) -> NativeAppRuntime | None: ...

    @property
    def platform(self) -> ControlPlatform: ...

    @property
    def spec(self) -> PlatformRuntimeSpec | None: ...

    @property
    def family(self) -> Literal["darwin", "windows", "unsupported"]: ...

    def authenticate_compatible_owner(
        self,
        operations: CompatibleOwnerOperations[OwnerT, ProofT],
        *,
        allow_durable_handoff: bool = False,
        preverified_source: ProofT | None = None,
    ) -> OwnerT: ...

    def preverify_staged_update_source(
        self,
        operations: CompatibleOwnerOperations[OwnerT, ProofT],
    ) -> ProofT | None: ...


@dataclass(frozen=True)
class DarwinCompatibleOwnerPlatformHandler:
    runtime: NativeAppRuntime
    family: Literal["darwin"] = "darwin"

    @property
    def platform(self) -> ControlPlatform:
        return self.runtime.platform

    @property
    def spec(self) -> PlatformRuntimeSpec:
        return self.runtime.spec

    def authenticate_compatible_owner(
        self,
        operations: CompatibleOwnerOperations[OwnerT, ProofT],
        *,
        allow_durable_handoff: bool = False,
        preverified_source: ProofT | None = None,
    ) -> OwnerT:
        if allow_durable_handoff or preverified_source is not None:
            operations.reject("native update platform is unsupported")
        return operations.authenticate_darwin(self.runtime)

    def preverify_staged_update_source(
        self,
        operations: CompatibleOwnerOperations[OwnerT, ProofT],
    ) -> None:
        return None


@dataclass(frozen=True)
class WindowsCompatibleOwnerPlatformHandler:
    runtime: NativeAppRuntime
    family: Literal["windows"] = "windows"

    @property
    def platform(self) -> ControlPlatform:
        return self.runtime.platform

    @property
    def spec(self) -> PlatformRuntimeSpec:
        return self.runtime.spec

    def authenticate_compatible_owner(
        self,
        operations: CompatibleOwnerOperations[OwnerT, ProofT],
        *,
        allow_durable_handoff: bool = False,
        preverified_source: ProofT | None = None,
    ) -> OwnerT:
        return operations.authenticate_windows(
            self.runtime,
            allow_durable_handoff,
            preverified_source,
        )

    def preverify_staged_update_source(
        self,
        operations: CompatibleOwnerOperations[OwnerT, ProofT],
    ) -> ProofT:
        return operations.preverify_windows(self.runtime)


@dataclass(frozen=True)
class UnsupportedCompatibleOwnerPlatformHandler:
    runtime: None = None
    platform: ControlPlatform = ControlPlatform.UNKNOWN
    spec: None = None
    family: Literal["unsupported"] = "unsupported"

    def authenticate_compatible_owner(
        self,
        operations: CompatibleOwnerOperations[OwnerT, ProofT],
        *,
        allow_durable_handoff: bool = False,
        preverified_source: ProofT | None = None,
    ) -> NoReturn:
        operations.reject("native update platform is unsupported")

    def preverify_staged_update_source(
        self,
        operations: CompatibleOwnerOperations[OwnerT, ProofT],
    ) -> NoReturn:
        operations.reject("native update platform is unsupported")


def _darwin_handler(runtime: NativeAppRuntime) -> CompatibleOwnerPlatformHandler:
    return DarwinCompatibleOwnerPlatformHandler(runtime)


def _windows_handler(runtime: NativeAppRuntime) -> CompatibleOwnerPlatformHandler:
    return WindowsCompatibleOwnerPlatformHandler(runtime)


@dataclass(frozen=True)
class HandoffPlatformRegistration:
    """One exhaustive machine entry binds host validation to its handler."""

    expected_host: Literal["darwin", "win32"]
    factory: Callable[[NativeAppRuntime], CompatibleOwnerPlatformHandler]


SUPPORTED_NATIVE_HANDOFF_PLATFORMS = frozenset(
    platform for platform in ControlPlatform if platform is not ControlPlatform.UNKNOWN
)
HANDLER_REGISTRATIONS: dict[ControlPlatform, HandoffPlatformRegistration] = {
    ControlPlatform.DARWIN_UNIVERSAL: HandoffPlatformRegistration("darwin", _darwin_handler),
    ControlPlatform.DARWIN_ARM64: HandoffPlatformRegistration("darwin", _darwin_handler),
    ControlPlatform.DARWIN_X64: HandoffPlatformRegistration("darwin", _darwin_handler),
    ControlPlatform.WINDOWS_X64: HandoffPlatformRegistration("win32", _windows_handler),
    ControlPlatform.WINDOWS_ARM64: HandoffPlatformRegistration("win32", _windows_handler),
}
if frozenset(HANDLER_REGISTRATIONS) != SUPPORTED_NATIVE_HANDOFF_PLATFORMS:
    raise RuntimeError("native handoff platform mapping is incomplete")


def registration_for(platform: ControlPlatform) -> HandoffPlatformRegistration | None:
    """Return one supported registration without granting unknown authority."""

    if platform not in HANDLER_REGISTRATIONS:
        return None
    return HANDLER_REGISTRATIONS[platform]


def is_windows_registration(registration: HandoffPlatformRegistration) -> bool:
    """Keep the nonthrowing Meetings callsite hint tied to the registry."""

    return registration.factory is _windows_handler
