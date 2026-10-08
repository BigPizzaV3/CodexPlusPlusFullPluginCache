from __future__ import annotations

import json
import math
import sqlite3
from typing import Any

from .jsonutil import canonical_json, sha256_json


class TravelError(RuntimeError):
    pass


class AccessBlocked(TravelError):
    pass


class TravelUnresolved(TravelError):
    pass


def evaluate_conditional_edge(
    connection: sqlite3.Connection,
    edge_id: str,
    observer_id: str,
    context: dict[str, Any],
    *,
    synthetic: bool,
) -> dict[str, Any]:
    row = connection.execute(
        "SELECT * FROM topology_edge WHERE topology_edge_id=?", (edge_id,)
    ).fetchone()
    if row is None:
        raise TravelError(f"unknown topology edge: {edge_id}")
    if row["edge_class"] not in {"CONDITIONAL", "DIMENSIONAL", "REDIRECTING"}:
        raise TravelError("edge does not require conditional evaluation")
    policy = json.loads(row["access_policy_json"])
    clause_keys = {
        key
        for clause in policy.get("clauses", [])
        for key in clause.get("required_all", [])
    }
    redirect_keys = set(policy.get("redirect_when", {}).get("required_all", []))
    relevant = clause_keys | redirect_keys
    if not relevant.issubset(context):
        status = "UNRESOLVED"
    elif redirect_keys and all(context.get(key) is True for key in redirect_keys):
        status = "REDIRECTED"
    elif any(
        all(context.get(key) is True for key in clause.get("required_all", []))
        for clause in policy.get("clauses", [])
    ):
        status = "AVAILABLE"
    else:
        status = "UNAVAILABLE"

    visible = {
        "edge_id": edge_id,
        "observer_id": observer_id,
        "status": status,
        "statement": policy.get(
            "visible_statement",
            "Availability depends on the currently established route and access state.",
        ),
        "destination_node_id": row["destination_node_id"] if status == "AVAILABLE" else None,
        "redirect_node_id": row["redirect_node_id"] if status == "REDIRECTED" else None,
    }
    material = {
        "edge_id": edge_id,
        "observer_id": observer_id,
        "context": context,
        "policy_sha256": sha256_json(policy),
        "status": status,
    }
    evaluation_id = f"topology-eval:{sha256_json(material)[:32]}"
    with connection:
        connection.execute(
            """
            INSERT OR IGNORE INTO topology_evaluation_receipt(
                evaluation_id,topology_edge_id,observer_id,context_sha256,
                policy_sha256,result_status,visible_result_json,sealed_basis_hash,
                synthetic
            ) VALUES(?,?,?,?,?,?,?,?,?)
            """,
            (
                evaluation_id, edge_id, observer_id, sha256_json(context),
                sha256_json(policy), status, canonical_json(visible),
                sha256_json({"policy": policy, "context": context}), int(synthetic),
            ),
        )
    return visible


def record_route_observation(
    connection: sqlite3.Connection,
    *,
    observation_id: str,
    edge_id: str,
    observer_id: str,
    outcome: str,
    evidence_class: str,
    novelty_class: str,
    payload: dict[str, Any],
    visibility: str = "VISIBLE",
) -> None:
    edge = connection.execute(
        "SELECT * FROM topology_edge WHERE topology_edge_id=?", (edge_id,)
    ).fetchone()
    if edge is None:
        raise TravelError(f"unknown topology edge: {edge_id}")
    with connection:
        connection.execute(
            """
            INSERT INTO route_observation(
                observation_id,topology_edge_id,observer_id,traveler_class,
                observed_origin_node_id,observed_destination_node_id,outcome,
                subjective_duration_min_seconds,subjective_duration_max_seconds,
                evidence_class,novelty_class,source_message_id,authority_class,
                visibility,payload_json
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                observation_id, edge_id, observer_id, "OBSERVED_TRAVELER",
                edge["origin_node_id"],
                edge["destination_node_id"] if outcome == "ARRIVED" else None,
                outcome, None, None, evidence_class, novelty_class, None,
                "ADJUDICATED_OBSERVATION", visibility, canonical_json(payload),
            ),
        )


def weather_multiplier(weather: dict[str, Any]) -> tuple[int, int, int]:
    minimum = weather.get("duration_multiplier_min_milli", 1000)
    maximum = weather.get("duration_multiplier_max_milli", minimum)
    if (
        not isinstance(minimum, int)
        or not isinstance(maximum, int)
        or minimum <= 0
        or maximum < minimum
    ):
        raise TravelError("invalid weather multiplier interval")
    if (minimum, maximum) != (1000, 1000) and not weather.get("source_ref"):
        raise TravelError("non-neutral weather effects require a source")
    return minimum, maximum, 1000


def plan_ordinary_travel(
    connection: sqlite3.Connection,
    *,
    plan_id: str,
    observer_id: str,
    edge_ids: tuple[str, ...],
    documents: set[str],
    fuel_available_ml: int,
    supplies_available_units: int,
    weather: dict[str, Any],
    synthetic: bool,
) -> dict[str, Any]:
    if not edge_ids:
        raise TravelError("travel plan requires at least one edge")
    multiplier_min, multiplier_max, denominator = weather_multiplier(weather)
    legs = []
    duration_min = duration_max = fuel = supplies = 0
    origin = destination = previous_destination = None

    for ordinal, edge_id in enumerate(edge_ids):
        row = connection.execute(
            "SELECT * FROM topology_edge WHERE topology_edge_id=?", (edge_id,)
        ).fetchone()
        if row is None:
            raise TravelError(f"unknown edge: {edge_id}")
        if row["edge_class"] != "ORDINARY":
            raise TravelError("ordinary planner cannot collapse a conditional edge")
        if previous_destination is not None and row["origin_node_id"] != previous_destination:
            raise TravelError("route legs are not contiguous")
        if row["duration_min_seconds"] is None or row["duration_max_seconds"] is None:
            raise TravelUnresolved("route duration is unresolved")

        profile = json.loads(row["resource_profile_json"])
        policy = json.loads(row["access_policy_json"])
        required_documents = set(policy.get("required_documents", []))
        if not required_documents.issubset(documents):
            raise AccessBlocked(
                "missing documents: " + ", ".join(sorted(required_documents - documents))
            )

        leg_min = math.floor(row["duration_min_seconds"] * multiplier_min / denominator)
        leg_max = math.ceil(row["duration_max_seconds"] * multiplier_max / denominator)
        distance_max = row["distance_max_m"] or 0
        leg_fuel = math.ceil(distance_max * profile.get("fuel_ml_per_km", 0) / 1000)
        leg_supplies = math.ceil(leg_max * profile.get("supply_units_per_hour", 0) / 3600)
        duration_min += leg_min
        duration_max += leg_max
        fuel += leg_fuel
        supplies += leg_supplies
        origin = origin or row["origin_node_id"]
        destination = row["destination_node_id"]
        previous_destination = destination
        legs.append({
            "ordinal": ordinal,
            "edge_id": edge_id,
            "duration_min_seconds": leg_min,
            "duration_max_seconds": leg_max,
            "distance_min_m": row["distance_min_m"],
            "distance_max_m": row["distance_max_m"],
            "fuel_delta_ml": -leg_fuel,
            "supply_delta_units": -leg_supplies,
            "fatigue_effect": profile.get("fatigue_effect", "NONE"),
            "weather_source_ref": weather.get("source_ref"),
        })

    if fuel > fuel_available_ml:
        raise AccessBlocked(f"insufficient fuel: need {fuel}, have {fuel_available_ml}")
    if supplies > supplies_available_units:
        raise AccessBlocked(f"insufficient supplies: need {supplies}, have {supplies_available_units}")

    result = {
        "plan_id": plan_id,
        "observer_id": observer_id,
        "origin_node_id": origin,
        "destination_node_id": destination,
        "edge_ids": list(edge_ids),
        "duration_min_seconds": duration_min,
        "duration_max_seconds": duration_max,
        "resource_deltas": {"fuel_ml": -fuel, "supply_units": -supplies},
        "weather_source_ref": weather.get("source_ref"),
        "status": "DRAFT_VALID",
        "synthetic": synthetic,
    }
    with connection:
        connection.execute(
            """
            INSERT INTO travel_plan(
                travel_plan_id,observer_id,origin_node_id,destination_node_id,
                route_edge_ids_json,duration_min_seconds,duration_max_seconds,
                resource_deltas_json,access_evidence_json,status,synthetic,
                content_sha256,visibility
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                plan_id,observer_id,origin,destination,canonical_json(edge_ids),
                duration_min,duration_max,canonical_json(result["resource_deltas"]),
                canonical_json({
                    "documents": sorted(documents),
                    "weather_source_ref": weather.get("source_ref"),
                }),
                "DRAFT_VALID",int(synthetic),sha256_json(result),"VISIBLE",
            ),
        )
        connection.executemany(
            """
            INSERT INTO travel_leg(
                travel_plan_id,ordinal,topology_edge_id,duration_min_seconds,
                duration_max_seconds,distance_min_m,distance_max_m,fuel_delta_ml,
                supply_delta_units,fatigue_effect,weather_source_ref
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?)
            """,
            [
                (
                    plan_id,leg["ordinal"],leg["edge_id"],leg["duration_min_seconds"],
                    leg["duration_max_seconds"],leg["distance_min_m"],leg["distance_max_m"],
                    leg["fuel_delta_ml"],leg["supply_delta_units"],leg["fatigue_effect"],
                    leg["weather_source_ref"],
                )
                for leg in legs
            ],
        )
    return result


def find_routes(
    connection: sqlite3.Connection,
    origin_node_id: str,
    destination_node_id: str,
    *,
    include_conditional: bool = False,
    max_legs: int = 8,
) -> list[list[str]]:
    queue: list[tuple[str, list[str], set[str]]] = [(origin_node_id, [], {origin_node_id})]
    routes: list[list[str]] = []
    while queue:
        node, edges, visited = queue.pop(0)
        if len(edges) >= max_legs:
            continue
        rows = connection.execute(
            "SELECT * FROM topology_edge WHERE origin_node_id=? ORDER BY topology_edge_id",
            (node,),
        )
        for row in rows:
            if row["edge_class"] != "ORDINARY" and not include_conditional:
                continue
            next_node = row["destination_node_id"]
            next_edges = edges + [row["topology_edge_id"]]
            if next_node == destination_node_id:
                routes.append(next_edges)
            elif next_node not in visited:
                queue.append((next_node, next_edges, visited | {next_node}))
    return routes
