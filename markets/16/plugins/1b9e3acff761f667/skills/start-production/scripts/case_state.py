#!/usr/bin/env python3
"""Local revision/dependency bookkeeping; does not validate medical meaning."""
import argparse
import copy
import json
import os
from pathlib import Path
import tempfile


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def positive(value):
    return type(value) is int and value > 0


def validate(state):
    if state.get('schema_version') != 1 or not positive(state.get('revision')):
        raise ValueError('Invalid schema_version or revision')
    if not state.get('case_id'):
        raise ValueError('case_id is required')
    profile = state.get('profile', {})
    if not profile.get('doctor_id') or not positive(profile.get('version')):
        raise ValueError('Profile doctor_id and positive version are required')
    claims, artifacts = state['claims'], state['artifacts']
    for key, claim in claims.items():
        if not key or not positive(claim.get('version')) or not claim.get('text'):
            raise ValueError('Invalid claim: ' + key)
        if claim.get('verification') not in ('verified', 'partial', 'unverified'):
            raise ValueError('Invalid claim verification: ' + key)
        if claim['verification'] == 'verified' and not claim.get('source_refs'):
            raise ValueError('Verified claims need source_refs: ' + key)
    for key, artifact in artifacts.items():
        if not key or not positive(artifact.get('version')):
            raise ValueError('Invalid artifact: ' + key)
        if artifact.get('status') not in ('draft', 'complete', 'needs_update'):
            raise ValueError('Invalid status: ' + key)
        if not artifact.get('location'):
            raise ValueError('Artifact location is required: ' + key)
        for ref, version in artifact['dependencies'].items():
            kind, sep, ident = ref.partition(':')
            pool = claims if kind == 'claim' else artifacts if kind == 'artifact' else {'doctor': profile} if kind == 'profile' else {}
            if not sep or ident not in pool or not positive(version):
                raise ValueError('Unknown dependency or invalid version: ' + ref)
    visited, active = set(), set()
    def visit(key):
        if key in active:
            raise ValueError('Dependency cycle: ' + key)
        if key in visited:
            return
        active.add(key)
        for ref in artifacts[key]['dependencies']:
            if ref.startswith('artifact:'):
                visit(ref.split(':', 1)[1])
        active.remove(key)
        visited.add(key)
    for key in artifacts:
        visit(key)
    return state


def refresh(state):
    validate(state)
    for _ in range(len(state['artifacts']) + 1):
        changed = False
        for artifact in state['artifacts'].values():
            reasons = []
            for ref, version in artifact['dependencies'].items():
                kind, ident = ref.split(':', 1)
                parent = state['profile'] if kind == 'profile' else state['claims' if kind == 'claim' else 'artifacts'][ident]
                if version != parent['version']:
                    reasons.append(ref + ':version_changed')
                if kind == 'claim' and parent['verification'] != 'verified':
                    reasons.append(ref + ':evidence_pending')
                if kind == 'artifact' and parent['status'] != 'complete':
                    reasons.append(ref + ':upstream_not_complete')
            artifact['issues'] = reasons
            if reasons and artifact['status'] == 'complete':
                artifact['status'] = 'needs_update'
                changed = True
        if not changed:
            break
    return state


def new_case(case_id, doctor_id, profile_version, source=''):
    return validate(dict(schema_version=1, revision=1, case_id=case_id,
                         profile=dict(doctor_id=doctor_id, version=profile_version, source=source),
                         claims={}, artifacts={}))


def put_claim(state, payload):
    result = copy.deepcopy(state)
    value = copy.deepcopy(payload)
    key = value.pop('claim_id')
    value['version'] = result['claims'].get(key, {}).get('version', 0) + 1
    result['claims'][key] = value
    return refresh(result)


def put_artifact(state, payload):
    result = copy.deepcopy(state)
    value = copy.deepcopy(payload)
    key = value.pop('artifact_id')
    if value.get('status') not in ('draft', 'complete'):
        raise ValueError('Register as draft or complete; stale status is computed')
    value['version'] = result['artifacts'].get(key, {}).get('version', 0) + 1
    result['artifacts'][key] = value
    return refresh(result)


def put_profile(state, payload):
    if payload.get('doctor_id') != state['profile']['doctor_id']:
        raise ValueError('Changing doctor requires a separate case')
    if not positive(payload.get('version')) or payload['version'] <= state['profile']['version']:
        raise ValueError('Profile update requires a newer version')
    result = copy.deepcopy(state)
    result['profile'] = copy.deepcopy(payload)
    return refresh(result)


def verify_local_artifacts(state, base):
    for key, artifact in state['artifacts'].items():
        if artifact['status'] != 'complete':
            continue
        location = artifact['location']
        if location.startswith(('https://', 'http://', 'chat:')):
            continue  # Remote/inline content must be checked by the calling workflow.
        path = Path(location)
        if not path.is_absolute():
            path = Path(base) / path
        if not path.is_file():
            raise ValueError('Completed local artifact does not exist: ' + key)


def commit(path, state, expected):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = path.with_name(path.name + '.lock')
    fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    temp = None
    try:
        os.close(fd)
        current = read(path) if path.exists() else None
        if expected is None:
            if current is not None:
                raise ValueError('Case already exists')
        elif current is None or current.get('revision') != expected:
            raise ValueError('Case changed; read latest revision before saving')
        value = copy.deepcopy(state)
        value['revision'] = 1 if expected is None else expected + 1
        refresh(value)
        verify_local_artifacts(value, path.parent)
        with tempfile.NamedTemporaryFile('w', encoding='utf-8', dir=path.parent,
                                         prefix='.' + path.name, delete=False) as out:
            temp = Path(out.name)
            json.dump(value, out, ensure_ascii=False, indent=2)
            out.write('\n')
        os.replace(temp, path)
        if read(path) != value:
            raise ValueError('Read-back mismatch')
        return value
    finally:
        if temp and temp.exists():
            temp.unlink()
        lock.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    init = sub.add_parser('init')
    init.add_argument('file')
    init.add_argument('--case-id', required=True)
    init.add_argument('--doctor-id', required=True)
    init.add_argument('--profile-version', required=True, type=int)
    init.add_argument('--profile-source', default='')
    for name in ('claim', 'artifact', 'profile'):
        cmd = sub.add_parser(name)
        cmd.add_argument('file')
        cmd.add_argument('payload', help='Path to JSON payload')
        cmd.add_argument('--expected-revision', required=True, type=int)
    for name in ('validate', 'status'):
        cmd = sub.add_parser(name)
        cmd.add_argument('file')
    args = parser.parse_args()
    try:
        if args.command == 'init':
            state = commit(args.file, new_case(args.case_id, args.doctor_id,
                           args.profile_version, args.profile_source), None)
        else:
            state = read(args.file)
            validate(state)
            if args.command in ('claim', 'artifact', 'profile'):
                if state['revision'] != args.expected_revision:
                    raise ValueError('Case changed; read latest revision')
                fn = {'claim': put_claim, 'artifact': put_artifact, 'profile': put_profile}[args.command]
                state = commit(args.file, fn(state, read(args.payload)), args.expected_revision)
            else:
                verify_local_artifacts(state, Path(args.file).parent)
                recalculated = refresh(copy.deepcopy(state))
                if recalculated != state:
                    raise ValueError('Stored status is inconsistent; reconcile before use')
        print(json.dumps(state, ensure_ascii=False, indent=2))
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    main()
