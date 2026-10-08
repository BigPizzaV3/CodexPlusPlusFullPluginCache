#!/usr/bin/env python3
"""Local fixed-point budget ledger for Empire Review."""

from __future__ import annotations

import hashlib
import json
import os
import sqlite3
import sys
import uuid
from datetime import datetime, timedelta, timezone
from decimal import ROUND_CEILING, Decimal, InvalidOperation
from pathlib import Path
from typing import Any

MICRO_USD = Decimal("1000000")


def platform_data_dir() -> Path:
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "empire-codex-router"
    if sys.platform == "win32":
        root = os.environ.get("LOCALAPPDATA") or os.environ.get("APPDATA")
        return (
            Path(root) / "Empire Codex Router"
            if root
            else Path.home() / "AppData" / "Local" / "Empire Codex Router"
        )
    root = os.environ.get("XDG_DATA_HOME")
    return (
        Path(root) / "empire-codex-router"
        if root
        else Path.home() / ".local" / "share" / "empire-codex-router"
    )


DEFAULT_BUDGET_DB = platform_data_dir() / "budget.sqlite3"


class BudgetError(Exception):
    pass


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def usd_to_microusd(value: Any) -> int:
    try:
        amount = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise BudgetError("USD value must be a valid decimal number") from exc
    if not amount.is_finite() or amount < 0:
        raise BudgetError("USD value must be finite and non-negative")
    return int((amount * MICRO_USD).to_integral_value(rounding=ROUND_CEILING))


def microusd_to_usd(value: int | None) -> float | None:
    if value is None:
        return None
    return float(Decimal(value) / MICRO_USD)


def project_identity(repository_root: str | Path) -> tuple[str, str]:
    root = Path(repository_root).expanduser().resolve()
    digest = hashlib.sha256(str(root).encode("utf-8")).hexdigest()[:20]
    return f"project-{digest}", root.name or "repository"


def pricing_snapshot_id(model: dict[str, Any], generated_at: str | None) -> str:
    payload = {
        "generated_at": generated_at or "unknown",
        "model_id": model["id"],
        "prompt_price": str(model["prompt_price"]),
        "completion_price": str(model["completion_price"]),
        "pricing_components": {
            key: None if value is None else str(value)
            for key, value in sorted((model.get("pricing_components") or {}).items())
        },
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "price-" + hashlib.sha256(encoded).hexdigest()[:20]


class BudgetStore:
    """Durable budget, reconciliation, and nondelivery-compensation ledger."""

    def __init__(self, path: str | Path | None = None):
        configured = path or os.environ.get("EMPIRE_BUDGET_DB") or DEFAULT_BUDGET_DB
        self.path = Path(configured).expanduser().resolve()
        self.path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        try:
            os.chmod(self.path.parent, 0o700)
        except OSError:
            pass
        self.connection = sqlite3.connect(self.path, timeout=10, isolation_level=None)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA busy_timeout = 10000")
        self.connection.execute("PRAGMA journal_mode = WAL")
        self.connection.execute("PRAGMA synchronous = FULL")
        self._initialize()
        try:
            os.chmod(self.path, 0o600)
        except OSError:
            pass

    def close(self) -> None:
        self.connection.close()

    def __enter__(self) -> "BudgetStore":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def _initialize(self) -> None:
        self.connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS reservations (
                reservation_id TEXT PRIMARY KEY,
                project_id TEXT NOT NULL,
                project_name TEXT NOT NULL,
                provider TEXT NOT NULL,
                model_id TEXT NOT NULL,
                authorized_microusd INTEGER NOT NULL CHECK (authorized_microusd >= 0),
                observed_microusd INTEGER,
                price_snapshot_id TEXT NOT NULL,
                state TEXT NOT NULL CHECK (
                    state IN (
                        'open', 'dispatched', 'pending_reconciliation',
                        'settled', 'released', 'expired'
                    )
                ),
                dispatch_count INTEGER NOT NULL DEFAULT 0,
                provider_generation_id TEXT,
                provider_request_id TEXT,
                last_outcome TEXT,
                created_at TEXT NOT NULL,
                expires_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );
            CREATE INDEX IF NOT EXISTS reservations_project_state
                ON reservations(project_id, state);

            CREATE TABLE IF NOT EXISTS cost_events (
                event_id TEXT PRIMARY KEY,
                project_id TEXT NOT NULL,
                project_name TEXT NOT NULL,
                event_type TEXT NOT NULL CHECK (
                    event_type IN ('budget_limit_set', 'cost_settled', 'cost_adjusted')
                ),
                amount_microusd INTEGER NOT NULL,
                reservation_id TEXT,
                provider TEXT,
                model_id TEXT,
                price_snapshot_id TEXT,
                created_at TEXT NOT NULL,
                details_json TEXT NOT NULL DEFAULT '{}'
            );
            CREATE INDEX IF NOT EXISTS cost_events_project_type
                ON cost_events(project_id, event_type);

            CREATE TABLE IF NOT EXISTS reconciliation_events (
                event_id TEXT PRIMARY KEY,
                reservation_id TEXT NOT NULL,
                project_id TEXT NOT NULL,
                event_type TEXT NOT NULL CHECK (
                    event_type IN (
                        'dispatch_started', 'outcome_ambiguous',
                        'conservative_expiry', 'late_settlement',
                        'manual_release'
                    )
                ),
                provider_request_id TEXT,
                created_at TEXT NOT NULL,
                details_json TEXT NOT NULL DEFAULT '{}'
            );
            CREATE INDEX IF NOT EXISTS reconciliation_reservation
                ON reconciliation_events(reservation_id, created_at);

            CREATE TABLE IF NOT EXISTS compensation_records (
                compensation_id TEXT PRIMARY KEY,
                reservation_id TEXT NOT NULL UNIQUE,
                project_id TEXT NOT NULL,
                project_name TEXT NOT NULL,
                provider TEXT NOT NULL,
                model_id TEXT NOT NULL,
                observed_microusd INTEGER NOT NULL CHECK (observed_microusd > 0),
                response_id TEXT,
                state TEXT NOT NULL CHECK (
                    state IN ('needed', 'pending_claim', 'credited', 'refunded', 'denied')
                ),
                evidence_reference TEXT,
                reason TEXT NOT NULL,
                opened_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );
            CREATE INDEX IF NOT EXISTS compensation_project_state
                ON compensation_records(project_id, state, updated_at);
            """
        )
        self._migrate_reservations_schema()

    def _migrate_reservations_schema(self) -> None:
        """Upgrade pre-reconciliation ledgers without discarding local history."""
        row = self.connection.execute(
            "SELECT sql FROM sqlite_master WHERE type = 'table' AND name = 'reservations'"
        ).fetchone()
        sql = str(row[0] if row else "")
        columns = {
            item[1]
            for item in self.connection.execute("PRAGMA table_info(reservations)")
        }
        required_columns = {"dispatch_count", "provider_request_id", "last_outcome"}
        if "pending_reconciliation" not in sql or not required_columns <= columns:
            self._begin()
            try:
                self.connection.execute("DROP INDEX IF EXISTS reservations_project_state")
                self.connection.execute(
                    "ALTER TABLE reservations RENAME TO reservations_legacy"
                )
                self.connection.execute(
                    """
                    CREATE TABLE reservations (
                        reservation_id TEXT PRIMARY KEY,
                        project_id TEXT NOT NULL,
                        project_name TEXT NOT NULL,
                        provider TEXT NOT NULL,
                        model_id TEXT NOT NULL,
                        authorized_microusd INTEGER NOT NULL
                            CHECK (authorized_microusd >= 0),
                        observed_microusd INTEGER,
                        price_snapshot_id TEXT NOT NULL,
                        state TEXT NOT NULL CHECK (
                            state IN (
                                'open', 'dispatched', 'pending_reconciliation',
                                'settled', 'released', 'expired'
                            )
                        ),
                        dispatch_count INTEGER NOT NULL DEFAULT 0,
                        provider_generation_id TEXT,
                        provider_request_id TEXT,
                        last_outcome TEXT,
                        created_at TEXT NOT NULL,
                        expires_at TEXT NOT NULL,
                        updated_at TEXT NOT NULL
                    )
                    """
                )
                self.connection.execute(
                    """
                    INSERT INTO reservations (
                        reservation_id, project_id, project_name, provider, model_id,
                        authorized_microusd, observed_microusd, price_snapshot_id,
                        state, dispatch_count, provider_generation_id,
                        provider_request_id, last_outcome, created_at, expires_at,
                        updated_at
                    )
                    SELECT
                        reservation_id, project_id, project_name, provider, model_id,
                        authorized_microusd, observed_microusd, price_snapshot_id,
                        state, 0, NULL, NULL, NULL, created_at, expires_at, updated_at
                    FROM reservations_legacy
                    """
                )
                self.connection.execute("DROP TABLE reservations_legacy")
                self.connection.execute(
                    "CREATE INDEX reservations_project_state "
                    "ON reservations(project_id, state)"
                )
                self.connection.commit()
            except Exception:
                self.connection.rollback()
                raise
        columns = {
            item[1]
            for item in self.connection.execute("PRAGMA table_info(reservations)")
        }
        if "provider_generation_id" not in columns:
            self.connection.execute(
                "ALTER TABLE reservations ADD COLUMN provider_generation_id TEXT"
            )

    def _begin(self) -> None:
        self.connection.execute("BEGIN IMMEDIATE")

    def _expire(self, now: str) -> None:
        self.connection.execute(
            "UPDATE reservations SET state = 'expired', updated_at = ? "
            "WHERE state = 'open' AND expires_at <= ?",
            (now, now),
        )
        unresolved = self.connection.execute(
            "SELECT * FROM reservations "
            "WHERE state IN ('dispatched', 'pending_reconciliation') "
            "AND expires_at <= ?",
            (now,),
        ).fetchall()
        for row in unresolved:
            details = json.dumps(
                {
                    "settlement_source": "conservative_authorized_maximum",
                    "reason": "unresolved_provider_outcome_expired",
                    "authorized_microusd": row["authorized_microusd"],
                },
                sort_keys=True,
            )
            self.connection.execute(
                "INSERT INTO cost_events "
                "(event_id, project_id, project_name, event_type, amount_microusd, "
                "reservation_id, provider, model_id, price_snapshot_id, created_at, details_json) "
                "VALUES (?, ?, ?, 'cost_settled', ?, ?, ?, ?, ?, ?, ?)",
                (
                    str(uuid.uuid4()),
                    row["project_id"],
                    row["project_name"],
                    row["authorized_microusd"],
                    row["reservation_id"],
                    row["provider"],
                    row["model_id"],
                    row["price_snapshot_id"],
                    now,
                    details,
                ),
            )
            self.connection.execute(
                "UPDATE reservations SET state = 'settled', "
                "observed_microusd = authorized_microusd, "
                "last_outcome = 'conservative_expiry', updated_at = ? "
                "WHERE reservation_id = ?",
                (now, row["reservation_id"]),
            )
            self._record_reconciliation(
                row,
                "conservative_expiry",
                now,
                {"cost_basis": "authorized_maximum"},
            )

    def _record_reconciliation(
        self,
        row: sqlite3.Row,
        event_type: str,
        created_at: str,
        details: dict[str, Any] | None = None,
        provider_request_id: str | None = None,
    ) -> None:
        self.connection.execute(
            "INSERT INTO reconciliation_events "
            "(event_id, reservation_id, project_id, event_type, "
            "provider_request_id, created_at, details_json) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                str(uuid.uuid4()),
                row["reservation_id"],
                row["project_id"],
                event_type,
                provider_request_id or row["provider_request_id"],
                created_at,
                json.dumps(details or {}, sort_keys=True),
            ),
        )

    def _limit(self, project_id: str) -> int | None:
        row = self.connection.execute(
            "SELECT amount_microusd FROM cost_events "
            "WHERE project_id = ? AND event_type = 'budget_limit_set' "
            "ORDER BY rowid DESC LIMIT 1",
            (project_id,),
        ).fetchone()
        return int(row[0]) if row else None

    def _settled(self, project_id: str) -> int:
        row = self.connection.execute(
            "SELECT COALESCE(SUM(amount_microusd), 0) FROM cost_events "
            "WHERE project_id = ? AND event_type IN ('cost_settled', 'cost_adjusted')",
            (project_id,),
        ).fetchone()
        return int(row[0])

    def _reserved(self, project_id: str) -> int:
        row = self.connection.execute(
            "SELECT COALESCE(SUM(authorized_microusd), 0) FROM reservations "
            "WHERE project_id = ? "
            "AND state IN ('open', 'dispatched', 'pending_reconciliation')",
            (project_id,),
        ).fetchone()
        return int(row[0])

    def set_limit(
        self, project_id: str, project_name: str, limit_microusd: int
    ) -> dict[str, Any]:
        if limit_microusd < 0:
            raise BudgetError("Budget limit must be non-negative")
        now = utcnow().isoformat()
        self._begin()
        try:
            self.connection.execute(
                "INSERT INTO cost_events "
                "(event_id, project_id, project_name, event_type, amount_microusd, created_at) "
                "VALUES (?, ?, ?, 'budget_limit_set', ?, ?)",
                (str(uuid.uuid4()), project_id, project_name, limit_microusd, now),
            )
            self.connection.commit()
        except Exception:
            self.connection.rollback()
            raise
        return self.status(project_id, project_name)

    def status(self, project_id: str, project_name: str) -> dict[str, Any]:
        now = utcnow().isoformat()
        self._begin()
        try:
            self._expire(now)
            limit = self._limit(project_id)
            settled = self._settled(project_id)
            reserved = self._reserved(project_id)
            reconciliation = self.connection.execute(
                "SELECT COUNT(*) FROM reservations WHERE project_id = ? "
                "AND state IN ('dispatched', 'pending_reconciliation')",
                (project_id,),
            ).fetchone()
            self.connection.commit()
        except Exception:
            self.connection.rollback()
            raise
        remaining = None if limit is None else max(0, limit - settled - reserved)
        if limit is None:
            state = "unconfigured"
        elif remaining == 0:
            state = "exhausted"
        else:
            state = "available"
        return {
            "status": state,
            "project_id": project_id,
            "project_name": project_name,
            "project_limit_usd": microusd_to_usd(limit),
            "settled_spend_usd": microusd_to_usd(settled),
            "active_reservations_usd": microusd_to_usd(reserved),
            "pending_reconciliation_count": int(reconciliation[0]),
            "unresolved_provider_outcome_count": int(reconciliation[0]),
            "project_budget_remaining_usd": microusd_to_usd(remaining),
            "accounting": "local_fixed_point_microusd",
        }

    def history(
        self, project_id: str, project_name: str, limit: int = 50
    ) -> dict[str, Any]:
        bounded_limit = min(500, max(1, int(limit)))
        rows = self.connection.execute(
            "SELECT event_type, amount_microusd, reservation_id, provider, model_id, "
            "price_snapshot_id, created_at, details_json FROM cost_events "
            "WHERE project_id = ? ORDER BY rowid DESC LIMIT ?",
            (project_id, bounded_limit),
        ).fetchall()
        return {
            "status": "available",
            "project_id": project_id,
            "project_name": project_name,
            "event_count": len(rows),
            "events": [
                {
                    "event_type": row["event_type"],
                    "amount_usd": microusd_to_usd(row["amount_microusd"]),
                    "reservation_id": row["reservation_id"],
                    "provider": row["provider"],
                    "model_id": row["model_id"],
                    "price_snapshot_id": row["price_snapshot_id"],
                    "created_at": row["created_at"],
                    "details": json.loads(row["details_json"] or "{}"),
                }
                for row in rows
            ],
            "storage": "private_platform_user_data",
            "contains_credentials": False,
        }

    def reserve(
        self,
        project_id: str,
        project_name: str,
        provider: str,
        model_id: str,
        authorized_microusd: int,
        price_snapshot_id: str,
        ttl_seconds: int = 600,
    ) -> tuple[str | None, dict[str, Any]]:
        if authorized_microusd < 0:
            raise BudgetError("Reservation amount must be non-negative")
        created = utcnow()
        now = created.isoformat()
        expires = (created + timedelta(seconds=max(60, ttl_seconds))).isoformat()
        reservation_id = str(uuid.uuid4())
        self._begin()
        try:
            self._expire(now)
            limit = self._limit(project_id)
            settled = self._settled(project_id)
            reserved = self._reserved(project_id)
            available = None if limit is None else max(0, limit - settled - reserved)
            if available is not None and authorized_microusd > available:
                self.connection.commit()
                return None, self.status(project_id, project_name)
            self.connection.execute(
                "INSERT INTO reservations "
                "(reservation_id, project_id, project_name, provider, model_id, "
                "authorized_microusd, price_snapshot_id, state, created_at, expires_at, updated_at) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, 'open', ?, ?, ?)",
                (
                    reservation_id,
                    project_id,
                    project_name,
                    provider,
                    model_id,
                    authorized_microusd,
                    price_snapshot_id,
                    now,
                    expires,
                    now,
                ),
            )
            self.connection.commit()
        except Exception:
            self.connection.rollback()
            raise
        return reservation_id, self.status(project_id, project_name)

    def release(self, reservation_id: str) -> None:
        now = utcnow().isoformat()
        self.connection.execute(
            "UPDATE reservations SET state = 'released', "
            "last_outcome = 'released_before_ambiguous_outcome', updated_at = ? "
            "WHERE reservation_id = ? AND state IN ('open', 'dispatched')",
            (now, reservation_id),
        )

    def mark_dispatched(
        self,
        reservation_id: str,
        provider_request_id: str | None = None,
        provider_generation_id: str | None = None,
    ) -> dict[str, Any]:
        """Durably record dispatch before transport can create an ambiguous bill."""
        request_id = self._provider_reference(provider_request_id)
        generation_id = self._provider_reference(provider_generation_id)
        now = utcnow().isoformat()
        self._begin()
        try:
            row = self.connection.execute(
                "SELECT * FROM reservations WHERE reservation_id = ?",
                (reservation_id,),
            ).fetchone()
            if not row or row["state"] not in ("open", "dispatched"):
                raise BudgetError("Reservation cannot be dispatched")
            for field, value in (
                ("provider_generation_id", generation_id),
                ("provider_request_id", request_id),
            ):
                if value is not None and row[field] not in (None, value):
                    raise BudgetError("Provider reference conflicts with durable ledger")
            self.connection.execute(
                "UPDATE reservations SET state = 'dispatched', "
                "dispatch_count = dispatch_count + 1, "
                "provider_request_id = COALESCE(provider_request_id, ?), "
                "provider_generation_id = COALESCE(provider_generation_id, ?), "
                "last_outcome = 'dispatch_started', updated_at = ? "
                "WHERE reservation_id = ?",
                (
                    request_id,
                    generation_id,
                    now,
                    reservation_id,
                ),
            )
            self._record_reconciliation(
                row,
                "dispatch_started",
                now,
                {"attempt": int(row["dispatch_count"]) + 1},
                request_id,
            )
            self.connection.commit()
        except Exception:
            self.connection.rollback()
            raise
        return self.reservation(reservation_id)

    @staticmethod
    def _provider_reference(value: str | None) -> str | None:
        if value is None:
            return None
        normalized = value.strip()
        if not normalized:
            return None
        if len(normalized) > 200 or any(ord(character) < 33 for character in normalized):
            raise BudgetError("Provider reference is invalid")
        return normalized

    def record_provider_references(
        self,
        reservation_id: str,
        *,
        provider_generation_id: str | None = None,
        provider_request_id: str | None = None,
    ) -> dict[str, Any]:
        """Attach immutable provider identifiers as soon as they are observed."""
        generation_id = self._provider_reference(provider_generation_id)
        request_id = self._provider_reference(provider_request_id)
        if generation_id is None and request_id is None:
            return self.reservation(reservation_id)
        now = utcnow().isoformat()
        self._begin()
        try:
            row = self.connection.execute(
                "SELECT * FROM reservations WHERE reservation_id = ?",
                (reservation_id,),
            ).fetchone()
            if not row:
                raise BudgetError("Reservation does not exist")
            for field, value in (
                ("provider_generation_id", generation_id),
                ("provider_request_id", request_id),
            ):
                if value is not None and row[field] not in (None, value):
                    raise BudgetError("Provider reference conflicts with durable ledger")
            self.connection.execute(
                "UPDATE reservations SET "
                "provider_generation_id = COALESCE(provider_generation_id, ?), "
                "provider_request_id = COALESCE(provider_request_id, ?), "
                "updated_at = ? WHERE reservation_id = ?",
                (generation_id, request_id, now, reservation_id),
            )
            self.connection.commit()
        except Exception:
            self.connection.rollback()
            raise
        return self.reservation(reservation_id)

    def mark_pending(
        self,
        reservation_id: str,
        reason: str,
        provider_request_id: str | None = None,
        provider_generation_id: str | None = None,
    ) -> dict[str, Any]:
        """Keep an ambiguous dispatch reserved until evidence can reconcile it."""
        now = utcnow().isoformat()
        bounded_reason = reason.strip()[:160] or "ambiguous_provider_outcome"
        request_id = self._provider_reference(provider_request_id)
        generation_id = self._provider_reference(provider_generation_id)
        self._begin()
        try:
            row = self.connection.execute(
                "SELECT * FROM reservations WHERE reservation_id = ?",
                (reservation_id,),
            ).fetchone()
            if not row:
                raise BudgetError("Reservation does not exist")
            already_pending = row["state"] == "pending_reconciliation"
            if row["state"] not in (
                "open",
                "dispatched",
                "pending_reconciliation",
            ):
                raise BudgetError("Reservation cannot enter reconciliation")
            conflicts = [
                field
                for field, value in (
                    ("provider_generation_id", generation_id),
                    ("provider_request_id", request_id),
                )
                if value is not None and row[field] not in (None, value)
            ]
            last_outcome = (
                "provider_reference_conflict:" + ",".join(conflicts)
                if conflicts
                else bounded_reason
            )
            self.connection.execute(
                "UPDATE reservations SET state = 'pending_reconciliation', "
                "provider_request_id = COALESCE(provider_request_id, ?), "
                "provider_generation_id = COALESCE(provider_generation_id, ?), "
                "last_outcome = ?, updated_at = ? WHERE reservation_id = ?",
                (
                    request_id,
                    generation_id,
                    last_outcome,
                    now,
                    reservation_id,
                ),
            )
            if not already_pending or conflicts:
                self._record_reconciliation(
                    row,
                    "outcome_ambiguous",
                    now,
                    {
                        "reason": bounded_reason,
                        "provider_reference_conflict_fields": conflicts,
                        "observed_provider_generation_id": generation_id
                        if "provider_generation_id" in conflicts
                        else None,
                        "observed_provider_request_id": request_id
                        if "provider_request_id" in conflicts
                        else None,
                    },
                    request_id,
                )
            self.connection.commit()
        except Exception:
            self.connection.rollback()
            raise
        return self.reservation(reservation_id)

    def reservation(self, reservation_id: str) -> dict[str, Any]:
        row = self.connection.execute(
            "SELECT * FROM reservations WHERE reservation_id = ?",
            (reservation_id,),
        ).fetchone()
        if not row:
            raise BudgetError("Reservation does not exist")
        return {
            "reservation_id": row["reservation_id"],
            "project_id": row["project_id"],
            "provider": row["provider"],
            "model_id": row["model_id"],
            "state": row["state"],
            "authorized_usd": microusd_to_usd(row["authorized_microusd"]),
            "observed_usd": microusd_to_usd(row["observed_microusd"]),
            "dispatch_count": int(row["dispatch_count"]),
            "provider_generation_id": row["provider_generation_id"],
            "provider_request_id": row["provider_request_id"],
            "last_outcome": row["last_outcome"],
            "created_at": row["created_at"],
            "expires_at": row["expires_at"],
            "updated_at": row["updated_at"],
        }

    def compensation_record(self, reservation_id: str) -> dict[str, Any]:
        row = self.connection.execute(
            "SELECT compensation_records.*, "
            "reservations.provider_generation_id, reservations.provider_request_id, "
            "reservations.created_at AS reservation_created_at "
            "FROM compensation_records JOIN reservations USING (reservation_id) "
            "WHERE compensation_records.reservation_id = ?",
            (reservation_id,),
        ).fetchone()
        if not row:
            raise BudgetError("Compensation record does not exist")
        return {
            "compensation_id": row["compensation_id"],
            "reservation_id": row["reservation_id"],
            "project_id": row["project_id"],
            "project_name": row["project_name"],
            "provider": row["provider"],
            "model_id": row["model_id"],
            "observed_microusd": int(row["observed_microusd"]),
            "observed_usd": microusd_to_usd(row["observed_microusd"]),
            "response_id": row["response_id"],
            "provider_generation_id": row["provider_generation_id"],
            "provider_request_id": row["provider_request_id"],
            "reservation_created_at": row["reservation_created_at"],
            "state": row["state"],
            "evidence_reference": row["evidence_reference"],
            "reason": row["reason"],
            "opened_at": row["opened_at"],
            "updated_at": row["updated_at"],
        }

    def open_compensation(
        self,
        reservation_id: str,
        *,
        response_id: str | None = None,
        reason: str = "settled_without_durable_delivery",
    ) -> dict[str, Any]:
        """Idempotently record that a settled paid call delivered no bytes."""
        bounded_response_id = (response_id or "").strip()[:200] or None
        bounded_reason = reason.strip()[:200]
        if not bounded_reason:
            raise BudgetError("A compensation reason is required")
        now = utcnow().isoformat()
        self._begin()
        try:
            existing = self.connection.execute(
                "SELECT reservation_id FROM compensation_records "
                "WHERE reservation_id = ?",
                (reservation_id,),
            ).fetchone()
            if existing:
                self.connection.commit()
                return self.compensation_record(reservation_id)
            reservation = self.connection.execute(
                "SELECT * FROM reservations WHERE reservation_id = ?",
                (reservation_id,),
            ).fetchone()
            if not reservation:
                raise BudgetError("Reservation does not exist")
            observed = int(reservation["observed_microusd"] or 0)
            if reservation["state"] != "settled" or observed <= 0:
                raise BudgetError(
                    "Compensation requires a settled reservation with observed cost"
                )
            self.connection.execute(
                "INSERT INTO compensation_records "
                "(compensation_id, reservation_id, project_id, project_name, "
                "provider, model_id, observed_microusd, response_id, state, "
                "reason, opened_at, updated_at) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'needed', ?, ?, ?)",
                (
                    str(uuid.uuid4()),
                    reservation_id,
                    reservation["project_id"],
                    reservation["project_name"],
                    reservation["provider"],
                    reservation["model_id"],
                    observed,
                    bounded_response_id,
                    bounded_reason,
                    now,
                    now,
                ),
            )
            self.connection.commit()
        except Exception:
            self.connection.rollback()
            raise
        return self.compensation_record(reservation_id)

    def compensations(
        self,
        project_id: str | None = None,
        *,
        state: str | None = None,
        limit: int = 100,
    ) -> dict[str, Any]:
        allowed_states = {"needed", "pending_claim", "credited", "refunded", "denied"}
        if state is not None and state not in allowed_states:
            raise BudgetError("Invalid compensation state")
        clauses: list[str] = []
        values: list[Any] = []
        if project_id is not None:
            clauses.append("project_id = ?")
            values.append(project_id)
        if state is not None:
            clauses.append("state = ?")
            values.append(state)
        where = " WHERE " + " AND ".join(clauses) if clauses else ""
        bounded_limit = min(500, max(1, int(limit)))
        rows = self.connection.execute(
            "SELECT reservation_id FROM compensation_records"
            + where
            + " ORDER BY updated_at DESC LIMIT ?",
            (*values, bounded_limit),
        ).fetchall()
        records = [self.compensation_record(row[0]) for row in rows]
        unresolved = sum(
            record["observed_microusd"]
            for record in records
            if record["state"] in {"needed", "pending_claim"}
        )
        return {
            "status": "attention_required" if unresolved else "clear",
            "record_count": len(records),
            "unresolved_usd": microusd_to_usd(unresolved),
            "records": records,
        }

    def update_compensation(
        self,
        reservation_id: str,
        state: str,
        evidence_reference: str,
    ) -> dict[str, Any]:
        """Advance a compensation record only with an external evidence reference."""
        allowed = {"pending_claim", "credited", "refunded", "denied"}
        if state not in allowed:
            raise BudgetError("Invalid compensation state transition")
        reference = evidence_reference.strip()[:500]
        if not reference:
            raise BudgetError("An evidence reference is required")
        current = self.compensation_record(reservation_id)
        transitions = {
            "needed": allowed,
            "pending_claim": {"credited", "refunded", "denied"},
            "credited": {"credited"},
            "refunded": {"refunded"},
            "denied": {"denied"},
        }
        if state not in transitions[current["state"]]:
            raise BudgetError("Compensation state transition is not allowed")
        self.connection.execute(
            "UPDATE compensation_records SET state = ?, evidence_reference = ?, "
            "updated_at = ? WHERE reservation_id = ?",
            (state, reference, utcnow().isoformat(), reservation_id),
        )
        return self.compensation_record(reservation_id)

    def pending(self, project_id: str, limit: int = 50) -> dict[str, Any]:
        now = utcnow().isoformat()
        self._begin()
        try:
            self._expire(now)
            rows = self.connection.execute(
                "SELECT reservation_id FROM reservations WHERE project_id = ? "
                "AND state IN ('dispatched', 'pending_reconciliation') "
                "ORDER BY updated_at ASC LIMIT ?",
                (project_id, min(500, max(1, int(limit)))),
            ).fetchall()
            self.connection.commit()
        except Exception:
            self.connection.rollback()
            raise
        return {
            "status": "attention_required" if rows else "clear",
            "pending_count": len(rows),
            "reservations": [self.reservation(row[0]) for row in rows],
        }

    def reconcile_release(self, reservation_id: str, reason: str) -> dict[str, Any]:
        """Release only after external evidence proves no billable request exists."""
        now = utcnow().isoformat()
        bounded_reason = reason.strip()[:160]
        if not bounded_reason:
            raise BudgetError("A reconciliation reason is required")
        self._begin()
        try:
            row = self.connection.execute(
                "SELECT * FROM reservations WHERE reservation_id = ?",
                (reservation_id,),
            ).fetchone()
            if not row or row["state"] != "pending_reconciliation":
                raise BudgetError("Reservation is not pending reconciliation")
            self.connection.execute(
                "UPDATE reservations SET state = 'released', last_outcome = ?, "
                "updated_at = ? WHERE reservation_id = ?",
                ("manual_release:" + bounded_reason, now, reservation_id),
            )
            self._record_reconciliation(
                row, "manual_release", now, {"reason": bounded_reason}
            )
            self.connection.commit()
        except Exception:
            self.connection.rollback()
            raise
        return self.reservation(reservation_id)

    def settle(
        self,
        reservation_id: str,
        observed_microusd: int,
        model_id: str | None = None,
        price_snapshot_id: str | None = None,
    ) -> dict[str, Any]:
        if observed_microusd < 0:
            raise BudgetError("Observed cost must be non-negative")
        now = utcnow().isoformat()
        self._begin()
        try:
            row = self.connection.execute(
                "SELECT * FROM reservations WHERE reservation_id = ?",
                (reservation_id,),
            ).fetchone()
            if not row:
                raise BudgetError("Reservation does not exist")
            settled_model = model_id or row["model_id"]
            settled_snapshot = price_snapshot_id or row["price_snapshot_id"]
            if row["state"] == "settled":
                previous = int(row["observed_microusd"] or 0)
                if previous == observed_microusd:
                    self.connection.commit()
                    return self.status(row["project_id"], row["project_name"])
                delta = observed_microusd - previous
                self.connection.execute(
                    "INSERT INTO cost_events "
                    "(event_id, project_id, project_name, event_type, amount_microusd, "
                    "reservation_id, provider, model_id, price_snapshot_id, created_at, details_json) "
                    "VALUES (?, ?, ?, 'cost_adjusted', ?, ?, ?, ?, ?, ?, ?)",
                    (
                        str(uuid.uuid4()),
                        row["project_id"],
                        row["project_name"],
                        delta,
                        reservation_id,
                        row["provider"],
                        settled_model,
                        settled_snapshot,
                        now,
                        json.dumps(
                            {
                                "previous_observed_microusd": previous,
                                "reconciled_observed_microusd": observed_microusd,
                            },
                            sort_keys=True,
                        ),
                    ),
                )
                self.connection.execute(
                    "UPDATE reservations SET observed_microusd = ?, model_id = ?, "
                    "price_snapshot_id = ?, last_outcome = 'late_adjustment', "
                    "updated_at = ? WHERE reservation_id = ?",
                    (
                        observed_microusd,
                        settled_model,
                        settled_snapshot,
                        now,
                        reservation_id,
                    ),
                )
                self._record_reconciliation(
                    row,
                    "late_settlement",
                    now,
                    {"adjustment_microusd": delta},
                )
                self.connection.commit()
                return self.status(row["project_id"], row["project_name"])
            if row["state"] not in ("open", "dispatched", "pending_reconciliation"):
                raise BudgetError("Reservation cannot be settled")
            details = json.dumps(
                {
                    "authorized_microusd": row["authorized_microusd"],
                    "provider_overrun_possible": observed_microusd
                    > row["authorized_microusd"],
                },
                sort_keys=True,
            )
            self.connection.execute(
                "INSERT INTO cost_events "
                "(event_id, project_id, project_name, event_type, amount_microusd, "
                "reservation_id, provider, model_id, price_snapshot_id, created_at, details_json) "
                "VALUES (?, ?, ?, 'cost_settled', ?, ?, ?, ?, ?, ?, ?)",
                (
                    str(uuid.uuid4()),
                    row["project_id"],
                    row["project_name"],
                    observed_microusd,
                    reservation_id,
                    row["provider"],
                    settled_model,
                    settled_snapshot,
                    now,
                    details,
                ),
            )
            self.connection.execute(
                "UPDATE reservations SET state = 'settled', observed_microusd = ?, "
                "model_id = ?, price_snapshot_id = ?, last_outcome = 'settled', "
                "updated_at = ? WHERE reservation_id = ?",
                (
                    observed_microusd,
                    settled_model,
                    settled_snapshot,
                    now,
                    reservation_id,
                ),
            )
            if row["state"] == "pending_reconciliation":
                self._record_reconciliation(
                    row,
                    "late_settlement",
                    now,
                    {"observed_microusd": observed_microusd},
                )
            self.connection.commit()
        except Exception:
            self.connection.rollback()
            raise
        return self.status(row["project_id"], row["project_name"])
