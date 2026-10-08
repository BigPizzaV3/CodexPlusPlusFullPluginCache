"""Metadata-only vetoes for automatic owner replacement, never kill authority."""

from __future__ import annotations

import os
import re
import stat
import time
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

import control_client

RECENT_AUDIO_SECONDS = 300
_MAXIMUM_ENTRIES = 4_096
_MAXIMUM_GENERATIONS = 256
_MAXIMUM_DEPTH = 16
_MAXIMUM_SCAN_SECONDS = 0.5
_STORAGE_GENERATION = re.compile(r"storage-[0-9a-f]{32}\Z")
_AUDIO_DIRECTORIES = ("Recordings", "NativeCaptureScratch", "UploadOutbox")


class AudioActivityStatus(str, Enum):
    COMPLETE = "complete"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class _FileActivity:
    path: Path
    device: int
    inode: int
    size: int
    modified_ns: int
    changed_ns: int


@dataclass(frozen=True)
class AudioActivitySnapshot:
    control_root: Path
    status: AudioActivityStatus
    recent_audio: bool = False
    files: tuple[_FileActivity, ...] = ()
    directories: tuple[tuple[Path, tuple[int, int] | None], ...] = ()


class _Unavailable(Exception):
    pass


def _identity(metadata: os.stat_result) -> tuple[int, int]:
    return metadata.st_dev, metadata.st_ino


def _reject_links(metadata: os.stat_result) -> None:
    # st_file_attributes is available only on Windows, including Python 3.10.
    if stat.S_ISLNK(metadata.st_mode) or (
        getattr(metadata, "st_file_attributes", 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT
    ):
        raise _Unavailable


@dataclass
class _Scan:
    now_ns: int
    deadline: float
    entries: int = 0
    files: list[_FileActivity] = field(default_factory=list[_FileActivity])
    directories: dict[Path, os.stat_result | None] = field(
        default_factory=dict[Path, os.stat_result | None]
    )

    def check(self) -> None:
        if self.entries > _MAXIMUM_ENTRIES or time.monotonic() >= self.deadline:
            raise _Unavailable

    def metadata(self, path: Path, *, directory: bool) -> os.stat_result:
        self.check()
        current = path.lstat()
        _reject_links(current)
        expected = stat.S_ISDIR if directory else stat.S_ISREG
        if not expected(current.st_mode):
            raise _Unavailable
        self.check()
        return current

    def directory(self, path: Path, *, optional: bool = False) -> bool:
        try:
            metadata = self.metadata(path, directory=True)
        except FileNotFoundError:
            if not optional:
                raise
            self.directories[path] = None
            return False
        self.directories[path] = metadata
        return True

    def audio(self, path: Path, depth: int = 0) -> None:
        if depth > _MAXIMUM_DEPTH:
            raise _Unavailable
        if not self.directory(path, optional=depth == 0):
            return
        with os.scandir(path) as entries:
            for entry in entries:
                self.entries += 1
                self.check()
                metadata = entry.stat(follow_symlinks=False)
                _reject_links(metadata)
                child = path / entry.name
                if stat.S_ISDIR(metadata.st_mode):
                    self.audio(child, depth + 1)
                elif stat.S_ISREG(metadata.st_mode):
                    metadata = self.metadata(child, directory=False)
                    # No payload reads or extension assumptions: encrypted frames,
                    # legacy WAVs and partially prepared uploads all preserve work.
                    if depth == 0 and entry.name == "audio-encryption-key.v1.dpapi":
                        continue
                    self.files.append(
                        _FileActivity(
                            child,
                            metadata.st_dev,
                            metadata.st_ino,
                            metadata.st_size,
                            metadata.st_mtime_ns,
                            metadata.st_ctime_ns,
                        )
                    )
                else:
                    raise _Unavailable

    def generations(self, rust: Path) -> None:
        if not self.directory(rust, optional=True):
            return
        with os.scandir(rust) as entries:
            for count, entry in enumerate(entries, 1):
                self.entries += 1
                self.check()
                if count > _MAXIMUM_GENERATIONS:
                    raise _Unavailable
                if _STORAGE_GENERATION.fullmatch(entry.name):
                    generation = rust / entry.name
                    self.directory(generation)
                    self.audio(generation / "Recordings")

    def revalidate(self, control_root: Path) -> None:
        for path, expected in self.directories.items():
            self.check()
            if expected is None:
                try:
                    path.lstat()
                except FileNotFoundError:
                    continue
                raise _Unavailable
            current = self.metadata(path, directory=True)
            if _identity(current) != _identity(expected):
                raise _Unavailable
            # Health/control files can change independently of audio. Other
            # directory mutations make enumeration incomplete for this attempt.
            if path != control_root and (
                current.st_mtime_ns != expected.st_mtime_ns
                or current.st_ctime_ns != expected.st_ctime_ns
            ):
                raise _Unavailable


def capture_audio_activity(control_root: Path) -> AudioActivitySnapshot:
    """Observe fixed native audio roots without interfering with listener repair.

    Missing optional roots are safe to observe only beneath verified parents.
    Limits and uncertain filesystem evidence return UNKNOWN, which later vetoes
    automatic termination but does not stop the ordinary health challenge.
    """
    try:
        if (
            not control_root.is_absolute()
            or control_root.name != "LocalMeetingsControl"
            or ".." in control_root.parts
            or control_root.drive.startswith("\\\\")
        ):
            raise _Unavailable
        scan = _Scan(time.time_ns(), time.monotonic() + _MAXIMUM_SCAN_SECONDS)
        # Do not enter redirected ancestors, including Windows junctions.
        for ancestor in reversed((control_root, *control_root.parents)):
            scan.check()
            _reject_links(ancestor.lstat())
        app = control_root.parent
        scan.directory(app)
        scan.directory(control_root)
        private_control = control_client.require_private(control_root, directory=True)
        observed_control = scan.directories[control_root]
        if observed_control is None or _identity(private_control) != _identity(observed_control):
            raise _Unavailable
        # Native audio directories can have ordinary inherited permissions.
        # They provide a conservative veto, not owner or replacement authority.
        for name in _AUDIO_DIRECTORIES:
            scan.audio(app / name)
        scan.generations(app / "Rust")
        scan.revalidate(control_root)
        files = tuple(sorted(scan.files, key=lambda item: item.path))
        recent = any(
            max(item.modified_ns, item.changed_ns)
            >= scan.now_ns - RECENT_AUDIO_SECONDS * 1_000_000_000
            for item in files
        )
        return AudioActivitySnapshot(
            control_root,
            AudioActivityStatus.COMPLETE,
            recent,
            files,
            tuple(
                sorted(
                    (path, _identity(value) if value is not None else None)
                    for path, value in scan.directories.items()
                )
            ),
        )
    except (OSError, ValueError, control_client.ControlUnavailable, _Unavailable):
        return AudioActivitySnapshot(control_root, AudioActivityStatus.UNKNOWN)


def require_audio_inactive(baseline: AudioActivitySnapshot) -> None:
    """Recheck an automatic attempt's baseline immediately before each signal."""
    current = capture_audio_activity(baseline.control_root)
    if (
        baseline.status != AudioActivityStatus.COMPLETE
        or current.status != AudioActivityStatus.COMPLETE
    ):
        raise control_client.CooperativeHandoffDeclined(
            "Automatic recovery could not verify local audio activity",
            recovery_blocker="audio-activity-unavailable",
        )
    if baseline.recent_audio or current.recent_audio or baseline.files != current.files:
        raise control_client.CooperativeHandoffDeclined(
            "Automatic recovery preserved recently changed local audio",
            recovery_blocker="recent-audio-activity",
        )
    if baseline.directories != current.directories:
        raise control_client.CooperativeHandoffDeclined(
            "Automatic recovery audio directories changed",
            recovery_blocker="audio-activity-unavailable",
        )
