"""Read the stable, shared registry afresh for every database connection."""
import json
import os
import platform
import sys
from pathlib import Path, PurePosixPath


def instance_id():
    return platform.node().casefold()


def sqlite_uri(path, mode='ro'):
    path = Path(path).resolve()
    uri = path.as_uri()
    if os.name == 'nt' and path.drive.startswith('\\\\'):
        uri = uri.replace('file://', 'file:////', 1)
    # Linux CIFS rejects SQLite's default shared-to-exclusive lock upgrade on
    # some SMB servers. unix-excl obtains the compatible file lock up front.
    return uri+'?mode='+mode+('&vfs=unix-excl' if sys.platform.startswith('linux') else '')


def read_registry(settings, edition=None, allow_pending=False):
    registry = Path(settings['storage_registry_path']).expanduser()
    if not registry.is_absolute():
        raise ValueError('The storage registry path must be absolute on this host')
    data = json.loads(registry.read_text(encoding='utf-8-sig'))
    if data.get('version') != 1 or data.get('edition') not in ('public', 'private'):
        raise ValueError('Unsupported BetterContext storage registry')
    if edition and data['edition'] != edition:
        raise ValueError('Storage belongs to a different BetterContext edition')
    if data.get('state') != 'active' and not allow_pending:
        raise ValueError('BetterContext storage migration is pending; retry after completion or use memory_recover_storage. No fallback was opened.')
    return data


def locate(settings, location):
    if 'relative_path' in location:
        relative = PurePosixPath(location['relative_path'])
        if relative.is_absolute() or '..' in relative.parts or '\\' in str(relative) or ':' in str(relative):
            raise ValueError('Registry path must remain inside the configured shared root')
        root = Path(settings['shared_root']).expanduser().resolve()
        path = (root / Path(*relative.parts)).resolve()
        if not path.is_relative_to(root):
            raise ValueError('Registry path escapes the configured shared root')
        return path
    identity = settings.get('instance_id', instance_id())
    value = location.get('host_paths', {}).get(identity)
    if not value:
        raise ValueError('This installation needs its path to the relocated database registered: '+identity)
    path = Path(value).expanduser()
    if not path.is_absolute():
        raise ValueError('Registered database path must be absolute on this host')
    return path.resolve()


def resolve_settings(settings, edition=None):
    if settings.get('storage_registry_path'):
        data = read_registry(settings, edition)
        path = locate(settings, data['database'])
        if not path.is_file():
            raise FileNotFoundError('Shared database is unavailable; no fallback was created: '+str(path))
        return path
    return resolve_database(Path(settings['database_path']), edition)


def resolve_database(path, edition=None):
    path = Path(path).expanduser()
    if not path.is_absolute():
        raise ValueError('Storage must use an absolute path accessible from this computer')
    visited = set()
    for _ in range(8):
        path = path.resolve()
        if path in visited:
            raise ValueError('Storage redirect cycle detected')
        visited.add(path)
        pointer = path.with_name(path.name+'.registry.json')
        if pointer.exists():
            data = json.loads(pointer.read_text(encoding='utf-8-sig'))
            settings = {'storage_registry_path': str((path.parent/data['registry_relative_path']).resolve()),
                        'shared_root': str((path.parent/data['root_relative_path']).resolve()),
                        'instance_id': instance_id()}
            return resolve_settings(settings, edition)
        redirect = path.with_name(path.name+'.redirect.json')
        if not redirect.exists():
            return path
        data = json.loads(redirect.read_text(encoding='utf-8-sig'))
        if edition and data.get('edition') != edition:
            raise ValueError('Storage belongs to a different BetterContext edition')
        target = Path(data['database_path'])
        path = target if target.is_absolute() else path.parent/target
    raise ValueError('Too many storage redirects')
