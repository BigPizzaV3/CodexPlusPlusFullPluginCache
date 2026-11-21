"""Compatibility import for the Codex runtime."""

import sys

from .studio import cli as _implementation

if __name__ == "__main__":
    raise SystemExit(_implementation.main())
else:
    sys.modules[__name__] = _implementation
