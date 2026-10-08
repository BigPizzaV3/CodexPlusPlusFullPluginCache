"""Conservative, host-optional context preflight for Empire external routing.

This module is deliberately side-effect free. It does not read Codex history,
dispatch a provider request, reserve money, compact a thread, or create a new
thread. Callers may attach its bounded receipt to route previews and later use
the same contract for an explicitly approved enforcement phase.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class ContextPolicyError(ValueError):
    """Raised when context-policy inputs are internally inconsistent."""


class ContextDecision(str, Enum):
    INLINE_SAFE = "inline_safe"
    INLINE_SHAPED = "inline_shaped"
    ARTIFACT_DELIVERY = "artifact_delivery"
    COMPACT_BEFORE_DISPATCH = "compact_before_dispatch"
    FRESH_THREAD_REQUIRED = "fresh_thread_required"
    ROUTE_REJECTED = "route_rejected"


class ThresholdState(str, Enum):
    UNKNOWN = "unknown"
    HEALTHY = "healthy"
    WARNING = "warning"
    SHAPE = "shape"
    CHECKPOINT = "checkpoint"
    CONTINUATION = "continuation"
    EMERGENCY = "emergency"


@dataclass(frozen=True)
class ResponseClassSpec:
    name: str
    minimum_tokens: int
    target_tokens: int
    maximum_tokens: int
    inline_summary_maximum_tokens: int | None = None


RESPONSE_CLASSES: dict[str, ResponseClassSpec] = {
    "micro": ResponseClassSpec("micro", 128, 300, 450),
    "compact": ResponseClassSpec("compact", 350, 700, 1_000),
    "standard": ResponseClassSpec("standard", 900, 1_600, 2_500),
    "artifact": ResponseClassSpec("artifact", 128, 300, 500, 500),
}


@dataclass(frozen=True)
class ContextPolicy:
    warning: float = 0.70
    shape: float = 0.75
    checkpoint: float = 0.80
    continuation: float = 0.85
    emergency: float = 0.90
    fixed_operational_tokens: int = 1_200
    synthesis_tokens: int = 900
    tool_result_tokens: int = 600
    total_reserve_cap_ratio: float = 0.20

    def __post_init__(self) -> None:
        thresholds = (
            self.warning,
            self.shape,
            self.checkpoint,
            self.continuation,
            self.emergency,
        )
        if tuple(sorted(thresholds)) != thresholds or not all(
            0 < value <= 1 for value in thresholds
        ):
            raise ContextPolicyError("Context thresholds must increase inside (0, 1]")
        if min(
            self.fixed_operational_tokens,
            self.synthesis_tokens,
            self.tool_result_tokens,
        ) < 0:
            raise ContextPolicyError("Context reserves must be non-negative")
        if not 0 <= self.total_reserve_cap_ratio <= 1:
            raise ContextPolicyError("Reserve cap ratio must be inside [0, 1]")


UNCERTAINTY_MARGIN = {
    "high": 0.03,
    "medium": 0.08,
    "low": 0.15,
    "unknown": 0.25,
}


@dataclass(frozen=True)
class ContextMeasurement:
    context_limit_tokens: int | None
    current_usage_tokens: int | None
    usage_ratio: float | None
    measurement_source: str
    measurement_confidence: str
    measured_at: str

    def to_dict(self) -> dict[str, Any]:
        remaining = (
            max(0, self.context_limit_tokens - self.current_usage_tokens)
            if self.context_limit_tokens is not None
            and self.current_usage_tokens is not None
            else None
        )
        return {
            "context_limit_tokens": self.context_limit_tokens,
            "current_usage_tokens": self.current_usage_tokens,
            "remaining_tokens": remaining,
            "usage_ratio": self.usage_ratio,
            "measurement_source": self.measurement_source,
            "measurement_confidence": self.measurement_confidence,
            "measured_at": self.measured_at,
        }


@dataclass(frozen=True)
class ResponseBudget:
    requested_class: str
    recommended_class: str
    minimum_tokens: int
    target_tokens: int
    maximum_tokens: int
    allocated_tokens: int
    output_limit_supported: bool
    limiting_factors: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "requested_class": self.requested_class,
            "recommended_class": self.recommended_class,
            "minimum_tokens": self.minimum_tokens,
            "target_tokens": self.target_tokens,
            "maximum_tokens": self.maximum_tokens,
            "allocated_tokens": self.allocated_tokens,
            "output_limit_supported": self.output_limit_supported,
            "limiting_factors": list(self.limiting_factors),
        }


@dataclass(frozen=True)
class ContextProjection:
    adjusted_current_usage_tokens: int | None
    pending_input_tokens: int
    external_output_tokens: int
    reasoning_allowance_tokens: int
    reserve_tokens: int
    projected_usage_tokens: int | None
    projected_usage_ratio: float | None
    threshold_state: ThresholdState
    decision: ContextDecision
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "adjusted_current_usage_tokens": self.adjusted_current_usage_tokens,
            "pending_input_tokens": self.pending_input_tokens,
            "external_output_tokens": self.external_output_tokens,
            "reasoning_allowance_tokens": self.reasoning_allowance_tokens,
            "reserve_tokens": self.reserve_tokens,
            "projected_usage_tokens": self.projected_usage_tokens,
            "projected_usage_ratio": self.projected_usage_ratio,
            "threshold_state": self.threshold_state.value,
            "decision": self.decision.value,
            "reason": self.reason,
        }


def estimate_text_tokens(value: str, fixed_overhead_tokens: int = 0) -> int:
    """Return the existing Empire four-UTF-8-bytes-per-token estimate."""
    if fixed_overhead_tokens < 0:
        raise ContextPolicyError("Fixed token overhead must be non-negative")
    return max(1, math.ceil(len(value.encode("utf-8")) / 4)) + fixed_overhead_tokens


def measure_context(
    *,
    context_limit_tokens: int | None = None,
    current_usage_tokens: int | None = None,
    measurement_source: str = "unknown",
    measurement_confidence: str = "unknown",
    measured_at: str | None = None,
) -> ContextMeasurement:
    if (context_limit_tokens is None) != (current_usage_tokens is None):
        raise ContextPolicyError(
            "Context limit and current usage must be supplied together"
        )
    if context_limit_tokens is not None and context_limit_tokens <= 0:
        raise ContextPolicyError("Context limit must be positive")
    if current_usage_tokens is not None and current_usage_tokens < 0:
        raise ContextPolicyError("Current context usage must be non-negative")
    if measurement_confidence not in UNCERTAINTY_MARGIN:
        raise ContextPolicyError("Unknown context measurement confidence")
    if context_limit_tokens is None:
        measurement_source = "unknown"
        measurement_confidence = "unknown"
    ratio = (
        current_usage_tokens / context_limit_tokens
        if current_usage_tokens is not None and context_limit_tokens is not None
        else None
    )
    return ContextMeasurement(
        context_limit_tokens=context_limit_tokens,
        current_usage_tokens=current_usage_tokens,
        usage_ratio=ratio,
        measurement_source=measurement_source,
        measurement_confidence=measurement_confidence,
        measured_at=measured_at or datetime.now(timezone.utc).isoformat(),
    )


def threshold_state(ratio: float | None, policy: ContextPolicy) -> ThresholdState:
    if ratio is None:
        return ThresholdState.UNKNOWN
    if ratio >= policy.emergency:
        return ThresholdState.EMERGENCY
    if ratio >= policy.continuation:
        return ThresholdState.CONTINUATION
    if ratio >= policy.checkpoint:
        return ThresholdState.CHECKPOINT
    if ratio >= policy.shape:
        return ThresholdState.SHAPE
    if ratio >= policy.warning:
        return ThresholdState.WARNING
    return ThresholdState.HEALTHY


def recommend_response_class(
    measurement: ContextMeasurement,
    *,
    workflow: str,
    requested_class: str = "automatic",
    policy: ContextPolicy | None = None,
) -> str:
    selected_policy = policy or ContextPolicy()
    if requested_class != "automatic":
        if requested_class not in RESPONSE_CLASSES:
            raise ContextPolicyError("Unknown response class")
        return requested_class
    state = threshold_state(measurement.usage_ratio, selected_policy)
    if state == ThresholdState.UNKNOWN:
        return "artifact" if workflow == "handoff" else "compact"
    if state in {ThresholdState.HEALTHY, ThresholdState.WARNING}:
        return "standard"
    if state in {ThresholdState.SHAPE, ThresholdState.CHECKPOINT}:
        return "compact"
    return "micro"


def allocate_response_budget(
    *,
    requested_class: str,
    recommended_class: str,
    requested_output_tokens: int,
    provider_output_limit: int | None,
    model_output_limit: int | None = None,
    user_output_cap: int | None = None,
    output_limit_supported: bool = True,
) -> ResponseBudget:
    if recommended_class not in RESPONSE_CLASSES:
        raise ContextPolicyError("Unknown recommended response class")
    if requested_output_tokens <= 0:
        raise ContextPolicyError("Requested output tokens must be positive")
    caps: list[tuple[str, int]] = [("requested_output", requested_output_tokens)]
    for label, value in (
        ("provider_output_limit", provider_output_limit),
        ("model_output_limit", model_output_limit),
        ("user_output_cap", user_output_cap),
    ):
        if value is not None:
            if value <= 0:
                raise ContextPolicyError(f"{label} must be positive")
            caps.append((label, value))
    spec = RESPONSE_CLASSES[recommended_class]
    caps.append(("response_class", spec.maximum_tokens))
    allocated = min(value for _, value in caps) if output_limit_supported else 0
    limiting = tuple(label for label, value in caps if value == allocated)
    if not output_limit_supported:
        limiting = ("output_limit_unsupported",)
    return ResponseBudget(
        requested_class=requested_class,
        recommended_class=recommended_class,
        minimum_tokens=spec.minimum_tokens,
        target_tokens=spec.target_tokens,
        maximum_tokens=spec.maximum_tokens,
        allocated_tokens=allocated,
        output_limit_supported=output_limit_supported,
        limiting_factors=limiting,
    )


def project_operation(
    measurement: ContextMeasurement,
    response_budget: ResponseBudget,
    *,
    workflow: str,
    pending_input_tokens: int,
    reasoning_allowance_tokens: int = 0,
    compaction_attempted: bool = False,
    policy: ContextPolicy | None = None,
) -> ContextProjection:
    selected_policy = policy or ContextPolicy()
    if pending_input_tokens < 0 or reasoning_allowance_tokens < 0:
        raise ContextPolicyError("Projected token components must be non-negative")
    if not response_budget.output_limit_supported:
        return ContextProjection(
            adjusted_current_usage_tokens=None,
            pending_input_tokens=pending_input_tokens,
            external_output_tokens=0,
            reasoning_allowance_tokens=reasoning_allowance_tokens,
            reserve_tokens=0,
            projected_usage_tokens=None,
            projected_usage_ratio=None,
            threshold_state=ThresholdState.UNKNOWN,
            decision=ContextDecision.ROUTE_REJECTED,
            reason="output_limit_parameter_unsupported",
        )
    if measurement.context_limit_tokens is None or measurement.current_usage_tokens is None:
        return ContextProjection(
            adjusted_current_usage_tokens=None,
            pending_input_tokens=pending_input_tokens,
            external_output_tokens=response_budget.allocated_tokens,
            reasoning_allowance_tokens=reasoning_allowance_tokens,
            reserve_tokens=0,
            projected_usage_tokens=None,
            projected_usage_ratio=None,
            threshold_state=ThresholdState.UNKNOWN,
            decision=ContextDecision.ARTIFACT_DELIVERY
            if workflow == "handoff"
            else ContextDecision.INLINE_SHAPED,
            reason="context_measurement_unavailable",
        )
    margin = UNCERTAINTY_MARGIN[measurement.measurement_confidence]
    adjusted_current = math.ceil(measurement.current_usage_tokens * (1 + margin))
    raw_reserve = (
        selected_policy.fixed_operational_tokens
        + selected_policy.synthesis_tokens
        + selected_policy.tool_result_tokens
    )
    reserve_cap = math.floor(
        measurement.context_limit_tokens * selected_policy.total_reserve_cap_ratio
    )
    reserve = min(raw_reserve, reserve_cap)
    projected = (
        adjusted_current
        + pending_input_tokens
        + response_budget.allocated_tokens
        + reasoning_allowance_tokens
        + reserve
    )
    ratio = projected / measurement.context_limit_tokens
    state = threshold_state(ratio, selected_policy)
    if ratio >= selected_policy.continuation:
        decision = (
            ContextDecision.FRESH_THREAD_REQUIRED
            if compaction_attempted
            else ContextDecision.COMPACT_BEFORE_DISPATCH
        )
        reason = (
            "post_compaction_projection_unsafe"
            if compaction_attempted
            else "projected_context_reaches_continuation_threshold"
        )
    elif ratio >= selected_policy.shape:
        decision = ContextDecision.INLINE_SHAPED
        reason = "projected_context_requires_response_shaping"
    else:
        decision = ContextDecision.INLINE_SAFE
        reason = "projected_context_below_shaping_threshold"
    return ContextProjection(
        adjusted_current_usage_tokens=adjusted_current,
        pending_input_tokens=pending_input_tokens,
        external_output_tokens=response_budget.allocated_tokens,
        reasoning_allowance_tokens=reasoning_allowance_tokens,
        reserve_tokens=reserve,
        projected_usage_tokens=projected,
        projected_usage_ratio=ratio,
        threshold_state=state,
        decision=decision,
        reason=reason,
    )


def build_preflight_receipt(
    *,
    workflow: str,
    request_text: str,
    requested_output_tokens: int,
    provider_output_limit: int | None,
    output_limit_supported: bool,
    context_limit_tokens: int | None = None,
    current_usage_tokens: int | None = None,
    requested_class: str = "automatic",
    measured_at: str | None = None,
) -> dict[str, Any]:
    measurement = measure_context(
        context_limit_tokens=context_limit_tokens,
        current_usage_tokens=current_usage_tokens,
        measurement_source="caller_reported"
        if context_limit_tokens is not None
        else "unknown",
        measurement_confidence="medium"
        if context_limit_tokens is not None
        else "unknown",
        measured_at=measured_at,
    )
    recommended_class = recommend_response_class(
        measurement,
        workflow=workflow,
        requested_class=requested_class,
    )
    budget = allocate_response_budget(
        requested_class=requested_class,
        recommended_class=recommended_class,
        requested_output_tokens=requested_output_tokens,
        provider_output_limit=provider_output_limit,
        output_limit_supported=output_limit_supported,
    )
    projection = project_operation(
        measurement,
        budget,
        workflow=workflow,
        pending_input_tokens=estimate_text_tokens(request_text, 750),
    )
    return {
        "schema_version": "1.0",
        "mode": "measurement_only",
        "applied_to_dispatch": False,
        "context_measurement": measurement.to_dict(),
        "response_budget": budget.to_dict(),
        "projection": projection.to_dict(),
        "privacy": {
            "request_text_persisted": False,
            "transcript_persisted": False,
            "provider_envelope_persisted": False,
        },
    }
