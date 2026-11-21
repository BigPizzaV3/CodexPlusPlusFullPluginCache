#!/usr/bin/env python3
"""Transfer MCP-issued file tickets without accessing host OAuth credentials."""
from __future__ import annotations

import argparse
import hashlib
import http.client
import ipaddress
import json
import os
from pathlib import Path
import socket
import ssl
import tempfile
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 64 * 1024 * 1024


def verified_tls_context() -> ssl.SSLContext:
    """Retain platform trust and load Mozilla roots for Python installs without a CA store."""
    context = ssl.create_default_context()
    try:
        import certifi
    except ImportError as exc:
        raise ValueError("Install the plugin requirements to provide trusted TLS certificates") from exc
    context.load_verify_locations(cafile=certifi.where())
    return context


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as output:
            output.write(data)
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def configured_endpoint() -> str:
    servers = json.loads((ROOT / ".mcp.json").read_text())["mcpServers"]
    if len(servers) != 1:
        raise ValueError("Expected exactly one selected Reteno MCP connection")
    return next(iter(servers.values()))["url"]


def validate_url(url: str, endpoint: str) -> tuple[str, int, str]:
    target, server = urlsplit(url), urlsplit(endpoint)
    if (target.scheme != "https" or target.username or target.password or target.fragment
            or not target.hostname or target.hostname != server.hostname
            or (target.port or 443) != (server.port or 443)):
        raise ValueError("A transfer ticket must use the selected MCP server's HTTPS origin")
    if any(ord(c) < 33 or ord(c) == 127 for c in url):
        raise ValueError("Invalid transfer URL")
    return target.hostname, target.port or 443, target.path + ("?" + target.query if target.query else "")


class PinnedHTTPSConnection(http.client.HTTPSConnection):
    """Keep certificate/SNI checks on the hostname while connecting to a checked IP."""
    def connect(self) -> None:
        addresses = socket.getaddrinfo(self.host, self.port, type=socket.SOCK_STREAM)
        if not addresses or any(not ipaddress.ip_address(item[4][0]).is_global for item in addresses):
            raise ValueError("Transfer host must resolve only to public addresses")
        last_error = None
        certificate_error = None
        for family, kind, proto, _, address in addresses:
            raw = socket.socket(family, kind, proto)
            raw.settimeout(self.timeout)
            try:
                raw.connect(address)
                self.sock = self._context.wrap_socket(raw, server_hostname=self.host)
                return
            except (OSError, ssl.SSLError) as exc:
                raw.close()
                last_error = exc
                if isinstance(exc, ssl.SSLCertVerificationError):
                    certificate_error = exc
        if certificate_error is not None:
            raise certificate_error
        raise OSError("Transfer connection failed") from last_error


def transfer(*, url: str, method: str, body: bytes | None = None,
             content_type: str = "application/octet-stream", max_bytes: int = MAX_BYTES,
             endpoint: str | None = None) -> bytes:
    host, port, request_path = validate_url(url, endpoint or configured_endpoint())
    if method not in {"GET", "PUT", "POST"}:
        raise ValueError("Unsupported transfer method")
    if body is not None and len(body) > max_bytes:
        raise ValueError("Upload exceeds the transfer byte limit")
    connection = PinnedHTTPSConnection(host, port, timeout=60, context=verified_tls_context())
    try:
        connection.request(method, request_path, body=body,
                           headers={"Content-Type": content_type} if body is not None else {})
        response = connection.getresponse()
        # Never follow a redirect or print a response body containing ticket data.
        if response.status < 200 or response.status >= 300:
            raise ValueError(f"File transfer returned HTTP {response.status}; preserve the operation ID")
        length = response.getheader("Content-Length")
        expected_length = None
        if length is not None:
            if not length.strip().isascii() or not length.strip().isdigit():
                raise ValueError("Invalid response Content-Length")
            expected_length = int(length)
            if expected_length > max_bytes:
                raise ValueError("Response exceeds the transfer byte limit")
        data = response.read(max_bytes + 1)
        if len(data) > max_bytes:
            raise ValueError("Response exceeds the transfer byte limit")
        if expected_length is not None and len(data) != expected_length:
            raise ValueError("Response was truncated or its Content-Length did not match")
        return data
    finally:
        connection.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=["download", "upload"])
    parser.add_argument("--url", required=True)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--content-type", default="application/json")
    parser.add_argument("--method", choices=["PUT", "POST"], default="PUT")
    parser.add_argument("--sha256")
    parser.add_argument("--max-bytes", type=int, default=MAX_BYTES)
    args = parser.parse_args()
    try:
        if not 0 < args.max_bytes <= MAX_BYTES:
            raise ValueError("max-bytes must be between 1 and 67108864")
        if args.operation == "download":
            if args.output is None:
                raise ValueError("download requires --output")
            data = transfer(url=args.url, method="GET", max_bytes=args.max_bytes)
            digest = hashlib.sha256(data).hexdigest()
            if args.sha256 and digest != args.sha256.lower():
                raise ValueError("Downloaded file checksum does not match its manifest")
            atomic_write(args.output, data)
            print(json.dumps({"downloaded": True, "bytes": len(data), "sha256": digest}))
        else:
            if args.input is None or not args.input.is_file():
                raise ValueError("upload requires an existing --input file")
            if args.input.stat().st_size > args.max_bytes:
                raise ValueError("Upload exceeds the transfer byte limit")
            data = args.input.read_bytes()
            receipt = transfer(url=args.url, method=args.method, body=data,
                               content_type=args.content_type, max_bytes=args.max_bytes)
            if args.output:
                atomic_write(args.output, receipt)
            print(json.dumps({"transferred": True, "bytes": len(data),
                              "sha256": hashlib.sha256(data).hexdigest(), "persisted": False}))
    except (ValueError, OSError, http.client.HTTPException) as exc:
        # These errors are ours or network error classes, never upstream bodies/URLs.
        print(json.dumps({"success": False, "error": str(exc) if isinstance(exc, ValueError)
                          else type(exc).__name__}))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
