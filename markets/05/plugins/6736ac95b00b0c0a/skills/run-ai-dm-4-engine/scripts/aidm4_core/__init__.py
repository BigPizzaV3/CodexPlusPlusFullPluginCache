"""AI-DM 4.0 canonical campaign engine."""

from .db import connect, initialize_database
from .kernel import (
    DuplicateSourceTurn,
    KernelError,
    Mutation,
    SimulatedCrash,
    TurnDraft,
    commit_turn,
    stable_source_turn_id,
)

__all__ = [
    "DuplicateSourceTurn",
    "KernelError",
    "Mutation",
    "SimulatedCrash",
    "TurnDraft",
    "commit_turn",
    "connect",
    "initialize_database",
    "stable_source_turn_id",
]

__version__ = "4.0.0-dev1"
