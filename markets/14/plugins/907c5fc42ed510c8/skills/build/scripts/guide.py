"""Read-only preview of Build_'s welcome/help; not a ChatGPT composer integration.

No engine, project directory, database, account API, network request or log writer is used.
The installed skill may read the same bundled Markdown without executing this helper.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

AUTO = Path(__file__).resolve().parents[1] / "Automation"
COMPOSER_LABEL = 'Build_'
TEXT_ALIASES = ('Build Faster', 'BuildFaster')
LEGACY_LABEL = 'Build_: /help to get started'
_HELP = frozenset(("/help", "help", "help please", "please help", "show help",
                   "how do i use build_", "how do i use build",
                   "how do i use build faster", "how do i use buildfaster",
                   "how do i get started", "what can build_ do", "what can build faster do", "what can you do"))
_WELCOME = frozenset(("", "hi", "hello", "hey", "get started", "welcome", "press enter to start", "press enter to begin"))
_REMINDER = "After testing, please send back LogReport.zip."


def guidance(message: str, *, already_welcomed: bool = False,
             selected: bool = True) -> dict:
    """Recognize only narrow, full-message aliases, never authorize a build.

    This is a deterministic local preview, not a replacement for contextual intent
    handling by the host. Unsupported/mixed wording is returned to normal conversation.
    The current-conversation welcomed flag is provided by the caller, never persisted.
    """
    if not isinstance(message, str) or len(message) > 16000:
        raise ValueError("Expected a message of at most 16000 characters.")
    if type(already_welcomed) is not bool or type(selected) is not bool:
        raise ValueError("Context flags must be booleans.")
    result = {"handled": False, "route": "conversation", "text": None,
              "build_authorized": False, "state_changed": False,
              "native_composer_control": False}
    if not selected:
        return result
    text = message.strip()
    # Some hosts represent their selected chip as its full label in model input.
    # The text aliases here do NOT register native @mentions with the host.
    # Only strip this exact leading label at a boundary; quoted text is not a chip.
    for label in (COMPOSER_LABEL, *TEXT_ALIASES, "@Build Faster", "@Build_", "@BuildFaster"):
        # A literal @ here is textual input; not a registered native mention alias.
        prefix = text[:len(label)]
        tail = text[len(label):]
        if prefix.casefold() == label.casefold() and (not tail or tail[0].isspace()):
            text = tail.strip()
            break
    key = " ".join(text.casefold().split()).rstrip("?!").strip()
    if key in _HELP:
        route, filename = "help", "HP12.md"
    elif key in _WELCOME:
        if already_welcomed:
            return {**result, "handled": True, "route": "ask",
                    "text": "What would you like to build or change?"}
        route, filename = "welcome", "WC23.md"
    else:
        return result
    # Fixed bundled filenames only; the user's text is never a path or executable.
    reply = (AUTO / filename).read_text(encoding="utf-8").strip()
    if not reply or (filename == "HP12.md" and "LogReport.zip" not in reply) or (filename == "WC23.md" and "What would you like to make?" not in reply):
        raise ValueError("The bundled guidance copy is incomplete.")
    return {**result, "handled": True, "route": route, "text": reply}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--message", help="Preview one user message; /help shows guidance.")
    group.add_argument("--welcome", action="store_true", help="Preview the first-use introduction.")
    parser.add_argument("--already-welcomed", action="store_true")
    parser.add_argument("--json", action="store_true", help="Include routing metadata.")
    args = parser.parse_args()
    try:
        result = guidance("" if args.welcome else args.message,
                          already_welcomed=args.already_welcomed)
        if args.json or not result["handled"]:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(result["text"])
        return 0
    except (ValueError, OSError, UnicodeError):
        print("The local guidance preview could not be loaded. No project was changed.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.dont_write_bytecode = True
    raise SystemExit(main())
