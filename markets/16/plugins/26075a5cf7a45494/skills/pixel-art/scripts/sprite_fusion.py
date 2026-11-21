#!/usr/bin/env python3
"""Sprite Fusion public API client. Python 3.9+, standard library only."""

import argparse
import base64
import binascii
import hashlib
from http.client import HTTPException
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

BASE_URL = "https://www.spritefusion.com/api/v1"
MIME_TYPES = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}
FIELDS = {
    "generate": {"operation", "prompt", "size"},
    "edit": {"operation", "prompt", "size", "inputs"},
    "style-reference": {"operation", "prompt", "size", "inputs"},
    "direction-set": {"operation", "size", "inputs"},
    "animate": {"operation", "prompt", "inputs", "output_frames", "colors"},
}


class ClientError(Exception):
    pass


class HTTPResponseError(ClientError):
    pass


class NoRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # Never forward API credentials or signed-upload headers to a redirect.
        return None


def encode(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def write_result(directory, record):
    temporary = directory / "result.json.tmp"
    temporary.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(directory / "result.json")


def new_directory(parent):
    parent = Path(parent).expanduser().resolve()
    parent.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return Path(tempfile.mkdtemp(prefix=stamp + "-", dir=parent))


class Client:
    def __init__(self, key):
        if not key or any(c.isspace() for c in key):
            raise ClientError("Provide a valid SPRITE_FUSION_API_KEY or use --key-stdin.")
        self.key = key
        self.opener = build_opener(NoRedirects())

    def open(self, method, url, data=None, headers=None, authenticated=False):
        parsed = urlsplit(url)
        if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
            raise ClientError("Only HTTPS URLs without embedded credentials are supported.")
        headers = dict(headers or {})
        if authenticated:
            if parsed.netloc != "www.spritefusion.com" or not parsed.path.startswith("/api/v1/"):
                raise ClientError("API credentials may only be sent to the Sprite Fusion API.")
            headers["Authorization"] = "Bearer " + self.key
        try:
            return self.opener.open(Request(url, data=data, headers=headers, method=method), timeout=180)
        except HTTPError as exc:
            # Do not include request URLs: temporary upload URLs are credentials.
            message = f"HTTP {exc.code}"
            if authenticated:
                try:
                    error = json.loads(exc.read(65536)).get("error", {})
                    message += ": " + str(error.get("code", "api_error")) + ": " + str(error.get("message", "Request failed."))
                except (ValueError, AttributeError):
                    pass
            if exc.headers.get("Retry-After"):
                message += "; Retry-After: " + exc.headers["Retry-After"]
            raise HTTPResponseError(message.replace(self.key, "[redacted]")) from None
        except (URLError, TimeoutError, OSError, HTTPException):
            raise ClientError("Network request interrupted; no automatic retry was made.") from None

    def api(self, method, path, payload=None):
        data = encode(payload) if payload is not None else None
        headers = {"Content-Type": "application/json"} if data is not None else {}
        return self.open(method, BASE_URL + path, data, headers, authenticated=True)

    def get(self, path):
        with self.api("GET", path) as response:
            return json.load(response)

    def upload(self, data, content_type):
        with self.api("POST", "/uploads", {
            "content_type": content_type,
            "size_bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
        }) as response:
            descriptor = json.load(response)
        with self.open("PUT", descriptor["upload_url"], data, descriptor["headers"]):
            pass
        return {"upload_id": descriptor["upload_id"]}


def validate_request(payload):
    if not isinstance(payload, dict):
        raise ClientError("Request must be a JSON object.")
    operation = payload.get("operation")
    if not isinstance(operation, str) or operation not in FIELDS:
        raise ClientError("Unsupported generation operation.")
    if set(payload) - FIELDS[operation]:
        raise ClientError("Unknown fields for this operation.")
    if operation != "direction-set":
        prompt = payload.get("prompt")
        maximum = 2000 if operation == "animate" else 10000
        if not isinstance(prompt, str) or not prompt.strip() or len(prompt.encode("utf-16-le")) // 2 > maximum:
            raise ClientError(f"A nonempty prompt of at most {maximum} characters is required.")
    if "size" in payload or operation == "generate":
        if type(payload.get("size")) is not int or payload["size"] not in (16, 32, 64):
            raise ClientError("Size must be 16, 32, or 64.")
    for field, low, high in (("output_frames", 2, 16), ("colors", 2, 256)):
        if field in payload:
            value = payload[field]
            if type(value) is not int or not low <= value <= high or (field == "output_frames" and value % 2):
                raise ClientError(f"Invalid {field}.")
    if operation != "generate":
        inputs = payload.get("inputs")
        maximum = {"edit": 9, "style-reference": 20}.get(operation, 1)
        if not isinstance(inputs, list) or not 1 <= len(inputs) <= maximum:
            raise ClientError(f"This operation requires between 1 and {maximum} inputs.")
        for source in inputs:
            if not isinstance(source, dict) or len(source) != 1 or not set(source) <= {"file", "asset_id", "data_url", "upload_id"}:
                raise ClientError("Each input needs exactly one source: file, asset_id, data_url, or upload_id.")
            if not isinstance(next(iter(source.values())), str) or not next(iter(source.values())).strip():
                raise ClientError("Input source must be a nonempty string.")


def prepare_request(payload, base_path, client):
    validate_request(payload)
    result = dict(payload)
    sources, prepared, local_files = [], [], []
    inline_bytes = total_bytes = 0
    # Validate/read all inputs before uploading anything.
    for source in payload.get("inputs", []):
        if "file" in source:
            path = (base_path / Path(source["file"]).expanduser()).resolve()
            content_type = MIME_TYPES.get(path.suffix.lower())
            if content_type is None:
                raise ClientError("Local images must use PNG, JPEG, or WebP extensions.")
            with path.open("rb") as handle:
                data = handle.read(20 * 1024 * 1024 + 1)
            if not data or len(data) > 20 * 1024 * 1024:
                raise ClientError("Local input must contain between 1 byte and 20 MiB.")
            total_bytes += len(data)
            sources.append({"file": str(path), "sha256": hashlib.sha256(data).hexdigest()})
            local_files.append((len(prepared), data, content_type))
            prepared.append(None)
        elif "data_url" in source:
            match = re.fullmatch(r"data:image/(png|jpeg|webp);base64,([A-Za-z0-9+/]+={0,2})", source["data_url"])
            try:
                data = base64.b64decode(match[2], validate=True) if match else b""
            except (ValueError, binascii.Error):
                data = b""
            if not data or len(data) > 1000000:
                raise ClientError("Invalid or oversized inline image; use a local file for automatic staging.")
            inline_bytes += len(data)
            total_bytes += len(data)
            prepared.append(dict(source))
            sources.append({"type": "inline", "sha256": hashlib.sha256(data).hexdigest()})
        else:
            prepared.append(dict(source))
            sources.append(dict(source) if "asset_id" in source else {"type": "temporary_upload"})
    if inline_bytes > 2500000 or total_bytes > 40 * 1024 * 1024:
        raise ClientError("Inputs exceed the inline or aggregate byte limit.")
    staged = []
    for index, data, content_type in local_files:
        if len(data) <= 1000000 and inline_bytes + len(data) <= 2500000:
            prepared[index] = {"data_url": f"data:{content_type};base64," + base64.b64encode(data).decode("ascii")}
            inline_bytes += len(data)
        else:
            # Reserve modest space for the signed descriptor while checking JSON size.
            prepared[index] = {"upload_id": "x" * 4096}
            staged.append((index, data, content_type))
    if "inputs" in payload:
        result["inputs"] = prepared
    if len(encode(result)) > 4000000:
        raise ClientError("JSON request exceeds 4,000,000 bytes.")
    for index, data, content_type in staged:
        prepared[index] = client.upload(data, content_type)
    if len(encode(result)) > 4000000:
        raise ClientError("JSON request exceeds 4,000,000 bytes after staging.")
    return result, sources


def events(response):
    lines = []
    for raw_line in response:
        line = raw_line.decode("utf-8").rstrip("\r\n")
        if not line:
            if lines:
                yield json.loads("\n".join(lines))
                lines = []
        elif line.startswith("data:"):
            lines.append(line[5:].lstrip(" "))
    # A partial last event is not a completed SSE block.


def consume_stream(response, record, directory):
    seen_ids, seen_indices = set(), set()
    for event in events(response):
        kind = event.get("type")
        if kind == "started":
            record["request_id"] = event["request_id"]
            record["credits"] = event.get("credits")
            record["status"] = "running"
        elif kind == "progress":
            print("Sprite Fusion: generation in progress", file=sys.stderr, flush=True)
            continue
        elif kind == "output":
            asset, index = event["asset"], event["index"]
            if asset["id"] in seen_ids or index in seen_indices or type(index) is not int or index < 0:
                raise ClientError("Unexpected duplicate or invalid output; inspect saved results before retrying.")
            seen_ids.add(asset["id"])
            seen_indices.add(index)
            record["outputs"].append({"index": index, "asset": asset, "files": {}})
        elif kind == "completed":
            record["completion"] = event
            record["credits"] = event.get("credits")
            if event.get("output_count") != len(record["outputs"]):
                raise ClientError("Output count mismatch; inspect the asset library before retrying.")
            if event.get("status") not in ("succeeded", "failed"):
                raise ClientError("Invalid completion status.")
            if event["status"] == "succeeded" and not record["outputs"]:
                raise ClientError("Success event contained no usable outputs.")
            record["status"] = event["status"]
            write_result(directory, record)
            return
        else:
            continue
        write_result(directory, record)
    raise ClientError("stream_interrupted: no completed event; inspect saved assets before retrying.")


def download_outputs(client, record, directory):
    failed = False
    for output in record["outputs"]:
        asset = output["asset"]
        safe_id = re.sub(r"[^A-Za-z0-9_-]", "_", str(asset["id"]))[:100]
        for field in ("assetUrl", "sourceImageUrl", "spritesheetUrl"):
            if not asset.get(field) or field in output["files"]:
                continue
            extension = ".webp" if field == "assetUrl" and asset.get("type") == "animation" else ".png"
            path = directory / f"{output['index']:02d}-{safe_id}-{field}{extension}"
            partial = path.with_suffix(path.suffix + ".part")
            try:
                with client.open("GET", asset[field]) as response, partial.open("xb") as handle:
                    while True:
                        chunk = response.read(65536)
                        if not chunk:
                            break
                        handle.write(chunk)
                if not partial.stat().st_size:
                    raise ClientError("Empty asset download.")
                partial.replace(path)
                output["files"][field] = str(path)
            except (ClientError, OSError, ValueError, HTTPException):
                failed = True
                output.setdefault("download_errors", {})[field] = "Download failed; recover this saved asset without regenerating."
                partial.unlink(missing_ok=True)
            write_result(directory, record)
    return failed


def generate(client, request_path, output_path):
    request_path = Path(request_path).expanduser().resolve()
    payload = json.loads(request_path.read_text(encoding="utf-8"))
    validate_request(payload)
    directory = new_directory(output_path)
    record = {"operation": payload["operation"], "prompt": payload.get("prompt"),
              "parameters": {k: v for k, v in payload.items() if k not in ("operation", "prompt", "inputs")},
              "created_at": datetime.now(timezone.utc).isoformat(), "status": "preparing", "outputs": []}
    write_result(directory, record)
    print(f"Result directory: {directory}", file=sys.stderr, flush=True)
    submitted = False
    try:
        prepared, sources = prepare_request(payload, request_path.parent, client)
        record["sources"] = sources
        record["status"] = "submitting"
        write_result(directory, record)
        submitted = True
        with client.api("POST", "/generate", prepared) as response:
            if "text/event-stream" not in response.headers.get("Content-Type", "").lower():
                raise ClientError("Expected an SSE response; inspect saved assets before retrying.")
            consume_stream(response, record, directory)
    except (ClientError, OSError, ValueError, KeyError, TypeError, HTTPException) as exc:
        record["status"] = "interrupted" if submitted and not isinstance(exc, HTTPResponseError) else "failed"
        record["error"] = str(exc) if isinstance(exc, ClientError) else "Could not read inputs or finish the response; no retry was made."
        write_result(directory, record)
    except KeyboardInterrupt:
        record["status"] = "interrupted" if submitted else "failed"
        record["error"] = "Cancelled locally; inspect saved assets before resubmitting."
        write_result(directory, record)
        return record, 1
    download_failed = download_outputs(client, record, directory)
    record["result_path"] = str(directory / "result.json")
    write_result(directory, record)
    code = 1 if record["status"] != "succeeded" else (2 if download_failed else 0)
    return record, code


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--key-stdin", action="store_true", help="Read API key from one line of stdin, not an argument")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("credits", help="Get account credits")
    listing = commands.add_parser("assets", help="List one page of saved assets")
    listing.add_argument("--limit", type=int, default=20, choices=range(1, 101), metavar="1-100")
    listing.add_argument("--cursor")
    asset = commands.add_parser("asset", help="Get and optionally download one saved asset")
    asset.add_argument("asset_id")
    asset.add_argument("--output")
    generation = commands.add_parser("generate", help="Run any of the five operations from a JSON request file")
    generation.add_argument("--request", required=True)
    generation.add_argument("--output", required=True)
    args = parser.parse_args()
    key = sys.stdin.readline().strip() if args.key_stdin else os.environ.get("SPRITE_FUSION_API_KEY", "").strip()
    try:
        client = Client(key)
        code = 0
        if args.command == "credits":
            result = client.get("/credits")
        elif args.command == "assets":
            query = {"limit": args.limit}
            if args.cursor:
                query["cursor"] = args.cursor
            result = client.get("/assets?" + urlencode(query))
        elif args.command == "asset":
            result = client.get("/assets/" + quote(args.asset_id, safe=""))
            if args.output:
                directory = new_directory(args.output)
                result = {"operation": "retrieve", "status": "succeeded", "outputs": [{"index": 0, "asset": result["asset"], "files": {}}], "result_path": str(directory / "result.json")}
                write_result(directory, result)
                code = 2 if download_outputs(client, result, directory) else 0
        else:
            result, code = generate(client, args.request, args.output)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return code
    except (ClientError, OSError, ValueError, KeyError, TypeError) as exc:
        message = str(exc) if isinstance(exc, ClientError) else "Unable to read the request or API response."
        print(json.dumps({"error": message.replace(key, "[redacted]") if key else message}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
