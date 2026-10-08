from __future__ import annotations

import subprocess
from collections.abc import Sequence
from pathlib import Path
from typing import Literal, TypedDict

import native_runtime

from helpers import is_json, unique_json_object

_E2EProcessRole = Literal["companion", "stdio-mcp"]


class _RequiredE2ELiveProcess(TypedDict):
    """Identity fields persisted for every process in an isolated E2E run."""

    pid: int
    startTimeSec: int
    startTimeUsec: int
    role: _E2EProcessRole


class _E2ELiveProcess(_RequiredE2ELiveProcess, total=False):
    """Validated live-process entry; only the stdio MCP has a process group."""

    processGroupId: int


def _process_start_identity(pid: int) -> tuple[int, int]:
    if native_runtime.sys.platform != "darwin":
        raise native_runtime.NativeRuntimeError("E2E launch report requires macOS")
    library = native_runtime.ctypes.CDLL("/usr/lib/libproc.dylib")
    function = library.proc_pidinfo
    function.argtypes = [
        native_runtime.ctypes.c_int,
        native_runtime.ctypes.c_int,
        native_runtime.ctypes.c_uint64,
        native_runtime.ctypes.c_void_p,
        native_runtime.ctypes.c_int,
    ]
    function.restype = native_runtime.ctypes.c_int
    info = native_runtime._ProcBSDInfo()
    size = native_runtime.ctypes.sizeof(info)
    result = function(pid, 3, 0, native_runtime.ctypes.byref(info), size)
    if result != size or info.pbi_pid != pid or info.pbi_start_tvusec >= 1_000_000:
        raise native_runtime.NativeRuntimeError("E2E launch process identity is unavailable")
    return int(info.pbi_start_tvsec), int(info.pbi_start_tvusec)


def _strict_live_process_registry(raw: bytes) -> list[_E2ELiveProcess]:
    def bounded_integer(value: str) -> int:
        if len(value.lstrip("-")) > 19:
            raise ValueError("registry integer is unbounded")
        return int(value)

    try:
        payload: object = native_runtime.json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=unique_json_object,
            parse_int=bounded_integer,
            parse_constant=int,
        )
    except (
        UnicodeDecodeError,
        ValueError,
        RecursionError,
        native_runtime.json.JSONDecodeError,
    ) as exc:
        raise native_runtime.NativeRuntimeError("E2E live-process registry is malformed") from exc
    if not is_json(payload) or set(payload) != {"schemaVersion", "processes"}:
        raise native_runtime.NativeRuntimeError("E2E live-process registry schema did not match")
    processes = payload.get("processes")
    if (
        type(payload.get("schemaVersion")) is not int
        or payload["schemaVersion"] != 1
        or not isinstance(processes, list)
        or len(processes) > native_runtime.E2E_LIVE_PROCESS_REGISTRY_MAX_ENTRIES
    ):
        raise native_runtime.NativeRuntimeError("E2E live-process registry is malformed")
    process_items: list[object] = processes
    seen_pids: set[int] = set()
    validated: list[_E2ELiveProcess] = []
    for process in process_items:
        if not is_json(process):
            raise native_runtime.NativeRuntimeError("E2E live-process registry entry is malformed")
        role = process.get("role")
        expected_keys = {"pid", "startTimeSec", "startTimeUsec", "role"}
        if role == "stdio-mcp":
            validated_role: _E2EProcessRole = "stdio-mcp"
            expected_keys.add("processGroupId")
        elif role == "companion":
            validated_role = "companion"
        else:
            raise native_runtime.NativeRuntimeError("E2E live-process registry role is invalid")
        if set(process) != expected_keys:
            raise native_runtime.NativeRuntimeError(
                "E2E live-process registry entry schema did not match"
            )
        pid = process.get("pid")
        start_seconds = process.get("startTimeSec")
        start_microseconds = process.get("startTimeUsec")
        process_group_id = process.get("processGroupId")
        if (
            type(pid) is not int
            or not 0 < pid <= 2_147_483_647
            or type(start_seconds) is not int
            or not 0 < start_seconds <= 9_223_372_036_854_775_807
            or type(start_microseconds) is not int
            or not 0 <= start_microseconds < 1_000_000
            or pid in seen_pids
        ):
            raise native_runtime.NativeRuntimeError("E2E live-process registry entry is malformed")
        seen_pids.add(pid)
        entry: _E2ELiveProcess = {
            "pid": pid,
            "startTimeSec": start_seconds,
            "startTimeUsec": start_microseconds,
            "role": validated_role,
        }
        if validated_role == "stdio-mcp":
            if type(process_group_id) is not int or process_group_id != pid:
                raise native_runtime.NativeRuntimeError(
                    "E2E live-process registry entry is malformed"
                )
            entry["processGroupId"] = process_group_id
        validated.append(entry)
    return validated


def _live_process_registry_entry(
    *,
    pid: int,
    start_identity: tuple[int, int],
    role: _E2EProcessRole,
    process_group_id: int | None = None,
) -> _E2ELiveProcess:
    entry: _E2ELiveProcess = {
        "pid": pid,
        "startTimeSec": start_identity[0],
        "startTimeUsec": start_identity[1],
        "role": role,
    }
    if process_group_id is not None:
        entry["processGroupId"] = process_group_id
    # Reuse the exact consumer parser so producers cannot emit a wider shape.
    return native_runtime._strict_live_process_registry(
        native_runtime.json.dumps(
            {"schemaVersion": 1, "processes": [entry]},
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    )[0]


def _read_live_process_registry_at(
    directory_descriptor: int,
) -> list[_E2ELiveProcess] | None:
    flags = native_runtime.os.O_RDONLY
    if hasattr(native_runtime.os, "O_NOFOLLOW"):
        flags |= native_runtime.os.O_NOFOLLOW
    try:
        descriptor = native_runtime.os.open(
            native_runtime.E2E_LIVE_PROCESS_REGISTRY_RELATIVE_PATH.name,
            flags,
            dir_fd=directory_descriptor,
        )
    except FileNotFoundError:
        return None
    except OSError as exc:
        raise native_runtime.NativeRuntimeError("E2E live-process registry is unavailable") from exc
    try:
        metadata = native_runtime.os.fstat(descriptor)
        if (
            not native_runtime.stat.S_ISREG(metadata.st_mode)
            or metadata.st_uid != native_runtime.os.getuid()
            or metadata.st_nlink != 1
            or native_runtime.stat.S_IMODE(metadata.st_mode) != 0o600
            or not 0 < metadata.st_size <= native_runtime.E2E_LIVE_PROCESS_REGISTRY_MAX_BYTES
        ):
            raise native_runtime.NativeRuntimeError("E2E live-process registry is unsafe")
        chunks = bytearray()
        while len(chunks) <= native_runtime.E2E_LIVE_PROCESS_REGISTRY_MAX_BYTES:
            chunk = native_runtime.os.read(
                descriptor,
                min(
                    8_192,
                    native_runtime.E2E_LIVE_PROCESS_REGISTRY_MAX_BYTES + 1 - len(chunks),
                ),
            )
            if not chunk:
                break
            chunks.extend(chunk)
        if len(chunks) > native_runtime.E2E_LIVE_PROCESS_REGISTRY_MAX_BYTES:
            raise native_runtime.NativeRuntimeError("E2E live-process registry is oversized")
        final_metadata = native_runtime.os.fstat(descriptor)
        if (
            final_metadata.st_dev != metadata.st_dev
            or final_metadata.st_ino != metadata.st_ino
            or final_metadata.st_size != metadata.st_size
            or final_metadata.st_mtime_ns != metadata.st_mtime_ns
            or final_metadata.st_ctime_ns != metadata.st_ctime_ns
            or len(chunks) != metadata.st_size
        ):
            raise native_runtime.NativeRuntimeError(
                "E2E live-process registry changed while reading"
            )
        return native_runtime._strict_live_process_registry(bytes(chunks))
    finally:
        native_runtime.os.close(descriptor)


def _write_live_process_registry_at(
    directory_descriptor: int,
    processes: Sequence[_E2ELiveProcess],
) -> None:
    raw = (
        native_runtime.json.dumps(
            {"schemaVersion": 1, "processes": processes},
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")
    if not 0 < len(raw) <= native_runtime.E2E_LIVE_PROCESS_REGISTRY_MAX_BYTES:
        raise native_runtime.NativeRuntimeError("E2E live-process registry is oversized")
    destination = native_runtime.E2E_LIVE_PROCESS_REGISTRY_RELATIVE_PATH.name
    temporary = f".{destination}.{native_runtime.uuid.uuid4().hex}.tmp"
    flags = native_runtime.os.O_WRONLY | native_runtime.os.O_CREAT | native_runtime.os.O_EXCL
    if hasattr(native_runtime.os, "O_NOFOLLOW"):
        flags |= native_runtime.os.O_NOFOLLOW
    descriptor = -1
    try:
        existing = native_runtime._read_live_process_registry_at(directory_descriptor)
        if existing is not None:
            # The safe read above binds the replace destination immediately
            # before publication. The marker lock excludes cooperative writers.
            native_runtime._strict_live_process_registry(
                native_runtime.json.dumps(
                    {"schemaVersion": 1, "processes": existing},
                    separators=(",", ":"),
                ).encode("utf-8")
            )
        descriptor = native_runtime.os.open(
            temporary,
            flags,
            0o600,
            dir_fd=directory_descriptor,
        )
        native_runtime.os.fchmod(descriptor, 0o600)
        offset = 0
        while offset < len(raw):
            written = native_runtime.os.write(descriptor, raw[offset:])
            if written <= 0:
                raise native_runtime.NativeRuntimeError(
                    "E2E live-process registry write was incomplete"
                )
            offset += written
        native_runtime.os.fsync(descriptor)
        native_runtime.os.close(descriptor)
        descriptor = -1
        native_runtime.os.replace(
            temporary,
            destination,
            src_dir_fd=directory_descriptor,
            dst_dir_fd=directory_descriptor,
        )
        native_runtime.os.fsync(directory_descriptor)
    except OSError as exc:
        raise native_runtime.NativeRuntimeError("E2E live-process registry is unavailable") from exc
    finally:
        if descriptor >= 0:
            native_runtime.os.close(descriptor)
        try:
            native_runtime.os.unlink(temporary, dir_fd=directory_descriptor)
        except FileNotFoundError:
            pass


def _mutate_e2e_live_process_registry(
    root: Path,
    *,
    entry: _E2ELiveProcess | None,
    initialize: bool,
) -> None:
    if native_runtime.fcntl is None:
        raise native_runtime.NativeRuntimeError("POSIX E2E isolation is unavailable on Windows")
    native_runtime.require_e2e_root_marker(root)
    temporary_root = native_runtime._private_e2e_directory(root / "tmp")
    marker_flags = native_runtime.os.O_RDONLY
    directory_flags = native_runtime.os.O_RDONLY
    if hasattr(native_runtime.os, "O_NOFOLLOW"):
        marker_flags |= native_runtime.os.O_NOFOLLOW
        directory_flags |= native_runtime.os.O_NOFOLLOW
    if hasattr(native_runtime.os, "O_DIRECTORY"):
        directory_flags |= native_runtime.os.O_DIRECTORY
    marker_descriptor = -1
    directory_descriptor = -1
    try:
        marker_descriptor = native_runtime.os.open(
            root / native_runtime.E2E_ROOT_MARKER, marker_flags
        )
        marker_metadata = native_runtime.os.fstat(marker_descriptor)
        if (
            not native_runtime.stat.S_ISREG(marker_metadata.st_mode)
            or marker_metadata.st_uid != native_runtime.os.getuid()
            or marker_metadata.st_nlink != 1
            or native_runtime.stat.S_IMODE(marker_metadata.st_mode) != 0o600
        ):
            raise native_runtime.NativeRuntimeError("E2E isolation root is unclaimed")
        deadline = (
            native_runtime.time.monotonic()
            + native_runtime.E2E_LIVE_PROCESS_REGISTRY_LOCK_TIMEOUT_SECONDS
        )
        while True:
            try:
                native_runtime.fcntl.flock(
                    marker_descriptor,
                    native_runtime.fcntl.LOCK_EX | native_runtime.fcntl.LOCK_NB,
                )
                break
            except BlockingIOError:
                if native_runtime.time.monotonic() >= deadline:
                    raise native_runtime.NativeRuntimeError(
                        "E2E live-process registry lock timed out"
                    ) from None
                native_runtime.time.sleep(0.01)
        native_runtime.os.lseek(marker_descriptor, 0, native_runtime.os.SEEK_SET)
        if (
            native_runtime.os.read(
                marker_descriptor, len(native_runtime.E2E_ROOT_MARKER_CONTENT) + 1
            )
            != native_runtime.E2E_ROOT_MARKER_CONTENT
        ):
            raise native_runtime.NativeRuntimeError("E2E isolation root is unclaimed")
        directory_descriptor = native_runtime.os.open(temporary_root, directory_flags)
        processes = native_runtime._read_live_process_registry_at(directory_descriptor)
        if initialize:
            if processes is not None:
                raise native_runtime.NativeRuntimeError("E2E live-process registry already exists")
            processes = []
        elif processes is None:
            raise native_runtime.NativeRuntimeError("E2E live-process registry is unavailable")
        if entry is not None:
            validated_entry = native_runtime._strict_live_process_registry(
                native_runtime.json.dumps(
                    {"schemaVersion": 1, "processes": [entry]},
                    separators=(",", ":"),
                ).encode("utf-8")
            )[0]
            processes = [
                process for process in processes if process["pid"] != validated_entry["pid"]
            ]
            if len(processes) >= native_runtime.E2E_LIVE_PROCESS_REGISTRY_MAX_ENTRIES:
                raise native_runtime.NativeRuntimeError(
                    "E2E live-process registry exceeded its bound"
                )
            processes.append(validated_entry)
        native_runtime._write_live_process_registry_at(directory_descriptor, processes)
    finally:
        if directory_descriptor >= 0:
            native_runtime.os.close(directory_descriptor)
        if marker_descriptor >= 0:
            try:
                native_runtime.fcntl.flock(marker_descriptor, native_runtime.fcntl.LOCK_UN)
            finally:
                native_runtime.os.close(marker_descriptor)


def _initialize_e2e_live_process_registry(root: Path) -> None:
    native_runtime._mutate_e2e_live_process_registry(root, entry=None, initialize=True)


def _register_e2e_live_process(
    root: Path,
    *,
    pid: int,
    start_identity: tuple[int, int],
    role: _E2EProcessRole,
    process_group_id: int | None = None,
) -> None:
    entry = native_runtime._live_process_registry_entry(
        pid=pid,
        start_identity=start_identity,
        role=role,
        process_group_id=process_group_id,
    )
    native_runtime._mutate_e2e_live_process_registry(root, entry=entry, initialize=False)


def _terminate_unreported_e2e_child(process: native_runtime.subprocess.Popen[bytes]) -> None:
    if process.poll() is not None:
        process.wait()
        return
    process.terminate()
    try:
        process.wait(timeout=2)
    except native_runtime.subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=2)


def _retain_registered_e2e_child(process: subprocess.Popen[bytes]) -> None:
    """Keep an exact child unreaped until probe cleanup retires its owning MCP."""

    with native_runtime._E2E_REGISTERED_CHILD_ANCHORS_LOCK:
        existing = native_runtime._E2E_REGISTERED_CHILD_ANCHORS.get(process.pid)
        if existing is process:
            return
        if (
            existing is not None
            or len(native_runtime._E2E_REGISTERED_CHILD_ANCHORS)
            >= native_runtime.E2E_LIVE_PROCESS_REGISTRY_MAX_ENTRIES
        ):
            raise native_runtime.NativeRuntimeError("E2E companion anchor capacity is unavailable")
        native_runtime._E2E_REGISTERED_CHILD_ANCHORS[process.pid] = process


def _discard_pre_exec_e2e_child(process: subprocess.Popen[bytes]) -> None:
    with native_runtime._E2E_REGISTERED_CHILD_ANCHORS_LOCK:
        if native_runtime._E2E_REGISTERED_CHILD_ANCHORS.get(process.pid) is process:
            native_runtime._E2E_REGISTERED_CHILD_ANCHORS.pop(process.pid)


def _require_e2e_pipe_descriptor(descriptor: int, *, write_end: bool) -> None:
    if native_runtime.fcntl is None:
        raise native_runtime.NativeRuntimeError("POSIX E2E isolation is unavailable on Windows")
    try:
        metadata = native_runtime.os.fstat(descriptor)
        status_flags = native_runtime.fcntl.fcntl(descriptor, native_runtime.fcntl.F_GETFL)
    except OSError as exc:
        raise native_runtime.NativeRuntimeError("E2E companion gate is unavailable") from exc
    expected_access = native_runtime.os.O_WRONLY if write_end else native_runtime.os.O_RDONLY
    if (
        descriptor < 3
        or not native_runtime.stat.S_ISFIFO(metadata.st_mode)
        or metadata.st_uid != native_runtime.os.getuid()
        or metadata.st_nlink != 0
        or status_flags & native_runtime.os.O_ACCMODE != expected_access
    ):
        raise native_runtime.NativeRuntimeError("E2E companion gate is unsafe")


def _e2e_exec_gate(argv: list[str], *, companion: bool) -> int:
    """Exec a verified E2E target only after its exact identity is durable.

    Both the companion and stdio helpers start inside a registered process
    group. Before the one-byte gate arrives neither can detach or execute
    target code; after it arrives the PID/start identity is already durable.
    """

    if (
        len(argv) != 3
        or native_runtime.re.fullmatch(r"[0-9]{1,4}", argv[0]) is None
        or native_runtime.re.fullmatch(r"[0-9]{1,4}", argv[1]) is None
        or (not companion and argv[2] not in native_runtime.E2E_STDIO_PROFILES)
    ):
        return 64
    gate_descriptor = int(argv[0])
    status_descriptor = int(argv[1])
    if gate_descriptor == status_descriptor:
        return 64
    try:
        native_runtime._require_e2e_pipe_descriptor(gate_descriptor, write_end=False)
        native_runtime._require_e2e_pipe_descriptor(status_descriptor, write_end=True)
        token = native_runtime.os.read(gate_descriptor, 2)
        if token != b"\x01":
            raise native_runtime.NativeRuntimeError("E2E exec gate was not released")
        native_runtime.os.close(gate_descriptor)
        gate_descriptor = -1
        if native_runtime.configured_e2e_isolation() is None:
            raise native_runtime.NativeRuntimeError("E2E exec gate requires isolation")
        if companion:
            supplied_executable = native_runtime.Path(argv[2])
            if not supplied_executable.is_absolute() or supplied_executable.is_symlink():
                raise native_runtime.NativeRuntimeError("E2E companion executable is unsafe")
            spec = native_runtime.configured_platform_spec()
            app_path = native_runtime.plugin_artifact_path(native_runtime.PLUGIN_ROOT, spec)
            _, executable, _ = native_runtime._load_app_metadata(app_path, spec)
            if supplied_executable.resolve(strict=True) != executable.resolve(strict=True):
                raise native_runtime.NativeRuntimeError("E2E companion executable changed")
            arguments = [str(executable)]
        else:
            entrypoint = native_runtime.PLUGIN_ROOT / "scripts" / "meetings_mcp_entrypoint.py"
            if entrypoint.is_symlink() or entrypoint.resolve(strict=True) != entrypoint:
                raise native_runtime.NativeRuntimeError("E2E stdio entrypoint is unsafe")
            # Keep the supported interpreter that already admitted this runtime.
            executable = native_runtime.Path(native_runtime.sys.executable).resolve(strict=True)
            if not executable.is_file():
                raise native_runtime.NativeRuntimeError("E2E stdio interpreter is unavailable")
            arguments = [str(executable), "./scripts/meetings_mcp_entrypoint.py"]
            if argv[2] == native_runtime.E2E_STDIO_PROFILE_PRODUCTION:
                arguments.extend(["--profile", native_runtime.E2E_STDIO_PROFILE_PRODUCTION])
        descriptor_flags = native_runtime.fcntl.fcntl(
            status_descriptor, native_runtime.fcntl.F_GETFD
        )
        native_runtime.fcntl.fcntl(
            status_descriptor,
            native_runtime.fcntl.F_SETFD,
            descriptor_flags | native_runtime.fcntl.FD_CLOEXEC,
        )
        native_runtime.os.setsid()
        if not companion:
            native_runtime.os.chdir(native_runtime.PLUGIN_ROOT)
        if (
            family_root := native_runtime.plugin_cache_family_root(native_runtime.PLUGIN_ROOT)
        ) is not None:
            native_runtime.require_canonical_plugin_registration(
                native_runtime.PLUGIN_ROOT, family_root
            )
        native_runtime.os.execve(str(executable), arguments, dict(native_runtime.os.environ))
    except BaseException:
        try:
            native_runtime.os.write(status_descriptor, b"\x01")
        except OSError:
            pass
        return 70
    finally:
        for descriptor in (gate_descriptor, status_descriptor):
            if descriptor < 0:
                continue
            try:
                native_runtime.os.close(descriptor)
            except OSError:
                pass
    return 70


def _e2e_companion_exec_gate(argv: list[str]) -> int:
    return native_runtime._e2e_exec_gate(argv, companion=True)


def _e2e_stdio_exec_gate(argv: list[str]) -> int:
    return native_runtime._e2e_exec_gate(argv, companion=False)


def _spawn_registered_e2e_companion(
    executable: native_runtime.Path,
    *,
    isolation: native_runtime.E2EIsolation,
    capture_mode: str | None,
) -> native_runtime.subprocess.Popen[bytes]:
    gate_read, gate_write = native_runtime.os.pipe()
    status_read, status_write = native_runtime.os.pipe()
    process: native_runtime.subprocess.Popen[bytes] | None = None
    anchor_retained = False
    gate_released = False
    explicit_preexec_failure = False
    exec_succeeded = False
    try:
        process = native_runtime.subprocess.Popen(
            [
                native_runtime.sys.executable,
                "-I",
                "-B",
                str(
                    native_runtime.Path(native_runtime.__file__)
                    .with_name("native_runtime_entrypoint.py")
                    .resolve(strict=True)
                ),
                native_runtime.E2E_COMPANION_EXEC_GATE_ARGUMENT,
                str(gate_read),
                str(status_write),
                str(executable),
            ],
            env=isolation.child_environment(capture_mode=capture_mode),
            stdout=native_runtime.subprocess.DEVNULL,
            stderr=native_runtime.subprocess.DEVNULL,
            pass_fds=(gate_read, status_write),
            close_fds=True,
            # The helper must remain in the registered MCP group until its
            # exact identity is durable. It calls setsid itself after release.
            start_new_session=False,
        )
        native_runtime._retain_registered_e2e_child(process)
        anchor_retained = True
        native_runtime.os.close(gate_read)
        gate_read = -1
        native_runtime.os.close(status_write)
        status_write = -1
        start_identity = native_runtime._process_start_identity(process.pid)
        native_runtime._register_e2e_live_process(
            isolation.root,
            pid=process.pid,
            start_identity=start_identity,
            role="companion",
        )
        # Give the probe the exact registered handle before target code may
        # run or detach. A report failure therefore remains a pre-exec failure
        # that can safely terminate and reap this still-gated helper.
        native_runtime._publish_e2e_launch_report(process, capture_mode=capture_mode)
        try:
            if native_runtime.os.write(gate_write, b"\x01") != 1:
                raise native_runtime.NativeRuntimeError("E2E companion gate write was incomplete")
        except BrokenPipeError as error:
            raise native_runtime.NativeRuntimeError("E2E companion exec failed") from error
        gate_released = True
        released_gate_descriptor = gate_write
        gate_write = -1
        try:
            native_runtime.os.close(released_gate_descriptor)
        except OSError:
            # The one-byte atomic write already released the gate. close(2)
            # errors leave descriptor state ambiguous, so never retry a bare
            # numeric FD; status-pipe EOF remains the exec authority.
            pass
        while True:
            try:
                exec_failure = native_runtime.os.read(status_read, 1)
                break
            except InterruptedError:
                continue
        if exec_failure:
            explicit_preexec_failure = True
            raise native_runtime.NativeRuntimeError("E2E companion exec failed")
        # EOF is the exec proof: the gate marks this descriptor CLOEXEC only
        # after setsid and immediately before execve. From this point onward,
        # no local failure path may poll, wait, reap, or drop the Popen anchor;
        # the marker-locked outer supervisor owns the whole detached forest.
        exec_succeeded = True
        return process
    except BaseException:
        root_only_cleanup_is_safe = (
            not gate_released or explicit_preexec_failure
        ) and not exec_succeeded
        if process is not None and root_only_cleanup_is_safe:
            try:
                native_runtime._terminate_unreported_e2e_child(process)
            except BaseException as cleanup_error:
                raise native_runtime.NativeRuntimeError(
                    "E2E companion registration failed and child cleanup failed"
                ) from cleanup_error
            finally:
                if anchor_retained:
                    native_runtime._discard_pre_exec_e2e_child(process)
        raise
    finally:
        for descriptor in (gate_read, gate_write, status_read, status_write):
            if descriptor < 0:
                continue
            try:
                native_runtime.os.close(descriptor)
            except OSError:
                pass


def _publish_e2e_launch_report(
    process: subprocess.Popen[bytes],
    *,
    capture_mode: str | None,
) -> None:
    if native_runtime.fcntl is None:
        raise native_runtime.NativeRuntimeError("POSIX E2E isolation is unavailable on Windows")
    raw_descriptor = native_runtime.os.environ.get(native_runtime.E2E_LAUNCH_REPORT_FD_ENV)
    nonce = native_runtime.os.environ.get(native_runtime.E2E_LAUNCH_REPORT_NONCE_ENV)
    if raw_descriptor is None and nonce is None:
        raise native_runtime.NativeRuntimeError("E2E launch report is required before exec")
    if (
        not isinstance(raw_descriptor, str)
        or native_runtime.re.fullmatch(r"[0-9]{1,4}", raw_descriptor) is None
        or not isinstance(nonce, str)
        or native_runtime.re.fullmatch(r"[a-f0-9]{64}", nonce) is None
    ):
        raise native_runtime.NativeRuntimeError("E2E launch report configuration is invalid")
    descriptor = int(raw_descriptor)
    if descriptor < 3:
        raise native_runtime.NativeRuntimeError("E2E launch report configuration is invalid")
    try:
        metadata = native_runtime.os.fstat(descriptor)
        status_flags = native_runtime.fcntl.fcntl(descriptor, native_runtime.fcntl.F_GETFL)
        if (
            not native_runtime.stat.S_ISFIFO(metadata.st_mode)
            or metadata.st_uid != native_runtime.os.getuid()
            or metadata.st_nlink != 0
            or status_flags & native_runtime.os.O_ACCMODE != native_runtime.os.O_WRONLY
        ):
            raise native_runtime.NativeRuntimeError("E2E launch report descriptor is unsafe")
        start_seconds, start_microseconds = native_runtime._process_start_identity(process.pid)
        payload = native_runtime.json.dumps(
            {
                "schemaVersion": 1,
                "kind": native_runtime.E2E_LAUNCH_REPORT_KIND,
                "nonce": nonce,
                "launcherPid": native_runtime.os.getpid(),
                "pid": process.pid,
                "startIdentity": {
                    "seconds": start_seconds,
                    "microseconds": start_microseconds,
                },
                "captureMode": capture_mode,
            },
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
        if not payload or len(payload) > 4_096:
            raise native_runtime.NativeRuntimeError("E2E launch report is malformed")
        frame = len(payload).to_bytes(4, byteorder="big") + payload
        written = 0
        while written < len(frame):
            count = native_runtime.os.write(descriptor, frame[written:])
            if count <= 0:
                raise native_runtime.NativeRuntimeError("E2E launch report write was incomplete")
            written += count
    except native_runtime.NativeRuntimeError:
        raise
    except OSError as exc:
        raise native_runtime.NativeRuntimeError("E2E launch report could not be published") from exc
    finally:
        try:
            native_runtime.os.close(descriptor)
        except OSError:
            pass
