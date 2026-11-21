"""Small runtime evidence protocol. Copied verbatim to Automation/RT42.py.

Use ready() only after real initialization. Use fail('stable-reason-code') for
blocking handled errors, and with case(id, category): for actual test assertions.
No customer content belongs in IDs or codes. observe() adds bounded status-only
functional evidence to LogReport.zip. It is app-authored evidence, not attestation.
"""
from __future__ import annotations
from contextlib import contextmanager
import json
import os
from pathlib import Path
import re
import threading

PROTOCOL = 'iteration.lifecycle/1'
MAX_CASES = 128
MAX_OBSERVATIONS = 32
MAX_OBSERVATION_COUNT = 65535
_ID = re.compile(r'[a-z][a-z0-9_.-]{0,63}')
_lock = threading.RLock()
_path: Path | None = None
_nonce = ''
_state: dict = {}
_owner: int | None = None


def _code(value: str) -> str:
    if not isinstance(value, str) or not _ID.fullmatch(value):
        raise ValueError('Use a short stable lowercase code, not customer data.')
    return value


def validate(value: dict, nonce: str | None = None) -> dict:
    """Strict bounded snapshot parser, shared with the supervisor and log reader."""
    if not isinstance(value, dict) or value.get('protocol') != PROTOCOL:
        raise ValueError('Unsupported lifecycle protocol.')
    if nonce is not None and value.get('nonce') != nonce:
        raise ValueError('Lifecycle belongs to another run.')
    if type(value.get('ready')) is not bool or type(value.get('failed')) is not bool:
        raise ValueError('Invalid lifecycle state.')
    if type(value.get('sequence')) is not int or not 0 <= value['sequence'] <= 100000:
        raise ValueError('Invalid lifecycle sequence.')
    codes = value.get('failure_codes')
    checks = value.get('checks')
    observations = value.get('observations', [])  # Existing lifecycle/1 reports remain valid.
    if not isinstance(codes, list) or len(codes) > 16 or not isinstance(checks, list) or len(checks) > MAX_CASES:
        raise ValueError('Oversized lifecycle snapshot.')
    for code in codes:
        _code(code)
    seen = set()
    safe_checks = []
    for check in checks:
        if not isinstance(check, dict):
            raise ValueError('Invalid case record.')
        key, category = _code(check.get('id')), _code(check.get('category'))
        if key in seen or type(check.get('passed')) is not bool:
            raise ValueError('Duplicate or invalid case record.')
        seen.add(key)
        safe_checks.append({'id': key, 'category': category, 'passed': check['passed']})
    if not isinstance(observations, list) or len(observations) > MAX_OBSERVATIONS:
        raise ValueError('Oversized functional observation summary.')
    safe_observations = []
    observed_ids = set()
    for item in observations:
        if not isinstance(item, dict) or set(item) != {'id', 'category', 'ok', 'failed'}:
            raise ValueError('Invalid functional observation record.')
        key, category = _code(item['id']), _code(item['category'])
        ok, failed = item['ok'], item['failed']
        if key in observed_ids or type(ok) is not int or type(failed) is not int:
            raise ValueError('Duplicate or invalid functional observation record.')
        if not 0 <= ok <= MAX_OBSERVATION_COUNT or not 0 <= failed <= MAX_OBSERVATION_COUNT or not (ok or failed):
            raise ValueError('Invalid functional observation counters.')
        observed_ids.add(key)
        safe_observations.append({'id': key, 'category': category, 'ok': ok, 'failed': failed})
    if (codes or any(not c['passed'] for c in safe_checks)) and not value['failed']:
        raise ValueError('Inconsistent failure state.')
    return {'protocol': PROTOCOL, 'ready': value['ready'], 'failed': value['failed'],
            'sequence': value['sequence'], 'failure_codes': codes[:], 'checks': safe_checks,
            'observations': safe_observations}


def _start(path: Path, nonce: str) -> None:
    global _path, _nonce, _state, _owner
    with _lock:
        _path, _nonce, _owner = path, nonce, os.getpid()
        _state = {'protocol': PROTOCOL, 'ready': False, 'failed': False,
                  'sequence': 0, 'failure_codes': [], 'checks': [], 'observations': []}
        _save()


def _save() -> None:
    if _path is None or _owner != os.getpid():
        return
    value = {**_state, 'nonce': _nonce}
    temporary = _path.with_suffix('.tmp')
    try:
        temporary.write_text(json.dumps(value, separators=(',', ':')), encoding='utf-8')
        os.replace(temporary, _path)
    finally:
        temporary.unlink(missing_ok=True)


def ready() -> None:
    """Record actual usable startup. It never cancels an earlier failure."""
    with _lock:
        if _path is None or _owner != os.getpid():
            return  # Direct, unsupervised main.py execution has no diagnostic channel.
        if _state['ready']:
            return
        _state['ready'] = True
        _state['sequence'] += 1
        _save()


def fail(code: str) -> None:
    """Record a terminal handled failure even if the app later returns zero.

    Caller should close safely and return nonzero. The supervisor enforces a
    failure regardless. Log technical details separately, never in this code.
    """
    code = _code(code)
    with _lock:
        if _path is None or _owner != os.getpid():
            return
        _state['failed'] = True
        if code not in _state['failure_codes'] and len(_state['failure_codes']) < 16:
            _state['failure_codes'].append(code)
        _state['sequence'] += 1
        _save()


@contextmanager
def case(case_id: str, category: str):
    """Wrap genuine assertions. A caught failure remains a failed test record."""
    case_id, category = _code(case_id), _code(category)
    with _lock:
        if _path is not None and _owner == os.getpid():
            if len(_state['checks']) >= MAX_CASES or any(c['id'] == case_id for c in _state['checks']):
                fail('invalid-test-record')
                raise ValueError('Case IDs must be unique and bounded in each run.')
    passed = False
    try:
        yield
        passed = True
    finally:
        with _lock:
            if _path is not None and _owner == os.getpid():
                # Check again on exit, including parallel/nested test bodies.
                if len(_state['checks']) >= MAX_CASES or any(c['id'] == case_id for c in _state['checks']):
                    fail('invalid-test-record')
                    raise ValueError('Duplicate case ID.')
                _state['checks'].append({'id': case_id, 'category': category, 'passed': passed})
                if not passed:
                    _state['failed'] = True
                _state['sequence'] += 1
                _save()


def observe(observation_id: str, category: str, passed: bool) -> None:
    """Log a bounded, status-only user-session observation.

    Call *after* checking a real condition (e.g., read-back equals saved state or
    restored data matches the displayed widget), NOT merely after calling a
    function. IDs/categories are fixed developer-authored codes; no user values,
    counts, paths, screenshots or serialized records are transmitted. Repeated
    events aggregate counts, and failures remain visible even after recovery.
    Ordinary observed failures are nonfatal; blocking errors still use fail().
    """
    observation_id, category = _code(observation_id), _code(category)
    if type(passed) is not bool:
        raise TypeError('Observation status must be a boolean.')
    with _lock:
        if _path is None or _owner != os.getpid():
            return
        matching = next((item for item in _state['observations'] if item['id'] == observation_id), None)
        if matching and matching['category'] != category:
            raise ValueError('Observation category must remain stable for an ID.')
        if matching is None:
            if len(_state['observations']) >= MAX_OBSERVATIONS:
                return  # Bounded diagnostics must not break the customer's program.
            matching = {'id': observation_id, 'category': category, 'ok': 0, 'failed': 0}
            _state['observations'].append(matching)
        field = 'ok' if passed else 'failed'
        if matching[field] >= MAX_OBSERVATION_COUNT:
            return
        if _state['sequence'] >= 100000:
            return  # The bounded lifecycle channel must never exceed its protocol sequence limit.
        matching[field] += 1
        _state['sequence'] += 1
        _save()
