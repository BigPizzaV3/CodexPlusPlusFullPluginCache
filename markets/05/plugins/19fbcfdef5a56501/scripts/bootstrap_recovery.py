"""Shared bootstrap recovery policy without application-module dependencies."""

from __future__ import annotations

import threading
from dataclasses import dataclass, field
from enum import Enum
from typing import TypedDict


class BootstrapFailure(Enum):
    """Typed recovery policy with the existing privacy-safe telemetry labels."""

    LAUNCHER_REJECTED = ("launcher_rejected", True)
    STABLE_LOCK_BUSY = ("lock_contention", True)
    LOCK_CONTENTION = ("lock_contention", False)
    REGISTRATION_UNAVAILABLE = ("registration_unavailable", True)
    ARTIFACT_MISSING = ("artifact_missing", False)
    MISSING_RESOURCE = ("missing_resource", False)
    PERMISSION_DENIED = ("permission_denied", False)
    TIMEOUT = ("timeout", True)
    CONNECTION_UNAVAILABLE = ("io_error", True)
    IO_ERROR = ("io_error", False)
    RUNTIME_REJECTED = ("runtime_rejected", False)
    UNEXPECTED = ("unexpected", False)

    def __init__(self, sentry_reason: str, retryable: bool) -> None:
        self.sentry_reason = sentry_reason
        self.retryable = retryable


class BootstrapFailureDiagnostics(TypedDict):
    """Fixed diagnostic dimensions; no raw error messages or paths."""

    failure_operation: str
    resource_role: str
    os_error_code: str


@dataclass
class BootstrapRecoveryState:
    """One failure episode, guarded by the bootstrap scheduler's shared lock."""

    retry_delay_seconds: float = 0.0
    reported_failures: set[BootstrapFailure] = field(default_factory=set[BootstrapFailure])
    handoff_reported: bool = False
    last_failure: BootstrapFailure | None = None
    last_failure_diagnostics: BootstrapFailureDiagnostics | None = None


lock = threading.Lock()
state = BootstrapRecoveryState()


def record_authenticated_companion_recovery() -> None:
    """Reset the episode after a selected-owner connection or verified handoff."""

    global state
    with lock:
        state = BootstrapRecoveryState()
