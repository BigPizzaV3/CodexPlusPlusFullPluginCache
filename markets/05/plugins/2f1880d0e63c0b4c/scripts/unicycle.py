#!/usr/bin/env python3
"""Private delivery cache. Native tools and genuine user consent remain host-owned."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import secrets
import sqlite3
import sys

MAX = 65536
PERSONAS = {'unicycle', 'jarvis', 'evie'}
STATES = {'delivered', 'queued', 'uncertain', 'failed'}


def _json(value):
    return json.dumps(value, separators=(',', ':'), ensure_ascii=False, sort_keys=True)


def _text(value, limit=1200):
    if not isinstance(value, str) or not value.strip() or len(value) > limit:
        raise ValueError('invalid bounded text')
    return value


def _identity(value):
    if not isinstance(value, dict):
        raise ValueError('qualified identity required')
    return (_text(value.get('threadId', value.get('id')), 200),
            _text(value.get('hostId'), 200))


def _owner(thread, host):
    return {'threadId': thread, 'hostId': host}


def _known(c, identity):
    if not c.execute('SELECT 1 FROM owners WHERE thread=? AND host=?', identity).fetchone():
        raise ValueError('unknown owner or host')


def _db(state):
    path = Path(state).expanduser().absolute()
    if any(p.is_symlink() for p in (path, *path.parents)):
        raise ValueError('symlink state path rejected')
    path.mkdir(mode=0o700, parents=True, exist_ok=True)
    os.chmod(path, 0o700)
    database = path / 'state.db'
    if database.is_symlink():
        raise ValueError('database symlink rejected')
    fd = os.open(database, os.O_CREAT | os.O_RDWR | getattr(os, 'O_NOFOLLOW', 0), 0o600)
    os.fchmod(fd, 0o600)
    os.close(fd)
    c = sqlite3.connect(database, timeout=5, isolation_level=None)
    c.row_factory = sqlite3.Row
    c.execute('PRAGMA secure_delete=ON')
    version = c.execute('PRAGMA user_version').fetchone()[0]
    if version not in (0, 1, 2, 3):
        c.close()
        raise ValueError('unsupported state schema')
    c.executescript('''
        CREATE TABLE IF NOT EXISTS config(id INTEGER PRIMARY KEY CHECK(id=1), coordinator TEXT, persona TEXT);
        CREATE TABLE IF NOT EXISTS owners(thread TEXT, host TEXT, title TEXT, cursor TEXT,
            message_hash TEXT, turn_hash TEXT, read_sequence INTEGER DEFAULT 0, PRIMARY KEY(thread,host));
        CREATE TABLE IF NOT EXISTS events(id TEXT PRIMARY KEY, thread TEXT, host TEXT, source TEXT,
            kind TEXT, summary TEXT, scope TEXT, options TEXT, artifact TEXT,
            state TEXT DEFAULT 'new', claim TEXT, evidence TEXT,
            UNIQUE(thread,host,source,kind));
        CREATE TABLE IF NOT EXISTS answers(event TEXT PRIMARY KEY, text TEXT, source TEXT, packet TEXT,
            state TEXT DEFAULT 'prepared', evidence TEXT);
        CREATE TABLE IF NOT EXISTS errors(thread TEXT, host TEXT, PRIMARY KEY(thread,host));
        CREATE TABLE IF NOT EXISTS signals(id TEXT PRIMARY KEY, body TEXT NOT NULL);
    ''')
    c.execute('BEGIN IMMEDIATE')
    if 'read_sequence' not in {row[1] for row in c.execute('PRAGMA table_info(owners)')}:
        c.execute('ALTER TABLE owners ADD COLUMN read_sequence INTEGER DEFAULT 0')
    c.execute('PRAGMA user_version=3')
    c.commit()
    return c


def _pending(c):
    return c.execute("""SELECT e.* FROM events e LEFT JOIN answers a ON a.event=e.id
        WHERE e.kind='decision' AND a.event IS NULL AND e.state NOT IN ('new','superseded') ORDER BY e.rowid LIMIT 1""").fetchone()


def _event(c, event_id):
    row = c.execute('SELECT * FROM events WHERE id=?', (_text(event_id, 64),)).fetchone()
    if not row:
        raise ValueError('event not found')
    result = {'eventId': row['id'], 'owner': _owner(row['thread'], row['host']),
              'sourceId': row['source'], 'kind': row['kind'], 'summary': row['summary'],
              'scope': row['scope'], 'options': json.loads(row['options']),
              'artifact': row['artifact'], 'state': row['state'], 'claim': row['claim'],
              'evidence': row['evidence']}
    answer = c.execute('SELECT state,evidence FROM answers WHERE event=?', (event_id,)).fetchone()
    result['dispatchState'] = dict(answer) if answer else None
    return result


def configure(c, p):
    coordinator = _identity(p.get('coordinator'))
    owners = p.get('owners')
    if not isinstance(owners, list) or not 1 <= len(owners) <= 32:
        raise ValueError('choose 1 to 32 existing owners')
    persona = p.get('persona', 'unicycle')
    if persona not in PERSONAS:
        raise ValueError('invalid persona')
    rows = []
    for owner in owners:
        identity = _identity(owner)
        if identity == coordinator:
            raise ValueError('coordinator cannot own its own monitoring loop')
        rows.append((*identity, _text(owner.get('title'), 240)))
    keep = {(r[0], r[1]) for r in rows}
    if len(keep) != len(rows):
        raise ValueError('duplicate owner')
    unresolved = c.execute("""SELECT e.thread,e.host FROM events e LEFT JOIN answers a ON a.event=e.id
        WHERE e.kind='decision' AND e.state!='superseded' AND (a.event IS NULL OR a.state!='delivered')""").fetchall()
    old = c.execute('SELECT coordinator FROM config WHERE id=1').fetchone()
    if unresolved and old and json.loads(old[0]) != list(coordinator):
        raise ValueError('unresolved decision blocks coordinator change')
    if any((r[0], r[1]) not in keep for r in unresolved):
        raise ValueError('unresolved decision blocks owner removal')
    c.execute('INSERT OR REPLACE INTO config VALUES(1,?,?)', (_json(coordinator), persona))
    for row in rows:
        c.execute('''INSERT INTO owners(thread,host,title) VALUES(?,?,?)
            ON CONFLICT(thread,host) DO UPDATE SET title=excluded.title''', row)
    for row in c.execute('SELECT thread,host FROM owners').fetchall():
        if tuple(row) not in keep:
            c.execute('DELETE FROM owners WHERE thread=? AND host=?', tuple(row))
            c.execute('DELETE FROM errors WHERE thread=? AND host=?', tuple(row))
    return status(c, {})


def status(c, p):
    offset = p.get('offset', 0)
    if type(offset) is not int or not 0 <= offset <= 32:
        raise ValueError('invalid offset')
    config = c.execute('SELECT coordinator,persona FROM config').fetchone()
    targets = []
    for row in c.execute('SELECT * FROM owners ORDER BY read_sequence,rowid LIMIT 8 OFFSET ?', (offset,)):
        targets.append({**_owner(row['thread'], row['host']), 'title': row['title'],
                        'afterCursor': row['cursor']})
    counts = dict(c.execute('SELECT state,count(*) FROM events GROUP BY state').fetchall())
    dispatch_counts = dict(c.execute('SELECT state,count(*) FROM answers GROUP BY state').fetchall())
    pending = _pending(c)
    total = c.execute('SELECT count(*) FROM owners').fetchone()[0]
    return {'config': None if not config else {
                'coordinator': _owner(*json.loads(config[0])), 'persona': config[1]},
            'targets': targets, 'nextOffset': offset + 8 if offset + 8 < total else None,
            'counts': counts, 'dispatchCounts': dispatch_counts,
            'pendingSignals': c.execute('SELECT count(*) FROM signals').fetchone()[0],
            'pendingDecision': _event(c, pending['id']) if pending else None,
            'inFlight': [dict(r) for r in c.execute("SELECT id,state,claim FROM events WHERE state IN ('presenting','queued','uncertain','failed') LIMIT 8")],
            'errors': [_owner(*r) for r in c.execute('SELECT thread,host FROM errors LIMIT 32')]}


def ingest(c, p):
    polls, errors = p.get('polls', []), p.get('errors', [])
    if not isinstance(polls, list) or len(polls) > 8 or not isinstance(errors, list) or len(errors) > 8:
        raise ValueError('maximum 8 polls and 8 errors')
    signals, changed_errors = [], []
    for poll in polls:
        if not isinstance(poll, dict):
            raise ValueError('invalid poll')
        identity = _identity(poll.get('thread'))
        _known(c, identity)
        old = c.execute('SELECT * FROM owners WHERE thread=? AND host=?', identity).fetchone()
        cursor = poll.get('cursor')
        if cursor is not None:
            cursor = _text(cursor, 4000)
        message = poll.get('latestAssistantMessage') or {}
        turn = poll.get('latestTurn') or {}
        if not isinstance(message, dict) or not isinstance(turn, dict):
            raise ValueError('invalid native state')
        signal = {'owner': _owner(*identity)}
        message_hash, turn_hash = old['message_hash'], old['turn_hash']
        if message.get('id') and 'text' in message:
            mid = _text(message['id'], 300)
            text = message['text']
            if not isinstance(text, str):
                raise ValueError('invalid native message')
            fingerprint = hashlib.sha256(_json([turn.get('id'), text]).encode()).hexdigest()
            if fingerprint != message_hash:
                signal.update(messageId=mid, phase=_text(message.get('phase', 'unknown'), 100), text=text[:1200], truncated=len(text)>1200)
            message_hash = fingerprint
        if turn.get('id') and turn.get('status'):
            turn_id, turn_status = _text(turn['id'], 300), _text(turn['status'], 100)
            fingerprint = _json([turn_id, turn_status])
            if fingerprint != turn_hash:
                signal.update(turnId=turn_id, status='turn_completed' if turn_status=='completed' else turn_status)
            turn_hash = fingerprint
        if len(signal)>1:
            signal_id=hashlib.sha256(_json(signal).encode()).hexdigest()
            signal['signalId']=signal_id
            if c.execute('SELECT count(*) FROM signals').fetchone()[0]>=128:
                raise ValueError('unclassified signal capacity reached; classify before polling')
            c.execute('INSERT OR IGNORE INTO signals VALUES(?,?)',(signal_id,_json(signal)))
            signals.append(signal)
        c.execute('UPDATE owners SET cursor=?,message_hash=?,turn_hash=? WHERE thread=? AND host=?',
                  (cursor or old['cursor'], message_hash, turn_hash, *identity))
        c.execute('UPDATE owners SET read_sequence=(SELECT COALESCE(MAX(read_sequence),0)+1 FROM owners) WHERE thread=? AND host=?', identity)
        c.execute('DELETE FROM errors WHERE thread=? AND host=?', identity)
    for error in errors:
        if not isinstance(error, dict):
            raise ValueError('invalid error identity')
        identity = _identity(error.get('owner', error))
        _known(c, identity)
        if not c.execute('SELECT 1 FROM errors WHERE thread=? AND host=?', identity).fetchone():
            changed_errors.append({'owner': _owner(*identity), 'status':'error'})
        c.execute('INSERT OR IGNORE INTO errors VALUES(?,?)', identity)
        c.execute('UPDATE owners SET read_sequence=(SELECT COALESCE(MAX(read_sequence),0)+1 FROM owners) WHERE thread=? AND host=?', identity)
    return {'signals': signals, 'errors': changed_errors}


def add_event(c, p):
    identity = _identity(p.get('owner'))
    _known(c, identity)
    source = _text(p.get('sourceId'), 300)
    kind = p.get('kind')
    if kind not in {'decision', 'preview', 'completion', 'blocker'}:
        raise ValueError('invalid event kind')
    summary, scope = _text(p.get('summary')), _text(p.get('scope'))
    options = p.get('options', [])
    if not isinstance(options, list) or len(options)>3 or (kind=='decision' and len(options) not in (2,3)):
        raise ValueError('decision needs 2 or 3 options')
    for option in options:
        _text(option, 240)
    if len(set(options)) != len(options):
        raise ValueError('duplicate options')
    artifact = p.get('artifact')
    if artifact is not None:
        _text(artifact, 2000)
        if not Path(artifact).is_absolute():
            raise ValueError('artifact must be absolute')
    body = [*identity, source, kind, summary, scope, options, artifact]
    event_id = hashlib.sha256(_json(body).encode()).hexdigest()
    old = c.execute('SELECT id FROM events WHERE thread=? AND host=? AND source=? AND kind=?', (*identity,source,kind)).fetchone()
    if old:
        if old[0] != event_id:
            raise ValueError('source conflict; use a new source revision')
        return {'eventId':event_id, 'duplicate':True}
    if c.execute('SELECT count(*) FROM events').fetchone()[0] >= 128:
        raise ValueError('event capacity reached; preserve and reconcile state')
    c.execute('INSERT INTO events(id,thread,host,source,kind,summary,scope,options,artifact) VALUES(?,?,?,?,?,?,?,?,?)',
              (event_id,*identity,source,kind,summary,scope,_json(options),artifact))
    return {'eventId':event_id, 'duplicate':False}


def next_event(c, p):
    pending = _pending(c)
    row = c.execute("SELECT e.id FROM events e JOIN owners o ON o.thread=e.thread AND o.host=e.host WHERE e.state='new' AND (?=0 OR e.kind!='decision') ORDER BY e.rowid LIMIT 1", (int(pending is not None),)).fetchone()
    if not row:
        return {'event':None}
    c.execute("UPDATE events SET state='presenting',claim=? WHERE id=?", (secrets.token_urlsafe(18),row[0]))
    return {'event':_event(c,row[0])}


def receipt(c, p):
    event = _event(c,p.get('eventId'))
    if event['state']=='superseded':
        raise ValueError('superseded decision cannot be delivered')
    if not event['claim'] or event['claim'] != p.get('claim'):
        raise ValueError('claim mismatch')
    state = p.get('state')
    if state not in STATES:
        raise ValueError('invalid receipt state')
    if event['state']=='delivered' and state!='delivered':
        raise ValueError('delivered receipt cannot be downgraded')
    evidence = _text(p.get('evidence'))
    c.execute('UPDATE events SET state=?,evidence=? WHERE id=?', (state,evidence,event['eventId']))
    return {'eventId':event['eventId'],'state':state}


def answer(c,p):
    event = _event(c,p.get('eventId'))
    if event['kind']!='decision' or event['state']!='delivered':
        raise ValueError('decision not delivered')
    config = c.execute('SELECT coordinator FROM config').fetchone()
    if not config or _identity(p.get('coordinator')) != tuple(json.loads(config[0])) or p.get('scope') != event['scope']:
        raise ValueError('answer association mismatch')
    _known(c,_identity(event['owner']))
    text, source = _text(p.get('text')), _text(p.get('sourceMessageId'),300)
    old = c.execute('SELECT text,source FROM answers WHERE event=?',(event['eventId'],)).fetchone()
    if old:
        if tuple(old) != (text,source):
            raise ValueError('answer conflict')
        return {'dispatch':None,'duplicate':True}
    packet = {'owner':event['owner'],'eventId':event['eventId'],'text':text,
              'scope':event['scope'],'sourceMessageId':source}
    c.execute('INSERT INTO answers(event,text,source,packet) VALUES(?,?,?,?)',
              (event['eventId'],text,source,_json(packet)))
    return {'dispatch':packet,'duplicate':False}


def dispatch_receipt(c,p):
    event_id = _text(p.get('eventId'),64)
    row = c.execute('SELECT state FROM answers WHERE event=?',(event_id,)).fetchone()
    if not row:
        raise ValueError('answer not found')
    state = p.get('state')
    if state not in STATES:
        raise ValueError('invalid dispatch state')
    if row[0]=='delivered' and state!='delivered':
        raise ValueError('delivered dispatch cannot be downgraded')
    evidence = _text(p.get('evidence'))
    c.execute('UPDATE answers SET state=?,evidence=? WHERE event=?',(state,evidence,event_id))
    return {'eventId':event_id,'state':state}


def pending_signals(c,p):
    return {'signals':[json.loads(row[0]) for row in c.execute('SELECT body FROM signals ORDER BY rowid LIMIT 8')]}


def acknowledge_signals(c,p):
    ids=p.get('signalIds')
    if not isinstance(ids,list) or not 1<=len(ids)<=8:
        raise ValueError('acknowledge 1 to 8 classified signals')
    for signal_id in ids:
        c.execute('DELETE FROM signals WHERE id=?',(_text(signal_id,64),))
    return {'acknowledged':len(ids)}


def supersede(c,p):
    old = _event(c,p.get('eventId'))
    replacement = _event(c,p.get('replacementEventId'))
    if old['eventId']==replacement['eventId'] or old['owner']!=replacement['owner']:
        raise ValueError('replacement must be distinct and keep the owner')
    if old['dispatchState'] or replacement['state']!='new':
        raise ValueError('cannot replace an answered decision or use an active replacement')
    evidence = _text(p.get('evidence'))
    c.execute("UPDATE events SET state='superseded',evidence=? WHERE id=?",
              (_json({'replacementEventId':replacement['eventId'],'evidence':evidence}),old['eventId']))
    return {'eventId':old['eventId'],'state':'superseded','replacementEventId':replacement['eventId']}


def handle(state,operation,payload):
    if not isinstance(payload,dict) or len(_json(payload).encode())>MAX:
        raise ValueError('invalid bounded input')
    operations = {'configure':configure,'status':status,'ingest':ingest,'add-event':add_event,
                  'next':next_event,'receipt':receipt,'answer':answer,'dispatch-receipt':dispatch_receipt,
                  'get-event':lambda c,p:_event(c,p.get('eventId')), 'supersede':supersede, 'signals':pending_signals, 'ack-signals':acknowledge_signals}
    if operation not in operations:
        raise ValueError('unknown operation')
    c = _db(state)
    try:
        c.execute('BEGIN IMMEDIATE')
        result = operations[operation](c,payload)
        c.commit()
        return result
    except Exception:
        c.rollback()
        raise
    finally:
        c.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--state-dir',default=os.environ.get('UNICYCLE_STATE_DIR',str(Path.home()/'.local/state/unicycle')))
    parser.add_argument('operation')
    args = parser.parse_args()
    try:
        raw = sys.stdin.buffer.read(MAX+1)
        if len(raw)>MAX:
            raise ValueError('oversize input')
        print(_json(handle(args.state_dir,args.operation,json.loads(raw or b'{}'))))
        return 0
    except Exception:
        print(_json({'error':'invalid request or unavailable private state; no automatic retry'}))
        return 1


if __name__=='__main__':
    raise SystemExit(main())
