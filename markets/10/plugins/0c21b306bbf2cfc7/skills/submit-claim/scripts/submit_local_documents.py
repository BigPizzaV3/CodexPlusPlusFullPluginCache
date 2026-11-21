"""Send explicitly selected local attachments to Delos once, without an API key.

Uses only Python's standard library. Remote MCP file descriptors are unnecessary
for this transport. Never call without the user's approval of the exact payload
and complete file list. A receipt file prevents repeating the same command.
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import json
import mimetypes
import os
import re
import stat
import sys
import uuid
from pathlib import Path
from urllib.parse import urlsplit

ENDPOINT = "https://api.delosintelligence.com/mcp"
MAX_BYTES = 4 * 1024 * 1024
MAX_PAYLOAD_BYTES = 256 * 1024
MAX_RESPONSE_BYTES = 64 * 1024
PUBLIC_REFERENCE_PATTERN = r"DLSAINC-SUB-[A-Z0-9-]{1,64}"
LARGE_FILE_GUIDANCE = (
    "These files do not fit the ChatGPT plugin's 4 MiB complete-request limit. "
    "With the user's approval, submit the claim or portfolio without the oversized "
    "files. Delos should then email the supplied contact a secure link for uploading "
    "supporting materials up to 500 MB, including PDFs, video, audio, and other file types."
)


class PreparationError(ValueError):
    pass


def error(
    code: str,
    message: str,
    outcome: str = "not_submitted",
    *,
    automatic_retry_allowed: bool = False,
) -> dict:
    return {
        "status": "error",
        "code": code,
        "message": message,
        "submission_outcome": outcome,
        "automatic_retry_allowed": automatic_retry_allowed,
    }


def read_regular_file(path: Path, limit: int) -> bytes:
    # Reject directories/devices/FIFOs before reading, including replacement races.
    fd = os.open(path, os.O_RDONLY | getattr(os, "O_NONBLOCK", 0))
    with os.fdopen(fd, "rb") as stream:
        info = os.fstat(stream.fileno())
        if not stat.S_ISREG(info.st_mode):
            raise PreparationError("Each selected path must be a regular file.")
        if info.st_size > limit:
            raise PreparationError(
                "The selected files or payload exceed the upload size limit."
            )
        content = stream.read(limit + 1)
    if not content:
        raise PreparationError("Selected files and the payload must not be empty.")
    if len(content) > limit:
        raise PreparationError(
            "The selected files or payload exceed the upload size limit."
        )
    return content


def reject_constant(_value: str) -> None:
    raise PreparationError("Payload JSON must not contain NaN or Infinity.")


def previous_attempt(receipt_path: Path) -> dict:
    """Never call an earlier accepted or pending attempt 'not submitted'."""
    try:
        receipt = json.loads(read_regular_file(receipt_path, MAX_RESPONSE_BYTES))
        if (
            isinstance(receipt, dict)
            and receipt.get("status") == "accepted"
            and receipt.get("processing_status") == "queued"
            and isinstance(receipt.get("submission_reference"), str)
            and re.fullmatch(PUBLIC_REFERENCE_PATTERN, receipt["submission_reference"])
        ):
            return {
                "status": "accepted",
                "submission_reference": receipt["submission_reference"],
                "processing_status": "queued",
                "previously_recorded": True,
                "automatic_retry_allowed": False,
                "message": "An accepted receipt already exists. No new request was sent.",
            }
        if (
            isinstance(receipt, dict)
            and receipt.get("status") == "error"
            and receipt.get("code") == "connection_failed"
            and receipt.get("submission_outcome") == "not_submitted"
        ):
            return {
                **receipt,
                "previously_recorded": True,
                "automatic_retry_allowed": True,
                "retry_requires_network_access": True,
                "message": (
                    "The earlier attempt failed before opening a connection, so no request "
                    "was sent. The same approved payload and files may be retried with "
                    "--retry-connection-failure after outbound network access is enabled."
                ),
            }
    except (OSError, ValueError):
        pass
    return error(
        "prior_attempt",
        "An earlier attempt or pending receipt exists. No new request was sent; read the receipt and contact support before retrying.",
        "unknown",
    )


def open_retryable_connection_receipt(receipt_path: Path) -> int:
    """Open and clear only a receipt that proves no connection was opened."""
    flags = os.O_RDWR | getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(receipt_path, flags)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_size > MAX_RESPONSE_BYTES:
            raise PreparationError(
                "The prior receipt is not a retryable connection-failure receipt."
            )
        raw = os.read(fd, MAX_RESPONSE_BYTES + 1)
        receipt = json.loads(raw)
        if not (
            isinstance(receipt, dict)
            and receipt.get("status") == "error"
            and receipt.get("code") == "connection_failed"
            and receipt.get("submission_outcome") == "not_submitted"
        ):
            raise PreparationError(
                "Only a recorded pre-connection failure can use "
                "--retry-connection-failure."
            )
        os.lseek(fd, 0, os.SEEK_SET)
        os.ftruncate(fd, 0)
        return fd
    except Exception:
        os.close(fd)
        raise


def prepare(
    payload_path: Path, document_paths: list[Path]
) -> tuple[bytes, str, list[dict]]:
    if not 1 <= len(document_paths) <= 10:
        raise PreparationError("Select between one and ten documents.")
    resolved = [path.resolve(strict=True) for path in document_paths]
    if len(set(resolved)) != len(resolved):
        raise PreparationError("The same selected file was included more than once.")
    payload = json.loads(
        read_regular_file(payload_path, MAX_PAYLOAD_BYTES),
        parse_constant=reject_constant,
    )
    if not isinstance(payload, dict) or payload.get("submission_type") not in (
        "claim",
        "portfolio",
    ):
        raise PreparationError("Payload must be a claim or portfolio JSON object.")
    # Definitive field validation stays on the server before any backend POST.
    payload_bytes = json.dumps(
        payload, ensure_ascii=False, allow_nan=False, separators=(",", ":")
    ).encode("utf-8")
    boundary = "delos-" + uuid.uuid4().hex
    parts = []

    def append_part(
        name: str, data: bytes, mime: str, filename: str | None = None
    ) -> None:
        disposition = f'Content-Disposition: form-data; name="{name}"'
        if filename is not None:
            disposition += f'; filename="{filename}"'
        parts.append(
            (f"--{boundary}\r\n{disposition}\r\nContent-Type: {mime}\r\n\r\n").encode()
            + data
            + b"\r\n"
        )

    append_part("payload", payload_bytes, "application/json")
    append_part("confirmed", b"true", "text/plain")
    metadata = []
    total_files = 0
    for source, resolved_path in zip(document_paths, resolved):
        try:
            content = read_regular_file(resolved_path, MAX_BYTES - total_files)
        except PreparationError as exc:
            if "size limit" in str(exc):
                raise PreparationError(LARGE_FILE_GUIDANCE) from None
            raise
        total_files += len(content)
        filename = re.sub(r'[\x00-\x1f\x7f"\\/]', "_", source.name)[:180]
        if not filename:
            raise PreparationError("A selected document has no usable filename.")
        mime = mimetypes.guess_type(filename)[0] or "application/octet-stream"
        append_part("documents", content, mime, filename)
        metadata.append(
            {
                "filename": filename,
                "bytes": len(content),
                "content_type": mime,
                "sha256": hashlib.sha256(content).hexdigest(),
            }
        )
    body = b"".join(parts) + f"--{boundary}--\r\n".encode("ascii")
    if len(body) > MAX_BYTES:
        raise PreparationError(LARGE_FILE_GUIDANCE)
    return body, f"multipart/form-data; boundary={boundary}", metadata


def send_once(body: bytes, content_type: str, *, endpoint: str = ENDPOINT) -> dict:
    destination = urlsplit(endpoint)
    # A loopback override exists only for executable integration tests; arbitrary
    # hosts cannot be selected by the model or by text inside a document.
    loopback = (
        destination.scheme == "http"
        and destination.hostname in ("127.0.0.1", "::1")
        and destination.path == "/mcp"
        and not destination.query
        and not destination.fragment
        and not destination.username
    )
    if endpoint != ENDPOINT and not loopback:
        raise PreparationError(
            "The upload destination must be the configured Delos endpoint."
        )
    cls = (
        http.client.HTTPSConnection
        if destination.scheme == "https"
        else http.client.HTTPConnection
    )
    connection = cls(destination.hostname, destination.port, timeout=35)
    started = False
    try:
        connection.connect()
        started = True
        connection.request(
            "POST",
            "/mcp",
            body=body,
            headers={
                "Content-Type": content_type,
                "Content-Length": str(len(body)),
                "X-Delos-Upload-Version": "1",
                "Accept": "application/json",
                "User-Agent": "Delos-local-upload/1.0.10",
            },
        )
        response = connection.getresponse()
        raw = response.read(MAX_RESPONSE_BYTES + 1)
        if len(raw) > MAX_RESPONSE_BYTES:
            raise ValueError("Oversized receipt")
        data = json.loads(raw)
        if not isinstance(data, dict):
            raise TypeError("Invalid receipt")
        if (
            response.status in (200, 202)
            and data.get("status") == "accepted"
            and data.get("processing_status") == "queued"
            and isinstance(data.get("submission_reference"), str)
            and re.fullmatch(PUBLIC_REFERENCE_PATTERN, data["submission_reference"])
        ):
            return {**data, "automatic_retry_allowed": False}
        if (
            response.status in (200, 400, 403, 413, 415, 422, 502)
            and data.get("status") == "error"
            and data.get("submission_outcome")
            in ("not_submitted", "rejected", "unknown")
        ):
            return {**data, "automatic_retry_allowed": False}
        raise ValueError("No verified receipt")
    except (OSError, http.client.HTTPException, ValueError, TypeError):
        if started:
            return error(
                "submission_outcome_unknown",
                "No verified receipt was received. Do not retry; contact Delos support to check the submission.",
                "unknown",
            )
        return {
            **error(
                "connection_failed",
                "Could not connect to Delos before any request was sent. Retry only after enabling outbound network access, using the same reviewed payload and files.",
                "not_submitted",
                automatic_retry_allowed=True,
            ),
            "retry_requires_network_access": True,
        }
    finally:
        connection.close()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--payload", type=Path, required=True, help="Prepared submission JSON file"
    )
    parser.add_argument(
        "--document",
        type=Path,
        action="append",
        required=True,
        help="An exact user-selected local file; repeat for every document",
    )
    parser.add_argument(
        "--confirmed", action="store_true", help="User approved these details and files"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Check files and size without any network call",
    )
    parser.add_argument(
        "--receipt",
        type=Path,
        help="New receipt path; default: payload.delos-receipt.json",
    )
    parser.add_argument(
        "--retry-connection-failure",
        action="store_true",
        help=(
            "Retry the same approved payload and files after a recorded pre-connection "
            "failure, with outbound network access enabled"
        ),
    )
    args = parser.parse_args(argv)
    receipt_path = args.receipt or args.payload.with_suffix(".delos-receipt.json")
    submission_started = False
    result = None
    try:
        if not args.dry_run and not args.confirmed:
            raise PreparationError(
                "Explicit approval of the completed submission is required before sending."
            )
        if args.dry_run and args.retry_connection_failure:
            raise PreparationError(
                "--retry-connection-failure cannot be used with --dry-run."
            )
        if (
            not args.dry_run
            and receipt_path.exists()
            and not args.retry_connection_failure
        ):
            result = previous_attempt(receipt_path)
            print(json.dumps(result))
            return 0 if result.get("status") == "accepted" else 1
        if (
            not args.dry_run
            and args.retry_connection_failure
            and not receipt_path.exists()
        ):
            raise PreparationError(
                "--retry-connection-failure requires an existing connection-failure receipt."
            )
        body, content_type, files = prepare(args.payload, args.document)
        evidence = {
            "documents": files,
            "request_bytes": len(body),
            "endpoint": ENDPOINT,
        }
        if args.dry_run:
            print(
                json.dumps(
                    {
                        "status": "ready",
                        "submission_outcome": "not_submitted",
                        **evidence,
                    }
                )
            )
            return 0
        pending = {
            **error(
                "pending_attempt",
                "Submission started; check the final receipt before any further action.",
                "unknown",
            ),
            **evidence,
        }
        # Exclusive creation also blocks concurrent invocations of the same command.
        if args.retry_connection_failure:
            fd = open_retryable_connection_receipt(receipt_path)
        else:
            try:
                fd = os.open(
                    receipt_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600
                )
            except FileExistsError:
                result = previous_attempt(receipt_path)
                print(json.dumps(result))
                return 0 if result.get("status") == "accepted" else 1
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(pending, stream, indent=2)
            stream.flush()
            os.fsync(stream.fileno())
            submission_started = True
            result = {**send_once(body, content_type), **evidence}
            try:
                stream.seek(0)
                json.dump(result, stream, indent=2)
                stream.truncate()
                stream.flush()
                os.fsync(stream.fileno())
            except OSError:
                # Preserve and display the real accepted receipt even if disk fails.
                result["receipt_write_failed"] = True
        print(json.dumps(result))
        return 0 if result.get("status") == "accepted" else 1
    except (PreparationError, OSError, ValueError) as exc:
        if submission_started:
            if result is not None and result.get("status") == "accepted":
                print(json.dumps({**result, "receipt_write_failed": True}))
                return 0
            print(
                json.dumps(
                    error(
                        "submission_outcome_unknown",
                        "The attempt did not finish cleanly. Read the receipt and do not retry.",
                        "unknown",
                    )
                )
            )
            return 1
        message = (
            str(exc)
            if isinstance(exc, PreparationError)
            else "Unable to prepare the files or reserve the receipt. No request was sent."
        )
        print(json.dumps(error("preparation_failed", message)))
        return 1


if __name__ == "__main__":
    sys.exit(main())
