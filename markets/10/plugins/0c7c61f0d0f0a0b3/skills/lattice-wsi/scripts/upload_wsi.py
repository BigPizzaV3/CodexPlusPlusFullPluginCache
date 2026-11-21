#!/usr/bin/env python3
"""Upload one local WSI to a presigned GCS resumable session.

The session URL is read from stdin so it never appears in argv or an environment
variable. Output is limited to byte progress and terse status/error messages.
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import json
import os
import re
import ssl
import sys
from pathlib import Path
from urllib.parse import SplitResult, urlsplit

ALIGNMENT = 256 * 1024
DEFAULT_CHUNK_SIZE = 8 * 1024 * 1024
DEFAULT_SINGLE_REQUEST_MAX = 64 * 1024 * 1024
SUCCESS = {200, 201}
RANGE_RE = re.compile(r"^bytes=0-(\d+)$")
CONTENT_TYPES = {
    ".svs": "image/aperio-svs",
    ".tiff": "image/tiff",
    ".tif": "image/tiff",
    ".ndpi": "image/ndpi",
    ".scn": "image/scn",
    ".mrxs": "image/mrxs",
    ".vsi": "image/vsi",
    ".bif": "image/bif",
}


class UploadFailure(Exception):
    """A safe-to-print upload error that never contains the session URL."""


class LimitedReader:
    """Expose exactly one file slice to http.client without buffering it."""

    def __init__(self, file, length: int) -> None:
        self.file = file
        self.remaining = length

    def read(self, size: int = -1) -> bytes:
        if self.remaining == 0:
            return b""
        if size < 0 or size > self.remaining:
            size = self.remaining
        data = self.file.read(size)
        if not data:
            raise UploadFailure("local file ended before its declared size")
        self.remaining -= len(data)
        return data


def content_type(path: Path) -> str:
    return CONTENT_TYPES.get(path.suffix.lower(), "application/octet-stream")


def sha256(file) -> str:
    digest = hashlib.sha256()
    while chunk := file.read(1024 * 1024):
        digest.update(chunk)
    return digest.hexdigest()


def fingerprint(stat: os.stat_result) -> tuple[int, int, int, int, int]:
    return (stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns)


def assert_unchanged(file, approved: tuple[int, int, int, int, int]) -> None:
    if fingerprint(os.fstat(file.fileno())) != approved:
        raise UploadFailure("local file changed during transfer")


def read_session_url() -> SplitResult:
    raw = sys.stdin.readline(64 * 1024)
    if not raw or sys.stdin.read(1):
        raise UploadFailure("expected exactly one session URL on stdin")
    value = raw.strip()
    try:
        parsed = urlsplit(value)
        hostname = parsed.hostname
        _port = parsed.port
    except ValueError as exc:
        raise UploadFailure("invalid session URL") from exc
    loopback = hostname in {"127.0.0.1", "::1", "localhost"}
    if (
        (parsed.scheme != "https" and not (parsed.scheme == "http" and loopback))
        or not hostname
        or parsed.username is not None
        or parsed.password is not None
        or parsed.fragment
    ):
        raise UploadFailure("invalid session URL")
    return parsed


def request(
    session: SplitResult,
    *,
    body: object | None,
    headers: dict[str, str],
    timeout: float,
) -> tuple[int, str | None]:
    port = session.port
    if session.scheme == "https":
        connection: http.client.HTTPConnection = http.client.HTTPSConnection(
            session.hostname,
            port=port,
            timeout=timeout,
            context=ssl.create_default_context(),
        )
    else:
        connection = http.client.HTTPConnection(session.hostname, port=port, timeout=timeout)
    target = session.path or "/"
    if session.query:
        target += "?" + session.query
    try:
        connection.request("PUT", target, body=body, headers=headers)
        response = connection.getresponse()
        status = response.status
        acknowledged = response.getheader("Range")
        response.read(64 * 1024)
        return status, acknowledged
    except UploadFailure:
        raise
    except (OSError, http.client.HTTPException, ssl.SSLError) as exc:
        raise UploadFailure("network transfer interrupted") from exc
    finally:
        connection.close()


def acknowledged_offset(range_header: str | None, total: int) -> int:
    if range_header is None:
        return 0
    match = RANGE_RE.fullmatch(range_header.strip())
    if match is None:
        raise UploadFailure("server returned an invalid resume range")
    offset = int(match.group(1)) + 1
    if offset < 0 or offset > total:
        raise UploadFailure("server returned an invalid resume offset")
    return offset


def query_offset(session: SplitResult, total: int, timeout: float) -> tuple[int, bool]:
    status, range_header = request(
        session,
        body=b"",
        headers={"Content-Length": "0", "Content-Range": f"bytes */{total}"},
        timeout=timeout,
    )
    if status in SUCCESS:
        return total, True
    if status == 308:
        offset = acknowledged_offset(range_header, total)
        if offset == total:
            raise UploadFailure("server acknowledged all bytes without confirming completion")
        return offset, False
    if status in {404, 410}:
        raise UploadFailure("upload session expired or is unavailable")
    raise UploadFailure(f"resume query failed with HTTP {status}")


def put_range(
    session: SplitResult,
    file,
    *,
    start: int,
    length: int,
    total: int,
    mime: str,
    timeout: float,
) -> int:
    end = start + length - 1
    status, range_header = request(
        session,
        body=LimitedReader(file, length),
        headers={
            "Content-Length": str(length),
            "Content-Range": f"bytes {start}-{end}/{total}",
            "Content-Type": mime,
        },
        timeout=timeout,
    )
    final = end + 1 == total
    if status in SUCCESS:
        if not final:
            raise UploadFailure("server finalized before the declared file end")
        return total
    if status == 308:
        offset = acknowledged_offset(range_header, total)
        if offset <= start:
            raise UploadFailure("server made no upload progress")
        if offset > end + 1:
            raise UploadFailure("server returned an invalid chunk acknowledgement")
        if final and offset == total:
            raise UploadFailure("server acknowledged all bytes without confirming completion")
        return offset
    if status in {404, 410}:
        raise UploadFailure("upload session expired or is unavailable")
    label = "final" if final else "chunk"
    raise UploadFailure(f"{label} upload failed with HTTP {status}")


def upload(
    session: SplitResult,
    path: Path,
    *,
    expected_size: int,
    expected_sha256: str,
    chunk_size: int,
    single_request_max: int,
    timeout: float,
) -> None:
    if expected_size <= 0:
        raise UploadFailure("expected size must be positive")
    if not re.fullmatch(r"[0-9a-f]{64}", expected_sha256):
        raise UploadFailure("expected SHA-256 must be 64 lowercase hex characters")
    if chunk_size <= 0 or chunk_size % ALIGNMENT:
        raise UploadFailure("chunk size must be a positive multiple of 256 KiB")
    if single_request_max < 0:
        raise UploadFailure("single-request maximum must be nonnegative")

    mime = content_type(path)
    with path.open("rb") as file:
        approved = fingerprint(os.fstat(file.fileno()))
        total = approved[2]
        if total != expected_size:
            raise UploadFailure("local file size changed after approval")
        actual_sha256 = sha256(file)
        assert_unchanged(file, approved)
        if actual_sha256 != expected_sha256:
            raise UploadFailure("local file content changed after approval")

        offset, complete = query_offset(session, total, timeout)
        if complete:
            print(f"upload complete: {total}/{total} bytes")
            return
        if offset:
            print(f"resuming upload: {offset}/{total} bytes")

        file.seek(offset)
        if total <= single_request_max and offset == 0:
            offset = put_range(
                session,
                file,
                start=0,
                length=total,
                total=total,
                mime=mime,
                timeout=timeout,
            )
            assert_unchanged(file, approved)
            if offset == total:
                print(f"upload complete: {offset}/{total} bytes")
                return
            print(f"uploaded {offset}/{total} bytes")

        while offset < total:
            assert_unchanged(file, approved)
            file.seek(offset)
            length = min(chunk_size, total - offset)
            offset = put_range(
                session,
                file,
                start=offset,
                length=length,
                total=total,
                mime=mime,
                timeout=timeout,
            )
            assert_unchanged(file, approved)
            print(f"uploaded {offset}/{total} bytes")
    print("upload complete")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Upload a local WSI; read the presigned session URL from stdin.",
    )
    parser.add_argument("path", type=Path, help="authorized local WSI path")
    parser.add_argument(
        "--inspect",
        action="store_true",
        help="print basename, size, content type, and SHA-256 without uploading",
    )
    parser.add_argument("--expected-size", type=int, help=argparse.SUPPRESS)
    parser.add_argument("--expected-sha256", help=argparse.SUPPRESS)
    parser.add_argument("--chunk-size", type=int, default=DEFAULT_CHUNK_SIZE, help=argparse.SUPPRESS)
    parser.add_argument(
        "--single-request-max",
        type=int,
        default=DEFAULT_SINGLE_REQUEST_MAX,
        help=argparse.SUPPRESS,
    )
    parser.add_argument("--timeout", type=float, default=600.0, help=argparse.SUPPRESS)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        path = args.path.expanduser().resolve(strict=True)
        if not path.is_file() or not os.access(path, os.R_OK):
            raise UploadFailure("local path is not a readable file")
        if args.inspect:
            with path.open("rb") as file:
                before = fingerprint(os.fstat(file.fileno()))
                digest = sha256(file)
                assert_unchanged(file, before)
            print(
                json.dumps(
                    {
                        "content_type": content_type(path),
                        "filename": path.name,
                        "sha256": digest,
                        "size": before[2],
                    },
                    ensure_ascii=True,
                    separators=(",", ":"),
                    sort_keys=True,
                )
            )
            return 0
        if args.expected_size is None or args.expected_sha256 is None:
            raise UploadFailure("expected size and SHA-256 are required")
        if args.timeout <= 0:
            raise UploadFailure("timeout must be positive")
        session = read_session_url()
        upload(
            session,
            path,
            expected_size=args.expected_size,
            expected_sha256=args.expected_sha256,
            chunk_size=args.chunk_size,
            single_request_max=args.single_request_max,
            timeout=args.timeout,
        )
        return 0
    except KeyboardInterrupt:
        print("upload interrupted", file=sys.stderr)
    except (UploadFailure, OSError) as exc:
        message = str(exc) if isinstance(exc, UploadFailure) else "local file error"
        print(f"upload failed: {message}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
