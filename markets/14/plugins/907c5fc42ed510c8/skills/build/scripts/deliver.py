"""Export ONE original-engine ZIP with an explicit validation boundary.

windows-testable performs static, template and archive checks without running the
application. qualified retains the observed execution and portable-receipt path.
Neither mode claims native Windows testing. This is not a security sandbox.
"""
from __future__ import annotations
import argparse
import ast
import io
import json
import os
from pathlib import Path
import tempfile
import time
import uuid
import zipfile

from iteration.engine import Engine
from iteration.layout import INDEX, RUNNER, audit_archive
from iteration.records import LAUNCHER
from iteration.release_contract import (LIFECYCLE, PLAN, RECEIPT, RECEIPT_SCHEMA, payload_digest, validate_receipt)
from iteration.safety import IterationError, read_archive, sha
from release_check import qualify


def _check_output(output: Path) -> None:
    if output.exists() or output.is_symlink():
        raise IterationError('Choose a new output filename; existing user files are never overwritten.', 'output_exists')
    if any(p.is_symlink() for p in output.parents):
        raise IterationError('Refusing symlink output parent.', 'unsafe_output')


def _write_exact_output(raw: bytes, expected_sha: str, output: Path) -> bytes:
    """Create a new output and verify its exact bytes; never overwrite a file."""
    _check_output(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name('.'+output.name+'.tmp-'+uuid.uuid4().hex)
    owned_output = False
    try:
        temporary.write_bytes(raw)
        if sha(temporary.read_bytes()) != expected_sha:
            raise IterationError('Output differs from the inspected archive.', 'artifact_corrupt')
        with output.open('xb') as handle:
            owned_output = True
            handle.write(temporary.read_bytes())
        actual = output.read_bytes()
        if sha(actual) != expected_sha:
            raise IterationError('Post-export verification failed; do not attach output.', 'artifact_corrupt')
        return actual
    except BaseException:
        if owned_output:
            output.unlink(missing_ok=True)
        raise
    finally:
        temporary.unlink(missing_ok=True)


def deliver_windows_testable(engine: Engine, build_id: str, output: Path,
                             unverified_reasons: list[str] | None = None) -> dict:
    """Deliver an intact engine archive without inventing runtime qualification."""
    _check_output(output)
    if (not isinstance(unverified_reasons, list) or not 1 <= len(unverified_reasons) <= 16
            or any(not isinstance(reason, str) or not reason.strip() or len(reason) > 2000
                   for reason in unverified_reasons)):
        raise IterationError('Record at least one actual unverified check with --unverified-reason.', 'unverified_reason_required')
    reasons = list(dict.fromkeys(reason.strip() for reason in unverified_reasons))
    build, raw = engine.archive_bytes(build_id)
    if build.get('checks', {}).get('status') != 'passed':
        raise IterationError('Static checks must pass before delivery.', 'checks_failed')
    if build.get('validation_summary', {}).get('current_host_failures', 0):
        raise IterationError('Known application test failures require repair before delivery.', 'runtime_checks_failed')
    qualified = bool(build.get('release'))
    if build.get('last_qualification_failure') and not qualified:
        raise IterationError('A failed qualification cannot be relabelled as an unperformed check. Review and address its evidence before a new delivery.', 'qualification_failure_requires_review')
    audit = audit_archive(raw)
    files = read_archive(raw)
    for path, data in files.items():
        if path.lower().endswith('.py'):
            ast.parse(data, filename=path, feature_version=(3, 10))
            compile(data, path, 'exec', dont_inherit=True)
    templates = {
        'run.bat': LAUNCHER.encode('utf-8'),
        RUNNER: (Path(__file__).parent/'iteration/runner_template.py').read_bytes(),
        LIFECYCLE: (Path(__file__).parent/'iteration/lifecycle_template.py').read_bytes(),
    }
    for path, expected in templates.items():
        if files.get(path) != expected:
            raise IterationError('Use the original bundled runtime file unchanged: '+path, 'runtime_template_mismatch')
    if qualified:
        validate_receipt(files)
        evidence = build['release'].get('evidence', {})
        if evidence.get('status') != 'passed' or evidence.get('archive_sha256') != sha(raw):
            raise IterationError('Stored qualification is stale.', 'receipt_mismatch')
    elif RECEIPT in files:
        raise IterationError('An unqualified delivery must not contain a qualification receipt.', 'unexpected_qualification_receipt')
    actual = _write_exact_output(raw, sha(raw), output)
    try:
        delivery = engine._record_testable_delivery(build_id, sha(actual), reasons)
    except BaseException:
        output.unlink(missing_ok=True)
        raise
    return {
        'status': 'delivered_for_windows_test', 'path': str(output.resolve()),
        'bytes': len(actual), 'archive_sha256': sha(actual), 'build_id': build_id,
        'output_written': True, 'runtime_qualified': qualified,
        'qualification_stored_in_host_state': qualified,
        'portable_receipt': RECEIPT if qualified else None,
        'windows_bat_tested': False, 'unverified_checks': reasons,
        'static_checks': 'passed', 'archive_audit': audit, 'delivery': delivery,
        'instruction': 'Attach this exact original-engine ZIP for Windows testing. State the listed unverified checks; this export does not execute the application or establish runtime or Windows test success.',
    }


def freeze_receipt(raw: bytes, observed: dict) -> bytes:
    """Construct a portable receipt without claiming an impossible ZIP self-hash."""
    files = read_archive(raw)
    audit_archive(raw)
    if RECEIPT in files or observed.get('status') != 'passed' or observed.get('archive_sha256') != sha(raw):
        raise IterationError('An unchanged candidate with a passed preflight is required.', 'preflight_required')
    digest = payload_digest(files)
    if observed.get('payload_sha256') != digest:
        raise IterationError('Observed preflight does not match this payload.', 'receipt_mismatch')
    receipt = {'schema': RECEIPT_SCHEMA, 'status':'payload_qualified', 'payload_sha256':digest,
               'created_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
               'preflight':observed,
               'scope':'Observed preflight of the identical payload excluding this receipt and index self-hashes. '
                       'The final ZIP is independently re-executed; its exact SHA-256 receipt is stored in host state, '
                       'not impossibly embedded in itself. No signature or guarantee of all behavior.'}
    files[RECEIPT] = json.dumps(receipt, indent=2, ensure_ascii=False).encode()
    manifest = json.loads(files[INDEX])
    manifest['record_index']['qualification'] = RECEIPT
    manifest['release_qualification'] = {'path':RECEIPT, 'payload_sha256':digest, 'status':'payload_qualified'}
    manifest['file_sha256'] = {p:sha(data) for p,data in files.items() if p != INDEX}
    files[INDEX] = json.dumps(manifest, indent=2, ensure_ascii=False).encode()
    validate_receipt(files)
    out = io.BytesIO()
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, time.gmtime()[:6])
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, data)
    result = out.getvalue()
    audit_archive(result)
    return result


def deliver(engine: Engine, build_id: str, output: Path, *, allow_execute: bool = False,
            timeout: float = 30, previous_archive: Path | None = None,
            mode: str = 'qualified', unverified_reasons: list[str] | None = None) -> dict:
    if mode == 'windows-testable':
        return deliver_windows_testable(engine, build_id, output, unverified_reasons)
    if mode != 'qualified':
        raise IterationError('Unknown delivery mode.', 'invalid_delivery_mode')
    if not allow_execute:
        raise IterationError('Inspect source before using --allow-execute.', 'execution_not_authorized')
    _check_output(output)
    build, candidate = engine.archive_bytes(build_id)
    if build.get('delivery') and not build.get('release'):
        raise IterationError('This archive has already been delivered for Windows testing. Inspect it with release_check.py without changing its identity, or create a new build for a qualified release.', 'delivered_archive_immutable')
    if build.get('release'):
        # Repeat retrieval is not a new test; retain and verify its existing receipt.
        result = build['release']['evidence']
        validate_receipt(read_archive(candidate))
        if result.get('archive_sha256') != sha(candidate) or result.get('status') != 'passed':
            raise IterationError('Stored qualification is stale.', 'receipt_mismatch')
        final = candidate
    else:
        with tempfile.TemporaryDirectory(prefix='iteration qualified delivery ') as td:
            base = Path(td)/'candidate.zip'; base.write_bytes(candidate)
            preflight = qualify(base, allow_execute=True, timeout=timeout, previous_archive=previous_archive)
            if preflight['status'] != 'passed':
                attempt = {'status':'blocked', 'stage':'candidate_execution', 'evidence':preflight, 'output_written':False}
                engine._record_qualification_failure(build_id, attempt)
                return attempt
            final = freeze_receipt(candidate, preflight)
            frozen = Path(td)/'frozen.zip'; frozen.write_bytes(final)
            result = qualify(frozen, allow_execute=True, timeout=timeout,
                             previous_archive=previous_archive, require_receipt=True)
            if result['status'] != 'passed':
                attempt = {'status':'blocked', 'stage':'final_execution', 'evidence':result, 'output_written':False}
                engine._record_qualification_failure(build_id, attempt)
                return attempt
        engine._commit_qualification(build_id, sha(candidate), final, result)
    actual = _write_exact_output(final, result['archive_sha256'], output)
    return {'status':'passed', 'path':str(output.resolve()), 'bytes':len(actual),
            'archive_sha256':sha(actual), 'build_id':build_id, 'output_written':True,
            'qualification_stored_in_host_state':True, 'portable_receipt':RECEIPT,
            'windows_bat_tested':False, 'evidence':result,
            'instruction':'Attach this exact file. Any edit or re-ZIP invalidates this exact-archive receipt.'}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--state', type=Path, required=True)
    parser.add_argument('--build-id', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--mode', choices=('qualified', 'windows-testable'), default='qualified')
    parser.add_argument('--unverified-reason', action='append', default=[])
    parser.add_argument('--allow-execute', action='store_true')
    parser.add_argument('--timeout', type=float, default=30)
    parser.add_argument('--previous-archive', type=Path)
    args = parser.parse_args()
    engine = Engine(args.state)
    try:
        result = deliver(engine, args.build_id, args.output, allow_execute=args.allow_execute,
                         timeout=args.timeout, previous_archive=args.previous_archive,
                         mode=args.mode, unverified_reasons=args.unverified_reason)
    except (IterationError, OSError, ValueError, SyntaxError) as exc:
        result = {'status':'blocked','reason':str(exc),'code':getattr(exc,'code',type(exc).__name__), 'output_written':False}
    finally:
        engine.close()
    print(json.dumps(result, indent=2))
    return 0 if result['status'] in ('passed', 'delivered_for_windows_test') else 1


if __name__ == '__main__':
    raise SystemExit(main())
