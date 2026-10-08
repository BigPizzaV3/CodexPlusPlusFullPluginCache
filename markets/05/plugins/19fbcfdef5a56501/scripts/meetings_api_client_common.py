"""Shared validation and request helpers for direct Meetings API clients."""

from __future__ import annotations

import hashlib
import re

from codex_auth_client import AuthMaterial, chatgpt_auth_subject

MAXIMUM_MEETING_TITLE_BYTES = 4 * 1024
MAXIMUM_MEETING_TITLE_CHARACTERS = 512
# Persisted native owner/account bindings must remain compatible with released companions.
_LEGACY_ACCOUNT_SCOPE_V1_DOMAIN = b"com.openai.sushi.chatgpt-auth-scope/v1\x00"


def record_account_fingerprint(auth: AuthMaterial) -> bytes:
    """Derive the stable process-local account binding used by Record clients.

    Args:
        auth: Validated ChatGPT authentication material.

    Returns:
        The native-compatible SHA-256 scope digest of the user and account.
    """

    account = auth.account_id.encode("utf-8")
    if auth.subject is None:
        # Historical injected providers do not expose a JWT subject. Real
        # Codex app-server material always has a validated subject.
        return hashlib.sha256(account).digest()
    subject = auth.subject.encode("utf-8")
    scope = bytearray(_LEGACY_ACCOUNT_SCOPE_V1_DOMAIN)
    scope.extend(str(len(subject)).encode("ascii"))
    scope.extend(b":")
    scope.extend(subject)
    scope.extend(b"\x00\x01")
    scope.extend(str(len(account)).encode("ascii"))
    scope.extend(b":")
    scope.extend(account)
    scope.extend(b"\x00")
    return hashlib.sha256(scope).digest()


def record_owner_scope_fingerprint(auth: AuthMaterial) -> str | None:
    """Bind ownership to the exact authenticated Record user and account.

    Args:
        auth: Validated ChatGPT authentication material.

    Returns:
        The native-compatible owner fingerprint, or ``None`` if account ownership
        cannot be established safely.
    """

    account, subject = auth.account_id.strip(), chatgpt_auth_subject(auth)
    if subject is None or re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:@-]{0,255}", account) is None:
        return None
    try:
        subject_bytes, account_bytes = subject.encode("utf-8"), account.encode("utf-8")
    except UnicodeEncodeError:
        return None
    if len(subject_bytes) > 1024:
        return None
    material = bytearray(_LEGACY_ACCOUNT_SCOPE_V1_DOMAIN)
    material.extend(f"{len(subject_bytes)}:".encode("ascii") + subject_bytes + b"\0\x01")
    material.extend(f"{len(account_bytes)}:".encode("ascii") + account_bytes + b"\0")
    return hashlib.sha256(material).hexdigest()


def bounded_timeout_seconds(value: object) -> float:
    """Validate a Record request timeout and normalize it to seconds.

    Args:
        value: Candidate numeric timeout.

    Returns:
        The validated timeout as a float.

    Raises:
        ValueError: If the timeout is nonnumeric or outside the supported range.
    """

    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("timeout_seconds must be numeric")
    timeout = float(value)
    if not 0.1 <= timeout <= 5 * 60:
        raise ValueError("timeout_seconds is out of range")
    return timeout


def record_request_headers(
    auth: AuthMaterial,
    *,
    has_json_body: bool = False,
) -> dict[str, str]:
    """Build fixed first-party headers for one authenticated Record request.

    Args:
        auth: Validated ChatGPT authentication material.
        has_json_body: Whether the request carries a JSON body.

    Returns:
        A fresh header dictionary containing authentication and content metadata.
    """

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {auth.token}",
        "Cache-Control": "no-store",
        "ChatGPT-Account-Id": auth.account_id,
        # chatgpt.com rejects generic Python clients at the edge. This fixed
        # first-party identity mirrors the native product without exposing
        # host, Python, Codex, account, or plugin version details.
        "User-Agent": "ChatGPT Meetings/1.0",
    }
    if has_json_body:
        headers["Content-Type"] = "application/json"
    return headers


def nonempty_string(
    value: object,
    *,
    maximum_bytes: int,
    allow_controls: bool = False,
) -> str | None:
    """Normalize a bounded nonempty string from an untrusted value.

    Args:
        value: Candidate string value.
        maximum_bytes: Maximum UTF-8 size of the normalized string.
        allow_controls: Whether ASCII control characters are accepted.

    Returns:
        The stripped string when valid, otherwise ``None``.
    """

    if not isinstance(value, str):
        return None
    normalized = value.strip()
    try:
        encoded = normalized.encode("utf-8")
    except UnicodeEncodeError:
        return None
    if not normalized or len(encoded) > maximum_bytes:
        return None
    if not allow_controls and any(
        ord(character) < 0x20 or ord(character) == 0x7F for character in normalized
    ):
        return None
    return normalized


def project_meeting_title(value: object) -> str:
    """Project an untrusted meeting title into the bounded app contract.

    Args:
        value: Candidate backend title.

    Returns:
        A safe bounded title, falling back to ``"Meeting"`` when invalid.
    """

    if not isinstance(value, str):
        return "Meeting"
    normalized = value.strip()
    if not normalized or any(
        ord(character) < 0x20 or ord(character) == 0x7F for character in normalized
    ):
        return "Meeting"
    bounded = normalized[:MAXIMUM_MEETING_TITLE_CHARACTERS]
    try:
        encoded = bounded.encode("utf-8")
    except UnicodeEncodeError:
        return "Meeting"
    return bounded if len(encoded) <= MAXIMUM_MEETING_TITLE_BYTES else "Meeting"


__all__ = [
    "MAXIMUM_MEETING_TITLE_BYTES",
    "MAXIMUM_MEETING_TITLE_CHARACTERS",
    "bounded_timeout_seconds",
    "nonempty_string",
    "project_meeting_title",
    "record_account_fingerprint",
    "record_owner_scope_fingerprint",
    "record_request_headers",
]
