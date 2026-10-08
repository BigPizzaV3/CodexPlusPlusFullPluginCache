from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any, Mapping

from .jsonutil import canonical_json, normalize_json_text, sha256_text
from .kernel import DOMAIN_STATES, GENESIS_HASH, current_runtime_hash


JSON_COLUMNS = {
    "payload_json", "evidence_kinds_json", "query_json", "value_json",
    "object_json", "effect_json", "temporal_anchor_json", "exact_value_json",
    "authoritative_current_value_json", "adjudication_json", "previous_json",
    "delta_json", "new_json", "aliases_json", "state_json", "access_path_json",
    "stage_model_json", "eligible_events_json", "roll_json", "modifiers_json",
    "selected_result_json", "causality_json", "owned_state_json", "cadence_json",
    "triggers_json", "inputs_json", "outputs_json", "dependencies_json",
    "invariants_json", "consumers_json", "content_json",
}
NON_CANONICAL_COLUMNS = {"recorded_at", "applied_at"}


def primary_key_columns(connection: sqlite3.Connection, table: str) -> list[str]:
    rows = connection.execute(f"PRAGMA table_info({table})").fetchall()
    keys = sorted(
        ((int(row["pk"]), row["name"]) for row in rows if row["pk"]),
        key=lambda item: item[0],
    )
    return [name for _, name in keys]


def canonical_columns(connection: sqlite3.Connection, table: str) -> list[str]:
    return [
        row["name"]
        for row in connection.execute(f"PRAGMA table_info({table})")
        if row["name"] not in NON_CANONICAL_COLUMNS
    ]


def normalize_row_value(column: str, value: Any) -> Any:
    if column in JSON_COLUMNS and value is not None:
        return normalize_json_text(value)
    return value


def table_rows(connection: sqlite3.Connection, table: str) -> list[dict[str, Any]]:
    columns = canonical_columns(connection, table)
    order = primary_key_columns(connection, table) or columns
    rows = connection.execute(
        f"SELECT {', '.join(columns)} FROM {table} ORDER BY {', '.join(order)}"
    ).fetchall()
    return [
        {column: normalize_row_value(column, row[column]) for column in columns}
        for row in rows
    ]


def export_database(
    connection: sqlite3.Connection,
    destination: str | Path,
    *,
    table_map: Mapping[str, str],
    visibility_label: str,
) -> dict[str, Any]:
    """Deterministically export an explicitly supplied table/view map.

    Campaign/reconstruction policy chooses the map. The generic engine does not
    decide that one fixed list of tables is globally canonical.
    """
    root = Path(destination)
    root.mkdir(parents=True, exist_ok=True)
    files: list[dict[str, Any]] = []
    for output_name, source_name in sorted(table_map.items()):
        path = root / f"{output_name}.jsonl"
        rows = table_rows(connection, source_name)
        content = "".join(canonical_json(row) + "\n" for row in rows)
        path.write_text(content, encoding="utf-8")
        files.append({
            "path": path.name,
            "rows": len(rows),
            "sha256": sha256_text(content),
            "size_bytes": len(content.encode("utf-8")),
        })
    last = connection.execute(
        "SELECT transaction_hash FROM transaction_log ORDER BY rowid DESC LIMIT 1"
    ).fetchone()
    manifest = {
        "schema": "aidm4.deterministic_export.v2",
        "visibility": visibility_label,
        "runtime_hash": current_runtime_hash(connection),
        "last_transaction_hash": last["transaction_hash"] if last else GENESIS_HASH,
        "files": files,
    }
    (root/"MANIFEST.json").write_text(canonical_json(manifest)+"\n", encoding="utf-8")
    return manifest


def rebuild_runtime_projection(
    connection: sqlite3.Connection,
    *,
    scope_id: str,
    gameplay_authorized: bool,
    protected_boundary: str | None = None,
    projection_id: str | None = None,
    domain_states: Mapping[str, tuple[str, str, str, str]] = DOMAIN_STATES,
) -> dict[str, Any]:
    """Build a campaign-neutral current projection from canonical domain states."""
    last = connection.execute(
        """
        SELECT transaction_hash,phase_after,step_after
        FROM transaction_log ORDER BY rowid DESC LIMIT 1
        """
    ).fetchone()
    projection: dict[str, Any] = {
        "schema": "aidm4.current_runtime_projection.v2",
        "runtime_hash": current_runtime_hash(connection),
        "source_transaction_hash": last["transaction_hash"] if last else GENESIS_HASH,
        "phase": last["phase_after"] if last else "CONTROL",
        "phase_step": last["step_after"] if last else "NO_COMMITTED_GAMEPLAY",
        "gameplay_authorized": bool(gameplay_authorized),
        "protected_boundary": protected_boundary,
        "domains": {},
    }
    for domain, (_, table, identity_key, _) in sorted(domain_states.items()):
        rows = connection.execute(
            f"""
            SELECT {identity_key} AS identity,state_json,version,visibility
            FROM {table}
            WHERE visibility='VISIBLE'
            ORDER BY {identity_key}
            """
        ).fetchall()
        projection["domains"][domain] = [
            {
                "id": row["identity"],
                "state": normalize_json_text(row["state_json"]),
                "version": row["version"],
            }
            for row in rows
        ]
    content = canonical_json(projection)
    digest = sha256_text(content)
    pid = projection_id or f"projection:current-runtime:{scope_id}:visible"
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
        (
            pid, "CURRENT_RUNTIME", scope_id, projection["source_transaction_hash"],
            content, digest, "VISIBLE",
        ),
    )
    return projection
