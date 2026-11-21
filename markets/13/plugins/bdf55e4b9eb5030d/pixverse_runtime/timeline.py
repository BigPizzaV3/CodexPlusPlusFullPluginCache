"""Compatibility import for the Codex runtime."""

import sys

from .studio import timeline as _implementation

sys.modules[__name__] = _implementation
