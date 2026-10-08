from __future__ import annotations

import sqlite3
from typing import Any

from .jsonutil import canonical_json, normalize_json_text, sha256_json
from .kernel import GENESIS_HASH


class IntegrityError(RuntimeError):
    pass


def verify_hash_chain(connection: sqlite3.Connection) -> dict[str, Any]:
    previous = GENESIS_HASH
    checked = 0
    for row in connection.execute(
        "SELECT * FROM transaction_log ORDER BY rowid"
    ):
        if row["previous_transaction_hash"] != previous:
            raise IntegrityError(
                f"Hash-chain predecessor mismatch at {row['transaction_id']}"
            )
        deltas = [
            {
                "domain": delta["domain"],
                "subject_id": delta["subject_id"],
                "state_key": delta["state_key"],
                "previous_status": delta["previous_status"],
                "previous_value": normalize_json_text(delta["previous_json"]),
                "operation": delta["operation"],
                "delta": normalize_json_text(delta["delta_json"]),
                "new_status": delta["new_status"],
                "new_value": normalize_json_text(delta["new_json"]),
                "unit": delta["unit"],
                "authority_class": delta["authority_class"],
                "visibility": delta["visibility"],
            }
            for delta in connection.execute(
                """
                SELECT * FROM state_delta
                WHERE transaction_id=?
                ORDER BY ordinal
                """,
                (row["transaction_id"],),
            )
        ]
        material = {
            "source_turn_id": row["source_turn_id"],
            "source_message_id": row["source_message_id"],
            "previous_transaction_hash": row["previous_transaction_hash"],
            "input_runtime_hash": row["input_runtime_hash"],
            "phase_before": row["phase_before"],
            "step_before": row["step_before"],
            "phase_after": row["phase_after"],
            "step_after": row["step_after"],
            "player_declaration": row["player_declaration"],
            "adjudication": normalize_json_text(row["adjudication_json"]),
            "narration_hash": row["narration_hash"],
            "elapsed_min_seconds": row["elapsed_min_seconds"],
            "elapsed_max_seconds": row["elapsed_max_seconds"],
            "deltas": deltas,
            "schema_version": row["schema_version"],
        }
        calculated = sha256_json(material)
        if calculated != row["transaction_hash"]:
            raise IntegrityError(
                f"Transaction hash mismatch at {row['transaction_id']}"
            )
        visible = [delta for delta in deltas if delta["visibility"] == "VISIBLE"]
        sealed = [delta for delta in deltas if delta["visibility"] != "VISIBLE"]
        if sha256_json(visible) != row["visible_delta_hash"]:
            raise IntegrityError(
                f"Visible delta hash mismatch at {row['transaction_id']}"
            )
        if sha256_json(sealed) != row["sealed_delta_hash"]:
            raise IntegrityError(
                f"Sealed delta hash mismatch at {row['transaction_id']}"
            )
        previous = calculated
        checked += 1
    return {"transactions": checked, "last_hash": previous}


def verify_database(connection: sqlite3.Connection) -> dict[str, Any]:
    integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
    if integrity != "ok":
        raise IntegrityError(f"SQLite integrity check failed: {integrity}")
    foreign_keys = [tuple(row) for row in connection.execute("PRAGMA foreign_key_check")]
    if foreign_keys:
        raise IntegrityError(f"Foreign-key violations: {foreign_keys[:5]}")
    hash_chain = verify_hash_chain(connection)
    leaked = {}
    for view in (
        "visible_state_delta",
        "visible_actor_state",
        "visible_relationship_state",
        "visible_knowledge_status",
        "visible_capability_state",
        "visible_mystery_state",
        "visible_faction_state",
        "visible_location_state",
        "visible_item_state",
        "visible_project_clock_state",
        "visible_world_thread_state",
        "visible_environment_state",
        "visible_random_event_receipt",
        "visible_projection_record",
    ):
        count = connection.execute(
            f"SELECT count(*) FROM {view} WHERE visibility <> 'VISIBLE'"
        ).fetchone()[0]
        if count:
            leaked[view] = count
    if leaked:
        raise IntegrityError(f"Visible views leak restricted rows: {leaked}")
    return {
        "schema": "aidm4.integrity_report.v1",
        "status": "PASS",
        "sqlite_integrity": integrity,
        "foreign_key_violations": 0,
        "hash_chain": hash_chain,
        "visible_view_leaks": 0,
    }
