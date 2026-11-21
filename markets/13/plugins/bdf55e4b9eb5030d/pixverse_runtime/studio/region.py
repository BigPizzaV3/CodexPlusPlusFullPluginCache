"""Shared creation contract."""

import sys

from ..core import region as _implementation

sys.modules[__name__] = _implementation
