"""Opt-in execution gate for an exact, inspected program ZIP.

This is host-local development execution, NOT an MCP server action or a security
sandbox. Inspect source first. --allow-execute acknowledges execution of that code.
The archive is never modified; evidence is bound to its SHA-256.
"""
from __future__ import annotations
import argparse
import ast
import json
import os
import platform
import re
import signal
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from iteration.layout import audit_archive, INDEX, RUNNER
from iteration.release_contract import (PLAN, LIFECYCLE, RECEIPT, validate_plan, verify_plan_files, payload_digest, validate_receipt)
from iteration.logs import parse_log_report
from iteration.records import LAUNCHER
from iteration.safety import IterationError, read_archive, sha


def _stop(process: subprocess.Popen) -> None:
    if process.poll() is not None:
        return
    if os.name == 'nt':
        subprocess.run(['taskkill', '/PID', str(process.pid), '/T', '/F'],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False, timeout=10)
    else:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
    process.wait(timeout=10)



def _isolated_environment(data_root: Path) -> dict[str, str]:
    """Keep runtime/display support, not inherited app settings or credentials.

    This reduces accidental access to live data. It is NOT a security sandbox:
    inspected test entrypoints must honor ITERATION_TEST_DATA_DIR, and native
    code/absolute paths/network access remain subject to the host permissions.
    """
    allowed = {
        'PATH', 'SYSTEMROOT', 'WINDIR', 'COMSPEC', 'PATHEXT', 'SYSTEMDRIVE',
        'PROCESSOR_ARCHITECTURE', 'NUMBER_OF_PROCESSORS',
        'DISPLAY', 'XAUTHORITY', 'WAYLAND_DISPLAY', 'XDG_RUNTIME_DIR',
        'LANG', 'LANGUAGE', 'TERM', 'COLORTERM',
        'LD_LIBRARY_PATH', 'DYLD_LIBRARY_PATH', 'DYLD_FALLBACK_LIBRARY_PATH',
        'TCL_LIBRARY', 'TK_LIBRARY', 'QT_PLUGIN_PATH',
        'QT_QPA_PLATFORM', 'QT_QPA_PLATFORM_PLUGIN_PATH', 'QT_QPA_FONTDIR',
        'FONTCONFIG_PATH', 'FONTCONFIG_FILE', 'PULSE_SERVER',
    }
    env = {key: value for key, value in os.environ.items()
           if key.upper() in allowed or key.upper().startswith('LC_')}
    paths = {
        'LOCALAPPDATA': data_root / 'Local', 'APPDATA': data_root / 'Roaming',
        'HOME': data_root, 'USERPROFILE': data_root,
        'XDG_DATA_HOME': data_root / 'XDG' / 'data',
        'XDG_CONFIG_HOME': data_root / 'XDG' / 'config',
        'XDG_CACHE_HOME': data_root / 'XDG' / 'cache',
        'XDG_STATE_HOME': data_root / 'XDG' / 'state',
        'TEMP': data_root / 'Temp', 'TMP': data_root / 'Temp',
        'TMPDIR': data_root / 'Temp',
        'ITERATION_TEST_DATA_DIR': data_root / 'Application',
    }
    for key, directory in paths.items():
        directory.mkdir(parents=True, exist_ok=True)
        env[key] = str(directory)
    env.update({'PYTHONUTF8': '1', 'PYTHONDONTWRITEBYTECODE': '1'})
    return env


def qualify(archive: Path, *, allow_execute: bool = False, timeout: float = 30, previous_archive: Path | None = None, require_receipt: bool = False) -> dict:
    if not allow_execute:
        raise IterationError('Inspect the generated source, then authorize local execution with --allow-execute.', 'execution_not_authorized')
    if not 0.1 <= timeout <= 180:
        raise IterationError('Timeout must be from 0.1 to 180 seconds.')
    if archive.stat().st_size > 128*1024*1024:
        raise IterationError('Archive exceeds the import limit.')
    raw=archive.read_bytes()
    audit=audit_archive(raw)
    files=read_archive(raw)
    for name,data in files.items():
        if name.endswith('.py'):
            ast.parse(data,filename=name,feature_version=(3,10))
    if files['run.bat'] != LAUNCHER.encode('utf-8'):
        raise IterationError('Use the current bundled run.bat unchanged before release.', 'launcher_template_mismatch')
    if files[RUNNER] != (Path(__file__).parent/'iteration/runner_template.py').read_bytes():
        raise IterationError('Use the current bundled runtime supervisor unchanged before release.', 'runtime_template_mismatch')
    if files.get(LIFECYCLE) != (Path(__file__).parent/'iteration/lifecycle_template.py').read_bytes():
        raise IterationError('Copy the current lifecycle helper unchanged with the engine.', 'lifecycle_template_mismatch')
    try:
        plan = validate_plan(json.loads(files.get(PLAN, b'{}')))
    except (ValueError, UnicodeError) as exc:
        raise IterationError('Unreadable check plan.', 'invalid_plan') from exc
    verify_plan_files(plan, files)
    if RECEIPT in files or require_receipt:
        validate_receipt(files)
    previous_files = None
    if plan.get('previous_archive_sha256'):
        if previous_archive is None or previous_archive.stat().st_size > 128*1024*1024:
            raise IterationError('Inspect and supply the actual preceding archive with --previous-archive.', 'prior_version_required')
        previous_raw = previous_archive.read_bytes()
        if sha(previous_raw) != plan['previous_archive_sha256']:
            raise IterationError('Previous archive differs from the planned baseline.', 'prior_version_mismatch')
        previous_files = read_archive(previous_raw)
    evidence={'schema':'iteration-release-check/2', 'verifier_version':'0.8.0',
              'payload_sha256':payload_digest(files), 'plan_sha256':sha(files[PLAN]),
              'prior_archive_sha256':plan.get('previous_archive_sha256'),
              'test_case_evidence':'Application-reported assertion events observed during execution; not proof of semantic test coverage.','archive_sha256':sha(raw),
              'created_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
              'environment':{'system':platform.system(),'python':platform.python_version()},
              'archive_audit':audit,'checks':[], 'windows_bat_tested':False,
              'scope':'Observed local execution of inspected application test entrypoints. Not a security sandbox or all-behavior guarantee.'}
    with tempfile.TemporaryDirectory(prefix='iteration release check ') as td:
        previous_root = None
        if previous_files:
            previous_root = Path(td)/'previous inspected build'
            for path, data in previous_files.items():
                target = previous_root.joinpath(*path.split('/'))
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
        for name,flag,marker in (('startup','--iteration-smoke-test','ITERATION_SMOKE_OK'),
                                 ('regression','--iteration-self-test','ITERATION_SELF_TEST_OK')):
            # Extract the same frozen bytes independently for EACH phase.
            root=Path(td)/(name+' build space & unicode é');root.mkdir()
            for path,data in files.items():
                target=root.joinpath(*path.split('/'));target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
            output=root/'LogReport.zip';output.unlink(missing_ok=True)
            isolated=Path(td)/('data-'+name);isolated.mkdir()
            env=_isolated_environment(isolated)
            if previous_root:
                env['ITERATION_PREVIOUS_BUILD_DIR'] = str(previous_root)
            process=subprocess.Popen([sys.executable,str(root/RUNNER),flag],cwd=root,
                         stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.DEVNULL,
                         env=env,start_new_session=(os.name!='nt'),
                         creationflags=(subprocess.CREATE_NEW_PROCESS_GROUP if os.name=='nt' else 0))
            timed_out=False
            try:
                stdout,stderr=process.communicate(timeout=timeout)
            except subprocess.TimeoutExpired:
                timed_out=True;_stop(process);stdout,stderr=process.communicate(timeout=5)
            check={'name':name,'passed':False,'process_exit_code':process.returncode,'timed_out':timed_out,
                   'expected_marker':marker, 'report_received':output.is_file()}
            if output.is_file():
                log=parse_log_report(output.read_bytes())
                check.update({'log_exit_code':log['exit_code'],'log_state':log['state'],
                              'manifest_matches':log['manifest_sha256']==sha(files[INDEX]),
                              'entrypoint_matches':log['entrypoint_sha256']==sha(files['PROGRAM/main.py']),
                              'completion_marker': bool(re.search(r'^'+re.escape(marker)+r'\s*$',log['console'],re.M)),
                              'diagnostic_errors':bool(re.search(r'Traceback \(most recent call last\)|invalid command name|Exception in Tkinter callback',log['console'])),
                              'log_report_sha256':sha(output.read_bytes())})
                lifecycle = log.get('lifecycle') or {}
                observed = {c['id']: c for c in lifecycle.get('checks', [])}
                expected = [c for c in plan['cases'] if c['phase'] == name]
                check['application_ready'] = lifecycle.get('ready') is True
                check['lifecycle_failed'] = lifecycle.get('failed', True)
                check['observed_cases'] = lifecycle.get('checks', [])
                check['missing_or_failed_cases'] = [c['id'] for c in expected
                    if observed.get(c['id'], {}).get('passed') is not True or
                       observed.get(c['id'], {}).get('category') != c['category']]
                check['passed']=(check['application_ready'] and not check['lifecycle_failed'] and not check['missing_or_failed_cases'] and not timed_out and process.returncode==0 and log['exit_code']==0 and log['state']=='completed'
                                 and check['manifest_matches'] and check['entrypoint_matches'] and check['completion_marker']
                                 and not check['diagnostic_errors'])
                match=re.search(r'Ran (\d+) tests?',log['console'])
                if match:check['reported_test_count']=int(match.group(1))
            # A traceback belongs only in the local diagnostic archive, never the console.
            check['console_traceback_exposed']=b'Traceback (most recent call last)' in stdout+stderr
            changed = [p for p, data in files.items() if not (root/p).is_file() or (root/p).is_symlink() or sha((root/p).read_bytes()) != sha(data)]
            check['tracked_files_changed'] = changed
            check['passed']=check['passed'] and not check['console_traceback_exposed'] and not changed
            evidence['checks'].append(check)
            if not check['passed']:
                break
    evidence['status']='passed' if len(evidence['checks'])==2 and all(c['passed'] for c in evidence['checks']) else 'blocked'
    return evidence


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive',type=Path)
    parser.add_argument('--allow-execute',action='store_true')
    parser.add_argument('--timeout',type=float,default=30)
    parser.add_argument('--evidence',type=Path)
    parser.add_argument('--previous-archive',type=Path)
    parser.add_argument('--require-receipt',action='store_true')
    args=parser.parse_args()
    try:
        result=qualify(args.archive,allow_execute=args.allow_execute,timeout=args.timeout, previous_archive=args.previous_archive, require_receipt=args.require_receipt)
    except (IterationError,OSError,ValueError,SyntaxError) as exc:
        result={'status':'blocked','reason':str(exc),'code':getattr(exc,'code',type(exc).__name__)}
    if args.evidence:
        if args.evidence.resolve()==args.archive.resolve():
            raise SystemExit('Evidence must not overwrite the program archive.')
        args.evidence.parent.mkdir(parents=True,exist_ok=True)
        args.evidence.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    return 0 if result['status']=='passed' else 1


if __name__=='__main__':
    raise SystemExit(main())
