"""Shared helpers for the Meetings MCP runtime."""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import re
import ssl
from collections.abc import Mapping, Sequence
from datetime import datetime, timedelta, timezone
from http.client import HTTPMessage
from typing import IO, TypeAlias, TypeGuard, cast
from urllib.request import HTTPRedirectHandler, Request

ACCOUNT_SCOPE_GENERATION_PATTERN = re.compile(r"^[A-Za-z0-9_-]{43}$")
MAXIMUM_JSON_DEPTH = 128

JSONScalar: TypeAlias = None | bool | int | float | str
JSONValue: TypeAlias = JSONScalar | Sequence["JSONValue"] | Mapping[str, "JSONValue"]


class DuplicateJSONKeyError(ValueError):
    """Raised when a decoded JSON object repeats a key."""


class NoRedirectHandler(HTTPRedirectHandler):
    """Prevent credential-bearing Meetings requests from following redirects."""

    def redirect_request(
        self,
        req: Request,
        fp: IO[bytes],
        code: int,
        msg: str,
        headers: HTTPMessage,
        newurl: str,
    ) -> None:
        return None


def create_https_context() -> ssl.SSLContext:
    """Keep normal HTTPS verification while adding the selected enterprise CA bundle."""
    context = ssl.create_default_context()
    context.set_alpn_protocols(["http/1.1"])
    if getattr(context, "post_handshake_auth", None) is not None:
        context.post_handshake_auth = True
    custom_ca = os.environ.get("CODEX_CA_CERTIFICATE") or os.environ.get("SSL_CERT_FILE")
    if custom_ca:
        context.load_verify_locations(cafile=custom_ca)
    return context


def is_json(value: object) -> TypeGuard[dict[str, object]]:
    """Check whether a value is a shallow string-keyed JSON object.

    Args:
        value: Candidate decoded or application-produced value.

    Returns:
        Whether the value is a dictionary with only string keys. Values remain
        unvalidated so callers can apply their own schema-specific checks.
    """

    if not isinstance(value, dict):
        return False
    record = cast(dict[object, object], value)
    return all(isinstance(key, str) for key in record)


def is_json_array(value: object) -> TypeGuard[list[object]]:
    """Narrow a decoded value to a JSON array.

    Args:
        value: Candidate decoded JSON value.

    Returns:
        Whether the value is represented by a Python list.
    """

    return isinstance(value, list)


def is_json_value(value: object) -> TypeGuard[JSONValue]:
    """Check whether a value is recursively safe to serialize as JSON.

    Args:
        value: Candidate decoded or application-produced value.

    Returns:
        Whether the value contains only JSON scalars, arrays, and string-keyed
        objects.
    """

    if value is None or isinstance(value, bool | int | float | str):
        return True
    if is_json_array(value):
        return all(is_json_value(item) for item in value)
    if is_json(value):
        return all(is_json_value(item) for item in value.values())
    return False


def unique_json_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    """Build a decoded JSON object while rejecting duplicate keys.

    Args:
        pairs: Ordered key-value pairs supplied by ``json.loads``.

    Returns:
        A dictionary containing each unique key exactly once.

    Raises:
        DuplicateJSONKeyError: If the encoded object repeats a key.
    """

    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJSONKeyError("duplicate JSON object key")
        result[key] = value
    return result


def parse_bounded_json(text: str) -> object:
    """Decode trust metadata with fixed nesting and unique object keys.

    Python's JSON decoder has different recursion limits across versions.
    Bound container nesting before decoding so acceptance and memory use do
    not depend on the interpreter. The decoder still validates JSON grammar.

    Args:
        text: Encoded JSON whose byte size is bounded by the caller.

    Returns:
        The decoded value for the caller's schema validation.

    Raises:
        ValueError: If nesting exceeds the fixed bound, keys repeat, or JSON
            syntax or numeric constants are invalid.
    """

    depth = 0
    in_string = False
    escaped = False
    for character in text:
        if in_string:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == '"':
                in_string = False
        elif character == '"':
            in_string = True
        elif character in "[{":
            depth += 1
            if depth > MAXIMUM_JSON_DEPTH:
                raise ValueError("JSON nesting is too deep")
        elif character in "]}":
            depth -= 1
    value: object = json.loads(text, object_pairs_hook=unique_json_object, parse_constant=int)
    return value


def account_scope_generation(
    secret: bytes,
    account_fingerprint: bytes,
    *,
    domain: bytes,
) -> str:
    """Derive an opaque, domain-separated account-scope generation.

    Args:
        secret: Client-lifetime 256-bit secret.
        account_fingerprint: Stable 256-bit account fingerprint.
        domain: Fixed domain separator for the consuming client.

    Returns:
        A URL-safe opaque generation that exposes no account material.

    Raises:
        ValueError: If an input does not satisfy the derivation contract.
        RuntimeError: If the derived value violates its fixed wire shape.
    """

    if len(secret) != hashlib.sha256().digest_size:
        raise ValueError("account scope secret is invalid")
    if len(account_fingerprint) != hashlib.sha256().digest_size:
        raise ValueError("account fingerprint is invalid")
    if not domain or not domain.endswith(b"\0"):
        raise ValueError("account scope domain is invalid")
    digest = hmac.new(secret, domain + account_fingerprint, hashlib.sha256).digest()
    generation = base64.urlsafe_b64encode(digest).decode("ascii").rstrip("=")
    if ACCOUNT_SCOPE_GENERATION_PATTERN.fullmatch(generation) is None:
        raise RuntimeError("account scope generation is invalid")
    return generation


def local_day_bounds(
    now: datetime,
    day_offset: int,
    day_count: int = 1,
) -> tuple[datetime, datetime]:
    """Calculate a local-calendar window expressed as UTC instants.

    Args:
        now: Anchor instant whose local timezone defines calendar-day boundaries.
        day_offset: Number of local calendar days from the anchor day.
        day_count: Number of local calendar days in the window.

    Returns:
        Inclusive start and exclusive end instants normalized to UTC.
    """

    local_day = now.astimezone().date() + timedelta(days=day_offset)
    next_local_day = local_day + timedelta(days=day_count)
    return (
        datetime.combine(local_day, datetime.min.time()).astimezone(timezone.utc),
        datetime.combine(next_local_day, datetime.min.time()).astimezone(timezone.utc),
    )
