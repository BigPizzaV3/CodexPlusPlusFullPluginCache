from __future__ import annotations

import hashlib
import json
import math
import sqlite3
from dataclasses import dataclass, field
from typing import Any, Iterable

from .jsonutil import canonical_json, sha256_json, sha256_text
from .kernel import Mutation, TurnDraft, commit_turn, current_runtime_hash
from .verify import verify_database


class SimulationError(RuntimeError):
    pass


class SimulationGameplayDisabled(SimulationError):
    pass


SYSTEM_SPECS: dict[str, dict[str, Any]] = {
    "system:time": {
        "owned": ["temporal.nodes", "temporal.constraints"],
        "cadence": ["every committed elapsed-time change"],
        "triggers": ["turn", "travel", "project", "recovery"],
        "inputs": ["authoritative interval"],
        "outputs": ["elapsed interval", "calendar boundaries"],
        "dependencies": [],
        "consumers": ["system:travel", "system:weather", "system:actor", "system:faction", "system:projects"],
    },
    "system:spatial": {
        "owned": ["spatial.nodes", "topology.edges", "route.observations"],
        "cadence": ["on movement or topology evidence"],
        "triggers": ["destination", "route observation", "closure change"],
        "inputs": ["location", "observer", "access evidence"],
        "outputs": ["route candidates", "local access result"],
        "dependencies": ["system:time"],
        "consumers": ["system:travel", "system:weather", "system:information"],
    },
    "system:travel": {
        "owned": ["travel.plans", "travel.leg_receipts"],
        "cadence": ["per travel declaration"],
        "triggers": ["movement intent"],
        "inputs": ["topology", "weather", "documents", "fuel", "supplies"],
        "outputs": ["duration", "resource deltas", "fatigue"],
        "dependencies": ["system:time", "system:spatial", "system:weather", "system:economy"],
        "consumers": ["system:health", "system:actor", "system:faction"],
    },
    "system:weather": {
        "owned": ["environment.weather_receipts"],
        "cadence": ["meaningful local interval"],
        "triggers": ["elapsed time", "location promotion"],
        "inputs": ["climate", "season range", "recent state", "seed", "causal modifiers"],
        "outputs": ["weather interval", "forecast boundary", "domain effects"],
        "dependencies": ["system:time", "system:spatial", "system:random"],
        "consumers": ["system:travel", "system:disaster", "system:health", "system:infrastructure"],
    },
    "system:disaster": {
        "owned": ["disaster.risk_profiles", "disaster.evaluation_receipts"],
        "cadence": ["hazard interval"],
        "triggers": ["accumulation", "threshold", "causal shock"],
        "inputs": ["weather", "hazard", "infrastructure", "preparedness"],
        "outputs": ["warning", "trigger", "cascade", "mitigation"],
        "dependencies": ["system:weather", "system:infrastructure", "system:population"],
        "consumers": ["system:travel", "system:health", "system:faction", "system:governance"],
    },
    "system:population": {
        "owned": ["population.routines", "population.services"],
        "cadence": ["local day or promoted scene"],
        "triggers": ["elapsed time", "service demand", "shock"],
        "inputs": ["households", "work", "services", "culture"],
        "outputs": ["availability", "witnesses", "ordinary activity"],
        "dependencies": ["system:time", "system:economy", "system:infrastructure"],
        "consumers": ["system:actor", "system:media", "system:governance"],
    },
    "system:economy": {
        "owned": ["economy.accounts", "economy.transfer_receipts", "supply.state"],
        "cadence": ["transaction or strategic interval"],
        "triggers": ["purchase", "upkeep", "scarcity", "production"],
        "inputs": ["source", "destination", "amount/range", "unit", "time"],
        "outputs": ["account deltas", "prices", "supply latency"],
        "dependencies": ["system:time", "system:infrastructure"],
        "consumers": ["system:travel", "system:faction", "system:projects", "system:health"],
    },
    "system:infrastructure": {
        "owned": ["infrastructure.assets", "infrastructure.effect_receipts"],
        "cadence": ["damage, upkeep, project, disaster"],
        "triggers": ["failure", "repair", "load change"],
        "inputs": ["power", "water", "roads", "medicine", "communications"],
        "outputs": ["service state", "downstream effects"],
        "dependencies": ["system:economy", "system:weather"],
        "consumers": ["system:population", "system:travel", "system:information", "system:projects"],
    },
    "system:governance": {
        "owned": ["governance.jurisdictions", "governance.law_receipts", "legitimacy.state"],
        "cadence": ["policy, custody, public shock"],
        "triggers": ["law", "enforcement", "bureaucracy", "commitment"],
        "inputs": ["jurisdiction", "evidence chain", "capacity", "custom"],
        "outputs": ["policy", "enforcement", "legitimacy deltas"],
        "dependencies": ["system:information", "system:population", "system:faction"],
        "consumers": ["system:actor", "system:media", "system:faction"],
    },
    "system:media": {
        "owned": ["media.narratives", "media.detection_signatures", "threat.pressure"],
        "cadence": ["information arrival or public event"],
        "triggers": ["public signature", "rumor", "institutional release"],
        "inputs": ["information packets", "credibility", "audience"],
        "outputs": ["framing", "awareness", "actor-specific threat"],
        "dependencies": ["system:information", "system:governance"],
        "consumers": ["system:actor", "system:faction", "system:relationships"],
    },
    "system:information": {
        "owned": ["information.transmissions", "knowledge.access_paths"],
        "cadence": ["per packet/channel"],
        "triggers": ["observation", "message", "record", "interception"],
        "inputs": ["sender", "recipient", "channel", "delay", "distortion"],
        "outputs": ["actual recipients", "belief input", "downstream inference"],
        "dependencies": ["system:time", "system:infrastructure"],
        "consumers": ["system:actor", "system:faction", "system:media", "system:relationships"],
    },
    "system:actor": {
        "owned": ["actor.agency_profiles", "actor.decision_receipts"],
        "cadence": ["schedule/opportunity/threshold"],
        "triggers": ["motive", "information", "threat", "obligation"],
        "inputs": ["knowledge", "resources", "relationships", "time", "constraints"],
        "outputs": ["act", "fail", "stall", "delegate", "disagree", "no action"],
        "dependencies": ["system:information", "system:relationships", "system:attention", "system:time"],
        "consumers": ["system:faction", "system:information", "system:consequence-debt"],
    },
    "system:faction": {
        "owned": ["faction.agency_profiles", "faction.decision_receipts", "faction.budgets"],
        "cadence": ["strategic interval or trigger"],
        "triggers": ["priority", "initiative", "shock", "opportunity"],
        "inputs": ["leadership", "blocs", "budget", "reach", "intelligence", "latency"],
        "outputs": ["initiative outcome", "resource use", "signature"],
        "dependencies": ["system:information", "system:economy", "system:relationships", "system:attention"],
        "consumers": ["system:governance", "system:media", "system:projects", "system:consequence-debt"],
    },
    "system:relationships": {
        "owned": ["relationships.directional_dimensions", "relationships.change_receipts"],
        "cadence": ["causal interaction"],
        "triggers": ["promise", "harm", "disclosure", "gift", "absence"],
        "inputs": ["from actor", "to actor", "dimension", "cause"],
        "outputs": ["directional time-versioned delta"],
        "dependencies": ["system:time", "system:information"],
        "consumers": ["system:actor", "system:faction", "system:information"],
    },
    "system:health": {
        "owned": ["health.condition_receipts", "health.recovery_receipts"],
        "cadence": ["injury/treatment/recovery interval"],
        "triggers": ["harm", "treatment", "elapsed recovery"],
        "inputs": ["Resolve", "fatigue", "strain", "injury", "treatment", "resources"],
        "outputs": ["condition delta", "capability/body effects"],
        "dependencies": ["system:time", "system:economy", "system:technology"],
        "consumers": ["system:combat", "system:travel", "system:actor"],
    },
    "system:combat": {
        "owned": ["combat.exchange_state", "combat.deterioration"],
        "cadence": ["seconds/exchange"],
        "triggers": ["direct hostile exchange"],
        "inputs": ["phase machine", "health", "environment", "equipment"],
        "outputs": ["Resolve", "injury", "position", "aftermath"],
        "dependencies": ["system:health", "system:weather", "system:technology"],
        "consumers": ["system:health", "system:information", "system:consequence-debt"],
    },
    "system:technology": {
        "owned": ["technology.provenance", "technology.interaction_receipts"],
        "cadence": ["use, project, interaction"],
        "triggers": ["capability use", "engineering work", "countermeasure"],
        "inputs": ["mechanism", "scale", "cost", "dependency", "evidence"],
        "outputs": ["effect", "signature", "uncertainty"],
        "dependencies": ["system:projects", "system:economy"],
        "consumers": ["system:health", "system:combat", "system:infrastructure"],
    },
    "system:force-magic-cosmic": {
        "owned": ["cross-domain.interaction_receipts", "power.signatures"],
        "cadence": ["use or detected interaction"],
        "triggers": ["Force", "magic", "cosmic", "dimensional effect"],
        "inputs": ["provenance", "mechanism", "demonstrated scale", "resistance evidence"],
        "outputs": ["established/analogical/uncertain result"],
        "dependencies": ["system:technology", "system:spatial", "system:information"],
        "consumers": ["system:combat", "system:weather", "system:disaster", "system:media"],
    },
    "system:projects": {
        "owned": ["projects.stage_models", "projects.evaluation_receipts"],
        "cadence": ["allocated strategic interval"],
        "triggers": ["Action allocation", "blocker change", "elapsed minimum"],
        "inputs": ["stage", "Actions", "resources", "time", "opposition"],
        "outputs": ["stage effect", "setback", "stall", "output"],
        "dependencies": ["system:time", "system:economy", "system:actor", "system:faction"],
        "consumers": ["system:technology", "system:infrastructure", "system:consequence-debt"],
    },
    "system:random": {
        "owned": ["random.event_tables", "random.event_receipts"],
        "cadence": ["eligible simulation interval"],
        "triggers": ["event check"],
        "inputs": ["campaign seed", "eligible rows", "weights", "cooldowns", "canon"],
        "outputs": ["replayable circumstance"],
        "dependencies": ["system:time", "system:attention"],
        "consumers": ["system:weather", "system:actor", "system:faction", "system:disaster"],
    },
    "system:attention": {
        "owned": ["attention.tiers", "attention.transition_receipts"],
        "cadence": ["relevance or phase change"],
        "triggers": ["combat", "scene", "locality", "project", "distant event"],
        "inputs": ["elapsed campaign time", "relevance", "active pressure"],
        "outputs": ["resolution tier"],
        "dependencies": ["system:time"],
        "consumers": ["system:actor", "system:faction", "system:random", "system:population"],
    },
    "system:consequence-debt": {
        "owned": ["consequence_debt.records", "consequence_debt.transitions"],
        "cadence": ["world audit and elapsed time"],
        "triggers": ["required reaction deferred"],
        "inputs": ["causal event", "actor/faction", "latency", "knowledge"],
        "outputs": ["open/partial/discharged reaction"],
        "dependencies": ["system:time", "system:actor", "system:faction", "system:information"],
        "consumers": ["system:actor", "system:faction", "system:media"],
    },
}


def seed_system_registry(connection: sqlite3.Connection) -> dict[str, int]:
    with connection:
        for system_id, spec in SYSTEM_SPECS.items():
            connection.execute(
                """
                INSERT OR IGNORE INTO system_registry(
                    system_id,version,owned_state_json,cadence_json,triggers_json,
                    inputs_json,outputs_json,dependencies_json,visibility_rule,
                    randomness_rule,failure_rule,invariants_json,consumers_json
                ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    system_id,
                    "4.0.0-phase7",
                    canonical_json(spec["owned"]),
                    canonical_json(spec["cadence"]),
                    canonical_json(spec["triggers"]),
                    canonical_json(spec["inputs"]),
                    canonical_json(spec["outputs"]),
                    canonical_json(spec["dependencies"]),
                    "Visible projections are allowlisted; sealed inputs remain internal.",
                    (
                        "No randomness."
                        if system_id != "system:random"
                        else "SHA-256 deterministic weighted selection with a complete receipt."
                    ),
                    "May fail, stall, delay, disagree, or remain inactive for a recorded causal reason.",
                    canonical_json(
                        [
                            "campaign elapsed time only",
                            "no player-sovereignty mutation",
                            "no impossible knowledge",
                            "no retroactive perfect counter",
                            "explicit transaction coupling",
                        ]
                    ),
                    canonical_json(spec["consumers"]),
                ),
            )
        _seed_event_tables(connection)
    return {
        "systems": connection.execute("SELECT count(*) FROM system_registry").fetchone()[0],
        "event_tables": connection.execute("SELECT count(*) FROM event_table_definition").fetchone()[0],
        "event_entries": connection.execute("SELECT count(*) FROM event_table_entry").fetchone()[0],
    }


def _seed_event_tables(connection: sqlite3.Connection) -> None:
    entries = (
        ("ACTOR_CAUSAL", "delayed-messenger", 18, {"requires": {"actor_present": True}}, {"circumstance": "A messenger arrives late with incomplete information."}),
        ("ORDINARY_STOCHASTIC", "market-delay", 30, {"requires": {"settlement_active": True}}, {"circumstance": "An ordinary delivery is delayed."}),
        ("ENVIRONMENTAL", "runoff", 20, {"requires": {"precipitation": True}}, {"circumstance": "Runoff changes a local path and water workload."}),
        ("RARE_SHOCK", "communications-outage", 2, {"requires": {"infrastructure_exposed": True}}, {"circumstance": "A regional communications fault creates delay and ambiguity."}),
        ("MYSTICAL_COSMIC_DIMENSIONAL", "route-resonance", 1, {"requires": {"dimensional_signature": True}}, {"circumstance": "A route observation produces an anomalous but non-explanatory resonance."}),
    )
    for event_class, event_id, weight, eligibility, outcome in entries:
        table_id = f"events:{event_class.casefold()}"
        connection.execute(
            """
            INSERT OR IGNORE INTO event_table_definition(
                table_id,table_version,event_class,eligibility_schema_json
            ) VALUES(?,?,?,?)
            """,
            (
                table_id,
                "1.0",
                event_class,
                canonical_json({"requires": "exact context equality"}),
            ),
        )
        connection.execute(
            """
            INSERT OR IGNORE INTO event_table_entry(
                table_id,table_version,event_id,weight,eligibility_json,
                outcome_json,cooldown_seconds,fairness_json,visibility
            ) VALUES(?,?,?,?,?,?,?,?,?)
            """,
            (
                table_id,
                "1.0",
                event_id,
                weight,
                canonical_json(eligibility),
                canonical_json(outcome),
                86400,
                canonical_json(
                    {
                        "decides_player_choice": False,
                        "impossible_reinforcement": False,
                        "erases_decisive_success": False,
                        "retroactive_exact_fact": False,
                        "sealed_reveal_without_access": False,
                    }
                ),
                "VISIBLE",
            ),
        )


def verify_system_registry(connection: sqlite3.Connection) -> dict[str, Any]:
    rows = list(connection.execute("SELECT * FROM system_registry ORDER BY system_id"))
    ids = {row["system_id"] for row in rows}
    missing = sorted(set(SYSTEM_SPECS) - ids)
    unknown_dependencies = []
    ownership: dict[str, str] = {}
    duplicate_ownership = []
    for row in rows:
        for dependency in json.loads(row["dependencies_json"]):
            if dependency not in ids:
                unknown_dependencies.append([row["system_id"], dependency])
        for owned in json.loads(row["owned_state_json"]):
            if owned in ownership:
                duplicate_ownership.append([owned, ownership[owned], row["system_id"]])
            ownership[owned] = row["system_id"]
    return {
        "status": "PASS" if not missing and not unknown_dependencies and not duplicate_ownership and len(rows) == 22 else "FAIL",
        "systems": len(rows),
        "missing": missing,
        "unknown_dependencies": unknown_dependencies,
        "duplicate_ownership": duplicate_ownership,
    }


def transition_attention(
    connection: sqlite3.Connection,
    *,
    subject_id: str,
    from_tier: int,
    to_tier: int,
    reason: str,
    trigger_ref: str,
    elapsed_campaign_seconds: int,
    synthetic: bool,
) -> str:
    if from_tier not in range(6) or to_tier not in range(6):
        raise SimulationError("attention tier must be 0–5")
    if elapsed_campaign_seconds < 0:
        raise SimulationError("elapsed campaign time cannot be negative")
    if trigger_ref.startswith("WALL_CLOCK"):
        raise SimulationError("wall-clock time cannot advance in-world simulation")
    if from_tier == 5 and to_tier < 5 and not (
        elapsed_campaign_seconds > 0
        or trigger_ref.startswith(("EVENT:", "PLAYER:", "PHASE:"))
    ):
        raise SimulationError("dormant promotion requires campaign elapsed time or relevance trigger")
    latest = connection.execute(
        """
        SELECT to_tier,sequence FROM attention_transition
        WHERE subject_id=? ORDER BY sequence DESC LIMIT 1
        """,
        (subject_id,),
    ).fetchone()
    if latest is not None and latest["to_tier"] != from_tier:
        raise SimulationError("attention transition does not continue the recorded tier")
    sequence = (latest["sequence"] if latest else 0) + 1
    material = {
        "subject_id": subject_id,
        "from_tier": from_tier,
        "to_tier": to_tier,
        "reason": reason,
        "trigger_ref": trigger_ref,
        "elapsed_campaign_seconds": elapsed_campaign_seconds,
        "sequence": sequence,
    }
    transition_id = f"attention:{sha256_json(material)[:32]}"
    with connection:
        connection.execute(
            """
            INSERT INTO attention_transition(
                attention_transition_id,subject_id,from_tier,to_tier,reason,
                trigger_ref,elapsed_campaign_seconds,sequence,synthetic
            ) VALUES(?,?,?,?,?,?,?,?,?)
            """,
            (
                transition_id,
                subject_id,
                from_tier,
                to_tier,
                reason,
                trigger_ref,
                elapsed_campaign_seconds,
                sequence,
                int(synthetic),
            ),
        )
    return transition_id


def _hash_roll(seed: str, namespace: str, modulus: int = 1_000_000) -> int:
    digest = hashlib.sha256(f"{seed}|{namespace}".encode("utf-8")).digest()
    return int.from_bytes(digest[:8], "big") % modulus


def decide_agency(
    *,
    owner_type: str,
    owner_id: str,
    context: dict[str, Any],
    campaign_seed: str,
    cycle_id: str,
) -> dict[str, Any]:
    required = {
        "motive",
        "knowledge_refs",
        "resources_available",
        "relationships_available",
        "opportunity",
        "obligations",
        "constraints",
        "latency_seconds",
        "elapsed_seconds",
        "characteristic_actions",
    }
    missing = sorted(required - set(context))
    if missing:
        raise SimulationError(f"agency context missing: {missing}")
    if not context["motive"] or not context["opportunity"]:
        outcome = "NO_ACTION"
    elif context["latency_seconds"] > context["elapsed_seconds"]:
        outcome = "STALL"
    elif not context["resources_available"]:
        outcome = "STALL"
    elif context.get("internal_disagreement"):
        outcome = "DISAGREE"
    else:
        roll = _hash_roll(campaign_seed, f"{cycle_id}:{owner_type}:{owner_id}", 100)
        failure_chance = int(context.get("failure_chance_percent", 0))
        delegation_chance = int(context.get("delegation_chance_percent", 0))
        if roll < failure_chance:
            outcome = "FAIL"
        elif roll < failure_chance + delegation_chance:
            outcome = "DELEGATE"
        else:
            outcome = "ACT"
    material = {
        "owner_type": owner_type,
        "owner_id": owner_id,
        "outcome": outcome,
        "context": context,
        "cycle_id": cycle_id,
    }
    return {
        "decision_id": f"decision:{sha256_json(material)[:32]}",
        "owner_type": owner_type,
        "owner_id": owner_id,
        "outcome": outcome,
        "motive_ref": context["motive"],
        "knowledge_refs": context["knowledge_refs"],
        "resource_refs": context.get("resource_refs", []),
        "opportunity": context["opportunity"],
        "constraints": context["constraints"],
        "latency_seconds": context["latency_seconds"],
        "evidence_signatures": context.get("evidence_signatures", []),
        "basis_hash": sha256_json(material),
        "visibility": context.get("visibility", "VISIBLE"),
    }


def propagate_information(
    *,
    transmission_id: str,
    proposition: str,
    originator_id: str,
    sender_id: str,
    intended_recipients: list[str],
    channel: str,
    delay_seconds: int,
    elapsed_seconds: int,
    distortion: dict[str, Any],
    credibility: str,
    classification: str,
    interception: dict[str, Any],
    downstream_inference: dict[str, Any],
    visibility: str = "VISIBLE",
) -> dict[str, Any]:
    if delay_seconds < 0 or elapsed_seconds < 0:
        raise SimulationError("information delay/time cannot be negative")
    actual = intended_recipients if elapsed_seconds >= delay_seconds else []
    return {
        "transmission_id": transmission_id,
        "proposition": proposition,
        "originator_id": originator_id,
        "sender_id": sender_id,
        "intended_recipients": intended_recipients,
        "actual_recipients": actual,
        "channel": channel,
        "delay_seconds": delay_seconds,
        "distortion": distortion,
        "credibility": credibility,
        "classification": classification,
        "interception": interception,
        "downstream_inference": downstream_inference if actual else {},
        "visibility": visibility,
    }


def relationship_change(
    *,
    change_id: str,
    from_actor_id: str,
    to_actor_id: str,
    dimension: str,
    previous_value: Any,
    delta: Any,
    new_value: Any,
    causal_event_ref: str,
    effective_sequence: int,
    visibility: str = "VISIBLE",
) -> dict[str, Any]:
    if from_actor_id == to_actor_id:
        raise SimulationError("directional relationship requires distinct actors")
    return {
        "relationship_change_id": change_id,
        "from_actor_id": from_actor_id,
        "to_actor_id": to_actor_id,
        "dimension": dimension,
        "previous_value": previous_value,
        "delta": delta,
        "new_value": new_value,
        "causal_event_ref": causal_event_ref,
        "effective_sequence": effective_sequence,
        "visibility": visibility,
    }


def resource_transfer(
    *,
    transfer_id: str,
    source_account: str,
    destination_account: str,
    amount_min: int,
    amount_max: int,
    unit: str,
    purpose: str,
    elapsed_campaign_seconds: int,
    provenance_ref: str,
    visibility: str = "VISIBLE",
) -> dict[str, Any]:
    if amount_max < amount_min or not unit or source_account == destination_account:
        raise SimulationError("invalid resource transfer")
    return {
        "transfer_id": transfer_id,
        "source_account": source_account,
        "destination_account": destination_account,
        "amount_min": amount_min,
        "amount_max": amount_max,
        "unit": unit,
        "purpose": purpose,
        "elapsed_campaign_seconds": elapsed_campaign_seconds,
        "provenance_ref": provenance_ref,
        "visibility": visibility,
    }


def infrastructure_effect(
    *,
    effect_id: str,
    infrastructure_id: str,
    cause_class: str,
    cause_ref: str,
    effect: dict[str, Any],
    downstream_domains: list[str],
    mitigation: dict[str, Any],
    visibility: str = "VISIBLE",
) -> dict[str, Any]:
    if len(set(downstream_domains)) < 2:
        raise SimulationError("infrastructure effects must name coupled downstream domains")
    return {
        "infrastructure_effect_id": effect_id,
        "infrastructure_id": infrastructure_id,
        "cause_class": cause_class,
        "cause_ref": cause_ref,
        "effect": effect,
        "downstream_domains": downstream_domains,
        "mitigation": mitigation,
        "visibility": visibility,
    }


def generate_weather(
    *,
    campaign_seed: str,
    cycle_id: str,
    location_id: str,
    climate_profile: dict[str, Any],
    season: dict[str, Any],
    recent_state: dict[str, Any],
    causal_modifiers: list[dict[str, Any]],
) -> dict[str, Any]:
    if season.get("status") not in {"EXACT", "RANGE", "UNRESOLVED"}:
        raise SimulationError("season must be exact, ranged, or unresolved")
    base_min = int(climate_profile["temperature_min_c"])
    base_max = int(climate_profile["temperature_max_c"])
    if season["status"] == "UNRESOLVED":
        base_min -= int(climate_profile.get("unresolved_season_margin_c", 8))
        base_max += int(climate_profile.get("unresolved_season_margin_c", 8))
    roll = _hash_roll(campaign_seed, f"weather:{cycle_id}:{location_id}", 2001) - 1000
    anomaly = roll / 1000 * float(climate_profile.get("max_anomaly_c", 4))
    minimum = math.floor((base_min + anomaly) * 10) / 10
    maximum = math.ceil((base_max + anomaly) * 10) / 10
    precipitation_roll = _hash_roll(
        campaign_seed, f"precip:{cycle_id}:{location_id}", 100
    )
    precipitation = precipitation_roll < int(
        climate_profile.get("precipitation_chance_percent", 30)
    )
    wind_kph = int(climate_profile.get("base_wind_kph", 10)) + _hash_roll(
        campaign_seed, f"wind:{cycle_id}:{location_id}", 25
    )
    supernatural = [item for item in causal_modifiers if item.get("source_ref")]
    travel_multiplier = 1000
    if precipitation:
        travel_multiplier += 150
    if wind_kph >= 25:
        travel_multiplier += 100
    for modifier in supernatural:
        travel_multiplier += int(modifier.get("travel_multiplier_delta_milli", 0))
    state = {
        "temperature_c": {"min": minimum, "max": maximum},
        "precipitation": {
            "present": precipitation,
            "type": climate_profile.get("precipitation_type", "rain") if precipitation else "none",
            "intensity": "moderate" if precipitation else "none",
        },
        "wind_kph": wind_kph,
        "visibility_m": max(500, 10000 - (5000 if precipitation else 0) - wind_kph * 50),
        "season_status": season["status"],
        "recent_state_ref": recent_state.get("state_ref"),
        "causal_modifiers": supernatural,
        "effects": {
            "travel_duration_multiplier_min_milli": travel_multiplier,
            "travel_duration_multiplier_max_milli": travel_multiplier + (100 if season["status"] == "UNRESOLVED" else 0),
            "concealment": "INCREASED" if precipitation else "BASELINE",
            "health": "EXPOSURE_RISK" if minimum < 0 else "BASELINE",
            "infrastructure": "RUNOFF_LOAD" if precipitation else "BASELINE",
        },
    }
    environment_state_id = f"environment:{sha256_json({'cycle': cycle_id, 'location': location_id, 'state': state})[:32]}"
    state["effects"]["travel_overlay"] = {
        "duration_multiplier_min_milli": travel_multiplier,
        "duration_multiplier_max_milli": travel_multiplier
        + (100 if season["status"] == "UNRESOLVED" else 0),
        "source_ref": environment_state_id,
    }
    return {
        "environment_state_id": environment_state_id,
        "location_id": location_id,
        "state": state,
        "generation_source": "SHA256_SEEDED_WEATHER_V1",
        "seed_receipt": {
            "campaign_seed_hash": sha256_text(campaign_seed),
            "namespace": f"weather:{cycle_id}:{location_id}",
        },
        "visibility": "VISIBLE",
    }


def evaluate_disaster(
    *,
    risk_profile_id: str,
    preconditions: dict[str, bool],
    required_preconditions: list[str],
    accumulation: int,
    warning_threshold: int,
    trigger_threshold: int,
    preparedness: dict[str, Any],
    cascade_rules: list[dict[str, Any]],
    causal_trigger: bool,
    visibility: str = "VISIBLE",
) -> dict[str, Any]:
    met = all(preconditions.get(key) is True for key in required_preconditions)
    warning = met and accumulation >= warning_threshold
    triggered = met and causal_trigger and accumulation >= trigger_threshold
    mitigation = {
        "available": bool(preparedness),
        "effectiveness": preparedness.get("effectiveness", "NONE"),
    }
    cascades = cascade_rules if triggered else []
    severity = None
    if triggered:
        severity = (
            "MITIGATED"
            if preparedness.get("effectiveness") in {"HIGH", "COMPLETE"}
            else "ACTIVE"
        )
    material = {
        "risk_profile_id": risk_profile_id,
        "preconditions": preconditions,
        "accumulation": accumulation,
        "warning": warning,
        "triggered": triggered,
        "preparedness": preparedness,
        "cascades": cascades,
    }
    return {
        "disaster_evaluation_id": f"disaster-eval:{sha256_json(material)[:32]}",
        "risk_profile_id": risk_profile_id,
        "preconditions_met": met,
        "accumulation": accumulation,
        "warning_issued": warning,
        "triggered": triggered,
        "severity": severity,
        "cascade_effects": cascades,
        "mitigation": mitigation,
        "basis_hash": sha256_json(material),
        "visibility": visibility,
    }


def select_random_event(
    connection: sqlite3.Connection,
    *,
    table_id: str,
    table_version: str,
    context: dict[str, Any],
    campaign_seed: str,
    cycle_id: str,
) -> dict[str, Any]:
    entries = []
    for row in connection.execute(
        """
        SELECT * FROM event_table_entry
        WHERE table_id=? AND table_version=?
        ORDER BY event_id
        """,
        (table_id, table_version),
    ):
        eligibility = json.loads(row["eligibility_json"])
        required = eligibility.get("requires", {})
        fair = json.loads(row["fairness_json"])
        fairness_ok = not any(fair.values())
        eligible = fairness_ok and all(context.get(k) == v for k, v in required.items())
        if eligible:
            entries.append(dict(row))
    total = sum(row["weight"] for row in entries)
    roll = _hash_roll(campaign_seed, f"event:{cycle_id}:{table_id}:{table_version}", total) if total else None
    selected = None
    if entries:
        cursor = 0
        for row in entries:
            cursor += row["weight"]
            if roll < cursor:
                selected = row
                break
    material = {
        "table_id": table_id,
        "version": table_version,
        "eligible": [row["event_id"] for row in entries],
        "weights": [row["weight"] for row in entries],
        "roll": roll,
        "selected": selected["event_id"] if selected else None,
        "context": context,
    }
    return {
        "random_event_receipt_id": f"rng:{sha256_json(material)[:32]}",
        "campaign_seed_hash": sha256_text(campaign_seed),
        "table_id": table_id,
        "table_version": table_version,
        "eligible_events": [
            {"event_id": row["event_id"], "weight": row["weight"]}
            for row in entries
        ],
        "roll": {"value": roll, "range": [0, total - 1] if total else None},
        "modifiers": {"context_hash": sha256_json(context)},
        "selected_result": (
            {
                "event_id": selected["event_id"],
                "outcome": json.loads(selected["outcome_json"]),
            }
            if selected
            else None
        ),
        "causality": {
            "eligibility_evaluated_before_roll": True,
            "player_choice_decided": False,
            "earned_success_erased": False,
            "impossible_reinforcement": False,
        },
        "visibility": selected["visibility"] if selected else "VISIBLE",
    }


def recover_health(
    *,
    actor_id: str,
    condition_class: str,
    previous_severity: int,
    treatment: dict[str, Any],
    elapsed_seconds: int,
    resources: dict[str, Any],
    capability_dependencies: list[str],
) -> dict[str, Any]:
    if elapsed_seconds <= 0:
        raise SimulationError("recovery requires positive elapsed campaign time")
    if not treatment.get("provided") or not resources.get("available"):
        improvement = 0
    else:
        required = int(treatment.get("minimum_seconds", 0))
        improvement = 1 if elapsed_seconds >= required else 0
    new_severity = max(0, previous_severity - improvement)
    material = {
        "actor_id": actor_id,
        "condition": condition_class,
        "previous": previous_severity,
        "treatment": treatment,
        "elapsed": elapsed_seconds,
        "resources": resources,
        "dependencies": capability_dependencies,
        "new": new_severity,
    }
    return {
        "recovery_id": f"recovery:{sha256_json(material)[:32]}",
        "actor_id": actor_id,
        "condition_class": condition_class,
        "previous_state": {"severity": previous_severity},
        "treatment": treatment,
        "elapsed_seconds": elapsed_seconds,
        "resources": resources,
        "capability_dependencies": capability_dependencies,
        "new_state": {"severity": new_severity},
        "visibility": "VISIBLE",
    }


def resolve_cross_domain_interaction(
    *,
    source_domain: str,
    target_domain: str,
    source_capability_ref: str | None,
    target_resistance_ref: str | None,
    evidence_refs: list[str],
    analogy_refs: list[str],
    claimed_exact_outcome: Any | None = None,
) -> dict[str, Any]:
    if source_capability_ref and target_resistance_ref and evidence_refs:
        status = "ESTABLISHED"
        outcome = claimed_exact_outcome
    elif evidence_refs or analogy_refs:
        status = "ANALOGICAL"
        outcome = {"bounded": True, "exact": None}
    else:
        status = "UNCERTAIN"
        outcome = {"unknown_interaction": True}
    material = {
        "source_domain": source_domain,
        "target_domain": target_domain,
        "source": source_capability_ref,
        "target": target_resistance_ref,
        "evidence": evidence_refs,
        "analogy": analogy_refs,
        "status": status,
        "outcome": outcome,
    }
    return {
        "interaction_id": f"interaction:{sha256_json(material)[:32]}",
        "source_domain": source_domain,
        "target_domain": target_domain,
        "source_capability_ref": source_capability_ref,
        "target_resistance_ref": target_resistance_ref,
        "evidence_refs": evidence_refs + analogy_refs,
        "resolution_status": status,
        "outcome": outcome,
        "invented_power_score": 0,
        "visibility": "VISIBLE",
    }


def evaluate_project_stage(
    *,
    project_id: str,
    stage_model: list[dict[str, Any]],
    stage_before: str,
    elapsed_seconds: int,
    actions_spent: int,
    resources_met: bool,
    blockers: list[str],
    outcome_degree: str,
) -> dict[str, Any]:
    ids = [stage["stage_id"] for stage in stage_model]
    if len(ids) != len(set(ids)) or len(ids) < 2:
        raise SimulationError("project stages must be distinct")
    if stage_before not in ids:
        raise SimulationError("unknown current project stage")
    current = stage_model[ids.index(stage_before)]
    if blockers or not resources_met:
        stage_after = stage_before
        outcome = "STALL"
    elif elapsed_seconds < int(current.get("minimum_seconds", 0)):
        stage_after = stage_before
        outcome = "STALL"
    elif actions_spent < int(current.get("action_cost", 0)):
        stage_after = stage_before
        outcome = "STALL"
    else:
        outcome = outcome_degree
        advance = outcome_degree in {
            "CRITICAL_SUCCESS",
            "CLEAN_SUCCESS",
            "SUCCESS_WITH_SETBACK",
        }
        index = ids.index(stage_before)
        stage_after = ids[min(index + 1, len(ids) - 1)] if advance else stage_before
    material = {
        "project": project_id,
        "before": stage_before,
        "after": stage_after,
        "outcome": outcome,
        "elapsed": elapsed_seconds,
        "actions": actions_spent,
        "resources_met": resources_met,
        "blockers": blockers,
    }
    return {
        "project_evaluation_id": f"project-eval:{sha256_json(material)[:32]}",
        "project_clock_id": project_id,
        "stage_before": stage_before,
        "stage_after": stage_after,
        "outcome_degree": outcome,
        "elapsed_seconds": elapsed_seconds,
        "action_cost": actions_spent,
        "resource_effects": {"requirements_met": resources_met},
        "blockers": blockers,
        "output": current.get("output", {}),
        "basis_hash": sha256_json(material),
        "visibility": "VISIBLE",
    }


def consequence_debt(
    *,
    debt_id: str,
    causal_event_ref: str,
    required_reaction_class: str,
    debtor_actor_or_faction_id: str,
    created_campaign_time_ref: str,
    earliest_discharge_seconds: int,
    visibility: str = "SEALED",
) -> dict[str, Any]:
    if not causal_event_ref or earliest_discharge_seconds < 0:
        raise SimulationError("Consequence Debt requires a causal event and valid latency")
    return {
        "consequence_debt_id": debt_id,
        "causal_event_ref": causal_event_ref,
        "required_reaction_class": required_reaction_class,
        "debtor_actor_or_faction_id": debtor_actor_or_faction_id,
        "created_campaign_time_ref": created_campaign_time_ref,
        "earliest_discharge_seconds": earliest_discharge_seconds,
        "status": "OPEN",
        "visibility": visibility,
        "payload": {
            "cannot_grant_impossible_knowledge": True,
            "cannot_act_as_punishment_quota": True,
        },
    }


def discharge_consequence_debt(
    *,
    transition_id: str,
    debt: dict[str, Any],
    elapsed_seconds: int,
    discharge_form: str,
    causal_basis: dict[str, Any],
    to_status: str = "DISCHARGED",
) -> dict[str, Any]:
    if elapsed_seconds < debt["earliest_discharge_seconds"]:
        raise SimulationError("Consequence Debt cannot discharge before causal latency")
    if causal_basis.get("impossible_knowledge") or causal_basis.get("punishment_only"):
        raise SimulationError("invalid Consequence Debt discharge")
    return {
        "debt_transition_id": transition_id,
        "consequence_debt_id": debt["consequence_debt_id"],
        "from_status": debt["status"],
        "to_status": to_status,
        "discharge_form": discharge_form,
        "causal_basis": causal_basis,
        "elapsed_seconds": elapsed_seconds,
        "visibility": debt["visibility"],
    }


@dataclass(frozen=True)
class SimulationPlan:
    cycle_id: str
    mutations: tuple[Mutation, ...]
    effect_system_ids: tuple[str, ...]
    resolution_scope: dict[str, Any]
    auxiliary: dict[str, Any] = field(default_factory=dict)


def commit_simulation_cycle(
    connection: sqlite3.Connection,
    *,
    campaign_id: str,
    campaign_seed: str,
    elapsed_campaign_seconds: int,
    plan: SimulationPlan,
    expected_runtime_hash: str,
    synthetic: bool,
    gameplay_authorized: bool = False,
) -> dict[str, Any]:
    if elapsed_campaign_seconds <= 0:
        raise SimulationError("simulation requires positive committed campaign time")
    if not synthetic and not gameplay_authorized:
        raise SimulationGameplayDisabled("campaign world simulation is disabled")
    if len(plan.mutations) != len(plan.effect_system_ids):
        raise SimulationError("every mutation requires one owning system")
    unknown_systems = [
        system_id
        for system_id in plan.effect_system_ids
        if system_id not in SYSTEM_SPECS
    ]
    if unknown_systems:
        raise SimulationError(f"unknown systems: {unknown_systems}")
    seed_hash = sha256_text(campaign_seed)

    def side_effect(db: sqlite3.Connection, transaction_id: str) -> None:
        db.execute(
            """
            INSERT INTO simulation_cycle(
                simulation_cycle_id,campaign_id,elapsed_campaign_seconds,
                source_temporal_node_id,campaign_seed_hash,transaction_id,
                resolution_scope_json,synthetic,status
            ) VALUES(?,?,?,?,?,?,?,?,?)
            """,
            (
                plan.cycle_id,
                campaign_id,
                elapsed_campaign_seconds,
                None,
                seed_hash,
                transaction_id,
                canonical_json(plan.resolution_scope),
                int(synthetic),
                "COMMITTED",
            ),
        )
        for ordinal, (mutation, system_id) in enumerate(
            zip(plan.mutations, plan.effect_system_ids)
        ):
            db.execute(
                """
                INSERT INTO simulation_effect(
                    simulation_effect_id,simulation_cycle_id,system_id,domain,
                    subject_id,state_key,delta_ordinal,causal_ref,visibility
                ) VALUES(?,?,?,?,?,?,?,?,?)
                """,
                (
                    f"simulation-effect:{sha256_json({'cycle': plan.cycle_id, 'ordinal': ordinal, 'system': system_id})[:32]}",
                    plan.cycle_id,
                    system_id,
                    mutation.domain,
                    mutation.subject_id,
                    mutation.state_key,
                    ordinal,
                    plan.auxiliary.get("causal_ref", plan.cycle_id),
                    mutation.visibility,
                ),
            )
        weather = plan.auxiliary.get("weather")
        if weather:
            db.execute(
                """
                INSERT INTO environment_state(
                    environment_state_id,location_id,temporal_node_id,state_json,
                    generation_source,random_event_receipt_id,transaction_id,visibility
                ) VALUES(?,?,NULL,?,?,NULL,?,?)
                """,
                (
                    weather["environment_state_id"],
                    weather["location_id"],
                    canonical_json(weather["state"]),
                    weather["generation_source"],
                    transaction_id,
                    weather["visibility"],
                ),
            )
        event = plan.auxiliary.get("random_event")
        if event:
            db.execute(
                """
                INSERT INTO random_event_receipt(
                    random_event_receipt_id,campaign_seed_hash,table_id,
                    table_version,eligible_events_json,roll_json,modifiers_json,
                    selected_result_json,causality_json,transaction_id,visibility
                ) VALUES(?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    event["random_event_receipt_id"],
                    event["campaign_seed_hash"],
                    event["table_id"],
                    event["table_version"],
                    canonical_json(event["eligible_events"]),
                    canonical_json(event["roll"]),
                    canonical_json(event["modifiers"]),
                    canonical_json(event["selected_result"]),
                    canonical_json(event["causality"]),
                    transaction_id,
                    event["visibility"],
                ),
            )
        for decision in plan.auxiliary.get("decisions", []):
            db.execute(
                """
                INSERT INTO agency_decision_receipt(
                    decision_id,simulation_cycle_id,decision_owner_type,
                    decision_owner_id,decision_outcome,motive_ref,
                    knowledge_refs_json,resource_refs_json,opportunity_json,
                    constraints_json,latency_seconds,evidence_signatures_json,
                    decision_basis_hash,visibility
                ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    decision["decision_id"],
                    plan.cycle_id,
                    decision["owner_type"],
                    decision["owner_id"],
                    decision["outcome"],
                    decision["motive_ref"],
                    canonical_json(decision["knowledge_refs"]),
                    canonical_json(decision["resource_refs"]),
                    canonical_json(decision["opportunity"]),
                    canonical_json(decision["constraints"]),
                    decision["latency_seconds"],
                    canonical_json(decision["evidence_signatures"]),
                    decision["basis_hash"],
                    decision["visibility"],
                ),
            )
        for packet in plan.auxiliary.get("information", []):
            db.execute(
                """
                INSERT INTO information_transmission(
                    transmission_id,simulation_cycle_id,proposition,originator_id,
                    sender_id,intended_recipients_json,actual_recipients_json,
                    channel,delay_seconds,distortion_json,credibility,
                    classification,interception_json,downstream_inference_json,
                    source_packet_id,visibility
                ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,NULL,?)
                """,
                (
                    packet["transmission_id"],
                    plan.cycle_id,
                    packet["proposition"],
                    packet["originator_id"],
                    packet["sender_id"],
                    canonical_json(packet["intended_recipients"]),
                    canonical_json(packet["actual_recipients"]),
                    packet["channel"],
                    packet["delay_seconds"],
                    canonical_json(packet["distortion"]),
                    packet["credibility"],
                    packet["classification"],
                    canonical_json(packet["interception"]),
                    canonical_json(packet["downstream_inference"]),
                    packet["visibility"],
                ),
            )
        for change in plan.auxiliary.get("relationship_changes", []):
            db.execute(
                """
                INSERT INTO relationship_change_receipt(
                    relationship_change_id,simulation_cycle_id,from_actor_id,
                    to_actor_id,dimension,previous_value_json,delta_json,
                    new_value_json,causal_event_ref,effective_sequence,visibility
                ) VALUES(?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    change["relationship_change_id"],
                    plan.cycle_id,
                    change["from_actor_id"],
                    change["to_actor_id"],
                    change["dimension"],
                    canonical_json(change["previous_value"]),
                    canonical_json(change["delta"]),
                    canonical_json(change["new_value"]),
                    change["causal_event_ref"],
                    change["effective_sequence"],
                    change["visibility"],
                ),
            )
        for transfer in plan.auxiliary.get("resource_transfers", []):
            db.execute(
                """
                INSERT INTO resource_transfer_receipt(
                    transfer_id,simulation_cycle_id,source_account,
                    destination_account,amount_min,amount_max,unit,purpose,
                    elapsed_campaign_seconds,provenance_ref,visibility
                ) VALUES(?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    transfer["transfer_id"],
                    plan.cycle_id,
                    transfer["source_account"],
                    transfer["destination_account"],
                    transfer["amount_min"],
                    transfer["amount_max"],
                    transfer["unit"],
                    transfer["purpose"],
                    transfer["elapsed_campaign_seconds"],
                    transfer["provenance_ref"],
                    transfer["visibility"],
                ),
            )
        for effect in plan.auxiliary.get("infrastructure_effects", []):
            db.execute(
                """
                INSERT INTO infrastructure_effect_receipt(
                    infrastructure_effect_id,simulation_cycle_id,
                    infrastructure_id,cause_class,cause_ref,effect_json,
                    downstream_domains_json,mitigation_json,visibility
                ) VALUES(?,?,?,?,?,?,?,?,?)
                """,
                (
                    effect["infrastructure_effect_id"],
                    plan.cycle_id,
                    effect["infrastructure_id"],
                    effect["cause_class"],
                    effect["cause_ref"],
                    canonical_json(effect["effect"]),
                    canonical_json(effect["downstream_domains"]),
                    canonical_json(effect["mitigation"]),
                    effect["visibility"],
                ),
            )
        disaster = plan.auxiliary.get("disaster")
        if disaster:
            db.execute(
                """
                INSERT INTO disaster_evaluation_receipt(
                    disaster_evaluation_id,simulation_cycle_id,risk_profile_id,
                    preconditions_met,accumulation,warning_issued,triggered,
                    severity,cascade_effects_json,mitigation_json,basis_hash,visibility
                ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    disaster["disaster_evaluation_id"],
                    plan.cycle_id,
                    disaster["risk_profile_id"],
                    int(disaster["preconditions_met"]),
                    disaster["accumulation"],
                    int(disaster["warning_issued"]),
                    int(disaster["triggered"]),
                    disaster["severity"],
                    canonical_json(disaster["cascade_effects"]),
                    canonical_json(disaster["mitigation"]),
                    disaster["basis_hash"],
                    disaster["visibility"],
                ),
            )
        for recovery in plan.auxiliary.get("health", []):
            db.execute(
                """
                INSERT INTO health_recovery_receipt(
                    recovery_id,simulation_cycle_id,actor_id,condition_class,
                    previous_state_json,treatment_json,elapsed_seconds,
                    resources_json,capability_dependencies_json,new_state_json,
                    visibility
                ) VALUES(?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    recovery["recovery_id"],
                    plan.cycle_id,
                    recovery["actor_id"],
                    recovery["condition_class"],
                    canonical_json(recovery["previous_state"]),
                    canonical_json(recovery["treatment"]),
                    recovery["elapsed_seconds"],
                    canonical_json(recovery["resources"]),
                    canonical_json(recovery["capability_dependencies"]),
                    canonical_json(recovery["new_state"]),
                    recovery["visibility"],
                ),
            )
        for interaction in plan.auxiliary.get("interactions", []):
            db.execute(
                """
                INSERT INTO cross_domain_interaction_receipt(
                    interaction_id,simulation_cycle_id,source_domain,target_domain,
                    source_capability_ref,target_resistance_ref,evidence_refs_json,
                    resolution_status,outcome_json,invented_power_score,visibility
                ) VALUES(?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    interaction["interaction_id"],
                    plan.cycle_id,
                    interaction["source_domain"],
                    interaction["target_domain"],
                    interaction["source_capability_ref"],
                    interaction["target_resistance_ref"],
                    canonical_json(interaction["evidence_refs"]),
                    interaction["resolution_status"],
                    canonical_json(interaction["outcome"]),
                    0,
                    interaction["visibility"],
                ),
            )
        for project in plan.auxiliary.get("projects", []):
            db.execute(
                """
                INSERT INTO project_evaluation_receipt(
                    project_evaluation_id,simulation_cycle_id,project_clock_id,
                    stage_before,stage_after,outcome_degree,elapsed_seconds,
                    action_cost,resource_effects_json,blockers_json,output_json,
                    basis_hash,visibility
                ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    project["project_evaluation_id"],
                    plan.cycle_id,
                    project["project_clock_id"],
                    project["stage_before"],
                    project["stage_after"],
                    project["outcome_degree"],
                    project["elapsed_seconds"],
                    project["action_cost"],
                    canonical_json(project["resource_effects"]),
                    canonical_json(project["blockers"]),
                    canonical_json(project["output"]),
                    project["basis_hash"],
                    project["visibility"],
                ),
            )
        for debt in plan.auxiliary.get("consequence_debts", []):
            db.execute(
                """
                INSERT INTO consequence_debt_record(
                    consequence_debt_id,causal_event_ref,required_reaction_class,
                    debtor_actor_or_faction_id,created_campaign_time_ref,
                    earliest_discharge_seconds,status,visibility,payload_json
                ) VALUES(?,?,?,?,?,?,?,?,?)
                """,
                (
                    debt["consequence_debt_id"],
                    debt["causal_event_ref"],
                    debt["required_reaction_class"],
                    debt["debtor_actor_or_faction_id"],
                    debt["created_campaign_time_ref"],
                    debt["earliest_discharge_seconds"],
                    debt["status"],
                    debt["visibility"],
                    canonical_json(debt["payload"]),
                ),
            )
        for transition in plan.auxiliary.get("debt_transitions", []):
            db.execute(
                """
                INSERT INTO consequence_debt_transition(
                    debt_transition_id,consequence_debt_id,simulation_cycle_id,
                    from_status,to_status,discharge_form,causal_basis_json,
                    elapsed_seconds,visibility
                ) VALUES(?,?,?,?,?,?,?,?,?)
                """,
                (
                    transition["debt_transition_id"],
                    transition["consequence_debt_id"],
                    plan.cycle_id,
                    transition["from_status"],
                    transition["to_status"],
                    transition["discharge_form"],
                    canonical_json(transition["causal_basis"]),
                    transition["elapsed_seconds"],
                    transition["visibility"],
                ),
            )

    draft = TurnDraft(
        source_turn_id=f"simulation-turn:{sha256_json({'campaign': campaign_id, 'cycle': plan.cycle_id})}",
        source_message_id=None,  # type: ignore[arg-type]
        expected_runtime_hash=expected_runtime_hash,
        phase_before="CONTROL",
        step_before="WORLD_SIMULATION_DRAFT",
        phase_after="CONTROL",
        step_after="WORLD_SIMULATION_COMMITTED",
        player_declaration="Synthetic world-system verification" if synthetic else "Committed elapsed-time world cycle",
        adjudication={
            "kind": "COUPLED_WORLD_SIMULATION",
            "cycle_id": plan.cycle_id,
            "systems": list(plan.effect_system_ids),
            "synthetic": synthetic,
        },
        narration=None,
        elapsed_min_seconds=elapsed_campaign_seconds,
        elapsed_max_seconds=elapsed_campaign_seconds,
        mutations=plan.mutations,
        schema_version=3,
    )
    transaction_id = commit_turn(
        connection, draft, transaction_side_effect=side_effect
    )
    return {
        "cycle_id": plan.cycle_id,
        "transaction_id": transaction_id,
        "runtime_hash_after": current_runtime_hash(connection),
        "integrity": verify_database(connection)["status"],
        "effects": len(plan.mutations),
    }
