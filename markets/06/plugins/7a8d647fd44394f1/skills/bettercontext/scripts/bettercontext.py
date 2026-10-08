#!/usr/bin/env python3
"""Run the bundled public BetterContext CLI with edition-specific storage."""
from contextlib import closing
import argparse
import json
import os
from pathlib import Path
import runpy
import sqlite3
import sys


sys.path.insert(0, str(Path(__file__).resolve().parents[3]/'scripts'))
import storage_settings


def configuration_path():
    return storage_settings.configuration_path('public')


def default_database():
    configured = os.environ.get('BETTERCONTEXT_PUBLIC_DB_PATH')
    if not configured and configuration_path().is_file():
        return storage_settings.resolve_settings(json.loads(configuration_path().read_text(encoding='utf-8-sig')), 'public')
    if configured:
        return storage_settings.resolve_database(Path(configured), 'public')
    if os.name == 'nt':
        base = Path(os.environ.get('LOCALAPPDATA', str(Path.home()/'AppData/Local')))
    elif sys.platform == 'darwin':
        base = Path.home()/'Library/Application Support'
    else:
        base = Path(os.environ.get('XDG_STATE_HOME', str(Path.home()/'.local/state')))
    return base/'BetterContextPublic/memory.db'


def inspect_database(path):
    result = {'edition': 'public', 'database_path': str(path), 'exists': path.is_file()}
    if path.is_file():
        uri = path.as_uri()
        if os.name == 'nt' and path.drive.startswith('\\\\'):
            uri = uri.replace('file://', 'file:////', 1)
        with closing(sqlite3.connect(uri + '?mode=ro', uri=True, timeout=10)) as conn:
            result['quick_check'] = conn.execute('PRAGMA quick_check').fetchone()[0]
            result['journal_mode'] = conn.execute('PRAGMA journal_mode').fetchone()[0]
            result['schema_version'] = conn.execute('PRAGMA user_version').fetchone()[0]
    return result


def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__, add_help=False)
    parser.add_argument('--database', help='Explicit PUBLIC database path, before the command.')
    parser.add_argument('command', nargs='?', default='--help')
    parser.add_argument('arguments', nargs=argparse.REMAINDER)
    args, unknown = parser.parse_known_args()
    if unknown and unknown != ['--help']:
        parser.error('unknown launcher options: ' + ' '.join(unknown))
    path = Path(args.database).expanduser() if args.database else default_database()
    if not path.is_absolute():
        parser.error('database path must be absolute')
    path = storage_settings.resolve_database(path, 'public')
    if args.command == 'doctor':
        print(json.dumps(inspect_database(path), indent=2))
        return
    command = args.command
    if command != '--help':
        if command == 'init':
            path.parent.mkdir(parents=True, exist_ok=True)
        elif not path.is_file():
            raise ValueError('Public database is not initialized. Run init first: ' + str(path))
    # Deliberately override the legacy variable: an inherited setting must never
    # connect the public edition to a private installation by accident.
    os.environ['BETTERCONTEXT_DB_PATH'] = str(path)
    runtime = Path(__file__).resolve().parent / 'runtime'
    sys.path.insert(0, str(runtime))
    sys.dont_write_bytecode = True
    sys.argv = [str(runtime / 'memory.py'), command, *args.arguments]
    runpy.run_path(sys.argv[0], run_name='__main__')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, sqlite3.Error) as error:
        print(f'Error: {error}', file=sys.stderr)
        raise SystemExit(2)
