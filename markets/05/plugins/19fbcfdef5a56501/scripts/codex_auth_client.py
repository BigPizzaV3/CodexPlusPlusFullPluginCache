#!/usr/bin/env python3
"""Fetch ChatGPT auth from Codex app-server without reading credential files."""

from __future__ import annotations

import base64
import ctypes
import hashlib
import json
import logging
import os
import plistlib
import queue
import re
import shutil
import signal
import stat
import subprocess
import sys
import tempfile
import threading
import time
from collections.abc import Callable, Generator, Mapping
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal, Protocol, TypedDict, cast, runtime_checkable
from xml.parsers.expat import ExpatError

from control_client import windows_acl_is_private
from meetings_metrics import (
    AuthCacheOperation,
    AuthFetchResult,
    AuthFetchTransport,
    record_auth_cache_failure,
    record_auth_fetch_latency,
)
from meetings_sentry import (
    MCP_SENTRY_AUTH_FAILURE_REASONS,
    MCP_SENTRY_AUTH_REQUESTED_STORES,
    report_mcp_error,
)

from helpers import is_json, unique_json_object

MAXIMUM_JSON_LINE_BYTES = 1 * 1024 * 1024
MAXIMUM_AUTH_TOKEN_BYTES = 64 * 1024
MAXIMUM_AUTH_FILE_BYTES = 1 * 1024 * 1024
MAXIMUM_JWT_PAYLOAD_SEGMENT_BYTES = 48 * 1024
MAXIMUM_JWT_PAYLOAD_BYTES = 32 * 1024
MAXIMUM_ACCOUNT_ID_BYTES = 256
MAXIMUM_IGNORED_NOTIFICATIONS = 128
DEFAULT_TIMEOUT_SECONDS = 10.0
HELPER_ATTEMPT_SECONDS = 2.0
PROCESS_EXIT_GRACE_SECONDS = 0.25
PROCESS_TERMINATE_GRACE_SECONDS = 1.5
PROCESS_KILL_GRACE_SECONDS = 0.5
AUTH_MANAGER_SHUTDOWN_GRACE_SECONDS = (
    (2 * PROCESS_EXIT_GRACE_SECONDS)
    + PROCESS_TERMINATE_GRACE_SECONDS
    + (2 * PROCESS_KILL_GRACE_SECONDS)
)
MAXIMUM_CODEX_CACHE_ENTRIES = 64
MAXIMUM_CODEX_CLI_BYTES = 1024 * 1024 * 1024
MAXIMUM_BUNDLE_INFO_BYTES = 1 * 1024 * 1024
MAXIMUM_BUNDLE_VERSION_BYTES = 256
WINDOWS_ACL_TIMEOUT_SECONDS = 5.0
AUTH_CACHE_FRESH_SECONDS = 60.0
AUTH_CACHE_MAXIMUM_AGE_SECONDS = 300.0
MAXIMUM_AUTH_CACHE_BYTES = 96 * 1024
MAXIMUM_WINDOWS_CREDENTIAL_BYTES = 5 * 512

_AUTH_CLAIM_NAMESPACE = "https://api.openai.com/auth"  # citadel-ignore: JWT claim namespace
_AUTH_CACHE_SERVICE = "com.openai.chatgpt-meetings.codex-auth.v1"
_MACOS_SECURITY_FRAMEWORK = "/System/Library/Frameworks/Security.framework/Security"
_MACOS_CORE_FOUNDATION_FRAMEWORK = (
    "/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation"
)
_MACOS_KEYCHAIN_ITEM_NOT_FOUND = -25300
_MACOS_KEYCHAIN_DUPLICATE_ITEM = -25299
_MACOS_BUNDLED_CODEX_RELATIVE_PATHS = (
    Path("Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex"),
    Path("Contents/Resources/codex"),
)
_MACOS_NESTED_CODEX_PATH = Path("codex-cli/CodexCLI.app/Contents/MacOS/codex")
_WINDOWS_CREDENTIAL_TYPE_GENERIC = 1
_WINDOWS_CREDENTIAL_PERSIST_SESSION = 1
_SAFE_ACCOUNT_ID_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:@-]{0,255}\Z")
_JWT_SEGMENT_PATTERN = re.compile(r"[A-Za-z0-9_-]+\Z")
_CODEX_CACHE_KEY_PATTERN = re.compile(r"[a-f0-9]{8,128}\Z", re.IGNORECASE)
_WINDOWS_SID_PATTERN = re.compile(r"S-1-(?:[0-9]+-){1,14}[0-9]+")
_MACOS_KEYCHAIN_INTERACTION_LOCK = threading.RLock()
_LOGGER = logging.getLogger(__name__)
_LOGGER.addHandler(logging.NullHandler())

_TransportErrorKind = Literal[
    "spawn",
    "timeout",
    "protocol",
    "io",
    "remote",
    "unsupported",
    "eof",
    "oversize",
]
_SessionEventKind = Literal["line", "eof", "oversize", "io", "protocol"]

AuthFailureReason = Literal[
    "session_unverified",
    "missing_access_token",
    "auth_required",
    "account_changed",
    "invalid_auth_response",
    "host_auth_unavailable",
    "host_auth_timeout",
    "host_auth_unsupported",
    "host_auth_error",
]


class CodexAuthError(RuntimeError):
    """Codex could not provide safe, usable ChatGPT authentication."""

    failure_reason: AuthFailureReason = "invalid_auth_response"

    def __init__(self, message: str, *, failure_reason: AuthFailureReason | None = None) -> None:
        super().__init__(message)
        if failure_reason is not None:
            self.failure_reason = failure_reason


class CodexAuthUnavailable(CodexAuthError):
    """Authentication is temporarily unavailable without proof of sign-out."""

    failure_reason: AuthFailureReason = "host_auth_unavailable"


class CodexAuthAccountUnverified(CodexAuthUnavailable):
    """An observed ChatGPT account cannot be bound to the previous workspace."""

    failure_reason: AuthFailureReason = "session_unverified"


class CodexAuthRequired(CodexAuthError):
    """The active Codex login is absent or is not a ChatGPT login."""

    failure_reason: AuthFailureReason = "auth_required"


class CodexAuthAccountChanged(CodexAuthRequired):
    """The active Codex account changed during an authentication refresh."""

    failure_reason: AuthFailureReason = "account_changed"


class CodexAuthCancelled(CodexAuthError):
    """The caller cancelled an in-flight authentication request."""


class ChatGPTAuthProvider(Protocol):
    """Minimal in-memory auth provider accepted by the Record clients."""

    def get_chatgpt_auth(
        self,
        *,
        refresh_token: bool = False,
        cancellation_event: threading.Event | None = None,
    ) -> AuthMaterial: ...


@runtime_checkable
class _RefreshableChatGPTAuthProvider(ChatGPTAuthProvider, Protocol):
    """Auth provider that can refresh a rejected cached token generation."""

    def refresh_after_unauthorized(
        self,
        rejected: AuthMaterial,
        *,
        cancellation_event: threading.Event | None = None,
    ) -> AuthMaterial: ...


@runtime_checkable
class _ClosableAuthProvider(Protocol):
    """Auth provider that owns resources requiring explicit cleanup."""

    def close(self) -> None: ...


@dataclass(frozen=True, repr=False)
class AuthMaterial:
    """Backend authentication material protected from ordinary serialization.

    The token is deliberately excluded from dataclass-generated formatting.
    Only the bounded platform credential cache may serialize this material.
    """

    token: str = field(repr=False)
    account_id: str
    expires_at_unix_ms: int
    subject: str | None = field(default=None, repr=False)

    def __repr__(self) -> str:
        return "AuthMaterial(token=<redacted>, account_id=<redacted>)"


class AuthCacheDiagnostics(TypedDict):
    """Credential-free cache status safe for the app-only diagnostics panel."""

    cached: bool
    storage: Literal["protected", "memory", "none"]
    expiresAtUnixMs: int | None


@dataclass(frozen=True, repr=False)
class _PersistedAuthEntry:
    material: AuthMaterial
    verified_at_unix_ms: int

    def __repr__(self) -> str:
        return "_PersistedAuthEntry(material=<redacted>, verified_at_unix_ms=<redacted>)"


class _CredentialStore(Protocol):
    """Platform-owned protected storage for one scoped credential entry."""

    def read(self) -> bytes | None: ...

    def write(self, payload: bytes) -> bool: ...

    def delete(self) -> None: ...


class _PersistentAuthCache(Protocol):
    """Bounded, account-validated persistent auth cache."""

    def load(self) -> _PersistedAuthEntry | None: ...

    def save(self, material: AuthMaterial, verified_at_unix_ms: int) -> bool: ...

    def clear(self) -> None: ...


class _NoopAuthCache:
    """Preserve memory-only authentication when protected storage is unsupported."""

    def load(self) -> _PersistedAuthEntry | None:
        return None

    def save(self, material: AuthMaterial, verified_at_unix_ms: int) -> bool:
        del material, verified_at_unix_ms
        return False

    def clear(self) -> None:
        pass


def _report_auth_cache_failure(operation: AuthCacheOperation) -> None:
    try:
        record_auth_cache_failure(operation)
    except Exception:
        pass
    try:
        _LOGGER.warning(
            "Meetings protected auth cache %s failed; continuing with process-local authentication",
            operation,
        )
    except Exception:
        pass


class _MacOSCredentialStore:
    """Access one scoped Keychain item directly through Security.framework."""

    def __init__(self, scope: str) -> None:
        self._service = _AUTH_CACHE_SERVICE.encode("utf-8")
        self._account = scope.encode("utf-8")

    @staticmethod
    def _api() -> tuple[ctypes.CDLL, ctypes.CDLL]:
        if sys.platform != "darwin":
            raise OSError("macOS Keychain storage is unavailable")
        security = ctypes.CDLL(_MACOS_SECURITY_FRAMEWORK)
        core_foundation = ctypes.CDLL(_MACOS_CORE_FOUNDATION_FRAMEWORK)
        security.SecKeychainFindGenericPassword.argtypes = [
            ctypes.c_void_p,
            ctypes.c_uint32,
            ctypes.c_char_p,
            ctypes.c_uint32,
            ctypes.c_char_p,
            ctypes.POINTER(ctypes.c_uint32),
            ctypes.POINTER(ctypes.c_void_p),
            ctypes.POINTER(ctypes.c_void_p),
        ]
        security.SecKeychainFindGenericPassword.restype = ctypes.c_int32
        security.SecKeychainAddGenericPassword.argtypes = [
            ctypes.c_void_p,
            ctypes.c_uint32,
            ctypes.c_char_p,
            ctypes.c_uint32,
            ctypes.c_char_p,
            ctypes.c_uint32,
            ctypes.c_void_p,
            ctypes.POINTER(ctypes.c_void_p),
        ]
        security.SecKeychainAddGenericPassword.restype = ctypes.c_int32
        security.SecKeychainItemModifyAttributesAndData.argtypes = [
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_uint32,
            ctypes.c_void_p,
        ]
        security.SecKeychainItemModifyAttributesAndData.restype = ctypes.c_int32
        security.SecKeychainItemDelete.argtypes = [ctypes.c_void_p]
        security.SecKeychainItemDelete.restype = ctypes.c_int32
        security.SecKeychainItemFreeContent.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        security.SecKeychainItemFreeContent.restype = ctypes.c_int32
        security.SecKeychainGetUserInteractionAllowed.argtypes = [ctypes.POINTER(ctypes.c_ubyte)]
        security.SecKeychainGetUserInteractionAllowed.restype = ctypes.c_int32
        security.SecKeychainSetUserInteractionAllowed.argtypes = [ctypes.c_ubyte]
        security.SecKeychainSetUserInteractionAllowed.restype = ctypes.c_int32
        core_foundation.CFRelease.argtypes = [ctypes.c_void_p]
        core_foundation.CFRelease.restype = None
        return security, core_foundation

    @contextmanager
    def _noninteractive_api(self) -> Generator[tuple[ctypes.CDLL, ctypes.CDLL], None, None]:
        security, core_foundation = self._api()
        with _MACOS_KEYCHAIN_INTERACTION_LOCK:
            previously_allowed = ctypes.c_ubyte()
            if security.SecKeychainGetUserInteractionAllowed(ctypes.byref(previously_allowed)) != 0:
                raise OSError("macOS Keychain interaction state is unavailable")
            if security.SecKeychainSetUserInteractionAllowed(False) != 0:
                raise OSError("macOS Keychain interaction could not be disabled")
            try:
                yield security, core_foundation
            finally:
                if security.SecKeychainSetUserInteractionAllowed(previously_allowed.value) != 0:
                    raise OSError("macOS Keychain interaction state could not be restored")

    def read(self) -> bytes | None:
        try:
            with self._noninteractive_api() as (security, _):
                password_length = ctypes.c_uint32()
                password_data = ctypes.c_void_p()
                status = security.SecKeychainFindGenericPassword(
                    None,
                    len(self._service),
                    self._service,
                    len(self._account),
                    self._account,
                    ctypes.byref(password_length),
                    ctypes.byref(password_data),
                    None,
                )
                if status != 0:
                    if status != _MACOS_KEYCHAIN_ITEM_NOT_FOUND:
                        _report_auth_cache_failure("read")
                    return None
                try:
                    if (
                        not password_data
                        or not 0 < password_length.value <= MAXIMUM_AUTH_CACHE_BYTES
                    ):
                        return None
                    return ctypes.string_at(password_data, password_length.value)
                finally:
                    if password_data:
                        security.SecKeychainItemFreeContent(None, password_data)
        except (OSError, AttributeError, TypeError, ValueError, OverflowError):
            _report_auth_cache_failure("read")
            return None

    def write(self, payload: bytes) -> bool:
        if not payload or len(payload) > MAXIMUM_AUTH_CACHE_BYTES:
            return False
        try:
            with self._noninteractive_api() as (security, core_foundation):
                password_buffer = (ctypes.c_ubyte * len(payload)).from_buffer_copy(payload)
                password_data = ctypes.cast(password_buffer, ctypes.c_void_p)
                status = security.SecKeychainAddGenericPassword(
                    None,
                    len(self._service),
                    self._service,
                    len(self._account),
                    self._account,
                    len(payload),
                    password_data,
                    None,
                )
                if status == 0:
                    return True
                if status != _MACOS_KEYCHAIN_DUPLICATE_ITEM:
                    return False
                item = ctypes.c_void_p()
                status = security.SecKeychainFindGenericPassword(
                    None,
                    len(self._service),
                    self._service,
                    len(self._account),
                    self._account,
                    None,
                    None,
                    ctypes.byref(item),
                )
                if status != 0 or not item:
                    return False
                try:
                    return (
                        security.SecKeychainItemModifyAttributesAndData(
                            item,
                            None,
                            len(payload),
                            password_data,
                        )
                        == 0
                    )
                finally:
                    core_foundation.CFRelease(item)
        except (OSError, AttributeError, TypeError, ValueError, OverflowError):
            return False

    def delete(self) -> None:
        try:
            with self._noninteractive_api() as (security, core_foundation):
                item = ctypes.c_void_p()
                status = security.SecKeychainFindGenericPassword(
                    None,
                    len(self._service),
                    self._service,
                    len(self._account),
                    self._account,
                    None,
                    None,
                    ctypes.byref(item),
                )
                if status != 0:
                    if status != _MACOS_KEYCHAIN_ITEM_NOT_FOUND:
                        _report_auth_cache_failure("delete")
                    return
                if not item:
                    _report_auth_cache_failure("delete")
                    return
                try:
                    if security.SecKeychainItemDelete(item) != 0:
                        _report_auth_cache_failure("delete")
                finally:
                    core_foundation.CFRelease(item)
        except (OSError, AttributeError, TypeError, ValueError, OverflowError):
            _report_auth_cache_failure("delete")


class _WindowsFileTime(ctypes.Structure):
    _fields_ = [("low", ctypes.c_uint32), ("high", ctypes.c_uint32)]


class _WindowsCredential(ctypes.Structure):
    _fields_ = [
        ("flags", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("target_name", ctypes.c_wchar_p),
        ("comment", ctypes.c_wchar_p),
        ("last_written", _WindowsFileTime),
        ("credential_blob_size", ctypes.c_uint32),
        ("credential_blob", ctypes.POINTER(ctypes.c_ubyte)),
        ("persist", ctypes.c_uint32),
        ("attribute_count", ctypes.c_uint32),
        ("attributes", ctypes.c_void_p),
        ("target_alias", ctypes.c_wchar_p),
        ("user_name", ctypes.c_wchar_p),
    ]


class _WindowsCredentialApi(Protocol):
    def WinDLL(self, name: str, *, use_last_error: bool) -> ctypes.CDLL: ...


class _WindowsCredentialStore:
    """Store one non-roaming, current-logon Windows generic credential."""

    def __init__(self, scope: str) -> None:
        self._target = f"{_AUTH_CACHE_SERVICE}/{scope}"

    @staticmethod
    def _api() -> ctypes.CDLL:
        if os.name != "nt":
            raise OSError("Windows credential storage is unavailable")
        windows_api: _WindowsCredentialApi = ctypes
        return windows_api.WinDLL("advapi32", use_last_error=True)

    def read(self) -> bytes | None:
        try:
            api = self._api()
            credential_pointer = ctypes.POINTER(_WindowsCredential)()
            api.CredReadW.argtypes = [
                ctypes.c_wchar_p,
                ctypes.c_uint32,
                ctypes.c_uint32,
                ctypes.POINTER(ctypes.POINTER(_WindowsCredential)),
            ]
            api.CredReadW.restype = ctypes.c_int
            api.CredFree.argtypes = [ctypes.c_void_p]
            api.CredFree.restype = None
            if not api.CredReadW(
                self._target,
                _WINDOWS_CREDENTIAL_TYPE_GENERIC,
                0,
                ctypes.byref(credential_pointer),
            ):
                return None
            try:
                credential = credential_pointer.contents
                if (
                    credential.type != _WINDOWS_CREDENTIAL_TYPE_GENERIC
                    or not credential.credential_blob
                    or credential.credential_blob_size <= 0
                    or credential.credential_blob_size > MAXIMUM_WINDOWS_CREDENTIAL_BYTES
                ):
                    return None
                return ctypes.string_at(
                    credential.credential_blob,
                    credential.credential_blob_size,
                )
            finally:
                api.CredFree(ctypes.cast(credential_pointer, ctypes.c_void_p))
        except (OSError, AttributeError, ValueError):
            _report_auth_cache_failure("read")
            return None

    def write(self, payload: bytes) -> bool:
        if not payload or len(payload) > MAXIMUM_WINDOWS_CREDENTIAL_BYTES:
            return False
        try:
            api = self._api()
            api.CredWriteW.argtypes = [ctypes.POINTER(_WindowsCredential), ctypes.c_uint32]
            api.CredWriteW.restype = ctypes.c_int
            blob = (ctypes.c_ubyte * len(payload)).from_buffer_copy(payload)
            credential = _WindowsCredential()
            credential.type = _WINDOWS_CREDENTIAL_TYPE_GENERIC
            credential.target_name = self._target
            credential.credential_blob_size = len(payload)
            credential.credential_blob = ctypes.cast(blob, ctypes.POINTER(ctypes.c_ubyte))
            credential.persist = _WINDOWS_CREDENTIAL_PERSIST_SESSION
            credential.user_name = "chatgpt-meetings"
            return bool(api.CredWriteW(ctypes.byref(credential), 0))
        except (OSError, AttributeError, ValueError):
            return False

    def delete(self) -> None:
        try:
            api = self._api()
            api.CredDeleteW.argtypes = [ctypes.c_wchar_p, ctypes.c_uint32, ctypes.c_uint32]
            api.CredDeleteW.restype = ctypes.c_int
            api.CredDeleteW(self._target, _WINDOWS_CREDENTIAL_TYPE_GENERIC, 0)
        except (OSError, AttributeError, ValueError):
            _report_auth_cache_failure("delete")


class _PlatformAuthCache:
    """Validate protected cache contents against their embedded JWT identity."""

    def __init__(self, store: _CredentialStore) -> None:
        self._store = store

    def load(self) -> _PersistedAuthEntry | None:
        try:
            payload = self._store.read()
            if payload is None or not 0 < len(payload) <= MAXIMUM_AUTH_CACHE_BYTES:
                return None
            decoded: object = json.loads(
                payload,
                object_pairs_hook=unique_json_object,
                parse_constant=int,
            )
            if not is_json(decoded) or set(decoded) != {"token", "verifiedAtUnixMs"}:
                return None
            verified_at = decoded["verifiedAtUnixMs"]
            if type(verified_at) is not int or verified_at <= 0:
                return None
            material = _auth_material_from_result(
                {"authMethod": "chatgpt", "authToken": decoded["token"]}
            )
            return _PersistedAuthEntry(material=material, verified_at_unix_ms=verified_at)
        except (CodexAuthError, OSError, UnicodeDecodeError, ValueError, RecursionError):
            _report_auth_cache_failure("read")
            return None

    def save(self, material: AuthMaterial, verified_at_unix_ms: int) -> bool:
        if type(verified_at_unix_ms) is not int or verified_at_unix_ms <= 0:
            return False
        try:
            verified_material = _auth_material_from_result(
                {"authMethod": "chatgpt", "authToken": material.token}
            )
            if (
                material.account_id,
                material.subject,
                material.expires_at_unix_ms,
            ) != (
                verified_material.account_id,
                verified_material.subject,
                verified_material.expires_at_unix_ms,
            ):
                return False
            payload = json.dumps(
                {
                    "token": material.token,
                    "verifiedAtUnixMs": verified_at_unix_ms,
                },
                ensure_ascii=True,
                separators=(",", ":"),
            ).encode("ascii")
            if len(payload) > MAXIMUM_AUTH_CACHE_BYTES:
                return False
            return self._store.write(payload)
        except (CodexAuthError, OSError, TypeError, ValueError):
            return False

    def clear(self) -> None:
        try:
            self._store.delete()
        except OSError:
            _report_auth_cache_failure("delete")


def _default_persistent_auth_cache() -> _PersistentAuthCache:
    if sys.platform != "darwin" and os.name != "nt":
        return _NoopAuthCache()
    try:
        scope = hashlib.sha256(str(_active_codex_home(None)).encode("utf-8")).hexdigest()
        store: _CredentialStore
        if sys.platform == "darwin":
            store = _MacOSCredentialStore(scope)
        else:
            store = _WindowsCredentialStore(scope)
        return _PlatformAuthCache(store)
    except Exception:
        _report_auth_cache_failure("initialize")
        return _NoopAuthCache()


class _TransportError(Exception):
    """Internal fixed-message transport failure safe for local control flow."""

    def __init__(self, kind: _TransportErrorKind, *, account_unverified: bool = False) -> None:
        super().__init__(kind)
        self.kind: _TransportErrorKind = kind
        self.account_unverified = account_unverified


@dataclass(frozen=True)
class _ProcessSpec:
    argv: tuple[str, ...]
    environment: Mapping[str, str]
    working_directory: Path | None = None


class _AuthSession(Protocol):
    """Bounded JSON-RPC transport used only for Codex authentication."""

    def set_cancellation_event(self, event: threading.Event | None) -> None: ...

    def request(
        self,
        request_id: int,
        method: str,
        params: Mapping[str, object],
        *,
        deadline: float,
    ) -> object: ...

    def notify(self, method: str, *, deadline: float) -> None: ...

    def close(self, *, force: bool) -> None: ...


class _JsonLineSession:
    """One bounded, cancellable JSON-RPC session over child stdio."""

    def __init__(
        self,
        process: subprocess.Popen[bytes],
        *,
        cancellation_event: threading.Event | None,
    ) -> None:
        if process.stdin is None or process.stdout is None:
            raise _TransportError("spawn")
        self._process = process
        self._stdin = process.stdin
        self._stdout = process.stdout
        self._cancellation_event = cancellation_event
        self._events: queue.Queue[tuple[_SessionEventKind, bytes | None]] = queue.Queue(
            maxsize=MAXIMUM_IGNORED_NOTIFICATIONS + 4
        )
        self._reader = threading.Thread(
            target=self._read_stdout,
            name="codex-auth-app-server-reader",
            daemon=True,
        )
        try:
            self._reader.start()
        except RuntimeError:
            # Thread exhaustion is a session startup failure, like child spawn failure.
            raise _TransportError("spawn") from None

    def set_cancellation_event(self, event: threading.Event | None) -> None:
        self._cancellation_event = event

    def request(
        self,
        request_id: int,
        method: str,
        params: Mapping[str, object],
        *,
        deadline: float,
    ) -> object:
        self._write_message(
            {
                "jsonrpc": "2.0",
                "id": request_id,
                "method": method,
                "params": dict(params),
            },
            deadline=deadline,
        )
        return self._wait_for_response(request_id, deadline=deadline)

    def notify(
        self,
        method: str,
        *,
        deadline: float,
    ) -> None:
        self._write_message(
            {"jsonrpc": "2.0", "method": method},
            deadline=deadline,
        )

    def close(self, *, force: bool) -> None:
        try:
            self._stdin.close()
        except OSError:
            pass

        if not force and _wait_for_exit(self._process, PROCESS_EXIT_GRACE_SECONDS):
            self._reader.join(timeout=PROCESS_EXIT_GRACE_SECONDS)
            try:
                self._stdout.close()
            except OSError:
                pass
            return

        _terminate_process(self._process)
        self._reader.join(timeout=PROCESS_KILL_GRACE_SECONDS)
        try:
            self._stdout.close()
        except OSError:
            pass

    def _write_message(
        self,
        message: Mapping[str, object],
        *,
        deadline: float,
    ) -> None:
        _raise_if_cancelled(self._cancellation_event)
        if time.monotonic() >= deadline:
            raise _TransportError("timeout")
        try:
            payload = (
                json.dumps(
                    message,
                    ensure_ascii=True,
                    separators=(",", ":"),
                ).encode("utf-8")
                + b"\n"
            )
        except (TypeError, ValueError):
            raise _TransportError("protocol") from None
        if len(payload) > MAXIMUM_JSON_LINE_BYTES:
            raise _TransportError("protocol")
        try:
            self._stdin.write(payload)
            self._stdin.flush()
        except (BrokenPipeError, OSError, ValueError):
            raise _TransportError("io") from None

    def _wait_for_response(self, request_id: int, *, deadline: float) -> object:
        ignored = 0
        while True:
            _raise_if_cancelled(self._cancellation_event)
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise _TransportError("timeout")
            try:
                event_kind, payload = self._events.get(timeout=min(0.05, remaining))
            except queue.Empty:
                continue

            if event_kind != "line":
                raise _TransportError(event_kind)
            if payload is None:
                raise _TransportError("protocol")
            try:
                decoded: object = json.loads(
                    payload,
                    object_pairs_hook=unique_json_object,
                    parse_constant=int,
                )
            except (ValueError, UnicodeDecodeError, RecursionError):
                raise _TransportError("protocol") from None
            if not is_json(decoded):
                raise _TransportError("protocol")
            message = decoded
            if message.get("jsonrpc") not in (
                None,
                "2.0",
            ):
                raise _TransportError("protocol")

            if "id" not in message:
                if not isinstance(message.get("method"), str):
                    raise _TransportError("protocol")
                ignored += 1
                if ignored > MAXIMUM_IGNORED_NOTIFICATIONS:
                    raise _TransportError("protocol")
                continue

            response_id = message.get("id")
            if type(response_id) is not int or response_id != request_id or "method" in message:
                raise _TransportError("protocol")
            if "error" in message:
                # Never propagate an app-server error body; it is not a safe
                # public surface and could contain credential-adjacent data.
                remote_error = message["error"]
                if is_json(remote_error) and remote_error.get("code") == -32601:
                    raise _TransportError("unsupported")
                raise _TransportError("remote")
            if "result" not in message:
                raise _TransportError("protocol")
            return message["result"]

    def _read_stdout(self) -> None:
        try:
            while True:
                line = self._stdout.readline(MAXIMUM_JSON_LINE_BYTES + 1)
                if not line:
                    self._put_event("eof", None)
                    return
                if len(line) > MAXIMUM_JSON_LINE_BYTES or not line.endswith(b"\n"):
                    self._put_event("oversize", None)
                    return
                self._put_event("line", line)
        except (OSError, ValueError):
            self._put_event("io", None)

    def _put_event(
        self,
        kind: _SessionEventKind,
        payload: bytes | None,
    ) -> None:
        try:
            self._events.put_nowait((kind, payload))
        except queue.Full:
            # A full bounded queue is itself a protocol failure. Dropping the
            # event is safe: the foreground deadline/cancellation remains live.
            pass


class CodexAuthClient:
    """Obtain short-lived ChatGPT credentials through Codex app-server."""

    def __init__(
        self,
        *,
        codex_path: str | os.PathLike[str] | None = None,
        codex_home: str | os.PathLike[str] | None = None,
        timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
    ) -> None:
        if timeout_seconds <= 0:
            raise ValueError("timeout must be positive")
        self._codex_path = _resolve_codex_path(codex_path, prefer_platform_helpers=False)
        self._allow_fallback = codex_path is None and (
            sys.platform != "darwin" or not os.environ.get("CODEX_BIN", "").strip()
        )
        self._active_codex_home = _active_codex_home(codex_home)
        self._timeout_seconds = float(timeout_seconds)
        self._session_lock = threading.RLock()
        self._closed = False

    def close(self) -> None:
        """Prevent further isolated-child authentication requests."""

        with self._session_lock:
            self._closed = True

    def get_chatgpt_auth(
        self,
        *,
        refresh_token: bool = False,
        cancellation_event: threading.Event | None = None,
    ) -> AuthMaterial:
        """Return in-memory ChatGPT auth, optionally forcing one token refresh."""

        if type(refresh_token) is not bool:
            raise TypeError("refresh_token must be a bool")
        _raise_if_cancelled(cancellation_event)

        with self._session_lock:
            if self._closed:
                raise CodexAuthUnavailable("Codex authentication could not be completed")
            return self._get_chatgpt_auth_locked(
                refresh_token=refresh_token,
                cancellation_event=cancellation_event,
            )

    def _get_chatgpt_auth_locked(
        self,
        *,
        refresh_token: bool,
        cancellation_event: threading.Event | None,
    ) -> AuthMaterial:
        _raise_if_cancelled(cancellation_event)
        overall_deadline = time.monotonic() + self._timeout_seconds

        temporary_directory: tempfile.TemporaryDirectory[str] | None = None
        requested_store = "unavailable"
        transport_failure: _TransportErrorKind | None = None
        try:
            temporary_directory = tempfile.TemporaryDirectory(prefix="chatgpt-meetings-codex-home-")
            temporary_home = Path(temporary_directory.name)
            temporary_home.chmod(0o700)
            credential_store, child_home = self._prepare_temporary_credentials(temporary_home)
            requested_store = credential_store
            child_spec = _ProcessSpec(
                argv=(
                    self._codex_path,
                    "app-server",
                    "--listen",
                    "stdio://",
                    "--disable",
                    "plugins",
                    "-c",
                    f"cli_auth_credentials_store={credential_store}",
                    # Token export must not depend on the user's inference provider.
                    "-c",
                    'model_provider="openai"',
                ),
                environment=self._environment_for(child_home),
                working_directory=temporary_home,
            )
            candidate_paths = (self._codex_path,)
            if self._allow_fallback:
                candidate_paths += _fallback_codex_paths(self._codex_path)
            last_error = _TransportError("spawn")
            account_unverified = False
            for index, candidate_path in enumerate(candidate_paths):
                _raise_if_cancelled(cancellation_event)
                if time.monotonic() >= overall_deadline:
                    last_error = _TransportError("timeout")
                    break
                candidate_deadline = overall_deadline
                if index < len(candidate_paths) - 1:
                    candidate_deadline = min(
                        overall_deadline,
                        time.monotonic() + HELPER_ATTEMPT_SECONDS,
                    )
                candidate_spec = _ProcessSpec(
                    argv=(candidate_path, *child_spec.argv[1:]),
                    environment=child_spec.environment,
                    working_directory=child_spec.working_directory,
                )
                try:
                    material = self._run_session(
                        candidate_spec,
                        refresh_token=refresh_token,
                        cancellation_event=cancellation_event,
                        deadline=candidate_deadline,
                    )
                except _TransportError as error:
                    last_error = error
                    account_unverified |= error.account_unverified
                    continue
                self._codex_path = candidate_path
                return material
            transport_failure = last_error.kind
            public_error = _public_transport_error(last_error)
            if account_unverified:
                # A failed recovery or later helper must not resurrect the bearer
                # invalidated by a preceding null auth method.
                raise CodexAuthAccountUnverified(
                    "ChatGPT account could not be verified",
                    failure_reason=public_error.failure_reason,
                ) from None
            raise public_error from None
        except (CodexAuthRequired, CodexAuthCancelled):
            raise
        except CodexAuthAccountUnverified:
            _report_auth_failure("account_unverified", requested_store)
            raise
        except CodexAuthError:
            _report_auth_failure(transport_failure or "invalid_auth", requested_store)
            raise
        except OSError:
            _report_auth_failure("io", requested_store)
            raise CodexAuthUnavailable("Codex app-server is unavailable") from None
        finally:
            if temporary_directory is not None:
                temporary_directory.cleanup()

    def _run_session(
        self,
        process_spec: _ProcessSpec,
        *,
        refresh_token: bool,
        cancellation_event: threading.Event | None,
        deadline: float,
    ) -> AuthMaterial:
        attempt_started = time.monotonic()
        attempt_result: AuthFetchResult = "error"
        process: subprocess.Popen[bytes] | None = None
        session: _JsonLineSession | None = None
        completed = False
        account_unverified = False
        try:
            for attempt in range(2):
                _raise_if_cancelled(cancellation_event)
                if time.monotonic() >= deadline:
                    raise _TransportError("timeout")
                process = _spawn_process(process_spec)
                session = _JsonLineSession(
                    process,
                    cancellation_event=cancellation_event,
                )
                auth_result = self._initialize_auth_session(
                    session,
                    refresh_token=refresh_token,
                    deadline=deadline,
                )
                account_unverified |= is_json(auth_result) and auth_result.get("authMethod") is None
                if attempt == 0:
                    override = _profile_provider_override(
                        session, auth_result, process_spec.working_directory, deadline
                    )
                    if override is not None:
                        session.close(force=True)
                        session = None
                        process = None
                        process_spec = _ProcessSpec(
                            argv=(*process_spec.argv, "-c", override),
                            environment=process_spec.environment,
                            working_directory=process_spec.working_directory,
                        )
                        # The first request already refreshed before checking its provider.
                        refresh_token = False
                        continue
                material = _auth_material_from_session_result(
                    auth_result,
                    session=session,
                    account_read_request_id=3,
                    deadline=deadline,
                )
                completed = True
                attempt_result = "success"
                return material
            raise _TransportError("protocol")
        except CodexAuthCancelled:
            attempt_result = "cancelled"
            raise
        except _TransportError as error:
            error.account_unverified |= account_unverified
            raise
        except CodexAuthError:
            raise
        except OSError:
            raise _TransportError("io", account_unverified=account_unverified) from None
        finally:
            if session is not None:
                session.close(force=not completed)
            elif process is not None:
                _terminate_process(process)
            _record_auth_fetch_attempt(
                "isolated_child",
                attempt_result,
                attempt_started,
            )

    @staticmethod
    def _initialize_auth_session(
        session: _AuthSession,
        *,
        refresh_token: bool,
        deadline: float,
    ) -> object:
        initialize_result = session.request(
            1,
            "initialize",
            {
                "clientInfo": {
                    "name": "chatgpt-meetings-local-mcp",
                    "title": "Meetings Local Runtime",
                    "version": "0.1.1",
                },
                "capabilities": {
                    "experimentalApi": True,
                    "requestAttestation": False,
                },
            },
            deadline=deadline,
        )
        if not isinstance(initialize_result, dict):
            raise _TransportError("protocol")
        session.notify("initialized", deadline=deadline)
        return session.request(
            2,
            "getAuthStatus",
            {
                "includeToken": True,
                "refreshToken": refresh_token,
            },
            deadline=deadline,
        )

    def _prepare_temporary_credentials(self, temporary_home: Path) -> tuple[str, Path]:
        source = self._active_codex_home / "auth.json"
        if os.name == "nt" and _harden_windows_auth_file(source):
            # Windows Codex commonly stores the active ChatGPT login in a
            # file-backed credential store. The MCP must never parse or copy
            # that file, and a temporary-home keyring lookup cannot see it.
            # Let the plugins-disabled app-server read the exact active home;
            # the child still has an isolated working directory and returns
            # only one bounded, in-memory auth response.
            return "file", self._active_codex_home
        if not _owner_only_regular_file(source):
            try:
                source.lstat()
            except FileNotFoundError:
                # Codex keyring credentials are scoped to the active home.
                return "keyring", self._active_codex_home
            except OSError:
                pass
            return "keyring", temporary_home
        # A credential-file symlink does not preserve the active Codex home's
        # authentication context. Keep that identity for the admitted file;
        # the disposable child still uses a private cwd with plugins disabled.
        return "file", self._active_codex_home

    @staticmethod
    def _environment_for(codex_home: Path) -> dict[str, str]:
        environment = dict(os.environ)
        environment["CODEX_HOME"] = str(codex_home)
        return environment


def _record_auth_fetch_attempt(
    transport: AuthFetchTransport,
    result: AuthFetchResult,
    started_at: float,
) -> None:
    duration_milliseconds = max(0, int((time.monotonic() - started_at) * 1000))
    record_auth_fetch_latency(transport, result, duration_milliseconds)


def _report_auth_failure(reason: str, requested_store: str) -> None:
    """Report a terminal child failure without credential or exception contents."""

    if (
        type(reason) is not str
        or reason not in MCP_SENTRY_AUTH_FAILURE_REASONS
        or type(requested_store) is not str
        or requested_store not in MCP_SENTRY_AUTH_REQUESTED_STORES
    ):
        return
    try:
        report_mcp_error(
            "auth", "auth", failure_reason=reason, auth_requested_store=requested_store
        )
    except Exception:
        pass
    try:
        print(
            "ChatGPT Meetings auth: "
            + json.dumps(
                {"failure_reason": reason, "auth_requested_store": requested_store},
                sort_keys=True,
            ),
            file=sys.stderr,
            flush=True,
        )
    except Exception:
        pass


@dataclass
class _AuthRefreshFlight:
    """One manager-owned auth load or refresh shared by request waiters."""

    refresh_token: bool
    previous: AuthMaterial | None
    owner_epoch: int = 0
    host_generation: int | None = None
    background: bool = False
    done: bool = False
    result: AuthMaterial | None = None
    error: CodexAuthError | None = None


class CodexAuthManager:
    """ChatGPT auth cache with protected persistence and single-flight refreshes.

    A request cancellation only stops that request from waiting. The shared
    auth operation is owned by a daemon worker and remains available to other
    backend requests.
    """

    def __init__(
        self,
        provider: ChatGPTAuthProvider | None = None,
        *,
        provider_factory: Callable[[], ChatGPTAuthProvider] = CodexAuthClient,
        clock: Callable[[], float] = time.time,
        persistent_cache: _PersistentAuthCache | None = None,
    ) -> None:
        self._provider = provider
        self._provider_factory = provider_factory
        self._clock = clock
        self._persistent_cache: _PersistentAuthCache = (
            persistent_cache if persistent_cache is not None else _default_persistent_auth_cache()
        )
        self._persistent_cache_loaded = isinstance(self._persistent_cache, _NoopAuthCache)
        self._persistent_cache_available = False
        self._condition = threading.Condition()
        self._material: AuthMaterial | None = None
        self._verified_at_unix_ms: int | None = None
        self._next_background_verification_at_unix_ms = 0
        self._flight: _AuthRefreshFlight | None = None
        self._last_refresh_error: CodexAuthError | None = None
        self._worker: threading.Thread | None = None
        self._shutdown_event = threading.Event()
        self._closed = False
        self._owner_epoch = 0
        self._host_generation: int | None = None
        self._host_owner_generation: int | None = None
        self._awaiting_auth_change = False
        self._persistent_clear_pending = False

    def begin_auth_change_session(self) -> None:
        """Fence prior credentials until the negotiated host sends its snapshot."""

        with self._condition:
            self._raise_if_closed_locked()
            self._host_generation = None
            self._host_owner_generation = None
            self._awaiting_auth_change = True
            self._invalidate_owner_locked()
            self._condition.notify_all()

    def end_auth_change_session(self) -> None:
        """Retire connection-local counters and credentials without blocking IO."""

        with self._condition:
            if self._closed:
                return
            self._host_generation = None
            self._host_owner_generation = None
            # A later client may not support notifications. It must perform
            # a fresh ordinary auth read rather than wait for a missing event.
            self._awaiting_auth_change = False
            self._invalidate_owner_locked()
            self._condition.notify_all()

    def handle_auth_changed(
        self,
        *,
        generation: int,
        owner_generation: int,
        on_owner_changed: Callable[[], None] | None = None,
    ) -> None:
        """Re-read host auth, retaining a usable bearer only for the same owner."""

        start: _AuthRefreshFlight | None = None
        with self._condition:
            if self._closed:
                return
            if self._host_generation is not None and generation <= self._host_generation:
                return
            if owner_generation != self._host_owner_generation:
                if self._host_owner_generation is not None and on_owner_changed is not None:
                    # Cancel requests admitted for the previous owner before
                    # any waiter can acquire replacement credentials. This
                    # callback must only update in-memory cancellation state.
                    on_owner_changed()
                self._invalidate_owner_locked()
            self._host_generation = generation
            self._host_owner_generation = owner_generation
            self._awaiting_auth_change = False
            # Notifications describe already changed credentials. Forcing a
            # refresh here could itself generate another host notification.
            if self._flight is None:
                start = self._begin_flight_locked(
                    refresh_token=False,
                    background=self._is_valid(self._material, self._now_ms()),
                )
            self._condition.notify_all()
        if start is not None:
            self._start_flight(start)

    def _invalidate_owner_locked(self) -> None:
        self._owner_epoch += 1
        self._material = None
        self._last_refresh_error = None
        self._verified_at_unix_ms = None
        self._next_background_verification_at_unix_ms = 0
        # Protected storage is retired by the auth worker, never on the MCP
        # reader. No subsequent load in this process may restore that entry.
        self._persistent_cache_loaded = True
        self._persistent_cache_available = False
        self._persistent_clear_pending = True

    def _wait_for_initial_auth_change_locked(
        self, cancellation_event: threading.Event | None
    ) -> None:
        while self._awaiting_auth_change:
            self._raise_if_closed_locked()
            _raise_if_cancelled(cancellation_event)
            self._condition.wait(timeout=0.05)

    def warm(self) -> bool:
        """Warm missing credentials or revalidate a stale protected-cache entry."""

        with self._condition:
            self._raise_if_closed_locked()
            now_ms = self._now_ms()
            material = self._material
            if self._flight is not None or self._awaiting_auth_change:
                return False
            if self._is_valid(material, now_ms):
                if self._requires_synchronous_verification_locked(now_ms):
                    start = self._begin_flight_locked(refresh_token=False)
                elif self._needs_background_verification_locked(now_ms):
                    start = self._begin_flight_locked(refresh_token=False, background=True)
                else:
                    return False
            else:
                start = self._begin_flight_locked(refresh_token=material is not None)
        self._start_flight(start)
        return True

    def close(
        self,
        *,
        join_timeout_seconds: float = AUTH_MANAGER_SHUTDOWN_GRACE_SECONDS,
    ) -> None:
        """Cancel process-owned auth work without deleting the protected cache."""

        with self._condition:
            self._closed = True
            self._shutdown_event.set()
            self._material = None
            self._last_refresh_error = None
            self._verified_at_unix_ms = None
            worker = self._worker
            self._condition.notify_all()
        if (
            worker is not None
            and worker is not threading.current_thread()
            and worker.ident is not None
        ):
            worker.join(timeout=max(0.0, join_timeout_seconds))
        with self._condition:
            provider = self._provider
            self._provider = None
        if isinstance(provider, _ClosableAuthProvider):
            provider.close()

    def get_chatgpt_auth(
        self,
        *,
        refresh_token: bool = False,
        cancellation_event: threading.Event | None = None,
    ) -> AuthMaterial:
        if type(refresh_token) is not bool:
            raise TypeError("refresh_token must be a bool")
        with self._condition:
            self._raise_if_closed_locked()
        if refresh_token:
            return self._get_forced(cancellation_event)
        return self._get_normal(cancellation_event)

    def peek_cached_chatgpt_auth(self) -> AuthMaterial | None:
        """Read valid process-local auth without loading, refreshing, or waiting."""

        with self._condition:
            material = self._material
            now_ms = self._now_ms()
            if (
                self._closed
                or not self._is_valid(material, now_ms)
                or self._requires_synchronous_verification_locked(now_ms)
            ):
                return None
            return material

    def peek_auth_diagnostics(self) -> AuthCacheDiagnostics:
        """Return safe cache state without loading, refreshing, or exposing auth."""

        with self._condition:
            material = self._material
            now_ms = self._now_ms()
            if (
                self._closed
                or not self._is_valid(material, now_ms)
                or self._requires_synchronous_verification_locked(now_ms)
            ):
                return {"cached": False, "storage": "none", "expiresAtUnixMs": None}
            assert material is not None
            return {
                "cached": self._persistent_cache_available,
                "storage": "protected" if self._persistent_cache_available else "memory",
                "expiresAtUnixMs": material.expires_at_unix_ms,
            }

    def peek_diagnostic_scope(
        self, *, expected_account: tuple[str, str | None] | None = None
    ) -> tuple[int, str | None]:
        """Fence process-local diagnostic history without exposing or refreshing auth.

        This opaque comparison key is never serialized into logs or telemetry.
        The epoch also separates a return to the same account after host changes.
        An expected account restricts the owner to the exact authorized subject.
        """
        with self._condition:
            material = self.peek_cached_chatgpt_auth()
            if expected_account is not None and (
                material is None or (material.account_id, material.subject) != expected_account
            ):
                return self._owner_epoch, None
            owner = (
                hashlib.sha256(
                    json.dumps([material.account_id, material.subject]).encode("utf-8")
                ).hexdigest()
                if material is not None
                else None
            )
            return self._owner_epoch, owner

    def refresh_after_unauthorized(
        self,
        rejected: AuthMaterial,
        *,
        cancellation_event: threading.Event | None = None,
    ) -> AuthMaterial:
        """Refresh only if the rejected token is still the cached generation."""

        while True:
            _raise_if_cancelled(cancellation_event)
            start: _AuthRefreshFlight | None = None
            force_after_wait = False
            with self._condition:
                self._raise_if_closed_locked()
                self._wait_for_initial_auth_change_locked(cancellation_event)
                flight = self._flight
                if flight is None:
                    now_ms = self._now_ms()
                    material = self._material
                    if (
                        self._is_valid(material, now_ms)
                        and material is not None
                        and material.token != rejected.token
                    ):
                        return material
                    flight = self._begin_flight_locked(refresh_token=True)
                    start = flight
                elif not flight.refresh_token:
                    force_after_wait = True
            if start is not None:
                self._start_flight(start)
            result = self._wait_for_flight(flight, cancellation_event)
            if not force_after_wait:
                return result

    def _get_normal(
        self,
        cancellation_event: threading.Event | None,
    ) -> AuthMaterial:
        while True:
            result = self._get_normal_once(cancellation_event)
            with self._condition:
                self._raise_if_closed_locked()
                if result is self._material:
                    return result

    def _get_normal_once(
        self,
        cancellation_event: threading.Event | None,
    ) -> AuthMaterial:
        _raise_if_cancelled(cancellation_event)
        start: _AuthRefreshFlight | None = None
        immediate: AuthMaterial | None = None
        with self._condition:
            self._raise_if_closed_locked()
            self._wait_for_initial_auth_change_locked(cancellation_event)
            now_ms = self._now_ms()
            material = self._material
            flight = self._flight
            if self._is_valid(material, now_ms):
                assert material is not None
                if self._requires_synchronous_verification_locked(now_ms):
                    if flight is None:
                        flight = self._begin_flight_locked(refresh_token=False)
                        start = flight
                    elif flight.background:
                        flight.background = False
                elif flight is None:
                    if self._needs_background_verification_locked(now_ms):
                        flight = self._begin_flight_locked(refresh_token=False, background=True)
                        start = flight
                    immediate = material
                elif flight.background:
                    immediate = material
            elif flight is None:
                flight = self._begin_flight_locked(refresh_token=material is not None)
                start = flight
        if start is not None:
            self._start_flight(start)
        if immediate is not None:
            return immediate
        assert flight is not None
        return self._wait_for_flight(flight, cancellation_event)

    def _get_forced(
        self,
        cancellation_event: threading.Event | None,
    ) -> AuthMaterial:
        while True:
            _raise_if_cancelled(cancellation_event)
            start: _AuthRefreshFlight | None = None
            force_after_wait = False
            with self._condition:
                self._raise_if_closed_locked()
                self._wait_for_initial_auth_change_locked(cancellation_event)
                flight = self._flight
                if flight is None:
                    flight = self._begin_flight_locked(refresh_token=True)
                    start = flight
                elif not flight.refresh_token:
                    force_after_wait = True
            if start is not None:
                self._start_flight(start)
            result = self._wait_for_flight(flight, cancellation_event)
            if not force_after_wait:
                return result

    def _begin_flight_locked(
        self,
        *,
        refresh_token: bool,
        background: bool = False,
    ) -> _AuthRefreshFlight:
        assert self._flight is None
        flight = _AuthRefreshFlight(
            refresh_token=refresh_token,
            previous=self._material,
            owner_epoch=self._owner_epoch,
            host_generation=self._host_generation,
            background=background,
        )
        self._flight = flight
        return flight

    def _start_flight(self, flight: _AuthRefreshFlight) -> None:
        try:
            worker = threading.Thread(
                target=self._run_flight,
                args=(flight,),
                name="chatgpt-meetings-auth-refresh",
                daemon=True,
            )
        except (OSError, RuntimeError):
            self._fail_to_start_flight(flight)
            return
        start_error = False
        with self._condition:
            if self._closed:
                start_error = True
            else:
                self._worker = worker
                try:
                    worker.start()
                except (OSError, RuntimeError):
                    self._worker = None
                    start_error = True
        if start_error:
            self._fail_to_start_flight(flight)

    def _fail_to_start_flight(self, flight: _AuthRefreshFlight) -> None:
        # No worker exists to retry a superseded revision. Finish atomically
        # so a notification racing thread startup cannot strand its waiters.
        with self._condition:
            if (
                flight.background
                and self._is_valid(self._material, self._now_ms())
                and not self._requires_synchronous_verification_locked(self._now_ms())
            ):
                flight.result = self._material
            else:
                self._material = None
                self._verified_at_unix_ms = None
                self._persistent_cache_available = False
                self._persistent_cache_loaded = True
                self._persistent_clear_pending = True
                flight.error = CodexAuthUnavailable("Codex authentication could not be completed")
            flight.owner_epoch = self._owner_epoch
            flight.host_generation = self._host_generation
            flight.done = True
            if not self._closed:
                self._last_refresh_error = flight.error
            if self._flight is flight:
                self._flight = None
            self._condition.notify_all()

    def _run_flight(self, flight: _AuthRefreshFlight) -> None:
        while not self._run_flight_once(flight):
            # Coalesce changes observed during IO into one subsequent read.
            # Keep the same flight so all admitted waiters follow the new owner.
            pass

    def _retarget_flight_locked(self, flight: _AuthRefreshFlight) -> None:
        flight.refresh_token = False
        flight.previous = self._material
        flight.background = flight.background and self._material is not None
        flight.owner_epoch = self._owner_epoch
        flight.host_generation = self._host_generation
        flight.result = None
        flight.error = None

    def _flight_is_current_locked(self, flight: _AuthRefreshFlight) -> bool:
        return (
            flight.owner_epoch == self._owner_epoch
            and flight.host_generation == self._host_generation
            and not self._awaiting_auth_change
        )

    def _run_flight_once(self, flight: _AuthRefreshFlight) -> bool:
        try:
            with self._condition:
                self._wait_for_initial_auth_change_locked(self._shutdown_event)
                self._raise_if_closed_locked()
                if not self._flight_is_current_locked(flight):
                    self._retarget_flight_locked(flight)
                clear_persistent = self._persistent_clear_pending
                self._persistent_clear_pending = False
            if clear_persistent:
                self._clear_persistent_cache()
            if not flight.refresh_token and not self._persistent_cache_loaded:
                cached = self._load_persistent_entry()
                if cached is not None:
                    now_ms = self._now_ms()
                    if self._is_valid(
                        cached.material, now_ms
                    ) and 0 <= now_ms - cached.verified_at_unix_ms < int(
                        AUTH_CACHE_MAXIMUM_AGE_SECONDS * 1000
                    ):
                        self._persistent_cache_available = True
                        completed = self._complete_flight(
                            flight,
                            material=cached.material,
                            verified_at_unix_ms=cached.verified_at_unix_ms,
                        )
                        if completed and now_ms - cached.verified_at_unix_ms >= int(
                            AUTH_CACHE_FRESH_SECONDS * 1000
                        ):
                            try:
                                self.warm()
                            except CodexAuthError:
                                pass
                        return completed
                    self._clear_persistent_cache()
            self._persistent_cache_loaded = True
            provider = self._provider
            if provider is None:
                provider = self._provider_factory()
                with self._condition:
                    closed = self._closed
                    if not closed:
                        self._provider = provider
                if closed:
                    if isinstance(provider, _ClosableAuthProvider):
                        provider.close()
                    raise CodexAuthCancelled("Codex authentication was cancelled")
            material = provider.get_chatgpt_auth(
                refresh_token=flight.refresh_token,
                cancellation_event=self._shutdown_event,
            )
            if flight.previous is not None and (
                material.account_id,
                material.subject,
            ) != (flight.previous.account_id, flight.previous.subject):
                raise CodexAuthAccountChanged("Codex authentication account changed")
            if not self._is_valid(material, self._now_ms()):
                raise CodexAuthUnavailable(
                    "Codex authentication data is expired", failure_reason="session_unverified"
                )
        except CodexAuthCancelled:
            return self._complete_flight(
                flight,
                error=CodexAuthUnavailable("Codex authentication could not be completed"),
            )
        except CodexAuthError as error:
            return self._complete_flight(flight, error=error)
        except Exception:
            return self._complete_flight(
                flight,
                error=CodexAuthUnavailable("Codex authentication could not be completed"),
            )
        else:
            with self._condition:
                if self._closed:
                    return self._complete_flight(
                        flight,
                        error=CodexAuthUnavailable("Codex authentication could not be completed"),
                    )
                if not self._flight_is_current_locked(flight):
                    return False
            verified_at_unix_ms = self._now_ms()
            try:
                saved = self._persistent_cache.save(material, verified_at_unix_ms)
            except Exception:
                saved = False
            if saved:
                self._persistent_cache_available = True
            elif not isinstance(self._persistent_cache, _NoopAuthCache):
                _report_auth_cache_failure("write")
            return self._complete_flight(
                flight,
                material=material,
                verified_at_unix_ms=verified_at_unix_ms,
            )

    def _complete_flight(
        self,
        flight: _AuthRefreshFlight,
        *,
        material: AuthMaterial | None = None,
        error: CodexAuthError | None = None,
        verified_at_unix_ms: int | None = None,
    ) -> bool:
        clear_persistent = False
        with self._condition:
            if not self._closed and not self._flight_is_current_locked(flight):
                return False
            if (
                error is None
                and material is not None
                and flight.previous is not None
                and (material.account_id, material.subject)
                != (flight.previous.account_id, flight.previous.subject)
            ):
                error = CodexAuthAccountChanged("Codex authentication account changed")
            if self._closed:
                self._material = None
                self._verified_at_unix_ms = None
                flight.error = CodexAuthUnavailable("Codex authentication could not be completed")
            elif error is None:
                assert material is not None
                self._material = material
                self._verified_at_unix_ms = verified_at_unix_ms
                self._next_background_verification_at_unix_ms = 0
                flight.result = material
            elif (
                flight.background
                and isinstance(error, CodexAuthUnavailable)
                and not isinstance(error, CodexAuthAccountUnverified)
                and flight.previous is not None
                and self._is_valid(flight.previous, self._now_ms())
                and not self._requires_synchronous_verification_locked(self._now_ms())
            ):
                self._material = flight.previous
                self._next_background_verification_at_unix_ms = self._now_ms() + int(
                    AUTH_CACHE_FRESH_SECONDS * 1000
                )
                flight.result = flight.previous
            else:
                self._material = None
                self._verified_at_unix_ms = None
                clear_persistent = True
                if isinstance(error, CodexAuthUnavailable) and not isinstance(
                    error, CodexAuthAccountUnverified
                ):
                    error = CodexAuthAccountUnverified(
                        "ChatGPT account could not be verified", failure_reason=error.failure_reason
                    )
                flight.error = _copy_auth_error(error)
        if clear_persistent:
            self._clear_persistent_cache()
        with self._condition:
            if not self._closed and not self._flight_is_current_locked(flight):
                return False
            flight.done = True
            if not self._closed:
                self._last_refresh_error = flight.error
            if self._flight is flight:
                self._flight = None
            if self._worker is threading.current_thread():
                self._worker = None
            self._condition.notify_all()
        return True

    def _load_persistent_entry(self) -> _PersistedAuthEntry | None:
        self._persistent_cache_loaded = True
        try:
            return self._persistent_cache.load()
        except Exception:
            _report_auth_cache_failure("read")
            return None

    def _clear_persistent_cache(self) -> None:
        self._persistent_cache_available = False
        try:
            self._persistent_cache.clear()
        except Exception:
            _report_auth_cache_failure("delete")

    def _requires_synchronous_verification_locked(self, now_ms: int) -> bool:
        if not self._persistent_cache_available or self._verified_at_unix_ms is None:
            return False
        age_ms = now_ms - self._verified_at_unix_ms
        return age_ms < 0 or age_ms >= int(AUTH_CACHE_MAXIMUM_AGE_SECONDS * 1000)

    def _needs_background_verification_locked(self, now_ms: int) -> bool:
        if not self._persistent_cache_available or self._verified_at_unix_ms is None:
            return False
        age_ms = now_ms - self._verified_at_unix_ms
        return (
            int(AUTH_CACHE_FRESH_SECONDS * 1000)
            <= age_ms
            < int(AUTH_CACHE_MAXIMUM_AGE_SECONDS * 1000)
            and now_ms >= self._next_background_verification_at_unix_ms
        )

    def _wait_for_flight(
        self,
        flight: _AuthRefreshFlight,
        cancellation_event: threading.Event | None,
    ) -> AuthMaterial:
        while True:
            _raise_if_cancelled(cancellation_event)
            start: _AuthRefreshFlight | None = None
            with self._condition:
                self._raise_if_closed_locked()
                self._wait_for_initial_auth_change_locked(cancellation_event)
                if flight.done:
                    if flight.owner_epoch != self._owner_epoch:
                        if self._flight is None:
                            if self._last_refresh_error is not None:
                                raise _copy_auth_error(self._last_refresh_error) from None
                            material = self._material
                            if (
                                material is not None
                                and self._is_valid(material, self._now_ms())
                                and not self._requires_synchronous_verification_locked(
                                    self._now_ms()
                                )
                            ):
                                return material
                            start = self._begin_flight_locked(refresh_token=False)
                        assert self._flight is not None
                        flight = self._flight
                    else:
                        if flight.error is not None:
                            raise _copy_auth_error(flight.error) from None
                        assert flight.result is not None
                        return flight.result
                if start is None:
                    self._condition.wait(timeout=0.05)
            if start is not None:
                self._start_flight(start)

    def _now_ms(self) -> int:
        return int(self._clock() * 1000)

    @staticmethod
    def _is_valid(material: AuthMaterial | None, now_ms: int) -> bool:
        return (
            material is not None
            and type(material.expires_at_unix_ms) is int
            and now_ms < material.expires_at_unix_ms
        )

    def _raise_if_closed_locked(self) -> None:
        if self._closed:
            raise CodexAuthUnavailable("Codex authentication could not be completed")


_PROCESS_AUTH_MANAGER_LOCK = threading.Lock()
_process_auth_manager: CodexAuthManager | None = None


def get_process_auth_manager() -> CodexAuthManager:
    """Return the single auth manager shared by this MCP process."""

    global _process_auth_manager
    with _PROCESS_AUTH_MANAGER_LOCK:
        if _process_auth_manager is None:
            _process_auth_manager = CodexAuthManager()
        return _process_auth_manager


def warm_process_auth() -> bool:
    """Best-effort background auth warm-up for MCP process startup."""

    return get_process_auth_manager().warm()


def close_process_auth() -> None:
    """Shut down the existing process manager without creating one."""

    global _process_auth_manager
    with _PROCESS_AUTH_MANAGER_LOCK:
        manager = _process_auth_manager
        _process_auth_manager = None
    if manager is not None:
        manager.close()


def refresh_chatgpt_auth_after_unauthorized(
    provider: ChatGPTAuthProvider,
    rejected: AuthMaterial,
    *,
    cancellation_event: threading.Event | None = None,
) -> AuthMaterial:
    """Use generation-aware refresh when the provider supports it."""

    if isinstance(provider, _RefreshableChatGPTAuthProvider):
        return provider.refresh_after_unauthorized(
            rejected,
            cancellation_event=cancellation_event,
        )
    return provider.get_chatgpt_auth(
        refresh_token=True,
        cancellation_event=cancellation_event,
    )


def _copy_auth_error(error: CodexAuthError) -> CodexAuthError:
    return type(error)(str(error), failure_reason=error.failure_reason)


def _resolve_codex_path(
    explicit_path: str | os.PathLike[str] | None,
    *,
    prefer_platform_helpers: bool = True,
) -> str:
    """Resolve one helper; retry-capable auth explicitly opts into PATH-first discovery."""

    candidate: str | None
    if explicit_path is not None:
        candidate = os.fspath(explicit_path)
    else:
        intentional_override = (
            os.environ.get("CODEX_BIN", "").strip() if sys.platform == "darwin" else ""
        )
        candidate = intentional_override or _environment_codex_path(
            os.environ.get("CODEX_CLI_PATH")
        )
        if not candidate:
            candidate = next(
                _discovered_codex_paths(prefer_platform_helpers=prefer_platform_helpers), None
            )
    if not candidate:
        raise CodexAuthUnavailable("Codex app-server is unavailable")

    resolved = shutil.which(candidate) if os.path.sep not in candidate else candidate
    if not resolved:
        raise CodexAuthUnavailable("Codex app-server is unavailable")
    path = Path(resolved).expanduser()
    try:
        metadata = path.stat()
    except OSError:
        raise CodexAuthUnavailable("Codex app-server is unavailable") from None
    if not stat.S_ISREG(metadata.st_mode) or not os.access(path, os.X_OK):
        raise CodexAuthError("Codex app-server is unavailable")
    return str(path.resolve())


def _environment_codex_path(candidate: str | None) -> str | None:
    if not candidate:
        return None
    try:
        path = Path(candidate).expanduser()
        if not os.path.dirname(candidate) and not path.is_dir():
            return next(_path_codex_paths(candidate), None)
        resolved = str(path)
        if _is_windows_platform():
            return _windows_directory_codex_path(resolved)
        if sys.platform == "darwin":
            resolved = _macos_directory_codex_path(resolved)
            if not resolved or _is_macos_dotslash_path(resolved):
                return None
        path = Path(resolved).expanduser()
        if path.is_dir():
            path /= "codex"
        if stat.S_ISREG(path.stat().st_mode) and os.access(path, os.X_OK):
            return str(path)
    except (OSError, RuntimeError, ValueError):
        pass
    return None


def _discovered_codex_paths(*, prefer_platform_helpers: bool = False) -> Generator[str, None, None]:
    """Preserve platform priority for consumers that cannot retry PATH helpers."""

    configured = os.environ.get("CODEX_CLI_PATH", "")
    if sys.platform == "darwin" and configured:
        try:
            directory = Path(configured).expanduser()
            if directory.is_dir():
                for candidate in _macos_resources_codex_paths(directory):
                    if not _is_macos_dotslash_path(candidate) and os.access(candidate, os.X_OK):
                        yield candidate
        except (OSError, RuntimeError, ValueError):
            pass
    if prefer_platform_helpers and sys.platform == "darwin":
        # The pinned companion cannot recover a failed PATH launcher through a
        # nested host bundle. Keep the initiating app's appended helper first.
        for candidate in _path_codex_paths(reverse_path=True):
            if _macos_codex_app_bundle(Path(candidate)) is not None:
                yield candidate
    if not prefer_platform_helpers:
        yield from _path_codex_paths()
    if _is_windows_platform():
        # Windows native auth also binds one helper before Python auth warms.
        yield from _windows_cached_codex_paths()
    elif sys.platform == "darwin":
        for candidate in _macos_bundled_codex_paths():
            if not _is_macos_dotslash_path(candidate) and os.access(candidate, os.X_OK):
                yield candidate
    if prefer_platform_helpers:
        yield from _path_codex_paths()


def _fallback_codex_paths(selected_path: str) -> tuple[str, ...]:
    """Return remaining distinct helpers after an app-server capability failure."""

    try:
        selected = Path(selected_path).resolve(strict=False)
    except (OSError, RuntimeError, ValueError):
        selected = None
    fallbacks: list[str] = []
    seen: set[str] = set()
    for candidate in _discovered_codex_paths():
        try:
            resolved = Path(candidate).resolve(strict=False)
        except (OSError, RuntimeError, ValueError):
            continue
        if resolved == selected or str(resolved) in seen:
            continue
        seen.add(str(resolved))
        fallbacks.append(str(resolved))
    return tuple(fallbacks)


def _macos_codex_app_bundle(executable: Path) -> Path | None:
    """Find the desktop bundle for either supported bundled CLI layout."""

    for relative in _MACOS_BUNDLED_CODEX_RELATIVE_PATHS:
        suffix = executable.parts[-len(relative.parts) :]
        if tuple(part.casefold() for part in suffix) == tuple(
            part.casefold() for part in relative.parts
        ):
            return executable.parents[len(relative.parts) - 1]
    return None


def _path_codex_paths(
    command: str = "codex", *, reverse_path: bool = False
) -> Generator[str, None, None]:
    """Yield usable CLI helpers in the supplied PATH order."""

    windows = _is_windows_platform()
    # Python 3.10/3.11 do not expand PATHEXT for directory-qualified commands.
    names = (
        (command, f"{command}.exe")
        if windows and not command.lower().endswith(".exe")
        else (command,)
    )
    seen: set[str] = set()
    directories = os.get_exec_path()
    if reverse_path:
        directories.reverse()
    for directory in directories:
        for name in names:
            try:
                # A qualified command avoids Windows which() injecting the current directory.
                candidate = shutil.which(os.path.join(directory or os.curdir, name))
                if not candidate:
                    continue
                if windows:
                    candidate = _windows_directory_codex_path(candidate)
                    if not candidate:
                        continue
                elif sys.platform == "darwin" and _is_macos_dotslash_path(candidate):
                    continue
                path = Path(candidate).expanduser()
                if not stat.S_ISREG(path.stat().st_mode):
                    continue
                resolved = str(path.resolve())
            except (OSError, RuntimeError, ValueError):
                continue
            if resolved not in seen:
                seen.add(resolved)
                yield resolved


def _macos_resources_codex_paths(resources: Path) -> tuple[str, ...]:
    nested = resources / _MACOS_NESTED_CODEX_PATH
    candidates: list[str] = []
    try:
        # Discovery must not follow a replaced nested app or helper outside the bundle.
        components = (
            resources,
            *(resources / part for part in _MACOS_NESTED_CODEX_PATH.parents[:-1]),
        )
        if (
            all(
                not component.is_symlink() and stat.S_ISDIR(component.lstat().st_mode)
                for component in components
            )
            and not nested.is_symlink()
            and stat.S_ISREG(nested.lstat().st_mode)
            and os.access(nested, os.X_OK)
        ):
            candidates.append(str(nested))
    except OSError:
        pass
    candidates.append(str(resources / "codex"))
    return tuple(candidates)


def _macos_bundled_codex_paths() -> tuple[str, ...]:
    app_names = (
        "ChatGPT (Nightly)",
        "ChatGPT (Alpha)",
        "ChatGPT",
        "Codex (Alpha)",
        "Codex",
    )
    roots = (Path("/Applications"), Path.home() / "Applications")
    candidates = tuple(
        candidate
        for root in roots
        for name in app_names
        for candidate in _macos_resources_codex_paths(
            root / f"{name}.app" / "Contents" / "Resources"
        )
    )
    return _macos_ranked_bundled_codex_paths(candidates)


def _macos_ranked_bundled_codex_paths(
    candidates: tuple[str, ...],
) -> tuple[str, ...]:
    """Prefer the newest readable app bundle without executing any helper."""

    ranked = [
        (_macos_bundle_version_key(candidate), index, candidate)
        for index, candidate in enumerate(candidates)
    ]
    ranked.sort(
        key=lambda item: (item[0] is not None, item[0] or ((), ()), -item[1]),
        reverse=True,
    )
    return tuple(candidate for _, _, candidate in ranked)


def _macos_bundle_version_key(
    candidate: str,
) -> tuple[tuple[int, ...], tuple[int, ...]] | None:
    app = _macos_codex_app_bundle(Path(candidate))
    if app is None:
        return None
    # The nested CLI has its own version; rank by the initiating desktop app.
    info_path = app / "Contents" / "Info.plist"
    try:
        metadata = info_path.lstat()
        if (
            not stat.S_ISREG(metadata.st_mode)
            or info_path.is_symlink()
            or metadata.st_size > MAXIMUM_BUNDLE_INFO_BYTES
        ):
            return None
        flags = (
            os.O_RDONLY
            | getattr(os, "O_CLOEXEC", 0)
            | getattr(os, "O_NOFOLLOW", 0)
            | getattr(os, "O_NONBLOCK", 0)
        )
        descriptor = os.open(info_path, flags)
        try:
            opened = os.fstat(descriptor)
            if (
                not stat.S_ISREG(opened.st_mode)
                or opened.st_dev != metadata.st_dev
                or opened.st_ino != metadata.st_ino
                or opened.st_size != metadata.st_size
            ):
                return None
            payload = os.read(descriptor, MAXIMUM_BUNDLE_INFO_BYTES + 1)
        finally:
            os.close(descriptor)
        if len(payload) > MAXIMUM_BUNDLE_INFO_BYTES:
            return None
        decoded_info: object = plistlib.loads(payload)
    except (
        OSError,
        ExpatError,
        plistlib.InvalidFileException,
        OverflowError,
        RecursionError,
        TypeError,
        ValueError,
    ):
        return None
    if not is_json(decoded_info):
        return None
    info = decoded_info

    build = _macos_bundle_version_components(info.get("CFBundleVersion"))
    short = _macos_bundle_version_components(info.get("CFBundleShortVersionString"))
    if build is None and short is None:
        return None
    return build or short or (), short or ()


def _macos_bundle_version_components(value: object) -> tuple[int, ...] | None:
    if isinstance(value, bool) or not isinstance(value, (int, str)):
        return None
    raw = str(value)
    try:
        encoded = raw.encode("utf-8")
    except UnicodeError:
        return None
    if not encoded or len(encoded) > MAXIMUM_BUNDLE_VERSION_BYTES:
        return None
    if re.fullmatch(r"[A-Za-z0-9._+\-]+", raw, re.ASCII) is None:
        return None
    components = re.findall(r"[0-9]+", raw, re.ASCII)
    if not components or len(components) > 32:
        return None
    return tuple(int(component) for component in components)


def _macos_directory_codex_path(candidate: str) -> str | None:
    try:
        path = Path(candidate).expanduser()
        metadata = path.stat()
    except (OSError, RuntimeError, ValueError):
        return None
    if not stat.S_ISDIR(metadata.st_mode):
        return str(path)
    for helper in _macos_resources_codex_paths(path):
        if not _is_macos_dotslash_path(helper) and os.access(helper, os.X_OK):
            return helper
    return None


def _is_macos_dotslash_path(candidate: str) -> bool:
    # A runnable Codex image can live in a source tree or any cache directory.
    # Reject launcher manifests by their contents, not their installation path.
    path = Path(candidate).expanduser()
    try:
        path = path.resolve(strict=False)
    except (OSError, RuntimeError):
        return True
    try:
        metadata = path.stat()
        if not stat.S_ISREG(metadata.st_mode):
            return True
        with path.open("rb") as handle:
            first_line = handle.readline(256).lower()
    except OSError:
        return True
    return first_line.startswith(b"#!") and b"dotslash" in first_line


def _windows_cached_codex_paths() -> tuple[str, ...]:
    local = os.environ.get("LOCALAPPDATA", "").strip()
    if not local:
        return ()
    root = Path(local) / "OpenAI" / "Codex" / "bin"
    reparse_point = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    candidates: list[tuple[int, str, Path]] = []
    try:
        root_metadata = root.lstat()
        if (
            not stat.S_ISDIR(root_metadata.st_mode)
            or root.is_symlink()
            or getattr(root_metadata, "st_file_attributes", 0) & reparse_point
        ):
            return ()
        with os.scandir(root) as entries:
            for scanned, entry in enumerate(entries):
                if scanned >= MAXIMUM_CODEX_CACHE_ENTRIES:
                    break
                if _CODEX_CACHE_KEY_PATTERN.fullmatch(entry.name) is None:
                    continue
                directory = root / entry.name
                executable = directory / "codex.exe"
                try:
                    directory_metadata = directory.lstat()
                    metadata = executable.lstat()
                except OSError:
                    # An interrupted Codex upgrade can leave one empty cache
                    # key beside the last runnable runtime.
                    continue
                if (
                    not stat.S_ISDIR(directory_metadata.st_mode)
                    or directory.is_symlink()
                    or getattr(directory_metadata, "st_file_attributes", 0) & reparse_point
                    or not stat.S_ISREG(metadata.st_mode)
                    or executable.is_symlink()
                    or getattr(metadata, "st_file_attributes", 0) & reparse_point
                    or not 2 <= metadata.st_size <= MAXIMUM_CODEX_CLI_BYTES
                    or not os.access(executable, os.X_OK)
                ):
                    continue
                try:
                    with executable.open("rb") as source:
                        opened = os.fstat(source.fileno())
                        header = source.read(2)
                except OSError:
                    continue
                if (
                    not stat.S_ISREG(opened.st_mode)
                    or opened.st_size != metadata.st_size
                    or opened.st_dev != metadata.st_dev
                    or opened.st_ino
                    and metadata.st_ino
                    and opened.st_ino != metadata.st_ino
                    or header != b"MZ"
                ):
                    continue
                candidates.append((metadata.st_mtime_ns, entry.name.casefold(), executable))
    except OSError:
        return ()
    if not candidates:
        return ()
    candidates.sort(reverse=True)
    return tuple(str(candidate[2].resolve()) for candidate in candidates)


def _windows_directory_codex_path(candidate: str) -> str | None:
    # Store resources can pass metadata checks but fail CreateProcess with Access denied.
    if "/windowsapps/" in candidate.replace("\\", "/").casefold():
        return None
    reparse_point = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    try:
        path = Path(candidate).expanduser()
        metadata = path.lstat()
        if path.is_symlink() or getattr(metadata, "st_file_attributes", 0) & reparse_point:
            return None
        if stat.S_ISDIR(metadata.st_mode):
            path /= "codex.exe"
            metadata = path.lstat()
        if (
            not stat.S_ISREG(metadata.st_mode)
            or path.is_symlink()
            or getattr(metadata, "st_file_attributes", 0) & reparse_point
            or not 2 <= metadata.st_size <= MAXIMUM_CODEX_CLI_BYTES
            or not os.access(path, os.X_OK)
        ):
            return None
        with path.open("rb") as source:
            opened = os.fstat(source.fileno())
            header = source.read(2)
    except (OSError, RuntimeError, ValueError):
        return None
    if (
        not stat.S_ISREG(opened.st_mode)
        or opened.st_size != metadata.st_size
        or opened.st_dev != metadata.st_dev
        or opened.st_ino
        and metadata.st_ino
        and opened.st_ino != metadata.st_ino
        or header != b"MZ"
    ):
        return None
    return str(path.resolve())


def _is_windows_platform() -> bool:
    return sys.platform != "darwin" and (os.name == "nt" or sys.platform == "win32")


def _active_codex_home(
    explicit_home: str | os.PathLike[str] | None,
) -> Path:
    raw_home = (
        os.fspath(explicit_home)
        if explicit_home is not None
        else os.environ.get("CODEX_HOME") or str(Path.home() / ".codex")
    )
    path = Path(raw_home).expanduser()
    if not path.is_absolute():
        raise CodexAuthError("Codex app-server is unavailable")
    if os.name == "nt":
        # Preserve the lexical path so a junction/symlink ancestor remains
        # visible to the auth-file guard. Resolving here would erase it.
        if ".." in path.parts:
            raise CodexAuthError("Codex app-server is unavailable")
        return path
    return path.resolve(strict=False)


def _owner_only_regular_file(path: Path) -> bool:
    try:
        metadata = path.lstat()
    except OSError:
        return False
    if not stat.S_ISREG(metadata.st_mode):
        return False
    if metadata.st_mode & (stat.S_IRWXG | stat.S_IRWXO):
        return False
    if not metadata.st_mode & stat.S_IRUSR:
        return False
    getuid = getattr(os, "getuid", None)
    return getuid is not None and metadata.st_uid == getuid()


def _safe_windows_auth_file(path: Path) -> bool:
    """Allow the app-server to use one bounded, non-redirected auth file."""

    metadata = _windows_auth_file_metadata(path)
    if metadata is None:
        return False
    try:
        return windows_acl_is_private(path)
    except OSError:
        return False


def _windows_auth_file_metadata(path: Path) -> os.stat_result | None:
    reparse_point = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    try:
        metadata = path.lstat()
        if any(
            candidate.is_symlink()
            or getattr(candidate, "is_junction", lambda: False)()
            or getattr(candidate.lstat(), "st_file_attributes", 0) & reparse_point
            for candidate in (path, *path.parents)
        ):
            return None
    except OSError:
        return None
    if not stat.S_ISREG(metadata.st_mode) or stat.S_ISLNK(metadata.st_mode):
        return None
    if not 0 < metadata.st_size <= MAXIMUM_AUTH_FILE_BYTES:
        return None
    if getattr(metadata, "st_nlink", 1) != 1:
        return None
    return metadata


def _harden_windows_auth_file(path: Path) -> bool:
    """Remove inherited grants before the plugins-disabled child uses auth.json."""

    before = _windows_auth_file_metadata(path)
    if before is None:
        return False
    if _safe_windows_auth_file(path):
        return True
    system_root = os.environ.get("SystemRoot", "").strip()
    if not system_root:
        return False
    system32 = Path(system_root) / "System32"
    whoami = system32 / "whoami.exe"
    icacls = system32 / "icacls.exe"
    try:
        identity = subprocess.run(
            [str(whoami), "/user", "/fo", "csv", "/nh"],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
            timeout=WINDOWS_ACL_TIMEOUT_SECONDS,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
        if identity.returncode != 0 or len(identity.stdout) > 16 * 1024:
            return False
        matches = _WINDOWS_SID_PATTERN.findall(identity.stdout.decode("utf-8", errors="replace"))
        if len(matches) != 1:
            return False
        grant = [
            str(icacls),
            str(path),
            "/inheritance:r",
            "/grant:r",
            f"*{matches[0]}:(F)",
            "*S-1-5-18:(F)",
            "*S-1-5-32-544:(F)",
        ]

        def run(arguments: list[str]) -> subprocess.CompletedProcess[bytes]:
            return subprocess.run(
                arguments,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False,
                timeout=WINDOWS_ACL_TIMEOUT_SECONDS,
                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
            )

        with _windows_auth_file_guard(path) as pinned:
            if not pinned:
                return False
            pinned_metadata = _windows_auth_file_metadata(path)
            if (
                pinned_metadata is None
                or before.st_dev != pinned_metadata.st_dev
                or before.st_size != pinned_metadata.st_size
                or before.st_ino
                and pinned_metadata.st_ino
                and before.st_ino != pinned_metadata.st_ino
            ):
                return False
            updated = run(grant)
            # /inheritance:r removes inherited sandbox grants. An explicit
            # untrusted ACE survives that operation, so reset the DACL once
            # and immediately replace the inherited rules. A read/no-delete
            # handle pins the exact file throughout both mutations.
            if updated.returncode == 0 and not _safe_windows_auth_file(path):
                reset = run([str(icacls), str(path), "/reset"])
                if reset.returncode != 0:
                    return False
                updated = run(grant)
            after = _windows_auth_file_metadata(path)
    except (OSError, subprocess.TimeoutExpired, UnicodeError):
        return False
    if updated.returncode != 0 or after is None:
        return False
    if (
        before.st_dev != after.st_dev
        or before.st_size != after.st_size
        or before.st_ino
        and after.st_ino
        and before.st_ino != after.st_ino
    ):
        return False
    return _safe_windows_auth_file(path)


@contextmanager
def _windows_auth_file_guard(path: Path) -> Generator[bool]:
    """Pin an auth file against swaps and writes while its DACL changes."""

    if os.name != "nt":
        yield False
        return
    import ctypes

    kernel = ctypes.WinDLL("kernel32", use_last_error=True)
    create = kernel.CreateFileW
    create.argtypes = [
        ctypes.c_wchar_p,
        ctypes.c_uint32,
        ctypes.c_uint32,
        ctypes.c_void_p,
        ctypes.c_uint32,
        ctypes.c_uint32,
        ctypes.c_void_p,
    ]
    create.restype = ctypes.c_void_p
    close = kernel.CloseHandle
    close.argtypes = [ctypes.c_void_p]
    close.restype = ctypes.c_int
    # GENERIC_READ, FILE_SHARE_READ (no WRITE or DELETE),
    # OPEN_EXISTING, FILE_FLAG_BACKUP_SEMANTICS | OPEN_REPARSE_POINT.
    handle = create(str(path), 0x80000000, 0x00000001, None, 3, 0x02200000, None)
    if handle in {None, ctypes.c_void_p(-1).value}:
        yield False
        return
    try:
        yield True
    finally:
        close(handle)


def _spawn_process(spec: _ProcessSpec) -> subprocess.Popen[bytes]:
    try:
        return subprocess.Popen(
            list(spec.argv),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            cwd=str(spec.working_directory) if spec.working_directory else None,
            env=dict(spec.environment),
            bufsize=0,
            start_new_session=os.name == "posix",
        )
    except OSError:
        raise _TransportError("spawn") from None


def _raise_if_cancelled(event: threading.Event | None) -> None:
    if event is not None and event.is_set():
        raise CodexAuthCancelled("Codex authentication was cancelled")


def _wait_for_exit(process: subprocess.Popen[bytes], timeout: float) -> bool:
    try:
        process.wait(timeout=timeout)
        return True
    except subprocess.TimeoutExpired:
        return False
    except OSError:
        return True


def _terminate_process(process: subprocess.Popen[bytes]) -> None:
    if process.poll() is not None:
        return
    try:
        if os.name == "posix":
            os.killpg(process.pid, signal.SIGTERM)
        else:  # pragma: no cover - exercised by Windows integration coverage.
            process.terminate()
    except (OSError, ProcessLookupError):
        pass
    if _wait_for_exit(process, PROCESS_TERMINATE_GRACE_SECONDS):
        return
    try:
        if os.name == "posix":
            os.killpg(process.pid, signal.SIGKILL)
        else:  # pragma: no cover - exercised by Windows integration coverage.
            process.kill()
    except (OSError, ProcessLookupError):
        pass
    _wait_for_exit(process, PROCESS_KILL_GRACE_SECONDS)


def _public_transport_error(error: _TransportError) -> CodexAuthError:
    if error.kind == "timeout":
        return CodexAuthUnavailable(
            "Codex authentication timed out", failure_reason="host_auth_timeout"
        )
    if error.kind == "spawn":
        return CodexAuthUnavailable("Codex app-server is unavailable")
    if error.kind in {"protocol", "oversize"}:
        return CodexAuthError("Codex authentication could not be completed")
    if error.kind == "unsupported":
        return CodexAuthUnavailable(
            "Codex authentication could not be completed", failure_reason="host_auth_unsupported"
        )
    if error.kind == "remote":
        return CodexAuthUnavailable(
            "Codex authentication could not be completed", failure_reason="host_auth_error"
        )
    return CodexAuthUnavailable("Codex authentication could not be completed")


def _profile_provider_override(
    session: _AuthSession, result: object, cwd: Path | None, deadline: float
) -> str | None:
    if (
        not is_json(result)
        or result.get("authMethod") is not None
        or result.get("requiresOpenaiAuth") is not False
    ):
        return None
    response = session.request(
        4,
        "config/read",
        {"includeLayers": False, "cwd": str(cwd) if cwd is not None else None},
        deadline=deadline,
    )
    if not is_json(response) or not is_json(config := response.get("config")):
        raise _TransportError("protocol")
    profile = config.get("profile")
    if profile is None:
        return None
    if not isinstance(profile, str):
        raise _TransportError("protocol")
    try:
        profile.encode("utf-8")
    except UnicodeEncodeError:
        raise _TransportError("protocol") from None
    # Codex splits dotted CLI paths literally. A quoted inline-table key instead
    # overlays only the selected profile's provider, retaining its other settings.
    key = json.dumps(profile, ensure_ascii=False).replace("\x7f", "\\u007f")
    return f'profiles={{{key}={{model_provider="openai"}}}}'


def _auth_material_from_session_result(
    result: object,
    *,
    session: _AuthSession,
    account_read_request_id: int,
    deadline: float,
) -> AuthMaterial:
    """Disambiguate a tokenless legacy status in the same bounded session."""

    if not is_json(result) or result.get("authMethod") is not None:
        return _auth_material_from_result(result)

    try:
        account_result = session.request(
            account_read_request_id,
            "account/read",
            {"refreshToken": False},
            deadline=deadline,
        )
    except _TransportError as error:
        if error.kind in {"protocol", "oversize"}:
            raise CodexAuthError("Codex authentication data is invalid") from None
        # The preceding null auth method already invalidated workspace
        # identity; an unavailable follow-up cannot resurrect its old bearer.
        raise CodexAuthAccountUnverified(
            "ChatGPT account could not be verified",
            failure_reason=_public_transport_error(error).failure_reason,
        ) from None

    if (
        not is_json(account_result)
        or type(account_result.get("requiresOpenaiAuth")) is not bool
        or "account" not in account_result
    ):
        raise CodexAuthError("Codex authentication data is invalid")
    account = account_result["account"]
    if account is None:
        raise CodexAuthRequired("ChatGPT authentication is required")
    if not is_json(account) or not isinstance(account.get("type"), str):
        raise CodexAuthError("Codex authentication data is invalid")
    if account["type"] == "chatgpt":
        # account/read intentionally exposes no workspace/account identifier.
        # Another ChatGPT account must never inherit the previous bearer.
        raise CodexAuthAccountUnverified("ChatGPT account could not be verified")
    if account["type"] in {"apiKey", "amazonBedrock"}:
        raise CodexAuthRequired("ChatGPT authentication is required")
    raise CodexAuthError("Codex authentication data is invalid")


def _auth_material_from_result(result: object) -> AuthMaterial:
    if not is_json(result):
        raise CodexAuthError("Codex authentication data is invalid")
    if result.get("authMethod") != "chatgpt":
        raise CodexAuthRequired("ChatGPT authentication is required")
    token = result.get("authToken")
    if token is None or token == "":
        # Codex can report the active ChatGPT method before refreshed token
        # material is available. It proves neither sign-out nor account scope.
        raise CodexAuthAccountUnverified(
            "ChatGPT account could not be verified", failure_reason="missing_access_token"
        )
    if not isinstance(token, str):
        raise CodexAuthError("Codex authentication data is invalid")
    try:
        token_size = len(token.encode("ascii"))
    except UnicodeEncodeError:
        raise CodexAuthError("Codex authentication data is invalid") from None
    if token_size > MAXIMUM_AUTH_TOKEN_BYTES:
        raise CodexAuthError("Codex authentication data is invalid")
    payload = _jwt_payload(token)
    return AuthMaterial(
        token=token,
        account_id=_account_id_from_payload(payload),
        expires_at_unix_ms=_expires_at_unix_ms_from_payload(payload),
        subject=_subject_from_payload(payload),
    )


def chatgpt_auth_subject(auth: AuthMaterial) -> str | None:
    """Return only the current authenticated user's bounded JWT subject."""

    subject = auth.subject
    if subject is not None:
        try:
            return _subject_from_payload({"sub": subject})
        except CodexAuthError:
            return None
    token = cast(object, auth.token)
    if not isinstance(token, str):
        return None
    try:
        return _subject_from_payload(_jwt_payload(token))
    except CodexAuthError:
        return None


def _jwt_payload(token: str) -> dict[str, object]:
    parts = token.split(".")
    if len(parts) != 3:
        raise CodexAuthError("Codex authentication data is invalid")
    encoded_payload = parts[1]
    if (
        not encoded_payload
        or len(encoded_payload) > MAXIMUM_JWT_PAYLOAD_SEGMENT_BYTES
        or _JWT_SEGMENT_PATTERN.fullmatch(encoded_payload) is None
    ):
        raise CodexAuthError("Codex authentication data is invalid")
    padding = "=" * (-len(encoded_payload) % 4)
    try:
        payload_bytes = base64.b64decode(
            (encoded_payload + padding).encode("ascii"),
            altchars=b"-_",
            validate=True,
        )
    except (ValueError, UnicodeEncodeError):
        raise CodexAuthError("Codex authentication data is invalid") from None
    if not payload_bytes or len(payload_bytes) > MAXIMUM_JWT_PAYLOAD_BYTES:
        raise CodexAuthError("Codex authentication data is invalid")
    try:
        decoded: object = json.loads(
            payload_bytes,
            object_pairs_hook=unique_json_object,
            parse_constant=int,
        )
    except (ValueError, UnicodeDecodeError, RecursionError):
        raise CodexAuthError("Codex authentication data is invalid") from None
    if not is_json(decoded):
        raise CodexAuthError("Codex authentication data is invalid")
    return decoded


def _expires_at_unix_ms_from_payload(payload: Mapping[str, object]) -> int:
    expires_at = payload.get("exp")
    if (
        not isinstance(expires_at, int)
        or isinstance(expires_at, bool)
        or expires_at <= 0
        or expires_at > (2**53 - 1) // 1000
    ):
        raise CodexAuthError("Codex authentication data is invalid")
    return expires_at * 1000


def _subject_from_payload(payload: Mapping[str, object]) -> str:
    subject = payload.get("sub")
    if not isinstance(subject, str):
        raise CodexAuthError("Codex authentication data is invalid")
    try:
        encoded = subject.encode("utf-8")
    except UnicodeEncodeError:
        raise CodexAuthError("Codex authentication data is invalid") from None
    if (
        not encoded
        or len(encoded) > 1024
        or subject != subject.strip()
        or any(ord(character) < 32 or ord(character) == 127 for character in subject)
    ):
        raise CodexAuthError("Codex authentication data is invalid")
    return subject


def _account_id_from_payload(payload: Mapping[str, object]) -> str:
    auth_claim = payload.get(_AUTH_CLAIM_NAMESPACE)
    if not is_json(auth_claim):
        raise CodexAuthError("Codex authentication data is invalid")
    account_id = auth_claim.get("chatgpt_account_id")
    fallback_account_id = auth_claim.get("account_id")
    if account_id is None:
        account_id = fallback_account_id
    elif fallback_account_id is not None and fallback_account_id != account_id:
        raise CodexAuthError("Codex authentication data is invalid")
    if not isinstance(account_id, str):
        raise CodexAuthError("Codex authentication data is invalid")
    try:
        account_id_size = len(account_id.encode("ascii"))
    except UnicodeEncodeError:
        raise CodexAuthError("Codex authentication data is invalid") from None
    if (
        account_id_size > MAXIMUM_ACCOUNT_ID_BYTES
        or _SAFE_ACCOUNT_ID_PATTERN.fullmatch(account_id) is None
    ):
        raise CodexAuthError("Codex authentication data is invalid")
    return account_id


__all__ = [
    "AuthMaterial",
    "CodexAuthAccountChanged",
    "CodexAuthAccountUnverified",
    "CodexAuthCancelled",
    "CodexAuthClient",
    "CodexAuthError",
    "CodexAuthManager",
    "CodexAuthRequired",
    "CodexAuthUnavailable",
    "close_process_auth",
    "get_process_auth_manager",
    "refresh_chatgpt_auth_after_unauthorized",
    "warm_process_auth",
]
