"""Typed observations for authenticated, native-owned companion handoff."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

from recording_control_action_contract import RECORDING_CONTROL_SAFE_INTEGER_MAX
from recording_status_contract import RecordingState, is_recording_state

from helpers import is_json


@dataclass(frozen=True, repr=False)
class HandoffStateObservation:
    """One shape-checked native state and its bounded progress observation.

    Native companions own their upload queues, receipts, phases, and completion.
    Only their bounded pending-count observation participates in the existing
    chronological owner fence; queue contents and receipt metadata stay opaque.
    This shape check never authenticates its input; callers must first verify
    the native owner's authenticated stream state or request-bound response.
    """

    wire: Mapping[str, object]
    contract: RecordingState | None
    pending_count: int

    @classmethod
    def from_wire(
        cls,
        value: object,
    ) -> HandoffStateObservation | None:
        """Narrow a state shape; the caller separately owns wire authentication."""

        if not is_json(value) or "upload" not in value:
            return None
        upload = value["upload"]
        if not is_json(upload) or "pendingCount" not in upload:
            return None
        pending_count = upload["pendingCount"]
        if type(pending_count) is not int or not (
            0 <= pending_count <= RECORDING_CONTROL_SAFE_INTEGER_MAX
        ):
            return None
        return cls(
            wire=value,
            contract=value if is_recording_state(value) else None,
            pending_count=pending_count,
        )


@dataclass(frozen=True, repr=False)
class HandoffProgress:
    """Chronological observations from independently authenticated native states."""

    initial: HandoffStateObservation
    response: HandoffStateObservation
    current: HandoffStateObservation

    @classmethod
    def from_states(
        cls,
        *,
        initial: object,
        response: object,
        current: object,
    ) -> HandoffProgress | None:
        """Reject malformed shapes or work introduced after the earlier observation."""

        initial_snapshot = HandoffStateObservation.from_wire(initial)
        response_snapshot = HandoffStateObservation.from_wire(response)
        current_snapshot = HandoffStateObservation.from_wire(current)
        if (
            initial_snapshot is None
            or response_snapshot is None
            or current_snapshot is None
            or not (
                current_snapshot.pending_count
                <= response_snapshot.pending_count
                <= initial_snapshot.pending_count
            )
        ):
            return None
        return cls(
            initial=initial_snapshot,
            response=response_snapshot,
            current=current_snapshot,
        )
