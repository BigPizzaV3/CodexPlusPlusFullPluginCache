from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .jsonutil import sha256_json


AUDITOR_ID = "aidm4.independent-semantic-auditor.v1"
REQUIRED_RETRIEVAL_DOMAINS = {
    "current",
    "historical",
    "actor",
    "relationship",
    "knowledge",
    "capability",
    "mystery",
    "environment",
    "sealed",
}
INVARIANT_CODES = {
    "SOURCE_MESSAGE_MISMATCH",
    "RETRIEVAL_INCOMPLETE",
    "SOVEREIGNTY_UNDECLARED",
    "PHASE_ILLEGAL",
    "RESPONSE_BYPASSED",
    "ACTION_COST_INVALID",
    "TIME_DURATION_OMITTED",
    "CHRONOLOGY_UNSUPPORTED",
    "ARITHMETIC_MISMATCH",
    "NPC_KNOWLEDGE_NO_ACCESS",
    "NPC_VOICE_COLLISION",
    "MASTERY_FALSE_DISCOVERY",
    "MYSTERY_REPETITION_FALSE_REVELATION",
    "NEGATIVE_FINDING_OVERCLAIM",
    "SEALED_LEAKAGE",
    "WORLD_AUDIT_MISSING",
    "ACTOR_ABSENCE_UNEXPLAINED",
    "DIFFICULTY_FAIRNESS_VIOLATION",
    "RETROACTIVE_PERFECT_COUNTER",
    "UNSUPPORTED_PRECISION",
    "UNCAUSED_ESCALATION",
    "ENVIRONMENT_EFFECT_MISSING",
    "LOGISTICS_EFFECT_MISSING",
    "NARRATION_DELTA_MISMATCH",
    "BOOK_HORIZON_THIN",
}


@dataclass(frozen=True)
class Finding:
    code: str
    message: str
    evidence: dict[str, Any]
    severity: str = "BLOCK"


@dataclass(frozen=True)
class AuditResult:
    passed: bool
    findings: tuple[Finding, ...]
    input_sha256: str
    result_sha256: str
    auditor_id: str
    auditor_code_sha256: str


def _finding(code: str, message: str, **evidence: Any) -> Finding:
    return Finding(code, message, evidence)


def _arithmetic_valid(entry: dict[str, Any]) -> bool:
    previous = entry.get("previous")
    delta = entry.get("delta")
    new = entry.get("new")
    if not all(
        isinstance(value, (int, float)) and not isinstance(value, bool)
        for value in (previous, delta, new)
    ):
        return False
    return previous + delta == new


def audit(envelope: dict[str, Any]) -> AuditResult:
    """Audit a plain data envelope without calling generation or compiler code."""
    findings: list[Finding] = []
    source = envelope.get("source", {})
    semantics = envelope.get("semantics", {})
    output = envelope.get("output", {})

    exact_message = source.get("exact_player_message", "")
    if hashlib.sha256(exact_message.encode("utf-8")).hexdigest() != source.get(
        "exact_player_message_sha256"
    ):
        findings.append(
            _finding("SOURCE_MESSAGE_MISMATCH", "Exact player message hash mismatch.")
        )

    retrieved = set(semantics.get("retrieval_domains", []))
    missing_domains = sorted(REQUIRED_RETRIEVAL_DOMAINS - retrieved)
    if missing_domains:
        findings.append(
            _finding(
                "RETRIEVAL_INCOMPLETE",
                "Required retrieval domains are missing.",
                missing=missing_domains,
            )
        )

    for attribution in semantics.get("pc_attributions", []):
        if attribution.get("kind") == "VOLUNTARY_UNDECLARED":
            findings.append(
                _finding(
                    "SOVEREIGNTY_UNDECLARED",
                    "Narration supplies an undeclared voluntary player action, thought, dialogue, method, emotion, or decision.",
                    attribution=attribution,
                )
            )

    phase = semantics.get("phase", {})
    if phase.get("legal") is not True:
        findings.append(_finding("PHASE_ILLEGAL", "The proposed phase step is illegal."))
    if (
        phase.get("hostile_action_consequential")
        and phase.get("response_possible")
        and not phase.get("response_offered")
    ):
        findings.append(
            _finding(
                "RESPONSE_BYPASSED",
                "A consequential hostile action finalizes before a valid player Response opportunity.",
            )
        )

    action = semantics.get("action", {})
    cost = action.get("cost", 0)
    available = action.get("available", 0)
    if (
        not isinstance(cost, int)
        or cost < 0
        or not isinstance(available, int)
        or cost > available
        or (cost > 0 and not action.get("player_confirmed"))
        or (action.get("routine_scene_act") and cost != 0)
    ):
        findings.append(
            _finding(
                "ACTION_COST_INVALID",
                "Action cost or player allocation is invalid.",
                action=action,
            )
        )

    time = semantics.get("time", {})
    if time.get("time_consuming") and time.get("elapsed_min_seconds", 0) <= 0:
        findings.append(
            _finding("TIME_DURATION_OMITTED", "Time-consuming work has no elapsed time.")
        )
    if time.get("chronology_supported") is not True or time.get("duration_supported") is not True:
        findings.append(
            _finding(
                "CHRONOLOGY_UNSUPPORTED",
                "Chronology or duration is unsupported by retrieved authority.",
            )
        )

    for arithmetic in semantics.get("arithmetic", []):
        if not _arithmetic_valid(arithmetic):
            findings.append(
                _finding(
                    "ARITHMETIC_MISMATCH",
                    "A proposed exact delta does not reconcile.",
                    arithmetic=arithmetic,
                )
            )

    knowledge = semantics.get("knowledge_access", {})
    signatures: dict[str, str] = {}
    for speech in semantics.get("npc_speech", []):
        speaker = speech.get("speaker")
        signature = speech.get("voice_signature")
        for knowledge_ref in speech.get("knowledge_refs", []):
            access = knowledge.get(knowledge_ref, {})
            if access.get("access") is not True or not access.get("path"):
                findings.append(
                    _finding(
                        "NPC_KNOWLEDGE_NO_ACCESS",
                        "NPC speech uses knowledge without a causal access path.",
                        speaker=speaker,
                        knowledge_ref=knowledge_ref,
                    )
                )
        if signature:
            if signature in signatures and signatures[signature] != speaker:
                findings.append(
                    _finding(
                        "NPC_VOICE_COLLISION",
                        "Two NPCs share an indistinguishable declared voice signature.",
                        speakers=[signatures[signature], speaker],
                    )
                )
            signatures[signature] = speaker

    for item in semantics.get("novelty", []):
        if item.get("prior_occurrences", 0) > 0 and item.get("framing") == "FIRST_DISCOVERY":
            findings.append(
                _finding(
                    "MASTERY_FALSE_DISCOVERY",
                    "Established capability or deduction is framed as first discovery.",
                    item=item,
                )
            )
    for item in semantics.get("mystery", []):
        if item.get("novelty_class") in {
            "ALREADY_ESTABLISHED",
            "CORROBORATION",
            "REFINEMENT",
        } and item.get("framing") == "FIRST_REVELATION":
            findings.append(
                _finding(
                    "MYSTERY_REPETITION_FALSE_REVELATION",
                    "Repeated or refining evidence is framed as a first revelation.",
                    item=item,
                )
            )
        if item.get("negative_finding_as_proof_of_absence"):
            findings.append(
                _finding(
                    "NEGATIVE_FINDING_OVERCLAIM",
                    "Failure to find evidence is treated as proof of absence.",
                    item=item,
                )
            )

    visible_refs = set(semantics.get("visible_refs", []))
    sealed_refs = set(semantics.get("sealed_refs", []))
    leaked = sorted(visible_refs & sealed_refs)
    narration = output.get("narration", "")
    raw_leaks = sorted(
        term
        for term in source.get("sealed_terms", [])
        if term and term.casefold() in narration.casefold()
    )
    sealed_delta_leaks = [
        delta
        for delta in output.get("visible_deltas", [])
        if delta.get("visibility") not in (None, "VISIBLE")
    ]
    if (
        leaked
        or raw_leaks
        or sealed_delta_leaks
        or semantics.get("sealed_truth_in_narration")
    ):
        findings.append(
            _finding(
                "SEALED_LEAKAGE",
                "Sealed state reaches visible output.",
                refs=leaked,
                raw_terms=raw_leaks,
                sealed_deltas=sealed_delta_leaks,
            )
        )

    world = semantics.get("world", {})
    if world.get("audit_required") and not world.get("audit_complete"):
        findings.append(
            _finding("WORLD_AUDIT_MISSING", "Required world-reaction audit is absent.")
        )
    for actor in world.get("relevant_actors", []):
        if not actor.get("response") and not actor.get("absence_reason"):
            findings.append(
                _finding(
                    "ACTOR_ABSENCE_UNEXPLAINED",
                    "A relevant actor is absent without an in-world reason.",
                    actor=actor.get("actor_id"),
                )
            )

    fairness = semantics.get("fairness", {})
    for key in (
        "predetermined_failure",
        "enemy_omniscience",
        "impossible_counter",
        "arbitrary_reinforcements",
        "catastrophe_quota",
        "forced_equalization",
        "always_worst_hidden_result",
    ):
        if fairness.get(key):
            findings.append(
                _finding(
                    "DIFFICULTY_FAIRNESS_VIOLATION",
                    f"Forbidden difficulty behavior: {key}.",
                    key=key,
                )
            )
    if fairness.get("opponent_counter") and (
        fairness.get("counter_source")
        not in {
            "prior_observation",
            "intelligence",
            "established_capability",
            "credible_ally",
            "general_capability",
            "hidden_plan",
        }
        or not fairness.get("prepared_before_declaration")
    ):
        findings.append(
            _finding(
                "RETROACTIVE_PERFECT_COUNTER",
                "Countermeasure lacks prior information, capability, or preparation.",
            )
        )

    for precision in semantics.get("precision_claims", []):
        if precision.get("exact") and (
            not precision.get("source_refs")
            or precision.get("source_status") != "EXACT"
        ):
            findings.append(
                _finding(
                    "UNSUPPORTED_PRECISION",
                    "An exact value lacks exact authority.",
                    claim=precision,
                )
            )

    for escalation in semantics.get("escalations", []):
        if escalation.get("activated") and (
            not escalation.get("causal_source")
            or not escalation.get("source_existed_before_trigger")
        ):
            findings.append(
                _finding(
                    "UNCAUSED_ESCALATION",
                    "Escalation lacks a source established before its trigger.",
                    escalation=escalation,
                )
            )

    effects = semantics.get("effects", {})
    if effects.get("environment_relevant") and not effects.get("environment_effects"):
        findings.append(
            _finding("ENVIRONMENT_EFFECT_MISSING", "Relevant environmental effect is omitted.")
        )
    if effects.get("logistics_relevant") and not effects.get("logistics_effects"):
        findings.append(
            _finding("LOGISTICS_EFFECT_MISSING", "Relevant logistical effect is omitted.")
        )

    if set(semantics.get("narrated_change_ids", [])) != set(
        semantics.get("delta_ids", [])
    ):
        findings.append(
            _finding(
                "NARRATION_DELTA_MISMATCH",
                "Narrated state changes and proposed deltas disagree.",
                narration=semantics.get("narrated_change_ids", []),
                deltas=semantics.get("delta_ids", []),
            )
        )

    book = semantics.get("book_preflight", {})
    if (
        book.get("horizon_supported") is not True
        or (
            book.get("triggered")
            and book.get("blocking_module_validated") is not True
        )
    ):
        findings.append(
            _finding(
                "BOOK_HORIZON_THIN",
                "Campaign-book horizon is unsupported or a blocking module is not validated.",
                preflight=book,
            )
        )

    input_hash = sha256_json(envelope)
    result_material = {
        "auditor_id": AUDITOR_ID,
        "input_sha256": input_hash,
        "findings": [
            {
                "code": finding.code,
                "severity": finding.severity,
                "message": finding.message,
                "evidence": finding.evidence,
            }
            for finding in findings
        ],
    }
    return AuditResult(
        passed=not findings,
        findings=tuple(findings),
        input_sha256=input_hash,
        result_sha256=sha256_json(result_material),
        auditor_id=AUDITOR_ID,
        auditor_code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    )
