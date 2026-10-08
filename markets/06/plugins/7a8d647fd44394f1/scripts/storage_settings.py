"""Storage enrollment and recoverable migrations through a permanent shared registry."""
from contextlib import closing, contextmanager, nullcontext
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import sqlite3
import subprocess
import sys
import time
import uuid
from storage_registry import instance_id, locate, read_registry, resolve_database, resolve_settings, sqlite_uri

REQUIRED = {'core_facts', 'tasks', 'session_logs', 'chat_aliases', 'relay_messages'}
GUARD = 'bc_storage_frozen_'


def configuration_path(edition):
    override = os.environ.get('BETTERCONTEXT_'+edition.upper()+'_CONFIG')
    if override:
        return Path(override).expanduser()
    base = Path(os.environ.get('LOCALAPPDATA', str(Path.home()/'AppData/Local'))) if os.name == 'nt' else Path(os.environ.get('XDG_CONFIG_HOME', str(Path.home()/'.config')))
    return base/('BetterContext'+edition.title())/'plugin-config.json'


def database_uri(path, mode='ro'):
    return sqlite_uri(path, mode)


def inspect_database(path, connection=None):
    if not path.is_file():
        raise ValueError('Database does not exist; no replacement was created')
    with (nullcontext(connection) if connection is not None else closing(sqlite3.connect(database_uri(path), uri=True, timeout=30))) as db:
        db.execute('PRAGMA cache_size = -32768')
        if not db.in_transaction: db.execute('BEGIN')
        tables = [r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
        if not REQUIRED <= set(tables):
            raise ValueError('This is not a complete BetterContext database')
        if db.execute('PRAGMA quick_check').fetchall() != [('ok',)]:
            raise ValueError('Database integrity check failed')
        if db.execute('PRAGMA foreign_key_check').fetchone():
            raise ValueError('Database foreign key check failed')
        if db.execute('PRAGMA journal_mode').fetchone()[0].lower() != 'delete':
            raise ValueError('Shared storage requires DELETE journal mode; this database was not changed')
        digest = hashlib.sha256()
        counts = {}
        for name in tables:
            rows = []
            for row in db.execute('SELECT * FROM "'+name.replace('"','""')+'"'):
                encoded = json.dumps(row, ensure_ascii=True, separators=(',', ':'), default=lambda b:{'blob':b.hex()}).encode()
                rows.append(hashlib.sha256(encoded).digest())
            counts[name] = len(rows)
            digest.update(name.encode())
            for value in sorted(rows): digest.update(value)
        schema = db.execute("SELECT type,name,tbl_name,sql FROM sqlite_master ORDER BY type,name").fetchall()
        schema = [r for r in schema if not r[1].startswith(GUARD)]
        digest.update(json.dumps(schema, ensure_ascii=True).encode())
        return {'tables':counts, 'schema_version':db.execute('PRAGMA user_version').fetchone()[0], 'content_sha256':digest.hexdigest()}


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+'.'+uuid.uuid4().hex+'.tmp')
    try:
        with temporary.open('x', encoding='utf-8') as handle:
            json.dump(value, handle, indent=2)
            handle.write('\n'); handle.flush(); os.fsync(handle.fileno())
        temporary.replace(path)
    finally:
        if temporary.exists(): temporary.unlink()


@contextmanager
def registry_lock(path):
    """OS lock released on process exit, including crashes; never delete the lock file."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.with_name(path.name+'.lock').open('a+b') as handle:
        if handle.seek(0, 2) == 0:
            handle.write(b'0'); handle.flush()
        handle.seek(0)
        try:
            if os.name == 'nt':
                import msvcrt
                msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as error:
            raise ValueError('Another installation is updating this storage registry; retry later') from error
        try:
            yield
        finally:
            handle.seek(0)
            if os.name == 'nt': msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else: fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def saved_settings(edition):
    path = configuration_path(edition)
    return json.loads(path.read_text(encoding='utf-8-sig')) if path.exists() else {}


def save_settings(edition, settings):
    path = configuration_path(edition)
    if path.exists():
        backup = path.with_name(path.name+'.before-storage-change-'+uuid.uuid4().hex[:8]+'.bak')
        shutil.copy2(path, backup)
    write_json(path, settings)


def location_for(target, settings, registry, destination_paths=None):
    root = Path(settings['shared_root']).resolve()
    if target.is_relative_to(root) and not destination_paths:
        return {'relative_path':target.relative_to(root).as_posix()}
    paths = {row['instance_id']:row['database_path'] for row in (destination_paths or [])}
    paths[settings['instance_id']] = str(target)
    missing = set(registry.get('instances', {})) - set(paths)
    if missing:
        raise ValueError('Moving outside the shared root requires destination_paths for every enrolled installation: '+', '.join(sorted(missing)))
    return {'host_paths':paths}


def attach_pointer(database, settings, edition):
    # Relative pointers work across Windows/Linux mounts of the same share.
    root = Path(settings['shared_root']).resolve()
    registry = Path(settings['storage_registry_path']).resolve()
    if not database.is_relative_to(root) or not registry.is_relative_to(root):
        return
    value = {'edition':edition, 'registry_relative_path':os.path.relpath(registry, database.parent).replace('\\','/'),
             'root_relative_path':os.path.relpath(root, database.parent).replace('\\','/')}
    pointer = database.with_name(database.name+'.registry.json')
    if pointer.exists() and json.loads(pointer.read_text(encoding='utf-8-sig')) != value:
        raise ValueError('Database already points at a different registry')
    write_json(pointer, value)


def status():
    from host_adapter import EDITION, load_host
    settings = saved_settings(EDITION)
    result = {'edition':EDITION, 'config_path':str(configuration_path(EDITION)), 'settings':settings}
    if settings.get('storage_registry_path'):
        registry = read_registry(settings, EDITION, allow_pending=True)
        result['registry'] = registry
        if registry['state'] != 'active':
            result['available'] = False
            return result
    try:
        loaded, _ = load_host()
        result.update(database_path=str(loaded['database_path']), exists=loaded['database_path'].is_file())
    except FileNotFoundError:
        result['configured'] = False
    return result


def set_guards(connection, freeze):
    if not freeze:
        for (name,) in connection.execute("SELECT name FROM sqlite_master WHERE type='trigger'").fetchall():
            if name.startswith(GUARD): connection.execute('DROP TRIGGER "'+name+'"')
        return
    for (table,) in connection.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall():
        if table.startswith('sqlite_'): continue
        quoted = '"'+table.replace('"','""')+'"'
        for operation in ('INSERT', 'UPDATE', 'DELETE'):
            name = GUARD+hashlib.sha256((table+operation).encode()).hexdigest()[:20]
            connection.execute(f'''CREATE TRIGGER IF NOT EXISTS "{name}" BEFORE {operation} ON {quoted}
                BEGIN SELECT RAISE(ABORT, 'BetterContext storage moved; reconnect through the shared registry'); END''')


def activate(settings, registry, destination):
    completed = dict(registry)
    completed.update(state='active', database=destination, revision=registry['revision']+1,
                     last_migration=registry.get('migration'))
    completed.pop('migration', None)
    write_json(Path(settings['storage_registry_path']), completed)
    return completed


def migrate(settings, edition, target, destination_paths=None):
    registry_path = Path(settings['storage_registry_path'])
    with registry_lock(registry_path):
        registry = read_registry(settings, edition)
        source = locate(settings, registry['database'])
        if source == target: return {'migrated':False, 'database_path':str(source)}
        if target.exists(): raise ValueError('Destination exists; migration never overwrites or merges it')
        if registry_path.is_relative_to(target.parent):
            raise ValueError('Keep the permanent registry separate from the destination database folder')
        target_location = location_for(target, settings, registry, destination_paths)
        transaction = uuid.uuid4().hex
        backup = source.parent/'backups'/('before-migration-'+transaction+'.db')
        pending = dict(registry, state='migrating', migration={
            'id':transaction, 'source':registry['database'], 'target':target_location,
            'started_at':datetime.now(timezone.utc).isoformat(), 'initiator':settings['instance_id'],
            'backup_on_initiator':str(backup)})
        # Publish the move BEFORE copying or changing either database.
        write_json(registry_path, pending)
        # Failures after this point deliberately leave the registry paused. Recovery
        # is explicit; an offline installation must never silently use an old copy.
        with closing(sqlite3.connect(database_uri(source, 'rw'), uri=True, timeout=30)) as lock:
            lock.execute('BEGIN IMMEDIATE')
            try:
                before = inspect_database(source, lock)
                # Commit source write guards before the SQLite backup. A second
                # connection backing up while this host holds a write reservation
                # can stall on CIFS even though it works on a local filesystem.
                set_guards(lock, True)
                lock.commit()
            except BaseException:
                lock.rollback()
                raise
        target.parent.mkdir(parents=True, exist_ok=True)
        backup.parent.mkdir(parents=True, exist_ok=True)
        with target.open('xb'): pass
        deadline = time.monotonic()+30
        def progress(status, remaining, total):
            if time.monotonic() > deadline:
                raise TimeoutError('Database copy exceeded 30 seconds; migration is paused for recovery')
        with closing(sqlite3.connect(database_uri(source), uri=True, timeout=30)) as reader:
            with closing(sqlite3.connect(database_uri(target, 'rw'), uri=True)) as copy:
                reader.backup(copy, pages=256, progress=progress, sleep=0.05)
                set_guards(copy, False)
                copy.commit()
        after = inspect_database(target)
        if before != after: raise ValueError('Migration content verification failed')
        with backup.open('xb') as handle, target.open('rb') as copied:
            shutil.copyfileobj(copied, handle); handle.flush(); os.fsync(handle.fileno())
        if inspect_database(backup) != before: raise ValueError('Backup verification failed')
        pending['migration']['verified'] = before
        write_json(registry_path, pending)
        attach_pointer(target, settings, edition)
        activate(settings, pending, target_location)
        return {'migrated':True, 'database_path':str(target), 'backup_path':str(backup),
                'original_path':str(source), 'original_writes_blocked':True, 'verified':after,
                'registry_path':str(registry_path), 'enrolled_instances':len(registry['instances'])}


def recover(action, check_only=True):
    from host_adapter import EDITION
    if action not in ('finish', 'cancel'): raise ValueError('action must be finish or cancel')
    settings = saved_settings(EDITION)
    path = Path(settings['storage_registry_path'])
    with registry_lock(path):
        data = read_registry(settings, EDITION, allow_pending=True)
        if data['state'] == 'active': return {'recovered':False, 'state':'active'}
        move = data['migration']
        source = locate(settings, move['source'])
        target = locate(settings, move['target'])
        plan = {'action':action, 'check_only':check_only, 'source':str(source), 'target':str(target)}
        if check_only: return plan
        with closing(sqlite3.connect(database_uri(source, 'rw'), uri=True, timeout=30)) as db:
            db.execute('BEGIN IMMEDIATE')
            try:
                if action == 'finish':
                    before, after = inspect_database(source, db), inspect_database(target)
                    if before != after or move.get('verified') != before:
                        raise ValueError('Verified source, destination and backup record do not match; cancel the move and choose a fresh destination')
                    set_guards(db, True)
                else:
                    set_guards(db, False)
                db.commit()
            except BaseException:
                db.rollback(); raise
        if action == 'finish': attach_pointer(target, settings, EDITION)
        activate(settings, data, move['target'] if action == 'finish' else move['source'])
        return dict(plan, recovered=True, retained_destination=str(target), state='active')


def configure(directory, mode, check_only=True, registry_path=None, shared_root=None, destination_paths=None):
    from host_adapter import EDITION, load_host
    if mode not in ('connect', 'create', 'migrate'): raise ValueError('mode must be connect, create, or migrate')
    folder = Path(directory).expanduser()
    if not folder.is_absolute(): raise ValueError('Choose an absolute storage folder path')
    target = (folder/'memory.db').resolve()
    settings = saved_settings(EDITION)
    override = os.environ.get('BETTERCONTEXT_'+EDITION.upper()+'_DB_PATH')
    if override: raise ValueError('Remove the edition database environment override before saving storage configuration')
    if mode == 'migrate':
        if not settings.get('storage_registry_path'):
            raise ValueError('First connect the current database to a permanent storage registry')
        data = read_registry(settings, EDITION)
        source = locate(settings, data['database'])
        inspect_database(source)
        if target != source and target.exists(): raise ValueError('Destination exists; migration never overwrites or merges it')
        if Path(settings['storage_registry_path']).is_relative_to(target.parent):
            raise ValueError('Keep the permanent registry outside the destination database folder')
        location_for(target, settings, data, destination_paths)
        if check_only: return {'check_only':True, 'source':str(source), 'target':str(target), 'registry_path':settings['storage_registry_path'], 'instances':list(data['instances'])}
        return migrate(settings, EDITION, target, destination_paths)
    registry_path = Path(registry_path or settings.get('storage_registry_path') or (folder.parent/'bettercontext-registry'/f'{EDITION}.json')).expanduser()
    shared_root = Path(shared_root or settings.get('shared_root') or folder.parent).expanduser()
    if not registry_path.is_absolute() or not shared_root.is_absolute(): raise ValueError('Registry and shared root paths must be absolute')
    registry_path, shared_root = registry_path.resolve(), shared_root.resolve()
    if not registry_path.is_relative_to(shared_root): raise ValueError('Keep the registry inside the stable shared root')
    if registry_path.is_relative_to(folder.resolve()): raise ValueError('Keep the registry outside the database folder that may move')
    settings.update(storage_registry_path=str(registry_path), shared_root=str(shared_root), instance_id=settings.get('instance_id', instance_id()))
    settings['runtime_mode'] = 'bundled'
    if mode == 'connect':
        target = resolve_database(target, EDITION)
        inspected = inspect_database(target)
    elif target.exists(): raise ValueError('Destination exists; use connect')
    else: inspected = None
    other = 'private' if EDITION == 'public' else 'public'
    other_settings = saved_settings(other)
    if other_settings:
        other_database = resolve_settings(other_settings, other)
        if other_database == target: raise ValueError('Public and private editions must use separate databases')
    if registry_path.exists():
        data = read_registry(settings, EDITION)
        if 'host_paths' in data['database'] and settings['instance_id'] not in data['database']['host_paths']:
            data['database']['host_paths'][settings['instance_id']] = str(target)
        if locate(settings, data['database']) != target:
            raise ValueError('Registry points to another database; use its current location or migrate it')
    else:
        data = {'version':1, 'edition':EDITION, 'registry_id':uuid.uuid4().hex, 'revision':1,
                'state':'active', 'database':location_for(target, settings, {}), 'instances':{}}
    plan = {'mode':mode, 'edition':EDITION, 'database_path':str(target), 'registry_path':str(registry_path),
            'shared_root':str(shared_root), 'instance_id':settings['instance_id'], 'check_only':check_only, 'verified':inspected}
    if check_only: return plan
    with registry_lock(registry_path):
        if registry_path.exists():
            data = read_registry(settings, EDITION)
            if 'host_paths' in data['database'] and settings['instance_id'] not in data['database']['host_paths']:
                data['database']['host_paths'][settings['instance_id']] = str(target)
            if locate(settings, data['database']) != target: raise ValueError('Storage changed while enrolling; retry')
        if mode == 'create':
            runtime = Path(__file__).resolve().parents[1]/'skills'/('bettercontext-private' if EDITION=='private' else 'bettercontext')/'scripts/runtime'
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open('xb'): pass
            env = os.environ.copy(); env['BETTERCONTEXT_DB_PATH']=str(target)
            result = subprocess.run([sys.executable,'-B',str(runtime/'memory.py'),'init'],env=env,capture_output=True,text=True,timeout=30)
            if result.returncode: raise ValueError('Initialization failed; reserved file retained: '+result.stderr.strip())
            plan['verified'] = inspect_database(target)
        data['instances'][settings['instance_id']] = {'shared_root':str(shared_root), 'platform':sys.platform}
        write_json(registry_path, data)
        attach_pointer(target, settings, EDITION)
        settings['database_path'] = str(target)  # compatibility breadcrumb, never used when registry is present
        save_settings(EDITION, settings)
    return dict(plan, configured=True)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['status','connect','create','migrate','recover'])
    parser.add_argument('--directory')
    parser.add_argument('--registry-path')
    parser.add_argument('--shared-root')
    parser.add_argument('--action', choices=['finish','cancel'])
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    if args.mode == 'status': result = status()
    elif args.mode == 'recover': result = recover(args.action, not args.apply)
    else: result = configure(args.directory,args.mode,not args.apply,args.registry_path,args.shared_root)
    print(json.dumps(result, indent=2))
