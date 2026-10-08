#!/usr/bin/env python3
"""Deterministic helpers for Meetings post-meeting note delivery.

This module intentionally has no connector dependencies. Skills can use it to
make the parts of delivery that must be identical across agents testable:

* strict extraction of a Meetings meeting id from a user-visible URL;
* narrow Calendar candidate windows and strict event association;
* strict normalization of caller-supplied Google Doc links; and
* internal-only share-recipient scope; and
* shared idempotency markers, association guards, and provenance footers.

Connector reads and writes remain in the calling workflow. In particular,
these helpers do not search Drive, mutate Calendar, or edit a document.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
from typing import Any, Iterable, Mapping, Sequence
from urllib.parse import parse_qs, unquote, urlsplit
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

_ALLOWED_HOSTS = frozenset({"chatgpt.com", "www.chatgpt.com"})
_MEETING_ID_VALUE_PATTERN = r"[A-Za-z][A-Za-z0-9-]*_[A-Za-z0-9][A-Za-z0-9_-]*"
_MEETING_ID_RE = re.compile(rf"^{_MEETING_ID_VALUE_PATTERN}$")
_HTTPS_URL_TOKEN_RE = re.compile(r"(?:^|[\s(<\[{\"'])(?P<url>https://[^\s<>\]\[(){}\"']*)")
_TRAILING_URL_PUNCTUATION = ".,;:!?)]}'\""
_GOOGLE_DOC_ID_RE = re.compile(r"^[A-Za-z0-9_-]+$")
_GOOGLE_DOC_PATH_RE = re.compile(r"^/document/(?:u/[0-9]+/)?d/([A-Za-z0-9_-]+)(?:/|$)")
_CALENDAR_SELECTOR_STATUSES = frozenset(
    {
        "selected",
        "needs_user_selection",
        "no_suitable_invite",
        "invalid_input",
        "failed",
    }
)
_NON_MEETING_EVENT_TYPES = frozenset({"workinglocation", "outofoffice", "focustime"})
_MAX_SEMANTIC_CALENDAR_CANDIDATES = 5
_MAX_USER_SELECTION_CANDIDATES = 3
_MAX_INVITE_TITLE_BYTES = 2 * 1024
_MAX_INVITE_DESCRIPTION_BYTES = 16 * 1024
_MAX_GENERATED_SUMMARY_BYTES = 64 * 1024
_MAX_DIRECT_DOCS_PER_INVITE = 5
_MAX_DIRECT_DOCS_TOTAL = 10
_RECIPIENT_EMAIL_RE = re.compile(r"^[^@\s,<>]+@[^@\s,<>]+$")
# Keep this standalone plugin projection aligned with
# record_shared.meeting_controls.internal_domains.
_INTERNAL_EMAIL_SUFFIXES = (
    "@openai.com",
    "@c-openai.com",
    "@dogfoodit.com",
    "@oaibots.com",
    "@oaimeetings.com",
)
_MAX_CALENDAR_ATTENDEES = 500
_CALENDAR_SELECTION_EVIDENCE = frozenset(
    {
        "summary_topic_alignment",
        "meeting_identity_alignment",
        "timing_alignment",
        "invite_context_alignment",
        "direct_doc_topic_alignment",
    }
)
_SUBSTANTIVE_CALENDAR_SELECTION_EVIDENCE = frozenset(
    {
        "summary_topic_alignment",
        "meeting_identity_alignment",
        "direct_doc_topic_alignment",
    }
)
_CHECKPOINT_V3_FIELDS = frozenset(
    {
        "schema_version",
        "last_checked_at",
        "processed_meeting_ids",
        "pending_meetings",
        "needs_review",
        "last_error_fingerprint",
    }
)
_CHECKPOINT_V4_FIELDS = _CHECKPOINT_V3_FIELDS | {"pending_user_actions"}


class InvalidMeetingsUrl(ValueError):
    """Raised when a URL cannot establish one unambiguous Meetings identity."""


class UntrustworthyRecordingTiming(ValueError):
    """Raised when semantic fallback has no trustworthy recording time window."""


@dataclass(frozen=True)
class ParsedMeetingsUrl:
    meetings_url: str
    meeting_id: str


def _parse_recording_timestamp(value: str, *, field_name: str) -> datetime:
    """Parse one recording timestamp without silently inventing a time."""

    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty ISO timestamp")
    timestamp = value.strip()
    if "T" not in timestamp and " " not in timestamp:
        raise ValueError(f"{field_name} must include a time")
    normalized = f"{timestamp[:-1]}+00:00" if timestamp.endswith("Z") else timestamp
    try:
        return datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ValueError(f"{field_name} must be a valid ISO timestamp") from exc


def _parse_timezone_aware_timestamp(value: str, *, field_name: str) -> datetime:
    parsed = _parse_recording_timestamp(value, field_name=field_name)
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError(f"{field_name} must include a UTC offset")
    return parsed


def calendar_candidate_windows(
    recording_start_time: str,
    recording_end_time: str | None = None,
) -> list[dict[str, str]]:
    """Build the two narrow, separate Calendar-enumeration windows.

    The caller should enumerate each returned window without a free-text query,
    then deduplicate exact event IDs before fetching full event details.
    """

    # Keep the pre-existing exact-association helper permissive. The semantic
    # fallback validates offset-bearing recording times separately before it
    # calls this shared window builder.
    start = _parse_recording_timestamp(recording_start_time, field_name="recording_start_time")
    windows = [
        {
            "anchor": "recording_start_time",
            "time_min": (start - timedelta(minutes=30)).isoformat(),
            "time_max": (start + timedelta(minutes=30)).isoformat(),
        }
    ]
    if recording_end_time is not None and (
        not isinstance(recording_end_time, str) or recording_end_time.strip()
    ):
        end = _parse_recording_timestamp(recording_end_time, field_name="recording_end_time")
        windows.append(
            {
                "anchor": "recording_end_time",
                "time_min": (end - timedelta(minutes=30)).isoformat(),
                "time_max": (end + timedelta(minutes=60)).isoformat(),
            }
        )
    return windows


def _decode_bounded(value: str, *, max_rounds: int = 2) -> str:
    """Decode only a nested route, and never recurse without a small bound."""

    decoded = value
    for _ in range(max_rounds):
        next_value = unquote(decoded)
        if next_value == decoded:
            break
        decoded = next_value
    return decoded


def _path_meeting_ids(path: str) -> set[str]:
    """Extract exact meeting-id path segments from supported Meetings routes."""

    # URL paths can contain one level of harmless encoding. We never scan a
    # query string here; only path-shaped input reaches this function.
    decoded_path = _decode_bounded(path, max_rounds=2)
    route = decoded_path.split("?", 1)[0].split("#", 1)[0]
    segments = [segment for segment in route.split("/") if segment]
    if len(segments) == 1 and _MEETING_ID_RE.fullmatch(segments[0]):
        return {segments[0]}
    if segments and segments[0] == "meetings":
        return {segment for segment in segments[1:] if _MEETING_ID_RE.fullmatch(segment)}
    return set()


def _next_route_meeting_ids(route: str) -> set[str]:
    """Extract identity only from the supported nested Meetings route."""

    decoded_route = _decode_bounded(route, max_rounds=2)
    route_path = decoded_route.split("?", 1)[0].split("#", 1)[0]
    segments = [segment for segment in route_path.split("/") if segment]
    if not segments or segments[0] != "meetings":
        return set()
    return {segment for segment in segments[1:] if _MEETING_ID_RE.fullmatch(segment)}


def parse_meetings_url(meetings_url: str) -> ParsedMeetingsUrl:
    """Parse one current Meetings URL form into its stable meeting identity.

    Identity is accepted only from supported path routes or from a next route.
    Other query parameters are deliberately ignored, even when they contain a
    meeting-looking string.
    """

    if not isinstance(meetings_url, str) or not meetings_url.strip():
        raise InvalidMeetingsUrl("meetings_url must be a non-empty string")

    original_url = meetings_url.strip()
    try:
        parsed = urlsplit(original_url)
    except ValueError as exc:
        raise InvalidMeetingsUrl("malformed Meetings URL") from exc

    if parsed.scheme != "https" or parsed.hostname not in _ALLOWED_HOSTS:
        raise InvalidMeetingsUrl("Meetings URL must use https://chatgpt.com")
    try:
        parsed_port = parsed.port
    except ValueError as exc:
        raise InvalidMeetingsUrl("Meetings URL authority is malformed") from exc
    if parsed.username or parsed.password or parsed_port is not None:
        raise InvalidMeetingsUrl("Meetings URL authority is malformed")

    candidates = _path_meeting_ids(parsed.path)

    # parse_qs preserves repeated next parameters so distinct nested identities
    # are detected as ambiguity instead of silently picking one.
    try:
        query = parse_qs(parsed.query, keep_blank_values=True, strict_parsing=False)
    except ValueError as exc:
        raise InvalidMeetingsUrl("malformed Meetings URL query") from exc
    for next_route in query.get("next", []):
        candidates.update(_next_route_meeting_ids(next_route))

    if len(candidates) != 1:
        if not candidates:
            raise InvalidMeetingsUrl("meeting identity could not be established")
        raise InvalidMeetingsUrl("Meetings URL contains ambiguous meeting identities")

    return ParsedMeetingsUrl(meetings_url=original_url, meeting_id=next(iter(candidates)))


def _strip_url_punctuation(token: str) -> str:
    return token.rstrip(_TRAILING_URL_PUNCTUATION)


def _calendar_event_id(candidate: Mapping[str, Any]) -> str:
    for field_name in ("calendar_event_id", "event_id", "id"):
        value = candidate.get(field_name)
        if value is not None and str(value).strip():
            return str(value).strip()
    return ""


def _calendar_hangout_link(candidate: Mapping[str, Any]) -> str:
    for field_name in ("hangout_link", "hangoutLink"):
        value = candidate.get(field_name)
        if value is not None:
            return str(value).strip()
    return ""


def _contains_exact_https_url_token(text: Any, expected_url: str) -> bool:
    """Match one exact URL token, never a loose substring."""

    if not isinstance(text, str) or not text:
        return False
    expected = expected_url.strip()
    if not expected:
        return False
    return any(
        _strip_url_punctuation(match.group("url")) == expected
        for match in _HTTPS_URL_TOKEN_RE.finditer(text)
    )


def _contains_exact_meeting_id_token(text: str, meeting_id: str) -> bool:
    """Match one canonical meeting ID without requiring any surrounding URL form."""

    if not isinstance(meeting_id, str) or not _MEETING_ID_RE.fullmatch(meeting_id):
        raise ValueError("meeting_id must be a canonical Meetings meeting id")
    if not text:
        return False

    normalized_text = text
    for _ in range(8):
        decoded_text = unquote(normalized_text)
        if decoded_text == normalized_text:
            break
        normalized_text = decoded_text
    else:
        if unquote(normalized_text) != normalized_text:
            raise ValueError("excessively_encoded_calendar_event_description")

    meeting_id_pattern = re.compile(rf"(?<![A-Za-z0-9_-]){re.escape(meeting_id)}(?![A-Za-z0-9_-])")
    return meeting_id_pattern.search(normalized_text) is not None


def calendar_description_has_meeting_id(description: Any, meeting_id: str) -> bool:
    """Match the canonical meeting ID in a Calendar description."""

    if not isinstance(meeting_id, str) or not _MEETING_ID_RE.fullmatch(meeting_id):
        raise ValueError("meeting_id must be a canonical Meetings meeting id")
    if description is None:
        return False
    if not isinstance(description, str):
        raise ValueError("Calendar description must be a string or null")
    return _contains_exact_meeting_id_token(description, meeting_id)


def calendar_description_has_canonical_meetings_url(description: Any, meetings_url: str) -> bool:
    """Compatibility wrapper that derives the ID from a Meetings URL."""

    parsed = parse_meetings_url(meetings_url)
    if description is None:
        return False
    if not isinstance(description, str):
        raise ValueError("Calendar description must be a string or null")
    return calendar_description_has_meeting_id(description, parsed.meeting_id)


def dedupe_calendar_event_candidates(
    candidates: Iterable[Mapping[str, Any]],
) -> list[Mapping[str, Any]]:
    """Deduplicate fetched Calendar candidates by exact occurrence ID."""

    deduped: list[Mapping[str, Any]] = []
    seen_ids: set[str] = set()
    for candidate in candidates:
        event_id = _calendar_event_id(candidate)
        if not event_id or event_id in seen_ids:
            continue
        seen_ids.add(event_id)
        deduped.append(candidate)
    return deduped


def _explicit_event_type(candidate: Mapping[str, Any]) -> str:
    for field_name in ("event_type", "eventType"):
        value = candidate.get(field_name)
        if isinstance(value, str) and value.strip():
            return value.strip().replace("_", "").lower()
    return ""


def _is_explicitly_all_day(candidate: Mapping[str, Any]) -> bool:
    """Return true only when the public payload explicitly proves all-day."""

    for field_name in ("all_day", "allDay"):
        if candidate.get(field_name) is True:
            return True
    start = candidate.get("start")
    end = candidate.get("end")
    # Public google_calendar.fetch currently projects date-only event times to
    # explicit empty strings. Treat only the complete pair as its all-day
    # sentinel; a lone empty or malformed time remains invalid input.
    if start == "" and end == "" and "start" in candidate and "end" in candidate:
        return True
    # google_calendar.read_event preserves a date-only event as local midnight
    # strings without offsets. Timed events carry offsets. Require a positive
    # whole-day span so arbitrary naïve times do not become all-day evidence.
    if isinstance(start, str) and isinstance(end, str) and start and end:
        try:
            parsed_start = _parse_recording_timestamp(start, field_name="calendar_event_start")
            parsed_end = _parse_recording_timestamp(end, field_name="calendar_event_end")
        except ValueError:
            pass
        else:
            if (
                parsed_start.tzinfo is None
                and parsed_end.tzinfo is None
                and parsed_start.time() == datetime.min.time()
                and parsed_end.time() == datetime.min.time()
            ):
                delta = parsed_end - parsed_start
                if delta.days >= 1 and delta.seconds == 0:
                    return True
    if not isinstance(start, Mapping):
        return False
    has_date = isinstance(start.get("date"), str) and bool(start["date"].strip())
    has_datetime = any(
        isinstance(start.get(field_name), str) and bool(start[field_name].strip())
        for field_name in ("dateTime", "date_time")
    )
    return has_date and not has_datetime


def _authenticated_user_explicitly_declined(candidate: Mapping[str, Any]) -> bool:
    """Use only explicit public response state; never infer the authenticated user."""

    for field_name in (
        "my_response_status",
        "myResponseStatus",
        "response_status",
        "responseStatus",
    ):
        value = candidate.get(field_name)
        if isinstance(value, str) and value.strip().lower() == "declined":
            return True
    attendees = candidate.get("attendees")
    if not isinstance(attendees, list):
        return False
    for attendee in attendees:
        if not isinstance(attendee, Mapping) or not (
            attendee.get("self") is True or attendee.get("is_self") is True
        ):
            continue
        for field_name in ("response_status", "responseStatus"):
            value = attendee.get(field_name)
            if isinstance(value, str) and value.strip().lower() == "declined":
                return True
    return False


def _first_nonempty_string(candidate: Mapping[str, Any], field_names: Sequence[str]) -> str:
    for field_name in field_names:
        if field_name not in candidate:
            continue
        value = candidate[field_name]
        if value is not None and not isinstance(value, str):
            raise ValueError(f"invalid_calendar_event_{field_name}")
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def _project_event_time(value: Any) -> str | dict[str, str] | None:
    """Canonicalize one explicit Calendar time or reject malformed evidence."""

    if value is None:
        return None
    if isinstance(value, str):
        if not value.strip() or value != value.strip():
            raise ValueError("invalid_calendar_event_time")
        _parse_timezone_aware_timestamp(value, field_name="calendar_event_time")
        return value
    if not isinstance(value, Mapping):
        raise ValueError("invalid_calendar_event_time")

    for field_name in (
        "date",
        "dateTime",
        "date_time",
        "timeZone",
        "time_zone",
        "timezone",
    ):
        raw_value = value.get(field_name)
        if raw_value is not None and not isinstance(raw_value, str):
            raise ValueError("invalid_calendar_event_time")

    date_values = {
        raw.strip()
        for field_name in ("date",)
        if isinstance((raw := value.get(field_name)), str) and raw.strip()
    }
    datetime_values = {
        raw.strip()
        for field_name in ("dateTime", "date_time")
        if isinstance((raw := value.get(field_name)), str) and raw.strip()
    }
    timezone_values = {
        raw.strip()
        for field_name in ("timeZone", "time_zone", "timezone")
        if isinstance((raw := value.get(field_name)), str) and raw.strip()
    }
    if len(date_values) > 1 or len(datetime_values) > 1 or len(timezone_values) > 1:
        raise ValueError("conflicting_calendar_event_time")
    if date_values and datetime_values:
        raise ValueError("conflicting_calendar_event_time")
    if date_values:
        # Date-only events should already have been removed by the all-day filter.
        raise ValueError("invalid_calendar_event_time")
    if not datetime_values:
        if value:
            raise ValueError("invalid_calendar_event_time")
        return None
    date_time = next(iter(datetime_values))
    parsed_date_time = _parse_recording_timestamp(date_time, field_name="calendar_event_time")
    if (
        parsed_date_time.tzinfo is None or parsed_date_time.utcoffset() is None
    ) and not timezone_values:
        raise ValueError("calendar_event_time must include a UTC offset or time zone")
    projected = {"date_time": date_time}
    if timezone_values:
        time_zone = next(iter(timezone_values))
        try:
            ZoneInfo(time_zone)
        except (ZoneInfoNotFoundError, ValueError) as exc:
            raise ValueError("invalid_calendar_event_time_zone") from exc
        projected["time_zone"] = time_zone
    return projected


def _projected_event_datetime(value: str | Mapping[str, str] | None) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, str):
        return _parse_timezone_aware_timestamp(value, field_name="calendar_event_time")
    parsed = _parse_recording_timestamp(value["date_time"], field_name="calendar_event_time")
    if parsed.tzinfo is not None and parsed.utcoffset() is not None:
        return parsed
    try:
        return parsed.replace(tzinfo=ZoneInfo(value["time_zone"]))
    except (KeyError, ZoneInfoNotFoundError, ValueError) as exc:
        raise ValueError("invalid_calendar_event_time_zone") from exc


def _direct_google_doc_urls(candidate: Mapping[str, Any], description: str) -> list[str]:
    links: list[Any] = []
    if "direct_doc_urls" in candidate:
        direct_doc_urls = candidate["direct_doc_urls"]
        if direct_doc_urls is not None and not isinstance(direct_doc_urls, list):
            raise ValueError("invalid_direct_document_links")
    else:
        direct_doc_urls = None
    if isinstance(direct_doc_urls, list):
        if any(not isinstance(value, str) for value in direct_doc_urls):
            raise ValueError("invalid_direct_document_links")
        links.extend(direct_doc_urls)
    if "attachments" in candidate:
        attachments = candidate["attachments"]
        if attachments is not None and not isinstance(attachments, list):
            raise ValueError("invalid_calendar_event_attachments")
    else:
        attachments = None
    if isinstance(attachments, list):
        for attachment in attachments:
            if not isinstance(attachment, Mapping):
                raise ValueError("invalid_calendar_event_attachment")
            for field_name in ("fileUrl", "file_url", "url"):
                if field_name in attachment:
                    link = attachment[field_name]
                    if link is not None and not isinstance(link, str):
                        raise ValueError("invalid_calendar_event_attachment")
                    if isinstance(link, str):
                        links.append(link)
    links.extend(
        _strip_url_punctuation(token) for token in _HTTPS_URL_TOKEN_RE.findall(description)
    )
    normalized = normalize_google_doc_links(links)
    return [item["url"] for item in normalized["candidates"]]


def _project_semantic_calendar_candidate(
    candidate: Mapping[str, Any], *, event_id: str
) -> dict[str, Any]:
    """Project one fetched occurrence to the selector's least-data contract."""

    description = _first_nonempty_string(candidate, ("description", "notes"))
    title = _first_nonempty_string(candidate, ("title", "summary"))
    if len(title.encode("utf-8")) > _MAX_INVITE_TITLE_BYTES:
        raise ValueError("oversized_calendar_event_title")
    if len(description.encode("utf-8")) > _MAX_INVITE_DESCRIPTION_BYTES:
        raise ValueError("oversized_calendar_event_description")
    direct_doc_urls = _direct_google_doc_urls(candidate, description)
    if len(direct_doc_urls) > _MAX_DIRECT_DOCS_PER_INVITE:
        raise ValueError("too_many_direct_document_links")
    start = _project_event_time(candidate.get("start"))
    end = _project_event_time(candidate.get("end"))
    start_datetime = _projected_event_datetime(start)
    end_datetime = _projected_event_datetime(end)
    if start_datetime is not None and end_datetime is not None and end_datetime < start_datetime:
        raise ValueError("inverted_calendar_event_time")
    return {
        "event_id": event_id,
        "title": title,
        "description": description,
        "start": start,
        "end": end,
        "direct_doc_urls": direct_doc_urls,
    }


def prepare_semantic_meeting_context(meeting: Mapping[str, Any]) -> dict[str, str]:
    """Validate and project the only Meetings fields allowed into selection."""

    if not isinstance(meeting, Mapping):
        raise ValueError("meeting must be an object")
    required = {"meeting_id", "generated_summary"}
    allowed = required | {"recording_start", "recording_end"}
    if not required.issubset(meeting) or not set(meeting).issubset(allowed):
        raise ValueError("meeting must use the exact semantic input shape")

    meeting_id_value = meeting.get("meeting_id")
    meeting_id = meeting_id_value.strip() if isinstance(meeting_id_value, str) else ""
    if meeting_id_value != meeting_id or not _MEETING_ID_RE.fullmatch(meeting_id):
        raise ValueError("meeting has an invalid meeting_id")

    summary_value = meeting.get("generated_summary")
    summary = summary_value.strip() if isinstance(summary_value, str) else ""
    if not summary:
        raise ValueError("generated_summary must be a non-empty string")
    if len(summary.encode("utf-8")) > _MAX_GENERATED_SUMMARY_BYTES:
        raise ValueError("generated_summary exceeds 64 KiB")

    recording_start = meeting.get("recording_start")
    try:
        start = _parse_timezone_aware_timestamp(recording_start, field_name="recording_start")
    except ValueError as exc:
        raise UntrustworthyRecordingTiming("missing_or_invalid_recording_timing") from exc
    result = {
        "meeting_id": meeting_id,
        "recording_start": recording_start,
    }

    recording_end = meeting.get("recording_end")
    if recording_end is not None:
        try:
            end = _parse_timezone_aware_timestamp(recording_end, field_name="recording_end")
        except ValueError as exc:
            raise UntrustworthyRecordingTiming("missing_or_invalid_recording_timing") from exc
        if end < start:
            raise UntrustworthyRecordingTiming("missing_or_invalid_recording_timing")
        result["recording_end"] = recording_end

    result["generated_summary"] = summary
    return result


def prepare_semantic_association_scope(
    meeting: Mapping[str, Any], candidate: Mapping[str, Any]
) -> dict[str, Any]:
    """Build the exact canonical JSON scope used by confirmation hashes."""

    prepared_meeting = prepare_semantic_meeting_context(meeting)
    prepared_candidates = prepare_semantic_calendar_candidates(
        [candidate], meeting_id=prepared_meeting["meeting_id"]
    )
    if prepared_candidates["status"] != "ready" or prepared_candidates["candidate_count"] != 1:
        raise ValueError("candidate cannot form a safe semantic association scope")
    return {
        "meeting": prepared_meeting,
        "candidate_invite": prepared_candidates["candidates"][0],
    }


def _explicit_event_state_fingerprint(candidate: Mapping[str, Any]) -> dict[str, Any]:
    raw_status = candidate.get("status")
    if raw_status is not None and not isinstance(raw_status, str):
        raise ValueError("invalid_calendar_event_state")
    for field_name in ("event_type", "eventType"):
        value = candidate.get(field_name)
        if value is not None and not isinstance(value, str):
            raise ValueError("invalid_calendar_event_type")
    for field_name in ("all_day", "allDay"):
        value = candidate.get(field_name)
        if value is not None and type(value) is not bool:
            raise ValueError("invalid_calendar_all_day_state")
    for field_name in (
        "my_response_status",
        "myResponseStatus",
        "response_status",
        "responseStatus",
    ):
        value = candidate.get(field_name)
        if value is not None and not isinstance(value, str):
            raise ValueError("invalid_calendar_response_status")
    attendees = candidate.get("attendees")
    if attendees is not None and not isinstance(attendees, list):
        raise ValueError("invalid_calendar_attendees")
    if isinstance(attendees, list):
        for attendee in attendees:
            if not isinstance(attendee, Mapping):
                raise ValueError("invalid_calendar_attendee")
            for field_name in ("self", "is_self"):
                value = attendee.get(field_name)
                if value is not None and type(value) is not bool:
                    raise ValueError("invalid_calendar_attendee_self_state")
            for field_name in ("response_status", "responseStatus"):
                value = attendee.get(field_name)
                if value is not None and not isinstance(value, str):
                    raise ValueError("invalid_calendar_attendee_response_status")
    return {
        "status": raw_status.strip().lower() if isinstance(raw_status, str) else None,
        "event_type": _explicit_event_type(candidate) or None,
        "all_day": _is_explicitly_all_day(candidate),
        "declined": _authenticated_user_explicitly_declined(candidate),
    }


def _calendar_description_for_association_guard(candidate: Mapping[str, Any]) -> str:
    """Validate the exact Calendar description field used by the early guard."""

    descriptions: list[str] = []
    for field_name in ("description", "notes"):
        if field_name not in candidate:
            continue
        value = candidate[field_name]
        if value is None:
            descriptions.append("")
        elif isinstance(value, str):
            descriptions.append(value)
        else:
            raise ValueError("invalid_calendar_event_description")
    if len(set(descriptions)) > 1:
        raise ValueError("conflicting_calendar_event_description")
    description = descriptions[0] if descriptions else ""
    if len(description.encode("utf-8")) > _MAX_INVITE_DESCRIPTION_BYTES:
        raise ValueError("oversized_calendar_event_description")
    return description


def prepare_semantic_calendar_candidates(
    candidates: Iterable[Mapping[str, Any]],
    *,
    meeting_id: str,
) -> dict[str, Any]:
    """Apply deterministic hard filters before semantic invite selection.

    Before filtering, this helper checks every structurally safe exact event
    description for the canonical meeting ID without requiring a particular
    URL form. It deliberately does not rank or score events. Missing public
    fields are treated as unknown, not as evidence for exclusion or for a
    Calendar source. The caller owns the narrow time-window recall and full
    exact-event fetches.
    """

    if isinstance(candidates, (str, bytes, Mapping)) or not isinstance(candidates, Iterable):
        raise ValueError("candidates must be an array")
    if not isinstance(meeting_id, str) or not _MEETING_ID_RE.fullmatch(meeting_id):
        raise ValueError("meeting_id must be a canonical Meetings meeting id")

    kept: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    unsafe_input = False
    grouped: dict[str, list[tuple[int, Mapping[str, Any]]]] = {}
    descriptions_by_index: dict[int, str] = {}
    for index, candidate in enumerate(candidates):
        if not isinstance(candidate, Mapping):
            rejected.append({"index": index, "reason": "invalid_candidate"})
            unsafe_input = True
            continue
        event_ids: set[str] = set()
        invalid_event_id = False
        for field_name in ("calendar_event_id", "event_id", "id"):
            value = candidate.get(field_name)
            if value is None or (isinstance(value, str) and not value.strip()):
                continue
            if not isinstance(value, str) or value != value.strip():
                invalid_event_id = True
                break
            event_ids.add(value.strip())
        if invalid_event_id:
            rejected.append({"index": index, "reason": "invalid_calendar_event_id"})
            unsafe_input = True
            continue
        if len(event_ids) > 1:
            rejected.append({"index": index, "reason": "conflicting_calendar_event_id"})
            unsafe_input = True
            continue
        event_id = next(iter(event_ids), "")
        if not event_id:
            rejected.append({"index": index, "reason": "missing_calendar_event_id"})
            unsafe_input = True
            continue
        try:
            descriptions_by_index[index] = _calendar_description_for_association_guard(candidate)
        except ValueError as exc:
            rejected.append({"index": index, "reason": str(exc)})
            unsafe_input = True
            continue
        grouped.setdefault(event_id, []).append((index, candidate))

    if unsafe_input:
        rejected.sort(key=lambda item: item["index"])
        return {
            "status": "invalid_input",
            "candidates": [],
            "candidate_count": 0,
            "rejected": rejected,
        }

    already_associated = False
    for _event_id, entries in sorted(grouped.items()):
        try:
            association_bits = {
                calendar_description_has_meeting_id(descriptions_by_index[index], meeting_id)
                for index, _ in entries
            }
        except ValueError as exc:
            rejected.extend({"index": index, "reason": str(exc)} for index, _ in entries)
            unsafe_input = True
            continue
        if len(association_bits) != 1:
            rejected.extend(
                {
                    "index": index,
                    "reason": "conflicting_duplicate_calendar_event_association",
                }
                for index, _ in entries
            )
            unsafe_input = True
            continue
        if True in association_bits:
            already_associated = True

    if unsafe_input:
        rejected.sort(key=lambda item: item["index"])
        return {
            "status": "invalid_input",
            "candidates": [],
            "candidate_count": 0,
            "rejected": rejected,
        }
    if already_associated:
        return {
            "status": "already_associated",
            "candidates": [],
            "candidate_count": 0,
            "rejected": [],
        }

    for event_id, entries in sorted(grouped.items()):
        try:
            state_fingerprints = {
                json.dumps(
                    _explicit_event_state_fingerprint(candidate),
                    sort_keys=True,
                    separators=(",", ":"),
                )
                for _, candidate in entries
            }
        except ValueError as exc:
            rejected.extend({"index": index, "reason": str(exc)} for index, _ in entries)
            unsafe_input = True
            continue
        if len(state_fingerprints) != 1:
            rejected.extend(
                {
                    "index": index,
                    "reason": "conflicting_duplicate_calendar_event_state",
                }
                for index, _ in entries
            )
            unsafe_input = True
            continue

        ineligible: list[tuple[int, str]] = []
        for index, candidate in entries:
            status = candidate.get("status")
            if isinstance(status, str) and status.strip().lower() == "cancelled":
                ineligible.append((index, "cancelled"))
            elif _explicit_event_type(candidate) in _NON_MEETING_EVENT_TYPES:
                ineligible.append((index, "non_meeting_event_type"))
            elif _is_explicitly_all_day(candidate):
                ineligible.append((index, "all_day"))
            elif _authenticated_user_explicitly_declined(candidate):
                ineligible.append((index, "authenticated_user_declined"))
        if ineligible:
            if len(entries) > 1 and len(ineligible) != len(entries):
                rejected.extend(
                    {
                        "index": index,
                        "reason": "conflicting_duplicate_calendar_event_state",
                    }
                    for index, _ in entries
                )
                unsafe_input = True
            else:
                rejected.extend({"index": index, "reason": reason} for index, reason in ineligible)
            continue

        try:
            projected = [
                (index, _project_semantic_calendar_candidate(candidate, event_id=event_id))
                for index, candidate in entries
            ]
        except ValueError as exc:
            rejected.extend({"index": index, "reason": str(exc)} for index, _ in entries)
            unsafe_input = True
            continue
        fingerprints = {
            json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            for _, item in projected
        }
        if len(fingerprints) != 1:
            rejected.extend(
                {
                    "index": index,
                    "reason": "conflicting_duplicate_calendar_event_payload",
                }
                for index, _ in entries
            )
            unsafe_input = True
            continue
        kept.append(projected[0][1])
        rejected.extend(
            {"index": index, "reason": "duplicate_calendar_event_id"} for index, _ in projected[1:]
        )

    if sum(len(item["direct_doc_urls"]) for item in kept) > _MAX_DIRECT_DOCS_TOTAL:
        unsafe_input = True
        rejected.append({"index": -1, "reason": "too_many_total_direct_document_links"})

    rejected.sort(key=lambda item: item["index"])

    if unsafe_input:
        return {
            "status": "invalid_input",
            "candidates": [],
            "candidate_count": len(kept),
            "rejected": rejected,
        }

    if len(kept) > _MAX_SEMANTIC_CALENDAR_CANDIDATES:
        return {
            "status": "too_many_candidates",
            "candidates": [],
            "candidate_count": len(kept),
            "rejected": rejected,
        }
    return {
        "status": "ready",
        "candidates": kept,
        "candidate_count": len(kept),
        "rejected": rejected,
    }


def validate_calendar_selector_result(
    result: Mapping[str, Any],
    *,
    candidate_event_ids: Iterable[str],
) -> dict[str, Any]:
    """Validate semantic-selector scope without making a semantic judgment."""

    if not isinstance(result, Mapping):
        raise ValueError("selector result must be an object")
    if isinstance(candidate_event_ids, (str, bytes, Mapping)) or not isinstance(
        candidate_event_ids, Iterable
    ):
        raise ValueError("candidate event IDs must be an array")
    raw_candidate_ids = list(candidate_event_ids)
    if any(
        not isinstance(value, str) or not value.strip() or value != value.strip()
        for value in raw_candidate_ids
    ):
        raise ValueError("candidate event IDs must be non-empty strings")
    normalized_candidate_ids = [value.strip() for value in raw_candidate_ids]
    allowed_ids = set(normalized_candidate_ids)
    if len(allowed_ids) != len(normalized_candidate_ids):
        raise ValueError("candidate event IDs must be unique")
    if len(allowed_ids) > _MAX_SEMANTIC_CALENDAR_CANDIDATES:
        raise ValueError("selector input must contain at most 5 candidate event IDs")
    status = result.get("status")
    if not isinstance(status, str) or status not in _CALENDAR_SELECTOR_STATUSES:
        raise ValueError("unsupported Calendar selector status")
    if set(result) != {"status", "selected_event", "candidate_options"}:
        raise ValueError("selector result must use the exact output shape")

    candidate_options = result.get("candidate_options")
    if not isinstance(candidate_options, list):
        raise ValueError("candidate_options must be an array")

    def validate_option(candidate: Any) -> str:
        if not isinstance(candidate, Mapping) or set(candidate) != {"event_id", "evidence"}:
            raise ValueError("candidate option must contain only event_id and evidence")
        event_id_value = candidate.get("event_id")
        event_id = event_id_value.strip() if isinstance(event_id_value, str) else ""
        evidence = candidate.get("evidence")
        if (
            not event_id
            or event_id_value != event_id
            or event_id not in allowed_ids
            or not isinstance(evidence, list)
            or len(evidence) < 2
            or any(not isinstance(value, str) for value in evidence)
            or len(evidence) != len(set(evidence))
            or any(value not in _CALENDAR_SELECTION_EVIDENCE for value in evidence)
            or not _SUBSTANTIVE_CALENDAR_SELECTION_EVIDENCE.intersection(evidence)
        ):
            raise ValueError("candidate option is out of scope or has invalid evidence")
        return event_id

    if status == "selected":
        selected_event = result.get("selected_event")
        if not isinstance(selected_event, str):
            raise ValueError("selected_event must be an event ID")
        event_id = selected_event.strip()
        if selected_event != event_id or not event_id or event_id not in allowed_ids:
            raise ValueError("selected Calendar event is outside the input candidate set")
        if len(candidate_options) != 1 or validate_option(candidate_options[0]) != event_id:
            raise ValueError("selected result must contain one matching candidate option")
        return {"status": status, "calendar_event_id": event_id}

    if status == "needs_user_selection":
        if result.get("selected_event") is not None or not (
            2 <= len(candidate_options) <= _MAX_USER_SELECTION_CANDIDATES
        ):
            raise ValueError("needs_user_selection requires 2..3 candidate_options")
        selected_ids: list[str] = []
        for candidate in candidate_options:
            event_id = validate_option(candidate)
            if event_id in selected_ids:
                raise ValueError("user-selection candidate is duplicate or out of scope")
            selected_ids.append(event_id)
        return {
            "status": status,
            "candidate_calendar_event_ids": sorted(selected_ids),
        }

    if result.get("selected_event") is not None or candidate_options:
        raise ValueError("terminal selector status must not contain candidates")
    return {"status": status}


def canonical_scope_sha256(value: Any) -> str:
    """Hash one JSON scope using a deterministic representation."""

    try:
        encoded = json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise ValueError("scope must be finite JSON data") from exc
    return hashlib.sha256(encoded).hexdigest()


def _normalized_internal_email(value: Any) -> str | None:
    """Mirror Record's Calendar-invitee internal-domain normalization."""

    if not isinstance(value, str):
        return None
    normalized = value.strip().casefold()
    if (
        not normalized
        or not _RECIPIENT_EMAIL_RE.fullmatch(normalized)
        or not normalized.endswith(_INTERNAL_EMAIL_SUFFIXES)
    ):
        return None
    return normalized


def canonical_recipient_set_sha256(
    recipient_emails: Iterable[Any], *, attendees_omitted: bool | None
) -> dict[str, Any]:
    """Hash one complete normalized internal-recipient set without returning addresses."""

    if attendees_omitted is True:
        raise ValueError("Calendar attendee snapshot is incomplete")
    if attendees_omitted is not None and attendees_omitted is not False:
        raise ValueError("attendees_omitted must be boolean or null")
    if isinstance(recipient_emails, (str, bytes, Mapping)) or not isinstance(
        recipient_emails, Iterable
    ):
        raise ValueError("recipient emails must be an array")
    raw_recipients = list(recipient_emails)
    if len(raw_recipients) > 500:
        raise ValueError("recipient email set is too large")
    normalized: list[str] = []
    for raw_recipient in raw_recipients:
        if not isinstance(raw_recipient, str):
            raise ValueError("recipient email must be a string")
        recipient = _normalized_internal_email(raw_recipient)
        if recipient is None:
            raise ValueError("recipient email must be a valid OpenAI-internal address")
        normalized.append(recipient)
    canonical_recipients = sorted(set(normalized))
    return {
        "sha256": canonical_scope_sha256(canonical_recipients),
        "recipient_count": len(canonical_recipients),
    }


def _calendar_attendees_omitted(calendar_event: Mapping[str, Any]) -> bool | None:
    values = [
        calendar_event[field_name]
        for field_name in ("attendees_omitted", "attendeesOmitted")
        if field_name in calendar_event
    ]
    if len(values) > 1 and values[0] != values[1]:
        raise ValueError("Calendar attendees_omitted aliases conflict")
    value = values[0] if values else None
    if value is not None and type(value) is not bool:
        raise ValueError("attendees_omitted must be boolean or null")
    return value


def prepare_internal_share_recipients(
    calendar_event: Mapping[str, Any],
) -> dict[str, Any]:
    """Project the existing internal Calendar-invitee eligibility boundary.

    This mirrors Record's Calendar invitee snapshot: normalize and deduplicate
    non-resource attendees in Record's allowed internal domains, and include an
    internal organizer even when it is absent from the attendee list. External
    attendees never enter the returned list or its hash.
    """

    if not isinstance(calendar_event, Mapping):
        raise ValueError("Calendar event must be an object")
    attendees_omitted = _calendar_attendees_omitted(calendar_event)
    if attendees_omitted is True:
        raise ValueError("Calendar attendee snapshot is incomplete")

    attendees = calendar_event.get("attendees")
    if attendees is None:
        attendee_rows: list[Any] = []
    elif not isinstance(attendees, list):
        raise ValueError("Calendar attendees must be an array or null")
    else:
        attendee_rows = attendees
    if len(attendee_rows) > _MAX_CALENDAR_ATTENDEES:
        raise ValueError("Calendar attendee set is too large")

    recipient_emails: set[str] = set()
    for attendee in attendee_rows:
        if not isinstance(attendee, Mapping):
            raise ValueError("Calendar attendee must be an object")
        resource_values = [
            attendee[field_name]
            for field_name in ("resource", "is_resource", "isResource")
            if field_name in attendee
        ]
        normalized_resource_values = [
            False if value is None else value for value in resource_values
        ]
        if any(type(value) is not bool for value in normalized_resource_values):
            raise ValueError("Calendar attendee resource state must be boolean or null")
        if any(normalized_resource_values):
            continue
        email = _normalized_internal_email(attendee.get("email"))
        if email is not None:
            recipient_emails.add(email)

    organizer = calendar_event.get("organizer")
    if organizer is not None:
        if not isinstance(organizer, Mapping):
            raise ValueError("Calendar organizer must be an object or null")
        organizer_email = _normalized_internal_email(organizer.get("email"))
        if organizer_email is not None:
            recipient_emails.add(organizer_email)

    canonical_recipients = sorted(recipient_emails)
    recipient_scope = canonical_recipient_set_sha256(
        canonical_recipients,
        attendees_omitted=attendees_omitted,
    )
    return {
        "recipient_emails": canonical_recipients,
        **recipient_scope,
    }


def _validate_meeting_id_list(value: Any, *, field_name: str, limit: int) -> list[str]:
    if not isinstance(value, list) or len(value) > limit:
        raise ValueError(f"{field_name} must be an array with at most {limit} entries")
    if any(
        not isinstance(meeting_id, str)
        or meeting_id != meeting_id.strip()
        or not _MEETING_ID_RE.fullmatch(meeting_id)
        for meeting_id in value
    ):
        raise ValueError(f"{field_name} contains an invalid meeting ID")
    if len(value) != len(set(value)):
        raise ValueError(f"{field_name} contains duplicate meeting IDs")
    return list(value)


def _validate_meeting_id_map(value: Any, *, field_name: str, limit: int) -> dict[str, Any]:
    if not isinstance(value, Mapping) or len(value) > limit:
        raise ValueError(f"{field_name} must be an object with at most {limit} entries")
    result: dict[str, Any] = {}
    for meeting_id, item in value.items():
        if (
            not isinstance(meeting_id, str)
            or meeting_id != meeting_id.strip()
            or not _MEETING_ID_RE.fullmatch(meeting_id)
            or not isinstance(item, Mapping)
        ):
            raise ValueError(f"{field_name} contains an invalid keyed entry")
        result[meeting_id] = dict(item)
    return result


def validate_pending_user_actions(value: Any) -> dict[str, dict[str, Any]]:
    """Keep the v4 compatibility field empty; user input is invocation-local."""

    if not isinstance(value, Mapping) or value:
        raise ValueError("pending_user_actions must be an empty object")
    return {}


def _validate_checkpoint_common(
    checkpoint: Mapping[str, Any], *, schema_version: int
) -> dict[str, Any]:
    expected_fields = _CHECKPOINT_V4_FIELDS if schema_version == 4 else _CHECKPOINT_V3_FIELDS
    if (
        set(checkpoint) != expected_fields
        or type(checkpoint.get("schema_version")) is not int
        or checkpoint.get("schema_version") != schema_version
    ):
        raise ValueError(f"checkpoint must use the exact v{schema_version} shape")

    last_checked_at = checkpoint.get("last_checked_at")
    if last_checked_at is not None:
        if not isinstance(last_checked_at, str) or last_checked_at != last_checked_at.strip():
            raise ValueError("checkpoint has an invalid last_checked_at")
        try:
            _parse_timezone_aware_timestamp(last_checked_at, field_name="last_checked_at")
        except ValueError as exc:
            raise ValueError("checkpoint has an invalid last_checked_at") from exc

    last_error = checkpoint.get("last_error_fingerprint")
    if last_error is not None and (
        not isinstance(last_error, str)
        or not last_error.strip()
        or last_error != last_error.strip()
    ):
        raise ValueError("checkpoint has an invalid last_error_fingerprint")

    processed = _validate_meeting_id_list(
        checkpoint.get("processed_meeting_ids"),
        field_name="processed_meeting_ids",
        limit=200,
    )
    pending_meetings = _validate_meeting_id_map(
        checkpoint.get("pending_meetings"), field_name="pending_meetings", limit=100
    )
    needs_review = _validate_meeting_id_map(
        checkpoint.get("needs_review"), field_name="needs_review", limit=100
    )
    pending_actions = (
        validate_pending_user_actions(checkpoint.get("pending_user_actions"))
        if schema_version == 4
        else {}
    )
    bucket_sets = [
        set(processed),
        set(pending_meetings),
        set(pending_actions),
        set(needs_review),
    ]
    if any(
        left.intersection(right)
        for index, left in enumerate(bucket_sets)
        for right in bucket_sets[index + 1 :]
    ):
        raise ValueError("checkpoint meeting buckets must be mutually exclusive")
    return {
        **dict(checkpoint),
        "processed_meeting_ids": processed,
        "pending_meetings": pending_meetings,
        "needs_review": needs_review,
        **({"pending_user_actions": pending_actions} if schema_version == 4 else {}),
    }


def validate_delivery_checkpoint(checkpoint: Mapping[str, Any]) -> dict[str, Any]:
    """Validate the complete v4 checkpoint before exclusion, resume, or writes."""

    if not isinstance(checkpoint, Mapping):
        raise ValueError("checkpoint must be an object")
    return _validate_checkpoint_common(checkpoint, schema_version=4)


def migrate_delivery_state_v3_to_v4(
    delivery_preferences: Mapping[str, Any], checkpoint: Mapping[str, Any]
) -> dict[str, Any]:
    """Strictly migrate the immediately previous delivery contract once."""

    if not isinstance(delivery_preferences, Mapping) or set(delivery_preferences) != {
        "schema_version",
        "integrate_notes_into_linked_doc",
    }:
        raise ValueError("delivery_preferences must use the exact v3 shape")
    if (
        type(delivery_preferences.get("schema_version")) is not int
        or delivery_preferences.get("schema_version") != 3
    ):
        raise ValueError("delivery_preferences must use schema_version 3")
    enabled = delivery_preferences.get("integrate_notes_into_linked_doc")
    if not isinstance(enabled, bool):
        raise ValueError("integrate_notes_into_linked_doc must be a boolean")
    if not isinstance(checkpoint, Mapping):
        raise ValueError("checkpoint must be an object")
    v3_checkpoint = _validate_checkpoint_common(checkpoint, schema_version=3)
    v4_checkpoint = validate_delivery_checkpoint(
        {
            **v3_checkpoint,
            "schema_version": 4,
            "pending_user_actions": {},
        }
    )
    return {
        "delivery_preferences": {
            "schema_version": 4,
            "integrate_notes_into_linked_doc": enabled,
        },
        "checkpoint": v4_checkpoint,
    }


def resolve_calendar_event_candidate(
    candidates: Iterable[Mapping[str, Any]],
    *,
    meeting_url: str,
    meetings_url: str,
    calendar_event_id: str | None = None,
) -> dict[str, Any]:
    """Resolve one fetched Calendar occurrence using strict association tiers.

    meeting_url is the original call/Google Meet URL. meetings_url identifies
    the Meetings record represented in the result.
    """

    parsed_meetings_url = parse_meetings_url(meetings_url)
    deduped = dedupe_calendar_event_candidates(candidates)
    expected_event_id = str(calendar_event_id or "").strip()
    expected_meeting_url = str(meeting_url or "").strip()

    if expected_event_id:
        tiers = (
            (
                "exact_calendar_event_id",
                [
                    candidate
                    for candidate in deduped
                    if _calendar_event_id(candidate) == expected_event_id
                ],
            ),
        )
    else:
        tiers = (
            (
                "structured_hangout_link",
                [
                    candidate
                    for candidate in deduped
                    if expected_meeting_url
                    and _calendar_hangout_link(candidate) == expected_meeting_url
                ],
            ),
            (
                "description_meet_url",
                [
                    candidate
                    for candidate in deduped
                    if expected_meeting_url
                    and not _calendar_hangout_link(candidate)
                    and _contains_exact_https_url_token(
                        candidate.get("description"), expected_meeting_url
                    )
                ],
            ),
        )

    for match_method, matches in tiers:
        if not matches:
            continue
        if len(matches) > 1:
            return {
                "status": "calendar_event_ambiguous",
                "meeting_id": parsed_meetings_url.meeting_id,
                "calendar_event_id": None,
                "match_method": match_method,
                "candidate_count": len(matches),
            }
        selected = matches[0]
        selected_event_id = _calendar_event_id(selected)
        return {
            "status": "selected",
            "meeting_id": parsed_meetings_url.meeting_id,
            "calendar_event_id": selected_event_id,
            "match_method": match_method,
            "candidate_count": 1,
        }

    return {
        "status": "calendar_event_not_found",
        "meeting_id": parsed_meetings_url.meeting_id,
        "calendar_event_id": None,
        "match_method": None,
        "candidate_count": 0,
    }


def meeting_marker(meeting_id: str) -> str:
    """Return the shared cross-agent marker for one exact meeting id."""

    if not isinstance(meeting_id, str) or not _MEETING_ID_RE.fullmatch(meeting_id):
        raise ValueError("invalid Meetings meeting id")
    return f"meetings:{meeting_id}"


def render_provenance_footer(actor_name: str, meetings_url: str) -> str:
    """Render the visible provenance footer used by document append."""

    if not isinstance(actor_name, str) or not actor_name.strip():
        raise ValueError("actor_name must be a non-empty string")
    parsed = parse_meetings_url(meetings_url)
    marker = meeting_marker(parsed.meeting_id)
    return "\n".join(
        (
            f"Appended by {actor_name.strip()}'s Meetings agent",
            f"Meetings ID: {parsed.meeting_id}",
            f"View in Meetings: {parsed.meetings_url}",
            f"Meetings marker: {marker}",
        )
    )


def normalize_google_doc_links(links: Iterable[Any]) -> dict[str, Any]:
    """Validate, canonicalize, and deduplicate caller-supplied Google Doc links.

    This helper deliberately makes no semantic judgment about whether a
    document is meeting notes. The caller must supply the bounded links; this
    function only keeps safely shaped native Google Docs URLs.
    """

    if isinstance(links, (str, bytes)) or not isinstance(links, Iterable):
        raise ValueError("links must be an array")

    candidates: list[dict[str, str]] = []
    rejected: list[dict[str, Any]] = []
    seen_document_ids: set[str] = set()
    for index, raw_link in enumerate(links):
        if not isinstance(raw_link, str) or not raw_link.strip():
            rejected.append({"index": index, "reason": "invalid_link"})
            continue
        try:
            parsed = urlsplit(raw_link.strip())
            has_port = parsed.port is not None
        except ValueError:
            rejected.append({"index": index, "reason": "invalid_link"})
            continue
        if (
            parsed.scheme != "https"
            or parsed.netloc != "docs.google.com"
            or parsed.username is not None
            or parsed.password is not None
            or has_port
        ):
            rejected.append({"index": index, "reason": "unsupported_document_link"})
            continue
        match = _GOOGLE_DOC_PATH_RE.match(parsed.path)
        document_id = match.group(1) if match else ""
        if not document_id or not _GOOGLE_DOC_ID_RE.fullmatch(document_id):
            rejected.append({"index": index, "reason": "unsupported_document_link"})
            continue
        if document_id in seen_document_ids:
            rejected.append({"index": index, "reason": "duplicate_document_link"})
            continue
        seen_document_ids.add(document_id)
        candidates.append(
            {
                "document_id": document_id,
                "url": f"https://docs.google.com/document/d/{document_id}/edit",
            }
        )
    return {"candidates": candidates, "rejected": rejected}


def _json_dump(value: Any) -> None:
    json.dump(value, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")


def _main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    parse_parser = subparsers.add_parser("parse-url")
    parse_parser.add_argument("meetings_url")

    windows_parser = subparsers.add_parser("calendar-windows")
    windows_parser.add_argument("--recording-start-time", required=True)
    windows_parser.add_argument("--recording-end-time")

    resolve_event_parser = subparsers.add_parser("resolve-calendar-event")
    resolve_event_parser.add_argument("--candidates-json", required=True)
    resolve_event_parser.add_argument("--meeting-url", default="")
    resolve_event_parser.add_argument("--meetings-url", required=True)
    resolve_event_parser.add_argument("--calendar-event-id")

    prepare_event_parser = subparsers.add_parser("prepare-semantic-calendar-candidates")
    prepare_event_parser.add_argument("--candidates-json", required=True)
    prepare_event_parser.add_argument("--meeting-id", required=True)

    prepare_meeting_parser = subparsers.add_parser("prepare-semantic-meeting-context")
    prepare_meeting_parser.add_argument("--meeting-json", required=True)

    prepare_scope_parser = subparsers.add_parser("prepare-semantic-association-scope")
    prepare_scope_parser.add_argument("--meeting-json", required=True)
    prepare_scope_parser.add_argument("--candidate-json", required=True)

    validate_selection_parser = subparsers.add_parser("validate-calendar-selection")
    validate_selection_parser.add_argument("--result-json", required=True)
    validate_selection_parser.add_argument("--candidate-event-ids-json", required=True)

    validate_checkpoint_parser = subparsers.add_parser("validate-delivery-checkpoint")
    validate_checkpoint_parser.add_argument("--checkpoint-json", required=True)

    migrate_v3_parser = subparsers.add_parser("migrate-v3-delivery-state")
    migrate_v3_parser.add_argument("--delivery-preferences-json", required=True)
    migrate_v3_parser.add_argument("--checkpoint-json", required=True)

    scope_hash_parser = subparsers.add_parser("scope-sha256")
    scope_hash_parser.add_argument("--scope-json", required=True)

    recipient_hash_parser = subparsers.add_parser("recipient-set-sha256")
    recipient_hash_parser.add_argument("--recipient-emails-json", required=True)
    recipient_hash_parser.add_argument("--attendees-omitted-json", required=True)

    internal_recipients_parser = subparsers.add_parser("prepare-internal-share-recipients")
    internal_recipients_parser.add_argument("--calendar-event-json", required=True)

    associated_id_parser = subparsers.add_parser("calendar-description-has-meeting-id")
    associated_id_parser.add_argument("--description-json", required=True)
    associated_id_parser.add_argument("--meeting-id", required=True)

    legacy_associated_parser = subparsers.add_parser("calendar-description-has-meetings-url")
    legacy_associated_parser.add_argument("--description-json", required=True)
    legacy_associated_parser.add_argument("--meetings-url", required=True)

    normalize_links_parser = subparsers.add_parser("normalize-document-links")
    normalize_links_parser.add_argument("--links-json", required=True)

    footer_parser = subparsers.add_parser("render-footer")
    footer_parser.add_argument("--meetings-url", required=True)
    footer_parser.add_argument("--actor-name", required=True)

    args = parser.parse_args(argv)
    try:
        if args.command == "parse-url":
            _json_dump(asdict(parse_meetings_url(args.meetings_url)))
        elif args.command == "calendar-windows":
            _json_dump(
                {
                    "windows": calendar_candidate_windows(
                        args.recording_start_time, args.recording_end_time
                    )
                }
            )
        elif args.command == "resolve-calendar-event":
            candidates = json.loads(args.candidates_json)
            if not isinstance(candidates, list):
                raise ValueError("candidates-json must be a JSON array")
            _json_dump(
                resolve_calendar_event_candidate(
                    candidates,
                    meeting_url=args.meeting_url,
                    meetings_url=args.meetings_url,
                    calendar_event_id=args.calendar_event_id,
                )
            )
        elif args.command == "prepare-semantic-calendar-candidates":
            candidates = json.loads(args.candidates_json)
            if not isinstance(candidates, list):
                raise ValueError("candidates-json must be a JSON array")
            _json_dump(
                prepare_semantic_calendar_candidates(
                    candidates,
                    meeting_id=args.meeting_id,
                )
            )
        elif args.command == "prepare-semantic-meeting-context":
            meeting = json.loads(args.meeting_json)
            if not isinstance(meeting, dict):
                raise ValueError("meeting-json must be a JSON object")
            _json_dump(prepare_semantic_meeting_context(meeting))
        elif args.command == "prepare-semantic-association-scope":
            meeting = json.loads(args.meeting_json)
            candidate = json.loads(args.candidate_json)
            if not isinstance(meeting, dict) or not isinstance(candidate, dict):
                raise ValueError("meeting-json and candidate-json must be JSON objects")
            _json_dump(prepare_semantic_association_scope(meeting, candidate))
        elif args.command == "validate-calendar-selection":
            result = json.loads(args.result_json)
            candidate_event_ids = json.loads(args.candidate_event_ids_json)
            if not isinstance(result, dict):
                raise ValueError("result-json must be a JSON object")
            if not isinstance(candidate_event_ids, list):
                raise ValueError("candidate-event-ids-json must be a JSON array")
            _json_dump(
                validate_calendar_selector_result(result, candidate_event_ids=candidate_event_ids)
            )
        elif args.command == "validate-delivery-checkpoint":
            checkpoint = json.loads(args.checkpoint_json)
            if not isinstance(checkpoint, dict):
                raise ValueError("checkpoint-json must be a JSON object")
            _json_dump(validate_delivery_checkpoint(checkpoint))
        elif args.command == "migrate-v3-delivery-state":
            delivery_preferences = json.loads(args.delivery_preferences_json)
            checkpoint = json.loads(args.checkpoint_json)
            if not isinstance(delivery_preferences, dict) or not isinstance(checkpoint, dict):
                raise ValueError(
                    "delivery-preferences-json and checkpoint-json must be JSON objects"
                )
            _json_dump(migrate_delivery_state_v3_to_v4(delivery_preferences, checkpoint))
        elif args.command == "scope-sha256":
            scope = json.loads(args.scope_json)
            _json_dump({"sha256": canonical_scope_sha256(scope)})
        elif args.command == "recipient-set-sha256":
            recipient_emails = json.loads(args.recipient_emails_json)
            attendees_omitted = json.loads(args.attendees_omitted_json)
            if not isinstance(recipient_emails, list):
                raise ValueError("recipient-emails-json must be a JSON array")
            _json_dump(
                canonical_recipient_set_sha256(
                    recipient_emails, attendees_omitted=attendees_omitted
                )
            )
        elif args.command == "prepare-internal-share-recipients":
            calendar_event = json.loads(args.calendar_event_json)
            if not isinstance(calendar_event, dict):
                raise ValueError("calendar-event-json must be a JSON object")
            _json_dump(prepare_internal_share_recipients(calendar_event))
        elif args.command == "calendar-description-has-meeting-id":
            description = json.loads(args.description_json)
            _json_dump(
                {
                    "already_associated": calendar_description_has_meeting_id(
                        description,
                        args.meeting_id,
                    )
                }
            )
        elif args.command == "calendar-description-has-meetings-url":
            description = json.loads(args.description_json)
            _json_dump(
                {
                    "already_associated": calendar_description_has_canonical_meetings_url(
                        description,
                        args.meetings_url,
                    )
                }
            )
        elif args.command == "normalize-document-links":
            links = json.loads(args.links_json)
            if not isinstance(links, list):
                raise ValueError("links-json must be a JSON array")
            _json_dump(normalize_google_doc_links(links))
        elif args.command == "render-footer":
            parsed = parse_meetings_url(args.meetings_url)
            _json_dump(
                {
                    "meeting_id": parsed.meeting_id,
                    "marker": meeting_marker(parsed.meeting_id),
                    "footer": render_provenance_footer(args.actor_name, args.meetings_url),
                }
            )
    except UntrustworthyRecordingTiming:
        _json_dump(
            {
                "status": "not_applicable",
                "reason": "missing_or_invalid_recording_timing",
            }
        )
        return 0
    except InvalidMeetingsUrl as exc:
        _json_dump({"status": "invalid_meetings_url", "reason": str(exc)})
        return 2
    except (ValueError, json.JSONDecodeError) as exc:
        _json_dump({"status": "invalid_input", "reason": str(exc)})
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
