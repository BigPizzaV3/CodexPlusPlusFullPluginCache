# GENERATED FILE. DO NOT EDIT.
# Source: chatgpt-meetings-core/contracts/companion-control-health.v1.schema.json
# SHA-256: 4cfc756a220ba4c26be9725ff8e535f1c8801aef41f59bb64b0a9bb4db7d786a
# Regenerate: python3 chatgpt-meetings-core/scripts/generate_recording_control_stream_contract.py

from __future__ import annotations

import re
from collections.abc import Mapping
from typing import TYPE_CHECKING, Final, Literal, TypedDict

if TYPE_CHECKING:
    from typing import TypeGuard
else:
    try:
        from typing import TypeGuard
    except ImportError:

        class TypeGuard:
            @classmethod
            def __class_getitem__(cls, _value: object) -> type[bool]:
                return bool


HEALTH_VERSION: Final = 1
HEALTH_MAX_BYTES: Final = 2048
HEALTH_MAX_TTL_MILLIS: Final = 5000
HEALTH_MAX_ENDPOINT_CHARACTERS: Final = 1024


def _is_object(value: object) -> TypeGuard[Mapping[object, object]]:
    return isinstance(value, dict)


class HealthSupport(TypedDict):
    version: Literal[1]
    ownerEpoch: str
    pid: int


def is_health_support(value: object) -> TypeGuard[HealthSupport]:
    return (
        _is_object(value)
        and set(value) == {"version", "ownerEpoch", "pid"}
        and type(value["version"]) is int
        and value["version"] == 1
        and isinstance(value["ownerEpoch"], str)
        and re.fullmatch(
            "^[A-Za-z0-9_-]{8,128}$",
            value["ownerEpoch"],
        )
        is not None
        and type(value["pid"]) is int
        and value["pid"] >= 1
        and value["pid"] <= 4294967295
    )


class HealthRequest(TypedDict):
    version: Literal[1]
    ownerEpoch: str
    requestId: str
    deadlineUnixMillis: int


def is_health_request(value: object) -> TypeGuard[HealthRequest]:
    return (
        _is_object(value)
        and set(value)
        == {
            "version",
            "ownerEpoch",
            "requestId",
            "deadlineUnixMillis",
        }
        and type(value["version"]) is int
        and value["version"] == 1
        and isinstance(value["ownerEpoch"], str)
        and re.fullmatch(
            "^[A-Za-z0-9_-]{8,128}$",
            value["ownerEpoch"],
        )
        is not None
        and isinstance(value["requestId"], str)
        and re.fullmatch(
            "^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
            value["requestId"],
        )
        is not None
        and type(value["deadlineUnixMillis"]) is int
        and value["deadlineUnixMillis"] >= 1
        and value["deadlineUnixMillis"] <= 9007199254740991
    )


class HealthResponse(TypedDict):
    version: Literal[1]
    ownerEpoch: str
    requestId: str
    endpoint: str


def is_health_response(value: object) -> TypeGuard[HealthResponse]:
    return (
        _is_object(value)
        and set(value) == {"version", "ownerEpoch", "requestId", "endpoint"}
        and type(value["version"]) is int
        and value["version"] == 1
        and isinstance(value["ownerEpoch"], str)
        and re.fullmatch(
            "^[A-Za-z0-9_-]{8,128}$",
            value["ownerEpoch"],
        )
        is not None
        and isinstance(value["requestId"], str)
        and re.fullmatch(
            "^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
            value["requestId"],
        )
        is not None
        and isinstance(value["endpoint"], str)
        and re.fullmatch("^[^\\u0000\\r\\n]+$", value["endpoint"]) is not None
        and len(value["endpoint"]) >= 1
        and len(value["endpoint"]) <= 1024
    )
