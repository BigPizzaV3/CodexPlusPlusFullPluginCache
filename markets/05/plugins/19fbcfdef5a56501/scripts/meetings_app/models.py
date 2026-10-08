"""Frozen typed native Meetings app machine facts."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

from native_runtime_types import PlatformRuntimeSpec
from recording_control_action_contract import ControlPlatform
from recording_status_contract import RecordingDetails, is_recording_details

from helpers import is_json


@dataclass(frozen=True, repr=False)
class NativeAppRuntime:
    """An unverified runtime candidate with a validated host-bound machine spec."""

    status: Mapping[str, object]
    platform: ControlPlatform
    spec: PlatformRuntimeSpec


@dataclass(frozen=True, repr=False)
class NativeCaptureObservation:
    """Shape-checked capture fields with an optional generated modern contract.

    Historical Windows recording identifiers predate the generated recording
    schema, so a missing contract is not itself evidence of unsafe capture.
    The surrounding caller must still authenticate the native stream state.
    """

    wire: dict[str, object]
    contract: RecordingDetails | None

    @classmethod
    def from_value(cls, value: object) -> NativeCaptureObservation | None:
        if not is_json(value):
            return None
        return cls(
            wire=value,
            contract=value if is_recording_details(value) else None,
        )
