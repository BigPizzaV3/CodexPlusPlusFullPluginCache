import sqlite3
import os
import json
from typing import List, Dict, Optional, Sequence, Tuple

DB_PATH = os.path.join(os.path.dirname(__file__), 'memory.db')
SCHEMA_VERSION = 1


def get_db_path() -> str:
    from storage_registry import resolve_database
    from pathlib import Path
    return str(resolve_database(Path(os.environ.get('BETTERCONTEXT_DB_PATH', DB_PATH))))


def get_connection():
    from storage_registry import sqlite_uri
    conn = sqlite3.connect(sqlite_uri(get_db_path(), "rwc"), uri=True, timeout=30)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA busy_timeout = 30000')
    conn.execute('PRAGMA foreign_keys = ON')
    return conn


def init_db():
    with get_connection() as conn:
        journal_mode = conn.execute('PRAGMA journal_mode').fetchone()[0].lower()
        if journal_mode == 'wal':
            conn.execute('PRAGMA wal_checkpoint(TRUNCATE)')
            journal_mode = conn.execute('PRAGMA journal_mode = DELETE').fetchone()[0].lower()
        if journal_mode != 'delete':
            raise sqlite3.OperationalError(
                f"BetterContext requires DELETE journal mode for a shared database; got {journal_mode!r}"
            )

        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS core_facts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                fact TEXT NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS session_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chat_aliases (
                short_id TEXT PRIMARY KEY,
                uuid TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS relay_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sender_chat TEXT NOT NULL,
                sender_uuid TEXT NOT NULL,
                recipient_chat TEXT NOT NULL,
                recipient_uuid TEXT NOT NULL,
                body TEXT NOT NULL,
                reply_to_id INTEGER,
                dedupe_key TEXT,
                metadata_json TEXT,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                delivered_at TIMESTAMP,
                read_at TIMESTAMP,
                FOREIGN KEY (reply_to_id) REFERENCES relay_messages(id),
                CHECK (length(trim(sender_chat)) > 0),
                CHECK (length(trim(recipient_chat)) > 0),
                CHECK (length(trim(body)) > 0)
            )
        ''')
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS relay_messages_recipient_state
            ON relay_messages (recipient_chat, read_at, delivered_at, id)
        ''')
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS relay_messages_sender
            ON relay_messages (sender_chat, id)
        ''')
        cursor.execute('''
            CREATE UNIQUE INDEX IF NOT EXISTS relay_messages_sender_dedupe
            ON relay_messages (sender_chat, dedupe_key)
            WHERE dedupe_key IS NOT NULL
        ''')
        cursor.execute(f'PRAGMA user_version = {SCHEMA_VERSION}')
        conn.commit()


# --- Core Facts Functions ---

def add_fact(category: str, fact: str) -> bool:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO core_facts (category, fact) VALUES (?, ?)', (category, fact))
            conn.commit()
            return True
    except sqlite3.IntegrityError:
        return False


def get_facts(category: Optional[str] = None) -> List[Dict]:
    with get_connection() as conn:
        cursor = conn.cursor()
        if category:
            cursor.execute('SELECT * FROM core_facts WHERE category = ? ORDER BY created_at ASC', (category,))
        else:
            cursor.execute('SELECT * FROM core_facts ORDER BY category, created_at ASC')
        return [dict(row) for row in cursor.fetchall()]


def delete_fact(fact_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM core_facts WHERE id = ?', (fact_id,))
        conn.commit()


# --- Task Functions ---

def add_task(description: str) -> int:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (description) VALUES (?)', (description,))
        conn.commit()
        return cursor.lastrowid


def update_task_status(task_id: int, status: str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE tasks
            SET status = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        ''', (status, task_id))
        conn.commit()


def get_tasks(status: Optional[str] = None) -> List[Dict]:
    with get_connection() as conn:
        cursor = conn.cursor()
        if status:
            cursor.execute('SELECT * FROM tasks WHERE status = ? ORDER BY created_at ASC', (status,))
        else:
            cursor.execute('SELECT * FROM tasks ORDER BY status DESC, created_at ASC')
        return [dict(row) for row in cursor.fetchall()]


# --- Session Log Functions ---

def add_log(session_id: str, role: str, content: str, timestamp: Optional[str] = None):
    with get_connection() as conn:
        cursor = conn.cursor()
        if timestamp:
            cursor.execute('''
                INSERT INTO session_logs (session_id, role, content, timestamp)
                VALUES (?, ?, ?, ?)
            ''', (session_id, role, content, timestamp))
        else:
            cursor.execute('''
                INSERT INTO session_logs (session_id, role, content)
                VALUES (?, ?, ?)
            ''', (session_id, role, content))
        conn.commit()


def replace_logs(session_id: str, logs: Sequence[Tuple[str, str, str, str]]):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM session_logs WHERE session_id = ?', (session_id,))
        cursor.executemany('''
            INSERT INTO session_logs (session_id, role, content, timestamp)
            VALUES (?, ?, ?, ?)
        ''', logs)
        conn.commit()


def count_logs(session_id: Optional[str] = None) -> int:
    with get_connection() as conn:
        cursor = conn.cursor()
        if session_id:
            cursor.execute('SELECT COUNT(*) FROM session_logs WHERE session_id = ?', (session_id,))
        else:
            cursor.execute('SELECT COUNT(*) FROM session_logs')
        return int(cursor.fetchone()[0])


def get_logs(session_id: str, limit: int = 50) -> List[Dict]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM session_logs
            WHERE session_id = ?
            ORDER BY timestamp DESC, id DESC
            LIMIT ?
        ''', (session_id, limit))
        rows = cursor.fetchall()
        return [dict(row) for row in reversed(rows)]


# --- Chat Alias Functions ---

def link_chat(short_id: str, uuid: str) -> bool:
    short_id = short_id.strip()
    uuid = uuid.strip()
    if not short_id or not uuid:
        return False
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT short_id FROM chat_aliases WHERE short_id = ? COLLATE NOCASE',
                (short_id,),
            )
            existing = cursor.fetchone()
            canonical_short_id = existing['short_id'] if existing else short_id
            cursor.execute(
                'INSERT OR REPLACE INTO chat_aliases (short_id, uuid) VALUES (?, ?)',
                (canonical_short_id, uuid),
            )
            conn.commit()
            return True
    except Exception:
        return False


def resolve_chat(short_id: str) -> Optional[str]:
    identity = resolve_chat_identity(short_id)
    return identity['uuid'] if identity else None


def _resolve_chat_with_connection(conn: sqlite3.Connection, identifier: str) -> Optional[Dict]:
    identifier = identifier.strip()
    if not identifier:
        return None
    cursor = conn.cursor()
    cursor.execute('''
        SELECT short_id, uuid, created_at
        FROM chat_aliases
        WHERE short_id = ? COLLATE NOCASE
        ORDER BY created_at ASC
        LIMIT 1
    ''', (identifier,))
    row = cursor.fetchone()
    if row:
        return dict(row)
    cursor.execute('''
        SELECT short_id, uuid, created_at
        FROM chat_aliases
        WHERE uuid = ?
        ORDER BY created_at ASC
        LIMIT 1
    ''', (identifier,))
    row = cursor.fetchone()
    return dict(row) if row else None


def resolve_chat_identity(identifier: str) -> Optional[Dict]:
    with get_connection() as conn:
        return _resolve_chat_with_connection(conn, identifier)


def get_all_aliases() -> List[Dict]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM chat_aliases ORDER BY created_at ASC')
        return [dict(row) for row in cursor.fetchall()]


# --- Cross-Chat Relay Functions ---

def _relay_message_dict(row: sqlite3.Row) -> Dict:
    message = dict(row)
    metadata_json = message.pop('metadata_json', None)
    message['metadata'] = json.loads(metadata_json) if metadata_json else None
    if message.get('read_at'):
        message['state'] = 'read'
    elif message.get('delivered_at'):
        message['state'] = 'delivered'
    else:
        message['state'] = 'pending'
    return message


def _validate_limit(limit: int) -> int:
    if limit < 1 or limit > 500:
        raise ValueError('limit must be between 1 and 500')
    return limit


def send_relay_message(
    sender: str,
    recipient: str,
    body: str,
    reply_to_id: Optional[int] = None,
    dedupe_key: Optional[str] = None,
    metadata: Optional[Dict] = None,
) -> Dict:
    body = body.strip()
    if not body:
        raise ValueError('relay message body cannot be empty')
    if dedupe_key is not None:
        dedupe_key = dedupe_key.strip()
        if not dedupe_key:
            raise ValueError('dedupe key cannot be empty')
    metadata_json = None
    if metadata is not None:
        if not isinstance(metadata, dict):
            raise ValueError('relay metadata must be a JSON object')
        metadata_json = json.dumps(metadata, sort_keys=True, separators=(',', ':'))

    with get_connection() as conn:
        sender_identity = _resolve_chat_with_connection(conn, sender)
        recipient_identity = _resolve_chat_with_connection(conn, recipient)
        if not sender_identity:
            raise ValueError(f"unknown sender chat: {sender}")
        if not recipient_identity:
            raise ValueError(f"unknown recipient chat: {recipient}")
        if reply_to_id is not None:
            reply = conn.execute(
                'SELECT id FROM relay_messages WHERE id = ?',
                (reply_to_id,),
            ).fetchone()
            if not reply:
                raise ValueError(f"relay message {reply_to_id} does not exist")

        if dedupe_key is not None:
            existing = conn.execute('''
                SELECT * FROM relay_messages
                WHERE sender_chat = ? AND dedupe_key = ?
            ''', (sender_identity['short_id'], dedupe_key)).fetchone()
            if existing:
                result = _relay_message_dict(existing)
                result['created'] = False
                return result

        try:
            cursor = conn.execute('''
                INSERT INTO relay_messages (
                    sender_chat, sender_uuid, recipient_chat, recipient_uuid,
                    body, reply_to_id, dedupe_key, metadata_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                sender_identity['short_id'],
                sender_identity['uuid'],
                recipient_identity['short_id'],
                recipient_identity['uuid'],
                body,
                reply_to_id,
                dedupe_key,
                metadata_json,
            ))
            message_id = cursor.lastrowid
            conn.commit()
        except sqlite3.IntegrityError:
            if dedupe_key is None:
                raise
            existing = conn.execute('''
                SELECT * FROM relay_messages
                WHERE sender_chat = ? AND dedupe_key = ?
            ''', (sender_identity['short_id'], dedupe_key)).fetchone()
            if not existing:
                raise
            result = _relay_message_dict(existing)
            result['created'] = False
            return result

        row = conn.execute('SELECT * FROM relay_messages WHERE id = ?', (message_id,)).fetchone()
        result = _relay_message_dict(row)
        result['created'] = True
        return result


def get_relay_inbox(
    recipient: str,
    limit: int = 50,
    include_read: bool = False,
    claim: bool = False,
) -> List[Dict]:
    limit = _validate_limit(limit)
    with get_connection() as conn:
        identity = _resolve_chat_with_connection(conn, recipient)
        if not identity:
            raise ValueError(f"unknown recipient chat: {recipient}")
        if claim:
            conn.execute('BEGIN IMMEDIATE')
        read_filter = '' if include_read else 'AND read_at IS NULL'
        rows = conn.execute(f'''
            SELECT * FROM relay_messages
            WHERE recipient_chat = ? {read_filter}
            ORDER BY id ASC
            LIMIT ?
        ''', (identity['short_id'], limit)).fetchall()
        if claim:
            selected_ids = [row['id'] for row in rows]
            pending_ids = [row['id'] for row in rows if row['delivered_at'] is None]
            if pending_ids:
                placeholders = ','.join('?' for _ in pending_ids)
                conn.execute(f'''
                    UPDATE relay_messages
                    SET delivered_at = CURRENT_TIMESTAMP
                    WHERE id IN ({placeholders}) AND delivered_at IS NULL
                ''', pending_ids)
            if selected_ids:
                placeholders = ','.join('?' for _ in selected_ids)
                rows = conn.execute(f'''
                    SELECT * FROM relay_messages
                    WHERE id IN ({placeholders})
                    ORDER BY id ASC
                ''', selected_ids).fetchall()
            conn.commit()
        return [_relay_message_dict(row) for row in rows]


def get_relay_outbox(sender: str, limit: int = 50) -> List[Dict]:
    limit = _validate_limit(limit)
    with get_connection() as conn:
        identity = _resolve_chat_with_connection(conn, sender)
        if not identity:
            raise ValueError(f"unknown sender chat: {sender}")
        rows = conn.execute('''
            SELECT * FROM relay_messages
            WHERE sender_chat = ?
            ORDER BY id DESC
            LIMIT ?
        ''', (identity['short_id'], limit)).fetchall()
        return [_relay_message_dict(row) for row in reversed(rows)]


def acknowledge_relay_messages(recipient: str, message_ids: Sequence[int]) -> List[Dict]:
    ids = list(dict.fromkeys(int(message_id) for message_id in message_ids))
    if not ids:
        raise ValueError('at least one relay message id is required')
    with get_connection() as conn:
        identity = _resolve_chat_with_connection(conn, recipient)
        if not identity:
            raise ValueError(f"unknown recipient chat: {recipient}")
        placeholders = ','.join('?' for _ in ids)
        rows = conn.execute(f'''
            SELECT * FROM relay_messages
            WHERE id IN ({placeholders}) AND recipient_chat = ?
        ''', (*ids, identity['short_id'])).fetchall()
        found_ids = {row['id'] for row in rows}
        missing = [message_id for message_id in ids if message_id not in found_ids]
        if missing:
            raise ValueError(
                f"relay message(s) not found in {identity['short_id']} inbox: "
                + ', '.join(str(message_id) for message_id in missing)
            )
        conn.execute(f'''
            UPDATE relay_messages
            SET delivered_at = COALESCE(delivered_at, CURRENT_TIMESTAMP),
                read_at = COALESCE(read_at, CURRENT_TIMESTAMP)
            WHERE id IN ({placeholders}) AND recipient_chat = ?
        ''', (*ids, identity['short_id']))
        conn.commit()
        rows = conn.execute(f'''
            SELECT * FROM relay_messages
            WHERE id IN ({placeholders})
            ORDER BY id ASC
        ''', ids).fetchall()
        return [_relay_message_dict(row) for row in rows]


def get_relay_message(message_id: int) -> Optional[Dict]:
    with get_connection() as conn:
        row = conn.execute(
            'SELECT * FROM relay_messages WHERE id = ?',
            (message_id,),
        ).fetchone()
        return _relay_message_dict(row) if row else None
