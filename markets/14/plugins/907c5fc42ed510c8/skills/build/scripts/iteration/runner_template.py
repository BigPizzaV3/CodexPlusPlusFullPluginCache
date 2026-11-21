"""Portable Build_ runtime supervisor. Copied as Automation/ZP90.py into each build.

Only starts the adjacent PROGRAM/main.py selected by the user via run.bat. The MCP
service never uses this file to execute a managed customer's program.
"""
from __future__ import annotations
import hashlib
import importlib
import tempfile
import json
import os
import platform
import re
import runpy
import traceback
import signal
import subprocess
import sys
import threading
import time
import uuid
import zipfile
from pathlib import Path

SCHEMA = 'iteration.logreport/1'
MAX_LOG = 65536
MAX_LINE = 8192
REMINDER = 'After testing, please send back LogReport.zip.'


def utc() -> str:
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def redact(text: str) -> str:
    """Best effort, not a guarantee against application-printed personal data."""
    # Remove escape/control characters; never preserve terminal escape sequences.
    text = re.sub(r'\x1b\[[0-?]*[ -/]*[@-~]', '', text)
    text = ''.join(c for c in text if c in '\n\t' or (ord(c) >= 32 and ord(c) != 127))
    lines = []
    for line in text.splitlines(keepends=True):
        if re.search(r'(?i)(?:authorization\s*[:=]|bearer\s+|(?:api[_ -]?key|password|passwd|secret|access[_ -]?token|refresh[_ -]?token|token)\s*[\"\']?\s*[:=]|-----BEGIN .*PRIVATE KEY)', line):
            lines.append('[credential-bearing line omitted]\n')
            continue
        line = re.sub(r'\b(?:sk-(?:proj-)?[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{16})\b', '[credential omitted]', line)
        line = re.sub(r'https?://[^\s<>\"\']+', '[URL omitted]', line)
        line = re.sub(r'(?i)\b[A-Z]:[\\/][^\r\n\"\']+', '[local path omitted]', line)
        line = re.sub(r'(?<!\w)/(?:home|Users|mnt|tmp|private|var|root)/[^\s\"\']+', '[local path omitted]', line)
        line = re.sub(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', '[email omitted]', line)
        lines.append(line)
    return ''.join(lines)


class SessionReport:
    """Bounded local report. Atomic replacement leaves the previous ZIP usable."""
    def __init__(self, program: Path, output: Path | None = None):
        self.program = program.resolve()
        self.output = output or self.program.parent / 'LogReport.zip'
        self.lock = threading.RLock()
        self.tail = ''
        self.pending = b''
        self.discard_line = False
        self.truncated = False
        self.started = time.monotonic()
        self.manifest = self.program / 'Automation' / 'AB60.json'
        if not self.manifest.is_file():
            self.manifest = self.program / 'Automation' / 'A00.json'
        self.identity = {}
        self.lifecycle = None
        self.lifecycle_error = False
        self.console_mode = 'quiet'
        self.manifest_sha256 = None
        self.entrypoint_sha256 = None
        try:
            entry = self.program/'main.py'
            if entry.is_file() and not entry.is_symlink() and entry.stat().st_size <= 16*1024*1024:
                self.entrypoint_sha256 = hashlib.sha256(entry.read_bytes()).hexdigest()
        except OSError:
            pass
        try:
            data = self.manifest.read_bytes()
            if len(data) <= 2 * 1024 * 1024:
                value = json.loads(data)
                if isinstance(value, dict):
                    self.identity = {k: value.get(k) for k in ('project_id', 'project_name', 'build_id', 'build_number')}
                    self.manifest_sha256 = hashlib.sha256(data).hexdigest()
                    runtime = value.get('runtime', {})
                    if isinstance(runtime, dict) and runtime.get('console_mode') == 'interactive':
                        self.console_mode = 'interactive'
        except (OSError, ValueError, UnicodeError):
            pass
        # Do not report username, hostname, command-line args, env, or absolute paths.
        self.report = {'schema': SCHEMA, 'report_id': 'r_' + uuid.uuid4().hex,
                       'identity': self.identity, 'manifest_sha256': self.manifest_sha256,
                       'entrypoint_sha256': self.entrypoint_sha256,
                       'started_utc': utc(), 'updated_utc': utc(), 'state': 'starting',
                       'exit_code': None, 'elapsed_seconds': 0,
                       'environment': {'system': platform.system(), 'release': platform.release(),
                                       'machine': platform.machine(), 'python': platform.python_version()},
                       'trust': 'user-supplied diagnostics; not independently authenticated',
                       'lifecycle': None, 'process_exit_code': None,
                       'tests_passed': None, 'supervisor_version': '0.8.2', 'console_mode': self.console_mode,
                       'privacy': {'source_included': False, 'environment_variables_included': False,
                                   'arguments_included': False, 'console_redaction': 'best effort; inspect before sharing'},
                       'console_truncated': False, 'reminder': REMINDER}

    def read_lifecycle(self, path: Path, nonce: str, api) -> None:
        with self.lock:
            try:
                if not path.exists():
                    return
                if path.is_symlink() or path.stat().st_size > 65536:
                    raise ValueError('Unsafe lifecycle snapshot.')
                value = api.validate(json.loads(path.read_text(encoding='utf-8')), nonce)
                if self.lifecycle and (value['sequence'] < self.lifecycle['sequence'] or
                                       self.lifecycle['failed'] and not value['failed']):
                    raise ValueError('Lifecycle state regressed.')
                self.lifecycle = value
                self.report['lifecycle'] = value
            except (OSError, ValueError, TypeError):
                self.lifecycle_error = True
                self.report['lifecycle_protocol_error'] = True

    def finish(self, process_code: int) -> tuple[str, int]:
        self.report['process_exit_code'] = process_code
        life = self.lifecycle or {}
        if self.lifecycle_error:
            return 'protocol_error', process_code or 78
        if process_code != 0:
            return ('runtime_failed' if life.get('ready') else 'startup_failed'), process_code
        if life.get('failed'):
            return ('runtime_failed' if life.get('ready') else 'startup_failed'), 1
        if not life.get('ready'):
            # A swallowed startup error returning zero is NOT a successful run.
            return 'startup_unconfirmed', 78
        return 'completed', 0

    def _append(self, line: bytes):
        text = redact(line.decode('utf-8', errors='replace'))
        self.tail += text
        if len(self.tail) > MAX_LOG:
            self.tail = self.tail[-MAX_LOG:]
            self.truncated = True

    def feed(self, data: bytes):
        with self.lock:
            data = self.pending + data
            self.pending = b''
            chunks = data.split(b'\n')
            for line in chunks[:-1]:
                if not self.discard_line and len(line) <= MAX_LINE:
                    self._append(line + b'\n')
                else:
                    self._append(b'[oversized console line omitted]\n')
                    self.truncated = True
                self.discard_line = False
            last = chunks[-1]
            if self.discard_line or len(last) > MAX_LINE:
                self.discard_line = True
                self.truncated = True
            else:
                self.pending = last

    def flush(self):
        with self.lock:
            if self.discard_line:
                self._append(b'[oversized console line omitted]\n')
            elif self.pending:
                self._append(self.pending)
            self.pending = b''
            self.discard_line = False

    def save(self, state: str | None = None, exit_code: int | None = None) -> bool:
        with self.lock:
            if state:
                self.report['state'] = state
            if exit_code is not None:
                self.report['exit_code'] = exit_code
            self.report['updated_utc'] = utc()
            self.report['elapsed_seconds'] = round(time.monotonic() - self.started, 2)
            self.report['console_truncated'] = self.truncated
            temp = self.output.with_name('.' + self.output.name + '.tmp-' + uuid.uuid4().hex[:8])
            try:
                if self.output.is_symlink() or self.output.parent.is_symlink():
                    return False
                with zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED) as z:
                    z.writestr('report.json', json.dumps(self.report, indent=2, ensure_ascii=False))
                    z.writestr('console.log', self.tail)
                    z.writestr('readme.md', '# Build_ test report\n\n'
                        'Created locally when you ran run.bat. Nothing is uploaded automatically.\n'
                        'Contains build identity, interpreter/OS version, exit status, bounded console tail,\n'
                        'and optional code-only functional observations. No private saved values are included.\n'
                        'No source files, screenshots, environment-variable dump or command-line arguments are collected.\n'
                        'Console output may still contain private data printed by your application. Inspect before sharing.\n'
                        'A running report is not a completed test; exit code 0 is not a gameplay or quality pass.\n'
                        'Hard power-off or forced termination can leave the last running snapshot.\n\n' + REMINDER + '\n')
                os.replace(temp, self.output)
                return True
            except OSError:
                return False
            finally:
                try:
                    temp.unlink(missing_ok=True)
                except OSError:
                    pass



def _managed_child(program: Path, args: list[str]) -> int:
    """Run the adjacent entrypoint, retaining callback failures as nonzero exits.

    Tkinter normally reports callback errors and continues with exit code zero.
    Here unexpected callbacks close the application and mark this run failed.
    Normal validation errors handled by the app remain normal UI interactions.
    """
    failed = threading.Event()
    sys.path.insert(0, str(program))
    lifecycle = importlib.import_module('Automation.RT42')
    lifecycle._start(Path(os.environ.pop('_ITERATION_EVENT_FILE')), os.environ.pop('_ITERATION_EVENT_NONCE'))

    def report_error(kind, exc_type, exc, tb):
        failed.set()
        try:
            lifecycle.fail('unhandled-runtime-error')
        except Exception:
            pass
        print("Build_ diagnostic: " + kind, file=sys.stderr, flush=True)
        traceback.print_exception(exc_type, exc, tb, file=sys.stderr)

    def thread_error(info):
        report_error("unhandled thread error", info.exc_type, info.exc_value, info.exc_traceback)

    threading.excepthook = thread_error
    try:
        import tkinter as tk
    except ImportError:
        tk = None
    if tk is not None:
        original_init = tk.Tk.__init__
        original_destroy = tk.Tk.destroy

        def guarded_destroy(self):
            job = getattr(self, '_iteration_watch_id', None)
            if job:
                try:
                    self.after_cancel(job)
                except tk.TclError:
                    pass
                self._iteration_watch_id = None
            return original_destroy(self)

        def guarded_init(self, *a, **kw):
            original_init(self, *a, **kw)
            def watch():
                if failed.is_set():
                    try:
                        self.quit()
                        self.destroy()
                    except tk.TclError:
                        pass
                else:
                    self._iteration_watch_id = self.after(100, watch)
            self._iteration_watch_id = self.after(100, watch)

        def callback_error(self, exc_type, exc, tb):
            report_error("unhandled UI callback", exc_type, exc, tb)
            try:
                self.quit()
                self.destroy()
            except tk.TclError:
                pass

        tk.Tk.__init__ = guarded_init
        tk.Tk.destroy = guarded_destroy
        tk.Tk.report_callback_exception = callback_error
    sys.path.insert(0, str(program))
    sys.argv = [str(program / 'main.py'), *args]
    code = 0
    try:
        runpy.run_path(str(program / 'main.py'), run_name='__main__')
    except SystemExit as exc:
        if exc.code is None:
            code = 0
        elif isinstance(exc.code, int):
            code = exc.code
        else:
            print(str(exc.code), file=sys.stderr)
            code = 1
    except KeyboardInterrupt:
        code = 130
    except BaseException:
        report_error("unhandled runtime error", *sys.exc_info())
        code = 1
    return code or (1 if failed.is_set() else 0)


def _friendly_failure(saved: bool) -> None:
    # Default GUI mode never streams the traceback to the console at all. For
    # interactive console programs, clear only our current terminal on failure.
    if os.name == 'nt' and sys.stdout.isatty():
        try:
            subprocess.run(['cmd.exe', '/d', '/c', 'cls'], check=False)
        except OSError:
            pass
    print('\nRuntime error. The program could not continue.', flush=True)
    if saved:
        print('Please close this window and send LogReport.zip back to Build_ for a fix.', flush=True)
        print('You will find it beside run.bat. Nothing has been uploaded automatically.', flush=True)
    else:
        print('A new LogReport.zip could not be saved. Do not send an older report.', flush=True)
        print('Extract the ZIP to a writable folder, then retry. If it still fails, tell Build_.', flush=True)


def run_program(program: Path, args: list[str]) -> int:
    program = program.resolve()
    entry = program / 'main.py'
    report = SessionReport(program)
    saved = report.save('starting')
    label = report.identity.get('project_name') or 'Program'
    label = ''.join(c for c in str(label) if c.isprintable())[:60]
    print('Starting ' + label + '...', flush=True)
    if saved:
        print('Local diagnostics: LogReport.zip beside run.bat. Nothing uploads automatically.', flush=True)
    if os.name == 'nt' and hasattr(signal, 'SIGBREAK'):
        def stop_on_break(signum, frame):
            raise KeyboardInterrupt
        signal.signal(signal.SIGBREAK, stop_on_break)
    creation = subprocess.CREATE_NEW_PROCESS_GROUP if os.name == 'nt' else 0
    child = None
    worker = None
    stopped = False
    channel_dir = None
    try:
        sys.path.insert(0, str(program))
        api = importlib.import_module('Automation.RT42')
        channel_dir = tempfile.TemporaryDirectory(prefix='iteration-session-')
        channel = Path(channel_dir.name) / 'events.json'
        nonce = uuid.uuid4().hex
        if not entry.is_file() or entry.is_symlink():
            raise FileNotFoundError('The adjacent PROGRAM/main.py is missing or is a symlink.')
        child = subprocess.Popen([sys.executable, '-u', str(Path(__file__).resolve()),
                    '--iteration-managed-child', *args], cwd=program,
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                    stdin=None if report.console_mode == 'interactive' else subprocess.DEVNULL,
                    shell=False, creationflags=creation,
                    env={**os.environ, 'PYTHONUTF8': '1', 'PYTHONDONTWRITEBYTECODE': '1',
                         '_ITERATION_EVENT_FILE':str(channel), '_ITERATION_EVENT_NONCE':nonce})
        report.save('running')
        def reader():
            assert child is not None and child.stdout is not None
            try:
                while True:
                    data = child.stdout.read1(4096)
                    if not data:
                        break
                    report.feed(data)
                    if report.console_mode == 'interactive':
                        try:
                            if hasattr(sys.stdout, 'buffer'):
                                sys.stdout.buffer.write(data)
                                sys.stdout.buffer.flush()
                            else:
                                sys.stdout.write(data.decode('utf-8', errors='replace'))
                                sys.stdout.flush()
                        except (OSError, UnicodeError):
                            pass
            except (OSError, ValueError):
                pass
            finally:
                report.flush()
        worker = threading.Thread(target=reader, daemon=True)
        worker.start()
        while child.poll() is None:
            try:
                child.wait(timeout=1)
            except subprocess.TimeoutExpired:
                report.read_lifecycle(channel, nonce, api)
                report.save('running')
        worker.join(timeout=3)
        report.read_lifecycle(channel, nonce, api)
        state, code = report.finish(child.returncode)
        if state == 'startup_unconfirmed':
            report.feed(b'Initialization was not confirmed. A clean process exit is not successful startup.\n')
            report.flush()
        saved = report.save(state, code)
    except KeyboardInterrupt:
        stopped = True
        if child and child.poll() is None:
            try:
                child.send_signal(signal.CTRL_BREAK_EVENT if os.name == 'nt' else signal.SIGINT)
                child.wait(timeout=5)
            except (OSError, subprocess.TimeoutExpired, KeyboardInterrupt):
                try:
                    child.terminate()
                    child.wait(timeout=3)
                except (OSError, subprocess.TimeoutExpired):
                    child.kill()
                    child.wait(timeout=3)
        if worker:
            worker.join(timeout=2)
        code = child.returncode if child and child.returncode is not None else 130
        report.flush()
        if channel_dir:
            report.read_lifecycle(channel, nonce, api)
        report.report['process_exit_code'] = code
        saved = report.save('stopped_by_user', code)
    except Exception:
        code = 1
        report.feed(traceback.format_exc().encode('utf-8', errors='replace'))
        report.flush()
        saved = report.save('launcher_error', code)
    finally:
        if child and child.poll() is None:
            child.terminate()
            try:
                child.wait(timeout=3)
            except subprocess.TimeoutExpired:
                child.kill()
                child.wait(timeout=3)
        if worker:
            worker.join(timeout=2)
        if child and child.stdout and not (worker and worker.is_alive()):
            child.stdout.close()
        if channel_dir:
            channel_dir.cleanup()
    if code and not stopped:
        _friendly_failure(saved)
    elif not saved:
        print('A new LogReport.zip could not be saved; do not send an older report.', flush=True)
    else:
        print('\n' + REMINDER, flush=True)
    return (0 if stopped else code) if saved else 74


def main() -> int:
    sys.dont_write_bytecode = True
    program = Path(__file__).resolve().parent.parent
    if sys.argv[1:2] == ['--iteration-managed-child']:
        return _managed_child(program, sys.argv[2:])
    try:
        return run_program(program, sys.argv[1:])
    except BaseException:
        # Last resort for the supervisor itself; do not expose a raw traceback.
        saved = False
        try:
            report = SessionReport(program)
            report.feed(traceback.format_exc().encode('utf-8', errors='replace'))
            report.flush()
            saved = report.save('launcher_error', 1)
        except BaseException:
            pass
        _friendly_failure(saved)
        return 1 if saved else 74


if __name__ == '__main__':
    raise SystemExit(main())
