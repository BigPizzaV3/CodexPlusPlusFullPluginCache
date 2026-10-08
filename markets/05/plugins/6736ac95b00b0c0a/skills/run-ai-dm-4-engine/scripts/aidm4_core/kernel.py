from __future__ import annotations

import json
import os
import sqlite3
from dataclasses import asdict, dataclass, field
from typing import Any, Callable

from .jsonutil import canonical_json, normalize_json_text, sha256_json, sha256_text


GENESIS_HASH = "0" * 64
VISIBILITIES = {"VISIBLE", "OBSCURED", "SEALED"}
STATUSES = {"KNOWN", "UNKNOWN", "UNRESOLVED", "ABSENT"}

DOMAIN_STATES: dict[str, tuple[str, str, str, str]] = {
    "actor": ("actor", "actor_state", "actor_id", "actor_id"),
    "relationship": (
        "relationship",
        "relationship_state",
        "relationship_id",
        "relationship_id",
    ),
    "knowledge": (
        "knowledge_packet",
        "knowledge_status",
        "knowledge_packet_id",
        "knowledge_packet_id",
    ),
    "capability": (
        "capability",
        "capability_state",
        "capability_id",
        "capability_id",
    ),
    "mystery": ("mystery", "mystery_state", "mystery_id", "mystery_id"),
    "faction": ("faction", "faction_state", "faction_id", "faction_id"),
    "location": ("location", "location_state", "location_id", "location_id"),
    "item": ("item_record", "item_state", "item_id", "item_id"),
    "project": (
        "project_clock",
        "project_clock_state",
        "project_clock_id",
        "project_clock_id",
    ),
    "thread": (
        "world_thread",
        "world_thread_state",
        "world_thread_id",
        "world_thread_id",
    ),
}


class KernelError(RuntimeError):
    pass


class DuplicateSourceTurn(KernelError):
    pass


class StaleRuntime(KernelError):
    pass


class InvalidMutation(KernelError):
    pass


class SimulatedCrash(KernelError):
    pass


@dataclass(frozen=True)
class Mutation:
    domain: str
    subject_id: str
    state_key: str
    operation: str
    value: Any
    new_status: str
    authority_class: str
    visibility: str
    unit: str | None = None
    expected_previous_status: str | None = None
    expected_previous_value: Any = field(default=None)
    check_previous_value: bool = False


@dataclass(frozen=True)
class TurnDraft:
    source_turn_id: str
    source_message_id: str
    expected_runtime_hash: str
    phase_before: str
    step_before: str
    phase_after: str
    step_after: str
    player_declaration: str
    adjudication: dict[str, Any]
    narration: str | None
    elapsed_min_seconds: int
    elapsed_max_seconds: int
    mutations: tuple[Mutation, ...]
    schema_version: int = 1


def stable_source_turn_id(
    campaign_id: str, conversation_id: str, message_id: str
) -> str:
    material = canonical_json(
        {
            "campaign_id": campaign_id,
            "conversation_id": conversation_id,
            "message_id": message_id,
        }
    )
    return f"turn:{sha256_text(material)}"


def _latest_transaction_hash(connection: sqlite3.Connection) -> str:
    row = connection.execute(
        """
        SELECT transaction_hash
        FROM transaction_log
        ORDER BY rowid DESC
        LIMIT 1
        """
    ).fetchone()
    return row["transaction_hash"] if row else GENESIS_HASH


def current_runtime_hash(connection: sqlite3.Connection) -> str:
    state: dict[str, list[dict[str, Any]]] = {}
    for domain, (_, table, identity_key, _) in sorted(DOMAIN_STATES.items()):
        rows = connection.execute(
            f"""
            SELECT {identity_key} AS identity, state_json, version, visibility
            FROM {table}
            ORDER BY {identity_key}
            """
        ).fetchall()
        state[domain] = [
            {
                "identity": row["identity"],
                "state": normalize_json_text(row["state_json"]),
                "version": row["version"],
                "visibility": row["visibility"],
            }
            for row in rows
        ]
    temporal_authority: list[dict[str, Any]] = []
    if connection.execute(
        """
        SELECT count(*) FROM sqlite_master
        WHERE type='table' AND name='temporal_authority_record'
        """
    ).fetchone()[0]:
        temporal_authority = [
            {
                "id": row["authority_record_id"],
                "axis": row["axis"],
                "status": row["resolution_status"],
                "value": normalize_json_text(row["value_json"]),
                "visibility": row["visibility"],
            }
            for row in connection.execute(
                """
                SELECT authority_record_id, axis, resolution_status,
                       value_json, visibility
                FROM temporal_authority_record
                ORDER BY authority_record_id
                """
            )
        ]
    runtime_snapshots: list[dict[str, Any]] = []
    if connection.execute(
        """
        SELECT count(*) FROM sqlite_master
        WHERE type='table' AND name='runtime_snapshot'
        """
    ).fetchone()[0]:
        runtime_snapshots = [
            {
                "snapshot_id": row["snapshot_id"],
                "content_sha256": row["content_sha256"],
                "visibility": row["visibility"],
            }
            for row in connection.execute(
                """
                SELECT snapshot_id, content_sha256, visibility
                FROM runtime_snapshot
                ORDER BY snapshot_id
                """
            )
        ]
    return sha256_json(
        {
            "last_transaction_hash": _latest_transaction_hash(connection),
            "state": state,
            "temporal_authority": temporal_authority,
            "runtime_snapshots": runtime_snapshots,
        }
    )


def _validate_mutation(mutation: Mutation) -> None:
    if mutation.domain not in DOMAIN_STATES:
        raise InvalidMutation(f"Unsupported domain: {mutation.domain}")
    if mutation.operation not in {"SET", "MERGE", "ADD", "REMOVE", "SUPERSEDE"}:
        raise InvalidMutation(f"Unsupported operation: {mutation.operation}")
    if mutation.visibility not in VISIBILITIES:
        raise InvalidMutation(f"Unsupported visibility: {mutation.visibility}")
    if mutation.new_status not in STATUSES:
        raise InvalidMutation(f"Unsupported status: {mutation.new_status}")
    if (
        mutation.expected_previous_status is not None
        and mutation.expected_previous_status not in STATUSES
    ):
        raise InvalidMutation(
            f"Unsupported expected status: {mutation.expected_previous_status}"
        )
    if mutation.operation == "MERGE" and not isinstance(mutation.value, dict):
        raise InvalidMutation("MERGE requires an object value")
    if mutation.operation == "REMOVE" and mutation.new_status != "ABSENT":
        raise InvalidMutation("REMOVE must result in ABSENT")
    if mutation.new_status in {"UNKNOWN", "UNRESOLVED", "ABSENT"}:
        if mutation.operation in {"ADD", "MERGE"}:
            raise InvalidMutation(
                f"{mutation.operation} cannot produce {mutation.new_status}"
            )


def _current_field(
    connection: sqlite3.Connection, mutation: Mutation
) -> tuple[dict[str, Any], int, str, str, Any]:
    identity_table, state_table, identity_key, state_identity_key = DOMAIN_STATES[
        mutation.domain
    ]
    exists = connection.execute(
        f"SELECT 1 FROM {identity_table} WHERE {identity_key}=?",
        (mutation.subject_id,),
    ).fetchone()
    if not exists:
        raise InvalidMutation(
            f"{mutation.domain} identity does not exist: {mutation.subject_id}"
        )
    row = connection.execute(
        f"""
        SELECT state_json, version, visibility
        FROM {state_table}
        WHERE {state_identity_key}=?
        """,
        (mutation.subject_id,),
    ).fetchone()
    if row:
        state = normalize_json_text(row["state_json"])
        version = int(row["version"])
        row_visibility = row["visibility"]
    else:
        state = {}
        version = 0
        row_visibility = mutation.visibility
    current = state.get(mutation.state_key)
    if current is None:
        previous_status = "ABSENT"
        previous_value = None
    else:
        previous_status = current["status"]
        previous_value = current.get("value")
    return state, version, row_visibility, previous_status, previous_value


def _resolve_mutation(
    connection: sqlite3.Connection, mutation: Mutation
) -> dict[str, Any]:
    _validate_mutation(mutation)
    state, version, row_visibility, previous_status, previous_value = _current_field(
        connection, mutation
    )
    if mutation.expected_previous_status is not None:
        if previous_status != mutation.expected_previous_status:
            raise InvalidMutation(
                f"{mutation.domain}/{mutation.subject_id}/{mutation.state_key} "
                f"expected {mutation.expected_previous_status}, found {previous_status}"
            )
    if mutation.check_previous_value and previous_value != mutation.expected_previous_value:
        raise InvalidMutation(
            f"{mutation.domain}/{mutation.subject_id}/{mutation.state_key} "
            "previous value mismatch"
        )
    if row_visibility != mutation.visibility and version:
        raise InvalidMutation("A state row cannot change visibility through mutation")

    if mutation.operation in {"SET", "SUPERSEDE"}:
        new_value = mutation.value
    elif mutation.operation == "MERGE":
        if previous_status != "KNOWN" or not isinstance(previous_value, dict):
            raise InvalidMutation("MERGE requires a known object previous value")
        new_value = {**previous_value, **mutation.value}
    elif mutation.operation == "ADD":
        if previous_status != "KNOWN":
            raise InvalidMutation("ADD cannot derive an exact value from unknown state")
        if not isinstance(previous_value, (int, float)) or isinstance(
            previous_value, bool
        ):
            raise InvalidMutation("ADD requires a numeric previous value")
        if not isinstance(mutation.value, (int, float)) or isinstance(
            mutation.value, bool
        ):
            raise InvalidMutation("ADD requires a numeric delta")
        new_value = previous_value + mutation.value
    else:
        new_value = None

    if (
        previous_status in {"UNKNOWN", "UNRESOLVED"}
        and mutation.new_status == "KNOWN"
        and mutation.operation not in {"SET", "SUPERSEDE"}
    ):
        raise InvalidMutation("Unknown previous state cannot yield false exactness")
    if (
        previous_status in {"UNKNOWN", "UNRESOLVED"}
        and mutation.new_status == "KNOWN"
        and not mutation.authority_class.startswith(("PRIMARY_", "ADJUDICATED_"))
    ):
        raise InvalidMutation(
            "Resolving unknown state requires primary or adjudicated authority"
        )

    next_field = {
        "status": mutation.new_status,
        "value": new_value,
        "unit": mutation.unit,
        "authority": mutation.authority_class,
    }
    next_state = dict(state)
    if mutation.operation == "REMOVE":
        next_state.pop(mutation.state_key, None)
    else:
        next_state[mutation.state_key] = next_field
    return {
        "mutation": mutation,
        "previous_status": previous_status,
        "previous_value": previous_value,
        "new_value": new_value,
        "next_state": next_state,
        "next_version": version + 1,
    }


def _transaction_material(
    draft: TurnDraft,
    previous_transaction_hash: str,
    input_runtime_hash: str,
    resolved: list[dict[str, Any]],
) -> dict[str, Any]:
    deltas = []
    for item in resolved:
        mutation: Mutation = item["mutation"]
        deltas.append(
            {
                "domain": mutation.domain,
                "subject_id": mutation.subject_id,
                "state_key": mutation.state_key,
                "previous_status": item["previous_status"],
                "previous_value": item["previous_value"],
                "operation": mutation.operation,
                "delta": mutation.value,
                "new_status": mutation.new_status,
                "new_value": item["new_value"],
                "unit": mutation.unit,
                "authority_class": mutation.authority_class,
                "visibility": mutation.visibility,
            }
        )
    return {
        "source_turn_id": draft.source_turn_id,
        "source_message_id": draft.source_message_id,
        "previous_transaction_hash": previous_transaction_hash,
        "input_runtime_hash": input_runtime_hash,
        "phase_before": draft.phase_before,
        "step_before": draft.step_before,
        "phase_after": draft.phase_after,
        "step_after": draft.step_after,
        "player_declaration": draft.player_declaration,
        "adjudication": draft.adjudication,
        "narration_hash": sha256_text(draft.narration) if draft.narration else None,
        "elapsed_min_seconds": draft.elapsed_min_seconds,
        "elapsed_max_seconds": draft.elapsed_max_seconds,
        "deltas": deltas,
        "schema_version": draft.schema_version,
    }


def _crash(
    boundary: int,
    fail_after_boundary: int | None,
    crash_callback: Callable[[int], None] | None,
) -> None:
    if fail_after_boundary is None or boundary != fail_after_boundary:
        return
    if crash_callback:
        crash_callback(boundary)
    raise SimulatedCrash(f"simulated crash at write boundary {boundary}")


def commit_turn(
    connection: sqlite3.Connection,
    draft: TurnDraft,
    *,
    fail_after_boundary: int | None = None,
    crash_callback: Callable[[int], None] | None = None,
    transaction_side_effect: Callable[[sqlite3.Connection, str], None] | None = None,
) -> str:
    if draft.elapsed_min_seconds < 0:
        raise KernelError("elapsed_min_seconds cannot be negative")
    if draft.elapsed_max_seconds < draft.elapsed_min_seconds:
        raise KernelError("elapsed_max_seconds cannot precede elapsed_min_seconds")
    if len(draft.expected_runtime_hash) != 64:
        raise KernelError("expected_runtime_hash must be a SHA-256 digest")
    if not draft.mutations:
        raise KernelError("A substantive commit requires at least one typed mutation")

    try:
        connection.execute("BEGIN IMMEDIATE")
        duplicate = connection.execute(
            "SELECT transaction_id FROM transaction_log WHERE source_turn_id=?",
            (draft.source_turn_id,),
        ).fetchone()
        if duplicate:
            raise DuplicateSourceTurn(draft.source_turn_id)

        input_runtime_hash = current_runtime_hash(connection)
        if input_runtime_hash != draft.expected_runtime_hash:
            raise StaleRuntime(
                f"Expected {draft.expected_runtime_hash}, found {input_runtime_hash}"
            )
        previous_transaction_hash = _latest_transaction_hash(connection)
        resolved = [_resolve_mutation(connection, item) for item in draft.mutations]
        material = _transaction_material(
            draft, previous_transaction_hash, input_runtime_hash, resolved
        )
        visible_deltas = [
            row for row in material["deltas"] if row["visibility"] == "VISIBLE"
        ]
        sealed_deltas = [
            row for row in material["deltas"] if row["visibility"] != "VISIBLE"
        ]
        transaction_hash = sha256_json(material)
        transaction_id = f"txn:{transaction_hash[:32]}"
        connection.execute(
            """
            INSERT INTO transaction_log(
                transaction_id, source_turn_id, source_message_id,
                previous_transaction_hash, transaction_hash, input_runtime_hash,
                phase_before, step_before, phase_after, step_after,
                player_declaration, adjudication_json, narration_hash,
                elapsed_min_seconds, elapsed_max_seconds,
                visible_delta_hash, sealed_delta_hash, schema_version, commit_status
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                transaction_id,
                draft.source_turn_id,
                draft.source_message_id,
                previous_transaction_hash,
                transaction_hash,
                input_runtime_hash,
                draft.phase_before,
                draft.step_before,
                draft.phase_after,
                draft.step_after,
                draft.player_declaration,
                canonical_json(draft.adjudication),
                sha256_text(draft.narration) if draft.narration else None,
                draft.elapsed_min_seconds,
                draft.elapsed_max_seconds,
                sha256_json(visible_deltas),
                sha256_json(sealed_deltas),
                draft.schema_version,
                "COMMITTED",
            ),
        )
        _crash(0, fail_after_boundary, crash_callback)

        for ordinal, item in enumerate(resolved):
            mutation: Mutation = item["mutation"]
            _, state_table, _, state_identity_key = DOMAIN_STATES[mutation.domain]
            connection.execute(
                f"""
                INSERT INTO {state_table}(
                    {state_identity_key}, state_json, version,
                    last_transaction_id, visibility
                ) VALUES(?,?,?,?,?)
                ON CONFLICT({state_identity_key}) DO UPDATE SET
                    state_json=excluded.state_json,
                    version=excluded.version,
                    last_transaction_id=excluded.last_transaction_id
                """,
                (
                    mutation.subject_id,
                    canonical_json(item["next_state"]),
                    item["next_version"],
                    transaction_id,
                    mutation.visibility,
                ),
            )
            delta_material = material["deltas"][ordinal]
            delta_id = f"delta:{sha256_json({'txn': transaction_id, 'ordinal': ordinal, 'delta': delta_material})[:32]}"
            connection.execute(
                """
                INSERT INTO state_delta(
                    delta_id, transaction_id, ordinal, domain, subject_id,
                    state_key, previous_status, previous_json, operation,
                    delta_json, new_status, new_json, unit, authority_class,
                    source_message_id, visibility
                ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    delta_id,
                    transaction_id,
                    ordinal,
                    mutation.domain,
                    mutation.subject_id,
                    mutation.state_key,
                    item["previous_status"],
                    canonical_json(item["previous_value"])
                    if item["previous_status"] != "ABSENT"
                    else None,
                    mutation.operation,
                    canonical_json(mutation.value),
                    mutation.new_status,
                    canonical_json(item["new_value"])
                    if mutation.new_status != "ABSENT"
                    else None,
                    mutation.unit,
                    mutation.authority_class,
                    draft.source_message_id,
                    mutation.visibility,
                ),
            )
            _crash(ordinal + 1, fail_after_boundary, crash_callback)
        if transaction_side_effect is not None:
            transaction_side_effect(connection, transaction_id)
        connection.commit()
        return transaction_id
    except BaseException:
        if connection.in_transaction:
            connection.rollback()
        raise


def hard_exit_crash_callback(exit_code: int = 86) -> Callable[[int], None]:
    def callback(_: int) -> None:
        os._exit(exit_code)

    return callback
