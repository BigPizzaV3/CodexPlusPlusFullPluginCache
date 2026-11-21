"""Prepare exact Build_ runtime files in a host-owned sandbox; no network or installs.

This is a consistency/copy tool, not a security sandbox or proof of host activation.
It never executes customer application code. Only --probe runs the verified engine's
three --help commands, which do not create projects or qualify an application.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

SCHEMA = 'build.runtime-access/1'
ENGINE_FILES = {'deliver.py': {'sha256': '6a21d687096c4ba886601f25fde912875b10fa2866b1a6aa3555e0ce29e591c6', 'bytes': 12246}, 'iteration/__init__.py': {'sha256': '08cbd3b43857b8c860ca1afdccebe48e13d57da6febbfa20a5b71c24212424b6', 'bytes': 122}, 'iteration/engine.py': {'sha256': '05f43ab07801d57dedc24ca147d80ccc6c219a68ffdbea3bfbe537ed98f1f16f', 'bytes': 45490}, 'iteration/layout.py': {'sha256': '4e9bc6d21804276b581447ff4deaaa8198de817db995fa767a13467a991906a4', 'bytes': 12621}, 'iteration/lifecycle_template.py': {'sha256': 'ed369b871d5e95af68399d7ba33ef636985c6ab51da225a9b8f01d16cd677967', 'bytes': 8528}, 'iteration/logs.py': {'sha256': '810fd02fb730421bf818168047eefce5edea2d54c459a2fc88d817c2341602f4', 'bytes': 5808}, 'iteration/mcp.py': {'sha256': '9507ce14775448bf5257e41071602095d68d5f0cfec64e81be87bb9d9f3495fe', 'bytes': 16222}, 'iteration/records.py': {'sha256': 'f15f6c0953c472468922d53debb616d40d40b5d11f176e6454fcdbce149ac8cf', 'bytes': 12303}, 'iteration/release_contract.py': {'sha256': 'b65a0f1c41ee48a7315b5878b10ac3e0a0f2b097140bd79001b21e99087faab2', 'bytes': 7938}, 'iteration/runner_template.py': {'sha256': '1f02f7f8e635624658f385db7b93f2053114dc76259d1648599ba63e6bbf7467', 'bytes': 20081}, 'iteration/safety.py': {'sha256': '3c43c919b4debe421bcd1982f67bb7f4b5c05d8eaf83a14a72f4213a26f64d44', 'bytes': 8831}, 'iteration/store.py': {'sha256': '83f37a1442fa6878a0a637f0e7da4884d8abb8b7ab38dd605733cb00605b936f', 'bytes': 3666}, 'iteration_cli.py': {'sha256': '8b6625b4e18ce2d48db9de6504dd2f52b0a9fa53c801c9227fedbde4fef83958', 'bytes': 7600}, 'release_check.py': {'sha256': '6a9a089d52eb2d3f4b57c3159295de8e90d1dd8727707a8d46a967c51a402eec', 'bytes': 12173}}
MAX_FILE_BYTES = 256 * 1024
ENTRYPOINTS = ('iteration_cli.py', 'deliver.py', 'release_check.py')


class RuntimeAccessError(ValueError):
    pass


def _real_path(value: Path) -> Path:
    """Reject symlinks/junctions in every existing ancestor before resolving."""
    path = Path(os.path.abspath(value))
    for component in (path, *path.parents):
        if component.is_symlink() or (hasattr(component, 'is_junction') and component.is_junction()):
            raise RuntimeAccessError('Linked runtime path refused: ' + str(component))
    return path


def inspect(root: Path, *, reject_extra_python: bool = False) -> dict:
    """Read and hash source only; no imports from the target or project writes."""
    root = _real_path(root)
    missing, mismatched, invalid = [], [], []
    if root.exists() and not root.is_dir():
        raise RuntimeAccessError('Runtime root must be a directory')
    for name, record in ENGINE_FILES.items():
        path = _real_path(root.joinpath(*name.split('/')))
        if not path.exists():
            missing.append(name)
            continue
        if not path.is_file() or path.stat().st_size > MAX_FILE_BYTES:
            invalid.append({'file': name, 'reason': 'not a bounded regular file'})
            continue
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        if digest != record['sha256'] or len(raw) != record['bytes']:
            mismatched.append({'file': name, 'expected_sha256': record['sha256'],
                               'actual_sha256': digest, 'expected_bytes': record['bytes'],
                               'actual_bytes': len(raw)})
            continue
        try:
            ast.parse(raw.decode('utf-8'), filename=name)
        except (UnicodeError, SyntaxError) as exc:
            invalid.append({'file': name, 'reason': str(exc)})
    extras = []
    if reject_extra_python and root.is_dir():
        # Prevent source imports from silently using extra/shadowing modules.
        for path in root.rglob('*'):
            _real_path(path)
            rel = path.relative_to(root).as_posix()
            if path.is_file() and path.suffix.lower() in ('.py', '.pyc', '.pyd', '.so') and rel not in ENGINE_FILES:
                extras.append(rel)
    passed = not (missing or mismatched or invalid or extras)
    return {'schema': SCHEMA, 'status': 'passed' if passed else 'blocked',
            'runtime_root': str(root), 'expected_files': len(ENGINE_FILES),
            'files_verified': len(ENGINE_FILES) - len(missing) - len(mismatched) - len(invalid),
            'missing': missing, 'mismatched': mismatched, 'invalid': invalid,
            'unexpected_python_files': extras,
            'entrypoints': {name: str(root / name) for name in ENTRYPOINTS},
            'network_used': False, 'customer_code_executed': False,
            'application_qualified': False}


def copy_runtime(source: Path, destination: Path) -> dict:
    """Copy only pinned runtime files into a NEW directory; never overwrite state."""
    source = _real_path(source)
    destination = _real_path(destination)
    check = inspect(source)
    if check['status'] != 'passed':
        return check
    if destination.exists():
        raise RuntimeAccessError('Destination already exists; choose a fresh runtime directory')
    if not destination.parent.is_dir():
        raise RuntimeAccessError('Destination parent must be an existing session-owned directory')
    # A separate staging directory avoids exposing a partially copied runtime as ready.
    with tempfile.TemporaryDirectory(prefix='.build-runtime-stage-', dir=destination.parent) as temporary:
        stage = Path(temporary) / 'runtime'
        stage.mkdir()
        for name, record in ENGINE_FILES.items():
            src = _real_path(source.joinpath(*name.split('/')))
            raw = src.read_bytes()
            # Detect source changes between inspection and copy, without executing them.
            if hashlib.sha256(raw).hexdigest() != record['sha256'] or len(raw) != record['bytes']:
                raise RuntimeAccessError('Runtime source changed while copying: ' + name)
            target = stage.joinpath(*name.split('/'))
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open('xb') as stream:
                stream.write(raw)
        checked = inspect(stage, reject_extra_python=True)
        if checked['status'] != 'passed':
            raise RuntimeAccessError('Staged runtime did not verify')
        # mkdir is an exclusive reservation even if another process creates a target.
        destination.mkdir()
        created = []
        try:
            for name in ENGINE_FILES:
                target = destination.joinpath(*name.split('/'))
                target.parent.mkdir(parents=True, exist_ok=True)
                _real_path(target)
                with target.open('xb') as stream:
                    stream.write((stage / name).read_bytes())
                created.append(target)
        except BaseException:
            # Delete only this invocation's files, never a pre-existing tree.
            for target in reversed(created):
                if not target.is_symlink():
                    target.unlink(missing_ok=True)
            for directory in (destination / 'iteration', destination):
                try:
                    directory.rmdir()
                except OSError:
                    pass
            raise
    result = inspect(destination, reject_extra_python=True)
    result['source_root'] = str(source)
    result['materialized'] = result['status'] == 'passed'
    return result


def probe(root: Path) -> dict:
    """Prove verified entrypoints import and parse --help; not an app/build test."""
    check = inspect(root, reject_extra_python=True)
    if check['status'] != 'passed':
        return check
    environment = dict(os.environ)
    environment.pop('PYTHONPATH', None)
    environment.pop('PYTHONHOME', None)
    environment['PYTHONDONTWRITEBYTECODE'] = '1'
    runs = []
    with tempfile.TemporaryDirectory(prefix='build-runtime-probe-') as work:
        for name in ENTRYPOINTS:
            try:
                completed = subprocess.run(
                    [sys.executable, '-B', '-E', '-s', str(Path(check['runtime_root']) / name), '--help'],
                    cwd=work, env=environment, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                    timeout=15, check=False)
                output = completed.stdout.decode('utf-8', errors='replace')
                error = completed.stderr.decode('utf-8', errors='replace')
                ok = completed.returncode == 0 and 'usage:' in output.lower()
                runs.append({'entrypoint': name, 'status': 'passed' if ok else 'blocked',
                             'exit_code': completed.returncode,
                             'detail': '' if ok else (error or output)[-2000:]})
            except subprocess.TimeoutExpired:
                runs.append({'entrypoint': name, 'status': 'blocked', 'detail': 'timeout'})
        check['created_project_state'] = any(Path(work).iterdir())
    check['command_probes'] = runs
    check['runtime_executable'] = all(r['status'] == 'passed' for r in runs) and not check['created_project_state']
    check['status'] = 'passed' if check['runtime_executable'] else 'blocked'
    return check


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--check', type=Path, metavar='RUNTIME_DIR')
    mode.add_argument('--copy-from', type=Path, metavar='SOURCE_DIR')
    mode.add_argument('--inventory', action='store_true')
    parser.add_argument('--destination', type=Path)
    parser.add_argument('--probe', action='store_true', help='Run verified --help entrypoints only')
    args = parser.parse_args(argv)
    if args.copy_from is not None and args.destination is None:
        parser.error('--copy-from requires --destination')
    if args.copy_from is None and args.destination is not None:
        parser.error('--destination is only valid with --copy-from')
    if args.inventory and args.probe:
        parser.error('--inventory cannot execute probes')
    try:
        if args.inventory:
            result = {'schema': SCHEMA, 'status': 'inventory', 'files': ENGINE_FILES,
                      'network_used': False, 'customer_code_executed': False}
        elif args.copy_from is not None:
            result = copy_runtime(args.copy_from, args.destination)
        else:
            result = inspect(args.check, reject_extra_python=True)
        if args.probe and result['status'] == 'passed':
            result = probe(Path(result['runtime_root']))
    except (OSError, ValueError) as exc:
        result = {'schema': SCHEMA, 'status': 'blocked', 'reason': str(exc),
                  'network_used': False, 'customer_code_executed': False,
                  'application_qualified': False}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result['status'] in ('passed', 'inventory') else 1


if __name__ == '__main__':
    raise SystemExit(main())
