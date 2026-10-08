from __future__ import annotations

import json
import re
import sqlite3
from collections import defaultdict, deque
from collections.abc import Callable, Iterable
from typing import Any

from .jsonutil import canonical_json, sha256_text
from .kernel import GENESIS_HASH


TEMPORAL_PATTERNS: dict[str, re.Pattern[str]] = {
    "CLOCK": re.compile(r"\b(?:[01]?\d|2[0-3]):[0-5]\d\b"),
    "DAY_NUMBER": re.compile(
        r"\b(?:day|w\d+d)\s*(?:one|two|three|four|five|six|seven|eight|nine|ten|\d+)\b",
        re.IGNORECASE,
    ),
    "WEEK_NUMBER": re.compile(
        r"\b(?:strategic\s+)?week\s+(?:one|two|three|four|five|six|seven|eight|nine|ten|"
        r"eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|"
        r"nineteen|twenty|thirty|\d+)(?:[- ](?:one|two|three|four|five|six|seven|"
        r"eight|nine))?\b",
        re.IGNORECASE,
    ),
    "SLEEP_BOUNDARY": re.compile(
        r"\b(?:sleep|slept|wake|woke|waking|overnight|through the night)\b",
        re.IGNORECASE,
    ),
    "DAYPART": re.compile(
        r"\b(?:dawn|morning|noon|afternoon|evening|dusk|night|midnight)\b",
        re.IGNORECASE,
    ),
    "ELAPSED": re.compile(
        r"\b(?:seconds?|minutes?|hours?|days?|weeks?|months?|years?)\s+(?:pass|passed|"
        r"elapsed|later|earlier|ago)\b|\bfor\s+(?:a few|several|\d+)\s+"
        r"(?:seconds?|minutes?|hours?|days?|weeks?|months?|years?)\b",
        re.IGNORECASE,
    ),
    "CALENDAR_OR_SEASON": re.compile(
        r"\b(?:civil date|calendar date|spring|summer|autumn|fall|winter|season)\b",
        re.IGNORECASE,
    ),
}


def temporal_kinds(text: str) -> list[str]:
    return sorted(name for name, pattern in TEMPORAL_PATTERNS.items() if pattern.search(text))


def discover_temporal_candidates(connection: sqlite3.Connection) -> list[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    for row in connection.execute(
        """
        SELECT message_id,session_ordinal,sequence_index,role,content_type,rendered_content
        FROM source_message
        ORDER BY session_ordinal,sequence_index,message_id
        """
    ):
        kinds = temporal_kinds(row["rendered_content"])
        if kinds:
            candidates.append({
                "message_id": row["message_id"],
                "session_ordinal": row["session_ordinal"],
                "sequence_index": row["sequence_index"],
                "role": row["role"],
                "content_type": row["content_type"],
                "rendered_content": row["rendered_content"],
                "kinds": kinds,
            })
    return candidates


def verify_temporal_graph(
    connection: sqlite3.Connection,
    *,
    scope_id: str,
    required_axes: Iterable[str] = (),
    boundary_validator: Callable[[dict[str, Any]], None] | None = None,
) -> dict[str, Any]:
    nodes = {
        row["temporal_node_id"]: row
        for row in connection.execute("SELECT * FROM temporal_node")
    }
    edges: dict[str, list[str]] = defaultdict(list)
    indegree = {node_id: 0 for node_id in nodes}
    checked = 0
    for row in connection.execute("SELECT * FROM temporal_constraint ORDER BY constraint_id"):
        checked += 1
        if row["from_node_id"] not in nodes or row["to_node_id"] not in nodes:
            raise RuntimeError("Temporal constraint references missing node")
        if row["relation"] in {"BEFORE", "NOT_AFTER"}:
            edges[row["from_node_id"]].append(row["to_node_id"])
            indegree[row["to_node_id"]] += 1
    queue = deque(sorted(node for node, degree in indegree.items() if degree == 0))
    visited = 0
    while queue:
        node = queue.popleft()
        visited += 1
        for neighbor in sorted(edges[node]):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    if visited != len(nodes):
        raise RuntimeError("Temporal precedence graph contains a cycle")

    records = {
        row["axis"]: json.loads(row["value_json"])
        for row in connection.execute(
            """
            SELECT * FROM temporal_authority_record
            WHERE scope_id=?
            ORDER BY authority_record_id
            """,
            (scope_id,),
        )
    }
    missing = sorted(set(required_axes) - records.keys())
    if missing:
        raise RuntimeError(f"Missing temporal authority axes: {missing}")
    if boundary_validator is not None:
        boundary_validator(records)

    return {
        "schema": "aidm4.temporal_graph_verification.v2",
        "status": "PASS",
        "scope_id": scope_id,
        "nodes": len(nodes),
        "constraints": checked,
        "precedence_cycle": False,
        "authority_axes": sorted(records),
    }


def rebuild_temporal_projection(
    connection: sqlite3.Connection,
    *,
    scope_id: str,
    campaign_id: str,
    gameplay_authorized: bool,
    source_transaction_hash: str | None = None,
    projection_id: str | None = None,
) -> dict[str, Any]:
    authority = [
        {
            "axis": row["axis"],
            "status": row["resolution_status"],
            "value": json.loads(row["value_json"]),
            "rationale": row["rationale"],
            "confidence": row["confidence"],
        }
        for row in connection.execute(
            """
            SELECT * FROM visible_temporal_authority_record
            WHERE scope_id=?
            ORDER BY axis,authority_record_id
            """,
            (scope_id,),
        )
    ]
    transaction = source_transaction_hash
    if transaction is None:
        last = connection.execute(
            "SELECT transaction_hash FROM transaction_log ORDER BY rowid DESC LIMIT 1"
        ).fetchone()
        transaction = last["transaction_hash"] if last else GENESIS_HASH

    projection = {
        "schema": "aidm4.current_time_projection.v2",
        "campaign_id": campaign_id,
        "scope_id": scope_id,
        "source_transaction_hash": transaction,
        "gameplay_authorized": bool(gameplay_authorized),
        "authority": authority,
    }
    content = canonical_json(projection)
    digest = sha256_text(content)
    pid = projection_id or f"projection:current-time:{scope_id}:visible"
    connection.execute(
        """
        INSERT INTO projection_record(
            projection_id,projection_kind,scope_id,source_transaction_hash,
            content_json,content_sha256,visibility
        ) VALUES(?,?,?,?,?,?,?)
        ON CONFLICT(projection_kind,scope_id,visibility) DO UPDATE SET
            projection_id=excluded.projection_id,
            source_transaction_hash=excluded.source_transaction_hash,
            content_json=excluded.content_json,
            content_sha256=excluded.content_sha256
        """,
        (pid,"CURRENT_TIME",scope_id,transaction,content,digest,"VISIBLE"),
    )
    return projection
