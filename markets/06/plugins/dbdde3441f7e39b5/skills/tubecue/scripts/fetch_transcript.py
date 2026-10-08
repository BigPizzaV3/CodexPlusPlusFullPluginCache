#!/usr/bin/env python3

"""Fetch a complete timestamped YouTube transcript with stable status codes."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse


VENDORED_LIBRARY_VERSION = "1.2.4"
VIDEO_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")
VENDOR_DIR = Path(__file__).resolve().with_name("vendor")
sys.path.insert(0, str(VENDOR_DIR))


def extract_video_id(value: str) -> str:
    value = value.strip()
    if VIDEO_ID_RE.fullmatch(value):
        return value

    parsed = urlparse(value)
    host = parsed.netloc.lower().split(":", 1)[0]
    if host.startswith("www."):
        host = host[4:]

    video_id = ""
    if host == "youtu.be":
        video_id = parsed.path.strip("/").split("/", 1)[0]
    elif host in {"youtube.com", "m.youtube.com", "music.youtube.com"}:
        if parsed.path.rstrip("/") == "/watch":
            video_id = parse_qs(parsed.query).get("v", [""])[0]
        else:
            match = re.match(
                r"^/(?:shorts|live|embed)/([A-Za-z0-9_-]{11})(?:/|$)",
                parsed.path,
            )
            video_id = match.group(1) if match else ""

    if not VIDEO_ID_RE.fullmatch(video_id):
        raise ValueError("Unsupported or invalid YouTube URL")
    return video_id


def format_timestamp(seconds: float) -> str:
    milliseconds = max(0, round(float(seconds) * 1000))
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    secs, millis = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}.{millis:03d}"


def language_matches(code: str, preferred: str) -> bool:
    code = code.lower()
    preferred = preferred.lower()
    return code == preferred or code.split("-", 1)[0] == preferred.split("-", 1)[0]


def select_transcript(available: list, preferred_languages: list[str]):
    manual = [track for track in available if not track.is_generated]
    generated = [track for track in available if track.is_generated]

    for preferred in preferred_languages:
        for group in (manual, generated):
            match = next(
                (track for track in group if language_matches(track.language_code, preferred)),
                None,
            )
            if match is not None:
                return match

    if manual:
        return manual[0]
    if generated:
        return generated[0]
    return None


def print_error(label: str, message: str, exit_code: int) -> int:
    print(f"{label}: {message}", file=sys.stderr)
    return exit_code


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("video", help="YouTube URL or 11-character video ID")
    parser.add_argument(
        "--languages",
        nargs="+",
        default=["en"],
        metavar="CODE",
        help="preferred language codes in priority order (default: en)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        video_id = extract_video_id(args.video)
    except ValueError as exc:
        return print_error("INVALID_URL", str(exc), 2)

    try:
        from youtube_transcript_api import (
            AgeRestricted,
            IpBlocked,
            RequestBlocked,
            TranscriptsDisabled,
            VideoUnavailable,
            VideoUnplayable,
            YouTubeTranscriptApi,
        )
    except (ImportError, ModuleNotFoundError) as exc:
        return print_error("DEPENDENCY_MISSING", exc.name or str(exc), 7)

    try:
        available = list(YouTubeTranscriptApi().list(video_id))
        selected = select_transcript(available, args.languages)
        if selected is None:
            return print_error("NO_CAPTIONS", "No caption track is available.", 3)
        fetched = selected.fetch()
    except TranscriptsDisabled:
        return print_error("NO_CAPTIONS", "Captions are disabled for this video.", 3)
    except (RequestBlocked, IpBlocked):
        return print_error(
            "BLOCKED",
            "YouTube blocked direct transcript retrieval; use the Tactiq fallback.",
            4,
        )
    except (AgeRestricted, VideoUnavailable, VideoUnplayable):
        return print_error("VIDEO_UNAVAILABLE", "The video is unavailable or restricted.", 5)
    except Exception as exc:
        return print_error("DIRECT_RETRIEVAL_FAILED", str(exc).splitlines()[0], 6)

    snippets = [snippet for snippet in fetched if " ".join(snippet.text.split())]
    if not snippets:
        return print_error("NO_CAPTIONS", "The selected caption track is empty.", 3)

    last_end = max(snippet.start + snippet.duration for snippet in snippets)
    print(f"VIDEO_ID: {video_id}")
    print(f"URL: https://www.youtube.com/watch?v={video_id}")
    print(f"BACKEND: youtube-transcript-api {VENDORED_LIBRARY_VERSION}")
    display_language = re.sub(
        r"\s+\(auto-generated\)\s*$", "", selected.language, flags=re.IGNORECASE
    )
    print(f"LANGUAGE: {display_language} ({selected.language_code})")
    print("CAPTION_TYPE: " + ("auto-generated" if selected.is_generated else "manual"))
    print(f"CUE_COUNT: {len(snippets)}")
    print(f"LAST_TIMESTAMP: {format_timestamp(last_end)}")
    print("--- TRANSCRIPT ---")
    for snippet in snippets:
        text = " ".join(snippet.text.split())
        print(f"[{format_timestamp(snippet.start)}] {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
