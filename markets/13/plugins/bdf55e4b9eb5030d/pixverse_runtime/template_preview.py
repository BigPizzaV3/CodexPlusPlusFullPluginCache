"""Compatibility import for the Codex runtime."""

import sys

from .studio import template_preview as _implementation

sys.modules[__name__] = _implementation
