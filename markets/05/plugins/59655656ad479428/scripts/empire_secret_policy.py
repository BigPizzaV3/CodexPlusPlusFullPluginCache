"""Shared outbound secret-detection policy for Empire review artifacts."""

from __future__ import annotations

import math
import re
from collections import Counter

SENSITIVE_NAMES = {
    ".env",
    ".env.local",
    ".env.production",
    "credentials",
    "credentials.json",
    "secrets.json",
    "id_rsa",
    "id_ed25519",
}
SENSITIVE_SUFFIXES = {".pem", ".p12", ".pfx", ".key"}
SECRET_PATTERNS = (
    re.compile(r"\bsk-or-v1-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\baa_[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\b(?:github_pat_|ghp_)[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(
        r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----",
        re.S,
    ),
    re.compile(
        r"(?im)^(\s*(?:api[_-]?key|access[_-]?token|auth[_-]?token|password|secret)\s*[:=]\s*)[^\s#]+"
    ),
    re.compile(r"\beyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\b"),
    re.compile(r"(?i)\b(?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis)://[^\s'\"]+"),
)


def high_entropy_secret_labels(value: str) -> list[str]:
    """Return non-secret labels for opaque values unsafe to transmit."""
    labels: list[str] = []
    candidates = re.findall(
        r"(?<![A-Za-z0-9+/=_-])[A-Za-z0-9+/=_-]{32,}(?![A-Za-z0-9+/=_-])",
        value,
    )
    previous_fragments: list[str] = []
    for line in value.splitlines():
        if line.startswith("+") and not line.startswith("+++"):
            fragments = re.findall(r"[A-Za-z0-9+/=_-]{12,}", line[1:])
            if previous_fragments and fragments:
                candidates.append(previous_fragments[-1] + fragments[0])
            previous_fragments = fragments
        else:
            previous_fragments = []
    for candidate in candidates:
        classes = sum(
            bool(re.search(pattern, candidate))
            for pattern in (r"[a-z]", r"[A-Z]", r"[0-9]", r"[+/=_-]")
        )
        if classes < 3:
            continue
        counts = Counter(candidate)
        entropy = -sum(
            (count / len(candidate)) * math.log2(count / len(candidate))
            for count in counts.values()
        )
        if entropy >= 4.3:
            labels.append("high_entropy_value")
    return sorted(set(labels))


def secret_findings(value: str) -> list[str]:
    """Return only policy labels; never return the detected secret value."""
    labels = [
        f"recognized_secret_pattern_{index}"
        for index, pattern in enumerate(SECRET_PATTERNS, start=1)
        if pattern.search(value)
    ]
    labels.extend(high_entropy_secret_labels(value))
    return sorted(set(labels))
