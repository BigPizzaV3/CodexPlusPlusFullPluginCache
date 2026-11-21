"""No model, network, shell, user commands, credentials, or DAW access."""
from __future__ import annotations
import hashlib
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import platform
import re
import signal
import subprocess
import sys
import threading
import time
import uuid
import zipfile
from . import __version__

HERE = Path(__file__).resolve().parent
STAGES = ('inputs', 'build', 'offline_validation', 'package', 'generated_output_rights', 'daw_acceptance',
          'signing', 'notarization', 'publishing')
ID = re.compile(r'[a-z][a-z0-9-]{0,39}\Z')
RUN = re.compile(r'[0-9a-f]{32}\Z')
class DisproError(Exception): pass
class Stopped(DisproError): pass

def digest(data): return hashlib.sha256(data).hexdigest()
def json_bytes(obj): return (json.dumps(obj, indent=2, sort_keys=True) + '\n').encode()

def no_links(path):
    for part in (path, *path.parents):
        if part.is_symlink(): raise DisproError('symlink paths are not accepted')
    return path

def regular(path, maximum=1048576):
    no_links(path)
    if not path.is_file() or path.stat().st_nlink != 1 or path.stat().st_size > maximum:
        raise DisproError('expected a bounded regular file with one link')
    return path.read_bytes()

def write_new(path, data):
    no_links(path)
    with path.open('xb') as f: f.write(data)

def save_receipt(path, data):
    no_links(path)
    tmp = path.with_suffix('.tmp')
    write_new(tmp, json_bytes(data))
    os.replace(tmp, path)

def deterministic_zip(path, files):
    no_links(path)
    with zipfile.ZipFile(path, 'x', zipfile.ZIP_DEFLATED) as z:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, data)

def recipe(project):
    return {
        'project.json': json_bytes({'schema': 1, 'recipe': 'lv2-mono-gain-v1', 'name': project}),
        'gain.c': regular(HERE/'templates/gain.c').replace(b'__PROJECT__', project.encode()),
        'lv2.h': regular(HERE/'vendor/lv2.h'),
        'LV2-COPYING': regular(HERE/'vendor/LV2-COPYING'),
        'LICENSE': regular(HERE/'OUTPUT-LICENSE.txt'),
        'OUTPUT-LICENSE.txt': regular(HERE/'OUTPUT-LICENSE.txt'),
    }

class Workspace:
    def __init__(self, root, initialize=False):
        self.root = no_links(Path(root).absolute())
        if initialize:
            self.root.mkdir(mode=0o700, parents=True, exist_ok=True)
            if not (self.root/'.dispro-workspace').exists():
                if any(self.root.iterdir()): raise DisproError('initialize requires an empty directory')
                write_new(self.root/'.dispro-workspace', b'Dispro workspace v1\n')
        if regular(self.root/'.dispro-workspace') != b'Dispro workspace v1\n':
            raise DisproError('initialize a dedicated workspace first')

    def project(self, name):
        if not isinstance(name, str) or not ID.fullmatch(name):
            raise DisproError('project must be a lowercase slug, 1–40 characters')
        return no_links(self.root/name)

    def scaffold(self, name):
        target = self.project(name)
        if target.exists(): raise DisproError('project exists; refusing to overwrite')
        target.mkdir(mode=0o700)
        for filename, data in recipe(name).items(): write_new(target/filename, data)
        return {'project': name, 'recipe': 'lv2-mono-gain-v1', 'status': 'created',
                'next': 'start_pipeline', 'native_release_ready': False}

    def verify_inputs(self, name):
        target = self.project(name)
        expected = recipe(name)
        for filename, data in expected.items():
            if regular(target/filename) != data:
                raise DisproError('recipe changed; this version builds only its reviewed fixed recipe')
        return {key: digest(value) for key, value in expected.items()}

    def receipt(self, name, run_id):
        if not isinstance(run_id,str) or not RUN.fullmatch(run_id): raise DisproError('invalid run id')
        return json.loads(regular(self.project(name)/'runs'/run_id/'receipt.json'))

def child_env(scratch):
    # Never inherit API keys, compiler overrides, preload hooks, or signing settings.
    return {'PATH': '/usr/bin:/bin', 'HOME': str(scratch), 'TMPDIR': str(scratch),
            'LANG': 'C', 'LC_ALL': 'C', 'PYTHONNOUSERSITE': '1'}

def run_process(argv, cwd, scratch, seconds, cancel):
    if cancel.is_set(): raise Stopped('cancelled')
    start = time.monotonic()
    # All production callers construct fixed argument lists; never shell=True.
    process = subprocess.Popen(argv, cwd=cwd, env=child_env(scratch),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               start_new_session=True)
    captured = bytearray()
    overflow = threading.Event()
    def drain(stream):
        while True:
            chunk = stream.read(4096)
            if not chunk: break
            # Logs are deliberately not returned or saved: they can contain paths/data.
            if len(captured) + len(chunk) <= 65536: captured.extend(chunk)
            else: overflow.set()
    readers = [threading.Thread(target=drain, args=(s,), daemon=True)
               for s in (process.stdout, process.stderr)]
    for reader in readers: reader.start()
    reason = None
    while process.poll() is None:
        if cancel.is_set(): reason = 'cancelled'
        elif time.monotonic()-start > seconds: reason = 'timed_out'
        elif overflow.is_set(): reason = 'output_limit'
        if reason:
            try: os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError: pass
            break
        cancel.wait(0.02)
    process.wait()
    for reader in readers: reader.join(timeout=1)
    process.stdout.close()
    process.stderr.close()
    if reason: raise Stopped(reason)
    if overflow.is_set(): raise DisproError('output_limit')
    return {'exit_code': process.returncode, 'output_sha256': digest(captured),
            'output_bytes': len(captured)}

def bundle_metadata(name, binary):
    prefix = '@prefix lv2: <http://lv2plug.in/ns/lv2core#> .\n'
    manifest = prefix + '@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n' + \
        f'<urn:dispro:{name}> a lv2:Plugin ; lv2:binary <{binary}> ; rdfs:seeAlso <gain.ttl> .\n'
    ttl = prefix + '@prefix doap: <http://usefulinc.com/ns/doap#> .\n' + \
        f'<urn:dispro:{name}> a lv2:Plugin, lv2:AmplifierPlugin ; doap:name "{name}" ;\n' + \
        'doap:license <OUTPUT-LICENSE.txt> ; lv2:minorVersion 0 ; lv2:microVersion 1 ;\n' + \
        'lv2:port [ a lv2:InputPort, lv2:AudioPort ; lv2:index 0 ; lv2:symbol "in" ; lv2:name "Input" ],\n' + \
        '[ a lv2:OutputPort, lv2:AudioPort ; lv2:index 1 ; lv2:symbol "out" ; lv2:name "Output" ],\n' + \
        '[ a lv2:InputPort, lv2:ControlPort ; lv2:index 2 ; lv2:symbol "gain" ; lv2:name "Gain" ;\n' + \
        'lv2:default 1.0 ; lv2:minimum 0.0 ; lv2:maximum 2.0 ] .\n'
    return {'manifest.ttl': manifest.encode(), 'gain.ttl': ttl.encode()}

def pipeline(ws, name, timeout=30, cancel=None, run_id=None):
    if type(timeout) is not int or not 1 <= timeout <= 60: raise DisproError('timeout must be 1–60 seconds')
    cancel = cancel or threading.Event()
    run_id = run_id or uuid.uuid4().hex
    if not RUN.fullmatch(run_id): raise DisproError('invalid run id')
    project = ws.project(name)
    if not project.is_dir(): raise DisproError('project missing')
    runs = no_links(project/'runs'); runs.mkdir(exist_ok=True)
    out = no_links(runs/run_id); out.mkdir(mode=0o700)
    scratch = out/'scratch'; scratch.mkdir(mode=0o700)
    receipt = {'schema': 1, 'dispro_version': __version__, 'project': name, 'run_id': run_id,
               'started_at': datetime.now(timezone.utc).isoformat(),
               'host': {'system': platform.system(), 'machine': platform.machine(),
                        'os_version': platform.release(), 'python': platform.python_version()},
               'stages': {s: {'status':'unrun'} for s in STAGES}, 'outcome': 'running',
               'native_release_ready': False}
    receipt_path = out/'receipt.json'
    save_receipt(receipt_path, receipt)
    stage = 'inputs'
    deadline = time.monotonic()+timeout
    def remaining():
        if cancel.is_set(): raise Stopped('cancelled')
        value = deadline-time.monotonic()
        if value <= 0: raise Stopped('timed_out')
        return value
    try:
        remaining()
        receipt['input_sha256'] = ws.verify_inputs(name)
        receipt['stages'][stage] = {'status':'passed'}
        receipt['stages']['generated_output_rights'] = {
            'status': 'passed', 'licence': 'Dispro Generated Output Licence 1.0',
            'notice_sha256': receipt['input_sha256']['OUTPUT-LICENSE.txt'],
            'scope': 'Bundled first-party template only; LV2 ISC notices retained.'}
        save_receipt(receipt_path, receipt)
        stage = 'build'
        system = platform.system()
        if system not in ('Darwin', 'Linux'): raise DisproError('native build supports macOS/Linux only')
        if not Path('/usr/bin/cc').is_file(): raise DisproError('install the platform C compiler yourself')
        binary = 'gain.dylib' if system == 'Darwin' else 'gain.so'
        bundle = out/(name+'.lv2'); bundle.mkdir()
        # Snapshot verified bytes; do not compile mutable project files.
        source = out/'source'; source.mkdir()
        for key, value in recipe(name).items(): write_new(source/key, value)
        for key, value in bundle_metadata(name, binary).items(): write_new(bundle/key, value)
        argv = ['/usr/bin/cc', '-std=c99', '-O2', '-Wall', '-Wextra', '-Werror', '-fPIC',
                '-dynamiclib' if system == 'Darwin' else '-shared',
                str(source/'gain.c'), '-o', str(bundle/binary)]
        result = run_process(argv, out, scratch, remaining(), cancel)
        if result['exit_code'] != 0: raise DisproError('compiler failed; no native pass')
        receipt['compiler'] = {'command': '/usr/bin/cc', 'flags': argv[1:8]}
        receipt['stages'][stage] = {'status':'passed', **result}
        binary_hash = digest(regular(bundle/binary, 8*1048576))
        receipt['binary_sha256'] = binary_hash
        save_receipt(receipt_path, receipt)
        stage = 'offline_validation'
        result = run_process([sys.executable, '-I', str(HERE/'validate_native.py'),
                              str(bundle/binary), name, binary_hash], out, scratch, remaining(), cancel)
        if result['exit_code'] != 0: raise DisproError('offline LV2 contract failed')
        receipt['stages'][stage] = {'status':'passed', 'checks':
            ['descriptor', 'instantiate', 'mono_audio', 'gain_changes', 'in_place',
             'zero_block', 'finite_output', 'three_sample_rates', 'control_bounds'], **result}
        save_receipt(receipt_path, receipt)
        stage = 'package'
        remaining()
        if digest(regular(bundle/binary,8*1048576)) != binary_hash: raise DisproError('binary changed')
        files = {f'{name}.lv2/{key}': regular(bundle/key,8*1048576)
                 for key in (binary,'manifest.ttl','gain.ttl')}
        for key in ('LICENSE','OUTPUT-LICENSE.txt','LV2-COPYING'): files[f'{name}.lv2/{key}'] = regular(source/key)
        receipt['bundle_sha256'] = {key:digest(value) for key,value in files.items()}
        archive = out/(name+'.zip')
        deterministic_zip(archive, files)
        with zipfile.ZipFile(archive) as z:
            if set(z.namelist()) != set(files) or any(z.read(key)!=value for key,value in files.items()):
                raise DisproError('package round-trip mismatch')
        receipt['stages'][stage] = {'status':'passed', 'archive': name+'.zip',
                                  'sha256': digest(regular(archive,8*1048576))}
        receipt['outcome'] = 'passed'
    except (DisproError, OSError) as error:
        receipt['stages'][stage] = {'status':'failed', 'reason': str(error) if isinstance(error,DisproError) else 'filesystem/process error'}
        receipt['outcome'] = str(error) if isinstance(error,Stopped) else 'failed'
    finally:
        receipt['finished_at'] = datetime.now(timezone.utc).isoformat()
        save_receipt(receipt_path, receipt)
    return receipt
