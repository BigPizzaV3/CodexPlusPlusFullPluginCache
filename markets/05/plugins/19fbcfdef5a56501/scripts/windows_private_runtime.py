"""Windows code storage outside legacy sandbox-writable user profiles.

Only newly created directories receive an ACL. Existing directories are inspected,
never repaired. Native bytes still require the release's independent hash checks.
"""

from __future__ import annotations

import ctypes
import hashlib
import os
import re
import uuid
from collections.abc import Generator
from contextlib import ExitStack, contextmanager
from dataclasses import dataclass
from pathlib import Path, PureWindowsPath
from typing import TYPE_CHECKING, Protocol

_SYSTEM = "S-1-5-18"
_ADMINS = "S-1-5-32-544"
_INSTALLER = "S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464"
_OS_OWNERS = frozenset((_SYSTEM, _ADMINS, _INSTALLER))
_PARENT_REPLACEMENT_RIGHTS = 0x000D0040 | 0x10000000  # DELETE, DELETE_CHILD, DAC, OWNER, GA
_FULL_ACCESS = 0x001F01FF
_INHERIT_ONLY = 0x08
_PROTECTED_DACL = 0x1000
_DIRECTORY = 0x10
_REPARSE = 0x400
_NAMESPACE = "OpenAI-Meetings-"


class WindowsPrivateRuntimeError(RuntimeError):
    """The Windows runtime's code-storage boundary could not be established."""


class _WindowsCtypesApi(Protocol):
    def WinDLL(self, name: str, *, use_last_error: bool) -> ctypes.CDLL: ...

    def get_last_error(self) -> int: ...


if TYPE_CHECKING:
    _windows_ctypes: _WindowsCtypesApi
else:
    _windows_ctypes = ctypes


# Fixed-width Windows types also make structure-layout tests meaningful on Unix.
_U32 = ctypes.c_uint32
_U16 = ctypes.c_uint16
_PTR = ctypes.c_void_p


class _UnicodeString(ctypes.Structure):
    _fields_ = [("length", _U16), ("maximum_length", _U16), ("buffer", _PTR)]


class _ObjectAttributes(ctypes.Structure):
    _fields_ = [
        ("length", _U32),
        ("root", _PTR),
        ("name", ctypes.POINTER(_UnicodeString)),
        ("attributes", _U32),
        ("security", _PTR),
        ("qos", _PTR),
    ]


class _IoStatusValue(ctypes.Union):
    _fields_ = [("status", ctypes.c_int32), ("pointer", _PTR)]


class _IoStatusBlock(ctypes.Structure):
    _fields_ = [("value", _IoStatusValue), ("information", ctypes.c_size_t)]


class _FileInfo(ctypes.Structure):
    _fields_ = [
        ("attributes", _U32),
        ("creation", _U32 * 2),
        ("access", _U32 * 2),
        ("write", _U32 * 2),
        ("volume", _U32),
        ("size_high", _U32),
        ("size_low", _U32),
        ("links", _U32),
        ("index_high", _U32),
        ("index_low", _U32),
    ]


class _AclInfo(ctypes.Structure):
    _fields_ = [("count", _U32), ("used", _U32), ("free", _U32)]


@dataclass(frozen=True)
class _Ace:
    kind: int
    flags: int
    mask: int
    sid: str


@dataclass(frozen=True)
class _Security:
    owner: str
    protected: bool
    aces: tuple[_Ace, ...]


def _validate_security(security: _Security, sid: str, *, private: bool) -> None:
    trusted = frozenset((sid, _SYSTEM, _ADMINS))
    if private:
        # An exact fresh-directory contract avoids treating formerly writable ACLs
        # with extra entries as a supported private runtime namespace.
        expected = {_Ace(0, 3, _FULL_ACCESS, trustee) for trustee in trusted}
        if (
            security.owner != sid
            or not security.protected
            or len(security.aces) != len(expected)
            or set(security.aces) != expected
        ):
            raise WindowsPrivateRuntimeError("Windows runtime directory is not private")
        return
    if security.owner not in _OS_OWNERS:
        raise WindowsPrivateRuntimeError("Windows shared storage owner is not trusted")
    trusted_ancestors = trusted | _OS_OWNERS
    for ace in security.aces:
        if ace.kind not in (0, 1):
            raise WindowsPrivateRuntimeError("Windows shared storage ACL is unsupported")
        if ace.kind == 0 and not ace.flags & _INHERIT_ONLY:
            if ace.sid not in trusted_ancestors and ace.mask & _PARENT_REPLACEMENT_RIGHTS:
                raise WindowsPrivateRuntimeError("Windows shared storage permits replacement")


def _leaf(value: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,180}", value):
        raise WindowsPrivateRuntimeError("Windows runtime directory name is invalid")
    return value


def _namespace(sid: str, codex_home: Path, flavor: str) -> str:
    _leaf(flavor)
    identity = os.path.normcase(str(codex_home.expanduser().resolve(strict=False)))
    digest = hashlib.sha256((sid + "\0" + identity + "\0" + flavor).encode()).hexdigest()
    return _NAMESPACE + digest[:40]


class _WindowsApi:
    kernel: ctypes.CDLL
    advapi: ctypes.CDLL
    nt: ctypes.CDLL
    shell: ctypes.CDLL
    ole: ctypes.CDLL
    sid: str

    def __init__(self) -> None:
        if os.name != "nt":
            raise WindowsPrivateRuntimeError("Windows private storage is unavailable on this host")
        self.kernel = _windows_ctypes.WinDLL("kernel32", use_last_error=True)
        self.advapi = _windows_ctypes.WinDLL("advapi32", use_last_error=True)
        self.nt = _windows_ctypes.WinDLL("ntdll", use_last_error=True)
        self.shell = _windows_ctypes.WinDLL("shell32", use_last_error=True)
        self.ole = _windows_ctypes.WinDLL("ole32", use_last_error=True)
        self.kernel.GetCurrentProcess.argtypes = []
        self.kernel.GetCurrentProcess.restype = _PTR
        self.kernel.CloseHandle.argtypes = [_PTR]
        self.kernel.CloseHandle.restype = ctypes.c_int
        self.kernel.LocalFree.argtypes = [_PTR]
        self.kernel.LocalFree.restype = _PTR
        self.kernel.CreateFileW.argtypes = [ctypes.c_wchar_p, _U32, _U32, _PTR, _U32, _U32, _PTR]
        self.kernel.CreateFileW.restype = _PTR
        self.kernel.GetFileInformationByHandle.argtypes = [_PTR, ctypes.POINTER(_FileInfo)]
        self.kernel.GetFileInformationByHandle.restype = ctypes.c_int
        self.kernel.SetFileInformationByHandle.argtypes = [_PTR, ctypes.c_int, _PTR, _U32]
        self.kernel.SetFileInformationByHandle.restype = ctypes.c_int
        self.advapi.OpenProcessToken.argtypes = [_PTR, _U32, ctypes.POINTER(_PTR)]
        self.advapi.OpenProcessToken.restype = ctypes.c_int
        self.advapi.GetTokenInformation.argtypes = [_PTR, _U32, _PTR, _U32, ctypes.POINTER(_U32)]
        self.advapi.GetTokenInformation.restype = ctypes.c_int
        self.advapi.ConvertSidToStringSidW.argtypes = [_PTR, ctypes.POINTER(_PTR)]
        self.advapi.ConvertSidToStringSidW.restype = ctypes.c_int
        self.advapi.GetSecurityInfo.argtypes = [
            _PTR,
            _U32,
            _U32,
            ctypes.POINTER(_PTR),
            _PTR,
            ctypes.POINTER(_PTR),
            _PTR,
            ctypes.POINTER(_PTR),
        ]
        self.advapi.GetSecurityInfo.restype = _U32
        self.advapi.GetSecurityDescriptorControl.argtypes = [
            _PTR,
            ctypes.POINTER(_U16),
            ctypes.POINTER(_U32),
        ]
        self.advapi.GetSecurityDescriptorControl.restype = ctypes.c_int
        self.advapi.IsValidAcl.argtypes = [_PTR]
        self.advapi.IsValidAcl.restype = ctypes.c_int
        self.advapi.GetAclInformation.argtypes = [_PTR, _PTR, _U32, _U32]
        self.advapi.GetAclInformation.restype = ctypes.c_int
        self.advapi.GetAce.argtypes = [_PTR, _U32, ctypes.POINTER(_PTR)]
        self.advapi.GetAce.restype = ctypes.c_int
        self.advapi.ConvertStringSecurityDescriptorToSecurityDescriptorW.argtypes = [
            ctypes.c_wchar_p,
            _U32,
            ctypes.POINTER(_PTR),
            _PTR,
        ]
        self.advapi.ConvertStringSecurityDescriptorToSecurityDescriptorW.restype = ctypes.c_int
        self.nt.NtCreateFile.argtypes = [
            ctypes.POINTER(_PTR),
            _U32,
            ctypes.POINTER(_ObjectAttributes),
            ctypes.POINTER(_IoStatusBlock),
            _PTR,
            _U32,
            _U32,
            _U32,
            _U32,
            _PTR,
            _U32,
        ]
        self.nt.NtCreateFile.restype = ctypes.c_int32
        self.nt.RtlNtStatusToDosError.argtypes = [ctypes.c_int32]
        self.nt.RtlNtStatusToDosError.restype = _U32
        self.shell.SHGetKnownFolderPath.argtypes = [_PTR, _U32, _PTR, ctypes.POINTER(_PTR)]
        self.shell.SHGetKnownFolderPath.restype = ctypes.c_int32
        self.ole.CoTaskMemFree.argtypes = [_PTR]
        self.ole.CoTaskMemFree.restype = None
        self.sid = self._current_sid()

    @staticmethod
    def _error(operation: str, code: int | None = None) -> WindowsPrivateRuntimeError:
        if code is None:
            code = _windows_ctypes.get_last_error()
        return WindowsPrivateRuntimeError(f"Windows private storage {operation} failed ({code})")

    def _sid_string(self, pointer: _PTR) -> str:
        result = _PTR()
        if not pointer or not self.advapi.ConvertSidToStringSidW(pointer, ctypes.byref(result)):
            raise self._error("SID read")
        try:
            return ctypes.wstring_at(result)
        finally:
            self.kernel.LocalFree(result)

    def _current_sid(self) -> str:
        token = _PTR()
        if not self.advapi.OpenProcessToken(
            self.kernel.GetCurrentProcess(), 8, ctypes.byref(token)
        ):
            raise self._error("token query")
        try:
            size = _U32()
            self.advapi.GetTokenInformation(token, 1, None, 0, ctypes.byref(size))
            if not 0 < size.value <= 65536:
                raise self._error("token sizing")
            # A pointer-aligned allocation: TOKEN_USER begins with SID_AND_ATTRIBUTES.
            data = (
                ctypes.c_size_t * ((size.value + ctypes.sizeof(_PTR) - 1) // ctypes.sizeof(_PTR))
            )()
            if not self.advapi.GetTokenInformation(token, 1, data, size, ctypes.byref(size)):
                raise self._error("token read")
            return self._sid_string(_PTR(data[0]))
        finally:
            self.kernel.CloseHandle(token)

    def program_data(self) -> Path:
        guid = (ctypes.c_ubyte * 16).from_buffer_copy(
            uuid.UUID("62ab5d82-fdc1-4dc3-a9dd-070d1d495d97").bytes_le
        )
        result = _PTR()
        hr = self.shell.SHGetKnownFolderPath(guid, 0, None, ctypes.byref(result))
        if hr < 0 or not result:
            raise self._error("known folder lookup", hr)
        try:
            path = Path(ctypes.wstring_at(result))
            parsed = PureWindowsPath(path)
            if not parsed.is_absolute() or len(parsed.drive) != 2 or parsed.drive[1] != ":":
                raise WindowsPrivateRuntimeError("Windows shared storage is not on a local drive")
            if any(part in (".", "..") or part.endswith((".", " ")) for part in parsed.parts[1:]):
                raise WindowsPrivateRuntimeError("Windows shared storage path is invalid")
            return path
        finally:
            if result:
                self.ole.CoTaskMemFree(result)

    @contextmanager
    def root_handle(self, path: Path) -> Generator[int, None, None]:
        handle = self.kernel.CreateFileW(str(path), 0x00120081, 3, None, 3, 0x02200000, None)
        if not isinstance(handle, int) or handle == _PTR(-1).value:
            raise self._error("drive open")
        try:
            yield handle
        finally:
            self.kernel.CloseHandle(handle)

    @contextmanager
    def directory_handle(
        self, parent: int, name: str, *, create: bool = False, delete: bool = False
    ) -> Generator[int, None, None]:
        # Deletion opens either kind of leaf with DELETE access. The handle is
        # relative to its pinned parent and never follows a reparse point.
        if create and delete:
            raise WindowsPrivateRuntimeError("Windows directory operation is invalid")
        if (
            not name
            or name in (".", "..")
            or any(c in name for c in "\\/:")
            or name.endswith((".", " "))
        ):
            raise WindowsPrivateRuntimeError("Windows directory component is invalid")
        raw_name = ctypes.create_unicode_buffer(name)
        byte_length = len(name.encode("utf-16-le"))
        if byte_length > 65532:
            raise WindowsPrivateRuntimeError("Windows directory component is too long")
        unicode_name = _UnicodeString(byte_length, byte_length + 2, ctypes.addressof(raw_name))
        descriptor = _PTR()
        if create:
            sddl = f"O:{self.sid}D:P(A;OICI;FA;;;{self.sid})(A;OICI;FA;;;SY)(A;OICI;FA;;;BA)"
            if not self.advapi.ConvertStringSecurityDescriptorToSecurityDescriptorW(
                sddl, 1, ctypes.byref(descriptor), None
            ):
                raise self._error("private descriptor")
        attributes = _ObjectAttributes(
            ctypes.sizeof(_ObjectAttributes),
            parent,
            ctypes.pointer(unicode_name),
            0x1040,
            descriptor,
            None,
        )
        handle = _PTR()
        io = _IoStatusBlock()
        try:
            status = self.nt.NtCreateFile(
                ctypes.byref(handle),
                0x00130081 if delete else 0x00120081,
                ctypes.byref(attributes),
                ctypes.byref(io),
                None,
                0 if delete else _DIRECTORY,
                3,
                2 if create else 1,
                0x00200020 if delete else 0x00200021,
                None,
                0,
            )
        finally:
            if descriptor:
                self.kernel.LocalFree(descriptor)
        if status < 0:
            error = self.nt.RtlNtStatusToDosError(status)
            if error in (2, 3):
                raise FileNotFoundError(error, "Windows runtime directory is missing")
            if error in (80, 183):
                raise FileExistsError(error, "Windows runtime directory already exists")
            raise self._error("directory creation" if create else "directory open", error)
        if handle.value is None:
            raise WindowsPrivateRuntimeError("Windows directory handle is unavailable")
        try:
            yield handle.value
        finally:
            self.kernel.CloseHandle(handle)

    def file_info(self, handle: int) -> _FileInfo:
        info = _FileInfo()
        if not self.kernel.GetFileInformationByHandle(handle, ctypes.byref(info)):
            raise self._error("directory metadata")
        return info

    def delete(self, handle: int) -> None:
        disposition = ctypes.c_ubyte(1)  # FILE_DISPOSITION_INFO.DeleteFile
        if not self.kernel.SetFileInformationByHandle(
            handle, 4, ctypes.byref(disposition), ctypes.sizeof(disposition)
        ):
            raise self._error("cache payload deletion")

    def security(self, handle: int) -> _Security:
        info = self.file_info(handle)
        if not info.attributes & _DIRECTORY or info.attributes & _REPARSE:
            raise WindowsPrivateRuntimeError("Windows runtime path is not a plain directory")
        owner, dacl, descriptor = _PTR(), _PTR(), _PTR()
        error = self.advapi.GetSecurityInfo(
            handle,
            1,
            5,
            ctypes.byref(owner),
            None,
            ctypes.byref(dacl),
            None,
            ctypes.byref(descriptor),
        )
        if error:
            raise self._error("ACL read", error)
        try:
            if not owner or not dacl or not self.advapi.IsValidAcl(dacl):
                raise WindowsPrivateRuntimeError("Windows runtime ACL is invalid")
            control, revision = _U16(), _U32()
            if not self.advapi.GetSecurityDescriptorControl(
                descriptor, ctypes.byref(control), ctypes.byref(revision)
            ):
                raise self._error("ACL control read")
            details = _AclInfo()
            if not self.advapi.GetAclInformation(
                dacl, ctypes.byref(details), ctypes.sizeof(details), 2
            ):
                raise self._error("ACL information")
            aces: list[_Ace] = []
            for index in range(details.count):
                pointer = _PTR()
                if (
                    not self.advapi.GetAce(dacl, index, ctypes.byref(pointer))
                    or pointer.value is None
                ):
                    raise self._error("ACL entry read")
                header = ctypes.string_at(pointer, 4)
                kind, flags = header[0], header[1]
                size = int.from_bytes(header[2:4], "little")
                if kind not in (0, 1) or size < 16:
                    raise WindowsPrivateRuntimeError("Windows runtime ACL entry is unsupported")
                raw = ctypes.string_at(pointer, 8)
                aces.append(
                    _Ace(
                        kind,
                        flags,
                        int.from_bytes(raw[4:8], "little"),
                        self._sid_string(_PTR(pointer.value + 8)),
                    )
                )
            return _Security(
                self._sid_string(owner), bool(control.value & _PROTECTED_DACL), tuple(aces)
            )
        finally:
            if descriptor:
                self.kernel.LocalFree(descriptor)


@contextmanager
def _program_data_boundary(api: _WindowsApi) -> Generator[tuple[Path, int], None, None]:
    path = api.program_data()
    with ExitStack() as stack:
        handle = stack.enter_context(api.root_handle(Path(path.anchor)))
        _validate_security(api.security(handle), api.sid, private=False)
        ancestors = [handle]
        for component in path.parts[1:]:
            handle = stack.enter_context(api.directory_handle(handle, component))
            _validate_security(api.security(handle), api.sid, private=False)
            ancestors.append(handle)
        yield path, handle
        # ProgramData may grant write-attributes without granting replacement.
        # Recheck after creating the private child: it now keeps every ancestor
        # nonempty, preventing a later directory-to-reparse conversion. All
        # ancestor and private-child pins remain live during this readback.
        for ancestor in ancestors:
            _validate_security(api.security(ancestor), api.sid, private=False)


def _private_child(
    api: _WindowsApi, stack: ExitStack, parent: int, name: str, *, create: bool
) -> int:
    try:
        handle = stack.enter_context(api.directory_handle(parent, name))
    except FileNotFoundError:
        if not create:
            raise
        try:
            handle = stack.enter_context(api.directory_handle(parent, name, create=True))
        except FileExistsError:
            # Another trusted startup may have won creation; no ACL rewrite.
            handle = stack.enter_context(api.directory_handle(parent, name))
    _validate_security(api.security(handle), api.sid, private=True)
    return handle


def windows_runtime_root(codex_home: Path, flavor: str, create: bool = True) -> Path:
    """Return a verified private code root, isolated by user, Codex home and flavor."""
    api = _WindowsApi()
    name = _namespace(api.sid, codex_home, flavor)
    with ExitStack() as stack, _program_data_boundary(api) as (program_data, parent):
        handle = _private_child(api, stack, parent, name, create=create)
        # Released companions recognize this fixed suffix when proving their
        # launch path. Keep the namespace separate from the runtime directory.
        handle = _private_child(api, stack, handle, flavor, create=create)
        for child in ("versions", "state"):
            _private_child(api, stack, handle, child, create=create)
        return program_data / name / flavor


@contextmanager
def fresh_private_directory(parent: Path, prefix: str) -> Generator[Path, None, None]:
    """Create a private generation while continuously pinning its safe parents.

    The returned directory itself is not pinned during the body, so the caller
    can atomically rename it into another verified private directory. No existing
    generation is reused or recursively removed by this helper.
    """
    _leaf(prefix)
    api = _WindowsApi()
    with ExitStack() as stack, _program_data_boundary(api) as (program_data, handle):
        try:
            relative = parent.absolute().relative_to(program_data)
        except ValueError as exc:
            raise WindowsPrivateRuntimeError(
                "Windows generation parent is outside private storage"
            ) from exc
        if not relative.parts or not re.fullmatch(_NAMESPACE + r"[0-9a-f]{40}", relative.parts[0]):
            raise WindowsPrivateRuntimeError("Windows generation parent is not a runtime namespace")
        for component in relative.parts:
            _leaf(component)
            handle = stack.enter_context(api.directory_handle(handle, component))
            _validate_security(api.security(handle), api.sid, private=True)
        name = _leaf(prefix + "-" + uuid.uuid4().hex)
        with api.directory_handle(handle, name, create=True) as fresh:
            _validate_security(api.security(fresh), api.sid, private=True)
        yield parent / name


def remove_cache_payload(path: Path, parent_identity: tuple[int, int]) -> None:
    """Remove an unused payload while denying replacement of every ancestor.

    Cache ACLs may permit untrusted writes. Open children relative to parent
    handles and delete the opened objects, never a re-resolved pathname.
    """

    api = _WindowsApi()

    def remove(parent: int, target: Path) -> None:
        with api.directory_handle(parent, target.name, delete=True) as handle:
            info = api.file_info(handle)
            if info.attributes & _REPARSE:
                raise WindowsPrivateRuntimeError("Windows cache payload is a reparse point")
            if info.attributes & _DIRECTORY:
                # The path supplies names only. Even a concurrent substitution
                # cannot redirect the handle-relative opens and deletions.
                for child in target.iterdir():
                    remove(handle, child)
            api.delete(handle)

    if not path.is_absolute() or path != Path(os.path.normpath(path)):
        raise WindowsPrivateRuntimeError("Windows cache payload path is invalid")
    with ExitStack() as stack:
        handle = stack.enter_context(api.root_handle(Path(path.anchor)))
        api.security(handle)
        for component in path.parent.parts[1:]:
            handle = stack.enter_context(api.directory_handle(handle, component))
            api.security(handle)
        parent = path.parent.stat()
        if (parent.st_dev, parent.st_ino) != parent_identity:
            raise WindowsPrivateRuntimeError("Windows cache payload parent changed")
        remove(handle, path)
