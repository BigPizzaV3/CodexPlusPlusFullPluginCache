"""Public host adapter; bundled runtime and independent user storage only."""
from contextlib import closing
from pathlib import Path
import os
import storage_settings
import sqlite3
import subprocess
import sys

EDITION = 'public'
SERVER_NAME = 'bettercontext'
SKILL = Path(__file__).resolve().parents[1] / 'skills/bettercontext/scripts'
sys.path.insert(0, str(SKILL))
from bettercontext import default_database, configuration_path

def load_host():
    path = default_database().expanduser()
    if not path.is_absolute():
        raise ValueError('BETTERCONTEXT_PUBLIC_DB_PATH must be an absolute path')
    settings = storage_settings.saved_settings('public') if not os.environ.get('BETTERCONTEXT_PUBLIC_DB_PATH') else {}
    return {**settings, 'database_path': path.resolve(), 'bettercontext_root': SKILL / 'runtime'}, configuration_path()

def initialize_database(settings):
    path = settings['database_path']
    if path.exists():
        # Initialization must never migrate, truncate or change a pre-existing file.
        uri = path.as_uri()
        if os.name == 'nt' and path.drive.startswith('\\\\'):
            uri = uri.replace('file://', 'file:////', 1)
        with closing(sqlite3.connect(uri + '?mode=ro', uri=True)) as conn:
            tables = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
            required = {'core_facts', 'tasks', 'session_logs', 'chat_aliases', 'relay_messages'}
            if not required <= tables:
                raise ValueError('Existing database schema is incomplete; no changes made')
        return {'initialized': True, 'created': False, 'database_path': str(path)}
    env = os.environ.copy()
    env['BETTERCONTEXT_DB_PATH'] = str(path)
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    path.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run([sys.executable, '-B', str(settings['bettercontext_root'] / 'memory.py'), 'init'],
                            env=env, capture_output=True, text=True, encoding='utf-8', timeout=30)
    if result.returncode:
        raise ValueError(result.stderr.strip() or 'Public initialization failed')
    return {'initialized': True, 'created': True, 'database_path': str(path)}
