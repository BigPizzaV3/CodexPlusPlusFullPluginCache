"""Request-local desktop observations; never infer the app build from its CLI."""

from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
from contextvars import ContextVar

_CODEX_VERSION: ContextVar[str] = ContextVar("meetings_codex_host_version", default="")


def get_current_codex_version() -> str:
    """Return the validated desktop build observed by this request, if any."""
    return _CODEX_VERSION.get()


@contextmanager
def scoped_codex_version(version: str) -> Iterator[None]:
    """Scope an already validated host observation across synchronous dispatch."""
    token = _CODEX_VERSION.set(version)
    try:
        yield
    finally:
        _CODEX_VERSION.reset(token)
