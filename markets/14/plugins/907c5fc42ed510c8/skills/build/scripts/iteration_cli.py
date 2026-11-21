"""Host-local Build_ tools for the installable chat workflow.

Runs only the bundled bookkeeping engine. It never executes customer program code.
State is local to the host environment; import the last program ZIP in a fresh session.
"""
from __future__ import annotations
import argparse
import base64
import json
import os
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from iteration.engine import Engine
from iteration.mcp import MCP
from iteration.layout import audit_archive
from iteration.safety import IterationError, canonical, code_path, sha


def main() -> int:
    parser = argparse.ArgumentParser(description='Build_ chat workflow tools; no dashboard or external AI calls')
    parser.add_argument('--state', type=Path, default=Path(os.environ.get('ITERATION_STATE_DIR', str(Path.cwd()/'.iteration-state'))))
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('status'); sub.add_parser('projects')
    call = sub.add_parser('call'); call.add_argument('tool'); call.add_argument('--arguments', type=Path, required=True)
    plan = sub.add_parser('plan'); plan.add_argument('--task-id', required=True); plan.add_argument('--revision', type=int, required=True); plan.add_argument('--file', type=Path, required=True)
    imp = sub.add_parser('import'); imp.add_argument('archive', type=Path); imp.add_argument('--name', default='')
    audit = sub.add_parser('audit'); audit.add_argument('archive', type=Path)
    log = sub.add_parser('log'); log.add_argument('archive', type=Path)
    export = sub.add_parser('export'); export.add_argument('--build-id', required=True); export.add_argument('--output', type=Path, required=True)
    checkout = sub.add_parser('checkout'); checkout.add_argument('--project-id', required=True); checkout.add_argument('--snapshot-id', required=True); checkout.add_argument('--output', type=Path, required=True)
    save = sub.add_parser('save'); save.add_argument('--task-id', required=True); save.add_argument('--revision', type=int, required=True); save.add_argument('--source', type=Path, required=True)
    args = parser.parse_args()
    engine = Engine(args.state)
    try:
        if args.command in ('status','projects'):
            result = MCP(engine).call('iteration_status' if args.command == 'status' else 'iteration_projects', {})
        elif args.command == 'call':
            if args.arguments.stat().st_size > 32 * 1024 * 1024:
                raise IterationError('Arguments file exceeds the size limit.')
            result = MCP(engine).call(args.tool, json.loads(args.arguments.read_text(encoding='utf-8')))
        elif args.command == 'plan':
            if args.file.stat().st_size > 128*1024:
                raise IterationError('Plan exceeds the size limit.')
            result = engine.configure_checks(args.task_id, args.revision, json.loads(args.file.read_text(encoding='utf-8')))
        elif args.command == 'import':
            if args.archive.stat().st_size > 128 * 1024 * 1024:
                raise IterationError('Archive exceeds the import size limit.')
            result = engine.import_zip(args.name, args.archive.read_bytes())
        elif args.command == 'log':
            if args.archive.stat().st_size > 512 * 1024:
                raise IterationError('Report exceeds the size limit.')
            result = engine.ingest_log_report(base64.b64encode(args.archive.read_bytes()).decode('ascii'))
        elif args.command == 'audit':
            if args.archive.stat().st_size > 128 * 1024 * 1024:
                raise IterationError('Archive exceeds the audit limit.')
            result = audit_archive(args.archive.read_bytes())
        elif args.command == 'export':
            build, raw = engine.archive_bytes(args.build_id)
            audit_archive(raw)
            if args.output.is_symlink():
                raise IterationError('Refusing to overwrite a symlink.')
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_bytes(raw)
            if sha(args.output.read_bytes()) != build['archive_sha256']:
                raise IterationError('Export verification failed.')
            result = {'path':str(args.output.resolve()), 'sha256':sha(raw), 'bytes':len(raw), 'build_id':build['id'], 'release_status':build.get('release',{}).get('status') or build.get('delivery',{}).get('status') or 'candidate_only', 'delivery_status':build.get('delivery',{}).get('status','not_delivered'), 'runtime_qualified':bool(build.get('release')), 'note':'Use deliver.py --mode windows-testable for the customer attachment with explicit unverified checks, or qualified mode for observed runtime qualification. This raw export does not establish a new delivery or new test success.'}
        elif args.command == 'checkout':
            if args.output.is_symlink():
                raise IterationError('Checkout refuses a symlink output directory.')
            if args.output.exists() and any(args.output.iterdir()):
                raise IterationError('Checkout requires a new or empty directory.')
            listing = engine.list_files(args.project_id, args.snapshot_id)
            with engine.store.transaction() as st:
                files = engine._snapshot_files(st, args.snapshot_id)
            count = 0
            for name, data in files.items():
                if name in ('run.bat', 'Run.bat', 'PROGRAM/readme.md', 'readme.md') or name.startswith(('PROGRAM/Automation/', 'Program/Automation/')):
                    continue
                safe = code_path(name)
                target = args.output.joinpath(*safe.split('/'))
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data); count += 1
            result = {'path':str(args.output.resolve()), 'files':count, 'note':'Editable source only; read production records through resume/read_file.'}
        else:
            if not args.source.is_dir() or args.source.is_symlink():
                raise IterationError('A real source directory is required.')
            items = []
            for path in sorted(args.source.rglob('*')):
                if path.is_symlink():
                    raise IterationError('Symlinks are not permitted in a source snapshot.')
                if not path.is_file():
                    continue
                rel = path.relative_to(args.source).as_posix()
                name = code_path(rel)
                if path.stat().st_size > 16 * 1024 * 1024:
                    raise IterationError('One source file exceeds the size limit.')
                items.append({'path':name, 'content':base64.b64encode(path.read_bytes()).decode('ascii'), 'encoding':'base64'})
            if not items:
                raise IterationError('Source tree is empty. Expected PROGRAM/main.py beneath --source.')
            revision = args.revision
            for offset in range(0, len(items), 100):
                result = engine.write_files(args.task_id, revision, items[offset:offset+100])
                revision = result['task_revision']
            result['note'] = 'Complete files saved. Missing files are not silently deleted; authorize deletions explicitly.'
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    except (IterationError, OSError, ValueError) as exc:
        print(json.dumps({'error':getattr(exc, 'code', type(exc).__name__), 'message':str(exc)}))
        return 1
    finally:
        engine.close()


if __name__ == '__main__':
    raise SystemExit(main())
