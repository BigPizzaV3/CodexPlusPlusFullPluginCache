#!/usr/bin/env python3
"""Authenticated Windows process ownership and image verification for Meetings."""

from __future__ import annotations

import ctypes
import hmac
import os
from collections.abc import Callable
from ctypes import wintypes
from pathlib import Path
from typing import TYPE_CHECKING, Protocol

from control_protocol import ControlUnavailable
from native_runtime import NativeRuntimeError

_PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
_PROCESS_TERMINATE = 0x0001
_ERROR_ACCESS_DENIED = 5
_ERROR_INVALID_PARAMETER = 87
_STILL_ACTIVE = 259


class _WindowsCtypesApi(Protocol):
    def WinDLL(self, name: str, *, use_last_error: bool) -> ctypes.CDLL: ...

    def get_last_error(self) -> int: ...


# Linux Pyright stubs intentionally omit these Windows-only ctypes members.
if TYPE_CHECKING:
    _windows_ctypes: _WindowsCtypesApi
else:
    _windows_ctypes = ctypes


def windows_pid_is_proven_dead(pid: int) -> bool:
    """Query Windows process liveness without sending a terminating signal."""

    try:
        kernel32 = _windows_ctypes.WinDLL("kernel32", use_last_error=True)
    except (AttributeError, OSError) as exc:
        raise ControlUnavailable("native control descriptor liveness is unavailable") from exc

    kernel32.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
    kernel32.OpenProcess.restype = wintypes.HANDLE
    kernel32.GetExitCodeProcess.argtypes = [
        wintypes.HANDLE,
        ctypes.POINTER(wintypes.DWORD),
    ]
    kernel32.GetExitCodeProcess.restype = wintypes.BOOL
    kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
    kernel32.CloseHandle.restype = wintypes.BOOL

    handle = kernel32.OpenProcess(_PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
    if not handle:
        error = _windows_ctypes.get_last_error()
        if error == _ERROR_INVALID_PARAMETER:
            return True
        if error == _ERROR_ACCESS_DENIED:
            return False
        raise ControlUnavailable("native control descriptor liveness is unavailable")
    try:
        exit_code = wintypes.DWORD()
        if not kernel32.GetExitCodeProcess(handle, ctypes.byref(exit_code)):
            raise ControlUnavailable("native control descriptor liveness is unavailable")
        return exit_code.value != _STILL_ACTIVE
    finally:
        kernel32.CloseHandle(handle)


def require_windows_owner_process_image(
    pid: int,
    *,
    expected_path: Path,
    app_path: Path,
    expected_digest: str,
    digest_reader: Callable[[Path], str],
    expected_start_identity: tuple[int, int] | None = None,
) -> tuple[int, int]:
    """Prove the canonical image and creation time through one query-only handle."""

    if os.path.normcase(str(expected_path)) != os.path.normcase(str(app_path)):
        raise ControlUnavailable("native update handoff owner image identity does not match")
    try:
        kernel32 = _windows_ctypes.WinDLL("kernel32", use_last_error=True)
        kernel32.OpenProcess.argtypes = [
            wintypes.DWORD,
            wintypes.BOOL,
            wintypes.DWORD,
        ]
        kernel32.OpenProcess.restype = wintypes.HANDLE
        kernel32.QueryFullProcessImageNameW.argtypes = [
            wintypes.HANDLE,
            wintypes.DWORD,
            wintypes.LPWSTR,
            ctypes.POINTER(wintypes.DWORD),
        ]
        kernel32.QueryFullProcessImageNameW.restype = wintypes.BOOL
        kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
        kernel32.CloseHandle.restype = wintypes.BOOL
        handle = kernel32.OpenProcess(_PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
    except (AttributeError, OSError) as exc:
        raise ControlUnavailable(
            "native update handoff owner image identity is unavailable"
        ) from exc
    if not handle:
        raise ControlUnavailable("native update handoff owner image identity is unavailable")
    try:
        start_identity = _windows_process_start_identity(kernel32, handle)
        if expected_start_identity is not None and start_identity != expected_start_identity:
            raise ControlUnavailable("native update handoff owner process identity changed")
        buffer = ctypes.create_unicode_buffer(32_768)
        length = wintypes.DWORD(len(buffer))
        if not kernel32.QueryFullProcessImageNameW(handle, 0, buffer, ctypes.byref(length)):
            raise ControlUnavailable("native update handoff owner image identity is unavailable")
        try:
            actual_path = Path(buffer.value).resolve(strict=True)
        except (OSError, ValueError) as exc:
            raise ControlUnavailable(
                "native update handoff owner image identity is unavailable"
            ) from exc
        if os.path.normcase(str(actual_path)) != os.path.normcase(str(expected_path)):
            raise ControlUnavailable("native update handoff owner image identity does not match")
        try:
            actual_digest = digest_reader(actual_path)
        except (NativeRuntimeError, OSError) as exc:
            raise ControlUnavailable(
                "native update handoff owner image identity is unavailable"
            ) from exc
        if not hmac.compare_digest(actual_digest, expected_digest):
            raise ControlUnavailable("native update handoff owner image identity does not match")
        return start_identity
    finally:
        kernel32.CloseHandle(handle)


def _windows_process_start_identity(kernel32: ctypes.CDLL, handle: int) -> tuple[int, int]:
    """Read the process creation FILETIME without reopening its PID."""
    try:
        kernel32.GetProcessTimes.argtypes = [
            wintypes.HANDLE,
            ctypes.POINTER(wintypes.FILETIME),
            ctypes.POINTER(wintypes.FILETIME),
            ctypes.POINTER(wintypes.FILETIME),
            ctypes.POINTER(wintypes.FILETIME),
        ]
        kernel32.GetProcessTimes.restype = wintypes.BOOL
        created, exited, kernel, user = (wintypes.FILETIME() for _ in range(4))
        if not kernel32.GetProcessTimes(
            handle,
            ctypes.byref(created),
            ctypes.byref(exited),
            ctypes.byref(kernel),
            ctypes.byref(user),
        ):
            raise ControlUnavailable("native update handoff owner process identity is unavailable")
    except (AttributeError, OSError) as exc:
        raise ControlUnavailable(
            "native update handoff owner process identity is unavailable"
        ) from exc
    identity = (created.dwLowDateTime, created.dwHighDateTime)
    if identity == (0, 0):
        raise ControlUnavailable("native update handoff owner process identity is unavailable")
    return identity


def terminate_verified_windows_owner_process(
    pid: int,
    *,
    expected_path: Path,
    app_path: Path,
    expected_digest: str,
    digest_reader: Callable[[Path], str],
    revalidate_owner: Callable[[], None],
    before_terminate: Callable[[], None] | None = None,
    expected_start_identity: tuple[int, int] | None = None,
) -> None:
    """Verify and terminate the exact owner with one continuously pinned handle."""

    if os.path.normcase(str(expected_path)) != os.path.normcase(str(app_path)):
        raise ControlUnavailable("native update handoff owner image identity does not match")
    try:
        kernel32 = _windows_ctypes.WinDLL("kernel32", use_last_error=True)
        kernel32.OpenProcess.argtypes = [
            wintypes.DWORD,
            wintypes.BOOL,
            wintypes.DWORD,
        ]
        kernel32.OpenProcess.restype = wintypes.HANDLE
        kernel32.QueryFullProcessImageNameW.argtypes = [
            wintypes.HANDLE,
            wintypes.DWORD,
            wintypes.LPWSTR,
            ctypes.POINTER(wintypes.DWORD),
        ]
        kernel32.QueryFullProcessImageNameW.restype = wintypes.BOOL
        kernel32.TerminateProcess.argtypes = [wintypes.HANDLE, wintypes.UINT]
        kernel32.TerminateProcess.restype = wintypes.BOOL
        kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
        kernel32.CloseHandle.restype = wintypes.BOOL
        handle = kernel32.OpenProcess(
            _PROCESS_QUERY_LIMITED_INFORMATION | _PROCESS_TERMINATE,
            False,
            pid,
        )
    except (AttributeError, OSError) as exc:
        raise ControlUnavailable(
            "native update handoff owner image identity is unavailable"
        ) from exc
    if not handle:
        raise ControlUnavailable("native update handoff owner image identity is unavailable")
    try:
        if (
            expected_start_identity is not None
            and _windows_process_start_identity(kernel32, handle) != expected_start_identity
        ):
            raise ControlUnavailable("native update handoff owner process identity changed")
        buffer = ctypes.create_unicode_buffer(32_768)
        length = wintypes.DWORD(len(buffer))
        try:
            queried = kernel32.QueryFullProcessImageNameW(
                handle,
                0,
                buffer,
                ctypes.byref(length),
            )
        except (AttributeError, OSError) as exc:
            raise ControlUnavailable(
                "native update handoff owner image identity is unavailable"
            ) from exc
        if not queried:
            raise ControlUnavailable("native update handoff owner image identity is unavailable")
        try:
            actual_path = Path(buffer.value).resolve(strict=True)
        except (OSError, ValueError) as exc:
            raise ControlUnavailable(
                "native update handoff owner image identity is unavailable"
            ) from exc
        if os.path.normcase(str(actual_path)) != os.path.normcase(str(expected_path)):
            raise ControlUnavailable("native update handoff owner image identity does not match")
        try:
            actual_digest = digest_reader(actual_path)
        except (NativeRuntimeError, OSError) as exc:
            raise ControlUnavailable(
                "native update handoff owner image identity is unavailable"
            ) from exc
        if not hmac.compare_digest(actual_digest, expected_digest):
            raise ControlUnavailable("native update handoff owner image identity does not match")
        if before_terminate is not None:
            before_terminate()
        revalidate_owner()
        try:
            terminated = kernel32.TerminateProcess(handle, 1)
        except (AttributeError, OSError) as exc:
            raise ControlUnavailable("native update owner could not be restarted") from exc
        if not terminated:
            raise ControlUnavailable("native update owner could not be restarted")
    finally:
        kernel32.CloseHandle(handle)
