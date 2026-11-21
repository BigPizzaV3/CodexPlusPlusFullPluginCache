"""Bounded iteration engine. Model-facing actions never run project code; acceptance requires explicit user authorization."""
from __future__ import annotations
import ast
import base64
import io
import json
import platform
import re
import sys
import time
import uuid
import zipfile
from pathlib import Path
from . import BUILD, __version__
from .records import LAUNCHER, continuation, make_records
from .safety import (IterationError, MAX_FILES, MAX_TOTAL, canonical, code_path, decode_file,
                     read_archive, sha, SECRET)
from .store import Store
from .release_contract import (LIFECYCLE, PLAN, RECEIPT, validate_plan, verify_plan_files, validate_receipt)
from .logs import parse_log_report, MAX_REPORT_BYTES
from .runner_template import REMINDER
from .layout import (AUTO, RECORDS, OLD, INDEX, RUNNER, RETAINED_PREFIX, record, identity,
                     split_input, retain, check_delivery, audit_archive)

def now() -> str:
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())

def ident(prefix: str) -> str:
    return prefix + '_' + uuid.uuid4().hex[:16]

def digest_map(hashes: dict[str, str]) -> str:
    return sha(json.dumps(hashes, sort_keys=True, separators=(',', ':')).encode())

def clean_text(value: str, limit: int = 16000) -> str:
    if not isinstance(value, str) or len(value) > limit:
        raise IterationError('Text is invalid or too long.')
    if SECRET.search(value):
        raise IterationError('A likely credential was detected in the project notes.', 'possible_secret')
    return value.strip()

def clean_list(values: list[str], limit: int = 100) -> list[str]:
    if not isinstance(values, list) or len(values) > limit:
        raise IterationError('Expected a bounded list of text items.')
    return [clean_text(s) for s in values]

class Engine:
    def __init__(self, root: Path):
        self.store = Store(root)

    def close(self):
        self.store.close()

    def status(self) -> dict:
        return {'name': 'Build_', 'version': __version__, 'build': BUILD,
                'mode': 'chat-first private test', 'python': platform.python_version(), 'platform': platform.platform(),
                'capabilities': {'source_writes': True, 'complete_zip_export': True, 'coded_records': True, 'opaque_layout_v2': True, 'final_archive_audit': True,
                                 'syntax_checks': True, 'chat_acceptance': True, 'log_report_ingestion': True, 'runtime_log_zip': True, 'friendly_runtime_errors': True, 'host_release_gate': True, 'windows_testable_delivery': True, 'runtime_qualification_required_for_delivery': False, 'lifecycle_readiness_v1': True, 'functional_observations_v1': True, 'hash_bound_delivery_v1': True, 'automatic_code_execution': False, 'model_inference': False,
                                 'new_chat_creation': False, 'native_project_management': False, 'reasoning_switch': False},
                'chat_entry': {'display_name': 'Build_', 'text_alias': 'Build_', 'typed_prefix_required': False, 'starter_prompts': [], 'composer_rendering': 'host-controlled; not verified in this session'},
                'reply_footer': REMINDER,
                'runtime_requirement': 'Installed Python 3.10+; standard library only; no third-party DLLs required.',
                'limits': {'max_file_mib': 16, 'max_zip_import_mib': 128, 'max_payload_mib': 384, 'max_files': MAX_FILES}}

    def list_projects(self) -> dict:
        with self.store.transaction() as s:
            return {'projects': s.all('project')}

    def create_project(self, name: str, description: str = '', constraints: list[str] | None = None,
                       locked_paths: list[str] | None = None, console_mode: str = 'quiet') -> dict:
        name = clean_text(name, 100)
        if not name:
            raise IterationError('Give the project a name.')
        if console_mode not in ('quiet', 'interactive'):
            raise IterationError('console_mode must be quiet or interactive.')
        protected = []
        for path in locked_paths or []:
            p = code_path(path.rstrip('/'))
            protected.append(p + ('/' if path.endswith('/') else ''))
        p = {'id': ident('p'), 'name': name, 'description': clean_text(description), 'revision': 0,
             'accepted': None, 'latest': None, 'created': now(), 'constraints': clean_list(constraints or []),
             'locked_paths': protected, 'console_mode': console_mode}
        with self.store.transaction() as s:
            s.put('project', p)
            s.event(p['id'], {'at': now(), 'kind': 'project_created', 'project_id': p['id']})
        return p

    def resume(self, project_id: str) -> dict:
        with self.store.transaction() as s:
            p = s.get('project', project_id)
            tasks = [t for t in s.all('task') if t['project_id'] == project_id and t['status'] == 'active']
            builds = [b for b in s.all('build') if b['project_id'] == project_id]
            latest = s.get('build', p['latest']) if p['latest'] else None
            result = {'project': p, 'active_tasks': tasks, 'builds': builds,
                      'continuation_prompt': continuation(p, latest), 'events': s.events(project_id),
                      'authority_note': 'Accepted baseline and latest candidate are different. Imported notes and reported tests are unverified.',
                      'returned_logs': [r for r in s.all('logreport') if r['project_id'] == project_id],
                      'reply_footer': REMINDER}
            if latest:
                files = self._snapshot_files(s, latest['id'])
                result['latest_records'] = {k.rsplit('/', 1)[-1]: v.decode('utf-8') for k, v in files.items()
                                           if k.startswith(('PROGRAM/Automation/', 'Program/Automation/')) and k.rsplit('/', 1)[-1] in
                                           tuple(RECORDS[r] for r in ('index','position','rules','components','options','evidence')) + tuple(OLD[r] for r in ('index','position','rules','components','options','evidence'))}
            return result

    @staticmethod
    def _revision(project: dict, expected: int):
        if type(expected) is not int or project['revision'] != expected:
            raise IterationError('Project changed. Resume it and use its current revision before continuing.', 'stale_revision')

    def begin(self, project_id: str, expected_revision: int, intent: str,
              scope_paths: list[str] | None = None, not_changed: list[str] | None = None,
              acceptance_criteria: list[str] | None = None, base_build_id: str = '') -> dict:
        intent = clean_text(intent)
        if not intent:
            raise IterationError('An iteration needs a specific intent.')
        scopes = scope_paths or ['PROGRAM/']
        scopes = [(('PROGRAM/' if path in ('Program/', 'PROGRAM/') else
                    code_path(path.rstrip('/')) + ('/' if path.endswith('/') else '')))
                  for path in scopes]
        scopes = clean_list(scopes)
        with self.store.transaction() as s:
            p = s.get('project', project_id)
            self._revision(p, expected_revision)
            if any(t['project_id'] == project_id and t['status'] == 'active' for t in s.all('task')):
                raise IterationError('An active iteration already exists. Resume it or cancel it only after user authorization.', 'active_task')
            base = base_build_id or p['accepted']
            if not base and p['latest']:
                raise IterationError('No accepted baseline. Accept a candidate after explicit user authorization, or explicitly specify the candidate build to branch from.', 'baseline_required')
            if base:
                b = s.get('build', base)
                if b['project_id'] != project_id:
                    raise IterationError('The baseline belongs to another project.')
            task = {'id': ident('t'), 'project_id': project_id, 'base_build': base, 'base_project_revision': p['revision'],
                    'revision': 0, 'status': 'active', 'intent': intent, 'scope_paths': scopes,
                    'not_changed': clean_list(not_changed or []), 'acceptance_criteria': clean_list(acceptance_criteria or []),
                    'created': now(), 'reports': []}
            if base:
                prior_files = self._snapshot_files(s, base)
                base_source, base_notes = split_input(prior_files)
                base_manifest, _ = identity(prior_files, verify=True)
                if base_manifest.get('format_version') == 2:
                    retained = {k:v for k,v in base_notes.items() if k.startswith(RETAINED_PREFIX)}
                    if retained:
                        task['preserved_files'] = retain(retained, base_manifest)
                    old_context = record(prior_files, 'retained')
                    if old_context and not retained:
                        task['archive_context'] = old_context.decode('utf-8', errors='replace')
                elif base_notes:
                    task['preserved_files'] = retain(base_notes, base_manifest)
            s.put('task', task)
            if base:
                for path, data in base_source.items():
                    s.set_file(task['id'], path, data)
            s.event(project_id, {'at': now(), 'kind': 'iteration_started', 'task_id': task['id'], 'base_build': base, 'intent': intent})
            return task

    def _active(self, s: Store, task_id: str, expected_task_revision: int | None = None) -> tuple[dict, dict]:
        t = s.get('task', task_id)
        p = s.get('project', t['project_id'])
        if t['status'] != 'active':
            raise IterationError('This iteration is no longer active.', 'closed_task')
        self._revision(p, t['base_project_revision'])
        if expected_task_revision is not None and (type(expected_task_revision) is not int or t['revision'] != expected_task_revision):
            raise IterationError('Source changed since you read it. Refresh the task revision before writing.', 'stale_revision')
        return t, p

    @staticmethod
    def _permitted(path: str, task: dict, project: dict):
        if not any(path == p or (p.endswith('/') and path.startswith(p)) for p in task['scope_paths']):
            raise IterationError(f'Path is outside the approved task scope: {path}', 'out_of_scope')
        if task.get('base_build') and any(path == p or (p.endswith('/') and path.startswith(p)) for p in project['locked_paths']):
            raise IterationError(f'Path is locked: {path}', 'locked_path')

    def write_files(self, task_id: str, expected_task_revision: int, files: list[dict], deletions: list[str] | None = None) -> dict:
        if not isinstance(files, list) or len(files) > 100:
            raise IterationError('Send at most 100 complete files in one call.')
        updates = {}
        for item in files:
            if not isinstance(item, dict) or set(item)-{'path', 'content', 'encoding'}:
                raise IterationError('Each file needs path, content, and optional encoding.')
            path = code_path(item.get('path', ''))
            if path.casefold() in {x.casefold() for x in updates}:
                raise IterationError('Duplicate file in write request.')
            updates[path] = decode_file(item)
        deletes = [code_path(x) for x in clean_list(deletions or [], 100)]
        if set(deletes) & set(updates):
            raise IterationError('A file cannot be written and deleted in the same call.')
        if not updates and not deletes:
            raise IterationError('No source changes supplied.')
        with self.store.transaction() as s:
            t, p = self._active(s, task_id, expected_task_revision)
            old = s.file_map(task_id)
            new = dict(old)
            for path in (*updates.keys(), *deletes):
                self._permitted(path, t, p)
            for path in deletes:
                if path not in new:
                    raise IterationError(f'Cannot delete missing file: {path}')
                del new[path]
            new.update(updates)
            folded: dict[str, str] = {}
            for path in new:
                parts = path.split('/')
                for i in range(1, len(parts)+1):
                    prefix = '/'.join(parts[:i]); key = prefix.casefold()
                    if key in folded and folded[key] != prefix:
                        raise IterationError('Case-colliding Windows path.')
                    folded[key] = prefix
                if any('/'.join(parts[:i]) in new for i in range(1, len(parts))):
                    raise IterationError('A file is also being used as a directory.')
            if len(new) > MAX_FILES or sum(map(len, new.values())) > MAX_TOTAL:
                raise IterationError('Project exceeds the alpha file/size limits.')
            for path in deletes:
                s.db.execute('DELETE FROM files WHERE ns=? AND path=?', (task_id, path))
            for path, data in updates.items():
                s.set_file(task_id, path, data)
            t['revision'] += 1
            s.put('task', t)
            s.event(p['id'], {'at': now(), 'kind': 'source_updated', 'task_id': task_id,
                              'task_revision': t['revision'], 'paths': list(updates), 'deleted': deletes})
            return {'task_id': task_id, 'task_revision': t['revision'], 'written': list(updates), 'deleted': deletes,
                    'source_digest': digest_map(s.hashes(task_id))}

    def list_files(self, project_id: str, snapshot_id: str = '') -> dict:
        with self.store.transaction() as s:
            p = s.get('project', project_id)
            target = snapshot_id or p['latest']
            if not target:
                return {'project_id': project_id, 'files': [], 'snapshot_id': None}
            kind = 'task' if target.startswith('t_') else 'build'
            entity = s.get(kind, target)
            if entity['project_id'] != project_id:
                raise IterationError('Snapshot does not belong to this project.')
            files = self._snapshot_files(s, target)
            return {'project_id': project_id, 'snapshot_id': target, 'task_revision': entity.get('revision'),
                    'files': [{'path': p, 'bytes': len(d), 'sha256': sha(d)} for p, d in files.items()]}

    def read_file(self, project_id: str, snapshot_id: str, path: str, offset: int = 0, max_bytes: int = 120000) -> dict:
        path = canonical(path)
        if path.startswith('Program/'):
            path = 'PROGRAM/' + path[len('Program/'):]
        elif path == 'Run.bat':
            path = 'run.bat'
        elif path == 'readme.md':
            path = 'PROGRAM/readme.md'
        if type(offset) is not int or offset < 0 or type(max_bytes) is not int or not 1 <= max_bytes <= 512000:
            raise IterationError('Invalid file range.')
        with self.store.transaction() as s:
            kind = 'task' if snapshot_id.startswith('t_') else 'build'
            snap = s.get(kind, snapshot_id)
            if snap['project_id'] != project_id:
                raise IterationError('Snapshot does not belong to this project.')
            files = self._snapshot_files(s, snapshot_id)
            if path not in files:
                raise IterationError('File not found.', 'not_found')
            data = files[path]; part = data[offset:offset+max_bytes]
            try:
                content = part.decode('utf-8'); encoding = 'utf-8'
            except UnicodeDecodeError:
                content = base64.b64encode(part).decode(); encoding = 'base64'
            return {'path': path, 'snapshot_id': snapshot_id, 'offset': offset, 'total_bytes': len(data),
                    'sha256': sha(data), 'encoding': encoding, 'content': content,
                    'next_offset': offset+len(part) if offset+len(part) < len(data) else None}

    def _checks(self, s: Store, task: dict) -> dict:
        files = s.file_map(task['id'])
        results = []
        results.append({'name': 'entrypoint', 'passed': 'PROGRAM/main.py' in files, 'detail': 'PROGRAM/main.py is required.'})
        syntax_count = 0
        for path, data in files.items():
            if path.lower().endswith('.py'):
                syntax_count += 1
                try:
                    # Parse against our declared minimum as well as this interpreter.
                    # This checks grammar only, not runtime-library compatibility.
                    ast.parse(data, filename=path, mode='exec', feature_version=(3, 10))
                    compile(data, path, 'exec', dont_inherit=True)
                    results.append({'name': 'python_syntax', 'path': path, 'passed': True})
                except (SyntaxError, ValueError, OverflowError) as exc:
                    results.append({'name': 'python_syntax', 'path': path, 'passed': False, 'detail': str(exc)[:1000]})
            try:
                code_path(path)
                if SECRET.search(data.decode('utf-8', errors='ignore')):
                    raise IterationError('Possible credential.')
            except IterationError as exc:
                results.append({'name': 'package_safety', 'path': path, 'passed': False, 'detail': str(exc)})
        return {'status': 'passed' if all(r['passed'] for r in results) else 'failed', 'created_utc': now(),
                'environment': platform.platform(), 'python_version': platform.python_version(),
                'source_digest': digest_map(s.hashes(task['id'])), 'task_revision': task['revision'],
                'python_files_parsed': syntax_count, 'minimum_python_syntax': '3.10', 'checks': results,
                'scope': 'Static syntax, entrypoint, paths and best-effort credential patterns. No project code executed.',
                'not_validated': ['Windows BAT execution', 'runtime dependencies', 'program behavior', 'visual quality', 'semantic design constraints']}

    def check(self, task_id: str) -> dict:
        with self.store.transaction() as s:
            t, _ = self._active(s, task_id)
            return self._checks(s, t)

    def report(self, task_id: str, expected_task_revision: int, description: str, outcome: str, environment: str) -> dict:
        if outcome not in ('passed', 'failed', 'not_run'):
            raise IterationError('Report outcome must be passed, failed, or not_run.')
        with self.store.transaction() as s:
            t, p = self._active(s, task_id, expected_task_revision)
            report = {'created_utc': now(), 'description': clean_text(description), 'outcome': outcome,
                      'environment': clean_text(environment, 1000), 'source_digest': digest_map(s.hashes(task_id)),
                      'trust': 'host_reported_not_independently_observed', 'task_revision': t['revision']}
            t['reports'].append(report)
            if len(t['reports']) > 100:
                raise IterationError('Too many reports for this iteration.')
            s.put('task', t)
            s.event(p['id'], {'at': now(), 'kind': 'host_test_reported', 'task_id': task_id, 'outcome': outcome})
            return report

    def configure_checks(self, task_id: str, expected_task_revision: int, plan: dict) -> dict:
        checked = validate_plan(plan)
        clean_text(json.dumps(checked), 100000)
        with self.store.transaction() as s:
            t, p = self._active(s, task_id, expected_task_revision)
            prior = s.get('build', t['base_build']) if t.get('base_build') else {}
            externally_used = bool(prior.get('release') or prior.get('delivery') or prior.get('imported_identity') or (t.get('base_build') and p.get('accepted') == t['base_build']))
            if checked['continuation'] != externally_used:
                raise IterationError('Plan must distinguish a fresh project from a continuation.', 'plan_context_mismatch')
            if checked.get('previous_archive_sha256'):
                prior = s.get('build', t['base_build'])
                expected = prior.get('imported_archive_sha256') or prior.get('release', {}).get('archive_sha256') or prior['archive_sha256']
                if checked['previous_archive_sha256'] != expected:
                    raise IterationError('Use the actual preceding build archive, not an invented legacy fixture.', 'prior_version_mismatch')
            t['release_plan'] = checked
            t['revision'] += 1
            s.put('task', t)
            s.event(p['id'], {'at': now(), 'kind': 'checks_planned', 'task_id': task_id,
                             'case_ids': [c['id'] for c in checked['cases']]})
            return {'task_revision': t['revision'], 'plan': checked}

    def _snapshot_files(self, s: Store, snapshot_id: str) -> dict[str, bytes]:
        if snapshot_id.startswith('b_'):
            build = s.get('build', snapshot_id)
            if build.get('release'):
                return s.file_map(build['release']['id'])
        return s.file_map(snapshot_id)

    def _record_qualification_failure(self, build_id: str, attempt: dict) -> None:
        with self.store.transaction() as s:
            b = s.get('build', build_id)
            if b.get('release'):
                return
            b['last_qualification_failure'] = attempt
            b['validation_summary']['release_gate'] = 'blocked'
            s.put('build', b)
            s.event(b['project_id'], {'at': now(), 'kind': 'qualification_blocked',
                                     'build_id': build_id, 'stage': attempt.get('stage', 'validation')})

    def _record_testable_delivery(self, build_id: str, archive_sha256: str,
                                  unverified_checks: list[str]) -> dict:
        """Track actual delivery separately from observed runtime qualification."""
        reasons = clean_list(unverified_checks, limit=16)
        if not reasons or any(not reason.strip() for reason in reasons):
            raise IterationError('Record the actual unverified checks.', 'unverified_reason_required')
        with self.store.transaction() as s:
            b = s.get('build', build_id)
            raw = self._archive(s, b)
            if sha(raw) != archive_sha256:
                raise IterationError('Delivery archive changed before recording.', 'artifact_corrupt')
            if b.get('checks', {}).get('status') != 'passed':
                raise IterationError('Static checks must pass before delivery.', 'checks_failed')
            if b.get('validation_summary', {}).get('current_host_failures', 0):
                raise IterationError('Known application failures must be repaired.', 'runtime_checks_failed')
            if b.get('last_qualification_failure') and not b.get('release'):
                raise IterationError('Failed qualification requires review before delivery.', 'qualification_failure_requires_review')
            delivery = {'mode': 'windows-testable', 'status': 'delivered_for_windows_test',
                        'archive_sha256': archive_sha256, 'archive_bytes': len(raw),
                        'runtime_qualified': bool(b.get('release')), 'windows_bat_tested': False,
                        'unverified_checks': reasons, 'created_utc': now()}
            b['delivery'] = delivery
            s.put('build', b)
            s.event(b['project_id'], {'at': delivery['created_utc'], 'kind': 'windows_testable_delivered',
                                     'build_id': build_id, 'archive_sha256': archive_sha256,
                                     'runtime_qualified': delivery['runtime_qualified'],
                                     'unverified_checks': reasons})
            return delivery

    def _commit_qualification(self, build_id: str, candidate_sha: str, raw: bytes, evidence: dict) -> dict:
        # Internal host-local handoff only. MCP never executes or accepts a model-written
        # receipt. deliver.py produces evidence directly from its own subprocess runs.
        files = read_archive(raw)
        audit_archive(raw)
        validate_receipt(files)
        if evidence.get('status') != 'passed' or evidence.get('archive_sha256') != sha(raw):
            raise IterationError('Exact final archive is not qualified.', 'release_not_qualified')
        with self.store.transaction() as s:
            b = s.get('build', build_id)
            p = s.get('project', b['project_id'])
            if b.get('release') or b.get('delivery') or b['archive_sha256'] != candidate_sha:
                raise IterationError('Candidate changed or has already been delivered.', 'release_conflict')
            if p.get('accepted') == build_id or any(t['project_id'] == p['id'] and t['status'] == 'active' for t in s.all('task')):
                raise IterationError('Cannot qualify a build already accepted or branched into active work.', 'release_conflict')
            qid = 'q_' + sha(raw)[:32]
            release = {'id': qid, 'archive_sha256': sha(raw), 'archive_bytes': len(raw),
                       'manifest_sha256': sha(files[INDEX]), 'status': 'passed',
                       'candidate_sha256': candidate_sha, 'evidence': evidence}
            # Keep the original candidate ZIP and file namespace immutable.
            target = s.exports / (qid+'.zip')
            target.write_bytes(raw)
            for path, data in files.items():
                s.set_file(qid, path, data)
            s.put('qualification', release)
            b['release'] = release
            b['validation_summary']['release_gate'] = 'passed_exact_archive_execution'
            s.put('build', b)
            s.event(p['id'], {'at': now(), 'kind': 'release_qualified', 'build_id': build_id,
                             'archive_sha256': sha(raw), 'candidate_retained': True})
            return release

    def package(self, task_id: str, expected_task_revision: int, summary: str, completed: list[str],
                remaining: list[str], what_to_test: list[str], architecture: str = '', brainstorm: str = '',
                quarantined: str = '', risks: str = '', next_prompt: str = '') -> dict:
        meta = {k: clean_text(v) for k, v in {'summary': summary, 'architecture': architecture,
                'brainstorm': brainstorm, 'quarantined': quarantined, 'risks': risks, 'next_prompt': next_prompt}.items()}
        meta.update({'completed': clean_list(completed), 'remaining': clean_list(remaining), 'what_to_test': clean_list(what_to_test)})
        if not meta['summary'] or not meta['what_to_test']:
            raise IterationError('Provide a summary and at least one first-test instruction.')
        export_path = None
        try:
            with self.store.transaction() as s:
                t, p = self._active(s, task_id, expected_task_revision)
                checks = self._checks(s, t)
                if t.get('base_build'):
                    prior = s.get('build', t['base_build'])
                    for field in ('architecture','brainstorm','quarantined','risks','next_prompt'):
                        if not meta[field]:
                            meta[field] = prior.get(field, '')
                reports = [{**r, 'applies_to_current_source': r['source_digest'] == checks['source_digest']} for r in t['reports']]
                validation = {'static_checks': checks['status'],
                              'current_host_passes': sum(r['applies_to_current_source'] and r['outcome']=='passed' for r in reports),
                              'current_host_failures': sum(r['applies_to_current_source'] and r['outcome']=='failed' for r in reports),
                              'stale_reports': sum(not r['applies_to_current_source'] for r in reports),
                              'runtime_independently_observed': False, 'release_gate': 'pending_exact_archive_execution'}
                if checks['status'] != 'passed':
                    raise IterationError('Static checks failed. Call iteration_check and fix the reported issues before packaging.', 'checks_failed')
                if validation['current_host_failures']:
                    raise IterationError('Known failing tests apply to this source. Repair and rerun before packaging.', 'runtime_checks_failed')
                number = 1 + len([b for b in s.all('build') if b['project_id'] == p['id']])
                bid = ident('b')
                b = {'id': bid, 'project_id': p['id'], 'number': number, 'created': now(),
                     'task_id': task_id, 'parent_build_id': t['base_build'], 'status': 'candidate',
                     'checks': checks, 'reports': reports, 'validation_summary': validation, **meta}
                payload = s.file_map(task_id)
                payload['run.bat'] = LAUNCHER.encode('utf-8')
                payload[RUNNER] = (Path(__file__).parent/'runner_template.py').read_bytes()
                payload[LIFECYCLE] = (Path(__file__).parent/'lifecycle_template.py').read_bytes()
                if t.get('release_plan'):
                    verify_plan_files(t['release_plan'], payload)
                    payload[PLAN] = json.dumps(t['release_plan'], indent=2).encode()
                b['returned_runtime_reports'] = [{k: v for k, v in r.items() if k != 'console'} for r in s.all('logreport') if r['project_id'] == p['id'] and r['build_id'] == t.get('base_build')]
                p['revision'] += 1
                p['latest'] = bid
                event = {'at': now(), 'kind': 'candidate_packaged', 'build_id': bid, 'task_id': task_id,
                         'source_digest': checks['source_digest'], 'status': 'candidate'}
                events = s.events(p['id']) + [event]
                payload.update(make_records(p, t, b, payload, events))
                # Include record hashes without circular self-hashing. A00 hashes all other files.
                a00 = json.loads(payload[INDEX])
                a00['file_sha256'] = {x: sha(d) for x, d in sorted(payload.items()) if x != INDEX}
                payload[INDEX] = json.dumps(a00, indent=2, ensure_ascii=False).encode()
                check_delivery(payload)
                for path, data in payload.items():
                    s.set_file(bid, path, data)
                out = io.BytesIO()
                with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as z:
                    for path, data in sorted(payload.items()):
                        zi = zipfile.ZipInfo(path, time.gmtime()[:6]); zi.compress_type = zipfile.ZIP_DEFLATED
                        zi.external_attr = 0o100644 << 16
                        z.writestr(zi, data)
                raw = out.getvalue()
                b['delivery_audit'] = audit_archive(raw)
                slug = re.sub(r'[^A-Za-z0-9_-]+', '_', p['name']).strip('_')[:60] or 'Program'
                b.update({'archive_name': f'{slug}_I{number:03d}_{bid[2:8]}.zip', 'archive_sha256': sha(raw), 'archive_bytes': len(raw)})
                export_path = s.exports / (bid + '.zip')
                temporary = export_path.with_suffix('.tmp')
                temporary.write_bytes(raw)
                temporary.replace(export_path)
                t['status'] = 'packaged'; t['build_id'] = bid
                s.put('task', t); s.put('project', p); s.put('build', b); s.event(p['id'], event)
                return b
        except BaseException:
            if export_path and export_path.exists():
                export_path.unlink(missing_ok=True)
            raise

    def artifact(self, project_id: str, build_id: str, offset: int = 0, max_bytes: int = 196608) -> dict:
        if type(offset) is not int or offset < 0 or type(max_bytes) is not int or not 1 <= max_bytes <= 524288:
            raise IterationError('Invalid artifact range.')
        with self.store.transaction() as s:
            b = s.get('build', build_id)
            if b['project_id'] != project_id:
                raise IterationError('Build does not belong to this project.')
            raw = self._archive(s, b)
            part = raw[offset:offset+max_bytes]
            return {'build_id': build_id, 'file_name': b['archive_name'], 'sha256': sha(raw),
                    'total_bytes': len(raw), 'offset': offset, 'content_base64': base64.b64encode(part).decode(),
                    'next_offset': offset+len(part) if offset+len(part)<len(raw) else None,
                    'release_status': b.get('release', {}).get('status') or b.get('delivery', {}).get('status') or ('blocked' if b.get('last_qualification_failure') else 'candidate_only'),
                    'delivery_status': b.get('delivery', {}).get('status', 'not_delivered'),
                    'runtime_qualified': bool(b.get('release')),
                    'instruction': 'Use deliver.py --mode windows-testable to export an audited original-engine ZIP with explicit unverified checks. The qualified mode additionally requires actual runtime qualification. Never claim unperformed tests passed.'}

    def _archive(self, s: Store, build: dict) -> bytes:
        selected = build.get('release', build)
        path = s.exports / (selected['id'] + '.zip')
        if not path.is_file():
            raise IterationError('Archive file is missing. Source snapshot is preserved; export recovery is needed.', 'artifact_missing')
        raw = path.read_bytes()
        if sha(raw) != selected['archive_sha256']:
            raise IterationError('Archive checksum mismatch; refusing to return corrupted data.', 'artifact_corrupt')
        return raw

    def archive_bytes(self, build_id: str) -> tuple[dict, bytes]:
        with self.store.transaction() as s:
            b = s.get('build', build_id)
            raw = self._archive(s, b)
            return {**b, 'archive_sha256': sha(raw), 'archive_bytes': len(raw)}, raw

    def accept(self, project_id: str, build_id: str, expected_revision: int, feedback: str, windows_tested: bool = False, authorization_source: str = "local_user_report") -> dict:
        """Local authenticated acceptance; chat relay uses the explicit-authorization wrapper."""
        with self.store.transaction() as s:
            p = s.get('project', project_id); self._revision(p, expected_revision)
            b = s.get('build', build_id)
            if b['project_id'] != project_id:
                raise IterationError('Build belongs to another project.')
            if any(t['project_id'] == project_id and t['status'] == 'active' for t in s.all('task')):
                raise IterationError('Finish or cancel the active iteration before changing the accepted baseline.')
            p['accepted'] = build_id; p['revision'] += 1
            s.put('project', p)
            event = {'at': now(), 'kind': 'user_accepted', 'build_id': build_id, 'feedback': clean_text(feedback),
                     'windows_tested': bool(windows_tested), 'trust': authorization_source, 'archive_unchanged': True}
            s.event(project_id, event)
            return {'project': p, 'acceptance': event}

    def cancel(self, task_id: str) -> dict:
        with self.store.transaction() as s:
            t = s.get('task', task_id)
            if t['status'] != 'active':
                raise IterationError('Task is not active.')
            t['status'] = 'cancelled'; s.put('task', t)
            s.event(t['project_id'], {'at': now(), 'kind': 'iteration_cancelled', 'task_id': task_id, 'sources_retained': True})
            return t

    def continuation_packet(self, project_id: str) -> dict:
        with self.store.transaction() as s:
            p = s.get('project', project_id)
            b = s.get('build', p['latest']) if p['latest'] else None
            return {'project_id': project_id, 'prompt': continuation(p, b), 'chat_created': False,
                    'reasoning_changed': False, 'instructions': 'Copy this into a new chat with Build_ enabled, or supply the matching ZIP.'}

    def import_zip(self, name: str, raw: bytes) -> dict:
        """Read v1/v2 or recognized legacy records; retain exact application/data bytes."""
        files = read_archive(raw)
        files.pop('LogReport.zip', None)  # A report is not application source.
        manifest, manifest_path = identity(files, verify=True)
        source, notes = split_input(files)
        preserved = retain(notes, manifest)
        for path, data in {**source, **notes}.items():
            if SECRET.search(data.decode('utf-8', errors='ignore')):
                raise IterationError('Possible credential in imported files.', 'possible_secret')
        p = self.create_project(name or manifest.get('project_name', 'Imported program'),
                                'Imported archive; external claims require review.',
                                manifest.get('constraints', []), manifest.get('locked_paths', []),
                                console_mode=manifest.get('runtime', {}).get('console_mode', 'quiet'))
        t = self.begin(p['id'], 0, 'Import and review the supplied program without changing its application source.',
                       not_changed=['Application source, assets, and included saved data'],
                       acceptance_criteria=['Inspect source and test locally before accepting.'])
        with self.store.transaction() as st:
            for path, data in source.items():
                st.set_file(t['id'], path, data)
            t['revision'] = 1
            if preserved:
                t['preserved_files'] = preserved
            t['imported_archive_sha256'] = sha(raw)
            st.put('task', t)
            st.event(p['id'], {'at': now(), 'kind': 'archive_imported', 'input_sha256': sha(raw),
                              'original_project_id': manifest.get('project_id'), 'source_claims_verified': False,
                              'source_bytes_preserved': True, 'included_data_bytes_preserved': True,
                              'retained_record_count': len(preserved)})
        def note(role: str, fallback: str) -> str:
            return record(files, role).decode('utf-8', errors='replace')[:16000] or fallback
        try:
            b = self.package(t['id'], 1, 'Recovered the program and normalized its record layout without executing or modifying application source.',
                     ['Original source, assets and included data retained', 'Launcher and PROGRAM/readme.md regenerated', 'Existing reference bytes preserved in coded records'],
                     ['Review recovered notes', 'Test on Windows before acceptance'], ['Run the extracted run.bat after reviewing its source.'],
                     architecture=note('components', 'Inspect the imported source tree.'),
                     brainstorm=note('options', 'Review existing intent before further changes.'),
                     risks='Imported notes and previous validation claims remain untrusted reports.',
                     next_prompt='Review this exact candidate, its original intent, and feedback before another change.')
        except IterationError as exc:
            return {'project': p, 'task': t, 'packaged': False, 'checks': self.check(t['id']),
                    'message': 'Imported into an active task; packaging did not pass.', 'error': str(exc)}
        if manifest.get('project_id') and manifest.get('build_id') and manifest_path:
            with self.store.transaction() as st:
                stored = st.get('build', b['id'])
                stored['imported_archive_sha256'] = sha(raw)
                stored['imported_identity'] = {'project_id': manifest['project_id'], 'build_id': manifest['build_id'],
                                              'manifest_sha256': sha(files[manifest_path])}
                st.put('build', stored)
                b = stored
        return {'project': p, 'build': b, 'packaged': True}


    def accept_from_chat(self, project_id: str, build_id: str, expected_revision: int,
                         user_confirmation: str, windows_tested: bool = False) -> dict:
        confirmation = clean_text(user_confirmation, 2000)
        if len(confirmation) < 3:
            raise IterationError('Quote the user authorization for this exact build; logs alone are not approval.', 'confirmation_required')
        result = self.accept(project_id, build_id, expected_revision, confirmation, windows_tested, "host_relay_of_user_authorization")
        with self.store.transaction() as st:
            st.event(project_id, {'at': now(), 'kind': 'acceptance_authorization_relayed',
                'build_id': build_id, 'user_confirmation': confirmation,
                'trust': 'host_relay_of_user_authorization_not_independently_verified'})
        result['authorization_source'] = 'chat_user_authorization_relayed_by_host'
        result['reply_footer'] = REMINDER
        return result

    def cancel_from_chat(self, task_id: str, user_confirmation: str) -> dict:
        confirmation = clean_text(user_confirmation, 2000)
        if len(confirmation) < 3:
            raise IterationError('Explicit user authorization is required to cancel a task.', 'confirmation_required')
        result = self.cancel(task_id)
        with self.store.transaction() as st:
            st.event(result['project_id'], {'at': now(), 'kind': 'cancel_authorized_in_chat',
                'task_id': task_id, 'user_confirmation': confirmation})
        return result

    def ingest_log_report(self, report_base64: str) -> dict:
        if not isinstance(report_base64, str) or len(report_base64) > (MAX_REPORT_BYTES * 4 // 3 + 8):
            raise IterationError('Report exceeds the bounded log-upload limit.', 'invalid_log_report')
        try:
            raw = base64.b64decode(report_base64, validate=True)
        except (ValueError, TypeError) as exc:
            raise IterationError('Invalid report encoding.', 'invalid_log_report') from exc
        report = parse_log_report(raw)
        with self.store.transaction() as st:
            builds = st.all('build')
            exact = next((b for b in builds if b['id'] == report['build_id'] and b['project_id'] == report['project_id']), None)
            if exact:
                manifest = record(self._snapshot_files(st, exact['id']), 'index')
                if sha(manifest) != report['manifest_sha256']:
                    raise IterationError('The report manifest does not match the identified build.', 'log_build_mismatch')
            else:
                key = {k: report[k] for k in ('project_id','build_id','manifest_sha256')}
                exact = next((b for b in builds if b.get('imported_identity') == key), None)
                if not exact:
                    raise IterationError('The matching build is not registered. Import its program ZIP before attaching this report.', 'unknown_log_build')
                report['reported_original_identity'] = key
                report['project_id'] = exact['project_id']; report['build_id'] = exact['id']
                report['applies_to_imported_original_not_regenerated_launcher'] = True
            report['manifest_matches_known_build'] = True
            declared_entry = report.get('entrypoint_sha256')
            known_entry = self._snapshot_files(st, exact['id']).get('PROGRAM/main.py', b'')
            report['reported_entrypoint_matches_known_build'] = (declared_entry == sha(known_entry)) if declared_entry else None
            report['received_utc'] = now()
            # Duplicate uploads return the same record. Running snapshots share a run ID;
            # preserve each distinct snapshot instead of overwriting a final report.
            original_id = report['id']
            report['run_id'] = original_id
            report['id'] = 'lr_' + report['report_sha256'][:32]
            existing = next((r for r in st.all('logreport') if r['id'] == report['id']), None)
            if not existing:
                st.put('logreport', report)
                st.event(report['project_id'], {'at': now(), 'kind': 'runtime_log_received',
                    'build_id': report['build_id'], 'report_id': report['id'], 'state': report['state'],
                    'trust': report['trust'], 'user_acceptance_inferred': False})
            current = existing or report
            return {'report': current, 'duplicate': existing is not None,
                    'accepted_automatically': False,
                    'review_direction': (
                        'Investigate and fix functional failures in this build within the existing approved scope.'
                        if any(o['failed'] for o in current.get('functional_observations', [])) else
                        'Functional observations recorded. Advance the next already-approved unfinished item, if any; do not invent a feature.'
                        if current.get('functional_observations', []) else
                        'Report has no functional observations. Do not assert unmeasured behavior. Retain any user-reported successful behavior as separate evidence; add functional instrumentation on the next authorized iteration.'),
                    'reply_footer': REMINDER}

    def import_from_chat(self, name: str, archive_base64: str) -> dict:
        if len(archive_base64) > 24 * 1024 * 1024:
            raise IterationError('This chat transfer supports ZIPs up to 18 MiB. Use the host-local workflow for larger files.')
        try:
            raw = base64.b64decode(archive_base64, validate=True)
        except ValueError as exc:
            raise IterationError('Invalid archive encoding.') from exc
        return self.import_zip(name, raw)
