"""Transactional state and deduplicated immutable file content."""
from __future__ import annotations
import contextlib
import json
import sqlite3
import threading
from pathlib import Path
from .safety import IterationError, sha

class Store:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        self.exports = self.root / "A92"
        self.exports.mkdir(exist_ok=True)
        self.lock = threading.RLock()
        self.db = sqlite3.connect(str(self.root / "A90.db"), timeout=30, check_same_thread=False, isolation_level=None)
        self.db.execute("PRAGMA journal_mode=WAL")
        self.db.execute("PRAGMA synchronous=FULL")
        self.db.execute("PRAGMA foreign_keys=ON")
        self.db.executescript('''
            CREATE TABLE IF NOT EXISTS entities(kind TEXT, id TEXT PRIMARY KEY, data TEXT NOT NULL);
            CREATE INDEX IF NOT EXISTS entity_kind ON entities(kind);
            CREATE TABLE IF NOT EXISTS blobs(hash TEXT PRIMARY KEY, data BLOB NOT NULL);
            CREATE TABLE IF NOT EXISTS files(ns TEXT NOT NULL, path TEXT NOT NULL, hash TEXT NOT NULL REFERENCES blobs(hash), PRIMARY KEY(ns,path));
            CREATE TABLE IF NOT EXISTS events(seq INTEGER PRIMARY KEY AUTOINCREMENT, project TEXT NOT NULL, data TEXT NOT NULL);
        ''')

    @contextlib.contextmanager
    def transaction(self):
        with self.lock:
            self.db.execute("BEGIN IMMEDIATE")
            try:
                yield self
                self.db.execute("COMMIT")
            except BaseException:
                self.db.execute("ROLLBACK")
                raise

    def get(self, kind: str, ident: str) -> dict:
        r = self.db.execute("SELECT data FROM entities WHERE kind=? AND id=?", (kind, ident)).fetchone()
        if not r:
            raise IterationError(f"Unknown {kind} identifier.", "not_found")
        return json.loads(r[0])

    def put(self, kind: str, value: dict) -> None:
        self.db.execute("INSERT INTO entities VALUES(?,?,?) ON CONFLICT(id) DO UPDATE SET data=excluded.data", (kind, value["id"], json.dumps(value, ensure_ascii=False)))

    def all(self, kind: str) -> list[dict]:
        return [json.loads(r[0]) for r in self.db.execute("SELECT data FROM entities WHERE kind=? ORDER BY rowid DESC", (kind,))]

    def file_map(self, ns: str) -> dict[str, bytes]:
        return {r[0]: bytes(r[1]) for r in self.db.execute("SELECT f.path,b.data FROM files f JOIN blobs b ON b.hash=f.hash WHERE f.ns=? ORDER BY f.path", (ns,))}

    def hashes(self, ns: str) -> dict[str, str]:
        return dict(self.db.execute("SELECT path,hash FROM files WHERE ns=? ORDER BY path", (ns,)))

    def set_file(self, ns: str, path: str, data: bytes) -> None:
        digest = sha(data)
        self.db.execute("INSERT OR IGNORE INTO blobs VALUES(?,?)", (digest, data))
        self.db.execute("INSERT INTO files VALUES(?,?,?) ON CONFLICT(ns,path) DO UPDATE SET hash=excluded.hash", (ns, path, digest))

    def clone(self, source: str, dest: str) -> None:
        self.db.execute("INSERT INTO files(ns,path,hash) SELECT ?,path,hash FROM files WHERE ns=?", (dest, source))

    def event(self, project: str, data: dict) -> None:
        self.db.execute("INSERT INTO events(project,data) VALUES(?,?)", (project, json.dumps(data, ensure_ascii=False)))

    def events(self, project: str, limit: int = 60) -> list[dict]:
        rows = self.db.execute("SELECT data FROM events WHERE project=? ORDER BY seq DESC LIMIT ?", (project, limit)).fetchall()
        return [json.loads(r[0]) for r in reversed(rows)]

    def close(self):
        self.db.close()
