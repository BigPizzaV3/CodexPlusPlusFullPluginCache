"""Authenticated process identity for stream-only native owner recovery."""

from __future__ import annotations

from pathlib import Path


def verified_darwin_owner_process_image(
    pid: int,
    *,
    expected_path: Path,
    expected_identity: tuple[int, int],
    expected_digest: str,
    expected_start_identity: tuple[int, int] | None = None,
) -> tuple[int, int]:
    """Bind one live Darwin PID and its birth time to the signed owner image."""

    import control_client

    if control_client.sys.platform != "darwin" or type(pid) is not int or pid <= 0:
        raise control_client.ControlUnavailable("native owner process identity is unavailable")

    import native_runtime

    try:
        initial_start = native_runtime.process_start_identity(pid)
        if expected_start_identity is not None and initial_start != expected_start_identity:
            raise control_client.ControlUnavailable("native owner process identity changed")
        native = control_client.ctypes
        library = native.CDLL("/usr/lib/libproc.dylib", use_errno=True)
        library.proc_pidpath.argtypes = [
            native.c_int,
            native.c_void_p,
            native.c_uint32,
        ]
        library.proc_pidpath.restype = native.c_int
        buffer = native.create_string_buffer(4096)
        if library.proc_pidpath(pid, buffer, len(buffer)) <= 0:
            raise control_client.ControlUnavailable("native owner process image is unavailable")
        actual_path = Path(control_client.os.fsdecode(buffer.value)).resolve(strict=True)
        if actual_path != expected_path:
            raise control_client.ControlUnavailable("native owner process image does not match")
        metadata = actual_path.stat()
        if (metadata.st_dev, metadata.st_ino) != expected_identity:
            raise control_client.ControlUnavailable("native owner process image identity changed")
        if not control_client.hmac.compare_digest(
            control_client.sha256_regular_file(actual_path),
            expected_digest,
        ):
            raise control_client.ControlUnavailable("native owner process image digest changed")
        final_start = native_runtime.process_start_identity(pid)
        if final_start != initial_start:
            raise control_client.ControlUnavailable("native owner process identity changed")
        return final_start
    except (
        control_client.NativeRuntimeError,
        AttributeError,
        OSError,
        TypeError,
        ValueError,
    ) as exc:
        raise control_client.ControlUnavailable(
            "native owner process identity is unavailable"
        ) from exc


def require_unchanged_darwin_owner_process_birth(
    pid: int,
    expected_start_identity: tuple[int, int],
) -> None:
    """Fence PID reuse immediately before terminating an authenticated owner."""

    import control_client
    import native_runtime

    try:
        actual_start_identity = native_runtime.process_start_identity(pid)
    except (
        control_client.NativeRuntimeError,
        AttributeError,
        OSError,
        TypeError,
        ValueError,
    ) as exc:
        raise control_client.ControlUnavailable(
            "native owner process identity is unavailable"
        ) from exc
    if actual_start_identity != expected_start_identity:
        raise control_client.ControlUnavailable("native owner process identity changed")
