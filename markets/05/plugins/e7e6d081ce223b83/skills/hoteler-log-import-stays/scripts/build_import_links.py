#!/usr/bin/env python3
"""Build privacy-minimized Hoteler Log v1 import links requested by the user.

Input is read from stdin unless --input is supplied. The script performs no
network requests and emits no input data on validation failures.
"""

from __future__ import annotations

import argparse
import base64
import json
import re
import sys
import unicodedata
import uuid
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP, localcontext
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable, Sequence


BASE_URL = "https://hoteler-log.pages.dev/import"
MAX_STAYS = 20
MAX_PAYLOAD_BYTES = 16 * 1_024
MAX_HOTEL_NAME_LENGTH = 100
MAX_BOOKING_CHANNEL_LENGTH = 50
MAX_NOTES_LENGTH = 500
MAX_PRICE_LENGTH = 20
MAX_RATE_LENGTH = 40
MAX_POINTS_USED = 1_000_000_000
MAX_STAY_NIGHTS = 365
EARLIEST_STAY_DATE = date(1900, 1, 1)
FUTURE_YEARS = 5
KNOWN_HOTEL_NAMES_PATH = Path(__file__).resolve().parents[1] / "assets" / "known-hotel-names.json"

KNOWN_BOOKING_CHANNELS = frozenset(
    {
        "公式サイト",
        "ポイント予約",
        "一休.com",
        "楽天トラベル",
        "じゃらん",
        "JTB",
        "Yahoo!トラベル",
        "Relux",
        "Agoda",
        "Booking.com",
        "Expedia",
        "Trip.com",
        "Hotels.com",
        "Amex FHR",
        "Amex THR",
        "Hotelux",
        "Tablet Hotels",
        "Mr & Mrs Smith",
        "Virtuoso",
        "Visa Luxury Hotel Collection",
    }
)
SAFE_NOTE_TAGS = frozenset(
    {
        "朝食付き",
        "夕食付き",
        "朝夕食付き",
        "素泊まり",
        "返金不可",
        "現地払い",
        "事前決済",
        "駐車場付き",
        "クラブラウンジ利用",
        "アーリーチェックイン",
        "レイトチェックアウト",
    }
)
GENERIC_HOTEL_NAMES = frozenset(
    {
        "hotel",
        "inn",
        "lodging",
        "resort",
        "unknown",
        "ホテル",
        "旅館",
        "宿",
        "宿泊施設",
        "不明",
        "未定",
    }
)

ROOT_FIELDS = frozenset({"linkCreationRequested", "stays"})
STAY_FIELDS = frozenset(
    {
        "hotelName",
        "unlistedHotelNameConfirmed",
        "checkIn",
        "checkOut",
        "bookingChannel",
        "priceAmount",
        "priceCurrency",
        "exchangeRate",
        "pointsUsed",
        "notes",
    }
)

DATE_PATTERN = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", re.ASCII)
DECIMAL_PATTERN = re.compile(r"^[0-9]+(?:\.[0-9]+)?$", re.ASCII)
CURRENCY_PATTERN = re.compile(r"^[A-Z]{3}$", re.ASCII)
SUPPORTED_ECB_SOURCE_CURRENCIES = frozenset(
    {
        "USD",
        "EUR",
        "GBP",
        "CNY",
        "KRW",
        "THB",
        "SGD",
        "AUD",
        "CAD",
        "CHF",
        "HKD",
    }
)
EXCHANGE_RATE_FIELDS = frozenset(
    {
        "provider",
        "rateDate",
        "sourceUnitsPerEUR",
        "jpyPerEUR",
    }
)
EMAIL_PATTERN = re.compile(r"(?<![\w.+-])[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}(?![\w.-])")
PHONE_PATTERN = re.compile(r"(?<!\d)(?:\+?\d[\s().-]*){10,15}(?!\d)")
LONG_NUMBER_PATTERN = re.compile(r"(?<!\d)(?:\d[ -]?){13,19}(?!\d)")
SENSITIVE_LABEL_PATTERN = re.compile(
    r"(?:"
    r"(?:氏名|姓名|お名前|宿泊者名|予約者|メール(?:アドレス)?|電話(?:番号)?|住所|"
    r"予約番号|確認番号|照会番号|暗証番号|会員番号|カード(?:番号)?|旅券|パスポート)|"
    r"(?<![A-Za-z0-9])(?:guest[\s_-]*name|e[\s_-]*mail|"
    r"phone(?:[\s_-]*(?:no\.?|number))?|telephone(?:[\s_-]*(?:no\.?|number))?|"
    r"postal[\s_-]*address|street[\s_-]*address|"
    r"(?:reservation|confirmation|booking|itinerary)[\s_-]*(?:id|no\.?|number|reference|code)|"
    r"pin(?:[\s_-]*(?:code|number))?|member(?:ship)?[\s_-]*(?:id|no\.?|number)|"
    r"card[\s_-]*(?:id|no\.?|number)|passport(?:[\s_-]*(?:id|no\.?|number))?"
    r")(?![A-Za-z0-9])"
    r")\s*[:：=]\s*\S",
    re.IGNORECASE,
)
LABELED_IDENTIFIER_PATTERN = re.compile(
    r"(?:"
    r"(?:予約番号|確認番号|照会番号|暗証番号|会員番号|カード番号)|"
    r"(?<![A-Za-z0-9])(?:"
    r"(?:reservation|confirmation|booking|itinerary)[\s_-]*(?:id|no\.?|number|reference|code)|"
    r"pin(?:[\s_-]*(?:code|number))?|member(?:ship)?[\s_-]*(?:id|no\.?|number)|"
    r"card[\s_-]*(?:id|no\.?|number)|passport[\s_-]*(?:id|no\.?|number)"
    r")(?![A-Za-z0-9])"
    r")\s+(?=[A-Za-z0-9_-]{4,}\b)(?=[A-Za-z0-9_-]*[0-9])[A-Za-z0-9_-]+",
    re.IGNORECASE,
)
COLONLESS_SENSITIVE_LABEL_PATTERN = re.compile(
    r"(?:"
    r"(?:氏名|姓名|お名前|宿泊者名|予約者|住所)\s+\S+|"
    r"(?<![A-Za-z0-9])(?:"
    r"guest[_-]name|e[_-]mail|postal[_-]address|street[_-]address|"
    r"phone[_-](?:no\.?|number)|telephone[_-](?:no\.?|number)|"
    r"(?:reservation|confirmation|booking|itinerary)[_-](?:id|no\.?|number|reference|code)|"
    r"pin[_-](?:code|number)|member(?:ship)?[_-](?:id|no\.?|number)|"
    r"card[_-](?:id|no\.?|number)|passport[_-](?:id|no\.?|number)"
    r")(?![A-Za-z0-9])\s+\S+|"
    r"(?<![A-Za-z0-9])(?:"
    r"guest\s+name|postal\s+address|street\s+address|"
    r"phone\s+(?:no\.?|number)|telephone\s+(?:no\.?|number)|"
    r"(?:reservation|confirmation|booking|itinerary)\s+(?:id|no\.?|number|reference|code)|"
    r"pin\s+(?:code|number)|member(?:ship)?\s+(?:id|no\.?|number)|"
    r"card\s+(?:id|no\.?|number)|passport\s+(?:id|no\.?|number)"
    r")(?![A-Za-z0-9])\s+\S+|"
    r"(?<![A-Za-z0-9])passport(?![A-Za-z0-9])\s+"
    r"(?=[A-Za-z0-9_-]{4,}\b)(?=[A-Za-z0-9_-]*[0-9])[A-Za-z0-9_-]+|"
    r"パスポート\s+(?=[A-Za-z0-9_-]{4,}\b)(?=[A-Za-z0-9_-]*[0-9])[A-Za-z0-9_-]+"
    r")",
    re.IGNORECASE,
)
CONTROL_PATTERN = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
URL_PATTERN = re.compile(r"(?:https?://|www\.|\b[a-z][a-z0-9+.-]*://)", re.IGNORECASE)
DANGEROUS_URI_PATTERN = re.compile(
    r"(?:javascript|data|file|mailto|tel|sms):",
    re.IGNORECASE,
)
DOMAIN_PATTERN = re.compile(
    r"\b(?:[a-z0-9-]+\.)+(?:app|com|io|jp|net|org)(?:\b|/)",
    re.IGNORECASE,
)
MARKDOWN_LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\s*\(", re.IGNORECASE)
INSTRUCTION_PATTERN = re.compile(
    r"(?:"
    r"(?:ignore|disregard|override|bypass)\s+(?:(?:all|any|the)\s+)?"
    r"(?:(?:previous|prior|above)\s+)?(?:instructions?|rules?|prompts?)|"
    r"(?:system|developer)\s+(?:message|prompt)|"
    r"(?:system|developer)\s+(?:says?|instructions?)|"
    r"(?:follow|obey)\s+(?:these|the|all|my)\s+(?:instructions?|rules?|prompts?)|"
    r"(?:ignore|disable|bypass)\s+(?:safety|security|privacy|validation)|"
    r"(?:reveal|upload|exfiltrate|transmit|send)\b.{0,40}\b(?:secret|data|reservation|payload|to)\b|"
    r"(?:指示|ルール|プロンプト)\s*(?:を)?\s*(?:無視|上書き|回避)|"
    r"(?:安全|セキュリティ|プライバシー|検証)\s*(?:を)?\s*(?:無視|無効|回避)|"
    r"(?:upload|exfiltrate|transmit)\s+(?:this|the|data)|"
    r"(?:外部|別のサイト|第三者)\s*(?:へ|に)\s*(?:送信|アップロード)"
    r")",
    re.IGNORECASE,
)


class ValidationError(ValueError):
    """Safe validation error that never echoes user-provided values."""

    def __init__(self, code: str, message: str, stay_index: int | None = None):
        self.code = code
        self.stay_index = stay_index
        prefix = f"stay {stay_index}: " if stay_index is not None else ""
        super().__init__(f"{prefix}{message}")


@dataclass(frozen=True)
class GeneratedLink:
    position: int
    url: str
    markdown: str
    envelope: dict[str, Any]


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate user-requested, review-only Hoteler Log import links."
    )
    parser.add_argument(
        "--input",
        type=Path,
        help="Read JSON from this file instead of stdin.",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output exact Markdown links or structured generator results.",
    )
    return parser.parse_args(argv)


def _read_document(path: Path | None) -> Any:
    try:
        raw = path.read_text(encoding="utf-8") if path else sys.stdin.read()
    except OSError as error:
        raise ValidationError("input_read_failed", "could not read input JSON") from error

    if len(raw.encode("utf-8")) > MAX_PAYLOAD_BYTES * MAX_STAYS:
        raise ValidationError("input_too_large", "input document is too large")

    try:
        return json.loads(raw)
    except (json.JSONDecodeError, UnicodeError) as error:
        raise ValidationError("invalid_json", "input must be valid UTF-8 JSON") from error


def _require_exact_fields(
    value: Any,
    allowed: frozenset[str],
    *,
    code: str,
    stay_index: int | None = None,
) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValidationError(code, "value must be a JSON object", stay_index)
    if not all(isinstance(key, str) for key in value):
        raise ValidationError(code, "field names must be strings", stay_index)
    if not set(value).issubset(allowed):
        raise ValidationError(code, "unsupported field is present", stay_index)
    return value


def _required_text(
    value: Any,
    *,
    code: str,
    maximum: int,
    stay_index: int,
) -> str:
    if not isinstance(value, str):
        raise ValidationError(code, "required text field is missing or invalid", stay_index)
    normalized = value.strip()
    if not normalized or len(normalized) > maximum:
        raise ValidationError(code, "required text field is empty or too long", stay_index)
    _reject_sensitive_text(normalized, stay_index)
    return normalized


def _optional_text(
    value: Any,
    *,
    code: str,
    maximum: int,
    stay_index: int,
) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValidationError(code, "optional text field has an invalid type", stay_index)
    normalized = value.strip()
    if not normalized:
        return None
    if len(normalized) > maximum:
        raise ValidationError(code, "optional text field is too long", stay_index)
    _reject_sensitive_text(normalized, stay_index)
    return normalized


def _reject_sensitive_text(value: str, stay_index: int) -> None:
    if CONTROL_PATTERN.search(value):
        raise ValidationError("unsafe_text", "text contains unsupported control characters", stay_index)
    security_form = unicodedata.normalize("NFKC", value)
    if (
        EMAIL_PATTERN.search(security_form)
        or PHONE_PATTERN.search(security_form)
        or LONG_NUMBER_PATTERN.search(security_form)
        or SENSITIVE_LABEL_PATTERN.search(security_form)
        or LABELED_IDENTIFIER_PATTERN.search(security_form)
        or COLONLESS_SENSITIVE_LABEL_PATTERN.search(security_form)
    ):
        raise ValidationError(
            "sensitive_text",
            "text appears to contain personal or secret data; remove it before retrying",
            stay_index,
        )


@lru_cache(maxsize=1)
def _known_hotel_names() -> frozenset[str]:
    try:
        decoded = json.loads(KNOWN_HOTEL_NAMES_PATH.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise ValidationError(
            "hotel_catalog_unavailable",
            "bundled hotel-name catalog could not be validated",
        ) from error
    if not isinstance(decoded, list) or not decoded or not all(
        isinstance(value, str) and value for value in decoded
    ):
        raise ValidationError(
            "hotel_catalog_unavailable",
            "bundled hotel-name catalog has an invalid shape",
        )
    return frozenset(decoded)


def _normalize_hotel_name(
    value: Any,
    *,
    unlisted_confirmed: Any,
    stay_index: int,
) -> str:
    normalized = unicodedata.normalize(
        "NFC",
        _required_text(
            value,
            code="invalid_hotel_name",
            maximum=MAX_HOTEL_NAME_LENGTH,
            stay_index=stay_index,
        ),
    )
    security_form = unicodedata.normalize("NFKC", normalized)
    if any(unicodedata.category(character).startswith("C") for character in normalized):
        raise ValidationError(
            "unsafe_hotel_name",
            "hotelName contains unsupported invisible or control characters",
            stay_index,
        )
    if (
        URL_PATTERN.search(security_form)
        or DANGEROUS_URI_PATTERN.search(security_form)
        or DOMAIN_PATTERN.search(security_form)
        or MARKDOWN_LINK_PATTERN.search(security_form)
        or INSTRUCTION_PATTERN.search(security_form)
    ):
        raise ValidationError(
            "unsafe_hotel_name",
            "hotelName appears to contain a URL or instruction rather than a lodging name",
            stay_index,
        )
    if security_form.casefold() in GENERIC_HOTEL_NAMES:
        raise ValidationError(
            "invalid_hotel_name",
            "hotelName must identify a specific lodging property",
            stay_index,
        )
    if unlisted_confirmed is not None and not isinstance(unlisted_confirmed, bool):
        raise ValidationError(
            "invalid_hotel_name_confirmation",
            "unlistedHotelNameConfirmed must be a boolean",
            stay_index,
        )
    if normalized in _known_hotel_names():
        return normalized
    if unlisted_confirmed is not True:
        raise ValidationError(
            "unconfirmed_unlisted_hotel_name",
            "an unlisted hotelName must be shown and explicitly confirmed by the user",
            stay_index,
        )
    return normalized


def _parse_local_date(value: Any, code: str, stay_index: int) -> date:
    if not isinstance(value, str) or not DATE_PATTERN.fullmatch(value):
        raise ValidationError(code, "date must use exact YYYY-MM-DD format", stay_index)
    try:
        parsed = date.fromisoformat(value)
    except ValueError as error:
        raise ValidationError(code, "date is not a real calendar date", stay_index) from error
    if parsed.isoformat() != value:
        raise ValidationError(code, "date must use exact YYYY-MM-DD format", stay_index)
    return parsed


def _add_years(value: date, years: int) -> date:
    try:
        return value.replace(year=value.year + years)
    except ValueError:
        # Match calendar-style year arithmetic for February 29.
        return value.replace(year=value.year + years, day=28)


def _normalize_decimal_string(
    value: Any,
    *,
    code: str,
    maximum: int,
    positive: bool,
    stay_index: int,
) -> tuple[str, Decimal]:
    if (
        not isinstance(value, str)
        or not value
        or len(value) > maximum
        or not DECIMAL_PATTERN.fullmatch(value)
    ):
        raise ValidationError(code, "value must be a plain decimal string", stay_index)
    try:
        parsed = Decimal(value)
    except InvalidOperation as error:
        raise ValidationError(code, "value must be a valid decimal", stay_index) from error
    if not parsed.is_finite() or (parsed <= 0 if positive else parsed < 0):
        comparison = "greater than zero" if positive else "zero or greater"
        raise ValidationError(code, f"value must be {comparison}", stay_index)
    return value, parsed


def _normalize_currency(value: Any, *, stay_index: int) -> str:
    if not isinstance(value, str) or not CURRENCY_PATTERN.fullmatch(value):
        raise ValidationError(
            "invalid_currency",
            "priceCurrency must be exactly three uppercase ASCII letters",
            stay_index,
        )
    return value


def _normalize_exchange_rate(
    value: Any,
    *,
    source_currency: str,
    check_in: date,
    today: date,
    stay_index: int,
) -> tuple[Decimal, Decimal]:
    if value is None:
        raise ValidationError(
            "missing_exchange_rate",
            "foreign price requires verified ECB exchange-rate evidence",
            stay_index,
        )
    evidence = _require_exact_fields(
        value,
        EXCHANGE_RATE_FIELDS,
        code="invalid_exchange_rate",
        stay_index=stay_index,
    )
    if set(evidence) != EXCHANGE_RATE_FIELDS:
        raise ValidationError(
            "invalid_exchange_rate",
            "exchange-rate evidence must contain all four required fields",
            stay_index,
        )
    if evidence.get("provider") != "ECB":
        raise ValidationError(
            "unsupported_exchange_rate_provider",
            "exchange-rate provider must be ECB",
            stay_index,
        )

    rate_date = _parse_local_date(
        evidence.get("rateDate"),
        "invalid_exchange_rate_date",
        stay_index,
    )
    if rate_date > today:
        raise ValidationError(
            "exchange_rate_in_future",
            "exchange-rate date cannot be after the generator date",
            stay_index,
        )
    if check_in > today:
        raise ValidationError(
            "future_foreign_stay",
            "foreign prices for future stays must be omitted",
            stay_index,
        )
    if rate_date > check_in:
        raise ValidationError(
            "exchange_rate_after_check_in",
            "exchange-rate date cannot be after checkIn",
            stay_index,
        )
    if (check_in - rate_date).days > 10:
        raise ValidationError(
            "stale_exchange_rate",
            "exchange-rate date must be within ten calendar days before checkIn",
            stay_index,
        )

    _, source_units_per_eur = _normalize_decimal_string(
        evidence.get("sourceUnitsPerEUR"),
        code="invalid_exchange_rate_value",
        maximum=MAX_RATE_LENGTH,
        positive=True,
        stay_index=stay_index,
    )
    _, jpy_per_eur = _normalize_decimal_string(
        evidence.get("jpyPerEUR"),
        code="invalid_exchange_rate_value",
        maximum=MAX_RATE_LENGTH,
        positive=True,
        stay_index=stay_index,
    )
    if source_currency == "EUR" and source_units_per_eur != Decimal("1"):
        raise ValidationError(
            "invalid_eur_exchange_rate",
            "EUR sourceUnitsPerEUR must equal one",
            stay_index,
        )
    return source_units_per_eur, jpy_per_eur


def _normalize_money(
    item: dict[str, Any],
    *,
    check_in: date,
    today: date,
    stay_index: int,
) -> tuple[str | None, str | None]:
    raw_price = item.get("priceAmount")
    raw_currency = item.get("priceCurrency")
    raw_exchange_rate = item.get("exchangeRate")

    if raw_price is None and raw_currency is None:
        if raw_exchange_rate is not None:
            raise ValidationError(
                "unexpected_exchange_rate",
                "exchange-rate evidence requires a foreign price",
                stay_index,
            )
        return None, None
    if raw_price is None or raw_currency is None:
        raise ValidationError(
            "invalid_price_pair",
            "priceAmount and priceCurrency must both be supplied or both be omitted",
            stay_index,
        )

    exact_price, amount = _normalize_decimal_string(
        raw_price,
        code="invalid_price",
        maximum=MAX_PRICE_LENGTH,
        positive=False,
        stay_index=stay_index,
    )
    currency = _normalize_currency(raw_currency, stay_index=stay_index)
    if currency == "JPY":
        if raw_exchange_rate is not None:
            raise ValidationError(
                "unexpected_exchange_rate",
                "JPY price must not include exchange-rate evidence",
                stay_index,
            )
        return exact_price, "JPY"
    if currency not in SUPPORTED_ECB_SOURCE_CURRENCIES:
        raise ValidationError(
            "unsupported_exchange_rate_currency",
            "source currency is not supported by the verified ECB conversion path",
            stay_index,
        )

    source_units_per_eur, jpy_per_eur = _normalize_exchange_rate(
        raw_exchange_rate,
        source_currency=currency,
        check_in=check_in,
        today=today,
        stay_index=stay_index,
    )
    with localcontext() as context:
        context.prec = 200
        converted = (amount * jpy_per_eur / source_units_per_eur).quantize(
            Decimal("1"),
            rounding=ROUND_HALF_UP,
        )
    converted_string = format(converted, "f")
    if len(converted_string) > MAX_PRICE_LENGTH:
        raise ValidationError(
            "converted_price_out_of_range",
            "converted JPY price exceeds the supported length",
            stay_index,
        )
    return converted_string, "JPY"


def _normalize_points(value: Any, stay_index: int) -> int | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValidationError("invalid_points", "pointsUsed must be an integer", stay_index)
    if not 0 <= value <= MAX_POINTS_USED:
        raise ValidationError("invalid_points", "pointsUsed is outside the supported range", stay_index)
    return value


def _normalize_booking_channel(value: Any, stay_index: int) -> str | None:
    normalized = _optional_text(
        value,
        code="invalid_booking_channel",
        maximum=MAX_BOOKING_CHANNEL_LENGTH,
        stay_index=stay_index,
    )
    if normalized is None:
        return None
    if normalized not in KNOWN_BOOKING_CHANNELS:
        raise ValidationError(
            "unknown_booking_channel",
            "unknown bookingChannel must be omitted and selected in the app",
            stay_index,
        )
    return normalized


def _normalize_notes(value: Any, stay_index: int) -> str | None:
    normalized = _optional_text(
        value,
        code="invalid_notes",
        maximum=MAX_NOTES_LENGTH,
        stay_index=stay_index,
    )
    if normalized is None:
        return None
    if normalized not in SAFE_NOTE_TAGS:
        raise ValidationError(
            "unsafe_notes",
            "notes must be one predefined non-sensitive tag or omitted",
            stay_index,
        )
    return normalized


def _normalize_stay(raw: Any, *, stay_index: int, today: date) -> dict[str, Any]:
    item = _require_exact_fields(
        raw,
        STAY_FIELDS,
        code="invalid_stay",
        stay_index=stay_index,
    )

    hotel_name = _normalize_hotel_name(
        item.get("hotelName"),
        unlisted_confirmed=item.get("unlistedHotelNameConfirmed"),
        stay_index=stay_index,
    )
    check_in = _parse_local_date(item.get("checkIn"), "invalid_check_in", stay_index)
    check_out = _parse_local_date(item.get("checkOut"), "invalid_check_out", stay_index)
    if check_out <= check_in:
        raise ValidationError("invalid_date_range", "checkOut must be later than checkIn", stay_index)
    if (check_out - check_in).days > MAX_STAY_NIGHTS:
        raise ValidationError("stay_too_long", "stay exceeds 365 nights", stay_index)
    if check_in < EARLIEST_STAY_DATE or check_out > _add_years(today, FUTURE_YEARS):
        raise ValidationError("date_out_of_range", "dates are outside the app's supported range", stay_index)

    price, currency = _normalize_money(
        item,
        check_in=check_in,
        today=today,
        stay_index=stay_index,
    )

    return {
        "hotelName": hotel_name,
        "checkIn": check_in.isoformat(),
        "checkOut": check_out.isoformat(),
        "bookingChannel": _normalize_booking_channel(item.get("bookingChannel"), stay_index),
        "priceAmount": price,
        "priceCurrency": currency,
        "pointsUsed": _normalize_points(item.get("pointsUsed"), stay_index),
        "notes": _normalize_notes(item.get("notes"), stay_index),
    }


def _encode_envelope(envelope: dict[str, Any]) -> str:
    data = json.dumps(
        envelope,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    if len(data) > MAX_PAYLOAD_BYTES:
        raise ValidationError("payload_too_large", "generated payload exceeds 16 KiB")
    return base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")


def build_links(
    document: Any,
    *,
    now: datetime | None = None,
    today: date | None = None,
    uuid_factory: Callable[[], uuid.UUID] = uuid.uuid4,
) -> list[GeneratedLink]:
    root = _require_exact_fields(document, ROOT_FIELDS, code="invalid_document")
    if root.get("linkCreationRequested") is not True:
        raise ValidationError(
            "link_creation_request_required",
            "linkCreationRequested must be true after the user requests Hoteler Log link creation",
        )

    stays = root.get("stays")
    if not isinstance(stays, list) or isinstance(stays, (str, bytes)):
        raise ValidationError("invalid_stays", "stays must be an array")
    if not 1 <= len(stays) <= MAX_STAYS:
        raise ValidationError("invalid_stay_count", "stays must contain between 1 and 20 items")

    instant = now or datetime.now(timezone.utc)
    if instant.tzinfo is None or instant.utcoffset() is None:
        raise ValueError("now must be timezone-aware")
    instant = instant.astimezone(timezone.utc).replace(microsecond=0)
    local_today = today or date.today()
    expires_at = (instant + timedelta(hours=24)).isoformat().replace("+00:00", "Z")

    results: list[GeneratedLink] = []
    for position, raw_stay in enumerate(stays, start=1):
        stay = _normalize_stay(raw_stay, stay_index=position, today=local_today)
        envelope = {
            "version": 1,
            "importId": str(uuid_factory()),
            "expiresAt": expires_at,
            "source": "chatgpt",
            "stay": stay,
        }
        payload = _encode_envelope(envelope)
        url = f"{BASE_URL}#payload={payload}"
        label = "Hoteler Logで確認して登録"
        if len(stays) > 1:
            label += f"（{position}/{len(stays)}）"
        results.append(
            GeneratedLink(
                position=position,
                url=url,
                markdown=f"[{label}]({url})",
                envelope=envelope,
            )
        )
    return results


def _render(results: Sequence[GeneratedLink], output_format: str) -> str:
    if output_format == "markdown":
        return "\n".join(result.markdown for result in results)
    return json.dumps(
        {
            "count": len(results),
            "links": [
                {
                    "position": result.position,
                    "url": result.url,
                    "markdown": result.markdown,
                    "envelope": result.envelope,
                }
                for result in results
            ],
        },
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    try:
        document = _read_document(args.input)
        results = build_links(document)
    except ValidationError as error:
        print(f"error[{error.code}]: {error}", file=sys.stderr)
        return 2

    print(_render(results, args.format))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
