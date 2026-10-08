from __future__ import annotations

import hashlib
import sqlite3
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
MIGRATIONS = REPO / "migrations"


def connect(path: str | Path, *, readonly: bool = False) -> sqlite3.Connection:
    database = Path(path)
    if readonly:
        uri = f"file:{database.resolve().as_posix()}?mode=ro"
        connection = sqlite3.connect(uri, uri=True)
    else:
        database.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(database)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA busy_timeout = 5000")
    if not readonly:
        connection.execute("PRAGMA journal_mode = WAL")
        connection.execute("PRAGMA synchronous = FULL")
    return connection


def _migration_files() -> list[Path]:
    return sorted(MIGRATIONS.glob("*.sql"), key=lambda path: path.name)


def initialize_database(path: str | Path) -> sqlite3.Connection:
    connection = connect(path)
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS schema_migration (
            version INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            sha256 TEXT NOT NULL CHECK(length(sha256) = 64),
            applied_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        ) STRICT
        """
    )
    applied = {
        int(row["version"]): (row["name"], row["sha256"])
        for row in connection.execute(
            "SELECT version, name, sha256 FROM schema_migration"
        )
    }
    for path in _migration_files():
        prefix = path.name.split("_", 1)[0]
        version = int(prefix)
        sql = path.read_text(encoding="utf-8")
        digest = hashlib.sha256(sql.encode("utf-8")).hexdigest()
        if version in applied:
            expected_name, expected_digest = applied[version]
            if expected_name != path.name or expected_digest != digest:
                raise RuntimeError(
                    f"Applied migration {version} differs from {path.name}"
                )
            continue
        with connection:
            connection.executescript(sql)
            connection.execute(
                "INSERT INTO schema_migration(version, name, sha256) VALUES(?,?,?)",
                (version, path.name, digest),
            )
    return connection


def backup_database(source: str | Path, destination: str | Path) -> None:
    target_path = Path(destination)
    target_path.parent.mkdir(parents=True, exist_ok=True)
    with connect(source, readonly=True) as source_connection:
        with sqlite3.connect(target_path) as target_connection:
            source_connection.backup(target_connection)


def restore_database(source: str | Path, destination: str | Path) -> None:
    backup_database(source, destination)
