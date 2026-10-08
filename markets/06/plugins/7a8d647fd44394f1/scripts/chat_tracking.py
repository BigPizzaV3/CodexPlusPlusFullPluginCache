"""Persistent visible-message counters and scoped history recovery for BetterContext.

The caller provides connections to the selected edition's database. History is
read only for the registered identity. No transcripts are copied during recovery.
"""
from contextlib import closing
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3

PREFIX = re.compile(r'^\s*(?:\*\*)?MEM(\d+)\b', re.IGNORECASE)
IMPORT = re.compile(r'^\[codex_thread=([^\s]+) rollout_line=(\d+)([^\]]*)\]\s*')
UUID = re.compile(r'^[0-9a-fA-F]{8}(?:-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}$')


def schema(conn):
    # Reuse the historical table without resetting any existing value.
    conn.execute('''CREATE TABLE IF NOT EXISTS message_counters (
        session_id TEXT PRIMARY KEY, value INTEGER NOT NULL DEFAULT 0,
        updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS chat_counter_state (
        session_id TEXT PRIMARY KEY, prefix TEXT NOT NULL,
        history_count INTEGER NOT NULL DEFAULT 0, history_source TEXT NOT NULL,
        updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS chat_counter_events (
        session_id TEXT NOT NULL, event_key TEXT NOT NULL, value INTEGER NOT NULL,
        PRIMARY KEY(session_id, event_key))''')


def uri(path):
    value = path.resolve().as_uri()
    if os.name == 'nt' and path.drive.startswith('\\\\'):
        value = value.replace('file://', 'file:////', 1)
    return value + '?mode=ro'


def message_text(payload):
    return ''.join(p.get('text', p.get('output_text', '')) for p in payload.get('content', []) if isinstance(p, dict))


def visible(payload):
    return (payload.get('type') == 'message' and payload.get('role') == 'assistant'
            and payload.get('phase') not in {'analysis', 'reasoning', 'summary'})


def find_rollouts(identities, codex_home=None):
    root = Path(codex_home or os.environ.get('CODEX_HOME', str(Path.home() / '.codex')))
    ids = sorted({s for s in identities if UUID.fullmatch(s)})
    paths = {}
    if not ids:
        return paths
    for state in sorted(root.glob('state_*.sqlite'), reverse=True):
        try:
            with closing(sqlite3.connect(uri(state), uri=True, timeout=2)) as conn:
                query = 'SELECT id, rollout_path FROM threads WHERE id IN (' + ','.join('?' for _ in ids) + ')'
                for identity, path in conn.execute(query, ids):
                    if path and Path(path).is_file():
                        paths[identity] = Path(path)
        except sqlite3.Error:
            continue
        if paths:
            break
    for identity in set(ids) - set(paths):
        for folder in ('sessions', 'archived_sessions'):
            candidate = next((root / folder).glob('**/*' + identity + '.jsonl'), None)
            if candidate is not None:
                paths[identity] = candidate
                break
    return paths


def scan_rollout(path, identity):
    count = 0
    highest = 0
    seen = set()
    validated = False
    with Path(path).open(encoding='utf-8') as source:
        for line in source:
            try:
                obj = json.loads(line)
            except (ValueError, UnicodeError):
                continue  # An active rollout may end with an incomplete line.
            payload = obj.get('payload') or {}
            if obj.get('type') == 'session_meta':
                if payload.get('id') != identity:
                    raise ValueError('History identity does not match registered chat')
                validated = True
            if obj.get('type') != 'response_item' or not visible(payload):
                continue
            text = message_text(payload)
            if not text.strip():
                continue
            event_id = payload.get('id')
            if event_id and event_id in seen:
                continue
            if event_id:
                seen.add(event_id)
            count += 1
            matched = PREFIX.match(text)
            if matched:
                highest = max(highest, int(matched[1]))
    if not validated:
        raise ValueError('History has no matching session metadata')
    return {'visible_messages': count, 'highest_prefix': highest, 'source': 'local_rollout'}


def history_floor(connect, alias, identity, codex_home=None):
    keys = {alias, identity, 'CODEX-' + alias}
    imported = set()
    count = highest = 0
    with connect() as conn:
        rows = conn.execute('SELECT session_id, content FROM session_logs WHERE role = ? AND session_id IN ('
                            + ','.join('?' for _ in keys) + ')', ['assistant', *keys])
        for _, content in rows:
            match = IMPORT.match(content)
            if match:
                if 'phase=analysis' in match[3] or 'phase=summary' in match[3]:
                    continue
                key = (match[1], match[2])
                if key in imported:
                    continue
                imported.add(key)
                content = content[match.end():]
            if not content.strip():
                continue
            count += 1
            prefix = PREFIX.match(content)
            if prefix:
                highest = max(highest, int(prefix[1]))
    evidence = {'visible_messages': count, 'highest_prefix': highest,
                'source': 'saved_history_only' if count else 'no_available_history'}
    # Import metadata can identify a real local task behind a synthetic alias.
    identities = {identity, *(key[0] for key in imported)}
    local = []
    for real_id, path in find_rollouts(identities, codex_home).items():
        try:
            local.append(scan_rollout(path, real_id))
        except (OSError, ValueError):
            continue
    if local:
        # Multiple imported histories can overlap; do not add copies together.
        selected = max(local, key=lambda x: x['visible_messages'])
        evidence['visible_messages'] = max(count, selected['visible_messages'])
        evidence['highest_prefix'] = max(highest, *(s['highest_prefix'] for s in local))
        evidence['source'] = 'local_rollout_and_saved_history'
    evidence['floor'] = max(evidence['visible_messages'], evidence['highest_prefix'])
    evidence['history_complete'] = False  # No provider guarantee that exports are complete.
    return evidence


def register(connect, alias, identity, codex_home=None, visible_history_count=None):
    alias, identity = alias.strip(), identity.strip()
    if not alias or not identity or len(alias) > 200 or len(identity) > 200:
        raise ValueError('A nonempty alias and identity of at most 200 characters are required')
    with connect() as conn:
        existing = conn.execute('SELECT short_id, uuid FROM chat_aliases WHERE short_id = ? COLLATE NOCASE', (alias,)).fetchone()
        if existing and existing['uuid'] != identity:
            raise ValueError('Alias belongs to another identity; choose a different prefix')
        if existing:
            alias = existing['short_id']
    history = history_floor(connect, alias, identity, codex_home)
    if visible_history_count is not None:
        if type(visible_history_count) is not int or visible_history_count < 0:
            raise ValueError('visible_history_count must be a nonnegative integer from counted history')
        history['floor'] = max(history['floor'], visible_history_count)
        history['source'] += '+caller_counted_visible_history'
    with connect() as conn:
        conn.execute('BEGIN IMMEDIATE')
        schema(conn)
        # Recheck inside the transaction to prevent concurrent alias takeover.
        existing = conn.execute('SELECT short_id, uuid FROM chat_aliases WHERE short_id = ? COLLATE NOCASE', (alias,)).fetchone()
        if existing and existing['uuid'] != identity:
            raise ValueError('Alias belongs to another identity; choose a different prefix')
        if not existing:
            conn.execute('INSERT INTO chat_aliases (short_id, uuid) VALUES (?, ?)', (alias, identity))
        # Historic counters sometimes used the alias instead of the UUID.
        old = conn.execute('SELECT MAX(value) FROM message_counters WHERE session_id IN (?, ?, ?)', (identity, alias, 'CODEX-' + alias)).fetchone()[0] or 0
        value = max(old, history['floor'])
        conn.execute('''INSERT INTO message_counters(session_id,value) VALUES (?,?)
            ON CONFLICT(session_id) DO UPDATE SET value=MAX(value,excluded.value), updated_at=CURRENT_TIMESTAMP''', (identity,value))
        conn.execute('''INSERT INTO chat_counter_state(session_id,prefix,history_count,history_source) VALUES (?,?,?,?)
            ON CONFLICT(session_id) DO UPDATE SET history_count=excluded.history_count,
            history_source=excluded.history_source, updated_at=CURRENT_TIMESTAMP''', (identity,alias,history['visible_messages'],history['source']))
        state = conn.execute('SELECT prefix FROM chat_counter_state WHERE session_id=?', (identity,)).fetchone()
    return {'alias': alias, 'identity': identity, 'prefix': state['prefix'], 'count': value,
            'next_prefix': f"MEM{value + 1:03d} - {state['prefix']}", 'history': history, 'created': not bool(existing)}


def status(connect, chat):
    with connect() as conn:
        alias = conn.execute('SELECT short_id, uuid FROM chat_aliases WHERE short_id=? COLLATE NOCASE OR uuid=? ORDER BY created_at LIMIT 1', (chat,chat)).fetchone()
        if not alias:
            raise ValueError('Chat is not registered; use chat_register first')
        tables = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        counter = conn.execute('SELECT value FROM message_counters WHERE session_id=?', (alias['uuid'],)).fetchone() if 'message_counters' in tables else None
        state = conn.execute('SELECT prefix,history_count,history_source FROM chat_counter_state WHERE session_id=?', (alias['uuid'],)).fetchone() if 'chat_counter_state' in tables else None
        value = counter['value'] if counter else None
        prefix = state['prefix'] if state else alias['short_id']
        return {'identity':alias['uuid'], 'alias':alias['short_id'], 'prefix':prefix, 'count':value,
                'next_prefix': f'MEM{value + 1:03d} - {prefix}' if value is not None else None,
                'backfill_needed': state is None,
                'history_source':state['history_source'] if state else 'not_reconciled'}


def next_message(connect, chat, event_key):
    if not event_key.strip() or len(event_key) > 300:
        raise ValueError('Use a stable nonempty event key of at most 300 characters')
    before = status(connect, chat)
    if before['backfill_needed']:
        register(connect, before['alias'], before['identity'])
    with connect() as conn:
        conn.execute('BEGIN IMMEDIATE')
        schema(conn)
        identity = before['identity']
        previous = conn.execute('SELECT value FROM chat_counter_events WHERE session_id=? AND event_key=?', (identity,event_key)).fetchone()
        if previous:
            value = previous['value']
        else:
            value = conn.execute('SELECT value FROM message_counters WHERE session_id=?', (identity,)).fetchone()['value'] + 1
            conn.execute('UPDATE message_counters SET value=?,updated_at=CURRENT_TIMESTAMP WHERE session_id=?', (value,identity))
            conn.execute('INSERT INTO chat_counter_events(session_id,event_key,value) VALUES (?,?,?)', (identity,event_key,value))
    return {'count':value, 'message_prefix':f"MEM{value:03d} - {before['prefix']}", 'reused':bool(previous)}
