#!/usr/bin/env python3
"""Validated prompt-data and URL boundaries for the Meetings MCP runtime."""

from __future__ import annotations

import re
from typing import Literal, TypedDict
from urllib.parse import quote

from runtime_config import (
    LOCAL_DEVELOPMENT_MARKETPLACE,
    LOCAL_DEVELOPMENT_PLUGIN,
    TRUSTED_MEETINGS_PLUGIN_PUBLISHERS,
)


class InvalidArguments(ValueError):
    """The caller supplied an invalid Meetings tool argument."""


class PromptPayload(TypedDict):
    """Fixed model context and prompt prepared for a new Codex task."""

    modelContext: str
    prompt: str


def require_string(
    value: object,
    label: str,
    *,
    nonempty: bool = False,
    nullable: bool = False,
) -> str | None:
    """Validate one untrusted optional or required string argument.

    Args:
        value: Candidate argument value.
        label: Safe field label used in validation errors.
        nonempty: Whether whitespace-only strings are rejected.
        nullable: Whether ``None`` is accepted.

    Returns:
        The original string, or ``None`` when explicitly allowed.
    """

    if value is None and nullable:
        return None
    if not isinstance(value, str):
        raise InvalidArguments(f"{label} must be a string")
    if nonempty and not value.strip():
        raise InvalidArguments(f"{label} must be a non-empty string")
    return value


PROMPT_MEETING_ID_PATTERN = re.compile(r"[A-Za-z0-9_-]{1,512}")
RESOURCE_MEETING_ID_PATTERN = re.compile(r"[A-Za-z0-9_-]{1,512}")
PROMPT_SERVER_NAME_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")


def require_prompt_meeting_id(value: object) -> str:
    """Validate the raw canonical Record identifier used by prompt preparation.

    Args:
        value: Candidate raw canonical meeting or private-note identifier.

    Returns:
        The normalized canonical meeting or private-note identifier.
    """

    meeting_id = require_string(value, "meetingId", nonempty=True)
    assert meeting_id is not None
    normalized_id = meeting_id.strip()
    if not PROMPT_MEETING_ID_PATTERN.fullmatch(normalized_id):
        raise InvalidArguments("meetingId is malformed")
    return normalized_id


def _require_resource_meeting_id(value: object) -> str:
    meeting_id = require_string(value, "meetingId", nonempty=True)
    assert meeting_id is not None
    normalized_id = meeting_id.strip()
    if not RESOURCE_MEETING_ID_PATTERN.fullmatch(normalized_id):
        raise InvalidArguments("meetingId is malformed")
    return normalized_id


def require_prompt_title(value: object) -> str:
    """Validate a bounded source title used as a resource-link label.

    Args:
        value: Candidate meeting title.

    Returns:
        The normalized bounded title.
    """

    title = require_string(value, "title", nonempty=True)
    assert title is not None
    normalized_title = title.strip()
    if len(normalized_title) > 512 or any(
        ord(character) < 32 or ord(character) == 127 for character in normalized_title
    ):
        raise InvalidArguments("title is malformed")
    return normalized_title


def _require_prompt_server_name(value: object) -> str:
    server_name = require_string(value, "serverName", nonempty=True)
    assert server_name is not None
    normalized_name = server_name.strip()
    if not PROMPT_SERVER_NAME_PATTERN.fullmatch(normalized_name):
        raise InvalidArguments("serverName is malformed")
    return normalized_name


def _escape_markdown_link_label(value: str) -> str:
    # Codex resource chips decode HTML entities but otherwise render the source
    # label literally. Entities preserve the visible title without leaking
    # Markdown backslashes while keeping title text inside the link boundary.
    return (
        value.replace("&", "&amp;")
        .replace("\\", "&#92;")
        .replace("[", "&#91;")
        .replace("]", "&#93;")
    )


def build_resource_link(
    resource_id: str,
    *,
    server_name: str,
    resource_kind: Literal["meeting", "note"],
) -> str:
    """Build the Codex reference to one canonical Meetings MCP resource.

    Args:
        resource_id: Canonical meeting or private-note identifier.
        server_name: MCP server that owns the resource.
        resource_kind: Backend source associated with the identifier.

    Returns:
        A server-qualified MCP resource reference for prompt or clipboard links.
    """

    normalized_id = _require_resource_meeting_id(resource_id)
    normalized_server = _require_prompt_server_name(server_name)
    resource_uri = f"meetings://{resource_kind}/{normalized_id}"
    return f"mcp-resource://{normalized_server}/{quote(resource_uri, safe='')}"


def build_note_payload(
    resource_id: str,
    title: str,
    *,
    server_name: str,
    resource_kind: Literal["meeting", "note"] = "meeting",
    marketplace_name: object,
    plugin_name: object,
    allow_local_development: bool = False,
) -> PromptPayload:
    """Build the fixed prompt payload for one validated meeting resource.

    Args:
        resource_id: Canonical Record Meeting or UserMeetingNote identifier.
        title: Source-backed meeting title shown on the resource chip.
        server_name: MCP server name that owns the meeting resource.
        resource_kind: Whether the canonical identifier belongs to a meeting or private note.
        marketplace_name: Trusted publisher of the current Meetings installation.
        plugin_name: Plugin name of the verified production or local development registration.
        allow_local_development: Whether the verified installation uses the explicit local policy.

    Returns:
        Fixed model context and a prompt containing the meeting resource link.
    """

    normalized_title = require_prompt_title(title)
    official = (
        isinstance(marketplace_name, str)
        and isinstance(plugin_name, str)
        and marketplace_name in TRUSTED_MEETINGS_PLUGIN_PUBLISHERS
        and plugin_name == "chatgpt-meetings"
    )
    development = (
        allow_local_development
        and isinstance(marketplace_name, str)
        and marketplace_name == LOCAL_DEVELOPMENT_MARKETPLACE
        and isinstance(plugin_name, str)
        and plugin_name in {"chatgpt-meetings", LOCAL_DEVELOPMENT_PLUGIN}
    )
    if not official and not development:
        raise InvalidArguments("Meetings plugin publisher is not trusted")
    resource_href = build_resource_link(
        resource_id, server_name=server_name, resource_kind=resource_kind
    )
    resource_link = f"[{_escape_markdown_link_label(normalized_title)}]({resource_href})"
    plugin_mention = f"[@Meetings](plugin://{plugin_name}@{marketplace_name})"
    return {
        "modelContext": (
            "The user opened a new Codex chat from a meeting in the Meetings app. "
            "The attached MCP resource identifies that exact meeting context."
        ),
        "prompt": f"{plugin_mention} {resource_link}",
    }


__all__ = [
    "PROMPT_MEETING_ID_PATTERN",
    "InvalidArguments",
    "build_note_payload",
    "build_resource_link",
    "require_prompt_meeting_id",
    "require_prompt_title",
    "require_string",
]
