from __future__ import annotations

import hashlib
import json
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from .jsonutil import canonical_json, sha256_json, sha256_text
from .kernel import GENESIS_HASH


class RuleViolation(RuntimeError):
    """Raised when an executable rule or transition contract is violated."""


class InvalidTransition(RuleViolation):
    pass


class GameplayDisabled(RuleViolation):
    pass


@dataclass(frozen=True)
class State:
    state_id: str
    kind: str
    description: str


@dataclass(frozen=True)
class Transition:
    transition_id: str
    from_machine: str
    from_state: str
    to_machine: str
    to_state: str
    trigger: str
    guard: dict[str, Any]
    effects: dict[str, Any]
    rule_refs: tuple[str, ...]


def S(state_id: str, kind: str = "INTERMEDIATE", description: str = "") -> State:
    return State(state_id, kind, description or state_id.replace("_", " ").title())


MACHINES: dict[str, dict[str, Any]] = {
    "COMBAT": {
        "time_scale": "SECONDS",
        "initial": "ENTRY",
        "terminal": ["AFTERMATH"],
        "refs": ["combat-engine.md", "core-runtime-rules-v2-verbatim.txt §5"],
        "states": [
            S("ENTRY", "INITIAL"),
            S("ROUND_START"),
            S("INITIATIVE"),
            S("ACTION", "PLAYER_BOUNDARY"),
            S("PROVISIONAL_TRAJECTORY"),
            S("RESPONSE", "PLAYER_BOUNDARY"),
            S("RESOLUTION"),
            S("FOLLOW_UP"),
            S("FOLLOW_UP_RESOLUTION"),
            S("CLASH", "PLAYER_BOUNDARY"),
            S("DETERIORATION"),
            S("ESCALATION_CHECK", "AUDIT"),
            S("ROUND_COMMIT", "COMMIT"),
            S("COMBAT_END", "TERMINAL"),
            S("AFTERMATH", "TERMINAL"),
        ],
    },
    "NARRATIVE": {
        "time_scale": "MINUTES_OR_HOURS",
        "initial": "SCENE_START",
        "terminal": ["SCENE_END"],
        "refs": ["narrative-engine.md", "core-runtime-rules-v2-verbatim.txt §6"],
        "states": [
            S("SCENE_START", "INITIAL"),
            S("PLAYER_DECLARATION", "PLAYER_BOUNDARY"),
            S("SCOPE_CHECK", "AUDIT"),
            S("RETRIEVAL", "AUDIT"),
            S("UNCERTAINTY_CHECK", "AUDIT"),
            S("ADJUDICATION"),
            S("OUTCOME_DRAFT"),
            S("INTERRUPT_CHECK", "AUDIT"),
            S("COMMIT", "COMMIT"),
            S("CHOICES", "PLAYER_BOUNDARY"),
            S("SCENE_END", "TERMINAL"),
        ],
    },
    "STRATEGIC": {
        "time_scale": "DAYS_WEEKS_OR_MONTHS",
        "initial": "TURN_START",
        "terminal": ["TURN_END"],
        "refs": ["strategic-engine.md", "core-runtime-rules-v2-verbatim.txt §7"],
        "states": [
            S("TURN_START", "INITIAL"),
            S("START_REPORT"),
            S("ALLOCATE", "PLAYER_BOUNDARY"),
            S("PLAYER_RESOLUTION"),
            S("WORLD_TURN"),
            S("WORLD_REACTION_AUDIT", "AUDIT"),
            S("INTERRUPT_CHECK", "AUDIT"),
            S("CLOSE", "COMMIT"),
            S("REPORT"),
            S("TURN_END", "TERMINAL"),
            S("REBASE", "AUDIT"),
        ],
    },
    "INTERRUPT": {
        "time_scale": "BOUNDARY",
        "initial": "DETECTED",
        "terminal": [],
        "refs": ["strategic-engine.md §3D", "report-save-engine.md"],
        "states": [
            S("DETECTED", "INITIAL"),
            S("RECEIPT"),
            S("PLAYER_RESPONSE_BOUNDARY", "PLAYER_BOUNDARY"),
        ],
    },
    "REPORT_PRODUCT": {
        "time_scale": "CONTROL",
        "initial": "DRAFT",
        "terminal": ["PUBLISHED"],
        "refs": ["report-save-engine.md", "strategic-engine.md §7"],
        "states": [
            S("DRAFT", "INITIAL"),
            S("VISIBILITY_AUDIT", "AUDIT"),
            S("VALIDATED", "AUDIT"),
            S("PUBLISHED", "TERMINAL"),
        ],
    },
    "SAVE_PRODUCT": {
        "time_scale": "CONTROL",
        "initial": "DRAFT",
        "terminal": ["VERSIONED"],
        "refs": ["save-compiler-protocol-v2-verbatim.txt", "report-save-engine.md"],
        "states": [
            S("DRAFT", "INITIAL"),
            S("COVERAGE_AUDIT", "AUDIT"),
            S("INTEGRITY_AUDIT", "AUDIT"),
            S("VALIDATED", "AUDIT"),
            S("VERSIONED", "TERMINAL"),
        ],
    },
}


def T(
    transition_id: str,
    source: str,
    target: str,
    trigger: str,
    *,
    guard: dict[str, Any] | None = None,
    effects: dict[str, Any] | None = None,
    refs: Iterable[str] = (),
) -> Transition:
    from_machine, from_state = source.split(".", 1)
    to_machine, to_state = target.split(".", 1)
    return Transition(
        transition_id,
        from_machine,
        from_state,
        to_machine,
        to_state,
        trigger,
        guard or {},
        effects or {},
        tuple(refs),
    )


TRANSITIONS: tuple[Transition, ...] = (
    # Combat.
    T("combat.entry", "COMBAT.ENTRY", "COMBAT.ROUND_START", "ESTABLISH_ENTRY",
      guard={"required_true": ["entry_state_complete"]}, refs=["combat-engine.md §1"]),
    T("combat.round_start", "COMBAT.ROUND_START", "COMBAT.INITIATIVE", "UPDATE_ROUND",
      guard={"required_true": ["hazards_updated", "deterioration_updated"]}, refs=["combat-engine.md §2A"]),
    T("combat.initiative", "COMBAT.INITIATIVE", "COMBAT.ACTION", "SET_INITIATIVE",
      guard={"required_nonempty": ["initiative_basis"], "forbidden_true": ["invented_stat_sum"]},
      refs=["combat-engine.md §3", "core-runtime-rules-v2-verbatim.txt §5.2"]),
    T("combat.action", "COMBAT.ACTION", "COMBAT.PROVISIONAL_TRAJECTORY", "DECLARE_ACTION",
      guard={"required_true": ["intent_declared"], "forbidden_true": ["outcome_finalized"]},
      refs=["combat-engine.md §2B"]),
    T("combat.response", "COMBAT.PROVISIONAL_TRAJECTORY", "COMBAT.RESPONSE", "OFFER_RESPONSE",
      guard={"required_true": ["hostile_action_consequential", "response_possible"]},
      refs=["combat-engine.md §2C"]),
    T("combat.no_response", "COMBAT.PROVISIONAL_TRAJECTORY", "COMBAT.RESOLUTION", "NO_RESPONSE_POSSIBLE",
      guard={"required_false": ["response_possible"], "required_nonempty": ["no_response_reason"]},
      refs=["combat-engine.md §2B"]),
    T("combat.resolve_response", "COMBAT.RESPONSE", "COMBAT.RESOLUTION", "RESOLVE_RESPONSE",
      guard={"required_true": ["response_resolved"]}, refs=["combat-engine.md §2C"]),
    T("combat.follow_up", "COMBAT.RESOLUTION", "COMBAT.FOLLOW_UP", "FOLLOW_UP_WARRANTED",
      guard={"required_true": ["response_interrupted_action", "initiative_still_meaningful", "time_permits"]},
      refs=["combat-engine.md §2D"]),
    T("combat.follow_up_resolve", "COMBAT.FOLLOW_UP", "COMBAT.FOLLOW_UP_RESOLUTION", "RESOLVE_FOLLOW_UP",
      guard={"required_true": ["follow_up_resolved"]}, refs=["combat-engine.md §2D"]),
    T("combat.follow_up_end", "COMBAT.FOLLOW_UP_RESOLUTION", "COMBAT.DETERIORATION", "EXCHANGE_COMPLETE",
      guard={"required_true": ["exchange_resolved"]}, refs=["combat-engine.md §2D"]),
    T("combat.follow_up_clash", "COMBAT.FOLLOW_UP_RESOLUTION", "COMBAT.CLASH", "CLASH_WARRANTED",
      guard={"required_true": ["clash_warranted"]}, refs=["combat-engine.md §2E"]),
    T("combat.clash", "COMBAT.RESOLUTION", "COMBAT.CLASH", "CLASH_WARRANTED",
      guard={"required_true": ["clash_warranted"]}, refs=["combat-engine.md §2E"]),
    T("combat.resolve_exchange", "COMBAT.RESOLUTION", "COMBAT.DETERIORATION", "EXCHANGE_COMPLETE",
      guard={"required_true": ["exchange_resolved"]}, refs=["combat-engine.md §2F"]),
    T("combat.resolve_clash", "COMBAT.CLASH", "COMBAT.DETERIORATION", "RESOLVE_CLASH",
      guard={"required_true": ["both_intents_resolved", "state_changed"]},
      refs=["combat-engine.md §2E", "core-runtime-rules-v2-verbatim.txt §5.3E"]),
    T("combat.deterioration", "COMBAT.DETERIORATION", "COMBAT.ESCALATION_CHECK", "UPDATE_STATE",
      guard={"required_true": ["resolve_updated", "fatigue_updated", "equipment_updated"]},
      refs=["combat-engine.md §4"]),
    T("combat.no_escalation", "COMBAT.ESCALATION_CHECK", "COMBAT.ROUND_COMMIT", "NO_ESCALATION",
      guard={"required_false": ["escalation_activated"]}, refs=["combat-engine.md §6"]),
    T("combat.causal_escalation", "COMBAT.ESCALATION_CHECK", "COMBAT.ROUND_COMMIT", "ACTIVATE_ESCALATION",
      guard={"required_true": ["escalation_activated", "source_existed_before_trigger"],
             "required_nonempty": ["escalation_causal_source"],
             "forbidden_true": ["arbitrary_resolve_refill", "impossible_reinforcement", "erases_decisive_victory"]},
      refs=["combat-engine.md §6", "core-runtime-rules-v2-verbatim.txt §5.7"]),
    T("combat.next_round", "COMBAT.ROUND_COMMIT", "COMBAT.ROUND_START", "CONTINUE_COMBAT",
      guard={"required_true": ["round_committed", "combat_continues"]}, refs=["combat-engine.md §2F"]),
    T("combat.end", "COMBAT.ROUND_COMMIT", "COMBAT.COMBAT_END", "END_COMBAT",
      guard={"required_true": ["round_committed", "combat_end_condition"]}, refs=["combat-engine.md §7"]),
    T("combat.aftermath", "COMBAT.COMBAT_END", "COMBAT.AFTERMATH", "ENTER_AFTERMATH",
      guard={"required_true": ["immediate_outcome_framed"]}, refs=["combat-engine.md §7"]),
    T("combat.to_narrative", "COMBAT.AFTERMATH", "NARRATIVE.SCENE_START", "AFTERMATH_SCENE",
      guard={"required_true": ["aftermath_required"]}, refs=["core-runtime-rules-v2-verbatim.txt §2.4"]),
    # Narrative.
    T("narrative.frame", "NARRATIVE.SCENE_START", "NARRATIVE.PLAYER_DECLARATION", "FRAME_SCENE",
      guard={"required_true": ["scene_framed"]}, refs=["narrative-engine.md"]),
    T("narrative.scope", "NARRATIVE.PLAYER_DECLARATION", "NARRATIVE.SCOPE_CHECK", "RECEIVE_DECLARATION",
      guard={"required_true": ["player_declared"]}, refs=["turn-protocol.md"]),
    T("narrative.retrieve", "NARRATIVE.SCOPE_CHECK", "NARRATIVE.RETRIEVAL", "SCOPE_VALID",
      guard={"required_true": ["time_scope_checked", "action_economy_checked"]}, refs=["turn-protocol.md"]),
    T("narrative.uncertainty", "NARRATIVE.RETRIEVAL", "NARRATIVE.UNCERTAINTY_CHECK", "RETRIEVAL_COMPLETE",
      guard={"required_true": ["authority_retrieved", "rules_retrieved", "knowledge_retrieved"]}, refs=["turn-protocol.md"]),
    T("narrative.adjudicate", "NARRATIVE.UNCERTAINTY_CHECK", "NARRATIVE.ADJUDICATION", "MEANINGFUL_UNCERTAINTY",
      guard={"required_true": ["meaningful_uncertainty"], "required_nonempty": ["decisive_factors"]}, refs=["integrated-runtime-engine.md §4"]),
    T("narrative.certain", "NARRATIVE.UNCERTAINTY_CHECK", "NARRATIVE.OUTCOME_DRAFT", "CERTAIN_ACT",
      guard={"required_false": ["meaningful_uncertainty"], "forbidden_true": ["manufactured_check"]}, refs=["integrated-runtime-engine.md §4"]),
    T("narrative.outcome", "NARRATIVE.ADJUDICATION", "NARRATIVE.OUTCOME_DRAFT", "RESOLUTION_COMPLETE",
      guard={"required_nonempty": ["outcome_degree"]}, refs=["integrated-runtime-engine.md §4"]),
    T("narrative.interrupt_check", "NARRATIVE.OUTCOME_DRAFT", "NARRATIVE.INTERRUPT_CHECK", "AUDIT_DRAFT",
      guard={"required_true": ["player_sovereignty_checked"]}, refs=["turn-protocol.md"]),
    T("narrative.commit", "NARRATIVE.INTERRUPT_CHECK", "NARRATIVE.COMMIT", "NO_IMMEDIATE_INTERRUPT",
      guard={"required_false": ["immediate_interrupt"], "required_true": ["semantic_audit_passed"]}, refs=["turn-protocol.md"]),
    T("narrative.interrupt", "NARRATIVE.INTERRUPT_CHECK", "INTERRUPT.DETECTED", "INTERRUPT_FIRES",
      guard={"required_true": ["immediate_interrupt"], "required_nonempty": ["interrupt_causal_trigger"]}, refs=["turn-protocol.md"]),
    T("narrative.choices", "NARRATIVE.COMMIT", "NARRATIVE.CHOICES", "COMMIT_TURN",
      guard={"required_true": ["transaction_committed"]}, refs=["narrative-engine.md"]),
    T("narrative.loop", "NARRATIVE.CHOICES", "NARRATIVE.PLAYER_DECLARATION", "CONTINUE_SCENE",
      guard={"required_true": ["scene_continues"], "forbidden_true": ["choices_claim_exhaustive"]}, refs=["narrative-engine.md §Choices"]),
    T("narrative.end", "NARRATIVE.CHOICES", "NARRATIVE.SCENE_END", "END_SCENE",
      guard={"required_true": ["scene_resolved"]}, refs=["narrative-engine.md §Aftermath"]),
    T("narrative.to_combat", "NARRATIVE.SCENE_END", "COMBAT.ENTRY", "HOSTILE_EXCHANGE",
      guard={"required_true": ["direct_hostile_exchange"]}, refs=["integrated-runtime-engine.md §6"]),
    T("narrative.to_strategic", "NARRATIVE.SCENE_END", "STRATEGIC.TURN_START", "BEGIN_LONG_TERM",
      guard={"required_true": ["immediate_pressure_resolved", "player_chose_long_term"]}, refs=["integrated-runtime-engine.md §6"]),
    # Strategic and interrupt.
    T("strategic.start", "STRATEGIC.TURN_START", "STRATEGIC.START_REPORT", "ESTABLISH_TURN",
      guard={"required_nonempty": ["duration", "action_pool"], "required_true": ["resources_loaded"]}, refs=["strategic-engine.md §3A"]),
    T("strategic.allocate", "STRATEGIC.START_REPORT", "STRATEGIC.ALLOCATE", "REQUEST_ALLOCATION",
      guard={"required_true": ["known_constraints_presented"]}, refs=["strategic-engine.md §3A"]),
    T("strategic.player_resolve", "STRATEGIC.ALLOCATE", "STRATEGIC.PLAYER_RESOLUTION", "CONFIRM_ALLOCATIONS",
      guard={"required_true": ["player_confirmed_allocations", "allocation_within_pool"]}, refs=["strategic-engine.md §3B"]),
    T("strategic.world", "STRATEGIC.PLAYER_RESOLUTION", "STRATEGIC.WORLD_TURN", "RESOLVE_PLAYER",
      guard={"required_true": ["player_allocations_resolved", "costs_applied"]}, refs=["strategic-engine.md §3B"]),
    T("strategic.audit", "STRATEGIC.WORLD_TURN", "STRATEGIC.WORLD_REACTION_AUDIT", "RESOLVE_WORLD",
      guard={"required_true": ["actor_initiatives_resolved", "elapsed_time_applied"]}, refs=["strategic-engine.md §3C"]),
    T("strategic.interrupt_check", "STRATEGIC.WORLD_REACTION_AUDIT", "STRATEGIC.INTERRUPT_CHECK", "AUDIT_WORLD",
      guard={"required_true": ["relevant_domains_audited", "absences_reasoned"]}, refs=["strategic-engine.md §3C"]),
    T("strategic.interrupt", "STRATEGIC.INTERRUPT_CHECK", "INTERRUPT.DETECTED", "INTERRUPT_FIRES",
      guard={"required_true": ["immediate_interrupt"], "required_nonempty": ["interrupt_causal_trigger"]}, refs=["strategic-engine.md §3D"]),
    T("strategic.close", "STRATEGIC.INTERRUPT_CHECK", "STRATEGIC.CLOSE", "NO_INTERRUPT",
      guard={"required_false": ["immediate_interrupt"]}, refs=["strategic-engine.md §3E"]),
    T("strategic.report", "STRATEGIC.CLOSE", "STRATEGIC.REPORT", "CLOSE_CHUNK",
      guard={"required_true": ["closure_record_committed"]}, refs=["strategic-engine.md §3E"]),
    T("strategic.end", "STRATEGIC.REPORT", "STRATEGIC.TURN_END", "PRESENT_REPORT",
      guard={"required_true": ["visible_report_validated"], "forbidden_true": ["sealed_content_exposed"]}, refs=["strategic-engine.md §7"]),
    T("strategic.continue", "STRATEGIC.TURN_END", "STRATEGIC.TURN_START", "CONTINUE_DOWNTIME",
      guard={"required_true": ["player_chose_continue"]}, refs=["strategic-engine.md §3E"]),
    T("strategic.exit", "STRATEGIC.TURN_END", "NARRATIVE.SCENE_START", "END_DOWNTIME",
      guard={"required_true": ["player_chose_end"]}, refs=["integrated-runtime-engine.md §6"]),
    T("strategic.rebase", "STRATEGIC.TURN_END", "STRATEGIC.REBASE", "REBASE_REQUIRED",
      guard={"required_true": ["rebase_requested_or_triggered"]}, refs=["report-save-engine.md"]),
    T("strategic.rebase_done", "STRATEGIC.REBASE", "STRATEGIC.TURN_START", "REBASE_COMPLETE",
      guard={"required_true": ["rebase_validated"]}, refs=["report-save-engine.md"]),
    T("interrupt.receipt", "INTERRUPT.DETECTED", "INTERRUPT.RECEIPT", "BUILD_RECEIPT",
      guard={"required_true": ["elapsed_time_recorded", "spent_actions_recorded", "known_deltas_recorded", "visible_trigger_recorded"],
             "forbidden_true": ["full_report_delayed_urgent_scene"]}, refs=["strategic-engine.md §3E"]),
    T("interrupt.boundary", "INTERRUPT.RECEIPT", "INTERRUPT.PLAYER_RESPONSE_BOUNDARY", "FRAME_URGENT_SCENE",
      guard={"required_true": ["receipt_committed"]}, refs=["strategic-engine.md §3E"]),
    T("interrupt.narrative", "INTERRUPT.PLAYER_RESPONSE_BOUNDARY", "NARRATIVE.SCENE_START", "RETURN_NARRATIVE",
      guard={"required_true": ["player_response_preserved"], "required_false": ["direct_hostile_exchange"]}, refs=["strategic-engine.md §3E"]),
    T("interrupt.combat", "INTERRUPT.PLAYER_RESPONSE_BOUNDARY", "COMBAT.ENTRY", "RETURN_COMBAT",
      guard={"required_true": ["player_response_preserved", "direct_hostile_exchange"]}, refs=["strategic-engine.md §3E"]),
    # Products.
    T("report.audit", "REPORT_PRODUCT.DRAFT", "REPORT_PRODUCT.VISIBILITY_AUDIT", "AUDIT_VISIBILITY"),
    T("report.validate", "REPORT_PRODUCT.VISIBILITY_AUDIT", "REPORT_PRODUCT.VALIDATED", "VALIDATE_REPORT",
      guard={"required_false": ["sealed_content_exposed"], "required_true": ["uncertainty_labeled"]}),
    T("report.publish", "REPORT_PRODUCT.VALIDATED", "REPORT_PRODUCT.PUBLISHED", "PUBLISH_REPORT",
      guard={"required_true": ["projection_only"]}),
    T("save.coverage", "SAVE_PRODUCT.DRAFT", "SAVE_PRODUCT.COVERAGE_AUDIT", "AUDIT_COVERAGE",
      guard={"required_true": ["sources_resolved", "coverage_map_complete"]}),
    T("save.integrity", "SAVE_PRODUCT.COVERAGE_AUDIT", "SAVE_PRODUCT.INTEGRITY_AUDIT", "AUDIT_INTEGRITY",
      guard={"required_true": ["ambiguity_preserved", "sealed_separated", "numbers_validated"]}),
    T("save.validate", "SAVE_PRODUCT.INTEGRITY_AUDIT", "SAVE_PRODUCT.VALIDATED", "VALIDATE_SAVE",
      guard={"required_true": ["referential_integrity", "chronology_valid", "file_integrity"]}),
    T("save.version", "SAVE_PRODUCT.VALIDATED", "SAVE_PRODUCT.VERSIONED", "VERSION_SAVE",
      guard={"required_true": ["versioned_not_overwritten"], "forbidden_true": ["silent_rebase"]}),
)


DIFFICULTIES = {
    "EASY": (0, "forgiving"),
    "STANDARD": (1, "credible"),
    "HARD": (2, "competent_and_ruthless"),
    "EXTREME": (3, "high_pressure"),
    "BEYOND_IMPOSSIBLE": (4, "maximum_credible_opposition"),
}


PRODUCT_CONTRACTS = {
    "INTERRUPT_RECEIPT": {
        "required": ["elapsed_time", "spent_actions", "known_deltas", "visible_trigger"],
        "forbidden": ["sealed_clocks", "objective_hidden_truth", "full_dashboard"],
        "transition": {"defer_full_report_until_pressure_allows": True},
        "refs": ["strategic-engine.md §3E", "report-save-engine.md"],
    },
    "FULL_REPORT": {
        "required": ["status", "ledger", "projects", "visible_trackers", "event_log", "time_deltas", "urgent_decisions"],
        "forbidden": ["sealed_clocks", "objective_hidden_truth", "invented_exact_values"],
        "transition": {"normal_turn_end_only": True},
        "refs": ["strategic-engine.md §7"],
    },
    "SESSION_DELTA": {
        "required": ["start_point", "events", "state_changes", "end_state", "resume_point"],
        "forbidden": ["entire_master_copy", "sealed_material"],
        "transition": {"append_only": True},
        "refs": ["save-compiler-protocol-v2-verbatim.txt §14"],
    },
    "ARCHIVAL_MASTER": {
        "required": ["source_coverage", "raw_source_identity", "validation"],
        "forbidden": ["overwrite_previous_authority"],
        "transition": {"explicit_request_or_coverage_need": True},
        "refs": ["report-save-engine.md"],
    },
    "REBASE": {
        "required": ["coverage_map", "prior_version", "validation"],
        "forbidden": ["deleted_sources", "resolved_ambiguity_without_authority"],
        "transition": {"requested_or_staleness_triggered": True},
        "refs": ["report-save-engine.md", "save-compiler-protocol-v2-verbatim.txt"],
    },
}


def _validate_guards(guard: dict[str, Any], context: dict[str, Any]) -> None:
    errors: list[str] = []
    for key in guard.get("required_true", []):
        if context.get(key) is not True:
            errors.append(f"{key} must be true")
    for key in guard.get("required_false", []):
        if context.get(key) is not False:
            errors.append(f"{key} must be false")
    for key in guard.get("required_nonempty", []):
        if context.get(key) in (None, "", [], {}):
            errors.append(f"{key} must be nonempty")
    for key in guard.get("forbidden_true", []):
        if context.get(key) is True:
            errors.append(f"{key} is forbidden")
    if errors:
        raise RuleViolation("; ".join(errors))


def validate_fairness(context: dict[str, Any]) -> None:
    forbidden = {
        "predetermined_failure",
        "enemy_omniscience",
        "impossible_counter",
        "arbitrary_reinforcements",
        "catastrophe_quota",
        "forced_equalization",
        "always_worst_hidden_result",
    }
    violated = sorted(key for key in forbidden if context.get(key) is True)
    if violated:
        raise RuleViolation("ruthless fairness violation: " + ", ".join(violated))
    if context.get("opponent_counter"):
        allowed = {
            "prior_observation",
            "intelligence",
            "established_capability",
            "credible_ally",
            "general_capability",
            "hidden_plan",
        }
        source = context.get("counter_source")
        if source not in allowed or not context.get("prepared_before_declaration"):
            raise RuleViolation("retroactive perfect counter")
    if context.get("critical_failure") and not (
        context.get("severe_risk_established")
        and context.get("severe_risk_causally_realized")
    ):
        raise RuleViolation("critical failure lacks established causal severe risk")


def validate_combat_termination(context: dict[str, Any]) -> None:
    outcomes = {
        "VICTORY",
        "DEFEAT",
        "RETREAT",
        "SURRENDER",
        "DISENGAGEMENT",
        "STALEMATE",
    }
    outcome = context.get("outcome")
    if context.get("combat_end_condition") is not True or outcome not in outcomes:
        raise RuleViolation("combat end requires a typed causal outcome")
    if outcome == "RETREAT" and not context.get("retreat_route"):
        raise RuleViolation("retreat requires an established route")
    if outcome == "DEFEAT" and not context.get("defeat_consequence_recorded"):
        raise RuleViolation("defeat requires a recorded consequence")
    if (
        outcome == "VICTORY"
        and context.get("decisive")
        and context.get("forced_post_victory_escalation")
    ):
        raise RuleViolation("decisive victory cannot force an extra escalation")


def validate_action_allocation(
    *,
    available: int,
    allocations: Iterable[dict[str, Any]],
    player_confirmed: bool,
) -> dict[str, int]:
    if not player_confirmed:
        raise RuleViolation("the player must allocate Strategic Actions")
    spent = 0
    routine = 0
    for allocation in allocations:
        cost = allocation.get("cost")
        if not isinstance(cost, int) or cost < 0:
            raise RuleViolation("Action cost must be a nonnegative integer")
        if allocation.get("routine_scene_act"):
            if cost:
                raise RuleViolation("routine scene-scale acts cannot consume Strategic Actions")
            routine += 1
        else:
            spent += cost
    if spent > available:
        raise RuleViolation(f"allocation exceeds Action pool: {spent}>{available}")
    return {"available": available, "spent": spent, "remaining": available - spent, "routine_acts": routine}


def validate_product(kind: str, product: dict[str, Any]) -> None:
    contract = PRODUCT_CONTRACTS[kind]
    missing = [key for key in contract["required"] if key not in product]
    forbidden = [key for key in contract["forbidden"] if key in product]
    if missing or forbidden:
        raise RuleViolation(f"{kind}: missing={missing}; forbidden={forbidden}")
    if product.get("visibility") == "SEALED":
        raise RuleViolation(f"{kind} is a player-visible product")


class StateMachineEngine:
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection

    def create_instance(
        self,
        instance_id: str,
        machine_id: str,
        *,
        campaign_id: str = "test",
        synthetic: bool = True,
        gameplay_authorized: bool = False,
        context: dict[str, Any] | None = None,
    ) -> None:
        if not synthetic and not gameplay_authorized:
            raise GameplayDisabled("campaign phase instances require explicit gameplay authorization")
        machine = MACHINES[machine_id]
        self.connection.execute(
            """
            INSERT INTO phase_instance(
                instance_id,campaign_id,machine_id,state_id,status,
                gameplay_authorized,synthetic,context_json,last_receipt_hash
            ) VALUES(?,?,?,?,?,?,?,?,?)
            """,
            (
                instance_id,
                campaign_id,
                machine_id,
                machine["initial"],
                "ACTIVE",
                int(gameplay_authorized),
                int(synthetic),
                canonical_json(context or {}),
                GENESIS_HASH,
            ),
        )

    def advance(
        self,
        instance_id: str,
        trigger: str,
        context: dict[str, Any],
        *,
        target_machine: str | None = None,
        target_state: str | None = None,
    ) -> str:
        row = self.connection.execute(
            "SELECT * FROM phase_instance WHERE instance_id=?", (instance_id,)
        ).fetchone()
        if row is None:
            raise InvalidTransition(f"unknown phase instance: {instance_id}")
        if not row["synthetic"] and not row["gameplay_authorized"]:
            raise GameplayDisabled("campaign gameplay is disabled")
        candidates = list(
            self.connection.execute(
                """
                SELECT * FROM phase_transition
                WHERE from_machine_id=? AND from_state_id=? AND trigger_id=? AND active=1
                ORDER BY transition_id
                """,
                (row["machine_id"], row["state_id"], trigger),
            )
        )
        if target_machine is not None:
            candidates = [item for item in candidates if item["to_machine_id"] == target_machine]
        if target_state is not None:
            candidates = [item for item in candidates if item["to_state_id"] == target_state]
        if len(candidates) != 1:
            raise InvalidTransition(
                f"{row['machine_id']}.{row['state_id']} has no unique {trigger} transition"
            )
        transition = candidates[0]
        validate_fairness(context)
        if trigger == "END_COMBAT":
            validate_combat_termination(context)
        _validate_guards(json.loads(transition["guard_json"]), context)
        sequence = int(
            self.connection.execute(
                "SELECT count(*) FROM phase_transition_receipt WHERE instance_id=?",
                (instance_id,),
            ).fetchone()[0]
        ) + 1
        material = {
            "instance_id": instance_id,
            "transition_id": transition["transition_id"],
            "sequence": sequence,
            "from": [row["machine_id"], row["state_id"]],
            "to": [transition["to_machine_id"], transition["to_state_id"]],
            "context_sha256": sha256_json(context),
            "previous_receipt_hash": row["last_receipt_hash"],
        }
        receipt_hash = sha256_json(material)
        receipt_id = f"phase-receipt:{receipt_hash[:32]}"
        terminal = (
            transition["to_state_id"]
            in MACHINES[transition["to_machine_id"]]["terminal"]
        )
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO phase_transition_receipt(
                    receipt_id,instance_id,transition_id,sequence,
                    from_machine_id,from_state_id,to_machine_id,to_state_id,
                    context_sha256,previous_receipt_hash,receipt_hash,synthetic
                ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    receipt_id,
                    instance_id,
                    transition["transition_id"],
                    sequence,
                    row["machine_id"],
                    row["state_id"],
                    transition["to_machine_id"],
                    transition["to_state_id"],
                    sha256_json(context),
                    row["last_receipt_hash"],
                    receipt_hash,
                    row["synthetic"],
                ),
            )
            self.connection.execute(
                """
                UPDATE phase_instance
                SET machine_id=?, state_id=?, status=?, version=version+1,
                    context_json=?, last_receipt_hash=?
                WHERE instance_id=?
                """,
                (
                    transition["to_machine_id"],
                    transition["to_state_id"],
                    "TERMINAL" if terminal else "ACTIVE",
                    canonical_json(context),
                    receipt_hash,
                    instance_id,
                ),
            )
        return receipt_id


RULE_SOURCE_SPECS = (
    ("rules:integrated", "Integrated Runtime Engine", 3, "integrated-runtime-engine.md", False),
    ("rules:combat", "Combat Engine", 3, "combat-engine.md", False),
    ("rules:narrative", "Narrative Engine", 3, "narrative-engine.md", False),
    ("rules:strategic", "Strategic Engine", 3, "strategic-engine.md", False),
    ("rules:turn", "Turn Protocol", 3, "turn-protocol.md", False),
    ("rules:report_save", "Report and Save Engine", 3, "report-save-engine.md", False),
    ("rules:book_lifecycle", "Campaign-book Lifecycle", 3, "campaign-book-lifecycle.md", False),
    ("rules:new_campaign", "New Campaign Engine", 3, "new-campaign-engine.md", False),
    ("rules:core_v2", "Core Runtime Rules 2.0", 4, "core-runtime-rules-v2-verbatim.txt", True),
    ("rules:original", "Original AI-DM Combat + Campaign", 5, "original-ai-dm-combat-campaign-verbatim.txt", True),
    ("rules:save_v2", "Save Compiler Protocol 2.0", 5, "save-compiler-protocol-v2-verbatim.txt", True),
)


BEHAVIOR_TESTS = {
    "PHASE_TRANSITIONS": ["P4-TRANSITIONS", "P4-INVALID"],
    "PLAYER_SOVEREIGNTY": ["P4-NARRATIVE", "P5-SOVEREIGNTY"],
    "RESOLUTION": ["P4-NARRATIVE", "P4-FAIRNESS"],
    "COMBAT": ["P4-COMBAT", "P4-RESPONSE"],
    "NARRATIVE": ["P4-NARRATIVE"],
    "STRATEGIC": ["P4-STRATEGIC", "P4-ACTIONS"],
    "INTERRUPT_REPORT": ["P4-INTERRUPT", "P4-PRODUCTS"],
    "SAVE": ["P4-PRODUCTS", "P5-CORRECTION"],
    "INFORMATION": ["P4-FAIRNESS", "P5-EPISTEMICS"],
    "DIFFICULTY_FAIRNESS": ["P4-FAIRNESS", "P4-COUNTER"],
    "CAMPAIGN_BOOK": ["P8-LIFECYCLE", "P8-CONTRACT"],
    "WORLD": ["P7-WORLD", "P7-AGENCY"],
    "STYLE": ["P5-VOICE", "P5-PRESENTATION"],
    "SETUP": ["P11-NEW-CAMPAIGN"],
    "AUTHORITY": ["P4-LINEAGE", "P5-CORRECTION"],
}


def _behavior_for(text: str, relative_path: str) -> str:
    value = text.casefold()
    if "new-campaign" in relative_path or any(k in value for k in ("scenario selection", "character selection", "loadout selection")):
        return "SETUP"
    if "save" in relative_path or any(k in value for k in ("save", "rebase", "archive", "session delta")):
        return "SAVE"
    if "campaign-book" in relative_path or "book" in value and "campaign" in value:
        return "CAMPAIGN_BOOK"
    if any(k in value for k in ("combat", "resolve", "initiative", "clash", "fatigue", "injur")):
        return "COMBAT"
    if any(k in value for k in ("strategic", "project", "action pool", "downtime", "faction turn")):
        return "STRATEGIC"
    if any(k in value for k in ("narrative", "scene", "dialogue", "conversation")):
        return "NARRATIVE"
    if any(k in value for k in ("interrupt", "report", "dashboard")):
        return "INTERRUPT_REPORT"
    if any(k in value for k in ("difficulty", "ruthless", "omnisc", "counter", "fair", "catastroph")):
        return "DIFFICULTY_FAIRNESS"
    if any(k in value for k in ("knowledge", "information", "hidden", "sealed", "mystery", "evidence")):
        return "INFORMATION"
    if any(k in value for k in ("world", "actor", "faction", "weather", "event", "coalition")):
        return "WORLD"
    if any(k in value for k in ("phase", "transition", "round sequence", "turn sequence")):
        return "PHASE_TRANSITIONS"
    if any(k in value for k in ("player controls", "player character", "player sovereignty", "never decides")):
        return "PLAYER_SOVEREIGNTY"
    if any(k in value for k in ("success", "failure", "uncertainty", "outcome", "check")):
        return "RESOLUTION"
    if any(k in value for k in ("prose", "vivid", "style", "choices", "words", "names")):
        return "STYLE"
    return "AUTHORITY"


def _extract_requirements(path: Path) -> list[tuple[int, str]]:
    result: list[tuple[int, str]] = []
    for number, raw in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        text = raw.strip()
        if not text:
            continue
        normative = (
            text.startswith(("-", "*", "•"))
            or bool(re.match(r"^\d+(?:\.\d+)*[.)]?\s", text))
            or any(
                token in text.casefold()
                for token in (
                    "must", "should", "never", "always", "do not", "cannot",
                    "may ", "only ", "require", "preserve", "track", "use ",
                    "apply ", "resolve ", "offer ", "check ", "update ",
                )
            )
        )
        if normative:
            result.append((number, text))
    return result


def seed_rule_system(
    connection: sqlite3.Connection,
    rule_root: str | Path,
) -> dict[str, int]:
    """Seed executable rule definitions from an explicitly supplied rule lineage root."""
    root = Path(rule_root)
    with connection:
        for source_id, title, precedence, relative_path, verbatim in RULE_SOURCE_SPECS:
            path = root / relative_path
            data = path.read_bytes()
            connection.execute(
                """
                INSERT OR IGNORE INTO rule_source(
                    rule_source_id,title,precedence,relative_path,sha256,
                    byte_count,verbatim,payload_json
                ) VALUES(?,?,?,?,?,?,?,?)
                """,
                (
                    source_id,
                    title,
                    precedence,
                    relative_path,
                    hashlib.sha256(data).hexdigest(),
                    len(data),
                    int(verbatim),
                    canonical_json({"cumulative": True, "immutable_baseline": True}),
                ),
            )
            for line, text in _extract_requirements(path):
                behavior = _behavior_for(text, relative_path)
                lower = text.casefold()
                if "example" in lower and not any(k in lower for k in ("never", "must", "do not")):
                    classification = "EXAMPLE_NON_CANON"
                    tests: list[str] = []
                    rationale = "Illustrative example; examples do not establish campaign canon."
                elif behavior == "SETUP":
                    classification = "SETUP_ONLY"
                    tests = BEHAVIOR_TESTS[behavior]
                    rationale = "Applies only to explicitly authorized new-campaign setup."
                elif any(k in lower for k in ("every action", "repeat the clash", "mysterious challenger", "predetermines defeat", "secret \"complication roll\"", "simulated roll")):
                    classification = "CONTROLLED_BY_LATER_RULE"
                    tests = BEHAVIOR_TESTS.get(behavior, ["P4-LINEAGE"])
                    rationale = "Later runtime rules narrow this legacy instruction while preserving compatible intent."
                else:
                    classification = "COMPATIBLE_ACTIVE"
                    tests = BEHAVIOR_TESTS.get(behavior, ["P4-LINEAGE"])
                    rationale = "Compatible cumulative behavior mapped to the v4 executable contract."
                requirement_id = f"rule:{sha256_text(relative_path + ':' + str(line) + ':' + text)[:32]}"
                connection.execute(
                    """
                    INSERT OR IGNORE INTO rule_requirement(
                        requirement_id,rule_source_id,line_start,line_end,
                        source_text,classification,behavior_id,test_ids_json,
                        rationale,source_text_sha256,payload_json
                    ) VALUES(?,?,?,?,?,?,?,?,?,?,?)
                    """,
                    (
                        requirement_id,
                        source_id,
                        line,
                        line,
                        text,
                        classification,
                        behavior,
                        canonical_json(tests),
                        rationale,
                        sha256_text(text),
                        canonical_json({"relative_path": relative_path}),
                    ),
                )

        for machine_id, spec in MACHINES.items():
            connection.execute(
                """
                INSERT OR IGNORE INTO phase_machine(
                    machine_id,name,time_scale,initial_state,
                    terminal_states_json,rule_refs_json,payload_json
                ) VALUES(?,?,?,?,?,?,?)
                """,
                (
                    machine_id,
                    machine_id.replace("_", " ").title(),
                    spec["time_scale"],
                    spec["initial"],
                    canonical_json(spec["terminal"]),
                    canonical_json(spec["refs"]),
                    canonical_json({"schema": "aidm4.phase_machine.v1"}),
                ),
            )
            for ordinal, state in enumerate(spec["states"]):
                connection.execute(
                    """
                    INSERT OR IGNORE INTO phase_state(
                        machine_id,state_id,ordinal,state_kind,description
                    ) VALUES(?,?,?,?,?)
                    """,
                    (machine_id, state.state_id, ordinal, state.kind, state.description),
                )
        for transition in TRANSITIONS:
            connection.execute(
                """
                INSERT OR IGNORE INTO phase_transition(
                    transition_id,from_machine_id,from_state_id,to_machine_id,
                    to_state_id,trigger_id,guard_json,effect_json,rule_refs_json
                ) VALUES(?,?,?,?,?,?,?,?,?)
                """,
                (
                    transition.transition_id,
                    transition.from_machine,
                    transition.from_state,
                    transition.to_machine,
                    transition.to_state,
                    transition.trigger,
                    canonical_json(transition.guard),
                    canonical_json(transition.effects),
                    canonical_json(transition.rule_refs),
                ),
            )
        for difficulty_id, (rank, posture) in DIFFICULTIES.items():
            connection.execute(
                """
                INSERT OR IGNORE INTO difficulty_profile(
                    difficulty_id,rank,posture_json,invariant_json
                ) VALUES(?,?,?,?)
                """,
                (
                    difficulty_id,
                    rank,
                    canonical_json(
                        {
                            "posture": posture,
                            "changes": [
                                "opposition_competence",
                                "preparation",
                                "risk_tolerance",
                                "mistake_exploitation",
                                "resource_pressure",
                                "forgiveness",
                            ],
                        }
                    ),
                    canonical_json(
                        {
                            "predetermined_failure": False,
                            "enemy_omniscience": False,
                            "impossible_counter": False,
                            "arbitrary_reinforcements": False,
                        }
                    ),
                ),
            )
        for kind, contract in PRODUCT_CONTRACTS.items():
            connection.execute(
                """
                INSERT OR IGNORE INTO phase_product_contract(
                    product_kind,required_fields_json,forbidden_fields_json,
                    transition_rule_json,rule_refs_json
                ) VALUES(?,?,?,?,?)
                """,
                (
                    kind,
                    canonical_json(contract["required"]),
                    canonical_json(contract["forbidden"]),
                    canonical_json(contract["transition"]),
                    canonical_json(contract["refs"]),
                ),
            )
    return {
        "sources": connection.execute("SELECT count(*) FROM rule_source").fetchone()[0],
        "requirements": connection.execute("SELECT count(*) FROM rule_requirement").fetchone()[0],
        "machines": connection.execute("SELECT count(*) FROM phase_machine").fetchone()[0],
        "states": connection.execute("SELECT count(*) FROM phase_state").fetchone()[0],
        "transitions": connection.execute("SELECT count(*) FROM phase_transition").fetchone()[0],
    }


def verify_rule_system(connection: sqlite3.Connection) -> dict[str, Any]:
    unmapped = connection.execute(
        """
        SELECT count(*) FROM rule_requirement
        WHERE classification IN ('COMPATIBLE_ACTIVE','CONTROLLED_BY_LATER_RULE')
          AND (behavior_id IS NULL OR json_array_length(test_ids_json)=0)
        """
    ).fetchone()[0]
    orphan_transitions = connection.execute(
        """
        SELECT count(*) FROM phase_transition t
        LEFT JOIN phase_state f
          ON f.machine_id=t.from_machine_id AND f.state_id=t.from_state_id
        LEFT JOIN phase_state d
          ON d.machine_id=t.to_machine_id AND d.state_id=t.to_state_id
        WHERE f.state_id IS NULL OR d.state_id IS NULL
        """
    ).fetchone()[0]
    return {
        "schema": "aidm4.phase4_rule_verification.v1",
        "status": "PASS" if not unmapped and not orphan_transitions else "FAIL",
        "unmapped_compatible_requirements": unmapped,
        "orphan_transitions": orphan_transitions,
        "counts": seed_rule_system(connection),
    }
